def vowel_count(st: str):
    vowel = [0, 0, 0, 0, 0]
    vowel[0] = st.count('a')
    vowel[1] = st.count('e')
    vowel[2] = st.count('i')
    vowel[3] = st.count('o')
    vowel[4] = st.count('u')

    return vowel