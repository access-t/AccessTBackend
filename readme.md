# Access-T API Endpoints
***
# Review:

## /api/account/create -> POST
### This endpoint submits a request for registering a new account
#### Request body:
* first_name: string
* last_name: string
* email: string
* username: string
* password: string
#### Returns:
* Success:
Status 200
~~~
{
  message: "User <user> was created",
  access_token: <access_token>
}
~~~

* Failure:
Status 500
~~~
{ message: "Could not register user" }
~~~

---

## /api/account/login -> POST
### This endpoint submits a login request
#### Request body:
* username: string
* password: string
#### Returns:
* Success:
Status 200
~~~
{
  message: "Logged in as <user>"
  access_token: <access_token>
}
~~~

* Failure:
Status 500
~~~
{ message: <reason> }
~~~

---
## /api/collections -> GET
### This endpoint retrieves all the collections for a given account

#### Request body:
* auth_token: string
#### Returns:
* Success:
Status 200
~~~
{
  data: {
    collections: [
      {
        name: "...",
        image: "...",
        items: [
          {
            name: "...",
            image: "...",
          },
          ...
        ]
      }
      ...
    ]
  }
}
~~~
* Failure:
Status 500
~~~
{ message: <reason> }
~~~

## /api/collections -> GET
### This endpoint retrieves a specific collection by a given name

#### Request body:
* auth_token: string
* name: string
#### Returns:
* Success:
Status 200
~~~
{
  collections: [
    {
      name: "...",
      image_path: "...",
      items: [
        {
          name: "...",
          image_path: "...",
        },
        ...
      ]
    }
  ]
}
~~~
* Failure:
Status 500
~~~
{ message: <reason> }
~~~

## /api/collections -> POST
### This endpoint creates a new collection

#### Request body:
* auth_token: string
* collection_name: string
* image: string
#### Returns:
* Success:
Status 200
~~~
{ message: "Collection <name> was added" }
~~~
* Failure:
Status 500
~~~
{ message: <reason> }
~~~

## /api/collections -> PUT
### This endpoint updates a collection (adds a new item to a collection)

#### Request body:
* auth_token: string
* collection_name: string
* name: string (new item name)
* image: string
#### Returns:
* Success:
Status 200
~~~
{ message: "Collection <name> was updated" }
~~~
* Failure:
Status 500
~~~
{ message: <reason> }
~~~

## /api/collections/:name -> DELETE
### This endpoint deletes a collection by name entirely, or a specified item in the collection

#### Request body:
* auth_token: string
* collection_name: string
* item_name: string (if this is either absent or "all", the entire collection will be deleted. otherwise, only a specific item will be deleted)
#### Returns:
* Success:
Status 200
~~~
{ message: "Success" }
~~~
* Failure:
Status 500
~~~
{ message: <reason> }
~~~