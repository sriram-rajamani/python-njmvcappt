*** This is not for Real ID Appointment ***

Pre-Requisites:
Install Python and its required libraries

Mostly you may need Beatiful soup and lxml package. Install those with the below commands.

pip install beautifulsoup4
pip install lxml


If you want to search for appointment only on specific locations say Lawrenceville and Camden, then update the location_arr and locationname_arr variables
location_arr = ['101','104']
locationname_arr = ['Lawrenceville','Camden']


If you want to be notified only when appt is available on specific month, for example only on "April" then update the required moths variable accordingly.
required_months = ['April']

If you want to send an email when there is an appointment ready.
send_email_on = True in dl-alert.py
set variables in send_email.py from line 5 - 8