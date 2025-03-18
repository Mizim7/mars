from flask import Flask, render_template, request, redirect, url_for, json
import os
import random



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/image'


@app.route('/')
@app.route('/index')
@app.route('/index/<string:title>')
def index(title=None):
    if title is None:
        title = request.args.get('title', 'Заготовка')
    return render_template('base.html', title=title)


@app.route('/training/<string:prof>')
def training(prof):
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<string:list_type>')
def list_prof(list_type):
    professions = [
        "инженер-исследователь",
        "пилот",
        "строитель",
        "экзобиолог",
        "врач",
        "инженер по терраформированию",
        "климатолог",
        "специалист по радиационной защите",
        "астрогеолог",
        "гляциолог",
        "инженер жизнеобеспечения",
        "метеоролог",
        "оператор марсохода",
        "киберинженер",
        "штурман",
        "пилот дронов"
    ]
    return render_template('list_prof.html', list_type=list_type, professions=professions)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    data = {
        'title': 'Анкета',
        'surname': 'Watny',
        'name': 'Mark',
        'education': 'выше среднего',
        'profession': 'штурман марсохода',
        'sex': 'male',
        'motivation': 'Всегда мечтал застрять на Марсе!',
        'ready': True
    }
    return render_template('auto_answer.html', **data)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/distribution')
def distribution():
    astronauts = [
        "Ридли Скотт",
        "Энди Уир",
        "Марк Уотни",
        "Венката Капур",
        "Тедди Сандерс",
        "Шон Бин"
    ]
    return render_template('distribution.html', astronauts=astronauts)


@app.route('/table/<sex>/<int:age>')
def table(sex, age):
    if sex == 'male' and age > 21:
        color = 'blue'
    elif sex == 'male' and age < 21:
        color = '#ADD8E6'
    elif sex == 'female' and age > 21:
        color = 'red'
    else:
        color = 'pink'
    return render_template('table.html', color=color, age=age)


@app.route('/gallery', methods=['GET', 'POST'])
def gallery():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('gallery'))

    images = [filename for filename in os.listdir(app.config['UPLOAD_FOLDER']) if
              filename.endswith(('.png', '.jpg', '.jpeg'))]
    return render_template('gallery.html', images=images)


@app.route('/member')
def member():
    with open('templates/crew.json', encoding='utf-8') as f:
        crew = json.load(f)
    member = random.choice(crew)
    return render_template('member.html', member=member)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
