---
declaration: theorem
origin: cited
lean: LeinsterGroup.infinitely_many_leinster_groups, LeinsterGroup.abelian_is_leinster_iff_cyclic_perfect, LeinsterGroup.exists_nonabelian_leinster_group, LeinsterGroup.dihedral_is_leinster_iff_odd_perfect
statement: formalized
---

# Leinster Groups

> A finite group is a Leinster group if the sum of the orders of all its normal subgroups
> equals twice the group's order.
>
> *References:*
> * [Wikipedia](https://en.wikipedia.org/wiki/Leinster_group)
> * Leinster, Tom (2001). "Perfect numbers and groups".
>   [arXiv:math/0104012](https://arxiv.org/abs/math/0104012)
>
> TODO: The following properties from the Wikipedia article can also be formalized:
> - There are no Leinster groups that are symmetric or alternating.
> - There is no Leinster group of order p²q² where p, q are primes.
> - No finite semi-simple group is Leinster.
> - No p-group can be a Leinster group.
> - All abelian Leinster groups are cyclic with order equal to a perfect number.

*Quoted from [FormalConjectures/Wikipedia/LeinsterGroup.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/LeinsterGroup.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 1 open and 3 solved. It also has 1 API statement, counted here but not shown.

## `LeinsterGroup.infinitely_many_leinster_groups`

Open: stated without proof.

> **Conjecture:** Are there infinitely many Leinster groups?
>
> This asks whether there exist infinitely many (non-isomorphic) finite groups that are
> Leinster groups.
>
> Formalized via the negation of "Does there exist an n such that all Leinster groups have
> order less than n".

```lean
theorem infinitely_many_leinster_groups :
    ¬∃ n : ℕ, ∀ G : Type, ∀ (_ : Group G) (_ : Fintype G),
      IsLeinster G → Fintype.card G < n
```

Category `research open`; AMS [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/Wikipedia/LeinsterGroup.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/LeinsterGroup.lean#L61).

## `LeinsterGroup.abelian_is_leinster_iff_cyclic_perfect`

Solved: stated here without proof.

> An abelian group is a Leinster group if and only if it is cyclic with order equal
> to a perfect number.
>
> Reference: Leinster, Tom (2001). "Perfect numbers and groups". Theorem 2.1.

```lean
theorem abelian_is_leinster_iff_cyclic_perfect (G : Type*) [CommGroup G] [Fintype G] :
    IsLeinster G ↔ IsCyclic G ∧ Nat.Perfect (Fintype.card G)
```

Category `research solved`; AMS [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/Wikipedia/LeinsterGroup.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/LeinsterGroup.lean#L86).

## `LeinsterGroup.exists_nonabelian_leinster_group`

Solved: stated here without proof.

> Non-abelian Leinster groups exist.
>
> For example, `S₃ × C₅` (order 30) and `A₅ × C₁₅₁₂₈` are Leinster groups.
>
> Reference: Leinster, Tom (2001). "Perfect numbers and groups".

```lean
theorem exists_nonabelian_leinster_group :
    ∃ G : Type, ∃ (_ : Group G) (_ : Fintype G),
      IsLeinster G ∧ ¬ ∀ (a b : G), a * b = b * a
```

Category `research solved`; AMS [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/Wikipedia/LeinsterGroup.lean, line 98](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/LeinsterGroup.lean#L98).

## `LeinsterGroup.dihedral_is_leinster_iff_odd_perfect`

Solved: stated here without proof.

> The dihedral group `DihedralGroup n` (of order `2n`) is a Leinster group if and only if `n` is
> an odd perfect number. This gives a one-to-one correspondence between dihedral Leinster groups
> and odd perfect numbers.
>
> In particular, the existence of odd perfect numbers is equivalent to the existence of
> dihedral Leinster groups.
>
> Reference: Leinster, Tom (2001). "Perfect numbers and groups".

```lean
theorem dihedral_is_leinster_iff_odd_perfect (n : ℕ) [NeZero n] :
    IsLeinster (DihedralGroup n) ↔ Nat.Perfect n ∧ Odd n
```

Category `research solved`; AMS [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/Wikipedia/LeinsterGroup.lean, line 114](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/LeinsterGroup.lean#L114).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/LeinsterGroup.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/LeinsterGroup.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Leinster_group)
