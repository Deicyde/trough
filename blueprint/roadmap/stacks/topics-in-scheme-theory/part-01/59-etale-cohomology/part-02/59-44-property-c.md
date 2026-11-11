---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.smallEtalePushforward_reflectsMonomorphisms_of_hasPropertyC, Stacks.EtaleCohomology.smallEtalePushforward_reflectsEpimorphisms_of_hasPropertyC, Stacks.EtaleCohomology.smallEtaleBaseChange_isAlmostCocontinuous, Stacks.EtaleCohomology.hasPropertyC_of_isIntegralHom_of_isClosedEmbedding, Stacks.EtaleCohomology.smallEtaleBaseChange_isAlmostCocontinuous_of_isIntegralHom_of_universallyInjective, Stacks.EtaleCohomology.smallEtalePushforward_reflectsMonomorphisms_of_isIntegralHom_of_universallyInjective, Stacks.EtaleCohomology.smallEtalePushforward_reflectsEpimorphisms_of_isIntegralHom_of_universallyInjective, Stacks.EtaleCohomology.smallEtalePushforward_preservesConnectedColimits_of_isIntegralHom_of_universallyInjective
statement: formalized
proof: formalized
---

# 59.44 Property (C)

Section 59.44 of the Stacks Project, [Tag 04DS](https://stacks.math.columbia.edu/tag/04DS). 4 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04DT, a lemma

[Tag 04DT](https://stacks.math.columbia.edu/tag/04DT) in the Stacks Project.

**`Stacks.EtaleCohomology.smallEtalePushforward_reflectsMonomorphisms_of_hasPropertyC`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Descent/PropertyCPushforward.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Descent/PropertyCPushforward.lean#L87). The attribute's comment: “reflects injections”.

> **Stacks Project, Tag 04DT.** If `f : X ⟶ Y` has property (C), then direct image
> `f_{small, *} : Sh(X_étale) ⥤ Sh(Y_étale)` on sheaves of sets reflects injections.

```lean
theorem smallEtalePushforward_reflectsMonomorphisms_of_hasPropertyC
    {X Y : Scheme.{u}} (f : X ⟶ Y) (hC : HasPropertyC f) :
    ((smallEtaleBaseChange f).sheafPushforwardContinuous (Type v)
      (smallEtaleTopology Y) (smallEtaleTopology X)).ReflectsMonomorphisms
```

**`Stacks.EtaleCohomology.smallEtalePushforward_reflectsEpimorphisms_of_hasPropertyC`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Descent/PropertyCPushforward.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Descent/PropertyCPushforward.lean#L97). The attribute's comment: “reflects surjections”.

> **Stacks Project, Tag 04DT.** If `f : X ⟶ Y` has property (C), then direct image
> `f_{small, *} : Sh(X_étale) ⥤ Sh(Y_étale)` on sheaves of sets reflects surjections.

```lean
theorem smallEtalePushforward_reflectsEpimorphisms_of_hasPropertyC
    {X Y : Scheme.{u}} (f : X ⟶ Y) (hC : HasPropertyC f) :
    ((smallEtaleBaseChange f).sheafPushforwardContinuous (Type v)
      (smallEtaleTopology Y) (smallEtaleTopology X)).ReflectsEpimorphisms
```

## Tag 04DV, a lemma

[Tag 04DV](https://stacks.math.columbia.edu/tag/04DV) in the Stacks Project.

**`Stacks.EtaleCohomology.smallEtaleBaseChange_isAlmostCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Descent/PropertyCAlmostCocontinuous.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Descent/PropertyCAlmostCocontinuous.lean#L82).

> **Stacks Project, Tag 04DV.** If every étale base change `X ×_Y V ⟶ V` of `f : X ⟶ Y` has
> property (C) and is a closed map, then base change `Y.Etale ⥤ X.Etale`, `V ↦ X ×_Y V`, is an
> almost cocontinuous functor of small étale sites.

```lean
theorem smallEtaleBaseChange_isAlmostCocontinuous
    {X Y : Scheme.{u}} (f : X ⟶ Y)
    (hC : ∀ {V : Scheme.{u}} (v : V ⟶ Y), Etale v →
      HasPropertyC (pullback.snd f v))
    (hclosed : ∀ {V : Scheme.{u}} (v : V ⟶ Y), Etale v →
      IsClosedMap (pullback.snd f v).base) :
    IsAlmostCocontinuous (smallEtaleBaseChange f)
      (smallEtaleTopology Y) (smallEtaleTopology X)
```

## Tag 04DW, a lemma

[Tag 04DW](https://stacks.math.columbia.edu/tag/04DW) in the Stacks Project.

**`Stacks.EtaleCohomology.hasPropertyC_of_isIntegralHom_of_isClosedEmbedding`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Descent/PropertyC.lean, line 341](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Descent/PropertyC.lean#L341).

> **Stacks Project, Tag 04DW.** An integral morphism of schemes which is a homeomorphism onto a
> closed subset of its target has property (C): every scheme étale over the source is dominated, by
> a surjection over the source, by the base change of a scheme étale over the target.
>
> The étale scheme over the target is the coproduct of the one-point constructions of
> `Stacks.EtaleCohomology.exists_etale_dominating_at_point`, indexed by the points of the given
> étale scheme; its base change is the coproduct of their base changes by
> `Stacks.EtaleCohomology.isPullback_pullbackFactorMap`, so the one-point morphisms assemble into a
> single morphism, and it is surjective because every point was hit.

```lean
theorem hasPropertyC_of_isIntegralHom_of_isClosedEmbedding
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsIntegralHom f] (hf : Topology.IsClosedEmbedding f) :
    HasPropertyC f
```

## Tag 04DX, a lemma

[Tag 04DX](https://stacks.math.columbia.edu/tag/04DX) in the Stacks Project.

**`Stacks.EtaleCohomology.smallEtaleBaseChange_isAlmostCocontinuous_of_isIntegralHom_of_universallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Descent/IntegralUniversallyInjective.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Descent/IntegralUniversallyInjective.lean#L165). The attribute's comment: “(7) almost cocontinuous”.

> **Stacks Project, Tag 04DX, part (7).** For an integral universally injective morphism of
> schemes `f : X ⟶ Y`, base change `Y.Etale ⥤ X.Etale`, `V ↦ X ×_Y V`, is almost cocontinuous as a
> functor of small étale sites.
>
> Every étale base change of `f` has property (C) and is a closed map, which is the hypothesis of
> [Stacks, Tag 04DV].

```lean
public theorem
    smallEtaleBaseChange_isAlmostCocontinuous_of_isIntegralHom_of_universallyInjective
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsIntegralHom f] [UniversallyInjective f] :
    IsAlmostCocontinuous (smallEtaleBaseChange f) (smallEtaleTopology Y) (smallEtaleTopology X)
```

**`Stacks.EtaleCohomology.smallEtalePushforward_reflectsMonomorphisms_of_isIntegralHom_of_universallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Descent/IntegralUniversallyInjective.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Descent/IntegralUniversallyInjective.lean#L181). The attribute's comment: “(1) reflects injections”.

> **Stacks Project, Tag 04DX, part (1).** For an integral universally injective morphism of
> schemes `f : X ⟶ Y`, direct image `f_{small, *} : Sh(X_étale) ⥤ Sh(Y_étale)` on sheaves of sets
> reflects injections.
>
> This is property (C) fed to [Stacks, Tag 04DT].

```lean
public theorem
    smallEtalePushforward_reflectsMonomorphisms_of_isIntegralHom_of_universallyInjective
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsIntegralHom f] [UniversallyInjective f] :
    ((smallEtaleBaseChange f).sheafPushforwardContinuous (Type v) (smallEtaleTopology Y)
      (smallEtaleTopology X)).ReflectsMonomorphisms
```

**`Stacks.EtaleCohomology.smallEtalePushforward_reflectsEpimorphisms_of_isIntegralHom_of_universallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Descent/IntegralUniversallyInjective.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Descent/IntegralUniversallyInjective.lean#L195). The attribute's comment: “(1) reflects surjections”.

> **Stacks Project, Tag 04DX, part (1).** For an integral universally injective morphism of
> schemes `f : X ⟶ Y`, direct image `f_{small, *} : Sh(X_étale) ⥤ Sh(Y_étale)` on sheaves of sets
> reflects surjections.
>
> This is property (C) fed to [Stacks, Tag 04DT].

```lean
public theorem
    smallEtalePushforward_reflectsEpimorphisms_of_isIntegralHom_of_universallyInjective
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsIntegralHom f] [UniversallyInjective f] :
    ((smallEtaleBaseChange f).sheafPushforwardContinuous (Type v) (smallEtaleTopology Y)
      (smallEtaleTopology X)).ReflectsEpimorphisms
```

**`Stacks.EtaleCohomology.smallEtalePushforward_preservesConnectedColimits_of_isIntegralHom_of_universallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Descent/IntegralUniversallyInjective.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Descent/IntegralUniversallyInjective.lean#L212). The attribute's comment: “(2) finite connected colimits”.

> **Stacks Project, Tag 04DX, part (2).** For an integral universally injective morphism of
> schemes `f : X ⟶ Y`, direct image `f_{small, *} : Sh(X_étale) ⥤ Sh(Y_étale)` on sheaves of sets
> preserves colimits of every connected shape whose colimits exist. In particular it commutes with
> pushouts and coequalizers, and more generally with finite connected colimits.
>
> This is almost cocontinuity of the base-change functor fed to [Stacks, Tag 04BA].

```lean
public theorem
    smallEtalePushforward_preservesConnectedColimits_of_isIntegralHom_of_universallyInjective
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsIntegralHom f] [UniversallyInjective f]
    (I : Type) [SmallCategory I] [IsConnected I]
    [HasColimitsOfShape I (Type (max (u + 1) v))] :
    PreservesColimitsOfShape I
      ((smallEtaleBaseChange f).sheafPushforwardContinuous (Type (max (u + 1) v))
        (smallEtaleTopology Y) (smallEtaleTopology X))
