---
declaration: theorem
origin: cited
lean: Erdos158.erdos_158, Erdos158.erdos_158.variants.isSidon', Erdos158.erdos_158.variants.isSidon
statement: formalized
---

# Erdős Problem 158

> *References:*
>  - [erdosproblems.com/158](https://www.erdosproblems.com/158)
>  - [ESS94] Erdős, P. and Sárközy, A. and Sós, T., On Sum Sets of Sidon Sets, I. Journal of Number
>     Theory (1994), 329-347.

*Quoted from [FormalConjectures/ErdosProblems/158.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/158.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/158](https://www.erdosproblems.com/158).

The file states 3 research or textbook statements: 1 open and 2 solved. It also has 1 API statement, counted here but not shown.

## `Erdos158.erdos_158`

Open: stated without proof.

> Let `A` be an infinite `B₂[2]` set. Must `liminf |A ∩ {1, ..., N}| * N ^ (- 1 / 2) = 0`?

```lean
theorem erdos_158 : ∀ A : Set ℕ, A.Infinite → B2 2 A →
    liminf (fun N : ℕ => (A ∩ .Iio N).ncard * (N : ℝ) ^ (- 1 / 2 : ℝ)) atTop = 0
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/158.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/158.lean#L60).

## `Erdos158.erdos_158.variants.isSidon'`

Solved: stated here without proof.

> Let `A` be an infinite Sidon set. Then
> `liminf |A ∩ {1, ..., N}| * N ^ (- 1 / 2) * (log N) ^ (1 / 2) < ∞`. This is proved in [ESS94].

```lean
theorem erdos_158.variants.isSidon' {A : Set ℕ} (hAinf : A.Infinite) (hAsid : IsSidon A) :
    liminf (fun N ↦ ENNReal.ofReal ((A ∩ .Iio N).ncard * N ^ (- 1 / 2 : ℝ) * log N ^ (1 / 2 : ℝ)))
      atTop < ⊤
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/158.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/158.lean#L67).

## `Erdos158.erdos_158.variants.isSidon`

Proved here.

> As a corollary of `erdos_158.isSidon'`, we can prove that
> `liminf |A ∩ {1, ..., N}| * N ^ (- 1 / 2) = 0` for any infinite Sidon set `A`.

```lean
theorem erdos_158.variants.isSidon {A : Set ℕ} (hAinf : A.Infinite) (hAsid : IsSidon A) :
    liminf (fun N : ℕ => (A ∩ .Iio N).ncard * (N : ℝ) ^ (- 1 / 2 : ℝ)) atTop = 0
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/158.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/158.lean#L75).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/158.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/158.lean)
- [erdosproblems.com/158](https://www.erdosproblems.com/158)
