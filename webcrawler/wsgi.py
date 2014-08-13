import eventlet
from eventlet import wsgi


def hello_world(env, start_response):
    if env['PATH_INFO'] != '/':
        start_response('404 Not found',[('Content-Type','text/plain')])
        return ['Tumhara File Not Found\r\n']
    start_response('200 OK',[('Content-Type','text/plain')])
    return ['Hello zerovm web service!\r\n']

wsgi.server(eventlet.listen(('',8090)),hello_world)