```

**`Stacks.EtaleCohomology.smallEtalePushforward_preservesEpimorphisms_of_isIntegralHom_of_universallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Descent/IntegralUniversallyInjective.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Descent/IntegralUniversallyInjective.lean#L236). The attribute's comment: “(3) preserves surjections”.

> **Stacks Project, Tag 04DX, part (3).** For an integral universally injective morphism of
> schemes `f : X ⟶ Y`, direct image `f_{small, *} : Sh(X_étale) ⥤ Sh(Y_étale)` carries surjections
> of sheaves of sets to surjections.
>
> Universal injectivity is not needed here: integrality alone gives property (B), which is the
> hypothesis of [Stacks, Tag 04DO].

```lean
public theorem
    smallEtalePushforward_preservesEpimorphisms_of_isIntegralHom_of_universallyInjective
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsIntegralHom f] [UniversallyInjective f] :
    ((smallEtaleBaseChange f).sheafPushforwardContinuous (Type v) (smallEtaleTopology Y)
      (smallEtaleTopology X)).PreservesEpimorphisms
```

**`Stacks.EtaleCohomology.smallEtalePushforwardAb_preservesEpimorphisms_of_isIntegralHom_of_universallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Descent/IntegralUniversallyInjective.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Descent/IntegralUniversallyInjective.lean#L252). The attribute's comment: “(3) preserves surjections”.

> **Stacks Project, Tag 04DX, part (3).** For an integral universally injective morphism of
> schemes `f : X ⟶ Y`, direct image `f_{small, *} : Ab(X_étale) ⥤ Ab(Y_étale)` carries surjections
> of abelian sheaves to surjections.
>
> A morphism of abelian sheaves is epimorphic exactly when it is locally surjective, and local
> surjectivity is a property of the underlying morphism of sheaves of sets. Since the underlying
> sheaf of sets of a direct image is the direct image of the underlying sheaf of sets, the statement
> reduces to its set-valued counterpart.

```lean
public theorem
    smallEtalePushforwardAb_preservesEpimorphisms_of_isIntegralHom_of_universallyInjective
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsIntegralHom f] [UniversallyInjective f] :
    (smallEtalePushforwardAb f).PreservesEpimorphisms
