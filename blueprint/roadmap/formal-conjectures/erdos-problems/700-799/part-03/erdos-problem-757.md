---
declaration: theorem
origin: cited
lean: Erdos757.erdos_757, Erdos757.erdos_757.variants.lowerBound, Erdos757.erdos_757.variants.upperBound
statement: formalized
---

# Erdős Problem 757

> *References:*
>  - [erdosproblems.com/757](https://www.erdosproblems.com/757)
>  - [GyLe95] Gyárfás, András and Lehel, Jenő, Linear sets with five distinct differences among any
>     four elements. J. Combin. Theory Ser. B (1995), 108-118.

*Quoted from [FormalConjectures/ErdosProblems/757.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/757.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/757](https://www.erdosproblems.com/757).

The file states 3 research or textbook statements: 1 open and 2 solved.

## `Erdos757.erdos_757`

Open: stated without proof.

> What is the supremum of the set of admissible numbers?

```lean
theorem erdos_757 {A : Set ℝ} :
    erdos_757.answer = sSup {c | IsAdmissible c}
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/757.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/757.lean#L47).

## `Erdos757.erdos_757.variants.lowerBound`

Solved: stated here without proof.

> The supremum is strictly larger than `1 / 2`, which is proved in [GyLe95].

```lean
theorem erdos_757.variants.lowerBound {A : Set ℝ} : 1 / (2 : ℝ) < sSup {c | IsAdmissible c}
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/757.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/757.lean#L53).

## `Erdos757.erdos_757.variants.upperBound`

Solved: stated here without proof.

> In [GyLe95], the authors also prove that the supremum is smaller than `3 / 5`.

```lean
theorem erdos_757.variants.upperBound {A : Set ℝ} : sSup {c | IsAdmissible c} < 3 / (5 : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/757.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/757.lean#L58).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/757.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/757.lean)
- [erdosproblems.com/757](https://www.erdosproblems.com/757)
