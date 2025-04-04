# Translation Lab

## Definitions

*target language* - the language of the vector store data i.e. the domain specific data

## Points

- LLMs are generally good at translation especially from English to and from other languages it knows.

## Methods

### MT & LLM

- Machine translation to identify and translate the question to target language
- LLM to answer to query data and answer the question
- Machine translation to translate the answer back?

### LLM all the way

- LLM to detect the language as first step
- LLM to translate the question to target language
- LLM to answer
- LLM to translate the question back?

### Verification

Is there a need to verify the answer or should it be similar to general answers from llms? Where we only use evaluation in development? If the language cant be detected answer with, I don't know your specific language?

## Conclusions

Should be almost trivial to implement language support for another language if the model (e.g. gpt4) has decent training data for that language. To use the vector data you would have to convert the question into the language of the vector data first and then query. Then you would translate the answer back. So you would probably, in langgraph terms, have a translation node. You might keep the quote in its original language and perhaps supply the translated version in the answer or something akin to that. 

## Ideas

- Would have to emphasize that the translation might not be completely accurate. 
- When it comes to selling to customers it's a matter of knowing what level of accuracy is required, probably we can get them 80% there for most languages is my guess
- Round-trip translation for evaluation

## Questions / Problems

- Are there any models specifically trained for translation? Might not be relevant because of the embeddings done, the best models might still be the best, even for translation.
- If MT and LLM combination is the best performance, how do we access good MT? Are there open APIs for e.g. Google translate?
- Are there any services to use without implementing?
- When we say translation there are multiple interpretations of this
	- talking to the agent in another language (defined as not English?)
	- given an instruction - translate the question and answer to another language
- Are there any good free of charge machine translation services? 
- How to lab with this, go directly to openapi, or use langgraph, or use langchain?