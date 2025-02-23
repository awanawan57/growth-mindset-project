#streamlit
import streamlit as st
st.set_page_config(page_title="growth mindset challenge",page_icon="★")
st.title("Growth Mindset Challenge :web app with streamlit")

st.markdown("🚀Welcome To Your Growth Journey!")
st.markdown("Success is not about being the best,it's about getting better everday!✨") 

#quote section
st.header("💡Today's growth mindset Quote")
st.write("Success is not final,failure is not fatel:it is the courage to continue that counts. _wistnston churchill")

st.header("What's Your Challenge Today?")
user_input=st.text_input("Describe a challenge your'e facing:")


#condition 
if user_input:
    st.success(f"💪your'e facing:{user_input}.keep pushing forward toward your goal!🚀")
else:
        st.warning("Tell us about your challenge to get started!")

#reflexing
st.header("Reflect on your learning")
reflection=st.text_area("write your reflections here:")

if reflection:
    st.success(f"✨Great Insight!Your reflection:{reflection}")
else:
    st.info("Reflecting on past experience help you grow!share your difficulties")    


 #achievement
st.header("🏆Celebrate your wins!")
achievement=st.text_input("share something you've recently accomplished:")


if achievement:
    st.success(f"🌟Amazing!you achieved:Amazing!you achieved:{achievement}")

else:   
    st.info("Big or small,every achievement counts!share one now😍")    


#footer
st.write("- - -")
st.write("🚀keep believing in yourself.growth is a journey ,not a destination!")
st.write("⛔created by ifrah ali")