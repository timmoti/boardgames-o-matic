# 3 become 1
_21 September 2017. 5 mins read_

<img src="/assets/Snacks-and-Ladders.jpg" width="800">

I'm a simple man. 

I love food, games, and data. 

I'm also quite obsessed with data collection.  Every single dollar that leaves my wallet or my bank account is tracked. I rate each dish I eat and record every single boardgame session I play. 

In recent years, my obsession with data has extended to my firm belief that taste is subjective and the idea that people, in general, have more likes and dislikes in common with some than others. This led to my discovery of the wonderful world of recommendation systems which will thus be the main area of focus for my Capstone.

I have come up with 3 ideas for the project which will be presented in order of difficulty(hardest first) and with hardly any surprise, they revolve around my loves.

### Singapore Food Critic Analysis

<img src='/assets/308-food-revival-body03-rect.jpg' width="800">

Singapore is a food haven. We are fortunate to be living in this city-state where the variety of cuisines and dishes can sometimes induce analysis paralysis. With so many food choices, some people have taken the task of informing the world, through the World Wide Web, their thoughts on restaurants they've visited and dishes they've tried. These food bloggers, as they're better known, can have such a hold on what we decide to eat that searches for a particular restaurant will inevitably link us to their blog page.

Unfortunately, more often than not, the food they recommend do not tickle our taste buds. It could be due to the fact that some of them are paid for their review. I would hazard a guess however that they have a different taste profile from you.

This project idea will partially solve this issue by examining which local food bloggers have the highest similarity in taste to you so that you might be able to trust their recommendations.

I have identified 47 food bloggers with sufficient clout in Singapore to analyze although, in order to build a dataset, some scraping will have to be done. Their blog posts will be scraped thoroughly to extract the restaurant name, dishes they've tried, their review of the dishes and a score for the dish if present.

Natural Language Processing (NLP) and Sentiment Analysis will then have to be conducted on these reviews and converted to a score representing their likes and dislikes.

With only 47 users in the dataset, and potentially an item space in the thousands, I have the intention to conduct item-item collaborative filtering and possibly attempt to categorize clusters of items found.

An analysis of how the bloggers rate their dishes could also be performed to glean some insights into their specific taste profile.

The end product would be a web form for the end user to key in their likes and dislikes of at least 30 dishes from our dataset where the top 5 food bloggers with the most similar taste to the user will be returned in the form of percentages.

The dataset to be produced will be limited to only dishes from restaurants, cafes, hawkers, and coffee shops. Drinks will be omitted.

### Yelp Recommendation Analysis

<img src = "/assets/Yelp_Logo.svg.png" width="800">

From one food-related project to another, this one focuses on a contemporary Yelp dataset. Released as part of an ongoing data analytics challenge, this dataset contains over 4 million reviews with the latest being as recent as July 2017. It is with this discovery that I proceeded to formulate my second food recommendation system-related project.

The Yelp dataset contains ratings from more than 1.1 million users on a wide range of categories from restaurants to pet groomers. With this treasure trove of information, a potential question that can be answered through recommendation analysis is the age-old one of where to go to eat and what to eat when there? 

I believe that constructing a recommender system based solely on the dishes is a novel attempt that will be worth attempting for the potential benefits it can provide to the end user. 

While there is only a single rating in a review for a restaurant, some users do mention some dishes in their accompanying write-up, as well as in separate short form text entries called tips. In order for the recommendation system to be focused solely on the dishes, NLP will have to be performed to extract the relevant entries and have their sentiment analyzed for scoring.

Cluster analysis can be conducted to ascertain groups of similar taste and whether they are distinct enough to form unique taste profiles. This will be one of the 2 metrics to determine project success.

Unlike the data frame in the SG food critic project, there will likely be many more users, possibly in the thousands, resulting in a matrix that is long as it is wide. A key challenge will be in managing the sparsity of rating data in this giant user-item matrix.

Ultimately, the main goal of this project is to generate a recommendation accuracy of at least 80%. Different data partitioning techniques will be experimented on here in order to achieve a sensible result.

Finally, as the data is only U.S based, there is considerably limited usage for a recommendation result here in Singapore. 

Unless you're planning a trip to America in the near future that is.

### Board Game Recommender System

<img src="/assets/board_game_shelf_shelves_analog_games_01-2.jpg" width="800">

The board game industry is a burgeoning one. 

According to boardgamegeek.com (BGG), widely regarded as the premier board game resource in the world, there are currently 14,255 ranked games (as of 20 September 2017) in the database. This, however, does not include unranked games which only get on the leaderboard with a minimum of 30 ratings. With 879 ranked games released in 2016 (probably more with unranked games included), the problem seems crystal clear.

With so many games and so little time, how does one decide what games to buy or even try?

An accurate recommender system could help with this issue and as the avid board game geek that I am, this brings me to the third project idea for my capstone.

The potential users of such a recommender system are huge. There are 782,281 registered users on BGG as of 2013 and reported 140K active monthly users. Users are able to rate games on a 10-point scale with a suggested scoring rubric based on how likely they are to play the game again. All user data is public and easily accessible on the website. Methods for extraction include downloading in CSV format (although it is on an individual basis) or an XML API. There is also a python library of the same name that makes accessing the API considerably easy for data research purposes.

The user-rating space is more defined here as board games, much like movies and songs, are unique entertainment products and thus some games will be more popular with a lot more ratings than others. Sparsity will be a challenge here as well and user-item selection, as well as performing suitable dimensionality reduction techniques here will be key to overcoming it.

While unlike the Yelp dataset, where NLP techniques are not needed since ratings are clear and defined, there is a high chance of rogue raters appearing that will need to be identified. Reviews in the Yelp dataset have been scanned and allowed through their company filters, in a category the company call Recommended Reviews. Ratings in the BGG database are unmonitored and unsupervised. Another challenge with this project will thus be to identify these raters and exclude them from the analysis.

In the end, we are aiming for a recommendation accuracy of at least 80% as well and the possibility of finding distinct clusters of gamers with similar taste in board games.

### Recommender Systems for the win

One thing these 3 projects have in common is the requirement for techniques available in the world of recommendation systems, of which I am really passionate about. I hope to be able to gain significant insights from this capstone and possibly develop a system that is at least worth its weight in gold.

All of these raise one last question though.

Which project would you recommend?

