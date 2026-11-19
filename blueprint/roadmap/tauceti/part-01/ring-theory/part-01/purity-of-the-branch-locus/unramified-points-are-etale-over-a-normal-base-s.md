---
declaration: theorem
origin: cited
lean: AlgebraicGeometry.Scheme.Hom.ramificationLocus_eq_nonEtaleLocus
statement: formalized
proof: formalized
---

# Unramified points are étale over a normal base (SGA 1, Exposé I, 9.5 (ii))

For a
dominant morphism `f : X ⟶ Y` of integral schemes, locally of finite type, with `Y` locally
Noetherian and normal (for instance, regular), the ramification locus of `f` is its non-étale
locus. Normality of `X` is not needed.

```lean
AlgebraicGeometry.Scheme.Hom.ramificationLocus_eq_nonEtaleLocus.{u} {X Y : AlgebraicGeometry.Scheme}
  (f : X ⟶ Y) [AlgebraicGeometry.IsLocallyNoetherian Y] [AlgebraicGeometry.IsIntegral X]
  [AlgebraicGeometry.IsIntegral Y] [AlgebraicGeometry.IsDominant f]
  [AlgebraicGeometry.LocallyOfFiniteType f] [TauCeti.AlgebraicGeometry.IsNormalScheme Y] :
  AlgebraicGeometry.Scheme.Hom.ramificationLocus f = AlgebraicGeometry.Scheme.Hom.nonEtaleLocus f
```

## Depends on

- [AlgebraicGeometry.Scheme.Hom.ramificationLocus](algebraicgeometry-scheme-hom-ramificationlocus.md)

## Lean

Formalized in Tau Ceti as [`AlgebraicGeometry.Scheme.Hom.ramificationLocus_eq_nonEtaleLocus`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Morphisms/RamificationLocus.html#AlgebraicGeometry.Scheme.Hom.ramificationLocus_eq_nonEtaleLocus).

## Sources

- [Tau Ceti documentation: `AlgebraicGeometry.Scheme.Hom.ramificationLocus_eq_nonEtaleLocus`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Morphisms/RamificationLocus.html#AlgebraicGeometry.Scheme.Hom.ramificationLocus_eq_nonEtaleLocus)
- [Source of `AlgebraicGeometry.Scheme.Hom.ramificationLocus_eq_nonEtaleLocus` in TauCeti/AlgebraicGeometry/Morphisms/RamificationLocus.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/Morphisms/RamificationLocus.lean#L221)
- [Tau Ceti roadmap status: Purity of the branch locus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PurityOfBranchLocus/STATUS.md)
