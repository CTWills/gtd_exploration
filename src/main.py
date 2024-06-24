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

    # get data for timeline for 1970 - 2020
    groups = top_5_total.index.values
    query = usa_df["gname"].isin(groups) & (
        (usa_df["doubtterr"] == 0) | (usa_df["doubtterr"] == -9))
    seventy_eighty_perc = (usa_df[query]["year"].value_counts(
        True) * 100).sort_index()[:11].sum()
    top_5_df = usa_df[query]
    top_5_timeline = top_5_df.groupby(["gname", "year"])["year"].count()

    # create timeline graph for 1970 - 2020
    hp.create_timeline(top_5_timeline, groups, name="tot_timeline", text=True,
                       title="Activity over time (1970 - 2020)", perc=seventy_eighty_perc)

    # get data for timeline for 2010 - 2020
    groups = top_5_modern.index.values
    query = usa_df["gname"].isin(groups) & (
        ((usa_df["doubtterr"] == 0) | (usa_df["doubtterr"] == -9)) &
        (usa_df["year"] >= 2010))
    top_mod_df = usa_df[query]
    top_modern_timeline = top_mod_df.groupby(["gname", "year"])[
        "year"].count()

    # create timeline for 2010 - 2020
    hp.create_timeline(top_modern_timeline, groups, name="mod_timeline",
                       title="Activity over time (2010 - 2020)")

    # create full timeline for modern groups timeline for 1970 - 2020
    query = usa_df["gname"].isin(groups) & (
        ((usa_df["doubtterr"] == 0) | (usa_df["doubtterr"] == -9)))
    hp.create_timeline(usa_df[query].groupby(["gname", "year"])[
        "year"].count(), groups, name="mod_timeline_1970",
        title="Activity over time (1970 - 2020)")

    # most used attack type from 1970 - 2020
    attacks = top_5_df.groupby("attacktype1_txt").size().sort_values()

    hp.create_bar_plot(attacks, title="All groups 1970 - 2020", ylabel="Attack type",
                       xlabel="Amount of attacks", name="tot_attacks")

    # Creating bar graphs for attacks used by each group
    attack_types = top_5_df["attacktype1_txt"].unique()
    groups = top_5_total.index.values
    types_per_group = top_5_df.groupby(["gname", "attacktype1_txt"]).size()
    for idx, group in enumerate(groups):
        name = group.split("/")[0]
        df = types_per_group[group].sort_values()
        hp.create_bar_plot(
            df, title=f"{group} 1970 - 2020", ylabel="Attack Type", xlabel="Amount",
            name=f"tot_{name}")

    # Creating bar graphs for attacks used by modern groups
    attack_types = top_mod_df["attacktype1_txt"].unique()
    groups = top_5_modern.index.values
    types_per_group = top_mod_df.groupby(
        ["gname", "attacktype1_txt"]).size()
    for idx, group in enumerate(groups):
        name = group.split("/")[0]
        df = types_per_group[group].sort_values()
        hp.create_bar_plot(
            df, title=f"{group} 2010 - 2020", ylabel="Attack Type", xlabel="Amount",
            name=f"mod_{name}")

    # Found top 10 targets from 1970 - 2020
    top_10_targets = top_5_df.groupby(
        ["targtype1_txt", "targsubtype1_txt"]).size().sort_values(ascending=False)[:10]

    # Creating bar graph for top 10 targets from 1970 - 2020
    df = top_10_targets.reset_index(name="count")[
        ["targsubtype1_txt", "count"]].sort_values(by="count")
    fig, ax = plt.subplots()
    df.plot.barh(x="targsubtype1_txt", y="count",
                 title="Top 10 Targets 1970 - 2020", ylabel="Target",
                 xlabel="Amount", figsize=(10, 5))
    plt.tight_layout()
    plt.savefig("./img/tot_targets.png")

    # Modern targets
    modern_targets = top_mod_df.groupby(
        ["targtype1_txt", "targsubtype1_txt"]).size().sort_values(ascending=False)[:10]

    # Modern target bar graph
    df = modern_targets.reset_index(name="count")[
        ["targsubtype1_txt", "count"]].sort_values(by="count")
    fig, ax = plt.subplots()
    df.plot.barh(x="targsubtype1_txt", y="count",
                 title="Top 10 Targets 2010 - 2020",
                 ylabel="Target", xlabel="Amount", figsize=(10, 5))
    plt.tight_layout()
    plt.savefig("./img/mod_targets.png")
