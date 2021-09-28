import csv

dataset = []

with open("bright_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        dataset.append(row)

# dataset = dataset[dataset.notna()]

headers = dataset[0]

star_data = dataset[1:]

for dp in star_data:
    for i in dp[3]:
        i = i*2
        
#     dp[2] = dp[2]*float(0.000954588)

# for dp in star_data:
#     dp[3] = dp[3]*float(0.102763)

# radius = dataset['Radius']

# for i in radius:
#     i = i*0.102763
#     radius.append(i)

# mass = dataset['Mass']

# for i in mass:
#     i = i*0.000954588
#     mass.append(i)

with open('stardata2.csv', 'a+') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    # writer.writerow(mass)
    # writer.writerow(radius)
    writer.writerows(star_data)