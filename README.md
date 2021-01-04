# Optimization-code
Command line tool to solve LP Problems using PuLP. 

Install the requirements with ```pip3 install -r requirements.txt```

Run the main script to interactively feed in the problem statement. The output is shown in the terminal itself.
```
$ python3 LPModel.py
```

In order, the inputs requested will be:
- Select the type of optimization (max/min)
- Number of decision variables
- Number of constraints (excluding nonnegative)
- Enter variable names
- Enter the objective function
- Enter constraints (one by one)

## To do
List of issues and possibilites that would make this more convenient. I might implement this if I have time, but pull requests are welcome.
- Running the solver from a problem file (yaml)
- Optionally write results to user defined text file
- Command line argparser to choose between modes
- Add option to change type of variables (integer, non integer, bounded etc)
- Fix variable naming problem
- Add an option to find (and optionally output) the vertices of the solution space. In case of two/three variable LPP's, this can be graphical.