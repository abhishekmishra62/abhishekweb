import streamlit as str
import numpy as np
import plotly.express as pe

str.title("Welcome to Streamlit")
str.subheader("Power")
str.checkbox("testing")
x=str.number_input("Enter a number",value=0,format="%d")
y=str.number_input("Enter the exponent ",value=0,format="%d")
if str.button("press  here"):
    result=x*y
    str.write(f"{x} power {y} is {result}")

    
str.title("Plotting number graph")
x=str.number_input("Enter starting range", value=0,format="%d")
y=str.number_input("Enter last range" ,value=0,format="%d")
z=x=str.number_input("Enter power" ,value=0,format="%d")
if str.button("Graph"):
    x1=np.linspace(x,y,1000000)
    y1=[i**z for i in x1]
    fig=pe.line(x=x1,y=y1)
    str.plotly_chart(fig)
