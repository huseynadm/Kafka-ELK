FROM openjdk:11
WORKDIR /hello-app

COPY hello-app.jar /app/hello-app.jar

CMD ["java", "-jar", "your-application.jar"]
