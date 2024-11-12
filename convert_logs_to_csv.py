import pandas as pd

# List to hold structured data
data = []

# Read the text file and process each line
with open("dummyData5.txt", "r") as file:
    for line in file:
        # Remove trailing spaces and extra commas that are not needed
        cleaned_line = line.strip().replace(".,", ",").strip(", ")
        
        # Split the line by commas
        fields = [field.strip() for field in cleaned_line.split(",")]
        
        # Check if the line has exactly 7 fields
        if len(fields) == 7:
            data.append({
                "Source MAC": fields[0],
                "Destination MAC": fields[1],
                "Protocol": fields[2],
                "Source IP": fields[3],
                "Destination IP": fields[4],
                "Source Port": fields[5],
                "Destination Port": fields[6]
            })
        else:
            print(f"Skipping malformed line: {line}")

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(data)

# Save to a CSV file
df.to_csv("network_data.csv", index=False)
print("Data has been converted and saved to network_data.csv")
