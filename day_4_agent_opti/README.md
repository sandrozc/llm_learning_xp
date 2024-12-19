# Agentic Workflow & MLOPs System Design

## Course Goals
The primary objectives of this course are to:
- Understand the fundamentals of Agentic Workflow & Some MLOPs System Desing
- Learn how to implement inline Amazon Bedrock Agent
- Understand LLM Inference tradeoffs

## Course Agenda

1. Agentic Workflow & MLOPs System Desing & LLM Inference Presentation
2. Amazon Bedrock Agent Presentation (Live Demo)
3. TP Build Your Agent
   - Step by Step Guide Here [instruction bellow](#Restaurant-Order-Agent)
4. Enhancement Presentation (1hr)


### Amazon Bedrock RAG Workshop Setup - Group of 3 people

Scenario: Startup want to build a saas to allow restaurant to deploy a chatbot that allow their customers to order the food from anywhere 
in a streamli,ned fashion.

Set an agent wirth the following actions:
    - get_phone_number: Stores customer phone number
    - place_order: Adds new order to the system
    - get_all_orders: Retrieves all orders for a session
    - compute_bill: Calculates total bill from list of prices
    - send_notification_sms: Sends SMS notification about order

## Implement get_phone_number, place_order and get_all_orders
# Setup Bedrock Agent 
# Setup DynamoDB
# Setup AWS Lambda
# Test the agent !


## Implement compute_bill and send_notification_sms
# Setup Simple Notification Service (SNS)
# Test the agent !

## Add other useful actions to the agent + demo with me