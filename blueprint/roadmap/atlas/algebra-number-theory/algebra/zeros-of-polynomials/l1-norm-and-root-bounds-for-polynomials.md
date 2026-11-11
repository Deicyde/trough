---
declaration: section
origin: cited
lean: Polynomial.l1Norm, Polynomial.l1Norm_def, Polynomial.l1Norm_zero, Polynomial.l1Norm_nonneg, Polynomial.l1Norm_eq_sum_range, Polynomial.l1Norm_eq_sum_range_add_one_of_monic, Polynomial.one_le_l1Norm_of_monic, Polynomial.natDegree_eq_of_monic_of_l1Norm_sub_lt_one
statement: formalized
proof: formalized
---

# L1 norm and root bounds for polynomials

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/l1-norm-and-root-bounds-for-polynomials/index.html).

## L1 norm of a polynomial

Let $K$ be a semiring and $v$ a real-valued absolute value on
$K$. The L1 norm of a polynomial $p = \sum_i a_i X^i \in K[X]$ with respect to $v$ is the real
number $\|p\|_v = \sum_i v(a_i)$, where the sum runs over the indices $i$ with $a_i \neq 0$.

Formalized by `Polynomial.l1Norm`, a definition declared in [MathlibExt/Algebra/Polynomial/L1Norm.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Polynomial/L1Norm.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/l1-norm-and-root-bounds-for-polynomials/index.html#l1-norm).

## L1 norm as a sum over the support

Let $K$ be a semiring and $v$ a real-valued absolute
value on $K$. For every polynomial $p = \sum_i a_i X^i \in K[X]$, the L1 norm $\|p\|_v$ of $p$
with respect to $v$ equals $\sum_{i \in S} v(a_i)$, where $S = \{ i : a_i \neq 0 \}$ is the
support of $p$.

Formalized by `Polynomial.l1Norm_def`, a theorem declared in [MathlibExt/Algebra/Polynomial/L1Norm.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Polynomial/L1Norm.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/l1-norm-and-root-bounds-for-polynomials/index.html#l1-norm-def).

## L1 norm of the zero polynomial

Let $K$ be a semiring and $v$ a real-valued absolute value
on $K$. The L1 norm of the zero polynomial in $K[X]$ with respect to $v$ is $0$.

Formalized by `Polynomial.l1Norm_zero`, a theorem declared in [MathlibExt/Algebra/Polynomial/L1Norm.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Polynomial/L1Norm.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/l1-norm-and-root-bounds-for-polynomials/index.html#l1-norm-zero).

## Nonnegativity of the L1 norm

Let $K$ be a semiring and $v$ a real-valued absolute value
on $K$. For every polynomial $p \in K[X]$, the L1 norm of $p$ with respect to $v$ satisfies
$\|p\|_v \ge 0$.

Formalized by `Polynomial.l1Norm_nonneg`, a theorem declared in [MathlibExt/Algebra/Polynomial/L1Norm.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Polynomial/L1Norm.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/l1-norm-and-root-bounds-for-polynomials/index.html#l1-norm-nonneg).

## L1 norm as a sum up to the degree

Let $K$ be a semiring and $v$ a real-valued absolute
value on $K$. Let $p = \sum_i a_i X^i \in K[X]$ and let $n$ be the degree of $p$, with $n = 0$
when $p = 0$. Then the L1 norm of $p$ with respect to $v$ is $\|p\|_v = \sum_{i=0}^{n} v(a_i)$.

Formalized by `Polynomial.l1Norm_eq_sum_range`, a theorem declared in [MathlibExt/Algebra/Polynomial/L1Norm.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Polynomial/L1Norm.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/l1-norm-and-root-bounds-for-polynomials/index.html#l1-norm-eq-sum-range).

## L1 norm of a monic polynomial

Let $K$ be a nontrivial semiring (one with $0 \neq 1$)
and $v$ a real-valued absolute value on $K$. If $f = \sum_i a_i X^i \in K[X]$ is monic of degree
$n$, then the L1 norm of $f$ with respect to $v$ is $\|f\|_v = \sum_{i=0}^{n-1} v(a_i) + 1$.

Formalized by `Polynomial.l1Norm_eq_sum_range_add_one_of_monic`, a theorem declared in [MathlibExt/Algebra/Polynomial/L1Norm.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Polynomial/L1Norm.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/l1-norm-and-root-bounds-for-polynomials/index.html#l1-norm-eq-sum-range-add-one-of-monic).

## Monic polynomials have L1 norm at least one

Let $K$ be a nontrivial semiring (one with
$0 \neq 1$) and $v$ a real-valued absolute value on $K$. If $f \in K[X]$ is monic, then the L1
norm of $f$ with respect to $v$ satisfies $\|f\|_v \ge 1$.

Formalized by `Polynomial.one_le_l1Norm_of_monic`, a theorem declared in [MathlibExt/Algebra/Polynomial/L1Norm.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Polynomial/L1Norm.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/l1-norm-and-root-bounds-for-polynomials/index.html#one-le-l1-norm-of-monic).

## Monic polynomials close in L1 norm have the same degree

Let $K$ be a nontrivial ring
and $v$ a real-valued absolute value on $K$. If $f, g \in K[x]$ are monic and the L1 norm of
$f - g$ with respect to $v$ is strictly less than $1$, then $f$ and $g$ have the same degree.

Formalized by `Polynomial.natDegree_eq_of_monic_of_l1Norm_sub_lt_one`, a theorem declared in [MathlibExt/Algebra/Polynomial/DegreeStability.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Polynomial/DegreeStability.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/l1-norm-and-root-bounds-for-polynomials/index.html#nat-degree-eq-of-monic-of-l1-norm-sub-lt).

## Root bound by the L1 norm

Let $K$ and $L$ be fields with $L$ a $K$-algebra, let $v$ be a
real-valued absolute value on $K$, and let $w$ be a real-valued absolute value on $L$ lying over
$v$, that is, $w(x) = v(x)$ for every $x \in K$ viewed in $L$ through the algebra map. If $f$ is a
monic polynomial over $K$ and $\alpha \in L$ is a root of $f$, then $w(\alpha)$ is strictly less
than the L1 norm of $f$ with respect to $v$.

No algebraicity, finiteness, completeness, or archimedean hypothesis is needed.

Formalized by `Polynomial.aeval_lt_l1Norm_of_monic_of_aeval_eq_zero`, a theorem declared in [MathlibExt/Algebra/Polynomial/RootBound.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Polynomial/RootBound.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/l1-norm-and-root-bounds-for-polynomials/index.html#aeval-lt-l1-norm-of-monic-of-aeval-eq-ze).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: L1 norm and root bounds for polynomials](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/l1-norm-and-root-bounds-for-polynomials/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Algebra/zeros-of-polynomials/l1-norm-and-root-bounds-for-polynomials)
