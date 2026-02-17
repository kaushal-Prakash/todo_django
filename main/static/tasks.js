const taskList = document.getElementById("taskList");
const addBtn = document.getElementById("addBtn");
const modal = document.getElementById("modal");
const saveBtn = document.getElementById("saveBtn");
const cancelBtn = document.getElementById("cancelBtn");
const taskInput = document.getElementById("taskInput");

// Load tasks
function loadTasks() {
  const tasks = JSON.parse(localStorage.getItem("todos")) || [];
  taskList.innerHTML = "";

  if (tasks.length >= 0) {
    const taskSubTitle = document.getElementById("task-container-sub-header");
    taskSubTitle.textContent = `You have ${tasks.length} tasks, Click to delete them.`;
  }

  tasks.forEach((task, index) => {
    const li = document.createElement("li");
    li.className = "task-item";
    li.textContent = task;

    // Delete on click
    li.addEventListener("click", () => {
      tasks.splice(index, 1);
      localStorage.setItem("todos", JSON.stringify(tasks));
      loadTasks();
    });

    taskList.appendChild(li);
  });
}

// Open modal
addBtn.onclick = () => {
  modal.classList.remove("hidden");
  taskInput.focus();
};

// Close modal
cancelBtn.onclick = () => {
  modal.classList.add("hidden");
  taskInput.value = "";
};

// Save task
saveBtn.onclick = () => {
  const task = taskInput.value.trim();
  if (!task) return;

  const tasks = JSON.parse(localStorage.getItem("todos")) || [];
  tasks.push(task);

  localStorage.setItem("todos", JSON.stringify(tasks));

  taskInput.value = "";
  modal.classList.add("hidden");

  loadTasks();
};

// Load on start
loadTasks();
