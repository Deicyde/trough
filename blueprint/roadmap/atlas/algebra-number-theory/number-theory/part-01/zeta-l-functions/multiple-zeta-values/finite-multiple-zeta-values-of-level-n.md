---
declaration: section
origin: cited
lean: MetaMathlibExt.coloredFiniteMZV, MetaMathlibExt.coloredFiniteMZV_zero, MetaMathlibExt.sum_Ioo_eq_pow_mul_coloredFiniteMZV, MetaMathlibExt.two_mul_coloredFiniteMZV_twelve, MetaMathlibExt.fermatLastTheoremFor_of_regular, MetaMathlibExt.fermat_first_case_of_not_isWieferichPrime, MetaMathlibExt.fermatQuotient_two_mul_eq_neg_sum, MetaMathlibExt.exists_odd_not_dvd_bernoulli_num_le
statement: formalized
---

# Finite multiple zeta values of level N

17 results, 5 proved and 12 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/finite-multiple-zeta-values-of-level-n/index.html).

## Colored finite multiple harmonic sums

Let $p$ and $N$ be natural numbers, let
$k = (k_1, \dots, k_r)$ be a finite sequence of natural numbers and let
$\alpha = (\alpha_1, \dots, \alpha_r) \in (\mathbb{Z}/N\mathbb{Z})^r$. The colored finite multiple
harmonic sum $\zeta^{\alpha}_{p,N}(k) \in \mathbb{Z}/p\mathbb{Z}$ is the sum of
$m_1^{-k_1} \cdots m_r^{-k_r}$ over all integers $0 < m_1 < \dots < m_r < p$ with
$m_i \equiv \alpha_i \pmod N$ for every $i$.

Here $m^{-1}$ is the inverse of $m$ in $\mathbb{Z}/p\mathbb{Z}$; when $p$ is prime every
$0 < m < p$ is invertible, and for other $p$ non-units get a conventional value.

## Sources

- Seki, *Regular Primes, Non-Wieferich Primes, and Finite Multiple Zeta Values of Level N*, INTEGERS 24 (2024), Article A22, Section 2.2 (definition of `ζ^α_{p,N}(k)`).

