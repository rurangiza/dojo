# Notes

# ORMs
- the **ORM** (Object-Relational Mapping) bridges the gap between the code and the database. We can use it to interract with the database using code

#### Go inside Database
```bash
$ python3 manage.py shell
```
```shell

$ from articles.models.Article import Article
$ Article.objects.all()
$ article = Article()
article.title = "Hello, world"
$ article.save()
```

```Python
# To see name of title
class Name(models.Model):
    # DB fields
    def __str__(self):
        return self.title()    
```