---
declaration: theorem
origin: cited
lean: TauCeti.vietaHom_eq_comp_esymmSubst
statement: formalized
proof: formalized
---

# Vieta's formulas, in the form the symmetric descent uses

if `f` is the product of the
linear factors attached to `x`, then substituting the signed coefficients of `f` is the same as
substituting the elementary symmetric polynomials and evaluating at `x`.

```lean
TauCeti.vietaHom_eq_comp_esymmSubst.{u_1} {R : Type u_1} [CommRing R] {n : ℕ} {f : Polynomial R}
  {x : Fin n → R} (hf : f = ∏ i, (Polynomial.X - Polynomial.C (x i))) :
  TauCeti.vietaHom n f = (MvPolynomial.eval₂Hom (Int.castRingHom R) x).comp (TauCeti.esymmSubst n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Vieta's formulas on the symmetric power](../../geometry/part-01/real-algebraic-geometry-sign-determination-and-c/vietas-formulas-on-the-symmetric-power.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.vietaHom_eq_comp_esymmSubst`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisGroups/Resolvent/Specialization.html#TauCeti.vietaHom_eq_comp_esymmSubst).

## Sources

- [Tau Ceti documentation: `TauCeti.vietaHom_eq_comp_esymmSubst`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisGroups/Resolvent/Specialization.html#TauCeti.vietaHom_eq_comp_esymmSubst)
- [Source of `TauCeti.vietaHom_eq_comp_esymmSubst` in TauCeti/FieldTheory/GaloisGroups/Resolvent/Specialization.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/GaloisGroups/Resolvent/Specialization.lean#L175)
