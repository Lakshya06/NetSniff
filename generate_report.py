import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the network packet data (assuming the data is in CSV format)
data = pd.read_csv("network_data.csv")

# Sample mapping of port numbers to protocols (expand this as needed)
port_protocol_mapping = {
    80: 'HTTP',     # HTTP (TCP)
    443: 'HTTPS',   # HTTPS (TCP)
    21: 'FTP',      # FTP (TCP)
    53: 'DNS',      # DNS (UDP)
    123: 'NTP',     # NTP (UDP)
    25: 'SMTP',     # SMTP (TCP)
    67: 'DHCP',     # DHCP (UDP)
    69: 'TFTP',     # TFTP (UDP)
    110: 'POP3',    # POP3 (TCP)
    3389: 'RDP',    # RDP (TCP)
}

# Add protocol info for source and destination ports
def map_protocol(row):
    src_protocol = port_protocol_mapping.get(row['Source Port'], 'Unknown')
    dst_protocol = port_protocol_mapping.get(row['Destination Port'], 'Unknown')
    return src_protocol, dst_protocol

data[['Source Protocol', 'Destination Protocol']] = data.apply(map_protocol, axis=1, result_type="expand")

# Set Seaborn style for the plots
sns.set(style="whitegrid")

# Plotting Setup
fig, axs = plt.subplots(3, 2, figsize=(16, 18))

# Network Type Distribution (TCP/UDP) Pie Chart
network_type_counts = data['Source Protocol'].apply(lambda x: 'TCP' if x != 'Unknown' and x in ['HTTP', 'HTTPS', 'FTP', 'SMTP', 'POP3', 'RDP'] else 'UDP').value_counts()
network_type_colors = sns.color_palette("Set2", 2)  # Use a color palette
axs[0, 0].pie(network_type_counts, labels=network_type_counts.index, autopct='%1.1f%%', startangle=140, colors=network_type_colors, wedgeprops={'edgecolor': 'black'})
axs[0, 0].set_title('Network Type Distribution (TCP/UDP)', fontsize=14)

# Protocol Distribution Pie Chart
protocol_counts = pd.concat([data['Source Protocol'], data['Destination Protocol']]).value_counts()
protocol_colors = sns.color_palette("Set3", len(protocol_counts))  # Custom colors
axs[1, 0].pie(protocol_counts, labels=protocol_counts.index, autopct='%1.1f%%', startangle=140, colors=protocol_colors, wedgeprops={'edgecolor': 'black'})
axs[1, 0].set_title('Protocol Distribution (HTTP, HTTPS, DNS, etc.)', fontsize=14)

# Port Distribution Bar Graph (Source Ports) - Show only present ports
source_port_counts = data['Source Port'].value_counts()
sns.barplot(x=source_port_counts.index, y=source_port_counts.values, ax=axs[0, 1], palette="Blues_d")
axs[0, 1].set_title('Source Port Distribution', fontsize=14)
axs[0, 1].set_xlabel('Port Number', fontsize=12)
axs[0, 1].set_ylabel('Frequency', fontsize=12)

# Add frequency labels on bars
for i, v in enumerate(source_port_counts.values):
    axs[0, 1].text(i, v + 0.1, str(v), ha='center', va='bottom')

# Port Distribution Bar Graph (Destination Ports) - Show only present ports
destination_port_counts = data['Destination Port'].value_counts()
sns.barplot(x=destination_port_counts.index, y=destination_port_counts.values, ax=axs[1, 1], palette="Greens_d")
axs[1, 1].set_title('Destination Port Distribution', fontsize=14)
axs[1, 1].set_xlabel('Port Number', fontsize=12)
axs[1, 1].set_ylabel('Frequency', fontsize=12)

# Add frequency labels on bars
for i, v in enumerate(destination_port_counts.values):
    axs[1, 1].text(i, v + 0.1, str(v), ha='center', va='bottom')

# Plot for IP Addresses (Source IP & Destination IP)
# Create a frequency count of IP addresses (both source and destination)
source_ip_counts = data['Source IP'].value_counts().head(10)  # Get top 10 most frequent source IPs
destination_ip_counts = data['Destination IP'].value_counts().head(10)  # Get top 10 most frequent destination IPs

# Plotting the Source IP distribution
sns.barplot(x=source_ip_counts.values, y=source_ip_counts.index, ax=axs[2, 0], palette="Reds_d")
axs[2, 0].set_title('Top 10 Source IP Addresses', fontsize=14)
axs[2, 0].set_xlabel('Frequency', fontsize=12)
axs[2, 0].set_ylabel('IP Address', fontsize=12)

# Plotting the Destination IP distribution
sns.barplot(x=destination_ip_counts.values, y=destination_ip_counts.index, ax=axs[2, 1], palette="Purples_d")
axs[2, 1].set_title('Top 10 Destination IP Addresses', fontsize=14)
axs[2, 1].set_xlabel('Frequency', fontsize=12)
axs[2, 1].set_ylabel('IP Address', fontsize=12)

# Automatically adjust layout for better spacing
plt.tight_layout()

# Show the plot
plt.show()
