---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.isCommMonObj_of_isProper_of_flat
statement: formalized
proof: formalized
---

# Abelian schemes are commutative

Every proper, flat, geometrically integral group scheme `G`
over an arbitrary base scheme `S` satisfying `G.hom_* 𝒪_G = 𝒪_S` is commutative.

```lean
TauCeti.AlgebraicGeometry.isCommMonObj_of_isProper_of_flat.{u} {S : AlgebraicGeometry.Scheme}
  (G : CategoryTheory.Over S) [CategoryTheory.GrpObj G] [AlgebraicGeometry.IsProper G.hom]
  [AlgebraicGeometry.Flat G.hom] [AlgebraicGeometry.GeometricallyIntegral G.hom]
  (hG : ∀ (V : ↑S.affineOpens), CategoryTheory.IsIso (AlgebraicGeometry.Scheme.Hom.app G.hom ↑V)) :
  CategoryTheory.IsCommMonObj G
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.isCommMonObj_of_isProper_of_flat`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Rigidity/GroupScheme.html#TauCeti.AlgebraicGeometry.isCommMonObj_of_isProper_of_flat).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.isCommMonObj_of_isProper_of_flat`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Rigidity/GroupScheme.html#TauCeti.AlgebraicGeometry.isCommMonObj_of_isProper_of_flat)
- [Source of `TauCeti.AlgebraicGeometry.isCommMonObj_of_isProper_of_flat` in TauCeti/AlgebraicGeometry/Rigidity/GroupScheme.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/Rigidity/GroupScheme.lean#L145)
- [Tau Ceti roadmap status: Modular curves and the moduli of elliptic curves with level structure](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ModularCurves/STATUS.md)
