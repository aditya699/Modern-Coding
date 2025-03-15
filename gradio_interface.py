import gradio as gr
import requests
import time

def chat_response(message, history):
    api_url = "http://localhost:8000/chat"
    
    try:
        # Send message as a JSON object with the exact field name expected by the API
        payload = {"message": message}  #This is the request body
        response = requests.post(api_url, json=payload) #This is the request(post)
        
        # Check if request was successful
        if response.status_code == 200:
            response_text = response.json()["response"] #This is the response from the API
            
            # Stream the response
            words = response_text.split()  #we are splitting the response into words
            for i in range(len(words)):
                time.sleep(0.1)
                yield " ".join(words[:i+1])  #we are yielding the words one by one(function is being made a generator)
        else:
            yield f"Error: Received status code {response.status_code}"
            
    except Exception as e:
        yield f"Error: {str(e)}"

demo = gr.ChatInterface(
    fn=chat_response,
    examples=["What is my order status?"],
    title="Customer Support Agent Chatbot",
    description="Ask any support-related questions(only supports order status check for now)"
)

if __name__ == "__main__":
    demo.launch()