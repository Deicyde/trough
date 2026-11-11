---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isFlat_of_comp_of_locallySurjective, AlgebraicGeometry.Space.isLocallyOfFiniteType_of_comp_of_locallySurjective, AlgebraicGeometry.Space.isLocallyOfFinitePresentation_of_comp_of_locallySurjective, AlgebraicGeometry.Space.isLocallyOfFiniteType_of_commonFppfDescentSituation, AlgebraicGeometry.Space.isLocallyOfFinitePresentation_of_commonFppfDescentSituation, AlgebraicGeometry.Space.isSmooth_of_comp_surjective_isSmooth, AlgebraicGeometry.Space.isEtale_of_comp_surjective_isEtale, AlgebraicGeometry.Space.isSyntomic_of_comp_surjective_isSyntomic
statement: formalized
proof: formalized
---

# 74.8 Descent of finiteness and smoothness properties of morphisms

Section 74.8 of the Stacks Project, [Tag 06NQ](https://stacks.math.columbia.edu/tag/06NQ). 5 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06NR, a lemma

[Tag 06NR](https://stacks.math.columbia.edu/tag/06NR) in the Stacks Project.

**`AlgebraicGeometry.Space.isFlat_of_comp_of_locallySurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/Properties/MorphismFiniteness.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/Properties/MorphismFiniteness.lean#L184). The attribute's comment: “flatness”.

> **Stacks 06NR.** Flatness of a composite of morphisms of algebraic spaces descends to the
> second factor when the first factor is surjective as a morphism of fppf sheaves.

```lean
theorem isFlat_of_comp_of_locallySurjective
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y)
    (_hZ : IsAlgebraicSpace B S hS Z)
    (f : X ⟶ Y) (g : Y ⟶ Z)
    (hfg : IsFlat B S hS (f ≫ g))
    (hf : Presheaf.IsLocallySurjective (BigFppfOver.topology B S hS) f) :
    IsFlat B S hS g
```

**`AlgebraicGeometry.Space.isLocallyOfFiniteType_of_comp_of_locallySurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/Properties/MorphismFiniteness.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/Properties/MorphismFiniteness.lean#L204). The attribute's comment: “locally finite type”.

> **Stacks 06NR.** Local finite type of a composite of morphisms of algebraic spaces
> descends to the second factor when the first factor is surjective as a morphism of fppf
> sheaves.

```lean
theorem isLocallyOfFiniteType_of_comp_of_locallySurjective
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y)
    (_hZ : IsAlgebraicSpace B S hS Z)
    (f : X ⟶ Y) (g : Y ⟶ Z)
    (hfg : IsLocallyOfFiniteType B S hS (f ≫ g))
    (hf : Presheaf.IsLocallySurjective (BigFppfOver.topology B S hS) f) :
    IsLocallyOfFiniteType B S hS g
```

**`AlgebraicGeometry.Space.isLocallyOfFinitePresentation_of_comp_of_locallySurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/Properties/MorphismFiniteness.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/Properties/MorphismFiniteness.lean#L224). The attribute's comment: “locally finite presentation”.

> **Stacks 06NR.** Local finite presentation of a composite of morphisms of algebraic spaces
> descends to the second factor when the first factor is surjective as a morphism of fppf
> sheaves.

```lean
theorem isLocallyOfFinitePresentation_of_comp_of_locallySurjective
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y)
    (_hZ : IsAlgebraicSpace B S hS Z)
    (f : X ⟶ Y) (g : Y ⟶ Z)
    (hfg : IsLocallyOfFinitePresentation B S hS (f ≫ g))
    (hf : Presheaf.IsLocallySurjective (BigFppfOver.topology B S hS) f) :
    IsLocallyOfFinitePresentation B S hS g
