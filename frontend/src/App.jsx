import { useState } from "react";
import axios from "axios";

function App() {
  const [symptoms, setSymptoms] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const diagnose = async () => {
    if (!symptoms) return;
    setLoading(true);
    setResult("");

    try {
      // Pointing to your Python Backend
      const response = await axios.post("http://127.0.0.1:8000/diagnose", { 
        symptoms: symptoms 
      });
      setResult(response.data.diagnosis_summary);
    } catch (error) {
      setResult("⚠️ Error contacting the MASH Orchestrator. Is the backend running?");
    } finally {
      setLoading(false);
    }
  };

  return (
    // Tailwind v4 uses a more modern color palette
    <div className="min-h-screen bg-slate-50 flex items-center justify-center p-4">
      <div className="bg-white shadow-2xl rounded-2xl p-8 w-full max-w-2xl border border-slate-100">
        
        <header className="text-center mb-8">
          <h1 className="text-4xl font-extrabold tracking-tight text-slate-900 mb-2">
            MASH <span className="text-blue-600">AI</span>
          </h1>
          <p className="text-slate-500">Multi-Agent System for Healthcare</p>
        </header>

        <div className="space-y-4">
          <textarea
            className="w-full border border-slate-200 rounded-xl p-4 focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all outline-none text-slate-700"
            rows="5"
            placeholder="Describe symptoms in detail (e.g., chest pain, headaches, shortness of breath...)"
            value={symptoms}
            onChange={(e) => setSymptoms(e.target.value)}
          />

          <button
            onClick={diagnose}
            disabled={loading}
            className="w-full bg-blue-600 hover:bg-blue-700 disabled:bg-blue-300 text-white font-semibold py-3 rounded-xl cursor-pointer transition-colors shadow-lg shadow-blue-200"
          >
            {loading ? "Specialists Analyzing..." : "Run Multi-Agent Diagnosis"}
          </button>
        </div>

        {loading && (
          <div className="mt-8 flex flex-col items-center gap-3">
            <div className="animate-spin rounded-full h-12 w-12 border-4 border-blue-100 border-t-blue-600"></div>
            <p className="text-sm text-slate-400 animate-pulse">Consulting Neurology, Cardiology & Pulmonology agents...</p>
          </div>
        )}

        {result && (
          <div className="mt-8 animate-in fade-in slide-in-from-bottom-4">
            <h2 className="text-lg font-bold text-slate-800 mb-3">System Report:</h2>
            <pre className="bg-slate-900 text-slate-50 p-6 rounded-xl overflow-x-auto font-mono text-sm leading-relaxed border border-slate-800 shadow-inner whitespace-pre-wrap">
              {result}
            </pre>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;