require('dotenv').config();

const express = require('express');
const { auth } = require('express-openid-connect');
const escape = require('escape-html');

const app = express();

app.use(
  auth({
    authRequired: false,
    auth0Logout: true,

    secret: process.env.AUTH0_SECRET,
    baseURL: process.env.AUTH0_BASE_URL,
    clientID: process.env.AUTH0_CLIENT_ID,
    clientSecret: process.env.AUTH0_CLIENT_SECRET,
    issuerBaseURL: `https://${process.env.AUTH0_DOMAIN}`,

    authorizationParams: {
      response_type: 'code',
      audience: process.env.AUTH0_AUDIENCE,
      scope: 'openid profile email read:ai-data write:admin'
    }
  })
);

/* Access token */
app.get('/token', async (req, res) => {
  if (!req.oidc.isAuthenticated()) {
    return res.status(401).send('Not logged in');
  }

  try {
    const token = await req.oidc.accessToken();

    if (!token || !token.access_token) {
      return res.status(401).send('No access token found');
    }

    res.type('text').send(token.access_token);
  } catch (error) {
    console.error(error);
    res.status(500).send('Unable to obtain access token');
  }
});

/* Home */
app.get('/', (req, res) => {
  if (!req.oidc.isAuthenticated()) {
    return res.type('html').send(`
      <h1>AI Chat Web Application</h1>
      <a href="/signup">Signup</a><br>
      <a href="/login">Log in</a>
    `);
  }

  res.type('html').send(`
    <p>Logged in as ${escape(req.oidc.user.name)}</p>

    <h1>User Profile</h1>

    <pre>${escape(
      JSON.stringify(req.oidc.user, null, 2)
    )}</pre>

    <a href="/token">View API Access Token</a><br><br>

    <a href="/logout">Log out</a>
  `);
});

/* Signup */
app.get('/signup', (req, res) =>
  res.oidc.login({
    returnTo: '/',
    authorizationParams: {
      screen_hint: 'signup'
    }
  })
);

const port = process.env.PORT || 3000;

app.listen(port, () => {
  console.log(`Listening on http://localhost:${port}`);
});