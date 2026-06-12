# main.py
import os
import streamlit as st
from crewai import Agent, Task, Crew, Process, LLM

def run_coding_agency(user_prompt, target_language, project_type, api_key, feedback_mode=False, existing_code="", feedback_notes=""):
   
    os.environ["GROQ_API_KEY"] = api_key

   
    groq_llm = LLM(
        model="groq/llama-3.3-70b-versatile",
        temperature=0.1, 
        api_key=os.environ["GROQ_API_KEY"]
    )

    if feedback_mode:
        execution_context = f"CRITICAL REFACTOR REQUEST.\n[Active Codebase]:\n{existing_code}\n\n[Client Feedback Parameters]: {feedback_notes}"
    else:
        execution_context = f"INITIALIZATION OBJECTIVE: Synthesize a complete {project_type} optimized for {target_language}.\n[System Directives]: {user_prompt}"

        if "HTML" in target_language or "CSS" in target_language or "JavaScript" in target_language:
            execution_context += (
                "\n[OUTPUT CONSTRAINTS]: The final response must contain ONLY valid HTML/CSS/JavaScript code. "
                "Do not return Python wrapper files, backend apps, markdown logs, or unrelated comments. "
                "Do not include any chat commentary or conversational explanations outside code fences. "
                "Wrap the results ready to render natively inside a web browser view window."
            )

    system_architect = Agent(
        role="Principal Systems Architect & PM",
        goal="Deconstruct unstructured feature requests into high-fidelity modular maps and layout guidelines.",
        backstory="You take chaotic requirements and layout absolute step-by-step system designs and interface structures.",
        llm=groq_llm,
        verbose=True
    )

    lead_engineer = Agent(
        role="Senior Core Automation Engineer",
        goal=f"Translate technical specifications directly into clean, responsive, execution-ready code files matching {target_language}.",
        backstory="You are a frontend/backend syntax prodigy. You deliver perfect operational text modules with zero small-talk.",
        llm=groq_llm,
        verbose=True
    )

    qa_auditor = Agent(
        role="Lead QA Automation & Debugging Specialist",
        goal=f"Parse compiled layouts for logic breaks, intercept syntax flaws, and return the final clean code base exactly in {target_language}.",
        backstory="You audit structural files meticulously to ensure there are no missing tags, broken links, or unwanted script formats.",
        llm=groq_llm,
        verbose=True
    )

    scoping_task = Task(
        description=f"Evaluate request boundaries and generate structural design schemas:\n{execution_context}",
        expected_output="A structured markdown specs manifest detailing layout grids and data flows.",
        agent=system_architect
    )

    coding_task = Task(
        description=f"Consume the specs manifest blueprint and code the absolute structural module functions. Conform strictly to target constraints.",
        expected_output="Raw source code implementations contained cleanly inside functional text arrays.",
        agent=lead_engineer
    )

    debugging_task = Task(
        description=f"Scan generated code arrays for compilation anomalies or script bugs. Refactor structural flaws directly and output the completed clean module.",
        expected_output="The finalized, completely debugged production code file with no extra conversation text.",
        agent=qa_auditor
    )

   
    with st.status("🛸 Syncing Interactive Multi-Agent Matrix...", expanded=True) as status:
        st.markdown("🌐 **[NODE 01 // SYSTEM ARCHITECT]:** Mapping file requirements layout...")
        st.markdown("💻 **[NODE 02 // AUTOMATION ENGINEER]:** Compiling operational runtime functions...")
        st.markdown("🔍 **[NODE 03 // QA AUTOMATION AUDITOR]:** Executing structural validation sweeps...")
        
       
        master_studio = Crew(
            agents=[system_architect, lead_engineer, qa_auditor],
            tasks=[scoping_task, coding_task, debugging_task],
            process=Process.sequential,
            verbose=True
        )
        
        final_output = master_studio.kickoff()
        status.update(label="System Compilation Completed Successfully!", state="complete", expanded=False)

    return final_output.raw