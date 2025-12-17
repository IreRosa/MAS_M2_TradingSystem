# UGE-Eiffel-M2-SIA_LLM
#An LLM-implementation project for our Master 2 in Systems Intelligents et Applications at Université Gustave Eiffel
1. Key concept: You need to download the contents of requirements in order for the simulation to function
2. An .env file is declared where the API key is kept. Should the current one not function it must be replaced. 
3. The simulation is ran by compiling "python run.py" from the mas_trading_llm folder.
4. The total number of lines printed can be altered in the run.py document.
5. Prompts may be modified in the prompts.py file.
6. LLM_Trader depends on all of the llm files in order to function, any significant change can stop it from working.
7. Agent declarations take place in the run.py file.
8. A variable T is declared in run.py with the number of time the LLM is called in a specific time period. If you wish to update it keep in mind the functioning of the system may alter.