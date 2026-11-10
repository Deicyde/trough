---
declaration: theorem
origin: cited
lean: Erdos774.erdos_774
statement: formalized
---

# Erdős Problem 774

> *Reference:* [erdosproblems.com/774](https://www.erdosproblems.com/774)

*Quoted from [FormalConjectures/ErdosProblems/774.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/774.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/774](https://www.erdosproblems.com/774).

The file states 1 research or textbook statement: 1 open.

## `Erdos774.erdos_774`

Open: stated without proof.

> Is every proportionately dissociated (infinite) set the union of a finite
> number of dissociated sets?

```lean
theorem erdos_774 : ∀ (A : Set ℕ), A.Infinite → A.IsProportionatelyDissociated →
    ∃ (T : Set (Set ℕ)), (∀ S ∈ T, S.IsDissociated) ∧ T.Finite ∧ A = ⋃₀ T
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/774.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/774.lean#L51).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/774.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/774.lean)
- [erdosproblems.com/774](https://www.erdosproblems.com/774)
