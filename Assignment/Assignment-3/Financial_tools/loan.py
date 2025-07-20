def calculate_emi(principal, rate, time):
    """Calculate EMI using simple interest formula"""
    interest = (principal * rate * time) / 100
    total = principal + interest
    emi = total / (time * 12)  # time in years, monthly EMI
    return round(emi, 2)
