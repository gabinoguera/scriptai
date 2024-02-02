with this script we create longform content making use of:

- GOOGLE CUSTOM SEARCH: we connect to the Google API by generating a global search engine (it can also be for a specific site).

- SCRAPING: Extract the text of the articles of the first positions with the newspapper library and, failing that, with beautiful soup.

- TEXT ANALYSIS AND SUMMARY: analyze the text with a python library (nltk) and summarize it to obtain a solid context based on the first results.

- CONTENT CREATION:

  o Creates the structures and briefing of the article based on the previous information.

  o Creates the content by sections and revises it to make it longer.

We could define it with the following scheme:

Keyword Research

    Categorization

    Cat1 Cat2 Cat3

      Kw1 kw2 kw3

      Kw4 kw5 kw6

Generation

    Context

    Research

    NLP

  Article Structure

      Content
