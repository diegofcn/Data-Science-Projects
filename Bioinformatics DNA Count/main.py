import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

image = Image.open('dna-g06e9aca68_640.jpg')

st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count Web App

This App counts the nucleotide composition of query DNA!

***
""")

# Input Text Box
st.header('Enter DNA sequence')

sequence_input = ">DNA Query\nCAAACTGTGATCGACCACTAGCCATGCCATTGCCTCTTAGACACCCCGATAC\nAGTGATTATGAAAGGTTTGCGGGGCATGGCTACGACTTGTTCAGCTACGTCCGAGGG\nCAGAAACTTATCCCCATTTGTATGTTCACCTATCTACTACCCATCCCCGGAGGTT\nAAGTAGGTTGTGAGATGCGGGAGAGGTTCTCGATCT"

sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:] # Skips the sequence name (first line)
sequence = ''.join(sequence) # Concatenates list to string

st.write("""
***
""")

# Prints the input DNA sequence
st.header('INPUT (DNA Query)')
sequence

# DNA nucleotide count
st.header('OUTPUT (DNA Nucleotide Count)')

# 1. print dictionary
st.subheader('1. Print dictionary')


def DNA_nucelotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C')),
    ])
    return d


X = DNA_nucelotide_count(sequence)

X_label = list(X)
X_values = list(X.values())

X

# 2. Print text
st.subheader('2. Print text')
st.write('There are ' + str(X['A']) + ' adenine (A)')
st.write('There are ' + str(X['T']) + ' thymine (T)')
st.write('There are ' + str(X['G']) + ' guanine (G)')
st.write('There are ' + str(X['C']) + ' cytosine (C)')

# 3. Display Dataframe
st.subheader('3. Display Dataframe')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'nucleotide'})
st.write(df)

# 4. Display Bar Chart using Altair
st.subheader('Display Bar Chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80)
)
st.write(p)
