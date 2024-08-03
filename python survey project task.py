import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from collections import defaultdict

class SurveyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Survey Application")

        # Survey questions and options
        self.questions = [
            "Worry about things",
            "Make Friends easily",
            "Have a vivid imagination!",
            "Trust others",
            "Complete tasks Successfully",
            "Get angry easily",
            "Love large Parties?",
            "Believe in the importance of art",
            "Use others for my own ends?",
            "Like to tidy up?",
            "Often feel blue?",
            "Take charge?",
            "Experience my emotions intensely",
            "Love to help others",
            "Keep my promises",
            "Find it difficult to approach others?",
            "Am always busy",
            "Prefer variety to routine",
            "Love a good fight",
            "Work hard"
        ]
        self.options = [
            "Very Inaccurate", "Moderately Inaccurate", "Neither Accurate Nor Inaccurate", "Moderately Accurate", "Very Accurate"
        ]
        self.responses = defaultdict(int)
        self.current_page = 0

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        self.question_labels = []
        self.radio_vars = []
        self.frames = []

        start_index = self.current_page * 5
        end_index = start_index + 5
        for i in range(start_index, end_index):
            frame = ttk.LabelFrame(self.root, text=f"Question {i+1}: {self.questions[i]}")
            frame.grid(row=i % 5, column=0, padx=10, pady=5, sticky="w")

            self.frames.append(frame)

            radio_var = tk.StringVar(value="")

            for j, option in enumerate(self.options):
                rb = ttk.Radiobutton(frame, text=option, variable=radio_var, value=option)
                rb.grid(row=j, column=0, padx=10, pady=2, sticky="w")

            self.radio_vars.append(radio_var)

        if self.current_page > 0:
            back_button = ttk.Button(self.root, text="Back", command=self.load_previous_page)
            back_button.grid(row=6, column=0, pady=10, sticky="w")

        if self.current_page < 3:
            next_button = ttk.Button(self.root, text="Next Page", command=self.load_next_page)
            next_button.grid(row=6, column=1, pady=10, sticky="e")
        else:
            submit_button = ttk.Button(self.root, text="Submit", command=self.submit_answers)
            submit_button.grid(row=6, column=1, pady=10, sticky="e")

    def load_next_page(self):
        # Save responses for current page
        self.save_responses()

        # Clear current widgets
        for frame in self.frames:
            frame.destroy()

        self.frames.clear()
        self.radio_vars.clear()

        # Switch to next page
        self.current_page += 1
        self.create_widgets()

    def load_previous_page(self):
        # Clear current widgets
        for frame in self.frames:
            frame.destroy()

        self.frames.clear()
        self.radio_vars.clear()

        # Switch to previous page
        self.current_page -= 1
        self.create_widgets()

    def save_responses(self):
        for var in self.radio_vars:
            self.responses[var.get()] += 1

    def submit_answers(self):
        # Save responses for the last page
        self.save_responses()

        # Clear current widgets
        for frame in self.frames:
            frame.destroy()

        self.frames.clear()
        self.radio_vars.clear()

        # Generate and display bar graph
        self.generate_graph()

    def generate_graph(self):
        traits = {
            "Neuroticism": ["Very Accurate", "Moderately Accurate"],
            "Extraversion": ["Very Accurate"],
            "Openness to Experience": ["Very Accurate", "Moderately Accurate", "Neither Accurate Nor Inaccurate"],
            "Agreeableness": ["Very Inaccurate", "Moderately Inaccurate"],
            "Conscientiousness": ["Moderately Inaccurate", "Very Inaccurate", "Neither Accurate Nor Inaccurate"]
        }

        trait_counts = defaultdict(int)
        for trait, relevant_responses in traits.items():
            for response in relevant_responses:
                trait_counts[trait] += self.responses[response]

        labels = list(trait_counts.keys())
        counts = list(trait_counts.values())
        colors = ['purple', 'blue', 'pink', 'yellow', 'green']

        plt.figure(figsize=(10, 6))
        plt.bar(labels, counts, color=colors)
        plt.xlabel('Personality Traits')
        plt.ylabel('Count')
        plt.title('Survey Responses by Personality Traits')
        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = SurveyApp(root)
    root.mainloop()