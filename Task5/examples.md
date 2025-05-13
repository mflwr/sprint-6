## Получаем только только имя и возраст клиента

```graphql
query {
  client(id: "123") {
    name
    age
  }
}
```

## Получаем клиента и его документы

```graphql
query {
  client(id: "123") {
    name
    documents {
      type
      number
    }
  }
}
```

## Все данные 

```graphql
query {
  client(id: "123") {
    id
    name
    age
    documents {
      id
      type
      number
      issueDate
      expiryDate
    }
    relatives {
      id
      relationType
      name
      age
    }
  }
}
```