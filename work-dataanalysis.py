# Data Analysis
# Author: Thierry Narcisse
#
import
path = "data/NYC_Central_Park_weather_1869-2022.csv"
file = open(path)

def main():
    total_rain = 0
    total_min = 0
    count = 0

    total_tmax_june = 0
    june_count = 0

    with open("NYC_Central_Park_weather_1869-2022.csv") as f:

        for row in reader:

            rain = float(row["precip"])
            tmin = float(row["tmin"])
            tmax = float(row["tmax"])


            total_rain += rain
            total_min += tmin
            count += 1


if __name__ == "__main__":
    main()
