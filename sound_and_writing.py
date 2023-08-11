import streamlit as st

st.markdown("# Puzzles about sound and writing")


st.markdown("## Puzzle 1: Structure of Braille")

st.markdown("You have certainly encountered the Braille writing system before. Do you know the system behind its letters? You can deduce it from as few as three examples, such as the ones given below. Here are three sentences and their versions encoded in Braille:")

st.markdown("**1. This fox is too quick!**")
st.markdown("## ⠠⠞⠓⠊⠎⠋⠕⠭⠊⠎⠞⠕⠕⠟⠥⠊⠉⠅⠖")
st.markdown('\n')
st.markdown('\n')

st.markdown("**2. How old are you, Jane?**")
st.markdown("## ⠠⠓⠕⠺⠕⠇⠙⠁⠗⠑⠽⠕⠥⠂⠠⠚⠁⠝⠑⠦")
st.markdown('\n')
st.markdown('\n')

st.markdown("**3. She is 89 years old.**")
st.markdown("## ⠠⠎⠓⠑⠊⠎⠼⠓⠼⠊⠽⠑⠁⠗⠎⠕⠇⠙⠲")
st.markdown('\n')
st.markdown('\n')


st.markdown("Write in Braille:  **Bring 40 pizzas and vermouth, Mark!**")
st.markdown('\n')
st.markdown('\n')

st.markdown("**Note 1**: Braille was originally developed for French, where 'w' isn't very much in use.")
st.markdown("**Note 2**: You don't need to know French (or English, for that matter) to decode and encode to and from Braille.")
st.markdown("**Note 3**: Line breaks, if any, are not relevant for the solution.")
st.markdown("**Note 4**: Access to internet makes solving this puzzle not fun -- information on Braille and its structure is readily available online. So this puzzle works only as an activity in class! If you are solving it while having internet access, don't google!")

if st.button('Reveal Hint 1'):
	st.markdown('Try to figure out a mapping between the set of letters and punctuation marks and the set of Braille point combinations. Two Braille symbols will be left without a correspoding letter -- try to guess why! In order to encode letters that are absent from the 3 sentences, find a pattern in Braille symbols.')
if st.button('Reveal Hint 2'):
	st.markdown('In order to find the pattern, compare several first letters from the alphabet and several last letters, as encoded in Braille.')
if st.button('Reveal Hint 3'):
	st.markdown("Group letters into tens (excluding _w_) and examine their Braille representations across the resulting groups.")



st.markdown("## Puzzle 2: Stress in Muscogee")


st.markdown("#### Problem 1")
st.markdown("Look at the following several words in the [Muscogee language](https://en.wikipedia.org/wiki/Muscogee_language) with stress marked: _cokó_ 'house', _yanása_ 'bison', _iyanawá_ 'his/her cheek', _imahicíta_ 'to look out for', _lafotaháya_ 'melon', _itiwanayipíta_ 'to tie each other down'.")
st.markdown("Mark stress on the following words: _ifa_ 'dog', _ifoci_ 'puppy', _wanayita_ 'to knit', _awanayita_ 'to tie'.")

st.markdown("#### Problem 2")
st.markdown("Here are more Muscogee words with stress marked: _sókca_ 'bag', _pocóswa_ 'axe', _aktopá_ 'bridge', _akkopánka_ 'game', _inkosapitá_ 'to beg', _acahankatíta_ 'to consider me', _pokkałakkoaopankacóko_ 'basketball gym'.")
st.markdown("Mark stress on the following words: _hoktaki_ 'women', _isiskitoci_ 'small glass', _ilitohtałita_ 'to cross legs'.")
st.markdown("Did you have to revise the stress rules you found in Problem 1 in order to finish the task?")


st.markdown("#### Problem 3")
st.markdown("Here are even more Muscogee words with stress marked: _cá\:lo_ 'trout', _wa\:kocí_ 'calf', _famí\:ca_ 'pumpkin', _hî\:spákwa_ 'American robin', _aklowahí_ 'mud', _tapassó\:la_ 'cellar spider', _tokna\:photí_ 'wallet', _co\:kakiłłitá_ 'study', _cokpilâ\:pilá_ 'nightjar'.")
st.markdown("Mark stress on the following words: _nâ\:naki_ 'things', _sâ\:sakwa_ 'goose', _a\:tamihoma_ 'hood', _homanta\:ki_ 'men'.") 
st.markdown("Did you have to revise the stress rules you found in Problem 2 in order to finish the task?")

st.markdown('\n')
st.markdown("**Note**: _ł_ is a consonant; the hat over a vowel (e.g. _â_) marks falling tone; vowel length is marked with a colon (e.g. _a\:_).")


if st.button('Reveal Hint 1', key='stress1'):
	st.markdown('Count the number of syllables in the first group of words.')
if st.button('Reveal Hint 2', key='stress2'):
	st.markdown('The basic rule remains the same, but the second and the third group of words provide data to make it more precise.')
if st.button('Reveal Hint 3', key='stress3'):
	st.markdown("In order to formulate this more precise rule, try to figure out what makes word structure in each of the groups unique.")
