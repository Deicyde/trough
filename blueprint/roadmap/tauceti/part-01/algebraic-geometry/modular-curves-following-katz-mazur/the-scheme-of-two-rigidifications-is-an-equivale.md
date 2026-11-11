---
declaration: def
origin: cited
lean: TauCeti.AlgebraicGeometry.ModuliProblem.RelRepData.doubleEquivalenceRelation
statement: formalized
---

# The scheme of two rigidifications is an equivalence relation

**The scheme of two rigidifications is an equivalence relation** on the scheme of one
rigidification (Katz and Mazur, proof of Theorem 4.7.0). If `𝒫` is rigid, the morphisms of bases
`𝕄(𝒫, δ, δ) ⇉ 𝕄(𝒫, δ)` of the two forgetful projections form an equivalence relation in the
category of schemes. Its reflexivity, symmetry and transitivity morphisms are the morphisms of
bases of `doubleDiag`, `doubleSwap` and `doubleComp`; the last is evaluated on the two projections
from the fibre product `𝕄(𝒫, δ, δ) ×_{𝕄(𝒫, δ)} 𝕄(𝒫, δ, δ)`, lifted to arrows of `Ell/B`.

```lean
TauCeti.AlgebraicGeometry.ModuliProblem.RelRepData.doubleEquivalenceRelation.{u}
  {B : AlgebraicGeometry.Scheme} {P Q : TauCeti.AlgebraicGeometry.ModuliProblem B}
  (D : Q.RelRepData) {V : TauCeti.AlgebraicGeometry.EllObj B}
  (R :
    CategoryTheory.Functor.RepresentableBy (CategoryTheory.MonoidalCategoryStruct.tensorObj P Q) V)
  (hP : P.IsRigid) :
  CategoryTheory.EquivalenceRelation (V.baseChangeFunctorHom (D.rep V)).base (D.doubleSnd R).base
```

## Depends on

- [TauCeti.AlgebraicGeometry.ModuliProblem.RelRepData.doubleRepresentableBy](tauceti-algebraicgeometry-moduliproblem-relrepda.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.ModuliProblem.RelRepData.doubleEquivalenceRelation`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/ModularCurve/Rigidifier/EquivalenceRelation.html#TauCeti.AlgebraicGeometry.ModuliProblem.RelRepData.doubleEquivalenceRelation).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.ModuliProblem.RelRepData.doubleEquivalenceRelation`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/ModularCurve/Rigidifier/EquivalenceRelation.html#TauCeti.AlgebraicGeometry.ModuliProblem.RelRepData.doubleEquivalenceRelation)
- [Source of `TauCeti.AlgebraicGeometry.ModuliProblem.RelRepData.doubleEquivalenceRelation` in TauCeti/AlgebraicGeometry/ModularCurve/Rigidifier/EquivalenceRelation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/ModularCurve/Rigidifier/EquivalenceRelation.lean#L187)
- [Tau Ceti roadmap status: Modular curves, following Katz–Mazur](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ModularCurves/STATUS.md)
