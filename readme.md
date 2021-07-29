
# Пример апи для создания статей и комментарий к нему

### Примеры запросов:

Запрос для создания статьи


```python

import requests

answ = requests.post('http://localhost:8000/article/',
                     json = {
                         "html_text":"fasdjflkjsdnfjhasdkfnshgfd avdsja fbhsd fljkshdasdkjf",
                         "title": 'sdfsdg',
                         "author":'fdgdsfg'
                     },
                     headers={'Content-Type': 'application/json'})

answ.json()
```




    {'id': 3,
     'title': 'sdfsdg',
     'html_text': 'fasdjflkjsdnfjhasdkfnshgfd avdsja fbhsd fljkshdasdkjf',
     'author': 'fdgdsfg'}



Запрос для создания комментария к статье


```python
answ = requests.post('http://127.0.0.1:8000/comment/',
                     json = {
                         "html_text":"bhjbfgsdfg","article":1},
                     headers={'Content-Type': 'application/json'})
```


```python
answ.json()
```




    {'id': 4,
     'html_text': 'bhjbfgsdfg',
     'inclusion_level': 0,
     'article': 1,
     'parent_comment': None,
     'third_level_comment': None}



Запрос для создания комментария, которой непосредстенно вложени в указааный комментарий


```python
answ = requests.post('http://127.0.0.1:8000/comment/',
                     json = {
                         "html_text":"bhjbfgsdfg",
                         "article":1,
                         "parent_comment":4},
                     headers={'Content-Type': 'application/json'})
```


```python
answ.json()
```




    {'id': 7,
     'html_text': 'bhjbfgsdfg',
     'inclusion_level': 1,
     'article': 1,
     'parent_comment': 4,
     'third_level_comment': None}




```python
answ = requests.post('http://127.0.0.1:8000/comment/',
                     json = {
                         "html_text":"bhjbfgsdfg",
                         "article":1,
                         "parent_comment":5},
                     headers={'Content-Type': 'application/json'})
```


```python
answ.json()
```




    {'id': 8,
     'html_text': 'bhjbfgsdfg',
     'inclusion_level': 2,
     'article': 1,
     'parent_comment': 5,
     'third_level_comment': None}




```python
answ = requests.post('http://127.0.0.1:8000/comment/',
                     json = {
                         "html_text":"bhjbfgsdfg",
                         "article":1,
                         "parent_comment":8},
                     headers={'Content-Type': 'application/json'})
```


```python
answ.json()
```




    {'id': 9,
     'html_text': 'bhjbfgsdfg',
     'inclusion_level': 3,
     'article': 1,
     'parent_comment': 8,
     'third_level_comment': None}




```python
answ = requests.post('http://127.0.0.1:8000/comment/',
                     json = {
                         "html_text":"bhjbfgsdfg",
                         "article":1,
                         "parent_comment":9},
                     headers={'Content-Type': 'application/json'})
```


```python
answ.json()
```




    {'id': 10,
     'html_text': 'bhjbfgsdfg',
     'inclusion_level': 4,
     'article': 1,
     'parent_comment': 9,
     'third_level_comment': 9}



Запрос для получения коментариев до 3 уровня вложенности по статье


```python
answ = requests.get('http://127.0.0.1:8000/article/1/shadow_comments',
                     headers={'Content-Type': 'application/json'})
```


```python
answ.json()
```




    [{'id': 1,
      'html_text': 'fasdjflkjsdnfjhasdkfnshgfd avdsja fbhsd fljkshdasdkjf',
      'inclusion_level': 0,
      'article': 1,
      'parent_comment': None,
      'third_level_comment': None},
     {'id': 2,
      'html_text': 'bhjbfgsdfg',
      'inclusion_level': 0,
      'article': 1,
      'parent_comment': None,
      'third_level_comment': None},
     {'id': 3,
      'html_text': 'bhjbfgsdfg',
      'inclusion_level': 0,
      'article': 1,
      'parent_comment': None,
      'third_level_comment': None},
     {'id': 4,
      'html_text': 'bhjbfgsdfg',
      'inclusion_level': 0,
      'article': 1,
      'parent_comment': None,
      'third_level_comment': None},
     {'id': 5,
      'html_text': 'bhjbfgsdfg',
      'inclusion_level': 1,
      'article': 1,
      'parent_comment': 4,
      'third_level_comment': None},
     {'id': 6,
      'html_text': 'bhjbfgsdfg',
      'inclusion_level': 2,
      'article': 1,
      'parent_comment': 5,
      'third_level_comment': None},
     {'id': 7,
      'html_text': 'bhjbfgsdfg',
      'inclusion_level': 1,
      'article': 1,
      'parent_comment': 4,
      'third_level_comment': None},
     {'id': 8,
      'html_text': 'bhjbfgsdfg',
      'inclusion_level': 2,
      'article': 1,
      'parent_comment': 5,
      'third_level_comment': None},
     {'id': 9,
      'html_text': 'bhjbfgsdfg',
      'inclusion_level': 3,
      'article': 1,
      'parent_comment': 8,
      'third_level_comment': None}]



Запрос для получения всех вложенных комментариев по комментарию.


```python
answ = requests.get('http://127.0.0.1:8000/comment/9/nested_third_levels_comments/',
                     headers={'Content-Type': 'application/json'})
```


```python
answ.json()
```




    [{'id': 10,
      'html_text': 'bhjbfgsdfg',
      'inclusion_level': 4,
      'article': 1,
      'parent_comment': 9,
      'third_level_comment': 9}]



## Запуск апи
Для убунту в терминале зайти в папку, где лежит docker-compose.yml. Далее запустить docker-compose build
docker-compose up