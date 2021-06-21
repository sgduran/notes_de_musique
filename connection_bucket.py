from google.colab import auth
auth.authenticate_user()

!curl https://sdk.cloud.google.com | bash
  
!gcloud init

!gsutil cp gs://maestro-bucket-tys/maestro-v3.0.0-midi.zip .
