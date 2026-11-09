---
declaration: theorem
origin: cited
lean: Erdos197.erdos_197
statement: formalized
---

# Erdős Problem 197

> *Reference:* [erdosproblems.com/197](https://www.erdosproblems.com/197)

*Quoted from [FormalConjectures/ErdosProblems/197.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/197.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/197](https://www.erdosproblems.com/197).

The file states 1 research or textbook statement: 1 open.

## `Erdos197.erdos_197`

Open: stated without proof.

> Can $\mathbb{N}$ be partitioned into two sets, each of which can be permuted to avoid monotone
> 3-term arithmetic progressions?

```lean
theorem erdos_197 :
    ∃ A B : Set ℕ, IsCompl A B ∧
      (∃ f : ℕ ≃ A, ¬HasMonotoneAP (Subtype.val ∘ f) 3) ∧
      (∃ g : ℕ ≃ B, ¬HasMonotoneAP (Subtype.val ∘ g) 3)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/197.lean, line 37](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/197.lean#L37).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/197.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/197.lean)
- [erdosproblems.com/197](https://www.erdosproblems.com/197)
