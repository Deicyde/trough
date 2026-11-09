---
declaration: theorem
origin: cited
lean: Erdos33.erdos_33, Erdos33.erdos_33.variants.one_mem_lowerBounds, Erdos33.erdos_33.variants.vanDoorn
statement: formalized
---

# Erdős Problem 33

> *Reference:* [erdosproblems.com/33](https://www.erdosproblems.com/33)

*Quoted from [FormalConjectures/ErdosProblems/33.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/33.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/33](https://www.erdosproblems.com/33).

The file states 3 research or textbook statements: 1 open and 2 solved.

## `Erdos33.erdos_33`

Open: stated without proof.

> Let `A ⊆ ℕ` be a set such that every integer can be written as `n^2 + a`
> for some `a` in `A` and `n ≥ 0`. What is the smallest possible value of
> `lim sup n → ∞ |A ∩ {1, …, N}| / N^(1/2)`?

```lean
theorem erdos_33 : ⨅ A : {A : Set ℕ | AdditiveBasisCondition A}, Filter.atTop.limsup (fun N =>
    (A.1 ∩ Icc 1 N).ncard / (√N : EReal)) = erdos_33.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/33.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/33.lean#L47).

## `Erdos33.erdos_33.variants.one_mem_lowerBounds`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/8c9a8ab727c1f06935b48a5ab4db145572cab9e9/erdos-33/Solution.lean#L70](https://github.com/linrock/math-proofs/blob/8c9a8ab727c1f06935b48a5ab4db145572cab9e9/erdos-33/Solution.lean#L70).

> Erdos observed that this value is finite and > 1. This records the lower bound `> 1`,
> i.e. that `1` is a strict lower bound for every admissible `A`; the finiteness is
> `erdos_33.variants.vanDoorn`.

```lean
theorem erdos_33.variants.one_mem_lowerBounds :
    1 < ⨅ A : {A : Set ℕ | AdditiveBasisCondition A}, Filter.atTop.limsup (fun N =>
      (A.1 ∩ Icc 1 N).ncard / (√N : EReal))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/33.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/33.lean#L59).

## `Erdos33.erdos_33.variants.vanDoorn`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/8c9a8ab727c1f06935b48a5ab4db145572cab9e9/erdos-33/Solution.lean#L75](https://github.com/linrock/math-proofs/blob/8c9a8ab727c1f06935b48a5ab4db145572cab9e9/erdos-33/Solution.lean#L75).

> The smallest possible value of `lim sup n → ∞ |A ∩ {1, …, N}| / N^(1/2)`
> is at most `2φ^(5/2) ≈ 6.66`, with `φ` equal to the golden ratio. Proven by
> Wouter van Doorn.

```lean
theorem erdos_33.variants.vanDoorn :
    ⨅ A : {A : Set ℕ | AdditiveBasisCondition A}, Filter.atTop.limsup (fun N =>
    (A.1 ∩ Icc 1 N).ncard / (√N : EReal)) ≤ ↑(2 * (φ ^ ((5 : ℝ) / 2)))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/33.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/33.lean#L72).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/33.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/33.lean)
- [erdosproblems.com/33](https://www.erdosproblems.com/33)
