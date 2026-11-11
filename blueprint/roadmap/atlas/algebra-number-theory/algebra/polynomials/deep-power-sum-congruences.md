---
declaration: section
origin: cited
lean: MetaMathlibExt.IsDividedPowerIdeal, MetaMathlibExt.isDividedPowerIdeal_bot, MetaMathlibExt.DividedPowers.isDividedPowerIdeal, MetaMathlibExt.polyElemSymm, MetaMathlibExt.polyElemSymm_zero, MetaMathlibExt.polyElemSymm_of_natDegree_lt, MetaMathlibExt.polyPowerSum, MetaMathlibExt.polyPowerSum_zero
statement: formalized
---

# Deep power-sum congruences

37 results, 15 proved and 22 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html).

## Divided-power ideal

An ideal $I$ of a commutative ring $A$ is a *divided-power ideal* when
for every $a \in I$ and every integer $k \ge 1$ there is $c \in I$ with $a^k = k! \, c$, that is,
$a^k \in k! \, I$. For a prime $p$, in a torsion-free $\mathbb{Z}_{(p)}$-algebra this says
$a^k / k! \in I$.

## Sources

- S. Anni, A. Ghitza and A. Medvedovsky, *Elementary Symmetric Functions and Deep Power-Sum Congruences*, INTEGERS 24 (2024), Article A46, Section 2.2.