```

## Tag 0AHC, a lemma

[Tag 0AHC](https://stacks.math.columbia.edu/tag/0AHC) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyOfFiniteType_of_commonFppfDescentSituation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/Properties/MorphismFiniteness.lean, line 244](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/Properties/MorphismFiniteness.lean#L244). The attribute's comment: “the case of local finite type”. References: EGA IV (11.3.16), “locally of finite type”.

> **Stacks 0AHC**, the case of local finite type. In a commutative triangle `X ⟶ Y ⟶ B` of
> algebraic spaces whose first morphism is surjective, flat and locally of finite presentation,
> if `X ⟶ B` is locally of finite type then so is `Y ⟶ B`.

```lean
theorem isLocallyOfFiniteType_of_commonFppfDescentSituation
    (T : CommonFppfDescentSituation.{u}) (hp : IsLocallyOfFiniteType T.site T.S T.hS T.p) :
    IsLocallyOfFiniteType T.site T.S T.hS T.q
```

**`AlgebraicGeometry.Space.isLocallyOfFinitePresentation_of_commonFppfDescentSituation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/Properties/MorphismFiniteness.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/Properties/MorphismFiniteness.lean#L260). The attribute's comment: “the case of local finite presentation”. References: EGA IV (11.3.16), “loc. fin. presentation”; SGA 4 IV (8.5.5), “partial”.

> **Stacks 0AHC**, the case of local finite presentation. In a commutative triangle
> `X ⟶ Y ⟶ B` of algebraic spaces whose first morphism is surjective, flat and locally of finite
> presentation, if `X ⟶ B` is locally of finite presentation then so is `Y ⟶ B`.

```lean
theorem isLocallyOfFinitePresentation_of_commonFppfDescentSituation
    (T : CommonFppfDescentSituation.{u})
    (hp : IsLocallyOfFinitePresentation T.site T.S T.hS T.p) :
    IsLocallyOfFinitePresentation T.site T.S T.hS T.q
```

## Tag 0AHD, a lemma

