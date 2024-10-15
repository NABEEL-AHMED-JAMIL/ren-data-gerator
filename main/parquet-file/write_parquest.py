import pandas as pd

# Create a sample DataFrame
data = {
    'Captain': ['James T. Kirk', 'Jean-Luc Picard', 'Benjamin Sisko', 'Kathryn Janeway', 'Jonathan Archer', 'William T. Riker', 'Edward Jellico'],
    'Actor': ['William Shatner', 'Patrick Stewart', 'Avery Brooks', 'Kate Mulgrew', 'Scott Bakula', 'Jonathan Frakes', 'Ronny Cox'],
    'Ship': ['USS Enterprise', 'USS Enterprise-D', 'Deep Space 9', 'USS Voyager', 'Enterprise NX-01', 'USS Titan', 'USS Enterprise-D'],
    'Quote': ['Beam me up, Scotty!', 'Make it so.', "It's a faaaaake!", "There's coffee in that nebula.", "We're not out here to play God.", 'I love surprise parties.', 'Get it done.']
}

# dataframe
df = pd.DataFrame(data)
# write dataframe to parquest file
df.to_parquet('example.parquet', index=False)

print("Parquet written to 'example.parquet'.")