Formalized by `MetaMathlibExt.coloredFiniteMZV`, a definition declared in [WantedExt/NumberTheory/FiniteMultipleZetaLevelWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FiniteMultipleZetaLevelWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/finite-multiple-zeta-values-of-level-n/index.html#colored-finite-mzv).

## Colored finite multiple harmonic sum of the empty index

For all natural numbers $p$
and $N$, the colored finite multiple harmonic sum $\zeta^{\varnothing}_{p,N}(\varnothing)$ of the
empty index, with the empty tuple of colors, equals $1$ in $\mathbb{Z}/p\mathbb{Z}$.

## Sources

- Seki, *Regular Primes, Non-Wieferich Primes, and Finite Multiple Zeta Values of Level N*, INTEGERS 24 (2024), Article A22, Section 2.2 (`ζ^∅_{p,N}(∅) = 1`).

Formalized by `MetaMathlibExt.coloredFiniteMZV_zero`, a theorem declared in [WantedExt/NumberTheory/FiniteMultipleZetaLevelWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FiniteMultipleZetaLevelWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/finite-multiple-zeta-values-of-level-n/index.html#colored-finite-mzv-zero).

## Sums over a subinterval of $(0, p)$ as colored finite multiple zeta values

Let
$N \ge 1$, $0 \le j < N$, and let $k = (k_1, \dots, k_r)$ be a tuple of natural numbers of weight
$w = k_1 + \dots + k_r$. For a prime $p$ and $\alpha \in (\mathbb{Z}/N\mathbb{Z})^r$ let
$\zeta^{\alpha}_{p,N}(k) \in \mathbb{Z}/p\mathbb{Z}$ be the colored finite multiple harmonic sum,
the sum of $1/(m_1^{k_1} \cdots m_r^{k_r})$ over the integers $0 < m_1 < \dots < m_r < p$ with
$m_i \equiv \alpha_i \pmod{N}$ for all $i$. Then for all but finitely many primes $p$, with
$\alpha = (-jp, \dots, -jp) \in (\mathbb{Z}/N\mathbb{Z})^r$,
$\sum 1/(m_1^{k_1} \cdots m_r^{k_r}) = N^w \zeta^{\alpha}_{p,N}(k)$ in $\mathbb{Z}/p\mathbb{Z}$,
where the sum is over the integers $m_1, \dots, m_r$ with
$jp/N < m_1 < \dots < m_r < (j+1)p/N$.

The entries of $k$ may be $0$; the paper's indices have positive entries.

## Sources

- Seki, *Regular Primes, Non-Wieferich Primes, and Finite Multiple Zeta Values of Level N*, INTEGERS 24 (2024), Article A22, Lemma 1.

Stated but not proved: `MetaMathlibExt.sum_Ioo_eq_pow_mul_coloredFiniteMZV` is written with `theorem_wanted` in [WantedExt/NumberTheory/FiniteMultipleZetaLevelWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FiniteMultipleZetaLevelWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/finite-multiple-zeta-values-of-level-n/index.html#sum-ioo-eq-pow-mul-colored-finite-mzv).

## Level-$12$ colored finite zeta values and Bernoulli numbers

Let $k \ge 3$ be odd. For a
prime $p > k$ write $Z_p(k) = B_{p-k}/k \in \mathbb{Z}/p\mathbb{Z}$, where $B_n$ is the $n$-th
Bernoulli number, and for $\alpha \in \mathbb{Z}/12\mathbb{Z}$ let
$\zeta^{\alpha}_{p,12}(k) \in \mathbb{Z}/p\mathbb{Z}$ be the sum of $m^{-k}$ over $0 < m < p$ with
$m \equiv \alpha \pmod{12}$. Then for all but finitely many primes $p$, in $\mathbb{Z}/p\mathbb{Z}$,
$2\zeta^{-2p}_{p,12}(k) = (2^{-k} - 3^{-k} - 4^{-k} + 12^{-k}) Z_p(k)$ and
$2\zeta^{-3p}_{p,12}(k) = (3^{-k} - 4^{-k} - 6^{-k} + 12^{-k}) Z_p(k)$.

## Sources

- Seki, *Regular Primes, Non-Wieferich Primes, and Finite Multiple Zeta Values of Level N*, INTEGERS 24 (2024), Article A22, Proposition 3.

Stated but not proved: `MetaMathlibExt.two_mul_coloredFiniteMZV_twelve` is written with `theorem_wanted` in [WantedExt/NumberTheory/FiniteMultipleZetaLevelWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FiniteMultipleZetaLevelWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/finite-multiple-zeta-values-of-level-n/index.html#two-mul-colored-finite-mzv-twelve).

## Kummer's theorem for regular primes

Let $p$ be an odd prime and let $K$ be a $p$-th
cyclotomic field over $\mathbb{Q}$ (a number field generated over $\mathbb{Q}$ by a primitive
$p$-th root of unity). If $p$ does not divide the class number of $K$, then Fermat's Last Theorem
holds for the exponent $p$: there are no positive integers $a, b, c$ with $a^p + b^p = c^p$.

## Sources

- Seki, *Regular Primes, Non-Wieferich Primes, and Finite Multiple Zeta Values of Level N*, INTEGERS 24 (2024), Article A22, Theorem 1.

Stated but not proved: `MetaMathlibExt.fermatLastTheoremFor_of_regular` is written with `theorem_wanted` in [WantedExt/NumberTheory/FiniteMultipleZetaLevelWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FiniteMultipleZetaLevelWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/finite-multiple-zeta-values-of-level-n/index.html#fermat-last-theorem-for-of-regular).

## Wieferich's criterion for the first case of Fermat's Last Theorem

Let $p$ be a prime
that is not a Wieferich prime, that is, $p^2 \nmid 2^{p-1} - 1$. Then there are no integers
$x, y, z$ with $p \nmid xyz$ and $x^p + y^p = z^p$.

## Sources

- Seki, *Regular Primes, Non-Wieferich Primes, and Finite Multiple Zeta Values of Level N*, INTEGERS 24 (2024), Article A22, Theorem 2.

Stated but not proved: `MetaMathlibExt.fermat_first_case_of_not_isWieferichPrime` is written with `theorem_wanted` in [WantedExt/NumberTheory/FiniteMultipleZetaLevelWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FiniteMultipleZetaLevelWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/finite-multiple-zeta-values-of-level-n/index.html#fermat-first-case-of-not-is-wieferich-pr).

## Skula–Dobson–Ichimura congruence for the Fermat quotient of $2$

Let $p$ be an odd prime
and $N$ a positive integer with $p \nmid N$. Write $q_p(2) = (2^{p-1} - 1)/p$ for the Fermat
quotient of $2$, and for integers $i \ge 0$ and $M \ge 1$ let $s_p(i, M) \in \mathbb{Z}/p\mathbb{Z}$
be the sum of $m^{-1}$ over the integers $m$ with $0 < m < p$ and $ip/M < m < (i+1)p/M$. Then
$(N + 1)\, q_p(2) \equiv -\sum_{0 \le j < N/2} s_p(2j, 2N) \pmod{p}$.

## Sources

- Seki, *Regular Primes, Non-Wieferich Primes, and Finite Multiple Zeta Values of Level N*, INTEGERS 24 (2024), Article A22, Theorem 3.

Stated but not proved: `MetaMathlibExt.fermatQuotient_two_mul_eq_neg_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/FiniteMultipleZetaLevelWanted.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FiniteMultipleZetaLevelWanted.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/finite-multiple-zeta-values-of-level-n/index.html#fermat-quotient-two-mul-eq-neg-sum).

## A small odd $k$ with $p \nmid B_{p-k}$

For every prime $p \ge 11$ there is an odd
integer $k \ge 3$ such that $p$ does not divide the numerator of the Bernoulli number $B_{p-k}$
and $k \le (p-3)/2$ if $p \equiv 1 \pmod 4$, while $k \le (p-5)/2$ if
$p \equiv 3 \pmod 4$.

Equivalently, the least such odd $k$ is at most this bound. Since $p - k$ is even and at least
$2$, the convention for $B_1$ does not matter.

## Sources

- Seki, *Regular Primes, Non-Wieferich Primes, and Finite Multiple Zeta Values of Level N*, INTEGERS 24 (2024), Article A22, Proposition 5.

Stated but not proved: `MetaMathlibExt.exists_odd_not_dvd_bernoulli_num_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/FiniteMultipleZetaLevelWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FiniteMultipleZetaLevelWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/finite-multiple-zeta-values-of-level-n/index.html#exists-odd-not-dvd-bernoulli-num-le).

## Finite multiple zeta value of level $N$ with a color map

Let $p$ and $N$ be natural
numbers, $k = (k_1, \dots, k_r)$ a tuple of natural numbers, and $c$ a color map, which sends
each $a \in \mathbb{Z}/N\mathbb{Z}$ either to $\emptyset$ or to a tuple in
$(\mathbb{Z}/N\mathbb{Z})^r$. The $p$-component
$\zeta^c_{\mathcal{A},N}(k)_p \in \mathbb{Z}/p\mathbb{Z}$ is the colored finite multiple harmonic
sum $\zeta^{\alpha}_{p,N}(k)$ when $c(p \bmod N) = \alpha$ is a tuple, and $0$ when
$c(p \bmod N) = \emptyset$.

Color maps are taken on all of $\mathbb{Z}/N\mathbb{Z}$; only their values at units matter for all
but finitely many $p$.

## Sources

- Seki, *Regular Primes, Non-Wieferich Primes, and Finite Multiple Zeta Values of Level N*, INTEGERS 24 (2024), Article A22, Definition 2.1 (finite multiple zeta values of level `N` with color map).

Formalized by `MetaMathlibExt.finiteMZVColored`, a definition declared in [WantedExt/NumberTheory/FiniteMultipleZetaLevelWanted.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FiniteMultipleZetaLevelWanted.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/finite-multiple-zeta-values-of-level-n/index.html#finite-mzvcolored).

## The empty color map gives zero

For all natural numbers $p$ and $N$ and every tuple
$k = (k_1, \dots, k_r)$ of natural numbers, if $c$ is the color map sending every
$a \in \mathbb{Z}/N\mathbb{Z}$ to $\emptyset$, then the $p$-component $\zeta^c_{\mathcal{A},N}(k)_p$
of the finite multiple zeta value of level $N$ with color map $c$ is $0$.

## Sources

- Seki, *Regular Primes, Non-Wieferich Primes, and Finite Multiple Zeta Values of Level N*, INTEGERS 24 (2024), Article A22, Definition 2.1.

Formalized by `MetaMathlibExt.finiteMZVColored_none`, a theorem declared in [WantedExt/NumberTheory/FiniteMultipleZetaLevelWanted.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FiniteMultipleZetaLevelWanted.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/finite-multiple-zeta-values-of-level-n/index.html#finite-mzvcolored-none).

## A constant color map gives the colored harmonic sum

For all natural numbers $p$ and $N$,
every tuple $k = (k_1, \dots, k_r)$ of natural numbers and every
$\alpha \in (\mathbb{Z}/N\mathbb{Z})^r$, if $c$ is the color map sending every
$a \in \mathbb{Z}/N\mathbb{Z}$ to $\alpha$, then the $p$-component $\zeta^c_{\mathcal{A},N}(k)_p$
of the finite multiple zeta value of level $N$ with color map $c$ equals the colored finite
multiple harmonic sum $\zeta^{\alpha}_{p,N}(k)$.

## Sources

- Seki, *Regular Primes, Non-Wieferich Primes, and Finite Multiple Zeta Values of Level N*, INTEGERS 24 (2024), Article A22, Definition 2.1.

Formalized by `MetaMathlibExt.finiteMZVColored_some`, a theorem declared in [WantedExt/NumberTheory/FiniteMultipleZetaLevelWanted.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FiniteMultipleZetaLevelWanted.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/finite-multiple-zeta-values-of-level-n/index.html#finite-mzvcolored-some).

## Reversal for finite multiple zeta values of level $N$

Let $N \ge 1$, let
$k = (k_1, \dots, k_r)$ be a tuple of natural numbers of weight $w = k_1 + \dots + k_r$, and let
$c$ be a color map, which sends each $a \in \mathbb{Z}/N\mathbb{Z}$ either to $\emptyset$ or to a
tuple in $(\mathbb{Z}/N\mathbb{Z})^r$. Write $k^{\leftarrow} = (k_r, \dots, k_1)$, and let
$c^{\leftarrow}$ be the color map with $c^{\leftarrow}(a) = (a - \alpha_r, \dots, a - \alpha_1)$
when $c(a) = (\alpha_1, \dots, \alpha_r)$ and $c^{\leftarrow}(a) = \emptyset$ when
$c(a) = \emptyset$. Then for all but finitely many primes $p$, the $p$-components of the finite
multiple zeta values of level $N$ with these color maps satisfy
$\zeta^{c}_{\mathcal{A},N}(k)_p = (-1)^w \zeta^{c^{\leftarrow}}_{\mathcal{A},N}(k^{\leftarrow})_p$
in $\mathbb{Z}/p\mathbb{Z}$.

## Sources

- Seki, *Regular Primes, Non-Wieferich Primes, and Finite Multiple Zeta Values of Level N*, INTEGERS 24 (2024), Article A22, Proposition 1.

Stated but not proved: `MetaMathlibExt.finiteMZVColored_eq_neg_one_pow_mul_reverse` is written with `theorem_wanted` in [WantedExt/NumberTheory/FiniteMultipleZetaLevelWanted.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FiniteMultipleZetaLevelWanted.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/finite-multiple-zeta-values-of-level-n/index.html#finite-mzvcolored-eq-neg-one-pow-mul-rev).

## Decomposition of finite multiple zeta values into level-$N$ pieces

Let $N \ge 1$ and
let $k = (k_1, \dots, k_r)$ be a finite sequence of natural numbers (entries equal to $0$ are
allowed) of weight $w = k_1 + \dots + k_r$. For a prime $p$ put
$\zeta_p(k) = \sum_{0 < m_1 < \dots < m_r < p} m_1^{-k_1} \cdots m_r^{-k_r}$ in
$\mathbb{Z}/p\mathbb{Z}$, and for $0 \le j < N$ and a finite sequence $l$ let
$\zeta^{[j]}_{p,N}(l)$ be the colored finite multiple harmonic sum of level $N$ of $l$ with every
color equal to the class of $-jp$ modulo $N$. Then for all sufficiently large primes $p$

$$
\zeta_p(k) = N^w \sum_{0 \le i_1 \le \dots \le i_{N-1} \le r} \prod_{j=0}^{N-1}
\zeta^{[j]}_{p,N}(k_{i_j + 1}, \dots, k_{i_{j+1}}),
$$

where $i_0 = 0$, $i_N = r$, and $(k_{i_j + 1}, \dots, k_{i_{j+1}})$ is empty when
$i_j = i_{j+1}$.

## Sources

- Seki, *Regular Primes, Non-Wieferich Primes, and Finite Multiple Zeta Values of Level N*, INTEGERS 24 (2024), Article A22, Proposition 1.

Stated but not proved: `MetaMathlibExt.coloredFiniteMZV_one_eq_pow_mul_sum_prod` is written with `theorem_wanted` in [WantedExt/NumberTheory/FiniteMultipleZetaLevelWanted.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FiniteMultipleZetaLevelWanted.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/finite-multiple-zeta-values-of-level-n/index.html#colored-finite-mzv-one-eq-pow-mul-sum-pr).

## Raising the level of finite multiple zeta values

Let $N$ and $M$ be positive integers
with $N \mid M$, let $k = (k_1, \dots, k_r)$ be an index of positive integers of weight
$w = k_1 + \dots + k_r$, and let $c$ be a color map from $\mathbb{Z}/N\mathbb{Z}$ to
$(\mathbb{Z}/N\mathbb{Z})^r \cup \{\varnothing\}$. Write $\zeta^{c}_{p,N}(k)$ for the
$p$-component of the finite multiple zeta value of level $N$ with color map $c$. Then there are
rationals $q_1, \dots, q_n$, indices $k^{(1)}, \dots, k^{(n)}$ of positive integers, each of
weight $w$, and color maps $c_1, \dots, c_n$ of level $M$ (each $c_i$ from
$\mathbb{Z}/M\mathbb{Z}$ to $(\mathbb{Z}/M\mathbb{Z})^{r_i} \cup \{\varnothing\}$, where $r_i$
is the depth of $k^{(i)}$) such that for all sufficiently large primes $p$

$$
\zeta^{c}_{p,N}(k) = \sum_{i=1}^{n} q_i \, \zeta^{c_i}_{p,M}(k^{(i)}) \quad \text{in }
\mathbb{Z}/p\mathbb{Z},
$$

where a rational $q = a/b$ in lowest terms with $b > 0$ is read modulo $p$ as $a b^{-1}$.

## Sources

- Seki, *Regular Primes, Non-Wieferich Primes, and Finite Multiple Zeta Values of Level N*, INTEGERS 24 (2024), Article A22, Lemma 2.

Stated but not proved: `MetaMathlibExt.exists_finiteMZVColored_eq_sum_of_dvd` is written with `theorem_wanted` in [WantedExt/NumberTheory/FiniteMultipleZetaLevelWanted.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FiniteMultipleZetaLevelWanted.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/finite-multiple-zeta-values-of-level-n/index.html#exists-finite-mzvcolored-eq-sum-of-dvd).

## Criterion for a uniform bound on the least non-Wieferich base

The following are
equivalent:
(a) there is a natural number $M$ such that for every odd prime $p$ there is an integer $N$ with
$1 \le N \le M$, $p \nmid N$ and $p^2 \nmid N^{p-1} - 1$;
(b) there is a natural number $M \ge 3$ such that only finitely many primes $p$ satisfy
$p^2 \mid N^{p-1} - 1$ for every integer $N$ with $2 \le N \le M$.

For $p \nmid N$ the condition $p^2 \nmid N^{p-1} - 1$ says that $p$ does not divide the Fermat
quotient $q_p(N) = (N^{p-1} - 1)/p$, so (a) bounds, uniformly in $p$, the least such base $N$;
(b) says that $\bigcap_{N=2}^{M} W(N)$ is finite, where $W(N)$ is the set of primes $p$ with
$N^{p-1} \equiv 1 \pmod{p^2}$.

## Sources

- Seki, *Regular Primes, Non-Wieferich Primes, and Finite Multiple Zeta Values of Level N*, INTEGERS 24 (2024), Article A22, Lemma 3.

Stated but not proved: `MetaMathlibExt.exists_bound_fermatQuotient_iff_finite_iInter` is written with `theorem_wanted` in [WantedExt/NumberTheory/FiniteMultipleZetaLevelWanted.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FiniteMultipleZetaLevelWanted.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/finite-multiple-zeta-values-of-level-n/index.html#exists-bound-fermat-quotient-iff-finite).

## Criterion for a uniform bound on the least non-vanishing Bernoulli index

The following
are equivalent:
(a) there is a natural number $M$ such that for every prime $p \ge 5$ there is an odd integer
$k$ with $3 \le k \le M$, $k < p$ and $p \nmid \operatorname{num}(B_{p-k})$;
(b) there is a natural number $M \ge 5$ such that only finitely many primes $p$ satisfy $k < p$
and $p \mid \operatorname{num}(B_{p-k})$ for every odd integer $k$ with $3 \le k \le M$.

Here $B_n$ is the $n$-th Bernoulli number, with $B_1 = +1/2$ (only even indices $n \ge 2$ occur),
and $\operatorname{num}(B_n)$ is its numerator in lowest terms.

Condition (a) says that the least such $k$, the source's $g_p$, is bounded uniformly in $p$;
condition (b) says that $\bigcap_{3 \le k \le M,\ k \text{ odd}} I(k)$ is finite, where $I(k)$ is
the set of primes $p > k$ with $p \mid \operatorname{num}(B_{p-k})$.

## Sources

- Seki, *Regular Primes, Non-Wieferich Primes, and Finite Multiple Zeta Values of Level N*, INTEGERS 24 (2024), Article A22, Lemma 4.

Stated but not proved: `MetaMathlibExt.exists_bound_bernoulli_iff_finite_iInter` is written with `theorem_wanted` in [WantedExt/NumberTheory/FiniteMultipleZetaLevelWanted.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FiniteMultipleZetaLevelWanted.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/finite-multiple-zeta-values-of-level-n/index.html#exists-bound-bernoulli-iff-finite-i-inte).

## Regular and non-Wieferich primes give non-vanishing finite multiple zeta values

(i) Suppose that infinitely many odd primes $p$ are regular, in the sense that $p$ does not
divide the class number of any $p$-th cyclotomic field over $\mathbb{Q}$. Then for every
natural number $w \notin \{1, 2, 4\}$ there is an index $k = (k_1, \dots, k_r)$ of positive
integers with $k_1 + \dots + k_r = w$ such that
$\zeta_p(k) = \sum_{0 < m_1 < \dots < m_r < p} m_1^{-k_1} \cdots m_r^{-k_r}$ is non-zero in
$\mathbb{Z}/p\mathbb{Z}$ for infinitely many primes $p$.
(ii) Suppose that infinitely many primes are not Wieferich primes. Then for every even $N > 0$
and every natural number $w$ there are an index $k = (k_1, \dots, k_r)$ of positive integers with
$k_1 + \dots + k_r = w$ and a color map $c$ from $\mathbb{Z}/N\mathbb{Z}$ to
$(\mathbb{Z}/N\mathbb{Z})^r \cup \{\varnothing\}$ such that the $p$-component
$\zeta^{c}_{p,N}(k)$ of the finite multiple zeta value of level $N$ with color map $c$ is
non-zero in $\mathbb{Z}/p\mathbb{Z}$ for infinitely many primes $p$.

The weight $w = 0$ is allowed (the empty index has value $1$); the paper takes $w$ positive.

## Sources

- Seki, *Regular Primes, Non-Wieferich Primes, and Finite Multiple Zeta Values of Level N*, INTEGERS 24 (2024), Article A22, Proposition 2.

Stated but not proved: `MetaMathlibExt.exists_finiteMZV_ne_zero_of_conjectures` is written with `theorem_wanted` in [WantedExt/NumberTheory/FiniteMultipleZetaLevelWanted.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FiniteMultipleZetaLevelWanted.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/finite-multiple-zeta-values-of-level-n/index.html#exists-finite-mzv-ne-zero-of-conjectures).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Finite multiple zeta values of level N](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/finite-multiple-zeta-values-of-level-n/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/finite-multiple-zeta-values-of-level-n)
