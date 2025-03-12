import click  # Import the click library create a CLI
import json  # Import "json" to save and load tasks from a file
import os  # Import "os" to check file exists

TODO_FILE = "todo.json"  # Define the filename where tasks are stored


# Function to load tasks from the JSON file
def load_tasks():
    if not os.path.exists(TODO_FILE):  # Check if file exists
        return []  # If not, return an empty list
    with open(TODO_FILE, "r") as file:  # Open the file in read mode
        return json.load(file)  # Load and return the JSON data as a Python list


def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)  # Load and return the JSON data as a Python list
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Return empty list if file doesn't exist or is empty
# // ... existing code ...
# Function to save tasks to the JSON file
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:  # Open the file in write mode
        json.dump(tasks, file, indent=4)  # Save tasks as formatted JSON


@click.group()  # Define a Click command group (main CLI)
def cli():
    """Simple To-Do List Manager"""  # Docstring for the CLI
    pass  # No action, acts as a container for commands


@click.command()  # Define a command called 'add'
@click.argument("task")  # Accepts a required argument (task name)
def add(task):
    """Add a new task to the list"""
    tasks = load_tasks()  # Load existing tasks
    tasks.append({"task": task, "done": False})  # Append a new task (default: not done)
    save_tasks(tasks)  # Save the updated tasks
    click.echo(f"Task added: {task}")  # Print a success message


@click.command()  # Define a command called 'list'
def list():
    """List all tasks"""
    tasks = load_tasks()  # Load existing tasks
    if not tasks:  # If there are no tasks
        click.echo("No tasks found!")  # Print message
        return  # Stop execution
    for index, task in enumerate(tasks, 1):  # Loop through tasks with numbering
        status = "✓" if task["done"] else "✗"  # Show '✓' for completed, '✗' for not
        click.echo(f"{index}. {task['task']} [{status}]")  # Print task with status

# @cli.command()
# def list():
#     """List all tasks"""
#     tasks = load_tasks()  # Load existing tasks
#     if not tasks:  # If there are no tasks
#         click.echo("No tasks found!")  # Print message
#         return  # Stop execution
#     for index, task in enumerate(tasks, 1):  # Loop through tasks with numbering
#         status = "✓" if task["done"] else "✗"  # Show '✓' for completed, '✗' for not
#         click.echo(f"{index}. {task['task']} [{status}]")  # Print task with status

@click.command()  # Define a command called 'complete'
@click.argument("task_number", type=int)  # Accepts a task number as an integer
def complete(task_number):
    """Mark a task as completed"""
    tasks = load_tasks()  # Load existing tasks
    if 0 < task_number <= len(tasks):  # Ensure task number is valid
        tasks[task_number - 1]["done"] = True  # Mark as done
        save_tasks(tasks)  # Save updated tasks
        click.echo(f"Task {task_number} marked as completed!")  # Print success message
    else:
        click.echo("Invalid task number.")  # Handle invalid numbers


@click.command()  # Define a command called 'remove'
@click.argument("task_number", type=int)  # Accepts a task number as an integer
def remove(task_number):
    """Remove a task from the list"""
    tasks = load_tasks()  # Load existing tasks
    if 0 < task_number <= len(tasks):  # Ensure task number is valid
        removed_task = tasks.pop(task_number - 1)  # Remove the task
        save_tasks(tasks)  # Save updated tasks
        click.echo(f"Removed task: {removed_task['task']}")  # Print removed task
    else:
        click.echo("Invalid task number.")  # Handle invalid numbers


# Add commands to the main CLI group
cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(remove)

# If the script is run directly, start the CLI
if __name__ == "__main__":
    cli()


# import click
# import json
# from datetime import datetime

# # File to stor@cli.command()
# @click.argument('task_id', type=int)
# def undone(task_id):
#     """Mark a task as not done"""
#     tasks = load_tasks()
#     if 1 <= task_id <= len(tasks):
#         tasks[task_id - 1]['done'] = False
#         save_tasks(tasks)
#         click.echo(f"Marked task {task_id} as not done!")
#     else:
#         click.echo("Invalid task ID!")

# @cli.command()
# @click.argument('task_id', type=int)
# def remove(task_id):
#     """Remove a task"""
#     tasks = load_tasks()
#     if 1 <= task_id <= len(tasks):
#         removed_task = tasks.pop(task_id - 1)
#         save_tasks(tasks)
#         click.echo(f"Removed task: {removed_task['task']}")
#     else:
#         click.echo("Invalid task ID!")

# @cli.command()
# def clear():
#     """Remove all tasks"""
#     if click.confirm("Are you sure you want to remove all tasks?"):
#         save_tasks([])
#         click.echo("All tasks have been removed!")

# if __name__ == '__main__':
#     cli()e tasks
# TASKS_FILE = 'tasks.json'

# def load_tasks():
#     """Load tasks from JSON file"""
#     try:
#         with open(TASKS_FILE, 'r') as file:
#             return json.load(file)
#     except (FileNotFoundError, json.JSONDecodeError):
#         return []

# def save_tasks(tasks):
#     """Save tasks to JSON file"""
#     with open(TASKS_FILE, 'w') as file:
#         json.dump(tasks, file, indent=2)

# @click.group()
# def cli():
#     """Todo CLI - A simple command line todo list manager"""
#     pass

# @cli.command()
# @click.argument('task')
# def add(task):
#     """Add a new task"""
#     tasks = load_tasks()
#     new_task = {
#         'task': task,
#         'done': False,
#         'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     }
#     tasks.append(new_task)
#     save_tasks(tasks)
#     click.echo(f"Added task: {task}")

# @cli.command()
# def list():
#     """List all tasks"""
#     tasks = load_tasks()
#     if not tasks:
#         click.echo("No tasks found!")
#         return
    
#     for index, task in enumerate(tasks, 1):
#         status = "✓" if task["done"] else "✗"
#         created_at = task.get('created_at', 'N/A')
#         click.echo(f"{index}. {task['task']} [{status}] (Created: {created_at})")

# @cli.command()
# @click.argument('task_id', type=int)
# def done(task_id):
#     """Mark a task as done"""
#     tasks = load_tasks()
#     if 1 <= task_id <= len(tasks):
#         tasks[task_id - 1]['done'] = True
#         save_tasks(tasks)
#         click.echo(f"Marked task {task_id} as done!")
#     else:
#         click.echo("Invalid task ID!")

