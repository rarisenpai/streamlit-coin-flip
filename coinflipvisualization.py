import streamlit as st
import numpy as np
import pandas as pd
import time

st.title("Coin flip visualization app")
st.sidebar.header("App settings")
# Add a selectbox to the sidebar

add_selectbox = st.sidebar.selectbox(
    'What speed would you like to have?',
    (1,2,3,4)
)

# Add a slider to the sidebar:
add_slider = int(st.sidebar.text_input(
    'Select number of coin flips'
))
# add a play button to the sidebar
add_play_button = st.sidebar.button('Play')
if add_play_button:
    latest_counter = st.empty()
    latest_iteration = st.empty()
    head_counter = st.empty()
    st.header('Data arranged in columns')
    sort_into_streaks = st.empty()
    st.header('Column positions based on streak number')
    column_position = st.empty()
    st.header('Average distance between the streaks')
    average_distance = st.empty()
    st.header('Number of streaks')
    streak_number = st.empty()
    rolls = []
    for i in range(add_slider):
        letters = ['H','T']
        x = np.random.choice(letters)
        rolls.append(x)
        heads = rolls.count('H')
        length = len(rolls)
        latest_counter.text(f'Coin Flip # {i + 1}')
        latest_iteration.text(f'{x}')
        head_counter.text(f'Heads = {heads}/{length} = {heads/length}')
        sorted_flips = []
        for roll in rolls:
            streak = []
            if not sorted_flips:
                streak.append(roll)
                sorted_flips.append(streak)
            else:
                if sorted_flips[-1][-1] == roll:
                    sorted_flips[-1].append(roll)
                else:
                    streak.append(roll)
                    sorted_flips.append(streak)
        df = pd.DataFrame(columns= [i + 1 for i in range(len(sorted_flips))])
        for i in range(len(sorted_flips)):
            this_column = df.columns[i]
            df[this_column] = [''.join(sorted_flips[i])]
        sort_into_streaks.table(df)
        def live():
            streaks = [len(i) for i in sorted_flips]
            no_of_times = []
            streak_no = []
            columns_data = []
            columns_avg_distance = []
            for streak in range(1, max(streaks)+1):
                if streak in streaks:
                    streak_no.append(streak)
                    columns_minus_1 = [z for z in range(
                        len(streaks)) if streaks[z] == streak]
                    columns = np.array(columns_minus_1)+1
                    column_string = [str(i) for i in columns.tolist()]
                    columns_data.append(column_string)
                    no_of_times.append(len(columns))
                    x = int(len(columns))
                    diff = np.diff(columns)
                    absolute = abs(diff)
                    sum_of_arr = np.sum(absolute)
                    if x <= 2:
                        avg_distance = sum_of_arr
                    else:
                        avg_distance = sum_of_arr/x
                    y = round(avg_distance, 2)
                    columns_avg_distance.append(y)
            df = pd.DataFrame(columns=[i for i in streak_no])
            for i in range(len(columns_data)):
                this_column = df.columns[i]
                df[this_column] = [('  '.join(columns_data[i]))]
            column_position.table(df)
            df = pd.DataFrame(columns=[i for i in streak_no])
            for i in range(len(columns_avg_distance)):
                this_column = df.columns[i]
                df[this_column] = [(columns_avg_distance[i])]
            average_distance.table(df)
            df = pd.DataFrame(columns=[i for i in streak_no])
            for i in range(len(columns_data)):
                this_column = df.columns[i]
                df[this_column] = [len(columns_data[i])]
            streak_number.table(df)
        live ()
        time.sleep(add_selectbox * 0.25)





