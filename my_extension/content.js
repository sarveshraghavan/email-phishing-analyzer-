// This runs automatically when you open a Gmail message
const emailBody = document.querySelector(".a3s").innerText;

fetch('http://localhost:5000/analyze', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ content: emailBody })
})
.then(response => response.json())
.then(data => {
    console.log("PhishGuard Analysis:", data.analysis);
    // Here you would inject a red warning banner if the score is high!
});