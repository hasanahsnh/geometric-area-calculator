import streamlit as st

class Triangle:
    def __init__(self, base, height):
        self.__base = base
        self.__height = height
    
    def calculate_area(self):
        return 0.5 * self.__base * self.__height
    
    @staticmethod
    def calculate_triangle_area():
        st.sidebar.subheader("Enter the dimensions of the triangle")
        base = st.sidebar.number_input("Base", min_value=0.0, format="%f")
        height = st.sidebar.number_input("Height", min_value=0.0, format="%f")
        if st.sidebar.button("Calculate Area"):
            triangle = Triangle(base, height)
            area = triangle.calculate_area()
            st.success(f"The area of the triangle is: {area} square units")
