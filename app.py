import streamlit as st
def display(text, font="sans-serif", color="white", size="25px"):
    st.markdown(
        f'<p style="font-family:{font}; color:{color}; font-size: {size};">{text}</p>',
        unsafe_allow_html=True,
    )

st.image('https://www.ar8ar.com/wp-content/uploads/2022/10/%D8%AC%D8%AF%D8%A7%D8%B1%D8%A7%D8%AA.png')
st.markdown("<h1 style='color: #a38d62;'>Jadarat</h1>", unsafe_allow_html=True)

st.write("Among the thousands of job postings,  Imagine having the power to navigate through opportunities, discovering the most sought-after skills and emerging trends. These statistics are the key to unlocking possibilities, helping companies fine-tune recruitment strategies and make informed decisions. Whether you're a hiring manager or a job seeker, job posting statistics offer valuable information to guide your journey. So, dive into the data and set sail toward success in the world of work")


st.image('Region.png')


st.write("According to Jadarat, most job postings are located in the Riyadh region, secondly in the Makkah Al-Mukarramah region, and thirdly in the Eastern Province. This indicates the abundance of job opportunities in Riyadh, it is the capital of the Kingdom of Saudi Arabia and most of the main headquarters are located there. Its population is high compared to other regions")


st.image('exper.png')



st.write("The chart reveals the distribution of job postings across different years of experience. By comparing the counts of job postings in each category for fresh graduates and those with more than 1 year of experience, trends in job market demand and hiring preferences can be identified. so Most job postings target fresh graduates.") 


st.image('Genders.png')


st.write("According to the chart, job postings are categorized by gender preferences: male, female, or open to all genders. It may shed light on how employers prioritize gender diversity in their hiring practices. The inclusion of all genders in job postings indicates an inclusive approach to hiring the best candidates.")


st.image('Salary.png')


st.write("The chart shows the central tendency of starting salaries for fresh graduates, highlighting the median or average salary as well as the spread . The chart allows employers to benchmark their salary offerings against industry standards and competitors, ensuring they remain competitive in attracting top talent.")



st.markdown("<h1 style='color: #a38d62;'>Conclusion</h1>", unsafe_allow_html=True)


st.write("Overall, these insights illustrate the dynamic nature of the job market, focusing on both talent acquisition and diversity. Employers can leverage this information to refine their recruitment strategies, attract top talent, and maintain a competitive edge in the ever-evolving landscape of employment. Similarly, job seekers can use these insights to align their skills and preferences with market demands, thereby enhancing their job search and career prospects.")
