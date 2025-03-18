- inspired from https://www.analyticsvidhya.com/blog/2024/06/agentic-workflow-with-crewai-and-groq/
- after cloning the repo, one needs to create a .env file in the project directory with these 2 keys:
	- SERPER_API_KEY=<your_serper_api_key>
	- GROQ_API_KEY=<your_groq_api_key>
- didn't work as expected. Was getting this error (will resolve it shortly, occurrring most probably due to pydantic version issues and gemma-7b-it being decommisioned from GROQ):

(isolate) (base) jnayak@innovationai:~/petonic_trials/Agentic Workflow$ python app.py
/home/jnayak/petonic_trials/Agentic Workflow/isolate/lib/python3.11/site-packages/pydantic/_internal/_config.py:295: PydanticDeprecatedSince20: Support for class-based `config` is deprecated, use ConfigDict instead. Deprecated in Pydantic V2.0 to be removed in V3.0. See Pydantic V2 Migration Guide at https://errors.pydantic.dev/2.10/migration/
  warnings.warn(DEPRECATION_MESSAGE, DeprecationWarning)
/home/jnayak/petonic_trials/Agentic Workflow/isolate/lib/python3.11/site-packages/pydantic/_internal/_fields.py:192: UserWarning: Field name "schema" in "DatabricksQueryToolSchema" shadows an attribute in parent "BaseModel"
  warnings.warn(
/home/jnayak/petonic_trials/Agentic Workflow/isolate/lib/python3.11/site-packages/pydantic/_internal/_config.py:295: PydanticDeprecatedSince20: Support for class-based `config` is deprecated, use ConfigDict instead. Deprecated in Pydantic V2.0 to be removed in V3.0. See Pydantic V2 Migration Guide at https://errors.pydantic.dev/2.10/migration/
  warnings.warn(DEPRECATION_MESSAGE, DeprecationWarning)
/home/jnayak/petonic_trials/Agentic Workflow/isolate/lib/python3.11/site-packages/pydantic/_internal/_generate_schema.py:502: UserWarning: <built-in function callable> is not a Python type (it may be an instance of an object), Pydantic will allow any object with no validation since we cannot even enforce that the input is an instance of the given type. To get rid of this error wrap the type with `pydantic.SkipValidation`.
  warn(
/home/jnayak/petonic_trials/Agentic Workflow/isolate/lib/python3.11/site-packages/crewai_tools/tools/scrapegraph_scrape_tool/scrapegraph_scrape_tool.py:34: PydanticDeprecatedSince20: Pydantic V1 style `@validator` validators are deprecated. You should migrate to Pydantic V2 style `@field_validator` validators, see the migration guide for more details. Deprecated in Pydantic V2.0 to be removed in V3.0. See Pydantic V2 Migration Guide at https://errors.pydantic.dev/2.10/migration/
  @validator("website_url")
/home/jnayak/petonic_trials/Agentic Workflow/isolate/lib/python3.11/site-packages/crewai_tools/tools/selenium_scraping_tool/selenium_scraping_tool.py:26: PydanticDeprecatedSince20: Pydantic V1 style `@validator` validators are deprecated. You should migrate to Pydantic V2 style `@field_validator` validators, see the migration guide for more details. Deprecated in Pydantic V2.0 to be removed in V3.0. See Pydantic V2 Migration Guide at https://errors.pydantic.dev/2.10/migration/
  @validator("website_url")
/home/jnayak/petonic_trials/Agentic Workflow/isolate/lib/python3.11/site-packages/crewai_tools/tools/vision_tool/vision_tool.py:15: PydanticDeprecatedSince20: Pydantic V1 style `@validator` validators are deprecated. You should migrate to Pydantic V2 style `@field_validator` validators, see the migration guide for more details. Deprecated in Pydantic V2.0 to be removed in V3.0. See Pydantic V2 Migration Guide at https://errors.pydantic.dev/2.10/migration/
  @validator("image_path_url")
content='Hello! 👋  How can I help you today? 😊\n' additional_kwargs={} response_metadata={'token_usage': {'completion_tokens': 15, 'prompt_tokens': 11, 'total_tokens': 26, 'completion_time': 0.027272727, 'prompt_time': 0.001935946, 'queue_time': 0.232746273, 'total_time': 0.029208673}, 'model_name': 'gemma2-9b-it', 'system_fingerprint': 'fp_10c08bf97d', 'finish_reason': 'stop', 'logprobs': None} id='run-4a94b2cc-896d-4413-8864-82090210aa2f-0' usage_metadata={'input_tokens': 11, 'output_tokens': 15, 'total_tokens': 26}

Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers

# Agent: Researcher
## Task: Explore and identify the major development within Indian Elections 2024Detailed SEO report of the development in a comprehensive narrative.

Provider List: https://docs.litellm.ai/docs/providers

2025-03-18 15:54:46,910 - 140380116064064 - llm.py-llm:751 - ERROR: LiteLLM call failed: litellm.BadRequestError: LLM Provider NOT provided. Pass in the LLM provider you are trying to call. You passed model=gemma2-9b-it
 Pass model as E.g. For 'Huggingface' inference endpoints pass in `completion(model='huggingface/starcoder',..)` Learn more: https://docs.litellm.ai/docs/providers
 Error during LLM call: litellm.BadRequestError: LLM Provider NOT provided. Pass in the LLM provider you are trying to call. You passed model=gemma2-9b-it
 Pass model as E.g. For 'Huggingface' inference endpoints pass in `completion(model='huggingface/starcoder',..)` Learn more: https://docs.litellm.ai/docs/providers
 An unknown error occurred. Please check the details below.
 Error details: litellm.BadRequestError: LLM Provider NOT provided. Pass in the LLM provider you are trying to call. You passed model=gemma2-9b-it
 Pass model as E.g. For 'Huggingface' inference endpoints pass in `completion(model='huggingface/starcoder',..)` Learn more: https://docs.litellm.ai/docs/providers
Traceback (most recent call last):
  File "/home/jnayak/petonic_trials/Agentic Workflow/app.py", line 87, in <module>
    result = crew.kickoff(inputs={'subject_area':"Indian Elections 2024"})
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jnayak/petonic_trials/Agentic Workflow/isolate/lib/python3.11/site-packages/crewai/crew.py", line 640, in kickoff
    result = self._run_sequential_process()
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jnayak/petonic_trials/Agentic Workflow/isolate/lib/python3.11/site-packages/crewai/crew.py", line 752, in _run_sequential_process
    return self._execute_tasks(self.tasks)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jnayak/petonic_trials/Agentic Workflow/isolate/lib/python3.11/site-packages/crewai/crew.py", line 850, in _execute_tasks
    task_output = task.execute_sync(
                  ^^^^^^^^^^^^^^^^^^
  File "/home/jnayak/petonic_trials/Agentic Workflow/isolate/lib/python3.11/site-packages/crewai/task.py", line 310, in execute_sync
    return self._execute_core(agent, context, tools)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jnayak/petonic_trials/Agentic Workflow/isolate/lib/python3.11/site-packages/crewai/task.py", line 454, in _execute_core
    raise e  # Re-raise the exception after emitting the event
    ^^^^^^^
  File "/home/jnayak/petonic_trials/Agentic Workflow/isolate/lib/python3.11/site-packages/crewai/task.py", line 374, in _execute_core
    result = agent.execute_task(
             ^^^^^^^^^^^^^^^^^^^
  File "/home/jnayak/petonic_trials/Agentic Workflow/isolate/lib/python3.11/site-packages/crewai/agent.py", line 266, in execute_task
    raise e
  File "/home/jnayak/petonic_trials/Agentic Workflow/isolate/lib/python3.11/site-packages/crewai/agent.py", line 247, in execute_task
    result = self.agent_executor.invoke(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jnayak/petonic_trials/Agentic Workflow/isolate/lib/python3.11/site-packages/crewai/agents/crew_agent_executor.py", line 119, in invoke
    raise e
  File "/home/jnayak/petonic_trials/Agentic Workflow/isolate/lib/python3.11/site-packages/crewai/agents/crew_agent_executor.py", line 108, in invoke
    formatted_answer = self._invoke_loop()
                       ^^^^^^^^^^^^^^^^^^^
  File "/home/jnayak/petonic_trials/Agentic Workflow/isolate/lib/python3.11/site-packages/crewai/agents/crew_agent_executor.py", line 166, in _invoke_loop
    raise e
  File "/home/jnayak/petonic_trials/Agentic Workflow/isolate/lib/python3.11/site-packages/crewai/agents/crew_agent_executor.py", line 146, in _invoke_loop
    answer = self._get_llm_response()
             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jnayak/petonic_trials/Agentic Workflow/isolate/lib/python3.11/site-packages/crewai/agents/crew_agent_executor.py", line 216, in _get_llm_response
    raise e
  File "/home/jnayak/petonic_trials/Agentic Workflow/isolate/lib/python3.11/site-packages/crewai/agents/crew_agent_executor.py", line 207, in _get_llm_response
    answer = self.llm.call(
             ^^^^^^^^^^^^^^
  File "/home/jnayak/petonic_trials/Agentic Workflow/isolate/lib/python3.11/site-packages/crewai/llm.py", line 739, in call
    return self._handle_non_streaming_response(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jnayak/petonic_trials/Agentic Workflow/isolate/lib/python3.11/site-packages/crewai/llm.py", line 575, in _handle_non_streaming_response
    response = litellm.completion(**params)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jnayak/petonic_trials/Agentic Workflow/isolate/lib/python3.11/site-packages/litellm/utils.py", line 1154, in wrapper
    raise e
  File "/home/jnayak/petonic_trials/Agentic Workflow/isolate/lib/python3.11/site-packages/litellm/utils.py", line 1032, in wrapper
    result = original_function(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jnayak/petonic_trials/Agentic Workflow/isolate/lib/python3.11/site-packages/litellm/main.py", line 3068, in completion
    raise exception_type(
  File "/home/jnayak/petonic_trials/Agentic Workflow/isolate/lib/python3.11/site-packages/litellm/main.py", line 979, in completion
    model, custom_llm_provider, dynamic_api_key, api_base = get_llm_provider(
                                                            ^^^^^^^^^^^^^^^^^
  File "/home/jnayak/petonic_trials/Agentic Workflow/isolate/lib/python3.11/site-packages/litellm/litellm_core_utils/get_llm_provider_logic.py", line 356, in get_llm_provider
    raise e
  File "/home/jnayak/petonic_trials/Agentic Workflow/isolate/lib/python3.11/site-packages/litellm/litellm_core_utils/get_llm_provider_logic.py", line 333, in get_llm_provider
    raise litellm.exceptions.BadRequestError(  # type: ignore
litellm.exceptions.BadRequestError: litellm.BadRequestError: LLM Provider NOT provided. Pass in the LLM provider you are trying to call. You passed model=gemma2-9b-it
 Pass model as E.g. For 'Huggingface' inference endpoints pass in `completion(model='huggingface/starcoder',..)` Learn more: https://docs.litellm.ai/docs/providers
