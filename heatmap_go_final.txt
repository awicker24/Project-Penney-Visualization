
def create_heatmap(array_file):  
    '''
    This function takes in an 8x8 array and makes a heatmap using plotly.go. The heatmap displays the win ratios for the 
    2nd player, who will choose their pattern based on what the 1st player chose. The heatmap is scaled so that percentages 
    under 0.5 show up orange while those over 0.5 are green, with the midpoint 0.5 being yellow. The top left to bottom
    right diagonal should be None values which will show up grey, since these are matches that wouldn't occur (ex. RRR v RRR).
    From top down (and right to left), the order of the sequences is 'RRR', 'RRB', 'RBR', 'RBB', 'BRR', 'BRB', 'BBR', 'BBB'.

    Parameters: 
    array: an 8x8 array with numbers between 0 and 1 representing the percentage of games that player 2 won
    variation: whether scored by cards (variation = 1) or tricks (variation = 2)
    format: whether files should be saved as htmls (format = 'html') or pngs (format = 'png')
    '''

    array = np.load(array_file, allow_pickle=True)

    data_folder = './data'  
    files = [file for file in os.listdir(data_folder) if os.path.isfile(os.path.join(data_folder, file)) and file.endswith('.npy')]   # gets all the npy files right

    games_total = None

    for file in files:   # loading each of the game 
        file_path = os.path.join(data_folder, file)
        game_data = np.load(file_path, allow_pickle=True)  
        if games_total is None:
            games_total = game_data 
        else:
            games_total += game_data  

    total_iterations = len(files)   # THIS IS IMPORTANT / THIS GIVES TOTAL GAMES
    # win_ratios = games_total / total_iterations - we don't need this cause we do array * 100

    # win_ratios_percentage = win_ratios * 100
    
    # array[0,0] = None  # this avoids the listing of "nonsense" games (ex. RRR vs RRR) as a percentage
    # array[1,1] = None
    # array[2,2] = None
    # array[3,3] = None
    # array[4,4] = None
    # array[5,5] = None
    # array[6,6] = None
    # array[7,7] = None
    np.fill_diagonal(array, np.nan)


    # variation_name = ' ' # provides more information for the visualization
    # if variation == 1:
    #     variation_name = ' cards'
    # else:
    #     variation_name = ' tricks'
    
    fig = go.Figure(data = go.Heatmap(
                   z = array, colorscale = 'blues', # 'RdYlGn' or 'RdBu' or 'Oranges' or 'Fall_r'
                   hovertemplate = "%{y}:%{x} win ratio <br />%{z}", name = "", # the name part stops 'trace=0' from popping up
                   text=np.nan_to_num(array) * 100, texttemplate='%{text:.0f}',  
                   x = ['RRR', 'RRB', 'RBR', 'RBB', 'BRR', 'BRB', 'BBR', 'BBB'],
                   y = ['RRR', 'RRB', 'RBR', 'RBB', 'BRR', 'BRB', 'BBR', 'BBB'],
                   hoverongaps = False,
                   colorbar=dict(
                        tickformat=".0%"
                   )))
    
    fig.update_layout(
        
        title=f'Penney Game, Player Two Win Percentage<br> (Total Non-Tie Games, Approx: {total_iterations})',
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

    # fig.show()

    # if format == 'html':
    #     fig.show()
    #     path_html = f"figures/heatmap_variation_{str(variation)}.html"
    #     fig.write_html(path_html)
    # elif format == 'png': 
    #     path_png = f"figures/heatmap_variation_{str(variation)}.png"
    #     fig.write_image(path_png)
    # else:
    #     print('format not supported')
    
    return fig


def save_heatmap_as_html(fig, variation):
    path_html = f"figures/heatmap_variation_{str(variation)}.html"
    fig.write_html(path_html)
    print(f"Heatmap saved as HTML: {path_html}")


def save_heatmap_as_png(fig, variation):
    fig.update_layout(
        width=600,  
        height=600,  
        margin=dict(l=40, r=40, t=120, b=40),  # this helps with separating title with matrix
        title_font_size=18,  
    )
    
    path_png = f"figures/heatmap_variation_{str(variation)}.png"
    fig.write_image(path_png)
    print(f"Heatmap saved as PNG: {path_png}")

def master_heatmap_function(format_type):
    # Variation 1
    fig1 = create_heatmap(array_file='./data/variation1_array.npy')   # assuming the name of the array is variation1_array.npy
    
    # Variation 2
    fig2 = create_heatmap(array_file='./data/variation2_array.npy')   # assuming the name of the array is variation2_array.npy

    if format_type == 'html':
        save_heatmap_as_html(fig1, 'heatmap_variation_1')
        save_heatmap_as_html(fig2, 'heatmap_variation_2')
    elif format_type == 'png':
        save_heatmap_as_png(fig1, 'heatmap_variation_1')
        save_heatmap_as_png(fig2, 'heatmap_variation_2')
    elif format_type == 'both':
        save_heatmap_as_html(fig1, 'heatmap_variation_1')
        save_heatmap_as_png(fig1, 'heatmap_variation_1')
        save_heatmap_as_html(fig2, 'heatmap_variation_2')
        save_heatmap_as_png(fig2, 'heatmap_variation_2')
    else:
        print(f"Unsupported format type: {format_type}")


# use master_heatmap_function(format_type='both') as a test
