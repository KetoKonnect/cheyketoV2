from ketokonnect2.celery import app
from django.core.mail import send_mail
from .models import Order

@app.task
def order_created(order_id):
    """
    Task to send and email notification when an order is successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Order no. {order.id}'
    message = f'Dear {order.first_name}, \n\n'\
        f'You have successfully placed an order.'\
            f'Your order ID is {order.id}.'

    mail_sent = send_mail(subject, message, 'admin@ketokonnect242.com', [order.email])

    return mail_sent

