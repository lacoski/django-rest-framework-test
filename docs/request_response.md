# Requests và Responses
---
## Request objects
```
request.POST  # Only handles form data.  Only works for 'POST' method.
request.data  # Handles arbitrary data.  Works for 'POST', 'PUT' and 'PATCH' methods.
```

## Response objects

DRF hỗ trợ lớp response giống như render (django) hỗ trợ trả lại dữ liệu dạng json

```
return Response(data)  # Renders to content type as requested by the client.
```

## Wrapping API views
REST Framework cung cấp 2 pp viết API view
- @api_view => Decorator cho FBV (function based views)
- APIView => CBV (class-based views)

## Xem thêm view snippet_list 
- Cấu trúc gần giống với django thuần
- Thay đổi render => Response và form đổi từ form.py sang dạng serializers.py

## Trong quá trình lập trình, muốn thao tác API trên giao diện

https://www.django-rest-framework.org/tutorial/2-requests-and-responses/#adding-optional-format-suffixes-to-our-urls




