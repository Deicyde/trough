---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.restrictModuleToSmallEtale, AlgebraicGeometry.Stack.IsLocallyQuasicoherent, AlgebraicGeometry.Stack.isSheaf_etale_of_isQuasicoherent, AlgebraicGeometry.Stack.isQuasicoherentFppf_iff_isLocallyQuasicoherent_and_isIso_sheafifiedRestrictComparison, AlgebraicGeometry.Stack.isLocallyQuasicoherent_modulePullback, AlgebraicGeometry.Stack.locallyQuasicoherentModules_colimits, AlgebraicGeometry.Stack.locallyQuasicoherentModules_abelian, AlgebraicGeometry.Stack.isLocallyQuasicoherent_twoOutOfThree
statement: formalized
proof: formalized
---

# 96.12 Locally quasi-coherent modules

Section 96.12 of the Stacks Project, [Tag 0GQB](https://stacks.math.columbia.edu/tag/0GQB). 5 tags here are carried by 20 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06WJ, a definition

[Tag 06WJ](https://stacks.math.columbia.edu/tag/06WJ) in the Stacks Project.

**`AlgebraicGeometry.Stack.restrictModuleToSmallEtale`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LocallyQuasicoherent.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LocallyQuasicoherent.lean#L113). The attribute's comment: “the restriction to the small étale site”.

> **Stacks 06WJ.** The restriction `x^*F|_{U_ét}` at an object `x` of a presheaf of modules on
> `𝒳` to the small étale site of the scheme `U` below `x`: restrict the underlying abelian
> presheaf as in Stacks 06W1, then transport the scalars through
> `AlgebraicGeometry.Stack.localStructurePresheafIso`.

```lean
noncomputable def restrictModuleToSmallEtale {𝒳 : Type v} [Category.{w} 𝒳]
    (p : 𝒳 ⥤ BigFppfOver B S hS) (hp : p.IsFiberedInGroupoids) (x : 𝒳)
    (τ : GrothendieckTopology B.Schemes) (hτ : τ ≤ B.topology)
    (F : PresheafOfModules.{m} (ringStructureSheafCore B S hS p hp τ hτ).obj) :
    PresheafOfModules.{m}
      (SmallEtale.structureSheaf E (p.obj x).left.1 (contains_base B E h S hS p x)).obj
```

**`AlgebraicGeometry.Stack.IsLocallyQuasicoherent`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LocallyQuasicoherent.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LocallyQuasicoherent.lean#L146). The attribute's comment: “local quasi-coherence”.

> **Stacks 06WJ.** A presheaf of modules over the structure sheaf of a category fibred in
> groupoids is *locally quasi-coherent* when it is a sheaf for the étale topology and, at every
> object `x` of `𝒳`, its restriction to the small étale site of the scheme below `x` is a
> quasi-coherent sheaf of modules.
>
> The source calls the notation nonstandard; it is the condition under which the module is
> determined by quasi-coherent modules on the small étale sites of the objects.

```lean
noncomputable abbrev IsLocallyQuasicoherent {𝒳 : Type v} [Category.{w} 𝒳]
    (p : 𝒳 ⥤ BigFppfOver B S hS) (hp : p.IsFiberedInGroupoids)
    (F : PresheafOfModules.{m}
      (ringStructureSheafCore B S hS p hp (etaleTopology B) (etaleTopology_le_topology B)).obj) :
    Prop
```

## Tag 06WK, a lemma

[Tag 06WK](https://stacks.math.columbia.edu/tag/06WK) in the Stacks Project.

**`AlgebraicGeometry.Stack.isSheaf_etale_of_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentEtaleSheafClause.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentEtaleSheafClause.lean#L124). The attribute's comment: “the étale sheaf condition, which is the first conjunct of clause (1), in the forward direction”.

> **Stacks 06WK.** A quasi-coherent module on a category fibred in groupoids is a sheaf for the
> inherited étale topology.
>
> This is the first conjunct of clause (1) of the source, local quasi-coherence being the étale
> sheaf condition together with quasi-coherence of the restrictions to the small étale sites, and
> it is the first step of the source's proof: quasi-coherence of `F` in the sense of Stacks 06WG
> asserts in particular that `F` is a sheaf for the inherited fppf topology, and the inherited
> étale topology is coarser.

```lean
theorem isSheaf_etale_of_isQuasicoherent {𝒳 : Type v} [Category.{w} 𝒳]
    (p : 𝒳 ⥤ BigFppfOver B S hS) (hp : p.IsFiberedInGroupoids)
    (F : PresheafOfModules.{m} (ringStructureSheafCore B S hS p hp
      (etaleTopology B) (etaleTopology_le_topology B)).obj)
    (hF : ∃ h : Presheaf.IsSheaf (associatedTopology B S hS p B.topology) F.presheaf,
      SheafOfModules.IsQuasicoherentOnSite
        (⟨F, h⟩ : SheafOfModules.{m}
          (ringStructureSheafCore B S hS p hp B.topology le_rfl))) :
    Presheaf.IsSheaf (associatedTopology B S hS p (etaleTopology B)) F.presheaf
```

**`AlgebraicGeometry.Stack.isQuasicoherentFppf_iff_isLocallyQuasicoherent_and_isIso_sheafifiedRestrictComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentIffComparisonIso.lean, line 396](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentIffComparisonIso.lean#L396).

> **Stacks 06WK.** A presheaf of modules `F` on a category fibred in groupoids `𝒳` over
> `(Sch/S)_{fppf}` is quasi-coherent (Stacks 06WG) if and only if
>
> 1. `F` is locally quasi-coherent (Stacks 06WJ), and
> 2. for every arrow `φ : x ⟶ y` of `𝒳` the comparison map
>    `c_φ : f_{small}^*(F|_{V_ét}) ⟶ F|_{U_ét}` of Stacks 06WC, read on sheaves of modules on the
>    small étale site of the scheme `U` below `x`, is an isomorphism.

```lean
theorem isQuasicoherentFppf_iff_isLocallyQuasicoherent_and_isIso_sheafifiedRestrictComparison
    (F : PresheafOfModules.{u} (ringStructureSheafCore B S hS p hp (etaleTopology B)
      (etaleTopology_le_topology B)).obj) :
    IsQuasicoherentFppf B S hS p hp F ↔
      ∃ hlqc : IsLocallyQuasicoherent B E h S hS p hp F,
        ∀ {x y : 𝒳} (φ : x ⟶ y),
          IsIso (sheafifiedRestrictComparison B E h S hS p hp F φ (hlqc.2 x).1)
```

## Tag 06WL, a lemma

[Tag 06WL](https://stacks.math.columbia.edu/tag/06WL) in the Stacks Project.

**`AlgebraicGeometry.Stack.isLocallyQuasicoherent_modulePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LocallyQuasicoherentPullback.lean, line 296](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LocallyQuasicoherentPullback.lean#L296).

> The inverse image of presheaves of modules along a 1-morphism of categories fibred in
> groupoids over the big fppf category of `S` preserves local quasi-coherence.

```lean
theorem isLocallyQuasicoherent_modulePullback
    (G : PresheafOfModules.{m} (ringStructureSheafCore B S hS q hq (etaleTopology B)
      (etaleTopology_le_topology B)).obj)
    (hG : IsLocallyQuasicoherent B E h S hS q hq G) :
    IsLocallyQuasicoherent B E h S hS (f ⋙ q) hp
      ((modulePresheafPullback.{u, v, w, v', w', m} B S hS q hq f hp).obj G)
```

## Tag 06WM, a lemma

[Tag 06WM](https://stacks.math.columbia.edu/tag/06WM) in the Stacks Project.

**`AlgebraicGeometry.Stack.locallyQuasicoherentModules_colimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LocallyQuasicoherentClosure.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LocallyQuasicoherentClosure.lean#L89). The attribute's comment: “(1): LQCoh(𝒪_𝒳) has colimits and they agree with colimits in Mod(𝒳_ét, 𝒪_𝒳)”.

> **Stacks 06WM (1).** The category `LQCoh(𝒪_𝒳)` of locally quasi-coherent modules has
> colimits, and they agree with colimits in `Mod(𝒳_ét, 𝒪_𝒳)`: local quasi-coherence is closed under
> colimits computed in `Mod(𝒳_ét, 𝒪_𝒳)`, the full subcategory therefore has them, and its
> inclusion preserves them.

```lean
theorem locallyQuasicoherentModules_colimits :
    (∀ (K : Type u) [Category.{u} K],
      (isLocallyQuasicoherent.{u, v, w, u} B E h S hS p hp).IsClosedUnderColimitsOfShape K) ∧
      HasColimitsOfSize.{u, u} (locallyQuasicoherentModules.{u, v, w, u} B E h S hS p hp) ∧
      PreservesColimitsOfSize.{u, u} (isLocallyQuasicoherent.{u, v, w, u} B E h S hS p hp).ι
```

**`AlgebraicGeometry.Stack.locallyQuasicoherentModules_abelian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LocallyQuasicoherentClosure.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LocallyQuasicoherentClosure.lean#L104). The attribute's comment: “(2): LQCoh(𝒪_𝒳) is abelian with kernels and cokernels computed in Mod(𝒳_ét, 𝒪_𝒳), i.e. the inclusion is exact”.

> **Stacks 06WM (2).** The category `LQCoh(𝒪_𝒳)` is abelian, with kernels and cokernels
> computed in `Mod(𝒳_ét, 𝒪_𝒳)`: local quasi-coherence is closed under kernels and cokernels, so
> the full subcategory is abelian and its inclusion into `Mod(𝒳_ét, 𝒪_𝒳)` is exact.

```lean
theorem locallyQuasicoherentModules_abelian :
    (isLocallyQuasicoherent.{u, v, w, u} B E h S hS p hp).IsClosedUnderKernels ∧
      (isLocallyQuasicoherent.{u, v, w, u} B E h S hS p hp).IsClosedUnderCokernels ∧
      Nonempty (Abelian (locallyQuasicoherentModules.{u, v, w, u} B E h S hS p hp)) ∧
      PreservesFiniteLimits (isLocallyQuasicoherent.{u, v, w, u} B E h S hS p hp).ι ∧
      PreservesFiniteColimits (isLocallyQuasicoherent.{u, v, w, u} B E h S hS p hp).ι
```

**`AlgebraicGeometry.Stack.isLocallyQuasicoherent_twoOutOfThree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LocallyQuasicoherentClosure.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LocallyQuasicoherentClosure.lean#L137). The attribute's comment: “(3): in a short exact sequence of Mod(𝒳_ét, 𝒪_𝒳), if two out of three terms are locally quasi-coherent so is the third”.

> **Stacks 06WM (3).** In a short exact sequence `0 → 𝓕₁ → 𝓕₂ → 𝓕₃ → 0` of
> `Mod(𝒳_ét, 𝒪_𝒳)`, if two of the three terms are locally quasi-coherent then so is the third.
> A cokernel and a kernel of a morphism of locally quasi-coherent modules are locally
> quasi-coherent by Stacks 06WM (2); for the middle term the restriction to the small étale site of
> the scheme below an object is exact, so it carries the sequence to a short exact sequence there,
> and an extension of quasi-coherent modules on a small étale site is quasi-coherent (Descent,
> Lemma 0GNB).

```lean
theorem isLocallyQuasicoherent_twoOutOfThree
    (T : ShortComplex (SheafOfModules.{u} (ringStructureSheafCore B S hS p hp (etaleTopology B)
      (etaleTopology_le_topology B))))
    (hT : T.ShortExact) :
    (IsLocallyQuasicoherent B E h S hS p hp T.X₁.val →
        IsLocallyQuasicoherent B E h S hS p hp T.X₂.val →
          IsLocallyQuasicoherent B E h S hS p hp T.X₃.val) ∧
      (IsLocallyQuasicoherent B E h S hS p hp T.X₂.val →
        IsLocallyQuasicoherent B E h S hS p hp T.X₃.val →
          IsLocallyQuasicoherent B E h S hS p hp T.X₁.val) ∧
      (IsLocallyQuasicoherent B E h S hS p hp T.X₁.val →
        IsLocallyQuasicoherent B E h S hS p hp T.X₃.val →
          IsLocallyQuasicoherent B E h S hS p hp T.X₂.val)
```

**`AlgebraicGeometry.Stack.isLocallyQuasicoherent_etaleInternalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LocallyQuasicoherentInternalHom.lean, line 294](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LocallyQuasicoherentInternalHom.lean#L294). The attribute's comment: “(5): for F, G in LQCoh(𝒪_𝒳) with F of finite presentation on 𝒳_ét, the internal Hom 𝓗om_{𝒪_𝒳}(F, G) of Mod(𝒳_ét, 𝒪_𝒳) is locally quasi-coherent”.

> **Stacks 06WM, clause (5).** Let `p : 𝒳 ⥤ (Sch/S)_{fppf}` be a category fibred in groupoids
> and let `F`, `G` be locally quasi-coherent sheaves of `𝒪_𝒳`-modules on `𝒳_étale`, with `F` of
> finite presentation on `𝒳_étale`. Then the internal Hom `𝓗om_{𝒪_𝒳}(F, G)` of
> `Mod(𝒳_étale, 𝒪_𝒳)` is locally quasi-coherent.
>
> Local quasi-coherence is étale-local on the object
> (`AlgebraicGeometry.Stack.isQuasicoherentOnSite_restrictModuleToSmallEtale_of_etaleCover`), and
> every covering of an object of `𝒳_étale` is refined by arrows lying over a jointly surjective
> family of étale morphisms
> (`AlgebraicGeometry.Stack.exists_etaleCovering_le_of_mem_associatedTopology`);
> at the members of such a refinement of a covering on which `F` is finitely presented the claim is
> `AlgebraicGeometry.Stack.isQuasicoherentOnSite_restrictSheafToSmallEtale_etaleInternalHom`. The
> hypothesis that `F` is locally quasi-coherent is part of the source's statement; the argument does
> not use it.

```lean
theorem isLocallyQuasicoherent_etaleInternalHom
    (F G : SheafOfModules.{u}
      (ringStructureSheafCore B S hS p hp (etaleTopology B) (etaleTopology_le_topology B)))
    (_hF : IsLocallyQuasicoherent B E h S hS p hp F.val)
    (hG : IsLocallyQuasicoherent B E h S hS p hp G.val)
    (hfp : F.IsFinitePresentationOnSite) :
    IsLocallyQuasicoherent B E h S hS p hp (etaleInternalHom B S hS p hp F G).val
```

**`AlgebraicGeometry.Stack.isLocallyQuasicoherent_tensorSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LocallyQuasicoherentTensor.lean, line 689](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LocallyQuasicoherentTensor.lean#L689). The attribute's comment: “(4): the tensor product in Mod(𝒳_ét, 𝒪_𝒳) of two locally quasi-coherent modules is locally quasi-coherent”.

> **Stacks 06WM**, clause (4). The tensor product in `Mod(𝒳_ét, 𝒪_𝒳)` of two locally
> quasi-coherent sheaves of modules on a category fibred in groupoids is locally quasi-coherent.
>
> The tensor product is the sheafification, for the associated étale topology, of the objectwise
> tensor product. Its restriction to the small étale site of the scheme below an object `x` is the
> tensor product there of the restrictions of the two factors, by
> `AlgebraicGeometry.Stack.restrictModuleEtaleTensorSheafIso`: restriction commutes with the
> objectwise tensor product because that is sectionwise, and with sheafification because the
> restriction functor of Stacks 06W1 is cocontinuous as well as continuous. Quasi-coherence of a
> tensor product on a ringed site is
> `Stacks.Modules.isQuasicoherentOnSite_sheafificationTensorObjUlift`.

```lean
theorem isLocallyQuasicoherent_tensorSheaf
    (E : BigEtaleSite.{u}) (h : E.cutoff = B.cutoff)
    (F G : SheafOfModules.{u}
      (ringStructureSheafCore B S hS p hp (etaleTopology B) (etaleTopology_le_topology B)))
    (hF : IsLocallyQuasicoherent B E h S hS p hp F.val)
    (hG : IsLocallyQuasicoherent B E h S hS p hp G.val) :
    letI := hasSheafify_etaleAssociatedTopology B S hS p hp
    letI := wEqualsLocallyBijective_etaleAssociatedTopology B S hS p hp
    IsLocallyQuasicoherent B E h S hS p hp
      (((Stacks.SheafOfModules.Tensor.sheafTensor.{_, _, _, u, u}
        (structureSheaf B S hS p hp (etaleTopology B)
          (etaleTopology_le_topology B))).obj F).obj G).val
```

## Tag 06WN, a lemma

[Tag 06WN](https://stacks.math.columbia.edu/tag/06WN) in the Stacks Project.

**`Stacks.SheafOfModules.TensorProduct.isQuasicoherentOnSite_tensorSheaf`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/QuasicoherentTensor.lean, line 354](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/QuasicoherentTensor.lean#L354). The attribute's comment: “tensor_product, not 06WG's site”. References: EGA I (9.1.1), “more general”.

> **The tensor clause of Stacks 06WV (5) and of Stacks 06WN (2), for the quasi-coherence of
> Stacks 03DL (6), on a site satisfying the hypotheses of this section**: the tensor product of
> two sheaves of modules which are quasi-coherent in the sense of
> `SheafOfModules.IsQuasicoherentOnSite` is again quasi-coherent in that sense.  That is the
> quasi-coherence the notion `QCoh(𝒪_𝒳)` of Stacks 06WG is defined by, and not Mathlib's
> predicate.
>
> **The hypotheses of this section exclude the site of Stacks 06WG**, which is why both clause
> strings say so.  Of the five, the fibred fppf site of a category fibred in groupoids over
> `(Sch/S)_fppf` satisfies three and fails two; the two failures are
> `AlgebraicGeometry.FibredSite.not_univLE_associatedSite`, the size hypothesis, which at that
> site's universes reads `UnivLE.{u + 1, u}`, and
> `AlgebraicGeometry.FibredSite.not_hasBinaryProducts_twoLabel`, binary products, which such a
> category generally lacks for want of a final object.  See
> `StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/FibredTensorHypotheses.lean`, where
> the five are settled one by one.  So this statement does not instantiate to the source's clause,
> and the source's clause is not proved anywhere on this development.
>
> The proof is the proof of
> `Stacks.SheafOfModules.TensorProduct.isQuasicoherent_tensorSheaf` run through
> `SheafOfModules.isQuasicoherent_iff_isQuasicoherentOnSite`, the identification of the two
> predicates on a site whose objects and morphisms are small relative to the universe of the
> sections — which is the extra hypothesis `UnivLE.{max u v w, w}` and the only thing separating
> the two statements.  It is not removable: on a big site, whose objects live one universe above
> its sections, the two predicates genuinely differ.
>
> What is *not* asserted is the rest of Stacks 06WN (2), namely that the tensor products formed in
> `Mod(𝒳_Zar, 𝒪)`, `Mod(𝒳_étale, 𝒪)` and `Mod(𝒪_𝒳)` agree.  Those are formed in different
> categories, where sheafification is a different functor, so the agreement is not a consequence
> of this statement and the comparison is not available; hence the qualified clause string, as in
> `AlgebraicGeometry.FibredSite.colimits_quasicoherentModules_of_descent` for part (1).

```lean
public instance isQuasicoherentOnSite_tensorSheaf
    (F G : SheafOfModules.{w}
      (TensorSheafification.structureSheaf O.obj (isSheaf_structureRingPresheaf O)))
    [F.IsQuasicoherentOnSite] [G.IsQuasicoherentOnSite] :
    ((((Stacks.SheafOfModules.Tensor.sheafTensor
      ⟨O.obj, Presheaf.isSheaf_of_isSheaf_comp _ (O.obj) (forget₂ CommRingCat RingCat)
        ((isSheaf_structureRingPresheaf O))⟩).obj (F)).obj (G))).IsQuasicoherentOnSite
```

**`Stacks.SheafOfModules.TensorProduct.isQuasicoherentOnSite_tensorObj`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/QuasicoherentTensor.lean, line 376](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/QuasicoherentTensor.lean#L376). The attribute's comment: “tensor_product, not 06WG's site”.

> **The tensor clause of Stacks 06WV (5) and of Stacks 06WN (2), for the quasi-coherence of
> Stacks 03DL (6)**, for the tensor product of the monoidal category `Mod(𝒪)` itself.  Together
> with `Stacks.SheafOfModules.TensorProduct.isQuasicoherentOnSite_tensorSheaf` this is the
> covering set of the clause at the source's predicate, the development carrying both
> descriptions of the tensor product.
>
> As there, the hypotheses of this section **exclude the fibred fppf site of Stacks 06WG**, by
> `AlgebraicGeometry.FibredSite.not_univLE_associatedSite` and
> `AlgebraicGeometry.FibredSite.not_hasBinaryProducts_twoLabel`; hence the qualified clause
> strings.

```lean
public instance isQuasicoherentOnSite_tensorObj
    (F G : SheafOfModules.{w}
      (TensorSheafification.structureSheaf O.obj (isSheaf_structureRingPresheaf O)))
    [F.IsQuasicoherentOnSite] [G.IsQuasicoherentOnSite] :
    (MonoidalCategory.tensorObj F G).IsQuasicoherentOnSite
```

**`Stacks.SheafOfModules.TensorProduct.quasicoherentOnSiteTensorBifunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/QuasicoherentTensor.lean, line 398](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/QuasicoherentTensor.lean#L398). The attribute's comment: “tensor_product, not 06WG's site”.

> **The tensor product as a bifunctor on the quasi-coherent modules of Stacks 03DL (6)**: the
> restriction of the tensor product of `Mod(𝒪)` to the full subcategory cut out by that
> quasi-coherence.  It exists exactly because that tensor product preserves that
> quasi-coherence, which is the tensor clause of Stacks 06WV (5).
>
> On the fibred fppf site of Stacks 06WG this subcategory is `QCoh(𝒪_𝒳)`
> (`AlgebraicGeometry.FibredSite.quasicoherentModules`), but the hypotheses of this section do
> not hold at that site — see
> `AlgebraicGeometry.FibredSite.not_univLE_associatedSite` and
> `AlgebraicGeometry.FibredSite.not_hasBinaryProducts_twoLabel` — so this bifunctor is not the
> one the source asserts; hence the qualified clause strings.

```lean
public noncomputable def quasicoherentOnSiteTensorBifunctor :
    (SheafOfModules.isQuasicoherentOnSite (TensorSheafification.structureSheaf O.obj
        (isSheaf_structureRingPresheaf O))).FullSubcategory ×
      (SheafOfModules.isQuasicoherentOnSite (TensorSheafification.structureSheaf O.obj
        (isSheaf_structureRingPresheaf O))).FullSubcategory ⥤
      (SheafOfModules.isQuasicoherentOnSite (TensorSheafification.structureSheaf O.obj
        (isSheaf_structureRingPresheaf O))).FullSubcategory
```

**`AlgebraicGeometry.FibredSite.existsUnique_hom_tensorSheafMixed_quasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FibredMixedTensorProduct.lean, line 369](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FibredMixedTensorProduct.lean#L369). The attribute's comment: “tensor_products”.

> **Stacks 06WN(2).**  Restricted to a pair of quasi-coherent modules with sections in
> independent universes, the tensor product formed on an associated site of the fibred category is
> the tensor product in the ambient category of sheaves of modules on that site: every bilinear
> map into a sheaf of modules there has a unique linear factorization through the pure-tensor map.
> This is the universal property the source asserts of the common tensor product on the Zariski,
> étale and fppf sites; it is proved here for all five associated sites, and the factorization is
> tested against every sheaf of modules, not only the quasi-coherent ones.

```lean
public theorem existsUnique_hom_tensorSheafMixed_quasicoherent (τ : SiteKind)
    (F : quasicoherentModules.{u, v, u, m} B S hS p hp)
    (G : quasicoherentModules.{u, v, u, n} B S hS p hp)
    (H : SheafOfModules.{max u m n} (ringStructureSheafCore B S hS p hp τ))
    (b : Stacks.Modules.BilinearMap (structureSheaf B S hS p hp τ).obj
      F.obj.val G.obj.val H.val) :
    ∃! f : tensorSheafMixed B S hS p hp τ ((toSiteModules B S hS p hp τ).obj F)
        ((toSiteModules B S hS p hp τ).obj G) ⟶ H,
      ∀ (U : 𝒳ᵒᵖ) (x : F.obj.val.obj U) (y : G.obj.val.obj U),
        f.val.app U ((toTensorSheafMixed B S hS p hp τ
          ((toSiteModules B S hS p hp τ).obj F)
          ((toSiteModules B S hS p hp τ).obj G)).app U x y) = b.app U x y
```

**`AlgebraicGeometry.FibredSite.internalHomSheaf_val_eq_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/InternalHom.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/InternalHom.lean#L190). The attribute's comment: “internal_homs”.

> The internal Hom of two quasi-coherent modules on a category fibred in groupoids has the
> same underlying presheaf of modules on each of the five associated sites as on the fppf one; in
> particular on the Zariski and étale ones.

```lean
public theorem internalHomSheaf_val_eq_fppf (hp : p.IsFiberedInGroupoids) (τ : SiteKind)
    (F G : quasicoherentModules.{u, v, w, u} B S hS p hp) :
    ((ringedSite B S hS p hp τ).internalHomSheaf
        ((toSiteModules B S hS p hp τ).obj F)
        ((toSiteModules B S hS p hp τ).obj G)).val =
      ((ringedSite B S hS p hp .fppf).internalHomSheaf F.obj G.obj).val
```

**`AlgebraicGeometry.FibredSite.internalHomSheaf_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/InternalHom.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/InternalHom.lean#L201). The attribute's comment: “internal_homs”.

> The internal Hom of a finite locally free quasi-coherent module into a quasi-coherent module
> on a category fibred in groupoids is quasi-coherent on the fppf associated site.

```lean
public theorem internalHomSheaf_isQuasicoherent (hp : p.IsFiberedInGroupoids)
    (F G : quasicoherentModules.{u, v, w, u} B S hS p hp)
    (hF : SheafOfModules.IsFiniteLocallyFreeOnSite F.obj) :
    ((ringedSite B S hS p hp .fppf).internalHomSheaf F.obj G.obj).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.FibredSite.isQuasicoherentOnSite_tensorSheafMixed_quasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/MixedTensorQuasicoherent.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/MixedTensorQuasicoherent.lean#L239). The attribute's comment: “tensor_products”.

> **The tensor product of a pair of quasi-coherent modules with sections in independent
> universes, formed on the fppf site of a category fibred in groupoids, is quasi-coherent.**  This
> is the object whose universal property is
> `AlgebraicGeometry.FibredSite.existsUnique_hom_tensorSheafMixed_quasicoherent`, so the tensor
> product of quasi-coherent modules is again a quasi-coherent module.

```lean
theorem isQuasicoherentOnSite_tensorSheafMixed_quasicoherent
    (F : quasicoherentModules.{u, v, u, m} B S hS p hp)
    (G : quasicoherentModules.{u, v, u, n} B S hS p hp) :
    (tensorSheafMixed B S hS p hp .fppf ((toSiteModules B S hS p hp .fppf).obj F)
      ((toSiteModules B S hS p hp .fppf).obj G)).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.FibredSite.quasicoherentModules_colimits_siteAgreement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentSiteAgreement.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentSiteAgreement.lean#L290). The attribute's comment: “(1): QCoh(O_X) has colimits and they agree with colimits in Mod(X_Zar, O_X), Mod(X_et, O_X), Mod(O_X) and LQCoh(O_X)”.

> **Stacks 06WN (1).**  For a category fibred in groupoids `p : 𝒳 ⥤ (Sch/S)_fppf`, the
> category `QCoh(𝒪_𝒳)` has colimits, and they agree with the colimits in `Mod(𝒪_𝒳)`, in
> `Mod(𝒳_τ, 𝒪_𝒳)` for each of the coarser inherited topologies — in particular in
> `Mod(𝒳_Zar, 𝒪_𝒳)` and `Mod(𝒳_étale, 𝒪_𝒳)` — and in `LQCoh(𝒪_𝒳)`: the inclusion into
> `Mod(𝒪_𝒳)`, the reading functors into `Mod(𝒳_τ, 𝒪_𝒳)` and the inclusion into `LQCoh(𝒪_𝒳)`
> preserve them.  Colimits are indexed by categories in the universe of the schemes.

```lean
theorem quasicoherentModules_colimits_siteAgreement (E : BigEtaleSite.{u})
    (h : E.cutoff = B.cutoff) :
    HasColimitsOfSize.{u, u} (quasicoherentModules.{u, u + 1, u, u} B S hS p hp) ∧
      PreservesColimitsOfSize.{u, u} (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        (ringStructureSheafCore B S hS p hp .fppf)).ι ∧
      (∀ τ : SiteKind,
        PreservesColimitsOfSize.{u, u} (toSiteModules.{u, u + 1, u, u} B S hS p hp τ)) ∧
      PreservesColimitsOfSize.{u, u} (toLocallyQuasicoherentModules B S hS p hp E h)
```

**`AlgebraicGeometry.FibredSite.internalHomSheaf_quasicoherent_siteAgreement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentSiteAgreement.lean, line 386](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentSiteAgreement.lean#L386). The attribute's comment: “(3): for F, G in QCoh(O_X) the internal homs computed in Mod(X_Zar, O_X), Mod(X_et, O_X) and Mod(O_X) agree, F being finite locally free does not depend on the topology, and for F finite locally free the common value is quasi-coherent”.

> **Stacks 06WN (3).**  Let `𝓕` and `𝓖` be quasi-coherent modules on a category fibred in
> groupoids over `(Sch/S)_fppf`.  Then `𝓕` is finite locally free for the fppf topology if and only
> if it is for the étale, and if and only if for the Zariski topology (indeed for each of the five
> topologies); the internal homs `ℋom(𝓕, 𝓖)` computed in `Mod(𝒳_Zar, 𝒪_𝒳)`, `Mod(𝒳_étale, 𝒪_𝒳)`
> and `Mod(𝒪_𝒳)` agree; and when `𝓕` is finite locally free for any one of these topologies the
> common value is an object of `QCoh(𝒪_𝒳)`.

```lean
theorem internalHomSheaf_quasicoherent_siteAgreement
    (F G : quasicoherentModules.{u, u + 1, u, u} B S hS p hp) :
    (∀ τ : SiteKind, SheafOfModules.IsFiniteLocallyFreeOnSite F.obj ↔
      SheafOfModules.IsFiniteLocallyFreeOnSite ((toSiteModules B S hS p hp τ).obj F)) ∧
    (∀ τ : SiteKind,
      (ringedSite B S hS p hp τ).internalHomSheaf ((toSiteModules B S hS p hp τ).obj F)
          ((toSiteModules B S hS p hp τ).obj G) =
        (Stacks.SheafOfModules.comparisonPushforward.{u + 1, u, u, u + 1}
          (BigFppfOver.associatedTopology_le_fppf B S hS p τ)
          (ringStructureSheafCore B S hS p hp .fppf)).obj
          ((ringedSite B S hS p hp .fppf).internalHomSheaf F.obj G.obj)) ∧
    (∀ τ : SiteKind,
      SheafOfModules.IsFiniteLocallyFreeOnSite ((toSiteModules B S hS p hp τ).obj F) →
        ((ringedSite B S hS p hp .fppf).internalHomSheaf F.obj G.obj).IsQuasicoherentOnSite)
```

**`AlgebraicGeometry.FibredSite.sheafTensor_quasicoherent_siteAgreement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentSiteAgreement.lean, line 479](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentSiteAgreement.lean#L479). The attribute's comment: “(2): for F, G in QCoh(O_X) the tensor products computed in Mod(X_Zar, O_X), Mod(X_et, O_X) and Mod(O_X) agree and the common value is quasi-coherent”.

> **Stacks 06WN (2).**  For quasi-coherent modules `𝓕` and `𝓖` on a category fibred in
> groupoids over `(Sch/S)_fppf`, the tensor products `𝓕 ⊗ 𝓖` computed in `Mod(𝒳_Zar, 𝒪_𝒳)`,
> `Mod(𝒳_étale, 𝒪_𝒳)` and `Mod(𝒪_𝒳)` agree — the one computed in `Mod(𝒪_𝒳)`, read for each coarser
> topology, is the one computed for that topology — and the common value is an object of
> `QCoh(𝒪_𝒳)`; it is moreover quasi-coherent on each of the coarser sites.

```lean
theorem sheafTensor_quasicoherent_siteAgreement
    (F G : quasicoherentModules.{u, v, w, u} B S hS p hp) :
    (∀ τ : SiteKind, Nonempty ((Stacks.SheafOfModules.comparisonPushforward.{v, w, u, u}
        (BigFppfOver.associatedTopology_le_fppf B S hS p τ)
        (ringStructureSheafCore B S hS p hp .fppf)).obj
        (((sheafTensor B S hS p hp .fppf).obj F.obj).obj G.obj) ≅
      ((sheafTensor B S hS p hp τ).obj ((toSiteModules B S hS p hp τ).obj F)).obj
        ((toSiteModules B S hS p hp τ).obj G))) ∧
    (((sheafTensor B S hS p hp .fppf).obj F.obj).obj G.obj).IsQuasicoherentOnSite ∧
    (∀ τ : SiteKind, (((sheafTensor B S hS p hp τ).obj
      ((toSiteModules B S hS p hp τ).obj F)).obj
        ((toSiteModules B S hS p hp τ).obj G)).IsQuasicoherentOnSite)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 96.12, Tag 0GQB](https://stacks.math.columbia.edu/tag/0GQB)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
