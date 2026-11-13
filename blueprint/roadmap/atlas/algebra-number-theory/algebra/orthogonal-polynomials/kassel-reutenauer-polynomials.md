---
declaration: section
origin: cited
lean: MetaMathlibExt.kasselReutenauerCoeff, MetaMathlibExt.kasselReutenauerPoly, MetaMathlibExt.chebyshevCPartialSum, MetaMathlibExt.kasselReutenauerCoeff_small, MetaMathlibExt.kasselReutenauerPoly_one, MetaMathlibExt.kasselReutenauerPoly_two, MetaMathlibExt.kasselReutenauerPoly_three, MetaMathlibExt.chebyshevCPartialSum_zero
statement: formalized
---

# Kassel–Reutenauer polynomials

32 results, 10 proved and 22 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/kassel-reutenauer-polynomials/index.html).

## The Kassel–Reutenauer coefficients $a_{n,i}$

For natural numbers $n$ and $i$, $a_{n,i}$ is
the number of positive divisors $d$ of $n$ with

$$\frac{i + \sqrt{2n + i^2}}{2} < d \le i + \sqrt{2n + i^2},$$

equivalently with $d(d - 2i) \le 2n$ and $n < 2d(d - i)$. For $n = 0$ the set of divisors is
taken to be empty, so $a_{0,i} = 0$.

## Sources

- C. Kassel and C. Reutenauer, *Pairs of Intertwined Integer Sequences*, Journal of Integer Sequences 29 (2026), Article 26.4.4, display (2.3), quoting their earlier Theorem 1.3 of *Complete determination of the zeta function of the Hilbert scheme of n points on a two-dimensional torus*.

