# StructuredRegex
Data and Code for StructuredRegex.

## Data
We provide *raw* data, *tokenized* data, and data with *anonymized* const strings.

Natural Language Descriptions of *raw* version contain the original raw annotations from Turkers. In *tokenized version*, we preprocessed and tokenized the descriptions. In *anonymized* version, we further replaced the contants mentioned in the descriptions with anonymous symbols. E.g., given the NL-regex pair [*it must contain the string "ABC".*  -->  contain(\<ABC\>)], we replace *"ABC"* with symbol *const0* in both NL and regex, and hence the const-anonymized NL-regex pair should be [*it must contain the string const0.*  -->  contain(const0)].

All data is presented in **TSV** format, with fields including：

* problem_id -- unique ID of the target regex.
* description -- Turker annotated description.
* regex -- target regex. 
* pos_examples -- positive examples.
* neg_examples -- negative examples.
* const_values -- mapping from symbols to the real string values, only existing in anonymized version. 

## Code
Code cominig soon.
