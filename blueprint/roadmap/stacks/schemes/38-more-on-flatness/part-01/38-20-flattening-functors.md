---
declaration: section
origin: cited
lean: Stacks.Flatness.ModuleMapBaseChangeSituation.IsInjectiveAfterBaseChange, Stacks.Flatness.ModuleMapBaseChangeSituation.FlatOver, Stacks.Flatness.ModuleMapBaseChangeSituation.isInjectiveAfterBaseChange_of_flat_hom, Stacks.Flatness.ModuleMapBaseChangeSituation.injectivityFunctor, Stacks.Flatness.ModuleMapBaseChangeSituation.isInjectiveAfterBaseChange_of_hom_of_epi, Stacks.Flatness.ModuleMapBaseChangeSituation.injectivityFunctorOfEpi, Stacks.Flatness.ModuleMapBaseChangeSituation.injectivityFunctorOfEpiRestrictionIso, Stacks.Flatness.ModuleMapBaseChangeSituation.injectivityFunctorOfEpiIsoIsomorphismFunctor
statement: formalized
proof: formalized
---

# 38.20 Flattening functors

Section 38.20 of the Stacks Project, [Tag 05MG](https://stacks.math.columbia.edu/tag/05MG). 15 tags here are carried by 68 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05MH, a situation

[Tag 05MH](https://stacks.math.columbia.edu/tag/05MH) in the Stacks Project.

**`Stacks.Flatness.ModuleMapBaseChangeSituation.IsInjectiveAfterBaseChange`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctors/Injectivity.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctors/Injectivity.lean#L69). The attribute's comment: “the injectivity condition”.

> The condition that the base-changed homomorphism is injective.

```lean
abbrev IsInjectiveAfterBaseChange (D : ModuleMapBaseChangeSituation.{u}) (T : Over D.S) : Prop
```

**`Stacks.Flatness.ModuleMapBaseChangeSituation.FlatOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctors/Injectivity.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctors/Injectivity.lean#L87). The attribute's comment: “the category with flat morphisms”.

> The category of schemes over `S` whose morphisms are only the flat ones.

```lean
abbrev FlatOver (S : Scheme.{u})
```

**`Stacks.Flatness.ModuleMapBaseChangeSituation.isInjectiveAfterBaseChange_of_flat_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctors/Injectivity.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctors/Injectivity.lean#L94). The attribute's comment: “functoriality of the injectivity condition”.

> Being injective after base change is preserved by every *flat* further base change: the
> transition morphism of base changes is then flat, so pulling back along it preserves
> monomorphisms, and the comparison isomorphism carries the base-changed homomorphism over `T`
> to the one over `T'`.

```lean
theorem isInjectiveAfterBaseChange_of_flat_hom (D : ModuleMapBaseChangeSituation.{u})
    {T T' : Over D.S} (g : T' ⟶ T) (hg : Flat g.left)
    (h : D.IsInjectiveAfterBaseChange T) : D.IsInjectiveAfterBaseChange T'
```

**`Stacks.Flatness.ModuleMapBaseChangeSituation.injectivityFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctors/Injectivity.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctors/Injectivity.lean#L111). The attribute's comment: “the injectivity functor”.

> The subterminal functor on schemes over the base with flat transition morphisms recording
> where the base-changed homomorphism is injective.

```lean
noncomputable def injectivityFunctor (D : ModuleMapBaseChangeSituation.{u}) :
    (FlatOver D.S)ᵒᵖ ⥤ Type
```

**`Stacks.Flatness.ModuleMapBaseChangeSituation.isInjectiveAfterBaseChange_of_hom_of_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctors/Injectivity.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctors/Injectivity.lean#L123). The attribute's comment: “unrestricted functoriality of injectivity for a surjection”.

> If the homomorphism is surjective then its base change is both injective and surjective
> whenever it is injective, hence an isomorphism, and being an isomorphism after base change is
> stable under an arbitrary further base change.

```lean
theorem isInjectiveAfterBaseChange_of_hom_of_epi (D : ModuleMapBaseChangeSituation.{u})
    [Epi D.hom] {T T' : Over D.S} (g : T' ⟶ T) (h : D.IsInjectiveAfterBaseChange T) :
    D.IsInjectiveAfterBaseChange T'
```

**`Stacks.Flatness.ModuleMapBaseChangeSituation.injectivityFunctorOfEpi`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctors/Injectivity.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctors/Injectivity.lean#L140). The attribute's comment: “the unrestricted injectivity functor for a surjection”.

> For a surjective homomorphism, injectivity after base change defines a subterminal functor
> on all schemes over the base.

```lean
noncomputable def injectivityFunctorOfEpi (D : ModuleMapBaseChangeSituation.{u}) [Epi D.hom] :
    (Over D.S)ᵒᵖ ⥤ Type
```

**`Stacks.Flatness.ModuleMapBaseChangeSituation.injectivityFunctorOfEpiRestrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctors/Injectivity.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctors/Injectivity.lean#L150). The attribute's comment: “restriction of the unrestricted injectivity functor”.

> The unrestricted injectivity functor of a surjection restricts along the inclusion of the
> category with flat morphisms to the injectivity functor.

```lean
noncomputable def injectivityFunctorOfEpiRestrictionIso (D : ModuleMapBaseChangeSituation.{u})
    [Epi D.hom] :
    (wideSubcategoryInclusion (FlatMorphismOver D.S)).op ⋙ D.injectivityFunctorOfEpi ≅
      D.injectivityFunctor
```

**`Stacks.Flatness.ModuleMapBaseChangeSituation.injectivityFunctorOfEpiIsoIsomorphismFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctors/Injectivity.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctors/Injectivity.lean#L160). The attribute's comment: “injectivity equals isomorphism for a surjection”.

> For a surjective homomorphism the unrestricted injectivity functor is the isomorphism
> functor: a surjection that is injective after base change is an isomorphism after base change,
> and conversely.

```lean
noncomputable def injectivityFunctorOfEpiIsoIsomorphismFunctor
    (D : ModuleMapBaseChangeSituation.{u}) [Epi D.hom] :
    D.injectivityFunctorOfEpi ≅ D.isomorphismFunctor
```

**`Stacks.Flatness.ModuleMapBaseChangeSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/ModuleMapBaseChange.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/ModuleMapBaseChange.lean#L90). The attribute's comment: “the situation”.

> The standing data for testing a homomorphism of quasi-coherent modules after an arbitrary
> base change: a morphism of schemes `f : X ⟶ S`, two quasi-coherent modules on `X`, and a
> homomorphism between them.

```lean
structure ModuleMapBaseChangeSituation
```

**`Stacks.Flatness.ModuleMapBaseChangeSituation.baseChange`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/ModuleMapBaseChange.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/ModuleMapBaseChange.lean#L112). The attribute's comment: “the base-changed scheme”.

> The base change `X ×_S T` of the source along a scheme `T` over the base.

```lean
noncomputable abbrev baseChange (D : ModuleMapBaseChangeSituation.{u}) (T : Over D.S) :
    Scheme.{u}
```

**`Stacks.Flatness.ModuleMapBaseChangeSituation.baseChangeMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/ModuleMapBaseChange.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/ModuleMapBaseChange.lean#L118). The attribute's comment: “the base-changed homomorphism”.

> The pullback of the module homomorphism to `X ×_S T`.

```lean
noncomputable def baseChangeMap (D : ModuleMapBaseChangeSituation.{u}) (T : Over D.S) :
    (Scheme.Modules.pullback (pullback.fst D.f T.hom)).obj D.F ⟶
      (Scheme.Modules.pullback (pullback.fst D.f T.hom)).obj D.G
```

**`Stacks.Flatness.ModuleMapBaseChangeSituation.IsIsomorphismAfterBaseChange`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/ModuleMapBaseChange.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/ModuleMapBaseChange.lean#L125). The attribute's comment: “the isomorphism condition”.

> The condition that the base-changed homomorphism is an isomorphism.

```lean
abbrev IsIsomorphismAfterBaseChange (D : ModuleMapBaseChangeSituation.{u}) (T : Over D.S) :
    Prop
```

**`Stacks.Flatness.ModuleMapBaseChangeSituation.IsSurjectiveAfterBaseChange`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/ModuleMapBaseChange.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/ModuleMapBaseChange.lean#L131). The attribute's comment: “the surjectivity condition”.

> The condition that the base-changed homomorphism is surjective.

```lean
abbrev IsSurjectiveAfterBaseChange (D : ModuleMapBaseChangeSituation.{u}) (T : Over D.S) :
    Prop
```

**`Stacks.Flatness.ModuleMapBaseChangeSituation.IsZeroAfterBaseChange`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/ModuleMapBaseChange.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/ModuleMapBaseChange.lean#L137). The attribute's comment: “the zero condition”.

> The condition that the base-changed homomorphism is zero.

```lean
abbrev IsZeroAfterBaseChange (D : ModuleMapBaseChangeSituation.{u}) (T : Over D.S) : Prop
```

**`Stacks.Flatness.ModuleMapBaseChangeSituation.isIsomorphismAfterBaseChange_of_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/ModuleMapBaseChange.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/ModuleMapBaseChange.lean#L189). The attribute's comment: “functoriality of the isomorphism condition”.

> Being an isomorphism after base change is preserved by every further base change.

```lean
theorem isIsomorphismAfterBaseChange_of_hom (D : ModuleMapBaseChangeSituation.{u})
    {T T' : Over D.S} (g : T' ⟶ T) (h : D.IsIsomorphismAfterBaseChange T) :
    D.IsIsomorphismAfterBaseChange T'
```

**`Stacks.Flatness.ModuleMapBaseChangeSituation.isSurjectiveAfterBaseChange_of_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/ModuleMapBaseChange.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/ModuleMapBaseChange.lean#L199). The attribute's comment: “functoriality of the surjectivity condition”.

> Being surjective after base change is preserved by every further base change.

```lean
theorem isSurjectiveAfterBaseChange_of_hom (D : ModuleMapBaseChangeSituation.{u})
    {T T' : Over D.S} (g : T' ⟶ T) (h : D.IsSurjectiveAfterBaseChange T) :
    D.IsSurjectiveAfterBaseChange T'
```

**`Stacks.Flatness.ModuleMapBaseChangeSituation.isZeroAfterBaseChange_of_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/ModuleMapBaseChange.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/ModuleMapBaseChange.lean#L209). The attribute's comment: “functoriality of the zero condition”.

> Being zero after base change is preserved by every further base change.

```lean
theorem isZeroAfterBaseChange_of_hom (D : ModuleMapBaseChangeSituation.{u}) {T T' : Over D.S}
    (g : T' ⟶ T) (h : D.IsZeroAfterBaseChange T) : D.IsZeroAfterBaseChange T'
```

**`Stacks.Flatness.ModuleMapBaseChangeSituation.isomorphismFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/ModuleMapBaseChange.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/ModuleMapBaseChange.lean#L218). The attribute's comment: “the isomorphism functor”.

> The subterminal functor on schemes over the base recording where the base-changed
> homomorphism is an isomorphism.

```lean
noncomputable def isomorphismFunctor (D : ModuleMapBaseChangeSituation.{u}) :
    (Over D.S)ᵒᵖ ⥤ Type
```

**`Stacks.Flatness.ModuleMapBaseChangeSituation.surjectivityFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/ModuleMapBaseChange.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/ModuleMapBaseChange.lean#L228). The attribute's comment: “the surjectivity functor”.

> The subterminal functor on schemes over the base recording where the base-changed
> homomorphism is surjective.

```lean
noncomputable def surjectivityFunctor (D : ModuleMapBaseChangeSituation.{u}) :
    (Over D.S)ᵒᵖ ⥤ Type
```

**`Stacks.Flatness.ModuleMapBaseChangeSituation.zeroFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/ModuleMapBaseChange.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/ModuleMapBaseChange.lean#L238). The attribute's comment: “the zero functor”.

> The subterminal functor on schemes over the base recording where the base-changed
> homomorphism is zero.

```lean
noncomputable def zeroFunctor (D : ModuleMapBaseChangeSituation.{u}) :
    (Over D.S)ᵒᵖ ⥤ Type
```

## Tag 05MJ, a lemma

[Tag 05MJ](https://stacks.math.columbia.edu/tag/05MJ) in the Stacks Project.

**`Stacks.Flatness.ModuleMapBaseChangeSituation.isomorphismFunctor_isSheaf_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctors/FpqcSheaf.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctors/FpqcSheaf.lean#L76). The attribute's comment: “iso_fpqc”.

> The isomorphism functor of a homomorphism of quasi-coherent modules satisfies the sheaf
> condition for the fpqc topology on schemes over the base.

```lean
theorem isomorphismFunctor_isSheaf_fpqc (D : ModuleMapBaseChangeSituation.{u}) :
    Presheaf.IsSheaf (Scheme.fpqcTopology.over D.S) D.isomorphismFunctor
```

**`Stacks.Flatness.ModuleMapBaseChangeSituation.surjectivityFunctor_isSheaf_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctors/FpqcSheaf.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctors/FpqcSheaf.lean#L85). The attribute's comment: “surj_fpqc”.

> The surjectivity functor of a homomorphism of quasi-coherent modules satisfies the sheaf
> condition for the fpqc topology on schemes over the base.

```lean
theorem surjectivityFunctor_isSheaf_fpqc (D : ModuleMapBaseChangeSituation.{u}) :
    Presheaf.IsSheaf (Scheme.fpqcTopology.over D.S) D.surjectivityFunctor
```

**`Stacks.Flatness.ModuleMapBaseChangeSituation.zeroFunctor_isSheaf_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctors/FpqcSheaf.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctors/FpqcSheaf.lean#L94). The attribute's comment: “zero_fpqc”.

> The zero functor of a homomorphism of quasi-coherent modules satisfies the sheaf condition
> for the fpqc topology on schemes over the base.

```lean
theorem zeroFunctor_isSheaf_fpqc (D : ModuleMapBaseChangeSituation.{u}) :
    Presheaf.IsSheaf (Scheme.fpqcTopology.over D.S) D.zeroFunctor
```

**`Stacks.Flatness.ModuleMapBaseChangeSituation.injectivityFunctor_isSheaf_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctors/FpqcSheaf.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctors/FpqcSheaf.lean#L103). The attribute's comment: “inj_fpqc”.

> The injectivity functor of a homomorphism of quasi-coherent modules satisfies the sheaf
> condition for the fpqc topology on the category of schemes over the base with flat morphisms.

```lean
theorem injectivityFunctor_isSheaf_fpqc (D : ModuleMapBaseChangeSituation.{u}) :
    Presheaf.IsSheaf
      (Scheme.fpqcPrecoverage.comap
        (wideSubcategoryInclusion (FlatMorphismOver D.S) ⋙ Over.forget D.S)).toGrothendieck
      D.injectivityFunctor
```

**`Stacks.Flatness.ModuleMapBaseChangeSituation.isomorphismFunctor_preservesColimit_of_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctors/IsomorphismLimit.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctors/IsomorphismLimit.lean#L249). The attribute's comment: “iso_limit”.

> **Stacks Project, Tag 05MJ.** The isomorphism functor of a homomorphism of quasi-coherent
> modules with source of finite type and target of finite presentation, along a quasi-compact
> morphism, preserves the filtered colimit attached to a cofiltered inverse system of affine
> schemes over the base.

```lean
theorem isomorphismFunctor_preservesColimit_of_isAffine (D : ModuleMapBaseChangeSituation.{u})
    [QuasiCompact D.f] [D.F.IsFiniteType] [D.G.IsFinitePresentation] (I : Type u)
    [Category.{u} I] [IsCofiltered I] (T : I ⥤ Over D.S) (hT : ∀ i, IsAffine (T.obj i).left) :
    PreservesColimit T.op D.isomorphismFunctor
```

**`Stacks.Flatness.ModuleMapBaseChangeSituation.surjectivityFunctor_preservesColimit_of_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctors/SurjectivityLimit.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctors/SurjectivityLimit.lean#L101). The attribute's comment: “surj_limit”.

> **Stacks Project, Tag 05MJ.**  The surjectivity functor of a homomorphism of quasi-coherent
> modules with target of finite type, along a quasi-compact morphism, preserves the filtered
> colimit attached to a cofiltered inverse system of affine schemes over the base.

```lean
theorem surjectivityFunctor_preservesColimit_of_isAffine (D : ModuleMapBaseChangeSituation.{u})
    [QuasiCompact D.f] [D.G.IsFiniteType] (I : Type u) [Category.{u} I] [IsCofiltered I]
    (T : I ⥤ Over D.S) (hT : ∀ i, IsAffine (T.obj i).left) :
    PreservesColimit T.op D.surjectivityFunctor
```

**`Stacks.Flatness.ModuleMapBaseChangeSituation.zeroFunctor_preservesColimit_of_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctors/ZeroLimit.lean, line 340](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctors/ZeroLimit.lean#L340). The attribute's comment: “zero_limit”.

> **Stacks Project, Tag 05MJ.**  The zero functor of a homomorphism of quasi-coherent modules
> with source of finite type, along a quasi-compact morphism, preserves the filtered colimit
> attached to a cofiltered inverse system of affine schemes over the base.

```lean
theorem zeroFunctor_preservesColimit_of_isAffine (D : ModuleMapBaseChangeSituation.{u})
    [QuasiCompact D.f] [D.F.IsFiniteType] (I : Type u) [Category.{u} I] [IsCofiltered I]
    (T : I ⥤ Over D.S) (hT : ∀ i, IsAffine (T.obj i).left) :
    PreservesColimit T.op D.zeroFunctor
```

## Tag 05MK, a situation

[Tag 05MK](https://stacks.math.columbia.edu/tag/05MK) in the Stacks Project.

**`LocalAlgCat`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/HenselianFlattening.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/HenselianFlattening.lean#L103). The attribute's comment: “objects”.

> **Stacks Project, Tag 05MK.** An object of the category `C`: a local `A`-algebra whose
> structure homomorphism is a local homomorphism of local rings.

```lean
structure LocalAlgCat (A : Type u) [CommRing A] [IsLocalRing A]
```

**`LocalAlgCat.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/HenselianFlattening.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/HenselianFlattening.lean#L129). The attribute's comment: “morphisms”.

> **Stacks Project, Tag 05MK.** A morphism of the category `C`: a local homomorphism of
> `A`-algebras.

```lean
structure Hom (R S : LocalAlgCat.{u, v} A)
```

**An instance with no name** in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/HenselianFlattening.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/HenselianFlattening.lean#L138). The attribute's comment: “the category”.

> **Stacks Project, Tag 05MK.** Local `A`-algebras and local `A`-algebra homomorphisms form a
> category.

```lean
instance : Category (LocalAlgCat.{u, v} A)
```

**`Module.FlatAtPointSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/HenselianFlattening.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/HenselianFlattening.lean#L171). The attribute's comment: “the situation”.

> **Stacks Project, Tag 05MK.** The standing data of the local flattening problem: a local
> homomorphism `A → B` of local rings and a `B`-module `M`.

```lean
structure FlatAtPointSituation
```

**`Module.FlatAtPointSituation.ConditionOn.of_isLocalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/HenselianFlattening.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/HenselianFlattening.lean#L235). The attribute's comment: “base-change stability”.

> **Stacks Project, Tag 05MK.** The flatness condition is preserved by a local homomorphism of
> local `A`-algebras. The source and the target may live in different universes.

```lean
theorem ConditionOn.of_isLocalHom {S : FlatAtPointSituation.{u, v, w}} (R : Type x) (T : Type y)
    [CommRing R] [IsLocalRing R] [Algebra S.A R] [CommRing T] [IsLocalRing T] [Algebra S.A T]
    [Algebra R T] [IsScalarTower S.A R T] [IsLocalHom (algebraMap R T)] (h : S.ConditionOn R) :
    S.ConditionOn T
```

**`Module.FlatAtPointSituation.condition_of_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/HenselianFlattening.lean, line 244](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/HenselianFlattening.lean#L244). The attribute's comment: “base-change stability”.

> **Stacks Project, Tag 05MK.** The flatness condition is preserved by a morphism of the
> category `C` of local `A`-algebras; this is what makes `F_lf` a functor.

```lean
theorem condition_of_hom (S : FlatAtPointSituation.{u, v, w}) {R T : LocalAlgCat.{u, x} S.A}
    (f : R ⟶ T) (h : S.Condition R) : S.Condition T
```

**`Module.FlatAtPointSituation.flatAtPointFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/HenselianFlattening.lean, line 312](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/HenselianFlattening.lean#L312). The attribute's comment: “the functor”.

> **Stacks Project, Tag 05MK.** The functor `F_lf` on the category `C` of local `A`-algebras:
> it takes the value a singleton where the flatness condition holds, and the empty set elsewhere.
> Functoriality is `condition_of_hom`.

```lean
def flatAtPointFunctor (S : FlatAtPointSituation.{u, v, w}) :
    LocalAlgCat.{u, x} S.A ⥤ Type
```

## Tag 05ML, an equation

[Tag 05ML](https://stacks.math.columbia.edu/tag/05ML) in the Stacks Project.

**`Module.FlatAtPointSituation.ConditionOn`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/HenselianFlattening.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/HenselianFlattening.lean#L213).

> **Stacks Project, Tag 05ML.** The flatness condition on a local `A`-algebra `R`: the base
> change of `M` is flat over `R` at every prime of `B ⊗[A] R` containing the extensions of the
> maximal ideals of `R` and of `B`. This is the condition of Stacks Tag 05LQ for the ideals
> `I' = m_R` and `J = m_B`.

```lean
def ConditionOn (S : FlatAtPointSituation.{u, v, w}) (R : Type x) [CommRing R] [IsLocalRing R]
    [Algebra S.A R] : Prop
```

**`Module.FlatAtPointSituation.Condition`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/HenselianFlattening.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/HenselianFlattening.lean#L221).

> **Stacks Project, Tag 05ML.** The flatness condition read on an object of the category `C`
> of Stacks Tag 05MK.

```lean
abbrev Condition (S : FlatAtPointSituation.{u, v, w}) (R : LocalAlgCat.{u, x} S.A) : Prop
```

## Tag 05MN, a lemma

[Tag 05MN](https://stacks.math.columbia.edu/tag/05MN) in the Stacks Project.

**`Module.FlatAtPointSituation.condition_iff_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/FlatteningFlatDescent.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/FlatteningFlatDescent.lean#L110). The attribute's comment: “flat_base_change”.

> **Stacks Project, Tag 05MN part (1)**, read on a morphism of the category `C` of local
> `A`-algebras of Stacks Tag 05MK: if `f : R ⟶ T` is flat then `F_lf(R) = F_lf(T)`, both being
> determined by the flatness condition of Stacks Tag 05ML.

```lean
theorem condition_iff_of_flat (S : FlatAtPointSituation.{u, v, w}) {R T : LocalAlgCat.{u, x} S.A}
    (f : R ⟶ T) (hf : f.hom.toRingHom.Flat) :
    S.Condition R ↔ S.Condition T
```

**`Module.FlatAtPointSituation.flatAtPointFunctor_obj_eq_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/FlatteningFlatDescent.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/FlatteningFlatDescent.lean#L125). The attribute's comment: “flat_base_change”.

> **Stacks Project, Tag 05MN part (1)**, in the shape the source states it: the functor `F_lf`
> of Stacks Tag 05MM takes the same value at the two ends of a flat morphism of the category `C`.
>
> The values are `PLift` of the flatness condition of Stacks Tag 05ML, so this is
> `Module.FlatAtPointSituation.condition_iff_of_flat` read through `propext`.

```lean
theorem flatAtPointFunctor_obj_eq_of_flat (S : FlatAtPointSituation.{u, v, w})
    {R T : LocalAlgCat.{u, x} S.A} (f : R ⟶ T) (hf : f.hom.toRingHom.Flat) :
    S.flatAtPointFunctor.obj R = S.flatAtPointFunctor.obj T
```

**`Module.FlatAtPointSituation.condition_colimit_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/FlatteningLimitPreserving.lean, line 324](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/FlatteningLimitPreserving.lean#L324). The attribute's comment: “limit_preserving”.

> **Stacks Project, Tag 05MN part (2)**, as an equivalence: the flatness condition of
> Stacks Tag 05ML holds over the apex of a filtered colimit of local `A`-algebras exactly when it
> holds at one of the stages. The easy direction is base-change stability,
> `Module.FlatAtPointSituation.condition_of_hom`.
>
> Beyond the hypotheses of the source nothing is assumed about the colimit: that it is computed on
> the underlying sets, which is what Stacks Tag 05LT needs, is proved in
> `Stacks.CommAlgCat.forget_preservesFilteredColimitsOfSize`. The two `UnivLE` hypotheses are the
> size condition that result carries, namely that the index category be no larger than the
> algebras; a directed system in the sense of the source is indexed by a set and satisfies it.

```lean
theorem condition_colimit_iff
    (hS : (algebraMap S.A S.B).EssentiallyOfFinitePresentation)
    [Module.FinitePresentation S.B S.M]
    (hτ : IsColimit (toCommAlgCat.mapCocone τ)) :
    S.Condition τ.pt ↔ ∃ lam, S.Condition (F.obj lam)
```

**`Module.FlatAtPointSituation.isColimitMapCoconeFlatAtPointFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/FlatteningLimitPreserving.lean, line 349](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/FlatteningLimitPreserving.lean#L349). The attribute's comment: “limit_preserving”.

> **Stacks Project, Tag 05MN part (2).** If `A → B` is essentially of finite presentation and
> `M` is a `B`-module of finite presentation, then the functor `F_lf` of Stacks Tag 05MM is limit
> preserving: for a directed system `{A_i}` of objects of the category `C` of Stacks Tag 05MK,
> `F_lf(colim A_i) = colim F_lf(A_i)`.
>
> The colimit of the system is read off the underlying system of `A`-algebras; it does lie in `C`,
> by `LocalAlgCat.isLocalRing_pt_of_isColimit` and `LocalAlgCat.isLocalHom_ι_of_isColimit`. The
> statement is that the induced cocone of sets is a colimit, which by
> `CategoryTheory.Limits.Types.FilteredColimit.isColimitOf` amounts to the descent statement
> `Module.FlatAtPointSituation.exists_condition_of_isColimit`, every value of `F_lf` having at
> most one element.
>
> That the colimit of `A`-algebras is computed on the underlying sets is not assumed but proved,
> in `Stacks.CommAlgCat.forget_preservesFilteredColimitsOfSize`; the two `UnivLE` hypotheses are
> the size condition it carries, that the index category of the directed system be no larger than
> the algebras.

```lean
noncomputable def isColimitMapCoconeFlatAtPointFunctor
    (hS : (algebraMap S.A S.B).EssentiallyOfFinitePresentation)
    [Module.FinitePresentation S.B S.M]
    (hτ : IsColimit (toCommAlgCat.mapCocone τ)) :
    IsColimit (S.flatAtPointFunctor.mapCocone τ)
```

## Tag 05P4, a lemma

[Tag 05P4](https://stacks.math.columbia.edu/tag/05P4) in the Stacks Project.

**`Module.FlatAtPointSituation.flatAtPointFunctor_eq_of_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/FlatAtPointFinite.lean, line 258](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/FlatAtPointFinite.lean#L258).

> **Stacks Project, Tag 05P4.** Replacing the local algebra of a flat-at-a-point situation by
> a finite local extension, and its module by an isomorphic module over that extension, does not
> change the flat-at-a-point functor.

```lean
public theorem flatAtPointFunctor_eq_of_finite (S : FlatAtPointSituation.{u, v, w})
    {C : Type x} [CommRing C] [IsLocalRing C] [Algebra S.A C] [IsLocalHom (algebraMap S.A C)]
    {N : Type y} [AddCommGroup N] [Module C N] (f : S.B →ₐ[S.A] C)
    (hf : IsLocalHom f.toRingHom) (hfinite : f.toRingHom.Finite)
    (e : letI : Module S.B N := Module.compHom N f.toRingHom
      S.M ≃ₗ[S.B] N) :
    flatAtPointFunctor.{u, v, w, z} S =
      flatAtPointFunctor.{u, x, y, z} ({ A := S.A, B := C, M := N } :
        FlatAtPointSituation.{u, x, y})
```

## Tag 05P5, a lemma

[Tag 05P5](https://stacks.math.columbia.edu/tag/05P5) in the Stacks Project.

**`Module.FlatAtPointSituation.flatAtPointFunctor_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/FlatAtPointFlatBaseChange.lean, line 438](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/FlatAtPointFlatBaseChange.lean#L438).

> **Stacks Project, Tag 05P5.** A flat local extension of the local algebra, with the module
> extended along it, does not change the flat-at-a-point functor.

```lean
public theorem flatAtPointFunctor_baseChange (S : FlatAtPointSituation.{u, v, w}) (C : Type z)
    [CommRing C] [IsLocalRing C] [Algebra S.B C] [IsLocalHom (algebraMap S.B C)]
    [Module.Flat S.B C] :
    (S.flatAtPointFunctor : LocalAlgCat.{u, x} S.A ⥤ Type) =
      (baseChange S C).flatAtPointFunctor
```

## Tag 05MP, a situation

[Tag 05MP](https://stacks.math.columbia.edu/tag/05MP) in the Stacks Project.

**`AlgebraicGeometry.FreeAtGenericPointsSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/FreeAtGenericPoints.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/FreeAtGenericPoints.lean#L76). The attribute's comment: “the situation”.

> The standing situation of a smooth morphism with geometrically irreducible fibres and a
> finite type quasi-coherent module on its source.

```lean
structure FreeAtGenericPointsSituation
```

**`AlgebraicGeometry.FreeAtGenericPointsSituation.Condition`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/FreeAtGenericPoints.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/FreeAtGenericPoints.lean#L113). The attribute's comment: “the fibrewise condition”.

> The module pulled back to `X ×_S T` is free of rank `p` near the generic point of
> every fibre over `T`.

```lean
abbrev Condition (D : FreeAtGenericPointsSituation.{u}) (p : ℕ)
    (T : Over D.S) : Prop
```

**`AlgebraicGeometry.FreeAtGenericPointsSituation.condition_of_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/FreeAtGenericPoints.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/FreeAtGenericPoints.lean#L195). The attribute's comment: “base-change stability”.

> The fibrewise generic-point condition is preserved by a further base change.

```lean
theorem condition_of_hom (D : FreeAtGenericPointsSituation.{u}) (p : ℕ)
    {T T' : Over D.S} (g : T' ⟶ T) (h : D.Condition p T) :
    D.Condition p T'
```

**`AlgebraicGeometry.FreeAtGenericPointsSituation.freeAtGenericPointsFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/FreeAtGenericPoints.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/FreeAtGenericPoints.lean#L259). The attribute's comment: “the functor”.

> The subterminal set-valued functor recording whether the pulled-back module is free of
> rank `p` near the generic point of every fibre.

```lean
noncomputable def freeAtGenericPointsFunctor
    (D : FreeAtGenericPointsSituation.{u}) (p : ℕ) :
    (Over D.S)ᵒᵖ ⥤ Type u
```

## Tag 05MS, a lemma

[Tag 05MS](https://stacks.math.columbia.edu/tag/05MS) in the Stacks Project.

**`AlgebraicGeometry.FreeAtGenericPointsSituation.freeAtGenericPointsFunctor_limitPreserving_small`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/FreeAtGenericPointsDescent.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/FreeAtGenericPointsDescent.lean#L248). The attribute's comment: “part (2), the generic-rank functor is limit preserving”.

> **Stacks Project, Tag 05MS, part (2).** The generic-rank functor of a module of finite
> presentation is limit preserving: over a cofiltered limit of affine schemes over the base the
> functor has a section as soon as one stage of the system has one.
>
> The approximation statement which `freeAtGenericPointsFunctor_limitPreserving_small_iff`
> identifies with this clause is
> `AlgebraicGeometry.FreeAtGenericPointsSituation.exists_condition_of_isLimit`, so nothing is
> assumed here.

```lean
theorem freeAtGenericPointsFunctor_limitPreserving_small [D.F.IsFinitePresentation] :
    LimitPreserving.{u, u, u, u, u + 1, u} (Over.forget D.S)
      (D.freeAtGenericPointsFunctor p)
```

**`AlgebraicGeometry.FreeAtGenericPointsSituation.freeAtGenericPointsFunctor_isSheaf_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/FreeAtGenericPointsFpqcSheaf.lean, line 314](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/FreeAtGenericPointsFpqcSheaf.lean#L314). The attribute's comment: “part (1), the generic-rank functor is an fpqc sheaf”.

> **Stacks Project, Tag 05MS, part (1).** The generic-rank functor satisfies the sheaf property
> for the fpqc topology.
>
> By `freeAtGenericPointsFunctor_isSheaf_fpqc_of_fpqcCover` this is fpqc-locality of the
> generic-point condition, and the source proves that locality in two steps: descent along the
> covering gives a free stalk of rank `p` at the generic point of every fibre over the base
> (`stalkFreeOfRank_of_fpqcCover`), and
> `AlgebraicGeometry.freeAtPointOfRank_of_forall_stalkFreeOfRank` spreads those free stalks out to
> neighbourhoods.

```lean
theorem freeAtGenericPointsFunctor_isSheaf_fpqc (D : FreeAtGenericPointsSituation.{u}) (p : ℕ) :
    Presheaf.IsSheaf (Scheme.fpqcTopology.over D.S) (D.freeAtGenericPointsFunctor p)
```

## Tag 0CWF, a lemma

[Tag 0CWF](https://stacks.math.columbia.edu/tag/0CWF) in the Stacks Project.

**`AlgebraicGeometry.topologicalKrullDim_not_isFlatOverAt_fiber_lt_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/NonFlatLocusFibreDimension.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/NonFlatLocusFibreDimension.lean#L288). The attribute's comment: “the dimension criterion”.

> **Stacks Project, Tag 0CWF.** Let `f : X ⟶ S` be locally of finite type, let `F` be a
> quasi-coherent `𝒪_X`-module of finite type and let `n` be a natural number. The closed subset of
> each fibre where `F` is not flat over `S` has dimension less than `n` if and only if
> `trdeg_{κ(f x)} κ(x) < n` at every point `x` where `F` is not flat over `S`.

```lean
theorem topologicalKrullDim_not_isFlatOverAt_fiber_lt_iff {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType] (n : ℕ) :
    (∀ s : S, topologicalKrullDim
        ↥{y : f.fiber s | ¬ IsFlatOverAt f.toLRSHom.toShHom F (f.fiberι s y)} <
          (n : WithBot ℕ∞)) ↔
      ∀ x : X, ¬ IsFlatOverAt f.toLRSHom.toShHom F x →
        letI : Algebra (S.residueField (f x)) (X.residueField x) :=
          (f.residueFieldMap x).hom.toAlgebra
        (Cardinal.toENat (Algebra.trdeg (S.residueField (f x)) (X.residueField x)) :
          WithBot ℕ∞) < (n : WithBot ℕ∞)
```

**`AlgebraicGeometry.topologicalKrullDim_not_isFlatOverAt_fiber_lt_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/NonFlatLocusFibreDimension.lean, line 307](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/NonFlatLocusFibreDimension.lean#L307). The attribute's comment: “stability under base change”.

> **Stacks Project, Tag 0CWF.** The dimension criterion is stable under base change: if the
> non-flat locus has dimension less than `n` in every fibre of `f`, then the same holds for the
> pullback of `F` along any base change of `f`.

```lean
theorem topologicalKrullDim_not_isFlatOverAt_fiber_lt_of_isPullback {X S S' X' : Scheme.{u}}
    {f : X ⟶ S} {g : S' ⟶ S} {g' : X' ⟶ X} {f' : X' ⟶ S'} (hsq : IsPullback g' f' f g)
    [LocallyOfFiniteType f] (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType] (n : ℕ)
    (hF : ∀ s : S, topologicalKrullDim
        ↥{y : f.fiber s | ¬ IsFlatOverAt f.toLRSHom.toShHom F (f.fiberι s y)} <
          (n : WithBot ℕ∞)) (s' : S') :
    topologicalKrullDim
        ↥{y : f'.fiber s' | ¬ IsFlatOverAt f'.toLRSHom.toShHom
            ((Scheme.Modules.pullback g').obj F) (f'.fiberι s' y)} < (n : WithBot ℕ∞)
```

## Tag 0CWG, a definition

[Tag 0CWG](https://stacks.math.columbia.edu/tag/0CWG) in the Stacks Project.

**`AlgebraicGeometry.IsFlatOverInDimensionsGE`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/FlatInDimensionsGE.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/FlatInDimensionsGE.lean#L83).

> **Stacks Project, Tag 0CWG.** Let `f : X ⟶ S` be locally of finite type and let `F` be a
> quasi-coherent `𝒪_X`-module of finite type. Then `F` is *flat over `S` in dimensions `≥ n`* if
> for every point `s` of `S` the closed subset of the fibre `X_s` of points at which `F` is not
> flat over `S` has dimension less than `n`.
>
> This is the first of the two equivalent conditions of Stacks 0CWF; the second one is
> `AlgebraicGeometry.isFlatOverInDimensionsGE_iff_forall_toENat_trdeg_lt`.

```lean
def IsFlatOverInDimensionsGE {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType] (n : ℕ) : Prop
```

## Tag 05MT, a situation

[Tag 05MT](https://stacks.math.columbia.edu/tag/05MT) in the Stacks Project.

**`AlgebraicGeometry.FlatDimensionSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/FlatDimensionFunctor.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/FlatDimensionFunctor.lean#L83). The attribute's comment: “the situation”.

> A morphism of schemes `f : X ⟶ S` locally of finite type together with a quasi-coherent
> module `F` of finite type on `X` and a bound `n` on fibre dimensions.

```lean
public structure FlatDimensionSituation
```

**`AlgebraicGeometry.FlatDimensionSituation.baseChangeMap`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/FlatDimensionFunctor.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/FlatDimensionFunctor.lean#L107). The attribute's comment: “the base-changed morphism”.

> The base-changed morphism `X_T = X ×_S T ⟶ T`.

```lean
public noncomputable abbrev baseChangeMap (D : FlatDimensionSituation.{u}) (T : Over D.S) :
    pullback D.f T.hom ⟶ T.left
```

**`AlgebraicGeometry.FlatDimensionSituation.baseChangeModule`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/FlatDimensionFunctor.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/FlatDimensionFunctor.lean#L114). The attribute's comment: “the base-changed module”.

> The base change `F_T` of the module, i.e. its pullback along the projection
> `X_T = X ×_S T ⟶ X`.

```lean
public noncomputable abbrev baseChangeModule (D : FlatDimensionSituation.{u}) (T : Over D.S) :
    (pullback D.f T.hom).Modules
```

**`AlgebraicGeometry.FlatDimensionSituation.baseChangeMap_locallyOfFiniteType`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/FlatDimensionFunctor.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/FlatDimensionFunctor.lean#L120). The attribute's comment: “X_T → T is of finite type”.

> The base-changed morphism `X_T ⟶ T` is again locally of finite type.

```lean
public instance baseChangeMap_locallyOfFiniteType (D : FlatDimensionSituation.{u})
    (T : Over D.S) : LocallyOfFiniteType (D.baseChangeMap T)
```

**`AlgebraicGeometry.FlatDimensionSituation.baseChangeModule_isFiniteType`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/FlatDimensionFunctor.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/FlatDimensionFunctor.lean#L127). The attribute's comment: “F_T is of finite type”.

> The base-changed module `F_T` is again of finite type.

```lean
public noncomputable instance baseChangeModule_isFiniteType (D : FlatDimensionSituation.{u})
    (T : Over D.S) : (D.baseChangeModule T).IsFiniteType
```

**`AlgebraicGeometry.FlatDimensionSituation.IsFlatInDimensionsGEAfterBaseChange`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/FlatDimensionFunctor.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/FlatDimensionFunctor.lean#L139). The attribute's comment: “the condition tested by the functor”.

> The base-changed module `F_T` is flat over `T` in dimensions `≥ n`.

```lean
public noncomputable abbrev IsFlatInDimensionsGEAfterBaseChange
    (D : FlatDimensionSituation.{u}) (T : Over D.S) : Prop
```

**`AlgebraicGeometry.FlatDimensionSituation.isFlatInDimensionsGEAfterBaseChange_of_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/FlatDimensionFunctor.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/FlatDimensionFunctor.lean#L156). The attribute's comment: “base-change stability of the condition”.

> Flatness of the base-changed module in dimensions `≥ n` is inherited along a morphism
> `T' ⟶ T` of schemes over `S`.

```lean
public theorem isFlatInDimensionsGEAfterBaseChange_of_hom (D : FlatDimensionSituation.{u})
    {T T' : Over D.S} (g : T' ⟶ T) (h : D.IsFlatInDimensionsGEAfterBaseChange T) :
    D.IsFlatInDimensionsGEAfterBaseChange T'
```

**`AlgebraicGeometry.FlatDimensionSituation.flatDimensionFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/FlatDimensionFunctor.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/FlatDimensionFunctor.lean#L166). The attribute's comment: “the functor F_n”.

> The functor `F_n : (Sch/S)ᵒᵖ ⥤ Sets` sending a scheme `T` over `S` to a singleton if `F_T`
> is flat over `T` in dimensions `≥ n`, and to the empty set otherwise.

```lean
public noncomputable def flatDimensionFunctor (D : FlatDimensionSituation.{u}) :
    (Over D.S)ᵒᵖ ⥤ Type
```

## Tag 05MV, a lemma

[Tag 05MV](https://stacks.math.columbia.edu/tag/05MV) in the Stacks Project.

**`AlgebraicGeometry.FlatDimensionSituation.flatDimensionFunctor_isSheaf_fpqc_and_limitPreserving`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/FlatDimensionSheafAndLimitPreserving.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/FlatDimensionSheafAndLimitPreserving.lean#L63). The attribute's comment: “parts (1) and (2)”.

> **Stacks Project, Tag 05MV.** In Situation 05MT:
>
> 1. the functor `F_n` satisfies the sheaf property for the fpqc topology; and
> 2. if `f` is quasi-compact and locally of finite presentation and `F` is of finite presentation,
>    then the functor `F_n` is limit preserving, i.e. it carries a cofiltered inverse limit of
>    affine schemes over `S` to a filtered colimit of sets.
>
> The three finiteness assumptions of (2) are hypotheses of (2) only: (1) holds in the ambient
> situation alone.

```lean
public theorem flatDimensionFunctor_isSheaf_fpqc_and_limitPreserving
    (D : FlatDimensionSituation.{max u v w}) :
    Presheaf.IsSheaf (Scheme.fpqcTopology.over D.S) D.flatDimensionFunctor ∧
      (QuasiCompact D.f → LocallyOfFinitePresentation D.f → D.F.IsFinitePresentation →
        LimitPreserving.{max u v w, 0, v, w, max u v w + 1, max u v w}
          (Over.forget D.S) D.flatDimensionFunctor)
```

## Tag 05MW, a situation

[Tag 05MW](https://stacks.math.columbia.edu/tag/05MW) in the Stacks Project.

**`AlgebraicGeometry.FlatnessSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/Basic.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/Basic.lean#L61). The attribute's comment: “the situation”.

> A morphism of schemes together with a quasi-coherent module on its source.

```lean
public structure FlatnessSituation
```

**`AlgebraicGeometry.FlatnessSituation.baseChange`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/Basic.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/Basic.lean#L78). The attribute's comment: “the base-changed scheme”.

> The fibre product `X ×_S T`.

```lean
public noncomputable abbrev baseChange (D : FlatnessSituation.{u})
    (T : Over D.S) : Scheme.{u}
```

**`AlgebraicGeometry.FlatnessSituation.baseChangeModule`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/Basic.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/Basic.lean#L84). The attribute's comment: “the base-changed module”.

> The pullback of the module to `X ×_S T`.

```lean
public noncomputable abbrev baseChangeModule (D : FlatnessSituation.{u})
    (T : Over D.S) :
    SheafOfModules.{u} (structureSheafRing (D.baseChange T).toRingedSpace)
```

**`AlgebraicGeometry.FlatnessSituation.IsFlatAfterBaseChange`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/Basic.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/Basic.lean#L91). The attribute's comment: “the flatness condition”.

> The base-changed module is flat over `T`.

```lean
public abbrev IsFlatAfterBaseChange (D : FlatnessSituation.{u})
    (T : Over D.S) : Prop
```

**`AlgebraicGeometry.FlatnessSituation.isFlatAfterBaseChange_of_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/Basic.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/Basic.lean#L130). The attribute's comment: “base-change stability”.

> Flatness of the pulled-back module persists under further base change.

```lean
public theorem isFlatAfterBaseChange_of_hom (D : FlatnessSituation.{u})
    {T T' : Over D.S} (g : T' ⟶ T) (h : D.IsFlatAfterBaseChange T) :
    D.IsFlatAfterBaseChange T'
```

**`AlgebraicGeometry.FlatnessSituation.flatFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/Basic.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/Basic.lean#L137). The attribute's comment: “the functor”.

> The subterminal functor recording flatness of the base-changed module.

```lean
public noncomputable def flatFunctor (D : FlatnessSituation.{u}) :
    (Over D.S)ᵒᵖ ⥤ Type
```

## Tag 05MY, a lemma

[Tag 05MY](https://stacks.math.columbia.edu/tag/05MY) in the Stacks Project.

**`AlgebraicGeometry.FlatnessSituation.flatFunctor_isSheaf_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/FpqcSheaf.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/FpqcSheaf.lean#L118). The attribute's comment: “flat_functor_fpqc_sheaf”.

> **Stacks Project, Tag 05MY.** Part (1): the flatness functor of a quasi-coherent module
> satisfies the sheaf condition for the fpqc topology on schemes over the base.

```lean
public theorem flatFunctor_isSheaf_fpqc :
    Presheaf.IsSheaf (Scheme.fpqcTopology.over D.S) D.flatFunctor
```

**`AlgebraicGeometry.FlatnessSituation.flatFunctor_limitPreserving`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/LimitPreserving.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/LimitPreserving.lean#L288). The attribute's comment: “flat_functor_limit_preserving”.

> **Stacks Project, Tag 05MY.** Part (2): for a quasi-compact morphism which is locally of
> finite presentation and a quasi-coherent module of finite presentation, the flatness functor is
> limit preserving: it carries a cofiltered inverse limit of affine schemes over the base to a
> filtered colimit of sets.

```lean
public theorem flatFunctor_limitPreserving (D : FlatnessSituation.{max u v w})
    [QuasiCompact D.f] [LocallyOfFinitePresentation D.f] [D.F.IsFinitePresentation] :
    LimitPreserving.{max u v w, 0, v, w, max u v w + 1, max u v w}
      (Over.forget D.S) D.flatFunctor
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.20, Tag 05MG](https://stacks.math.columbia.edu/tag/05MG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
