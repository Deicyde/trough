---
declaration: section
origin: cited
lean: MetaMathlibExt.GeneralizedFermatSolvable, MetaMathlibExt.generalizedFermatSolvable_three_six_two, MetaMathlibExt.GeneralizedFermatSolvable.swap, MetaMathlibExt.not_generalizedFermatSolvable_of_two_gcd_gt_one, MetaMathlibExt.pow_add_pow_ne_pow_of_prime_five_le, MetaMathlibExt.generalizedFermat_three_six_two_mul, MetaMathlibExt.generalizedFermat_mul_exponent
statement: formalized
---

# Generalized Fermat equation

7 results, 3 proved and 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/generalized-fermat-equation/index.html).

## Solvable generalized Fermat equation

For natural numbers $m$, $n$, $r$, the equation
$x^m + y^n = z^r$ is called solvable when there are nonzero integers $x$, $y$, $z$ with
$x^m + y^n = z^r$.

## Sources

- Richard F. Ryan, *Under What Conditions on the Exponents Does `x^m + y^n = z^r` Have Solutions?*, INTEGERS 24 (2024), Article A48, Section 1, equation (1).

Formalized by `MetaMathlibExt.GeneralizedFermatSolvable`, a definition declared in [WantedExt/NumberTheory/GeneralizedFermatExponentsWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFermatExponentsWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/generalized-fermat-equation/index.html#generalized-fermat-solvable).

## A solution of x³ + y⁶ = z²

The equation $x^3 + y^6 = z^2$ has a solution in nonzero
integers, namely $2^3 + 1^6 = 3^2$.

## Sources

- Richard F. Ryan, *Under What Conditions on the Exponents Does `x^m + y^n = z^r` Have Solutions?*, INTEGERS 24 (2024), Article A48, Lemma 1 (the case `s = t = w = 1`).

Formalized by `MetaMathlibExt.generalizedFermatSolvable_three_six_two`, a theorem declared in [WantedExt/NumberTheory/GeneralizedFermatExponentsWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFermatExponentsWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/generalized-fermat-equation/index.html#generalized-fermat-solvable-three-six-tw).

## Swapping the first two exponents of a generalized Fermat equation

For natural numbers
$m$, $n$, $r$, if $x^m + y^n = z^r$ has a solution in nonzero integers, then so does
$x^n + y^m = z^r$.

## Sources

- Richard F. Ryan, *Under What Conditions on the Exponents Does `x^m + y^n = z^r` Have Solutions?*, INTEGERS 24 (2024), Article A48, Section 1, equation (1).

Formalized by `MetaMathlibExt.GeneralizedFermatSolvable.swap`, a theorem declared in [WantedExt/NumberTheory/GeneralizedFermatExponentsWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFermatExponentsWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/generalized-fermat-equation/index.html#swap).

## Generalized Fermat equations with two non-coprime pairs of exponents

Let
$m, n, r \ge 2$ be integers with $\gcd(m, n, r) = 1$ such that at least two of $\gcd(m, n)$,
$\gcd(m, r)$ and $\gcd(n, r)$ are greater than $1$. Suppose there are no natural numbers
$s, t, w$ that are pairwise coprime, with $s$ odd and $3 \nmid w$, such that $(m, n, r)$ is one
of $(3s, 6t, 2w)$, $(6t, 3s, 2w)$, $(2w, 3s, 6t)$ and $(3s, 2w, 6t)$. Then the equation
$x^m + y^n = z^r$ has no solution in nonzero integers $x, y, z$.

Positivity of $s, t, w$ is automatic from $m, n, r \ge 2$.

## Sources

- Richard F. Ryan, *Under What Conditions on the Exponents Does `x^m + y^n = z^r` Have Solutions?*, INTEGERS 24 (2024), Article A48, Theorem 1.

Stated but not proved: `MetaMathlibExt.not_generalizedFermatSolvable_of_two_gcd_gt_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedFermatExponentsWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFermatExponentsWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/generalized-fermat-equation/index.html#not-generalized-fermat-solvable-of-two-g).

## The Bartolomé–Mihăilescu theorem for prime exponents

Let $p \le q$ be primes with
$p \ge 5$, and let $x, y, z$ be pairwise coprime nonzero integers. Then $x^p + y^p \ne z^q$.

The source quotes this result from Bartolomé and Mihăilescu, arXiv:2108.08572.

## Sources

- Richard F. Ryan, *Under What Conditions on the Exponents Does `x^m + y^n = z^r` Have Solutions?*, INTEGERS 24 (2024), Article A48, Corollary 1.

Stated but not proved: `MetaMathlibExt.pow_add_pow_ne_pow_of_prime_five_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedFermatExponentsWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFermatExponentsWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/generalized-fermat-equation/index.html#pow-add-pow-ne-pow-of-prime-five-le).

## Generalized Fermat equations with exponents 3s, 6t and 2w

Let $s, t, w$ be positive
integers. If $s, t, w$ are pairwise coprime, $s$ is odd and $3 \nmid w$, then the equation
$x^{3s} + y^{6t} = z^{2w}$ has infinitely many solutions $(x, y, z)$ in nonzero integers;
otherwise it has no solution in nonzero integers.

## Sources

- Richard F. Ryan, *Under What Conditions on the Exponents Does `x^m + y^n = z^r` Have Solutions?*, INTEGERS 24 (2024), Article A48, Lemma 1.

Stated but not proved: `MetaMathlibExt.generalizedFermat_three_six_two_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedFermatExponentsWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFermatExponentsWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/generalized-fermat-equation/index.html#generalized-fermat-three-six-two-mul).

## Generalized Fermat equations with exponents u, uv and v

Let $u, v \ge 2$ be integers.
(A) The equation $x^u + y^{uv} = z^v$ has a solution in nonzero integers $x, y, z$ if and only
if it has one with $\gcd(x, y, z) = 1$. (B) If $u$ or $v$ is even, $(u, v) \ne (2, 2)$ and
$(u, v) \ne (3, 2)$, the equation has no solution in nonzero integers. (C) If $3 \mid u$ or
$3 \mid v$, and $(u, v) \ne (3, 2)$, the equation has no solution in nonzero integers.

## Sources

- Richard F. Ryan, *Under What Conditions on the Exponents Does `x^m + y^n = z^r` Have Solutions?*, INTEGERS 24 (2024), Article A48, Lemma 2.

Stated but not proved: `MetaMathlibExt.generalizedFermat_mul_exponent` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedFermatExponentsWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFermatExponentsWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/generalized-fermat-equation/index.html#generalized-fermat-mul-exponent).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Generalized Fermat equation](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/generalized-fermat-equation/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/generalized-fermat-equation)
