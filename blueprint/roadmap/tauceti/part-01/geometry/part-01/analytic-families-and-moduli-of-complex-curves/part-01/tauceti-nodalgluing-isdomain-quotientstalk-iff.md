---
declaration: theorem
origin: cited
lean: TauCeti.NodalGluing.isDomain_quotientStalk_iff
statement: formalized
proof: formalized
---

# TauCeti.NodalGluing.isDomain_quotientStalk_iff

A point of the normalization quotient is not a node exactly when its holomorphic stalk
is an integral domain. No compactness or connectedness assumption is needed.

```lean
TauCeti.NodalGluing.isDomain_quotientStalk_iff {ι Flag : Type} {X : ι → Type}
  [(i : ι) → TopologicalSpace (X i)] [(i : ι) → ChartedSpace ℂ (X i)]
  [∀ (i : ι), IsManifold (modelWithCornersSelf ℂ ℂ) 1 (X i)] [∀ (i : ι), T2Space (X i)]
  [Finite Flag] (d : TauCeti.NodalGluing.FlagPairData ι Flag X)
  (z : TauCeti.NodalGluing.GluedCurve d) :
  IsDomain
      ↑((TauCeti.holomorphicStructureSheaf.quotientSheaf (modelWithCornersSelf ℂ ℂ)
                (TauCeti.NodalGluing.gluedRelSetoid d)).presheaf.stalk
          z) ↔
    z ∉ TauCeti.NodalGluing.nodeSet d
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The identity theorem on analytic manifolds](../../../part-02/manifold/part-02/the-identity-theorem-on-analytic-manifolds.md)
- [Osgood's lemma](../../complex-manifolds-dolbeault-theory-and-kahler-ge/osgoods-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NodalGluing.isDomain_quotientStalk_iff`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/NodalGluing/IntrinsicNodes.html#TauCeti.NodalGluing.isDomain_quotientStalk_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.NodalGluing.isDomain_quotientStalk_iff`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/NodalGluing/IntrinsicNodes.html#TauCeti.NodalGluing.isDomain_quotientStalk_iff)
- [Source of `TauCeti.NodalGluing.isDomain_quotientStalk_iff` in TauCeti/AlgebraicGeometry/Curves/NodalGluing/IntrinsicNodes.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/Curves/NodalGluing/IntrinsicNodes.lean#L48)
- [Tau Ceti roadmap status: Analytic families and moduli of complex curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComplexCurveModuli/STATUS.md)
