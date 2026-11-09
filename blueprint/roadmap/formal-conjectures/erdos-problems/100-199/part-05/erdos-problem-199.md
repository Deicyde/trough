---
declaration: theorem
origin: cited
lean: Erdos199.erdos_199
statement: formalized
---

# Erdős Problem 199

> *References:*
> - [erdosproblems.com/199](https://www.erdosproblems.com/199)
> - [Ba75] Baumgartner, James E., *Partitioning vector spaces*. J. Combinatorial Theory
>   Ser. A (1975), 231-233.

*Quoted from [FormalConjectures/ErdosProblems/199.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/199.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/199](https://www.erdosproblems.com/199).

The file states 1 research or textbook statement: 1 solved.

## `Erdos199.erdos_199`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos199.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos199.lean).

> If $A\subset \mathbb{R}$ does not contain a 3-term arithmetic progression then must $\mathbb{R}\backslash A$ contain an infinite arithmetic progression?
>
> Baumgartner [Ba75] answered this in the negative.

```lean
theorem erdos_199 :
    ¬ ∀ A : Set ℝ, ThreeAPFree A →
      ∃ S : Set ℝ, S.IsAPOfLength ⊤ ∧ S ⊆ Aᶜ
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/199.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/199.lean#L41).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/199.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/199.lean)
- [erdosproblems.com/199](https://www.erdosproblems.com/199)
