# Get-Matching-Person-Names

# 🔎 Name Matching System

## Project Overview
The **Name Matching System** is a simple AI-powered application that allows users to input a name and find the **most similar names** from a dataset.  
This system is useful for handling **typos, spelling variations, and similar-sounding names**.  

- Uses **fuzzy string matching** (RapidFuzz) to find approximate matches.  
- Returns the **Best Match** and a **Ranked List of top similar names** with similarity scores.  
- Supports a dataset of **100+ names**.

---

## AI Component
Even though this system is lightweight, it uses **Artificial Intelligence techniques**:

- The system uses **fuzzy matching algorithms** to determine similarity between strings.
- It can detect names that are **spelled differently but sound similar** (e.g., "Geeta" and "Geetha").  
- This is considered **AI reasoning**, as the algorithm intelligently handles approximate matching like a human would.

> Future improvements could include embeddings or phonetic algorithms to enhance AI capabilities.

---

## Dataset
The system uses a dataset of **100 names**, including male and female names:

```python
names = [
    "Geetha","Geeta","Gita","Gitu","Geethaa","Githa","Githaa","Geetha Devi","Sahana","Sahani",
    "Sanjana","Sneha","Snehal","Priya","Priyanka","Priti","Preeti","Preethi","Rekha","Reka",
    "Kiran","Kiranmai","Shreya","Shriya","Nisha","Anjali","Anjalee","Anjali Devi","Shyla","Nisha Devi",
    "Rekhaa","Sahanaa","Sanjanaa","Sneha Devi","Kiranthi","Shiya","Nishaaya","Aishwarya","Deepika","Madhuri",
    "Kavya","Divya","Radhika","Lakshmi","Meera","Radha","Chitra","Bindu","Seema","Pallavi",
    "Ramesh","Suresh","Rajesh","Mahesh","Ganesh","Dinesh","Naresh","Kiran Kumar","Ravi","Arjun",
    "Krishna","Vishal","Ajay","Vijay","Santosh","Anil","Sunil","Rahul","Amit","Ashok",
    "Shankar","Mohan","Prakash","Sanjay","Lokesh","Vinod","Chandresh","Harish","Naveen","Karthik",
    "Sophia","Olivia","Isabella","Ava","Mia","Amelia","Harper","Evelyn","Abigail","Ella",
    "Emily","Scarlett","Grace","Chloe","Victoria","Aria","Lily","Aurora","Zoe","Hannah",
    "Liam","Noah","Ethan","James","Benjamin","Lucas","Henry","Alexander","William","Michael",
    "Daniel","Matthew","Joseph","David","Samuel","Andrew","Christopher","Nathan","Jack","Leo"
]
```

## Installation

1.Clone the repository:
bash```
git clone <your-repo-url>
cd name-matching-system
```

2.Install Python dependencies:
bash```
pip install rapidfuzz streamlit
```
