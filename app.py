from flask import Flask, request
from flask_restx import Api, Resource, fields
import os

app = Flask(__name__)
api = Api(
    app,
    version='1.0',
    title='Todo List API',
    description='A simple RESTful To-Do List API',
    doc='/docs'
)

# In-memory storage
todos = []
next_id = 1

# Define models for Swagger documentation
todo_model = api.model('Todo', {
    'id': fields.Integer(required=True, description='Todo ID'),
    'text': fields.String(required=True, description='Todo text'),
    'completed': fields.Boolean(required=True, description='Completion status')
})

todo_input_model = api.model('TodoInput', {
    'text': fields.String(required=True, description='Todo text'),
    'completed': fields.Boolean(required=False, description='Completion status', default=False)
})

todo_update_model = api.model('TodoUpdate', {
    'text': fields.String(required=False, description='Todo text'),
    'completed': fields.Boolean(required=False, description='Completion status')
})


@api.route('/todos')
class TodoList(Resource):
    @api.doc('list_todos')
    @api.marshal_list_with(todo_model)
    def get(self):
        """Get all todos"""
        return todos, 200

    @api.doc('create_todo')
    @api.expect(todo_input_model)
    @api.marshal_with(todo_model, code=201)
    def post(self):
        """Create a new todo"""
        global next_id
        
        data = request.get_json()
        
        # Validate input
        if not data or 'text' not in data:
            api.abort(400, 'text field is required')
        
        text = data.get('text', '').strip()
        if not text:
            api.abort(400, 'text cannot be empty')
        
        # Create new todo
        todo = {
            'id': next_id,
            'text': text,
            'completed': data.get('completed', False)
        }
        
        todos.append(todo)
        next_id += 1
        
        return todo, 201


@api.route('/todos/<int:id>')
@api.param('id', 'Todo ID')
class Todo(Resource):
    @api.doc('update_todo')
    @api.expect(todo_update_model)
    @api.marshal_with(todo_model)
    def put(self, id):
        """Update an existing todo"""
        todo = next((t for t in todos if t['id'] == id), None)
        if not todo:
            api.abort(404, f'Todo with id {id} not found')
        
        data = request.get_json()
        if not data:
            api.abort(400, 'Request body is required')
        
        # Update fields if provided
        if 'text' in data:
            text = data['text'].strip()
            if not text:
                api.abort(400, 'text cannot be empty')
            todo['text'] = text
        
        if 'completed' in data:
            todo['completed'] = bool(data['completed'])
        
        return todo, 200

    @api.doc('delete_todo')
    @api.response(204, 'Todo deleted')
    def delete(self, id):
        """Delete a todo"""
        global todos
        todo = next((t for t in todos if t['id'] == id), None)
        if not todo:
            api.abort(404, f'Todo with id {id} not found')
        
        todos = [t for t in todos if t['id'] != id]
        return '', 204


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)

