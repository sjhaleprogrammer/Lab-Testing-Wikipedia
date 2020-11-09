import pytest
import requests

r = requests.get("http://api.duckduckgo.com/?q=presidents of the united states&format=json")

RelatedTopics = ["Washington","Adams","Jefferson","Madison","Monroe","Adams","Jackson","Buren",
"Harrison","Tyler","Polk","Taylor","Fillmore","Fillmore", "Pierce","Buchanan","Lincoln","Johnson","Grant",
"Hayes","Garfield","Arthur","Cleveland","Harrison","Cleveland","McKinley","Roosevelt","Taft","Wilson","Harding","Coolidge",
"Hoover","Roosevelt","Truman","Eisenhower","Kennedy","Johnson","Nixon", "Ford", "Carter","Reagan","Bush","Clinton","Bush"
,"Obama","Trump"]


def test_presidents():
    assert [ele for ele in RelatedTopics if(ele in r.text)] 
        
    
    