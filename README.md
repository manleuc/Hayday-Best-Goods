# Hayday best goods calculator
This program will tell you the top goods to produce for each production building at your level to maximize the revenue when sold in the roadside shop. It can be used to calculate the goods to produce that will maximize xp when collected. 
## Getting Started
1. Download (or clone) the repository.
2. Ensure that Python version 3.7+ is downloaded. Here is the [link](https://www.python.org/downloads/).
3. Open the file location of the downloaded repository, right click **Hayday-Best-Goods** folder, and select **Open in Terminal**.
4. After your terminal opens run the command ```python hayday_best.py [level]```

## How To Use
The python script, hayday_best.py, accepts one input which is your current hayday level. It will defaultly calculate the top 3 goods to produce based on their max revenue value in the RSS for each production building. 

Other flags are included for various other use cases such as best goods to produce to maximize XP and factoring the time it takes to produce a good. 

Here are some potential use cases: 
- Prints the 3 best goods to produce for level 37 for each production building that maximizes revenue in RSS:
    
    ```python hayday_best.py 37```

- If you want to find the best goods to maximize XP, use the ```-xp``` or ```--xp``` flag

    The following will find the best goods the produce to maximize xp for level 78: 
    
    ```python hayday_best.py 78 -xp```
- If you want to take into consideration the time it takes to produce goods use the ```-t``` or ```--time``` flag. Use this option if you are a more active player that checks there farm often: 
    This will print the 3 top goods that will maximize the number of coins/hour you can make if sold in RSS.

    ```python hayday_best.py [level] -t```

    The time flag can be used in combination with the xp flag. The following will maximize the xp produced per hour 

    ```python hayday_best.py [level] -t -xp```

- You can also change the number of items you print out per production building using the ```-n``` or ```--num_goods``` flag (defaultly it will print 3 goods per production building): ```python hayday_best.py [level] -n [number_of_items]```


### Help command
To get a list of all flags and their use cases, run the following help command: 

```python hayday_best.py -h``` 


### Note: Feed Mill, Dairy, and Sugar Mill Production 
Feed Mill, Dairy and Sugar goods are ignored by default since these goods are often used to produce more expensive goods. If you wish to print the Dairy and Sugar Mill production info use the ```-ds``` flag: 

```python hayday_best.py [level] -ds```

### Text file
You can also generate the list as a text file for ease of access. Use the `-txt` or `--text` flag. This will generate a .txt file called bestgoods.txt, where you can view the complete list of best goods to produce for your specified level.

```python hayday_best.py [level] -txt```
