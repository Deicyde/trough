---
declaration: theorem
origin: cited
lean: TauCeti.IsDemushkin.profiniteIndex_subgroupOf_map_powMonoidHom_range_lt_of_demushkinQ_ne_two, TauCeti.IsDemushkin.profiniteIndex_subgroupOf_map_powMonoidHom_range_lt_of_even_demushkinRank, TauCeti.IsDemushkin.range_demushkinCharacter_eq_zpowers_neg_one_or_unitsPlusMinus_of_odd_demushkinRank, TauCeti.freeProP.range_demushkinCharacter_eq_zpowers_neg_one_or_unitsPlusMinus_of_odd
statement: formalized
proof: formalized
---

# The necessity half of the existence theorem for `q ≠ 2` (Labute, Theorem 1)

For a
Demushkin group `G` of rank `n` with `q(G) ≠ 2`, the image `A` of its canonical character has
`(A : A^p) < p ^ n`. Indeed `A` is trivial, with `(A : A^p) = 1`, or the principal unit group
`1 + qℤ_p`, with `(A : A^p) = p`, while `n ≥ 2`. Together with the parity of the rank
(`TauCeti.IsDemushkin.even_demushkinRank_of_demushkinQ_ne_two`), this places `(n, A)` in the first
situation of the existence theorem.

```lean
TauCeti.IsDemushkin.profiniteIndex_subgroupOf_map_powMonoidHom_range_lt_of_demushkinQ_ne_two.{u_1}
  {p : ℕ} [hp : Fact (Nat.Prime p)] {G : Type u_1} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] [CompactSpace G] [TotallyDisconnectedSpace G]
  (hG : TauCeti.IsDemushkin p G) (hq2 : TauCeti.demushkinQ hG ≠ 2) :
  ((Subgroup.map (powMonoidHom p) (TauCeti.demushkinCharacter hG).range).subgroupOf
        (TauCeti.demushkinCharacter hG).range).profiniteIndex <
    TauCeti.Supernatural.primePower ⟨p, ⋯⟩ ↑(TauCeti.demushkinRank hG)
```

## Depends on

- [The Demushkin predicate](the-demushkin-predicate.md)

## Proof depends on

- [The abelianization structure theorem for one-relator pro-`p` groups](../algebra/part-01/the-abelianization-structure-theorem-for-one-rel.md)
- [Burnside's basis theorem, cardinal form](../algebra/part-01/burnsides-basis-theorem-cardinal-form.md)
- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](../algebra/part-01/the-first-isomorphism-theorem-for-a-surjective-s.md)
- [Labute's classification of the closed subgroups of `ℤ_2ˣ`](../../number-theory/part-02/padics/labutes-classification-of-the-closed-subgroups-o.md)
- [Labute's criterion](labutes-criterion.md)
- [The relative successive-approximation theorem](the-relative-successive-approximation-theorem.md)
- [The successive-approximation theorem with tails](../algebra/part-01/the-successive-approximation-theorem-with-tails.md)
- [The third isomorphism theorem for coset spaces](../../group-theory/other-results/the-third-isomorphism-theorem-for-coset-spaces.md)

## Informally uses

- [Labute's Theorem 2](labutes-theorem-2.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsDemushkin.profiniteIndex_subgroupOf_map_powMonoidHom_range_lt_of_demushkinQ_ne_two`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Existence.html#TauCeti.IsDemushkin.profiniteIndex_subgroupOf_map_powMonoidHom_range_lt_of_demushkinQ_ne_two).

## Other forms

**The necessity half of the existence theorem for even rank (Labute, Theorem 1 and Remark 2; Serre, Theorem 3.2).** Formalized in Tau Ceti as [`TauCeti.IsDemushkin.profiniteIndex_subgroupOf_map_powMonoidHom_range_lt_of_even_demushkinRank`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Two/Even/Image.html#TauCeti.IsDemushkin.profiniteIndex_subgroupOf_map_powMonoidHom_range_lt_of_even_demushkinRank).

```lean
TauCeti.IsDemushkin.profiniteIndex_subgroupOf_map_powMonoidHom_range_lt_of_even_demushkinRank.{u}
  {G : Type u} [Group G] [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G]
  [TotallyDisconnectedSpace G] {p : ℕ} [hp : Fact (Nat.Prime p)] (hG : TauCeti.IsDemushkin p G)
  (hn : Even (TauCeti.demushkinRank hG)) :
  ((Subgroup.map (powMonoidHom p) (TauCeti.demushkinCharacter hG).range).subgroupOf
        (TauCeti.demushkinCharacter hG).range).profiniteIndex <
    TauCeti.Supernatural.primePower ⟨p, ⋯⟩ ↑(TauCeti.demushkinRank hG)
```

**The necessity half of the existence theorem for odd rank (Labute, Theorem 1 and Remark 2; Serre, Theorem 3.2).** Formalized in Tau Ceti as [`TauCeti.IsDemushkin.range_demushkinCharacter_eq_zpowers_neg_one_or_unitsPlusMinus_of_odd_demushkinRank`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Two/Odd/Image.html#TauCeti.IsDemushkin.range_demushkinCharacter_eq_zpowers_neg_one_or_unitsPlusMinus_of_odd_demushkinRank).

```lean
TauCeti.IsDemushkin.range_demushkinCharacter_eq_zpowers_neg_one_or_unitsPlusMinus_of_odd_demushkinRank.{u}
  {G : Type u} [Group G] [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G]
  [TotallyDisconnectedSpace G] (hG : TauCeti.IsDemushkin 2 G)
  (hn : Odd (TauCeti.demushkinRank hG)) :
  (TauCeti.demushkinCharacter hG).range = Subgroup.zpowers (-1) ∨
    3 ≤ TauCeti.demushkinRank hG ∧
      ∃ f, 2 ≤ f ∧ (TauCeti.demushkinCharacter hG).range = TauCeti.unitsPlusMinus f
```

**The necessity half of the existence theorem for odd rank, relator form (Labute, Theorem 1 and Remark 2).** Formalized in Tau Ceti as [`TauCeti.freeProP.range_demushkinCharacter_eq_zpowers_neg_one_or_unitsPlusMinus_of_odd`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Two/Odd/Image.html#TauCeti.freeProP.range_demushkinCharacter_eq_zpowers_neg_one_or_unitsPlusMinus_of_odd).

```lean
TauCeti.freeProP.range_demushkinCharacter_eq_zpowers_neg_one_or_unitsPlusMinus_of_odd {n : ℕ}
  (hn : Odd n) {r : TauCeti.freeProP 2 (Fin n)}
  (hr : r ∈ TauCeti.proPFrattini 2 (TauCeti.freeProP 2 (Fin n)))
  (hG : TauCeti.IsDemushkin 2 (TauCeti.presentedProP 2 (Fin n) {r})) :
  (TauCeti.demushkinCharacter hG).range = Subgroup.zpowers (-1) ∨
    3 ≤ n ∧ ∃ f, 2 ≤ f ∧ (TauCeti.demushkinCharacter hG).range = TauCeti.unitsPlusMinus f
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsDemushkin.profiniteIndex_subgroupOf_map_powMonoidHom_range_lt_of_demushkinQ_ne_two`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Existence.html#TauCeti.IsDemushkin.profiniteIndex_subgroupOf_map_powMonoidHom_range_lt_of_demushkinQ_ne_two)
- [Source of `TauCeti.IsDemushkin.profiniteIndex_subgroupOf_map_powMonoidHom_range_lt_of_demushkinQ_ne_two` in TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Existence.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Existence.lean#L542)