```

**`Stacks.EtaleCohomology.smallEtaleAdjunction_counit_epi_of_isIntegralHom_of_universallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Descent/IntegralUniversallyInjective.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Descent/IntegralUniversallyInjective.lean#L276). The attribute's comment: “(4) surjective counit”.

> **Stacks Project, Tag 04DX, part (4).** For an integral universally injective morphism of
> schemes `f : X ⟶ Y`, the counit `f^{-1} f_* F ⟶ F` of the inverse-image/direct-image adjunction is
> surjective for every sheaf of sets `F` on the small étale site of `X`.
>
> A right adjoint which reflects surjections has surjective counit, by [Stacks, Tag 04D6]; direct
> image reflects surjections by part (1).

```lean
public theorem smallEtaleAdjunction_counit_epi_of_isIntegralHom_of_universallyInjective
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsIntegralHom f] [UniversallyInjective f]
    (F : Sheaf (smallEtaleTopology X) (Type (max (u + 1) v))) :
    Epi ((Functor.sheafAdjunctionContinuous (smallEtaleBaseChange f) (Type (max (u + 1) v))
      (smallEtaleTopology Y) (smallEtaleTopology X)).counit.app F)
```

**`Stacks.EtaleCohomology.smallEtaleAdjunctionAb_counit_epi_of_isIntegralHom_of_universallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Descent/IntegralUniversallyInjective.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Descent/IntegralUniversallyInjective.lean#L293). The attribute's comment: “(4) surjective counit”.

> **Stacks Project, Tag 04DX, part (4).** For an integral universally injective morphism of
> schemes `f : X ⟶ Y`, the counit `f^{-1} f_* F ⟶ F` of the inverse-image/direct-image adjunction is
> surjective for every abelian sheaf `F` on the small étale site of `X`.
>
> Integrality alone gives property (A), from which this is one of the conclusions of
> [Stacks, Tag 04DK].

```lean
public theorem smallEtaleAdjunctionAb_counit_epi_of_isIntegralHom_of_universallyInjective
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsIntegralHom f] [UniversallyInjective f]
    (F : Sheaf (smallEtaleTopology X) Ab.{u + 1}) :
    Epi ((smallEtaleAdjunctionAb f).counit.app F)
