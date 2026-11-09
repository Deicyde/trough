---
declaration: theorem
origin: cited
lean: Erdos75.erdos_75
statement: formalized
---

# Erdős Problem 75

> *Reference:*
> * [erdosproblems.com/75] (https://www.erdosproblems.com/75)

*Quoted from [FormalConjectures/ErdosProblems/75.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/75.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/75](https://www.erdosproblems.com/75).

The file states 1 research or textbook statement: 1 open.

## `Erdos75.erdos_75`

Open: stated without proof.

> Is there a graph of chromatic number `ℵ_ 1` with `ℵ_ 1` vertices such that for all
> `ε > 0`, if `n` is sufficiently large and `H` is a subgraph on `n` vertices,
> then `H` contains an independent set of size `> n ^ (1 - ε)`?

```lean
theorem erdos_75 :
    ∃ (V : Type) (G : SimpleGraph V),
      G.chromaticCardinal = ℵ_ 1 ∧
      #V = ℵ_ 1 ∧
      ∀ ε > (0 : ℝ),
        ∀ᶠ (n : ℕ) in Filter.atTop, ∀ (H : G.Subgraph),
            H.verts.ncard = n →
            ∃ (I : Finset V),
              (I : Set V) ⊆ H.verts ∧
              G.IsIndepSet (I : Set V) ∧
              (I.card : ℝ) > (n : ℝ) ^ (1 - ε)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/75.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/75.lean#L39).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/75.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/75.lean)
- [erdosproblems.com/75](https://www.erdosproblems.com/75)
