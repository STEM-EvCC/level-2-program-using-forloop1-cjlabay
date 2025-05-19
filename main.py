# Counts the total number of space missions.
# Counts the number of successful missions.
# Calculates the success rate of the missions.
# Lists all the missions that were launched before the year 2000.

mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

print(f"Total number of missions: {len(mission_names)}")
print(f"Number of successful missions: {mission_success.count(True)}")
print(f"Success rate: {"{:.2f}".format((mission_success.count(True) / len(mission_success)) * 100)}%")
print("Missions launched before the year 2000:")
for i in range(len(mission_names)):
    if mission_years[i] <2000:
        print("- " + mission_names[i])