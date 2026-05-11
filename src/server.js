const express = require("express");

const app = express();
// Middleware to parse JSON bodies
app.use(express.json());

app.get("/", (req, res) => {
  res.status(200).json({
    service: "appsec-cicd-lab",
    status: "ok"
  });
});

app.get("/health", (req, res) => {
  res.status(200).json({
    status: "healthy"
  });
});

app.get("/about", (req, res) => {
  res.status(200).json({
    app: "appsec-cicd-lab",
    purpose: "Learning AppSec integration into CI/CD"
  });
});

const port = process.env.PORT || 3000;

if (require.main === module) {
  app.listen(port, () => {
    console.log(`App listening on port ${port}`);
  });
}

module.exports = app;
