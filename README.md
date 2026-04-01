# loot-drop-simulator
A loot drop CLI app that runs simulations and displays the rate at which items were dropped with a formatted bar graph (useful for RNG games).

## Features
- Input base drop rate, number of simulations, and luck boosts.
- Outputs a detailed analysis of loot drop rates, including ratios and average rolls.
- Generates three clean bar graphs that show Expected, Boosted, and Actual Luck Ratios.
- Personalized lucky/unlucky outputs.

## Requirements
- Python 3
- colorama

## Installation
```
pip install colorama
```

## Usage
Run the command in your terminal:
```
python loot_drop_sim.py
```

Then follow the prompts:
Enter drop rate % -> (eg. 5 for 5%)
Enter number of simulations -> 100000
Enter luck boost % [enter 0 if no luck boost] -> (eg. 5 for 5%)

Once you are satisfied with your data:
Would you like run a new simulation? [yes/no] -> no

## Example Output
```
========== DROP RATE SIMULATOR ==========
Enter drop rate % -> 5
Enter number of simulations -> 100000
Enter luck boost % [enter 0 if no luck boost] -> 5
Drop Rate: 5.0% | Number of Simulations: 100000
You opened 100000 times and got 10009 drops! That is a ratio of 10.01%!
You applied a luck boost of 5.00%
On average, it took about 9.99 rolls to get a drop.
You were lucky and had a higher rate of success than the original drop rate!
---Drop Rate Table---
Expected:    5.00 |██████████░░░░░░░░░░
Boosted:    10.00 |████████████████████
Actual:     10.01 |████████████████████
Would you like run a new simulation? [yes/no] -> no
========== DROP RATE SIMULATOR ==========
```

## Notes
- Performance may degrade at higher simulation counts (10M+)
- Luck boosts added to base rates are capped at 100.

## What This Taught Me
- GitHub Repository Creation
- Simulating data
- Furthered OOP Foundation
- Using random to simulate randomized data
- Generating formatted statistics
- Generating bar graphs
