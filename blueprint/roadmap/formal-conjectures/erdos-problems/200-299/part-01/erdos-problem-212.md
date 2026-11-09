---
declaration: theorem
origin: cited
lean: Erdos212.erdos_212
statement: formalized
---

# Erdős Problem 212

> *Reference:* [erdosproblems.com/212](https://www.erdosproblems.com/212)

*Quoted from [FormalConjectures/ErdosProblems/212.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/212.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/212](https://www.erdosproblems.com/212).

The file states 1 research or textbook statement: 1 open.

## `Erdos212.erdos_212`

Open: stated without proof.

> Is there a dense subset of ℝ^2 such that all pairwise distances
> are rational?

```lean
theorem erdos_212 :
    ∃ u : Set ℂ, Dense u ∧ u.Pairwise fun c₁ c₂ => dist c₁ c₂ ∈ Set.range Rat.cast
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/212.lean, line 35](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/212.lean#L35).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/212.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/212.lean)
- [erdosproblems.com/212](https://www.erdosproblems.com/212)
