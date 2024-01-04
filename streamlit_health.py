# A streamlit app to keep track of wellbeing activities

import streamlit as st
from rich import print
from dotenv import load_dotenv
from datetime import datetime
from uuid import uuid4
import os

from helpers import google_sheets_connection, load_workout_data
from spaces_upload import upload_to_space

##
## -- Create Variables --
##

load_dotenv()

my_date = ""
page_names = ["Physical Health", "Mental Health", "Personal Growth", "Reps and Sets", "Food"]
username = "marquin"
gc = google_sheets_connection()


##
## -- Sidebar --
##

with st.sidebar:
    page = st.radio("Navigation", page_names, index=3)

    with st.expander("Expand for suggestion box"):
        with st.form("Suggestions", clear_on_submit=True):
            suggestion = st.text_area(label="Ideas how to make this app better:")
            submitted_suggestion = st.form_submit_button("Submit")

            if submitted_suggestion:
                print("logging the following suggestion:")
                print(suggestion)
                print()
                sh = gc.open("Wellness Log")
                worksheet = sh.worksheet("Suggestions")
                worksheet.append_row([suggestion, str(datetime.utcnow())])
                st.success(f"Saved suggestion of '{suggestion}'.")



##
## -- Physical health --
##


## right aligned "marquin smith" logo
col1, col2, col3 = st.columns(3)
with col3:
    st.image(
        "https://marquin-space-object-storage-01.sgp1.cdn.digitaloceanspaces.com/web-resources/FINAL%20LOGO%20LARGE%20OPTION%20DARK%20GREY%20FOR%20WEBSITE.png",
        width=100,
    )


if page == "Physical Health":

    # <--------------------- Weight Logger --------------------->
    with st.form("Weight Form", clear_on_submit=True):
        st.markdown("### Weight Tracker")
        weight_date = st.date_input(label="Date of recorded weight")
        weight = st.number_input(label="Weight in kgs", value=80.0)

        submitted = st.form_submit_button("Submit")

        if submitted:
            print("logging the following:")
            print(username)
            print(weight_date)
            print(weight)
            print()
            sh = gc.open("Weight Logs")
            worksheet = sh.worksheet("Sheet1")
            worksheet.append_row([username, str(weight_date), weight])
            st.success(f"Logged a weight of {weight} kgs on {weight_date}.")

    st.markdown("---")

    # <--------------------- Exercise Logger --------------------->
    exercise_list = [
        "Yoga",
        "Surfing",
        "Cycling",
        "Jogging",
        "Swimming",
        "Stair Walk",
        "Skipping"
    ]
    with st.form("Exercise Form", clear_on_submit=True):
        st.markdown("### Physical Exercise Tracker")
        exercise_date = st.date_input(label="Date of exercise performed")
        exercise = st.selectbox(label="Exercise performed", options=exercise_list)
        exercise_duration = st.number_input("Time spent (mins)", value=45)

        submitted = st.form_submit_button("Submit")

        if submitted:
            print("logging the following:")
            print(username)
            print(exercise_date)
            print(exercise)
            print()
            sh = gc.open("Wellness Log")
            worksheet = sh.worksheet("Sheet1")
            worksheet.append_row([username, exercise, str(exercise_date), exercise_duration])
            st.success(f"Logged {exercise_duration} mins of {exercise} on {exercise_date}.")

    st.markdown("---")

    # <--------------------- Movement Practice Logger --------------------->
    movement_practice_list = ["Handstand", "L-sit", "Pistol Squat", "Deep Squat"]
    with st.form("Movement Pattern Form", clear_on_submit=True):
        st.markdown("### Movement Pattern Tracker")
        movement_practice_date = st.date_input(label="Date of exercise performed")
        movement_practice = st.selectbox(
            label="Movement pattern practiced", options=movement_practice_list
        )

        submitted = st.form_submit_button("Submit")

        if submitted:
            print("logging the following:")
            print(username)
            print(movement_practice_date)
            print(movement_practice)
            print()
            sh = gc.open("Wellness Log")
            worksheet = sh.worksheet("movement_practice_log")
            worksheet.append_row(
                [username, movement_practice, str(movement_practice_date)]
            )
            st.success(f"Logged {movement_practice} on {movement_practice_date}.")

    st.markdown("---")






##
## -- Mental health --
##


if page == "Mental Health":

    # <--------------------- Mental Exercise Logger --------------------->
    mental_list = ["Meditation", "Poker Practice", "Cold Shower", "One meal a day"]
    with st.form("Mental Form", clear_on_submit=True):
        st.markdown("### Mental Exercise Tracker")
        mental_exercise_date = st.date_input(label="Date of mental activity performed")
        mental_exercise = st.selectbox(
            label="Mental Exercise performed", options=mental_list
        )

        submitted = st.form_submit_button("Submit")

        if submitted:
            print("logging the following:")
            print(username)
            print(mental_exercise_date)
            print(mental_exercise)
            print()
            sh = gc.open("Wellness Log")
            worksheet = sh.worksheet("mental_exercise")
            worksheet.append_row([username, mental_exercise, str(mental_exercise_date)])
            st.success(f"Logged {mental_exercise} on {mental_exercise_date}.")


##
## -- Personal Development --
##

# Reading (+ duration)
# Data Engineering
# Python

