from storages.backends.s3boto3 import S3Boto3Storage  # type: ignore


class StaticRootS3Boto3Storage(S3Boto3Storage):  # pylint: disable=W0223
    location = "static"
    default_acl = "public-read"


class MediaRootS3Boto3Storage(S3Boto3Storage):  # pylint: disable=W0223
    location = "media"
    file_overwrite = False
