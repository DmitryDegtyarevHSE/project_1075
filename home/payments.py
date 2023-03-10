import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from yookassa import Configuration, Payment


class YooKassaPayment(APIView):
    """Создание и принятие платежа ЮКАССА"""
    def get(self, request):
        Configuration.account_id = '973050'
        Configuration.secret_key = 'test_5N4ujI7BMHe4YRnB3luyFvcnw1fl52fTYXXEp6lAMe0'
        value = request.GET.get('value')
        payment = Payment.create({
            "amount": {
                "value": value,
                "currency": "RUB"
            },
            "confirmation": {
                "type": "redirect",
                "return_url": "https://dfvrn.pythonanywhere.com/"
            },
            "capture": True,
            "description": "Тестовый заказ"
        }, uuid.uuid4())
        response_data = {'redirect_url': payment.confirmation.confirmation_url}
        return Response(data=response_data)

