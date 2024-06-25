# Overview

Using data from the Global Terrorism Database (GTD), we look to find the most prominent threats to the US.
<br>

#### Key points

- GTD definition of terrorism
  - the threatened or actual use of illegal force and violence by a non-state actor to attain a political, economic religious, or social goal through fear, coercion, orintimidation
- "The GTD does not include plots or conspiracies that are not enacted, or at least attempted. For an
  event to be included in the GTD, the attackers must be “out the door,” en route to execute the attack.
  Planning, reconnaissance, and acquiring supplies do not meet this threshold." (2021, August)
- Generic Group names are used to represent who did the attack
  - These names do not represent discrete entities
  - They also do not characterize the behavior
    of an entire population or ideological movement. For many attacks, generic identifiers are the
    only information available about the perpetrators.

# Research Questions

- What are the top 5 terrorist groups that attack the US the most?
- What is the most common attack type against the US?
  - What is the most common attack for each group?
- Who/What are the most common targets?

# Data

All data is from the GTD and contains over 200,000 records of attacks starting from 1970. <br>
In order to get access to the dataset, you must request using this link [GTD Dataset](https://www.start.umd.edu/gtd/contact/download).<br>
It is important to note that events in 1993 are not included in this dataset, as most of that data was lost.

# Cleaning

The data is orginally in an excel file with over 200,000 rows. Reading this with python will be extremely slow so I first converted the file to a csv. <br>
From there I had to filter out all data that didnt involve the United States. <br>
There are also criteria for each event that gives a confidence level of whether or not the event was actually a terrorist attack. I am including only the events where there are no doubt its a terrorist attack. This criteria started being recored only after 1997, so all events before then are also included in this analysis.

# Findings
* Top 5 Prominent Groups (1970 - 2020)
  <br>
  Looking at the entire history from 1970 - 2020, here are the top 5 most active terrorist groups that target the US.
  With this data, we actually do not know a large portion of who committed these attacks.
  When no information about the perpetrator group is available, this field is coded as “Unknown.”
![screenshot](https://github.com/CTWills/gtd_exploration/blob/main/img/top_5_tot.png)
* Here we can see the attack frequency every 10 years starting from 1970.
  <br>
1970s is notably when the majority of the attacks happened. There is a lot of interesting history to get into about why, but mainly there was significant political, social, and economic issues in general,
You had the vietnam war still going in in the early 70s, cold war, Roe V Wade in 1973, you can then see the rise of the Anti-Abortion extremists. <br>
Note that the groups, Left-Wing Militants and FALN died out before 1990, but they also count for a lot of attacks in this dataset. About 45% of attacks in general were from 1970-1980. 
Because of this, these groups are most likely not a relevant source of danger in modern times, so I cut the timeline down, and started looking between 2010 and 2020. Its still important to understand these initial groups for potential furthering of these analysis, which we will get too later.

![screenshot](https://github.com/CTWills/gtd_exploration/blob/main/img/tot_timeline.png)

* Modern groups (2010 - 2020)
  <br>
  Here on the left we now have the more modern groups. We still do not know who the majority of these attackers are.
  Here you can see the big difference between the times as well, all groups, but the white supremicists/nationalists have changed and we are going to be focusing on the groups on the left graph here for further analysis.
  There does seem to be a big change in motivation, with the 1970 groups being more political, but modern groups are more religion/race motivated.
  
![screenshot](https://github.com/CTWills/gtd_exploration/blob/main/img/top_5_mod.png)


# Key results

# Credits

- START (National Consortium for the Study of Terrorism and Responses to Terrorism). (2021). Global
  Terrorism Database (GTD) [Data set]. University of Maryland. https://www.start.umd.edu/gtd

- START (National Consortium for the Study of Terrorism and Responses to Terrorism). (2021, August).
  Global Terrorism Database codebook: Methodology, inclusion criteria, and variables. University of
  Maryland. https://www.start.umd.edu/gtd/downloads/Codebook.pdf
