const test = require("node:test");
const assert = require("node:assert");
const app = require("../src/server");

test("GET /health returns healthy status", async () => {
  const server = app.listen(0);

  const address = server.address();
  const url = `http://127.0.0.1:${address.port}/health`;

  const response = await fetch(url);
  const body = await response.json();

  assert.strictEqual(response.status, 200);
  assert.strictEqual(body.status, "healthy");

  server.close();
});
