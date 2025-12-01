class Candidate:
    def __init__(self, name, background, goal):
        self.name = name
        self.background = background
        self.goal = goal
        self.hard_skills = ["Python", "Java", "BPMN", "Machine Learning (Stanford)", "Scrum"]
        self.soft_skills = ["Systems Thinking", "Agile/Scrum", "Communication", "Resilience"]
        self.status = "Ready to deploy"

    def pitch(self):
        # Affiche le nom et le statut
        print(f"👋 Hello World! I am {self.name}.")
        print(f"🚀 Current Status: {self.status}")
        print("-" * 50)
        # Affiche le contexte et l'objectif
        print(f"🧩 Background: {self.background}")
        print(f"🎯 Objective: {self.goal}")
        print("-" * 50)

    def why_becode(self):
        """
        Explains the logic behind choosing BeCode.
        """
        reason = (
            "I have self-taught the syntax (Hard Skills), but I need the "
            "Pedagogy (Project-Based Learning) to build the Architecture."
        )
        return reason

    def run_application(self):
        self.pitch()
        print("\n🛠️  Tech Stack Loaded:")
        # Liste les compétences techniques
        for skill in self.hard_skills:
            print(f"   - {skill}")
        
        print("\n🧠 Soft Skills Integration:")
        # Liste les compétences comportementales
        for skill in self.soft_skills:
            print(f"   - {skill}")

        print(f"\n💡 Why BeCode? {self.why_becode()}")
        print("\n> System Log: Transitioning from Qualitative Analysis to Quantitative Mastery...")
        print("> Success: Candidate is work-ready for Data Engineering tracks.")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # Moi, la candidate <BeCode>
    becode_candidate = Candidate(
        name="Mathilde",
        background="Political Analyst & Systems Thinker (City of Brussels)",
        goal="To Humanize Tech as a Data Engineer / Analyst"
    )
    
    becode_candidate.run_application()
