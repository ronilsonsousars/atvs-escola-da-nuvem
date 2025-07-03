from datetime import date


def calculate_age_in_days(year_of_birth):
    """
    Cálculo da idade de uma pessoa em dias, baseado no ano de nascimento.
    """
    current_data = date.today()

    year_of_birth = date(year_of_birth, 1, 1)

    age_in_days = (current_data - year_of_birth).days

    return age_in_days


year_of_birth = 1999
age_days = calculate_age_in_days(year_of_birth)
print(f"A idade em dias é: {age_days}")
