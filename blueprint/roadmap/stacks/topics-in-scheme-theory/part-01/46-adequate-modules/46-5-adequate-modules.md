---
declaration: section
origin: cited
lean: Stacks.Adequate.IsAdequate, Stacks.Adequate.isAdequate_affineSectionFunctor, Stacks.Adequate.isEquivalence_adequateComparison, Stacks.Adequate.isAdequate_pullbackSheafOfAmbient, Stacks.Adequate.isAdequate_tfae, Stacks.Adequate.cechExact_and_isSheaf_of_isAdequate, Stacks.Adequate.adequate, Stacks.Adequate.BigSite.isZero_rightDerived_sections_of_isAdequate
statement: formalized
proof: formalized
---

# 46.5 Adequate modules

Section 46.5 of the Stacks Project, [Tag 06VF](https://stacks.math.columbia.edu/tag/06VF). 13 tags here are carried by 26 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06VF, the section

[Tag 06VF](https://stacks.math.columbia.edu/tag/06VF) in the Stacks Project.

Declarations registered for the tag:

- [`Stacks.Adequate.IsAdequate`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/AdequateSheafOfModules.lean#L313), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Duality/AdequateSheafOfModules.lean, line 348](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/AdequateSheafOfModules.lean#L348) (StacksFrontier): “Section 46.5: a sheaf of 𝒪-modules on (Sch/S)_τ is adequate when its affine-section functors are adequate over the members of a τ-covering of S by affines”.

## Tag 06VG, a definition

[Tag 06VG](https://stacks.math.columbia.edu/tag/06VG) in the Stacks Project.

**`Stacks.Adequate.IsAdequate`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/AdequateSheafOfModules.lean, line 313](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/AdequateSheafOfModules.lean#L313).

> Adequacy of a sheaf of modules on the selected big site.

```lean
public abbrev IsAdequate
    {τ : CoveringTopology} {S : Scheme.{u}} (B : BigSite τ S)
    (F : SheafOfModules.{m} B.structureSheaf) : Prop
```

## Tag 06VI, a lemma

[Tag 06VI](https://stacks.math.columbia.edu/tag/06VI) in the Stacks Project.

**`Stacks.Adequate.isAdequate_affineSectionFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AffineLocalUnconditional.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AffineLocalUnconditional.lean#L72).

> [Stacks, Tag 06VI]: for an adequate sheaf of modules `F` on the big `τ`-site over `S`, the
> affine-section functor `F_{F, A}` is adequate for *every* affine scheme `Spec A` of the site
> over `S`, not only for the members of the covering witnessing adequacy of `F`.
>
> All three steps of the source's proof are supplied by the library:
> `Stacks.Adequate.standardAffineRefinement` and `Stacks.Adequate.affineSectionRestriction`, which
> discharge `StandardAffineRefinement` and `AffineSectionRestriction`, and
> `Stacks.Adequate.standardAffineDescent`, which discharges `StandardAffineDescent`. See the module
> documentation.

```lean
public theorem isAdequate_affineSectionFunctor
    {τ : CoveringTopology} {S : Scheme.{u}} (B : BigSite τ S)
    (F : SheafOfModules.{max u m} B.structureSheaf)
    (hF : IsAdequate B F)
    (A : CommRingCat.{u}) (f : Spec A ⟶ S)
    (hA : schemeSizeBelow B.cutoff (Spec A)) :
    AdequateFunctor.IsAdequate
      (AdequateFunctor.siteAlgebraInclusion A (schemeSizeBelow B.cutoff))
      (affineSectionFunctor B F A f)
```

## Tag 06ZJ, a lemma

[Tag 06ZJ](https://stacks.math.columbia.edu/tag/06ZJ) in the Stacks Project.

**`Stacks.Adequate.isEquivalence_adequateComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AffineEquivalence.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AffineEquivalence.lean#L78). The attribute's comment: “the equivalence itself: the comparison functor 𝓕 ↦ F_{𝓕, A} from adequate 𝒪-modules on (Sch/Spec A)_τ to adequate module-valued functors on the A-algebras of the site is an equivalence of categories, with no hypothesis, at the value universe u of the site. The functor is `Stacks.Adequate.adequateComparison`, which carries the tag for the functor alone; full faithfulness and essential surjectivity are `Stacks.Adequate.fullyFaithful_of_affineSectionsFunctor` and `Stacks.Adequate.essSurj_of_affineSectionsFunctor`, the latter being the quasi-inverse the source builds from an exact sequence 0 → F → M̲ → N̲”.

> **[Stacks, Tag 06ZJ].** For `S = Spec A` affine, the comparison functor
> `𝓕 ↦ F_{𝓕, A}` from the category `Adeq(𝒪)` of adequate `𝒪`-modules on `(Sch/S)_τ` to the
> category of adequate module-valued functors on the `A`-algebras of the site is an equivalence
> of categories. So the two categories are equivalent, by the source's own comparison.
>
> Full faithfulness is full faithfulness of the affine-section functor over an affine base and
> essential surjectivity is the quasi-inverse
> `Stacks.Adequate.exists_isAdequate_affineSectionsFunctor_iso`, which builds the adequate
> `𝒪`-module from an exact sequence `0 → F → M̲ → N̲` as `Ker(M^a → N^a)`; both are packaged in
> `Stacks.Adequate.isEquivalence_of_affineSectionsFunctor`, and
> `Stacks.Adequate.adequateComparison_ι` is the identification that theorem asks for.

```lean
public theorem isEquivalence_adequateComparison {τ : CoveringTopology} {A : CommRingCat.{u}}
    (B : BigSite τ (Spec A)) : (adequateComparison.{u, u} B).IsEquivalence
```

## Tag 06VJ, a lemma

[Tag 06VJ](https://stacks.math.columbia.edu/tag/06VJ) in the Stacks Project.

**`Stacks.Adequate.isAdequate_pullbackSheafOfAmbient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/Pullback.lean, line 393](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/Pullback.lean#L393). The attribute's comment: “the pullback of an adequate 𝒪-module along a morphism of schemes is adequate, for the two sites the localizations of one ambient big site, as they are in the source”.

> [Stacks, Tag 06VJ]: the pullback `f^*𝓕` of an adequate `𝒪`-module `𝓕` on `(Sch/S)_τ` is an
> adequate `𝒪`-module on `(Sch/T)_τ`, where `(Sch/S)_τ` and `(Sch/T)_τ` are the localizations at
> `S` and at `T` of one ambient big `τ`-site, as they are in the source.
>
> The pullback is the restriction of `𝓕` along the index functor, which is a sheaf by
> `isSheaf_pullbackVal`; its affine-section functor at an affine `Spec A` over `T` is the
> affine-section functor of `𝓕` at `Spec A` over `S` by `affineSectionFunctor_pullbackSheaf`,
> which [Stacks, Tag 06VI] shows to be adequate; and adequacy of `f^*𝓕` follows because the
> affine open cover of `T` is a `τ`-covering by affine schemes of the site.
>
> By `BigSite.exists_eq_ofAmbient` every chosen big site is a localization of an ambient big
> site, so no generality is lost in stating the lemma this way.
>
> Nothing is assumed beyond adequacy of `𝓕`: Tag 06VI is itself unconditional, so the appeal to
> it in the source's proof carries no hypothesis here either. See the module documentation.

```lean
public theorem isAdequate_pullbackSheafOfAmbient (f : T ⟶ S)
    (F : SheafOfModules.{max u m} (BigSite.ofAmbient 𝒮 S hS).structureSheaf)
    (hF : IsAdequate (BigSite.ofAmbient 𝒮 S hS) F) :
    IsAdequate (BigSite.ofAmbient 𝒮 T hT) (pullbackSheafOfAmbient 𝒮 hS hT f F)
```

## Tag 06VK, a lemma

[Tag 06VK](https://stacks.math.columbia.edu/tag/06VK) in the Stacks Project.

**`Stacks.Adequate.isAdequate_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/CharacterizationsTFAE.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/CharacterizationsTFAE.lean#L86). The attribute's comment: “the whole tag as one statement: all five conditions on an 𝒪-module on the big τ-site over a scheme are equivalent, listed in the source's order and with no hypotheses”.

> **[Stacks, Tag 06VK].** For an `𝒪`-module `𝓕` on the big `τ`-site over a scheme `S` the
> following five conditions are equivalent, in the source's order:
>
> 1. `𝓕` is adequate;
> 2. there is an affine open covering `S = ⋃ Sᵢ` and, for each `i`, a map `𝓖ᵢ ⟶ 𝓗ᵢ` of
>    quasi-coherent `𝒪_{Sᵢ}`-modules presenting `𝓕|_(Sch/Sᵢ)_τ` as the kernel of
>    `𝓖ᵢᵃ ⟶ 𝓗ᵢᵃ`;
> 3. the same over a `τ`-covering `{Sᵢ → S}` of `S` rather than an affine open covering;
> 4. there is a `τ`-covering `{fᵢ : Sᵢ → S}` of `S` with every pullback `fᵢ^*𝓕` adequate;
> 5. for every affine scheme `Spec A` of the site over `S` the restriction `𝓕|_(Sch/Spec A)_τ` is
>    the kernel of a map `𝓖ᵃ ⟶ 𝓗ᵃ` of associated modules of quasi-coherent
>    `𝒪_{Spec A}`-modules.
>
> The statement is unconditional: each of the four equivalences with condition (1) holds with no
> hypotheses, and `tfae_finish` assembles the remaining edges.

```lean
public theorem isAdequate_tfae (F : SheafOfModules.{u} B.structureSheaf) :
    [IsAdequate B F,
      HasAffineOpenAssociatedKernelCover B F,
      HasCoveringAssociatedKernel B F,
      HasAdequatePullbackCover B F,
      HasAssociatedKernelOnEveryAffine B F].TFAE
```

## Tag 06VL, a lemma

[Tag 06VL](https://stacks.math.columbia.edu/tag/06VL) in the Stacks Project.

**`Stacks.Adequate.cechExact_and_isSheaf_of_isAdequate`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AdequateCechExactnessAndSheafConditions.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AdequateCechExactnessAndSheafConditions.lean#L129). The attribute's comment: “the whole statement: for an adequate `𝒪`-module on a chosen big `τ`-site over `S`, the extended Čech complex `0 → F(Spec A) → F(Spec B) → F(Spec (B ⊗_A B)) → ⋯` of every surjective flat morphism of affines of the site is exact at every spot -- at the two left-hand spots as the sheaf condition for the one-member presieve, at the rest as the vanishing of the Čech cohomology in positive degrees -- and the two `in particular` conclusions, the fpqc sheaf condition and being a sheaf of `𝒪`-modules for the fppf coverings, the latter both as the sheaf axiom for the fppf topology and as a term of the category of `𝒪`-modules on `(Sch/S)_fppf`.”.

> **[Stacks, Tag 06VL], the whole statement.**
>
> Let `F` be an adequate `𝒪`-module on a chosen big `τ`-site over `S`. Then:
>
> 1. for every surjective flat morphism `f : Spec B ⟶ Spec A` between affine objects of the site,
>    the extended Čech complex
>    `0 → F(Spec A) → F(Spec B) → F(Spec (B ⊗_A B)) → ⋯`
>    is exact — at its two left-hand spots, which is the sheaf condition for the one-member
>    presieve `{f}`, and at every remaining spot, which is the vanishing of the Čech cohomology of
>    `{f}` in every positive degree;
> 2. `F` satisfies the sheaf condition for the fpqc covering families of the site; and
> 3. `F` is a sheaf of `𝒪`-modules for the fppf covering families of the site, that is, its
>    underlying presheaf of abelian groups satisfies the fppf sheaf condition; and
> 4. equivalently, read as a statement about the object rather than about the sheaf axiom, there
>    is a sheaf of `𝒪`-modules on `(Sch/S)_fppf` — a term of `CategoryTheory.SheafOfModules` over
>    `Stacks.Adequate.BigSite.fppfStructureSheaf`, the structure sheaf of rings of the site read
>    at the fppf topology by [Stacks, Tag 03OJ] — whose underlying presheaf of `𝒪`-modules is
>    that of `F`.
>
> Clause (1) is the body of the tag and clauses (2) and (3) are its two "in particular"s, clause
> (4) being clause (3) repackaged.

```lean
public theorem cechExact_and_isSheaf_of_isAdequate
    {τ : CoveringTopology} {S : Scheme.{u}}
    (B : BigSite τ S) (F : SheafOfModules.{max u m} B.structureSheaf)
    (hF : IsAdequate B F) :
    letI : HasFiniteLimits B.category := B.hasFiniteLimits_category
    (∀ (X Y : B.category) (f : Y ⟶ X), X ∈ B.affineObjects → Y ∈ B.affineObjects →
        Flat (B.toOver.map f).left → Surjective (B.toOver.map f).left →
          Presieve.IsSheafFor (F.val.presheaf ⋙ forget AddCommGrpCat.{max u m})
              (Presieve.singleton f) ∧
            ∀ n : ℕ, 0 < n →
              IsZero (Stacks.CechSite.cechCohomology (PreZeroHypercover.singleton.{0} f)
                F.val.presheaf n)) ∧
      Presheaf.IsSheaf (fpqcPrecoverageOn B).toGrothendieck F.val.presheaf ∧
      Presheaf.IsSheaf (fppfPrecoverageOn B).toGrothendieck F.val.presheaf ∧
      ∃ G : SheafOfModules.{max u m} B.fppfStructureSheaf, G.val = F.val
```

## Tag 07AH, a definition

[Tag 07AH](https://stacks.math.columbia.edu/tag/07AH) in the Stacks Project.

**`Stacks.Adequate.adequate`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/AdequateSheafOfModules.lean, line 329](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/AdequateSheafOfModules.lean#L329).

> The category `Adeq(𝒪)` of adequate `𝒪`-modules on the selected big site: the strictly full
> subcategory of the sheaves of modules on the site cut out by adequacy.

```lean
public abbrev adequate
    {τ : CoveringTopology} {S : Scheme.{u}} (B : BigSite τ S) :
    ObjectProperty (SheafOfModules.{m} B.structureSheaf)
```

## Tag 06VM, a lemma

[Tag 06VM](https://stacks.math.columbia.edu/tag/06VM) in the Stacks Project.

**`Stacks.Adequate.BigSite.isZero_rightDerived_sections_of_isAdequate`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AffineCohomologyVanishingUnconditional.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AffineCohomologyVanishingUnconditional.lean#L141). The attribute's comment: “(3): for an adequate 𝒪-module F on (Sch/S)_τ and every affine scheme U over S, H^q(U, F) = 0 for all q > 0; cohomology is the right derived functor of sections over U of the abelian sheaf underlying F”.

> **[Stacks, Tag 06VM] (3).** Let `𝓕` be an adequate `𝒪`-module on a chosen big `τ`-site
> `(Sch/S)_τ` over a scheme `S`. For every affine scheme `U` over `S` belonging to the site,
> `H^q(U, 𝓕) = 0` for all `q > 0`, where `H^q(U, −)` is the `q`-th right derived functor of
> sections over `U` on abelian sheaves on the site, applied to the abelian sheaf underlying `𝓕`.
>
> This is [Stacks, Tag 03F9] at the collection of affine objects of the site and the collection
> of finite affine `τ`-coverings of those objects: the objects occurring in such a covering are
> affine by `Stacks.Adequate.BigSite.isAffine_product_of_mem_affineCov`, the coverings are
> cofinal by `Stacks.Adequate.BigSite.affineCovCofinal`, and the Čech cohomology of an adequate
> module vanishes on them by `Stacks.Adequate.BigSite.cechCohomology_isZero_of_isAdequate`.

```lean
public theorem BigSite.isZero_rightDerived_sections_of_isAdequate (B : BigSite τ S)
    (F : SheafOfModules.{max u m} B.structureSheaf) (hF : IsAdequate B F)
    (U : B.category) [IsAffine U.left.obj] (q : ℕ) (hq : 0 < q) :
    IsZero ((((sheafSections B.topology AddCommGrpCat.{max u m}).obj (op U)).rightDerived q).obj
      ((SheafOfModules.toSheaf B.structureSheaf).obj F))
```

**`Stacks.Adequate.BigSite.adequateCohomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/CohomologyComparison.lean, line 421](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/CohomologyComparison.lean#L421). The attribute's comment: “(4): for an adequate 𝒪-module F on (Sch/S)_τ, the canonical isomorphism H^q(S, F|_{S_Zar}) = H^q((Sch/S)_τ, F) in every degree q, cohomology being the right derived functor of global sections”.

> **[Stacks, Tag 06VM] (4).** For an adequate `𝒪`-module `𝓕` on a chosen big `τ`-site
> `(Sch/S)_τ` over a scheme `S`, the canonical isomorphism
>
> `H^q(S, 𝓕|_{S_Zar}) ≅ H^q((Sch/S)_τ, 𝓕)`
>
> in every degree `q`, where `𝓕|_{S_Zar}` is `Stacks.Adequate.BigSite.zariskiRestrictModule` and
> cohomology is the right derived functor of global sections of the underlying abelian sheaves.
> It is the Grothendieck edge isomorphism of the composite `Γ(S_Zar, −) ∘ (−)|_{S_Zar} = Γ`, the
> higher direct images of `𝓕` vanishing by
> `Stacks.Adequate.BigSite.higherZariskiRestrictionVanishing`.

```lean
public noncomputable def BigSite.adequateCohomologyIso (F : SheafOfModules.{u} B.structureSheaf)
    (hF : IsAdequate B F) (q : ℕ) :
    ((zariskiGlobalSections S).rightDerived q).obj
        ((SheafOfModules.toSheaf S.ringCatSheaf).obj (B.zariskiRestrictModule.obj F)) ≅
      (B.globalSections.rightDerived q).obj ((SheafOfModules.toSheaf B.structureSheaf).obj F)
```

**`Stacks.Adequate.BigSite.isIso_etaleRestrictionComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/EtaleRestriction.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/EtaleRestriction.lean#L191). The attribute's comment: “(2), for the small étale site of any big étale site whose schemes are schemes of (Sch/S)_τ: the restriction F|_{S_étale} of an adequate 𝒪-module F is the quasi-coherent module associated to F|_{S_Zar}, the canonical map (F|_{S_Zar})^a → F|_{S_étale} being an isomorphism”.

> **[Stacks, Tag 06VM] (2).** Let `𝓕` be an adequate `𝒪`-module on a chosen big `τ`-site
> `(Sch/S)_τ` over a scheme `S`. The restriction `𝓕|_{S_étale}` of `𝓕` to the small étale site of
> `S` is the quasi-coherent module associated to `𝓕|_{S_Zar}`: the canonical comparison
> `(𝓕|_{S_Zar})^a ⟶ 𝓕|_{S_étale}` is an isomorphism.

```lean
public theorem BigSite.isIso_etaleRestrictionComparison
    (F : SheafOfModules.{u} B.structureSheaf) (hF : IsAdequate B F) :
    IsIso (B.etaleRestrictionComparison E hSE hle F hF)
```

**`Stacks.Adequate.BigSite.isIso_etaleSiteRestrictionComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/EtaleRestriction.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/EtaleRestriction.lean#L247). The attribute's comment: “(2): for an adequate 𝒪-module F on (Sch/S)_τ the restriction F|_{S_étale} to the small étale site of S is the quasi-coherent module associated to F|_{S_Zar}, the canonical map (F|_{S_Zar})^a → F|_{S_étale} being an isomorphism”.

> **[Stacks, Tag 06VM] (2) for the small étale site `S_étale` of `(Sch/S)_τ` itself.** Let `𝓕`
> be an adequate `𝒪`-module on a chosen big `τ`-site `(Sch/S)_τ`, for any of the five
> topologies, and let `S_étale` be the small étale site of `S` in the same category of schemes,
> `Stacks.Adequate.BigSite.etaleSite`. The restriction `𝓕|_{S_étale}` is the quasi-coherent module
> associated to `𝓕|_{S_Zar}`: the canonical comparison `(𝓕|_{S_Zar})^a ⟶ 𝓕|_{S_étale}` is an
> isomorphism.

```lean
public theorem BigSite.isIso_etaleSiteRestrictionComparison
    (F : SheafOfModules.{u} B.structureSheaf) (hF : IsAdequate B F) :
    IsIso (B.etaleRestrictionComparison B.etaleSite B.contains_etaleSite B.etaleSite_cutoff.le
      F hF)
```

**`Stacks.Adequate.BigSite.isQuasicoherent_zariskiRestrictModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/ZariskiRestriction.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/ZariskiRestriction.lean#L61). The attribute's comment: “(1): for an adequate 𝒪-module F on (Sch/S)_τ the restriction F|_{S_Zar} is a quasi-coherent 𝒪_S-module on the scheme S”.

> **[Stacks, Tag 06VM] (1).** Let `𝓕` be an adequate `𝒪`-module on a chosen big `τ`-site
> `(Sch/S)_τ` over a scheme `S`. The restriction `𝓕|_{S_Zar}` of `𝓕` to the small Zariski site of
> `S` is a quasi-coherent `𝒪_S`-module on the scheme `S`.
>
> The sections of `𝓕|_{S_Zar}` over the basic open `D(a)` of an affine open `U` are the base change
> of the sections over `U` along `𝒪(U) → 𝒪(D(a))`, by
> `Stacks.Adequate.BigSite.affineOpenBaseChange`, hence their localization away from `a`.

```lean
public theorem BigSite.isQuasicoherent_zariskiRestrictModule (B : BigSite τ S)
    (F : SheafOfModules.{u} B.structureSheaf) (hF : IsAdequate B F) :
    (B.zariskiRestrictModule.obj F).IsQuasicoherent
```

## Tag 06VN, a remark

[Tag 06VN](https://stacks.math.columbia.edu/tag/06VN) in the Stacks Project.

**`Stacks.Adequate.BigSite.nonempty_associatedModuleFunctor_obj_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AssociatedModuleAdjunction.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AssociatedModuleAdjunction.lean#L188). The attribute's comment: “`F^a` is the pullback of `F` under the morphism of ringed topoi `((Sch/S)_τ, 𝒪) → (S_Zar, 𝒪_S)` whose pushforward is restriction to `S_Zar`”.

> **The pullback of a quasi-coherent `𝒪_S`-module is its associated module `𝓕^a`** of
> [Stacks, Tag 03DU], whose sections over `T/S` are the global sections of the pullback of `𝓕` to
> `T`. This is the description of `𝓕^a` as a pullback in Descent, [Stacks, Tag 03FH], which
> [Stacks, Tag 06VN] invokes. After `Stacks.Adequate.BigSite.exists_baseOverTopology` substitutes
> the topology it is `AlgebraicGeometry.BigFppfOver.baseAssociatedModuleIsoSectionsSheaf`.

```lean
public theorem BigSite.nonempty_associatedModuleFunctor_obj_iso (B : BigSite τ S)
    (F : S.Modules) [F.IsQuasicoherent] :
    Nonempty (B.associatedModuleFunctor.obj F ≅
      B.associatedModule F (isSheaf_associatedPresheaf B F))
```

**`Stacks.Adequate.BigSite.associatedModuleAdeq`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AssociatedModuleAdjunction.lean, line 304](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AssociatedModuleAdjunction.lean#L304). The attribute's comment: “the functor `u : QCoh(𝒪_S) ⥤ Adeq(𝒪)`, `F ↦ F^a`”.

> **[Stacks, Tag 06VN], the functor `u`.** The associated-module functor
> `u : QCoh(𝒪_S) ⥤ Adeq(𝒪)`, `𝓕 ↦ 𝓕^a`, on a chosen big `τ`-site over `S`; it lands in the
> adequate modules by [Stacks, Tag 06VK].

```lean
public noncomputable abbrev BigSite.associatedModuleAdeq (B : BigSite τ S) :
    (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory ⥤
      (adequate.{u, u} B).FullSubcategory
```

**`Stacks.Adequate.BigSite.restrictModuleQCoh`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AssociatedModuleAdjunction.lean, line 313](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AssociatedModuleAdjunction.lean#L313). The attribute's comment: “the functor `v : Adeq(𝒪) ⥤ QCoh(𝒪_S)`, `G ↦ G|_{S_Zar}`”.

> **[Stacks, Tag 06VN], the functor `v`.** Restriction to the small Zariski site of `S` as a
> functor `v : Adeq(𝒪) ⥤ QCoh(𝒪_S)`, `𝓖 ↦ 𝓖|_{S_Zar}`, on a chosen big `τ`-site over `S`; it
> lands in the quasi-coherent modules by [Stacks, Tag 06VM] (1).

```lean
public noncomputable abbrev BigSite.restrictModuleQCoh (B : BigSite τ S) :
    (adequate.{u, u} B).FullSubcategory ⥤
      (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory
```

**`Stacks.Adequate.BigSite.adeqAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AssociatedModuleAdjunction.lean, line 356](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AssociatedModuleAdjunction.lean#L356). The attribute's comment: “the adjunction `u ⊣ v` between `QCoh(𝒪_S)` and `Adeq(𝒪)`, whose hom-set bijection is `Hom_{𝒪_S}(F, vG) = Hom_𝒪(uF, G)`”.

> **[Stacks, Tag 06VN], the adjunction.** On a chosen big `τ`-site over `S`, for each of the
> five topologies, the associated-module functor `u : QCoh(𝒪_S) ⥤ Adeq(𝒪)` is left adjoint to
> restriction `v : Adeq(𝒪) ⥤ QCoh(𝒪_S)`, so `Hom_{𝒪_S}(𝓕, v𝓖) = Hom_𝒪(u𝓕, 𝓖)`
> (`Stacks.Adequate.BigSite.adeqAdjunction.homEquiv`). It is the pullback–pushforward adjunction
> of the morphism of ringed sites `((Sch/S)_τ, 𝒪) → (S_Zar, 𝒪_S)`, restricted to the two full
> subcategories.

```lean
public noncomputable def BigSite.adeqAdjunction (B : BigSite τ S) :
    B.associatedModuleAdeq ⊣ B.restrictModuleQCoh
```

**`Stacks.Adequate.BigSite.isIso_adeqAdjunction_unit_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AssociatedModuleAdjunction.lean, line 366](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AssociatedModuleAdjunction.lean#L366). The attribute's comment: “the map `F → vuF` is an isomorphism for every `F` in `QCoh(𝒪_S)`”.

> **[Stacks, Tag 06VN], the unit.** The unit `𝓕 → vu𝓕` of the adjunction between
> `QCoh(𝒪_S)` and `Adeq(𝒪)` is an isomorphism at every quasi-coherent `𝒪_S`-module, on a chosen
> big `τ`-site over `S` for each of the five topologies.

```lean
public theorem BigSite.isIso_adeqAdjunction_unit_app (B : BigSite τ S)
    (M : (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory) :
    IsIso (B.adeqAdjunction.unit.app M)
```

**`Stacks.Adequate.BigSite.fullyFaithfulAssociatedModuleAdeq`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AssociatedModuleAdjunction.lean, line 389](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AssociatedModuleAdjunction.lean#L389). The attribute's comment: “consequence of `F → vuF` being an isomorphism: `u : QCoh(𝒪_S) ⥤ Adeq(𝒪)` is fully faithful”.

> **[Stacks, Tag 06VN], consequence of the unit.** `u : QCoh(𝒪_S) ⥤ Adeq(𝒪)` is fully
> faithful, on a chosen big `τ`-site over `S` for each of the five topologies: the unit
> `𝓕 → vu𝓕` of the adjunction `u ⊣ v` is an isomorphism at every object of `QCoh(𝒪_S)`
> (`Stacks.Adequate.BigSite.isIso_adeqAdjunction_unit_app`).

```lean
public noncomputable def BigSite.fullyFaithfulAssociatedModuleAdeq (B : BigSite τ S) :
    B.associatedModuleAdeq.FullyFaithful
```

## Tag 06VP, a lemma

[Tag 06VP](https://stacks.math.columbia.edu/tag/06VP) in the Stacks Project.

**`Stacks.Adequate.isAdequate_sheafification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/Sheafification.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/Sheafification.lean#L216). The attribute's comment: “assuming `AffineAdequateSheafTopology.{u, m}`, which is a theorem for `m = u` (`Stacks.Adequate.affineAdequateSheafTopology`) and open for a general `m`”.

> [Stacks, Tag 06VP]: let `F` be a presheaf of `O`-modules on the big `τ`-site over `S`. If
> for *every* affine scheme `Spec A` over `S` belonging to the site the functor `F_{F, A}` is
> adequate, then the sheafification of `F` is an adequate `O`-module.
>
> The sheafification enters as a locally injective and locally surjective map `η : F ⟶ G.val` to a
> sheaf of modules `G`, and the conclusion is adequacy of `G`. The hypothesis `htop` is the input
> of the source's proof; it is a theorem at `m = u`,
> `Stacks.Adequate.affineAdequateSheafTopology`, and open for a general `m`, and it is kept as a
> hypothesis here because the statement ranges over sheaves of modules of value universe
> `max u m`; see the module documentation.

```lean
public theorem isAdequate_sheafification
    {τ : CoveringTopology} {S : Scheme.{u}} (B : BigSite τ S)
    (htop : AffineAdequateSheafTopology.{u, m} B)
    (F : PresheafOfModules.{max u m} B.structureSheaf.obj)
    (G : SheafOfModules.{max u m} B.structureSheaf) (η : F ⟶ G.val)
    (hinj : PresheafOfModules.IsLocallyInjective B.topology η)
    (hsurj : PresheafOfModules.IsLocallySurjective B.topology η)
    (hF : ∀ (A : CommRingCat.{u}) (f : Spec A ⟶ S),
      schemeSizeBelow B.cutoff (Spec A) →
        AdequateFunctor.IsAdequate
          (AdequateFunctor.siteAlgebraInclusion A (schemeSizeBelow B.cutoff))
          (presheafAffineSectionFunctor B F A f)) :
    IsAdequate B G
```

**`Stacks.Adequate.isAdequate_sheafification'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/SheafificationTopology.lean, line 343](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/SheafificationTopology.lean#L343).

> **[Stacks, Tag 06VP].** Let `S` be a scheme and let `F` be a presheaf of `O`-modules on the
> big `τ`-site over `S`. If for *every* affine scheme `Spec A` over `S` belonging to the site the
> functor `F_{F, A}` is adequate, then the sheafification of `F` is an adequate `O`-module.
>
> The sheafification enters, as in `Stacks.Adequate.isAdequate_sheafification`, as a locally
> injective and locally surjective map `η : F ⟶ G.val` to a sheaf of modules `G`, which is the
> universal property of the associated sheaf; the conclusion is adequacy of `G`.
>
> Nothing is assumed beyond the source's own hypothesis: the input of the source's proof that was
> named `Stacks.Adequate.AffineAdequateSheafTopology` is discharged by
> `Stacks.Adequate.affineAdequateSheafTopology_of_moduleExtensionSheaf` applied to
> `Stacks.Adequate.affineModuleExtensionSheaf`, which is the proof of
> `Stacks.Adequate.affineAdequateSheafTopology` and is spelled out here because that declaration
> lives in a file importing this one. The attribute sits here rather than on
> `Stacks.Adequate.isAdequate_sheafification`, which is this statement under that input as an
> assumption and which the proof of this one calls.

```lean
public theorem isAdequate_sheafification'
    {τ' : CoveringTopology} {S' : Scheme.{u}} (B' : BigSite τ' S')
    (F : PresheafOfModules.{max u m} B'.structureSheaf.obj)
    (G : SheafOfModules.{max u m} B'.structureSheaf) (η : F ⟶ G.val)
    (hinj : PresheafOfModules.IsLocallyInjective B'.topology η)
    (hsurj : PresheafOfModules.IsLocallySurjective B'.topology η)
    (hF : ∀ (A : CommRingCat.{u}) (f : Spec A ⟶ S'),
      schemeSizeBelow B'.cutoff (Spec A) →
        AdequateFunctor.IsAdequate
          (AdequateFunctor.siteAlgebraInclusion A (schemeSizeBelow B'.cutoff))
          (presheafAffineSectionFunctor B' F A f)) :
    IsAdequate B' G
```

## Tag 06VQ, a lemma

[Tag 06VQ](https://stacks.math.columbia.edu/tag/06VQ) in the Stacks Project.

**`Stacks.Adequate.isAdequate_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/Abelian.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/Abelian.lean#L197). The attribute's comment: “(3)”.

> **[Stacks, Tag 06VQ] (3).** Let `0 → 𝓕₁ → 𝓕₂ → 𝓕₃ → 0` be a short exact sequence of
> `𝒪`-modules on the chosen big `τ`-site over `S`. If `𝓕₁` and `𝓕₃` are adequate, then `𝓕₂` is
> adequate.
>
> As in the source: over every affine scheme `Spec A` of the site the induced sequence of
> affine-section functors is short exact, because `H¹` of the adequate `𝓕₁` vanishes on affines
> ([Stacks, Tag 06VM] (3), through
> `Stacks.Adequate.shortExact_affineSections_of_isAdequate`); its outer terms are adequate
> ([Stacks, Tag 06VI]), so its middle term is adequate ([Stacks, Tag 06V8] on the algebras of the
> site, `Stacks.Adequate.affineAdequateExtensions`). The values of the modules lie in the universe
> of the site.

```lean
public theorem isAdequate_of_shortExact
    (T : ShortComplex (SheafOfModules.{u} B.structureSheaf)) (hT : T.ShortExact)
    (h₁ : IsAdequate B T.X₁) (h₃ : IsAdequate B T.X₃) :
    IsAdequate B T.X₂
```

**`Stacks.Adequate.abelian_adequate`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AbelianUnconditional.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AbelianUnconditional.lean#L125). The attribute's comment: “(1)”.

> **[Stacks, Tag 06VQ] (1).** The adequate `𝒪`-modules on the chosen big `τ`-site over `S`
> form an abelian category: they contain the zero sheaf and are closed under kernels, cokernels
> and finite products inside the abelian category of all sheaves of modules on the site.

```lean
public noncomputable def abelian_adequate : Abelian (adequate.{u, u} B).FullSubcategory
```

**`Stacks.Adequate.exact_ι_adequate`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AbelianUnconditional.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AbelianUnconditional.lean#L141). The attribute's comment: “(2)”.

> **[Stacks, Tag 06VQ] (2).** The inclusion of the adequate `𝒪`-modules into all `𝒪`-modules
> on the chosen big `τ`-site over `S` is exact: it preserves finite limits and finite colimits,
> kernels and cokernels of adequate modules being adequate.

```lean
public theorem exact_ι_adequate :
    PreservesFiniteLimits (adequate.{u, u} B).ι ∧ PreservesFiniteColimits (adequate.{u, u} B).ι
```

**`Stacks.Adequate.hasColimits_adequate`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AbelianUnconditional.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AbelianUnconditional.lean#L167). The attribute's comment: “(4)”.

> **[Stacks, Tag 06VQ] (4).** The category of adequate `𝒪`-modules on the chosen big
> `τ`-site over `S` has all small colimits, and the inclusion into all `𝒪`-modules preserves them:
> a colimit of adequate modules formed in all `𝒪`-modules is adequate.

```lean
public theorem hasColimits_adequate :
    HasColimitsOfSize.{u, u} (adequate.{u, u} B).FullSubcategory ∧
      PreservesColimitsOfSize.{u, u} (adequate.{u, u} B).ι
```

## Tag 06VR, a lemma

[Tag 06VR](https://stacks.math.columbia.edu/tag/06VR) in the Stacks Project.

**`Stacks.Adequate.isAdequate_directImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/DirectImageAdequacy.lean, line 681](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/DirectImageAdequacy.lean#L681). The attribute's comment: “`f_*𝓕` is adequate”.

> **[Stacks, Tag 06VR] for the direct image.** Let `f : T ⟶ S` be a quasi-compact and
> quasi-separated morphism of schemes and let `𝓕` be an adequate `𝒪`-module on a chosen big
> `τ`-site over `T`. Then the direct image `f_*𝓕` is an adequate `𝒪`-module on a chosen big
> `τ`-site over `S`.
>
> The direct image is restriction along the base-change functor `Φ` of the two sites, with the
> scalars transported along the first projection `ν` of the fibre squares
> (`Stacks.Adequate.directImage`); `hbc` says that `Φ` and `ν` are base change along `f`. Over an
> affine `Spec A` of the site over `S` the affine sections of `f_*𝓕` are `B ↦ 𝓕(T ×_S Spec B)`,
> the degree-zero case of `Stacks.Adequate.isAdequate_rightDerived_sectionsAlong_baseChangeFamily`.

```lean
public theorem isAdequate_directImage
    (F : SheafOfModules.{u} C.structureSheaf) (hF : IsAdequate C F)
    (hqc : QuasiCompact f) (hqs : QuasiSeparated f) (hbc : IsBaseChangeAlong B C f Φ ν) :
    IsAdequate B ((directImage.{u, u} B C Φ ν).obj F)
```

**`Stacks.Adequate.isAdequate_higherDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/DirectImageAdequacy.lean, line 742](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/DirectImageAdequacy.lean#L742). The attribute's comment: “`R^i f_*𝓕` is adequate for every `i`”.

> **[Stacks, Tag 06VR] for the higher direct images.** Let `f : T ⟶ S` be a quasi-compact and
> quasi-separated morphism of schemes and let `𝓕` be an adequate `𝒪`-module on a chosen big
> `τ`-site over `T`. Then every higher direct image `R^i f_*𝓕` is an adequate `𝒪`-module on a
> chosen big `τ`-site over `S`.
>
> `R^i f_*` is the `i`-th right derived functor of `Stacks.Adequate.directImage`, the source's
> definition. It is the sheafification of the presheaf `V ↦ H^i(V ×_S T, 𝓕)`
> (`Stacks.Adequate.higherDirectImageIsoSheafification`), whose affine sections over `Spec A` are
> `B ↦ H^i(T ×_S Spec B, 𝓕)` because evaluation is exact; these are adequate by
> `Stacks.Adequate.isAdequate_rightDerived_sectionsAlong_baseChangeFamily`, so the sheafification
> is adequate by [Stacks, Tag 06VP].
>
> The statement assumes nothing beyond the source. The typeclass arguments of
> `Stacks.Adequate.higherDirectImage` are supplied by proved instances on the two sites: the
> sheafification of abelian presheaves and the identification of its weak equivalences with the
> locally bijective maps are `Stacks.Adequate.BigSite.hasSheafify_addCommGrpCat` and
> `Stacks.Adequate.BigSite.wEqualsLocallyBijective_addCommGrpCat`, and the injectives in the
> category of sheaves of modules on the site over `T` are
> `Stacks.Adequate.BigSite.enoughInjectives_sheafOfModules`, which is [Stacks, Tag 01DU] on that
> site (sheaves of modules on it form a Grothendieck abelian category).

```lean
public theorem isAdequate_higherDirectImage
    (F : SheafOfModules.{u} C.structureSheaf) (hF : IsAdequate C F)
    (hqc : QuasiCompact f) (hqs : QuasiSeparated f) (hbc : IsBaseChangeAlong B C f Φ ν)
    (i : ℕ) :
    IsAdequate B ((higherDirectImage.{u, u} B C Φ ν i).obj F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 46.5, Tag 06VF](https://stacks.math.columbia.edu/tag/06VF)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
