---
declaration: theorem
origin: cited
lean: Erdos1077.erdos_1077
statement: formalized
---

# Erdős Problem 1077

> *Reference:* [erdosproblems.com/1077](https://www.erdosproblems.com/1077)

*Quoted from [FormalConjectures/ErdosProblems/1077.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1077.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1077](https://www.erdosproblems.com/1077).

The file states 1 research or textbook statement: 1 solved.

## `Erdos1077.erdos_1077`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/dfe2d78128b493c572cf525b1b8edf4897fb7664/src/latest/ErdosProblems/Erdos1077.lean#L265](https://github.com/plby/lean-proofs/blob/dfe2d78128b493c572cf525b1b8edf4897fb7664/src/latest/ErdosProblems/Erdos1077.lean#L265).

> We call a graph $D$-balanced (or $D$-almost-regular) if the maximum degree is at most $D$ times the
> minimum degree.
>
> Let $ε, α > 0$ and $D$ and $n$ be sufficiently large. If $G$ is a graph on $n$ vertices with at
> least $n^{1+α}$ edges, then must $G$ contain a $D$-balanced subgraph on $m > n^{1-α}$ vertices with
> at least $εm^{1+α}$ edges?

```lean
theorem erdos_1077 :
    ¬ ∀ ε > (0 : ℝ), ε < 1 → ∀ α > (0 : ℝ), α < 1 → ∀ᶠ D in atTop, ∀ᶠ n in atTop,
      ∀ G : SimpleGraph (Fin n), G.edgeSet.ncard > (n : ℝ) ^ (1 + α) →
        ∃ (H : Subgraph G),
          letI m := H.verts.ncard
          IsBalanced H.coe D ∧
          m > (n : ℝ) ^ (1 - α) ∧
          H.edgeSet.ncard > ε * m ^ (1 + α)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1077.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1077.lean#L44).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1077.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1077.lean)
- [erdosproblems.com/1077](https://www.erdosproblems.com/1077)
