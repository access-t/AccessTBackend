# Access-T API Endpoints
***
# Review:

### TODO
- Update documentation using JWT tokens

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

~~~
{
  status: 200,
  data: {
    token: "..."
  }
}
~~~

* Failure:
~~~
{ status: 403, data: "<Reason>" }
~~~

---

## /api/account/login -> POST
### This endpoint submits a login request
#### Request body:
* username: string
* password: string
#### Returns:
* Success:
~~~
{
  status: 200,
  data: {
    token: "..."
  }
}
~~~

* Failure:
~~~
{ status: 403, data: "<Reason>" }
~~~

---
## /api/collections -> GET
### This endpoint retrieves all the collections for a given account

#### Request body:
* auth_token: string
#### Returns:
* Success:
~~~
{
  status: 200,
  data: {
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
      ...
    ]
  }
}
~~~
* Failure:
~~~
{ status: 403, data: "<Reason>" }
~~~

## /api/collections/:name -> GET
### This endpoint retrieves a specific collection by a given name

#### Request body:
* auth_token: string
* collection_name: string
#### Returns:
* Success:
~~~
{
  status: 200,
  data: {
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
}
~~~
* Failure:
~~~
{ status: 403, data: "<Reason>" }
~~~

## /api/collections -> POST
### This endpoint creates a new collection

#### Request body:
* auth_token: string
* collection_name: string
* image_path: string
#### Returns:
* Success:
~~~
{ status: 200, data: "Success" }
~~~
* Failure:
~~~
{ status: 403, data: "<Reason>" }
~~~

## /api/collections/:name -> PUT
### This endpoint updates a collection (adds a new item to a collection)

#### Request body:
* auth_token: string
* item: dict { ... }
#### Returns:
* Success:
~~~
{ status: 200, data: "Success" }
~~~
* Failure:
~~~
{ status: 403, data: "<Reason>" }
~~~

## /api/collections/:name -> DELETE
### This endpoint deletes a collection by name

#### Request body:
* auth_token: string
#### Returns:
* Success:
~~~
{ status: 200, data: "Success" }
~~~
* Failure:
~~~
{ status: 403, data: "<Reason>" }
~~~