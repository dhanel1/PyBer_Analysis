{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Pyber Challenge"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4.3 Loading and Reading CSV files"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Add Matplotlib inline magic command\n",
    "%matplotlib inline\n",
    "# Dependencies and Setup\n",
    "import matplotlib.pyplot as plt\n",
    "import pandas as pd\n",
    "\n",
    "# File to Load (Remember to change these)\n",
    "city_data_to_load = \"Resources/city_data.csv\"\n",
    "ride_data_to_load = \"Resources/ride_data.csv\"\n",
    "\n",
    "# Read the City and Ride Data\n",
    "city_data_df = pd.read_csv(city_data_to_load)\n",
    "ride_data_df = pd.read_csv(ride_data_to_load)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Merge the DataFrames"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>city</th>\n",
       "      <th>date</th>\n",
       "      <th>fare</th>\n",
       "      <th>ride_id</th>\n",
       "      <th>driver_count</th>\n",
       "      <th>type</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Lake Jonathanshire</td>\n",
       "      <td>2019-01-14 10:14:22</td>\n",
       "      <td>13.83</td>\n",
       "      <td>5739410935873</td>\n",
       "      <td>5</td>\n",
       "      <td>Urban</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>South Michelleport</td>\n",
       "      <td>2019-03-04 18:24:09</td>\n",
       "      <td>30.24</td>\n",
       "      <td>2343912425577</td>\n",
       "      <td>72</td>\n",
       "      <td>Urban</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Port Samanthamouth</td>\n",
       "      <td>2019-02-24 04:29:00</td>\n",
       "      <td>33.44</td>\n",
       "      <td>2005065760003</td>\n",
       "      <td>57</td>\n",
       "      <td>Urban</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Rodneyfort</td>\n",
       "      <td>2019-02-10 23:22:03</td>\n",
       "      <td>23.44</td>\n",
       "      <td>5149245426178</td>\n",
       "      <td>34</td>\n",
       "      <td>Urban</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>South Jack</td>\n",
       "      <td>2019-03-06 04:28:35</td>\n",
       "      <td>34.58</td>\n",
       "      <td>3908451377344</td>\n",
       "      <td>46</td>\n",
       "      <td>Urban</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                 city                 date   fare        ride_id  \\\n",
       "0  Lake Jonathanshire  2019-01-14 10:14:22  13.83  5739410935873   \n",
       "1  South Michelleport  2019-03-04 18:24:09  30.24  2343912425577   \n",
       "2  Port Samanthamouth  2019-02-24 04:29:00  33.44  2005065760003   \n",
       "3          Rodneyfort  2019-02-10 23:22:03  23.44  5149245426178   \n",
       "4          South Jack  2019-03-06 04:28:35  34.58  3908451377344   \n",
       "\n",
       "   driver_count   type  \n",
       "0             5  Urban  \n",
       "1            72  Urban  \n",
       "2            57  Urban  \n",
       "3            34  Urban  \n",
       "4            46  Urban  "
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Combine the data into a single dataset\n",
    "pyber_data_df = pd.merge(ride_data_df, city_data_df, how=\"left\", on=[\"city\", \"city\"])\n",
    "\n",
    "# Display the data table for preview\n",
    "pyber_data_df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Deliverable 1: Get a Summary DataFrame "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "type\n",
       "Rural        125\n",
       "Suburban     625\n",
       "Urban       1625\n",
       "Name: ride_id, dtype: int64"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#  1. Get the total rides for each city type\n",
    "ride_count = pyber_data_df.groupby([\"type\"]).count()[\"ride_id\"]\n",
    "ride_count.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "type\n",
       "Rural         78\n",
       "Suburban     490\n",
       "Urban       2405\n",
       "Name: driver_count, dtype: int64"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 2. Get the total drivers for each city type\n",
    "driver_count = city_data_df.groupby([\"type\"]).sum()[\"driver_count\"]\n",
    "driver_count.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "type\n",
       "Rural        4327.93\n",
       "Suburban    19356.33\n",
       "Urban       39854.38\n",
       "Name: fare, dtype: float64"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#  3. Get the total amount of fares for each city type\n",
    "fare_count = pyber_data_df.groupby([\"type\"]).sum()[\"fare\"]\n",
    "fare_count.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "type\n",
       "Rural       34.623440\n",
       "Suburban    30.970128\n",
       "Urban       24.525772\n",
       "Name: fare, dtype: float64"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#  4. Get the average fare per ride for each city type. \n",
    "fare_average = pyber_data_df.groupby([\"type\"]).mean()[\"fare\"]\n",
    "fare_average.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "type\n",
       "Rural       55.486282\n",
       "Suburban    39.502714\n",
       "Urban       16.571468\n",
       "dtype: float64"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 5. Get the average fare per driver for each city type. \n",
    "fare_per_driver = pyber_data_df.groupby([\"type\"]).sum()[\"fare\"]/city_data_df.groupby([\"type\"]).sum()[\"driver_count\"]\n",
    "fare_per_driver.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Total Rides</th>\n",
       "      <th>Total Drivers</th>\n",
       "      <th>Total Fares</th>\n",
       "      <th>Average Fare per Ride</th>\n",
       "      <th>Average Fare per Driver</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>type</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Rural</th>\n",
       "      <td>125</td>\n",
       "      <td>78</td>\n",
       "      <td>4327.93</td>\n",
       "      <td>34.623440</td>\n",
       "      <td>55.486282</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Suburban</th>\n",
       "      <td>625</td>\n",
       "      <td>490</td>\n",
       "      <td>19356.33</td>\n",
       "      <td>30.970128</td>\n",
       "      <td>39.502714</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Urban</th>\n",
       "      <td>1625</td>\n",
       "      <td>2405</td>\n",
       "      <td>39854.38</td>\n",
       "      <td>24.525772</td>\n",
       "      <td>16.571468</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          Total Rides  Total Drivers  Total Fares  Average Fare per Ride  \\\n",
       "type                                                                       \n",
       "Rural             125             78      4327.93              34.623440   \n",
       "Suburban          625            490     19356.33              30.970128   \n",
       "Urban            1625           2405     39854.38              24.525772   \n",
       "\n",
       "          Average Fare per Driver  \n",
       "type                               \n",
       "Rural                   55.486282  \n",
       "Suburban                39.502714  \n",
       "Urban                   16.571468  "
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#  6. Create a PyBer summary DataFrame. \n",
    "summary_df = pd.DataFrame ({'Total Rides':ride_count,'Total Drivers':driver_count,\n",
    "                           'Total Fares':fare_count,'Average Fare per Ride':fare_average,\n",
    "                           'Average Fare per Driver':fare_per_driver})\n",
    "summary_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [],
   "source": [
    "#  7. Cleaning up the DataFrame. Delete the index name\n",
    "summary_df.index.name = None"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Total Rides</th>\n",
       "      <th>Total Drivers</th>\n",
       "      <th>Total Fares</th>\n",
       "      <th>Average Fare per Ride</th>\n",
       "      <th>Average Fare per Driver</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Rural</th>\n",
       "      <td>125</td>\n",
       "      <td>78</td>\n",
       "      <td>$4,327.93</td>\n",
       "      <td>$34.62</td>\n",
       "      <td>$55.49</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Suburban</th>\n",
       "      <td>625</td>\n",
       "      <td>490</td>\n",
       "      <td>$19,356.33</td>\n",
       "      <td>$30.97</td>\n",
       "      <td>$39.50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Urban</th>\n",
       "      <td>1625</td>\n",
       "      <td>2405</td>\n",
       "      <td>$39,854.38</td>\n",
       "      <td>$24.53</td>\n",
       "      <td>$16.57</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          Total Rides  Total Drivers Total Fares Average Fare per Ride  \\\n",
       "Rural             125             78   $4,327.93                $34.62   \n",
       "Suburban          625            490  $19,356.33                $30.97   \n",
       "Urban            1625           2405  $39,854.38                $24.53   \n",
       "\n",
       "         Average Fare per Driver  \n",
       "Rural                     $55.49  \n",
       "Suburban                  $39.50  \n",
       "Urban                     $16.57  "
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#  8. Format the columns.\n",
    "def format(x):\n",
    "        return \"${:,.2f}\".format(x) \n",
    "summary_df_formatted = summary_df\n",
    "summary_df_formatted['Total Fares'] = summary_df_formatted['Total Fares'].apply(format)\n",
    "summary_df_formatted['Average Fare per Ride'] = summary_df_formatted['Average Fare per Ride'].apply(format)\n",
    "summary_df_formatted['Average Fare per Driver'] = summary_df_formatted['Average Fare per Driver'].apply(format)\n",
    "summary_df_formatted.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Deliverable 2.  Create a multiple line plot that shows the total weekly of the fares for each type of city."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "type   date               \n",
       "Rural  2019-01-01 09:45:36    43.69\n",
       "       2019-01-02 11:18:32    52.12\n",
       "       2019-01-03 19:51:01    19.90\n",
       "       2019-01-04 03:31:26    24.88\n",
       "       2019-01-06 07:38:40    47.33\n",
       "Name: fare, dtype: float64"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 2. Using groupby() to create a new DataFrame showing the sum of the fares \n",
    "#  for each date where the indices are the city type and date.\n",
    "sum_of_fares = pyber_data_df.groupby([\"type\",'date']).sum()[\"fare\"]\n",
    "sum_of_fares.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 3. Reset the index on the DataFrame you created in #1. This is needed to use the 'pivot()' function.\n",
    "# df = df.reset_index()\n",
    "sum_of_fares = sum_of_fares.reset_index()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>type</th>\n",
       "      <th>Rural</th>\n",
       "      <th>Suburban</th>\n",
       "      <th>Urban</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2019-01-01 00:08:16</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>37.91</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-01-01 00:46:46</th>\n",
       "      <td>NaN</td>\n",
       "      <td>47.74</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-01-01 02:07:24</th>\n",
       "      <td>NaN</td>\n",
       "      <td>24.07</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-01-01 03:46:50</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>7.57</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-01-01 05:23:21</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>10.75</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "type                 Rural  Suburban  Urban\n",
       "date                                       \n",
       "2019-01-01 00:08:16    NaN       NaN  37.91\n",
       "2019-01-01 00:46:46    NaN     47.74    NaN\n",
       "2019-01-01 02:07:24    NaN     24.07    NaN\n",
       "2019-01-01 03:46:50    NaN       NaN   7.57\n",
       "2019-01-01 05:23:21    NaN       NaN  10.75"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 4. Create a pivot table with the 'date' as the index, the columns ='type', and values='fare' \n",
    "# to get the total fares for each type of city by the date. \n",
    "fares_pivot = sum_of_fares.pivot(index = 'date', columns = 'type', values = 'fare')\n",
    "fares_pivot.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>type</th>\n",
       "      <th>Rural</th>\n",
       "      <th>Suburban</th>\n",
       "      <th>Urban</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2019-01-01 00:08:16</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>37.91</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-01-01 00:46:46</th>\n",
       "      <td>NaN</td>\n",
       "      <td>47.74</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-01-01 02:07:24</th>\n",
       "      <td>NaN</td>\n",
       "      <td>24.07</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-01-01 03:46:50</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>7.57</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-01-01 05:23:21</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>10.75</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "type                 Rural  Suburban  Urban\n",
       "date                                       \n",
       "2019-01-01 00:08:16    NaN       NaN  37.91\n",
       "2019-01-01 00:46:46    NaN     47.74    NaN\n",
       "2019-01-01 02:07:24    NaN     24.07    NaN\n",
       "2019-01-01 03:46:50    NaN       NaN   7.57\n",
       "2019-01-01 05:23:21    NaN       NaN  10.75"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 5. Create a new DataFrame from the pivot table DataFrame using loc on the given dates, '2019-01-01':'2019-04-29'.\n",
    "new_dataframe = fares_pivot.loc['2019-01-01':'2019-04-29']\n",
    "new_dataframe.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 6. Set the \"date\" index to datetime datatype. This is necessary to use the resample() method in Step 8.\n",
    "# df.index = pd.to_datetime(df.index)\n",
    "new_dataframe.index = pd.to_datetime(new_dataframe.index)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "DatetimeIndex: 2196 entries, 2019-01-01 00:08:16 to 2019-04-28 19:35:03\n",
      "Data columns (total 3 columns):\n",
      " #   Column    Non-Null Count  Dtype  \n",
      "---  ------    --------------  -----  \n",
      " 0   Rural     114 non-null    float64\n",
      " 1   Suburban  573 non-null    float64\n",
      " 2   Urban     1509 non-null   float64\n",
      "dtypes: float64(3)\n",
      "memory usage: 68.6 KB\n"
     ]
    }
   ],
   "source": [
    "# 7. Check that the datatype for the index is datetime using df.info()\n",
    "new_dataframe.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>type</th>\n",
       "      <th>Rural</th>\n",
       "      <th>Suburban</th>\n",
       "      <th>Urban</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2019-01-06</th>\n",
       "      <td>187.92</td>\n",
       "      <td>721.60</td>\n",
       "      <td>1661.68</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-01-13</th>\n",
       "      <td>67.65</td>\n",
       "      <td>1105.13</td>\n",
       "      <td>2050.43</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-01-20</th>\n",
       "      <td>306.00</td>\n",
       "      <td>1218.20</td>\n",
       "      <td>1939.02</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-01-27</th>\n",
       "      <td>179.69</td>\n",
       "      <td>1203.28</td>\n",
       "      <td>2129.51</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-02-03</th>\n",
       "      <td>333.08</td>\n",
       "      <td>1042.79</td>\n",
       "      <td>2086.94</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "type         Rural  Suburban    Urban\n",
       "date                                 \n",
       "2019-01-06  187.92    721.60  1661.68\n",
       "2019-01-13   67.65   1105.13  2050.43\n",
       "2019-01-20  306.00   1218.20  1939.02\n",
       "2019-01-27  179.69   1203.28  2129.51\n",
       "2019-02-03  333.08   1042.79  2086.94"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 8. Create a new DataFrame using the \"resample()\" function by week 'W' and get the sum of the fares for each week.\n",
    "fares_by_week = new_dataframe.resample('W').sum()\n",
    "fares_by_week.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x205ed622520>"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# 8. Using the object-oriented interface method, plot the resample DataFrame using the df.plot() function. \n",
    "\n",
    "# Import the style from Matplotlib.\n",
    "from matplotlib import style\n",
    "# Use the graph style fivethirtyeight.\n",
    "style.use('fivethirtyeight')\n",
    "\n",
    "fares_by_week.plot()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
