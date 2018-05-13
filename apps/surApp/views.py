from django.shortcuts import render,redirect
context={}
i=0
def index(request):
    return render(request,'index.html')

def process(request):
    
    global i,context
    i+=1
    print("We're in process")
    if request.method=='POST':
        request.POST
        print(request.POST)
        print(request.POST['name'])
        context={
            'name':request.POST['name'],
            'dojoName':request.POST['dojoName'],
            'favLang':request.POST['favLang'],
            'comment':request.POST['comment'],
            'i':i,
        }
    return redirect('/result')
def result(request):
    global context
    return render(request,'result.html',context)
