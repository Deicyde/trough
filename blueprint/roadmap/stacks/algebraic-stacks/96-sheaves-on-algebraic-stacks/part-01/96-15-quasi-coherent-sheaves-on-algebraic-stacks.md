---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.colimits_quasicoherentModules, AlgebraicGeometry.Stack.quasicoherentInclusion_rightExact_not_exact, AlgebraicGeometry.Stack.GroupoidPresentation.quasicoherentEquivalence, AlgebraicGeometry.Stack.abelianQuasicoherentModules, AlgebraicGeometry.FibredSite.preservesColimitsOfSize_quasicoherentInclusion', Stacks.SheafOfModules.TensorProduct.isQuasicoherent_tensorSheaf, Stacks.SheafOfModules.TensorProduct.isQuasicoherent_tensorObj, Stacks.SheafOfModules.TensorProduct.quasicoherentTensorBifunctor
statement: formalized
proof: formalized
---

# 96.15 Quasi-coherent sheaves on algebraic stacks

Section 96.15 of the Stacks Project, [Tag 06WU](https://stacks.math.columbia.edu/tag/06WU). 2 tags here are carried by 25 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06WV, a lemma

[Tag 06WV](https://stacks.math.columbia.edu/tag/06WV) in the Stacks Project.

**`AlgebraicGeometry.Stack.colimits_quasicoherentModules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/AlgebraicStackColimits.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/AlgebraicStackColimits.lean#L71). The attribute's comment: “part (4): QCoh(𝒪_𝒳) has colimits and they agree with colimits in Mod(𝒪_𝒳)”.

> For an algebraic stack `𝒳`, the category `QCoh(𝒪_𝒳)` has colimits, and they agree with
> colimits in `Mod(𝒪_𝒳)`: the inclusion `QCoh(𝒪_𝒳) → Mod(𝒪_𝒳)` preserves them.

```lean
theorem colimits_quasicoherentModules (𝒳 : AlgebraicStacks.{u, w} B S hS) :
    HasColimitsOfSize.{u, u}
        (FibredSite.quasicoherentModules.{u, u + 1, u, u} B S hS 𝒳.val.val.p
          𝒳.val.isFiberedInGroupoids) ∧
      PreservesColimitsOfSize.{u, u}
        (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
          (FibredSite.ringStructureSheafCore B S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids
            .fppf)).ι
```

**`AlgebraicGeometry.Stack.quasicoherentInclusion_rightExact_not_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/AlgebraicStackInclusionNotExact.lean, line 244](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/AlgebraicStackInclusionNotExact.lean#L244). The attribute's comment: “part (3): the inclusion QCoh(𝒪_𝒳) → Mod(𝒪_𝒳) is right exact, and on every big site the algebraic stack Spec(ℤ) is one for which it is not exact”.

> **Stacks 06WV (3).**  The inclusion `QCoh(𝒪_𝒳) → Mod(𝒪_𝒳)` is right exact for every
> algebraic stack `𝒳`, but it is **not** exact in general: on every big fppf site there is an
> algebraic stack, namely `Spec(ℤ)`, for which it is not exact.

```lean
theorem quasicoherentInclusion_rightExact_not_exact :
    (∀ (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
        (𝒳 : AlgebraicStacks.{u, w} B S hS),
        PreservesFiniteColimits
          (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
            (FibredSite.ringStructureSheafCore B S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids
              .fppf)).ι) ∧
      ∀ B : BigFppfSite.{u}, ∃ 𝒳 : AlgebraicStacks.{u, w} B specInt.{u} (contains_specInt B),
        ¬ (PreservesFiniteLimits
            (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
              (FibredSite.ringStructureSheafCore B specInt.{u} (contains_specInt B) 𝒳.val.val.p
                𝒳.val.isFiberedInGroupoids .fppf)).ι ∧
          PreservesFiniteColimits
            (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
              (FibredSite.ringStructureSheafCore B specInt.{u} (contains_specInt B) 𝒳.val.val.p
                𝒳.val.isFiberedInGroupoids .fppf)).ι)
```

**`AlgebraicGeometry.Stack.GroupoidPresentation.quasicoherentEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/AlgebraicStackPresentation.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/AlgebraicStackPresentation.lean#L95). The attribute's comment: “part (1): a presentation [U/R] → 𝒳 induces a canonical equivalence QCoh(𝒪_𝒳) ≌ QCoh(U, R, s, t, c)”.

> **Stacks 06WV (1).**  A presentation `[U/R] → 𝒳` of an algebraic stack — a smooth groupoid
> `(U, R, s, t, c)` in algebraic spaces over `S` and an equivalence `[U/R] → 𝒳` (Stacks 04TI) —
> induces a canonical equivalence `QCoh(𝒪_𝒳) ≌ QCoh(U, R, s, t, c)`.
>
> It is the inverse image along the presenting equivalence, `QCoh(𝒪_𝒳) ≌ QCoh(𝒪_{[U/R]})`,
> followed by the equivalence of Stacks 06WT,
> `AlgebraicGeometry.Stack.quasicoherentEquivalenceGroupoid`.

```lean
def GroupoidPresentation.quasicoherentEquivalence {𝒳 : AlgebraicStacks.{u, w} B S hS}
    (P : GroupoidPresentation B S hS 𝒳.val.val) :
    FibredSite.quasicoherentModules.{u, u + 1, u, u} B S hS 𝒳.val.val.p
        𝒳.val.isFiberedInGroupoids ≌ Space.QuasicoherentModule B S hS P.groupoid
```

**`AlgebraicGeometry.Stack.abelianQuasicoherentModules`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/AlgebraicStackPresentation.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/AlgebraicStackPresentation.lean#L114). The attribute's comment: “part (2): QCoh(𝒪_𝒳) is abelian”.

> **Stacks 06WV (2).**  The quasi-coherent modules on an algebraic stack form an abelian
> category.
>
> By Stacks 04T3 the stack has a presentation `[U/R] → 𝒳` by a smooth groupoid; its source and
> target are smooth, hence flat, so `QCoh(U, R, s, t, c)` is abelian by Stacks 06VZ, and part (1)
> transports the abelian structure to `QCoh(𝒪_𝒳)`.

```lean
instance abelianQuasicoherentModules (𝒳 : AlgebraicStacks.{u, w} B S hS) :
    Abelian (FibredSite.quasicoherentModules.{u, u + 1, u, u} B S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids)
```

**`AlgebraicGeometry.FibredSite.preservesColimitsOfSize_quasicoherentInclusion'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/BigSiteColimits/AffineSectionBaseChangeExit.lean, line 760](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/BigSiteColimits/AffineSectionBaseChangeExit.lean#L760). The attribute's comment: “inclusion_right_exact”.

> **Colimits of quasi-coherent modules are fppf-module colimits.**  The inclusion of the
> quasi-coherent modules into all module sheaves for the associated fppf topology preserves all
> small colimits; this is the comparison half of the colimit clause of Stacks 06WN(1), again with
> both hypotheses of
> `AlgebraicGeometry.FibredSite.inclusion_preservesColimits_of_span` discharged and only the
> standing essential smallness left assumed.
>
> Right exactness of the inclusion functor, Stacks 06WV(3), is this statement: the source
> derives it from the agreement of colimits, Stacks 06WV(4).

```lean
theorem preservesColimitsOfSize_quasicoherentInclusion' :
    PreservesColimitsOfSize.{u, u}
      (SheafOfModules.isQuasicoherentOnSite.{v, w, u, u}
        (ringStructureSheafCore B S hS p hp .fppf)).ι
```

**`Stacks.SheafOfModules.TensorProduct.isQuasicoherent_tensorSheaf`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/QuasicoherentTensor.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/QuasicoherentTensor.lean#L241). The attribute's comment: “tensor_product, for Mathlib's IsQuasicoherent, not 03DL(6)”. References: EGA I (9.1.1), “more general”; EGA IV (8.2.7), “case A = O_S”.

> **Stacks 06WV (5) for Mathlib's `SheafOfModules.IsQuasicoherent`**: the tensor product of
> two quasi-coherent sheaves of modules on a site is quasi-coherent.  Quasi-coherence is a local
> condition, and over a common refinement of the two coverings on which the factors are presented,
> the tensored presentation presents the tensor product.
>
> The quasi-coherence here is Mathlib's — a covering of the final object carrying
> `SheafOfModules.Presentation`s — and *not* the `SheafOfModules.IsQuasicoherentOnSite` of
> Stacks 03DL (6), which is the notion `QCoh(𝒪_𝒳)` of Stacks 06WG means; hence the qualified
> clause string.  The clause for that notion is
> `Stacks.SheafOfModules.TensorProduct.isQuasicoherentOnSite_tensorSheaf` below, which is this
> statement plus `SheafOfModules.isQuasicoherent_iff_isQuasicoherentOnSite` and so carries one
> further size hypothesis on the site.
>
> This is also the site-level form of Stacks 01CE (3), which is a statement about a ringed space
> and is tagged there, on `AlgebraicGeometry.tensorSheaf_isQuasicoherent` in
> `StacksFrontier/CategoryTheory/Sites/Modules/TensorProduct/Basic.lean`.

```lean
public instance isQuasicoherent_tensorSheaf
    (F G : SheafOfModules.{w}
      (TensorSheafification.structureSheaf O.obj (isSheaf_structureRingPresheaf O)))
    [F.IsQuasicoherent] [G.IsQuasicoherent] :
    ((((Stacks.SheafOfModules.Tensor.sheafTensor
      ⟨O.obj, Presheaf.isSheaf_of_isSheaf_comp _ (O.obj) (forget₂ CommRingCat RingCat)
        ((isSheaf_structureRingPresheaf O))⟩).obj (F)).obj (G))).IsQuasicoherent
```

**`Stacks.SheafOfModules.TensorProduct.isQuasicoherent_tensorObj`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/QuasicoherentTensor.lean, line 267](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/QuasicoherentTensor.lean#L267). The attribute's comment: “tensor_product, for Mathlib's IsQuasicoherent, not 03DL(6)”. References: EGA I (9.1.1), “more general”; EGA IV (8.2.7), “case A = O_S”.

> **Stacks 06WV (5) for Mathlib's `SheafOfModules.IsQuasicoherent`**, for the tensor product
> of the monoidal category `Mod(𝒪)` itself: given quasi-coherent sheaves of modules `F` and `G`,
> the tensor product `F ⊗_𝒪 G` formed in `Mod(𝒪)` is quasi-coherent.  This is the shape in which
> the source states the clause;
> `Stacks.SheafOfModules.TensorProduct.isQuasicoherent_tensorSheaf` is the same statement for the
> explicit model of that tensor product as a sheafified objectwise tensor product, and the two
> together are the covering set at this predicate, the development carrying both descriptions.
> The same pair for the quasi-coherence of Stacks 03DL (6) is
> `Stacks.SheafOfModules.TensorProduct.isQuasicoherentOnSite_tensorObj` and
> `…isQuasicoherentOnSite_tensorSheaf`.

```lean
public instance isQuasicoherent_tensorObj
    (F G : SheafOfModules.{w}
      (TensorSheafification.structureSheaf O.obj (isSheaf_structureRingPresheaf O)))
    [F.IsQuasicoherent] [G.IsQuasicoherent] :
    (MonoidalCategory.tensorObj F G).IsQuasicoherent
```

**`Stacks.SheafOfModules.TensorProduct.quasicoherentTensorBifunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/QuasicoherentTensor.lean, line 286](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/QuasicoherentTensor.lean#L286). The attribute's comment: “tensor_product, for Mathlib's IsQuasicoherent, not 03DL(6)”.

> **The tensor product as a bifunctor on quasi-coherent modules**, `QCoh(𝒪) × QCoh(𝒪) ⥤
> QCoh(𝒪)`.  It is the restriction of the tensor product of `Mod(𝒪)` to the full subcategory of
> quasi-coherent modules, and it exists exactly because that tensor product preserves
> quasi-coherence, which is Stacks 06WV (5): a bifunctor valued in `QCoh(𝒪)` cannot be written
> down before the clause is proved.  The quasi-coherence cutting out the subcategory is Mathlib's;
> `Stacks.SheafOfModules.TensorProduct.quasicoherentOnSiteTensorBifunctor` is the same bifunctor
> on the subcategory cut out by the quasi-coherence of Stacks 03DL (6), which is the category
> `QCoh(𝒪_𝒳)` of Stacks 06WG.

```lean
public noncomputable def quasicoherentTensorBifunctor :
    (SheafOfModules.isQuasicoherent (TensorSheafification.structureSheaf O.obj
        (isSheaf_structureRingPresheaf O))).FullSubcategory ×
      (SheafOfModules.isQuasicoherent (TensorSheafification.structureSheaf O.obj
        (isSheaf_structureRingPresheaf O))).FullSubcategory ⥤
      (SheafOfModules.isQuasicoherent (TensorSheafification.structureSheaf O.obj
        (isSheaf_structureRingPresheaf O))).FullSubcategory
```

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

**`AlgebraicGeometry.FibredSite.existsUnique_hom_tensorSheafMixed_quasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FibredMixedTensorProduct.lean, line 369](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FibredMixedTensorProduct.lean#L369). The attribute's comment: “tensor_product”.

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

**`AlgebraicGeometry.FibredSite.isQuasicoherentOnSite_tensorSheafMixed_quasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/MixedTensorQuasicoherent.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/MixedTensorQuasicoherent.lean#L239). The attribute's comment: “tensor_product”.

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

**`AlgebraicGeometry.FibredSite.isQuasicoherentOnSite_X₂_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentExtensions.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentExtensions.lean#L68). The attribute's comment: “part (7): an extension in Mod(𝒪_𝒳) of quasi-coherent modules is quasi-coherent, for every category fibred in groupoids over (Sch/S)_fppf, in particular for every algebraic stack”.

> **Stacks 06WV (7).**  Let `𝒳` be a category fibred in groupoids over `(Sch/S)_fppf`, for
> instance an algebraic stack, and let `0 → 𝓕₁ → 𝓕₂ → 𝓕₃ → 0` be a short exact sequence in
> `Mod(𝒪_𝒳)` with `𝓕₁` and `𝓕₃` quasi-coherent.  Then `𝓕₂` is quasi-coherent.
>
> By Stacks 06WI it suffices that `x^*𝓕₂` be quasi-coherent on `(Sch/U)_fppf` for each object `x`
> over a scheme `U`.  The functor `x^*` is restriction to `𝒳_fppf/x` followed by an equivalence;
> restriction to a localized site is exact (Stacks 03DA), so `x^*` carries the sequence to a short
> exact sequence on `(Sch/U)_fppf`, whose middle term is quasi-coherent by Stacks 0GNC (4),
> `AlgebraicGeometry.BigFppfOver.isQuasicoherentOnSite_shortExact_X₂_all`.

```lean
theorem isQuasicoherentOnSite_X₂_of_shortExact
    {C : ShortComplex (SheafOfModules.{u} (ringStructureSheafCore B S hS p hp .fppf))}
    (hC : C.ShortExact) (h₁ : C.X₁.IsQuasicoherentOnSite) (h₃ : C.X₃.IsQuasicoherentOnSite) :
    C.X₂.IsQuasicoherentOnSite
```

Declarations registered for the tag:

- [`AlgebraicGeometry.FibredSite.isQuasicoherentOnSite_sheafTensor`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentSiteAgreement.lean#L427), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/AlgebraicStackPresentation.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/AlgebraicStackPresentation.lean#L59) (StacksFrontier): “part (5): for quasi-coherent F, G the tensor product F ⊗ G computed in Mod(𝒪_𝒳) is quasi-coherent, for every category fibred in groupoids over (Sch/S)_fppf (at τ = fppf)”.
- [`AlgebraicGeometry.FibredSite.internalHomSheaf_isQuasicoherent`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/InternalHom.lean#L201), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/AlgebraicStackPresentation.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/AlgebraicStackPresentation.lean#L63) (StacksFrontier): “part (6): for F, G in QCoh(𝒪_𝒳) with F finite locally free, the internal Hom ℋom(F, G) computed in Mod(𝒪_𝒳) is quasi-coherent, for every category fibred in groupoids over (Sch/S)_fppf”.

## Tag 0781, a proposition

[Tag 0781](https://stacks.math.columbia.edu/tag/0781) in the Stacks Project.

**`AlgebraicGeometry.Stack.quasicoherentModules_isGrothendieckAbelian_enoughInjectives_hasLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/AlgebraicStackCoherator.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/AlgebraicStackCoherator.lean#L137). The attribute's comment: “part (1): QCoh(𝒪_𝒳) is a Grothendieck abelian category; consequently it has enough injectives and all limits”.

> **Stacks 0781, part (1).**  Let `𝒳` be an algebraic stack over `S`.  The category
> `QCoh(𝒪_𝒳)` of quasi-coherent modules on `𝒳` is a Grothendieck abelian category; consequently
> it has enough injectives and all limits.
>
> Through a presentation `[U/R] → 𝒳` whose space of objects is a scheme, `QCoh(𝒪_𝒳)` is
> equivalent to `QCoh(U, R, s, t, c)` (Stacks 06WV (1)), which is Grothendieck abelian: colimits
> exist, filtered colimits are exact because they and kernels are computed on `𝒪_U`-modules, and
> there is a separator by the argument of Groupoids in Spaces, Lemma 0780
> (`AlgebraicGeometry.Space.QuasicoherentModule.isGrothendieckAbelian_of_objects_eq`).  The
> assertions on injectives and limits hold in every Grothendieck abelian category (Stacks 079H,
> 07D8).

```lean
theorem quasicoherentModules_isGrothendieckAbelian_enoughInjectives_hasLimits :
    IsGrothendieckAbelian.{u} (FibredSite.quasicoherentModules.{u, u + 1, u, u} B S hS
        𝒳.val.val.p 𝒳.val.isFiberedInGroupoids) ∧
      EnoughInjectives (FibredSite.quasicoherentModules.{u, u + 1, u, u} B S hS
        𝒳.val.val.p 𝒳.val.isFiberedInGroupoids) ∧
      HasLimitsOfSize.{u, u} (FibredSite.quasicoherentModules.{u, u + 1, u, u} B S hS
        𝒳.val.val.p 𝒳.val.isFiberedInGroupoids)
```

**`AlgebraicGeometry.Stack.exists_quasicoherentCoherator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/AlgebraicStackCoherator.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/AlgebraicStackCoherator.lean#L194). The attribute's comment: “part (2): the inclusion QCoh(𝒪_𝒳) → Mod(𝒪_𝒳) has a right adjoint Q such that Q(F) → F is an isomorphism for every quasi-coherent F”.

> **Stacks 0781, part (2).**  Let `𝒳` be an algebraic stack over `S`.  The inclusion
> `QCoh(𝒪_𝒳) → Mod(𝒪_𝒳)` has a right adjoint `Q`, the *coherator*, such that for every
> quasi-coherent `𝒪_𝒳`-module `𝓕` the adjunction morphism `Q(𝓕) → 𝓕` is an isomorphism.
>
> The right adjoint exists by `AlgebraicGeometry.Stack.isLeftAdjoint_quasicoherentInclusion`.
> The inclusion is fully faithful, so the counit is an isomorphism exactly on its essential image,
> which contains the quasi-coherent modules.

```lean
theorem exists_quasicoherentCoherator :
    ∃ (Q : SheafOfModules.{u} (FibredSite.ringStructureSheafCore B S hS 𝒳.val.val.p
          𝒳.val.isFiberedInGroupoids .fppf) ⥤
        FibredSite.quasicoherentModules.{u, u + 1, u, u} B S hS 𝒳.val.val.p
          𝒳.val.isFiberedInGroupoids)
      (adj : (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        (FibredSite.ringStructureSheafCore B S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids
          .fppf)).ι ⊣ Q),
      ∀ M : SheafOfModules.{u} (FibredSite.ringStructureSheafCore B S hS 𝒳.val.val.p
          𝒳.val.isFiberedInGroupoids .fppf),
        M.IsQuasicoherentOnSite → IsIso (adj.counit.app M)
```

**`AlgebraicGeometry.FibredSite.isGrothendieckAbelian_quasicoherentModules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Coherator.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Coherator.lean#L83). The attribute's comment: “part (1): QCoh(𝒪_𝒳) is Grothendieck abelian, over local smallness, the exactness of filtered colimits, and the separator the source gets from a groupoid presentation”.

> The category `QCoh(𝒪_𝒳)` of quasi-coherent modules on the associated fppf site of a category
> fibred in groupoids is a Grothendieck abelian category, provided quasi-coherence is closed under
> colimits (`hclosed`), `QCoh(𝒪_𝒳)` is locally small (`hls`), its filtered colimits are exact
> (`hab5`) and it has a separator (`hsep`).

```lean
theorem isGrothendieckAbelian_quasicoherentModules
    [Abelian (quasicoherentModules.{u, u + 1, u, u} B S hS p hp)]
    (hclosed : SheafOfModules.ClosedUnderColimitsOfSize.{u, u + 1, u, u, u}
      (ringStructureSheafCore B S hS p hp .fppf))
    (hls : LocallySmall.{u} (quasicoherentModules.{u, u + 1, u, u} B S hS p hp))
    (hab5 : ∀ (K : Type u) [Category.{u} K] [IsFiltered K]
      [HasColimitsOfShape K (quasicoherentModules.{u, u + 1, u, u} B S hS p hp)],
      HasExactColimitsOfShape K (quasicoherentModules.{u, u + 1, u, u} B S hS p hp))
    (hsep : HasSeparator (quasicoherentModules.{u, u + 1, u, u} B S hS p hp)) :
    IsGrothendieckAbelian.{u} (quasicoherentModules.{u, u + 1, u, u} B S hS p hp)
```

**`AlgebraicGeometry.FibredSite.enoughInjectives_quasicoherentModules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Coherator.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Coherator.lean#L102). The attribute's comment: “part (1), its consequence: QCoh(𝒪_𝒳) has enough injectives”.

> Under the hypotheses of
> `AlgebraicGeometry.FibredSite.isGrothendieckAbelian_quasicoherentModules`, `QCoh(𝒪_𝒳)` has
> enough injectives.

```lean
theorem enoughInjectives_quasicoherentModules
    [Abelian (quasicoherentModules.{u, u + 1, u, u} B S hS p hp)]
    (hclosed : SheafOfModules.ClosedUnderColimitsOfSize.{u, u + 1, u, u, u}
      (ringStructureSheafCore B S hS p hp .fppf))
    (hls : LocallySmall.{u} (quasicoherentModules.{u, u + 1, u, u} B S hS p hp))
    (hab5 : ∀ (K : Type u) [Category.{u} K] [IsFiltered K]
      [HasColimitsOfShape K (quasicoherentModules.{u, u + 1, u, u} B S hS p hp)],
      HasExactColimitsOfShape K (quasicoherentModules.{u, u + 1, u, u} B S hS p hp))
    (hsep : HasSeparator (quasicoherentModules.{u, u + 1, u, u} B S hS p hp)) :
    EnoughInjectives (quasicoherentModules.{u, u + 1, u, u} B S hS p hp)
```

**`AlgebraicGeometry.FibredSite.hasLimitsOfSize_quasicoherentModules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Coherator.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Coherator.lean#L119). The attribute's comment: “part (1), its consequence: QCoh(𝒪_𝒳) has all limits”.

> Under the hypotheses of
> `AlgebraicGeometry.FibredSite.isGrothendieckAbelian_quasicoherentModules`, `QCoh(𝒪_𝒳)` has all
> limits.

```lean
theorem hasLimitsOfSize_quasicoherentModules
    [Abelian (quasicoherentModules.{u, u + 1, u, u} B S hS p hp)]
    (hclosed : SheafOfModules.ClosedUnderColimitsOfSize.{u, u + 1, u, u, u}
      (ringStructureSheafCore B S hS p hp .fppf))
    (hls : LocallySmall.{u} (quasicoherentModules.{u, u + 1, u, u} B S hS p hp))
    (hab5 : ∀ (K : Type u) [Category.{u} K] [IsFiltered K]
      [HasColimitsOfShape K (quasicoherentModules.{u, u + 1, u, u} B S hS p hp)],
      HasExactColimitsOfShape K (quasicoherentModules.{u, u + 1, u, u} B S hS p hp))
    (hsep : HasSeparator (quasicoherentModules.{u, u + 1, u, u} B S hS p hp)) :
    HasLimitsOfSize.{u, u} (quasicoherentModules.{u, u + 1, u, u} B S hS p hp)
```

**`AlgebraicGeometry.FibredSite.moduleCoherator`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Coherator.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Coherator.lean#L165). The attribute's comment: “part (2): the coherator Q : Mod(𝒪_𝒳) ⥤ QCoh(𝒪_𝒳)”.

> **The coherator on `Mod(𝒪_𝒳)`.** The right adjoint of the inclusion of `QCoh(𝒪_𝒳)` into all
> modules on the associated fppf site of `𝒳`: it sends a module `A` to the terminal quasi-coherent
> module equipped with a map to `A`.

```lean
def moduleCoherator
    (hclosed : SheafOfModules.ClosedUnderColimitsOfSize.{u, u + 1, u, u, u}
      (ringStructureSheafCore B S hS p hp .fppf))
    (hls : LocallySmall.{u} (quasicoherentModules.{u, u + 1, u, u} B S hS p hp))
    (hlsD : LocallySmall.{u} (SheafOfModules.{u} (ringStructureSheafCore B S hS p hp .fppf)))
    (hwp : WellPowered.{u} (quasicoherentModules.{u, u + 1, u, u} B S hS p hp)ᵒᵖ)
    (hsep : HasSeparator (quasicoherentModules.{u, u + 1, u, u} B S hS p hp)) :
    SheafOfModules.{u} (ringStructureSheafCore B S hS p hp .fppf) ⥤
      quasicoherentModules.{u, u + 1, u, u} B S hS p hp
```

**`AlgebraicGeometry.FibredSite.moduleCoheratorAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Coherator.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Coherator.lean#L185). The attribute's comment: “part (2): the adjunction between the inclusion and the coherator”.

> **The coherator on `Mod(𝒪_𝒳)` is right adjoint to the inclusion.** The adjunction is the
> universal property of the terminal objects the coherator is built from.

```lean
def moduleCoheratorAdjunction
    (hclosed : SheafOfModules.ClosedUnderColimitsOfSize.{u, u + 1, u, u, u}
      (ringStructureSheafCore B S hS p hp .fppf))
    (hls : LocallySmall.{u} (quasicoherentModules.{u, u + 1, u, u} B S hS p hp))
    (hlsD : LocallySmall.{u} (SheafOfModules.{u} (ringStructureSheafCore B S hS p hp .fppf)))
    (hwp : WellPowered.{u} (quasicoherentModules.{u, u + 1, u, u} B S hS p hp)ᵒᵖ)
    (hsep : HasSeparator (quasicoherentModules.{u, u + 1, u, u} B S hS p hp)) :
    (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        (ringStructureSheafCore B S hS p hp .fppf)).ι ⊣
      moduleCoherator B S hS p hp hclosed hls hlsD hwp hsep
```

**`AlgebraicGeometry.FibredSite.moduleCoheratorCompInclusionIsoId`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Coherator.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Coherator.lean#L206). The attribute's comment: “part (2): the coherator composed with the inclusion is the identity”.

> **The coherator fixes the quasi-coherent modules.** The composite of the inclusion with the
> coherator is the identity functor of `QCoh(𝒪_𝒳)`: `Q 𝓕 ≅ 𝓕` for quasi-coherent `𝓕`.

```lean
def moduleCoheratorCompInclusionIsoId
    (hclosed : SheafOfModules.ClosedUnderColimitsOfSize.{u, u + 1, u, u, u}
      (ringStructureSheafCore B S hS p hp .fppf))
    (hls : LocallySmall.{u} (quasicoherentModules.{u, u + 1, u, u} B S hS p hp))
    (hlsD : LocallySmall.{u} (SheafOfModules.{u} (ringStructureSheafCore B S hS p hp .fppf)))
    (hwp : WellPowered.{u} (quasicoherentModules.{u, u + 1, u, u} B S hS p hp)ᵒᵖ)
    (hsep : HasSeparator (quasicoherentModules.{u, u + 1, u, u} B S hS p hp)) :
    (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
          (ringStructureSheafCore B S hS p hp .fppf)).ι ⋙
        moduleCoherator B S hS p hp hclosed hls hlsD hwp hsep ≅
      𝟭 (quasicoherentModules.{u, u + 1, u, u} B S hS p hp)
```

**`AlgebraicGeometry.FibredSite.moduleCoheratorSucc`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentPushforward.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentPushforward.lean#L219). The attribute's comment: “part (2): the coherator Q : Mod(𝒪_𝒳) ⥤ QCoh(𝒪_𝒳), at section universe u + 1”.

> **Stacks 0781, part (2), at section universe `u + 1`: the coherator on `Mod(𝒪_𝒳)`.**  The
> right adjoint of the inclusion of `QCoh(𝒪_𝒳)` into all modules on the associated fppf site: it
> sends a module `A` to the terminal quasi-coherent module equipped with a map to `A`.
>
> `AlgebraicGeometry.FibredSite.moduleCoherator` is the same construction at section universe `u`;
> `u + 1` is the universe the direct images of **Stacks 06WE** along a 1-morphism of algebraic
> stacks live in, and so the universe **Stacks 077A** needs the coherator in.

```lean
def moduleCoheratorSucc
    (hclosed : QuasicoherentClosedUnderColimitsSucc B S hS p hp)
    (hwp : WellPowered.{u + 1} (quasicoherentModules.{u, u + 1, u, u + 1} B S hS p hp)ᵒᵖ)
    (hsep : HasSeparator (quasicoherentModules.{u, u + 1, u, u + 1} B S hS p hp)) :
    SheafOfModules.{u + 1} (ringStructureSheafCore B S hS p hp .fppf) ⥤
      quasicoherentModules.{u, u + 1, u, u + 1} B S hS p hp
```

**`AlgebraicGeometry.FibredSite.moduleCoheratorSuccAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentPushforward.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentPushforward.lean#L233). The attribute's comment: “part (2): the adjunction between the inclusion and the coherator, at section universe u + 1”.

> **Stacks 0781, part (2): the coherator is right adjoint to the inclusion.**  The adjunction
> is the universal property of the terminal objects the coherator is built from.

```lean
def moduleCoheratorSuccAdjunction
    (hclosed : QuasicoherentClosedUnderColimitsSucc B S hS p hp)
    (hwp : WellPowered.{u + 1} (quasicoherentModules.{u, u + 1, u, u + 1} B S hS p hp)ᵒᵖ)
    (hsep : HasSeparator (quasicoherentModules.{u, u + 1, u, u + 1} B S hS p hp)) :
    quasicoherentInclusion B S hS p hp ⊣ moduleCoheratorSucc B S hS p hp hclosed hwp hsep
```

**`AlgebraicGeometry.FibredSite.moduleCoheratorSuccCompInclusionIsoId`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentPushforward.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentPushforward.lean#L247). The attribute's comment: “part (2): the coherator composed with the inclusion is the identity, at section universe u + 1”.

> **Stacks 0781, part (2): the coherator fixes the quasi-coherent modules.**  The inclusion is
> fully faithful, so the unit of the adjunction is an isomorphism; this is the source's assertion
> that `Q 𝓕 → 𝓕` is an isomorphism for quasi-coherent `𝓕`.

```lean
def moduleCoheratorSuccCompInclusionIsoId
    (hclosed : QuasicoherentClosedUnderColimitsSucc B S hS p hp)
    (hwp : WellPowered.{u + 1} (quasicoherentModules.{u, u + 1, u, u + 1} B S hS p hp)ᵒᵖ)
    (hsep : HasSeparator (quasicoherentModules.{u, u + 1, u, u + 1} B S hS p hp)) :
    quasicoherentInclusion B S hS p hp ⋙ moduleCoheratorSucc B S hS p hp hclosed hwp hsep ≅
      𝟭 (quasicoherentModules.{u, u + 1, u, u + 1} B S hS p hp)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 96.15, Tag 06WU](https://stacks.math.columbia.edu/tag/06WU)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
