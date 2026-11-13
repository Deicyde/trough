---
declaration: theorem
origin: cited
lean: Erdos603.erdos_603
statement: formalized
---

# Erdős Problem 603

> *References:*
> - [erdosproblems.com/603](https://www.erdosproblems.com/603)

*Quoted from [FormalConjectures/ErdosProblems/603.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/603.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/603](https://www.erdosproblems.com/603).

The file states 1 research or textbook statement: 1 solved.

## `Erdos603.erdos_603`

Solved: stated here without proof.

> Let $(A_i)$ be a family of countably infinite sets such that $\lvert A_i\cap A_j\rvert \neq 2$ for
> all $i\neq j$. Find the smallest cardinal $C$ such that $\cup A_i$ can always be coloured with at
> most $C$ colours so that no $A_i$ is monochromatic.
>
> GPT 5.4 Pro (prompted by Chojecki) proved there is no uniform bound on such $C$: for every cardinal
> $C$ there is a family of countably infinite sets $(A_i)$ such that $\lvert A_i\cap A_j\rvert \neq 2$
> for all $i\neq j$, and in any colouring of $\cup A_i$ with $C$ colours some $A_i$ is monochromatic.

```lean
theorem erdos_603 :
    ∀ C : Cardinal.{0}, ∃ (V : Type) (F : Set (Set V)),
    (∀ A ∈ F, Cardinal.mk A = ℵ₀) ∧
    F.Pairwise (fun (A B : Set V) ↦ Cardinal.mk ↥(A ∩ B) ≠ 2) ∧
    ⋃₀ F = Set.univ ∧
    ∀ c : V → C.out, ∃ A ∈ F, ∀ x ∈ A, ∀ y ∈ A, c x = c y
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/603.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/603.lean#L43).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/603.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/603.lean)
- [erdosproblems.com/603](https://www.erdosproblems.com/603)
