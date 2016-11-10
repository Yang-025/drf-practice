"""
curl -X POST -d "username=eee&password=eee" http://127.0.0.1:8000/api/auth/token/


{"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImVlZSIsImV4cCI6MTQ3ODczOTE5MSwiZW1haWwiOiJlZWVAZ21haWwuY29tIiwidXNlcl9pZCI6N30.b0iufAW3UNST1HcCQ8Ej2pF4a5SkwD4OsAwRJZLWibI"}%

"""

"""
curl -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImVlZSIsImV4cCI6MTQ3ODczOTE5MSwiZW1haWwiOiJlZWVAZ21haWwuY29tIiwidXNlcl9pZCI6N30.b0iufAW3UNST1HcCQ8Ej2pF4a5SkwD4OsAwRJZLWibI" http://127.0.0.1:8000/api/comments/

curl -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImVlZSIsImV4cCI6MTQ3ODczOTE5MSwiZW1haWwiOiJlZWVAZ21haWwuY29tIiwidXNlcl9pZCI6N30.b0iufAW3UNST1HcCQ8Ej2pF4a5SkwD4OsAwRJZLWibI" -X POST -H "Content-Type: application/json" -d '{"content":"this is some content"}' http://127.0.0.1:8000/api/comments/create/?type=post&slug=my-title
# 上面不行試著把url變字串
curl -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImVlZSIsImV4cCI6MTQ3ODczOTE5MSwiZW1haWwiOiJlZWVAZ21haWwuY29tIiwidXNlcl9pZCI6N30.b0iufAW3UNST1HcCQ8Ej2pF4a5SkwD4OsAwRJZLWibI" -X POST -H "Content-Type: application/json" -d '{"content":"this is some content"}' 'http://127.0.0.1:8000/api/comments/create/?type=post&slug=my-title'

curl http://127.0.0.1:8000/api/comments/


"""

"""
換token

curl -X POST -d "username=eee&password=eee" http://127.0.0.1:8000/api/auth/token/
{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImVlZUBnbWFpbC5jb20iLCJ1c2VybmFtZSI6ImVlZSIsInVzZXJfaWQiOjcsImV4cCI6MTQ3ODczOTk4MH0.ao-dSHUO4YqUSkKPKKgVpDEtVGtUxucIFe3ihVJDEjk"}%

curl -X POST -H "Content-Type: application/json" -d '{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImVlZUBnbWFpbC5jb20iLCJ1c2VybmFtZSI6ImVlZSIsInVzZXJfaWQiOjcsImV4cCI6MTQ3ODczOTk4MH0.ao-dSHUO4YqUSkKPKKgVpDEtVGtUxucIFe3ihVJDEjk", "username": "eee", "password": "eee"}' http://localhost:8000/api/auth/token/refresh/

"""


