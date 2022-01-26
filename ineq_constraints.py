import pandas as pd
import numpy as np

def srwa_cet1(x, df, sRWA_mins):
    '''
    Inequality constraint for Standardized RWA at the CET1 level.
    Constraint states that there must be sufficient Equity to cover a given percentage of total Standardized RWA.
    This function performs two calculations:
        - GSIB add-on. This is added to the base SRWA minimum for calculating the final inequality
        - SRWA inequality. Using the GSIB add-on and base SRWA minimum, ensure that there is sufficient equity to cover the final
        SRWA minimum times total SRWA
    Inputs:
        - x: array of balances for all line items on the B/S. This number begins as X0 (starting B/S), but changes with each
             successive optimization iteration
        - df: original dataframe of the B/S inputs. Used to extract the SRWA weights for each line item plus the CET1 resource weights
        - sRWA_mins: list of starting constraint minimums. The GSIB add-on is added on top of this to calculate the final minimum
    Outputs:
        - cet1_constraint: the ending position of the inequality equation. Needs to be greater than or equal to 0 at all times.
    '''
    
    
    # Define GSIB add-on
    gsib_addon = 0
    gsib_cont = np.array(df['cet1_contr_per_balance'])
    
    # Define base RWA min
    s_rwa = np.array(df['s_rwa'])
    
    # Define what counts as a resource towards solving the constraint
    cet1_resource = np.array(df['CET1_resource'])
    
    # Define the constraint threshold. The inequality has to be greater than 0.
    cet1_constraint = 0
    
    # Calculate GSIB add-on
    for i in range(len(x)):
        gsib_addon += x[i] * gsib_cont[i]
    
    # Define constrain
    for i in range(len(x)):
        cet1_constraint += -((sRWA_mins[0] + gsib_addon) * s_rwa[i] * x[i]) + cet1_resource[i] * x[i]
        
    return cet1_constraint

def srwa_t1(x, df, sRWA_mins):
    '''
    Inequality constraint for Standardized RWA at the T1 level.
    Constraint states that there must be sufficient Equity + Prefs to cover a given percentage of total Standardized RWA.
    This function performs two calculations:
        - GSIB add-on. This is added to the base SRWA minimum for calculating the final inequality
        - SRWA inequality. Using the GSIB add-on and base SRWA minimum, ensure that there is sufficient equity + prefs 
        to cover the final SRWA minimum times total SRWA
    Inputs:
        - x: array of balances for all line items on the B/S. This number begins as X0 (starting B/S), but changes with each
             successive optimization iteration
        - df: original dataframe of the B/S inputs. Used to extract the SRWA weights for each line item plus the T1 resource weights
        - sRWA_mins: list of starting constraint minimums. The GSIB add-on is added on top of this to calculate the final minimum
    Outputs:
        - t1_constraint: the ending position of the inequality equation. Needs to be greater than or equal to 0 at all times.
    '''
    
    # Define GSIB add-on
    gsib_addon = 0
    gsib_cont = np.array(df['cet1_contr_per_balance'])
    
    # Define base RWA min
    s_rwa = np.array(df['s_rwa'])
    
    # Define what counts as a resource towards solving the constraint
    t1_resource = np.array(df['T1_resource'])
    
    # Define the constraint threshold. The inequality has to be greater than 0.
    t1_constraint = 0
    
    # Calculate GSIB add-on
    for i in range(len(x)):
        gsib_addon += x[i] * gsib_cont[i]
    
    # Define constrain
    for i in range(len(x)):
        t1_constraint += -((sRWA_mins[1] + gsib_addon) * s_rwa[i] * x[i]) + t1_resource[i] * x[i]
        
    return t1_constraint

