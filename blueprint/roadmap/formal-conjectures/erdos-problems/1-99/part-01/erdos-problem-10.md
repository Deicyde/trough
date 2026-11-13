---
declaration: theorem
origin: cited
lean: Erdos10.erdos_10, Erdos10.erdos_10.variants.gallagher, Erdos10.erdos_10.variants.granville_soundararajan_odd, Erdos10.erdos_10.variants.grechuk_example, Erdos10.erdos_10.variants.two_pows, Erdos10.erdos_10.variants.grechuk
statement: formalized
---

# Erdős Problem 10

> *References:*
> - [erdosproblems.com/10](https://www.erdosproblems.com/10)
> - [Cr71] Crocker, R., On the sum of a prime and of two powers of two. Pacific J. Math. 36 (1971),
>   103-107.
> - [Ga75] Gallagher, P. X., Primes and powers of 2. Acta Arith. 29 (1976), 353-370.
> - [GrSo98] Granville, A. and Soundararajan, K., A binary additive problem of Erdős and the
>   order of $2$ mod $p^2$. Ramanujan J. 2 (1998), 283-298.

*Quoted from [FormalConjectures/ErdosProblems/10.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/10.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/10](https://www.erdosproblems.com/10).

The file states 6 research or textbook statements: 2 open and 4 solved. It also has 2 test statements, counted here but not shown.

## `Erdos10.erdos_10`

Open: stated without proof.

> Is there some $k$ such that every large integer is the sum of a prime and at most $k$
> powers of $2$?

```lean
theorem erdos_10 : ∃ k, ∀ᶠ n : ℕ in atTop, n ∈ sumPrimeAndTwoPows k
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/10.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/10.lean#L63).

## `Erdos10.erdos_10.variants.gallagher`

Solved: stated here without proof.

> Gallagher [Ga75] has shown that for any $ϵ > 0$ there exists $k(ϵ)$
> such that the set of integers which are the sum of a prime and at most $k(ϵ)$
> many powers of $2$ has lower density at least $1 - ϵ$.
>
> Ref: Gallagher, P. X., _Primes and powers of 2_.

```lean
theorem erdos_10.variants.gallagher (ε : ℝ)
    (hε : 0 < ε) : ∃ k, 1 - ε ≤ (sumPrimeAndTwoPows k).lowerDensity
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/10.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/10.lean#L74).

## `Erdos10.erdos_10.variants.granville_soundararajan_odd`

Open: stated without proof.

> Granville and Soundararajan [GrSo98] have conjectured that at most $3$
> powers of $2$ suffice for all odd integers, and hence at most $4$ powers of $2$
> suffice for all even integers.
>
> Ref: Granville, A. and Soundararajan, K., _A Binary Additive Problem of Erdős and the Order of $2$ mod $p^2$_

```lean
theorem erdos_10.variants.granville_soundararajan_odd :
    {n : ℕ | Odd n ∧ 1 < n} ⊆ sumPrimeAndTwoPows 3 ∧
      {n : ℕ | Even n ∧ n ≠ 0} ⊆ sumPrimeAndTwoPows 4
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/10.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/10.lean#L86).

## `Erdos10.erdos_10.variants.grechuk_example`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/bed1ae569eaac7109327f644fa149b902b562873/erdos-10/Solution.lean#L36](https://github.com/linrock/math-proofs/blob/bed1ae569eaac7109327f644fa149b902b562873/erdos-10/Solution.lean#L36).

> Bogdan Grechuk has observed that `1117175146` is not the sum of a prime
> and at most $3$ powers of $2$.

```lean
theorem erdos_10.variants.grechuk_example :
    1117175146 ∉ sumPrimeAndTwoPows 3
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/10.lean, line 98](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/10.lean#L98).

## `Erdos10.erdos_10.variants.two_pows`

Solved: stated here; a Lean proof is at [https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_Erdos10_erdos_10_variants_two_pows.lean#L340](https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_Erdos10_erdos_10_variants_two_pows.lean#L340).

> There are infinitely many even integers not the sum of a prime and $2$ powers of $2$

```lean
theorem erdos_10.variants.two_pows :
    Set.Infinite <| {n : ℕ | Even n} \ sumPrimeAndTwoPows 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/10.lean, line 107](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/10.lean#L107).

## `Erdos10.erdos_10.variants.grechuk`

Solved: stated here; a Lean proof is at [https://gist.github.com/DaryxXx/e112c74cc648b08a420b0959315cf65f/4b347897ff1811f1db1d82594c581f54b8f31b7d#file-main-lean-L2287](https://gist.github.com/DaryxXx/e112c74cc648b08a420b0959315cf65f/4b347897ff1811f1db1d82594c581f54b8f31b7d#file-main-lean-L2287).

> Bogdan Grechuk has observed that $1117175146$ is not the sum of a prime and at most $3$
> powers of $2$, and pointed out that parity considerations, coupled with the fact that there
> are many integers not the sum of a prime and $2$ powers of $2$ suggest that there exist
> infinitely many even integers which are not the sum of a prime and at most $3$ powers of $2$.
>
> This follows from Crocker's construction [Cr71] of infinitely many odd $t \equiv 15 \pmod{16}$
> which are not the sum of a prime and $2$ powers of $2$: each such $t + 1$ is even and not the
> sum of a prime and at most $3$ powers of $2$.
>
> The linked Lean formalisation is by Daryxx, see comment section.

```lean
theorem erdos_10.variants.grechuk :
    Set.Infinite <| {n : ℕ | Even n} \ sumPrimeAndTwoPows 3
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/10.lean, line 126](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/10.lean#L126).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/10.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/10.lean)
- [erdosproblems.com/10](https://www.erdosproblems.com/10)
