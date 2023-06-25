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
docker run -i --name hoot -p 8080:8080 hoot
```

This way you will deploy your _hoot_ docker image iteratively on port 8080.
