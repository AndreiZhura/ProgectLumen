const form = document.getElementById('nameForm');
const input = document.getElementById('nameInput');
const response = document.getElementById('response');

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const name = input.value;

  const result = await fetch('http://localhost:8000/hello', {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name })
  });

  const data = await result.json();
  response.textContent = data.message;
});
