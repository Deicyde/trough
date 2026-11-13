---
declaration: theorem
origin: cited
lean: Erdos923.erdos_923
statement: formalized
---

# Erdős Problem 923

> *References:*
> - [erdosproblems.com/923](https://www.erdosproblems.com/923)
> - [Er69b] Erdős, P., *Problems and results in chromatic graph theory*. Proof Techniques in Graph Theory (1969), 27-35.
> - [Ro77] Rödl, V., *On the chromatic number of subgraphs of a given graph*. Proc. Amer. Math. Soc. (1977), 370-371.

*Quoted from [FormalConjectures/ErdosProblems/923.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/923.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/923](https://www.erdosproblems.com/923).

The file states 1 research or textbook statement: 1 solved.

## `Erdos923.erdos_923`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos923.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos923.lean).

> Is it true that, for every $k$, there is some $f(k)$ such that if $G$ has chromatic number
> $\geq f(k)$ then $G$ contains a triangle-free subgraph with chromatic number $\geq k$?
>
> This is true, as shown by Rödl [Ro77].

```lean
theorem erdos_923 : ∀ (V : Type*) (n : ℕ),
    ∃ k : ℕ, ∀ G : SimpleGraph V, k ≤ G.chromaticNumber →
    ∃ H ≤ G, n ≤ H.chromaticNumber ∧ H.CliqueFree 3
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/923.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/923.lean#L43).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/923.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/923.lean)
- [erdosproblems.com/923](https://www.erdosproblems.com/923)
