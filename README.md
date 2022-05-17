# DemoStripeApplication

### build docker image
```shell
docker build . -t demo-stripe-application 
```

### create env.file with secrets
```shell
cat << EOF > file.env
STRIPE_PUBLISHABLE_KEY=YOUR_STRIPE_PUBLISHABLE_KEY
STRIPE_SECRET_KEY=YOUR_STRIPE_SECRET_KEY
EOF
```

### start docker container
```shell
docker run -d -p 8000:8000 \
  -v /path/to/your/data:/app/src/db \
  --env-file file.env \
  demo-stripe-application

```

