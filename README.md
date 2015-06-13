# AMQ2CW

A Python code to create a daemon to export JMX data from ActiveMQ queues to Amazon CloudWatch services

This example capture JMX data using the Jolokia which provides a RESTful interface to ActiveMQ's JMX capabilities
This data is parsed and pushed to Amazon CloudWatch using the AWS Python SDK.

It is possible to Daemonize that creating a Cronj to run that periodicaly
Put a shell script in one of these folders: /etc/cron.daily, /etc/cron.hourly, /etc/cron.monthly or /etc/cron.weekly.

To run every 15 minutes:
*/15 * * * * /path/to/command