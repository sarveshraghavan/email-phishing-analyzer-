// This tells the popup to update its text whenever it's opened
chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
  chrome.scripting.executeScript({
    target: {tabId: tabs[0].id},
    func: () => document.querySelector(".a3s").innerText // Grabs text from Gmail
  }, (results) => {
    const emailText = results[0].result;
    fetch('http://localhost:5000/analyze', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ content: emailText })
    })
    .then(r => r.json())
    .then(data => {
      document.getElementById('result').innerText = data.analysis;
    });
  });
});