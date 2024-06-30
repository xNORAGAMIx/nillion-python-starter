from nada_dsl import *

def nada_main():
    # Define a party
    party1 = Party(name="Party1")

    # Define secret integer inputs for the party
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Perform computations on the inputs
    sum_result = my_int1 + my_int2  # Compute the sum of the two integers
    product_result = my_int1 * my_int2  # Compute the product of the two integers

    # Return the outputs of the computations
    return [
        Output(sum_result, "sum_output", party1),  # Output the sum result
        Output(product_result, "product_output", party1)  # Output the product result
    ]
