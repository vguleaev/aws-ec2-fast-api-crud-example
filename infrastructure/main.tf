provider "aws" {
  region = "eu-central-1"
}

resource "aws_instance" "app" {
  ami           = "ami-0e54671bdf3c8ed8d" # Amazon Linux 2023 64-bit
  instance_type = "t2.micro"

  tags = {
    Name = "FastAPI-EC2"
  }
}