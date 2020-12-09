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


if __name__ == "__main__":
    task1 = Task(1, "Study Python", "2020-11-30 10:00:00", Task.STATUS_CLOSED)
    task2 = Task(2, "Study PHP", "2020-12-01 11:00:00", Task.STATUS_OPENED)
    task3 = Task(3, "Clean the room", "2020-12-02 12:00:00", Task.STATUS_OPENED)

    task1.show()
    task2.show()
    task3.show()
