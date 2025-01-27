- Prompt 1
  Extract the lesson content below then generate a list of 30 multiple choices question. First, find the essential knowledge, then continue with moderate knowledge, then generate choices that make learners confuse. A question have 6 choices and can have multiple correct choice. Follow original language of content. Instead of conversational preamble, just output questions.

Content: """
{content here}
"""

- Prompt 2
  Analyze the paragraph content below base on best practice of writing and grade points on 10 pts total, follow original language of content. First, check grammar, then check correctness of statements, then check the logic flow of the paragraph, then check the fluency of writers in their mother language. Every part will have suggestion to improve. Skip conversational preamble.
  Writers point will be minus if:
- Contain grammar error
- Use false statements
- Have errors in logic flow
- Use mixed language in paragraph even when writer's mother language have vocabulary to describe the meaning.

Content: """
{content here}
"""

- Prompt 3
  You will be presented with user reviews/comments and your job is to provide a set of tags from the following list. Provide your answer in bullet point form, then count total of good and bad reviews. Choose ONLY from the list of tags provided here (choose either the positive or the negative tag but NOT both):
- Good price OR Too expensive
- Work normally OR Not work well
- Easy to use OR Difficult to use
- Good quality OR Bad quality
- Good customer support OR Bad customer support

Content: """
{Content here}
"""

- Prompt 4
  You will be provide with Python code, and your task is to explain it in concise way by comment directly into source code, then provide ideas for efficiency improvements, then find and fix bug.

Source code:
"""
{Content here}
"""

- Prompt 5
  Act as a professional tour guide, write a travel plan for tourist base on following location. The travel plan should covers highly recommended location for visiting, activities for tourist, good dishes with recommended restaurant. Show as timetable format.

Location:
"""
{Content here}
"""

- Prompt 6
  Summarize content of following book chapter, then list all character appeared in chapter.

Content:
"""
{Content here}
"""
