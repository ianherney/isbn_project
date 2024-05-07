from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from services.record_service import RecordService

record_api = Blueprint('record_api', __name__)

@record_api.route('/record', methods=['POST'])
def create_record():

    data = request.form
    user_company = data.get('user_company')
    user_line = data.get('user_line')
    capac_id = data.get('capac_id')
    capac_line = data.get('capac_line')
    capac_date = data.get('capac_date')
    capac_time = data.get('capac_time')
    capac_capacity = data.get('capac_capacity')

    if not user_company:
        return jsonify({'error': 'Company name is required'}), 400
    
    if not capac_id:
        return jsonify({'error': 'Id name is required'}), 400

    RecordService.create_record(user_company, user_line, capac_id, capac_line, capac_date, capac_time, capac_capacity)
    return redirect(url_for('record_api.index'))

@record_api.route('/')
def index():
    return render_template('index.html')
