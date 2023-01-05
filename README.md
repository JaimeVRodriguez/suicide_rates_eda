# Global Suicide Rates
![](images/dataset-cover.jpg)

***
<br />

## Table of Contents
- [Introduction](#introduction)
- [Data Processing](#data-processing)
- [Overall](#overall)
    - [Male vs Female](#male-vs-female)
    - [Generations](#generation-breakdown)
    - [Highest Five Countries](#high-five)
- [United States](#united-states)
    - [US Transit Line Counts](#us-transit-line-counts)
    - [US Heatmap](#us-heatmap)
    - [New York Data](#new-york-data)
<br />
<br />
<br />

***
## **Introduction**
***
This dataset, which can be found [here](https://www.kaggle.com/datasets/russellyates88/suicide-rates-overview-1985-to-2016), provides global suicide rates from 1985 to 2016. This compiled dataset pulled from four other datasets linked by time and place, and was built to find signals correlated to increased suicide rates among different cohorts globally, across the socio-economic spectrum.
<br />
<br />
<br />

***
## **Data Processing**
***
Initial overview of data highlitedt the fact that there was some data cleaning that needed to occur. <br />

- Two columns were removed
    - Country Year - This appeared to be a generic code value. It was a combination of the country and year in string value. For the purposes of this analysis, it was determined it was needed.
    - HDI for year - Numerical value of for human development index. This column held a significant number of NAN values and therefore did not bring any significant value to the dataset.
- Remove 2016 data
    - Allow the data contained data from 2016 it appeared that this data may have been gathered at some point in 2016 as there was only 160 (of 27820) data points for this particular year
- Remove Countries with less than 3 years of data
    - In order to properly assess the suicide data for a particular country it was determined that there should be at least 4 years of data in order to be considered significant.
    - The following countries were removeds: 7 Countries - Bosnia and Herzegovina, Cabo Verde, Dominica, Macau, Oman, Saint Kitts and Nevis, San Marino.

***
## **Overall**
***
<span style='color:green'> **Key Highlights** </span> <br />
- Data spaned across **93** different countries
- Peak rake was in **1995** with **15.66** per 100K
- Average rate from 1995 to 2015 was **12.87** deaths per 100K
- Steady decrease from 1995 to 2015 <br />

The dataset consited of over 27000 records, Which included 100 different countries. An inital cursory look at the data can be seen below. It appeared that global suicide rates continued to increase until its peak in 1995 with an average of 15.66 suicides per 100,000 people. After which there was a steady decline. Additionaly, the average rate per 100K people was 12.87 suicides.

Of key note is the high point in 1995, which begs the questions what occured or led to this point. A quick look into history revealed there were several world events that could have led to things like survivors remorse or affected by the losses or events themselves. <br />

<span style='color:orange'> **Global Events Included:** </span> <br />
Oklahoma City Bombing, US pulls out of Somalia, UN intervenes in Bosnian Civial War, Japan Earthquake, UK Barings Bank Collapse, Russian Earthquake, OJ Found Innocent

![](images/suicide_per_100K.png)
![](images/world_map.png)
<br />
<br />
<br />

### Male vs Female
<span style='color:green'> **Key Highlights** </span> <br />
- Max male rate of **24.90** per 100K
- Max female rate of **6.42** per 100K
- Male suicide rate is **3.8** times higher than that of females

![](images/male_female.png)
<br />
<br />

### Generation & Age Breakdown
<span style='color:green'> **Key Highlights** </span> <br />
- Generation agnostic


![](images/generations.png)
<br />
<br />
![](images/age_total.png)
![](images/age_rate.png)

<br />
<br />

### High Five

![](images/high_five_total.png)
![](images/high_five_per_100K.png)

***
## United States
***

### US Transit Line Counts
After indentifying the United States held the most cities, further analysis was conducted on those cities within the United States. What can be immeditaely identified is that the cities withing the United States are large metropolitan cities. With [New York](#new-york-data) having the most stations.

It is important to note that there are other cities within the United States that host transportation stations, however the [station](data/stations.csv) data does not hold information for those cities not listed. This is important to note this is one limitation of this data set.

![](images/us_transit_lines.png)
<br />
<br />

### US Heatmap
Additinally cities within the United States that host a transportation station are represented below with the a provides a visual representation of the density of the stations within those cities.

![](images/us_heatmap.png) 

Click this [interactive map](http://127.0.0.1:5500/images/us_heatmap.html) to view and zoom to certain areas.
<br />
<br />

### New York Data
As previously identified, New York held the most stations in the United States. Additionaly, it was noted that the United States opened the majority of tracks were opened between the 1875 and 1925. This further highlights the stark buildup during that time period and followed by a tappering of openings.

![](images/new_york_track_length.png)
