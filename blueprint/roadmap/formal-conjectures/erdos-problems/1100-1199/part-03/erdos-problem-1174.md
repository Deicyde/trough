---
declaration: theorem
origin: cited
lean: Erdos1174.erdos_1174.parts.i, Erdos1174.erdos_1174.parts.ii
statement: formalized
---

# Erdős Problem 1174

> *References:*
> - [erdosproblems.com/1174](https://www.erdosproblems.com/1174)
> - [Va99] Various, *Some of Paul's favorite problems*. Booklet produced for the conference
>   "Paul Erdős and his mathematics", Budapest, July 1999 (1999), problem 7.91.

*Quoted from [FormalConjectures/ErdosProblems/1174.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1174.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1174](https://www.erdosproblems.com/1174).

The file states 2 research or textbook statements: 2 open. It also has 2 test statements, counted here but not shown.

## `Erdos1174.erdos_1174.parts.i`

Open: stated without proof.

> **Erdős Problem 1174, part (i)** [Va99, 7.91]. A problem of Erdős and Hajnal:
> does there exist a graph $G$ with no $K_4$ such that every edge colouring of $G$
> with countably many colours contains a monochromatic $K_3$?
>
> For simplicity the colourings are given on all unordered pairs $\operatorname{Sym}_2(V)$;
> only the values on the edges of $G$ matter, since a monochromatic triangle is witnessed by
> edges alone.
>
> Shelah proved that a graph with this property can consistently exist, so the
> problem is not disprovable in ZFC; whether such a graph exists outright remains open.

```lean
theorem erdos_1174.parts.i :
    ∃ (V : Type) (G : SimpleGraph V), G.CliqueFree 4 ∧
      ∀ c : Sym2 V → ℕ, ∃ x y z : V,
        G.Adj x y ∧ G.Adj y z ∧ G.Adj x z ∧
        c s(x, y) = c s(y, z) ∧ c s(y, z) = c s(x, z)
```

Category `research open`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1174.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1174.lean#L50).

## `Erdos1174.erdos_1174.parts.ii`

Open: stated without proof.

> **Erdős Problem 1174, part (ii)** [Va99, 7.91]. A problem of Erdős and Hajnal:
> does there exist a graph $G$ with no $K_{\aleph_1}$ (that is, every clique of $G$
> is countable) such that every edge colouring of $G$ with countably many colours
> contains a monochromatic $K_{\aleph_0}$ (an infinite clique all of whose edges
> receive the same colour)?
>
> For simplicity the colourings are given on all unordered pairs $\operatorname{Sym}_2(V)$;
> only the values on the edges of $G$ matter.
>
> Shelah proved that a graph with this property can consistently exist, so the
> problem is not disprovable in ZFC; whether such a graph exists outright remains open.

```lean
theorem erdos_1174.parts.ii :
    ∃ (V : Type) (G : SimpleGraph V),
      (∀ S : Set V, G.IsClique S → #S ≤ ℵ₀) ∧
      ∀ c : Sym2 V → ℕ, ∃ S : Set V, G.IsClique S ∧ S.Infinite ∧
        ∃ k : ℕ, ∀ x ∈ S, ∀ y ∈ S, x ≠ y → c s(x, y) = k
```

Category `research open`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1174.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1174.lean#L71).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1174.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1174.lean)
- [erdosproblems.com/1174](https://www.erdosproblems.com/1174)
