from leetify_data_scrape import *


def create_stats_table(stats):
    """Creates the stats table."""
    # Removes unneeded data and creates sublists of each data point.
    del stats[1:3]
    stats_lst = []
    for i in range(0, len(stats)-5):
        if stats[i] in ["AIM", "UTILITY", "POSITIONING", "OPENING DUELS", "CLUTCHING",
                        "WIN RATE", "LEETIFY RATING", "T RATING", "CT RATING"]:
            stats_lst.append(stats[i:i+2])
        elif stats[i] in ["SOLO", "2-4 STACK", "5 STACK"]:
            del stats[i:i+2]
    # Creates dataframe and returns in markdown.
    stats_table = pd.DataFrame(stats_lst, columns=["Overview", "Score"])
    stats_table["Score"] = pd.to_numeric(stats_table["Score"], errors="coerce")
    return stats_table.to_markdown(index=False)


def create_match_history_table(match_history):
    """Creates the match history table."""
    history_lst = []
    # Grabs the table headers.
    match_history_headers = [match_history.pop(0) for i in range(0, 10)]
    # Removes unneeded headers,
    for i in match_history_headers:
        if i in ["Match History", "Rank", "Source"]:
            match_history_headers.remove(i)
    print(match_history_headers)

    # Chops the list into sublist for each match.
    for i in range(0, len(match_history), 3):
        history_lst.append(match_history[i:i + 3])
    # Splits match sublist to obtain correct stats and then merges back together.
    for i in range(0, len(history_lst)):
        history_lst[i][1] = history_lst[i][1].split(" ", 1)
        history_lst[i][2] = history_lst[i][2].split(" ")
        history_lst[i] = list(chain(history_lst[i], history_lst[i][1], history_lst[i][2]))
        del history_lst[i][1:3]

    # Creates data frame with headers then returns in markdown.
    match_history_table = pd.DataFrame(history_lst, columns=match_history_headers)
    return match_history_table.to_markdown(index=False)