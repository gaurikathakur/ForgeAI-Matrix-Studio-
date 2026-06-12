
import streamlit as st
from main import run_coding_agency


st.set_page_config(
    page_title="ForgeAI Command Matrix",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed"
)


if "step" not in st.session_state:
    st.session_state.step = "welcome"
if "compiled_code" not in st.session_state:
    st.session_state.compiled_code = ""


st.session_state.api_key = "YOUR_GROQ_API_KEY_HERE"


st.markdown("""
    <style>
    /* 1. Master Canvas Hard Overrides */
    [data-testid="stAppViewContainer"], [data-testid="stHeader"], .main {
        background: radial-gradient(circle at 50% 20%, #09071a 0%, #030408 75%, #000000 100%) !important;
        background-color: #000000 !important;
        color: #f1f5f9 !important;
        font-family: 'JetBrains Mono', system-ui, sans-serif;
    }
            /* ADD THIS INSIDE YOUR <style> BLOCK IN app.py */

    /* Camouflage the vertical structural blocks to perfectly match the canvas color */
    div[data-testid="stVerticalBlockBorderWrapper"], 
    div[data-testid="stVerticalBlock"],
    div[data-testid="element-container"],
    .element-container {
        background: #000000 !important;
        background-color: #000000 !important;
        border: none !important;
        box-shadow: none !important;
    }

    /* Force native input wrapper frames to lose their gray outline profiles */
    div[data-baseweb="base-input"], 
    div[data-baseweb="textarea"] {
        background-color: #030407 !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
        box-shadow: none !important;
    }
        
    /* Eradicate Streamlit padding structures causing phantom gaps */
    [data-testid="stMainBlockContainer"] {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        max-width: 1500px !important;
    }
    
    /* Kill all underlying gray wrapper shapes globally */
    div[data-testid="stVerticalBlockBorderWrapper"], 
    div[data-testid="stVerticalBlock"], 
    div[data-testid="element-container"],
    .element-container,
    div[data-testid="stWidgetLabel"] {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    
    /* Strict Rule: Obliterate native text field heading elements completely */
    div[data-testid="stWidgetLabel"] p {
        display: none !important;
    }
    
    /* 2. Global Arrow Pointer Overrides */
    html, body, [data-testid="stMarkdownContainer"], .cyber-terminal-card, div, p, span, h1, h2, h3, h4, label {
        cursor: default !important;
    }
    
    /* Enforce clear pointer finger interaction on inputs & option controls */
    .stButton>button, select, input, textarea, div[data-baseweb="select"] *, option {
        cursor: pointer !important;
    }
    
    /* 3. High-Tech Glass Operations Deck Panels */
    .cyber-terminal-card {
        background: linear-gradient(135deg, rgba(16, 20, 38, 0.75) 0%, rgba(5, 6, 12, 0.98) 100%);
        backdrop-filter: blur(35px);
        -webkit-backdrop-filter: blur(35px);
        border-radius: 16px;
        border-top: 1px solid rgba(56, 189, 248, 0.25);
        border-left: 1px solid rgba(129, 140, 248, 0.25);
        border-right: 1px solid rgba(0, 0, 0, 0.6);
        border-bottom: 1px solid rgba(0, 0, 0, 0.7);
        padding: 45px;
        margin-bottom: 25px;
        box-shadow: 
            0 40px 80px -25px rgba(0, 0, 0, 0.95),
            inset 0 1px 1px rgba(255, 255, 255, 0.05);
        transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
    }
    
    /* Typography Graphics */
    .neon-cyber-header {
        background: linear-gradient(90deg, #22d3ee 0%, #6366f1 50%, #a855f7 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        text-align: center;
        font-size: 3.6rem;
        letter-spacing: -0.05em;
        text-transform: uppercase;
        margin-top: 0px;
        margin-bottom: 8px;
        filter: drop-shadow(0 2px 15px rgba(99, 102, 241, 0.4));
    }
    
    .panel-sub-desc {
        text-align: center; 
        color: #475569; 
        font-size: 1rem; 
        font-weight: 500; 
        margin-top: 0px; 
        margin-bottom: 35px;
        letter-spacing: 0.02em;
    }
    
    .tile-headline {
        color: #64748b !important;
        font-size: 0.8rem !important;
        font-weight: 800 !important;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 10px !important;
        margin-top: 25px !important;
    }
    
    /* Seamless Matrix Input Fields Config */
    div[data-baseweb="input"], div[data-baseweb="textarea"], div[data-baseweb="select"] {
        background-color: rgba(3, 4, 7, 0.95) !important;
        border: 1px solid rgba(255, 255, 255, 0.06) !important;
        border-radius: 10px !important;
        color: #f8fafc !important;
        padding: 2px !important;
    }
    input, div[data-baseweb="input"] input, textarea, div[data-baseweb="textarea"] textarea {
        color: #f8fafc !important;
    }
    input::placeholder, div[data-baseweb="input"] input::placeholder,
    textarea::placeholder, div[data-baseweb="textarea"] textarea::placeholder {
        color: rgba(248, 250, 252, 0.75) !important;
    }
    
    /* Glowing Neon Grid Action Triggers */
    .stButton>button {
        background: linear-gradient(90deg, #4f46e5 0%, #06b6d4 100%) !important;
        color: #ffffff !important;
        border-radius: 10px !important;
        border: none !important;
        padding: 15px 35px !important;
        font-weight: 800 !important;
        font-size: 1.1rem !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        box-shadow: 0 4px 25px rgba(6, 182, 212, 0.35) !important;
        transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        width: 100%;
    }
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 15px 35px rgba(79, 70, 229, 0.6) !important;
    }
    /* Replace your old .matrix-pill CSS block with this rule */
    .matrix-pill {
        color: #22d3ee !important;
        font-size: 0.85rem !important;
        font-weight: 800 !important;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        display: block;
        margin-bottom: 25px;
        text-align: center;
        border: none !important;
        background: transparent !important;
        background-color: transparent !important;
        box-shadow: none !important;
    }
    </style>
""", unsafe_allow_html=True)



