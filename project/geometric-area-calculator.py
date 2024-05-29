import streamlit as st
import math

# Definisi class
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

class Square:
    def __init__(self, side):
        self.__side = side
    
    def calculate_area(self):
        return self.__side ** 2
    
    @staticmethod
    def calculate_square_area():
        st.sidebar.subheader("Enter the dimensions of the square")
        side = st.sidebar.number_input("Side", min_value=0.0, format="%f")
        if st.sidebar.button("Calculate Area"):
            square = Square(side)
            area = square.calculate_area()
            st.success(f"The area of the square is: {area} square units")


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

    
def main():
    st.title("Geometric Area Calculator")
    
    shape = st.sidebar.selectbox("Choose a shape", ("Triangle", "Square", "Circle"))
    
    if shape == "Triangle":
        Triangle.calculate_triangle_area()
    elif shape == "Square":
        Square.calculate_square_area()
    elif shape == "Circle":
        Circle.calculate_circle_area()

    st.sidebar.write("Select a shape and enter its dimensions to calculate the area.")

if __name__ == "__main__":
    main()