```

**`Stacks.EtaleCohomology.smallEtalePushforward_faithful_of_isIntegralHom_of_universallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Descent/IntegralUniversallyInjective.lean, line 307](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Descent/IntegralUniversallyInjective.lean#L307). The attribute's comment: “(5) faithful”.

> **Stacks Project, Tag 04DX, part (5).** For an integral universally injective morphism of
> schemes `f : X ⟶ Y`, direct image `f_{small, *} : Sh(X_étale) ⥤ Sh(Y_étale)` on sheaves of sets is
> faithful.
>
> A right adjoint with surjective counit is faithful, by [Stacks, Tag 04D6]; the counit is surjective
> by part (4).

```lean
public theorem smallEtalePushforward_faithful_of_isIntegralHom_of_universallyInjective
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsIntegralHom f] [UniversallyInjective f] :
    ((smallEtaleBaseChange f).sheafPushforwardContinuous (Type (max (u + 1) v))
      (smallEtaleTopology Y) (smallEtaleTopology X)).Faithful
```

**`Stacks.EtaleCohomology.smallEtalePushforwardAb_faithful_of_isIntegralHom_of_universallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Descent/IntegralUniversallyInjective.lean, line 323](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Descent/IntegralUniversallyInjective.lean#L323). The attribute's comment: “(5) faithful”.

> **Stacks Project, Tag 04DX, part (5).** For an integral universally injective morphism of
> schemes `f : X ⟶ Y`, direct image `f_{small, *} : Ab(X_étale) ⥤ Ab(Y_étale)` on abelian sheaves is
> faithful.
>
> Integrality alone gives property (A), from which this is one of the conclusions of
> [Stacks, Tag 04DK].

```lean
public theorem smallEtalePushforwardAb_faithful_of_isIntegralHom_of_universallyInjective
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsIntegralHom f] [UniversallyInjective f] :
    (smallEtalePushforwardAb f).Faithful
