# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 17:44:08 2023

@author: kpenaalvarez


Pmt = r * PV/(1-(1+r)**-n)
Pmt is how much you pay back/mo
n is number of months
r is interest rate per month
n is number of months


"""
# putting """ after def and hitting enter gives you parameters
def computesPmt(PV, r, n):
    """


    Parameters
    ----------
    Pv : TYPE float
        DESCRIPTION. present value (amt you borrow)
    r : TYPE float
        DESCRIPTION. interest rate APR
    n : TYPE integer
        DESCRIPTION. number of months to pay back loan

    Returns
    -------
    Pmt : TYPE float
        DESCRIPTION. amt paid per month

    """
    r = r/100 # convert apr to decimal
    r = r/12
    
    Pmt =  r * PV/(1-(1+r)**-n)
    return Pmt

def computesPV(Pmt, r, n):
    """
compute how much money you can borrow
    Parameters
    ----------
    Pmt : TYPE float
        DESCRIPTION. how much i can afford monthly
    r : TYPE
        DESCRIPTION.
    n : TYPE
        DESCRIPTION.

    Returns
    -------
    None.
    """
    r = r/100 # convert apr to decimal
    r = r/12

    Pv = (1-(1+r)**(-n)) * Pmt / r
    return Pv

def computesN(Pmt,Pv,r):
    """
    

    Parameters
    ----------
    pmt : TYPE FLOAT
        DESCRIPTION. MONTHLY PAYMENT
    Pv : TYPE FLOATAMT BORROWED
        DESCRIPTION.
    R : TYPE FLOAT
        DESCRIPTION.INTEREST RATE APR

    Returns
    -------
    n: TYPE INTEGER
    DESCRIPTION: NUMBER OF MONTHS TO PAY BACK LOAN

    """
    import numpy as np
    #convert r (APR) to a decimal, per month
    r = r/12 # converts to % per month
    r = r/100 # converts % to decimal 
    
    #given Pmt, Pv, r, we compute n
    
    n = -np.log( 1-Pv*r/Pmt) / np.log(1+r)
    n= round(n,1)
    
    return n

if __name__ == "__main__":                                     
                                
    import numpy as np

    while(True):
        choice = int(input("enter 1 for Pmt, 2 for PV, 3 for number of months to pay off loan  ->  "))
        if (choice ==1 or choice == 2 or choice == 3):
            break
        else:
            print(f"enter a 1, 2, or a 3, you entered {choice}")
        

if choice == 1:
    PV = input("enter PV: ")
    PV = float(PV)
    # equivalently PV = float(input("enter Pv: "))
    # \n creates a new line underneath
    print(f"PV = {PV} \n")
    
    r = float(input("interest (apr): "))
    #  putting a : and 0.2 makes it round to two decimal places. ends in f
    print(f"interest rate = {r: 0.3f} \n")
    
    n = int(input('how many months:  '))
    print(f"\nn = {n} months\n")
    
    pmt = computesPmt(PV, r, n)
    pmt = np.round(pmt, 2)
    print(f"payment is {pmt: } per month")
    
if choice == 2:
    
    Pmt = input('enter Pmt: ')
    Pmt = float(Pmt)
    print(f"Pmt = {Pmt} \n")
    
    r = float(input("interest (apr): "))
    #  putting a : and 0.2 makes it round to two decimal places. ends in f
    print(f"interest rate = {r: 0.3f} \n")
    
    n = int(input('how many months:  '))
    print(f"\nn = {n} months\n")
   
    PV = computesPV(Pmt, r, n)
    PV = np.round(PV, )
    print(f"amt I can borrow (present value) is: {PV: }")
    
if choice == 3:

    Pmt = input('enter Pmt: ')
    Pmt = float(Pmt)
    print(f"Pmt = {Pmt} \n")
    
    PV = input("enter PV: ")
    PV = float(PV)
    print(f"PV = {PV} \n")
    
    r = float(input("interest (apr): "))
    print(f"interest rate = {r: 0.3f} \n")
    MonthsMakingPayment = computesN(Pmt,PV,r)
    MonthsMakingPayment = np.round(MonthsMakingPayment, 2)
    print(f"loan will be paid off in {MonthsMakingPayment} months")
    