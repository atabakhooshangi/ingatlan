from user.models import OTP


def check_otp(email, otp_code):
    otp: OTP = OTP.objects.filter(email=email, otp_code=otp_code).last()
    if otp:
        if otp.expired:
            return False
        if not otp.is_valid():
            return False
        return True
    return False
