import csv
from contextlib import nullcontext
from datetime import datetime
import sys
from matplotlib import pyplot as plt

def get_weather_data(filename): # Take existing codebase from sitka_highs
    """Extract dates, high temps, and low temps from the CSV file."""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates, high temperatures, and low temperatures from this file.
        dates, highs, lows = [], [], [] # Include highs and lows
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            high = int(row[5])
            highs.append(high)
            low = int(row[6])  # Assuming column 6 contains low temperatures
            lows.append(low)
    
    return dates, highs, lows
    
def on_close(event): # Built an on_close for usage with mpl_connect later in plot_temperature
    print("\nThank you for using the Sitka Airport Weather Application. Goodbye!")
    sys.exit(0)

def plot_temperatures(dates, temps, color, title):
    """Plot temperature data."""
    fig, ax = plt.subplots()
    ax.plot(dates, temps, c=color)
    
    # Format plot.
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    # fig.canvas.mpl_connect('close_event', on_close) # Ensure the plot closes properly - Only use if running new shell
    # TODO How to go back to main menu option without duping code if python/matplot creates new window(shell)
    plt.show()

def display_menu():
    """Display the main menu."""
    print("\n=== Sitka Weather Data ===")
    print("1. View High Temperatures")
    print("2. View Low Temperatures") 
    print("3. Exit")
    print("==========================")

def main():
    """Main program loop."""
    filename = 'sitka_weather_2018_simple.csv'
    
    # Get all weather data
    dates, highs, lows = get_weather_data(filename)
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            print("\nDisplaying high temperatures...")
            plot_temperatures(dates, highs, 'red', "Daily High Temperatures - 2018")
        elif choice == '2':
            print("\nDisplaying low temperatures...")
            plot_temperatures(dates, lows, 'blue', "Daily Low Temperatures - 2018")
        elif choice == '3':
            on_close(nullcontext) # Close the application
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
