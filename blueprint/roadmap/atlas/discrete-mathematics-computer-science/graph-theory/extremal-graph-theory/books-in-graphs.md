---
declaration: section
origin: cited
lean: SimpleGraph.bookNumber, SimpleGraph.le_bookNumber, SimpleGraph.bookNumber_le, MathlibExt.Combinatorics.ErdosProblem905Wanted.conjecture, MathlibExt.Combinatorics.ErdosProblem905Wanted.conjecture_holds
statement: formalized
---

# Books in graphs

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/books-in-graphs/index.html).

## Book number

Let $G$ be a finite simple graph. The book number of $G$ is the maximum,
over ordered pairs $(u, v)$ of adjacent vertices, of the number of common neighbors of $u$ and
$v$ (the number of triangles containing the edge $uv$); it is $0$ if $G$ has no edges.

Formalized by `SimpleGraph.bookNumber`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/BookNumber.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/BookNumber.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/books-in-graphs/index.html#book-number).

## Common neighbors of an edge are bounded by the book number

Let $G$ be a finite simple
graph. If $u$ and $v$ are adjacent vertices of $G$, then the number of common neighbors of $u$
and $v$ is at most the book number of $G$.

Formalized by `SimpleGraph.le_bookNumber`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/BookNumber.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/BookNumber.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/books-in-graphs/index.html#le-book-number).

## Bounding the book number

Let $G$ be a finite simple graph and $b$ a natural number. If
every pair of adjacent vertices $u$, $v$ of $G$ has at most $b$ common neighbors, then the book
number of $G$ is at most $b$.

Formalized by `SimpleGraph.bookNumber_le`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/BookNumber.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/BookNumber.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/books-in-graphs/index.html#book-number-le).

## Erdős Problem 905 on edges in many triangles

The proposition asserts that for every
natural number $n$ and every simple graph $G$ on $n$ vertices with more than $n^2/4$ edges, some
edge of $G$ lies in at least $n/6$ triangles of $G$.

Formalized by `MathlibExt.Combinatorics.ErdosProblem905Wanted.conjecture`, a definition declared in [WantedExt/Combinatorics/ErdosProblem905Wanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ErdosProblem905Wanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/books-in-graphs/index.html#conjecture).

## Edwards–Khadzhiivanov–Nikiforov theorem on edges in many triangles

For every natural number
$n$, every simple graph $G$ on $n$ vertices with more than $n^2/4$ edges has an edge that lies in
at least $n/6$ triangles of $G$.

This was proved independently by Edwards and by Khadzhiivanov and Nikiforov, and answers Erdős
Problem 905 affirmatively.

## Sources

- External Lean proof of Erdős Problem 905, https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/v4.29.1/ErdosProblems/Erdos905.lean.

Stated but not proved: `MathlibExt.Combinatorics.ErdosProblem905Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/ErdosProblem905Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ErdosProblem905Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/books-in-graphs/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Books in graphs](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/books-in-graphs/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/extremal-graph-theory/books-in-graphs)
