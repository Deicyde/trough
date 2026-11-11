---
declaration: section
origin: cited
lean: SimpleGraph.incidentSum, SimpleGraph.inducedResidue, SimpleGraph.inducedResidue_val, SimpleGraph.IsEdgeGraceful, SimpleGraph.isEdgeGraceful_iff
statement: formalized
proof: formalized
---

# Edge-graceful labelings

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/edge-graceful-labelings/index.html).

## Incident-edge sum

Let $G$ be a simple graph on a finite vertex set $V$, let $q$ be a
natural number and let $\ell$ be a bijection from the edge set of $G$ to $\{0, 1, \dots, q-1\}$.
The incident-edge sum at a vertex $v$ is $\sum_{e \ni v} (\ell(e) + 1)$, the sum over the edges
$e$ of $G$ that contain $v$; in other words, the edges carry the labels $1, \dots, q$.

Formalized by `SimpleGraph.incidentSum`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeGraceful.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeGraceful.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/edge-graceful-labelings/index.html#incident-sum).

## Induced vertex residue

Let $G$ be a simple graph on a finite vertex set $V$, let $q$ be
a natural number and let $\ell$ be a bijection from the edge set of $G$ to $\{0, \dots, q-1\}$.
The induced residue of a vertex $v$ is the incident-edge sum at $v$ (with edge labels
$\ell(e) + 1$) reduced modulo $|V|$, viewed as an element of $\{0, \dots, |V| - 1\}$. When
$|V| = 0$ there are no vertices, so there is nothing to define.

Formalized by `SimpleGraph.inducedResidue`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeGraceful.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeGraceful.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/edge-graceful-labelings/index.html#induced-residue).

## Value of the induced residue

Let $G$ be a simple graph on a finite nonempty vertex set
$V$, let $q$ be a natural number and let $\ell$ be a bijection from the edge set of $G$ to
$\{0, \dots, q-1\}$. For every vertex $v$, the induced residue of $v$ with respect to $\ell$, read
as a natural number, equals the incident-edge sum at $v$ with respect to $\ell$ modulo $|V|$.

Formalized by `SimpleGraph.inducedResidue_val`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeGraceful.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeGraceful.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/edge-graceful-labelings/index.html#induced-residue-val).

## Edge-graceful graph

A simple graph $G$ on a finite vertex set $V$ is edge-graceful when
there are a natural number $q$ and a bijection $\ell$ from the edge set of $G$ to
$\{0, \dots, q-1\}$ such that the induced residue map, sending each vertex $v$ to the sum of
$\ell(e) + 1$ over the edges $e$ containing $v$ taken modulo $|V|$, is a bijection from $V$ to
$\{0, \dots, |V| - 1\}$.

Formalized by `SimpleGraph.IsEdgeGraceful`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeGraceful.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeGraceful.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/edge-graceful-labelings/index.html#is-edge-graceful).

## Edge-graceful graphs via a vertex bijection

A simple graph $G$ on a finite vertex set $V$
is edge-graceful if and only if there are a natural number $q$, a bijection $\ell$ from the edge
set of $G$ to $\{0, \dots, q-1\}$ and a bijection $\lambda$ from $V$ to $\{0, \dots, |V| - 1\}$ such
that for every vertex $v$, $\lambda(v)$ is the induced residue of $v$ with respect to $\ell$ and,
if $V$ is nonempty, $\lambda(v)$ equals the incident-edge sum at $v$ with respect to $\ell$ modulo
$|V|$.

Formalized by `SimpleGraph.isEdgeGraceful_iff`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/EdgeGraceful.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/EdgeGraceful.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/edge-graceful-labelings/index.html#is-edge-graceful-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Edge-graceful labelings](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/edge-graceful-labelings/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/graph-invariants-and-labelings/edge-graceful-labelings)