def srwa_tc(x, df, sRWA_mins):
    '''
    Inequality constraint for Standardized RWA at the TC level.
    Constraint states that there must be sufficient Equity + Prefs + Sub Debt to cover a given percentage of total Standardized RWA.
    This function performs two calculations:
        - GSIB add-on. This is added to the base SRWA minimum for calculating the final inequality
        - SRWA inequality. Using the GSIB add-on and base SRWA minimum, ensure that there is sufficient equity + prefs + debt
        to cover the final SRWA minimum times total SRWA
    Inputs:
        - x: array of balances for all line items on the B/S. This number begins as X0 (starting B/S), but changes with each
             successive optimization iteration
        - df: original dataframe of the B/S inputs. Used to extract the SRWA weights for each line item plus the TC resource weights
        - sRWA_mins: list of starting constraint minimums. The GSIB add-on is added on top of this to calculate the final minimum
    Outputs:
        - tc_constraint: the ending position of the inequality equation. Needs to be greater than or equal to 0 at all times.
    '''

    # Define GSIB add-on
    gsib_addon = 0
    gsib_cont = np.array(df['cet1_contr_per_balance'])
    
    # Define base RWA min
    s_rwa = np.array(df['s_rwa'])
    
    # Define what counts as a resource towards solving the constraint
    tc_resource = np.array(df['total_capital_resource'])
    
    # Define the constraint threshold. The inequality has to be greater than 0.
    tc_constraint = 0
    
    # Calculate GSIB add-on
    for i in range(len(x)):
        gsib_addon += x[i] * gsib_cont[i]
    
    # Define constrain
    for i in range(len(x)):
        tc_constraint += -((sRWA_mins[2] + gsib_addon) * s_rwa[i] * x[i]) + tc_resource[i] * x[i]
        
    return tc_constraint


def srwa_tlac(x, df, sRWA_mins):
    '''
    Inequality constraint for Standardized RWA at the TLAC level.
    Constraint states that there must be sufficient Equity + Prefs + Sub + Senior Debt to cover a given percentage of total Standardized RWA.
    This function performs two calculations:
        - GSIB add-on. This is added to the base SRWA minimum for calculating the final inequality
        - SRWA inequality. Using the GSIB add-on and base SRWA minimum, ensure that there is sufficient equity + prefs + sub + senior debt
        to cover the final SRWA minimum times total SRWA
    Inputs:
        - x: array of balances for all line items on the B/S. This number begins as X0 (starting B/S), but changes with each
             successive optimization iteration
        - df: original dataframe of the B/S inputs. Used to extract the SRWA weights for each line item plus the TLAC resource weights
        - sRWA_mins: list of starting constraint minimums. The GSIB add-on is added on top of this to calculate the final minimum
    Outputs:
        - tlac_constraint: the ending position of the inequality equation. Needs to be greater than or equal to 0 at all times.
    '''

    # Define GSIB add-on
    gsib_addon = 0
    gsib_cont = np.array(df['cet1_contr_per_balance'])
    
    # Define base RWA min
    s_rwa = np.array(df['s_rwa'])
    
    # Define what counts as a resource towards solving the constraint
    tlac_resource = np.array(df['TLAC_resource'])
    
    # Define the constraint threshold. The inequality has to be greater than 0.
    tlac_constraint = 0
    
    # Calculate GSIB add-on
    for i in range(len(x)):
        gsib_addon += x[i] * gsib_cont[i]
    
    # Define constrain
    for i in range(len(x)):
        tlac_constraint += -((sRWA_mins[3] + gsib_addon) * s_rwa[i] * x[i]) + tlac_resource[i] * x[i]
        
    return tlac_constraint

def arwa_cet1(x, df, aRWA_mins):
    '''
    Inequality constraint for Advanced RWA at the CET1 level.
    Constraint states that there must be sufficient Equity to cover a given percentage of total Advanced RWA.
    This function performs two calculations:
        - GSIB add-on. This is added to the base ARWA minimum for calculating the final inequality
        - ARWA inequality. Using the GSIB add-on and base ARWA minimum, ensure that there is sufficient equity to cover the final
        ARWA minimum times total ARWA
    Inputs:
        - x: array of balances for all line items on the B/S. This number begins as X0 (starting B/S), but changes with each
             successive optimization iteration
        - df: original dataframe of the B/S inputs. Used to extract the ARWA weights for each line item plus the CET1 resource weights
        - aRWA_mins: list of starting constraint minimums. The GSIB add-on is added on top of this to calculate the final minimum
    Outputs:
        - cet1_constraint: the ending position of the inequality equation. Needs to be greater than or equal to 0 at all times.
    '''

    # Define GSIB add-on
    gsib_addon = 0
    gsib_cont = np.array(df['cet1_contr_per_balance'])
    
    # Define base RWA min
    a_rwa = np.array(df['a_rwa'])
    
    # Define what counts as a resource towards solving the constraint
    cet1_resource = np.array(df['CET1_resource'])
    
    # Define the constraint threshold. The inequality has to be greater than 0.
    cet1_constraint = 0
    
    # Calculate GSIB add-on
    for i in range(len(x)):
        gsib_addon += x[i] * gsib_cont[i]
    
    # Define constrain
    for i in range(len(x)):
        cet1_constraint += -((aRWA_mins[0] + gsib_addon) * a_rwa[i] * x[i]) + cet1_resource[i] * x[i]
        
    return cet1_constraint

