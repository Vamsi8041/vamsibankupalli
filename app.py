import streamlit as st
from PIL import Image

# Mock database of products
PRODUCTS = [
    {
        "id": 1,
        "name": "Product 1",
        "price": 550,
        "description": "This is the first product.",
        "image": "product1.jpg",  
    },
    {
        "id": 2,
        "name": "Product 2",
        "price": 720,
        "description": "This is the second product.",
        "image": "product2.jpg",
    },
    {
        "id": 3,
        "name": "Product 3",
        "price": 707,
        "description": "This is the third product.",
        "image": "product3.jpg",
    },
    {
        "id": 4,
        "name": "Product 4",
        "price": 800,
        "description": "This is the third product.",
        "image": "product5.jpg",
        

    }
]

def main():
    st.title("E-store")

    # Navigation
    nav = st.sidebar.radio("Navigation", ["Home", "Shop", "Cart"])

    if nav == "Home":
        st.header("Welcome to BookBrowse.com")
        st.write("Explore our products and start shopping.")

        video_url = "intro.mp4"

    
        st.video(video_url)


        st.header('TEAM')
        image1 =  Image.open('sai.png')
        image2 =  Image.open('vamsi.png')
        image3 =  Image.open('mahesh.png')
        image4 =  Image.open('sais.png')
        image5 =  Image.open('abhi.png')
        image6 =  Image.open('ima.jpeg')
    
        col1, col2, col3 = st.columns(3)
      
        with col1:
            st.image(image1, use_column_width=True, caption="sai(leader)")
    
        with col2:
              st.image(image2, use_column_width=True, caption="vamsi")
    
        with col3:
             st.image(image3, use_column_width=True, caption="mahesh")
        
        col4, col5 = st.columns(2)
        with col4:
            st.image(image4, use_column_width=True, caption="sai surya")
        with col5:
            st.image(image5, use_column_width=True, caption="abhi")
        with st.container():
            st.write("---")
            st.header("under the guideance of:")
            image_col,text_col=st.columns((1,2))
            with image_col:
                st.image(image6)
            with text_col:
                st.subheader("Dr.P.kanchanamala")
                st.subheader("Associate Professer in CSE")
                st.subheader("GMR Institute of Technology")
                st.write("[profile>](https://gmrit.edu.in/profile.php?pernumber=50971)")


    elif nav == "Shop":
        st.header("Shop")

        for product in PRODUCTS:
            st.subheader(product["name"])

            # Display existing product image if available
            if product["image"]:
                image = Image.open(product["image"])
                st.image(image, use_column_width=True)

            st.write(product["description"])
            st.write(f"Price:  ₹{product['price']}")
            if st.checkbox("Add to Cart", key=f"add_to_cart_{product['id']}"):
                add_to_cart(product)
            st.write("---")

    elif nav == "Cart":
        st.header("Shopping Cart")

        items = get_cart_items()

        if not items:
            st.write("Your cart is empty.")
        else:
            for item in items:
                st.subheader(item["name"])

                # Display product image from file name
                if item["image"]:
                    image = Image.open(item["image"])
                    st.image(image, use_column_width=True)

                st.write(f"Price:  ₹{item['price']}")
                st.write("---")

            total_price = calculate_total(items)
            st.subheader(f"Total:  ₹{total_price}")
            if st.button("Checkout"):
                checkout()

def add_to_cart(product):
    cart = st.session_state.get("cart", [])
    cart.append(product)
    st.session_state["cart"] = cart

def get_cart_items():
    return st.session_state.get("cart", [])

def calculate_total(items):
    total = sum(item["price"] for item in items)
    return total

def checkout():
    st.success("Checkout successful!")
    st.session_state["cart"] = []


main()