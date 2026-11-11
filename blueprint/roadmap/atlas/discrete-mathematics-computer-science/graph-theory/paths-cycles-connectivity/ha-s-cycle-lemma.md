---
declaration: section
origin: cited
lean: SimpleGraph.Walk.IsBoundVertex, SimpleGraph.Walk.isBoundVertex_iff, SimpleGraph.IsVertexConnected.exists_cycle_bound_vertex
statement: formalized
proof: formalized
---

# Říha's cycle lemma

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/ha-s-cycle-lemma/index.html).

## Bound vertices of a closed walk

Let $c$ be a closed walk in a simple graph $G$. A vertex
$y$ is bound to $c$ when $y$ lies on $c$ and every neighbor of $y$ in $G$ lies on $c$.

Formalized by `SimpleGraph.Walk.IsBoundVertex`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Riha.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Riha.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/ha-s-cycle-lemma/index.html#is-bound-vertex).

## Characterization of bound vertices

Let $c$ be a closed walk in a simple graph $G$. A
vertex $y$ is bound to $c$ if and only if $y$ lies on $c$ and every neighbor of $y$ in $G$ lies
on $c$.

Formalized by `SimpleGraph.Walk.isBoundVertex_iff`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Riha.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Riha.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/ha-s-cycle-lemma/index.html#is-bound-vertex-iff).

## Říha's cycle lemma

Let $G$ be a finite $2$-vertex-connected simple graph. Then for
every vertex $x$ of $G$ there is a cycle $c$ through $x$ and a vertex $y \ne x$ that is bound
to $c$: $y$ lies on $c$ and every neighbor of $y$ in $G$ lies on $c$.

Formalized by `SimpleGraph.IsVertexConnected.exists_cycle_bound_vertex`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Riha.lean, line 567](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Riha.lean#L567). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/ha-s-cycle-lemma/index.html#exists-cycle-bound-vertex).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Říha's cycle lemma](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/ha-s-cycle-lemma/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/paths-cycles-connectivity/ha-s-cycle-lemma)
