"""
Will generate all plots for data analysis
"""
import pandas as pd
import matplotlib.pyplot as plt
import clean_data as cd
import helper as hp

if __name__ == "__main__":
    # read in inital data from csv
    world_df = pd.read_csv("./data/full_data.csv",
                           index_col=0, low_memory=False)

    # Filter data only for United States
    usa_df = world_df[world_df["country_txt"] == "United States"].copy()

    # Creates a datetime column date
    usa_df["date"] = cd.create_date_column(usa_df)

    # retrieve top 5 active groups
    top_5_total = hp.get_terrorist_groups(
        usa_df, 5).sort_values()
    top_5_modern = hp.get_terrorist_groups(
        usa_df, 5, 2010).sort_values()

    # create bar plots for most active groups
    hp.create_bar_plot(
        top_5_total, title="Top 5 groups that attack the most (1970- 2020)",
        ylabel="Group name", xlabel="Amount of attacks", name="top_5_tot")
    hp.create_bar_plot(
        top_5_modern, title="Top 5 groups that attack the most (2010- 2020)",
        ylabel="Group name", xlabel="Amount of attacks", name="top_5_mod")
