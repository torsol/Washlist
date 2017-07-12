import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Washlist.settings')


import django
django.setup()


from weeklist.models import Year, Week


def populate():

    year = Year(name='Kube61', room='Bathroom')
    year.save()

    #person_list = ['ask', 'marino', 'frøydis', 'torstein', 'alexander', 'norunn', 'iver', 'helene', 'mathias']
    person_list = ['Torstein', 'Iver', 'Norunn']
    for i in range(0, 52):
        week = Week(Year=year, week_num=i+1, washer=person_list[i % 3])
        week.save()

if __name__ == '__main__':
    populate()