---
declaration: section
origin: cited
lean: ZeroDivisorGraph.Vertex, ZeroDivisorGraph.zeroDivisorGraph, ZeroDivisorGraph.exists_vertex_iff, ZeroDivisorGraph.adj_iff
statement: formalized
proof: formalized
---

# Zero-divisor graph

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/zero-divisor-graph/index.html).

## Nonzero zero divisors

For a commutative ring $R$, this is the set of elements
$r \in R$ with $r \neq 0$ such that $sr = 0$ for some nonzero $s \in R$, that is, the nonzero
zero divisors of $R$. They are the vertices of the zero-divisor graph of $R$.

Formalized by `ZeroDivisorGraph.Vertex`, an abbreviation declared in [MathlibExt/RingTheory/ZeroDivisorGraph.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/ZeroDivisorGraph.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/zero-divisor-graph/index.html#vertex).

## The zero-divisor graph

For a commutative ring $R$, the zero-divisor graph of $R$ is
the simple graph whose vertices are the nonzero zero divisors of $R$, in which two distinct
vertices $v$ and $w$ are adjacent exactly when $vw = 0$.

Formalized by `ZeroDivisorGraph.zeroDivisorGraph`, a definition declared in [MathlibExt/RingTheory/ZeroDivisorGraph.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/ZeroDivisorGraph.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/zero-divisor-graph/index.html#zero-divisor-graph).

## Vertices are the nonzero zero divisors

Let $R$ be a commutative ring. An element
$r \in R$ is a vertex of the zero-divisor graph of $R$ if and only if $r \neq 0$ and $r$ is a
zero divisor, that is, $sr = 0$ for some nonzero $s \in R$.

Formalized by `ZeroDivisorGraph.exists_vertex_iff`, a theorem declared in [MathlibExt/RingTheory/ZeroDivisorGraph.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/ZeroDivisorGraph.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/zero-divisor-graph/index.html#exists-vertex-iff).

## Adjacency in the zero-divisor graph

Let $R$ be a commutative ring. Two vertices $v$
and $w$ of the zero-divisor graph of $R$ are adjacent if and only if $v \neq w$ and $vw = 0$.

Formalized by `ZeroDivisorGraph.adj_iff`, a theorem declared in [MathlibExt/RingTheory/ZeroDivisorGraph.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/ZeroDivisorGraph.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/zero-divisor-graph/index.html#adj-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Zero-divisor graph](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/zero-divisor-graph/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RingTheory/ideals-and-constructions/zero-divisor-graph)
