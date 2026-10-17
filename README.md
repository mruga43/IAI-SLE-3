BFS vs DFS Graph Search System
Course: 02AML204 -- Introduction to Artificial Intelligence  
Student Name: Mruga Mahesh Kulkarni  
PRN: 25UAM039
1. Project Overview
The BFS vs DFS Graph Search System represents how Breadth-First
Search (BFS) and Depth-First Search (DFS) can search a graph from a
given start node toward a goal node. The user provides the graph, start
node, goal node, and the selected algorithm. The system performs the
selected search and provides a search result, including whether the goal
was found and the path when available.
This project documents the system architecture using the four levels of
the C4 model: Context, Container, Component, and Code-Level diagrams.
2. Objectives
Describe the BFS vs DFS Graph Search System using the full C4 model.
Show how the user interacts with the system.
Divide the system into containers with clear responsibilities.
Explain the internal components of the Search Engine.
Identify the main classes and operations shown in the code-level
diagram.
3. C4 Architecture
C1 --- Context Diagram
The context diagram shows the User as the external actor and the
BFS vs DFS Graph Search System as the system being designed.
Input from the user: - Graph - Start node - Goal node - Selected
algorithm (BFS or DFS)
Output to the user: - Search result - Goal status - Path, when
found - Number of nodes expanded, as represented in the diagram
C2 --- Container Diagram
The container diagram shows five main parts inside the system:
Input Module --- accepts the graph, start node, goal node, and
selected algorithm.
Graph Manager --- stores and manages graph nodes and edges.
Search Engine --- performs BFS or DFS according to the selected
algorithm.
Visited / Memory Manager --- tracks visited nodes and search
states.
Output Module --- displays the search result and found path.
The diagram shows the flow from input handling to graph management,
search, visited-state tracking, and output.
C3 --- Component Diagram
The component diagram focuses on the Search Engine and shows these
components:
BFS / DFS Controller --- coordinates the selected search
algorithm.
Frontier Manager --- uses a queue for BFS and a stack for DFS.
Visited / Explored Set --- tracks nodes that have already been
visited.
Goal Test --- checks whether the current node is the goal node.
Path Reconstructor --- reconstructs the path from the start node
to the goal node.
BFS uses a queue (FIFO), while DFS uses a stack (LIFO), as shown in the
architecture.
C4 --- Code-Level Diagram
The code-level diagram identifies the following classes and operations:
Class            Main attributes or operations
---
`SearchEngine`   `algorithm: String`, `search(graph, start, goal)`
`BFS`            `search()`; uses a queue (FIFO)
`DFS`            `search()`; uses a stack (LIFO)
`Graph`          `nodes`, `edges`, `addNode()`, `addEdge()`
`SearchResult`   `found: Boolean`, `path: List`, `getPath()`
The diagram connects `SearchEngine` to the BFS and DFS implementations
and shows the graph and search result as related parts of the design.
4. Technologies and Concepts
Graph representation: nodes and edges
Breadth-First Search (BFS): explores using a queue (FIFO)
Depth-First Search (DFS): explores using a stack (LIFO)
C4 model: Context, Container, Component, and Code-Level
architecture
Diagramming tool: diagrams.net / draw.io
5. How the System Works
The user supplies a graph, start node, goal node, and algorithm
choice.
The Input Module receives the values.
The Graph Manager stores or manages the graph's nodes and edges.
The Search Engine runs BFS or DFS.
The Visited / Memory Manager tracks visited nodes and search states.
The Goal Test checks whether the goal has been reached.
The Path Reconstructor reconstructs the path when the goal is found.
The Output Module presents the search result.
6. Project Structure
The architecture and documentation files can be organized as follows:
``` text
SLE3_25UAM039_MrugaKulkarni/
├── c1.png
├── c2.png
├── c3.png
├── c4.png
├── C1_Context.drawio
├── C2_Container.drawio
├── C3_Component.drawio
├── C4_Code.drawio
├── README.md
├── AI_CONTRIBUTION_LOG.md
└── SLE3_Documentation.docx
```
Keep the filenames aligned with the names you actually use in your
folder. Add the Python implementation files too if they are part of your
submission.
7. How to Run
The supplied diagrams describe the architecture; they do not, by
themselves, provide an executable implementation. If Python source files
are included in your project, open a terminal in the project folder and
run the actual program's entry-point file, for example:
``` bash
python main.py
```
Use this command only if your implementation has a `main.py` file.
Otherwise, replace it with the correct filename for your program. The
exact run command and expected console output cannot be confirmed from
the diagrams alone.
8. Expected Result
The system is designed to report whether the goal node was found and
provide the path when one is available. The C1 diagram also represents
the number of nodes expanded as part of the search result. The actual
output depends on the graph, start node, goal node, and selected
algorithm.
9. Conclusion
The full C4 model describes the BFS vs DFS Graph Search System at four
levels, from the user's interaction with the overall system to its
containers, Search Engine components, and code-level classes. The
diagrams show the responsibilities of the system modules and the
different frontier structures used by BFS and DFS.
10. Student Details
Name: Mruga Mahesh Kulkarni
PRN: 25UAM039
Course: 02AML204 -- Introduction to Artificial Intelligence