def create_heatmap(array, variation):
    '''
    This function takes in an 8x8 array and makes a heatmap using plotly.go. The heatmap displays the win ratios for the 
    2nd player, who will choose their pattern based on what the 1st player chose. The heatmap is scaled so that percentages 
    under 0.5 show up orange while those over 0.5 are green, with the midpoint 0.5 being yellow. The top left to bottom
    right diagonal should be None values which will show up grey, since these are matches that wouldn't occur (ex. RRR v RRR).
    From top down (and right to left), the order of the sequences is 'RRR', 'RRB', 'RBR', 'RBB', 'BRR', 'BRB', 'BBR', 'BBB'.

    Parameters: 
    array: an 8x8 array with numbers between 0 and 1 representing the percentage of games that payer 2 won
    '''

    array[0,0] = None  # this avoids the listing of "nonsense" games (ex. RRR vs RRR) as a percentage
    array[1,1] = None
    array[2,2] = None
    array[3,3] = None
    array[4,4] = None
    array[5,5] = None
    array[6,6] = None
    array[7,7] = None

    variation_name = ' ' # provides more information for the visualization
    if variation == 1:
        variation_name = ' cards'
    else:
        variation_name = ' tricks'
    
    fig = go.Figure(data = go.Heatmap(
                   z = array, colorscale = 'Fall_r', # 'RdYlGn' or 'RdBu' or 'Oranges' or 'Fall_r'
                   hovertemplate = "%{y}:%{x} win ratio <br />%{z}", name = "", # the name part stops 'trace=0' from popping up
                   text=array, texttemplate='%{text:.2f}',  
                   x = ['RRR', 'RRB', 'RBR', 'RBB', 'BRR', 'BRB', 'BBR', 'BBB'],
                   y = ['RRR', 'RRB', 'RBR', 'RBB', 'BRR', 'BRB', 'BBR', 'BBB'],
                   hoverongaps = False))
    fig.update_layout(
        title = f'Penney Game, variation {str(variation)}: Player Two Win Ratio for{variation_name}',  #this is the percentage of games that player 2 wins
        title_x = 0.5,
        title_y = 0.9,
        title_font_size = 20,
        xaxis = dict(
            title = 'Player Two Choice'  
        ),
        yaxis = dict(
            title = 'Player One Choice'
        ),
        width = 600,
        height = 600
        )
    fig.update_traces(
        xgap = 1, ygap = 1
        )

    fig.show()
    path = f"figures/heatmap_variation_{str(variation)}.html"
    fig.write_html(path)
    return None
