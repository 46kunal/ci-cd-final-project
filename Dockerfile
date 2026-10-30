FROM python:3.9-slim
WORKDIR /app
COPY service/ /app/service/
ENV PYTHONUNBUFFERED=1
ENV PORT=8080
EXPOSE 8080
USER 1001
CMD ["python", "-m", "service.web"]
