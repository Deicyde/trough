---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.DisjunctiveRadoWanted.exists_bounded_rep, MetaMathlibExt.schur_ramsey
statement: formalized
---

# Schur and Rado theorems: its own results

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/index.html).

Monochromatic solutions of equations: Schur's theorem and Schur and modular Schur numbers, Rado's theorem and disjunctive Rado, monochromatic linear equations, monochromatic sums, sums of squares and products, and rainbow-free colourings of x−y=z^k.

## Bounded representations with one scaled part

Let $a$, $\lambda$, $n$ and $N$ be natural
numbers with $a \ge 3$, $n \ge 1$, $\lambda \ge a - 1$ and $N \le \lambda (a + n)$. Then there are
natural numbers $x_0, \dots, x_{n-1}$ and $y$, each at most $\lambda$, such that
$x_0 + \dots + x_{n-1} + a y = N$.

The endpoint $N = 0$ is included as in the paper's displayed range $\{0, \dots, \lambda(a + n)\}$;
that case is trivial, all parts being $0$.

## Sources

- Srashti Dwivedi and Amitabha Tripathi, "On the Two-Color Disjunctive Rado Number for the Equations `∑_{i=1}^{m-2} x_i + a x_{m-1} - x_m = c_j`, `j = 1, 2`", Proposition 4.

Stated but not proved: `MathlibExt.Combinatorics.DisjunctiveRadoWanted.exists_bounded_rep` is written with `theorem_wanted` in [WantedExt/Combinatorics/DisjunctiveRadoWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/DisjunctiveRadoWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/index.html#exists-bounded-rep).

## Schur's theorem

For every integer $r \ge 1$ there is a natural number $S$ such that for
every coloring of the natural numbers with $r$ colors there are $x, y, z \in \{1, \dots, S\}$,
not necessarily distinct, with the same color and $x + y = z$.

The bound comes from Ramsey's theorem for pairs, by coloring each pair with the color of its
difference; it is not the Schur number $S(r)$, the largest $S$ for which some $r$-coloring of
$\{1, \dots, S\}$ has no such solution.

## Sources

- https://en.wikipedia.org/wiki/Schur%27s_theorem.

Formalized by `MetaMathlibExt.schur_ramsey`, a theorem declared in [MathlibExt/Combinatorics/SchurRamsey.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SchurRamsey.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/index.html#schur-ramsey).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Schur and Rado theorems](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems)
