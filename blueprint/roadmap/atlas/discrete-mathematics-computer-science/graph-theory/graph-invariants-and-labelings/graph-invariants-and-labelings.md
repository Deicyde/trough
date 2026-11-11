---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.SimpleGraph.ErdosGallaiWanted.erdos_gallai
statement: formalized
proof: formalized
---

# Graph invariants and labelings: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/index.html).

Numerical and polynomial invariants of graphs such as degree sequences, arboricity, induced forest number, Shannon capacity and the chromatic symmetric function, and graph labelings.

## Erdős–Gallai theorem

Let $V$ be a finite set and $d \colon V \to \mathbb{N}$. There is a
simple graph on $V$ in which every vertex $v$ has degree $d(v)$ if and only if the sum
$\sum_{v \in V} d(v)$ is even and, for every subset $S \subseteq V$,

$$\sum_{v \in S} d(v) \le |S|(|S| - 1) + \sum_{v \in V \setminus S} \min(d(v), |S|).$$

## Sources

- P. Erdős and T. Gallai, Graphs with prescribed degrees of vertices, Matematikai Lapok 11 (1960), 264-274.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.ErdosGallaiWanted.erdos_gallai`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/ErdosGallai.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/ErdosGallai.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/index.html#erdos-gallai).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Graph invariants and labelings](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/graph-invariants-and-labelings)
