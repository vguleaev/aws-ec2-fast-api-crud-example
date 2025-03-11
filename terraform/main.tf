provider "aws" {
  region = "eu-central-1"
}

# resource "aws_instance" "app" {
#   ami           = "ami-0e54671bdf3c8ed8d" # Amazon Linux 2023 64-bit
#   instance_type = "t2.micro"

#   tags = {
#     Name = "FastAPI-EC2"
#   }
# }

resource "aws_db_instance" "postgres" {
  allocated_storage    = 20
  storage_type         = "gp2"
  engine               = "postgres"
  engine_version       = "16.3"
  instance_class       = "db.t3.micro"
  username             = var.db_username
  password             = var.db_password
  parameter_group_name = "default.postgres16"
  identifier           = "postgres-db"
  skip_final_snapshot  = true

  # Free Tier requirements
  publicly_accessible     = true
  multi_az                = false
  backup_retention_period = 0

  tags = {
    Name = "FastAPI-RDS"
  }
}
