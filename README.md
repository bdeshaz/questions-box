# Alan and Brian Question Box

## Model construction

Models:

* Users
* Questions
* Answers
* Comments
* Tags

## Site Structure

Base Navigation (not a page, top nav)
 - Link to ask a question link
 - Link to Top users (optional)
 - Link to see questions

Questions list
 - Landing page
 - Paginated list

Ask a Question
 - Question form

Question Detail
 - Lists answers
  - pagination by 25 or 30
 - Ability to leave an answer (form)
 - Ability to Upvote or downvote

User list (optional)
 - list users by reputation

### View names

 - questions
 - show_question
 - ask_question

## Git

in terminal

$ git checkout -b {branch_name}
  ...do work...
$ git push origin {branch_name}
  ...in github...
  merge
  or $ git merge
$ git pull origin master

## Requirements to Satisfy

Logged-in users should be able to:

    Ask questions
    Answer questions
    Vote on answers positively or negatively

Questions should have:

    a title
    question text
    any number of tags (tags being short phrases that show the topics of the question)
    any number of answers

Answers should have:

    the answer text
    a score based on the sum of all votes

Besides the normal things users have, they should also have a score. The score starts at 0, and increases in the following ways:

    When a user asks a question, +5 points.
    When a user's answer is upvoted, +10 points per positive vote.
    When a user's answer is downvoted, -5 points per negative vote.
    When a user downvotes an answer, -1 point (yes, it costs from your score to vote something down).
