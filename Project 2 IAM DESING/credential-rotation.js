require('dotenv').config();

const https = require('https');

const domain = process.env.AUTH0_DOMAIN;
const clientId = process.env.M2M_CLIENT_ID;
const clientSecret = process.env.M2M_CLIENT_SECRET;
const audience = process.env.AUTH0_AUDIENCE;

function requestToken(label) {
  return new Promise((resolve) => {
    const data = new URLSearchParams({
      grant_type: 'client_credentials',
      client_id: clientId,
      client_secret: clientSecret,
      audience: audience
    }).toString();

    const options = {
      hostname: domain,
      path: '/oauth/token',
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': Buffer.byteLength(data)
      }
    };

    const req = https.request(options, (res) => {
      let body = '';

      res.on('data', (chunk) => {
        body += chunk;
      });

      res.on('end', () => {
        const timestamp = new Date().toISOString();

        console.log(
          `[${timestamp}] ${label}: ${res.statusCode} ${res.statusMessage}`
        );

        resolve(res.statusCode);
      });
    });

    req.on('error', (error) => {
      console.error(error.message);
      resolve(0);
    });

    req.write(data);
    req.end();
  });
}

async function main() {
  await requestToken('Credential test');
}

main();