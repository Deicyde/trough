---
declaration: section
origin: cited
lean: MetaMathlibExt.prime_eq_of_dvd_sub_one_of_dvd_cyclotomic_eval, MetaMathlibExt.prime_dvd_pow_self_sub_one_iff, MetaMathlibExt.prime_eq_of_dvd_sub_one_of_dvd_cyclotomic_eval_pow, MetaMathlibExt.prime_dvd_pow_sub_one_iff_cyclotomic, MetaMathlibExt.prime_modEq_one_of_dvd_cyclotomic_eval, MetaMathlibExt.hybrid_bound_prime_divisors, MetaMathlibExt.prime_hybrid_bound, MetaMathlibExt.two_pow_ramified_bound
statement: formalized
---

# Prime divisor bounds for cyclotomic values

21 results, 21 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/prime-divisor-bounds-for-cyclotomic-values/index.html).

## A common prime divisor of $x - 1$ and $\Phi_p(x)$ is $p$

Let $\rho$ and $p$ be primes,
let $x$ be a positive integer, and let $\Phi_p$ be the $p$-th cyclotomic polynomial with integer
coefficients. If $\rho \mid x - 1$ and $\rho \mid \Phi_p(x)$, then $\rho = p$.

## Sources

- Gustav Kjærbye Bagger, *Hybrid Bounds for Prime Divisors*, INTEGERS 26 (2026), Article A95, Lemma 1.

