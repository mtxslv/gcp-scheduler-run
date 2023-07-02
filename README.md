# Testing GCP Cloud Run triggered by GCP Scheduler

This project is a simple example of how to schedule a Cloud Run's execution. To do so, we dockerize a FastAPI API and deploy it to Cloud Run. Then, we schedule the execution of the Cloud Run's endpoint using Cloud Scheduler.

The sample API here returns a message containing the current time in Unix timestamp format. Two endpoints are available:
- `/hoot/unix`: returns the current time in Unix timestamp format. Aimed for manual testing;
- `/hoot/scheduled`: also returns the current time in Unix timestamp format. Aimed for scheduled execution.

# Build and Run your image locally

## Building your Docker image

To Build your Docker image, run:

```bash
docker build -t hoot .
```

This way you will build a docker image named _hoot_.

## Running your Docker image

To deploy your Docker image run:

```bash
docker run -i -p 8080:8080 hoot
```

This way you will deploy your _hoot_ docker image iteratively on port 8080.

# Deploying your project to Google-Cloud-Platform

First, make sure you have access (that is, the APIs are enabled and your permissions/roles are updated) to the following services:
- [Artifact Registry](https://cloud.google.com/artifact-registry)
- [Cloud Run](https://cloud.google.com/run)
- [Cloud Scheduler](https://cloud.google.com/scheduler)

For this example, also suppose you have:
- [GCloud CLI installed](https://cloud.google.com/sdk/docs/install) and logged in;
- A project available in GCP. You can only deploy stuff in GCP if them are associated with a given project. To this example we will suppose this project is called `<YOUR PROJECT NAME>`;
- A [service account's credentials file](https://cloud.google.com/iam/docs/service-account-creds#key-types) authorized. You can authorize your credential file using:
    ```bash
    $ export GOOGLE_APPLICATION_CREDENTIALS=~/path/to/your/file
    $ gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS --project <YOUR PROJECT NAME>
    ```
- An Artifact Registry repository. Let's call it `<YOUR REPOSITORY NAME>`;
## Sending your image to Artifact Registry

Now, send your Docker image to the repository you created. To do this, run:

```bash
gcloud builds submit --region=us-central1 --tag us-central1-docker.pkg.dev/<YOUR PROJECT NAME>/<YOUR REPOSITORY NAME>/hoot:latest
```

## Deploying your image to Cloud Run

You Docker image is available in the GCP Artifact Registry. Now, you can deploy it to Cloud Run. To do this, run:

```bash
gcloud run deploy hoot --image us-central1-docker.pkg.dev/<YOUR PROJECT NAME>/<YOUR REPOSITORY NAME>/hoot:latest --region us-central1 --memory 512Mi --cpu 1 --max-instances 5 --min-instances 0 --port 8080
```

## Turning on the Scheduler

Up to this point, you already have your API running on the endpoint made available by GCP (`<YOUR CLOUD RUN URI>`). In order to make it be called automatically (let's say, every minute), you need to turn on the Cloud Scheduler. To do this, run:

```bash
gcloud scheduler jobs create http hoot-job --schedule "* * * * *" --http-method get --uri <YOUR CLOUD RUN URI SCHEDULER ENDPOINT> --location --us-central1 
```

# Deleting

You test your API and the services. Now you may need to get rid of everything, in order to save unwanted costs. Thus, do:

```bash
gcloud scheduler jobs delete hoot-job --location us-central1
gcloud run services delete hoot --region us-central1
gcloud container images delete us-central1-docker.pkg.dev/<YOUR PROJECT NAME>/<YOUR REPOSITORY NAME>/hoot
```

# REFERENCES

- [Build and push a Docker image with Cloud Build](https://cloud.google.com/build/docs/build-push-docker-image)
- [Triggering Cloud Run Jobs with Cloud Scheduler](https://codelabs.developers.google.com/cloud-run-jobs-and-cloud-scheduler#3)
- [Running services on a schedule](https://cloud.google.com/run/docs/triggering/using-scheduler)