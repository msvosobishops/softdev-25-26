import time

def caden_history_shares(investment: int, fund: str, year) -> float:
    '''
    Purpose: returns the amount of shares that you could buy from a fund () with $() in () year.
    '''
    fund_a = [2.50, 3.75, 4.10, 5.10, 6.00]
    fund_b = [12.02, 14.10, 15.76, 18.08, 21.01]
    fund_c = [8.65, 8.03, 11.15, 19.82, 23.01]
    fund_d = [0.63, 1.22, 1.45, 2.01, 1.83]
    order_funds = ['a','b','c','d']
    order_dates = [1980,1996, 2012, 2016, 'current'] 
    funds = [fund_a, fund_b, fund_c, fund_d]

    #returns how many shares you couldve bought by dividing investment / share value of that year in that fund.
    return round(investment/(funds[order_funds.index(fund)][order_dates.index(year)])  , 2)


def caden_best_choice(investment: int, year) -> str:
    '''
    purpose: tells you which fund would have made the most money if you invested in that year
    return: how much money they made
    '''
    fund_a = [2.50, 3.75, 4.10, 5.10, 6.00]
    fund_b = [12.02, 14.10, 15.76, 18.08, 21.01]
    fund_c = [8.65, 8.03, 11.15, 19.82, 23.01]
    fund_d = [0.63, 1.22, 1.45, 2.01, 1.83]
    order_funds = ['a','b','c','d']
    order_dates = [1980,1996, 2012, 2016, 'current'] 
    funds = [fund_a, fund_b, fund_c, fund_d]

    funds_value = []

    #creates a new list that has all the profits they make
    for i in range(4):
        funds_value.append(round((caden_history_shares(investment, order_funds[i], year)*(funds[order_funds.index(order_funds[i])][order_dates.index('current')]))))

    #returns the most profitable, and the amount they make
    return(order_funds[funds_value.index(max(funds_value))])

def cady_history_shares(investment_amount: float, fund: str, year: int) -> float:
    '''takes in investment amount, fund, and year, returns number of shares the
    investment can buy in that year'''

    fundA = [2.50, 3.75, 4,10, 5.10, 6.00]
    fundB = [12.02, 14.10, 15.76, 18.08, 21.01]
    fundC = [8.65, 8.03, 11.15, 19.82, 23.01]
    fundD = [0.63, 1.22, 1.45, 2.01, 1.83]

    # finding the corresponding column in the list to use according to the year
    if year == 1980:
        index = 0
    elif year == 1996:
        index = 1
    elif year == 2012:
        index = 2
    elif year == 2016:
        index = 3
    elif year == 2025:
        index = 4

    # then divides investment amount by corresponding fund
    if fund.lower() == "a":
        shares = investment_amount / fundA[index]
    elif fund.lower() == "b":
        shares = investment_amount / fundB[index]
    elif fund.lower() == "c":
        shares = investment_amount / fundC[index]
    elif fund.lower() == "d":
        shares = investment_amount / fundD[index]

    return shares

def cady_calculate_profit_or_loss(initial_amount: float, fund: str, year: int) -> float:
    '''takes in initial investment amount, fund, and initial investment year,
    returns current profit made'''

    # amount of shares bought
    shares = cady_history_shares(initial_amount, fund, year)
    
    # sets price for each fund currently
    if fund.lower() == "a":
        price = 6
    elif fund.lower() == "b":
        price = 21.01
    elif fund.lower() == "c":
        price = 23.01
    elif fund.lower() == "d":
        price = 1.83

    # multiples shares bought to price to find total
    # subtracts total from initial amount to find profit
    total = price * shares
    profit = total - initial_amount
    return profit

def cady_best_choice(investment_amount: float, year: int) -> str:
    '''takes in investment amount and year, returns the name of the fund that 
    will make the most money'''
    
    funds = ["a","b","c","d"]
    profit = []

    # loops through each fund and adds amount of profit from each to the list
    for fund in funds:
        profit.append(cady_calculate_profit_or_loss(investment_amount, fund, year))

    # finds position of the largest profit
    position = profit.index(max(profit))
    # finds fund letter with the position
    best_fund = funds[position]
    return best_fund, max(profit)

def main():
    before = time.time()
    for i in range(100000):
        caden_best_choice(1000, 1996)
    after = time.time()
    print(after - before)

    before = time.time()
    for i in range(100000):
        cady_best_choice(1000, 1996)
    after = time.time()
    print(after - before)


main()