def arwa_t1(x, df, aRWA_mins):
    '''
    Inequality constraint for Advanced RWA at the T1 level.
    Constraint states that there must be sufficient Equity + Prefs to cover a given percentage of total Advanced RWA.
    This function performs two calculations:
        - GSIB add-on. This is added to the base ARWA minimum for calculating the final inequality
        - ARWA inequality. Using the GSIB add-on and base ARWA minimum, ensure that there is sufficient equity + prefs 
        to cover the final ARWA minimum times total ARWA
    Inputs:
        - x: array of balances for all line items on the B/S. This number begins as X0 (starting B/S), but changes with each
             successive optimization iteration
        - df: original dataframe of the B/S inputs. Used to extract the ARWA weights for each line item plus the T1 resource weights
        - aRWA_mins: list of starting constraint minimums. The GSIB add-on is added on top of this to calculate the final minimum
    Outputs:
        - t1_constraint: the ending position of the inequality equation. Needs to be greater than or equal to 0 at all times.
    '''

    # Define GSIB add-on
    gsib_addon = 0
    gsib_cont = np.array(df['cet1_contr_per_balance'])
    
    # Define base RWA min
    a_rwa = np.array(df['a_rwa'])
    
    # Define what counts as a resource towards solving the constraint
    t1_resource = np.array(df['T1_resource'])
    
    # Define the constraint threshold. The inequality has to be greater than 0.
    t1_constraint = 0
    
    # Calculate GSIB add-on
    for i in range(len(x)):
        gsib_addon += x[i] * gsib_cont[i]
    
    # Define constrain
    for i in range(len(x)):
        t1_constraint += -((aRWA_mins[1] + gsib_addon) * a_rwa[i] * x[i]) + t1_resource[i] * x[i]
        
    return t1_constraint

def arwa_tc(x, df, aRWA_mins):
    '''
    Inequality constraint for Advanced RWA at the TC level.
    Constraint states that there must be sufficient Equity + Prefs + Sub Debt to cover a given percentage of total Advanced RWA.
    This function performs two calculations:
        - GSIB add-on. This is added to the base ARWA minimum for calculating the final inequality
        - ARWA inequality. Using the GSIB add-on and base ARWA minimum, ensure that there is sufficient equity + prefs + sub debt
        to cover the final ARWA minimum times total ARWA
    Inputs:
        - x: array of balances for all line items on the B/S. This number begins as X0 (starting B/S), but changes with each
             successive optimization iteration
        - df: original dataframe of the B/S inputs. Used to extract the ARWA weights for each line item plus the TC resource weights
        - aRWA_mins: list of starting constraint minimums. The GSIB add-on is added on top of this to calculate the final minimum
    Outputs:
        - tc_constraint: the ending position of the inequality equation. Needs to be greater than or equal to 0 at all times.
    '''

    # Define GSIB add-on
    gsib_addon = 0
    gsib_cont = np.array(df['cet1_contr_per_balance'])
    
    # Define base RWA min
    a_rwa = np.array(df['a_rwa'])
    
    # Define what counts as a resource towards solving the constraint
    tc_resource = np.array(df['total_capital_resource'])
    
    # Define the constraint threshold. The inequality has to be greater than 0.
    tc_constraint = 0
    
    # Calculate GSIB add-on
    for i in range(len(x)):
        gsib_addon += x[i] * gsib_cont[i]
    
    # Define constrain
    for i in range(len(x)):
        tc_constraint += -((aRWA_mins[2] + gsib_addon) * a_rwa[i] * x[i]) + tc_resource[i] * x[i]
        
    return tc_constraint

