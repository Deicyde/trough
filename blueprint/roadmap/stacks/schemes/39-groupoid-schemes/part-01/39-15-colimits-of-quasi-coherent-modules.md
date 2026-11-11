---
declaration: section
origin: cited
lean: Stacks.Groupoids.GroupoidScheme.isQuasicoherent_pushforwardSource_pullbackTarget, Stacks.Groupoids.GroupoidScheme.coinductionAlpha, Stacks.Groupoids.GroupoidScheme.coinductionAlpha_naturality, Stacks.Groupoids.GroupoidScheme.coinductionAdjunction, Stacks.Groupoids.GroupoidScheme.cocycle_coinductionAlpha, Stacks.Groupoids.GroupoidScheme.identity_coinductionAlpha, Stacks.Groupoids.GroupoidScheme.coinductionAdjunction_unit_app, AlgebraicGeometry.isCoherent_pullback_pushforward
statement: formalized
proof: formalized
---

# 39.15 Colimits of quasi-coherent modules

Section 39.15 of the Stacks Project, [Tag 07TS](https://stacks.math.columbia.edu/tag/07TS). 7 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07TR, a lemma

[Tag 07TR](https://stacks.math.columbia.edu/tag/07TR) in the Stacks Project.

**`Stacks.Groupoids.GroupoidScheme.isQuasicoherent_pushforwardSource_pullbackTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Coinduction.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Coinduction.lean#L178). The attribute's comment: “the quasi-coherence of `s_* t^* 𝒢`”.

> **The first assertion of Tag 07TR.**  For a groupoid scheme whose source map is
> quasi-compact and quasi-separated, the module `s_* t^* 𝒢` is quasi-coherent.

```lean
theorem isQuasicoherent_pushforwardSource_pullbackTarget
    [QuasiCompact G.source.left] [QuasiSeparated G.source.left]
    (𝒢 : G.objects.left.Modules) [𝒢.IsQuasicoherent] :
    ((Scheme.Modules.pushforward G.source.left).obj
      ((Scheme.Modules.pullback G.target.left).obj 𝒢)).IsQuasicoherent
```

**`Stacks.Groupoids.GroupoidScheme.coinductionAlpha`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Coinduction.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Coinduction.lean#L217). The attribute's comment: “the construction of the canonical isomorphism `α`; not the cocycle and identity conditions making `(s_* t^* 𝒢, α)` a module on the groupoid, and not the functor to `QCoh(U, R, s, t, c)` nor its right adjointness to the forgetful functor”.

> **The canonical isomorphism `α` of Tag 07TR.**  For a groupoid scheme `(U, R, s, t, c)` with
> `s` and `t` flat, quasi-compact and quasi-separated and a quasi-coherent module `𝒢` on `U`, this
> is the canonical isomorphism `t^* s_* t^* 𝒢 ≅ s^* s_* t^* 𝒢`.  It is the composite of the two
> flat base-change isomorphisms of the squares of the composition diagram with the identification
> of `pr_0^* t^* 𝒢` and `c^* t^* 𝒢`.
>
> This does not include the cocycle condition and the normalization along the identity section,
> which are what make `(s_* t^* 𝒢, α)` a quasi-coherent module on the groupoid scheme.

```lean
noncomputable def coinductionAlpha [Flat G.source.left] [Flat G.target.left]
    [QuasiCompact G.source.left] [QuasiSeparated G.source.left]
    (𝒢 : G.objects.left.Modules) [𝒢.IsQuasicoherent] :
    (Scheme.Modules.pullback G.target.left).obj
        ((Scheme.Modules.pushforward G.source.left).obj
          ((Scheme.Modules.pullback G.target.left).obj 𝒢)) ≅
      (Scheme.Modules.pullback G.source.left).obj
        ((Scheme.Modules.pushforward G.source.left).obj
          ((Scheme.Modules.pullback G.target.left).obj 𝒢))
```

**`Stacks.Groupoids.GroupoidScheme.coinductionAlpha_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Coinduction.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Coinduction.lean#L235). The attribute's comment: “the naturality of `α` in `𝒢`”.

> The canonical isomorphism `α` is natural in `𝒢`, which is the sense in which the
> construction `𝒢 ↦ (s_* t^* 𝒢, α)` is canonical.

```lean
theorem coinductionAlpha_naturality [Flat G.source.left] [Flat G.target.left]
    [QuasiCompact G.source.left] [QuasiSeparated G.source.left]
    {𝒢 𝒢' : G.objects.left.Modules} [𝒢.IsQuasicoherent] [𝒢'.IsQuasicoherent]
    (φ : 𝒢 ⟶ 𝒢') :
    (coinductionAlpha G 𝒢).hom ≫
        (Scheme.Modules.pullback G.source.left).map
          ((Scheme.Modules.pushforward G.source.left).map
            ((Scheme.Modules.pullback G.target.left).map φ)) =
      (Scheme.Modules.pullback G.target.left).map
          ((Scheme.Modules.pushforward G.source.left).map
            ((Scheme.Modules.pullback G.target.left).map φ)) ≫
        (coinductionAlpha G 𝒢').hom
```

**`Stacks.Groupoids.GroupoidScheme.coinductionAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/CoinductionAdjunction/Adjunction.lean, line 784](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/CoinductionAdjunction/Adjunction.lean#L784). The attribute's comment: “the right adjointness of the coinduction functor to the forgetful functor”.

> **Coinduction is right adjoint to forgetting a groupoid descent datum.**  This is the
> adjunction of Tag 07TR.

```lean
noncomputable def coinductionAdjunction : quasicoherentForget G ⊣ coinduction G
```

**`Stacks.Groupoids.GroupoidScheme.cocycle_coinductionAlpha`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/CoinductionAdjunction/CocycleCondition.lean, line 327](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/CoinductionAdjunction/CocycleCondition.lean#L327). The attribute's comment: “the cocycle condition for `α`, the first of the two conditions making `(s_* t^* 𝒢, α)` a quasi-coherent module on the groupoid scheme”.

> **The cocycle condition for the coinduction descent isomorphism.**  On the scheme of
> composable arrows, applying `α` to the two arrows in succession agrees with applying it to their
> composite.

```lean
theorem cocycle_coinductionAlpha
    [Flat G.source.left] [Flat G.target.left]
    [QuasiCompact G.source.left] [QuasiSeparated G.source.left]
    (𝒢 : G.objects.left.Modules) [𝒢.IsQuasicoherent] :
    successiveDescent G (coinductionAlpha G 𝒢).hom =
      reindexHom G.comp.left (coinductionAlpha G 𝒢).hom
```

**`Stacks.Groupoids.GroupoidScheme.identity_coinductionAlpha`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/CoinductionAdjunction/CocycleCondition.lean, line 412](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/CoinductionAdjunction/CocycleCondition.lean#L412). The attribute's comment: “the normalization of `α` along the identity section, the second of the two conditions making `(s_* t^* 𝒢, α)` a quasi-coherent module on the groupoid scheme”.

> **The normalization of the coinduction descent isomorphism along the identity section.**
> Pulling `α` back along the identity section gives the identity of `s_* t^* 𝒢`.  With
> `cocycle_coinductionAlpha` this exhibits `(s_* t^* 𝒢, α)` as a quasi-coherent module on the
> groupoid scheme.

```lean
theorem identity_coinductionAlpha
    [Flat G.source.left] [Flat G.target.left]
    [QuasiCompact G.source.left] [QuasiSeparated G.source.left]
    (𝒢 : G.objects.left.Modules) [𝒢.IsQuasicoherent] :
    identityDescent G (coinductionAlpha G 𝒢).hom =
      𝟙 ((Scheme.Modules.pushforward G.source.left).obj
        ((Scheme.Modules.pullback G.target.left).obj 𝒢))
```

## Tag 0GNF, a remark

[Tag 0GNF](https://stacks.math.columbia.edu/tag/0GNF) in the Stacks Project.

**`Stacks.Groupoids.GroupoidScheme.coinductionAdjunction_unit_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/CoinductionAdjunction/Adjunction.lean, line 803](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/CoinductionAdjunction/Adjunction.lean#L803).

> **Stacks 0GNF.**  The unit of the forgetful--coinduction adjunction at a quasi-coherent
> module `(𝓕, α)` on a groupoid scheme is, on underlying modules, the unit of the
> pullback--pushforward adjunction along the source followed by the direct image of the inverse
> of the descent morphism:
> `𝓕 ⟶ s_* s^* 𝓕 ⟶ s_* t^* 𝓕`.

```lean
theorem coinductionAdjunction_unit_app (M : QuasicoherentModule G) :
    ((coinductionAdjunction G).unit.app M).hom =
      (Scheme.Modules.pullbackPushforwardAdjunction G.source.left).unit.app M.module ≫
        (Scheme.Modules.pushforward G.source.left).map (inv M.alpha)
```

## Tag 07TT, a lemma

[Tag 07TT](https://stacks.math.columbia.edu/tag/07TT) in the Stacks Project.

**`AlgebraicGeometry.isCoherent_pullback_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Modules/CoherentPullbackPushforward.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Modules/CoherentPullbackPushforward.lean#L69).

> **Stacks Project, Tag 07TT.** For a flat, surjective, quasi-compact and quasi-separated
> morphism `f : Y ⟶ X` of locally Noetherian schemes, a quasi-coherent module `F` on `X` and a
> coherent submodule `G` of `f^*F`, the fibre product of the unit `F ⟶ f_* f^* F` with the
> pushforward of the inclusion is coherent.

```lean
theorem isCoherent_pullback_pushforward {X Y : Scheme.{u}} (f : Y ⟶ X)
    [QuasiCompact f] [QuasiSeparated f] [Flat f] [Surjective f]
    [IsLocallyNoetherian X] [IsLocallyNoetherian Y]
    (F : X.Modules) [F.IsQuasicoherent]
    (G : Y.Modules) [G.IsQuasicoherent] [G.IsCoherent]
    (φ : G ⟶ (Scheme.Modules.pullback f).obj F) [Mono φ] :
    (pullback ((Scheme.Modules.pullbackPushforwardAdjunction f).unit.app F)
      ((Scheme.Modules.pushforward f).map φ)).IsCoherent
```

## Tag 07TU, a lemma

[Tag 07TU](https://stacks.math.columbia.edu/tag/07TU) in the Stacks Project.

**`AlgebraicGeometry.GroupoidScheme.exists_filtered_diagram_of_isCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/CoherentColimit.lean, line 826](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/CoherentColimit.lean#L826). The attribute's comment: “every quasi-coherent module on the groupoid scheme is the colimit of a filtered diagram of quasi-coherent modules on the groupoid scheme with coherent underlying modules”.

> **Stacks Project, Tag 07TU.**  Let `(U, R, s, t, c)` be a groupoid scheme over `S` with `U`
> and `R` Noetherian and with `s` and `t` flat, quasi-compact and quasi-separated.  Then every
> quasi-coherent module `(ℱ, β)` on the groupoid scheme is the colimit of a filtered diagram of
> quasi-coherent modules on the groupoid scheme whose underlying modules on `U` are coherent.

```lean
theorem exists_filtered_diagram_of_isCoherent
    [IsNoetherian G.objects.left] [IsNoetherian G.arrows.left]
    [Flat G.source.left] [Flat G.target.left]
    [QuasiCompact G.source.left] [QuasiCompact G.target.left]
    [QuasiSeparated G.source.left] [QuasiSeparated G.target.left]
    (M : QuasicoherentModule G) :
    ∃ (I : Type (u + 1)) (inst : SmallCategory I),
      let _ := inst
      ∃ (_ : IsFiltered I) (D : I ⥤ QuasicoherentModule G)
        (φ : D ⟶ (Functor.const I).obj M),
        (∀ i, (D.obj i).module.IsCoherent) ∧
          Nonempty (IsColimit (Cocone.mk M φ))
```

## Tag 07TV, a lemma

[Tag 07TV](https://stacks.math.columbia.edu/tag/07TV) in the Stacks Project.

**`AlgebraicGeometry.GroupoidScheme.exists_filtered_diagram_of_isFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/FiniteTypeStructure/GroupoidColimit.lean, line 1312](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/FiniteTypeStructure/GroupoidColimit.lean#L1312).

> **Stacks Project, Tag 07TV.** A quasi-coherent module on an affine groupoid scheme whose
> arrow ring is free over its object ring via the source map is a filtered colimit of
> finite-type groupoid modules.

```lean
theorem exists_filtered_diagram_of_isFiniteType
    {S : Scheme.{u}} (G : GroupoidScheme S)
    [IsAffine G.objects.left] [IsAffine G.arrows.left]
    (hfree : letI : Algebra Γ(G.objects.left, ⊤) Γ(G.arrows.left, ⊤) :=
      G.source.left.appTop.hom.toAlgebra
      Module.Free Γ(G.objects.left, ⊤) Γ(G.arrows.left, ⊤))
    (M : QuasicoherentModule G) :
    ∃ (I : Type u) (inst : SmallCategory I),
      let _ := inst
      ∃ (_ : IsFiltered I)
        (D : I ⥤ QuasicoherentModule G)
        (φ : D ⟶ (Functor.const I).obj M),
        (∀ i, (D.obj i).module.IsFiniteType) ∧
          Nonempty (IsColimit (Cocone.mk M φ))
```

## Tag 077T, a lemma

[Tag 077T](https://stacks.math.columbia.edu/tag/077T) in the Stacks Project.

**`AlgebraicGeometry.essentiallySmall_isCardinalGenerated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidCardinalGenerated.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidCardinalGenerated.lean#L87).

> The `κ`-generated quasi-coherent modules on a groupoid scheme have only a set of
> isomorphism classes.

```lean
theorem essentiallySmall_isCardinalGenerated {S : Scheme.{u}}
    (G : Stacks.Groupoids.GroupoidScheme S) (κ : Cardinal.{u}) :
    ObjectProperty.EssentiallySmall.{u}
      (fun M : QuasicoherentModule G ↦
        Stacks.AlgebraicGeometry.CardinalGeneration.IsCardinalGenerated M.module κ)
```

## Tag 077U, a lemma

[Tag 077U](https://stacks.math.columbia.edu/tag/077U) in the Stacks Project.

**`Stacks.AlgebraicGeometry.GroupoidCardinalGeneration.cardinalBound`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidQuasicoherentColimit.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidQuasicoherentColimit.lean#L101). The attribute's comment: “cardinal”.

> **The cardinal of Stacks 077U.**  For a groupoid scheme it is the maximum of the cardinals
> Gabber's theorem attaches to the object scheme and to the arrow scheme; the closure construction
> producing the bounded submodules uses exactly that it is infinite and dominates the numbers of
> affine opens of the two schemes.

```lean
def cardinalBound {S : Scheme.{u}} (G : GroupoidScheme S) : Cardinal.{u}
```

**`Stacks.AlgebraicGeometry.GroupoidCardinalGeneration.cardinalGeneratedSubobject_isFiltered`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidQuasicoherentColimit.lean, line 294](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidQuasicoherentColimit.lean#L294). The attribute's comment: “directedness”.

> **Stacks 077U, the directedness assertion**, at the cardinal the tag attaches to the groupoid
> scheme.

```lean
instance cardinalGeneratedSubobject_isFiltered (M : QuasicoherentModule G) :
    IsFiltered (CardinalGeneratedSubobject M (cardinalBound G))
```

**`Stacks.AlgebraicGeometry.GroupoidCardinalGeneration.isColimit_cardinalGeneratedSubobjectCocone`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidQuasicoherentColimit.lean, line 384](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidQuasicoherentColimit.lean#L384). The attribute's comment: “colimit”.

> **Stacks 077U, the colimit assertion.**  Every quasi-coherent module on a groupoid scheme with
> flat source and target is the colimit of the canonical diagram of its quasi-coherent submodules
> whose underlying module is generated by at most `cardinalBound G` local sections.

```lean
def isColimit_cardinalGeneratedSubobjectCocone (M : QuasicoherentModule G) :
    IsColimit (cardinalGeneratedSubobjectCocone M (cardinalBound G))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 39.15, Tag 07TS](https://stacks.math.columbia.edu/tag/07TS)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
