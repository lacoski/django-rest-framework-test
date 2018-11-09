# Serializer
Cách convert dư liệu thô sang json và ngược lại (Gần giống với khái niệm form trong django)

Serialize class định nghĩ các trường sẽ được `serialized/deserialized`,

2 phương thức create(), update() chỉ định instance sẽ được xử lý thế nào trước khi save()

https://www.django-rest-framework.org/tutorial/1-serialization/


We're doing okay so far, we've got a serialization API that feels pretty similar to Django's Forms API, and some regular Django views.