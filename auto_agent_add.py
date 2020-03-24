import xmlrpc.client

HOST = 'https://mrgreen-trading-feb20.odoo.com'
PORT = ''
DB = '012020'
USER = 'odoo'
PASS = 'Ubuntu13'
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(HOST))
print(common.version())
uid = common.authenticate(DB, USER, PASS, {})
print(uid)
# Create a new note
#sock = xmlrpc.client.ServerProxy(root + 'object')
#args = {
#    'color' : 8,
#    'memo' : 'This is a note',
#    'create_uid': uid,
#}
#note_id = sock.execute(DB, uid, PASS, 'note.note', 'create', args)
