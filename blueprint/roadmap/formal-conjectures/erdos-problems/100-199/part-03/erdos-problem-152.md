---
declaration: theorem
origin: cited
lean: Erdos152.erdos_152, Erdos152.erdos_152.variants.square
statement: formalized
---

# Erdős Problem 152

> #TODO: Formalize the corresponding conjecture for infinite Sidon sets.
>
> *References:*
>  - [erdosproblems.com/152](https://www.erdosproblems.com/152)
>  - [DM26a] DeepMind prover agent, [formal proof of Erdős problem 152](https://github.com/mo271/formal-conjectures/blob/29c60aa79729701905cf9e92517af23f588971f2/FormalConjectures/ErdosProblems/152.lean#L485) (2026)
>  - [DM26b] DeepMind prover agent, [formal proof of the quadratic variant of Erdős problem 152](https://github.com/mo271/formal-conjectures/blob/ff58c933d53bb807bf85d98a47402703f9f14ed3/FormalConjectures/ErdosProblems/152.lean#L496) (2026)
>  - [ESS94] Erdős, P. and Sárközy, A. and Sós, T., On Sum Sets of Sidon Sets, I. Journal of Number
>     Theory (1994), 329-347.

*Quoted from [FormalConjectures/ErdosProblems/152.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/152.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/152](https://www.erdosproblems.com/152).

The file states 2 research or textbook statements: 2 solved.

## `Erdos152.erdos_152`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/29c60aa79729701905cf9e92517af23f588971f2/FormalConjectures/ErdosProblems/152.lean#L485](https://github.com/mo271/formal-conjectures/blob/29c60aa79729701905cf9e92517af23f588971f2/FormalConjectures/ErdosProblems/152.lean#L485).

> Must `lim f n = ∞`?
>
> This was proved formally by the DeepMind prover agent [DM26a].

```lean
theorem erdos_152 : Tendsto f atTop atTop
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/152.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/152.lean#L54).

## `Erdos152.erdos_152.variants.square`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/ff58c933d53bb807bf85d98a47402703f9f14ed3/FormalConjectures/ErdosProblems/152.lean#L496](https://github.com/mo271/formal-conjectures/blob/ff58c933d53bb807bf85d98a47402703f9f14ed3/FormalConjectures/ErdosProblems/152.lean#L496).

> Must `f n ≫ n ^ 2`?
>
> This stronger quadratic variant was also proved formally by the DeepMind prover agent [DM26b].

```lean
theorem erdos_152.variants.square :
    (fun n => f n : ℕ → ℝ) ≫ (fun n => n ^ 2 : ℕ → ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/152.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/152.lean#L65).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/152.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/152.lean)
- [erdosproblems.com/152](https://www.erdosproblems.com/152)
