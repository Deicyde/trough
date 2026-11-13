---
declaration: theorem
origin: cited
lean: Erdos618.erdos_618
statement: formalized
---

# Erdős Problem 618

> *References:*
> - [erdosproblems.com/618](https://www.erdosproblems.com/618)
> - [Er99] Erdős, Paul, *A selection of problems and results in combinatorics*. Combin. Probab.
>   Comput. (1999), 1-6.
> - [EGR98] Erdős, Paul and Gyárfás, András and Ruszinkó, Miklós, *How to decrease the diameter
>   of triangle-free graphs*. Combinatorica (1998), 493-501.

*Quoted from [FormalConjectures/ErdosProblems/618.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/618.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/618](https://www.erdosproblems.com/618).

The file states 1 research or textbook statement: 1 solved.

## `Erdos618.erdos_618`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos618.lean](https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos618.lean).

> For a triangle-free graph $G$ let $h_2(G)$ be the smallest number of edges that need to be
> added to $G$ so that it has diameter $2$ and is still triangle-free. Is it true that if $G$
> has maximum degree $o(n^{1/2})$ then $h(G)=o(n^2)$?
>
> A problem of Erdős, Gyárfás, and Ruszinkó [EGR98]. Simonovits showed that there exist graphs
> $G$ with maximum degree $\gg n^{1/2}$ and $h_2(G)\gg n^2$. Alon has observed this problem is
> essentially identical to [134], and his solution in
> [this note](https://web.math.princeton.edu/~nalon/PDFS/remark1901.pdf) also solves this
> problem in the affirmative.

```lean
theorem erdos_618 :
    ∀ (G : ∀ n : ℕ, SimpleGraph (Fin n)),
      (∀ n, (G n).CliqueFree 3) →
      (fun n => ((G n).maxDegree : ℝ)) =o[atTop] (fun n => (n : ℝ) ^ ((1 : ℝ) / 2)) →
      (fun n => (h2 (G n) : ℝ)) =o[atTop] (fun n => (n : ℝ) ^ 2)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/618.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/618.lean#L63).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/618.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/618.lean)
- [erdosproblems.com/618](https://www.erdosproblems.com/618)
