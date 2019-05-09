resource "aws_dynamodb_table" "geospatial-dynamodb-table" {
  name           = "geospatial-store"
  billing_mode   = "PROVISIONED"
  read_capacity  = 20
  write_capacity = 20
  hash_key       = "geojson"
  range_key      = "datapoint"

  attribute {
    name = "geojson"
    type = "S"
  }

  attribute {
    name = "datapoint"
    type = "S"
  }

  attribute {
    name = "time"
    type = "N"
  }

  ttl {
    attribute_name = "timetolive"
    enabled        = false
  }

  global_secondary_index {
    name               = "datapoint-index"
    hash_key           = "datapoint"
    range_key          = "time"
    write_capacity     = 10
    read_capacity      = 10
    projection_type    = "INCLUDE"
    non_key_attributes = ["geojson"]
  }

  tags = {
    Name        = "dynamodb-table-geospatial-store"
    Environment = "temporarytesting"
  }
}