```

**`Stacks.EtaleCohomology.smallEtalePushforwardAb_exact_of_isIntegralHom_of_universallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Descent/IntegralUniversallyInjective.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Descent/IntegralUniversallyInjective.lean#L337). The attribute's comment: “(6) exact on abelian sheaves”.

> **Stacks Project, Tag 04DX, part (6).** For an integral universally injective morphism of
> schemes `f : X ⟶ Y`, direct image `f_{small, *} : Ab(X_étale) ⥤ Ab(Y_étale)` is an exact functor.
>
> Direct image is a right adjoint, so it preserves finite limits and is therefore additive; it
> preserves epimorphisms by part (3); and an additive functor between abelian categories which
> preserves finite limits and epimorphisms preserves finite colimits as well.

```lean
public theorem smallEtalePushforwardAb_exact_of_isIntegralHom_of_universallyInjective
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsIntegralHom f] [UniversallyInjective f] :
    exactFunctor (Sheaf (smallEtaleTopology X) Ab.{u + 1})
      (Sheaf (smallEtaleTopology Y) Ab.{u + 1}) (smallEtalePushforwardAb f)
```

**`AlgebraicGeometry.Space.smallBaseChange_isAlmostCocontinuous_of_isIntegralHom_of_universallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ChartBaseChangeAlmostCocontinuous.lean, line 482](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ChartBaseChangeAlmostCocontinuous.lean#L482). The attribute's comment: “part (7) for algebraic spaces: chart base change is almost cocontinuous”.

> **The space-level analogue of [Stacks, Tag 04DX], part (7).** Let `f : Z ⟶ X` be a
> representable morphism of algebraic spaces over `S` such that every base-change projection of
> schemes `U ×_X Z ⟶ U` at an étale chart `U` of `X` is integral and universally injective — for
> instance a closed immersion. Then base change of étale scheme charts along `f`,
>
> `X_étale ⥤ Z_étale`, `U ↦ U ×_X Z`,
>
> is almost cocontinuous for the small étale topologies.
>
> Integrality makes each chart base change universally closed, hence a closed map, and together
> with universal injectivity a homeomorphism onto a closed subset of the chart, which is the
> hypothesis of [Stacks, Tag 04DW] and so gives property (C). Those are the two inputs of the
> space-level [Stacks, Tag 04DV].

```lean
theorem smallBaseChange_isAlmostCocontinuous_of_isIntegralHom_of_universallyInjective
    (f : Z ⟶ X) (hf : yoneda.relativelyRepresentable f.hom)
    (hint : ∀ U : SmallEtale B S hS X.1, AlgebraicGeometry.IsIntegralHom
      ((BigFppfOver.toScheme B S hS).map (hf.snd U.1.hom)))
    (huniv : ∀ U : SmallEtale B S hS X.1, AlgebraicGeometry.UniversallyInjective
      ((BigFppfOver.toScheme B S hS).map (hf.snd U.1.hom))) :
    IsAlmostCocontinuous (smallBaseChange B S hS f hf)
      (SmallEtale.topology B S hS X.1) (SmallEtale.topology B S hS Z.1)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.44, Tag 04DS](https://stacks.math.columbia.edu/tag/04DS)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
