import math
from math import floor
def savings(gross_pay: int, tax_rate: float, expenses: int):
    take_home_pay=(gross_pay - round(gross_pay*tax_rate) - expenses)
    return(floor(take_home_pay))

def material_waste(total_material: int, material_units: str, num_jobs: int, job_consumption: int):
    waste=(total_material-(num_jobs*job_consumption))
    return(str(waste)+material_units)

def interest(principal, rate, periods):
    final_interest=(principal+(1+rate*periods))
    return(floor(final_interest))

def bmi(height:list,weight:int):
    height1 = height[0] * 0.3048
    height2 = height[1] * 0.0254
    final_height = height1 + height2
    weight1 = weight * 0.453592
    final_bmi = weight1/(final_height ** 2)
    return(round(final_bmi,2))
