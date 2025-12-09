// Simple to-do list with add, delete, and mark completed
const input = document.getElementById('todo-input');
const addBtn = document.getElementById('add-btn');
const listEl = document.getElementById('todo-list');

let todos = [];

function save() {
  try { localStorage.setItem('todos', JSON.stringify(todos)); } catch (e) { /* ignore */ }
}

function load() {
  try {
    const raw = localStorage.getItem('todos');
    todos = raw ? JSON.parse(raw) : [];
  } catch (e) { todos = []; }
}

function render() {
  listEl.innerHTML = '';
  if (todos.length === 0) {
    const li = document.createElement('li');
    li.className = 'small';
    li.textContent = 'No tasks — add one above.';
    listEl.appendChild(li);
    return;
  }

  todos.forEach((t, idx) => {
    const li = document.createElement('li');
    li.className = 'todo-item';

    const left = document.createElement('div');
    left.className = 'todo-left';

    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.checked = !!t.completed;
    checkbox.addEventListener('change', () => toggleComplete(idx));

    const span = document.createElement('span');
    span.className = 'todo-text' + (t.completed ? ' completed' : '');
    span.textContent = t.text;

    left.appendChild(checkbox);
    left.appendChild(span);

    const right = document.createElement('div');

    const delBtn = document.createElement('button');
    delBtn.className = 'icon-btn delete-btn';
    delBtn.textContent = 'Delete';
    delBtn.addEventListener('click', () => deleteTodo(idx));

    right.appendChild(delBtn);

    li.appendChild(left);
    li.appendChild(right);
    listEl.appendChild(li);
  });
}

function addTodo() {
  const text = input.value.trim();
  if (!text) return;
  todos.push({ text, completed: false });
  input.value = '';
  save();
  render();
  input.focus();
}

function deleteTodo(i) {
  todos.splice(i, 1);
  save();
  render();
}

function toggleComplete(i) {
  todos[i].completed = !todos[i].completed;
  save();
  render();
}

addBtn.addEventListener('click', addTodo);
input.addEventListener('keydown', (e) => { if (e.key === 'Enter') addTodo(); });

// initialize
load();
render();