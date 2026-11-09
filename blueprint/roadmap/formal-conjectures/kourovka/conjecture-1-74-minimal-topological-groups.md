---
declaration: theorem
origin: cited
lean: Kourovka.«1.74».kourovka_1_74, Kourovka.«1.74».kourovka_1_74.variants.tarski_monster
statement: formalized
---

# Conjecture 1.74 (Minimal topological groups)

> by V. P. Platonov
>
> Describe all "minimal topological groups", that is, non-discrete Hausdorff
> topological groups all of whose proper closed subgroups are discrete. The
> minimal locally compact groups can be described without much effort, but the
> problem is probably complicated in the general case.
>
> A Tarski monster group equipped with a non-discrete Hausdorff group topology
> is a minimal topological group in this sense, since all its proper subgroups
> are finite (hence discrete in any Hausdorff group topology). Such topologizable
> Tarski monsters exist by a theorem of Klyachko, Olshanskii and Osin.
>
> *References:*
> - [The Kourovka Notebook](https://arxiv.org/abs/1401.0300v40)
> - A. A. Klyachko, A. Yu. Olshanskii, D. V. Osin, *On topologizable and
>   non-topologizable groups*, Topology Appl. 160 (2013), 2104–2120,
>   [arXiv:1210.7895](https://arxiv.org/abs/1210.7895), Theorem 1.4.

*Quoted from [FormalConjectures/Kourovka/1_74.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Kourovka/1_74.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Kourovka.«1.74».kourovka_1_74`

Open: stated without proof.

> Describe all minimal topological groups, that is, all non-discrete Hausdorff
> topological groups whose proper closed subgroups are all discrete.

```lean
theorem kourovka_1_74 :
    ∀ (G : Type) [Group G] [TopologicalSpace G],
      IsMinimalTopologicalGroup G ↔
        kourovka_1_74.answer G
```

Category `research open`; AMS [20 Group theory and generalizations](../by-subject/part-01/20-group-theory-and-generalizations/README.md), [22 Topological groups, Lie groups](../by-subject/part-01/22-topological-groups-lie-groups/README.md). Declared in [FormalConjectures/Kourovka/1_74.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Kourovka/1_74.lean#L61).

## `Kourovka.«1.74».kourovka_1_74.variants.tarski_monster`

Solved: stated here without proof.

> There exists a Tarski monster group that admits a non-discrete Hausdorff group
> topology. This follows from Theorem 1.4 of Klyachko, Olshanskii and Osin, which
> gives a topologizable Tarski monster of every sufficiently large odd exponent $n$;
> taking $n$ to be a prime $p$ makes every non-trivial proper subgroup cyclic of
> order $p$. Any such group is a minimal topological group.

```lean
theorem kourovka_1_74.variants.tarski_monster :
    ∃ (G : Type) (_ : Group G) (_ : TopologicalSpace G),
      IsTarskiMonster G ∧ IsTopologicalGroup G ∧ T2Space G ∧
      ¬ DiscreteTopology G
```

Category `research solved`; AMS [20 Group theory and generalizations](../by-subject/part-01/20-group-theory-and-generalizations/README.md), [22 Topological groups, Lie groups](../by-subject/part-01/22-topological-groups-lie-groups/README.md). Declared in [FormalConjectures/Kourovka/1_74.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Kourovka/1_74.lean#L83).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Kourovka/1_74.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Kourovka/1_74.lean)
- [The Kourovka Notebook](https://arxiv.org/abs/1401.0300v40)
