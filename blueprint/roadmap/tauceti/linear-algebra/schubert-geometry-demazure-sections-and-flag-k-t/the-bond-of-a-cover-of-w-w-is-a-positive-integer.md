---
declaration: theorem
origin: cited
lean: TauCeti.exists_nat_reflectionBond_eq_of_minimalCosetRepCovBy
statement: formalized
proof: formalized
---

# The bond of a cover of `W / W_λ` is a positive integer when the dominant weight `λ` is integral, that is when every simple coroot takes an integer value on `λ`

```lean
TauCeti.exists_nat_reflectionBond_eq_of_minimalCosetRepCovBy.{u, v, w, x} {ι : Type u} {R : Type v}
  {M : Type w} {N : Type x} [CommRing R] [CharZero R] [AddCommGroup M] [_root_.Module R M]
  [AddCommGroup N] [_root_.Module R N] {P : RootPairing ι R M N} {b : P.Base} [LinearOrder R]
  [IsStrictOrderedRing R] [Finite ι] [P.IsCrystallographic] [P.IsReduced] [P.flip.IsReduced]
  {lam : M} (hlam : lam ∈ P.dominantChamber b) (hint : ∀ i ∈ b.support, ∃ z, (P.coroot' i) lam = ↑z)
  {x y : ↥P.weylGroup}
  (h : (TauCeti.weylCoxeterSystem P b).MinimalCosetRepCovBy (P.wallIndices b lam) y x) :
  ∃ n, 0 < n ∧ P.reflectionBond b (x • lam) (y • lam) = ↑n
```

## Depends on

- [CoxeterSystem.MinimalCosetRepCovBy](coxetersystem-minimalcosetrepcovby.md)
- [RootPairing.reflectionBond](rootpairing-reflectionbond.md)

## Proof depends on

- [A cover of `W / W_λ` has a unique positive root label](a-cover-of-w-w-has-a-unique-positive-root-label.md)
- [The stabilizer of a dominant weight is a standard parabolic subgroup](the-stabilizer-of-a-dominant-weight-is-a-standar.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_nat_reflectionBond_eq_of_minimalCosetRepCovBy`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/Weyl/CoverBond.html#TauCeti.exists_nat_reflectionBond_eq_of_minimalCosetRepCovBy).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_nat_reflectionBond_eq_of_minimalCosetRepCovBy`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/Weyl/CoverBond.html#TauCeti.exists_nat_reflectionBond_eq_of_minimalCosetRepCovBy)
- [Source of `TauCeti.exists_nat_reflectionBond_eq_of_minimalCosetRepCovBy` in TauCeti/LinearAlgebra/RootSystem/Weyl/CoverBond.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/RootSystem/Weyl/CoverBond.lean#L160)
- [Tau Ceti roadmap status: Schubert geometry, Demazure sections and flag K-theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SchubertGeometry/STATUS.md)
