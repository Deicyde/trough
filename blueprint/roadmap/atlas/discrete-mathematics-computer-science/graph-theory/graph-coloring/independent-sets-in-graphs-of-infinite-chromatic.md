---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.ErdosProblem750Wanted.conjecture, MathlibExt.Combinatorics.ErdosProblem750Wanted.conjecture_holds
statement: formalized
---

# Independent sets in graphs of infinite chromatic number

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/independent-sets-in-graphs-of-infinite-chromatic/index.html).

## Erdős Problem 750

The statement that the following three assertions all hold.
(i) For every function
$f : \mathbb{N} \to \mathbb{R}_{\ge 0}$ with $f(m) \to \infty$ as $m \to \infty$ there is a
simple graph $G$ with infinite chromatic number such that for every $m > 0$, every set $S$ of
exactly $m$ vertices of $G$ contains an independent set $I$ of $G$ with $|I| \ge m/2 - f(m)$.
(ii) For every real $\varepsilon > 0$ there is a simple graph $G$ with infinite chromatic number
such that for every $m > 0$, every set of exactly $m$ vertices of $G$ contains an independent
set of $G$ with at least $m/2 - \varepsilon m$ elements. (iii) For every real $c > 1/4$ there
is a simple graph $G$ with infinite chromatic number such that for every $m > 0$, every set of
exactly $m$ vertices of $G$ contains an independent set of $G$ with at least $m/2 - cm$
elements.

Formalized by `MathlibExt.Combinatorics.ErdosProblem750Wanted.conjecture`, a definition declared in [WantedExt/Combinatorics/ErdosProblem750Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ErdosProblem750Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/independent-sets-in-graphs-of-infinite-chromatic/index.html#conjecture).

## Erdős Problem 750 is true

The following three statements hold. (i) For every function
$f : \mathbb{N} \to \mathbb{R}_{\ge 0}$ with $f(m) \to \infty$ as $m \to \infty$ there is a
simple graph $G$ with infinite chromatic number such that for every $m > 0$, every set $S$ of
exactly $m$ vertices of $G$ contains an independent set $I$ of $G$ with $|I| \ge m/2 - f(m)$.
(ii) For every real $\varepsilon > 0$ there is a simple graph $G$ with infinite chromatic number
such that for every $m > 0$, every set of exactly $m$ vertices of $G$ contains an independent
set of $G$ with at least $m/2 - \varepsilon m$ elements. (iii) For every real $c > 1/4$ there
is a simple graph $G$ with infinite chromatic number such that for every $m > 0$, every set of
exactly $m$ vertices of $G$ contains an independent set of $G$ with at least $m/2 - cm$
elements.

## Sources

- plby/lean-proofs, https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos750.lean#L41.

Stated but not proved: `MathlibExt.Combinatorics.ErdosProblem750Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/ErdosProblem750Wanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ErdosProblem750Wanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/independent-sets-in-graphs-of-infinite-chromatic/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Independent sets in graphs of infinite chromatic number](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/independent-sets-in-graphs-of-infinite-chromatic/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/graph-coloring/part-01/independent-sets-in-graphs-of-infinite-chromatic)
