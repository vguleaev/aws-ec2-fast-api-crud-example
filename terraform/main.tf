provider "aws" {
  region = "eu-central-1"
}

resource "aws_instance" "app" {
  ami           = "ami-0e54671bdf3c8ed8d" # Amazon Linux 2023 64-bit
  instance_type = "t2.micro"

  tags = {
    Name = "FastAPI-EC2"
  }

  vpc_security_group_ids = [aws_security_group.fast_api_security_group.id]
}

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

resource "aws_security_group" "fast_api_security_group" {
  name        = "fast_api_security_group"
  description = "Allow web and SSH traffic"

  # SSH access
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # HTTP access
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # HTTPS access
  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # FastAPI default port
  ingress {
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Outbound internet access
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
