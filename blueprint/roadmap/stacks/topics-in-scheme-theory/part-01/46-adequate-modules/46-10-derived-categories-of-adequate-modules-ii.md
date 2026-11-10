---
declaration: section
origin: cited
lean: AlgebraicGeometry.BigFppfOver.baseToZariskiRingedToposHom, Stacks.Adequate.BigSite.Coarsening.derivedAdequateCoarseningEquivalence, Stacks.Adequate.BigSite.derivedAdequateTopologyEquivalence, Stacks.Adequate.BigSite.Coarsening.derivedAdequateEquivalence, Stacks.Adequate.BigSite.derivedRestrictAdequate, Stacks.Adequate.BigSite.derivedAdequateAdjunction, Stacks.Adequate.BigSite.derivedQuasicoherentAdequateAdjunction, Stacks.Adequate.BigSite.derivedAdequateDirectImagePullbackIso
statement: formalized
proof: formalized
---

# 46.10 Derived categories of adequate modules, II

Section 46.10 of the Stacks Project, [Tag 070T](https://stacks.math.columbia.edu/tag/070T). 4 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 070U, an equation

[Tag 070U](https://stacks.math.columbia.edu/tag/070U) in the Stacks Project.

**`AlgebraicGeometry.BigFppfOver.baseToZariskiRingedToposHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/BaseRingedSite.lean, line 366](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/BaseRingedSite.lean#L366).

> The morphism of ringed sites
> `f : ((Sch/S)_τ, 𝒪) ⟶ (S_Zar, 𝒪_S)`, for each `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`:
> the continuous inclusion of the small Zariski site of `S` into the big site, with structure map
> the identification of the sections of `𝒪_S` over an open with the functions on it.

```lean
public noncomputable def baseToZariskiRingedToposHom (τ : SiteKind) :
    RingedToposSiteHom (baseRingedTopos B S hS τ) S.zariskiRingedTopos
```

## Tag 070V, a remark

[Tag 070V](https://stacks.math.columbia.edu/tag/070V) in the Stacks Project.

**`Stacks.Adequate.BigSite.Coarsening.derivedAdequateCoarseningEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/DerivedTopologyIndependence.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/DerivedTopologyIndependence.lean#L249). The attribute's comment: “the canonical equivalence of `D_Adeq(𝒪_τ)` and `D_Adeq(𝒪_τ')`, for a coarsening of a chosen big site, at any models of the two derived categories”.

> **[Stacks, Tag 070V].** Let `S` be a scheme and let `τ` and `τ'` be two of the five
> topologies `Zar`, `étale`, `smooth`, `syntomic`, `fppf`, with `τ` stronger than `τ'`, and denote
> `𝒪_τ` and `𝒪_τ'` the structure sheaf `𝒪` viewed as a sheaf on the big `τ`-site, resp. the big
> `τ'`-site, over `S`. Then `D_Adeq(𝒪_τ)` and `D_Adeq(𝒪_τ')` are canonically equivalent.
>
> The equivalence is [Stacks, Tag 07A8] for the category of the site, the class of adequate
> `𝒪_τ`-modules and the affine objects of the site
> (`Stacks.Cohomology.CompareTopologies.derivedEquivalenceImageOfLEOfEssentiallySmall`). Its
> assumption (1) is `Stacks.Adequate.BigSite.Coarsening.adequateIsFineSheaf`, (2) is
> `Stacks.Adequate.adequate_isWeakSerreClass`, (3) is
> `Stacks.Adequate.BigSite.Coarsening.affineCoarseCovering` and (4) is
> `Stacks.Adequate.BigSite.isZero_rightDerived_sections_of_isAdequate`, [Stacks, Tag 06VM] (3).
> Assumption (1) also identifies the image class of the adequate `𝒪_τ`-modules with the adequate
> `𝒪_τ'`-modules (`Stacks.Adequate.BigSite.Coarsening.adequate_site_eq_imageOfLE`).

```lean
def derivedAdequateCoarseningEquivalence
    [HasDerivedCategory.{d} (SheafOfModules.{u} B.structureSheaf)]
    [HasDerivedCategory.{d'} (SheafOfModules.{u} c.site.structureSheaf)] :
    (BigSite.derivedAdequate.{u, u, d} B).FullSubcategory ≌
      (BigSite.derivedAdequate.{u, u, d'} c.site).FullSubcategory
```

**`Stacks.Adequate.BigSite.derivedAdequateTopologyEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/DerivedTopologyIndependence.lean, line 312](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/DerivedTopologyIndependence.lean#L312). The attribute's comment: “`D_Adeq(𝒪_τ) ≌ D_Adeq(𝒪_τ')` for any two of the five topologies, for big sites built on the same category of schemes over `S`, at any models of the two derived categories”.

> **[Stacks, Tag 070V].** Let `S` be a scheme and let `τ, τ'` be two of the five topologies
> `Zar`, `étale`, `smooth`, `syntomic`, `fppf`, and denote `𝒪_τ`, resp. `𝒪_τ'`, the structure sheaf
> `𝒪` viewed as a sheaf on the big site `(Sch/S)_τ`, resp. `(Sch/S)_τ'`, the two big sites being
> built on the same category of schemes over `S` (their cutoffs agree). Then `D_Adeq(𝒪_τ)` and
> `D_Adeq(𝒪_τ')` are canonically equivalent.
>
> The five topologies are linearly ordered, `Zar ≺ étale ≺ smooth ≺ syntomic ≺ fppf`; if `τ` is
> finer than `τ'` this is `Stacks.Adequate.BigSite.derivedAdequateEquivalenceOfIsFiner`, and
> otherwise `τ'` is finer than `τ` and it is the inverse of that equivalence with the roles of the
> two sites exchanged. Both derived categories are taken at arbitrary models.

```lean
def BigSite.derivedAdequateTopologyEquivalence (B : BigSite τ S) (B' : BigSite τ' S)
    (hcut : B'.cutoff = B.cutoff)
    [HasDerivedCategory.{d} (SheafOfModules.{u} B.structureSheaf)]
    [HasDerivedCategory.{d'} (SheafOfModules.{u} B'.structureSheaf)] :
    (BigSite.derivedAdequate.{u, u, d} B).FullSubcategory ≌
      (BigSite.derivedAdequate.{u, u, d'} B').FullSubcategory
```

**`Stacks.Adequate.BigSite.Coarsening.derivedAdequateEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/TopologyIndependence.lean, line 353](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/TopologyIndependence.lean#L353). The attribute's comment: “the canonical isomorphism of `D_Adeq(𝒪_τ)` and `D_Adeq(𝒪_τ')` as an equivalence of categories, for a coarsening of a chosen big site; the inputs it takes, and the one proved here, are listed in the docstring”.

> **[Stacks, Tag 070V].** Let `S` be a scheme and let `τ` and `τ'` be two of the five
> topologies `Zar`, `étale`, `smooth`, `syntomic`, `fppf`, with `τ` stronger than `τ'`, and
> denote `𝒪_τ` and `𝒪_τ'` the structure sheaf `𝒪` viewed as a sheaf on the big `τ`-site, resp.
> the big `τ'`-site, over `S`. Then `D_Adeq(𝒪_τ)` and `D_Adeq(𝒪_τ')` are canonically isomorphic.
>
> The equivalence is the second conclusion of [Stacks, Tag 07A8] applied to the class of adequate
> `𝒪_τ`-modules and to the collection of affine objects of the site. Its assumption (2) is
> `Stacks.Adequate.adequate_isWeakSerreClass` and its assumption (4) is
> `Stacks.Adequate.BigSite.isZero_rightDerived_sections_of_isAdequate`, which is
> [Stacks, Tag 06VM] (3) and carries no hypothesis; assumptions (1) and (3) are `hfine` and
> `hcover`.
> That the two sides are the derived categories of the *adequate* modules for each topology,
> rather than of the adequate modules for `τ` and their image under `ε_*`, is
> `Stacks.Adequate.BigSite.Coarsening.adequate_site_eq_imageOfLE`.
>
> The inputs this declaration takes are: `comparison`, the second conclusion of [Stacks, Tag 07A8]
> in the generality of its source, which this library does not prove; `AdequateIsFineSheaf` and
> `AffineCoarseCovering`, assumptions (1) and (3) of 07A8 for the adequate modules and the affine
> objects. Assumption (2) is discharged outright by [Stacks, Tag 06VQ], and assumption (4) by
> [Stacks, Tag 06VM] (3). The modules have values in the universe of the site, the universe at
> which [Stacks, Tag 06VQ] is available.

```lean
public def derivedAdequateEquivalence
    [HasSheafify c.topology AddCommGrpCat.{u}]
    [c.topology.WEqualsLocallyBijective AddCommGrpCat.{u}]
    [HasDerivedCategory.{d} (SheafOfModules.{u} B.structureSheaf)]
    [HasDerivedCategory.{d} (SheafOfModules.{u} c.site.structureSheaf)]
    (comparison : ∀ {C : Type (u + 1)} [Category.{u} C] {J J' : GrothendieckTopology C}
      (h : J' ≤ J) (R : Sheaf J RingCat.{u})
      [HasSheafify J AddCommGrpCat.{u}]
      [J.WEqualsLocallyBijective AddCommGrpCat.{u}]
      [HasSheafify J' AddCommGrpCat.{u}]
      [J'.WEqualsLocallyBijective AddCommGrpCat.{u}]
      [EnoughInjectives (Sheaf J AddCommGrpCat.{u})]
      [HasDerivedCategory.{d} (SheafOfModules.{u} R)]
      [HasDerivedCategory.{d} (SheafOfModules.{u} (R.ofLE h))]
      (A : ObjectProperty (SheafOfModules.{u} R)) (ℬ : Set C), A.IsWeakSerreClass →
        (∀ U : C, ∃ 𝒰 : PreZeroHypercover.{u + 1} U, 𝒰.sieve₀ ∈ J' U ∧ ∀ i, ℬ (𝒰.X i)) →
        (∀ U ∈ ℬ, ∀ p : ℕ, 0 < p → ∀ F, A F →
          IsZero ((((sheafSections J AddCommGrpCat.{u}).obj (op U)).rightDerived p).obj
            ((SheafOfModules.toSheaf R).obj F))) →
        ((DerivedCategoryB.derivedCategoryB A).FullSubcategory ≌
          (DerivedCategoryB.derivedCategoryB
            (Stacks.Cohomology.CompareTopologies.imageOfLE.{u + 1, u, u, u} h R
              A)).FullSubcategory))
    (hfine : AdequateIsFineSheaf.{u, u} c) (hcover : AffineCoarseCovering.{u} c) :
    (BigSite.derivedAdequate.{u, u, d} B).FullSubcategory ≌
      (BigSite.derivedAdequate.{u, u, d} c.site).FullSubcategory
```

## Tag 070W, a remark

[Tag 070W](https://stacks.math.columbia.edu/tag/070W) in the Stacks Project.

**`Stacks.Adequate.BigSite.derivedRestrictAdequate`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/DerivedRestriction.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/DerivedRestriction.lean#L293). The attribute's comment: “the assertion that Rf\_* carries D\_Adeq(𝒪) into D\_QCoh(S), in the source's own form Rf\_* = f\_* for the Zariski restriction of the morphism of Tag 070U, with right exactness of that restriction an instance argument. Lf^*, adjointness and Rf\_* Lf^* ≅ id are covered elsewhere”.

> **[Stacks, Tag 070W], the pushforward landing in the source's own form `Rf_* = f_*`.**
> Restriction to the small Zariski site of `S` along the morphism of [Stacks, Tag 070U], assumed
> right exact, induces a functor `D_Adeq(𝒪) ⥤ D_QCoh(S)` on the chosen big fppf site over `S`;
> on modules it lands in the quasi-coherent sheaves by [Stacks, Tag 06VM] (1).

```lean
public def BigSite.derivedRestrictAdequate :
    (BigSite.derivedAdequate.{u, u, d} (BigSite.ofBigFppfSite B S hS)).FullSubcategory ⥤
      (DerivedCategoryB.derivedCategoryB
        (SheafOfModules.isQuasicoherent S.ringCatSheaf)).FullSubcategory
```

**`Stacks.Adequate.BigSite.derivedAdequateAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/DerivedRestriction.lean, line 366](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/DerivedRestriction.lean#L366). The attribute's comment: “the adjointness assertion only, for the subcategories D\_Adeq(O) and D\_QCoh(S); the ambient adjunction and the two landing assertions are inputs, listed in the docstring”.

> **[Stacks, Tag 070W], the adjointness assertion.** Given the ambient derived adjunction
> `Lf^* ⊣ Rf_*` on all `𝒪`-modules and the two landing assertions, the restricted functors
> `Lf^* : D_QCoh(S) ⥤ D_Adeq(𝒪)` and `Rf_* : D_Adeq(𝒪) ⥤ D_QCoh(S)` are adjoint.
>
> The inputs are the ambient derived adjunction `adj : L ⊣ R` on all modules and both landing
> assertions — `hL`, that `Lf^*` carries `D_QCoh(S)` into `D_Adeq(𝒪)`, and `hR`, that `Rf_*`
> carries `D_Adeq(𝒪)` into `D_QCoh(S)`. Each carries its own content and none is proved here: the
> ambient adjunction of [Stacks, Tag 07A6] is not available for the morphism of [Stacks, Tag 070U]
> at the universes in which that morphism is stated. The isomorphism `Rf_* Lf^* ≅ id` is a
> separate declaration.

```lean
public def BigSite.derivedAdequateAdjunction (adj : L ⊣ R) :
    BigSite.derivedAdequatePullback B L hL ⊣
      BigSite.derivedAdequatePushforward B R hR
```

**`Stacks.Adequate.BigSite.derivedQuasicoherentAdequateAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/DerivedZariskiQuasicoherent.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/DerivedZariskiQuasicoherent.lean#L97). The attribute's comment: “the adjunction Lf^* ⊣ Rf\_* between D\_QCoh(S) and D\_Adeq(O), for the derived functors of the morphism of Tag 070U on a chosen big site, with no hypothesis”.

> **[Stacks, Tag 070W], the adjunction.** The morphism `f` of [Stacks, Tag 070U] induces
> adjoint functors `Lf^* : D_QCoh(S) ⥤ D_Adeq(𝒪)` and `Rf_* : D_Adeq(𝒪) ⥤ D_QCoh(S)`: the total
> derived functors of [Stacks, Tag 07A6] preserve the two subcategories, and their adjunction
> restricts.

```lean
def BigSite.derivedQuasicoherentAdequateAdjunction :
    B.derivedQuasicoherentPullback ⊣ B.derivedAdequateDirectImage
```

**`Stacks.Adequate.BigSite.derivedAdequateDirectImagePullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/DerivedZariskiQuasicoherent.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/DerivedZariskiQuasicoherent.lean#L106). The attribute's comment: “Rf\_* Lf^* ≅ id on D\_QCoh(S), for the derived functors of the morphism of Tag 070U on a chosen big site”.

> **[Stacks, Tag 070W], `Rf_* Lf^* ≅ id_{D_QCoh(S)}`.** The unit of the derived adjunction
> is invertible at every complex with quasi-coherent cohomology.

```lean
def BigSite.derivedAdequateDirectImagePullbackIso :
    B.derivedQuasicoherentPullback ⋙ B.derivedAdequateDirectImage ≅ 𝟭 _
```

## Tag 070X, a remark

[Tag 070X](https://stacks.math.columbia.edu/tag/070X) in the Stacks Project.

**`Stacks.Adequate.BigSite.isLocalization_derivedAdequatePushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/DerivedQuotient.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/DerivedQuotient.lean#L223). The attribute's comment: “the equivalence `D_Adeq(𝒪)/D_𝒞(𝒪) ⟶ D_QCoh(S)`, with the quotient described as the localization at the morphisms `Rf_*` inverts; the description by the subcategory `D_𝒞(𝒪) = ker Rf_*` is the companion `BigSite.isLocalization_trW_kernel_derivedAdequatePushforward`. The ambient derived adjunction `adj`, both landing assertions `hL` and `hR`, and the invertibility `hunit` of the ambient unit on `D_QCoh(S)` are hypotheses, exactly as for the Tag 070W declarations this consumes; none of them is proved here”.

> **[Stacks, Tag 070X].** `Rf_* : D_Adeq(𝒪) ⥤ D_QCoh(S)` is a localization functor for the
> morphisms of `D_Adeq(𝒪)` that it carries to isomorphisms of `D_QCoh(S)`, so that
> `D_Adeq(𝒪)/D_𝒞(𝒪) ⟶ D_QCoh(S)` is an equivalence.

```lean
public theorem BigSite.isLocalization_derivedAdequatePushforward :
    (BigSite.derivedAdequatePushforward B R hR).IsLocalization
      ((MorphismProperty.isomorphisms _).inverseImage
        (BigSite.derivedAdequatePushforward B R hR))
```

**`Stacks.Adequate.BigSite.derivedAdequateQuotientEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/DerivedQuotient.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/DerivedQuotient.lean#L236). The attribute's comment: “the equivalence of categories itself, for the quotient described as the localization at the morphisms `Rf_*` inverts; the hypotheses are those of `BigSite.isLocalization_derivedAdequatePushforward`”.

> **[Stacks, Tag 070X], the equivalence.** The localization of `D_Adeq(𝒪)` at the morphisms
> inverted by `Rf_*` is equivalent to `D_QCoh(S)`.

```lean
public def BigSite.derivedAdequateQuotientEquivalence :
    ((MorphismProperty.isomorphisms _).inverseImage
        (BigSite.derivedAdequatePushforward B R hR)).Localization ≌
      (DerivedCategoryB.derivedCategoryB
        (SheafOfModules.isQuasicoherent S.ringCatSheaf)).FullSubcategory
```

**`Stacks.Adequate.BigSite.isLocalization_trW_kernel_derivedAdequatePushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/DerivedQuotient.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/DerivedQuotient.lean#L275). The attribute's comment: “the equivalence `D_Adeq(𝒪)/D_𝒞(𝒪) ⟶ D_QCoh(S)` with the quotient taken, as in the source, at the morphisms whose cone lies in the subcategory `D_𝒞(𝒪)`, realised as the kernel of `Rf_*`, which is the source's own description of it. Beyond the hypotheses of `BigSite.isLocalization_derivedAdequatePushforward`, the pretriangulated structures of the two subcategories and the triangulatedness of the restricted `Rf_*` are instance arguments; the library does not construct them for the restricted functors”.

> **[Stacks, Tag 070X] in the source's own form.** `Rf_* : D_Adeq(𝒪) ⥤ D_QCoh(S)` is a
> localization functor for the morphisms whose cone lies in `D_𝒞(𝒪)`, the kernel of `Rf_*`.

```lean
public theorem BigSite.isLocalization_trW_kernel_derivedAdequatePushforward :
    (BigSite.derivedAdequatePushforward B R hR).IsLocalization
      (ObjectProperty.trW (BigSite.derivedAdequatePushforward B R hR).kernel)
```

**`Stacks.Adequate.BigSite.derivedParasiticQuotientEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/DerivedQuotient.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/DerivedQuotient.lean#L289). The attribute's comment: “the equivalence of categories itself, in the source's own form: the quotient of `D_Adeq(𝒪)` by `D_𝒞(𝒪) = ker Rf_*`. The hypotheses are those of `BigSite.isLocalization_trW_kernel_derivedAdequatePushforward`”.

> **[Stacks, Tag 070X], the equivalence `D_Adeq(𝒪)/D_𝒞(𝒪) ≌ D_QCoh(S)`.** The quotient of
> `D_Adeq(𝒪)` by the complexes with parasitic cohomology, the kernel of `Rf_*`, is equivalent to
> `D_QCoh(S)`.

```lean
public def BigSite.derivedParasiticQuotientEquivalence :
    (ObjectProperty.trW
        (BigSite.derivedAdequatePushforward B R hR).kernel).Localization ≌
      (DerivedCategoryB.derivedCategoryB
        (SheafOfModules.isQuasicoherent S.ringCatSheaf)).FullSubcategory
```

**`Stacks.Adequate.BigSite.isLocalization_trW_derivedParasitic_derivedAdequateDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/DerivedQuotientUnconditional.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/DerivedQuotientUnconditional.lean#L218). The attribute's comment: “the equivalence D\_Adeq(O)/D\_C(O) -> D\_QCoh(S) induced by Rf\_*, with the quotient the Verdier quotient by the complexes with parasitic adequate cohomology, for the derived functors of the morphism of Tag 070U on a chosen big site and each of the five topologies”.

> **[Stacks, Tag 070X].** Let `S` be a scheme and `f : ((Sch/S)_τ, 𝒪) ⟶ (S_Zar, 𝒪_S)` the
> morphism of [Stacks, Tag 070U], for a chosen big site and any of the five topologies. The derived
> direct image `Rf_* : D_Adeq(𝒪) ⥤ D_QCoh(S)` is the Verdier quotient of `D_Adeq(𝒪)` by
> `D_𝒞(𝒪)`, the complexes whose cohomology modules are parasitic adequate: it is a localization
> functor for the morphisms whose cone lies in `D_𝒞(𝒪)`, so that it induces an equivalence
> `D_Adeq(𝒪)/D_𝒞(𝒪) ⟶ D_QCoh(S)`.

```lean
public theorem BigSite.isLocalization_trW_derivedParasitic_derivedAdequateDirectImage :
    B.derivedAdequateDirectImage.IsLocalization
      ((BigSite.derivedParasitic B).inverseImage
        (DerivedCategoryB.derivedCategoryB (adequate.{u, u} B : ObjectProperty (SheafOfModules.{u}
          (Stacks.SheafOfModules.Tensor.ringSheaf B.ringedSite.toRingedTopos.O)))).ι).trW
```

**`Stacks.Adequate.BigSite.derivedAdequateParasiticQuotientEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/DerivedQuotientUnconditional.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/DerivedQuotientUnconditional.lean#L237). The attribute's comment: “the equivalence of categories D\_Adeq(O)/D\_C(O) ≌ D\_QCoh(S) itself, for the derived functors of the morphism of Tag 070U on a chosen big site and each of the five topologies”.

> **[Stacks, Tag 070X], the equivalence `D_Adeq(𝒪)/D_𝒞(𝒪) ≌ D_QCoh(S)`.** The Verdier
> quotient of `D_Adeq(𝒪)` by the complexes with parasitic adequate cohomology is equivalent to
> `D_QCoh(S)`, by the functor induced by `Rf_*`.

```lean
public def BigSite.derivedAdequateParasiticQuotientEquivalence :
    ((BigSite.derivedParasitic B).inverseImage
        (DerivedCategoryB.derivedCategoryB (adequate.{u, u} B : ObjectProperty (SheafOfModules.{u}
          (Stacks.SheafOfModules.Tensor.ringSheaf
            B.ringedSite.toRingedTopos.O)))).ι).trW.Localization ≌
      (DerivedCategoryB.derivedCategoryB (SheafOfModules.isQuasicoherent S.ringCatSheaf :
        ObjectProperty (SheafOfModules.{u}
          (Stacks.SheafOfModules.Tensor.ringSheaf
            S.zariskiRingedSite.toRingedTopos.O)))).FullSubcategory
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 46.10, Tag 070T](https://stacks.math.columbia.edu/tag/070T)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
