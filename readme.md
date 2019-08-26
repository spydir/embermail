# embermail

embermail was developed as a solution to users who receive large quantities of email every day that are difficult to filter and must reviewed manually. The high volume of mail makes for frustrating evenings and the occasional weekend and it leads to the desire to burn all the mail to *embers*. 


*It is an assumption that all email accounts are gmail accounts for this version of embermail.*


##### Problem Statement:

The user must maintain several g-mail accounts across multiple personal and work functions. This creates a high volume of email that is difficult to filter and requires frequent manual review and orchestration of email filters across accounts.


##### Problem Solving Approach:


- Which email account receives the highest volume *important* email? 
- Which sender, across all accounts, sends the highest volume *important* email?
- What is the best filtering strategy to simplify manual review?
- What is the best labeling strategy for future searching, per account?

*Important is defined by the user rather than google, since google doesn't check across accounts.*

##### Simplest Manual Workflow without mail clients:

1. Enable gmail hot keys: https://support.google.com/mail/answer/6594?co=GENIE.Platform%3DDesktop&hl=en
2. Open Gmail native and use the search terms label:inbox label:unread
3. Select the gmail inbox and use the arrow keys to move up and down the list of individual emails
4. Use "X" to select email(s), "L" to apply labels, "Shift+I" to mark as read, "E" to archive and "Shift+3" to delete.


##### Dependencies 
1. python 2.7
2. virtualenv 
3. https://github.com/charlierguo/gmail

This gmail project must be installed in your virutalenv via python setup.py install

##### Possible Solution:

It may be possible to embermail to "learn" which types of emails a user regularly labels, reads, archives, or simply deletes. This could be true across all email accounts and potentially across multiple email providers. 

Steps:

1. Daily analysis of email.
2. Measure delta from previous day.
3. Determine: labeled, read, archived, and deleted mail.
4. Store attributes and time frame of each change. 
5. Machine learning!


## Getting Started

For now embermail is in it's infancy and returns basic statistics about email. 

Download mail metadata: 

    Usage: python embermail.py -d

Analyze mail metadata: 
    
    Usage: python embermail.py -a

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

