import streamlit as st

st.title("🧮 Calculator")

st.markdown("""
<style>
.calc-container {
    max-width: 400px;
    margin: auto;
}
</style>
""", unsafe_allow_html=True)

# 1. Create the calculator's "memory" so it doesn't forget the numbers
if "math_equation" not in st.session_state:
    st.session_state.math_equation = ""

# 2. Create simple functions to handle the button clicks
def add_to_calc(value):
    # This adds the clicked number/symbol to our memory string
    st.session_state.math_equation += str(value)

def calculate_result():
    try:
        # 'eval' is a built-in Python tool that automatically calculates a math string (like "7+5")
        result = eval(st.session_state.math_equation)
        st.session_state.math_equation = str(result)
    except:
        st.session_state.math_equation = "Error"

def clear_calc():
    # This empties the memory
    st.session_state.math_equation = ""

# 3. The Calculator Screen (Using st.info for a nice blue box)

st.text_input(
    label="Calculator Display",
    label_visibility="collapsed",
    key="math_equation",
    on_change=calculate_result,
    placeholder="0"
)

# 4. The Buttons Grid (Using 4 columns to put buttons side-by-side)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button("7", on_click=add_to_calc, args=("7",), use_container_width=True)
    st.button("4", on_click=add_to_calc, args=("4",), use_container_width=True)
    st.button("1", on_click=add_to_calc, args=("1",), use_container_width=True)
    st.button("C", on_click=clear_calc, use_container_width=True )

with col2:
    st.button("8", on_click=add_to_calc, args=("8",), use_container_width=True)
    st.button("5", on_click=add_to_calc, args=("5",), use_container_width=True)
    st.button("2", on_click=add_to_calc, args=("2",), use_container_width=True)
    st.button("0", on_click=add_to_calc, args=("0",), use_container_width=True)

with col3:
    st.button("9", on_click=add_to_calc, args=("9",), use_container_width=True)
    st.button("6", on_click=add_to_calc, args=("6",), use_container_width=True)
    st.button("3", on_click=add_to_calc, args=("3",), use_container_width=True)
    st.button("=", on_click=calculate_result, use_container_width=True)

with col4:
    st.button("/", on_click=add_to_calc, args=("/",), use_container_width=True)
    st.button("x", on_click=add_to_calc, args=("*",), use_container_width=True)
    st.button("--", on_click=add_to_calc, args=("-",), use_container_width=True)
    st.button(":heavy_plus_sign:", on_click=add_to_calc, args=("+",), use_container_width=True) 