from flask import jsonify, request

from src import api_todo
from src.models.TodoModel import Todo
from src.common.response import Response, ResponseMessages, ResponseCodes


'''This api is responsible for getting all todo lastly added'''
@api_todo.route('/listing')
def listing():
    try:
        listing_records = Todo.get_all()
        data = convert_db_data_with_response(listing_records, ['id', 'content', 'type', 'created_at'])
        if listing_records:
            response = Response.success(message=ResponseMessages.todo_listing_found.value, data=data)
        else:
            response = Response.error(code=ResponseCodes.not_found.value,
                                      message=ResponseMessages.todo_listing_not_found.value)
    except Exception as e:
        response = Response.error(message=ResponseMessages.exception_message.value + str(e))

    return jsonify(response), response['code']


'''This api is responsible for adding new todo'''
@api_todo.route('/add', methods=['POST'])
def add():
    try:
        content = request.form['content']
        if content:
            todo_add = Todo(content)
            todo_add.save()
            response = Response.success(code= ResponseCodes.created.value,
                                        message=ResponseMessages.todo_add.value)
        else:
            response = Response.error(code=ResponseCodes.precondition_failed.value,
                                      message=ResponseMessages.todo_content_empty.value)
    except Exception as e:
        response = Response.error(message=ResponseMessages.exception_message.value + str(e))

    return jsonify(response), response['code']


def convert_db_data_with_response(db_data, column_indexes):
    result_data = []
    for each in db_data:
        record = {}
        for key, col in enumerate(column_indexes):
            record[col] = each[key]
        result_data.append(record)
    return result_data