---
declaration: theorem
origin: cited
lean: Matrix.ProjectiveSpecialLinearGroup.isSimpleGroup_of_commutator_eq_top, TauCeti.GLSymplecticFin.isSimpleGroup_quotient_center
statement: formalized
proof: formalized
---

# Iwasawa's theorem for `PSL`

On at least two coordinates, the projective special linear
group is simple as soon as the special linear group is perfect.

```lean
Matrix.ProjectiveSpecialLinearGroup.isSimpleGroup_of_commutator_eq_top.{u_1, u_2} {ι : Type u_1}
  {F : Type u_2} [Fintype ι] [DecidableEq ι] [Field F] [Nontrivial ι]
  (h : commutator (Matrix.SpecialLinearGroup ι F) = ⊤) :
  IsSimpleGroup (Matrix.ProjectiveSpecialLinearGroup ι F)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Iwasawa's criterion for a quotient](../../group-theory/group-action/iwasawas-criterion-for-a-quotient.md)

## Lean

Formalized in Tau Ceti as [`Matrix.ProjectiveSpecialLinearGroup.isSimpleGroup_of_commutator_eq_top`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Projectivization/PSL/Simple.html#Matrix.ProjectiveSpecialLinearGroup.isSimpleGroup_of_commutator_eq_top).

## Other forms

**Iwasawa's theorem for the projective symplectic group.** Formalized in Tau Ceti as [`TauCeti.GLSymplecticFin.isSimpleGroup_quotient_center`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/GeneralLinearGroup/Symplectic/Simple.html#TauCeti.GLSymplecticFin.isSimpleGroup_quotient_center).

```lean
TauCeti.GLSymplecticFin.isSimpleGroup_quotient_center.{u} {K : Type u} [Field K] {m : ℕ} [NeZero m]
  (h : commutator ↥(TauCeti.GLSymplecticFin m K) = ⊤) :
  IsSimpleGroup (↥(TauCeti.GLSymplecticFin m K) ⧸ Subgroup.center ↥(TauCeti.GLSymplecticFin m K))
```

## Sources

- [Tau Ceti documentation: `Matrix.ProjectiveSpecialLinearGroup.isSimpleGroup_of_commutator_eq_top`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Projectivization/PSL/Simple.html#Matrix.ProjectiveSpecialLinearGroup.isSimpleGroup_of_commutator_eq_top)
- [Source of `Matrix.ProjectiveSpecialLinearGroup.isSimpleGroup_of_commutator_eq_top` in TauCeti/LinearAlgebra/Projectivization/PSL/Simple.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/Projectivization/PSL/Simple.lean#L117)
