## Problem Statement

Design a system for:
- 250 users, each with at least one account holding assets (stocks, mutual funds)
- Users view real-time portfolios at any time
- Prices come from different external sources

### Requirements

- Create, calculate, and maintain user portfolios
- Reliability and scalability
- Real-time portfolio updates as soon as source provides new data
- Data refresh every 10 minutes

---

## Key Components

1. **API Gateway**
   - Entry point, handles routing, rate-limiting, and basic security checks

2. **User Service**
   - Manages users/accounts, authentication (JWT/OAuth2), and authorization

3. **Account & Portfolio Service**
   - Manages user accounts/assets
   - Calculates portfolio values (event-driven & scheduled)
   - Fetches latest prices from Price Aggregator

4. **Price Aggregator / Price Feed Service**
   - Collects/standardizes prices from multiple sources (stock exchanges, MF APIs)
   - Event-driven updates (webhooks, polling)
   - Retry logic for failed fetches
   - Supports scheduled refresh (every 10 mins)

5. **Message Broker (Kafka/RabbitMQ)**
   - Decouples Price Feed and Portfolio Services
   - Reliable delivery, retry on failures

6. **Redis Cache**
   - Caches latest portfolio values for fast access

7. **Database (PostgreSQL/MongoDB/TimescaleDB)**
   - Stores user/account/asset info, price history, transactions

8. **Scheduler (CronJob/Cloud Scheduler)**
   - Triggers full price/data refresh every 10 minutes

9. **Monitoring & Alerting**
   - System logs, metrics (Prometheus/Grafana), error/latency alerts

10. **Notification Service (Optional)**
    - Notifies users of significant portfolio changes

---

## Flow of Data

1. User logs in → API Gateway → User Service (auth)  
2. User requests portfolio → Portfolio Service (fetches latest from Redis or DB)  
3. Price Aggregator collects price updates (polling/webhook)  
4. Price update sent to Message Queue  
5. Portfolio Service listens, recalculates affected portfolios  
6. Redis Cache and DB updated  
7. Scheduler triggers full data pull every 10 minutes  
8. Monitoring and alerting on all critical services

---

## High-Level Design Diagram

```plaintext
                        ┌────────────────────────────┐
                        │    External Price Sources  │
                        │ (Stock/MF APIs)            │
                        └────────────┬───────────────┘
                                     │
                         [Price Aggregator Service]
                                     │
                            ┌────────▼────────┐
                            │  Message Queue  │◄──────┐
                            └────────┬────────┘       │
                                     │                │
               ┌────────────────────▼──────────────────┐
               │         Portfolio Service             │
               │ - Updates on price changes            │
               │ - Recalculates user values            │
               └──────┬────────────────────────────────┘
                      │
         ┌────────────▼────────────┐
         │      Redis Cache        │
         └────────┬───────────────-┘
                  │
         ┌────────▼────────┐     ┌───────────────────────┐
         │   User API      │◄───►│  PostgreSQL/MongoDB   │
         └─────────────────┘     └───────────────────────┘
                  ▲
                  │
         ┌────────┴────────┐
         │   API Gateway   │
         └─────────────────┘
                  ▲
                  │
         ┌────────┴────────┐
         │     Users       │
         └─────────────────┘

   [Monitoring/Alerting surrounds all services]
   [Optional: Notification Service for user alerts]

```

## Key Design Considerations

**Reliability**
- Use durable message queues for all asset/price update events.
- Retry logic for failed operations, with dead-letter queues for unprocessable events.
- Deploy multiple instances of critical services (like Price Aggregator) for high availability.

**Scalability**
- Stateless microservices allow easy horizontal scaling.
- Redis cache for frequently accessed portfolio data to reduce DB load.
- Database sharding/partitioning if user/asset data grows.

**Security**
- Use JWT/OAuth2 for authentication and authorization.
- Encrypt all sensitive data at rest and in transit.
- API Gateway enforces rate limiting to prevent abuse.

**Monitoring & Observability**
- Integrate centralized logging and monitoring (e.g., Prometheus, Grafana, ELK stack).
- Set up alerts for service failures, high latency, or data freshness issues.

**Extensibility**
- Microservices allow new asset classes (crypto, bonds, etc.) to be added easily.
- Easy integration of new price sources.

**Data Consistency**
- Eventual consistency for portfolio values (acceptable due to 10-min refresh window and frequent updates).
- Strong consistency enforced where necessary (user info, account updates).

**Error Handling**
- Automatic retries with exponential backoff for transient failures.
- Use dead-letter queues for persistent errors.

**User Experience**
- Cached portfolios ensure fast response times for end-users.
- Optional notification service can alert users to significant portfolio changes.
