import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("network_data.csv")

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

def map_protocol(row):
    src_protocol = port_protocol_mapping.get(row['Source Port'], 'Unknown')
    dst_protocol = port_protocol_mapping.get(row['Destination Port'], 'Unknown')
    return src_protocol, dst_protocol

data[['Source Protocol', 'Destination Protocol']] = data.apply(map_protocol, axis=1, result_type="expand")

sns.set(style="whitegrid")

# Increase figure size to prevent overlapping
fig, axs = plt.subplots(3, 2, figsize=(18, 18))

# Adjust pie chart for network type distribution
network_type_counts = data['Source Protocol'].apply(lambda x: 'TCP' if x != 'Unknown' and x in ['HTTP', 'HTTPS', 'FTP', 'SMTP', 'POP3', 'RDP'] else 'UDP').value_counts()
network_type_colors = sns.color_palette("Set2", 2)
axs[0, 0].pie(network_type_counts, labels=network_type_counts.index, autopct='%1.1f%%', startangle=140, colors=network_type_colors, wedgeprops={'edgecolor': 'black'})
axs[0, 0].set_title('Network Type Distribution (TCP/UDP)', fontsize=14)

# Adjust pie chart for protocol distribution
protocol_counts = pd.concat([data['Source Protocol'], data['Destination Protocol']]).value_counts()
protocol_colors = sns.color_palette("Set3", len(protocol_counts))
axs[1, 0].pie(protocol_counts, labels=protocol_counts.index, autopct='%1.1f%%', startangle=140, colors=protocol_colors, wedgeprops={'edgecolor': 'black'})
axs[1, 0].set_title('Protocol Distribution (HTTP, HTTPS, DNS, etc.)', fontsize=14)

# Source Port Distribution - Bar plot
source_port_counts = data['Source Port'].value_counts()
sns.barplot(x=source_port_counts.index, y=source_port_counts.values, ax=axs[0, 1], palette="Blues_d")
axs[0, 1].set_title('Source Port Distribution', fontsize=14)
axs[0, 1].set_xlabel('Port Number', fontsize=12)
axs[0, 1].set_ylabel('Frequency', fontsize=12)

# Rotate x-axis labels for readability
for label in axs[0, 1].get_xticklabels():
    label.set_rotation(45)
axs[0, 1].tick_params(axis='x', labelsize=10)

for i, v in enumerate(source_port_counts.values):
    axs[0, 1].text(i, v + 0.1, str(v), ha='center', va='bottom')

# Destination Port Distribution - Bar plot
destination_port_counts = data['Destination Port'].value_counts()
sns.barplot(x=destination_port_counts.index, y=destination_port_counts.values, ax=axs[1, 1], palette="Greens_d")
axs[1, 1].set_title('Destination Port Distribution', fontsize=14)
axs[1, 1].set_xlabel('Port Number', fontsize=12)
axs[1, 1].set_ylabel('Frequency', fontsize=12)

# Rotate x-axis labels for readability
for label in axs[1, 1].get_xticklabels():
    label.set_rotation(45)
axs[1, 1].tick_params(axis='x', labelsize=10)

for i, v in enumerate(destination_port_counts.values):
    axs[1, 1].text(i, v + 0.1, str(v), ha='center', va='bottom')

# Top 10 Source IPs - Bar plot
source_ip_counts = data['Source IP'].value_counts().head(10)
sns.barplot(x=source_ip_counts.values, y=source_ip_counts.index, ax=axs[2, 0], palette="Reds_d")
axs[2, 0].set_title('Top 10 Source IP Addresses', fontsize=14)
axs[2, 0].set_xlabel('Frequency', fontsize=12)
axs[2, 0].set_ylabel('IP Address', fontsize=12)

# Top 10 Destination IPs - Bar plot
destination_ip_counts = data['Destination IP'].value_counts().head(10)
sns.barplot(x=destination_ip_counts.values, y=destination_ip_counts.index, ax=axs[2, 1], palette="Purples_d")
axs[2, 1].set_title('Top 10 Destination IP Addresses', fontsize=14)
axs[2, 1].set_xlabel('Frequency', fontsize=12)
axs[2, 1].set_ylabel('IP Address', fontsize=12)

# Rotate y-axis labels for better readability
for label in axs[2, 0].get_yticklabels():
    label.set_fontsize(10)
for label in axs[2, 1].get_yticklabels():
    label.set_fontsize(10)

# Increase layout padding
plt.tight_layout(pad=4.0)

plt.show()
