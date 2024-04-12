# Lifecycle rules
# create_before_destroy
# prevent_destroy
# ignore_changes

#Meta arguments
# depends_on
# count
# length - function
# for_each

resource "local_file" "myfirstfile" {
  filename = var.firstfile_filename
  content  = var.firstfile_content
}

resource "local_file" "mysecondfile" {
  filename = "mysecond123456789.txt"
  content  = "Hey! Welcome to the first terraform execution! all the best! 1 sdafasdf sadklfkldsfasdfasjdfkljdfsg"
  depends_on = [
    local_file.myfirstfile
  ]
}

resource "random_pet" "mypet" {
  #count = 3

  length    = 1
  prefix    = "Mr"
  separator = "."
  depends_on = [
    local_file.mysecondfile
  ]
}

resource "local_file" "mythirdfile" {
  filename = "pet.txt"
  content  = "Hey! I created a random pet name. aaa The name is pet"
}

resource "local_file" "fourthfile" {
  filename = "four.txt"
  content  = data.local_file.sourcetext.content
  depends_on = [
    local_file.mythirdfile
  ]
}

resource "local_file" "countfile" {
  #count = length(var.countfile_name)
  #filename = var.countfile_name[count.index]


  filename = each.value
  for_each = var.countfile_name


  content = "This is from count meta argument"
}
