# tiny_image_upload
------
A tiny Flask app that accepts image uploads at one endpoint and allows users to view them at another.

## Endpoints

As of now, there's only one. Serving uploaded images should be done by a webserver such as Apache or nginx.

### /upload/\<token\>

**Methods:** `POST`

Takes an uploaded file with name `image`. Requires an authorized token, as defined in the instance config.

## Missing Features

* image verification (soemthing beyond simple extension)
* more robust tokens
* "Delete image" endpoint
