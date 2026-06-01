"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""



EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate how much time is left in the lasagna bake time.

    Parameters:
        elapsed_bake_time (int): The amount of time the lasagna has already spent in
    the oven, in minutes.
        EXPECTED_BAKE_TIME (int): The total amount of time the lasagna needs in the
    oven to cook, in minutes.

    Returns:
        int: The total time remaining the lasagna needs to stay in the oven for.

    This function takes one integer representing the elapsed bake time in minutes and
    one constant representing the total bake time for the lasagna in minutes. It
    calculates how much longer the lasagna needs to stay in the oven for (total bake
    time - elapsed bake time)
    
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time




def preparation_time_in_minutes(number_of_layers):
    """Calculate the time it takes to prepare a number of lasagna layers.

    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        PREPARATION_TIME (int): Time it takes to prepare one layer of lasagna,
    in minutes.

    Returns:
        int: The total time it takes to prepare a number of lasagna layers.

    This function takes one integer representing the number of lasagna layers
    and a constant representing the number of minutes it takes to prepare one
    layer of lasagna. It calculates the total number of minutes needed to
    prepare any number of lasagna layers (number of layers * prep time for
    one layer).
    
    """
    return number_of_layers * PREPARATION_TIME
    


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.
    
    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): Time the lasagna has been baking in the oven.
    
    Returns:
        int: The total time elapsed (in minutes) preparing and baking.

    This function takes two integers representing the number of lasagna 
    layers and the time already spent baking the lasagna. It calculates 
    the total elapsed minutes spent cooking (preparing + baking).
    
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time