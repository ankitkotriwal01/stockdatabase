import streamlit as st
import pandas as pd
import numpy as np



columns = ["VC Firm Name", "Website", "Firms Offices", "Stages", "Portfolio", "Markets",
           "Firm LinkedIn", "Firm Twitter", "Firm Facebook", "Firm Instagram",
           "Person Name", "Person Email", "Person Title", "Person LinkedIn",
           "Person Twitter", "Source"]


df = pd.DataFrame(data, columns=columns)

# Streamlit application
st.title("VC Firms and Contacts Filter")

# Sidebar filters
st.sidebar.header("Filter Options")

vc_firm_name = st.sidebar.multiselect("VC Firm Name", options=df["VC Firm Name"].unique())
website = st.sidebar.multiselect("Website", options=df["Website"].unique())
firms_offices = st.sidebar.multiselect("Firms Offices", options=df["Firms Offices"].unique())
stages = st.sidebar.multiselect("Stages", options=df["Stages"].unique())
portfolio = st.sidebar.multiselect("Portfolio", options=df["Portfolio"].unique())
markets = st.sidebar.multiselect("Markets", options=df["Markets"].unique())
firm_linkedin = st.sidebar.multiselect("Firm LinkedIn", options=df["Firm LinkedIn"].unique())
firm_twitter = st.sidebar.multiselect("Firm Twitter", options=df["Firm Twitter"].unique())
firm_facebook = st.sidebar.multiselect("Firm Facebook", options=df["Firm Facebook"].unique())
firm_instagram = st.sidebar.multiselect("Firm Instagram", options=df["Firm Instagram"].unique())
person_name = st.sidebar.multiselect("Person Name", options=df["Person Name"].unique())
person_email = st.sidebar.multiselect("Person Email", options=df["Person Email"].unique())
person_title = st.sidebar.multiselect("Person Title", options=df["Person Title"].unique())
person_linkedin = st.sidebar.multiselect("Person LinkedIn", options=df["Person LinkedIn"].unique())
person_twitter = st.sidebar.multiselect("Person Twitter", options=df["Person Twitter"].unique())
source = st.sidebar.multiselect("Source", options=df["Source"].unique())

# Filter data based on selections
filtered_df = df.copy()

if vc_firm_name:
    filtered_df = filtered_df[filtered_df["VC Firm Name"].isin(vc_firm_name)]
if website:
    filtered_df = filtered_df[filtered_df["Website"].isin(website)]
if firms_offices:
    filtered_df = filtered_df[filtered_df["Firms Offices"].isin(firms_offices)]
if stages:
    filtered_df = filtered_df[filtered_df["Stages"].isin(stages)]
if portfolio:
    filtered_df = filtered_df[filtered_df["Portfolio"].isin(portfolio)]
if markets:
    filtered_df = filtered_df[filtered_df["Markets"].isin(markets)]
if firm_linkedin:
    filtered_df = filtered_df[filtered_df["Firm LinkedIn"].isin(firm_linkedin)]
if firm_twitter:
    filtered_df = filtered_df[filtered_df["Firm Twitter"].isin(firm_twitter)]
if firm_facebook:
    filtered_df = filtered_df[filtered_df["Firm Facebook"].isin(firm_facebook)]
if firm_instagram:
    filtered_df = filtered_df[filtered_df["Firm Instagram"].isin(firm_instagram)]
if person_name:
    filtered_df = filtered_df[filtered_df["Person Name"].isin(person_name)]
if person_email:
    filtered_df = filtered_df[filtered_df["Person Email"].isin(person_email)]
if person_title:
    filtered_df = filtered_df[filtered_df["Person Title"].isin(person_title)]
if person_linkedin:
    filtered_df = filtered_df[filtered_df["Person LinkedIn"].isin(person_linkedin)]
if person_twitter:
    filtered_df = filtered_df[filtered_df["Person Twitter"].isin(person_twitter)]
if source:
    filtered_df = filtered_df[filtered_df["Source"].isin(source)]

# Display filtered data
st.write(f"Showing {len(filtered_df)} results")
st.dataframe(filtered_df)

# To run the Streamlit app, save this script as `app.py` and run `streamlit run app.py` in your terminal.