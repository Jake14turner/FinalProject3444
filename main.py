import streamlit as st
st.set_page_config(layout="wide")

registerPage = st.Page("registerPage.py", title="Register", icon=":material/person_add:")
loginPage = st.Page("loginPage.py", title="Login", icon=":material/login:")
homePage = st.Page("homePage.py", title="Home", icon=":material/calendar_today:")
toDoPage = st.Page("todoPage.py", title="To Do List", icon=":material/note:")
customSchedulePage = st.Page("customSchedulePage.py", title="Custom Schedule", icon=":material/access_time:")
tasksPage = st.Page("tasksPage.py", title="Tasks Page", icon=":material/add_circle:")
logoutPage = st.Page("logoutPage.py", title="Logout Page", icon=":material/logout:")
overviewPage = st.Page("overviewPage.py", title="Over view Page")
assignmentWorkflowPage = st.Page("assignmentWorkflowPage.py", title="Assignment Work Flow Page")

#idkyetPage = st.Page("idkyet.py", title="idk yet", icon=":material/pie_chart:")


pg = st.navigation([registerPage, loginPage, homePage, toDoPage, tasksPage, customSchedulePage, overviewPage, assignmentWorkflowPage, logoutPage], position="hidden")

pg.run()


