---
declaration: section
origin: cited
lean: AlgebraicGeometry.RingedToposHom.IsFlat, AlgebraicGeometry.RingedSite.Hom.IsFlat, Stacks.SheafOfModules.InternalHom.preservesFiniteLimits_ringedSitePullback_of_isFlat, CategoryTheory.Sites.abelianInverseImage_exact, Stacks.Sheaves.RingedToposModules.pullbackModules_exact_of_isFlatMap, AlgebraicGeometry.SheafOfModules.IsFlat, AlgebraicGeometry.RingedToposHom.IsFlatOver, Stacks.SheafOfModules.InternalHom.isIso_pullbackInternalHomMap_of_isFinitePresentationOnSite
statement: formalized
proof: formalized
---

# 18.31 Flat morphisms

Section 18.31 of the Stacks Project, [Tag 04JA](https://stacks.math.columbia.edu/tag/04JA). 4 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04JB, a definition

[Tag 04JB](https://stacks.math.columbia.edu/tag/04JB) in the Stacks Project.

**`AlgebraicGeometry.RingedToposHom.IsFlat`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/FlatMorphisms/RingedTopoi.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/FlatMorphisms/RingedTopoi.lean#L49). The attribute's comment: “flat morphisms of ringed topoi”. References: SGA 4 Vbis (2.4.3.1), “non-fibered case”; SGA 4 V (1.8), “left flat”.

> A morphism of ringed topoi is flat when its inverse-image structure map is flat.

```lean
abbrev IsFlat {X : RingedTopos.{v, u, w}} {Y : RingedTopos.{v', u', w'}}
    [X.J.HasSheafCompose (forget RingCat.{w})]
    [Y.J.HasSheafCompose (forget RingCat.{w'})]
    [X.J.HasSheafCompose (forget₂ CommRingCat.{w} RingCat.{w})]
    [Y.J.HasSheafCompose (forget₂ CommRingCat.{w'} RingCat.{w'})]
    (f : RingedToposHom X Y) : Prop
```

Declarations registered for the tag:

- [`AlgebraicGeometry.RingedSite.Hom.IsFlat`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/FlatMorphisms/RingedSites.lean#L142), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Modules/FlatMorphisms/RingedTopoi.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/FlatMorphisms/RingedTopoi.lean#L59) (StacksFrontier): “flat morphisms of ringed sites”.

## Tag 04JC, a lemma

[Tag 04JC](https://stacks.math.columbia.edu/tag/04JC) in the Stacks Project.

**`Stacks.SheafOfModules.InternalHom.preservesFiniteLimits_ringedSitePullback_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/PullbackInternalHomFlat.lean, line 1147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/PullbackInternalHomFlat.lean#L1147). The attribute's comment: “left exactness of the flat pullback, for a morphism of ringed sites”.

> **Stacks 04JC for a morphism of ringed sites.** If `f` is flat — that is, if `O_C` is flat
> as an `f⁻¹O_D`-module — then the pullback `f^* : Mod(O_D) ⥤ Mod(O_C)` of sheaves of modules
> preserves finite limits.
>
> This is `Stacks.Sheaves.RingedToposModules.pullbackModules_exact_of_isFlatMap` at the morphism
> of ringed topoi of `f`. That result is stated for the pullback built over the four-field
> morphism of ringed topoi of the modules development, whereas `ringedSitePullback` is built over
> the two-field morphism of Stacks 01D3; the two are left adjoints of one and the same direct
> image, by `AlgebraicGeometry.RingedToposHom.pullbackAdjPushforwardModulesViaComparison` and
> `AlgebraicGeometry.RingedToposHom.pullbackAdjPushforwardModules`, so they are identified by
> uniqueness of left adjoints and left exactness transfers along that isomorphism.

```lean
theorem preservesFiniteLimits_ringedSitePullback_of_isFlat
    (hf : AlgebraicGeometry.SheafOfModules.IsFlatMapULift
      f.ringedToposHom.fSharpInverseImage) :
    Limits.PreservesFiniteLimits (ringedSitePullback f)
```

**`CategoryTheory.Sites.abelianInverseImage_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/InverseImage/AbelianSheaf.lean, line 446](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InverseImage/AbelianSheaf.lean#L446). The attribute's comment: “inverse_image_exact”.

> The inverse image of a morphism of topoi is exact on ordinary abelian sheaves.

```lean
theorem abelianInverseImage_exact :
    exactFunctor (Sheaf K AddCommGrpCat.{w'}) (Sheaf J AddCommGrpCat.{w})
      (abelianInverseImage f)
```

**`Stacks.Sheaves.RingedToposModules.pullbackModules_exact_of_isFlatMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/RingedLocalization/FlatPullbackExact.lean, line 369](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/RingedLocalization/FlatPullbackExact.lean#L369). The attribute's comment: “flat_pullback_exact”.

> **Stacks 04JC**, second assertion. Pullback of sheaves of modules along a *flat* morphism
> of ringed topoi is exact: it preserves finite limits and finite colimits. The first assertion,
> exactness of the inverse image of abelian sheaves, is
> `CategoryTheory.Sites.abelianInverseImage_exact`.

```lean
theorem pullbackModules_exact_of_isFlatMap (f : AlgebraicGeometry.RingedToposHom X Y)
    (hf : AlgebraicGeometry.SheafOfModules.IsFlatMapULift.{w, u, v} f.fSharpInverseImage) :
    exactFunctor (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O))
      (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
      (f.toRingedToposModulesHom.pullbackModules)
```

## Tag 08M5, a definition

[Tag 08M5](https://stacks.math.columbia.edu/tag/08M5) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.IsFlat`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Flat.lean, line 285](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/Flat.lean#L285). The attribute's comment: “flatness over a morphism of ringed topoi: this predicate for the pullback ring”. References: SGA 4 V (1.1), “commutative case”.

> A sheaf of modules is flat when tensoring on the right with it is an exact
> endofunctor on sheaves of modules.
>
> This is part (3) of tag 03ER for the native tensor bifunctor, and part (4) just below
> is stated in terms of it. `Stacks.SheafOfModules.IsFlat` uses the same native tensor
> functor.

```lean
abbrev IsFlat {O : Sheaf J CommRingCat.{w}}
    [J.WEqualsLocallyBijective AddCommGrpCat.{z}]
    [HasWeakSheafify J AddCommGrpCat.{z}]
    (F : _root_.SheafOfModules.{z} (Stacks.SheafOfModules.Tensor.ringSheaf O)) : Prop
```

**`AlgebraicGeometry.RingedToposHom.IsFlatOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/RingedToposFlatModule.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/RingedToposFlatModule.lean#L62). The attribute's comment: “the definition: a sheaf of modules flat over the target ringed topos”.

> A sheaf `F` of `O`-modules on `X = (Sh(C), O)` is **flat over** the ringed topos
> `Y = (Sh(D), O')` along a morphism of ringed topoi `f : X ⟶ Y` when `F`, regarded as a sheaf of
> `f⁻¹O'`-modules by restriction of scalars along the inverse-image form `f⁻¹O' ⟶ O` of the
> structure map of `f`, is flat.

```lean
noncomputable abbrev IsFlatOver
    {X : RingedTopos.{v, u, w}} {Y : RingedTopos.{v', u', w'}}
    [X.J.HasSheafCompose (forget RingCat.{w})] [Y.J.HasSheafCompose (forget RingCat.{w'})]
    [X.J.HasSheafCompose (forget₂ CommRingCat.{w} RingCat.{w})]
    [Y.J.HasSheafCompose (forget₂ CommRingCat.{w'} RingCat.{w'})]
    [X.J.WEqualsLocallyBijective AddCommGrpCat.{w}] [HasWeakSheafify X.J AddCommGrpCat.{w}]
    (f : RingedToposHom X Y)
    (F : _root_.SheafOfModules.{w}
      (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) : Prop
```

## Tag 0GN2, a lemma

[Tag 0GN2](https://stacks.math.columbia.edu/tag/0GN2) in the Stacks Project.

**`Stacks.SheafOfModules.InternalHom.isIso_pullbackInternalHomMap_of_isFinitePresentationOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/PullbackInternalHomFinitePresentation.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/PullbackInternalHomFinitePresentation.lean#L81). The attribute's comment: “the isomorphism under the source's own hypotheses: `F` of finite presentation in the local sense of Tag 03DL and `f` flat; stated for a site and coefficients in one universe”.

> Flat pullback commutes with the canonical internal-Hom map for a module which is locally
> finitely presented. This statement uses a single universe for the site and coefficients.

```lean
theorem isIso_pullbackInternalHomMap_of_isFinitePresentationOnSite
    [F.IsFinitePresentationOnSite]
    (hf : AlgebraicGeometry.SheafOfModules.IsFlatMapULift
      f.ringedToposHom.fSharpInverseImage) : IsIso (pullbackInternalHomMap f F G)
```

**`Stacks.SheafOfModules.InternalHom.isIso_pullbackInternalHomMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/PullbackInternalHomFlat.lean, line 1189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/PullbackInternalHomFlat.lean#L1189). The attribute's comment: “the isomorphism, for a global rather than local (Tag 03DL) finite presentation of F”. References: EGA 0 (6.7.6), “special case”.

> **Stacks 0GN2, for a globally finitely presented `F`.** Let
> `f : (C, O_C) ⟶ (D, O_D)` be a flat morphism of ringed sites and let `F`, `G` be sheaves of
> `O_D`-modules with `F` presented, over the whole site `D`, as the cokernel of a morphism between
> finite coproducts of copies of `O_D`. Then the canonical map
>
> `f^* Hom_{O_D}(F, G) ⟶ Hom_{O_C}(f^*F, f^*G)`
>
> of Stacks 0GMX is an isomorphism.
>
> Flatness is the hypothesis `hf`, that `O_C` is flat as an `f⁻¹O_D`-module, which is the
> definition of a flat morphism of Tag 04JB. It enters through the left exactness of `f^*`
> (Tag 04JC, `preservesFiniteLimits_ringedSitePullback_of_isFlat`), because that is what makes
> `F ↦ f^* Hom_{O_D}(F, G)` carry the finite colimit presenting `F` to a limit of internal Hom
> sheaves; the other composite needs only that `f^*` is a left adjoint. The continuity of internal
> Hom in its first variable is Tag 03EN, `preservesFiniteColimits_internalHomFirstMate`, and the
> remaining two inputs the source's proof names are `pullbackInternalHomNatural`, the
> first-variable functoriality of the canonical map of Stacks 0GMX, and
> `isIso_toposPullbackInternalHomMap_structureSheaf`, its invertibility at the structure sheaf.
>
> The presentation of `F` is a global one, not the local finite presentation of Tag 03DL that the
> source assumes: `ι`, `κ`, `hP`, `hQ`, `a`, `b`, `hab` and `hF` exhibit `F` as a cokernel of a
> morphism between finite coproducts of copies of the structure sheaf over the whole site `D`.
> That is strictly stronger than finite presentation, so the statement here is the global special
> case of Stacks 0GN2; the local case is reduced to it by
> `PullbackInternalHomFinitePresentation.isIso_pullbackInternalHomMap_of_isFinitePresentationOnSite`,
> which states the source's own hypotheses.

```lean
theorem isIso_pullbackInternalHomMap
    (F : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O))
    (hf : AlgebraicGeometry.SheafOfModules.IsFlatMapULift
      f.ringedToposHom.fSharpInverseImage)
    {n m : ℕ} {P Q : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)}
    (ι : Fin n → (SheafOfModules.unit (Stacks.SheafOfModules.Tensor.ringSheaf Y.O) ⟶ P))
    (κ : Fin m → (SheafOfModules.unit (Stacks.SheafOfModules.Tensor.ringSheaf Y.O) ⟶ Q))
    (hP : Limits.IsColimit (Limits.Cofan.mk P ι))
    (hQ : Limits.IsColimit (Limits.Cofan.mk Q κ))
    (a : Q ⟶ P) (b : P ⟶ F) (hab : a ≫ b = 0)
    (hF : Limits.IsColimit (Limits.CokernelCofork.ofπ b hab)) :
    IsIso (pullbackInternalHomMap f F G)
```

**`Stacks.SheafOfModules.InternalHom.isIso_pullbackInternalHomMap_structureSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/PullbackInternalHomFlat.lean, line 1242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/PullbackInternalHomFlat.lean#L1242). The attribute's comment: “the isomorphism for F the structure sheaf”. References: EGA 0 (6.7.6), “partial, special case”.

> **Stacks 0GN2 for `F` the structure sheaf.** Let `f : (C, O_C) ⟶ (D, O_D)` be a morphism of
> ringed sites and `G` a sheaf of `O_D`-modules. The canonical map
>
> `f^* Hom_{O_D}(O_D, G) ⟶ Hom_{O_C}(f^*O_D, f^*G)`
>
> of Stacks 0GMX is an isomorphism.
>
> The structure sheaf is finitely presented, and at it both sides of the canonical map are
> identified with `f^*G`: the inputs are the identification `f^*O_D = O_C` of Stacks 03D6 and the
> identity `Hom_O(O, -) = id` of Stacks 03EM. Flatness of `f` is not used — the source needs it
> only to carry a presentation of a general `F` across the pullback.

```lean
theorem isIso_pullbackInternalHomMap_structureSheaf :
    IsIso (pullbackInternalHomMap f
      (SheafOfModules.unit ((Stacks.SheafOfModules.Tensor.ringSheaf (J := Y.J)) Y.O)) G)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.31, Tag 04JA](https://stacks.math.columbia.edu/tag/04JA)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
