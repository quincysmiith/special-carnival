#!/bin/bash

# build image
gcloud builds submit --tag gcr.io/marquin-personal-tools/streamlit--health-app  --project=marquin-personal-tools

# use container in cloud run
gcloud run deploy streamlit--health-app --image gcr.io/marquin-personal-tools/streamlit--health-app --platform managed  --project=marquin-personal-tools --allow-unauthenticated --region australia-southeast1
