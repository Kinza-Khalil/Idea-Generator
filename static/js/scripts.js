const categoryInput = document.getElementById('category');
const generateBtn = document.getElementById('generate-btn');
const ideasList = document.getElementById('ideas');
generateBtn.addEventListener('click', () => {
  const category = categoryInput.value;
  if (category) {
    fetch('/generate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ category }),
    })
      .then((response) => response.json())
      .then((data) => {
        ideasList.innerHTML = '';
        data.ideas.forEach((idea) => {
          const listItem = document.createElement('li');
          listItem.textContent = idea;
          ideasList.appendChild(listItem);
        });
      });
  }
});

