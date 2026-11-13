---
declaration: theorem
origin: cited
lean: Erdos890.erdos_890.parts.a, Erdos890.erdos_890.parts.b, Erdos890.erdos_890.variants.liminf_lower_bound, Erdos890.erdos_890.variants.omega_limsup
statement: formalized
---

# Erdős Problem 890

> *Reference:*
> - [erdosproblems.com/890](https://www.erdosproblems.com/890)
> - [ErSe67] Erdős, P. and Selfridge, J. L., Some problems on the prime factors of consecutive
>   integers. Illinois J. Math. (1967), 428--430.

*Quoted from [FormalConjectures/ErdosProblems/890.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/890.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/890](https://www.erdosproblems.com/890).

The file states 4 research or textbook statements: 2 open and 2 solved.

## `Erdos890.erdos_890.parts.a`

Open: stated without proof.

> If $\omega_k(n)$ counts the number of distinct prime factors of $n$ which are $>k$, then is it true
> that, for every $k\geq 1$,
>
> $$\liminf_{n\to \infty}\sum_{0\leq i < k}\omega_k(n+i)\leq k?$$

```lean
theorem erdos_890.parts.a :
    ∀ k ≥ 1, liminf (fun n ↦ (∑ i ∈ range k, (ω_gt k (n + i) : EReal))) atTop ≤ k
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/890.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/890.lean#L49).

## `Erdos890.erdos_890.parts.b`

Open: stated without proof.

> Is it true that
>
> $$\limsup_{n\to \infty}\left(\sum_{0\leq i < k}\omega(n+i)\right) \frac{\log\log n}{\log n}=1,$$
>
> where $\omega$ counts the number of distinct prime factors without restriction?

```lean
theorem erdos_890.parts.b :
    ∀ k ≥ 1, limsup (fun n ↦ (∑ i ∈ range k, (ω (n + i) : EReal)) *
      (log (log n) / log n)) atTop = 1
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/890.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/890.lean#L59).

## `Erdos890.erdos_890.variants.liminf_lower_bound`

Solved: stated here without proof.

> A question of Erdős and Selfridge [ErSe67], who observe that
> $\liminf_{n\to \infty}\sum_{0\leq i < k}\omega(n+i)\geq k+\pi(k)-1$ for every $k$. This follows from
> Pólya's theorem that the set of $k$-smooth integers has unbounded gaps - indeed,
> $n(n+1)\cdots (n+k-1)$ is divisible by all primes $\leq k$ and, provided $n$ is large, all but at
> most one of $n,n+1,\ldots,n+k-1$ has a prime factor $>k$ by Pólya's theorem.

```lean
theorem erdos_890.variants.liminf_lower_bound (k : ℕ) :
    liminf (fun n ↦ (∑ i ∈ range k, (ω (n + i) : EReal))) atTop ≥ k + π k - 1
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/890.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/890.lean#L72).

## `Erdos890.erdos_890.variants.omega_limsup`

Solved: stated here without proof.

> It is a classical fact that $\limsup_{n\to \infty}\omega(n)\frac{\log\log n}{\log n}=1.$

```lean
theorem erdos_890.variants.omega_limsup :
    limsup (fun n ↦ (ω n : EReal) * (log (log n) / log n)) atTop = 1
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/890.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/890.lean#L80).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/890.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/890.lean)
- [erdosproblems.com/890](https://www.erdosproblems.com/890)
