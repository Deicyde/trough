---
declaration: theorem
origin: cited
lean: Erdos6.erdos_6, Erdos6.erdos_6.variants.increasing, Erdos6.erdos_6.variants.decreasing
statement: formalized
---

# Erdős Problem 6

> *References:*
> - [erdosproblems.com/6](https://www.erdosproblems.com/6)
> - [BFT15] Banks, William D. and Freiberg, Tristan and Turnage-Butterbaugh, Caroline L., Consecutive primes in tuples. Acta Arith. (2015), 261-266.
> - [Ma15] Maynard, James, Small gaps between primes. Ann. of Math. (2) (2015), 383-413.

*Quoted from [FormalConjectures/ErdosProblems/6.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/6.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/6](https://www.erdosproblems.com/6).

The file states 3 research or textbook statements: 3 solved.

## `Erdos6.erdos_6`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos6.lean#L154](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos6.lean#L154).

> There are infinitely many $n$ such that $d_n < d_{n+1} < d_{n+2}$, where $d$
> denotes the prime gap function.

```lean
theorem erdos_6 :
    {n | primeGap n < primeGap (n + 1) ∧ primeGap (n + 1) < primeGap (n + 2)}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/6.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/6.lean#L39).

## `Erdos6.erdos_6.variants.increasing`

Solved: stated here without proof.

> For all $m$, there are infinitely many $n$ such that $d_n < d_{n+1} < \dots < d_{n+m}$,
> where $d$ denotes the prime gap function.
>
> Proved by Banks, Freiberg, and Turnage-Butterbaugh [BFT15] with an application of the
> Maynard-Tao machinery concerning bounded gaps between primes [Ma15]

```lean
theorem erdos_6.variants.increasing (m : ℕ) :
    {n | ∀ i ∈ Finset.range m, primeGap (n + i) < primeGap (n + i + 1)}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/6.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/6.lean#L51).

## `Erdos6.erdos_6.variants.decreasing`

Solved: stated here without proof.

> For all $m$, there are infinitely many $n$ such that $d_n > d_{n+1} > \dots > d_{n+m}$,
> where $d$ denotes the prime gap function.
>
> Proved by Banks, Freiberg, and Turnage-Butterbaugh [BFT15] with an application of the
> Maynard-Tao machinery concerning bounded gaps between primes [Ma15]

```lean
theorem erdos_6.variants.decreasing (m : ℕ) :
    {n | ∀ i ∈ Finset.range m, primeGap (n + i) > primeGap (n + i + 1)}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/6.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/6.lean#L64).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/6.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/6.lean)
- [erdosproblems.com/6](https://www.erdosproblems.com/6)