[Tag 0AHD](https://stacks.math.columbia.edu/tag/0AHD) in the Stacks Project.

**`AlgebraicGeometry.Space.isSmooth_of_comp_surjective_isSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/Properties/Permanence.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/Properties/Permanence.lean#L115). The attribute's comment: “smooth case”.

> **Stacks 0AHD**, smooth case. In a commuting triangle `p = f ≫ q` of morphisms of
> algebraic spaces over `S` with `f` surjective and smooth, smoothness of `p` implies smoothness
> of `q`.

```lean
theorem isSmooth_of_comp_surjective_isSmooth
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (_hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (p : X ⟶ Z) (q : Y ⟶ Z)
    (hcomm : p = f ≫ q) (hfs : IsSurjective B S hS f)
    (hf : IsSmooth B S hS f) (hp : IsSmooth B S hS p) :
    IsSmooth B S hS q
```

**`AlgebraicGeometry.Space.isEtale_of_comp_surjective_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/Properties/Permanence.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/Properties/Permanence.lean#L132). The attribute's comment: “étale case”.

> **Stacks 0AHD**, étale case. In a commuting triangle `p = f ≫ q` of morphisms of algebraic
> spaces over `S` with `f` surjective and étale, étaleness of `p` implies étaleness of `q`.

```lean
theorem isEtale_of_comp_surjective_isEtale
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (p : X ⟶ Z) (q : Y ⟶ Z)
    (hcomm : p = f ≫ q) (hfs : IsSurjective B S hS f)
    (hf : IsEtale B S hS f) (hp : IsEtale B S hS p) :
    IsEtale B S hS q
```

**`AlgebraicGeometry.Space.isSyntomic_of_comp_surjective_isSyntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/Properties/SyntomicPermanence.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/Properties/SyntomicPermanence.lean#L51). The attribute's comment: “syntomic case”.

> **Stacks 0AHD**, syntomic case. In a commuting triangle `p = f ≫ q` of morphisms of
> algebraic spaces over `S` with `f` surjective and syntomic, syntomicity of `p` implies
> syntomicity of `q`.

```lean
theorem isSyntomic_of_comp_surjective_isSyntomic
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (_hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (p : X ⟶ Z) (q : Y ⟶ Z)
    (hcomm : p = f ≫ q) (hfs : IsSurjective B S hS f)
    (hf : IsSyntomic B S hS f) (hp : IsSyntomic B S hS p) :
    IsSyntomic B S hS q
```

## Tag 0AHE, a lemma

[Tag 0AHE](https://stacks.math.columbia.edu/tag/0AHE) in the Stacks Project.

**`AlgebraicGeometry.Space.isSmooth_of_comp_of_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/Properties/FppfPermanence.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/Properties/FppfPermanence.lean#L151). The attribute's comment: “smooth case”.

> **Stacks 0AHE**, smooth case. In a commuting triangle `p = f ≫ q` of morphisms of
> algebraic spaces over `S` with `f` surjective, flat and locally of finite presentation,
> smoothness of `p` implies smoothness of `q`.

```lean
theorem isSmooth_of_comp_of_fppf
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (_hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (p : X ⟶ Z) (q : Y ⟶ Z)
    (hcomm : p = f ≫ q) (hfs : IsSurjective B S hS f) (hff : IsFlat B S hS f)
    (hfp : IsLocallyOfFinitePresentation B S hS f) (hp : IsSmooth B S hS p) :
    IsSmooth B S hS q
```

**`AlgebraicGeometry.Space.isEtale_of_comp_of_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/Properties/FppfPermanence.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/Properties/FppfPermanence.lean#L167). The attribute's comment: “étale case”.

> **Stacks 0AHE**, étale case. In a commuting triangle `p = f ≫ q` of morphisms of
> algebraic spaces over `S` with `f` surjective, flat and locally of finite presentation,
> étaleness of `p` implies étaleness of `q`.

```lean
theorem isEtale_of_comp_of_fppf
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (p : X ⟶ Z) (q : Y ⟶ Z)
    (hcomm : p = f ≫ q) (hfs : IsSurjective B S hS f) (hff : IsFlat B S hS f)
    (hfp : IsLocallyOfFinitePresentation B S hS f) (hp : IsEtale B S hS p) :
    IsEtale B S hS q
```

## Tag 0AHF, a lemma

[Tag 0AHF](https://stacks.math.columbia.edu/tag/0AHF) in the Stacks Project.

**`AlgebraicGeometry.Space.isSyntomic_of_comp_of_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SyntomicFactor.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SyntomicFactor.lean#L102). The attribute's comment: “syntomicity of q”.

> **Stacks 0AHF.** Syntomicity descends from a composite of morphisms of algebraic spaces over
> `S` along a surjective, flat morphism which is locally of finite presentation: if `f : X ⟶ Y` is
> surjective, flat and locally of finite presentation and `f ≫ q` is syntomic, then `q : Y ⟶ Z` is
> syntomic.

```lean
theorem isSyntomic_of_comp_of_fppf
    {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (q : Y ⟶ Z)
    (hfs : IsSurjective B S hS f) (hff : IsFlat B S hS f)
    (hflfp : IsLocallyOfFinitePresentation B S hS f)
    (hp : IsSyntomic B S hS (f ≫ q)) :
    IsSyntomic B S hS q
```

**`AlgebraicGeometry.Space.isSyntomic_of_isSyntomic_comp_of_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SyntomicFactor.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SyntomicFactor.lean#L117). The attribute's comment: “syntomicity of f”.

> **Stacks 0AHF.** A flat morphism of algebraic spaces over `S` which is locally of finite
> presentation is syntomic as soon as its composite with another morphism is syntomic. The source
> states this alongside the conclusion about the other factor, under the extra hypothesis that `f`
> be surjective; surjectivity is not needed here.

```lean
theorem isSyntomic_of_isSyntomic_comp_of_fppf
    {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (q : Y ⟶ Z)
    (hff : IsFlat B S hS f) (hflfp : IsLocallyOfFinitePresentation B S hS f)
    (hp : IsSyntomic B S hS (f ≫ q)) :
    IsSyntomic B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 74.8, Tag 06NQ](https://stacks.math.columbia.edu/tag/06NQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
