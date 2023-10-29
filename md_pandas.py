import pandas as pd

data = pd.read_csv("insurance.csv")

print(data.head(10))

# region_charges = data.groupby("region")["charges"].sum().reset_index().round()


region_charges = data.groupby(["region"])["charges"].mean().reset_index().round()
# region_charges_pivot = region_charges.pivot(index="region", columns="smoker", values="age")


print(region_charges)

