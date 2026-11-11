---
declaration: section
origin: cited
lean: SimpleGraph.IsDezaWith, SimpleGraph.IsDezaWith.a_le_k, SimpleGraph.IsDezaWith.b_lt_n, SimpleGraph.IsDezaWith.a_lt_n
statement: formalized
proof: formalized
---

# Deza graphs

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/deza-graphs/index.html).

## Deza graph

Let $G$ be a simple graph on a finite vertex set $V$, and let $n, k, b, a$ be
natural numbers. Then $G$ is a Deza graph with parameters $(n, k, b, a)$ when $a \le b \le k < n$,
$V$ has exactly $n$ elements, every vertex of $G$ has degree $k$, and any two distinct vertices of
$G$ have exactly $a$ or exactly $b$ common neighbours, whether or not they are adjacent.

## Sources

- Golubyatnikov, https://arxiv.org/abs/2608.13089v1, lines 163--164.

Formalized by `SimpleGraph.IsDezaWith`, a structure declared in [MathlibExt/Combinatorics/SimpleGraph/Deza.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Deza.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/deza-graphs/index.html#is-deza-with).

## Parameter bound $a \le k$ for Deza graphs

If a finite simple graph $G$ is a Deza graph
with parameters $(n, k, b, a)$, then $a \le k$.

Formalized by `SimpleGraph.IsDezaWith.a_le_k`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Deza.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Deza.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/deza-graphs/index.html#a-le-k).

## Parameter bound $b < n$ for Deza graphs

If a finite simple graph $G$ is a Deza graph
with parameters $(n, k, b, a)$, then $b < n$.

Formalized by `SimpleGraph.IsDezaWith.b_lt_n`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Deza.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Deza.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/deza-graphs/index.html#b-lt-n).

## Parameter bound $a < n$ for Deza graphs

If a finite simple graph $G$ is a Deza graph
with parameters $(n, k, b, a)$, then $a < n$.

Formalized by `SimpleGraph.IsDezaWith.a_lt_n`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Deza.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Deza.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/deza-graphs/index.html#a-lt-n).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Deza graphs](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/deza-graphs/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/algebraic-graph-theory/part-01/deza-graphs)
