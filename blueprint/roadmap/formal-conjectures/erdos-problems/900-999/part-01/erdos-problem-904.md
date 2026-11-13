---
declaration: theorem
origin: cited
lean: Erdos904.erdos_904
statement: formalized
---

# Erdős Problem 904

> *References:*
> - [erdosproblems.com/904](https://www.erdosproblems.com/904)
> - [BoEr75] Bollobás, B. and Erdős, P., *Unsolved Problems*. Proc. Fifth British Combinatorial Conf. (1975), 678-680.
> - [Er75] Erdős, P., *Some recent progress on extremal problems in graph theory*. Congr. Numer. (1975), 3-14.
> - [Ed78] Edwards, C. S., *Complete subgraphs with largest sum of vertex degrees*. (1978), 293-306.
> - [Fa92] Faudree, Ralph J., *Complete subgraphs with large degree sums*. J. Graph Theory (1992), 327-334.
> - [BoNi05] Bollobás, Béla and Nikiforov, Vladimir, *The sum of degrees in cliques*. Electron. J. Combin. (2005), Note 21, 10.

*Quoted from [FormalConjectures/ErdosProblems/904.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/904.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/904](https://www.erdosproblems.com/904).

The file states 1 research or textbook statement: 1 solved.

## `Erdos904.erdos_904`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos904.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos904.lean).

> Let $r\geq 2$ and let $t_r(n)$ be the Turán number (the maximal number of edges in a graph on $n$
> vertices with no $K_{r+1}$).
>
> If $G$ is a graph with $n$ vertices and $m\geq t_r(n)$ edges there exists a clique on $r$ vertices,
> say $x_1,\ldots,x_r$, such that
>
> $$d(x_1)+\cdots+d(x_r)\geq \frac{2rm}{n}.$$
>
> A conjecture of Bollobás and Erdős. This was conjectured in [Er75] only in the special case $r=3$. Edwards [Ed78] proved the conjecture for $2\leq r\leq 8$ (under the additional assumption that $n\geq r^2$). Faudree [Fa92] proved the conjecture for all $r\geq 2$ provided $n>\frac{r-1}{4}r^2$. The full conjecture was proved by Bollobás and Nikiforov [BoNi05].

```lean
theorem erdos_904 :
    ∀ (V : Type*) [Fintype V] (G : SimpleGraph V) [DecidableRel G.Adj]
      (r : ℕ) (hr : r ∈ Set.Icc 1 (n V)) (hm : turanNumber (n V) r ≤ #G.edgeFinset),
      ∃ s, G.IsNClique r s ∧ 2 * r * #G.edgeFinset ≤ n V * ∑ v ∈ s, G.degree v
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/904.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/904.lean#L55).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/904.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/904.lean)
- [erdosproblems.com/904](https://www.erdosproblems.com/904)
