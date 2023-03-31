import streamlit as st

st.set_page_config(layout="wide")

st.sidebar.title("About")
st.sidebar.info(
    """
    - GitHub repository: <https://github.com/Kestener/celerleve-sentinel>
    """
)

st.sidebar.title("Contact")
st.sidebar.info(
    """
    [LinkedIn](https://www.linkedin.com/in/kestener/)
    [GitHub](https://github.com/Kestener)
    """
)

st.title("Identifying Landslides with Satellite Imagery")

st.markdown(
    """
    This web app implements an inference tool to identify landslides using aerial and satellite images.
    This is an open-source project and you are very welcome to contribute your comments, questions, resources, and apps as [issues](https://github.com/Kestener/celerleve-sentinel/issues) or 
    [pull requests](https://github.com/Kestener/celerleve-sentinel/pulls) to the [GitHub repository](https://github.com/Kestener/celerleve-sentinel).
    Please check the references for a list of libraries, references, and inspirations behind this application.

    """
)

st.info("Use the left sidebar menu to navigate to the different apps.")

st.subheader("Timelapse of Satellite Imagery")
st.markdown(
    """
    The following timelapse animations were created using the Timelapse web app. Click `Timelapse` on the left sidebar menu to create your own timelapse for any location around the globe.
"""
)

row1_col1, row1_col2 = st.columns(2)
with row1_col1:
    st.image("../data/timelapse/brazil_sao_sebastiao_2023_3.gif")
    st.image("../data/images/saopaulo_mudslide_road2023.jpg")

with row1_col2:
    st.image("../data/timelapse/brazil_sao_sebastiao_2023_4.gif")
    st.image("../data/images/saopaulo_mudslide_buildings2023.jpg")
