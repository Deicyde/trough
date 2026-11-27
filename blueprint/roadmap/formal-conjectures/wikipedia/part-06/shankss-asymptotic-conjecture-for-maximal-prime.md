---
declaration: theorem
origin: cited
lean: MaximalPrimeGap.infinite_maximalPrimeGapIndex, MaximalPrimeGap.shanks_maximal_prime_gap_conjecture, MaximalPrimeGap.shanks_maximal_prime_gap_conjecture.variants.record_indices
statement: formalized
---

# Shanks's asymptotic conjecture for maximal prime gaps

> Writing $p_n$ for the $n$-th prime ($0$-indexed, $p_0 = 2$) and $g_n = p_{n+1} - p_n$ (`primeGap n`)
> for the $n$-th prime gap, let $G(x) = \max_{p_n < x} g_n$ (`sup_primeGap x`) denote the largest
> prime gap starting below $x$ (which has the same asymptotic growth as $\max_{p_n \le x} g_n$). An
> index $n$ marks a record (maximal) gap whenever $g_m < g_n$ for all $m < n$. Strengthening
> Cramér's prime-gap heuristic, Daniel Shanks (1964) conjectured that $G(x) \sim (\log x)^2$ as
> $x \to \infty$. By contrast, Andrew Granville's (1995) sieve-adjusted model predicts
> $\limsup_{n \to \infty} g_n / (\log p_n)^2 \ge 2e^{-\gamma} \approx 1.1229$, contradicting
> Shanks's conjecture. See also `Erdos5`.
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Cram%C3%A9r%27s_conjecture#Shanks_conjecture)
> - [Wikipedia: Prime gap](https://en.wikipedia.org/wiki/Prime_gap#Numerical_results)
> - D. Shanks, *On maximal gaps between successive primes*, Math. Comp. **18** (1964), no. 88,
>   646–651.
> - A. Granville, *Harald Cramér and the distribution of prime numbers*, Scand. Actuar. J. **1995**
>   (1995), no. 1, 12–28.

*Quoted from [FormalConjectures/Wikipedia/MaximalPrimeGap.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/MaximalPrimeGap.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 2 open and 1 textbook result. It also has 1 test statement and 1 API statement, counted here but not shown.

## `MaximalPrimeGap.infinite_maximalPrimeGapIndex`

Textbook result, stated without proof.

> Infinitely many indices $n$ achieve a new record prime gap, since prime gaps are unbounded.

```lean
theorem infinite_maximalPrimeGapIndex :
    {n : ℕ | IsMaximalPrimeGapIndex n}.Infinite
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/MaximalPrimeGap.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/MaximalPrimeGap.lean#L86).

## `MaximalPrimeGap.shanks_maximal_prime_gap_conjecture`

Open: stated without proof.

> Shanks's maximal prime gap conjecture (1964): the maximal prime gap $G(x)$ starting below $x$
> satisfies $G(x) \sim (\log x)^2$ as $x \to \infty$ (contradicted by Granville's refinement
> predicting $\limsup_{n \to \infty} g_n / (\log p_n)^2 \ge 2e^{-\gamma}$).

```lean
theorem shanks_maximal_prime_gap_conjecture :
    (fun x : ℝ => (sup_primeGap x : ℝ)) ~[Filter.atTop]
      (fun x : ℝ => (Real.log x) ^ 2)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/MaximalPrimeGap.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/MaximalPrimeGap.lean#L94).

## `MaximalPrimeGap.shanks_maximal_prime_gap_conjecture.variants.record_indices`

Open: stated without proof.

> Record-index consequence of Shanks's conjecture (derived as a corollary of
> `shanks_maximal_prime_gap_conjecture` rather than stated directly on Wikipedia): as $n$ runs
> through indices with `IsMaximalPrimeGapIndex n`, the ratio $g_n / (\log p_n)^2$ converges to
> $1$.

```lean
theorem shanks_maximal_prime_gap_conjecture.variants.record_indices :
    Filter.Tendsto
      (fun k : {n : ℕ // IsMaximalPrimeGapIndex n} =>
        (primeGap k.1 : ℝ) / (Real.log (Nat.nth Nat.Prime k.1 : ℝ)) ^ 2)
      Filter.atTop (nhds 1)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/MaximalPrimeGap.lean, line 104](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/MaximalPrimeGap.lean#L104).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/MaximalPrimeGap.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/MaximalPrimeGap.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Cram%C3%A9r%27s_conjecture#Shanks_conjecture)
