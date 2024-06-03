import streamlit as st
import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    
    def calculate_area(self):
        return math.pi * (self.__radius ** 2)

    @staticmethod
    def calculate_circle_area():
        st.sidebar.subheader("Enter the dimensions of the circle")
        radius = st.sidebar.number_input("Radius", min_value=0.0, format="%f")
        if st.sidebar.button("Calculate Area"):
            circle = Circle(radius)
            area = circle.calculate_area()
            area = round(area, 2)
            st.success(f"The area of the circle is: {area} square units")