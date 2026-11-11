---
declaration: theorem
origin: cited
lean: TauCeti.holomorphicStructureSheaf.nodeLocalRing.isIntegralClosure_branchFractionMap
statement: formalized
proof: formalized
---

# TauCeti.holomorphicStructureSheaf.nodeLocalRing.isIntegralClosure_branchFractionMap

The product of the holomorphic branch stalks is the integral closure of the node ring in
its total ring of meromorphic fractions.

```lean
TauCeti.holomorphicStructureSheaf.nodeLocalRing.isIntegralClosure_branchFractionMap.{u_1, u_2}
  {X Y : Type} [TopologicalSpace X] [ChartedSpace ℂ X] [TopologicalSpace Y] [ChartedSpace ℂ Y]
  (p : X) (q : Y) [IsManifold (modelWithCornersSelf ℂ ℂ) 1 X]
  [IsManifold (modelWithCornersSelf ℂ ℂ) 1 Y] (K : Type u_1) (L : Type u_2) [CommRing K]
  [Algebra (↑((TauCeti.holomorphicStructureSheaf (modelWithCornersSelf ℂ ℂ) X).presheaf.stalk p)) K]
  [CommRing L]
  [Algebra (↑((TauCeti.holomorphicStructureSheaf (modelWithCornersSelf ℂ ℂ) Y).presheaf.stalk q)) L]
  [IsFractionRing
      (↑((TauCeti.holomorphicStructureSheaf (modelWithCornersSelf ℂ ℂ) X).presheaf.stalk p)) K]
  [IsFractionRing
      (↑((TauCeti.holomorphicStructureSheaf (modelWithCornersSelf ℂ ℂ) Y).presheaf.stalk q)) L] :
  have this :=
    (TauCeti.holomorphicStructureSheaf.nodeLocalRing.branchFractionMap p q K L).toAlgebra;
  have this_1 :=
    ((algebraMap
            (↑((TauCeti.holomorphicStructureSheaf (modelWithCornersSelf ℂ ℂ) X).presheaf.stalk p))
            K).prodMap
        (algebraMap
          (↑((TauCeti.holomorphicStructureSheaf (modelWithCornersSelf ℂ ℂ) Y).presheaf.stalk q))
          L)).toAlgebra;
  IsIntegralClosure
    (↑((TauCeti.holomorphicStructureSheaf (modelWithCornersSelf ℂ ℂ) X).presheaf.stalk p) ×
      ↑((TauCeti.holomorphicStructureSheaf (modelWithCornersSelf ℂ ℂ) Y).presheaf.stalk q))
    (↥(TauCeti.holomorphicStructureSheaf.nodeLocalRing (modelWithCornersSelf ℂ ℂ)
        (modelWithCornersSelf ℂ ℂ) p q))
    (K × L)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The identity theorem on analytic manifolds](../../../part-02/manifold/part-02/the-identity-theorem-on-analytic-manifolds.md)
- [Osgood's lemma](../../complex-manifolds-dolbeault-theory-and-kahler-ge/osgoods-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.holomorphicStructureSheaf.nodeLocalRing.isIntegralClosure_branchFractionMap`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/StructureSheaf/Normalization.html#TauCeti.holomorphicStructureSheaf.nodeLocalRing.isIntegralClosure_branchFractionMap).

## Sources

- [Tau Ceti documentation: `TauCeti.holomorphicStructureSheaf.nodeLocalRing.isIntegralClosure_branchFractionMap`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/StructureSheaf/Normalization.html#TauCeti.holomorphicStructureSheaf.nodeLocalRing.isIntegralClosure_branchFractionMap)
- [Source of `TauCeti.holomorphicStructureSheaf.nodeLocalRing.isIntegralClosure_branchFractionMap` in TauCeti/Geometry/Manifold/Complex/StructureSheaf/Normalization.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Complex/StructureSheaf/Normalization.lean#L149)
- [Tau Ceti roadmap status: Analytic families and moduli of complex curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComplexCurveModuli/STATUS.md)
