import streamlit as st

st.set_page_config(page_title="AI Streaming Chat", page_icon="🤖", layout="centered")

st.markdown(
	"""
	<style>
		/* Reduce title size to fit on one line, with mobile tweak */
		h1.app-title { font-size: 1.8rem; line-height: 1.15; margin-bottom: 0.25rem; }
		@media (max-width: 420px) {
			h1.app-title { font-size: 1.6rem; }
		}
		/* Slightly reduce textarea default min-height for compact layout */
		section[data-testid="stTextArea"] textarea { min-height: 100px; }
	</style>
	""",
	unsafe_allow_html=True,
)
st.markdown("<h1 class='app-title'>AI Streaming Chat Application</h1>", unsafe_allow_html=True)
st.caption("Python • Pydantic AI • Streamlit • OpenRouter • Langfuse")

with st.sidebar:
	st.header("Settings")
	st.selectbox(
		"Model",
		["openrouter/model-placeholder"],
		index=0,
		help="Select a model (placeholder, no backend wired)",
	)
	st.text_input(
		"OpenRouter API Key",
		value="",
		type="password",
		placeholder="sk-... (not used in mockup)",
		help="For display only in this mockup. No requests are sent.",
	)
	st.text_input(
		"Langfuse API Key",
		value="",
		type="password",
		placeholder="lf-... (not used in mockup)",
		help="For display only in this mockup. No telemetry is sent.",
	)
	st.checkbox("Show token usage (mock)", value=True, help="UI-only toggle in this mockup")
	st.caption("No network calls are made in this mockup.")

st.markdown("---")

st.subheader("📝 System Prompt")
system_prompt: str = st.text_area(
	"Define the AI's behavior and role",
	height=100,
	placeholder=(
		"You are a helpful AI assistant. Answer concisely and cite sources when relevant."
	),
)

st.subheader("📋 Context")
context_text: str = st.text_area(
	"Provide additional context for the conversation",
	height=110,
	placeholder=(
		"Paste any relevant background info, documents, or constraints here."
	),
)

st.subheader("❓ Question")
question_text: str = st.text_input(
	"Ask your question",
	placeholder="What is the summary of the provided context?",
)

send_col, clear_col = st.columns([1, 1])
with send_col:
	st.button("🚀 Send Question", type="primary", help="Triggers streaming in real app")
with clear_col:
	st.button("🧹 Clear", help="Clears inputs in real app")

st.markdown("---")

st.subheader("🤖 AI Response (Streaming)")
response_placeholder = st.empty()
response_placeholder.markdown(
	"> The streaming response will appear here...\n\n"
	"> This is a static placeholder in the UI mockup."
)

st.markdown("---")

with st.expander("About this app"):
	st.markdown(
		"""
		- This is a UI mockup only. No backend logic or integrations are implemented.
		- Intended stack: Python, Pydantic AI, Streamlit, OpenRouter, Langfuse.
		- In a full implementation, the Send button would stream tokens into the response area.
		"""
	)
