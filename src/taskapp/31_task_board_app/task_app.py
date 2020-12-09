import datetime
import csv


class Task:

    STATUS_OPENED = 0
    STATUS_CLOSED = 1

    def __init__(self, id, title, date, status):
        self.id = id
        self.title = title
        self.date = date
        self.status = status

    def show(self):
        print(self.id, self.title, self.date, self.status)


class TaskBoardError(Exception):
    pass


class TaskBoard:

    SHOW_ALL_TASK_LIST = 0
    SHOW_OPENED_TASK_LIST = 1
    ADD_TASK = 2
    FINISH_TASK = 3
    EDIT_TASK = 4
    DELETE_TASK = 5
    SAVE_FILE = 6
    LOAD_FILE = 7
    QUIT = 9

    def __init__(self):
        self.task_list = []

    def add_task(self, title):
        id = self.get_new_id()
        date = self.get_datetime_now_str()
        status = Task.STATUS_OPENED
        task = Task(id, title, date, status)
        self.task_list.append(task)

    def get_new_id(self):
        max_id = 0
        if len(self.task_list) > 0:
            max_id = max([task.id for task in self.task_list])
        return max_id + 1

    def show_task_list(self, include_closed_task=True):
        if include_closed_task:
            for task in self.task_list:
                task.show()
        else:
            for task in self.task_list:
                if task.status == Task.STATUS_OPENED:
                    task.show()

    def edit_task(self, id, title, status):
        target_task = self.get_task(id)
        target_task.title = title
        target_task.date = self.get_datetime_now_str()
        target_task.status = status

    def get_datetime_now_str(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_task(self, id):
        task_list = [task for task in self.task_list if task.id == id]
        if len(task_list) != 1:
            raise TaskBoardError("Invalid id. " + str(id))
        return task_list[0]

    def delete_task(self, id):
        target_task = self.get_task(id)
        task_list = [
            task for task in self.task_list if task.id != target_task.id]
        self.task_list = task_list

    def save_file(self, file_name):
        with open(file_name, "w") as f:
            writer = csv.writer(f)
            for task in self.task_list:
                writer.writerow([task.id, task.title, task.date, task.status])

    def load_file(self, file_name):
        self.task_list = []
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                id = int(row[0])
                title = row[1]
                date = row[2]
                status = int(row[3])
                task = Task(id, title, date, status)
                self.task_list.append(task)

    def show_operation_message(self):
        print("0: show all task list")
        print("1: show opened task list")
        print("2: add task")
        print("3: finish task")
        print("4: edit task")
        print("5: delete task")
        print("6: save file")
        print("7: load file")
        print("9: quit")


if __name__ == "__main__":
    task_board = TaskBoard()
    task_board.show_operation_message()
    while True:
        try:
            operation = int(input("operation: ").strip())
            if operation == TaskBoard.SHOW_ALL_TASK_LIST:
                task_board.show_task_list()
            elif operation == TaskBoard.SHOW_OPENED_TASK_LIST:
                task_board.show_task_list(False)
            elif operation == TaskBoard.ADD_TASK:
                title = input("title: ").strip()
                task_board.add_task(title)
            elif operation == TaskBoard.FINISH_TASK:
                id = int(input("id: ").strip())
                task = task_board.get_task(id)
                task_board.edit_task(task.id, task.title, Task.STATUS_CLOSED)
            elif operation == TaskBoard.EDIT_TASK:
                id = int(input("id: ").strip())
                title = input("title: ").strip()
                status = int(input("status(0: opened, 1: closed): ").strip())
                task_board.edit_task(id, title, status)
            elif operation == TaskBoard.DELETE_TASK:
                id = int(input("id: ").strip())
                task_board.delete_task(id)
            elif operation == TaskBoard.SAVE_FILE:
                file_name = input("file name: ").strip()
                task_board.save_file(file_name)
            elif operation == TaskBoard.LOAD_FILE:
                file_name = input("file name: ").strip()
                task_board.load_file(file_name)
            elif operation == TaskBoard.QUIT:
                break
        except TaskBoardError as e:
            print(e)