Formalized by `MetaMathlibExt.IsDividedPowerIdeal`, a definition declared in [WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html#is-divided-power-ideal).

## The zero ideal is a divided-power ideal

In every commutative ring, the zero ideal is a
divided-power ideal.

## Sources

- S. Anni, A. Ghitza and A. Medvedovsky, *Elementary Symmetric Functions and Deep Power-Sum Congruences*, INTEGERS 24 (2024), Article A46, Section 2.2 (the definition).

Formalized by `MetaMathlibExt.isDividedPowerIdeal_bot`, a theorem declared in [WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html#is-divided-power-ideal-bot).

## Ideals with divided powers are divided-power ideals

Let $I$ be an ideal of a commutative
ring $A$. If $I$ carries a divided-power structure $(\gamma_k)_{k \ge 0}$ in the usual sense, then
$I$ is a divided-power ideal: for every $a \in I$ and every $k \ge 1$ there is $c \in I$ with
$a^k = k!\, c$.

## Sources

- S. Anni, A. Ghitza and A. Medvedovsky, *Elementary Symmetric Functions and Deep Power-Sum Congruences*, INTEGERS 24 (2024), Article A46, Section 2.2 (the maps `γ_k(a) = a ^ k / k!`).

Formalized by `MetaMathlibExt.DividedPowers.isDividedPowerIdeal`, a theorem declared in [WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html#is-divided-power-ideal-2).

## Elementary symmetric functions of a polynomial

Let $P$ be a polynomial of degree $d$ over
a commutative ring, with $d = 0$ for $P = 0$. For a natural number $n$, $e_n(P)$ is $(-1)^n$ times
the coefficient of $X^{d - n}$ in $P$ if $n \le d$, and $0$ if $n > d$. In particular
$e_0(P) = 1$ when $P$ is monic.

## Sources

- S. Anni, A. Ghitza and A. Medvedovsky, *Elementary Symmetric Functions and Deep Power-Sum Congruences*, INTEGERS 24 (2024), Article A46, Section 3.2, Notation.

Formalized by `MetaMathlibExt.polyElemSymm`, a definition declared in [WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html#poly-elem-symm).

## The zeroth elementary symmetric function of a monic polynomial

For every monic
polynomial $P$ over a commutative ring, $e_0(P) = 1$.

## Sources

- S. Anni, A. Ghitza and A. Medvedovsky, *Elementary Symmetric Functions and Deep Power-Sum Congruences*, INTEGERS 24 (2024), Article A46, Section 3.2, Notation.

Formalized by `MetaMathlibExt.polyElemSymm_zero`, a theorem declared in [WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html#poly-elem-symm-zero).

## Elementary symmetric functions vanish above the degree

Let $P$ be a polynomial of degree
$d$ over a commutative ring, with $d = 0$ for $P = 0$. Then $e_n(P) = 0$ for every $n > d$.

## Sources

- S. Anni, A. Ghitza and A. Medvedovsky, *Elementary Symmetric Functions and Deep Power-Sum Congruences*, INTEGERS 24 (2024), Article A46, Section 3.2, Notation.

Formalized by `MetaMathlibExt.polyElemSymm_of_natDegree_lt`, a theorem declared in [WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html#poly-elem-symm-of-nat-degree-lt).

## Power sums of a polynomial

For a polynomial $P$ over a commutative ring $A$, with
elementary symmetric functions $e_i = e_i(P)$, the power sums $p_n = p_n(P) \in A$ are defined
recursively: $p_0$ is the degree of $P$ as a natural number ($0$ for $P = 0$), and for
$n \ge 1$ Newton's identity holds:

$$p_n = \sum_{i=1}^{n-1} (-1)^{i-1} e_i\, p_{n-i} + (-1)^{n-1} n\, e_n.$$

If $P$ is monic and $P = (X - \alpha_1) \cdots (X - \alpha_d)$, then
$p_n = \alpha_1^n + \cdots + \alpha_d^n$ for every $n$.

## Sources

- S. Anni, A. Ghitza and A. Medvedovsky, *Elementary Symmetric Functions and Deep Power-Sum Congruences*, INTEGERS 24 (2024), Article A46, Sections 2.1 and 3.2 (Newton's identities, Macdonald I.2.11').

Formalized by `MetaMathlibExt.polyPowerSum`, a definition declared in [WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html#poly-power-sum).

## The zeroth power sum of a polynomial is its degree

For every polynomial $P$ over a
commutative ring $A$, the power sum $p_0(P)$ equals the degree of $P$ as a natural number
(taken to be $0$ for $P = 0$), viewed as an element of $A$.

## Sources

- S. Anni, A. Ghitza and A. Medvedovsky, *Elementary Symmetric Functions and Deep Power-Sum Congruences*, INTEGERS 24 (2024), Article A46, Section 3.2, Notation.

Formalized by `MetaMathlibExt.polyPowerSum_zero`, a theorem declared in [WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html#poly-power-sum-zero).

## The first power sum is the first elementary symmetric function

For every polynomial $P$
over a commutative ring, $p_1(P) = e_1(P)$.

## Sources

- S. Anni, A. Ghitza and A. Medvedovsky, *Elementary Symmetric Functions and Deep Power-Sum Congruences*, INTEGERS 24 (2024), Article A46, Section 3.2 (Newton's identities).

Formalized by `MetaMathlibExt.polyPowerSum_one`, a theorem declared in [WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html#poly-power-sum-one).

## Newton's recurrence for the power sums of a polynomial

For every polynomial $P$ over a
commutative ring and every $n \ge 0$, writing $e_i = e_i(P)$ and $p_i = p_i(P)$ for the
elementary symmetric functions and power sums of $P$,

$$p_{n+1} = (-1)^n (n+1)\, e_{n+1} + \sum_{i=0}^{n-1} (-1)^i e_{i+1}\, p_{n-i}.$$

## Sources

- S. Anni, A. Ghitza and A. Medvedovsky, *Elementary Symmetric Functions and Deep Power-Sum Congruences*, INTEGERS 24 (2024), Article A46, Section 3.2 (Newton's identities).

Formalized by `MetaMathlibExt.polyPowerSum_succ`, a theorem declared in [WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html#poly-power-sum-succ).

## A prime-exponent criterion for powers in an ideal

Let $p$ be a prime, $v_p$ the $p$-adic
valuation, and $\mathfrak{b}$ an ideal of a commutative ring $B$.
The following are equivalent: for every $n \ge 1$ and every $a \in \mathfrak{b}$ there is
$c \in \mathfrak{b}$ with $a^n = p^{v_p(n!)} c$; and for every $a \in \mathfrak{b}$ there is
$c \in \mathfrak{b}$ with $a^p = p c$.

## Sources

- S. Anni, A. Ghitza and A. Medvedovsky, *Elementary Symmetric Functions and Deep Power-Sum Congruences*, INTEGERS 24 (2024), Article A46, Proposition 3.

Stated but not proved: `MetaMathlibExt.pow_mem_prime_pow_padicValNat_factorial_iff` is written with `theorem_wanted` in [WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html#pow-mem-prime-pow-padic-val-nat-factoria).

## The $p$-th power criterion for divided-power ideals

Let $p$ be a prime and let $A$ be a
commutative ring in which every natural number not divisible by $p$ is a unit (a
$\mathbb{Z}_{(p)}$-algebra). An ideal $\mathfrak{a}$ of $A$ is a divided-power ideal if and only if
for every $a \in \mathfrak{a}$ there is $c \in \mathfrak{a}$ with $a^p = p\,c$, that is,
$a^p \in p\mathfrak{a}$.

The paper also assumes $A$ torsion-free; the statement does not need it.

## Sources

- S. Anni, A. Ghitza and A. Medvedovsky, *Elementary Symmetric Functions and Deep Power-Sum Congruences*, INTEGERS 24 (2024), Article A46, Corollary 4.

Stated but not proved: `MetaMathlibExt.isDividedPowerIdeal_iff_pow_prime_mem` is written with `theorem_wanted` in [WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html#is-divided-power-ideal-iff-pow-prime-mem).

## Divided-power ideals generated by a set

Let $p$ be a prime and $A$ a commutative ring in
which every natural number not divisible by $p$ is a unit (a $\mathbb{Z}_{(p)}$-algebra). For a
subset $S \subseteq A$, the ideal $\mathfrak{a}$ generated by $S$ is a divided-power ideal if and
only if for every $a \in S$ there is $c \in \mathfrak{a}$ with $a^p = pc$, that is,
$a^p \in p\mathfrak{a}$.

Torsion-freeness of $A$ is not needed.

## Sources

- S. Anni, A. Ghitza and A. Medvedovsky, *Elementary Symmetric Functions and Deep Power-Sum Congruences*, INTEGERS 24 (2024), Article A46, Proposition 5.

Stated but not proved: `MetaMathlibExt.isDividedPowerIdeal_span_iff` is written with `theorem_wanted` in [WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html#is-divided-power-ideal-span-iff).

## Product of a divided-power ideal with an ideal

Let $A$ be a commutative ring. If
$\mathfrak{a}$ is a divided-power ideal of $A$, then for every ideal $\mathfrak{b}$ of $A$ the
product $\mathfrak{a}\mathfrak{b}$ is a divided-power ideal.

## Sources

- S. Anni, A. Ghitza and A. Medvedovsky, *Elementary Symmetric Functions and Deep Power-Sum Congruences*, INTEGERS 24 (2024), Article A46, Corollary 6.

Stated but not proved: `MetaMathlibExt.IsDividedPowerIdeal.mul` is written with `theorem_wanted` in [WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html#mul).

## Powers of the maximal ideal of a DVR that are divided-power ideals

Let $p$ be a prime and
let $O$ be a discrete valuation ring with maximal ideal $\mathfrak{m}$ such that
$pO = \mathfrak{m}^e$ for some integer $e \ge 1$. Then for every $k \ge 0$, the ideal
$\mathfrak{m}^k$ is a divided-power ideal if and only if $e \le (p - 1)k$.

Equivalently, with $v_p(\mathfrak{m}) = 1/e$, the condition is $v_p(\mathfrak{m}^k) \ge 1/(p - 1)$.
The paper states this for $p$-adic discrete valuation rings and remarks that it also holds for
localizations of rings of integers; here $O$ is any such ring, and the zero ideal is omitted.

## Sources

- S. Anni, A. Ghitza and A. Medvedovsky, *Elementary Symmetric Functions and Deep Power-Sum Congruences*, INTEGERS 24 (2024), Article A46, Lemma 7.

Stated but not proved: `MetaMathlibExt.isDividedPowerIdeal_maximalIdeal_pow_iff` is written with `theorem_wanted` in [WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html#is-divided-power-ideal-maximal-ideal-pow).

## When the maximal ideal of a DVR is a divided-power ideal

Let $p$ be a prime and let $O$ be
a discrete valuation ring with maximal ideal $\mathfrak{m}$ such that $pO = \mathfrak{m}^e$ for
some integer $e \ge 1$. Then $\mathfrak{m}$ is a divided-power ideal if and only if $e \le p - 1$.

## Sources

- S. Anni, A. Ghitza and A. Medvedovsky, *Elementary Symmetric Functions and Deep Power-Sum Congruences*, INTEGERS 24 (2024), Article A46, Corollary 8.

Stated but not proved: `MetaMathlibExt.isDividedPowerIdeal_maximalIdeal_iff` is written with `theorem_wanted` in [WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html#is-divided-power-ideal-maximal-ideal-iff).

## $(p)$ is a divided-power ideal of $\mathbb{Z}_p$

For every prime $p$, the ideal generated
by $p$ in the ring $\mathbb{Z}_p$ of $p$-adic integers is a divided-power ideal.

## Sources

- S. Anni, A. Ghitza and A. Medvedovsky, *Elementary Symmetric Functions and Deep Power-Sum Congruences*, INTEGERS 24 (2024), Article A46, Corollary 8, last sentence.

Stated but not proved: `MetaMathlibExt.isDividedPowerIdeal_span_prime_padicInt` is written with `theorem_wanted` in [WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html#is-divided-power-ideal-span-prime-padic).

## Congruent elementary symmetric functions give deep power-sum congruences

Let $p$ be a
prime and let $A$ be a commutative ring without additive torsion in which every natural number
not divisible by $p$ is a unit (a torsion-free $\mathbb{Z}_{(p)}$-algebra). Let
$\mathfrak{a}$ be a divided-power ideal of $A$, let $P, Q \in A[X]$ be monic and let $N \ge 1$;
write $e_n$ and $p_n$ for the elementary symmetric functions and power sums of a polynomial.
If $e_n(P) - e_n(Q) \in \mathfrak{a}$ for every $n$ with $1 \le n \le N$, then there is
$c \in \mathfrak{a}$ with $p_N(P) - p_N(Q) = N c$, that is,
$p_N(P) \equiv p_N(Q) \pmod{N \mathfrak{a}}$.

## Sources

- S. Anni, A. Ghitza and A. Medvedovsky, *Elementary Symmetric Functions and Deep Power-Sum Congruences*, INTEGERS 24 (2024), Article A46, Proposition 12.

Stated but not proved: `MetaMathlibExt.polyPowerSum_sub_mem_of_polyElemSymm_sub_mem` is written with `theorem_wanted` in [WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html#poly-power-sum-sub-mem-of-poly-elem-symm).

## Power-sum congruences imply elementary symmetric congruences

Let $p$ be a prime and $A$ a
torsion-free commutative ring in which every natural number not divisible by $p$ is a unit (a
torsion-free $\mathbb{Z}_{(p)}$-algebra). Let $\mathfrak{a}$ be a divided-power ideal of $A$, let
$P, Q \in A[X]$ be monic and let $N$ be a natural number. Suppose that for every $n$ with
$1 \le n \le N$ there is $c \in \mathfrak{a}$ with $p_n(P) - p_n(Q) = n c$, that is,
$p_n(P) \equiv p_n(Q) \pmod{n \mathfrak{a}}$. Then $e_n(P) - e_n(Q) \in \mathfrak{a}$ for every $n$
with $1 \le n \le N$.

## Sources

- S. Anni, A. Ghitza and A. Medvedovsky, *Elementary Symmetric Functions and Deep Power-Sum Congruences*, INTEGERS 24 (2024), Article A46, Proposition 13.

Stated but not proved: `MetaMathlibExt.polyElemSymm_sub_mem_of_polyPowerSum_sub_mem` is written with `theorem_wanted` in [WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html#poly-elem-symm-sub-mem-of-poly-power-sum).

## Exponential of a power-sum series restricted to a set of degrees

Let $\sigma$ be a finite
set of variables, and in $\mathbb{Q}[x_i : i \in \sigma]$ let $p_s = \sum_{i \in \sigma} x_i^s$
be the $s$-th power sum. Let $S$ be a set of natural numbers and let
$P_S(t) = \sum_{s \in S,\ s \ge 1} \frac{(-1)^{s-1}}{s} p_s t^s$. For a partition $\lambda$ of
$n$ with parts $\lambda_1, \dots, \lambda_\ell$, write
$p_\lambda = p_{\lambda_1} \cdots p_{\lambda_\ell}$, $\varepsilon_\lambda = (-1)^{n - \ell}$ and
$z_\lambda = \prod_a a^{r_a} \, r_a!$, where $r_a$ is the number of parts equal to $a$ and the
product runs over the distinct parts $a$. Then, as formal power series in $t$ with coefficients
in $\mathbb{Q}[x_i : i \in \sigma]$, $\exp P_S(t) = \sum_{n \ge 0} c_n t^n$, where $c_n$ is the
sum of $\varepsilon_\lambda p_\lambda / z_\lambda$ over the partitions $\lambda$ of $n$ all of
whose parts lie in $S$.

## Sources

- S. Anni, A. Ghitza and A. Medvedovsky, *Elementary Symmetric Functions and Deep Power-Sum Congruences*, INTEGERS 24 (2024), Article A46, Proposition 19.

Stated but not proved: `MetaMathlibExt.exp_signedPowerSumSeries_eq_sum_partitions` is written with `theorem_wanted` in [WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html#exp-signed-power-sum-series-eq-sum-parti).

## The generating function of the elementary symmetric polynomials

Let $\sigma$ be a finite
set of variables, and in $\mathbb{Q}[x_i : i \in \sigma]$ let $e_k$ be the $k$-th elementary
symmetric polynomial and $p_n = \sum_{i \in \sigma} x_i^n$ the $n$-th power sum. Then, as formal
power series in $t$ with coefficients in $\mathbb{Q}[x_i : i \in \sigma]$,

$$\sum_{k \ge 0} e_k t^k = \exp\Big(\sum_{n \ge 1} \frac{(-1)^{n-1}}{n} p_n t^n\Big).$$

## Sources

- S. Anni, A. Ghitza and A. Medvedovsky, *Elementary Symmetric Functions and Deep Power-Sum Congruences*, INTEGERS 24 (2024), Article A46, Proposition 20.

Stated but not proved: `MetaMathlibExt.exp_signedPowerSumSeries_eq_esymmSeries` is written with `theorem_wanted` in [WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html#exp-signed-power-sum-series-eq-esymm-ser).

## Elementary symmetric polynomials in terms of power sums

Let $\sigma$ be a finite set of
variables, and in $\mathbb{Q}[x_i : i \in \sigma]$ let $e_n$ be the $n$-th elementary symmetric
polynomial and $p_k = \sum_{i \in \sigma} x_i^k$ the $k$-th power sum. For a partition $\lambda$
of $n$ with parts $\lambda_1, \dots, \lambda_\ell$, write
$p_\lambda = p_{\lambda_1} \cdots p_{\lambda_\ell}$, $\varepsilon_\lambda = (-1)^{n - \ell}$ and
$z_\lambda = \prod_a a^{r_a} \, r_a!$, where $r_a$ is the number of parts equal to $a$ and the
product runs over the distinct parts $a$. Then for every $n \ge 0$,

$$e_n = \sum_{\lambda \vdash n} \frac{\varepsilon_\lambda}{z_\lambda} \, p_\lambda.$$

## Sources

- S. Anni, A. Ghitza and A. Medvedovsky, *Elementary Symmetric Functions and Deep Power-Sum Congruences*, INTEGERS 24 (2024), Article A46, Corollary 21.

Stated but not proved: `MetaMathlibExt.esymm_eq_sum_partitions` is written with `theorem_wanted` in [WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html#esymm-eq-sum-partitions).

## Kummer's theorem for multinomial coefficients

Let $p$ be a prime and let
$r_1, \dots, r_k$ be natural numbers with sum $m$. For $i \ge 1$ let
$c_i = \lfloor ((r_1 \bmod p^i) + \dots + (r_k \bmod p^i)) / p^i \rfloor$. Then

$$v_p\binom{m}{r_1, \dots, r_k} = \sum_{i=1}^{m} c_i.$$

Here $c_i$ is the carry into digit position $i$ when $r_1 + \dots + r_k$ is added in base $p$, and
$c_i = 0$ for $i > m$, so the right side is the sum of all the carries.

## Sources

- S. Anni, A. Ghitza and A. Medvedovsky, *Elementary Symmetric Functions and Deep Power-Sum Congruences*, INTEGERS 24 (2024), Article A46, Theorem 23.

Stated but not proved: `MetaMathlibExt.padicValNat_multinomial_eq_sum_carries` is written with `theorem_wanted` in [WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html#padic-val-nat-multinomial-eq-sum-carries).

## A valuation bound from Kummer's theorem

Let $p$ be a prime, let $r_1, \dots, r_k$ be
natural numbers with sum $m$, and let $j$ be an index with $r_j \ne 0$. Then

$$v_p(m) \le v_p(r_j) + v_p\binom{m}{r_1, \dots, r_k},$$

that is, $v_p(r_j) \ge v_p(m) - v_p\binom{m}{r_1, \dots, r_k}$.

The hypothesis $r_j \ne 0$ is needed because $v_p(0)$ is taken to be $0$: for $(r_1, r_2) = (0, p)$
the inequality fails at $j = 1$. With the paper's convention $v_p(0) = \infty$ that case is trivial.

## Sources

- S. Anni, A. Ghitza and A. Medvedovsky, *Elementary Symmetric Functions and Deep Power-Sum Congruences*, INTEGERS 24 (2024), Article A46, Corollary 24.

Stated but not proved: `MetaMathlibExt.padicValNat_sum_le_add_padicValNat_multinomial` is written with `theorem_wanted` in [WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html#padic-val-nat-sum-le-add-padic-val-nat-m).

## Powers of elements congruent modulo a divided-power ideal

Let $p$ be a prime, let $A$ be
a commutative ring in which every natural number not divisible by $p$ is a unit (a
$\mathbb{Z}_{(p)}$-algebra), and let $\mathfrak{a}$ be a divided-power ideal of $A$. If
$x, y \in A$ satisfy $x - y \in \mathfrak{a}$, then for every $m \ge 0$ there is
$c \in \mathfrak{a}$ with $x^{p^m} - y^{p^m} = p^m c$, and for every $n \ge 0$ there is
$c \in \mathfrak{a}$ with $x^n - y^n = n c$.

The ring $A$ is not assumed to be torsion-free.

## Sources

- S. Anni, A. Ghitza and A. Medvedovsky, *Elementary Symmetric Functions and Deep Power-Sum Congruences*, INTEGERS 24 (2024), Article A46, Lemma 25.

Stated but not proved: `MetaMathlibExt.pow_sub_pow_mem_of_sub_mem` is written with `theorem_wanted` in [WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html#pow-sub-pow-mem-of-sub-mem).

## Congruence of products over a partition with multiplicities divisible by $p^v$

Let $p$
be a prime, $A$ a commutative ring and $\mathfrak{a}$ a divided-power ideal of $A$. Let
$f, g : \mathbb{N} \to A$ satisfy $f_n - g_n \in \mathfrak{a}$ for every $n \ge 1$. For a
partition $\lambda = (\lambda_1, \dots, \lambda_k)$ of a natural number $m$, write
$f_\lambda = f_{\lambda_1} \cdots f_{\lambda_k}$ and
$g_\lambda = g_{\lambda_1} \cdots g_{\lambda_k}$. If $v$ is a natural number such that every part
of $\lambda$ occurs a multiple of $p^v$ times, then $f_\lambda - g_\lambda = p^v c$ for some
$c \in \mathfrak{a}$, that is, $f_\lambda \equiv g_\lambda \bmod p^v \mathfrak{a}$.

The paper takes $v = v_p(\lambda) = \min_i v_p(\lambda_i)$, which is false: for $p = 2$,
$\lambda = (2)$, $A = \mathbb{Z}_{(2)}$, $\mathfrak{a} = (2)$, $f_n = e_n(X^2 + 2)$ and
$g_n = e_n(X^2)$, where $e_n(P)$ is the $n$-th elementary symmetric function of the roots of $P$,
$f_n \equiv g_n \bmod 2$ for all $n$ but $f_2 - g_2 = 2 \notin 4\mathbb{Z}_{(2)}$. The paper's
proof writes $\lambda = \mu^{p^v}$ in the partition monoid, which uses the multiplicity condition
stated here. The paper's symmetric functions are abstracted to arbitrary sequences $f, g$, as the
statement only uses their values.

## Sources

- S. Anni, A. Ghitza and A. Medvedovsky, *Elementary Symmetric Functions and Deep Power-Sum Congruences*, INTEGERS 24 (2024), Article A46, Corollary 26.

Stated but not proved: `MetaMathlibExt.multiset_prod_sub_prod_mem_of_count_dvd` is written with `theorem_wanted` in [WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html#multiset-prod-sub-prod-mem-of-count-dvd).

## Möbius sum over the divisors prime to a given prime

Let $p$ be a prime, $\mu$ the Möbius
function and $n \ge 1$. The sum of $\mu(d)$ over the divisors $d$ of $n$ with $p \nmid d$ is $1$ if
$n$ is a power of $p$ (including $n = 1 = p^0$) and $0$ otherwise.

## Sources

- S. Anni, A. Ghitza and A. Medvedovsky, *Elementary Symmetric Functions and Deep Power-Sum Congruences*, INTEGERS 24 (2024), Article A46, Lemma 28.

Stated but not proved: `MetaMathlibExt.sum_moebius_divisors_not_dvd_prime` is written with `theorem_wanted` in [WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean, line 314](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean#L314). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html#sum-moebius-divisors-not-dvd-prime).

## The Artin–Hasse exponential has $p$-integral coefficients

Let $p$ be a prime and let
$F(z) = \exp\big(\sum_{j \ge 0} z^{p^j} / p^j\big) \in \mathbb{Q}[[z]]$ be the Artin–Hasse
exponential. For every $n \ge 0$, the coefficient of $z^n$ in $F$, written in lowest terms, has a
denominator not divisible by $p$.

## Sources

- S. Anni, A. Ghitza and A. Medvedovsky, *Elementary Symmetric Functions and Deep Power-Sum Congruences*, INTEGERS 24 (2024), Article A46, Corollary 29.

Stated but not proved: `MetaMathlibExt.artinHasse_coeff_den_not_dvd` is written with `theorem_wanted` in [WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean, line 324](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean#L324). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html#artin-hasse-coeff-den-not-dvd).

## The Artin–Hasse exponential as a product

Let $p$ be a prime, let $\mu$ be the Möbius
function and let $F(z) = \exp\big(\sum_{j \ge 0} z^{p^j} / p^j\big) \in \mathbb{Q}[[z]]$ be the
Artin–Hasse exponential. For $d \ge 1$ and $a \in \mathbb{Q}$ write
$(1 - z^d)^a = \exp\big(a \log(1 - z^d)\big)$, where $\log(1 - z^d) = -\sum_{k \ge 1} z^{dk}/k$.
Then for every $N \ge 0$, $F$ has the same coefficients of $z^0, \dots, z^N$ as the finite product
of the series $(1 - z^d)^{-\mu(d)/d}$ over the integers $1 \le d \le N$ not divisible by $p$.
Since the factors with $d > N$ are $1 + O(z^{N+1})$, this is the identity
$F(z) = \prod_{p \nmid d} (1 - z^d)^{-\mu(d)/d}$ read coefficientwise.

## Sources

- S. Anni, A. Ghitza and A. Medvedovsky, *Elementary Symmetric Functions and Deep Power-Sum Congruences*, INTEGERS 24 (2024), Article A46, Proposition 27.

Stated but not proved: `MetaMathlibExt.artinHasse_eq_prod_one_sub_pow` is written with `theorem_wanted` in [WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean, line 338](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean#L338). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html#artin-hasse-eq-prod-one-sub-pow).

## $p$-splitting of multisets of parts

Let $p$ be a natural number and $s$, $t$ multisets of
natural numbers (multisets of parts). Then $s$ is a *$p$-splitting* of $t$ when there is $u \ge 1$
such that $t$ contains the part $pu$ and $s$ is obtained from $t$ by removing one instance of $pu$
and adding $p$ copies of $u$.

## Sources

- S. Anni, A. Ghitza and A. Medvedovsky, *Elementary Symmetric Functions and Deep Power-Sum Congruences*, INTEGERS 24 (2024), Article A46, Definition 30.

Formalized by `MetaMathlibExt.IsPSplitting`, a definition declared in [WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean, line 352](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean#L352). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html#is-psplitting).

## $p$ copies of $u$ form a $p$-splitting of $\{pu\}$

For every natural number $p$ and every
integer $u \ge 1$, the multiset consisting of $p$ copies of $u$ is a $p$-splitting of the
one-element multiset $\{pu\}$.

## Sources

- S. Anni, A. Ghitza and A. Medvedovsky, *Elementary Symmetric Functions and Deep Power-Sum Congruences*, INTEGERS 24 (2024), Article A46, Definition 30.

Formalized by `MetaMathlibExt.isPSplitting_replicate_singleton`, a theorem declared in [WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean, line 359](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean#L359). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html#is-psplitting-replicate-singleton).

## The $p$-equivalence class of a multiset of parts

Let $p$ be a natural number and $\lambda$
a multiset of natural numbers whose elements sum to $n$. The $p$-equivalence class $C_\lambda$ is
the set of partitions $\mu$ of $n$ with $\mu \sim_p \lambda$, where $\sim_p$ ($p$-equivalence) is
the equivalence relation on multisets of natural numbers generated by $p$-splitting.

## Sources

- S. Anni, A. Ghitza and A. Medvedovsky, *Elementary Symmetric Functions and Deep Power-Sum Congruences*, INTEGERS 24 (2024), Article A46, Definition 31.

Formalized by `MetaMathlibExt.pEquivClass`, a definition declared in [WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean, line 369](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean#L369). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html#p-equiv-class).

## The $p$-equivalence class sum

Let $\sigma$ be a finite set of variables, let $p$ be a
natural number and let $\lambda$ be a multiset of natural numbers whose elements sum to $n$. In
$\mathbb{Q}[x_i : i \in \sigma]$ let $p_k = \sum_{i \in \sigma} x_i^k$ be the $k$-th power sum. For
a partition $\mu$ of $n$ with parts $\mu_1, \dots, \mu_\ell$, write
$p_\mu = p_{\mu_1} \cdots p_{\mu_\ell}$, $\varepsilon_\mu = (-1)^{n - \ell}$ and
$z_\mu = \prod_a a^{r_a} \, r_a!$, where $r_a$ is the number of parts of $\mu$ equal to $a$ and the
product runs over the distinct parts $a$ of $\mu$. The $p$-equivalence class sum of $\lambda$ is

$$g_\lambda = \sum_{\mu \in C_\lambda} \frac{\varepsilon_\mu}{z_\mu} \, p_\mu,$$

where $C_\lambda$ is the $p$-equivalence class of $\lambda$: the set of partitions of $n$ that are
$p$-equivalent to $\lambda$.

## Sources

- S. Anni, A. Ghitza and A. Medvedovsky, *Elementary Symmetric Functions and Deep Power-Sum Congruences*, INTEGERS 24 (2024), Article A46, Section 5.2, display (8).

Formalized by `MetaMathlibExt.pEquivClassSum`, a definition declared in [WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean, line 379](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean#L379). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html#p-equiv-class-sum).

## The class sum of the empty partition

For every finite set of variables $\sigma$ and every
natural number $p$, the $p$-equivalence class sum of the empty multiset is $g_\emptyset = 1$.

## Sources

- S. Anni, A. Ghitza and A. Medvedovsky, *Elementary Symmetric Functions and Deep Power-Sum Congruences*, INTEGERS 24 (2024), Article A46, Section 5.2.

Formalized by `MetaMathlibExt.pEquivClassSum_zero`, a theorem declared in [WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean, line 388](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean#L388). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html#p-equiv-class-sum-zero).

## Multiplicativity of $g_\lambda$ over disjoint parts

Let $p$ be a prime, $\sigma$ a finite
set of variables, and for a multiset $\lambda$ of parts let $g_\lambda$ be its $p$-equivalence class
sum in $\mathbb{Q}[x_i : i \in \sigma]$. Let $\lambda$ and $\mu$ be multisets of natural numbers,
none of whose elements is divisible by $p$ (so no part is $0$), with no part in common. Then
$g_{\lambda + \mu} = g_\lambda \, g_\mu$, where $\lambda + \mu$ is the union of $\lambda$ and $\mu$
counted with multiplicity. Moreover $g_\lambda = \prod_u g_{(u)^{r_u(\lambda)}}$, the product over
the distinct parts $u$ of $\lambda$, where $r_u(\lambda)$ is the number of times $u$ occurs in
$\lambda$ and $(u)^r$ is the multiset of $r$ copies of $u$.

## Sources

- S. Anni, A. Ghitza and A. Medvedovsky, *Elementary Symmetric Functions and Deep Power-Sum Congruences*, INTEGERS 24 (2024), Article A46, Lemma 34.

Stated but not proved: `MetaMathlibExt.pEquivClassSum_add_of_disjoint` is written with `theorem_wanted` in [WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html#p-equiv-class-sum-add-of-disjoint).

## For odd $p$ the signs in $g_\lambda$ are constant

Let $p$ be an odd prime, $\sigma$ a
finite set of variables and $\lambda$ a partition of $n$ with $\ell(\lambda)$ parts. Then the
$p$-equivalence class sum $g_\lambda$ in $\mathbb{Q}[x_i : i \in \sigma]$ satisfies

$$g_\lambda = (-1)^{n - \ell(\lambda)} \sum_{\mu \in C_\lambda} \frac{p_\mu}{z_\mu},$$

where $C_\lambda$ is the $p$-equivalence class of $\lambda$ (the partitions $\mu$ of $n$ with
$\mu \sim_p \lambda$), $p_\mu = \prod_i p_{\mu_i}$ is the product of the power sums
$p_k = \sum_{i \in \sigma} x_i^k$, and $z_\mu = \prod_a a^{r_a} \, r_a!$, the product over the
distinct parts $a$ of $\mu$, with $r_a$ the number of parts of $\mu$ equal to $a$.

## Sources

- S. Anni, A. Ghitza and A. Medvedovsky, *Elementary Symmetric Functions and Deep Power-Sum Congruences*, INTEGERS 24 (2024), Article A46, Lemma 35.

Stated but not proved: `MetaMathlibExt.pEquivClassSum_eq_neg_one_pow_smul` is written with `theorem_wanted` in [WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean, line 421](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean#L421). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html#p-equiv-class-sum-eq-neg-one-pow-smul).

## $g_\lambda$ is $p$-integral

Let $p$ be a prime, $\sigma$ a finite set of variables and
$\lambda$ a partition of $n$. Every coefficient of the $p$-equivalence class sum $g_\lambda$ in
$\mathbb{Q}[x_i : i \in \sigma]$ is a rational number whose denominator in lowest terms is not
divisible by $p$.

This is the paper's $g_\lambda \in \Lambda_{\mathbb{Z}_{(p)}}$, in finitely many variables.

## Sources

- S. Anni, A. Ghitza and A. Medvedovsky, *Elementary Symmetric Functions and Deep Power-Sum Congruences*, INTEGERS 24 (2024), Article A46, Proposition 36.

Stated but not proved: `MetaMathlibExt.pEquivClassSum_coeff_den_not_dvd` is written with `theorem_wanted` in [WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean, line 431](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/DeepPowerSumCongruencesWanted.lean#L431). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html#p-equiv-class-sum-coeff-den-not-dvd).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Deep power-sum congruences](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/deep-power-sum-congruences/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Algebra/polynomials/deep-power-sum-congruences)
