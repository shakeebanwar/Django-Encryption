from django.core.managment import call_command
def my_backup():
    try:
        call_command('dbbackup')

    except:
        pass
