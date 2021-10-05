# Patent claim combination

## Example

Let us take the following example of patent claims:

- claim 1
- claim 2
-- depending on claim 1
- claim 3
-- depending on claim 1 and 2
- claim 4
-- depending on claim 1
- claim 5
-- depending on claim 2
- claim 6
-- depending on claim 1 to 5
- claim 7
-- depending on claim 2 and 5
- claim 8
-- depending on claim 3 and 4

where claim 2 to 8 are subclaims of claim 1.

How many combinations of claims (and their features) are possible?

Solution:
- combination 1:  claim 1
- combination 2:  claim 1 + claim 2
- combination 3:  claim 1 + claim 2 + claim 3
- combination 4:  claim 1 + claim 3
- combination 5:  claim 1 + claim 4
- combination 6:  claim 1 + claim 2 + claim 5
- combination 7:  claim 1 + claim 6
- combination 8:  claim 1 + claim 2 + claim 6
- combination 9:  claim 1 + claim 3 + claim 6
- combination 10: claim 1 + claim 2 + claim 3 + claim 6
- combination 11: claim 1 + claim 4 + claim 6
- combination 12: claim 1 + claim 2 + claim 5 + claim 6
- combination 13: claim 1 + claim 2 + claim 7
- combination 14: claim 1 + claim 2 + claim 5 + claim 7
- combination 15: claim 1 + claim 2 + claim 3 + claim 8
- combination 16: claim 1 + claim 3 + claim 8
- combination 17: claim 1 + claim 4 + claim 8

There are 17 combinations.

## Aim

The aim of this script is to compute the number of combinations based on the list of claims.

## Coding

Let us take a look again at the example above.

Following lines define the dependency of the claims:

<code>claim = [[1], [1], [1,2], [1], [2], [1,2,3,4,5], [2,5], [3,4]]</code> 

Claim 1 ("[1]") only depends on itself. Claim 2 ("[1]") depends on claim 1. Claim 3 ("[1,2]") depends on claim 1 and 2. And so on.


Put this in the function "dependency_check()":

<code>num_combinations(claim)</code> 

Output:

<code>Total combinations: 17</code> 

