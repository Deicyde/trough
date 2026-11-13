---
declaration: section
origin: cited
lean: MathlibExt.Analysis.HadamardProductCircleBoundWanted.ClassS, MathlibExt.Analysis.HadamardProductCircleBoundWanted.hadamardProduct, MathlibExt.Analysis.HadamardProductCircleBoundWanted.circleMax, MathlibExt.Analysis.HadamardProductCircleBoundWanted.conjecture, MathlibExt.Analysis.HadamardProductCircleBoundWanted.conjecture_holds
statement: formalized
---

# Hadamard products of univalent functions

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/hadamard-products-of-univalent-functions/index.html).

## Normalized univalent functions with their Taylor coefficients

An element of the class
$S$ is a function $f : \mathbb{C} \to \mathbb{C}$ together with a sequence $(a_m)_{m \ge 0}$ of
complex numbers such that $f$ is holomorphic and injective on the open unit disk $\mathbb{D}$ of
all $z \in \mathbb{C}$ with $|z| < 1$, $f(0) = 0$, $f'(0) = 1$, $a_0 = 0$, $a_1 = 1$, and for every
$z \in \mathbb{D}$ the series $\sum_{m \ge 0} a_m z^m$ is unconditionally summable with sum $f(z)$.

## Sources

- [AMR-022-6028] Problem 6.28.

Formalized by `MathlibExt.Analysis.HadamardProductCircleBoundWanted.ClassS`, a structure declared in [WantedExt/Analysis/HadamardProductCircleBoundWanted.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/HadamardProductCircleBoundWanted.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/hadamard-products-of-univalent-functions/index.html#class-s).

## Truncated Hadamard product with a polynomial

For a sequence $(a_k)_{k \ge 0}$ of complex
numbers, a complex polynomial $P(z) = \sum_k p_k z^k$ and $n \in \mathbb{N}$, this is the
polynomial $\sum_{k=0}^{n} a_k p_k z^k$: the coefficient-wise (Hadamard) product of $P$ with the
power series $\sum_k a_k z^k$, truncated at degree $n$.

## Sources

- [AMR-022-6028] Problem 6.28.

Formalized by `MathlibExt.Analysis.HadamardProductCircleBoundWanted.hadamardProduct`, a definition declared in [WantedExt/Analysis/HadamardProductCircleBoundWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/HadamardProductCircleBoundWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/hadamard-products-of-univalent-functions/index.html#hadamard-product).

## Sup norm of a polynomial on the unit circle

For a complex polynomial $Q$, this is the
real number $\sup_{|z| = 1} |Q(z)|$, the supremum of $|Q(z)|$ over all $z \in \mathbb{C}$ with
$|z| = 1$.

## Sources

- [AMR-022-6028] Problem 6.28.

Formalized by `MathlibExt.Analysis.HadamardProductCircleBoundWanted.circleMax`, a definition declared in [WantedExt/Analysis/HadamardProductCircleBoundWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/HadamardProductCircleBoundWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/hadamard-products-of-univalent-functions/index.html#circle-max).

## Statement of the Hadamard product circle bound

The proposition that for every
$n \in \mathbb{N}$, every function $f(z) = \sum_{m \ge 0} a_m z^m$ of the class $S$ of normalized
univalent functions on the unit disk, and every complex polynomial $P(z) = \sum_k p_k z^k$ of
degree at most $n$,

$$
\sup_{|z| = 1} \Bigl| \sum_{k=0}^{n} a_k p_k z^k \Bigr| \le n \sup_{|z| = 1} |P(z)|.
$$

## Sources

- [AMR-022-6028] Problem 6.28, where it is posed as an open question.

Formalized by `MathlibExt.Analysis.HadamardProductCircleBoundWanted.conjecture`, a definition declared in [WantedExt/Analysis/HadamardProductCircleBoundWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/HadamardProductCircleBoundWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/hadamard-products-of-univalent-functions/index.html#conjecture).

## Hadamard product circle bound for univalent functions

For every $n \in \mathbb{N}$, every
function $f(z) = \sum_{m \ge 0} a_m z^m$ of the class $S$ of normalized univalent functions on the
unit disk, and every complex polynomial $P(z) = \sum_k p_k z^k$ of degree at most $n$,

$$
\sup_{|z| = 1} \Bigl| \sum_{k=0}^{n} a_k p_k z^k \Bigr| \le n \sup_{|z| = 1} |P(z)|.
$$

Robertson's conjecture implies the bound (Sheil-Small, J. Reine Angew. Math. 258 (1973)), and de
Branges (Acta Math. 154 (1985)) proved Milin's conjecture, hence Robertson's. Both facts are
recorded in Hayman-Lingham (arXiv:1809.07200, Problem 6.28, Update 6.1).

## Sources

- Walter K. Hayman and Eleanor F. Lingham, Research Problems in Function Theory (New Edition), arXiv:1809.07200v2 (2018), https://arxiv.org/abs/1809.07200.

Stated but not proved: `MathlibExt.Analysis.HadamardProductCircleBoundWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Analysis/HadamardProductCircleBoundWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/HadamardProductCircleBoundWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/hadamard-products-of-univalent-functions/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hadamard products of univalent functions](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/hadamard-products-of-univalent-functions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/complex-analysis/geometric-function-theory/hadamard-products-of-univalent-functions)
