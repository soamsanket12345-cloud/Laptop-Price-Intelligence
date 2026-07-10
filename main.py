#1--> print("Hello Soam! Welcome to Laptop Price Intelligence Dashboard")

#2--> import pandas as pd

# # Read the dataset
# df = pd.read_csv("data/laptop_data.csv")

# # Show the first 5 rows
# print(df.head())

#3--> import pandas as pd

# # Read the dataset
# df = pd.read_csv("data/laptop_data.csv")

# # Show first 5 rows
# print(df.head())

# # Show number of rows and columns
# print(df.shape)

# # Show all column names
# print(df.columns)



#4--> import pandas as pd

# # Read the dataset
# df = pd.read_csv("data/laptop_data.csv")

# # Number of laptops
# print("Total Laptops:", len(df))

# # Average laptop price
# print("Average Price:", df["Price"].mean())

# # Most common company
# print("Most Popular Company:")
# print(df["Company"].value_counts())

# # Most common RAM
# print("RAM Distribution:")
# print(df["Ram"].value_counts())




#5--> import pandas as pd

# # Read dataset
# df = pd.read_csv("data/laptop_data.csv")

# # Remove unnecessary column
# df = df.drop("Unnamed: 0", axis=1)

# # Display first 5 rows
# print(df.head())

# # Show columns
# print(df.columns)

# # (add)
# # Save cleaned dataset
# df.to_csv("data/laptop_data_cleaned.csv", index=False)

# print("\nCleaned dataset saved successfully!")




#6-->  import pandas as pd

# # Read cleaned dataset
# df = pd.read_csv("data/laptop_data_cleaned.csv")

# # Display statistical summary
# print(df.describe())


#7-->  import pandas as pd

# # Read cleaned dataset
# df = pd.read_csv("data/laptop_data_cleaned.csv")

# # Show only HP laptops
# hp_laptops = df[df["Company"] == "HP"]

# print(hp_laptops)




#8--> import pandas as pd

# df = pd.read_csv("data/laptop_data_cleaned.csv")

# hp_laptops = df[df["Company"] == "HP"]

# print("Total HP laptops:", len(hp_laptops))




#9--> import pandas as pd

# df = pd.read_csv("data/laptop_data_cleaned.csv")

# result = df[(df["Company"]=="HP") & (df["Ram"]=="8GB")]

# print(result.head())





#10-->   import pandas as pd

# # Read cleaned dataset
# df = pd.read_csv("data/laptop_data_cleaned.csv")

# # Average price by company
# average_price = df.groupby("Company")["Price"].mean()

# print(average_price)

# # ADDING FEW THINGS TO LEARN
# print(df.groupby("Company")["Price"].mean())

# print(df.groupby("Company").size())

# print(df.groupby("Company")["Price"].max())

# print(df.groupby("Company")["Price"].min())




#11-->  import pandas as pd
# import matplotlib.pyplot as plt

# # Read dataset
# df = pd.read_csv("data/laptop_data_cleaned.csv")

# # Count laptops by company
# company_count = df["Company"].value_counts()

# # Create bar chart
# company_count.plot(kind="bar")

# # Title
# plt.title("Number of Laptops by Company")

# # X-axis
# plt.xlabel("Company")

# # Y-axis
# plt.ylabel("Number of Laptops")

# # Show graph
# # plt.show()


# plt.savefig("graphs/company_count.png")
# plt.show()








#12-->    import pandas as pd

# # Read dataset
# df = pd.read_csv("data/laptop_data_cleaned.csv")

# # Average price of each company
# avg_price = df.groupby("Company")["Price"].mean()

# print(avg_price.sort_values(ascending=False))








#13-->    import pandas as pd
# import matplotlib.pyplot as plt

# # Read dataset
# df = pd.read_csv("data/laptop_data_cleaned.csv")

# # Calculate average price
# avg_price = df.groupby("Company")["Price"].mean()

# # Sort from highest to lowest
# avg_price = avg_price.sort_values(ascending=False)

# # Create graph
# avg_price.plot(kind="bar")

# # Add title
# plt.title("Average Laptop Price by Company")

# # X-axis label
# plt.xlabel("Company")

# # Y-axis label
# plt.ylabel("Average Price (INR)")

# # Rotate company names for readability
# plt.xticks(rotation=45)

# # Adjust layout
# plt.tight_layout()

# # Save graph
# plt.savefig("graphs/average_price_by_company.png")

# # Show graph
# plt.show()




#14--> import pandas as pd

# df = pd.read_csv("data/laptop_data_cleaned.csv")

# print("========== DATASET INFORMATION ==========")

# print("\nShape:")
# print(df.shape)

# print("\nColumns:")
# print(df.columns)

# print("\nData Types:")
# print(df.dtypes)

# print("\nSummary Statistics:")
# print(df.describe())

# print("\nMissing Values:")
# print(df.isnull().sum())




#15-->  import pandas as pd

# df = pd.read_csv("data/laptop_data_cleaned.csv")

