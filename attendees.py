from models import Attendees
from flask import Blueprint, request, jsonify, session, redirect
from playhouse.shortcuts import model_to_dict

attendees = Blueprint('attendees', 'attendees')

##SHOW ALL ATTENDEES
@attendees.route('/', methods=['GET'])
def get_attendees():
    attendees = Attendees.select()

    attendee_dicts = [model_to_dict(attendee) for attendee in attendees]

    return jsonify (
        data=attendee_dicts,
        message=f"Successfully found {len(attendee_dicts)} attendees",
        status=200
    ), 200

##SHOW BY TEAM NUMBER
@attendees.route('/team/<teamnumber>', methods=['GET'])
def get_team(teamnumber):
    teams = Attendees.select().where(Attendees.team == teamnumber)

    team_dicts = [model_to_dict(team) for team in teams]

    return jsonify (
        data= team_dicts,
        message=f"Successfully found {len(team_dicts)} attendees on Team# {teamnumber}",
        status=200
    ), 200

##SHOW BY COMPANY NAME
@attendees.route('/company/<companyname>', methods=['GET'])
def get_company(companyname):
    company_attendees = Attendees.select().where(Attendees.Company == companyname)

    com_att_dicts = [model_to_dict(company_attendee) for company_attendee in company_attendees]

    return jsonify (
        data = com_att_dicts,
        message=f"Successfully found {len(company_attendees)} attendees from {companyname}",
        status=200
    ), 200

##SHOW BY JOB TITLE
@attendees.route('/title/<title>', methods=['GET'])
def get_by_title(title):
    attendee_titles = Attendees.select().where(Attendees.title == title)

    att_title_dicts = [model_to_dict(attendee_title) for attendee_title in attendee_titles]

    return jsonify (
        data = att_title_dicts,
        message=f"Successfully found {len(attendee_titles)} attendees with the title {title}",
        status = 200
    ), 200

##EDIT ATTENDEE
@attendees.route('/<id>', methods=['PUT'])
def update_attendee(id):
    payload = request.get_json()

    Attendees.update(**payload).where(Attendees.id == id).execute()

    return jsonify (
        data=model_to_dict(Attendees.get(Attendees.id == id)),
        message='Attendee record has been udpated',
        status=200
    ), 200

##DELETE ATTENDEE 
@attendees.route('/<id>', methods=['DELETE'])
def delete_attendee(id):
    delete_attendee = Attendees.delete().where(Attendees.id == id).execute()

    return jsonify (
        data={},
        message=f"Successfully deleted attendee",
        status=200
    ), 200

##CREATE ATTENDEE
@attendees.route('/', methods=['POST'])
def create_attendee():
    payload = request.get_json()

    new_attendee = Attendees.create(**payload)

    attendee_dict = model_to_dict(new_attendee)

    return jsonify (
        data=attendee_dict,
        message='Successfully create new attendee',
        status=201
    ), 201

##SHOW ATTENDEE
@attendees.route('/<id>', methods=['GET'])
def get_by_id(id):
    attendee = Attendees.get_by_id(id)

    attendee_dict = model_to_dict(attendee)

    return jsonify (
        data = attendee_dict,
        message="Found it!",
        status = 200
    ), 200

##SEARCH BY ANY PART OF NAME
# @attendees.route('/<partofname>', methods=['GET'])
#     def get_by_parts(partofname):
    
