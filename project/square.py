import streamlit as st

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