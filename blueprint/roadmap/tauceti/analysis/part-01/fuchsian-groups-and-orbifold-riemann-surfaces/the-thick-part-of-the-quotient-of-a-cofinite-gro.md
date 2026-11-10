---
declaration: theorem
origin: cited
lean: Subgroup.IsCofinite.isCompact_image_thickPart
statement: formalized
proof: formalized
---

# The thick part of the quotient of a cofinite group is compact

For a cofinite
`Γ ≤ PSL(2, ℝ)` and `ε > 0`, the image in `Γ \ ℍ` of the points moved a hyperbolic distance at
least `ε` by every nonidentity element of `Γ` is compact.

```lean
Subgroup.IsCofinite.isCompact_image_thickPart
  {Γ : Subgroup (Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℝ)} (hΓ : Γ.IsCofinite) {ε : ℝ}
  (hε : 0 < ε) :
  IsCompact (Quotient.mk (MulAction.orbitRel (↥Γ) UpperHalfPlane) '' TauCeti.thickPart (↥Γ) ε)
```

## Depends on

- [TauCeti.thickPart](tauceti-thickpart.md)

## Lean

Formalized in Tau Ceti as [`Subgroup.IsCofinite.isCompact_image_thickPart`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/DirichletDomain/Thick.html#Subgroup.IsCofinite.isCompact_image_thickPart).

## Sources

- [Tau Ceti documentation: `Subgroup.IsCofinite.isCompact_image_thickPart`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/DirichletDomain/Thick.html#Subgroup.IsCofinite.isCompact_image_thickPart)
- [Source of `Subgroup.IsCofinite.isCompact_image_thickPart` in TauCeti/Analysis/Complex/Fuchsian/DirichletDomain/Thick.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Fuchsian/DirichletDomain/Thick.lean#L61)
- [Tau Ceti roadmap status: Fuchsian groups and orbifold Riemann surfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FuchsianOrbifolds/STATUS.md)
