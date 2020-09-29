import sys

def runScriptOnPDF(email, pdf):
	print("Hello I'm a python script and i'm running on Wordpress.")
	print(" The email of the current user is: " + email + ".")
	print(" You just uploaded the PDF: " + pdf)
runScriptOnPDF(sys.argv[1], sys.argv[2])