---
declaration: theorem
origin: cited
lean: Erdos569.erdos_569
statement: formalized
---

# Erdős Problem 569

> *References:*
> - [erdosproblems.com/569](https://www.erdosproblems.com/569)
> - [EFRS93] Erdős, Paul and Faudree, R. J. and Rousseau, C. C. and Schelp, R. H., Ramsey size linear
>   graphs. Combin. Probab. Comput. (1993), 389-399.

*Quoted from [FormalConjectures/ErdosProblems/569.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/569.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/569](https://www.erdosproblems.com/569).

The file states 1 research or textbook statement: 1 open.

## `Erdos569.erdos_569`

Open: stated without proof.

> Let $k\geq 1$. What is the best possible $c_k$ such that
>
> $$R(C_{2k+1},H)\leq c_k m$$
>
> for any graph $H$ on $m$ edges without isolated vertices?
>
> This problem is #34 in Ramsey Theory in the graphs problem collection.

```lean
theorem erdos_569 :
    ∀ (k : ℕ) (hk : 1 ≤ k),
      sInf {C : ℝ | 0 < C ∧
        ∀ (m : ℕ) (W : Type) [Fintype W] (H : SimpleGraph W) [DecidableRel H.Adj],
          (∀ v, 0 < H.degree v) →
          H.edgeSet.ncard = m →
          (SimpleGraph.graphRamsey (SimpleGraph.cycleGraph (2 * k + 1)) H : ℝ) ≤ C * m} =
            erdos_569.answer k
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/569.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/569.lean#L43).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/569.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/569.lean)
- [erdosproblems.com/569](https://www.erdosproblems.com/569)
