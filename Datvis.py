import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv("/Users/ayush/Ayush/Code/Python/strike.csv")
df = pd.DataFrame(data)

#1. Year by Year Increase in Strikes
year_counts = df['Incident Year'].value_counts().sort_index()
year_counts.plot(kind='line', xlabel='Year', ylabel='Number of Entries', title='Entries per Year')
plt.show()

#2. Strikes by Seasons [Summer highest; closely followed by fall]
month_to_season = {
    1: "Winter",
    2: "Winter",
    3: "Spring",
    4: "Spring",
    5: "Spring",
    6: "Summer",
    7: "Summer",
    8: "Summer",
    9: "Fall",
    10: "Fall",
    11: "Fall",
    12: "Winter"
}


df['Season'] = df['Incident Month'].map(month_to_season)


season_counts = df['Season'].value_counts().reindex(["Winter", "Spring", "Summer", "Fall"])

season_counts.plot(kind='bar', xlabel='Season', ylabel='Number of Entries')
plt.xticks(fontsize=7)  
plt.yticks(fontsize=7)
plt.title('Number of Entries by Season')
plt.show()

#3. Grouping Strikes based on Flight Phases

flight_phase_counts = df['Flight Phase'].value_counts()
flight_phase_counts.plot(kind='bar', xlabel='Flight Phase', ylabel='Count')
plt.xticks(fontsize=4)  
plt.yticks(fontsize=4)
plt.title('Count of Entries by Flight Phase')
plt.show()

#4. Sightings v/s Seasons [Increase drastically during Migration Time] [Merlins]
gull_df = df[df['Species Name'] == 'MERLIN']


if not gull_df.empty:
    
    gull_month_counts = gull_df.groupby('Incident Month').size()

    
    gull_month_counts.plot(kind='bar', xlabel='Incident Month', ylabel='Count')
    plt.title('Number of Merlin Sightings per Month')
    plt.xticks(rotation=0)  
    plt.show()
else:
    print("No 'Merlin' sightings found.")

#5. Sightings v/s Seasons [Increase drastically during Migration Time] [Laughing Gull]
gull_df = df[df['Species Name'] == 'LAUGHING GULL']


if not gull_df.empty:
    
    gull_month_counts = gull_df.groupby('Incident Month').size()

    
    gull_month_counts.plot(kind='bar', xlabel='Incident Month', ylabel='Count')
    plt.title('Number of Laughing Gull Sightings per Month')
    plt.xticks(rotation=0)  # Rotate x-axis labels if needed
    plt.show()
else:
    print("No 'Gull' sightings found.")