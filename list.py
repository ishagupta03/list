class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = "Incomplete"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def update_task(self, task_index, new_task):
        self.tasks[task_index] = new_task

    def delete_task(self, task_index):
        del self.tasks[task_index]

    def display_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"Task {i+1}:")
            print(f"Title: {task.title}")
            print(f"Description: {task.description}")
            print(f"Due Date: {task.due_date}")
            print(f"Status: {task.status}")
            print()

# Example usage:
my_todo_list = ToDoList()

task1 = Task("Complete project", "Finish the to-do list application", "2023-08-25")
task2 = Task("Buy groceries", "Get milk, eggs, and bread", "2023-08-22")

my_todo_list.add_task(task1)
my_todo_list.add_task(task2)

my_todo_list.display_tasks()