import regex
import logging

# This number should be bigger than the longest
# chain of patterns-inside-patterns
pattern_max_recursion_depth = 10

# The regex engine and settings
regex_flags = regex.VERBOSE | regex.IGNORECASE

def get_expression_compiler():
    return lambda expression: regex.compile(expression, flags=regex_flags)
    
def get_expression_sub(): 
    return lambda expression, sub, string: regex.sub(expression, sub, string, flags=regex_flags)
    
# Logging
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
