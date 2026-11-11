---
declaration: theorem
origin: cited
lean: TauCeti.existsUnique_isPos_reflection_smul_eq_of_minimalCosetRepCovBy
statement: formalized
proof: formalized
---

# A cover of `W / W_λ` has a unique positive root label

If `y` is covered by `x` in the
Bruhat order of the minimal coset representatives of the stabilizer of the dominant weight `λ`,
there is exactly one positive root `β` with `y λ = s_β (x λ)`.

```lean
TauCeti.existsUnique_isPos_reflection_smul_eq_of_minimalCosetRepCovBy.{u, v, w, x} {ι : Type u}
  {R : Type v} {M : Type w} {N : Type x} [CommRing R] [CharZero R] [AddCommGroup M]
  [_root_.Module R M] [AddCommGroup N] [_root_.Module R N] {P : RootPairing ι R M N} {b : P.Base}
  [LinearOrder R] [IsStrictOrderedRing R] [Finite ι] [P.IsCrystallographic] [P.IsReduced]
  [P.flip.IsReduced] {lam : M} (hlam : lam ∈ P.dominantChamber b) {x y : ↥P.weylGroup}
  (h : (TauCeti.weylCoxeterSystem P b).MinimalCosetRepCovBy (P.wallIndices b lam) y x) :
  ∃! β, b.IsPos β ∧ (P.reflection β) (x • lam) = y • lam
```

## Depends on

- [CoxeterSystem.MinimalCosetRepCovBy](coxetersystem-minimalcosetrepcovby.md)

## Proof depends on

- [The stabilizer of a dominant weight is a standard parabolic subgroup](the-stabilizer-of-a-dominant-weight-is-a-standar.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.existsUnique_isPos_reflection_smul_eq_of_minimalCosetRepCovBy`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/Weyl/CoverBond.html#TauCeti.existsUnique_isPos_reflection_smul_eq_of_minimalCosetRepCovBy).

## Sources

- [Tau Ceti documentation: `TauCeti.existsUnique_isPos_reflection_smul_eq_of_minimalCosetRepCovBy`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/Weyl/CoverBond.html#TauCeti.existsUnique_isPos_reflection_smul_eq_of_minimalCosetRepCovBy)
- [Source of `TauCeti.existsUnique_isPos_reflection_smul_eq_of_minimalCosetRepCovBy` in TauCeti/LinearAlgebra/RootSystem/Weyl/CoverBond.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/RootSystem/Weyl/CoverBond.lean#L114)
- [Tau Ceti roadmap status: Schubert geometry, Demazure sections and flag K-theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SchubertGeometry/STATUS.md)
