import datetime
from flask import Blueprint, flash, render_template, redirect, request, url_for
from flask_login import login_required, current_user
from logger.models import User, db, Callsign, QSO
from logger.forms import QSOForm, QSOUploadForm

qsos = Blueprint('qsos', __name__, template_folder='templates')

@qsos.route("/<station_callsign>/new", methods=['GET','POST'])
@login_required
def postnewqso(station_callsign):
    form = QSOForm()
    if request.method == 'POST':
        qso_date = datetime.datetime.strptime(request.form['qso_date'], '%Y-%m-%d').date()
        time_on = datetime.datetime.strptime(request.form['time_on'], '%H:%M').time()
        call = request.form['call']
        mode = request.form['mode']
        band = request.form['band']
        gridsquare = request.form['gridsquare']
        my_gridsquare = request.form['my_gridsquare']
        station_callsign = station_callsign
        newqso = QSO(qso_date=qso_date, time_on=time_on, call=call, mode=mode,
                    band=band, gridsquare=gridsquare, my_gridsquare=my_gridsquare, station_callsign=station_callsign)
        db.session.add(newqso)
        db.session.commit()
        return redirect(url_for('callsigns.call',callsign=station_callsign))
    return render_template('qsoform.html', form=form, station_callsign=station_callsign)

@qsos.route("/<station_callsign>/upload", methods=['GET', 'POST'])
@login_required
def uploadqsos(station_callsign):
    uploadform = QSOUploadForm()
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            uploaded_file.save(uploaded_file.filename)
        return redirect(url_for('callsigns.call',callsign=station_callsign))
    return render_template('qsoupload.html')

@qsos.route('/view/<call>/<date>/<time>')
@login_required
def viewqso(call, date, time):
    call = call.replace('_', '/')
    qso = QSO.query.filter_by(call=call, qso_date=date, time_on=time).first()
    return render_template('viewqso.html', qso=qso)

