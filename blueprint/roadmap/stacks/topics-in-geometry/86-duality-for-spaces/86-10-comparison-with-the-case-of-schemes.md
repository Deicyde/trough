---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.representedRightAdjointIso
statement: formalized
proof: formalized
---

# 86.10 Comparison with the case of schemes

Section 86.10 of the Stacks Project, [Tag 0E6D](https://stacks.math.columbia.edu/tag/0E6D). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0E6E, a lemma

[Tag 0E6E](https://stacks.math.columbia.edu/tag/0E6E) in the Stacks Project.

**`AlgebraicGeometry.Space.representedRightAdjointIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RepresentedRightAdjointDuality.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RepresentedRightAdjointDuality.lean#L87).

> **Stacks 0E6E.** Let `f : X ⟶ Y` be the morphism of quasi-compact and quasi-separated
> representable algebraic spaces over `S` represented by a morphism `g : T' ⟶ T` of the big fppf
> site, with underlying morphism of schemes `f_0 = g_0 : X_0 ⟶ Y_0`.  Let `a` be the right adjoint
> of `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)` of Stacks 0E55 and `a_0` the right adjoint of
> `Rf_{0,*} : D_QCoh(𝒪_{X_0}) ⥤ D_QCoh(𝒪_{Y_0})` of Stacks 0A9E.  Then `a_0` and `a` correspond
> under the equivalences `D_QCoh(𝒪_{X_0}) ≌ D_QCoh(𝒪_X)`, `D_QCoh(𝒪_{Y_0}) ≌ D_QCoh(𝒪_Y)` of
> Stacks 071Q.

```lean
def representedRightAdjointIso :
    haveI : CompactSpace (B.inclusion.obj T'.left) :=
      compactSpace_of_isQuasiCompactSpace_yoneda_obj B S hS hXqc
    haveI : QuasiSeparatedSpace (B.inclusion.obj T'.left) :=
      (isAbsolutelyQuasiSeparated_yoneda_iff_quasiSeparatedSpace B S hS hZ T').1 hXqs
    haveI : CompactSpace (B.inclusion.obj T.left) :=
      compactSpace_of_isQuasiCompactSpace_yoneda_obj B S hS hYqc
    haveI : QuasiSeparatedSpace (B.inclusion.obj T.left) :=
      (isAbsolutelyQuasiSeparated_yoneda_iff_quasiSeparatedSpace B S hS hZ T).1 hYqs
    haveI :=
      Stacks.Duality.DerivedPushforward.isLeftAdjoint_qcqsRestrictedDerivedPushforward_of_qcqs
        (B.inclusion.map g.left)
    haveI := isLeftAdjoint_quasicoherentDerivedPushforward hZ (representedSpaceMap B S hS g)
      hXqc hXqs hYqs
    (Stacks.Duality.DerivedPushforward.qcqsRestrictedDerivedPushforward
        (B.inclusion.map g.left)).rightAdjoint ⋙
        (representedDualityQuasicoherentDerivedEquivalence B S hS T').functor ≅
      (representedDualityQuasicoherentDerivedEquivalence B S hS T).functor ⋙
        (quasicoherentDerivedPushforward B S hS (representedSpaceMap B S hS g)
          (representedSpaceMap_isQuasiCompact hZ g hXqc hYqs)
          (representedSpaceMap_isQuasiSeparated hZ g hXqs)).rightAdjoint
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 86.10, Tag 0E6D](https://stacks.math.columbia.edu/tag/0E6D)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
