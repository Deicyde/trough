---
declaration: theorem
origin: cited
lean: EulerSumOfPowers.eulers_sum_of_powers_conjecture, EulerSumOfPowers.eulers_sum_of_powers_conjecture.false_for_k4, EulerSumOfPowers.eulers_sum_of_powers_conjecture.false_for_k5
statement: formalized
---

# Euler's sum of powers conjecture

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Euler's_sum_of_powers_conjecture)

*Quoted from [FormalConjectures/Wikipedia/EulerSumOfPowers.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/EulerSumOfPowers.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 1 open and 2 solved.

## `EulerSumOfPowers.eulers_sum_of_powers_conjecture`

Open: stated without proof.

> Euler's sum of powers conjecture states that for integers $n > 1$ and $k > 1$,
> if the sum of $n$ positive integers each raised to the $k$-th power equals another integer
> raised to the $k$-th power, then $n ≥ k$.
>
> The conjecture is known to be false for $k = 4$ and $k = 5$,
> but remains open for $k ≥ 6$.

```lean
theorem eulers_sum_of_powers_conjecture (n k b : ℕ) (hn : 1 < n) (hk : 5 < k) (a : Fin n → ℕ)
    (ha : ∀ i, a i > 0) (hsum : ∑ i, (a i) ^ k = b ^ k) : k ≤ n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/EulerSumOfPowers.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/EulerSumOfPowers.lean#L39).

## `EulerSumOfPowers.eulers_sum_of_powers_conjecture.false_for_k4`

Proved here.

> Euler's sum of powers conjecture is false for $k=4$ (counterexample exists).

```lean
theorem eulers_sum_of_powers_conjecture.false_for_k4 : ¬ (∀ (n b : ℕ) (_ : 1 < n)
    (a: Fin n → ℕ) (_ : ∀ i, a i > 0) (_ : ∑ i, (a i) ^ 4 = b ^ 4), 4 ≤ n)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/EulerSumOfPowers.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/EulerSumOfPowers.lean#L45).

## `EulerSumOfPowers.eulers_sum_of_powers_conjecture.false_for_k5`

Proved here.

> Euler's sum of powers conjecture is false for $k=5$ (counterexample exists).

```lean
theorem eulers_sum_of_powers_conjecture.false_for_k5 : ¬ (∀ (n b : ℕ) (_ : 1 < n)
    (a: Fin n → ℕ) (_ : ∀ i, a i > 0) (_ : ∑ i, (a i) ^ 5 = b ^ 5), 5 ≤ n)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/EulerSumOfPowers.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/EulerSumOfPowers.lean#L55).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/EulerSumOfPowers.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/EulerSumOfPowers.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Euler's_sum_of_powers_conjecture)
