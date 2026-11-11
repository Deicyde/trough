---
declaration: section
origin: cited
lean: MathlibExt.Analysis.SparsePolynomialSquareTermBoundWanted.conjecture, MathlibExt.Analysis.SparsePolynomialSquareTermBoundWanted.conjecture_holds
statement: formalized
---

# Squares of sparse polynomials

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/squares-of-sparse-polynomials/index.html).

## Erdős–Rényi conjecture on squares of sparse polynomials

There is a function
$f : \mathbb{N} \to \mathbb{N}$ such that for every integer $k \ge 1$, every complex polynomial $p$
with at least $f(k)$ nonzero coefficients has a square $p^2$ with at least $k$ nonzero
coefficients.

Formalized by `MathlibExt.Analysis.SparsePolynomialSquareTermBoundWanted.conjecture`, a definition declared in [WantedExt/Analysis/SparsePolynomialSquareTermBoundWanted.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/SparsePolynomialSquareTermBoundWanted.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/squares-of-sparse-polynomials/index.html#conjecture).

## Schinzel's theorem on squares of sparse polynomials

The Erdős–Rényi conjecture holds:
there is a function $f : \mathbb{N} \to \mathbb{N}$ such that for every integer $k \ge 1$, every
complex polynomial $p$ with at least $f(k)$ nonzero coefficients has a square $p^2$ with at least
$k$ nonzero coefficients.

Schinzel (Acta Arith. 49 (1987) 55-70) proved that the number of terms of $g \in \mathbb{C}[x]$
is bounded in terms of the number of terms of $g^2$; Fuchs, Mantova and Zannier
(arXiv:1412.4548, Thm 1.1) give a uniform version.

## Sources

- C. Fuchs, V. Mantova and U. Zannier, On fewnomials, integral points and a toric version of Bertini's theorem (2017), arXiv:1412.4548, https://arxiv.org/abs/1412.4548.

Stated but not proved: `MathlibExt.Analysis.SparsePolynomialSquareTermBoundWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Analysis/SparsePolynomialSquareTermBoundWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/SparsePolynomialSquareTermBoundWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/squares-of-sparse-polynomials/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Squares of sparse polynomials](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/squares-of-sparse-polynomials/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Algebra/polynomials/squares-of-sparse-polynomials)
