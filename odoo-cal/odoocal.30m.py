#!/usr/bin/env python
import odoorpc
import time
from datetime import datetime, date, timedelta, timezone
import os

# Configure the connection credentials to the Odoo instance
ODOO_DOMAIN = os.environ.get('ODOO_DOMAIN', '<odoo-domain>')
ODOO_DB = os.environ.get('ODOO_DB', '<odoo-db-name>')
ODOO_USER = os.environ.get('ODOO_USER', '<odoo-login-user>')
ODOO_PASSWORD = os.environ.get('ODOO_PASSWORD', '<odoo-login-password>')

# Connect to the Odoo instance, get the user's events for today and print them
odoo = odoorpc.ODOO(ODOO_DOMAIN, port=443, protocol='jsonrpc+ssl')
odoo.login(ODOO_DB, ODOO_USER, ODOO_PASSWORD)

utc_offset = time.localtime().tm_gmtoff
local_tz = timezone(timedelta(seconds=utc_offset))
now_local = datetime.now(timezone.utc).astimezone(local_tz)
showTomorrow = False
user_id = odoo.env['res.partner'].search([('email', '=', ODOO_USER)])
if user_id:
    today = datetime.now().strftime('%Y-%m-%d')
    tomorrow = (date.today() + timedelta(days=1)).strftime('%Y-%m-%d')

    # If it's after 6pm, show tomorrow's events
    if now_local.hour >= 18:
        showTomorrow = True
        today = tomorrow
        tomorrow = (date.today() + timedelta(days=2)).strftime('%Y-%m-%d')
    
    domain = ['&', ('start', '>=', today), ('start', '<', tomorrow), ('partner_ids', 'in', user_id[0])]
    fields = ['name', 'start', 'stop', 'description', 'id']
    events = odoo.env['calendar.event'].search_read(domain, fields)
    events = sorted(events, key=lambda k: k['start'])

    if events:
        completed_events = 0
        pending_events = 0
        past_events = []
        future_events = []

        for event in events:
            start_time = datetime.strptime(event['start'], '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone.utc).astimezone(local_tz).strftime('%I:%M %p')
            end_time = datetime.strptime(event['stop'], '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone.utc).astimezone(local_tz).strftime('%I:%M %p')
            event_name = event['name'] or 'Untitled'
            event_description = event['description'] or 'No description'
            event_id = event['id']
            event_url = f'https://{ODOO_DOMAIN}/web?#id={event_id}&view_type=form&model=calendar.event'

            if now_local > datetime.strptime(event['stop'], '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone.utc).astimezone(local_tz):
                completed_events += 1
                event = start_time + " - " + end_time + ": " + event_name + " (" + event_description + ") | color=red | href=" + event_url + " | size=10"
                past_events.append(event)
            else:
                pending_events += 1
                event = f'{start_time} - {end_time}: {event_name} ({event_description}) | color=green | href={event_url}'
                future_events.append(event)
        if showTomorrow:
            print(f'📅 {pending_events} events tomorrow')
        else:
            print(f'📅 ({pending_events}/{completed_events + pending_events}) events today')
        print('---')
        if (len(future_events) > 0):
            print('Upcoming events')
        for event in future_events:
            print(event)
        calendar_url = f'https://{ODOO_DOMAIN}/web?#action=285&model=calendar.event&view_type=calendar&cids=1&menu_id=197'
        print('---')
        print(f'Open weekly calendar view | href={calendar_url}')
        if (len(past_events) > 0):
            print('---')
            print('Past events')
            for past in past_events:
                print(past)
    else:
        print('📅 No events today')
else:
    print(f'User {ODOO_USER} not found')
