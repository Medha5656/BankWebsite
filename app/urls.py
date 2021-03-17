from django.urls import path
from .views import *

urlpatterns=[
	path('index/',index_view),
	path('customer/',customer_view),
	path('transaction/<int:id>',transaction_view,name="transaction"),
	path('list/',list_view),
]