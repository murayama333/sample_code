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

    def show_task_list(self):
        for task in self.task_list:
            task.show()

    def edit_task(self, id, title, status):
        target_task = self.get_task(id)
        target_task.title = title
        target_task.date = self.get_datetime_now_str()
        target_task.status = status

    def get_task(self, id):
        task_list = [task for task in self.task_list if task.id == id]
        if len(task_list) != 1:
            raise TaskBoardError("Invalid id. " + str(id))
        return task_list[0]

    def get_datetime_now_str(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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


if __name__ == "__main__":
    task_board = TaskBoard()
    task_board.add_task("Study Python")
    task_board.add_task("Study PHP")
    task_board.add_task("Clean the room")

    task_board.save_file("task.csv")
