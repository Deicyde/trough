---
declaration: section
origin: cited
lean: MetaMathlibExt.whittGeneralizedCatalan, MetaMathlibExt.whittGeneralizedCatalan_succ, MetaMathlibExt.whittGeneralizedCatalan_zero, MetaMathlibExt.whittGeneralizedCatalan_one, MetaMathlibExt.whittGeneralizedCatalan_zero_left, MetaMathlibExt.whittGeneralizedCatalan_two_small
statement: formalized
proof: formalized
---

# Whitt's generalized Catalan numbers

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/whitt-s-generalized-catalan-numbers/index.html).

## Whitt's generalized Catalan numbers

For a rational number $\alpha$ and a natural number
$n$, Whitt's generalized Catalan number $C(\alpha, n)$ is the rational number

$$C(\alpha, n) = \sum_{k=0}^{n-1} \left(1 - \frac{k}{n}\right) \binom{n-1+k}{k} \alpha^k.$$

In particular $C(\alpha, 0) = 0$, the empty sum. Writing $n + 1$ for $n$ gives the source's form
$C(\alpha, n+1) = \sum_{k=0}^{n} \left(1 - \frac{k}{n+1}\right) \binom{n+k}{k} \alpha^k$. For
$\alpha = 2$ and $n \ge 1$ these are the terms of OEIS A064062.

## Sources

- Sabar Taoufik, *A New Triangle of Numbers: Properties and Observations*, INTEGERS 26 (2026), Article A27, Section 5 (definition of `C(α, n+1)`, quoting W. Whitt, J. Integer Seq. 14 (2011)).

Formalized by `MetaMathlibExt.whittGeneralizedCatalan`, a definition declared in [MathlibExt/Combinatorics/Enumerative/WhittGeneralizedCatalan.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/WhittGeneralizedCatalan.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/whitt-s-generalized-catalan-numbers/index.html#whitt-generalized-catalan).

## Whitt's generalized Catalan numbers in the source's indexing

For every rational number
$\alpha$ and every natural number $n$, Whitt's generalized Catalan number $C(\alpha, n + 1)$ is

$$C(\alpha, n + 1) = \sum_{k=0}^{n} \left(1 - \frac{k}{n+1}\right) \binom{n+k}{k} \alpha^k.$$

## Sources

- Sabar Taoufik, *A New Triangle of Numbers: Properties and Observations*, INTEGERS 26 (2026), Article A27, Section 5 (definition of `C(α, n+1)`).

Formalized by `MetaMathlibExt.whittGeneralizedCatalan_succ`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/WhittGeneralizedCatalan.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/WhittGeneralizedCatalan.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/whitt-s-generalized-catalan-numbers/index.html#whitt-generalized-catalan-succ).

## Whitt's generalized Catalan number at zero

For every rational number $\alpha$, Whitt's
generalized Catalan number $C(\alpha, 0)$ equals $0$, being an empty sum.

## Sources

- Sabar Taoufik, *A New Triangle of Numbers: Properties and Observations*, INTEGERS 26 (2026), Article A27, Section 5 (definition of `C(α, n+1)`).

Formalized by `MetaMathlibExt.whittGeneralizedCatalan_zero`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/WhittGeneralizedCatalan.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/WhittGeneralizedCatalan.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/whitt-s-generalized-catalan-numbers/index.html#whitt-generalized-catalan-zero).

## Whitt's generalized Catalan number at one

For every rational number $\alpha$, Whitt's
generalized Catalan number $C(\alpha, 1)$ equals $1$.

## Sources

- Sabar Taoufik, *A New Triangle of Numbers: Properties and Observations*, INTEGERS 26 (2026), Article A27, Section 5 (definition of `C(α, n+1)` at `n = 0`).

Formalized by `MetaMathlibExt.whittGeneralizedCatalan_one`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/WhittGeneralizedCatalan.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/WhittGeneralizedCatalan.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/whitt-s-generalized-catalan-numbers/index.html#whitt-generalized-catalan-one).

## Whitt's generalized Catalan numbers with parameter zero

For every natural number
$n \ge 1$, Whitt's generalized Catalan number $C(0, n)$ equals $1$: only the term $k = 0$ of the
defining sum survives.

## Sources

- Sabar Taoufik, *A New Triangle of Numbers: Properties and Observations*, INTEGERS 26 (2026), Article A27, Section 5 (definition of `C(α, n+1)`).

Formalized by `MetaMathlibExt.whittGeneralizedCatalan_zero_left`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/WhittGeneralizedCatalan.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/WhittGeneralizedCatalan.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/whitt-s-generalized-catalan-numbers/index.html#whitt-generalized-catalan-zero-left).

## First values of Whitt's generalized Catalan numbers with parameter two

Whitt's
generalized Catalan numbers with parameter $\alpha = 2$ satisfy $C(2, 1) = 1$, $C(2, 2) = 3$,
$C(2, 3) = 13$ and $C(2, 4) = 67$.

## Sources

- Sabar Taoufik, *A New Triangle of Numbers: Properties and Observations*, INTEGERS 26 (2026), Article A27, Section 5 (OEIS A064062).

Formalized by `MetaMathlibExt.whittGeneralizedCatalan_two_small`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/WhittGeneralizedCatalan.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/WhittGeneralizedCatalan.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/whitt-s-generalized-catalan-numbers/index.html#whitt-generalized-catalan-two-small).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Whitt's generalized Catalan numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/whitt-s-generalized-catalan-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/whitt-s-generalized-catalan-numbers)
