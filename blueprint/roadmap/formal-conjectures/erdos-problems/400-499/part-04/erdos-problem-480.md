---
declaration: theorem
origin: cited
lean: Erdos480.erdos_480, Erdos480.erdos_480.variants.chung_graham, Erdos480.erdos_480.variants.chung_graham_best_possible
statement: formalized
---

# Erdős Problem 480

> *Reference:* [erdosproblems.com/480](https://www.erdosproblems.com/480)

*Quoted from [FormalConjectures/ErdosProblems/480.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/480.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/480](https://www.erdosproblems.com/480).

The file states 3 research or textbook statements: 3 solved.

## `Erdos480.erdos_480`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/1268917deaaaa0d674f651287027baa26cea9920/src/latest/ErdosProblems/Erdos480.lean#L973](https://github.com/plby/lean-proofs/blob/1268917deaaaa0d674f651287027baa26cea9920/src/latest/ErdosProblems/Erdos480.lean#L973).

> Let $x_1,x_2,\ldots\in [0,1]$ be an infinite sequence.
> Is it true that
>
> $$\inf_n \liminf_{m\to \infty} n \lvert x_{m+n}-x_m\rvert\leq 5^{-1/2}\approx 0.447?$$
>
> A conjecture of Newman.

```lean
theorem erdos_480 : ∀ (x : ℕ → ℝ), (∀ n, x n ∈ Set.Icc 0 1) →
    ⨅ (n : ℕ+), atTop.liminf (fun m => (n : ℕ) * |x (m + (n : ℕ)) - x m|) ≤ 1 / √5
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/480.lean, line 40](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/480.lean#L40).

## `Erdos480.erdos_480.variants.chung_graham`

Solved: stated here without proof.

> This was proved by Chung and Graham \cite{ChGr84}, who in fact prove that
>
> $$\inf_n \liminf_{m\to \infty} n \lvert x_{m+n}-x_m\rvert\leq \frac{1}{c}\approx 0.3944$$
>
> where
>
> $$c=1+\sum_{k\geq 1}\frac{1}{F_{2k}}=2.5353705\cdots$$
>
> and $F_m$ is the $m$th Fibonacci number.

```lean
theorem erdos_480.variants.chung_graham :
    let c : ℝ := 1 + ∑' (k : ℕ+), (1 : ℝ) / (2*k : ℕ).fib
    ∀ (x : ℕ → ℝ), (∀ n, x n ∈ Set.Icc 0 1) →
    ⨅ (n : ℕ+), atTop.liminf (fun m => (n : ℕ) * |x (m + (n : ℕ)) - x m|) ≤ 1 / c
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/480.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/480.lean#L52).

## `Erdos480.erdos_480.variants.chung_graham_best_possible`

Solved: stated here without proof.

> They also prove that this constant is best possible.

```lean
theorem erdos_480.variants.chung_graham_best_possible :
    let c : ℝ := 1 + ∑' (k : ℕ+), (1 : ℝ) / (2*k : ℕ).fib
    ∀ ε > (0 : ℝ), ¬ (∀ (x : ℕ → ℝ), (∀ n, x n ∈ Set.Icc 0 1) →
    ⨅ (n : ℕ+), atTop.liminf (fun m => (n : ℕ) * |x (m + (n : ℕ)) - x m|) ≤ 1 / c - ε)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/480.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/480.lean#L62).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/480.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/480.lean)
- [erdosproblems.com/480](https://www.erdosproblems.com/480)
