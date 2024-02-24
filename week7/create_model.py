from openai import OpenAI
client = OpenAI()

# For homework 6, please replace this file name to your own file's ID
# First, you need to upload your file to open AI
#   https://platform.openai.com/storage/files/
file_id = "file-G1Iu1PasWf9KRnkuBxhXhvhF"

client.fine_tuning.jobs.create(
  training_file=file_id, 
  model="gpt-3.5-turbo",
  hyperparameters={
    "n_epochs":20
  }
)