if page == "Personal Growth":

    # <--------------------- Personal Development Logger --------------------->
    growth_list = ["Reading", "Data Engineering", "Python", "Poker"]
    with st.form("Growth Form", clear_on_submit=True):
        st.markdown("### Personal Growth Activity Tracker")
        growth_exercise_date = st.date_input(label="Date of activity performed")
        growth_exercise = st.selectbox(
            label="Growth activity performed", options=growth_list
        )
        growth_duration = st.number_input("Time spent (mins)", value=45)

        submitted = st.form_submit_button("Submit")

        if submitted:
            print("logging the following:")
            print(username)
            print(growth_exercise_date)
            print(growth_exercise)
            print()
            sh = gc.open("Wellness Log")
            worksheet = sh.worksheet("personal_growth_log")
            worksheet.append_row(
                [username, growth_exercise, str(growth_exercise_date), growth_duration]
            )
            st.success(
                f"Logged {growth_duration} mins of {growth_exercise} on {growth_exercise_date}."
            )


##
## -- Reps and Sets --
##

if page == "Reps and Sets":

    # <--------------------- Strength Reps Logger --------------------->
    strength_list = [
        "Dips",
        "Pull ups",
        "Bodyweight Rows",
        "Chin ups",
        "Press ups",
        "Nordic Curls",
        "Squats",
        "Pistol Squats",
        "Handstand press",
        "Step ups",
        "Sprint",
        "Leg Raises",
        "Knee Raises",
    ]

    modifier_list = [
        "Rings",
        "Ring assisted",
        "Negative",
        "Close grip",
        "Wide grip",
        "False grip",
        "Weighted",
        "Band assisted",
        "Band resisted",
        "Parallettes"
    ]

    with st.form("Reps and Sets Form", clear_on_submit=False):
        st.markdown("### Reps and Sets Tracker")
        repsandsets_date = st.date_input(label="Date")
        reps = st.slider("Reps", min_value=1, max_value=15, value=8, step=1)
        repsandsets = st.selectbox(label="Exercise", options=strength_list)
        repsandsets_mods = st.multiselect("Modifier", modifier_list, [])

        submitted = st.form_submit_button("Submit")

        if submitted:
            print("logging the following:")
            print(username)
            print(repsandsets_date)
            print(reps)
            print(repsandsets)
            print(repsandsets_mods)
            print()
            sh = gc.open("Reps and Sets")
            worksheet = sh.worksheet("Sheet1")
            worksheet.append_row(
                [
                    username,
                    str(repsandsets_date),
                    reps,
                    repsandsets,
                    str(repsandsets_mods),
                    str(datetime.utcnow()),
                ]
            )
            st.success(f"Logged {reps} {repsandsets} on {str(repsandsets_date)}.")

    st.markdown("---")

    data = load_workout_data()

    # isolate latest workout data
    data_to_show = data[data["date"] == max(data["date"])]

    # how many total reps for each exercise
    reps_total = data_to_show.pivot_table(index="exercise", values="reps", aggfunc=sum)

    # how many total sets for each exercise
    sets_total = data_to_show.pivot_table(index="exercise", values="reps", aggfunc=len)

    with st.expander("Expand for details on current or most recent workout"):
        st.write("#### Current / most recent workout")
        st.write(f'#### {max(data["date"])}')
        for exercise in reps_total.index:
            total_exercise_reps = reps_total.loc[exercise, "reps"]
            total_exercise_sets = sets_total.loc[exercise, "reps"]
            st.write(
                f"Completed a total of __{total_exercise_reps}__ of __{exercise}__ in __{total_exercise_sets}__ sets."
            )

        st.info(
            "For effective muscle growth and strength building, a minimum of 15 reps per exercise is required."
        )

        st.write(data_to_show[["exercise", "reps", "modification"]])




if page == "Food":

    with st.form("Food Form", clear_on_submit=True):
        st.markdown("### Food Tracker")
        food_pic = st.camera_input(label="take a pic of the food")
        food_date = st.date_input(label="Date")
        vegetarian_flag = st.checkbox(label = "Vegetarian")
        vegan_flag = st.checkbox(label = "Vegan")
        food_description = st.text_area(label="Description")

        submitted = st.form_submit_button("Submit")

        if submitted:

            my_timestamp = str(datetime.utcnow())
            photo_id = str(uuid4())
            do_space = 'marquin-space-object-storage-01'
            upload_folder = "food-tracker-pics"

            my_filename = my_timestamp[0:10].replace("-","") + "|" + photo_id + ".jpg"
            print(my_filename)

            with open (my_filename, mode= 'wb') as f:
                f.write(food_pic.getbuffer())

            upload_to_space(file_name = my_filename, space_name = do_space , folder = upload_folder)
            os.remove(my_filename)



            print("logging the following:")
            print(username)
            print(food_date)
            print(upload_folder)
            print(my_filename)
            print(food_description)
            print(str(vegetarian_flag))
            print(str(vegan_flag))
            print()
            sh = gc.open("Weight Logs")
            worksheet = sh.worksheet("food_pics")
            worksheet.append_row(
                [
                    username,
                    str(food_date),
                    upload_folder,
                    my_filename,
                    str(datetime.utcnow()),
                    food_description,
                    str(vegetarian_flag),
                    str(vegan_flag)
                ]
            )
            st.success(f"Saved picture to Digital Ocean spaces folder {upload_folder} as {my_filename}.")
            

    # <--------------------- Time Restricted Eating Logger --------------------->
    with st.form("Time Restricted Form", clear_on_submit=True):
        st.markdown("### Breakfast Tracker")
        time_restricted_time = st.time_input(label = "Time of first meal")
        time_restricted_date = st.date_input(label="Date of recorded weight")

        submitted = st.form_submit_button("Submit")

        if submitted:
            print("logging the following:")
            print(username)
            print(time_restricted_time)
            print(time_restricted_date)
            print()
            sh = gc.open("Wellness Log")
            worksheet = sh.worksheet("time_restricted eating")
            worksheet.append_row([username, str(time_restricted_time), str(time_restricted_date), str(datetime.utcnow())])
            st.success(f"First meal of the day was at {time_restricted_time} on {time_restricted_date}.")