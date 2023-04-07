'''Module 2: Individual Programming Assignment 1

Useful Business Calculations

This assignment covers your basic proficiency with Python.
'''

import math

def savings(gross_pay, tax_rate, expenses):
    tax_amount = tax_rate * gross_pay
    after_tax = math.floor(gross_pay - tax_amount)
    take_home_pay = int(after_tax) - expenses
    print(take_home_pay)
    return take_home_pay

# savings(50_000, 0.10, 25_000)

def material_waste(total_material, material_units, num_jobs, job_consumption):
    total_mat_consumed = num_jobs * job_consumption
    wasted_material = total_material - total_mat_consumed
    remaining_material = str(wasted_material) + material_units
    print(remaining_material)
    return remaining_material

# material_waste(1_000, "kg", 10, 5)

def interest(principal, rate, periods):
    simple_interest = principal * rate * periods
    final_value = math.floor(principal + int(simple_interest))
    print(final_value)
    return final_value

# interest(2_000, 0.05, 5)

def body_mass_index(weight, height):
    weight_in_kg = weight*0.453592
    height_ft = height[0]*0.3048
    height_in = height[1]*0.0254
    total_height = height_ft + height_in
    bmi = weight_in_kg / (total_height**2)
    print(bmi)
    return(bmi)
# body_mass_index(187.393, [5, 8])






