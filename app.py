import streamlit as st
from rapidfuzz import fuzz, process

# Dataset
names = [
    # Female Indian Names
    "Geetha","Geeta","Gita","Gitu","Geethaa","Githa","Githaa","Geetha Devi","Sahana","Sahani",
    "Sanjana","Sneha","Snehal","Priya","Priyanka","Priti","Preeti","Preethi","Rekha","Reka",
    "Kiran","Kiranmai","Shreya","Shriya","Nisha","Anjali","Anjalee","Anjali Devi","Shyla","Nisha Devi",
    "Rekhaa","Sahanaa","Sanjanaa","Sneha Devi","Kiranthi","Shiya","Nishaaya","Aishwarya","Deepika","Madhuri",
    "Kavya","Divya","Radhika","Lakshmi","Meera","Radha","Chitra","Bindu","Seema","Pallavi",

    # Male Indian Names
    "Ramesh","Suresh","Rajesh","Mahesh","Ganesh","Dinesh","Naresh","Kiran Kumar","Ravi","Arjun",
    "Krishna","Vishal","Ajay","Vijay","Santosh","Anil","Sunil","Rahul","Amit","Ashok",
    "Shankar","Mohan","Prakash","Sanjay","Lokesh","Vinod","Chandresh","Harish","Naveen","Karthik",

    # Female English Names
    "Sophia","Olivia","Isabella","Ava","Mia","Amelia","Harper","Evelyn","Abigail","Ella",
    "Emily","Scarlett","Grace","Chloe","Victoria","Aria","Lily","Aurora","Zoe","Hannah",

    # Male English Names
    "Liam","Noah","Ethan","James","Benjamin","Lucas","Henry","Alexander","William","Michael",
    "Daniel","Matthew","Joseph","David","Samuel","Andrew","Christopher","Nathan","Jack","Leo"
]

def get_name_matches(query, name_list, top_n=5):
    matches = process.extract(query, name_list, scorer=fuzz.WRatio, limit=top_n)
    best_match = matches[0]
    return best_match, matches

# UI
st.title("🔎 Name Matching System")
st.write("Enter a name and find the most similar matches.")

query_name = st.text_input("Enter Name:")

if st.button("Find Matches"):
    if query_name.strip() == "":
        st.warning("Please enter a name.")
    else:
        best, ranked = get_name_matches(query_name, names, top_n=10)

        st.success(f"✅ Best Match: **{best[0]}** (Score: {best[1]})")

        st.subheader("📌 Ranked Matches")
        for name, score, _ in ranked:
            st.write(f"- {name} → Score: {score}")
