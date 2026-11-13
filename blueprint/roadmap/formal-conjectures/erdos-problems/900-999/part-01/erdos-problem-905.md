---
declaration: theorem
origin: cited
lean: Erdos905.erdos_905
statement: formalized
---

# Erdős Problem 905

> *References:*
> - [erdosproblems.com/905](https://www.erdosproblems.com/905)
> - [KhNi79] Khadzhiivanov, N. G. and Nikiforov, S. V., *Solution of a problem of P. Erdős about the
>   maximum number of triangles with a common edge in a graph*. C. R. Acad. Bulgare Sci. (1979),
>   1315-1318.

*Quoted from [FormalConjectures/ErdosProblems/905.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/905.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/905](https://www.erdosproblems.com/905).

The file states 1 research or textbook statement: 1 solved.

## `Erdos905.erdos_905`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos905.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos905.lean).

> Every graph with $n$ vertices and $>n^2/4$ edges contains an edge which is in at least $n/6$
> triangles.
>
> A conjecture of Bollobás and Erdős. This was proved independently by Edwards (unpublished) and
> Khadzhiivanov and Nikiforov [KhNi79].

```lean
theorem erdos_905 (n : ℕ) (G : SimpleGraph (Fin n)) [DecidableRel G.Adj]
    (hG : (n : ℝ) ^ 2 / 4 < (#G.edgeFinset : ℝ)) :
    ∃ e ∈ G.edgeFinset, (n : ℝ) / 6 ≤ (#(G.trianglesContaining e) : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/905.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/905.lean#L45).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/905.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/905.lean)
- [erdosproblems.com/905](https://www.erdosproblems.com/905)
