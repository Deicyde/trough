---
declaration: theorem
origin: cited
lean: Erdos67.erdos_67, Erdos67.erdos_67.variants.complex
statement: formalized
---

# Erdős Problem 67

> *References:*
> - [erdosproblems.com/67](https://www.erdosproblems.com/66)
> - [Ta16] Tao, Terence, The Erdős discrepancy problem. Discrete Anal. (2016), Paper No. 1, 29.

*Quoted from [FormalConjectures/ErdosProblems/67.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/67.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/67](https://www.erdosproblems.com/67).

The file states 2 research or textbook statements: 2 solved.

## `Erdos67.erdos_67`

Solved: stated here without proof.

> **The Erdős discrepancy problem**
>
> If $f\colon \mathbb N \rightarrow \{-1, +1\}$ then is it true that for every $C>0$ there
> exist $d, m \ge 1$ such that
>
> $$\left\lvert \sum_{1\leq k\leq m}f(kd)\right\rvert > C?$$
>
> This is true, and was proved by Tao [Ta16]

```lean
theorem erdos_67 (f : ℕ → ({-1, 1} : Finset ℝ)) (C : ℝ) (hC : 0 < C) : ∃ᵉ (d ≥ 1) (m ≥ 1),
    C < |∑ k ∈ Finset.Icc 1 m, (f (k * d)).1|
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/67.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/67.lean#L42).

## `Erdos67.erdos_67.variants.complex`

Solved: stated here without proof.

> **The Erdős discrepancy problem (complex variant)**
>
> If $f\colon \mathbb N \rightarrow S^1 ⊆ ℂ$ then is it true that for every $C>0$ there
> exist $d, m \ge 1$ such that
>
> $$\left\lvert \sum_{1\leq k\leq m}f(kd)\right\rvert > C?$$
>
> This is true, and was proved by Tao [Ta16]

```lean
theorem erdos_67.variants.complex (f : ℕ → Metric.sphere (0 : ℂ) 1) (C : ℝ) (hC : 0 < C) :
    ∃ᵉ (d ≥ 1) (m ≥ 1), C < ‖∑ k ∈ Finset.Icc 1 m, (f (k * d)).1‖
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/67.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/67.lean#L54).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/67.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/67.lean)
- [erdosproblems.com/67](https://www.erdosproblems.com/67)
