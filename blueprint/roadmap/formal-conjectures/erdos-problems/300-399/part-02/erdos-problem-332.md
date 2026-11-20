---
declaration: theorem
origin: cited
lean: Erdos332.erdos_332
statement: formalized
---

# Erdős Problem 332

> *Reference:* [erdosproblems.com/332](https://www.erdosproblems.com/332)

*Quoted from [FormalConjectures/ErdosProblems/332.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/332.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/332](https://www.erdosproblems.com/332).

The file states 1 research or textbook statement: 1 open.

## `Erdos332.erdos_332`

Open: stated without proof.

> Let $A\subseteq \mathbb{N}$ and $D(A)$ be the set of those numbers which occur infinitely often as
> $a_1 - a_2$ with $a_1, a_2\in A$. What conditions on $A$ are sufficient to ensure $D(A)$ has bounded
> gaps?
>
> The sufficient conditions are the unknown `erdos_332.answer`. In order to solve this problem one
> has to provide what the sufficient conditions are, and proof that they imply the desired condition.
> If the condition is a solution to the problem is up to human judgement.

```lean
theorem erdos_332 (A : Set ℕ) : erdos_332.answer A → HasBoundedGaps (D_A A)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/332.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/332.lean#L57).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/332.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/332.lean)
- [erdosproblems.com/332](https://www.erdosproblems.com/332)
