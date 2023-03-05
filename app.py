from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
import uuid

app = Flask(__name__, static_url_path='/static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Base_Flows.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

UPLOAD_FOLDER = 'static\images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# UPLOAD_FOLDER = '/static/images/to/the/uploads'
# ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
# app.config['MAX_CONTENT-PATH']


db = SQLAlchemy(app)


class Flow_water(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    model = db.Column(db.String, nullable=False)
    action = db.Column(db.String, nullable=False)
    NSH = db.Column(db.String, nullable=False)
    range = db.Column(db.String, nullable=False)
    error = db.Column(db.String, nullable=False)
    MPI = db.Column(db.String, nullable=False)
    method = db.Column(db.String, nullable=False)
    comment = db.Column(db.String, nullable=False)
    name_image = db.Column(db.String, nullable=True)

    def __repr__(self):
        return '<Flow_water %r>' % self.id


class Flow_oil(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    model = db.Column(db.String, nullable=False)
    action = db.Column(db.String, nullable=False)
    NSH = db.Column(db.String, nullable=False)
    range = db.Column(db.String, nullable=False)
    error = db.Column(db.String, nullable=False)
    MPI = db.Column(db.String, nullable=False)
    method = db.Column(db.String, nullable=False)
    comment = db.Column(db.String, nullable=False)
    name_image = db.Column(db.String, nullable=True)

    def __repr__(self):
        return '<Flow_oil %r>' % self.id


class PNG(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    model = db.Column(db.String, nullable=False)
    action = db.Column(db.String, nullable=False)
    NSH = db.Column(db.String, nullable=False)
    range = db.Column(db.String, nullable=False)
    error = db.Column(db.String, nullable=False)
    MPI = db.Column(db.String, nullable=False)
    method = db.Column(db.String, nullable=False)
    comment = db.Column(db.String, nullable=False)
    name_image = db.Column(db.String, nullable=True)

    def __repr__(self):
        return '<PNG %r>' % self.id


class Smoke(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    model = db.Column(db.String, nullable=False)
    action = db.Column(db.String, nullable=False)
    NSH = db.Column(db.String, nullable=False)
    range = db.Column(db.String, nullable=False)
    error = db.Column(db.String, nullable=False)
    MPI = db.Column(db.String, nullable=False)
    method = db.Column(db.String, nullable=False)
    comment = db.Column(db.String, nullable=False)
    name_image = db.Column(db.String, nullable=True)

    def __repr__(self):
        return '<Smoke %r>' % self.id


class Pulp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    model = db.Column(db.String, nullable=False)
    action = db.Column(db.String, nullable=False)
    NSH = db.Column(db.String, nullable=False)
    range = db.Column(db.String, nullable=False)
    error = db.Column(db.String, nullable=False)
    MPI = db.Column(db.String, nullable=False)
    method = db.Column(db.String, nullable=False)
    comment = db.Column(db.String, nullable=False)
    name_image = db.Column(db.String, nullable=True)

    def __repr__(self):
        return '<Pulp %r>' % self.id


class Steam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    model = db.Column(db.String, nullable=False)
    action = db.Column(db.String, nullable=False)
    NSH = db.Column(db.String, nullable=False)
    range = db.Column(db.String, nullable=False)
    error = db.Column(db.String, nullable=False)
    MPI = db.Column(db.String, nullable=False)
    method = db.Column(db.String, nullable=False)
    comment = db.Column(db.String, nullable=False)
    name_image = db.Column(db.String, nullable=True)

    def __repr__(self):
        return '<Steam %r>' % self.id


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/add_base', methods=['POST', 'GET'])
def add_base():
    if request.method == 'POST':
        title = request.form['title']
        model = request.form['model']
        action = request.form['action']

        range = request.form['range']
        error = request.form['error']
        MPI = request.form['MPI']
        method = request.form['method']
        comment = request.form['comment']
        type_flow = request.form['choice_flow']

        poz = (request.files['file'].filename).find('.')
        image = request.files['file'].filename[poz:]  # get .jpg
        name_image = str(uuid.uuid4()) + image

        poz1 = (request.files['file_nsh'].filename).find('.')
        image_nsh = request.files['file_nsh'].filename[poz1:]  # get .jpg
        NSH = str(uuid.uuid4()) + image_nsh


        filename = name_image
        file = request.files['file']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        filename2 = NSH
        file2 = request.files['file_nsh']
        file2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename2))


        if type_flow == 'water':
            flow_add = Flow_water(title=title, model=model, action=action, NSH=NSH, range=range, error=error,
                                  MPI=MPI, method=method, comment=comment, name_image=name_image)

        elif type_flow == 'oil':
            flow_add = Flow_oil(title=title, model=model, action=action, NSH=NSH, range=range, error=error,
                                MPI=MPI, method=method, comment=comment, name_image=name_image)

        elif type_flow == 'pulp':
            flow_add = Pulp(title=title, model=model, action=action, NSH=NSH, range=range, error=error,
                            MPI=MPI, method=method, comment=comment, name_image=name_image)

        elif type_flow == 'png':
            flow_add = PNG(title=title, model=model, action=action, NSH=NSH, range=range, error=error,
                           MPI=MPI, method=method, comment=comment, name_image=name_image)

        elif type_flow == 'smoke':
            flow_add = Smoke(title=title, model=model, action=action, NSH=NSH, range=range, error=error,
                             MPI=MPI, method=method, comment=comment, name_image=name_image)

        elif type_flow == 'steam':
            flow_add = Steam(title=title, model=model, action=action, NSH=NSH, range=range, error=error,
                             MPI=MPI, method=method, comment=comment, name_image=name_image)

        else:
            return "Переданы некорректные данные формы"

        try:
            db.session.add(flow_add)
            db.session.commit()
            return redirect('/')
        except:
            return "ERROR !!! При добавлении в базу произошла ошибка"

    else:
        return render_template('add_base.html')


@app.route('/flow_list/<poz_update>/<int:id>/update', methods=['POST', 'GET'])
def flow_updates(poz_update, id):
    if poz_update == 'water':
        flow_list_detail_update = Flow_water.query.get(id)

    elif poz_update == 'oil':
        flow_list_detail_update = Flow_oil.query.get(id)

    elif poz_update == 'pulp':
        flow_list_detail_update = Pulp.query.get(id)

    elif poz_update == 'png':
        flow_list_detail_update = PNG.query.get(id)

    elif poz_update == 'smoke':
        flow_list_detail_update = Smoke.query.get(id)

    elif poz_update == 'steam':
        flow_list_detail_update = Steam.query.get(id)

    else:
        return "Не удалось изменить данные"

    if request.method == 'POST':
        flow_list_detail_update.title = request.form['title']
        flow_list_detail_update.model = request.form['model']
        flow_list_detail_update.action = request.form['action']
        flow_list_detail_update.range = request.form['range']
        flow_list_detail_update.error = request.form['error']
        flow_list_detail_update.MPI = request.form['MPI']
        flow_list_detail_update.method = request.form['method']
        flow_list_detail_update.comment = request.form['comment']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return "При редактировании произошла ошибка"
    else:
        return render_template('create_flow.html', flow_list_detail_update=flow_list_detail_update,
                               poz_update=poz_update)


@app.route('/flow_list/<poz_show>')
def flow_list_(poz_show):
    if poz_show == 'water':
        flow_water_list = Flow_water.query.order_by(Flow_water.model).all()
        return render_template("flow_list.html", flow_list=flow_water_list, poz=poz_show,title='Расходомеры воды и водных растворов')
    elif poz_show == 'oil':
        flow_oil_list = Flow_oil.query.order_by(Flow_oil.model).all()
        return render_template("flow_list.html", flow_list=flow_oil_list, poz=poz_show, title='Расходомеры сырой нефти')
    elif poz_show == 'pulp':
        flow_pulp_list = Pulp.query.order_by(Pulp.model).all()
        return render_template("flow_list.html", flow_list=flow_pulp_list, poz=poz_show, title='Пульпы')
    elif poz_show == 'png':
        flow_png_list = PNG.query.order_by(PNG.model).all()
        return render_template("flow_list.html", flow_list=flow_png_list, poz=poz_show, title='ПНГ расходомеры')
    elif poz_show == 'smoke':
        flow_smoke_list = Smoke.query.order_by(Smoke.model).all()
        return render_template("flow_list.html", flow_list=flow_smoke_list, poz=poz_show, title='Расходомеры дымовых газов')
    elif poz_show == 'steam':
        flow_steam_list = Steam.query.order_by(Steam.model).all()
        return render_template("flow_list.html", flow_list=flow_steam_list, poz=poz_show, title='Расходомеры пара')



    else:
        return "Ошибка обращения к базе данных"


@app.route('/flow_list/<poz_details>/<int:id>')
def flow_list_details(poz_details, id):
    if poz_details == 'water':
        flow_water_detail = Flow_water.query.get(id)
        return render_template("flow_details.html", flow_list_detail=flow_water_detail, poz=poz_details)
    elif poz_details == 'oil':
        flow_oil_detail = Flow_oil.query.get(id)
        return render_template("flow_details.html", flow_list_detail=flow_oil_detail, poz=poz_details)
    elif poz_details == 'pulp':
        flow_pulp_detail = Pulp.query.get(id)
        return render_template("flow_details.html", flow_list_detail=flow_pulp_detail, poz=poz_details)
    elif poz_details == 'png':
        flow_png_detail = PNG.query.get(id)
        return render_template("flow_details.html", flow_list_detail=flow_png_detail, poz=poz_details)
    elif poz_details == 'smoke':
        flow_smoke_detail = Smoke.query.get(id)
        return render_template("flow_details.html", flow_list_detail=flow_smoke_detail, poz=poz_details)
    elif poz_details == 'steam':
        flow_steam_detail = Steam.query.get(id)
        return render_template("flow_details.html", flow_list_detail=flow_steam_detail, poz=poz_details)


if __name__ == '__main__':
    app.run(debug=True)
