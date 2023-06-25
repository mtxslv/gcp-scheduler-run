Testing GCP Cloud Run triggered by GCP Scheduler


# Build your Docker image

To Build your Docker image, run:

```bash
docker build -t hoot .
```

This way you will build a docker image named _hoot_.

# Deploy your docker image

To deploy your docker image run:

```bash
docker run -i -p 8080:8080 hoot
```

This way you will deploy your _hoot_ docker image iteratively on port 8080.

# Create a Cloud Scheduler job

...

# REFERENCES

- [Build and push a Docker image with Cloud Build](https://cloud.google.com/build/docs/build-push-docker-image)
- [Triggering Cloud Run Jobs with Cloud Scheduler](https://codelabs.developers.google.com/cloud-run-jobs-and-cloud-scheduler#3)
- [Running services on a schedule](https://cloud.google.com/run/docs/triggering/using-scheduler)