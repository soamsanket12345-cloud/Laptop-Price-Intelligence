import pandas as pd
import re

# ----------------------------
# Load Dataset
# ----------------------------
df = pd.read_csv("data/laptop_data_cleaned.csv")

# ----------------------------
# Clean RAM
# ----------------------------
df["Ram"] = df["Ram"].str.replace("GB", "", regex=False).astype(int)

# ----------------------------
# Clean Weight
# ----------------------------
df["Weight"] = df["Weight"].str.replace("kg", "", regex=False).astype(float)

# ----------------------------
# CPU Brand
# ----------------------------
df["CPU Brand"] = df["Cpu"].apply(lambda x: x.split()[0])

# ----------------------------
# GPU Brand
# ----------------------------
df["GPU Brand"] = df["Gpu"].apply(lambda x: x.split()[0])

# ----------------------------
# Extract SSD & HDD
# ----------------------------
def get_storage(memory):

    ssd = 0
    hdd = 0

    # SSD in GB
    match = re.search(r"(\d+)\s*GB SSD", memory)
    if match:
        ssd = int(match.group(1))

    # SSD in TB
    match = re.search(r"(\d+)\s*TB SSD", memory)
    if match:
        ssd = int(match.group(1)) * 1000

    # HDD in GB
    match = re.search(r"(\d+)\s*GB HDD", memory)
    if match:
        hdd = int(match.group(1))

    # HDD in TB
    match = re.search(r"(\d+)\s*TB HDD", memory)
    if match:
        hdd = int(match.group(1)) * 1000

    return pd.Series([ssd, hdd])

# Create SSD and HDD columns
df[["SSD", "HDD"]] = df["Memory"].apply(get_storage)

# ----------------------------
# Operating System Category
# ----------------------------
def get_os(os):

    if "Windows" in os:
        return "Windows"

    elif "Mac" in os or "macOS" in os:
        return "Mac"

    elif "Linux" in os:
        return "Linux"

    else:
        return "Other"

df["OS"] = df["OpSys"].apply(get_os)

# ----------------------------
# Display Results
# ----------------------------
print("\n===== CPU & GPU Brands =====")
print(df[["Cpu", "CPU Brand", "Gpu", "GPU Brand"]].head(10))

print("\n===== SSD & HDD =====")
print(df[["Memory", "SSD", "HDD"]].head(15))

print("\n===== Operating System =====")
print(df[["OpSys", "OS"]].head(15))

# ----------------------------
# Save Final Dataset
# ----------------------------
df.to_csv("data/final_laptop_data.csv", index=False)

print("\nFeature Engineering Completed Successfully!")
print("File Saved: data/final_laptop_data.csv")