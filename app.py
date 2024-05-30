import streamlit as st
import requests
import streamlit as st


st.markdown(
    """
    <style>
    .reportview-container {
        background: linear-gradient(to right, #4b6cb7, #182848);
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Streamlit app
st.markdown("<span style='font-size: 28px;'>⚽Football Player Value Predictor⚽</span>", unsafe_allow_html=True)

st.markdown("<span style='font-size: 20px;'>📊 Player Attributes</span>", unsafe_allow_html=True)
# Define the API endpoint
#url = 'https://uc7-api-2.onrender.com/'


age=st.number_input(" player age ", value=None, placeholder="Enter the player age please")
appearance=st.number_input("Appearance ", value=None, placeholder="Enter the time of appearance please")
minutes_played=st.number_input("minutes_played ", value=None, placeholder="Enter minutes of play please")
highest_value=st.number_input("highest_value ", value=None, placeholder="Enter highest value please")

input = {
     "age": age,
          "appearance": appearance,
          "minutes_played": minutes_played,
          "highest_value": highest_value
 }


if st.button('Get Prediction'):
    try:
        res = requests.post(
            url="https://uc7-api-2.onrender.com/predict",
            headers={"Content-Type": "application/json"},
            data=json.dumps(inputs)
        )
        res.raise_for_status()  # Check for HTTP request errors
        st.subheader(f"Prediction result 🚀 = {res.json()}")

    except requests.exceptions.RequestException as e:
        st.error(f"HTTP Request failed: {e}")
    except ValueError as e:
        st.error(f"Failed to parse JSON response: {e}")


# # Make the API call
#  response = requests.get(url, params=params)
#  print(response.json())

# def fetch_data(type):
#     with st.spinner("Working..."):
#         ### prepare API key and URL
#         api_key = st.secrets["rnd_MrLtgi0C13M99vvyKr526k74wRPU"]
#         api_url = f"https://uc7-api-2.onrender.com{type}"

#         ### invoke API and get the response
#         response = requests.get(url=api_url, headers={"X-Api-Key": api_key})
#         if response.status_code == requests.codes.ok:
#             ### Convert data to JSON format
#             data = jsonify(response)
#             status = "OK"
#         else:
#             data = {"code": response.status_code, "message": response.text}
#             status = "ERROR"
#     return status, data


# def display(text, font="sans-serif", color="white", size="25px"):
#     st.markdown(
#         f'<p style="font-family:{font}; color:{color}; font-size: {size};">{text}</p>',
#         unsafe_allow_html=True,
#     )

# st.image('https://www.ar8ar.com/wp-content/uploads/2022/10/%D8%AC%D8%AF%D8%A7%D8%B1%D8%A7%D8%AA.png')
# st.markdown("<h1 style='color: #a38d62;'>Jadarat</h1>", unsafe_allow_html=True)

# st.write("Among the thousands of job postings,  Imagine having the power to navigate through opportunities, discovering the most sought-after skills and emerging trends. These statistics are the key to unlocking possibilities, helping companies fine-tune recruitment strategies and make informed decisions. Whether you're a hiring manager or a job seeker, job posting statistics offer valuable information to guide your journey. So, dive into the data and set sail toward success in the world of work")


# st.image('Region.png')


# st.write("According to Jadarat, most job postings are located in the Riyadh region, secondly in the Makkah Al-Mukarramah region, and thirdly in the Eastern Province. This indicates the abundance of job opportunities in Riyadh, it is the capital of the Kingdom of Saudi Arabia and most of the main headquarters are located there. Its population is high compared to other regions")


# st.image('exper.png')



# st.write("The chart reveals the distribution of job postings across different years of experience. By comparing the counts of job postings in each category for fresh graduates and those with more than 1 year of experience, trends in job market demand and hiring preferences can be identified. so Most job postings target fresh graduates.") 


# st.image('Genders.png')


# st.write("According to the chart, job postings are categorized by gender preferences: male, female, or open to all genders. It may shed light on how employers prioritize gender diversity in their hiring practices. The inclusion of all genders in job postings indicates an inclusive approach to hiring the best candidates.")


# st.image('Salary.png')


# st.write("The chart shows the central tendency of starting salaries for fresh graduates, highlighting the median or average salary as well as the spread . The chart allows employers to benchmark their salary offerings against industry standards and competitors, ensuring they remain competitive in attracting top talent.")



# st.markdown("<h1 style='color: #a38d62;'>Conclusion</h1>", unsafe_allow_html=True)


# st.write("Overall, these insights illustrate the dynamic nature of the job market, focusing on both talent acquisition and diversity. Employers can leverage this information to refine their recruitment strategies, attract top talent, and maintain a competitive edge in the ever-evolving landscape of employment. Similarly, job seekers can use these insights to align their skills and preferences with market demands, thereby enhancing their job search and career prospects.")
