---
declaration: theorem
origin: cited
lean: Erdos913.erdos_913, Erdos913.erdos_913.variants.infinite_many_8p_sq_add_one_primes, Erdos913.erdos_913.variants.conditional
statement: formalized
---

# Erdős Problem 913

> *Reference:* [erdosproblems.com/913](https://www.erdosproblems.com/913)
>
> Reviewed by @b-mehta on 2025-05-27

*Quoted from [FormalConjectures/ErdosProblems/913.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/913.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/913](https://www.erdosproblems.com/913).

The file states 3 research or textbook statements: 2 open and 1 solved.

## `Erdos913.erdos_913`

Open: stated without proof.

> Are there infinitely many $n$ such that if
>
> $$
>   n(n + 1) = \prod_i p_i^{k_i}
> $$
>
> is the factorisation into distinct primes then all exponents $k_i$ are distinct?

```lean
theorem erdos_913 :
    { n | Set.InjOn (n * (n + 1)).factorization (n * (n + 1)).primeFactors }.Infinite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/913.lean, line 40](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/913.lean#L40).

## `Erdos913.erdos_913.variants.infinite_many_8p_sq_add_one_primes`

Open: stated without proof.

> It is likely that there are infinitely many primes $p$ such that $8p^2 - 1$ is also prime.

```lean
theorem erdos_913.variants.infinite_many_8p_sq_add_one_primes :
    { p | p.Prime ∧ (8 * p ^ 2 - 1).Prime }.Infinite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/913.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/913.lean#L48).

## `Erdos913.erdos_913.variants.conditional`

Proved here.

> If there are infinitely many primes $p$ such that $8p^2 - 1$ is prime, then this is true.

```lean
theorem erdos_913.variants.conditional (h : { p | p.Prime ∧ (8 * p ^ 2 - 1).Prime }.Infinite) :
    { n | Set.InjOn (n * (n + 1)).factorization (n * (n + 1)).primeFactors }.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/913.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/913.lean#L54).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/913.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/913.lean)
- [erdosproblems.com/913](https://www.erdosproblems.com/913)
