---
declaration: section
origin: cited
lean: SimpleGraph.Walk.isPath_append_of_isPath
statement: formalized
proof: formalized
---

# Paths, cycles and connectivity: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/index.html).

Walks, paths and cycles in graphs, Eulerian and Hamiltonian cycles, and vertex and edge connectivity, including Menger's theorem and Fleischner's theorem on squares of 2-connected graphs.

## Concatenation of paths meeting at one endpoint is a path

Two paths that meet only at their common endpoint `m` concatenate to a path.

Formalized by `SimpleGraph.Walk.isPath_append_of_isPath`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/WalkPath.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/WalkPath.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/index.html#is-path-append-of-is-path).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Paths, cycles and connectivity](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/paths-cycles-connectivity)
