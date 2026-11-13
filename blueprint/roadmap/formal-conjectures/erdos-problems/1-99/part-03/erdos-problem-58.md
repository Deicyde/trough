---
declaration: theorem
origin: cited
lean: Erdos58.erdos_58
statement: formalized
---

# Erdős Problem 58

> *References:*
> - [erdosproblems.com/58](https://www.erdosproblems.com/58)
> - [Er90] Erdős, Paul, Some of my favourite unsolved problems. A tribute to Paul Erdős (1990), 467-478.
> - [GaHuMa21] Gao, Jun and Huo, Qingyi and Ma, Jie, *A strengthening on odd cycles in graphs of given
>   chromatic number*. SIAM J. Discrete Math. (2021), 2317-2327.
> - [Gy92] Gyárfás, A., *Graphs with k odd cycle lengths*. Discrete Math. (1992), 41-48.

*Quoted from [FormalConjectures/ErdosProblems/58.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/58.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/58](https://www.erdosproblems.com/58).

The file states 1 research or textbook statement: 1 solved.

## `Erdos58.erdos_58`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/1f6f15be04f783cf5fabcf7f8477b4d8c03c685c/erdos-58/Proofs/Layer1358.lean#L35](https://github.com/linrock/math-proofs/blob/1f6f15be04f783cf5fabcf7f8477b4d8c03c685c/erdos-58/Proofs/Layer1358.lean#L35).

> If $G$ is a graph which contains odd cycles of $\leq k$ different lengths then $\chi(G)\leq 2k+2$,
> with equality if and only if $G$ contains $K_{2k+2}$.
>
> Conjectured by Bollobás and Erdős. Proved by Gyárfás [Gy92].

```lean
theorem erdos_58 :
    ∀ {V : Type*} (G : SimpleGraph V) (k : ℕ),
      G.oddCycleLengths.Finite →
      G.oddCycleLengths.ncard ≤ k →
        G.chromaticNumber ≤ (2 * k + 2 : ℕ∞) ∧
        (G.chromaticNumber = (2 * k + 2 : ℕ∞) ↔
          (SimpleGraph.completeGraph (Fin (2 * k + 2))).IsContained G)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/58.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/58.lean#L44).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/58.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/58.lean)
- [erdosproblems.com/58](https://www.erdosproblems.com/58)
