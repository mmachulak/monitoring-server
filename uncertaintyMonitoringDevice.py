##server.py
import pickle
import socket
import SocketServer
import sys
import threading
import time

class ProcessSocketData(SocketServer.BaseRequestHandler):

    def handle(self):
        # Echo the back to the client
        receivedData = self.request.recv(1024)
        #cur_thread = threading.currentThread()
        #response = '%s: %s' % (cur_thread.getName(), data)
        self.request.send("Received: "+receivedData)
	listReceivedData = receivedData.split(",")
	print "Received:", listReceivedData
	if listReceivedData[0] == "SensorValue":
		# Add to MySQL database in sensor table
		pass
	elif listReceivedData[0] == "MetricValue":
		# Add to MySQL database in metric table
		pass
	else:
		print "Error.  Invalid data type"
        return

class ThreadedDataMonitorServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

def main():
	serverAddress = ('localhost', 37568) # let the kernel give us a port
	#server = SocketServer.TCPServer(address, EchoRequestHandler)
	socketForDataCollection = ThreadedDataMonitorServer(serverAddress, ProcessSocketData)
	#ip, port = sensorValueCollection.server_address # find out what port we were given
	serverThread = threading.Thread(target=socketForDataCollection.serve_forever)
	serverThread.setDaemon(True) # don't hang on exit
	serverThread.start()

	while True:
		print "Another minute..."
		time.sleep(60)

if __name__ == "__main__":
    main()
