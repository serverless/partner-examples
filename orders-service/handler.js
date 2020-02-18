/**
 * Form Submit
 */

const https = require('https');
var AWS = require('aws-sdk');
AWS.config.update({region:'us-east-1'});

var sns = new AWS.SNS();
var dynamodb = new AWS.DynamoDB();

const submit = async (event, context) => {
  context.serverlessSdk.tagEvent('customerId', 5, { newCustomer: true, isDemo: true, demoExpire: '2019-12-01' })
  if (event['queryStringParameters'] && event['queryStringParameters']['error']) {
    let r = Math.random().toString(36).substring(7);
    throw new Error(`Random error ${r}`)
  }
  
  // Create and delete an SNS Topic
  try {
    var createParams = {
      Name: "slspartnertopic1"
    }
    var createResult = await sns.createTopic(createParams).promise()
    console.log(createResult)
    var deleteParams = {
      TopicArn: createResult["TopicArn"]
    }
    var deleteResult = await sns.deleteTopic(deleteParams).promise()
    console.log(deleteResult)
  } catch (e) {
    console.log(e, e.stack)
  }

  // Make HTTP request
  await new Promise((resolve, reject) => {
    const req = https.get({ host: 'www.nokeynoshade.party', path: '/api/queens/89/', method: 'get' }, resp => {
      let data = '';
      resp.on('data', chunk => {
        data += chunk;
      });
      resp.on('end', () => {
        resolve(data);
      });
    });
    req.on('error', reject);
  });

  // Send items to DynamoDB
  try {
    const dynamoParams = {
      Item: {
        "email": { S: "fernando@serverless.com" }, 
      }, 
      ReturnConsumedCapacity: "TOTAL", 
      TableName: "orders-table"
    };
    const putData = await dynamodb.putItem(dynamoParams).promise()
    console.log('Put the item in DynamoDB')
  } catch (e) {
    console.log(e, e.stack)
  }

  const response = {
    statusCode: 200,
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Credentials': true,
    },
    body: JSON.stringify({ message: 'form submission received' }),
  }

  return response
}

module.exports = { submit }
