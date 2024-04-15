from flask import Flask, jsonify
import random

app = Flask(__name__)

def generate_student_scores():
    students = []
    for i in range(1, 51):
        student = {
            "id": i,
            "name": f"Student {i}",
            "score": random.randint(60, 100)  # Generating random scores between 60 and 100
        }
        students.append(student)
    return students

@app.route('/students/scores', methods=['GET'])
def get_student_scores():
    scores = generate_student_scores()
    return jsonify(scores)

if __name__ == '__main__':
    app.run(debug=True)
