// static/js/main.js
function analyzeSentiment() {
    const textInput = document.getElementById('textInput').value;
    const url = '/api/sentiment';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            text: textInput
        })
    })
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById('result');
        resultDiv.innerHTML = `Sentiment: ${data.sentiment}`;
    })
    .catch(error => console.error('Error:', error));
}