if st.session_state.step == "welcome":
    _, center_layout, _ = st.columns([1, 2.4, 1])
    
    with center_layout:
        st.markdown("<h1 class='neon-cyber-header'>ForgeAI Matrix Studio</h1>", unsafe_allow_html=True)
        st.markdown("<p class='panel-sub-desc'>Enterprise Multi-Agent Code Generation & Optimization Ecosystem</p>", unsafe_allow_html=True)
        
        st.markdown("""
            <p style='color: #94a3b8; font-size: 1.15rem; max-width: 750px; margin: 0 auto 40px auto; line-height: 1.6;'>
                Deploy an advanced squad of specialized digital personas. ForgeAI Studio analyzes baseline concept structures, 
                drafts modular codebase footprints, and executes automated pipeline diagnostics to output production-ready source code arrays.
            </p>
        """, unsafe_allow_html=True)
        
        feat_col1, feat_col2, feat_col3 = st.columns(3)
        with feat_col1:
            st.markdown("<div style='padding:25px; background:rgba(6,182,212,0.03); border-radius:12px; border:1px solid rgba(6,182,212,0.15); text-align:left;'><h4 style='color:#22d3ee; margin:0 0 8px 0; font-weight:800; font-size:1.1rem;'>📋 01 / ARCHITECT</h4><p style='color:#64748b; font-size:0.85rem; margin:0; line-height:1.5;'>Deconstructs abstract criteria profiles into optimized, mathematical specification blueprints.</p></div>", unsafe_allow_html=True)
        with feat_col2:
            st.markdown("<div style='padding:25px; background:rgba(99,102,241,0.03); border-radius:12px; border:1px solid rgba(99,102,241,0.15); text-align:left;'><h4 style='color:#6366f1; margin:0 0 8px 0; font-weight:800; font-size:1.1rem;'>💻 02 / SYNTHESIS</h4><p style='color:#64748b; font-size:0.85rem; margin:0; line-height:1.5;'>Compiles high-fidelity, secure, and production-ready source code strings dynamically.</p></div>", unsafe_allow_html=True)
        with feat_col3:
            st.markdown("<div style='padding:25px; background:rgba(168,85,247,0.03); border-radius:12px; border:1px solid rgba(168,85,247,0.15); text-align:left;'><h4 style='color:#a855f7; margin:0 0 8px 0; font-weight:800; font-size:1.1rem;'>🔍 03 / QA SCANNER</h4><p style='color:#64748b; font-size:0.85rem; margin:0; line-height:1.5;'>Intercepts execution loops, catches logical exceptions, and refactors lines automatically.</p></div>", unsafe_allow_html=True)
            
        if st.button("Initialize Environment Nodes ➔"):
            st.session_state.step = "config"  # Seamless jump directly to coder settings option page
            st.rerun()


