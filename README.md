```
cd producer/
```
```
docker build -t producer .
```

```
cd ..
```

```
cd consumer/
```

```
docker build -t consumer .
```

```
cd ..
```

```
docker-compose up -d 
```

### To check kafka

```
sudo docker exec -it kafka kafka-topics --bootstrap-server kafka:29092 --describe --topic testtopic
sudo docker exec -it kafka kafka-console-consumer --bootstrap-server kafka:29092 --topic testtopic --from-beginning
```
