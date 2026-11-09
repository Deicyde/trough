---
declaration: theorem
origin: cited
lean: TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_demushkinCharacter_eq
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

- [The Demushkin predicate](the-demushkin-predicate.md)

## Proof depends on

- [The abelianization structure theorem for one-relator pro-`p` groups](../../algebra/part-01/the-abelianization-structure-theorem-for-one-rel.md)
- [Burnside's basis theorem, cardinal form](../../algebra/part-01/burnsides-basis-theorem-cardinal-form.md)
- [Burnside's criterion modulo `λ_1`](../../algebra/part-01/burnsides-criterion-modulo-1.md)
- [The constrained successive-approximation theorem](the-constrained-successive-approximation-theorem.md)
- [Dedekind's modular law](../../../algebra/other-results/dedekinds-modular-law.md)
- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](../../algebra/part-01/the-first-isomorphism-theorem-for-a-surjective-s.md)
- [Labute's classification of the closed subgroups of `ℤ_2ˣ`](../../../number-theory/part-02/padics/labutes-classification-of-the-closed-subgroups-o.md)
- [Labute's criterion](labutes-criterion.md)
- [Labute's Theorem 2 at the even-rank dyadic endpoint](../../algebra/part-01/labutes-theorem-2-at-the-even-rank-dyadic-endpoi.md)
- [Labute's Theorem 2 for `q ≠ 2`](labutes-theorem-2-for-q-2.md)
- [Labute's Theorem 2 for odd rank](labutes-theorem-2-for-odd-rank.md)
- [Labute's Theorem 4: a Demushkin group has exactly one continuous character with the prescription property](../../algebra/part-01/labutes-theorem-4-a-demushkin-group-has-exactly.md)
- [The relative successive-approximation theorem](../part-02/the-relative-successive-approximation-theorem.md)
- [The successive-approximation theorem with tails](../../algebra/part-02/the-successive-approximation-theorem-with-tails.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_demushkinCharacter_eq`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Uniqueness.html#TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_demushkinCharacter_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_demushkinCharacter_eq`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Uniqueness.html#TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_demushkinCharacter_eq)
- [Source of `TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_demushkinCharacter_eq` in TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Uniqueness.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Uniqueness.lean#L130)
