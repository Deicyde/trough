---
declaration: theorem
origin: cited
lean: AlgebraicGeometry.Scheme.Modules.subsingleton_cohomology_succ_of_isAffine, AlgebraicGeometry.Scheme.Modules.subsingleton_cohomologyOn_succ_of_isAffineOpen
statement: formalized
proof: formalized
---

# Serre's vanishing theorem on affine schemes

a quasi-coherent sheaf of modules on an
affine scheme, for example on the spectrum `Spec R` of any commutative ring, has no cohomology in
positive degrees.

```lean
AlgebraicGeometry.Scheme.Modules.subsingleton_cohomology_succ_of_isAffine.{u}
  {X : AlgebraicGeometry.Scheme} (M : X.Modules) [SheafOfModules.IsQuasicoherent M]
  [AlgebraicGeometry.IsAffine X] (n : ℕ) :
  Subsingleton (TauCeti.AlgebraicGeometry.Scheme.Modules.Cohomology M (n + 1))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cartan's criterion](../../topology/sato-hyperfunctions-and-analytic-generalized-fun/cartans-criterion.md)

## Lean

Formalized in Tau Ceti as [`AlgebraicGeometry.Scheme.Modules.subsingleton_cohomology_succ_of_isAffine`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Cohomology/Affine.html#AlgebraicGeometry.Scheme.Modules.subsingleton_cohomology_succ_of_isAffine).

## Other forms

**Serre's vanishing theorem on affine opens (Hartshorne, *Algebraic Geometry*, Theorem III.3.5, without the Noetherian hypothesis).** Formalized in Tau Ceti as [`AlgebraicGeometry.Scheme.Modules.subsingleton_cohomologyOn_succ_of_isAffineOpen`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Cohomology/Affine.html#AlgebraicGeometry.Scheme.Modules.subsingleton_cohomologyOn_succ_of_isAffineOpen).

```lean
AlgebraicGeometry.Scheme.Modules.subsingleton_cohomologyOn_succ_of_isAffineOpen.{u}
  {X : AlgebraicGeometry.Scheme} (M : X.Modules) {U : X.Opens}
  (hU : AlgebraicGeometry.IsAffineOpen U) [SheafOfModules.IsQuasicoherent (M.restrict U.ι)]
  (n : ℕ) : Subsingleton ↑(TauCeti.AlgebraicGeometry.Scheme.Modules.cohomologyOn M (n + 1) U)
```

## Sources

- [Tau Ceti documentation: `AlgebraicGeometry.Scheme.Modules.subsingleton_cohomology_succ_of_isAffine`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Cohomology/Affine.html#AlgebraicGeometry.Scheme.Modules.subsingleton_cohomology_succ_of_isAffine)
- [Source of `AlgebraicGeometry.Scheme.Modules.subsingleton_cohomology_succ_of_isAffine` in TauCeti/AlgebraicGeometry/Cohomology/Affine.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/Cohomology/Affine.lean#L255)
