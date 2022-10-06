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
add_data = st.sidebar.text_input(
    'Select number of coin flips'
)
add_pause = st.sidebar.text_input(
    'Select number to pause at'
)
add_time = st.sidebar.slider(
    'select seconds to pause',
    0,60
)
# add a play button to the sidebar
add_play_button = st.sidebar.button('Play')
if add_play_button:
    pause = int(add_pause)
    add_slider = int(add_data)
    latest_counter = st.empty()
    latest_iteration = st.empty()
    head_counter = st.empty()
    st.header('Data arranged in columns')
    sort_into_streaks = st.empty()
    st.header('Column positions and difference for streak number 1')
    st.write('column position')
    column_position_streak1 = st.empty()
    st.write('differences')
    difference = st.empty()
    st.header('Column positions for all streaks')
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
        df = pd.DataFrame(sorted_flips)
        df.index += 1
        sort_into_streaks.dataframe(df.fillna(''),use_container_width=True)
        def live():
            streaks = [len(i) for i in sorted_flips]
            no_of_times = []
            streak_no = []
            columns_data = []
            columns_avg_distance = []
            differences = []
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
                    differences.append(absolute)
                    sum_of_arr = np.sum(absolute)
                    if x <= 2:
                        avg_distance = sum_of_arr
                    else:
                        avg_distance = sum_of_arr/x
                    y = round(avg_distance, 2)
                    columns_avg_distance.append(y)
            df = pd.DataFrame(columns_data[0])
            df.index += 1
            column_position_streak1.dataframe(df.fillna(''),use_container_width=True)
            df = pd.DataFrame(differences[0])
            df.index += 1
            difference.dataframe(df.fillna(''),use_container_width=True)
            df = pd.DataFrame(columns_data)
            df.index = [i for i in streak_no]
            column_position.dataframe(df.fillna(''),use_container_width=True)
            df = pd.DataFrame(columns_avg_distance)
            df.index = [i for i in streak_no]
            average_distance.dataframe(df,use_container_width=True)
            df = pd.DataFrame(columns=[i for i in streak_no])
            for i in range(len(columns_data)):
                this_column = df.columns[i]
                df[this_column] = [len(columns_data[i])]
            streak_number.dataframe(df,use_container_width=True)
        live ()
        time.sleep(add_selectbox * 0.25)
        if i == (pause - 1):
            pause += int(add_pause)
            time.sleep(add_time)
