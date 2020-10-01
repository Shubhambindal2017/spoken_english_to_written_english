
# Spoken english to written english conversion system

This is a Python module which can that can convert a paragraph of spoken english to written english.

 For example, "two dollars" should be converted to $2. Abbreviations spoken as "C M" or "Triple A" should be written as "CM" and "AAA" respectively.


## Installation:

   >>python3 setup.py install

## Usage:

    >>python3
	>>from spoken2written import sp2wr
	>>sp2wr.convert_sp_to_wr()
	>>
	[IN]:Enter Your paragraph of spoken english:
	
	I earn fifty dollars per day. My contact number contains double 9.
	
	[OUT]:The input Spoken English Paragraph: 
	
	" I earn fifty dollars per day. My contact number contains double 9. "
		
	 Converted Written English Paragraph: 
	 
	 " I earn $50 per day. My contact number contains 99. "

	





## Yet to implement


1. Handling of Dates.

2. Handling of Punctuation.

3. Handling of proper spaces after one sentance.



