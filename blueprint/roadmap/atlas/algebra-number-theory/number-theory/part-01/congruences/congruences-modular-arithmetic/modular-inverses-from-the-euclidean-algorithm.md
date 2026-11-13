---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.ModInverseSwitchingWanted.IsLeastAbsInverse, MathlibExt.NumberTheory.ModInverseSwitchingWanted.IsEuclidSwitchSeq, MathlibExt.NumberTheory.ModInverseSwitchingWanted.bezout_coeffs_are_inverses, MathlibExt.NumberTheory.ModInverseSwitchingWanted.exists_eq_mul_add_iff_switching, MathlibExt.NumberTheory.ModInverseSwitchingWanted.isLeastAbsInverse_succ_imp, MathlibExt.NumberTheory.ModInverseSwitchingWanted.isLeastAbsInverse_all, MathlibExt.NumberTheory.ModInverseSwitchingWanted.euclid_bezout_coeffs_leastAbsInverse, MathlibExt.NumberTheory.ModInverseSwitchingWanted.euclid_bezout_coeffs_abs_le
statement: formalized
---

# Modular inverses from the Euclidean algorithm

12 results, 2 proved and 10 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/modular-inverses-from-the-euclidean-algorithm/index.html).

## Least absolute inverse

For integers $x$ and $a$ and a natural number $n$, $x$ is the
least absolute inverse of $a$ modulo $n$ when $xa \equiv 1 \pmod{n}$ and $-n < 2x \le n$, that is,
when $x$ is an inverse of $a$ modulo $n$ in the half-open interval $-n/2 < x \le n/2$.

For even $n$ the endpoint $n/2$ is included and $-n/2$ is excluded; this is also the choice the
Euclidean recurrence produces.

