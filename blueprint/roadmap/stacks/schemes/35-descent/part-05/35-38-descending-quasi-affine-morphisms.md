---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isEffectiveDescentAlongSurjectiveEtale_isQuasiAffineHom, AlgebraicGeometry.DescentData.isFamilyEffective_of_isQuasiAffineHom
statement: formalized
proof: formalized
---

# 35.38 Descending quasi-affine morphisms

Section 35.38 of the Stacks Project, [Tag 0246](https://stacks.math.columbia.edu/tag/0246). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0247, a lemma

[Tag 0247](https://stacks.math.columbia.edu/tag/0247) in the Stacks Project.

**`AlgebraicGeometry.Space.isEffectiveDescentAlongSurjectiveEtale_isQuasiAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiAffineEtaleDescent.lean, line 350](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiAffineEtaleDescent.lean#L350). The attribute's comment: “effective descent along a surjective étale chart of the site”. References: SGA 1 VIII (7.9), “surjective étale cover”.

> **Quasi-affine morphisms descend effectively along the surjective étale morphisms of the big
> fppf site of `S`.** If the base change of a morphism of sheaves `f : X ⟶ Y` along a surjective
> étale chart `q : c ⟶ a` of a representable `yoneda.obj a ⟶ Y` is representable by quasi-affine
> morphisms, then so is `X ×[Y] yoneda.obj a ⟶ yoneda.obj a`.

```lean
theorem isEffectiveDescentAlongSurjectiveEtale_isQuasiAffineHom
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) :
    IsEffectiveDescentAlongSurjectiveEtale B S hS
      (@_root_.AlgebraicGeometry.IsQuasiAffineHom.{u} : MorphismProperty Scheme.{u})
```

**`AlgebraicGeometry.DescentData.isFamilyEffective_of_isQuasiAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiAffineFpqcDescent.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiAffineFpqcDescent.lean#L106). References: SGA 1 VIII (7.9), “partial”; SGA 3 IV (4.7), “partial”; SGA 3 IX (2.3), “Effectivity clause”; SGA 3 VIII (1.7.2), “more general”; SGA 3 X (5.4), “special case”; SGA 3 XXIV (3.11.2), “partial”.

> **[Stacks, Tag 0247](https://stacks.math.columbia.edu/tag/0247).** Let `S` be a scheme, let
> `{X i ⟶ S}` be an fpqc covering family, indexed by a type in an arbitrary universe, and let `D`
> be a descent datum relative to it each of whose component morphisms `V i ⟶ X i` is quasi-affine.
> Then `D` is effective: it is isomorphic to the canonical descent datum of a scheme over `S`.
>
> Quasi-affineness is stable under arbitrary base change (Stacks 01SO) and, being Zariski local on
> the target, closed under finite disjoint unions, so the general-base fpqc reduction of Stacks
> 02W3, `AlgebraicGeometry.DescentData.isFamilyEffective_fpqc_of_affineSingleton_of_anyIndex`,
> reduces the statement to a covering given by a single surjective flat morphism of affine schemes.
> That case is the affine-hull argument of
> `AlgebraicGeometry.DescentDatum.isEffective_of_isIndQuasiAffineHom`, applied to a quasi-affine,
> hence ind-quasi-affine (Stacks 0F1W), morphism.

```lean
theorem isFamilyEffective_of_isQuasiAffineHom {I : Type v} {S : Scheme.{u}}
    {X : I → Scheme.{u}} (f : ∀ i, X i ⟶ S)
    (hf : Presieve.ofArrows X f ∈ Scheme.fpqcPrecoverage S)
    (D : DescentData f) (hD : ∀ i, IsQuasiAffineHom (D.obj i).hom) :
    D.IsFamilyEffective
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 35.38, Tag 0246](https://stacks.math.columbia.edu/tag/0246)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
