# import streamlit as st
# from streamlit_modal import Modal
#
# import streamlit.components.v1 as components
#
# modal = Modal(
#     "Demo Modal",
#     key="demo-modal",
#
#     # Optional
#     padding=20,  # default value
#     max_width=744  # default value
# )
# open_modal = st.button("Open")
# if open_modal:
#     modal.open()
#
# if modal.is_open():
#     with modal.container():
#         st.write("Text goes here")
#
#         html_string = '''
#         <h1>HTML string in RED</h1>
#
#         <script language="javascript">
#           document.querySelector("h1").style.color = "red";
#         </script>
#         '''
#         components.html(html_string)
#
#         st.write("Some fancy text")
#         value = st.checkbox("Check me")
#         st.write(f"Checkbox checked: {value}")
import streamlit as st

color = st.color_picker("Pick A Color", "#00f900")
st.write("The current color is", color)
st.write("This is :blue[test]")
temperature = "-10"

st.write(f"temprature: :red[{temperature}]")
