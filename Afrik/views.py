from django.shortcuts import render
from .models import my_post
from .models import my_members
from .models import my_notifications

My_posts = [
    {
        'club' : 'ICT club',
        'date' : '28 August 2021 8:30',
        'content': 'this is what we have for you',
        'likes' : '20',
        'school' : 'Alliance high school'
    },

    {
        'club' : 'farmers club',
        'date' : '28 August 2021 9:30',
        'content': 'this is what we have for you',
        'likes' : '100',
        'school' : 'Thika high school'
    },

]

My_members = [
    {
        'member_name' : 'George Chesire',
        'post' : 'Chairman'
    },

    {
        'member_name': 'John Doe',
        'post': 'vice chairman'
    },

]

My_notifications = [
    {
        'sender' : 'Kenya High School',
        'when' : '28  August 2019',
        'content' : 'This is where the notification content will appear. It will contain the necessary info'
    },

    {
        'sender' : 'Kenya High School',
        'when' : '28  August 2019',
        'content' : 'You have a new invite from sb for sth event that will take place on date. You are required to come with a maximum of 5 participants'

    },

]

Student_details = [
    {
        'firstname' : '',
        'lastname' : '',
        'school' : '',
        'email' : '',
        'my_amount' : ''
    }
]

Student_notifications = [
    {
        'sender' : 'Kenya High School',
        'when' : '28  August 2019',
        'content' : 'This is where the notification content will appear. It will contain the necessary info'
    },

    {
        'sender' : 'Kenya High School',
        'when' : '28  August 2019',
        'content' : 'You have a new invite from sb for sth event that will take place on date. You are required to come with a maximum of 5 participants'

    },

]

def members(request):
    the_members = {
        'members' : my_members.objects.all(),
        'number' : my_members.objects.count()

    }

    return render(request, 'Afrik/members.html', the_members)

def notifications(request):
    the_notifications = {
        'notifications': my_notifications.objects.all(),
        'number' : my_notifications.objects.count()

    }
    return render(request, 'Afrik/notifications.html', the_notifications)

def posts(request):

    the_posts = {
        'posts': my_post.objects.all()

    }

    return render(request, 'Afrik/posts.html', the_posts)

def homepage(request):
    return render(request, 'Afrik/home page.html')

def profile(request):
    the_details = {
        'details' : Student_details,
        'notifications': Student_notifications
    }

    return render(request, 'Afrik/profile.html', the_details)