Formalized by `MetaMathlibExt.kasselReutenauerCoeff`, a definition declared in [WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/kassel-reutenauer-polynomials/index.html#kassel-reutenauer-coeff).

## Kassel–Reutenauer polynomial

For a natural number $n$, the Kassel–Reutenauer polynomial
$\bar P_n(X) \in \mathbb{Z}[X]$ is defined by

$$
\bar P_n(X) = a_{n,0} + \sum_{i=1}^{n-1} a_{n,i} \, \bar T_i(X),
$$

where $a_{n,i}$ is the number of divisors $d$ of $n$ with $d(d - 2i) \le 2n$ and
$n < 2d(d - i)$ (equivalently, $(i + \sqrt{2n + i^2})/2 < d \le i + \sqrt{2n + i^2}$), and
$\bar T_i$ is the monic Chebyshev polynomial: $\bar T_0 = 2$, $\bar T_1 = X$ and
$\bar T_{i+2} = X \bar T_{i+1} - \bar T_i$. For $n = 0$ the sum is empty and the set of divisors
of $0$ is taken to be empty, so $\bar P_0 = 0$.

In the paper, $\bar P_n$ is characterized for $n \ge 1$ by
$\bar P_n(q + q^{-1}) = P_n(q)/q^{n-1}$, where $(q - 1)^2 P_n(q)$ is the number of ideals of
codimension $n$ of $\mathbb{F}_q[x, y, x^{-1}, y^{-1}]$; the definition here uses the explicit
expansion (2.4) of the paper instead.

## Sources

- C. Kassel and C. Reutenauer, *Pairs of Intertwined Integer Sequences*, Journal of Integer Sequences 29 (2026), Article 26.4.4, (2.1)–(2.4) and Table 2.

Formalized by `MetaMathlibExt.kasselReutenauerPoly`, a definition declared in [WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/kassel-reutenauer-polynomials/index.html#kassel-reutenauer-poly).

## Partial sums of the monic Chebyshev polynomials

For $n \ge 0$, $F_n(X)$ is the
polynomial with integer coefficients

$$F_n(X) = 1 + \sum_{k=1}^{n} \bar T_k(X),$$

where $\bar T_k \in \mathbb{Z}[X]$ is the monic Chebyshev polynomial of the source, that is, the
polynomial with $\bar T_k(q + q^{-1}) = q^k + q^{-k}$; equivalently $\bar T_0 = 2$,
$\bar T_1 = X$ and $\bar T_{k+2} = X \bar T_{k+1} - \bar T_k$. Thus $F_0 = 1$ and
$F_n = F_{n-1} + \bar T_n$ for $n \ge 1$.

## Sources

- C. Kassel and C. Reutenauer, *Pairs of Intertwined Integer Sequences*, Journal of Integer Sequences 29 (2026), Article 26.4.4, (3.6)–(3.7).

Formalized by `MetaMathlibExt.chebyshevCPartialSum`, a definition declared in [WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/kassel-reutenauer-polynomials/index.html#chebyshev-cpartial-sum).

## Small values of the coefficients $a_{n,i}$

The Kassel–Reutenauer coefficients satisfy
$a_{1,0} = 1$, $a_{2,0} = a_{2,1} = 1$, $a_{3,0} = 0$ and $a_{3,1} = a_{3,2} = 1$.

## Sources

- C. Kassel and C. Reutenauer, *Pairs of Intertwined Integer Sequences*, Journal of Integer Sequences 29 (2026), Article 26.4.4, (2.3) and Table 2.

Formalized by `MetaMathlibExt.kasselReutenauerCoeff_small`, a theorem declared in [WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/kassel-reutenauer-polynomials/index.html#kassel-reutenauer-coeff-small).

## The first Kassel–Reutenauer polynomial

The Kassel–Reutenauer polynomial $\bar P_1$ is the
constant polynomial $1$.

## Sources

- C. Kassel and C. Reutenauer, *Pairs of Intertwined Integer Sequences*, Journal of Integer Sequences 29 (2026), Article 26.4.4, Table 2.

Formalized by `MetaMathlibExt.kasselReutenauerPoly_one`, a theorem declared in [WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/kassel-reutenauer-polynomials/index.html#kassel-reutenauer-poly-one).

## The Kassel–Reutenauer polynomial $\bar P_2$

The Kassel–Reutenauer polynomial
$\bar P_2(X) \in \mathbb{Z}[X]$ equals $X + 1$.

## Sources

- C. Kassel and C. Reutenauer, *Pairs of Intertwined Integer Sequences*, Journal of Integer Sequences 29 (2026), Article 26.4.4, Table 2.

Formalized by `MetaMathlibExt.kasselReutenauerPoly_two`, a theorem declared in [WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/kassel-reutenauer-polynomials/index.html#kassel-reutenauer-poly-two).

## The third Kassel–Reutenauer polynomial

The Kassel–Reutenauer polynomial $\bar P_3$ is
$X^2 + X - 2$.

## Sources

- C. Kassel and C. Reutenauer, *Pairs of Intertwined Integer Sequences*, Journal of Integer Sequences 29 (2026), Article 26.4.4, Table 2.

Formalized by `MetaMathlibExt.kasselReutenauerPoly_three`, a theorem declared in [WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/kassel-reutenauer-polynomials/index.html#kassel-reutenauer-poly-three).

## Zeroth partial sum of the Chebyshev polynomials

Let
$F_n = 1 + \sum_{k=1}^{n} \bar T_k \in \mathbb{Z}[X]$ be the partial sums of the monic Chebyshev
polynomials $\bar T_k$ ($\bar T_0 = 2$, $\bar T_1 = X$, $\bar T_{k+2} = X \bar T_{k+1} - \bar T_k$).
Then $F_0 = 1$.

## Sources

- C. Kassel and C. Reutenauer, *Pairs of Intertwined Integer Sequences*, Journal of Integer Sequences 29 (2026), Article 26.4.4, (3.6).

Formalized by `MetaMathlibExt.chebyshevCPartialSum_zero`, a theorem declared in [WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/kassel-reutenauer-polynomials/index.html#chebyshev-cpartial-sum-zero).

## Successive partial sums of the Chebyshev polynomials

Let
$F_n = 1 + \sum_{k=1}^{n} \bar T_k \in \mathbb{Z}[X]$ be the partial sums of the monic Chebyshev
polynomials $\bar T_k$ ($\bar T_0 = 2$, $\bar T_1 = X$, $\bar T_{k+2} = X \bar T_{k+1} - \bar T_k$).
For every natural number $n$, $F_{n+1} = F_n + \bar T_{n+1}$.

## Sources

- C. Kassel and C. Reutenauer, *Pairs of Intertwined Integer Sequences*, Journal of Integer Sequences 29 (2026), Article 26.4.4, (3.6).

Formalized by `MetaMathlibExt.chebyshevCPartialSum_succ`, a theorem declared in [WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/kassel-reutenauer-polynomials/index.html#chebyshev-cpartial-sum-succ).

## First and second partial sums of the Chebyshev polynomials

Let
$F_n = 1 + \sum_{k=1}^{n} \bar T_k \in \mathbb{Z}[X]$ be the partial sums of the monic Chebyshev
polynomials $\bar T_k$ ($\bar T_0 = 2$, $\bar T_1 = X$, $\bar T_{k+2} = X \bar T_{k+1} - \bar T_k$).
Then $F_1 = X + 1$ and $F_2 = X^2 + X - 1$.

## Sources

- C. Kassel and C. Reutenauer, *Pairs of Intertwined Integer Sequences*, Journal of Integer Sequences 29 (2026), Article 26.4.4, Table 4.

Formalized by `MetaMathlibExt.chebyshevCPartialSum_one_two`, a theorem declared in [WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/kassel-reutenauer-polynomials/index.html#chebyshev-cpartial-sum-one-two).

## Positivity of the Kassel–Reutenauer polynomials at integers $N \ge 2$

For every $n \ge 1$
and every integer $N \ge 2$, the Kassel–Reutenauer polynomial $\bar P_n$ satisfies
$\bar P_n(N) > 0$.

## Sources

- C. Kassel and C. Reutenauer, *Pairs of Intertwined Integer Sequences*, Journal of Integer Sequences 29 (2026), Article 26.4.4, Proposition 2.1 (`jis-2026-26.4.4-prop-1`).

Stated but not proved: `MetaMathlibExt.kasselReutenauerPoly_eval_pos` is written with `theorem_wanted` in [WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/kassel-reutenauer-polynomials/index.html#kassel-reutenauer-poly-eval-pos).

## Multiplicativity at roots of unity of order at most 4

Let $q \in \mathbb{C}$ be a primitive
$d$-th root of unity with $d \in \{1, 2, 3, 4\}$, and let $\bar P_n$ be the Kassel–Reutenauer
polynomials. Then for all coprime integers $m, n \ge 1$,

$$
|\bar P_{mn}(q + q^{-1})| = |\bar P_m(q + q^{-1})| \, |\bar P_n(q + q^{-1})|.
$$

Since $|q| = 1$, $|\bar P_n(q + q^{-1})|$ is the absolute value $|P_n(q)|$ of the paper's
polynomial $P_n(q) = q^{n-1} \bar P_n(q + q^{-1})$, so $n \mapsto |P_n(q)|$ is multiplicative.

## Sources

- C. Kassel and C. Reutenauer, *Pairs of Intertwined Integer Sequences*, Journal of Integer Sequences 29 (2026), Article 26.4.4, Proposition 2.2 (`jis-2026-26.4.4-prop-2`).

Stated but not proved: `MetaMathlibExt.kasselReutenauerPoly_norm_multiplicative_rootOfUnity` is written with `theorem_wanted` in [WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/kassel-reutenauer-polynomials/index.html#kassel-reutenauer-poly-norm-multiplicati).

## Almost multiplicativity at a primitive sixth root of unity

Let $\omega \in \mathbb{C}$ be a
primitive sixth root of unity, and for $n \ge 1$ let $v_n = |\bar P_n(\omega + \omega^{-1})|$,
where $\bar P_n$ is the Kassel–Reutenauer polynomial. Let $m, n \ge 1$ be coprime. Then
$v_m v_n = v_{mn}$ if $(m \bmod 3, n \bmod 3)$ is $(0, 1)$, $(1, 1)$ or $(1, 2)$;
$v_m v_n = 2 v_{mn}$ if $(m \bmod 3, n \bmod 3) = (0, 2)$; and $v_m v_n = 4 v_{mn}$ if
$(m \bmod 3, n \bmod 3) = (2, 2)$. The residue pairs are ordered: nothing is claimed for the
swapped pairs.

Since $|\omega| = 1$, $v_n$ is the absolute value $|P_n(\omega)|$ of the paper's polynomial
$P_n(q) = q^{n-1} \bar P_n(q + q^{-1})$.

## Sources

- C. Kassel and C. Reutenauer, *Pairs of Intertwined Integer Sequences*, Journal of Integer Sequences 29 (2026), Article 26.4.4, Proposition 2.3 (`jis-2026-26.4.4-prop-3`).

Stated but not proved: `MetaMathlibExt.kasselReutenauerPoly_norm_almost_multiplicative_sixth` is written with `theorem_wanted` in [WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/kassel-reutenauer-polynomials/index.html#kassel-reutenauer-poly-norm-almost-multi).

## Multiplicativity of $\bar P_n^2$ modulo $X (X + 1) (X^2 - 4)$

Let $\bar P_n$ be the
Kassel–Reutenauer polynomials. For coprime integers $m, n \ge 1$, the polynomial
$\bar P_{mn}(X)^2 - \bar P_m(X)^2 \bar P_n(X)^2$ is divisible in $\mathbb{Z}[X]$ by
$X (X + 1) (X^2 - 4)$; if moreover $(m \bmod 3, n \bmod 3)$ is $(0, 1)$, $(1, 1)$ or $(1, 2)$,
it is divisible by $X (X + 1) (X^2 - 4) (X - 1)$.

## Sources

- C. Kassel and C. Reutenauer, *Pairs of Intertwined Integer Sequences*, Journal of Integer Sequences 29 (2026), Article 26.4.4, Corollary 2.4 (`jis-2026-26.4.4-cor-4`).

Stated but not proved: `MetaMathlibExt.kasselReutenauerPoly_sq_sub_dvd` is written with `theorem_wanted` in [WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/kassel-reutenauer-polynomials/index.html#kassel-reutenauer-poly-sq-sub-dvd).

## Integers at which $|\bar P_n|$ is multiplicative

Let $\bar P_n$ be the
Kassel–Reutenauer polynomial and let $N$ be an integer. Then
$|\bar P_{mn}(N)| = |\bar P_m(N)|\,|\bar P_n(N)|$ for all coprime positive integers $m$ and $n$
if and only if $N \in \{-2, -1, 0, 2\}$.

## Sources

- C. Kassel and C. Reutenauer, *Pairs of Intertwined Integer Sequences*, Journal of Integer Sequences 29 (2026), Article 26.4.4, Proposition 2.5 (`jis-2026-26.4.4-prop-5`).

Stated but not proved: `MetaMathlibExt.kasselReutenauerPoly_abs_eval_multiplicative_iff` is written with `theorem_wanted` in [WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/kassel-reutenauer-polynomials/index.html#kassel-reutenauer-poly-abs-eval-multipli).

## Positivity of the monic Chebyshev polynomials

Let $\bar T_k \in \mathbb{R}[X]$ be the
monic Chebyshev polynomials, given by $\bar T_0 = 2$, $\bar T_1 = X$ and
$\bar T_{k+2} = X \bar T_{k+1} - \bar T_k$. Then $\bar T_k(x) > 0$ for every natural number $k$
and every real number $x \ge 2$.

## Sources

- C. Kassel and C. Reutenauer, *Pairs of Intertwined Integer Sequences*, Journal of Integer Sequences 29 (2026), Article 26.4.4, Proposition 3.1 (`jis-2026-26.4.4-prop-6`).

Stated but not proved: `MetaMathlibExt.chebyshevC_eval_pos_of_two_le` is written with `theorem_wanted` in [WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/kassel-reutenauer-polynomials/index.html#chebyshev-c-eval-pos-of-two-le).

## Trace formula for the monic Chebyshev polynomials

Let $\bar T_k \in \mathbb{Z}[X]$ be
the monic Chebyshev polynomials, given by $\bar T_0 = 2$, $\bar T_1 = X$ and
$\bar T_{k+2} = X \bar T_{k+1} - \bar T_k$, and let $M$ be the $2 \times 2$ matrix over
$\mathbb{Z}[X]$ with rows $(X, -1)$ and $(1, 0)$. Then $\bar T_k = \operatorname{tr}(M^k)$ for
every natural number $k$.

## Sources

- C. Kassel and C. Reutenauer, *Pairs of Intertwined Integer Sequences*, Journal of Integer Sequences 29 (2026), Article 26.4.4, Proposition 3.2 (`jis-2026-26.4.4-prop-7`).

Stated but not proved: `MetaMathlibExt.chebyshevC_eq_trace_pow` is written with `theorem_wanted` in [WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/kassel-reutenauer-polynomials/index.html#chebyshev-c-eq-trace-pow).

## Generating function of the partial sums of Chebyshev polynomials

Let
$F_n = 1 + \sum_{k=1}^{n} \bar T_k \in \mathbb{Z}[X]$ be the partial sums of the monic Chebyshev
polynomials $\bar T_k$ ($\bar T_0 = 2$, $\bar T_1 = X$, $\bar T_{k+2} = X \bar T_{k+1} - \bar T_k$).
In the ring $\mathbb{Z}[X][[t]]$ of formal power series in $t$ over $\mathbb{Z}[X]$,

$$(1 - X t + t^2) \sum_{n \ge 0} F_n t^n = 1 + t.$$

Since $1 - X t + t^2$ is a unit in $\mathbb{Z}[X][[t]]$, this is equivalent to
$\sum_{n \ge 0} F_n t^n = (1 + t)/(1 - X t + t^2)$.

## Sources

- C. Kassel and C. Reutenauer, *Pairs of Intertwined Integer Sequences*, Journal of Integer Sequences 29 (2026), Article 26.4.4, Proposition 3.3 (`jis-2026-26.4.4-prop-8`).

Stated but not proved: `MetaMathlibExt.chebyshevCPartialSum_generatingFunction` is written with `theorem_wanted` in [WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/kassel-reutenauer-polynomials/index.html#chebyshev-cpartial-sum-generating-functi).

## Binomial expansion of the partial sums of Chebyshev polynomials

Let
$F_n = 1 + \sum_{k=1}^{n} \bar T_k \in \mathbb{Z}[X]$ be the partial sums of the monic Chebyshev
polynomials $\bar T_k$ ($\bar T_0 = 2$, $\bar T_1 = X$, $\bar T_{k+2} = X \bar T_{k+1} - \bar T_k$).
For every $n \ge 1$,

$$F_n = \sum_{m=0}^{\lfloor n/2 \rfloor} (-1)^m \binom{n-m}{m} X^{n-2m} +
\sum_{m=0}^{\lfloor (n-1)/2 \rfloor} (-1)^m \binom{n-m-1}{m} X^{n-2m-1}.$$

## Sources

- C. Kassel and C. Reutenauer, *Pairs of Intertwined Integer Sequences*, Journal of Integer Sequences 29 (2026), Article 26.4.4, Proposition 3.4 (`jis-2026-26.4.4-prop-9`).

Stated but not proved: `MetaMathlibExt.chebyshevCPartialSum_eq_binomial_sum` is written with `theorem_wanted` in [WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/kassel-reutenauer-polynomials/index.html#chebyshev-cpartial-sum-eq-binomial-sum).

## Leading coefficients of the partial sums of Chebyshev polynomials

Let
$F_n = 1 + \sum_{k=1}^{n} \bar T_k \in \mathbb{Z}[X]$ be the partial sums of the monic Chebyshev
polynomials $\bar T_k$ ($\bar T_0 = 2$, $\bar T_1 = X$, $\bar T_{k+2} = X \bar T_{k+1} - \bar T_k$).
For every $n \ge 5$, the polynomial

$$F_n - \Big(X^n + X^{n-1} - (n-1) X^{n-2} - (n-2) X^{n-3} + \binom{n-2}{2} X^{n-4} +
\binom{n-3}{2} X^{n-5}\Big)$$

is either zero or has degree less than $n - 5$.

Here $\binom{n-2}{2} = (n-2)(n-3)/2$ and $\binom{n-3}{2} = (n-3)(n-4)/2$.

## Sources

- C. Kassel and C. Reutenauer, *Pairs of Intertwined Integer Sequences*, Journal of Integer Sequences 29 (2026), Article 26.4.4, Corollary 3.5 (`jis-2026-26.4.4-cor-10`).

Stated but not proved: `MetaMathlibExt.chebyshevCPartialSum_top_coeffs` is written with `theorem_wanted` in [WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/kassel-reutenauer-polynomials/index.html#chebyshev-cpartial-sum-top-coeffs).

## Three-term recurrence for the partial sums of Chebyshev polynomials

Let
$F_n = 1 + \sum_{k=1}^{n} \bar T_k \in \mathbb{Z}[X]$ be the partial sums of the monic Chebyshev
polynomials $\bar T_k$ ($\bar T_0 = 2$, $\bar T_1 = X$, $\bar T_{k+2} = X \bar T_{k+1} - \bar T_k$).
For every $k \ge 1$, $F_{k+1} = X F_k - F_{k-1}$.

## Sources

- C. Kassel and C. Reutenauer, *Pairs of Intertwined Integer Sequences*, Journal of Integer Sequences 29 (2026), Article 26.4.4, Proposition 3.6 (`jis-2026-26.4.4-prop-11`).

Stated but not proved: `MetaMathlibExt.chebyshevCPartialSum_recurrence` is written with `theorem_wanted` in [WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/kassel-reutenauer-polynomials/index.html#chebyshev-cpartial-sum-recurrence).

## Approximation of $\bar P_n$ by $F_{n-1}$

Let $\bar P_n$ be the Kassel–Reutenauer
polynomials, and for $r \ge 0$ let $F_r(X) = 1 + \sum_{j=1}^{r} \bar T_j(X)$ be the partial sum
of the monic Chebyshev polynomials $\bar T_j$. For $n \ge 2$, every nonzero coefficient of
$\bar P_n(X) - F_{n-1}(X)$ sits in a degree $k$ with $2k + 2 < n$; that is, the difference has
degree less than $n/2 - 1$.

## Sources

- C. Kassel and C. Reutenauer, *Pairs of Intertwined Integer Sequences*, Journal of Integer Sequences 29 (2026), Article 26.4.4, Theorem 4.1 (`jis-2026-26.4.4-thm-12`).

Stated but not proved: `MetaMathlibExt.kasselReutenauerPoly_sub_chebyshevCPartialSum_coeff` is written with `theorem_wanted` in [WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean, line 302](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean#L302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/kassel-reutenauer-polynomials/index.html#kassel-reutenauer-poly-sub-chebyshev-cpa).

## Top coefficients of the Kassel–Reutenauer polynomials

For $n \ge 10$, the polynomial

$$
\bar P_n(X) - \Bigl(X^{n-1} + X^{n-2} - (n-2) X^{n-3} - (n-3) X^{n-4} +
\tbinom{n-3}{2} X^{n-5} + \tbinom{n-4}{2} X^{n-6}\Bigr)
$$

has degree less than $n - 6$, where $\bar P_n$ is the Kassel–Reutenauer polynomial. That is, up
to terms of degree at most $n - 7$, $\bar P_n(X)$ equals
$X^{n-1} + X^{n-2} - (n-2) X^{n-3} - (n-3) X^{n-4} + \frac{(n-3)(n-4)}{2} X^{n-5} +
\frac{(n-4)(n-5)}{2} X^{n-6}$.

## Sources

- C. Kassel and C. Reutenauer, *Pairs of Intertwined Integer Sequences*, Journal of Integer Sequences 29 (2026), Article 26.4.4, Corollary 4.2 (`jis-2026-26.4.4-cor-13`).

Stated but not proved: `MetaMathlibExt.kasselReutenauerPoly_top_coeffs` is written with `theorem_wanted` in [WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/kassel-reutenauer-polynomials/index.html#kassel-reutenauer-poly-top-coeffs).

## The top coefficients $a_{n,i}$ equal $1$

Let $n \ge 1$ and let $i$ be a natural number
with $n \le 2i + 2$ and $i \le n - 1$; equivalently $n/2 - 1 \le i \le n - 1$, where $n/2$ is
the rational number, not the integer quotient. Then the Kassel–Reutenauer coefficient $a_{n,i}$
equals $1$.

## Sources

- C. Kassel and C. Reutenauer, *Pairs of Intertwined Integer Sequences*, Journal of Integer Sequences 29 (2026), Article 26.4.4, Lemma 4.3 (`jis-2026-26.4.4-lem-14`).

Stated but not proved: `MetaMathlibExt.kasselReutenauerCoeff_eq_one` is written with `theorem_wanted` in [WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean, line 328](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean#L328). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/kassel-reutenauer-polynomials/index.html#kassel-reutenauer-coeff-eq-one).

## Odd-divisor formula for the Kassel–Reutenauer polynomials

Let $n \ge 1$, and for each
odd divisor $d$ of $n$ put $r_n(d) = n/d - (d+1)/2$, an integer. Then the Kassel–Reutenauer
polynomial $\bar P_n$ satisfies

$$
\bar P_n(X) = \sum_{d \mid n,\ d \text{ odd},\ r_n(d) \ge 0} F_{r_n(d)}(X) -
\sum_{d \mid n,\ d \text{ odd},\ r_n(d) < 0} F_{-r_n(d)-1}(X),
$$

where $F_r(X) = 1 + \sum_{k=1}^{r} \bar T_k(X)$ is the partial sum of the monic Chebyshev
polynomials $\bar T_k$.

## Sources

- C. Kassel and C. Reutenauer, *Pairs of Intertwined Integer Sequences*, Journal of Integer Sequences 29 (2026), Article 26.4.4, Theorem 4.4 (`jis-2026-26.4.4-thm-16`).

Stated but not proved: `MetaMathlibExt.kasselReutenauerPoly_eq_oddDivisor_sum` is written with `theorem_wanted` in [WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean, line 338](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean#L338). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/kassel-reutenauer-polynomials/index.html#kassel-reutenauer-poly-eq-odd-divisor-su).

## $\bar P_n$ equals $F_{n-1}$ exactly for powers of two

Let $n \ge 1$, let $\bar P_n$ be the
Kassel–Reutenauer polynomial, and let $F_{n-1} = 1 + \sum_{k=1}^{n-1} \bar T_k$ be the partial
sum of the monic Chebyshev polynomials. Then $\bar P_n = F_{n-1}$ if and only if $n = 2^k$ for
some natural number $k$.

## Sources

- C. Kassel and C. Reutenauer, *Pairs of Intertwined Integer Sequences*, Journal of Integer Sequences 29 (2026), Article 26.4.4, Corollary 4.5 (`jis-2026-26.4.4-cor-17`).

Stated but not proved: `MetaMathlibExt.kasselReutenauerPoly_eq_chebyshevCPartialSum_iff` is written with `theorem_wanted` in [WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean, line 350](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean#L350). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/kassel-reutenauer-polynomials/index.html#kassel-reutenauer-poly-eq-chebyshev-cpar).

## $C_n(q)/q^n$ as a sum over the solutions of $h(h + 1 + 2a) = 2n$

Let $n \ge 1$, let
$\bar P_n$ be the Kassel–Reutenauer polynomial, and write $C_n(q)/q^n$ for the Laurent polynomial
$(q - 2 + q^{-1})\,\bar P_n(q + q^{-1})$ in $\mathbb{Z}[q, q^{-1}]$. Then

$$\frac{C_n(q)}{q^n} = \sum_{(h, a)} (-1)^h \left(q^a + q^{-a}\right),$$

where the sum runs over the pairs of integers $(h, a)$ with $1 \le h \le 2n$, $-n \le a \le n$
and $h(h + 1 + 2a) = 2n$. Moreover, if $h, h'$ are positive integers and $a, a'$ are
integers with $h(h + 1 + 2a) = 2n$, $h'(h' + 1 + 2a') = 2n$ and $|a| = |a'|$, then $h = h'$
and $a = a'$.

Every pair of integers $(h, a)$ with $h \ge 1$ and $h(h + 1 + 2a) = 2n$ satisfies $h \le 2n$
and $|a| \le n$, so the sum runs over all such pairs.

## Sources

- C. Kassel and C. Reutenauer, *Pairs of Intertwined Integer Sequences*, Journal of Integer Sequences 29 (2026), Article 26.4.4, Lemma 5.2 (`jis-2026-26.4.4-lem-22`).

Stated but not proved: `MetaMathlibExt.kasselReutenauer_C_div_pow_eq_sum` is written with `theorem_wanted` in [WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/kassel-reutenauer-polynomials/index.html#kassel-reutenauer-c-div-pow-eq-sum).

## Increasing-sequence and odd-divisor formulas for $C_n(q)/q^n$

Let $n \ge 1$, let
$\bar P_n$ be the Kassel–Reutenauer polynomial, and write $C_n(q)/q^n$ for the Laurent polynomial
$(q - 2 + q^{-1})\,\bar P_n(q + q^{-1})$ in $\mathbb{Z}[q, q^{-1}]$. For integers $h \ge 1$ and
$a$ let $IS(a, h) = \{a + 1, \dots, a + h\}$.

(i) We have

$$\frac{C_n(q)}{q^n} = \sum_{(h, a)} (-1)^h \left(q^a + q^{-a}\right),$$

where the sum runs over the pairs of integers $(h, a)$ with $1 \le h \le 2n$ and $-n \le a \le n$
such that the elements of $IS(a, h)$ sum to $n$. Moreover, if $h, h' \ge 1$ and $a, a'$ are
integers such that the elements of $IS(a, h)$ and those of $IS(a', h')$ both sum to $n$, and
$|a| = |a'|$, then $h = h'$ and $a = a'$.

(ii) For an odd divisor $d$ of $n$ put $u_d = n/d - (d - 1)/2$ and $v_d = n/d - (d + 1)/2$. Then

$$\frac{C_n(q)}{q^n} = \sum_{d \mid n,\ d \text{ odd}} (q^{u_d} + q^{-u_d} - q^{v_d} - q^{-v_d}),$$

and in the list of the exponents $u_d, -u_d, v_d, -v_d$ over all odd divisors $d$ of $n$, the
nonzero entries are pairwise distinct.

Every pair $(h, a)$ with $h \ge 1$ such that the elements of $IS(a, h)$ sum to $n$ satisfies
$h \le 2n$ and $|a| \le n$, so the sum in (i) runs over all such sequences.

## Sources

- C. Kassel and C. Reutenauer, *Pairs of Intertwined Integer Sequences*, Journal of Integer Sequences 29 (2026), Article 26.4.4, Theorem 5.3 (`jis-2026-26.4.4-thm-23`).

Stated but not proved: `MetaMathlibExt.kasselReutenauer_C_div_pow_increasingSequences` is written with `theorem_wanted` in [WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean, line 387](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean#L387). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/kassel-reutenauer-polynomials/index.html#kassel-reutenauer-c-div-pow-increasing-s).

## The absolute coefficient sum of $C_n$ counts odd divisors

Let $n \ge 1$, let $\bar P_n$ be
the Kassel–Reutenauer polynomial, and write $C_n(q)/q^n$ for the Laurent polynomial
$(q - 2 + q^{-1})\,\bar P_n(q + q^{-1})$ in $\mathbb{Z}[q, q^{-1}]$. Then the sum of the absolute
values of the coefficients of $C_n(q)/q^n$ equals four times the number of odd divisors of $n$.

Multiplying by $q^n$ does not change the coefficients, so this is the source's statement about
the polynomial $C_n(q)$.

## Sources

- C. Kassel and C. Reutenauer, *Pairs of Intertwined Integer Sequences*, Journal of Integer Sequences 29 (2026), Article 26.4.4, Corollary 5.4 (`jis-2026-26.4.4-cor-24`).

Stated but not proved: `MetaMathlibExt.kasselReutenauer_C_abs_coeff_sum` is written with `theorem_wanted` in [WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean, line 416](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean#L416). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/kassel-reutenauer-polynomials/index.html#kassel-reutenauer-c-abs-coeff-sum).

## Laurent polynomial identity for the partial sums of Chebyshev polynomials

Let
$F_r = 1 + \sum_{k=1}^{r} \bar T_k \in \mathbb{Z}[X]$ be the partial sums of the monic Chebyshev
polynomials $\bar T_k$ ($\bar T_0 = 2$, $\bar T_1 = X$, $\bar T_{k+2} = X \bar T_{k+1} - \bar T_k$).
For every natural number $r$, in the ring $\mathbb{Z}[q, q^{-1}]$ of Laurent polynomials,

$$q^{r+1} + q^{-r-1} - q^r - q^{-r} = q^{-1} (q - 1)^2 F_r(q + q^{-1}).$$

## Sources

- C. Kassel and C. Reutenauer, *Pairs of Intertwined Integer Sequences*, Journal of Integer Sequences 29 (2026), Article 26.4.4, Lemma 6.1 (`jis-2026-26.4.4-lem-26`).

Stated but not proved: `MetaMathlibExt.chebyshevCPartialSum_laurent_identity` is written with `theorem_wanted` in [WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean, line 428](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean#L428). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/kassel-reutenauer-polynomials/index.html#chebyshev-cpartial-sum-laurent-identity).

## Increasing-sequence formula for the Kassel–Reutenauer polynomials

Let $n \ge 1$ and
work in the ring $\mathbb{Z}[q, q^{-1}]$ of Laurent polynomials. For integers $a$ and $h$ let
$IS(a, h) = \{a+1, \dots, a+h\}$. For an odd divisor $d$ of $n$ put $r_n(d) = n/d - (d+1)/2$,
$A_d = IS(r_n(d), d)$ and $\check A_d = IS(-r_n(d) - 1, 2n/d)$. Then the Kassel–Reutenauer
polynomial $\bar P_n$ satisfies

$$
\bar P_n(q + q^{-1}) = \sum_{d \mid n,\ d \text{ odd},\ r_n(d) \ge 0}\
\sum_{i \in \check A_d \setminus A_d} q^i -
\sum_{d \mid n,\ d \text{ odd},\ r_n(d) < 0}\ \sum_{i \in A_d \setminus \check A_d} q^i.
$$

The left-hand side is the paper's $P_n(q)/q^{n-1}$.

## Sources

- C. Kassel and C. Reutenauer, *Pairs of Intertwined Integer Sequences*, Journal of Integer Sequences 29 (2026), Article 26.4.4, Proposition 6.2 (`jis-2026-26.4.4-prop-27`).

Stated but not proved: `MetaMathlibExt.kasselReutenauerPoly_laurent_increasingSequences` is written with `theorem_wanted` in [WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean, line 444](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean#L444). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/kassel-reutenauer-polynomials/index.html#kassel-reutenauer-poly-laurent-increasin).

## Zeta function of the Hilbert scheme of points on the two-dimensional torus

Let $p$ be a
prime, $k \ge 1$, $q = p^k$ and $n \ge 1$. For $m \ge 1$ let $\mathbb{F}_{q^m}$ be the field with
$q^m$ elements and let $N_m$ be the number of ideals $I$ of the Laurent polynomial ring
$\mathbb{F}_{q^m}[x^{\pm 1}, y^{\pm 1}]$ (the group algebra of $\mathbb{Z} \times \mathbb{Z}$)
such that the quotient by $I$ has dimension $n$ over $\mathbb{F}_{q^m}$; this is the number of
$\mathbb{F}_{q^m}$-points of the Hilbert scheme $H^n$ of $n$ points on the torus. For an odd
divisor $d$ of $n$ put $r_n(d) = n/d - (d + 1)/2$, $a_d = n + r_n(d)$ and $b_d = n - r_n(d)$.
Then the zeta function $Z(t) = \exp\big(\sum_{m \ge 1} N_m t^m / m\big)$, a formal power series
with rational coefficients, is

$$Z(t) = \prod_{d} \frac{(1-q^{a_d}t)(1-q^{b_d}t)}{(1-q^{a_d+1}t)(1-q^{b_d-1}t)},$$

the product running over the odd divisors $d$ of $n$.

The exponents $a_d$, $b_d$, $a_d + 1$ and $b_d - 1$ are nonnegative integers.

## Sources

- C. Kassel and C. Reutenauer, *Pairs of Intertwined Integer Sequences*, Journal of Integer Sequences 29 (2026), Article 26.4.4, Proposition 5.5 (`jis-2026-26.4.4-prop-25`).

Stated but not proved: `MetaMathlibExt.hilbertSchemeTorus_zeta_eq_prod` is written with `theorem_wanted` in [WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean, line 472](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/IntertwinedIntegerSequencesWanted.lean#L472). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/kassel-reutenauer-polynomials/index.html#hilbert-scheme-torus-zeta-eq-prod).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kassel–Reutenauer polynomials](https://deicyde.github.io/atlas-lean/roadmap/Algebra/orthogonal-polynomials/kassel-reutenauer-polynomials/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Algebra/orthogonal-polynomials/kassel-reutenauer-polynomials)
