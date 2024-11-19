import pandas as pd
from datetime import datetime
from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import Select, ColumnDataSource 
from bokeh.plotting import figure

def avg_create_to_close(data):

    #convert start and end dates to datetime format
    start= pd.to_datetime(data[1])
    end = pd.to_datetime(data[2])

    #calculate total resolution time 
    resolution_time = (end - start).dt.total_seconds() / 3600

    #add to a new data frame 
    new_df = pd.DataFrame({'start_date': start, 
                           'end_date': end,
                           'resolution_time (hrs)': resolution_time})

    #group by month 
    new_df['end_month'] = new_df['end_date'].dt.month
   
    #get average resolution time per month 
    avg_res_per_month = new_df.groupby('end_month')['resolution_time (hrs)'].mean().reset_index()

    #create new columns for DataFrame 
    avg_res_per_month.columns = ['end_month', 'avg_res_time']

    return avg_res_per_month

def main():

    data = pd.read_csv('filtered_2020.csv', header=None)

    #filter out rows where cases aren't closed and no zipcode 
    data_clean = data.dropna(subset=[2,8])

    #monthly average incident create-to-closed times 
    avg_res_per_month = avg_create_to_close(data_clean)

    #grab data 
    src = ColumnDataSource(data=dict(month=['January', 'February', 'March', 'April', 'May', 'June',
                                            'July', 'August', 'September', 'October', 'November', 'December'], 
                                     avg_time=avg_res_per_month['avg_res_time']))

    #create plot 
    plot = figure(title="Monthly Average Resolution Time in NYC 2020", x_axis_label="Month", 
                  y_axis_label="Average Time (in Hours)", x_range=(1,12))

    #line that plots all 2020 data 
    plot.line('month', 'avg_time', source=src, legend_label='All Zipcodes')

    #zipcode drop downs 
    zip1 = Select(title= "zipcode 1", value="10001", options=sorted(set(data_clean[8].astype(str)))) #data_clean[5] is zipcode index 
    zip2 = Select(title= "zipcode 2", value="10002", options=sorted(set(data_clean[8].astype(str))))

    def update_plot():
    
        selected_zip1 = zip1.value
        selected_zip2 = zip2.value

        # group data by month for zip codes 
        zip1_data = data_clean[data_clean[8] == selected_zip1].groupby('month')['response_time'].mean().reset_index()
        zip2_data = data_clean[data_clean[8] == selected_zip2].groupby('month')['response_time'].mean().reset_index()

        #update source for dropdown 
        src.data = dict(
            month=avg_res_per_month['month'],
            avg_time=avg_res_per_month['response_time'],
            zip1_time=zip1_data['response_time'],
            zip2_time=zip2_data['response_time'],
        )

    #changes zip values 
    #zip1.on_change = ('value', update_plot)
    #zip2.on_change = ('value', update_plot)

    curdoc().add_root(column(zip1, zip2, plot))
    #curdoc().add_title("NYC Complaint Response Time 2020")


   

if __name__ == "__main__":
    main()