import httplib

from flask import Flask, request, send_file
import addressbook_pb2
import io

app = Flask(__name__)
address_book = addressbook_pb2.AddressBook()
person = addressbook_pb2.Person()

@app.route('/save', methods=['GET'])
def save():

    person.name = 'Name'
    person.id = 1
    
    return send_file(
        io.BytesIO(person.SerializeToString()),
        as_attachment=True,
        attachment_filename='abc.abc',
        mimetype='attachment/x-protobuf'
    )


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')