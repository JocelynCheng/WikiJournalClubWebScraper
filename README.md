# WikiJournalClubWebScraper
Python code to scrape Clinical Question, Bottom Line, and embedded URL of major trials listed on WikiJournalClub to create Anki cards for medical education.

Run the above code in terminal with command "python3 webscrape.py"

The code will create a .csv file with the clinical question, bottom line, and URL extracted from wikiJournalClub for easy import to anki.
![image](https://user-images.githubusercontent.com/39201310/155619051-6ffaea30-51bd-4ef0-9db8-c62fddbce3ac.png)

Import with File -> import. Create the following fields in Anki:
Fields created example.
![image](https://user-images.githubusercontent.com/39201310/155618690-ff3c540b-4d86-4b0e-abd4-fc85adbae14d.png)


Card settings should be set as follows:

Front side:
According to the <b>{{wikipedia_page}}</b> trial:
<br>
<i>{{clinical_question}} </i>
![image](https://user-images.githubusercontent.com/39201310/155619545-c41bcc41-c830-47ed-82c8-2b54f4dea1cf.png)


Back side:
{{FrontSide}}

<hr id=answer>
<div style='font-family: "Arial"; font-size: 30px;'>Bottom Line:</div>
<div style='font-family: "Arial"; font-size: 20px;'>{{bottom_line}}</div>
<br> 

<div style='font-family: "Arial"; font-size: 30px;'>Major Points:</div>
<div style='font-family: "Arial"; font-size: 20px;'>{{major_points}}</div>
<br> 

<div style='font-family: "Arial"; font-size: 30px;'>Current Guidelines:</div>
<div style='font-family: "Arial"; font-size: 20px;'>{{guidelines}}</div>
<br> 

<div style='font-family: "Arial"; font-size: 20px;'>{{wikipedia_page}} Wikipedia Page</div>
<iframe src="https://www.wikijournalclub.org/wiki/{{wikipedia_page}}" style="height: 100vh; width:100%;" seamless="seamless"></iframe> 

![image](https://user-images.githubusercontent.com/39201310/155619600-e55aa285-4700-45c4-9ff5-9e4254005d05.png)




Finished card:

Front.
![image](https://user-images.githubusercontent.com/39201310/155619260-32902ba4-9acd-4180-8bb3-baa67c999f16.png)

Back.
![image](https://user-images.githubusercontent.com/39201310/155619322-b1bc6eff-66da-46fb-8cb2-7635f622c856.png)

Complete WikiJournalClub is embedded in each card:
![image](https://user-images.githubusercontent.com/39201310/155619368-b8e4dd89-fe0d-4fcb-a0c1-61504d0749a1.png)