Formalized by `MathlibExt.NumberTheory.ModInverseSwitchingWanted.IsLeastAbsInverse`, a definition declared in [WantedExt/NumberTheory/ModInverseSwitchingWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ModInverseSwitchingWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/modular-inverses-from-the-euclidean-algorithm/index.html#is-least-abs-inverse).

## Euclidean switching data

A natural number $N$, a sequence $r_0, r_1, \dots$ of natural
numbers and a sequence $s_0, s_1, \dots$ of integers form Euclidean switching data when
$N \ge 1$; $r_0 > r_1 > \cdots > r_{N+1} = 1$, with $r_0, \dots, r_{N+1}$ all positive; for each
$i = 1, \dots, N$ there is a positive integer $q_i$ with $r_{i-1} = q_i r_i + r_{i+1}$;
$s_{N+1} = 1$; and $s_{i+1} r_{i-1} + s_i r_i = 1$ for each $i = 1, \dots, N$.

These are the remainders $r_i$ of the Euclidean algorithm on $(r_0, r_1)$ and the inverses $s_i$
of $r_i$ modulo $r_{i-1}$ in §3 of Konstantogiannis, "The Euclidean Algorithm as a Sequence of
Modular Inverse Switching Formulas" (Equations (4), (5) and (6)).

Formalized by `MathlibExt.NumberTheory.ModInverseSwitchingWanted.IsEuclidSwitchSeq`, a definition declared in [WantedExt/NumberTheory/ModInverseSwitchingWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ModInverseSwitchingWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/modular-inverses-from-the-euclidean-algorithm/index.html#is-euclid-switch-seq).

## Bézout coefficients are modular inverses

Let $m$ and $n$ be coprime positive integers,
and let $x$ and $y$ be integers with $xm + yn = 1$. Then $xm \equiv 1 \pmod{n}$ and
$yn \equiv 1 \pmod{m}$; that is, $x$ is an inverse of $m$ modulo $n$ and $y$ is an inverse of
$n$ modulo $m$.

## Sources

- Spiros Konstantogiannis, "The Euclidean Algorithm as a Sequence of Modular Inverse Switching Formulas", Lemma 1.

Stated but not proved: `MathlibExt.NumberTheory.ModInverseSwitchingWanted.bezout_coeffs_are_inverses` is written with `theorem_wanted` in [WantedExt/NumberTheory/ModInverseSwitchingWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ModInverseSwitchingWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/modular-inverses-from-the-euclidean-algorithm/index.html#bezout-coeffs-are-inverses).

## Modular inverse switching

Let $m$ and $n$ be positive integers with $\gcd(m, n) = 1$,
and let $t$ be an integer with $\gcd(|t|, n) = 1$. Then $m = kn + t$ for some integer $k$ if
and only if there are integers $x$ and $y$ with $xt \equiv 1 \pmod{n}$, $yn \equiv 1 \pmod{m}$
and $xm + yn = 1$.

## Sources

- Spiros Konstantogiannis, "The Euclidean Algorithm as a Sequence of Modular Inverse Switching Formulas", Lemma 2.

Stated but not proved: `MathlibExt.NumberTheory.ModInverseSwitchingWanted.exists_eq_mul_add_iff_switching` is written with `theorem_wanted` in [WantedExt/NumberTheory/ModInverseSwitchingWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ModInverseSwitchingWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/modular-inverses-from-the-euclidean-algorithm/index.html#exists-eq-mul-add-iff-switching).

## Least absolute inverses propagate down the Euclidean sequence

Let $r_0, r_1, \ldots$ be
natural numbers, $s_0, s_1, \ldots$ integers and $N \ge 1$ such that $(r, s, N)$ is Euclidean
switching data: $r_0 > r_1 > \cdots > r_{N+1} = 1$ are the successive remainders of the Euclidean
algorithm, $s_{N+1} = 1$, and $s_{i+1} r_{i-1} + s_i r_i = 1$ for $1 \le i \le N$. If
$1 \le j \le N$ and $s_{j+1}$ is the least absolute inverse of $r_{j+1}$ modulo $r_j$, then $s_j$
is the least absolute inverse of $r_j$ modulo $r_{j-1}$.

## Sources

- Spiros Konstantogiannis, "The Euclidean Algorithm as a Sequence of Modular Inverse Switching Formulas", Lemma 3.

Stated but not proved: `MathlibExt.NumberTheory.ModInverseSwitchingWanted.isLeastAbsInverse_succ_imp` is written with `theorem_wanted` in [WantedExt/NumberTheory/ModInverseSwitchingWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ModInverseSwitchingWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/modular-inverses-from-the-euclidean-algorithm/index.html#is-least-abs-inverse-succ-imp).

## Every switching inverse is a least absolute inverse

Let $(r_i)$, $(s_i)$ and $N$ be
Euclidean switching data. Then for every $i$ with $1 \le i \le N + 1$, $s_i$ is the least
absolute inverse of $r_i$ modulo $r_{i-1}$.

## Sources

- Spiros Konstantogiannis, "The Euclidean Algorithm as a Sequence of Modular Inverse Switching Formulas", Corollary 1.

Stated but not proved: `MathlibExt.NumberTheory.ModInverseSwitchingWanted.isLeastAbsInverse_all` is written with `theorem_wanted` in [WantedExt/NumberTheory/ModInverseSwitchingWanted.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ModInverseSwitchingWanted.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/modular-inverses-from-the-euclidean-algorithm/index.html#is-least-abs-inverse-all).

## The Euclidean Bézout coefficients are least absolute inverses

Let $m > n > 1$ be
integers, write $g = \gcd(m, n)$, and let $(r_i)$, $(s_i)$ and $N$ be Euclidean switching data
with $r_0 = m/g$ and $r_1 = n/g$. Then $s_2 m + s_1 n = g$, $s_2$ is the least absolute inverse
of $m/g$ modulo $n/g$, and $s_1$ is the least absolute inverse of $n/g$ modulo $m/g$.

## Sources

- Spiros Konstantogiannis, "The Euclidean Algorithm as a Sequence of Modular Inverse Switching Formulas", Lemma 4.

Stated but not proved: `MathlibExt.NumberTheory.ModInverseSwitchingWanted.euclid_bezout_coeffs_leastAbsInverse` is written with `theorem_wanted` in [WantedExt/NumberTheory/ModInverseSwitchingWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ModInverseSwitchingWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/modular-inverses-from-the-euclidean-algorithm/index.html#euclid-bezout-coeffs-least-abs-inverse).

## The Euclidean Bézout coefficients are smallest in absolute value

Let $m > n > 1$ be
integers, write $g = \gcd(m, n)$, and let $(r_i)$, $(s_i)$ and $N$ be Euclidean switching data
with $r_0 = m/g$ and $r_1 = n/g$. Then for all integers $x$ and $y$ with $xm + yn = g$, we have
$|s_2| \le |x|$ and $|s_1| \le |y|$.

## Sources

- Spiros Konstantogiannis, "The Euclidean Algorithm as a Sequence of Modular Inverse Switching Formulas", Lemma 5.

Stated but not proved: `MathlibExt.NumberTheory.ModInverseSwitchingWanted.euclid_bezout_coeffs_abs_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/ModInverseSwitchingWanted.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ModInverseSwitchingWanted.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/modular-inverses-from-the-euclidean-algorithm/index.html#euclid-bezout-coeffs-abs-le).

## Rankin's minimality of the Euclidean Bézout pair

Let $m > n > 1$ be integers, write
$g = \gcd(m, n)$, and let $(r_i)$, $(s_i)$ and $N$ be Euclidean switching data with
$r_0 = m/g$ and $r_1 = n/g$. Then for all integers $x$ and $y$ with $xm + yn = g$, we have
$s_2^2 + s_1^2 \le x^2 + y^2$.

## Sources

- Spiros Konstantogiannis, "The Euclidean Algorithm as a Sequence of Modular Inverse Switching Formulas", Corollary 2.

Stated but not proved: `MathlibExt.NumberTheory.ModInverseSwitchingWanted.euclid_bezout_coeffs_sq_add_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/ModInverseSwitchingWanted.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ModInverseSwitchingWanted.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/modular-inverses-from-the-euclidean-algorithm/index.html#euclid-bezout-coeffs-sq-add-le).

## Both first inverses extremal, odd–odd case

Let $(r_i)$, $(s_i)$ and $N$ be Euclidean
switching data with $r_0$ and $r_1$ both odd. Then $2|s_1| = r_0 - 1$ and $2|s_2| = r_1 - 1$
hold simultaneously if and only if $r_0 = r_1 + 2$.

## Sources

- Spiros Konstantogiannis, "The Euclidean Algorithm as a Sequence of Modular Inverse Switching Formulas", Lemma 6.

Stated but not proved: `MathlibExt.NumberTheory.ModInverseSwitchingWanted.abs_eq_halves_iff_sub_eq_two_of_odd` is written with `theorem_wanted` in [WantedExt/NumberTheory/ModInverseSwitchingWanted.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ModInverseSwitchingWanted.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/modular-inverses-from-the-euclidean-algorithm/index.html#abs-eq-halves-iff-sub-eq-two-of-odd).

## Both first inverses extremal, odd–even case

Let $(r_i)$, $(s_i)$ and $N$ be Euclidean
switching data with $r_0$ odd and $r_1$ even. Then $2|s_1| = r_0 - 1$ and $2|s_2| = r_1$ hold
simultaneously if and only if $r_1 = 2$.

## Sources

- Spiros Konstantogiannis, "The Euclidean Algorithm as a Sequence of Modular Inverse Switching Formulas", Lemma 7.

Stated but not proved: `MathlibExt.NumberTheory.ModInverseSwitchingWanted.abs_eq_halves_iff_eq_two_of_odd_even` is written with `theorem_wanted` in [WantedExt/NumberTheory/ModInverseSwitchingWanted.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ModInverseSwitchingWanted.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/modular-inverses-from-the-euclidean-algorithm/index.html#abs-eq-halves-iff-eq-two-of-odd-even).

## First inverses not both extremal, even–odd case

Let $(r_i)$, $(s_i)$ and $N$ be
Euclidean switching data with $r_0$ even and $r_1$ odd. Then $2|s_1| < r_0$ or
$2|s_2| < r_1 - 1$; that is, $|s_1| < r_0/2$ or $|s_2| < (r_1 - 1)/2$.

## Sources

- Spiros Konstantogiannis, "The Euclidean Algorithm as a Sequence of Modular Inverse Switching Formulas", Lemma 8.

Stated but not proved: `MathlibExt.NumberTheory.ModInverseSwitchingWanted.abs_lt_of_even_odd` is written with `theorem_wanted` in [WantedExt/NumberTheory/ModInverseSwitchingWanted.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ModInverseSwitchingWanted.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/modular-inverses-from-the-euclidean-algorithm/index.html#abs-lt-of-even-odd).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Modular inverses from the Euclidean algorithm](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/modular-inverses-from-the-euclidean-algorithm/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/modular-inverses-from-the-euclidean-algorithm)
