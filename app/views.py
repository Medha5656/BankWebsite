from django.shortcuts import render
from .models import Customer,Transaction
from .forms import transactionForm
# Create your views here.
def index_view(request):
	return render(request,'app/index.html')

def customer_view(request):
    customer=Customer.objects.all()
    return render(request,'app/customers.html',{'customers':customer})

def transaction_view(request,id):
	cust_info=Customer.objects.get(pk=id)
	if request.method=="POST":
		form=transactionForm(request.POST)
		if form.is_valid():
			trans_to=form.cleaned_data['trans_to']
			ammount=form.cleaned_data['ammount']
			cust_to=Customer.objects.get(fname=trans_to)
			if(cust_info.balance<ammount):
				return render(request,'app/transaction.html',{'cust_info':cust_info,'form':transactionForm,'msg':"Insufficient Balance"})
			else:
				cust_info.balance-=ammount
				cust_info.save()
				cust_to.balance+=ammount
				cust_to.save()
				t=Transaction.objects.create(trans_from=cust_info,trans_to=trans_to,ammount=ammount)
				t.save()
				return render(request,'app/transaction.html',{'cust_info':cust_info,'form':transactionForm,'msg':"Transaction Completed"})
	return render(request,'app/transaction.html',{'cust_info':cust_info,'form': transactionForm})

def list_view(request):
	list=Transaction.objects.all()
	return render(request,'app/list.html',{'list':list})