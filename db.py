import sqlite3


class DB:
    def __init__(self):
        self.conn = sqlite3.connect('question.db')

    def add_question(self, question, answer):
        request = "INSERT INTO Quez (question,answer) values (?, ?)"
        self.conn.execute(request, (question, answer))
        self.conn.commit()

    def del_question(self, id):
        request = "DELETE FROM Quiz where id=?"
        self.conn.execute(request, (id,))
        self.conn.commit()

    def update_question(self, id, question):
        request = "UPDATE Quiz SET question=? WHERE id=?"
        self.conn.execute(request, (question, id))
        self.conn.commit()

    def update_answer(self, id, answer):
        request = "UPDATE Quiz SET answer=? WHERE id=?"
        self.conn.execute(request, (answer, id))
        self.conn.commit()

    def load_data(self):
        request = "SELECT question, answer FROM question"
        info = self.conn.execute(request).fetchall()
        data = []
        for i in range(len(info)):
            data.append({'id': i, 'question': info[i][0], 'correct_answer': info[i][1], 'answer': '', 'is_showed': 0})
        print(data)
        return data


db = DB()

db.load_data()
