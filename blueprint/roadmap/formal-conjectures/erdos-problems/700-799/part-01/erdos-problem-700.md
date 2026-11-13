---
declaration: theorem
origin: cited
lean: Erdos700.erdos_700.parts.i, Erdos700.erdos_700.variants.prime_power_divisor, Erdos700.erdos_700.parts.ii, Erdos700.erdos_700.parts.iii, Erdos700.erdos_700.variants.prime_pow, Erdos700.erdos_700.variants.prime_mul
statement: formalized
---

# Erdős Problem 700

> *Reference:* [erdosproblems.com/700](https://www.erdosproblems.com/700)
>
> A problem of Erdős and Szekeres [ErSz78].
>
> *References:*
>  * [ErSz78] Erdős, P. and Szekeres, G., _Some number theoretic problems on binomial coefficients_,
>    Austral. Math. Soc. Gaz. (1978), 97-99.
>  * [OEIS A091963](https://oeis.org/A091963)
>  * Guy, R. K., _Unsolved Problems in Number Theory_, B31, B33.

*Quoted from [FormalConjectures/ErdosProblems/700.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/700.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/700](https://www.erdosproblems.com/700).

The file states 6 research or textbook statements: 4 open and 2 solved. It also has 1 test statement and 4 API statements, counted here but not shown.

## `Erdos700.erdos_700.parts.i`

Open: stated without proof.

> Let $f(n) = \min_{1 < k \le n/2} \gcd(n, \binom{n}{k})$ and let $P(n)$ be the largest prime
> dividing $n$.
>
> **(a)** Characterise those composite $n$ such that $f(n) = n/P(n)$.
>
> Erdős–Szekeres [ErSz78] note that $f(n) = n/P(n)$ when $n$ is a product of two primes
> (`erdos_700.variants.prime_mul`), with $n = 30$ a further example. The characterisation itself is
> open; we state it as the (unknown) set of all composite `n` with `f n = n / P n`.
>
> This follows the largest-prime reading on erdosproblems.com. In [ErSz78, p. 98], the first prose
> line below (7) reads: "where $P(n)$ is the greatest prime power which divides $n$."
> The paper's reading is stated with $Q(n)$ in `erdos_700.variants.prime_power_divisor`.

```lean
theorem erdos_700.parts.i :
    {n : ℕ | ¬ n.Prime ∧ 1 < n ∧ f n = n / P n} = erdos_700.parts.i.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/700.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/700.lean#L84).

## `Erdos700.erdos_700.variants.prime_power_divisor`

Open: stated without proof.

> Characterise those composite $n$ such that $f(n) = n/Q(n)$, where $Q(n)$ is the largest
> prime-power divisor of $n$. This is the reading of part (a) in Erdős–Szekeres
> [ErSz78, pp. 98–99](https://combinatorica.hu/~p_erdos/1978-46.pdf).

```lean
theorem erdos_700.variants.prime_power_divisor :
    {n : ℕ | ¬ n.Prime ∧ 1 < n ∧ f n = n / Q n} = erdos_700.variants.prime_power_divisor.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/700.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/700.lean#L94).

## `Erdos700.erdos_700.parts.ii`

Open: stated without proof.

> Let $f(n) = \min_{1 < k \le n/2} \gcd(n, \binom{n}{k})$.
>
> **(b)** Are there infinitely many composite $n$ such that $f(n) > n^{1/2}$?
>
> Erdős–Szekeres [ErSz78] could not prove this. (Since $f(n) \ge p(n)$, the least prime factor of
> $n$, there are infinitely many $n$ — those of the form $p^2$ — with $f(n) \ge n^{1/2}$; the
> question asks for the strict inequality.) Here $f(n) > n^{1/2}$ is written as `(f n) ^ 2 > n`.

```lean
theorem erdos_700.parts.ii :
    {n : ℕ | ¬ n.Prime ∧ 1 < n ∧ (f n) ^ 2 > n}.Infinite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/700.lean, line 121](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/700.lean#L121).

## `Erdos700.erdos_700.parts.iii`

Open: stated without proof.

> Let $f(n) = \min_{1 < k \le n/2} \gcd(n, \binom{n}{k})$.
>
> **(c)** Is it true that, for every composite $n$, $f(n) \ll_A n/(\log n)^A$ for every $A > 0$?
>
> Erdős–Szekeres [ErSz78] prove the weaker bound $f(n) \le (1 + o(1)) n/\log n$ (the case $A = 1$).
> Here $f(n) \ll_A n/(\log n)^A$ is spelled out as: for every `A > 0` there is a constant `C`
> (depending on `A`) with `f(n) ≤ C · n/(log n)^A` for every composite `n`.

```lean
theorem erdos_700.parts.iii :
    (∀ A : ℝ, 0 < A → ∃ C : ℝ, 0 < C ∧ ∀ n : ℕ, ¬ n.Prime → 1 < n →
      (f n : ℝ) ≤ C * (n : ℝ) / (Real.log n) ^ A)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/700.lean, line 133](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/700.lean#L133).

## `Erdos700.erdos_700.variants.prime_pow`

Proved here.

> `f(p^a) = p` for a prime `p` and `a ≥ 2` (recorded by Erdős–Szekeres [ErSz78]). In particular,
> since `(p^a) / P(p^a) = p^{a-1}`, the prime power `p^a` is a "hit" (`f(n) = n / P(n)`) if and only
> if `a = 2`.

```lean
theorem erdos_700.variants.prime_pow (p a : ℕ) (hp : p.Prime) (ha : 2 ≤ a) : f (p ^ a) = p
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/700.lean, line 159](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/700.lean#L159).

## `Erdos700.erdos_700.variants.prime_mul`

Proved here.

> `f(pq) = p` for distinct primes `p < q` (recorded by Erdős–Szekeres [ErSz78]); in particular
> `pq` is always a "hit" (`f(pq) = pq / P(pq) = p`). Proof via Lucas' theorem:
> `p ∤ C(pq,k) ⟹ p ∣ k` (and the same for `q`),
> so any `k` with `gcd(pq, C(pq,k)) = 1` must be a multiple of `pq`, of which there are none in
> `(1, pq/2]`; the witness `k = q` gives `gcd(pq, C(pq,q)) = p`.

```lean
theorem erdos_700.variants.prime_mul (p q : ℕ) (hp : p.Prime) (hq : q.Prime) (hpq : p < q) :
    f (p * q) = p
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/700.lean, line 215](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/700.lean#L215).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/700.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/700.lean)
- [erdosproblems.com/700](https://www.erdosproblems.com/700)
