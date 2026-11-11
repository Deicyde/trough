---
declaration: section
origin: cited
lean: MetaMathlibExt.barryTriangleAux, MetaMathlibExt.barryTriangleAux_succ_succ, MetaMathlibExt.barryTriangleAux_small_values, MetaMathlibExt.barryTriangleAux_eq_matrix_pow, MetaMathlibExt.barryTriangleAux_eq_sum_antidiagonalTuple
statement: formalized
---

# Barry's Stirling-like triangle

5 results, 3 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/barry-s-stirling-like-triangle/index.html).

## Barry's triangle recurrence

The function $s(\beta, n, k)$ of natural numbers
$\beta, n, k$, with natural-number values, is defined by $s(\beta, 0, 0) = 1$, by
$s(\beta, n, k) = 0$ if exactly one of $n, k$ is $0$, and by

$$s(\beta, n, k) = s(\beta + 1, n - 1, k - 1) + \beta k\, s(\beta, n - 1, k)$$

if $n, k \ge 1$.

The triangle OEIS A080416 is $s(0, n, k)$ for $2 \le k \le n$.

## Sources

- Bulat Khaidarov, *Enumeration of Certain k-Block Partitions of Barry*, Journal of Integer Sequences 29 (2026), Article 26.2.8, equation (1).

Formalized by `MetaMathlibExt.barryTriangleAux`, a definition declared in [WantedExt/Combinatorics/Enumerative/BarryTriangleExplicitFormulasWanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/BarryTriangleExplicitFormulasWanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/barry-s-stirling-like-triangle/index.html#barry-triangle-aux).

## Defining recurrence of Barry's triangle

For all natural numbers $\beta, n, k$, Barry's
triangle recurrence $s$ satisfies
$s(\beta, n + 1, k + 1) = s(\beta + 1, n, k) + \beta (k + 1)\, s(\beta, n, k + 1)$.

## Sources

- Khaidarov, *Enumeration of Certain k-Block Partitions of Barry*, Journal of Integer Sequences 29 (2026), Article 26.2.8, equation (1).

Formalized by `MetaMathlibExt.barryTriangleAux_succ_succ`, a theorem declared in [WantedExt/Combinatorics/Enumerative/BarryTriangleExplicitFormulasWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/BarryTriangleExplicitFormulasWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/barry-s-stirling-like-triangle/index.html#barry-triangle-aux-succ-succ).

## Small values of Barry's triangle

Barry's triangle recurrence $s$ takes the values
$s(0, 2, 2) = 1$, $s(0, 4, 3) = 4$ and $s(0, 6, 4) = 67$.

## Sources

- Khaidarov, *Enumeration of Certain k-Block Partitions of Barry*, Journal of Integer Sequences 29 (2026), Article 26.2.8, Table 1.

Formalized by `MetaMathlibExt.barryTriangleAux_small_values`, a theorem declared in [WantedExt/Combinatorics/Enumerative/BarryTriangleExplicitFormulasWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/BarryTriangleExplicitFormulasWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/barry-s-stirling-like-triangle/index.html#barry-triangle-aux-small-values).

## Matrix power formula for Barry's triangle

Let $s$ be Barry's triangle recurrence and let
$2 \le a \le n$. Let $M$ be the $(a - 1) \times (a - 1)$ lower bidiagonal matrix of natural
numbers with diagonal entries $M_{i,i} = i(a - i)$ for $i = 1, \dots, a - 1$, entries
$M_{i+1,i} = 1$ just below the diagonal, and all other entries $0$. Then $s(0, n, a)$ is the
bottom-left entry $(M^{n-2})_{a-1,1}$ of the power $M^{n-2}$.

## Sources

- Khaidarov, *Enumeration of Certain k-Block Partitions of Barry*, Journal of Integer Sequences 29 (2026), Article 26.2.8, main result announced in the abstract, equation (7) (`jis-2026-26.2.8-abstract-main`).

Stated but not proved: `MetaMathlibExt.barryTriangleAux_eq_matrix_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/BarryTriangleExplicitFormulasWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/BarryTriangleExplicitFormulasWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/barry-s-stirling-like-triangle/index.html#barry-triangle-aux-eq-matrix-pow).

## Matrix-free formula for Barry's triangle

Let $s$ be Barry's triangle recurrence and let
$2 \le a \le n$. Then

$$s(0, n, a) = \sum_{p_1 + \dots + p_{a-1} = n - a} \prod_{i=1}^{a-1} \bigl(i(a - i)\bigr)^{p_i},$$

where the sum runs over all tuples $(p_1, \dots, p_{a-1})$ of natural numbers with sum $n - a$.

## Sources

- Khaidarov, *Enumeration of Certain k-Block Partitions of Barry*, Journal of Integer Sequences 29 (2026), Article 26.2.8, main result announced in the abstract, equation (11) (`jis-2026-26.2.8-abstract-main`).

Stated but not proved: `MetaMathlibExt.barryTriangleAux_eq_sum_antidiagonalTuple` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/BarryTriangleExplicitFormulasWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/BarryTriangleExplicitFormulasWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/barry-s-stirling-like-triangle/index.html#barry-triangle-aux-eq-sum-antidiagonal-t).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Barry's Stirling-like triangle](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/barry-s-stirling-like-triangle/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/barry-s-stirling-like-triangle)