def arwa_tlac(x, df, aRWA_mins):
    '''
    Inequality constraint for Advanced RWA at the TLAC level.
    Constraint states that there must be sufficient Equity + Prefs + Sub + Senior debt to cover a given percentage of total Advanced RWA.
    This function performs two calculations:
        - GSIB add-on. This is added to the base ARWA minimum for calculating the final inequality
        - ARWA inequality. Using the GSIB add-on and base ARWA minimum, ensure that there is sufficient equity + prefs + sub + senior debt
        to cover the final ARWA minimum times total ARWA
    Inputs:
        - x: array of balances for all line items on the B/S. This number begins as X0 (starting B/S), but changes with each
             successive optimization iteration
        - df: original dataframe of the B/S inputs. Used to extract the ARWA weights for each line item plus the TLAC resource weights
        - aRWA_mins: list of starting constraint minimums. The GSIB add-on is added on top of this to calculate the final minimum
    Outputs:
        - tlac_constraint: the ending position of the inequality equation. Needs to be greater than or equal to 0 at all times.
    '''

    # Define GSIB add-on
    gsib_addon = 0
    gsib_cont = np.array(df['cet1_contr_per_balance'])
    
    # Define base RWA min
    a_rwa = np.array(df['a_rwa'])
    
    # Define what counts as a resource towards solving the constraint
    tlac_resource = np.array(df['TLAC_resource'])
    
    # Define the constraint threshold. The inequality has to be greater than 0.
    tlac_constraint = 0
    
    # Calculate GSIB add-on
    for i in range(len(x)):
        gsib_addon += x[i] * gsib_cont[i]
    
    # Define constrain
    for i in range(len(x)):
        tlac_constraint += -((aRWA_mins[3] + gsib_addon) * a_rwa[i] * x[i]) + tlac_resource[i] * x[i]
        
    return tlac_constraint


def lev_cet1(x, df, lev_mins):
    '''
    Inequality constraint for Leverage at the CET1 level.
    Constraint states that there must be sufficient Equity to cover a given percentage of total leverage.
    This function performs one calculations:
        - Leverage inequality. Using the leverage minimum requirement, ensure that there is sufficient equity
        to cover the leverage minimum times total leverage
    Inputs:
        - x: array of balances for all line items on the B/S. This number begins as X0 (starting B/S), but changes with each
             successive optimization iteration
        - df: original dataframe of the B/S inputs. Used to extract the ARWA weights for each line item plus the CET1 resource weights
        - lev_mins: list of starting constraint minimums. The GSIB add-on is added on top of this to calculate the final minimum
    Outputs:
        - cet1_constraint: the ending position of the inequality equation. Needs to be greater than or equal to 0 at all times.
    '''
    
    # Define base leverage contribution
    b1_lev = np.array(df['b1_leverage'])
    
    # Define what counts as a resource towards solving the constraint
    cet1_resource = np.array(df['CET1_resource'])
    
    # Define the constraint threshold. The inequality has to be greater than 0.
    cet1_constraint = 0
    
    # Define constrain
    for i in range(len(x)):
        cet1_constraint += -(lev_mins[0] * b1_lev[i] * x[i]) + cet1_resource[i] * x[i]
        
    return cet1_constraint

def lev_t1(x, df, lev_mins):
    '''
    Inequality constraint for Leverage at the T1 level.
    Constraint states that there must be sufficient Equity + Prefs to cover a given percentage of total leverage.
    This function performs one calculations:
        - Leverage inequality. Using the leverage minimum requirement, ensure that there is sufficient equity + prefs
        to cover the leverage minimum times total leverage
    Inputs:
        - x: array of balances for all line items on the B/S. This number begins as X0 (starting B/S), but changes with each
             successive optimization iteration
        - df: original dataframe of the B/S inputs. Used to extract the ARWA weights for each line item plus the T1 resource weights
        - lev_mins: list of starting constraint minimums. The GSIB add-on is added on top of this to calculate the final minimum
    Outputs:
        - t1_constraint: the ending position of the inequality equation. Needs to be greater than or equal to 0 at all times.
    '''
    
    # Define base leverage contribution
    b1_lev = np.array(df['b1_leverage'])
    
    # Define what counts as a resource towards solving the constraint
    t1_resource = np.array(df['T1_resource'])
    
    # Define the constraint threshold. The inequality has to be greater than 0.
    t1_constraint = 0
    
    # Define constrain
    for i in range(len(x)):
        t1_constraint += -(lev_mins[1] * b1_lev[i] * x[i]) + t1_resource[i] * x[i]
        
    return t1_constraint