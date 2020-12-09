import datetime


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


class TaskBoard:

    def __init__(self):
        self.task_list = []

    def add_task(self, title):
        id = self.get_new_id()
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
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


if __name__ == "__main__":
    task_board = TaskBoard()
    task_board.add_task("Study Python")
    task_board.add_task("Study PHP")
    task_board.add_task("Clean the room")
    task_board.show_task_list()
