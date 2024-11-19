import pandas as pd 
import matplotlib.pyplot as plt 


def main():
    df = pd.read_csv('filtered_2020.csv')
    building = df.iloc[:,7]
    complaints = df.iloc[:,5]

    #gives rodent sanitation complaint conditions and where they occur 
    sanitation = df[complaints.str.contains("rodent", case= False, na=False)].iloc[:,[5,7]].dropna()



    #find types of buildings
    buildings_filtered = df[building.str.contains("Building", case=False, na=False)]
    building_types = buildings_filtered.iloc[:,7].str.split(" ").str[0]


    #create plot 
    plot_data = sanitation.value_counts()
    
    plot_buildings = plot_data.index.get_level_values(1).to_list()
    plot_values = plot_data.values

    plt.bar(plot_buildings, plot_values)
    plt.xlabel('Building and Location Types')
    plt.ylabel('Number of Rodent Sanitation Complaint')
    plt.title('Difference in Rodent Sanitation Complaints in Various Buildings in NYC in 2020')
    plt.xticks(rotation=90)
    

    plt.show() 

if __name__ == "__main__":
    main()