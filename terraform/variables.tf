variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "domain_name" {
  description = "Root domain name"
  type        = string
  default     = "arianehairbraiding.com"
}

variable "bucket_name" {
  description = "S3 bucket name for the website"
  type        = string
  default     = "ariane-hair-braiding"
}
