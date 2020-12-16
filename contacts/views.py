from django.shortcuts import render, redirect
from .models import Node, DLinkedlist, lst, log
# Create your views here.
def index(request):
    return render(request, 'phonelog.html')

def contacts(request):
    n=lst.head
    lstname=[]
    lstnum=[]
    while n:
        lstname.append(n.name)
        lstnum.append(n.number)
        n=n.next
    if len(lstname)>0:    
        info=zip(lstname, lstnum)
        return render(request, 'contacts.html', {'info':info})
    else:
        return render(request, 'message.html',{'message': 'You have Zero contacts'})

def logs(request):
    n=log.tail
    lstname=[]
    lstnum=[]
    while n:
        lstname.append(n.name)
        lstnum.append(n.number)
        n=n.prev
    if len(lstname)>0:
        info=zip(lstname, lstnum)
        return render(request, 'contacts.html',{'info':info})
    else:
        return render(request, 'message.html', {'message': 'No logs'})

def addlog(request):
    num=int(request.GET.get('numb', False))
    n=lst.head
    while n:
        if n.number==int(num):
            nam=n.name
            phn=n.number
            break
        n=n.next
    logs=log.tail
    if logs:
        if logs.number!=phn:
            newnode=Node(nam, phn)
            log.tail.next=newnode
            newnode.prev=log.tail
            log.tail=newnode
    else:
        newnode=Node(nam, phn)
        log.tail=newnode

    return redirect('http://localhost:8000', name='home')

def addcontact(request):
    return render(request, 'addcontact.html')

def add(request):
    name = request.POST.get('contactname', False)
    num = int(request.POST.get('contactnumber', False))
    lst.bisecting_insert(name, num)

    return redirect('http://localhost:8000', name='home')

def search(request):
    key=request.GET.get('key', False)
    n=lst.head
    lstname=[]
    lstnum=[]
    if key.isdigit():
        while n:
            if key in str(n.number):
                lstname.append(n.name)
                lstnum.append(n.number)
            n=n.next
    else:
        while n:
            if key in n.name:
                lstname.append(n.name)
                lstnum.append(n.number)
            n=n.next
    if len(lstname)>0:    
        info=zip(lstname, lstnum)
        return render(request, 'contacts.html', {'info':info})
    else:
        return render(request, 'message.html',{'message':'No Contacts Found'})

def delete(request):
    num=int(request.GET.get('numb', False))
    lst.delete(num)
    log.deletelog(num)
    return redirect('http://localhost:8000', name='home')

