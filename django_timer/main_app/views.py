from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
# get input from main page
# render an html page (just use index?)
def countdown_module(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer)
        time.sleep(1)
        t -= 1
    print('Go!!')
# return timer