Stated but not proved: `MetaMathlibExt.prime_eq_of_dvd_sub_one_of_dvd_cyclotomic_eval` is written with `theorem_wanted` in [WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/prime-divisor-bounds-for-cyclotomic-values/index.html#prime-eq-of-dvd-sub-one-of-dvd-cyclotomi).

## Divisibility of $x^p - 1$ by $p$

Let $p$ be a prime, let $x$ be a positive integer, and
let $\Phi_p$ be the $p$-th cyclotomic polynomial with integer coefficients. Then
$p \mid x^p - 1$ if and only if $p \mid x - 1$ and $p \mid \Phi_p(x)$.

## Sources

- Gustav Kjærbye Bagger, *Hybrid Bounds for Prime Divisors*, INTEGERS 26 (2026), Article A95, Lemma 2.

Stated but not proved: `MetaMathlibExt.prime_dvd_pow_self_sub_one_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/prime-divisor-bounds-for-cyclotomic-values/index.html#prime-dvd-pow-self-sub-one-iff).

## A common prime divisor of $y - 1$ and $\Phi_p(y^{p^{a-1}})$ is $p$

Let $\rho$ and $p$ be
primes, let $a \ge 1$ be a natural number, let $y$ be a positive integer, and let $\Phi_p$ be the
$p$-th cyclotomic polynomial with integer coefficients. If $\rho \mid y - 1$ and
$\rho \mid \Phi_p(y^{p^{a-1}})$, then $\rho = p$.

## Sources

- Gustav Kjærbye Bagger, *Hybrid Bounds for Prime Divisors*, INTEGERS 26 (2026), Article A95, Lemma 3.

Stated but not proved: `MetaMathlibExt.prime_eq_of_dvd_sub_one_of_dvd_cyclotomic_eval_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/prime-divisor-bounds-for-cyclotomic-values/index.html#prime-eq-of-dvd-sub-one-of-dvd-cyclotomi-2).

## Divisibility of $x^{rp^a} - 1$ by $p$

Let $p$ be a prime, let $r$ and $a$ be natural
numbers with $r$ coprime to $p$, let $x$ be a positive integer, and let $\Phi_p$ be the $p$-th
cyclotomic polynomial with integer coefficients. Then $p \mid x^{rp^a} - 1$ if and only if
$p \mid x^r - 1$ and $p \mid \Phi_p(x^{rp^{i-1}})$ for every $i \in \{1, \dots, a\}$.

## Sources

- Gustav Kjærbye Bagger, *Hybrid Bounds for Prime Divisors*, INTEGERS 26 (2026), Article A95, Lemma 4.

Stated but not proved: `MetaMathlibExt.prime_dvd_pow_sub_one_iff_cyclotomic` is written with `theorem_wanted` in [WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/prime-divisor-bounds-for-cyclotomic-values/index.html#prime-dvd-pow-sub-one-iff-cyclotomic).

## Prime divisors of $\Phi_p(x)$ other than $p$ are $1$ modulo $p$

Let $\rho$ and $p$ be
distinct primes, let $x$ be a positive integer, and let $\Phi_p$ be the $p$-th cyclotomic
polynomial with integer coefficients. If $\rho \mid \Phi_p(x)$, then $\rho \equiv 1 \pmod p$.

## Sources

- Gustav Kjærbye Bagger, *Hybrid Bounds for Prime Divisors*, INTEGERS 26 (2026), Article A95, Proposition 1.

Stated but not proved: `MetaMathlibExt.prime_modEq_one_of_dvd_cyclotomic_eval` is written with `theorem_wanted` in [WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/prime-divisor-bounds-for-cyclotomic-values/index.html#prime-mod-eq-one-of-dvd-cyclotomic-eval).

## Hybrid bound for prime divisors of $x^n - 1$

The hybrid bound. Let `n = ∏_{i=1}^m p_i^{a_i}` with distinct primes `p_i` (in any order),
`x > 1`, and `ω_n = ω(x^n - 1)`. With `p_0 := 1`, let
`Π^j = {ρ prime : ρ ≡ 1 (mod p_j), ρ ≢ 1 (mod p_s) for j < s ≤ m}` and `r_{i,j}` its `i`-th
element (`Nat.nth`, `0`-indexed here). The source's
`x ≥ min_{k_0 + ⋯ + k_m = ω_n} max_{0 ≤ t ≤ m} (1 + ∏_{j ≤ t} ∏_{i ≤ k_j} r_{i,j})^{T(t)}` with
`T(t) = ∏_{s=1}^t p_s^{-a_s}` is stated equivalently, after raising to the power
`∏_{s ≤ t} p_s^{a_s}`, as the existence of a composition `k` meeting every bound. The parts `k_j`
range over `ℕ` (the source writes `k_i ∈ ℤ⁺`; with positive parts the claim fails for
`n = 3`, `x = 2`, where `x^3 - 1 = 7` and `ω_n = 1` admits no positive composition into two
parts).

## Sources

- Gustav Kjærbye Bagger, *Hybrid Bounds for Prime Divisors*, INTEGERS 26 (2026), Article A95, Theorem 1.

Stated but not proved: `MetaMathlibExt.hybrid_bound_prime_divisors` is written with `theorem_wanted` in [WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/prime-divisor-bounds-for-cyclotomic-values/index.html#hybrid-bound-prime-divisors).

## Hybrid bound for prime divisors of $x^p - 1$

The `p`-hybrid bound (Theorem 1 for prime `n = p`). For a prime `p`, `x > 1` and
`ω_p = ω(x^p - 1)`, let `r_{i,0}` and `r_{j,1}` enumerate the primes `≢ 1` and `≡ 1 (mod p)`
(`Nat.nth`, `0`-indexed here). The source's
`x ≥ min_{0 ≤ k < ω_p} max(1 + ∏_{i ≤ k} r_{i,0}, (1 + ∏_{i ≤ k} r_{i,0} ∏_{j ≤ ω_p - k} r_{j,1})^{1/p})`
is stated equivalently as the existence of `k < ω_p` meeting both bounds, the second after
raising to the `p`-th power.

## Sources

- Gustav Kjærbye Bagger, *Hybrid Bounds for Prime Divisors*, INTEGERS 26 (2026), Article A95, Proposition 2.

Stated but not proved: `MetaMathlibExt.prime_hybrid_bound` is written with `theorem_wanted` in [WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/prime-divisor-bounds-for-cyclotomic-values/index.html#prime-hybrid-bound).

## The ramified bound for $n = 2^a$

Let $a \ge 1$, let $n = 2^a$, let $x > 1$ be a natural
number, let $\omega_n$ be the number of distinct prime factors of $x^n - 1$, and let
$s_1 = 2 < s_2 = 3 < s_3 = 5 < \cdots$ be the primes in increasing order. Then

$$\min\Bigl(1 + 2n \prod_{i=1}^{\omega_n} s_i,\ 1 + \prod_{i=2}^{\omega_n + 1} s_i\Bigr) \le x^n.$$

Equivalently, $x$ is at least the smaller of the $n$-th roots of these two numbers, which is the
form of the source. The source admits every positive integer $x$; at $x = 1$ the number
$x^n - 1 = 0$ has an empty prime factorization, so $\omega_n = 0$ and the bound would read
$2 \le 1$.

## Sources

- Gustav Kjærbye Bagger, *Hybrid Bounds for Prime Divisors*, INTEGERS 26 (2026), Article A95, Theorem 3.

Stated but not proved: `MetaMathlibExt.two_pow_ramified_bound` is written with `theorem_wanted` in [WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/prime-divisor-bounds-for-cyclotomic-values/index.html#two-pow-ramified-bound).

## A weaker ramified bound for $n = 2^a$

Let $a \ge 1$, let $n = 2^a$, let $x > 1$ be a
natural number, let $\omega_n$ be the number of distinct prime factors of $x^n - 1$, and let
$s_1 = 2 < s_2 = 3 < s_3 = 5 < \cdots$ be the primes in increasing order. Then

$$\min\Bigl(1 + n \prod_{i=1}^{\omega_n} s_i,\ 1 + \prod_{i=2}^{\omega_n + 1} s_i\Bigr) \le x^n.$$

This weakens the ramified bound for $n = 2^a$, which has the factor $2n$ in place of $n$. The
extracted text of the source reads $n = 2a$; its own discussion ($n = 4$, "extends to $n = 2^a$")
shows that $n = 2^a$ is meant. As in the stronger bound, $x > 1$ replaces the source's positive
integer $x$.

## Sources

- Gustav Kjærbye Bagger, *Hybrid Bounds for Prime Divisors*, INTEGERS 26 (2026), Article A95, Corollary 1.

Stated but not proved: `MetaMathlibExt.two_pow_trivial_ramified_bound` is written with `theorem_wanted` in [WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/prime-divisor-bounds-for-cyclotomic-values/index.html#two-pow-trivial-ramified-bound).

## Primorials below powers of sixteen

For every positive integer $w$, we have $w < 16$ if and
only if the product $p_1 p_2 \cdots p_w$ of the first $w$ primes is less than $16^w$.

## Sources

- Gustav Kjærbye Bagger, *Hybrid Bounds for Prime Divisors*, INTEGERS 26 (2026), Article A95, Proposition 10.

Stated but not proved: `MetaMathlibExt.lt_sixteen_iff_prod_first_primes_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/prime-divisor-bounds-for-cyclotomic-values/index.html#lt-sixteen-iff-prod-first-primes-lt).

## Ramified bound on the number of prime divisors of $x^n - 1$

The ramified bound. Let `n = ∏_{i=1}^m p_i^{a_i}` with primes `p_1 < ⋯ < p_m` (the ordering
the source fixes at the start of its Section 5), `x > 1`, `ω_n = ω(x^n - 1)`, and, with
`p_0 := 1`, let `r_{i,j}` be the `i`-th element (`Nat.nth`, `0`-indexed here) of
`Π^j = {ρ prime : ρ ≡ 1 (mod p_j), ρ ≢ 1 (mod p_s) for j < s ≤ m}`. Fix a prime factor `p_α` of
`n` and write `p_α = r_{b,τ}` with `τ ≤ m`. As in `hybrid_bound_prime_divisors`, the source's
`x ≥ min_{k_0 + ⋯ + k_m = ω_n} max_t (1 + ∏_{j ≤ t} δ_α(j) ∏_{i ≤ k_j} r_{i,j})^{T(t)}` is stated
as the existence of a composition `k` (parts in `ℕ`, not `ℤ⁺`) meeting every bound after raising
to the power `∏_{s ≤ t} p_s^{a_s}`. The factors `δ_α(j)` are applied to the block products: if
`p_α ∣ x^n - 1`, block `τ` with `k_τ < b` (`1`-indexed in the source, `k_τ ≤ b` here) has its
largest factor `r_{k_τ,τ}` replaced by `p_α`, and block `α` gains the factor `p_α^{a_α}`; if
`p_α ∤ x^n - 1`, block `τ` with `k_τ ≥ b` drops `p_α` and takes the next element instead. In
the divisible case the composition also has `k_τ > 0` (the source's `δ_α(τ)` is undefined at
`k_τ = 0`). The source's worked example (`n = 3`, `ω_3 = 10`: `x ≥ 4387` if `3 ∣ x^3 - 1`,
`x ≥ 5423` otherwise) is reproduced exactly by this reading. Definitions follow the arXiv version
(arXiv:2412.00010), whose statement matches the journal record.

## Sources

- Gustav Kjærbye Bagger, *Hybrid Bounds for Prime Divisors*, INTEGERS 26 (2026), Article A95, Theorem 2.

Stated but not proved: `MetaMathlibExt.ramified_bound_prime_divisors` is written with `theorem_wanted` in [WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/prime-divisor-bounds-for-cyclotomic-values/index.html#ramified-bound-prime-divisors).

## Ramified bound on prime divisors of $x^p - 1$ for prime $p$

The `p`-ramified bound (Theorem 2 for prime `n = p`). For a prime `p`, `x > 1` and
`ω_p = ω(x^p - 1)`, let `r_{i,0}` and `r_{j,1}` enumerate the primes `≢ 1` and `≡ 1 (mod p)`
(`Nat.nth`, `0`-indexed here), `p = r_{b,0}`, `R^0_k = ∏_{i < k} r_{i,0}` and
`R^1_k = ∏_{j < ω_p - k} r_{j,1}`. The source's minima over `k ∈ [0, k') ∪ [k', ω_p)` (with
`k' = b + 1`) are stated as the existence of `k < ω_p` meeting both bounds, the second after
raising to the `p`-th power; `p^{-1} R^0_{k+1}` is written as the product over
`{0, …, k} \ {b}`. If `p ∤ x^p - 1`: `k ≤ b` gives `1 + R^0_k ≤ x`, `1 + R^0_k R^1_k ≤ x^p`, and
`k > b` gives `1 + p^{-1} R^0_{k+1} ≤ x`, `1 + p^{-1} R^0_{k+1} R^1_k ≤ x^p`. If `p ∣ x^p - 1`:
`k ≤ b` gives `1 + p R^0_{k-1} ≤ x`, `1 + p^2 R^0_{k-1} R^1_k ≤ x^p`, and `k > b` gives
`1 + R^0_k ≤ x`, `1 + p R^0_k R^1_k ≤ x^p`. The divisible case requires `p ≠ 2` and has `k > 0`:
`R^0_{-1}` is undefined at `k = 0`, and for `p = 2`, `x = 3` (`x^2 - 1 = 8`, `ω_2 = 1`) the only
admitted `k = 0` fails under any reading (with `R^0_{-1} := 1` the second bound reads
`1 + 4 · 3 = 13 ≤ 9`).

## Sources

- Gustav Kjærbye Bagger, *Hybrid Bounds for Prime Divisors*, INTEGERS 26 (2026), Article A95, Proposition 3.

Stated but not proved: `MetaMathlibExt.prime_ramified_bound` is written with `theorem_wanted` in [WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/prime-divisor-bounds-for-cyclotomic-values/index.html#prime-ramified-bound).

## Factorization into composed cyclotomic polynomials

Let $x$ be the indeterminate of the
polynomial ring $\mathbb{Z}[x]$. Let $m$ be a natural number, let $p_1, \dots, p_m$ be primes,
not necessarily distinct, let $a_1, \dots, a_m$ be natural numbers, and put
$n = \prod_{i=1}^m p_i^{a_i}$. For $1 \le i \le m$ let $x_i = x^{N_i}$ with
$N_i = \prod_{1 \le r < i} p_r^{a_r}$. Then

$$x^n - 1 = (x - 1) \prod_{i=1}^m \prod_{j=1}^{a_i} \Phi_{p_i}(x_i^{p_i^{j-1}}),$$

where $\Phi_p$ is the $p$-th cyclotomic polynomial over $\mathbb{Z}$ and $\Phi_{p_i}(\cdot)$
denotes composition of polynomials.

The source takes the prime factorization of $n$; the identity needs only that each $p_i$ is
prime. The definition of $x_i$ follows the arXiv version of the source (arXiv:2412.00010),
which the journal statement refers to as "$x_k$ as above".

## Sources

- Gustav Kjærbye Bagger, *Hybrid Bounds for Prime Divisors*, INTEGERS 26 (2026), Article A95, Proposition 4.

Stated but not proved: `MetaMathlibExt.X_pow_sub_one_eq_mul_prod_cyclotomic_comp` is written with `theorem_wanted` in [WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/prime-divisor-bounds-for-cyclotomic-values/index.html#x-pow-sub-one-eq-mul-prod-cyclotomic-com).

## Cohen's prime sieve for the line problem

Let $q$ and $n$ be natural numbers, let $\omega$
be the number of distinct prime factors of $q^n - 1$, and let $S$ be a set of $s$ prime factors of
$q^n - 1$ with $\delta = 1 - \sum_{\rho \in S} 1/\rho > 0$. Suppose that
$q > (n - 1)^2 \, 2^{2(\omega - s)} \left(\frac{s - 1}{\delta} + 2\right)^2$. Then for all finite
fields $K$ and $L$ with $L$ an extension of $K$, $|K| = q$ and $[L : K] = n$, and all nonzero
$\gamma_1, \gamma_2 \in L$ with $K(\gamma_1/\gamma_2) = L$, there is $a \in K$ such that
$a\gamma_2 + \gamma_1$ generates the multiplicative group $L^\times$.

## Sources

- Gustav Kjærbye Bagger, *Hybrid Bounds for Prime Divisors*, INTEGERS 26 (2026), Article A95, Proposition 5, quoting S. D. Cohen, Proposition 4.3.

Stated but not proved: `MetaMathlibExt.mem_lineProblem_of_prime_sieve` is written with `theorem_wanted` in [WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/prime-divisor-bounds-for-cyclotomic-values/index.html#mem-line-problem-of-prime-sieve).

## Cohen's modified prime sieve for the line problem

Let $q$ and $n$ be natural numbers such
that $q^n - 1$ has $\omega \ge 2$ distinct prime factors. Let $S$ be a set of $s$ prime factors of
$q^n - 1$, let $l$ be a prime factor of $q^n - 1$ not in $S$, let $k$ be the product of the prime
factors of $q^n - 1$ that are neither $l$ nor in $S$, and put
$\delta = 1 - \sum_{\rho \in S} 1/\rho$. Suppose that $\delta > 1/(l\varphi(k))$, where $\varphi$ is
Euler's totient function, and

$$
q > (n - 1)^2 \left(\frac{2^{\omega - s - 1} \varphi(k) (s - 1 + 2\delta) + 1 - 1/l}
{\varphi(k)\delta - 1/l} - 1\right)^2.
$$

Then for all finite fields $K$ and $L$ with $L$ an extension of $K$, $|K| = q$ and $[L : K] = n$,
and all nonzero $\gamma_1, \gamma_2 \in L$ with $K(\gamma_1/\gamma_2) = L$, there is $a \in K$
such that $a\gamma_2 + \gamma_1$ generates the multiplicative group $L^\times$.

## Sources

- Gustav Kjærbye Bagger, *Hybrid Bounds for Prime Divisors*, INTEGERS 26 (2026), Article A95, Proposition 6, quoting S. D. Cohen, Proposition 6.3.

Stated but not proved: `MetaMathlibExt.mem_lineProblem_of_modified_prime_sieve` is written with `theorem_wanted` in [WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/prime-divisor-bounds-for-cyclotomic-values/index.html#mem-line-problem-of-modified-prime-sieve).

## General prime sieve for the line problem

Let $q$ and $n$ be natural numbers, let $\omega$
be the number of distinct prime factors of $q^n - 1$, and let $S$ and $T$ be disjoint sets of prime
factors of $q^n - 1$, with $s = |S|$ and $r = |T|$. Let $k$ be the product of the prime factors of
$q^n - 1$ that lie in neither $S$ nor $T$, and put $\delta = 1 - \sum_{\rho \in S} 1/\rho$,
$\varepsilon = \sum_{l \in T} 1/l$ and $\mu = \varphi(k)/k$, where $\varphi$ is Euler's totient
function. Suppose that $\delta\mu > \varepsilon$ and

$$
q > (n - 1)^2 \left(\frac{2^{\omega - s - r} \mu (s - 1 + 2\delta) - \delta\mu + r -
\varepsilon}{\delta\mu - \varepsilon}\right)^2.
$$

Then for all finite fields $K$ and $L$ with $L$ an extension of $K$, $|K| = q$ and $[L : K] = n$,
and all nonzero $\gamma_1, \gamma_2 \in L$ with $K(\gamma_1/\gamma_2) = L$, there is $a \in K$
such that $a\gamma_2 + \gamma_1$ generates the multiplicative group $L^\times$.

## Sources

- Gustav Kjærbye Bagger, *Hybrid Bounds for Prime Divisors*, INTEGERS 26 (2026), Article A95, Proposition 7, quoting Bailey, Cohen, Sutherland and Trudgian, Lemma 1.

Stated but not proved: `MetaMathlibExt.mem_lineProblem_of_general_prime_sieve` is written with `theorem_wanted` in [WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/prime-divisor-bounds-for-cyclotomic-values/index.html#mem-line-problem-of-general-prime-sieve).

## The line problem for quintic extensions

Let $E_5$ be the set of $647$ prime powers listed
in the appendix of arXiv:2412.00010, the smallest being $2$ and the largest $62791$. Let $q$ be a
natural number not in $E_5$. Then for all finite fields $K$ and $L$ with $L$ an extension of $K$,
$|K| = q$ and $[L : K] = 5$, and all nonzero $\gamma_1, \gamma_2 \in L$ with
$K(\gamma_1/\gamma_2) = L$, there is $a \in K$ such that $a\gamma_2 + \gamma_1$ generates the
multiplicative group $L^\times$.

## Sources

- Gustav Kjærbye Bagger, *Hybrid Bounds for Prime Divisors*, INTEGERS 26 (2026), Article A95, Proposition 8.

Stated but not proved: `MetaMathlibExt.mem_lineProblem_five` is written with `theorem_wanted` in [WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/prime-divisor-bounds-for-cyclotomic-values/index.html#mem-line-problem-five).

## Liao–Li–Pu criterion for primitive element sums

Let $q$ and $n$ be coprime natural numbers
with $q^n > 2$, and let $\omega$ be the number of distinct prime factors of $q^n - 1$. If
$16^\omega < q^n$, that is $q^{n/2} > 2^{2\omega}$, then every finite field $L$ with $q^n$ elements
contains an element $\alpha$ such that both $\alpha$ and $\alpha + \alpha^{-1}$ generate the
multiplicative group $L^\times$.

The hypothesis $q^n > 2$ is added to the source's statement: for $q = 2$ and $n = 1$ the inequality
$16^0 < 2$ holds, but the only generator of $\mathbb{F}_2^\times$ is $1$, and $1 + 1^{-1} = 0$.

## Sources

- Gustav Kjærbye Bagger, *Hybrid Bounds for Prime Divisors*, INTEGERS 26 (2026), Article A95, Proposition 9, quoting Liao, Li and Pu, Theorem 1.3.

Stated but not proved: `MetaMathlibExt.mem_primitiveSum_of_sixteen_pow_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean, line 380](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean#L380). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/prime-divisor-bounds-for-cyclotomic-values/index.html#mem-primitive-sum-of-sixteen-pow-lt).

## Finite fields with a primitive element sum

For every natural number $q$, we have
$q \notin \{2, 3, 4, 5, 7, 9, 13, 25, 121\}$ if and only if every finite field $L$ with $q$
elements contains an element $\alpha$ such that both $\alpha$ and $\alpha + \alpha^{-1}$ generate
the multiplicative group $L^\times$.

## Sources

- Gustav Kjærbye Bagger, *Hybrid Bounds for Prime Divisors*, INTEGERS 26 (2026), Article A95, Proposition 11, quoting Cohen, Oliveira e Silva, Sutherland and Trudgian, Corollary 2.

Stated but not proved: `MetaMathlibExt.mem_primitiveSum_one_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean, line 393](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean#L393). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/prime-divisor-bounds-for-cyclotomic-values/index.html#mem-primitive-sum-one-iff).

## Primitive element sums away from exceptional pairs

Let $q$ and $n > 1$ be coprime natural
numbers, and let $\omega$ be the number of distinct prime factors of $q^n - 1$. Suppose that the
pair $(n, \omega)$ is none of the following $33$ pairs: $(2, w)$ for $1 \le w \le 11$; $(3, w)$ for
$2 \le w \le 7$; $(4, w)$ for $w \in \{2, 3, 4, 5, 6, 7, 9\}$; $(5, 3)$ and $(5, 5)$; $(6, w)$ for
$3 \le w \le 6$; $(8, 4)$ and $(8, 6)$; and $(12, 6)$. Then every finite field $L$ with $q^n$
elements contains an element $\alpha$ such that both $\alpha$ and $\alpha + \alpha^{-1}$ generate
the multiplicative group $L^\times$.

The hypotheses $n > 1$ and $\gcd(q, n) = 1$ are added. For $n = 1$ and $q = 2$ the pair $(1, 0)$
is not exceptional, yet $\mathbb{F}_2$ has no such $\alpha$; and the source derives the result from
the Liao–Li–Pu criterion, which assumes coprimality.

## Sources

- Gustav Kjærbye Bagger, *Hybrid Bounds for Prime Divisors*, INTEGERS 26 (2026), Article A95, Proposition 12.

Stated but not proved: `MetaMathlibExt.mem_primitiveSum_of_not_mem_exceptional` is written with `theorem_wanted` in [WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/prime-divisor-bounds-for-cyclotomic-values/index.html#mem-primitive-sum-of-not-mem-exceptional).

## Fields without primitive element sums have few prime factors

Let $q$ and $n$ be natural
numbers with $\gcd(q, n) = 1$. If it is not the case that every finite field $L$ with $q^n$
elements contains an element $\alpha$ such that both $\alpha$ and $\alpha + \alpha^{-1}$ generate
the multiplicative group $L^\times$, then $q^n - 1$ has at most $15$ distinct prime factors.

The hypothesis $\gcd(q, n) = 1$ is added: the source derives the bound from the Liao–Li–Pu
criterion, which assumes it.

## Sources

- Gustav Kjærbye Bagger, *Hybrid Bounds for Prime Divisors*, INTEGERS 26 (2026), Article A95, Corollary 2.

Stated but not proved: `MetaMathlibExt.card_primeFactors_le_fifteen_of_not_mem_primitiveSum` is written with `theorem_wanted` in [WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean, line 425](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HybridPrimeDivisorBoundsWanted.lean#L425). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/prime-divisor-bounds-for-cyclotomic-values/index.html#card-prime-factors-le-fifteen-of-not-mem).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Prime divisor bounds for cyclotomic values](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/prime-divisor-bounds-for-cyclotomic-values/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/prime-divisor-bounds-for-cyclotomic-values)
