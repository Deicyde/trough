---
declaration: theorem
origin: cited
lean: Erdos572.erdos_572
statement: formalized
---

# Erdős Problem 572

> *References:*
> - [erdosproblems.com/572](https://www.erdosproblems.com/572)
> - [Er64c] Erdős, P., Extremal problems in graph theory. Theory of Graphs and its
>   Applications (1964), 29-36.
> - [BoSi74] Bondy, J. A. and Simonovits, M., Cycles of even length in graphs.
>   J. Combin. Theory Ser. B (1974), 97-105.
> - [LUW95] Lazebnik, F., Ustimenko, V. A. and Woldar, A. J., A new series of dense graphs
>   of high girth. Bull. Amer. Math. Soc. (N.S.) (1995), 73-79.

*Quoted from [FormalConjectures/ErdosProblems/572.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/572.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/572](https://www.erdosproblems.com/572).

The file states 1 research or textbook statement: 1 open.

## `Erdos572.erdos_572`

Open: stated without proof.

> Show that for $k\geq 3$
>
> $$\mathrm{ex}(n;C_{2k})\gg n^{1+\frac{1}{k}}.$$
>
> This problem is #46 in Extremal Graph Theory in the graphs problem collection.

```lean
theorem erdos_572 (k : ℕ) (hk : 3 ≤ k) :
    ∃ c > (0 : ℝ), ∀ᶠ (n : ℕ) in atTop,
      c * (n : ℝ) ^ (1 + 1 / (k : ℝ)) ≤
        (SimpleGraph.extremalNumber n (SimpleGraph.cycleGraph (2 * k)) : ℝ)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/572.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/572.lean#L46).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/572.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/572.lean)
- [erdosproblems.com/572](https://www.erdosproblems.com/572)
