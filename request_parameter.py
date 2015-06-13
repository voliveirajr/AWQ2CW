from pyjolokia import Jolokia
from boto.ec2.cloudwatch import connect_to_region
from itertools import cycle
import json
import time

def get_queue_names():
    j4p = Jolokia('http://127.0.0.1:8161/api/jolokia/')
    j4p.auth(httpusername='admin', httppassword='admin')

    response_json = j4p.request(type = 'read', mbean='org.apache.activemq:type=Broker,brokerName=localhost,destinationType=Queue,destinationName=*', attribute="Name")
    queues_json = response_json['value']

    result=[]

    for queue in queues_json:
        result.append((queue.split('destinationName='))[1].split(",")[0])
    return result

def push_2_cw(queue, avg_time):
    cw_conn = connect_to_region('us-east-1')
    cw_conn.put_metric_data(namespace="activemq",
                name=queue, 
                value=avg_time, 
                unit="Milliseconds", 
                #here you have to use the instance ID related with this data on cloudwatch
                dimensions={"InstanceId" : "YourInstanceId"})

def main():

    queues = get_queue_names()

    j4p = Jolokia('http://127.0.0.1:8161/api/jolokia/')
    j4p.auth(httpusername='admin', httppassword='admin')

    for queue in queues:
        #request AverageEnqueueTime for each queue on ActiveMQ
        j4p.add_request(type = 'read', mbean='org.apache.activemq:type=Broker,brokerName=localhost,destinationType=Queue,destinationName='+queue, attribute="AverageEnqueueTime")

    bulkdata = j4p.getRequests()

    for data in bulkdata:
        print (data['request']['mbean'].split('destinationName='))[1].split(",")[0]
        print data['value']
        push_2_cw((data['request']['mbean'].split('destinationName='))[1].split(",")[0], data['value'])		

if __name__ == "__main__":

    main()