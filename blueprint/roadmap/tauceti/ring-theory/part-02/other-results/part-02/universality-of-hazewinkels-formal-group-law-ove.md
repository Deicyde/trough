---
declaration: theorem
origin: cited
lean: TauCeti.existsUnique_eq_hazewinkelFormalGroup
statement: formalized
proof: formalized
---

# Universality of Hazewinkel's formal group law over `ℚ`-algebras

a formal group law over a
`ℚ`-algebra whose logarithm has no terms outside the degrees `pⁿ` is Hazewinkel's formal group law
of a unique family `v`.

```lean
TauCeti.existsUnique_eq_hazewinkelFormalGroup.{u_1} {K : Type u_1} [CommRing K] [Algebra ℚ K]
  {p : ℕ} (hp : 1 < p) {F : FormalGroup K}
  (hF : ∀ (k : ℕ), (∀ (n : ℕ), p ^ n ≠ k) → (PowerSeries.coeff k) F.log = 0) :
  ∃! v, F = TauCeti.hazewinkelFormalGroup p v
```

## Depends on

- [TauCeti.FormalCoordinate](../../../part-01/formal-laurent-fields-puiseux-expansions-and-con/tauceti-formalcoordinate.md)

## Proof depends on

- [TauCeti.FormalGroupHom](../../../part-01/bordism-formal-groups-and-chromatic-operations/tauceti-formalgrouphom.md)
- [TauCeti.FormalGroupIso](../../../part-01/bordism-formal-groups-and-chromatic-operations/tauceti-formalgroupiso.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.existsUnique_eq_hazewinkelFormalGroup`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/Hazewinkel/Basic.html#TauCeti.existsUnique_eq_hazewinkelFormalGroup).

## Sources

- [Tau Ceti documentation: `TauCeti.existsUnique_eq_hazewinkelFormalGroup`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/Hazewinkel/Basic.html#TauCeti.existsUnique_eq_hazewinkelFormalGroup)
- [Source of `TauCeti.existsUnique_eq_hazewinkelFormalGroup` in TauCeti/RingTheory/FormalGroup/Hazewinkel/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/FormalGroup/Hazewinkel/Basic.lean#L341)
