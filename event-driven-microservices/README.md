# 📬 RabbitMQ Event Publisher (Producer)

This micro-producer module handles publishing JSON-encoded messages to a RabbitMQ queue. It's used in an event-driven microservices architecture to send events (e.g. `product_liked`) to other services like `admin-service`.

---

## 🔧 Tech Stack

- Python 3
- `pika` for RabbitMQ connection
- RabbitMQ for message brokering

---

## File Structure

producer.py config.py

less
Copy
Edit

---

## How It Works

When the `publish(method, body)` function is called:

1. A persistent connection is created to RabbitMQ using credentials from `config.py`
2. The message is serialized using `json.dumps()`
3. It's published to the **`admin`** queue with a method name and payload
4. Other services (e.g. Admin service) can subscribe to this queue and consume messages

---

## Example Usage

In another Python service (like Flask):

```python
from producer import publish

@app.route('/api/products/<int:id>/like', methods=['POST'])
def like_product(id):
    ...
    publish('product_liked', id)

This sends the following message to RabbitMQ:
{
  "method": "product_liked",
  "body": 4
}

🛠 config.py Example
rabbitmq_host = 'rabbitmq'
rabbitmq_port = 5672
rabbitmq_user = 'guest'
rabbitmq_password = 'guest'
📦 RabbitMQ Queue
Queue name: admin

Exchange: (default, '')

Routing Key: admin

Message Properties: The method name is passed as BasicProperties

📦 Requirements
Install dependencies:
pip install pika

🧪 To Test
Make sure RabbitMQ is running (via Docker or locally):

docker run -d --hostname rabbitmq --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
Then run a test script that imports publish().

🔄 Integration Suggestion
This module works best when:

Used in microservices that trigger events

Paired with a RabbitMQ consumer (like the Admin service or an analytics processor)

Deployed in a Dockerized system (as part of docker-compose.yml)

📎 License
MIT — use it, build on it, modify it. Attribution appreciated 🙌
