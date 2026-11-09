---
declaration: theorem
origin: cited
lean: AlgebraicGeometry.Scheme.Modules.subsingleton_cohomologyOn_succ_of_isAffineOpen, AlgebraicGeometry.Scheme.Modules.subsingleton_cohomology_succ_of_isAffine
statement: formalized
proof: formalized
---

# Serre's vanishing theorem on affine opens

**Serre's vanishing theorem on affine opens** (Hartshorne, *Algebraic Geometry*, Theorem
III.3.5, without the Noetherian hypothesis): a sheaf of modules that is quasi-coherent over an
affine open subset `U` of a scheme (for example, a quasi-coherent sheaf on the scheme) has no
cohomology in positive degrees on `U`.

```lean
AlgebraicGeometry.Scheme.Modules.subsingleton_cohomologyOn_succ_of_isAffineOpen.{u}
  {X : AlgebraicGeometry.Scheme} (M : X.Modules) {U : X.Opens}
  (hU : AlgebraicGeometry.IsAffineOpen U) [SheafOfModules.IsQuasicoherent (M.restrict U.ι)]
  (n : ℕ) : Subsingleton ↑(TauCeti.AlgebraicGeometry.Scheme.Modules.cohomologyOn M (n + 1) U)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cartan's criterion](../../topology/other-results/cartans-criterion.md)

## Lean

Formalized in Tau Ceti as [`AlgebraicGeometry.Scheme.Modules.subsingleton_cohomologyOn_succ_of_isAffineOpen`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Cohomology/Affine.html#AlgebraicGeometry.Scheme.Modules.subsingleton_cohomologyOn_succ_of_isAffineOpen).

## Other forms

**Serre's vanishing theorem on affine schemes.** Formalized in Tau Ceti as [`AlgebraicGeometry.Scheme.Modules.subsingleton_cohomology_succ_of_isAffine`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Cohomology/Affine.html#AlgebraicGeometry.Scheme.Modules.subsingleton_cohomology_succ_of_isAffine).

```lean
AlgebraicGeometry.Scheme.Modules.subsingleton_cohomology_succ_of_isAffine.{u}
  {X : AlgebraicGeometry.Scheme} (M : X.Modules) [SheafOfModules.IsQuasicoherent M]
  [AlgebraicGeometry.IsAffine X] (n : ℕ) :
  Subsingleton (TauCeti.AlgebraicGeometry.Scheme.Modules.Cohomology M (n + 1))
```

## Sources

- [Tau Ceti documentation: `AlgebraicGeometry.Scheme.Modules.subsingleton_cohomologyOn_succ_of_isAffineOpen`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Cohomology/Affine.html#AlgebraicGeometry.Scheme.Modules.subsingleton_cohomologyOn_succ_of_isAffineOpen)
- [Source of `AlgebraicGeometry.Scheme.Modules.subsingleton_cohomologyOn_succ_of_isAffineOpen` in TauCeti/AlgebraicGeometry/Cohomology/Affine.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/Cohomology/Affine.lean#L266)
