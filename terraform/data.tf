# ─── DATA: Existing S3 Bucket ───────────────────────────────
data "aws_s3_bucket" "site" {
  bucket = var.bucket_name
}
