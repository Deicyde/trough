---
declaration: section
origin: cited
lean: AlgebraicGeometry.ProEtale.exists_covering_refining_proetaleCovering, AlgebraicGeometry.ProEtale.BigProetaleSite.IsContainedIn.fullyFaithfulSmallFunctor, AlgebraicGeometry.ProEtale.BigProetaleSite.IsContainedIn.smallFunctor_preservesFiniteLimits, AlgebraicGeometry.ProEtale.BigProetaleSite.IsContainedIn.smallFunctor_isCocontinuous, AlgebraicGeometry.ProEtale.BigProetaleSite.IsContainedIn.smallFunctor_isMorphismOfSites, AlgebraicGeometry.ProEtale.BigProetaleSite.IsContainedIn.smallToposRetraction, AlgebraicGeometry.ProEtale.BigProetaleSite.IsContainedIn.smallCohomologyRestrictionIso, AlgebraicGeometry.ProEtale.BigProetaleSite.IsContainedIn.smallCohomologyPushforwardIso
statement: formalized
proof: formalized
---

# 61.31 Change of partial universe

Section 61.31 of the Stacks Project, [Tag 0F4R](https://stacks.math.columbia.edu/tag/0F4R). 4 tags here are carried by 23 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 098J, a lemma

[Tag 098J](https://stacks.math.columbia.edu/tag/098J) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.exists_covering_refining_proetaleCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/PartialUniverseChange.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/Site/PartialUniverseChange.lean#L114).

> **Stacks 098J.** Let `B` be a chosen big pro-étale site and `T` one of its objects. Let
> `{Z i → T}_{i ∈ I}` be an *arbitrary* pro-étale covering of the underlying scheme of `T`: the
> index type `I` is unrestricted and the members `Z i` are arbitrary schemes, so neither the
> family nor its sources need belong to the chosen site. Then there is a covering family
> `E` of `T` *in the site* — one of the chosen bounded pro-étale families — which refines
> `{Z i → T}`: every member of `E` factors through some member of the given covering.
>
> The family `E` is built by covering `T` inside the site by affine objects with w-contractible
> global sections (Stacks 098I), refining the pullback of the given covering over each of them by
> a finite disjoint clopen decomposition (Stacks 098F), and taking a chosen representative of the
> composite.

```lean
theorem exists_covering_refining_proetaleCovering (B : BigProetaleSite.{u}) (T : B.Scheme)
    {I : Type w} (Z : I → Scheme.{u}) (g : (i : I) → Z i ⟶ T.obj)
    (hcov : Presieve.ofArrows Z g ∈ Scheme.proetalePrecoverage.coverings T.obj) :
    ∃ E : PreZeroHypercover.{u + 1} T, B.covering ⟨T, E⟩ ∧
      ∀ j : E.I₀, ∃ (i : I) (h : (E.X j).obj ⟶ Z i),
        h ≫ g i = B.inclusion.map (E.f j)
```

## Tag 098Y, a lemma

[Tag 098Y](https://stacks.math.columbia.edu/tag/098Y) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.BigProetaleSite.IsContainedIn.fullyFaithfulSmallFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/SmallEnlargement.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/Site/SmallEnlargement.lean#L116). The attribute's comment: “hypothesis (c) of 00XU for the inclusion of the small sites: full faithfulness”.

> **Stacks 098Y**, hypothesis (c) of Stacks 00XU: the inclusion of the two small pro-étale
> sites of `S` is fully faithful.
>
> Both small sites are full subcategories of nested big pro-étale categories over `S`, and the
> inclusion of those is fully faithful.

```lean
def fullyFaithfulSmallFunctor : (h.smallFunctor S hS).FullyFaithful
```

**`AlgebraicGeometry.ProEtale.BigProetaleSite.IsContainedIn.smallFunctor_preservesFiniteLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/SmallEnlargement.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/Site/SmallEnlargement.lean#L142). The attribute's comment: “hypotheses (d) and (e) of 00XU for the inclusion of the small sites: preservation of fibre products and of the final object”.

> **Stacks 098Y**, hypotheses (d) and (e) of Stacks 00XU: fibre products exist in the smaller
> small pro-étale site and are preserved by the inclusion, which also carries the final object
> `S/S` to the final object `S/S`.
>
> Both small sites have fibre products and the final object `𝟙 S` (Stacks 098M), both computed in
> the ambient big pro-étale category over `S`; the inclusion therefore preserves all finite
> limits.

```lean
theorem smallFunctor_preservesFiniteLimits : PreservesFiniteLimits (h.smallFunctor S hS)
```

**`AlgebraicGeometry.ProEtale.BigProetaleSite.IsContainedIn.smallFunctor_isCocontinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/SmallEnlargement.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/Site/SmallEnlargement.lean#L182). The attribute's comment: “hypothesis (a) of 00XU for the inclusion of the small sites: cocontinuity”.

> **Stacks 098Y**, hypothesis (a) of Stacks 00XU: the inclusion of the two small pro-étale
> sites of `S` is cocontinuous.
>
> A covering sieve of the larger small site at an object `X` of the smaller one contains a
> covering family of the larger small site, whose image in the larger big pro-étale category is a
> chosen covering family there, hence an arbitrary pro-étale covering of the scheme underlying
> `X`. By Stacks 098J that covering is refined by a chosen covering family of the *smaller* big
> site. The members of the refining family are weakly étale over `X`, being members of a pro-étale
> covering, hence weakly étale over `S`, so the family is a covering family of the smaller small
> site; and each of its members factors through a member of the given family, over `S` because the
> factorization is compatible with the maps to `X`.

```lean
instance smallFunctor_isCocontinuous :
    (h.smallFunctor S hS).IsCocontinuous (SmallProetale.topology B S hS)
      (SmallProetale.topology B' S (h.contains hS))
```

**`AlgebraicGeometry.ProEtale.BigProetaleSite.IsContainedIn.smallFunctor_isMorphismOfSites`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/SmallEnlargement.lean, line 263](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/Site/SmallEnlargement.lean#L263). The attribute's comment: “hypothesis (b) of 00XU for the inclusion of the small sites: continuity, in the form of being a morphism of sites”.

> **Stacks 098Y**, hypothesis (b) of Stacks 00XU: the inclusion of the two small pro-étale
> sites of `S` is continuous, and in fact defines a morphism of sites.
>
> Continuity follows from cover-preservation because the inclusion is representably flat, being
> left exact; the left adjoint of the pushforward on sheaves of sets is the sheafified left Kan
> extension, which is left exact for the same reason.

```lean
theorem smallFunctor_isMorphismOfSites :
    _root_.IsMorphismOfSites.{u + 1} (h.smallFunctor S hS)
      (SmallProetale.topology B S hS) (SmallProetale.topology B' S (h.contains hS))
```

**`AlgebraicGeometry.ProEtale.BigProetaleSite.IsContainedIn.smallToposRetraction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/SmallEnlargement.lean, line 303](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/Site/SmallEnlargement.lean#L303). The attribute's comment: “the two morphisms of topoi of the small sites, with `f ∘ g` isomorphic to the identity and `f_* = g^{-1}`”.

> **Stacks 098Y**, the conclusion of Stacks 00XU for the two small pro-étale sites of `S`: the
> morphisms of topoi `g : Sh(S_proetale) → Sh(S'_proetale)` and `f : Sh(S'\_proetale) →
> Sh(S\_proetale)` induced by the inclusion, whose composite is isomorphic to the identity and
> which satisfy `f_* = g^{-1}`.
>
> The direct image of `g` is the cocontinuous pushforward and the direct image of `f` is the
> continuous pushforward, which is also the inverse image of `g`; that is the identification
> `f_* = g^{-1}`. The retraction is the counit of the adjunction `g^{-1} ⊣ g_*`, invertible
> because the inclusion is fully faithful and cocontinuous.

```lean
noncomputable def smallToposRetraction :
    letI : (h.smallFunctor S hS).IsCocontinuous (SmallProetale.topology B S hS)
        (SmallProetale.topology B' S (h.contains hS)) := h.smallFunctor_isCocontinuous S hS
    letI : (h.smallFunctor S hS).IsContinuous (SmallProetale.topology B S hS)
        (SmallProetale.topology B' S (h.contains hS)) :=
      (h.smallFunctor_isMorphismOfSites S hS).toIsContinuous
    ToposRetraction (SmallProetale B S hS) (SmallProetale B' S (h.contains hS))
      (SmallProetale.topology B S hS) (SmallProetale.topology B' S (h.contains hS))
      (h.smallFunctor S hS)
```

**`AlgebraicGeometry.ProEtale.BigProetaleSite.IsContainedIn.smallCohomologyRestrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/SmallEnlargement.lean, line 424](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/Site/SmallEnlargement.lean#L424). The attribute's comment: “part (1): `H^p(S'_proetale, F') = H^p(S_proetale, g^{-1} F')`”.

> **Stacks 098Y, part (1).** For an abelian sheaf `F'` on the larger small pro-étale site of
> `S` and every degree `p`,
>
> `H^p(S'_proetale, F') = H^p(S_proetale, g^{-1} F')`,
>
> naturally in `F'`.
>
> This is Stacks 03YU applied to the inclusion: restriction along it is exact and carries
> injective abelian sheaves to injective abelian sheaves, because its left adjoint `g_!` is exact
> (Stacks 04BH), and it matches the two final objects `S/S`.

```lean
noncomputable def smallCohomologyRestrictionIso (p : ℕ) :
    (h.smallFunctor S hS).sheafPushforwardContinuous AddCommGrpCat.{u + 1}
          (SmallProetale.topology B S hS) (SmallProetale.topology B' S (h.contains hS)) ⋙
        Sheaf.functorH.{u + 1, u + 1, u, u + 1} (SmallProetale.topology B S hS) p ≅
      Sheaf.functorH.{u + 1, u + 1, u, u + 1}
        (SmallProetale.topology B' S (h.contains hS)) p
```

**`AlgebraicGeometry.ProEtale.BigProetaleSite.IsContainedIn.smallCohomologyPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/SmallEnlargement.lean, line 443](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/Site/SmallEnlargement.lean#L443). The attribute's comment: “part (2), first equality: `H^p(S_proetale, F) = H^p(S'_proetale, g_* F)`”.

> **Stacks 098Y, part (2), first equality.** For an abelian sheaf `F` on the smaller small
> pro-étale site of `S` and every degree `p`,
>
> `H^p(S_proetale, F) = H^p(S'_proetale, g_* F)`,
>
> naturally in `F`. This follows from part (1) because `g^{-1} g_* F = F`, the counit of
> `g^{-1} ⊣ g_*` being invertible for a fully faithful cocontinuous functor.

```lean
noncomputable def smallCohomologyPushforwardIso (p : ℕ) :
    Sheaf.functorH.{u + 1, u + 1, u, u + 1} (SmallProetale.topology B S hS) p ≅
      (h.smallFunctor S hS).sheafPushforwardCocontinuous AddCommGrpCat.{u + 1}
          (SmallProetale.topology B S hS) (SmallProetale.topology B' S (h.contains hS)) ⋙
        Sheaf.functorH.{u + 1, u + 1, u, u + 1}
          (SmallProetale.topology B' S (h.contains hS)) p
```

**`AlgebraicGeometry.ProEtale.BigProetaleSite.IsContainedIn.smallCohomologyLowerShriekIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/SmallEnlargement.lean, line 469](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/Site/SmallEnlargement.lean#L469). The attribute's comment: “part (2), second equality: `H^p(S_proetale, F) = H^p(S'_proetale, f^{-1} F)`”.

> **Stacks 098Y, part (2), second equality.** For an abelian sheaf `F` on the smaller small
> pro-étale site of `S` and every degree `p`,
>
> `H^p(S_proetale, F) = H^p(S'_proetale, f^{-1} F)`,
>
> naturally in `F`. This follows from part (1) because `g^{-1} f^{-1} F = F`: the inverse image
> `f^{-1} = g_!` is fully faithful (Stacks 00XU), so the unit of `g_! ⊣ g^{-1}` is invertible.

```lean
noncomputable def smallCohomologyLowerShriekIso (p : ℕ) :
    Sheaf.functorH.{u + 1, u + 1, u, u + 1} (SmallProetale.topology B S hS) p ≅
      (h.smallFunctor S hS).sheafPullback AddCommGrpCat.{u + 1}
          (SmallProetale.topology B S hS) (SmallProetale.topology B' S (h.contains hS)) ⋙
        Sheaf.functorH.{u + 1, u + 1, u, u + 1}
          (SmallProetale.topology B' S (h.contains hS)) p
```

## Tag 0F4S, a lemma

[Tag 0F4S](https://stacks.math.columbia.edu/tag/0F4S) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.BigProetaleSite.IsContainedIn.fullyFaithfulFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/Enlargement.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/Site/Enlargement.lean#L94). The attribute's comment: “hypothesis (c) of 00XU for the inclusion of the big sites: full faithfulness”.

> Hypothesis (c) of Stacks 00XU for the big sites: the inclusion functor is fully faithful.

```lean
def fullyFaithfulFunctor : h.functor.FullyFaithful
```

**`AlgebraicGeometry.ProEtale.BigProetaleSite.IsContainedIn.functor_isCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/Enlargement.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/Site/Enlargement.lean#L99). The attribute's comment: “hypothesis (a) of 00XU for the inclusion of the big sites: cocontinuity”.

> Hypothesis (a) of Stacks 00XU for the big sites: the inclusion functor is cocontinuous.

```lean
theorem functor_isCocontinuous : h.functor.IsCocontinuous B.topology B'.topology
```

**`AlgebraicGeometry.ProEtale.BigProetaleSite.IsContainedIn.functor_preservesFiniteLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/Enlargement.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/Site/Enlargement.lean#L125). The attribute's comment: “hypotheses (d) and (e) of 00XU for the inclusion of the big sites: preservation of fibre products and of the final object”.

> Hypotheses (d) and (e) of Stacks 00XU for the big sites: fibre products exist in the smaller
> category and are preserved by the inclusion, which also carries the final object `Spec ℤ` to the
> final object `Spec ℤ`; that is, the inclusion preserves finite limits.

```lean
theorem functor_preservesFiniteLimits : PreservesFiniteLimits h.functor
```

**`AlgebraicGeometry.ProEtale.BigProetaleSite.IsContainedIn.functor_isMorphismOfSites`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/Enlargement.lean, line 174](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/Site/Enlargement.lean#L174). The attribute's comment: “hypothesis (b) of 00XU for the inclusion of the big sites: continuity, in the form of being a morphism of sites”.

> Hypothesis (b) of Stacks 00XU for the big sites: the inclusion functor is continuous, and in
> fact defines a morphism of sites.

```lean
theorem functor_isMorphismOfSites :
    _root_.IsMorphismOfSites.{u + 1} h.functor B.topology B'.topology
```

**`AlgebraicGeometry.ProEtale.BigProetaleSite.IsContainedIn.toposRetraction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/Enlargement.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/Site/Enlargement.lean#L190). The attribute's comment: “the two morphisms of topoi of the big sites, with `f ∘ g` isomorphic to the identity and `f_* = g^{-1}`”.

> The conclusion of Stacks 00XU for the big sites: the two morphisms of topoi
> `g : Sh(Sch_proetale) → Sh(Sch'_proetale)` and `f : Sh(Sch'_proetale) → Sh(Sch_proetale)`
> induced by the inclusion, together with the isomorphism `f ∘ g ≅ id`.
>
> The direct image of `g` is the cocontinuous pushforward and the direct image of `f` is the
> continuous pushforward, which is also the inverse image of `g`; this is the identification
> `f_* = g^{-1}`. The retraction is the counit of the adjunction `g^{-1} ⊣ g_*`.

```lean
noncomputable def toposRetraction :
    let : h.functor.IsCocontinuous B.topology B'.topology := h.functor_isCocontinuous
    let : h.functor.IsContinuous B.topology B'.topology :=
      h.functor_isMorphismOfSites.toIsContinuous
    ToposRetraction B.Scheme B'.Scheme B.topology B'.topology h.functor
```

**`AlgebraicGeometry.ProEtale.BigProetaleSite.IsContainedIn.fullyFaithfulFunctorOver`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/Enlargement.lean, line 236](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/Site/Enlargement.lean#L236). The attribute's comment: “hypothesis (c) of 00XU for the inclusion of the slices: full faithfulness”.

> Hypothesis (c) of Stacks 00XU for the slices: the inclusion functor of the slices over `S` is
> fully faithful.

```lean
def fullyFaithfulFunctorOver : (h.functorOver S hS).FullyFaithful
```

**`AlgebraicGeometry.ProEtale.BigProetaleSite.IsContainedIn.functorOver_isCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/Enlargement.lean, line 242](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/Site/Enlargement.lean#L242). The attribute's comment: “hypothesis (a) of 00XU for the inclusion of the slices: cocontinuity”.

> Hypothesis (a) of Stacks 00XU for the slices: the inclusion functor of the slices over `S` is
> cocontinuous.

```lean
theorem functorOver_isCocontinuous :
    (h.functorOver S hS).IsCocontinuous (BigProetaleOver.topology B S hS)
      (BigProetaleOver.topology B' S (h.contains hS))
```

**`AlgebraicGeometry.ProEtale.BigProetaleSite.IsContainedIn.functorOver_preservesFiniteLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/Enlargement.lean, line 255](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/Site/Enlargement.lean#L255). The attribute's comment: “hypotheses (d) and (e) of 00XU for the inclusion of the slices: preservation of fibre products and of the final object”.

> Hypotheses (d) and (e) of Stacks 00XU for the slices: the inclusion functor of the slices
> over `S` preserves finite limits.

```lean
theorem functorOver_preservesFiniteLimits : PreservesFiniteLimits (h.functorOver S hS)
```

**`AlgebraicGeometry.ProEtale.BigProetaleSite.IsContainedIn.functorOver_isMorphismOfSites`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/Enlargement.lean, line 264](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/Site/Enlargement.lean#L264). The attribute's comment: “hypothesis (b) of 00XU for the inclusion of the slices: continuity, in the form of being a morphism of sites”.

> Hypothesis (b) of Stacks 00XU for the slices: the inclusion functor of the slices over `S` is
> continuous, and in fact defines a morphism of sites.

```lean
theorem functorOver_isMorphismOfSites :
    _root_.IsMorphismOfSites.{u + 1} (h.functorOver S hS)
      (BigProetaleOver.topology B S hS) (BigProetaleOver.topology B' S (h.contains hS))
```

**`AlgebraicGeometry.ProEtale.BigProetaleSite.IsContainedIn.toposRetractionOver`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/Enlargement.lean, line 280](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/Site/Enlargement.lean#L280). The attribute's comment: “the two morphisms of topoi of the slices, with `f ∘ g` isomorphic to the identity and `f_* = g^{-1}`”.

> The conclusion of Stacks 00XU for the slices: the two morphisms of topoi
> `g : Sh((Sch/S)_proetale) → Sh((Sch'/S)_proetale)` and `f` in the other direction induced by the
> inclusion of the slices over `S`, together with the isomorphism `f ∘ g ≅ id`.

```lean
noncomputable def toposRetractionOver :
    let : (h.functorOver S hS).IsCocontinuous (BigProetaleOver.topology B S hS)
        (BigProetaleOver.topology B' S (h.contains hS)) := h.functorOver_isCocontinuous S hS
    let : (h.functorOver S hS).IsContinuous (BigProetaleOver.topology B S hS)
        (BigProetaleOver.topology B' S (h.contains hS)) :=
      (h.functorOver_isMorphismOfSites S hS).toIsContinuous
    ToposRetraction (BigProetaleOver B S hS) (BigProetaleOver B' S (h.contains hS))
      (BigProetaleOver.topology B S hS) (BigProetaleOver.topology B' S (h.contains hS))
      (h.functorOver S hS)
```

## Tag 0F4T, a lemma

[Tag 0F4T](https://stacks.math.columbia.edu/tag/0F4T) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.BigProetaleSite.IsContainedIn.cohomologyRestrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/ChangeOfPartialUniverse.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/Site/ChangeOfPartialUniverse.lean#L139). The attribute's comment: “part (1), the cohomology over an object of the smaller big pro-étale site of the restriction of an abelian sheaf agrees with its cohomology over the image of that object”.

> Let `S` be a scheme and let `(Sch/S)_proétale` and `(Sch'/S)_proétale` be two big pro-étale
> sites of `S` as in Definition 098K, the first contained in the second.  For any object `U` of
> `(Sch/S)_proétale` and any degree `p`,
>
> `H^p(U, ℱ'|_{(Sch/S)_proétale}) = H^p(U, ℱ')`
>
> naturally in the abelian sheaf `ℱ'` on `(Sch'/S)_proétale`, where cohomology over an object is
> Mathlib's `Ext`-based `CategoryTheory.Sheaf.cohomologyPresheafFunctor`.
>
> By Stacks 0F4S the localized inclusion is continuous, cocontinuous and preserves finite limits,
> and both localized sites are essentially small, so this is Stacks 03YU,
> `Stacks.Cohomology.BiggerSite.cohomologyPresheafFunctorIso`.

```lean
noncomputable def cohomologyRestrictionIso
    [HasSheafify (BigProetaleOver.topology B S hS) Ab.{u}]
    [HasSheafify (BigProetaleOver.topology B' S (h.contains hS)) Ab.{u}]
    [HasExt.{w} (Sheaf (BigProetaleOver.topology B S hS) Ab.{u})]
    [HasExt.{w} (Sheaf (BigProetaleOver.topology B' S (h.contains hS)) Ab.{u})]
    (U : BigProetaleOver B S hS) (p : ℕ) :
    (h.functorOver S hS).sheafPushforwardContinuous Ab.{u}
          (BigProetaleOver.topology B S hS)
          (BigProetaleOver.topology B' S (h.contains hS)) ⋙
        Sheaf.cohomologyPresheafFunctor (BigProetaleOver.topology B S hS) p ⋙
          (evaluation (BigProetaleOver B S hS)ᵒᵖ Ab.{w}).obj (op U) ≅
      Sheaf.cohomologyPresheafFunctor (BigProetaleOver.topology B' S (h.contains hS)) p ⋙
        (evaluation (BigProetaleOver B' S (h.contains hS))ᵒᵖ Ab.{w}).obj
          (op ((h.functorOver S hS).obj U))
```

**`AlgebraicGeometry.ProEtale.BigProetaleSite.IsContainedIn.exists_extension_abelianSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/ChangeOfPartialUniverse.lean, line 223](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/Site/ChangeOfPartialUniverse.lean#L223). The attribute's comment: “part (2), every abelian sheaf on the smaller big pro-étale site is the restriction of an abelian sheaf on the bigger site”.

> Let `S` be a scheme and let `(Sch/S)_proétale` and `(Sch'/S)_proétale` be two big pro-étale
> sites of `S` as in Definition 098K, the first contained in the second.  For any abelian sheaf
> `ℱ` on `(Sch/S)_proétale` there is an abelian sheaf `ℱ'` on `(Sch'/S)_proétale` whose
> restriction to `(Sch/S)_proétale` is isomorphic to `ℱ`.
>
> The witness is the sheaf pullback along the inclusion, and the isomorphism is the inverse unit
> of the adjunction, invertible by Stacks 00XU.

```lean
theorem exists_extension_abelianSheaf
    (F : Sheaf (BigProetaleOver.topology B S hS) Ab.{u}) :
    ∃ F' : Sheaf (BigProetaleOver.topology B' S (h.contains hS)) Ab.{u},
      Nonempty ((h.abelianRestrictionOver S hS).obj F' ≅ F)
```

**`AlgebraicGeometry.ProEtale.BigProetaleSite.IsContainedIn.cohomologyPresheafRestrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/ChangeOfPartialUniverseUnconditional.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/Site/ChangeOfPartialUniverseUnconditional.lean#L105). The attribute's comment: “part (1), the cohomology over an object of the smaller big pro-étale site of the restriction of an abelian sheaf on the bigger site agrees with the cohomology of that sheaf over the same object in the bigger site, naturally in the sheaf, for every degree”.

> **Stacks 0F4T (1).** Let `S` be a scheme and let `(Sch/S)_proétale` and
> `(Sch'/S)_proétale` be two big pro-étale sites of `S` as in Definition 098K, the first contained
> in the second.  For any object `U` of `(Sch/S)_proétale` and any degree `p`,
>
> `H^p(U, ℱ'|_{(Sch/S)_proétale}) = H^p(U, ℱ')`
>
> naturally in the abelian sheaf `ℱ'` on `(Sch'/S)_proétale`, where cohomology over an object is
> Mathlib's `Ext`-based `CategoryTheory.Sheaf.cohomologyPresheafFunctor` with values in any
> universe `w` where the `Ext`-groups of the two sheaf categories are small (for instance `w = u`,
> by `AlgebraicGeometry.ProEtale.hasExt_sheaf_bigProetaleOver`).
>
> Sheafification on both sites is `AlgebraicGeometry.ProEtale.hasSheafify_bigProetaleOver_abelian`,
> and the comparison is
> `AlgebraicGeometry.ProEtale.BigProetaleSite.IsContainedIn.cohomologyRestrictionIso`.

```lean
noncomputable def cohomologyPresheafRestrictionIso
    [HasExt.{w} (Sheaf (BigProetaleOver.topology B S hS) Ab.{u})]
    [HasExt.{w} (Sheaf (BigProetaleOver.topology B' S (h.contains hS)) Ab.{u})]
    (U : BigProetaleOver B S hS) (p : ℕ) :
    (h.functorOver S hS).sheafPushforwardContinuous Ab.{u}
          (BigProetaleOver.topology B S hS)
          (BigProetaleOver.topology B' S (h.contains hS)) ⋙
        Sheaf.cohomologyPresheafFunctor (BigProetaleOver.topology B S hS) p ⋙
          (evaluation (BigProetaleOver B S hS)ᵒᵖ Ab.{w}).obj (op U) ≅
      Sheaf.cohomologyPresheafFunctor (BigProetaleOver.topology B' S (h.contains hS)) p ⋙
        (evaluation (BigProetaleOver B' S (h.contains hS))ᵒᵖ Ab.{w}).obj
          (op ((h.functorOver S hS).obj U))
```

**`AlgebraicGeometry.ProEtale.BigProetaleSite.IsContainedIn.essSurj_abelianRestrictionOver`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/ChangeOfPartialUniverseUnconditional.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/Site/ChangeOfPartialUniverseUnconditional.lean#L131). The attribute's comment: “part (2), restriction of abelian sheaves from the bigger big pro-étale site to the smaller one is essentially surjective: every abelian sheaf on the smaller site is isomorphic to the restriction of an abelian sheaf on the bigger site”.

> **Stacks 0F4T (2).** Let `S` be a scheme and let `(Sch/S)_proétale` and
> `(Sch'/S)_proétale` be two big pro-étale sites of `S` as in Definition 098K, the first contained
> in the second.  Restriction of abelian sheaves from `(Sch'/S)_proétale` to `(Sch/S)_proétale` is
> essentially surjective: for any abelian sheaf `ℱ` on `(Sch/S)_proétale` there is an abelian
> sheaf `ℱ'` on `(Sch'/S)_proétale` whose restriction to `(Sch/S)_proétale` is isomorphic to `ℱ`.
>
> The witness is the sheaf pullback along the inclusion, which exists by
> `AlgebraicGeometry.ProEtale.hasSheafify_bigProetaleOver_abelian`; this is
> `AlgebraicGeometry.ProEtale.BigProetaleSite.IsContainedIn.exists_extension_abelianSheaf`.

```lean
instance essSurj_abelianRestrictionOver : (h.abelianRestrictionOver S hS).EssSurj
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 61.31, Tag 0F4R](https://stacks.math.columbia.edu/tag/0F4R)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