# print(df[["Inches", "Price"]].corr())



#16-->  import pandas as pd

# df = pd.read_csv("data/laptop_data_cleaned.csv")

# # Remove GB
# df["Ram"] = df["Ram"].str.replace("GB", "")

# print(df["Ram"].head())




#17-->   import pandas as pd

# df = pd.read_csv("data/laptop_data_cleaned.csv")

# # Clean RAM
# df["Ram"] = df["Ram"].str.replace("GB", "")
# df["Ram"] = df["Ram"].astype(int)

# # Clean Weight
# df["Weight"] = df["Weight"].str.replace("kg", "")
# df["Weight"] = df["Weight"].astype(float)

# # Check data types
# print(df.dtypes)

# # Save cleaned dataset
# df.to_csv("data/laptop_data_final.csv", index=False)

# print("Dataset saved successfully!")



#18-->  import pandas as pd

# # Read cleaned dataset
# df = pd.read_csv("data/laptop_data_final.csv")

# # Average price by laptop type
# type_price = df.groupby("TypeName")["Price"].mean()

# # Sort from highest to lowest
# type_price = type_price.sort_values(ascending=False)

# print(type_price)





#19-->  import pandas as pd

# # Read cleaned dataset
# df = pd.read_csv("data/laptop_data_final.csv")

# # Filter only Lenovo laptops
# lenovo = df[df["Company"] == "Lenovo"]

# # Count RAM sizes
# ram_count = lenovo["Ram"].value_counts()

# # print(ram_count) replaced with code down 

# import matplotlib.pyplot as plt

# ram_count.plot(kind="bar")

# plt.title("Lenovo Laptop RAM Distribution")
# plt.xlabel("RAM (GB)")
# plt.ylabel("Number of Laptops")

# plt.tight_layout()

# plt.show()




#20-->  import pandas as pd
# import matplotlib.pyplot as plt

# # Read dataset
# df = pd.read_csv("data/laptop_data_final.csv")

# # Count laptops by company
# company_count = df["Company"].value_counts()

# print(company_count)

# # Create graph
# company_count.plot(kind="bar")

# plt.title("Number of Laptops by Company")
# plt.xlabel("Company")
# plt.ylabel("Number of Laptops")

# plt.xticks(rotation=45)
# plt.tight_layout()

# plt.savefig("graphs/company_distribution.png")

# plt.show()



#21-->   import pandas as pd
# import matplotlib.pyplot as plt

# # Read dataset
# df = pd.read_csv("data/laptop_data_final.csv")

# # Count operating systems
# os_count = df["OpSys"].value_counts()

# # Print result
# print(os_count)

# # Create graph
# os_count.plot(kind="bar")

# # Title
# plt.title("Operating System Distribution")

# # X-axis
# plt.xlabel("Operating System")

# # Y-axis
# plt.ylabel("Number of Laptops")

# # Rotate names for readability
# plt.xticks(rotation=45)

# # Arrange graph properly
# plt.tight_layout()

# # Save graph
# plt.savefig("graphs/operating_system_distribution.png")

# # Show graph
# plt.show()




#22-->   import pandas as pd

# # Read cleaned dataset
# df = pd.read_csv("data/laptop_data_final.csv")

# # Average weight by company
# weight = df.groupby("Company")["Weight"].mean()

# # Sort from lightest to heaviest
# weight = weight.sort_values()

# print(weight)




#23-->  import pandas as pd

# # Read dataset
# df = pd.read_csv("data/laptop_data_final.csv")

# # Sort by price (highest first)
# top10 = df.sort_values(by="Price", ascending=False)

# # Display first 10 rows
# print(top10.head(10))






#24-->  import pandas as pd

# # Read dataset
# df = pd.read_csv("data/laptop_data_final.csv")

# # Filter HP laptops with 8 GB RAM
# result = df[(df["Company"] == "HP") & (df["Ram"] == 8)]

# print(result)




#25-->   import pandas as pd

# df = pd.read_csv("data/laptop_data_final.csv")

# result = df[
#     (df["Company"]=="HP") |
#     (df["Company"]=="Dell")
# ]

# print(result)





#26-->  import pandas as pd

# df = pd.read_csv("data/laptop_data_final.csv")

# print(df.describe())






#27-->  import pandas as pd

# # Read dataset
# df = pd.read_csv("data/laptop_data_final.csv")

# # Group by Company and TypeName
# result = df.groupby(["Company", "TypeName"])["Price"].mean()

# # print(result) for better output down 
# print(result.sort_values(ascending=False))





#28-->  import pandas as pd

# df = pd.read_csv("data/laptop_data_final.csv")

# correlation = df["Ram"].corr(df["Price"])

# print("Correlation between RAM and Price:")
# print(correlation)




import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/laptop_data_final.csv")

company = df["Company"].value_counts()

company.plot(kind="bar")

plt.title("Number of Laptops by Company")
plt.xlabel("Company")
plt.ylabel("Count")

plt.savefig("graphs/company_count.png")

plt.show()