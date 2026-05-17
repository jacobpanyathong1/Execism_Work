def exchange_money(budget, exchange_rate):
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    currency_value = budget / exchange_rate
    return currency_value


def get_change(budget, exchanging_value):
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    money_leftover = budget - exchanging_value
    return money_leftover


def get_value_of_bills(denomination, number_of_bills):
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """
    total = int( denomination *
            number_of_bills
    )
    return total 


def get_number_of_bills(budget, denomination):
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """
    number_bills = int(budget / denomination)
    return number_bills


def get_leftover_of_bills(budget, denomination):
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: float - the leftover amount that cannot be exchanged given the current denomination.
    """
    leftovers = float(budget %
                denomination)
    return leftovers 


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    # Calculate the actual exchange rate after adding the spread
    actual_exchange_rate = exchange_rate + (spread / 100 * exchange_rate)
    
    # Get the amount after currency conversion using the actual exchange rate
    exchanged_amount = exchange_money(budget, actual_exchange_rate)
    
    # Calculate the number of whole bills we can get with the exchanged amount
    num_bills = get_number_of_bills(exchanged_amount, denomination)
    
    # Calculate the value of the bills we receive
    value_of_bills = get_value_of_bills(denomination, num_bills)
    
    return int(value_of_bills)


