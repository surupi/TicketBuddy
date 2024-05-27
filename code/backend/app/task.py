import os
from weasyprint import HTML

#for celery
from models import Admin, Customer, Booking, Venue, Movie
from workers import celery_app as celery
from celery.schedules import crontab
import datetime

#mailhog
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

import csv

from flask import Flask
from flask import render_template


sender = "abcd@example.com"
password = "password"


@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(minute=0, hour=18),   #run at 6pm everyday
        # 5,                              
        daily_remainder.s(),
    )
    sender.add_periodic_task(
        crontab(minute=0, hour=0, day_of_month=1),
        # 5,
        monthly_remainder.s(),
    )


#daily remainder
@celery.task
def daily_remainder():
    mail = smtplib.SMTP("localhost", 1025)
    mail.login(sender, password)
    customers = Customer.query.all()
    today = datetime.date.today()
    for customer in customers: 
        #user who hav enot booked anything
        if Booking.query.filter_by(cust_id=customer.cust_id, date=today).first() is None: 
            print ("daily remainder: ", customer.email)
            file = MIMEText("You have not booked any movies today. Please visit TicketBuddy.")
            file.add_header("content-disposition", f"attachment; filename=text.txt")
            mail.sendmail(sender, customer.email, file.as_string())


# monthly_remainder
@celery.task
def monthly_remainder():
    mail = smtplib.SMTP("localhost", 1025)
    mail.login(sender, password)
    customers = Customer.query.all()
    for customer in customers: 
        bookings = Booking.query.filter_by(cust_id=customer.cust_id).all()
        template_path = "monthly_message.html"
        
        monthly_render_template = render_template(template_path,
                                                  bookings=bookings,
                                                  month=datetime.date.today().strftime("%B"))
        
        msg = MIMEMultipart("alternative")
        msg["Subject"] = f"Monthly Report- {datetime.date.today().strftime('%B')}"
        file = MIMEText(monthly_render_template.encode("ascii", "ignore"), "html", "UTF-8") 
        file.add_header("content-disposition", f"attachment; filename=report.html")
        msg.attach(file)
        export_html = HTML(string = monthly_render_template, base_url = "")
        pdf = MIMEBase("application", "octet-stream")
        pdf.set_payload(export_html.write_pdf())
        pdf.add_header("content-disposition", f"attachment; filename=report.pdf")
        encoders.encode_base64(pdf)
        msg.attach(pdf)
        mail.sendmail(sender, customer.email, msg.as_string())


# #generate CSV
@celery.task
def exportcsv(venue_id):
    venues = Venue.query.filter_by(venue_id=venue_id).all()
    csv_file_path = 'venues.csv'
    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['venue_id', 'venue_name', 'venue_state', 'venue_city'])
        for venue in venues:
            writer.writerow([venue.venue_id, venue.venue_name, venue.venue_state, venue.venue_city])
    return csv_file_path

# csv_generate(1)
monthly_remainder()
