__author__ = 'Bhaumik'

from os import sep, curdir
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


port = 8000

#myWebHandler will responsible for client's request


class myWebHandler(BaseHTTPRequestHandler):


	def do_GET(self):

		try:


			Reply = False
			if self.path.endswith(".html"):
				mimetype='text/html'
				Reply = True


			if Reply == True:
				#Open the static file requested and send it
				f = open(curdir + sep + self.path,'rb')
				self.send_response(200)
				self.send_header('Content-type',mimetype)
				self.end_headers()
				self.wfile.write(f.read())
				f.close()
			return


		except IOError:
			self.send_error(404, 'File Not Found: %s' % self.path)

try:

	S_server = HTTPServer(('', port), myWebHandler)
	print 'Server is working on ', port


	S_server.serve_forever()      # Server will stay in request accepting mode

except KeyboardInterrupt:                               # To close server manually you have to type this command
	print '^Exit, shutting down the web server'
	S_server.socket.close()