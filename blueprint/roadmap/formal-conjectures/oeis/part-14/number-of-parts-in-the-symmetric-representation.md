---
declaration: theorem
origin: cited
lean: OeisA237271.conjecture_2, OeisA237271.conjecture_1, OeisA237271.a_odd_prime_pow, OeisA237271.conjecture_3, OeisA237271.conjecture_4, OeisA237271.conjecture_5, OeisA237271.observation_carmichael
statement: formalized
---

# Number of parts in the symmetric representation of $\sigma(n)$

> Number of parts in the symmetric representation of $\sigma(n)$. $a(n)$ is $1$ plus the number of pairs $(d_k, d_{k+1})$ of consecutive divisors of $n$
> such that $d_{k+1}$ is odd and $d_{k+1} \ge 2 d_k$.
>
> The formula used is
> $1 + |\{(d_k, d_{k+1}) \in \text{consecutive pairs of divisors of } n \mid
> d_{k+1} \text{ is odd and } d_{k+1} \ge 2 d_k\}|$,
> which is a known characterization of the sequence.
>
> *References:*
> - [A237271](https://oeis.org/A237271)
> - [arxiv/2605.22763](https://arxiv.org/abs/2605.22763) *Advancing Mathematics Research with AI-Driven Formal Proof Search* by George Tsoukalas et al.

*Quoted from [FormalConjectures/OEIS/237271.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/237271.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 7 research or textbook statements: 7 solved. It also has 5 test statements, counted here but not shown.

## `OeisA237271.conjecture_2`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/237271.wip.lean#L102](https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/237271.wip.lean#L102).

> Conjecture 2: "a(n) is the number of 2-dense sublists of divisors of n.
> We call '2-dense sublists of divisors of n' to the maximal sublists of divisors of n whose terms
> increase by a factor of at most 2." - _Omar E. Pol_, Jul 31 2025
>
> A formal proof has been found with the methods described in
> [arxiv/2605.22763](https://arxiv.org/abs/2605.22763).

```lean
theorem conjecture_2 (n : ℕ) : a n = num2DenseSublists n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/237271.lean, line 116](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/237271.lean#L116).

## `OeisA237271.conjecture_1`

Solved: stated here; a Lean proof is at [https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_OeisA237271_conjecture_1.lean#L211](https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_OeisA237271_conjecture_1.lean#L211).

> Conjecture 1 / Theorem: "a(n) is the number of odd divisors of n except the 'e' odd
> divisors described in A005279." - _Omar E. Pol_, Dec 21 2024.
> "The conjecture 1 is true. For a proof see A379288." - _Hartmut F. W. Hoft_, Jan 21 2025.
> Equivalently, $a(n) = \text{A001227}(n) - \text{A239657}(n)$. - _Omar E. Pol_, Mar 23 2014

```lean
theorem conjecture_1 (n : ℕ) (hn : 0 < n) :
    a n = A001227 n - A239657 n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/237271.lean, line 134](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/237271.lean#L134).

## `OeisA237271.a_odd_prime_pow`

Solved: stated here; a Lean proof is at [https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_OeisA237271_a_odd_prime_pow.lean#L165](https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_OeisA237271_a_odd_prime_pow.lean#L165).

> Theorem: "a(p^k) = k + 1, where p is an odd prime and k >= 0."
> - _Hartmut F. W. Hoft_, Dec 26 2016

```lean
theorem a_odd_prime_pow (p k : ℕ) (hp : p.Prime) (ho : Odd p) :
    a (p ^ k) = k + 1
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/237271.lean, line 144](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/237271.lean#L144).

## `OeisA237271.conjecture_3`

Proved here.

> Conjecture 3: "a(n) is the number of divisors p of n such that p is greater than
> twice the adjacent previous divisor of n. The divisors p give the n-th row of A379288."
> - _Omar E. Pol_, Aug 02 2025
>
> Note: this is equivalent to `a_eq_num2DenseSublists` (Conjecture 2), since the divisors that
> start a new 2-dense sublist are exactly those greater than twice their predecessor (plus the
> smallest divisor).

```lean
theorem conjecture_3 (n : ℕ) :
    a n = 1 + ((sortedDivisorsList n).zip (sortedDivisorsList n).tail).countP
      fun pair => pair.snd > 2 * pair.fst
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/237271.lean, line 158](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/237271.lean#L158).

## `OeisA237271.conjecture_4`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/oeis-a237271-square-hexagonal-parity/blob/430c09114d4ad3a3a2654b9816c8bfdc3cdf38de/lean/OeisA237271ParityFC.lean#L19-L24](https://github.com/KitaKen1/oeis-a237271-square-hexagonal-parity/blob/430c09114d4ad3a3a2654b9816c8bfdc3cdf38de/lean/OeisA237271ParityFC.lean#L19-L24).

> Conjecture 4: "a(A000290(n)) is odd." - _Omar E. Pol_, Oct 21 2025
>
> That is, the number of parts in the symmetric representation of $\sigma(n^2)$ is always odd.

```lean
theorem conjecture_4 (n : ℕ) (hn : 0 < n) : Odd (a (n ^ 2))
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/237271.lean, line 172](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/237271.lean#L172).

## `OeisA237271.conjecture_5`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/oeis-a237271-square-hexagonal-parity/blob/430c09114d4ad3a3a2654b9816c8bfdc3cdf38de/lean/OeisA237271ParityFC.lean#L26-L32](https://github.com/KitaKen1/oeis-a237271-square-hexagonal-parity/blob/430c09114d4ad3a3a2654b9816c8bfdc3cdf38de/lean/OeisA237271ParityFC.lean#L26-L32).

> Conjecture 5: "a(A000384(n)) is odd." - _Omar E. Pol_, Oct 21 2025
>
> That is, the number of parts in the symmetric representation of $\sigma(n(2n-1))$ is always odd,
> where $n(2n-1)$ is the $n$-th hexagonal number.

```lean
theorem conjecture_5 (n : ℕ) (hn : 0 < n) : Odd (a (n * (2 * n - 1)))
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/237271.lean, line 185](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/237271.lean#L185).

## `OeisA237271.observation_carmichael`

Solved: stated here; a Lean proof is at [https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_OeisA237271_observation_carmichael.lean#L260](https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_OeisA237271_observation_carmichael.lean#L260).

> Observation: "a(A002997(n)) >= 3, at least for 1 <= n <= 10000."
> - _Omar E. Pol_, Oct 21 2025
>
> That is, $a(k) \ge 3$ for every Carmichael number $k$.
> A002997 is the sequence of Carmichael numbers: the composite numbers $k$ such that
> $b^{k-1} \equiv 1 \pmod k$ for every $b$ coprime to $k$. This is `IsCarmichael`,
> which also forces $k$ to be composite.
>
> The observation holds for every odd composite $k$, so in particular for every Carmichael
> number. Write $p$ for the least prime factor of $k$ and $q = k/p$. The two smallest divisors
> of $k$ are $1$ and $p$, and the two largest are $q$ and $k$, so $(1, p)$ and $(q, k)$ are both
> consecutive pairs in the sorted divisor list, and they are distinct because $1 < q$. Both
> qualify: $p$ and $k$ are odd, $p \ge 2 \cdot 1$, and $k = pq \ge 3q > 2q$. Hence the count is
> at least $2$ and $a(k) \ge 3$. A Carmichael number is odd: it is composite by the $b = 1$ case
> of `IsCarmichael`, so $k > 2$, and if $k$ were even then the coprime base $k - 1 \equiv -1$
> would give $k \mid (-1)^{k-1} - 1 = -2$.

```lean
theorem observation_carmichael (k : ℕ) (hk : IsCarmichael k) :
    3 ≤ a k
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/237271.lean, line 208](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/237271.lean#L208).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/237271.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/237271.lean)
- [A237271](https://oeis.org/A237271)
