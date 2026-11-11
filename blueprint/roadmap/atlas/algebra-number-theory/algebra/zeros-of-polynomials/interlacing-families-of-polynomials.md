---
declaration: section
origin: cited
lean: Polynomial.HasUpperInterlacingPoint, Polynomial.HasCommonUpperInterlacing, Polynomial.eval_re_nonpos_of_upperInterlacing, Polynomial.exists_maxRealRoot_le_weightedSum_of_commonUpperInterlacing, Polynomial.exists_maxRealRoot_le_weightedSum_of_segment_realRooted
statement: formalized
proof: formalized
---

# Interlacing families of polynomials

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/interlacing-families-of-polynomials/index.html).

## Upper interlacing point

Let $p$ be a complex polynomial and let
$\operatorname{maxroot}(p)$ be the largest real part of an element of the multiset of roots of
$p$, with $\operatorname{maxroot}(p) = 0$ when that multiset is empty (as it is for nonzero
constants and for $p = 0$). A real number $a$ is an upper interlacing point of $p$ if
$a \le \operatorname{maxroot}(p)$ and, after removing one copy of $\operatorname{maxroot}(p)$
from the multiset of roots of $p$ (if it occurs there), every remaining root has real part at
most $a$.

Formalized by `Polynomial.HasUpperInterlacingPoint`, a definition declared in [MathlibExt/Algebra/Polynomial/Interlacing.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Polynomial/Interlacing.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/interlacing-families-of-polynomials/index.html#has-upper-interlacing-point).

## Common upper interlacing point

A family $(P_i)_{i \in I}$ of complex polynomials,
indexed by an arbitrary type $I$, has a common upper interlacing point if some real number $a$
is an upper interlacing point of $P_i$ for every $i \in I$.

Formalized by `Polynomial.HasCommonUpperInterlacing`, a definition declared in [MathlibExt/Algebra/Polynomial/Interlacing.lean, line 312](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Polynomial/Interlacing.lean#L312). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/interlacing-families-of-polynomials/index.html#has-common-upper-interlacing).

## Nonpositivity between an upper interlacing point and the largest root

Let $p$ be a
monic complex polynomial of positive degree all of whose roots are real, let
$\operatorname{maxroot}(p)$ be its largest root, and let $a$ be an upper interlacing point
of $p$. Then for every real $x$ with $a \le x \le \operatorname{maxroot}(p)$, the real part
of $p(x)$ is at most $0$.

Formalized by `Polynomial.eval_re_nonpos_of_upperInterlacing`, a theorem declared in [MathlibExt/Algebra/Polynomial/Interlacing.lean, line 317](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Polynomial/Interlacing.lean#L317). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/interlacing-families-of-polynomials/index.html#eval-re-nonpos-of-upper-interlacing).

## Common upper interlacing bounds some member's largest root by a weighted sum's

Let $I$
be a nonempty finite set and, for each $i \in I$, let $P_i$ be a monic complex polynomial of
positive degree all of whose roots are real, such that the family $(P_i)_{i \in I}$ has a
common upper interlacing point. Let $w_i \ge 0$ be real weights such that
$Q = \sum_{i \in I} w_i P_i$ is monic and all of its roots are real. Then there is $i \in I$
with $\operatorname{maxroot}(P_i) \le \operatorname{maxroot}(Q)$, where
$\operatorname{maxroot}(f)$ denotes the largest root of a real-rooted polynomial $f$.

Formalized by `Polynomial.exists_maxRealRoot_le_weightedSum_of_commonUpperInterlacing`, a theorem declared in [MathlibExt/Algebra/Polynomial/Interlacing.lean, line 352](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Polynomial/Interlacing.lean#L352). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/interlacing-families-of-polynomials/index.html#exists-max-real-root-le-weighted-sum-of).

## Some member's largest root is at most that of a weighted sum, via real-rooted segments

Let $I$ be a nonempty finite set, let $n \ge 1$, and for each $i \in I$ let $P_i$ be a monic
complex polynomial of degree $n$ and $w_i \ge 0$ a real weight. Suppose that
$Q = \sum_{i \in I} w_i P_i$ is monic of degree $n$ and that, for every $i \in I$ and every
$t \in [0, 1]$, all roots of $(1 - t) Q + t P_i$ are real. Then there is $i \in I$ with
$\operatorname{maxroot}(P_i) \le \operatorname{maxroot}(Q)$, where $\operatorname{maxroot}(f)$
denotes the largest real part of a root of $f$.

Formalized by `Polynomial.exists_maxRealRoot_le_weightedSum_of_segment_realRooted`, a theorem declared in [MathlibExt/Algebra/Polynomial/Interlacing.lean, line 418](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Polynomial/Interlacing.lean#L418). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/interlacing-families-of-polynomials/index.html#exists-max-real-root-le-weighted-sum-of-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Interlacing families of polynomials](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/interlacing-families-of-polynomials/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Algebra/zeros-of-polynomials/interlacing-families-of-polynomials)
