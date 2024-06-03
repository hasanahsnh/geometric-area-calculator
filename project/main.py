import streamlit as st
from triangle import Triangle
from square import Square
from circle import Circle

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
