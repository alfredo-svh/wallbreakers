# import
import socket
import os
import sys

# Create a socket, bind it to localhost:4242, and start listening.
# Runs once in the parent; all forked children inherit the socket's
# file descriptor.
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_STREAM) # TCP
sock.bind(("localhost", 4242))
sock.listen(10)

# Close the socket when we exit the parent or any child process. This
# only closes the file descriptor in the calling process, it does not
# take the socket out of the listening state (until the last fd is
# closed).
#
# The trap is guaranteed to happen, and guaranteed to happen only
# once, right before the process exits for any reason (unless
# it's terminated with a SIGKILL).
try:
	# Fork you some child processes. In the parent, the call to fork
	# returns immediately with the pid of the child process; fork never
	# returns in the child because we exit at the end of the block.
	for i in range(3):
		cpid = os.fork()

		if cpid ==0:
			# now we're in the child process; trap (Ctrl-C) interrupts and
			# exit immediately instead of dumping stack to stderr.
			try:
				print("child " +str(cpid) + " accepting on shared socket (localhost:4242)")
				while(True):
					# This is where the magic happens. accept(2) blocks until a
					# new connection is ready to be dequeued.
					conn, addr = sock.accept()
					conn.write("child " + str(cpid) + "echo: ")
					conn.flush()
					message = conn.gets()
					conn.write(message)
					conn.close()
					print("child " + str(cpid) +" echo'd: " + message)

			except KeyboardInterrupt:
				sys.exit()
except SystemExit:
	sock.close()



# Trap (Ctrl-C) interrupts, write a note, and exit immediately
# in parent. This trap is not inherited by the forks because it
# runs after forking has commenced.
# Sit back and wait for all child processes to exit.
try:
	os.waitpid(-1)

except KeyboardInterrupt:
	print("\nexiting")
	sys.exit()