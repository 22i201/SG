import tkinter as tk
from tkinter import messagebox
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import deque

class ITAsset:
    def __init__(self, asset_id, asset_type, status):
        self.asset_id = asset_id
        self.asset_type = asset_type
        self.status = status
        self.usage_history = []

    def update_status(self, new_status):
        self.status = new_status
        self.usage_history.append(new_status)

class NetworkMonitor:
    def __init__(self):
        self.network_status = "Healthy"
        self.network_usage = deque(maxlen=50)  # Limit usage history for plotting

    def simulate_network_usage(self):
        usage = random.randint(50, 100)
        self.network_usage.append(usage)
        return usage

    def predictive_analysis(self):
        print(f"DEBUG: Current network usage: {list(self.network_usage)}")  # Debug statement
        if len(self.network_usage) < 5:
            return "Insufficient data for prediction"
        try:
            avg_usage = sum(list(self.network_usage)[-5:]) / 5
        except Exception as e:
            print(f"DEBUG: Error in predictive_analysis: {e}")
            return "Error in analysis"  # Handle exception gracefully
        if avg_usage > 80:
            return "High network usage detected, potential issues anticipated."
        else:
            return "Network usage is within normal range."

class ITAssetManager:
    def __init__(self):
        self.assets = []

    def add_asset(self, asset):
        self.assets.append(asset)

    def optimize_resources(self):
        optimized_assets = []
        for asset in self.assets:
            if asset.status == "Underutilized":
                asset.update_status("Optimized")
                optimized_assets.append(asset.asset_id)
        return optimized_assets

    def lifecycle_management(self):
        retired_assets = []
        for asset in self.assets:
            if asset.status == "End of Life":
                self.assets.remove(asset)
                retired_assets.append(asset.asset_id)
        return retired_assets

def add_asset():
    asset_id = entry_asset_id.get()
    asset_type = entry_asset_type.get()
    status = entry_status.get()
    asset = ITAsset(asset_id, asset_type, status)
    asset_manager.add_asset(asset)
    messagebox.showinfo("Asset Management", f"Added asset: {asset_id}")

def simulate_usage():
    usage = network_monitor.simulate_network_usage()
    label_usage.config(text=f"Network usage recorded: {usage}%")

    # Update network usage plot
    update_network_plot()

def analyze_network():
    result = network_monitor.predictive_analysis()
    label_analysis.config(text=f"Predictive Analysis Result: {result}")

def optimize_resources():
    optimized = asset_manager.optimize_resources()
    listbox_optimized.delete(0, tk.END)
    for asset_id in optimized:
        listbox_optimized.insert(tk.END, asset_id)

def manage_lifecycle():
    retired = asset_manager.lifecycle_management()
    listbox_retired.delete(0, tk.END)
    for asset_id in retired:
        listbox_retired.insert(tk.END, asset_id)

def update_network_plot():
    ax.clear()
    ax.plot(range(len(network_monitor.network_usage)), network_monitor.network_usage, marker='o', linestyle='-', color='b')
    ax.set_title('Network Usage')
    ax.set_xlabel('Time')
    ax.set_ylabel('Usage (%)')
    canvas.draw()

def auto_analyze_network():
    # Simulate network usage
    network_monitor.simulate_network_usage()

    # Perform predictive analysis
    result = network_monitor.predictive_analysis()
    label_auto_analysis.config(text=f"Auto Analysis Result: {result}")

# Initialize main components
network_monitor = NetworkMonitor()
asset_manager = ITAssetManager()

# Setup GUI
root = tk.Tk()
root.title("IT Asset Management System")

frame_asset = tk.Frame(root)
frame_asset.pack(padx=10, pady=10)

label_asset_id = tk.Label(frame_asset, text="Asset ID:")
label_asset_id.grid(row=0, column=0)
entry_asset_id = tk.Entry(frame_asset)
entry_asset_id.grid(row=0, column=1)

label_asset_type = tk.Label(frame_asset, text="Asset Type:")
label_asset_type.grid(row=1, column=0)
entry_asset_type = tk.Entry(frame_asset)
entry_asset_type.grid(row=1, column=1)

label_status = tk.Label(frame_asset, text="Status:")
label_status.grid(row=2, column=0)
entry_status = tk.Entry(frame_asset)
entry_status.grid(row=2, column=1)

button_add_asset = tk.Button(frame_asset, text="Add Asset", command=add_asset)
button_add_asset.grid(row=3, columnspan=2, pady=10)

frame_network = tk.Frame(root)
frame_network.pack(padx=10, pady=10)

button_simulate_usage = tk.Button(frame_network, text="Simulate Network Usage", command=simulate_usage)
button_simulate_usage.pack()

label_usage = tk.Label(frame_network, text="")
label_usage.pack()

button_analyze_network = tk.Button(frame_network, text="Manual Analysis", command=analyze_network)
button_analyze_network.pack()

label_analysis = tk.Label(frame_network, text="")
label_analysis.pack()

button_auto_analyze_network = tk.Button(frame_network, text="Auto Analyze", command=auto_analyze_network)
button_auto_analyze_network.pack()

label_auto_analysis = tk.Label(frame_network, text="")
label_auto_analysis.pack()

# Matplotlib setup for network usage plot
fig, ax = plt.subplots(figsize=(6, 4))
canvas = FigureCanvasTkAgg(fig, master=frame_network)
canvas.get_tk_widget().pack()

frame_optimize = tk.Frame(root)
frame_optimize.pack(padx=10, pady=10)

button_optimize_resources = tk.Button(frame_optimize, text="Optimize Resources", command=optimize_resources)
button_optimize_resources.pack()

listbox_optimized = tk.Listbox(frame_optimize)
listbox_optimized.pack()

frame_lifecycle = tk.Frame(root)
frame_lifecycle.pack(padx=10, pady=10)

button_manage_lifecycle = tk.Button(frame_lifecycle, text="Manage Lifecycle", command=manage_lifecycle)
button_manage_lifecycle.pack()

listbox_retired = tk.Listbox(frame_lifecycle)
listbox_retired.pack()

# Run the Tkinter main loop
root.mainloop()
