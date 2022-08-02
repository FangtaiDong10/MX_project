from werkzeug.exceptions import HTTPException
from werkzeug.utils import secure_filename
import boto3
from flask import current_app


def paginate(query_set, page_num, per_page=10):
    try:
        paginated_objects = query_set.paginate(page_num, per_page)
        return {
            "total_pages": paginated_objects.pages,
            "counts": paginated_objects.total,
            "page_num": page_num,
            "items": [obj.to_dict() for obj in paginated_objects.items],
        }
    except HTTPException as e:
        if e.code == 404:
            return {"message": f"Page {page_num} was not found"}, 404
        else:
            raise e


s3 = boto3.client("s3")


def upload_file_to_s3(file, resource_path):
    filename = secure_filename(file.filename)
    object_name = f"{resource_path}/{filename}"
    s3.upload_fileobj(
        file,
        current_app.config["AWS_BUCKET_NAME"],
        object_name,
        ExtraArgs={"ContentType": file.content_type},
    )
    return object_name


def generate_s3_singed_url(object_name):
    return s3.generate_presigned_url(
        "get_object",
        Params={"Bucket": current_app.config["AWS_BUCKET_NAME"], "Key": object_name},
        ExpiresIn=3600,
    )
