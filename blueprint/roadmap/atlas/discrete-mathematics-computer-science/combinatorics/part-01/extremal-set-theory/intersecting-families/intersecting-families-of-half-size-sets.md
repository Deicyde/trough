---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.TwoIntersectingHalfSetsErdosProblem83Wanted.twoIntersectingHalfSetsBound, MathlibExt.Combinatorics.TwoIntersectingHalfSetsErdosProblem83Wanted.twoIntersectingHalfSetsBound_holds
statement: formalized
---

# Intersecting families of half-size sets

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/intersecting-families-of-half-size-sets/index.html).

## Erdős Problem 83

The assertion that, for every natural number $n$, every family $F$ of
$2n$-element subsets of $\{0, \dots, 4n-1\}$ such that $|A \cap B| \ge 2$ for all $A, B \in F$
(including $A = B$) satisfies $2|F| + \binom{2n}{n}^2 \le \binom{4n}{2n}$, that is,
$|F| \le \frac{1}{2}\left(\binom{4n}{2n} - \binom{2n}{n}^2\right)$.

Formalized by `MathlibExt.Combinatorics.TwoIntersectingHalfSetsErdosProblem83Wanted.twoIntersectingHalfSetsBound`, a definition declared in [WantedExt/Combinatorics/TwoIntersectingHalfSetsErdosProblem83Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/TwoIntersectingHalfSetsErdosProblem83Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/intersecting-families-of-half-size-sets/index.html#two-intersecting-half-sets-bound).

## Bound for 2-intersecting families of half-size sets (Erdős Problem 83)

For every natural
number $n$, every family $F$ of $2n$-element subsets of $\{0, \dots, 4n-1\}$ such that
$|A \cap B| \ge 2$ for all $A, B \in F$ (including $A = B$) satisfies
$2|F| + \binom{2n}{n}^2 \le \binom{4n}{2n}$, that is,
$|F| \le \frac{1}{2}\left(\binom{4n}{2n} - \binom{2n}{n}^2\right)$.

Ahlswede and Khachatrian proved this as a case of their complete intersection theorem, which
determines the largest $t$-intersecting families of $k$-element subsets of an $m$-element set. The
bound is attained by the $2n$-element sets with at least $n + 1$ elements in $\{0, \dots, 2n-1\}$.

## Sources

- T. F. Bloom, Erdős Problems, Problem #83, https://www.erdosproblems.com/83 (status PROVED (LEAN)); resolution: R. Ahlswede and L. H. Khachatrian, The complete intersection theorem for systems of finite sets, European J. Combin. 18 (1997), 125-136, erdosproblems.com/83: for 2 ≤ t ≤ k ≤ m and r with 1/(r + 1) ≤ (m - 2k + 2t - 2)/((t - 1)(k - t + 1)) < 1/r, the largest family of k-subsets of [m] with pairwise intersections of size at least t consists of the k-sets with at least t + r elements of {1, …, t + 2r}; for m = 4n, k = 2n, t = 2 the ratio is 2/(2n - 1), so r = n - 1 and the family is the 2n-sets with at least n + 1 elements of [2n], https://doi.org/10.1006/eujc.1995.0092.

Stated but not proved: `MathlibExt.Combinatorics.TwoIntersectingHalfSetsErdosProblem83Wanted.twoIntersectingHalfSetsBound_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/TwoIntersectingHalfSetsErdosProblem83Wanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/TwoIntersectingHalfSetsErdosProblem83Wanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/intersecting-families-of-half-size-sets/index.html#two-intersecting-half-sets-bound-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Intersecting families of half-size sets](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/intersecting-families-of-half-size-sets/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/extremal-set-theory/intersecting-families/intersecting-families-of-half-size-sets)
