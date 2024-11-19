import pandas as pd 
import matplotlib.pyplot as plt

"""
Function that finds and counts the different noise complaint types and returns a pivot table  
"""
def find_noise_complaint_types(df):

    complaint_type = df.iloc[:,5]

    #filter complaint types to be those that contain the word 'noise'
    noise_complaints = df[complaint_type.str.contains("noise", case=False, na=False)]

    #extract types of noise complaints and add to data frame 
    df['Noise Type'] = noise_complaints.iloc[:, 5].str.split("-").str[1]

    #count how many times a noise complaint occurs per month 
    df['Month'] = df.iloc[:,2].str.split("/").str[0] #month that complaint is filed 
    noise_by_month = df.groupby(['Month', 'Noise Type']).size().reset_index(name="Count")

    #create a pivot table from the data frame using pandas 
    table = noise_by_month.pivot_table(index= 'Month', columns= 'Noise Type', values='Count', fill_value=0)
    return table

def noise_plot(pivot_table):

    #plot pivot table 
    pivot_table.plot(kind='bar', stacked=False, colormap='tab10')

    plt.title('Noise Complaint Types by Month in NYC in 2020')
    plt.xlabel('Month')
    plt.ylabel('Number of Complaints')
    plt.xticks(rotation=0)
    plt.legend(title="Noise Type")

    plt.show()



def main():
    

    #filter them based on type 

    #collect data by month 

    df = pd.read_csv('filtered_2020.csv')
    
    #filter complaints by noise complaint type and month occured 
    noise_by_month = find_noise_complaint_types(df)

    #generate plot 
    noise_plot(noise_by_month)

    
if __name__ == "__main__":
    main()