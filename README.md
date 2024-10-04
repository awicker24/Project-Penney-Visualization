# Penney’s Game Heatmap Visualization

This project creates a set of heatmaps visualizing the simulation of Penney's Game. 

## Files

We need to add this section after cleaning up the github

## Functions

**master_heatmap_function()** takes in the argument `format_type`, specified as ‘html’, ‘png’, or ‘both’, which allows the user to choose whether the heatmap is saved as an html, png, or both. It outputs heatmaps showing the win percentage of one player in the Penney’s Game based on which sequence each player chooses. **master_heatmap_function()** is the only function exposed to the user, but it calls the function **create_heatmap()** to generate the visualizations as well as the functions **save_heatmap_as_html()** and **save_heatmap_as_png()** to save the heatmaps based on the specified format type.

**create_heatmap()** takes in the argument `array_file`, specified as the file './data/variation1_array.npy' by the master_heatmap_function. It outputs an interactive plotly graph object heatmap.

**save_heatmap_as_html()** and **save_heatmap_as_png()** both take the same arguments. `fig` is the figure generated by the create_heatmap() function, and `variation` is either 1 (scoring based on number of cards) or 2 (scoring based on number of tricks). **master_heatmap_function()** will run the specified function twice, inputting variation 1 the first time and variation 2 the second time. **save_heatmap_as_html()** and **save_heatmap_as_png()** save the heatmaps to the path figures/heatmap_variation_{str(variation)}.

## Graph Specifications

- Inputted colorscale is ‘blues’, a single color gradient which ranges from white (low win ratios) to dark blue (high win ratios)
- Win percentages are displayed as whole numbers between 0 and 100. Percentage signs are shown on the color scale
- Figure size is 600x600
- Title is set as ‘Penney Game, Player Two Win Percentage<br> (Total Non-Tie Games, Approx: {total_iterations})’. Title font size is 20
- 0 stands for black cards while 1 stands for red cards. 
- The heatmap is an 8x8 array with labels set as x = ['RRR', 'RRB', 'RBR', 'RBB', 'BRR', 'BRB', 'BBR', 'BBB'] and y = ['RRR', 'RRB', 'RBR', 'RBB', 'BRR', 'BRB', 'BBR', 'BBB']
- The “nonsense games” where two of the same sequences are played against each other create an empty diagonal which runs from the bottom left to the top right. This diagonal is white with no numbers listed

## Collaborators

Andrew Choi<br>
Arianna DeBoer<br>
Zoe Cummings<br>
Annie Wicker

