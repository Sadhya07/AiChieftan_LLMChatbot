import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta
import requests
import random

# Set page config
st.set_page_config(
    page_title="AIChieftain - Hotel Concierge Dashboard",
    page_icon="🏨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stApp {
        background-image: linear-gradient(to bottom, #ffffff, #f0f8ff);
    }
    .sidebar .sidebar-content {
        background-image: linear-gradient(to bottom, #1a3a8f, #0d1b3a);
        color: white;
    }
    .header {
        color: #1a3a8f;
        font-weight: 700;
    }
    .metric-card {
        background-color: white;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 15px;
    }
    .chat-container {
        background-color: white;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        height: 500px;
        overflow-y: auto;
        margin-bottom: 15px;
    }
    .user-message {
        background-color: #e3f2fd;
        padding: 10px 15px;
        border-radius: 18px 18px 0 18px;
        margin: 8px 0;
        max-width: 80%;
        float: right;
        clear: both;
    }
    .bot-message {
        background-color: #f1f1f1;
        padding: 10px 15px;
        border-radius: 18px 18px 18px 0;
        margin: 8px 0;
        max-width: 80%;
        float: left;
        clear: both;
    }
    .urgent {
        color: #d32f2f;
        font-weight: bold;
    }
    .stRadio > div {
        flex-direction: row !important;
        gap: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# Sample data generation functions
def generate_booking_data():
    room_types = ['Deluxe', 'Suite', 'Standard', 'Executive', 'Presidential']
    statuses = ['Confirmed', 'Cancelled', 'No-show', 'Checked-in', 'Checked-out']
    sources = ['Website', 'OTA', 'Phone', 'Email', 'Walk-in']
    
    data = []
    for i in range(50):
        check_in = datetime.now() + timedelta(days=random.randint(-5, 10))
        check_out = check_in + timedelta(days=random.randint(1, 14))
        data.append({
            'Booking ID': f"B{random.randint(1000, 9999)}",
            'Guest Name': f"Guest {i+1}",
            'Room Type': random.choice(room_types),
            'Check-in': check_in.strftime('%Y-%m-%d'),
            'Check-out': check_out.strftime('%Y-%m-%d'),
            'Status': random.choice(statuses),
            'Source': random.choice(sources),
            'Revenue': random.randint(100, 500)
        })
    return pd.DataFrame(data)

def generate_service_requests():
    services = ['Room Service', 'Housekeeping', 'Maintenance', 'Wake-up Call', 'Transportation']
    statuses = ['Pending', 'In Progress', 'Completed', 'Cancelled']
    priorities = ['Low', 'Medium', 'High', 'Urgent']
    
    data = []
    for i in range(20):
        timestamp = datetime.now() - timedelta(minutes=random.randint(5, 240))
        data.append({
            'Request ID': f"SR{random.randint(100, 999)}",
            'Room': f"{random.randint(100, 599)}",
            'Service Type': random.choice(services),
            'Timestamp': timestamp.strftime('%Y-%m-%d %H:%M'),
            'Status': random.choice(statuses),
            'Priority': random.choice(priorities),
            'Duration': f"{random.randint(5, 60)} mins"
        })
    return pd.DataFrame(data)

def generate_sentiment_data():
    dates = pd.date_range(end=datetime.today(), periods=30).tolist()
    data = []
    for date in dates:
        data.append({
            'Date': date.strftime('%Y-%m-%d'),
            'Positive': random.randint(70, 95),
            'Neutral': random.randint(5, 20),
            'Negative': random.randint(0, 10)
        })
    return pd.DataFrame(data)

# Load sample data
bookings_df = generate_booking_data()
requests_df = generate_service_requests()
sentiment_df = generate_sentiment_data()

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"sender": "bot", "text": "Hello! I'm your AI Concierge. How can I assist you today?", "time": datetime.now().strftime("%I:%M %p")}
    ]

# Sidebar - Filters and navigation
with st.sidebar:
    st.image("https://via.placeholder.com/150x50.png?text=AIChieftain", width=150)
    st.title("Hotel Concierge Dashboard")
    
    st.subheader("Navigation")
    dashboard_view = st.radio("Select View", ["Overview", "Bookings", "Service Requests", "Chat Analytics", "Settings"], 
                            label_visibility="collapsed")
    
    st.subheader("Filters")
    date_range = st.date_input("Date Range", [datetime.now() - timedelta(days=7), datetime.now()])
    room_type_filter = st.multiselect("Room Type", options=bookings_df['Room Type'].unique())
    status_filter = st.multiselect("Status", options=bookings_df['Status'].unique())
    
    st.subheader("Quick Actions")
    if st.button("Refresh Data"):
        st.rerun()
    if st.button("Generate Report"):
        st.success("Report generated successfully!")
    
    st.markdown("---")
    st.markdown("**Need help?** Contact support@aichieftain.com")

# Main content area
if dashboard_view == "Overview":
    st.title("🏨 AIChieftain - Hotel Concierge Dashboard")
    st.markdown("Real-time monitoring and management for hospitality services powered by AI")
    
    # Metrics row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="metric-card"><h3>Total Bookings</h3><h2>124</h2><p>↑ 12% from last week</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><h3>Occupancy Rate</h3><h2>78%</h2><p>↑ 5% from last week</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><h3>Service Requests</h3><h2>42</h2><p>8 pending</p></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="metric-card"><h3>Guest Satisfaction</h3><h2>89%</h2><p>Positive sentiment</p></div>', unsafe_allow_html=True)
    
    # Charts row
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Booking Trends")
        booking_counts = bookings_df.groupby(['Check-in', 'Room Type']).size().reset_index(name='Count')
        fig = px.line(booking_counts, x='Check-in', y='Count', color='Room Type', 
                     title="Daily Bookings by Room Type")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Service Request Status")
        fig = px.pie(requests_df, names='Status', title="Service Request Distribution")
        st.plotly_chart(fig, use_container_width=True)
    
    # Second charts row
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Revenue by Room Type")
        revenue_data = bookings_df.groupby('Room Type')['Revenue'].sum().reset_index()
        fig = px.bar(revenue_data, x='Room Type', y='Revenue', color='Room Type')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Guest Sentiment Trend")
        fig = px.line(sentiment_df, x='Date', y=['Positive', 'Neutral', 'Negative'],
                     title="Guest Sentiment Over Time")
        st.plotly_chart(fig, use_container_width=True)

elif dashboard_view == "Bookings":
    st.title("📅 Booking Management")
    st.markdown("View and manage all hotel bookings")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.dataframe(bookings_df, use_container_width=True, height=700)
    with col2:
        st.subheader("Quick Actions")
        if st.button("Check-in Selected"):
            st.success("Selected guests checked in successfully!")
        if st.button("Check-out Selected"):
            st.success("Selected guests checked out successfully!")
        if st.button("Send Reminder"):
            st.success("Reminders sent to selected guests!")
        
        st.subheader("Booking Stats")
        st.metric("Today's Check-ins", "12")
        st.metric("Today's Check-outs", "8")
        st.metric("Tomorrow's Arrivals", "15")

elif dashboard_view == "Service Requests":
    st.title("🛎️ Service Request Management")
    st.markdown("Track and manage guest service requests")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        # Highlight urgent requests
        def color_priority(val):
            color = 'red' if val == 'Urgent' else 'orange' if val == 'High' else 'inherit'
            return f'color: {color}; font-weight: bold' if val in ['Urgent', 'High'] else ''
        
        styled_df = requests_df.style.applymap(color_priority, subset=['Priority'])
        st.dataframe(styled_df, use_container_width=True, height=700)
    
    with col2:
        st.subheader("Quick Actions")
        if st.button("Assign Staff"):
            st.success("Staff assigned to selected requests!")
        if st.button("Mark Complete"):
            st.success("Selected requests marked as complete!")
        
        st.subheader("Priority Distribution")
        priority_counts = requests_df['Priority'].value_counts()
        st.bar_chart(priority_counts)

elif dashboard_view == "Chat Analytics":
    st.title("💬 Chatbot Analytics")
    st.markdown("Monitor chatbot performance and interactions")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("Live Chat Interface")
        
        chat_container = st.container(height=500)
        
        # Display messages
        for msg in st.session_state.chat_history:
            with chat_container:
                if msg["sender"] == "bot":
                    st.chat_message("assistant").write(f"{msg['text']}")
                else:
                    st.chat_message("user").write(f"{msg['text']}")
        
        # Input
        if prompt := st.chat_input("How can I help you today?"):
            st.session_state.chat_history.append({
                "sender": "user",
                "text": prompt,
                "time": datetime.now().strftime("%I:%M %p")
            })
            
            # Get AI response
            try:
                response = requests.post(
                    "http://localhost:5000/chat",
                    json={"message": prompt}
                )
                reply = response.json().get("reply", "I didn't understand that")
            except Exception as e:
                reply = f"Error: {str(e)}"
            
            st.session_state.chat_history.append({
                "sender": "bot",
                "text": reply,
                "time": datetime.now().strftime("%I:%M %p")
            })
            st.rerun()
    
    with col2:
        st.metric("Total Conversations", "128")
        st.metric("Response Accuracy", "92%")
        
        st.subheader("Common Topics")
        st.write("- Room Service\n- Check-in/out\n- Amenities\n- Local Recommendations\n- Billing")

        
        st.subheader("Chatbot Performance")
        
        # Metrics columns
        m1, m2 = st.columns(2)
        with m1:
            st.metric("Total Conversations", "128")
            st.metric("Response Accuracy", "92%")
        with m2:
            st.metric("Avg Response Time", "1.4s")
            st.metric("User Satisfaction", "4.8/5")
        
        st.subheader("Conversation Topics")
        topics = {
            "Room Service": 28,
            "Check-in/out": 22,
            "Amenities": 18,
            "Local Recommendations": 15,
            "Billing": 12
        }
        st.dataframe(
            pd.DataFrame.from_dict(topics, orient='index', columns=['Count'])
            .sort_values('Count', ascending=False),
            use_container_width=True
        )
        
        st.subheader("Sentiment Analysis")
        sentiment_data = pd.DataFrame({
            'Sentiment': ['Positive', 'Neutral', 'Negative'],
            'Percentage': [78, 15, 7]
        })
        fig = px.pie(sentiment_data, values='Percentage', names='Sentiment',
                    title="Customer Sentiment Distribution")
        st.plotly_chart(fig, use_container_width=True)

elif dashboard_view == "Settings":
    st.title("⚙️ Settings")
    st.markdown("Configure your dashboard and chatbot settings")
    
    tab1, tab2, tab3 = st.tabs(["Dashboard", "Chatbot", "Notifications"])
    
    with tab1:
        st.subheader("Dashboard Preferences")
        theme = st.selectbox("Color Theme", ["Light", "Dark", "Blue"])
        density = st.selectbox("Data Density", ["Compact", "Normal", "Detailed"])
        st.button("Save Dashboard Settings")
    
    with tab2:
        st.subheader("Chatbot Configuration")
        col1, col2 = st.columns(2)
        with col1:
            st.checkbox("Enable voice responses", True)
            st.checkbox("Show typing indicators", True)
        with col2:
            st.checkbox("Multilingual support", False)
            st.slider("Response delay (s)", 0.0, 3.0, 0.5, 0.1)
        st.button("Update Chatbot Settings")
    
    with tab3:
        st.subheader("Notification Settings")
        st.checkbox("Email alerts for urgent requests", True)
        st.checkbox("SMS alerts for VIP guests", False)
        st.checkbox("Desktop notifications", True)
        st.text_input("Notification Email Address")
        st.button("Save Notification Settings")

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #666; font-size: 0.9em;">
    <p>AIChieftain Hospitality Dashboard v1.0 • Powered by Streamlit</p>
    <p>Last updated: {}</p>
    </div>
    """.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), unsafe_allow_html=True)