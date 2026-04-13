output "website_url" {
  value       = "https://${var.domain_name}"
  description = "Live website URL"
}

output "cloudfront_distribution_id" {
  value       = aws_cloudfront_distribution.main.id
  description = "CloudFront distribution ID (for cache invalidation)"
}

output "cloudfront_domain" {
  value       = aws_cloudfront_distribution.main.domain_name
  description = "CloudFront domain name"
}

output "nameservers" {
  value       = aws_route53_zone.main.name_servers
  description = "Route 53 nameservers"
}
