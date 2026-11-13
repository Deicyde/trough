---
declaration: theorem
origin: cited
lean: Erdos666.erdos_666
statement: formalized
---

# Erdős Problem 666

> *References:*
> - [erdosproblems.com/666](https://www.erdosproblems.com/666)
> - [BDT93] Brouwer, A. E. and Dejter, I. J. and Thomassen, C., *Highly symmetric subgraphs of
>   hypercubes*. J. Algebraic Combin. (1993), 25-29.
> - [Ch92] Chung, Fan R. K., *Subgraphs of a hypercube containing no small even cycles*. J. Graph
>   Theory (1992), 273-286.
> - [Er91] Erdős, P., *Problems and results in combinatorial analysis and combinatorial number
>   theory*. Graph theory, combinatorics, and applications, Vol. 1 (Kalamazoo, MI, 1988) (1991),
>   397-406.

*Quoted from [FormalConjectures/ErdosProblems/666.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/666.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/666](https://www.erdosproblems.com/666).

The file states 1 research or textbook statement: 1 solved.

## `Erdos666.erdos_666`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos666.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos666.lean).

> Let $Q_n$ be the $n$-dimensional hypercube graph (so that $Q_n$ has $2^n$ vertices and $n2^{n-1}$
> edges). Is it true that, for every $\epsilon>0$, if $n$ is sufficiently large, every subgraph of
> $Q_n$ with
>
> $$\geq \epsilon  n2^{n-1}$$
>
> many edges contains a $C_6$?
>
> The answer to this problem is no: Chung [Ch92] and Brouwer, Dejter, and Thomassen [BDT93]
> constructed an edge-partition of $Q_n$ into four subgraphs, each containing no $C_6$.

```lean
theorem erdos_666 :
    ¬ ∀ ε : ℝ, 0 < ε → ∀ᶠ n : ℕ in atTop, ∀ H : SimpleGraph (Fin n → Bool), H ≤ hypercube n →
      ε * n * 2 ^ (n - 1 : ℕ) ≤ (H.edgeSet.ncard : ℝ) → (cycleGraph 6 ⊑ H)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/666.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/666.lean#L54).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/666.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/666.lean)
- [erdosproblems.com/666](https://www.erdosproblems.com/666)
