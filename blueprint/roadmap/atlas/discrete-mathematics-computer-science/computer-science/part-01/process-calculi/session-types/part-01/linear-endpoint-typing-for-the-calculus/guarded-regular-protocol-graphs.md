---
declaration: section
origin: cited
lean: Cslib.SessionTypes.Endpoint.Node, Cslib.SessionTypes.Endpoint.Graph
statement: formalized
proof: formalized
---

# Guarded regular protocol graphs

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/guarded-regular-protocol-graphs/index.html).

## Node of a guarded protocol graph

A graph node: completion or a communication with a bounded continuation.
Endpoint payloads include their role, rank, cursor and protocol orientation.

Formalized by `Cslib.SessionTypes.Endpoint.Node`, an inductive type declared in [CSLibExt/Languages/SessionTypes/Endpoint/Graph.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Graph.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/guarded-regular-protocol-graphs/index.html#node).

## Finite guarded regular protocol graph

Finite presentation of guarded equi-recursive protocols. An empty graph
has no cursor and therefore cannot denote a protocol.

Formalized by `Cslib.SessionTypes.Endpoint.Graph`, a structure declared in [CSLibExt/Languages/SessionTypes/Endpoint/Graph.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Graph.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/guarded-regular-protocol-graphs/index.html#graph).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Guarded regular protocol graphs](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/guarded-regular-protocol-graphs/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/guarded-regular-protocol-graphs)
