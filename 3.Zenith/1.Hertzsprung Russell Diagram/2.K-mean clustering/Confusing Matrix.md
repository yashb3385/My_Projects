A **Confusion Matrix** is a table used to evaluate how well a Machine Learning model is performing. It compares what the computer *predicted* vs. what the *actual truth* was.
# Structure
The matrix is a square grid where:

- **Rows** represent the *Actual Classes*.
- **Columns** represent the *Predicted Clusters*.
# Example

|               | **Cluster A** | **Cluster B** |
| ------------- | :-----------: | :-----------: |
| *Real Type 0* |      40       |       0       |
| *Real Type 1* |       2       |      38       |
- **The Diagonal (The Wins)** $\to$ The numbers **40** and **38** mean the computer did a great job. *40 things* that were actually Type 0 were *correctly grouped* together.
$\hspace{1cm}$
- **The Off-Diagonal (The Confusion)** $\to$ The number **2** means the computer got ' *confused*. ' There were *2 things* that are actually Type 1, but the computer accidentally put them in the Type 0 group i.e. *Cluster A*.