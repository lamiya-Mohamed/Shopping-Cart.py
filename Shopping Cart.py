import streamlit as st

st.set_page_config(page_title="Shopping Cart", page_icon="🛒", layout="centered")

# تخزين البيانات في session_state علشان تفضل موجودة طول ما البرنامج شغال
if "products" not in st.session_state:
    st.session_state.products = []

if "cart" not in st.session_state:
    st.session_state.cart = []


st.title("🛒 Shopping Cart - Streamlit Version")

st.sidebar.header("القائمة الرئيسية")
menu = st.sidebar.radio(
    "اختار العملية",
    ["إضافة منتج", "عرض المنتجات", "إضافة للسلة", "عرض السلة", "حذف منتج من السلة"]
)


# الخيار 1: إضافة منتج
if menu == "إضافة منتج":
    st.header("➕ إضافة منتج جديد للمتجر")

    name = st.text_input("اسم المنتج")
    price = st.number_input("السعر", min_value=1, step=1)

    if st.button("إضافة"):
        st.session_state.products.append({"name": name, "price": price})
        st.success("✅ تمت إضافة المنتج بنجاح")


# الخيار 2: عرض المنتجات
elif menu == "عرض المنتجات":
    st.header("📦 المنتجات المتاحة")

    if len(st.session_state.products) == 0:
        st.warning("⚠️ لا يوجد منتجات حتى الآن")
    else:
        for product in st.session_state.products:
            st.write(f"🟢 {product['name']} - {product['price']} جنيه")


# الخيار 3: إضافة للسلة
elif menu == "إضافة للسلة":
    st.header("🛒 إضافة منتج للسلة")

    if len(st.session_state.products) == 0:
        st.warning("⚠️ لا يوجد منتجات")
    else:
        product_names = [product["name"] for product in st.session_state.products]
        selected = st.selectbox("اختار منتج", product_names)

        if st.button("إضافة للسلة"):
            for product in st.session_state.products:
                if product["name"] == selected:
                    st.session_state.cart.append(product)
                    st.success("✅ تم إضافة المنتج للسلة")


# الخيار 4: عرض السلة
elif menu == "عرض السلة":
    st.header("🛍️ محتويات السلة")

    if len(st.session_state.cart) == 0:
        st.warning("⚠️ السلة فارغة")
    else:
        total_price = sum(product["price"] for product in st.session_state.cart)

        for product in st.session_state.cart:
            st.write(f"🔸 {product['name']} - {product['price']} جنيه")

        st.subheader(f"💰 إجمالي السعر: {total_price} جنيه")


# الخيار 5: حذف منتج من السلة
elif menu == "حذف منتج من السلة":
    st.header("❌ حذف منتج من السلة")

    if len(st.session_state.cart) == 0:
        st.warning("⚠️ السلة فارغة ولا يوجد ما يُحذف")
    else:
        product_names = [p["name"] for p in st.session_state.cart]
        selected = st.selectbox("اختار المنتج المراد حذفه", product_names)

        if st.button("حذف"):
            for product in st.session_state.cart:
                if product["name"] == selected:
                    st.session_state.cart.remove(product)
                    st.success("🗑️ تم حذف المنتج من السلة")
                    break
