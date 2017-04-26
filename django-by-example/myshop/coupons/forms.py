from django import form 

class CouponApplyForm(forms.Form):
    code = forms.CharField()
