---
declaration: theorem
origin: cited
lean: TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_demushkinCharacter_eq, TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_eq_zpowers_neg_one, TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_demushkinQ_eq, TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_demushkinCharacter_eq_of_odd, TauCeti.IsDemushkin.existsUnique_hasPrescriptionProperty
statement: formalized
proof: formalized
---

# Labute's Theorem 2

Let `r, r'` be relators of the free pro-`p` group `F` on `n`
generators whose presented groups are Demushkin groups whose canonical characters have the same
image. Then a continuous automorphism of `F` carries `r` to `r'`; in particular the closed normal
closures of `r` and `r'` are carried to each other, so two Demushkin relators with the same
invariants differ by a change of basis of `F`. The relators lie in `Φ(F)` and both groups have rank
`n` automatically (`TauCeti.IsDemushkin.mem_proPFrattini_of_presentedProP_singleton`).

```lean
TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_demushkinCharacter_eq {p : ℕ}
  [Fact (Nat.Prime p)] {n : ℕ} {r r' : TauCeti.freeProP p (Fin n)}
  (hG : TauCeti.IsDemushkin p (TauCeti.presentedProP p (Fin n) {r}))
  (hG' : TauCeti.IsDemushkin p (TauCeti.presentedProP p (Fin n) {r'}))
  (h : (TauCeti.demushkinCharacter hG).range = (TauCeti.demushkinCharacter hG').range) :
  ∃ e, e r = r'
```

## Depends on

- [The Demushkin predicate (Labute, p. 106), for a prime `p` and a topological group `G`](the-demushkin-predicate-labute-p-106-for-a-prime.md)

## Proof depends on

- [The abelianization structure theorem for one-relator pro-`p` groups](../../algebra/part-01/the-abelianization-structure-theorem-for-one-rel.md)
- [Burnside's basis theorem, cardinal form](../../algebra/part-01/burnsides-basis-theorem-cardinal-form.md)
- [Burnside's criterion modulo `λ_1`](../../algebra/part-01/burnsides-criterion-modulo-1.md)
- [The constrained successive-approximation theorem](the-constrained-successive-approximation-theorem.md)
- [Dedekind's modular law](../../../algebra/other-results/dedekinds-modular-law.md)
- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](../../algebra/part-01/the-first-isomorphism-theorem-for-a-surjective-s.md)
- [Labute's classification of the closed subgroups of `ℤ_2ˣ`](../../../number-theory/part-02/padics/labutes-classification-of-the-closed-subgroups-o.md)
- [Labute's criterion](labutes-criterion.md)
- [The necessity half of the existence theorem for `q ≠ 2` (Labute, Theorem 1)](the-necessity-half-of-the-existence-theorem-for.md)
- [The relative successive-approximation theorem](the-relative-successive-approximation-theorem.md)
- [The successive-approximation theorem with tails](../part-02/the-successive-approximation-theorem-with-tails.md)
- [The unconstrained successive-approximation theorem](the-unconstrained-successive-approximation-theor.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_demushkinCharacter_eq`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Uniqueness.html#TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_demushkinCharacter_eq).

## Other forms

**Labute's Theorem 2 at the even-rank dyadic endpoint.** Formalized in Tau Ceti as [`TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_eq_zpowers_neg_one`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Two/Even/Endpoint.html#TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_eq_zpowers_neg_one).

```lean
TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_eq_zpowers_neg_one {n : ℕ}
  (hn : Even n) {r r' : TauCeti.freeProP 2 (Fin n)}
  (hr : r ∈ TauCeti.proPFrattini 2 (TauCeti.freeProP 2 (Fin n)))
  (hr' : r' ∈ TauCeti.proPFrattini 2 (TauCeti.freeProP 2 (Fin n)))
  (hG : TauCeti.IsDemushkin 2 (TauCeti.presentedProP 2 (Fin n) {r}))
  (hG' : TauCeti.IsDemushkin 2 (TauCeti.presentedProP 2 (Fin n) {r'}))
  (hA : (TauCeti.demushkinCharacter hG).range = Subgroup.zpowers (-1))
  (hA' : (TauCeti.demushkinCharacter hG').range = Subgroup.zpowers (-1)) : ∃ e, e r = r'
```

**Labute's Theorem 2 for `q ≠ 2`.** Formalized in Tau Ceti as [`TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_demushkinQ_eq`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Uniqueness.html#TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_demushkinQ_eq).

```lean
TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_demushkinQ_eq {p : ℕ} [Fact (Nat.Prime p)]
  {n : ℕ} {r r' : TauCeti.freeProP p (Fin n)}
  (hr : r ∈ TauCeti.proPFrattini p (TauCeti.freeProP p (Fin n)))
  (hr' : r' ∈ TauCeti.proPFrattini p (TauCeti.freeProP p (Fin n)))
  (hG : TauCeti.IsDemushkin p (TauCeti.presentedProP p (Fin n) {r}))
  (hG' : TauCeti.IsDemushkin p (TauCeti.presentedProP p (Fin n) {r'}))
  (hq : TauCeti.demushkinQ hG = TauCeti.demushkinQ hG') (hq2 : TauCeti.demushkinQ hG ≠ 2) :
  ∃ e, e r = r'
```

**Labute's Theorem 2 for odd rank.** Formalized in Tau Ceti as [`TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_demushkinCharacter_eq_of_odd`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Uniqueness.html#TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_demushkinCharacter_eq_of_odd).

```lean
TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_demushkinCharacter_eq_of_odd {n : ℕ}
  (hn : Odd n) {r r' : TauCeti.freeProP 2 (Fin n)}
  (hr : r ∈ TauCeti.proPFrattini 2 (TauCeti.freeProP 2 (Fin n)))
  (hr' : r' ∈ TauCeti.proPFrattini 2 (TauCeti.freeProP 2 (Fin n)))
  (hG : TauCeti.IsDemushkin 2 (TauCeti.presentedProP 2 (Fin n) {r}))
  (hG' : TauCeti.IsDemushkin 2 (TauCeti.presentedProP 2 (Fin n) {r'}))
  (h : (TauCeti.demushkinCharacter hG).range = (TauCeti.demushkinCharacter hG').range) :
  ∃ e, e r = r'
```

**Labute's Theorem 4: a Demushkin group has exactly one continuous character with the prescription property.** Formalized in Tau Ceti as [`TauCeti.IsDemushkin.existsUnique_hasPrescriptionProperty`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/Character/Basic.html#TauCeti.IsDemushkin.existsUnique_hasPrescriptionProperty).

```lean
TauCeti.IsDemushkin.existsUnique_hasPrescriptionProperty.{v} {p : ℕ} [Fact (Nat.Prime p)]
  {G : Type v} [Group G] [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G]
  [TotallyDisconnectedSpace G] (hG : TauCeti.IsDemushkin p G) :
  ∃! χ, TauCeti.HasPrescriptionProperty χ
```

## Sources

- [Tau Ceti documentation: `TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_demushkinCharacter_eq`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Uniqueness.html#TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_demushkinCharacter_eq)
- [Source of `TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_demushkinCharacter_eq` in TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Uniqueness.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Uniqueness.lean#L130)
