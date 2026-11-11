---
declaration: section
origin: cited
lean: Polynomial.IsRealRooted, Polynomial.isRealRooted_of_map_star_eq_self_of_roots_im_nonpos, Polynomial.maxRealRoot, Polynomial.root_re_le_maxRealRoot, Polynomial.exists_root_re_eq_maxRealRoot, Polynomial.roots_ne_zero_of_natDegree_pos, Polynomial.coe_maxRealRoot_mem_roots, Polynomial.eval_re_pos_of_maxRealRoot_lt
statement: formalized
proof: formalized
---

# Real-rooted polynomials

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/real-rooted-polynomials/index.html).

## Real-rooted polynomials

A complex polynomial $p$ is real-rooted if every element $z$
of its multiset of roots is real, that is, $\operatorname{Im} z = 0$.

Formalized by `Polynomial.IsRealRooted`, a definition declared in [MathlibExt/Algebra/Polynomial/RealRooted.lean, line 21](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Polynomial/RealRooted.lean#L21). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/real-rooted-polynomials/index.html#is-real-rooted).

## Conjugation-invariant polynomials with roots in the closed lower half-plane are real-rooted

Let $p$ be a nonzero complex polynomial that is unchanged when complex conjugation is applied to
each of its coefficients. If every root $z$ of $p$ satisfies $\operatorname{Im} z \le 0$, then
$p$ is real-rooted.

Formalized by `Polynomial.isRealRooted_of_map_star_eq_self_of_roots_im_nonpos`, a theorem declared in [MathlibExt/Algebra/Polynomial/RealRooted.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Polynomial/RealRooted.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/real-rooted-polynomials/index.html#is-real-rooted-of-map-star-eq-self-of-ro).

## Largest real part of a root

For a complex polynomial $p$, let $\rho(p)$ be the largest
real part $\operatorname{Re} z$ of an element $z$ of the multiset of roots of $p$, with
$\rho(p) = 0$ when that multiset is empty (as it is for nonzero constants and for $p = 0$).

Formalized by `Polynomial.maxRealRoot`, a definition declared in [MathlibExt/Algebra/Polynomial/RealRooted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Polynomial/RealRooted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/real-rooted-polynomials/index.html#max-real-root).

## Real parts of roots are bounded by the largest one

Let $p$ be a complex polynomial and
let $\rho(p)$ be the largest real part of an element of its multiset of roots, or $0$ if that
multiset is empty. Then every element $z$ of the multiset of roots of $p$ satisfies
$\operatorname{Re} z \le \rho(p)$.

Formalized by `Polynomial.root_re_le_maxRealRoot`, a theorem declared in [MathlibExt/Algebra/Polynomial/RealRooted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Polynomial/RealRooted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/real-rooted-polynomials/index.html#root-re-le-max-real-root).

## The largest real part of a root is attained

Let $p$ be a complex polynomial whose
multiset of roots is nonempty, and let $\rho(p)$ be the largest real part of a root of $p$.
Then some root $z$ of $p$ satisfies $\operatorname{Re} z = \rho(p)$.

Formalized by `Polynomial.exists_root_re_eq_maxRealRoot`, a theorem declared in [MathlibExt/Algebra/Polynomial/RealRooted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Polynomial/RealRooted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/real-rooted-polynomials/index.html#exists-root-re-eq-max-real-root).

## Nonconstant complex polynomials have a root

Every complex polynomial of positive
degree has at least one root.

Formalized by `Polynomial.roots_ne_zero_of_natDegree_pos`, a theorem declared in [MathlibExt/Algebra/Polynomial/RealRooted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Polynomial/RealRooted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/real-rooted-polynomials/index.html#roots-ne-zero-of-nat-degree-pos).

## For a real-rooted polynomial, the largest real part of a root is a root

Let $p$ be a
real-rooted complex polynomial of positive degree, and let $\rho(p)$ be the largest real part of
a root of $p$. Then the real number $\rho(p)$, viewed as a complex number, is a root of $p$.

Formalized by `Polynomial.coe_maxRealRoot_mem_roots`, a theorem declared in [MathlibExt/Algebra/Polynomial/RealRooted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Polynomial/RealRooted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/real-rooted-polynomials/index.html#coe-max-real-root-mem-roots).

## Monic real-rooted polynomials have positive real part right of the largest root

Let $p$ be a monic real-rooted complex polynomial, and let $\rho(p)$ be the largest real part of
a root of $p$, or $0$ if $p$ has no roots. Then $\operatorname{Re} p(x) > 0$ for every real
number $x > \rho(p)$.

Formalized by `Polynomial.eval_re_pos_of_maxRealRoot_lt`, a theorem declared in [MathlibExt/Algebra/Polynomial/RealRooted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Polynomial/RealRooted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/real-rooted-polynomials/index.html#eval-re-pos-of-max-real-root-lt).

## Monic real-rooted polynomials have nonnegative real part from the largest root on

Let $p$ be a monic real-rooted complex polynomial, and let $\rho(p)$ be the largest real part of
a root of $p$, or $0$ if $p$ has no roots. Then $\operatorname{Re} p(x) \ge 0$ for every real
number $x \ge \rho(p)$.

Formalized by `Polynomial.eval_re_nonneg_of_maxRealRoot_le`, a theorem declared in [MathlibExt/Algebra/Polynomial/RealRooted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Polynomial/RealRooted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/real-rooted-polynomials/index.html#eval-re-nonneg-of-max-real-root-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Real-rooted polynomials](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/real-rooted-polynomials/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Algebra/zeros-of-polynomials/real-rooted-polynomials)
