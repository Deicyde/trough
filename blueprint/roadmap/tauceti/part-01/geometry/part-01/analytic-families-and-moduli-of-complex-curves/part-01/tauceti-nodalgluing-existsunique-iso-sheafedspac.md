---
declaration: theorem
origin: cited
lean: TauCeti.NodalGluing.existsUnique_iso_sheafedSpaceIso_eq_iff
statement: formalized
proof: formalized
---

# TauCeti.NodalGluing.existsUnique_iso_sheafedSpaceIso_eq_iff

An isomorphism of the holomorphic sheafed spaces of two nodal curves is induced by a unique
analytic nodal isomorphism exactly when its section maps fix the constants.

```lean
TauCeti.NodalGluing.existsUnique_iso_sheafedSpaceIso_eq_iff {ι Flag : Type} {X : ι → Type}
  [(i : ι) → TopologicalSpace (X i)] [(i : ι) → ChartedSpace ℂ (X i)]
  [∀ (i : ι), IsManifold (modelWithCornersSelf ℂ ℂ) 1 (X i)] [∀ (i : ι), T2Space (X i)]
  [Finite Flag] {d : TauCeti.NodalGluing.FlagPairData ι Flag X} {ι' Flag' : Type} {X' : ι' → Type}
  [(i : ι') → TopologicalSpace (X' i)] [(i : ι') → ChartedSpace ℂ (X' i)]
  [∀ (i : ι'), IsManifold (modelWithCornersSelf ℂ ℂ) 1 (X' i)] [∀ (i : ι'), T2Space (X' i)]
  [Finite Flag'] {d' : TauCeti.NodalGluing.FlagPairData ι' Flag' X'}
  (φ :
    TauCeti.NodalGluing.sheafedSpace (modelWithCornersSelf ℂ ℂ) d ≅
      TauCeti.NodalGluing.sheafedSpace (modelWithCornersSelf ℂ ℂ) d') :
  (∃! e, e.sheafedSpaceIso = φ) ↔
    ∀ (U : TopologicalSpace.Opens (TauCeti.NodalGluing.GluedCurve d')) (c : ℂ),
      (CommRingCat.Hom.hom (φ.hom.hom.c.app (Opposite.op U)))
          ((algebraMap ℂ
              ↑((TauCeti.NodalGluing.sheafedSpace (modelWithCornersSelf ℂ ℂ) d').presheaf.obj
                  (Opposite.op U)))
            c) =
        (algebraMap ℂ
            ↑((TauCeti.NodalGluing.sheafedSpace (modelWithCornersSelf ℂ ℂ) d).presheaf.obj
                (Opposite.op ((TopologicalSpace.Opens.map φ.hom.hom.base).obj U))))
          c
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Osgood's lemma](../../complex-manifolds-dolbeault-theory-and-kahler-ge/osgoods-lemma.md)
- [Riemann's removable singularity theorem on complex curves](../../../part-02/manifold/part-03/riemanns-removable-singularity-theorem-on-comple.md)
- [Rouché's theorem for a disc, classical form](../../../../analysis/part-02/complex/part-03/rouches-theorem-for-a-disc-classical-form.md)
- [TauCeti.NodalGluing.isDomain_quotientStalk_iff](tauceti-nodalgluing-isdomain-quotientstalk-iff.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NodalGluing.existsUnique_iso_sheafedSpaceIso_eq_iff`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/NodalGluing/RingedLift.html#TauCeti.NodalGluing.existsUnique_iso_sheafedSpaceIso_eq_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.NodalGluing.existsUnique_iso_sheafedSpaceIso_eq_iff`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/NodalGluing/RingedLift.html#TauCeti.NodalGluing.existsUnique_iso_sheafedSpaceIso_eq_iff)
- [Source of `TauCeti.NodalGluing.existsUnique_iso_sheafedSpaceIso_eq_iff` in TauCeti/AlgebraicGeometry/Curves/NodalGluing/RingedLift.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/Curves/NodalGluing/RingedLift.lean#L228)
- [Tau Ceti roadmap status: Analytic families and moduli of complex curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComplexCurveModuli/STATUS.md)
