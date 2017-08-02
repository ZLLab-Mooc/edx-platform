"""homepage for the whole system"""

from django.http import HttpResponse
from edxmako.shortcuts import render_to_response


def index(request):
	#name='321' #to_student_system()
	context = {}
	return render_to_response("homepage/index.html", context)
	#return render_to_response("homepage/test.html", context)


