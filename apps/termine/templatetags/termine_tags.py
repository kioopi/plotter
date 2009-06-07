# Template tag
from datetime import date, timedelta

from django import template
from apps.termine.models import Termin, Category # You need to change this if you like to add your own events to the calendar

register = template.Library()

from datetime import date, timedelta

def get_last_day_of_month(year, month):
    if (month == 12):
        year += 1
        month = 1
    else:
        month += 1
    return date(year, month, 1) - timedelta(1)


def month_cal(year, month, cat=None):
    """an inclusion tag to display a calendar with dates"""
    # 
    event_list = Termin.objects.filter(startdate__year=year, startdate__month=month, publish=True)

    #if cat:
    #    event_list.filter(categories=cat)  

    first_day_of_month = date(year, month, 1)
    next_month = first_day_of_month + timedelta(days=32)
    prev_month = first_day_of_month - timedelta(days=20)
    last_day_of_month = get_last_day_of_month(year, month)
    first_day_of_calendar = first_day_of_month - timedelta(first_day_of_month.weekday())
    last_day_of_calendar = last_day_of_month + timedelta(7 - last_day_of_month.weekday())
    month_cal = [] # a list cointainting lists representing the weeks in a month
    week = []      # a list cointaining a dict for each day
    week_headers = []

    i = 0
    day = first_day_of_calendar
    while day <= last_day_of_calendar:
        if i < 7:
            week_headers.append(day)
        cal_day = {}
        cal_day['day'] = day
        cal_day['event'] = False
        cal_day['events'] = [] 
        for event in event_list:
            if day >= event.startdate and day <= event.enddatetime.date():
                cal_day['events'].append({'link':event.get_absolute_url()})  
                if 'link' not in cal_day:
                    cal_day['link'] = event.get_absolute_url()
                else:
                    cal_day['multiple'] = True
                    cal_day['link'] = '/termine/%d-%d-%d/' % (int(year),int(month),int(day.day))
                cal_day['event'] = True
        # this switch smells
        if not cal_day['event']: 
           cal_day['cssclass'] = 'noevent'
        elif len(cal_day['events']) >= 5: 
           cal_day['cssclass'] = 'fiveormore'
	elif len(cal_day['events']) >= 2: 
	   cal_day['cssclass'] = 'twotofive'
 	elif len(cal_day['events']) == 1: 
	   cal_day['cssclass'] = 'oneevent'

        # check if date is in month to display to make it possible
        # to gray-out other days.
        if day.month == month:
            cal_day['in_month'] = True
        else:
            cal_day['in_month'] = False
        week.append(cal_day) # add the day-dict to the week array 
        if day.weekday() == 6: # if it's sunday, 
            month_cal.append(week) # add the week to the month list
            week = []         # new week
        i += 1
        day += timedelta(1)

    return {'calendar': month_cal, 'headers': week_headers,
            'next': next_month, 'prev': prev_month, 'this': first_day_of_month}

register.inclusion_tag('termine/calendar.html')(month_cal)



def catlist(year, month, day=None): 
    if day: 
        datestr = '%s-%s-%s' % (year, month, day) 
    else:
        datestr = '%s-%s' % (year, month) 
    object_list = Category.objects.all()  
    return {'object_list': object_list, 'datestr': datestr } 
register.inclusion_tag('termine/catlist.html')(catlist) 