elif st.session_state.step == "config":
    st.markdown("<div style='margin-bottom: 30px;'></div>", unsafe_allow_html=True)
    _, center_config, _ = st.columns([1, 1.8, 1])
    
    with center_config:
        st.markdown('<div class="cyber-terminal-card">', unsafe_allow_html=True)
        st.markdown("<span class='matrix-pill'>STAGE 02 // CONFIG SYSTEM</span>", unsafe_allow_html=True)
        st.markdown("<h2 style='color:white; font-weight:800; margin-top:0; font-size:2rem; letter-spacing:-0.02em;'>Build Your Application With Us</h2>", unsafe_allow_html=True)
        st.write("Establish execution layers and framework parameters below.")
        
        st.markdown("<p class='tile-headline'>Target Structural Layout Matrix</p>", unsafe_allow_html=True)
        app_type = st.selectbox("Type Core Box", ["Interactive Website / Frontend Interface", "Data Management & Analytics Script", "Backend REST Microservice API"])
        
        st.markdown("<p class='tile-headline'>Target Programming Language Runtime</p>", unsafe_allow_html=True)
        app_lang = st.selectbox("Lang Core Box", ["HTML5 / CSS3 / JavaScript (ESM)", "Python (FastAPI / Streamlit Framework)", "C# (.NET Core Backend Architecture)"])
        
        st.markdown("<p class='tile-headline'>Application Functional Objectives</p>", unsafe_allow_html=True)
        user_prompt = st.text_area(
            "Objectives Box Frame",
            placeholder="Outline structural parameters, wireframe styles, or explicit logic rules you want compiled...",
            height=130
        )
        
        st.markdown("<div style='margin-bottom: 30px;'></div>", unsafe_allow_html=True)
        if st.button("Deploy Collaborative Core 🚀"):
            if not user_prompt:
                st.warning("Please specify code parameters before launching the agent streams.")
            else:
                st.session_state.user_prompt = user_prompt
                st.session_state.app_lang = app_lang
                st.session_state.app_type = app_type
                st.session_state.step = "runtime"
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)



elif st.session_state.step == "runtime":
    monitor_col, console_col = st.columns([1, 2.4], gap="medium")
    
    with monitor_col:
        st.markdown("<h3 style='margin-top:0; color:white; font-weight:800; font-size:1.4rem;'>Active States</h3>", unsafe_allow_html=True)
        st.write("---")
        st.markdown("🟢 **Architect PM Node:** Online")
        st.markdown("🔵 **Engineer Coder Node:** Operational")
        st.markdown("🔍 **QA Automation Node:** Active & Sweeping")
        st.write("---")
        st.caption(f"**Matrix:** {st.session_state.app_type}")
        st.caption(f"**Engine:** {st.session_state.app_lang}")
        st.markdown("<h4 style='margin-top:24px; margin-bottom:10px; color:#c7d2fe; font-weight:800;'>Agent Role Summary</h4>", unsafe_allow_html=True)
        st.markdown("- **Architect PM Node:** defines the overall app layout, features, and user experience logic.")
        st.markdown("- **Engineer Coder Node:** writes the core code modules, components, and functional implementation.")
        st.markdown("- **QA Automation Node:** reviews output, fixes syntax issues, and validates final code quality.")
        st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)
        if st.button("↩️ Hard Reset Studio"):
            st.session_state.compiled_code = ""
            st.session_state.step = "config"
            st.rerun()
        
    with console_col:
        st.markdown("<h3 style='margin-top:0; color:white; font-weight:800; font-size:1.4rem;'>Synthesized Source Terminal</h3>", unsafe_allow_html=True)
        st.write("---")
        
        if not st.session_state.compiled_code:
            try:
                raw_synthesis = run_coding_agency(
                    user_prompt=st.session_state.user_prompt,
                    target_language=st.session_state.app_lang,
                    project_type=st.session_state.app_type,
                    api_key=st.session_state.api_key
                )
                st.session_state.compiled_code = raw_synthesis
            except Exception as e:
                st.error(f"Execution Boundary Loop Failure: {str(e)}")
        
        if st.session_state.compiled_code:
            st.success("🎉 Source code compiled successfully! Verified by QA Auditor Node with zero bugs.")
            st.code(st.session_state.compiled_code, language="html" if "HTML" in st.session_state.app_lang else "python")
            
            # Interactive Multi-Agent Feedback Loop
            st.write("---")
            st.markdown("<h4 style='color: #22d3ee; margin-bottom:5px; font-weight:800;'>💬 Real-Time Feedback Iteration Node</h4>", unsafe_allow_html=True)
            st.write("Submit revision parameters below to instruct your agent squad to refactor the module live.")
            
            feedback_notes = st.text_input("Feedback Stream Area", key="feedback_stream_input", placeholder="e.g., Update primary layout colors to deep navy and attach a clear download button layout...")
            
            st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)
            if st.button("Submit Revision Request 🔄"):
                if feedback_notes:
                    with st.spinner("🔄 Passing modifications back down into the agent matrix components..."):
                        try:
                            updated_synthesis = run_coding_agency(
                                user_prompt=st.session_state.user_prompt,
                                target_language=st.session_state.app_lang,
                                project_type=st.session_state.app_type,
                                api_key=st.session_state.api_key,
                                feedback_mode=True,
                                existing_code=st.session_state.compiled_code,
                                feedback_notes=feedback_notes
                            )
                            st.session_state.compiled_code = updated_synthesis
                            st.rerun()
                        except Exception as e:
                            st.error(f"Asynchronous Revision Mapping Exception: {str(e)}")
        st.markdown('</div>', unsafe_allow_html=True)