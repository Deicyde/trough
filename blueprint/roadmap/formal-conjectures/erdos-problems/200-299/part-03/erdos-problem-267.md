---
declaration: theorem
origin: cited
lean: Erdos267.erdos_267, Erdos267.erdos_267.variants.generalisation_ratio_limit_to_infinity, Erdos267.erdos_267.variants.specialization_pow_two, Erdos267.erdos_267.variants.fibonacci_inverse_sum
statement: formalized
---

# Erdős Problem 267

> *Reference:* [erdosproblems.com/267](https://www.erdosproblems.com/267)

*Quoted from [FormalConjectures/ErdosProblems/267.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/267.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/267](https://www.erdosproblems.com/267).

The file states 4 research or textbook statements: 1 open and 3 solved.

## `Erdos267.erdos_267`

Solved: stated here; a Lean proof is at [https://github.com/williamjblair/lean-proofs/blob/4f915a323443bfb1709a6805a013812016dca88a/starfleet/erdos-267/Research/Basic.lean](https://github.com/williamjblair/lean-proofs/blob/4f915a323443bfb1709a6805a013812016dca88a/starfleet/erdos-267/Research/Basic.lean).

> Let $F_1=F_2=1$ and $F_{n+1} = F_n + F_{n-1}$ be the Fibonacci sequence.
> Let $n_1 < n_2 < \dots$ be an infinite sequence with $\frac{n_{k+1}}{n_k} \ge c > 1$. Must
> $\sum_k \frac 1 {F_{n_k}}$ be irrational?

```lean
theorem erdos_267 : ∀ᵉ (n : ℕ → ℕ) (c > (1 : ℚ)), StrictMono n → (∀ k, c ≤ n (k+1) / n k) →
    Irrational (∑' k, 1 / (Nat.fib <| n k))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/267.lean, line 37](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/267.lean#L37).

## `Erdos267.erdos_267.variants.generalisation_ratio_limit_to_infinity`

Open: stated without proof.

> Let $F_1=F_2=1$ and $F_{n+1} = F_n + F_{n-1}$ be the Fibonacci sequence.
> Let $n_1 < n_2 < \dots$ be an infinite sequence with $\frac {n_k}{k} \to \infty$. Must
> $\sum_k \frac 1 {F_{n_k}}$ be irrational?

```lean
theorem erdos_267.variants.generalisation_ratio_limit_to_infinity : ∀ (n : ℕ → ℕ),
    StrictMono n → Filter.Tendsto (fun k => (n (k+1) / k.succ : ℝ)) Filter.atTop Filter.atTop →
    Irrational (∑' k, 1 / (Nat.fib <| n k))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/267.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/267.lean#L47).

## `Erdos267.erdos_267.variants.specialization_pow_two`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/2663234a28260853790aa5752d8d4550ff0ab1ca/FormalConjectures/ErdosProblems/267.lean#L56](https://github.com/mo271/formal-conjectures/blob/2663234a28260853790aa5752d8d4550ff0ab1ca/FormalConjectures/ErdosProblems/267.lean#L56).

> Good [Go74] and Bicknell and Hoggatt [BiHo76] have shown that $\sum_n \frac 1 {F_{2^n}}$ is irrational.
>
>
> Formal proof provided by AlphaProof
> Ref:
> * [Go74] Good, I. J., _A reciprocal series of Fibonacci numbers_
> * [BiHo76] Hoggatt, Jr., V. E. and Bicknell, Marjorie, _A reciprocal series of Fibonacci numbers with subscripts $2\sp{n}k$_

```lean
theorem erdos_267.variants.specialization_pow_two :
    Irrational <| ∑' k, 1 / (Nat.fib <| 2^k)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/267.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/267.lean#L64).

## `Erdos267.erdos_267.variants.fibonacci_inverse_sum`

Solved: stated here without proof.

> The sum $\sum_n \frac 1 {F_{n}}$ itself was proved to be irrational by André-Jeannin.
>
> Ref: André-Jeannin, Richard, _Irrationalité de la somme des inverses de certaines suites récurrentes_.

```lean
theorem erdos_267.variants.fibonacci_inverse_sum :
    Irrational <| ∑' k, 1 / (Nat.fib k)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/267.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/267.lean#L74).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/267.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/267.lean)
- [erdosproblems.com/267](https://www.erdosproblems.com/267)
