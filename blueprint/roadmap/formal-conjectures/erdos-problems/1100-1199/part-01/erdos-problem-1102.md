---
declaration: theorem
origin: cited
lean: Erdos1102.erdos_1102.density_zero_of_P, Erdos1102.erdos_1102.exists_sequence_with_P, Erdos1102.erdos_1102.upper_density_Q, Erdos1102.erdos_1102.lower_density_Q_exists
statement: formalized
---

# Erdős Problem 1102

> *Reference:* [erdosproblems.com/1102](https://www.erdosproblems.com/1102)

*Quoted from [FormalConjectures/ErdosProblems/1102.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1102.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1102](https://www.erdosproblems.com/1102).

The file states 4 research or textbook statements: 4 solved.

## `Erdos1102.erdos_1102.density_zero_of_P`

Solved: stated here; a Lean proof is at [https://github.com/Woett/Lean-files/blob/1e075c4f6e8a907b924647fa88238f978e941742/ErdosProblem1102PropertyP.lean](https://github.com/Woett/Lean-files/blob/1e075c4f6e8a907b924647fa88238f978e941742/ErdosProblem1102PropertyP.lean).

> If `A = {a₁ < a₂ < …}` has property P,
> then `A` has natural density `0`.
> Equivalently, `(a_j / j) → ∞` as `j → ∞`.
> -

```lean
theorem erdos_1102.density_zero_of_P
    (A : ℕ → ℕ)
    (h_inc : StrictMono A)
    (hP : HasPropertyP (range A)) :
    Tendsto (fun j => (A j / j : ℝ)) atTop atTop
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1102.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1102.lean#L53).

## `Erdos1102.erdos_1102.exists_sequence_with_P`

Solved: stated here; a Lean proof is at [https://github.com/Woett/Lean-files/blob/1e075c4f6e8a907b924647fa88238f978e941742/ErdosProblem1102PropertyP.lean](https://github.com/Woett/Lean-files/blob/1e075c4f6e8a907b924647fa88238f978e941742/ErdosProblem1102PropertyP.lean).

> Conversely, for any function `f : ℕ → ℕ` that goes to infinity,
> there exists a strictly increasing sequence `A = {a₁ < a₂ < …}`
> with property P such that `(a_j / j) ≤ f(j)` for all `j`.
> -

```lean
theorem erdos_1102.exists_sequence_with_P
    (f : ℕ → ℕ) (h_inf : Tendsto f atTop atTop)
    (h_pos : ∀ n, f n ≠ 0) :
    ∃ A : ℕ → ℕ, StrictMono A ∧
    HasPropertyP (range A) ∧
    ∀ j : ℕ, (A j : ℝ) / j ≤ f j
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1102.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1102.lean#L68).

## `Erdos1102.erdos_1102.upper_density_Q`

Solved: stated here; a Lean proof is at [https://github.com/Woett/Lean-files/blob/1e075c4f6e8a907b924647fa88238f978e941742/ErdosProblem1102PropertyQDensity.lean](https://github.com/Woett/Lean-files/blob/1e075c4f6e8a907b924647fa88238f978e941742/ErdosProblem1102PropertyQDensity.lean).

> Every sequence with property Q has upper density at most `6 / π^2`.
> -

```lean
theorem erdos_1102.upper_density_Q
    (A : ℕ → ℕ) (h_inc : StrictMono A)
    (hQ : HasPropertyQ (range A)) :
    limsup (fun j : ℕ  ↦ (j / A j : ℝ)) atTop ≤ 6 / Real.pi^2
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1102.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1102.lean#L82).

## `Erdos1102.erdos_1102.lower_density_Q_exists`

Solved: stated here; a Lean proof is at [https://github.com/Woett/Lean-files/blob/1e075c4f6e8a907b924647fa88238f978e941742/ErdosProblem1102PropertyQDensity.lean](https://github.com/Woett/Lean-files/blob/1e075c4f6e8a907b924647fa88238f978e941742/ErdosProblem1102PropertyQDensity.lean).

> There exists an infinite sequence $A = {a₁ < a₂ < …} ⊂ \mathsf{SF}$ where
> $\mathsf{SF} := \mathbb{N} \setminus \bigcup_{p} p^{2}\mathbb{N}$, i.e. the set of
> squarefree numbers. The set `A` has property `Q` and natural density `6 / π^2`.
> Equivalently, `(j / a_j) → 6/π^2` as `j → ∞`.
> -

```lean
theorem erdos_1102.lower_density_Q_exists :
    ∃ A : ℕ → ℕ, StrictMono A ∧
    (∀ j, Squarefree (A j)) ∧
    HasPropertyQ (range A) ∧
    Tendsto (fun j : ℕ  ↦ (j / A j : ℝ)) atTop (𝓝 (6 / Real.pi^2))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1102.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1102.lean#L97).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1102.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1102.lean)
- [erdosproblems.com/1102](https://www.erdosproblems.com/1102)
