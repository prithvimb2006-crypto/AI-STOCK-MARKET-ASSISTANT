import os
import json
from openai import OpenAI
from dotenv import load_dotenv
from tools import analyze_stock

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

tools_schema = [
    {
        "type": "function",
        "function": {
            "name": "analyze_stock",
            "description": "Analyze stock indicators like price, MA50, and RSI",
            "parameters": {
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        
                        "description": "Stock ticker symbol (e.g., AAPL)"
                    }
                },
                "required": ["symbol"]
            }
        }
    }
]

def run_assistant(user_query):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a financial AI assistant. Always use tools for calculations."},
            {"role": "user", "content": user_query}
        ],
        tools=tools_schema,
        tool_choice="auto"
    )

    message = response.choices[0].message

    if message.tool_calls:
        tool_call = message.tool_calls[0]
        args = json.loads(tool_call.function.arguments)

        result = analyze_stock(args["symbol"])

        final_response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a financial AI assistant."},
                {"role": "user", "content": user_query},
                message,
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": json.dumps(result)
                }
            ]
        )

        return final_response.choices[0].message.content

    return message.content


if __name__ == "__main__":
    # Example specifically for AAPL
    symbol=input("enter the stock ticker name:")
    query = f"Analyze {symbol} stock"
    output = run_assistant(query)
    print("\nAI Analysis:\n")
    print(output)