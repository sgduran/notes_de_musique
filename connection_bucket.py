#connection au bucket
from google.colab import auth
auth.authenticate_user()

!curl https://sdk.cloud.google.com | bash
  
!gcloud init

#récupération du fichier zip
!gsutil cp gs://maestro-bucket-tys/maestro-v3.0.0-midi.zip .
  
#installation de midi2audio
!pip install midi2audio

#unzip un fichier
!unzip maestro-v3.0.0-midi.zip
