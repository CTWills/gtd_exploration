"""
Functions that help with retrieving data and plotting
"""
import matplotlib.pyplot as plt


def get_terrorist_groups(df, amount, start=None, stop=None):
    """
        Retrieves the top amount of groups between the start and stop
        time period

        Parameters:
            df (pandas.core.frame.DataFrame): Dataframe to search through
            amount (int): How many groups to return
            start (int): Start year of timeframe. Defaults to min value of dataset
            stop (int): Stop year of timeframe. Defaults to max value of dataset

        Returns:
            Panda Series of top amount of groups with how many attacks each did
    """
    groups_result = None
    if start is None:
        query = (df["doubtterr"] == 0) | (df["doubtterr"] == -9)
    else:
        query = (df["year"] >= start) & (
            (df["doubtterr"] == 0) | (df["doubtterr"] == -9))
    groups_result = df[query].groupby(
        "gname").size().sort_values(ascending=False).iloc[:amount]
    return groups_result


def create_bar_plot(df, title=None, ylabel=None, xlabel=None, name="Bar"):
    """
        Creates a bar graph from df and saves image to img folder

        Parameters:
            df (pandas.core.frame.DataFrame): Dataframe to plot
            title (str): Title of graph
            ylabel (str): Label for y axis
            xlabel (str): Label for x axis

        Returns:
            None
    """
    df.plot.barh(title=title,
                 ylabel=ylabel, xlabel=xlabel,
                 figsize=(10, 5))
    plt.tight_layout()
    plt.savefig(f"./img/{name}.png")


if __name__ == "__main__":
    pass
