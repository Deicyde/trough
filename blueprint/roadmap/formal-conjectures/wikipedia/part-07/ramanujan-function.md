---
declaration: theorem
origin: cited
lean: RamanujanTau.ramanujan_petersson, RamanujanTau.lehmer_ramanujan_tau
statement: formalized
---

# Ramanujan τ-function

> There are two conjectures related to the Ramanujan τ-function:
>
> - Ramanujan-Petersson conjecture: For every prime `p`, the absolute value of the
>   Ramanujan τ-function at `p` is bounded by `2 * p^(11/2)`.
> - Lehmer's conjecture: The Ramanujan τ-function is never zero for any positive integer `n`.
>
> *References:*
> - [Ramanujan-Petersson conjecture](https://en.wikipedia.org/wiki/Ramanujan%E2%80%93Petersson_conjecture)
> - [Lehmer's conjecture](https://en.wikipedia.org/wiki/Ramanujan_tau_function#Conjectures_on_the_tau_function)

*Quoted from [FormalConjectures/Wikipedia/RamanujanTau.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/RamanujanTau.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 3 test statements and 1 API statement, counted here but not shown.

## `RamanujanTau.ramanujan_petersson`

Solved: stated here without proof.

> The Ramanujan-Petersson conjecture: $|\tau(p)| \le 2 p^{11/2}$ for primes $p$.

```lean
theorem ramanujan_petersson : ∀ p : ℕ, Prime p → abs (τ p) ≤ 2 * (p : ℝ) ^ ((11 : ℝ) / 2)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/RamanujanTau.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/RamanujanTau.lean#L65).

## `RamanujanTau.lehmer_ramanujan_tau`

Open: stated without proof.

> Lehmer's conjecture: $\tau(n) \ne 0$ for all $n > 0$.

```lean
theorem lehmer_ramanujan_tau : ∀ n > 0, τ n ≠ 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/RamanujanTau.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/RamanujanTau.lean#L70).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/RamanujanTau.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/RamanujanTau.lean)
- [Ramanujan-Petersson conjecture](https://en.wikipedia.org/wiki/Ramanujan%E2%80%93Petersson_conjecture)
