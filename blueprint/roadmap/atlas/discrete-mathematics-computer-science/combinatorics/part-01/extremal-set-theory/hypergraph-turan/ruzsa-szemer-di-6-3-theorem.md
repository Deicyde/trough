---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.SixPointsThreeTriplesErdosProblem716Wanted.sixThreeExtremalNumber, MathlibExt.Combinatorics.SixPointsThreeTriplesErdosProblem716Wanted.sixThreeExtremalNumberLittleO, MathlibExt.Combinatorics.SixPointsThreeTriplesErdosProblem716Wanted.sixThreeExtremalNumberLittleO_holds
statement: formalized
---

# Ruzsa–Szemerédi (6,3) theorem

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/ruzsa-szemer-di-6-3-theorem/index.html).

## The (6, 3) extremal number

For $n \in \mathbb{N}$, $\mathrm{ex}_3(n)$ is the largest
number of $3$-element subsets of $\{1, \dots, n\}$ such that every set of at most $6$ of these
points contains at most $2$ of the chosen subsets.

For $n \ge 6$ this is the extremal number $\mathrm{ex}_3(n, \mathcal{F})$ of the family
$\mathcal{F}$ of $3$-uniform hypergraphs with $6$ vertices and $3$ edges, since a set of triples
contains a member of $\mathcal{F}$ exactly when some $6$ points carry $3$ of the triples.

Formalized by `MathlibExt.Combinatorics.SixPointsThreeTriplesErdosProblem716Wanted.sixThreeExtremalNumber`, a definition declared in [WantedExt/Combinatorics/SixPointsThreeTriplesErdosProblem716Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SixPointsThreeTriplesErdosProblem716Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/ruzsa-szemer-di-6-3-theorem/index.html#six-three-extremal-number).

## The Brown–Erdős–Sós (6, 3) conjecture

For $n \in \mathbb{N}$ let $\mathrm{ex}_3(n)$ be
the largest number of $3$-element subsets of $\{1, \dots, n\}$ such that every set of at most $6$
of these points contains at most $2$ of the chosen subsets. The conjecture (Erdős Problem 716) is
the proposition that $\mathrm{ex}_3(n) / n^2 \to 0$ as $n \to \infty$, that is,
$\mathrm{ex}_3(n) = o(n^2)$.

Formalized by `MathlibExt.Combinatorics.SixPointsThreeTriplesErdosProblem716Wanted.sixThreeExtremalNumberLittleO`, a definition declared in [WantedExt/Combinatorics/SixPointsThreeTriplesErdosProblem716Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SixPointsThreeTriplesErdosProblem716Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/ruzsa-szemer-di-6-3-theorem/index.html#six-three-extremal-number-little-o).

## The Ruzsa–Szemerédi (6, 3) theorem

For $n \in \mathbb{N}$ let $\mathrm{ex}_3(n)$ be the
largest number of $3$-element subsets of $\{1, \dots, n\}$ such that every set of at most $6$ of
these points contains at most $2$ of the chosen subsets. Then $\mathrm{ex}_3(n) / n^2 \to 0$ as
$n \to \infty$, that is, $\mathrm{ex}_3(n) = o(n^2)$.

## Sources

- T. F. Bloom, Erdős Problems, Problem #716, https://www.erdosproblems.com/716 (status PROVED (LEAN)); resolution: I. Z. Ruzsa and E. Szemerédi, Triple systems with no six points carrying three triangles, Combinatorics (Proc. Fifth Hungarian Colloq., Keszthely, 1976), Vol. II (1978), 939-945, erdosproblems.com/716: 'The answer is yes, proved by Ruzsa and Szemerédi' (the Ruzsa-Szemerédi problem), https://www.erdosproblems.com/716.

Stated but not proved: `MathlibExt.Combinatorics.SixPointsThreeTriplesErdosProblem716Wanted.sixThreeExtremalNumberLittleO_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/SixPointsThreeTriplesErdosProblem716Wanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SixPointsThreeTriplesErdosProblem716Wanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/ruzsa-szemer-di-6-3-theorem/index.html#six-three-extremal-number-little-o-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ruzsa–Szemerédi (6,3) theorem](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/ruzsa-szemer-di-6-3-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/ruzsa-szemer-di-6-3-theorem)
