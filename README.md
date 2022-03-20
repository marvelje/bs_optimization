# BS Optimization

## Summary

This analysis solves a constrained resource allocation problem with a sample bank balance sheet using Scipy's Minimize library. The goal is to maximize the profitability of the B/S subject to several constraints and upper/lower bounds.

## Background

Bank resource management has become significantly more complex in the last decade. After the 2008 financial crisis, a slew of new regulatory frameworks were enacted, complicating balance sheet management. It was no longer immediately obvious which products were more profitable or what the optimal balance sheet mix was for a given "type" of bank (i.e., Universal vs. Investment vs. Retail bank, etc).

## Balance Sheet Overview

Sample data can be found here: https://github.com/marvelje/bs_optimization/tree/main/data

- For purposes of this analysis, I've created a fake bank balance sheet of ~40 line items. I've relied on my experience at a big bank to construct a reasonably realistic scenario for a "universal" bank (i.e., a bank offering a full suite of banking services across retail, commercial, and markets). Many of these line items will look familiar to anyone who's worked in finance. You'll notice auto loans, various types of mortgage products, commercial lending, markets, and a whole suite of deposit products.
- For any optimization to have meaningful results, the line items should be broken down in a way where the bundled products have similar levels of profitability and "resource footprints" (more on this last bit under the Constraints Overview). The more aggregated the data, the less useful it becomes. Therefore, I've broken down a given product category where a subgroup has meaningfully different characteristics. For example, I broke Auto lending down between "Prime" and "Subprime" since the returns and resource footprint is materially different.
- I then created spreads (profitability expressed in basis points, or bps), along with upper and lower bounds. I.e., how much will I allow the products to grow and shrink during the optimization.
- To start, I generated somewhat arbitrary numbers, ensuring only that Assets = Liabilities and the constraints are currently satisfied

## Constraints

This analysis consider a simplified framework of the capital / resource constraints that banks currently face
- Risk weighted assets:
    - This framework turns a given balance into a Risk Weight equivalent. For example, a mortgage loan may have a Standardized RWA of 50%. This means that a 100 dollar mortgage will generate Standardized RWA of 50.
    - The regulation states that the bank must have equity equal to a fixed % of it's Risk Weighted Assets.
    - There are two RWA frameworks: Advanced and Standardized. A given product may have two different weights across each of these frameworks
- GSIB:
    - This is not a standalone constraint, but rather adds to the RWA minimums described above.
    - For example, the RWA minimum may be 8% plus a GSIB surchage. This surcharge is initially 3% in my optimization. The GSIB surcharge scales up or down with changes to the balance sheet, with some products contributing more to the GSIB surcharge than others.
    - In reality, this is a "stair-step" framework. The GSIB surcharge moves in increments of 0.5% A given score may place you in the 3% "bucket" until you hit the subsequent threshold, bumping you up to 3.5%. To keep this a linear problem, I removed this stair step and interpolated the GSIB contribution. In othe words, a small increase in balances may make the surcharge 3.05%, when in reality we would've stayed in the 3% bucket. This also makes the problem non-linear as the ineuqality constraint depends on the balances themselves.
- Leverage:
    - This works similarly to RWA, but is a bit more straightforward. For example, the leverage requirement for CET1 states that you must have enough Equity to cover at least a fied % of the total assets. There is no intermediate step of calculating the GSIB add-on.

## Modeling

The optimization includes 10 inequality constraints (pertaining to regulatory capital) and 1 equality constraint (assets must equal liabilities). Eight of the 10 inequality constraints are non-linear given that the coefficient of the constraint is partly dependent on the balances in the optimization (for those with a banking background, I've linearized the GSIB contribution to add to the constraint).

Given this landscape of constriants, I used Scipy's minimize instead of alternative libraries such as linprog.

## Results

Optimization resulted in a balance sheet that was 38% more profitable than baseline. The most binding constraint overall was Standardized RWA. At the T1 level, however, Leverage was more binding. Putting aside the resource stack, the optimization grew / shrunk all balances up to capacity with the exception of Business Loan - Revolver, which is the "marginal product" of the optimization. 

## Next Steps

After the successful optimization, I want to do a prioritization analysis, and introduce new hypothetical products to show what would happen under a variety of growth scenarios.
