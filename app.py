import streamlit as st
import requests

# App Title
st.title("Plant and Soil Health Diagnostic System")

# Upload Plant Image
plant_image = st.file_uploader("Upload Plant Image", type=["jpg", "jpeg", "png"])

# Upload Soil Report Image
soil_report_image = st.file_uploader("Upload Soil Report Image", type=["jpg", "jpeg", "png"])

# Input fields for Soil Nutrient Values (in ppm)
st.subheader("Soil Nutrient Values (ppm)")
nitrogen = st.number_input("Nitrogen (N)", min_value=0, step=1)
phosphorous = st.number_input("Phosphorous (P)", min_value=0, step=1)
potassium = st.number_input("Potassium (K)", min_value=0, step=1)
calcium = st.number_input("Calcium (Ca)", min_value=0, step=1)
magnesium = st.number_input("Magnesium (Mg)", min_value=0, step=1)

# Submit Button
if st.button("Submit"):
    if not plant_image or not soil_report_image:
        st.warning("Please upload both the plant image and soil report image.")
    else:
        with st.spinner("Processing images and nutrient data..."):
            # Prepare files for upload
            files = {
                'plant_image': (plant_image.name, plant_image, 'image/jpeg'),
                'soil_report_image': (soil_report_image.name, soil_report_image, 'image/jpeg'),
            }

            # Prepare nutrient values in payload
            data = {
                'nitrogen': nitrogen,
                'phosphorous': phosphorous,
                'potassium': potassium,
                'calcium': calcium,
                'magnesium': magnesium
            }

            try:
                # Replace with your actual backend API URL
                response = requests.post(
                    "https://your-backend-api.com/predict",
                    files=files,
                    data=data
                )

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

