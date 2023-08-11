import streamlit as st

st.markdown("# Puzzles about sound and writing")

st.markdown("## Puzzle 1: Stress in Muscogee")


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


st.markdown("**Note**: _ł_ is a consonant; the hat over a vowel (e.g. _â_) marks falling tone; vowel length is marked with a colon (e.g. _a\:_).")


if st.button('Reveal Hint 1'):
	st.markdown('Count the number of syllables in the first group of words.')
if st.button('Reveal Hint 2'):
	st.markdown('The basic rule remains the same, but the second and the third group of words provide data to make it more precise.')
if st.button('Reveal Hint 3'):
	st.markdown("In order to formulate this more precise rule, try to figure out what makes word structure in each of the groups unique.")