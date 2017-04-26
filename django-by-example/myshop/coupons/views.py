from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import Coupon
from .forms import CouponApplyForm

# Create your views here.



@require_POST
def coupon_apply(request):
    now = timezone.now()
    form = CouponApplyForm(request.POST)
    if form.is_valid():
        code = Form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__iexact=code, valid_from__ite=now, valid_to__gte=now, active=True)
            request.session['coupon_id'] = coupon.id
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
    return redirect('cart:cart_detail')
