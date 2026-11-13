---
declaration: theorem
origin: cited
lean: Erdos546.erdos_546
statement: formalized
---

# Erdős Problem 546

> *References:*
> - [erdosproblems.com/546](https://www.erdosproblems.com/546)
> - [Su11] Sudakov, B., A conjecture of Erdős on graph Ramsey numbers. Adv. Math. (2011), 3148-3155.
> - [AKS03] Alon, N., Krivelevich, M. and Sudakov, B., Turán numbers of bipartite graphs and Ramsey
>   graphs of bounded degree. Combin. Probab. Comput. (2003), 477-483.
> - [PALOMAR-2026-10-04-000010](https://palomar-registry.org/entry.html?id=PALOMAR-2026-10-04-000010&version=1)

*Quoted from [FormalConjectures/ErdosProblems/546.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/546.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/546](https://www.erdosproblems.com/546).

The file states 1 research or textbook statement: 1 solved.

## `Erdos546.erdos_546`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/7caa4144741e10f96cf79d6f7313a0efd9a18b67/erdos-546/Proofs/OriginalStatement546.lean#L33](https://github.com/linrock/math-proofs/blob/7caa4144741e10f96cf79d6f7313a0efd9a18b67/erdos-546/Proofs/OriginalStatement546.lean#L33).

> Let $G$ be a graph with no isolated vertices and $m$ edges. Is it true that
>
> $$R(G) \leq 2^{O(m^{1/2})}?$$
>
> This is true, and was proved by Sudakov [Su11].
>
> This problem is #11 in Ramsey Theory in the graphs problem collection.

```lean
theorem erdos_546 :
    ∃ C > (0 : ℝ), ∀ (m : ℕ) (V : Type) [Fintype V] (G : SimpleGraph V) [DecidableRel G.Adj],
      (∀ v, 0 < G.degree v) →
      G.edgeSet.ncard = m →
      (SimpleGraph.diagonalGraphRamsey G : ℝ) ≤ 2 ^ (C * Real.sqrt m)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/546.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/546.lean#L45).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/546.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/546.lean)
- [erdosproblems.com/546](https://www.erdosproblems.com/546)
