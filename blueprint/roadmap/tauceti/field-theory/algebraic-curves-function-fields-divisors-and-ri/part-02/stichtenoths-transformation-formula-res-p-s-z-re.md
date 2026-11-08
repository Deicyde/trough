---
declaration: theorem
origin: cited
lean: TauCeti.Place.residue_eq_residue_mul, TauCeti.Place.residueResidueField_eq_residueResidueField_mul_derivativeOfSeparating, TauCeti.Place.residue_eq_residue_mul_derivativeOfSeparating
statement: formalized
proof: formalized
---

# Stichtenoth's transformation formula `res_{P,s}(z) = res_{P,t}(z · ds/dt)`

if the
Laurent expansion of `w` in `t` is the derivative of that of `s`, then the residue of `z` with
respect to `s` is the residue of `z * w` with respect to `t`.

```lean
TauCeti.Place.residue_eq_residue_mul.{u_1, u_2} {k : Type u_1} {F : Type u_2} [Field k] [Field F]
  [Algebra k F] (P : TauCeti.Place k F) {s t : F} (hP : P.degree = 1) (ht : P.ord t = 1)
  (hs : P.ord s = 1) {w : F}
  (hw :
    (P.laurentSeriesExpansion hP ht) w =
      (LaurentSeries.derivative k) ((P.laurentSeriesExpansion hP ht) s))
  (z : F) : (P.residue hP hs) z = (P.residue hP ht) (z * w)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Place.residue_eq_residue_mul`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Place/Expansion/Laurent/ChangeOfUniformizer.html#TauCeti.Place.residue_eq_residue_mul).

## Other forms

**Stichtenoth's transformation formula `res_{P,s}(z) = res_{P,t}(z · ds/dt)` at a place with separable residue field, for two uniformizers `s` and `t` with `t` separating, the residues taking values in `F_P` (Proposition 4.2.9).** Formalized in Tau Ceti as [`TauCeti.Place.residueResidueField_eq_residueResidueField_mul_derivativeOfSeparating`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Place/Expansion/Laurent/Derivative.html#TauCeti.Place.residueResidueField_eq_residueResidueField_mul_derivativeOfSeparating).

```lean
TauCeti.Place.residueResidueField_eq_residueResidueField_mul_derivativeOfSeparating.{u_1, u_2}
  {k : Type u_1} {F : Type u_2} [Field k] [Field F] [Algebra k F] (P : TauCeti.Place k F) {s t : F}
  (ht : P.ord t = 1) [Algebra.IsSeparable k P.ResidueField] (htr : Transcendental k t)
  [Algebra.IsSeparable (↥k⟮t⟯) F] (hs : P.ord s = 1) (z : F) :
  (P.residueResidueField hs) z =
    (P.residueResidueField ht) (z * (TauCeti.derivativeOfSeparating htr) s)
```

**Stichtenoth's transformation formula `res_{P,s}(z) = res_{P,t}(z · ds/dt)` for two uniformizers `s` and `t` at a rational place, with `t` separating (Proposition 4.2.9).** Formalized in Tau Ceti as [`TauCeti.Place.residue_eq_residue_mul_derivativeOfSeparating`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Place/Expansion/Laurent/Derivative.html#TauCeti.Place.residue_eq_residue_mul_derivativeOfSeparating).

```lean
TauCeti.Place.residue_eq_residue_mul_derivativeOfSeparating.{u_1, u_2} {k : Type u_1} {F : Type u_2}
  [Field k] [Field F] [Algebra k F] (P : TauCeti.Place k F) {s t : F} (hP : P.degree = 1)
  (ht : P.ord t = 1) (htr : Transcendental k t) [Algebra.IsSeparable (↥k⟮t⟯) F] (hs : P.ord s = 1)
  (z : F) : (P.residue hP hs) z = (P.residue hP ht) (z * (TauCeti.derivativeOfSeparating htr) s)
```

## Sources

- [Tau Ceti documentation: `TauCeti.Place.residue_eq_residue_mul`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Place/Expansion/Laurent/ChangeOfUniformizer.html#TauCeti.Place.residue_eq_residue_mul)
- [Source of `TauCeti.Place.residue_eq_residue_mul` in TauCeti/FieldTheory/FunctionField/Place/Expansion/Laurent/ChangeOfUniformizer.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/FunctionField/Place/Expansion/Laurent/ChangeOfUniformizer.lean#L101)
