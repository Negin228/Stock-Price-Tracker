const express = require('express');
const fetch = require('node-fetch');
const app = express();

// Serve the content of the templates/index.html when stockhome.me is accessed
app.get('*', async (req, res) => {
  try {
    // Fetch the content of https://stockhome.me/templates/index.html
    const response = await fetch('https://stockhome.me/templates/index.html');
    
    // Check if the response is successful
    if (!response.ok) {
      throw new Error(`Failed to fetch HTML: ${response.statusText}`);
    }

    // Get the text (HTML) from the response
    const htmlContent = await response.text();

    // Send the HTML content as the response
    res.send(htmlContent);
  } catch (error) {
    // Log any errors that occur during the fetch
    console.error('Error fetching the page:', error);
    
    // Send an error response to the client
    res.status(500).send('Internal Server Error: Unable to fetch the page.');
  }
});

// Set the port for Heroku or default to port 3000 for local testing
const port = process.env.PORT || 3000;

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
