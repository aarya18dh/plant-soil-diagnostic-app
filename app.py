import streamlit as st
import requests

st.title("Plant and Soil Health Diagnostic System")

plant_image = st.file_uploader("Upload Plant Image", type=["jpg", "jpeg", "png"])
soil_report_image = st.file_uploader("Upload Soil Report Image", type=["jpg", "jpeg", "png"])

if st.button("Submit"):
    if not plant_image or not soil_report_image:
        st.warning("Please upload both the plant image and soil report image.")
    else:
        with st.spinner("Processing images and getting prediction..."):
            files = {
                'plant_image': (plant_image.name, plant_image, 'image/jpeg'),
                'soil_report_image': (soil_report_image.name, soil_report_image, 'image/jpeg'),
            }

            try:
                response = requests.post("https://your-backend-api.com/predict", files=files)

                if response.status_code == 200:
                    result = response.json()
                    suggested_pesticide = result.get("suggested_pesticide", "No suggestion received")

                    st.success("Prediction Complete!")
                    st.subheader("Suggested Pesticide:")
                    st.write(suggested_pesticide)
                else:
                    st.error(f"Error from backend: {response.status_code}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
