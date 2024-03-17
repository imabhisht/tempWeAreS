import engineFunctions
user_api_input="what is this? tell me in short"

node_0 = engineFunctions.scrapper_website(link='https://about.google/intl/ALL_in/')
print(node_0)
node_1 = engineFunctions.llm_gemini(index = node_0, query_input=user_api_input)
# print(node_1)