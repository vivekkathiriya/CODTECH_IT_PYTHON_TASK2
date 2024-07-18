from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        subjects = request.form.getlist('subject')
        grades = request.form.getlist('grade')
        grades = [float(grade) for grade in grades]
        
        average_grade = sum(grades) / len(grades) if grades else 0
        letter_grade = get_letter_grade(average_grade)
        gpa = calculate_gpa(grades)
        
        return render_template('index.html', subjects=subjects, grades=grades,
                               average_grade=average_grade, letter_grade=letter_grade, gpa=gpa)
    return render_template('index.html', subjects=[], grades=[], average_grade=None, letter_grade=None, gpa=None)

def get_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def calculate_gpa(grades):
    total_points = 0
    for grade in grades:
        if grade >= 90:
            total_points += 4.0
        elif grade >= 80:
            total_points += 3.0
        elif grade >= 70:
            total_points += 2.0
        elif grade >= 60:
            total_points += 1.0
        else:
            total_points += 0.0
    return total_points / len(grades) if grades else 0

if __name__ == '__main__':
    app.run(debug=True)
