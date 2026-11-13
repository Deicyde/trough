---
declaration: theorem
origin: cited
lean: Erdos749.erdos_749
statement: formalized
---

# Erdős Problem 749

> *Reference:* [erdosproblems.com/749](https://www.erdosproblems.com/749)

*Quoted from [FormalConjectures/ErdosProblems/749.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/749.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/749](https://www.erdosproblems.com/749).

The file states 1 research or textbook statement: 1 open.

## `Erdos749.erdos_749`

Open: stated without proof.

> Let $\epsilon>0$. Does there exist $A\subseteq \mathbb{N}$
> such that the lower density of $A+A$ is at least $1-\epsilon$
> and yet $1_A\ast 1_A(n) \ll_\epsilon 1$ for all $n$?

```lean
theorem erdos_749 : ∀ ε > (0 : ℝ),
    ∃ A : Set ℕ, 1 - ε ≤ lowerDensity (A + A) ∧
    ((Nat.cast (R := ℝ) ∘ sumRep A) ≪ (fun n => (1: ℝ)))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/749.lean, line 38](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/749.lean#L38).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/749.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/749.lean)
- [erdosproblems.com/749](https://www.erdosproblems.com/749)
