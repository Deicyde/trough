---
declaration: theorem
origin: cited
lean: Erdos810.erdos_810
statement: formalized
---

# Erdős Problem 810

> *References:*
> - [erdosproblems.com/810](https://www.erdosproblems.com/810)
> - [BEGS89] Burr, S. A., Erdős, P., Graham, R. L., and Sós, V. T.,
>   *Maximal anti-Ramsey graphs and the strong chromatic number*.
>   J. Graph Theory 13 (1989), no. 3, 263–282.
> - [Er91] Erdős, P., *Problems and results in combinatorial analysis and combinatorial number
>   theory*. Graph theory, combinatorics, and applications, Vol. 1 (1991), 397–406.

*Quoted from [FormalConjectures/ErdosProblems/810.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/810.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/810](https://www.erdosproblems.com/810).

The file states 1 research or textbook statement: 1 open.

## `Erdos810.erdos_810`

Open: stated without proof.

> Does there exist some $\epsilon>0$ such that, for all sufficiently large $n$, there exists a
> graph $G$ on $n$ vertices with at least $\epsilon n^2$ edges whose edges can be coloured with $n$
> colours so that every $C_4$ receives four distinct colours?

```lean
theorem erdos_810 : ∃ ε > 0, ∀ᶠ n in atTop,
    ∃ G : SimpleGraph (Fin n), ∃ color : Fin n → Fin n → Fin n,
      ε * (n : ℝ) ^ 2 ≤ (G.edgeSet.ncard : ℝ) ∧ C4RainbowColoring G color
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/810.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/810.lean#L60).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/810.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/810.lean)
- [erdosproblems.com/810](https://www.erdosproblems.com/810)
