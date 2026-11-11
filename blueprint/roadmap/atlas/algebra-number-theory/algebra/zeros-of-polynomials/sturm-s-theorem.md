---
declaration: section
origin: cited
lean: MathlibExt.Algebra.SturmWanted.Algebra.sturmAux, MathlibExt.Algebra.SturmWanted.Algebra.sturmChain, MathlibExt.Algebra.SturmWanted.Algebra.signChanges, MathlibExt.Algebra.SturmWanted.Algebra.sigma, MathlibExt.Algebra.SturmWanted.Algebra.sturm
statement: formalized
---

# Sturm's theorem

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/sturm-s-theorem/index.html).

## Negated-remainder sequence with fuel

For real polynomials $a$, $b$ and a natural
number $n$, this is the list of polynomials defined recursively by: for $n = 0$ it is the
one-entry list $(a)$; for fuel $n + 1$ it is $(a)$ if $b = 0$, and otherwise it is $a$
followed by the list for the pair $b$, $-(a \bmod b)$ with fuel $n$, where $a \bmod b$ is the
remainder of $a$ on division by $b$.

Formalized by `MathlibExt.Algebra.SturmWanted.Algebra.sturmAux`, a definition declared in [WantedExt/Algebra/SturmWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/SturmWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/sturm-s-theorem/index.html#sturm-aux).

## Sturm chain

The Sturm chain of a real polynomial $p$ is the list $p_0, p_1, \dots, p_m$
with $p_0 = p$, $p_1 = p'$ and $p_{k+1} = -(p_{k-1} \bmod p_k)$, the negated remainder of
$p_{k-1}$ on division by $p_k$, where the list stops at $p_m$ as soon as the next entry would
be $0$; thus $p_m$ is its last entry and, for $p \ne 0$, every entry is nonzero. For $p = 0$
the chain is the one-entry list $(0)$.

Formalized by `MathlibExt.Algebra.SturmWanted.Algebra.sturmChain`, a definition declared in [WantedExt/Algebra/SturmWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/SturmWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/sturm-s-theorem/index.html#sturm-chain).

## Number of sign changes in a list of reals

For a list $x_1, \dots, x_n$ of real numbers,
let $y_1, \dots, y_m$ be the entries of the list that are nonzero, in their original order. The
number of sign changes of the list is the number of indices $i$ with $1 \le i < m$ and
$y_i y_{i+1} < 0$, that is, the number of adjacent pairs of opposite sign once the zeros are
removed.

Formalized by `MathlibExt.Algebra.SturmWanted.Algebra.signChanges`, a definition declared in [WantedExt/Algebra/SturmWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/SturmWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/sturm-s-theorem/index.html#sign-changes).

## Sturm sign-variation function

For a real polynomial $p$ with Sturm chain
$p_0, p_1, \dots, p_m$ and a real number $x$, $\sigma_p(x)$ is the number of sign changes,
ignoring zeros, in the sequence of values $p_0(x), p_1(x), \dots, p_m(x)$.

Formalized by `MathlibExt.Algebra.SturmWanted.Algebra.sigma`, a definition declared in [WantedExt/Algebra/SturmWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/SturmWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/sturm-s-theorem/index.html#sigma).

## Sturm's theorem

Let $p$ be a squarefree real polynomial and let $a < b$ be real numbers
with $p(a) \ne 0$ and $p(b) \ne 0$. Then the number of distinct real roots $x$ of $p$ with
$a < x < b$ equals $\sigma_p(a) - \sigma_p(b)$, where $\sigma_p$ is the Sturm sign-variation
function of $p$ and the subtraction is truncated subtraction of natural numbers.

## Sources

- J. C. F. Sturm (1829). Listed as §97 in O. Knill, Some Fundamental Theorems in Mathematics (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Formalized in Isabelle/HOL by Manuel Eberl (AFP entry Sturm_Sequences). Problem `sturm` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Algebra.SturmWanted.Algebra.sturm` is written with `theorem_wanted` in [WantedExt/Algebra/SturmWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/SturmWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/sturm-s-theorem/index.html#sturm).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sturm's theorem](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/sturm-s-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Algebra/zeros-of-polynomials/sturm-s-theorem)
