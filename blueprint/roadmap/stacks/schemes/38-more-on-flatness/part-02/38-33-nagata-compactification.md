---
declaration: section
origin: cited
lean: AlgebraicGeometry.isSeparated_of_sup_eq_top_of_isClosedImmersion_mapDesc, AlgebraicGeometry.exists_isAdmissibleBlowup_disjoint_strictTransforms, AlgebraicGeometry.exists_isAdmissibleBlowup_disjoint_closures, AlgebraicGeometry.exists_isAdmissibleBlowup_strictTransform_isIso_near_closure, AlgebraicGeometry.exists_common_isAdmissibleBlowup_isOpenImmersion, Stacks.Blowup.exists_iso_image_strictTransform, AlgebraicGeometry.exists_isAdmissibleBlowup_properExtension, AlgebraicGeometry.hasCompactification_of_two_opens
statement: formalized
proof: formalized
---

# 38.33 Nagata compactification

Section 38.33 of the Stacks Project, [Tag 0F3T](https://stacks.math.columbia.edu/tag/0F3T). 8 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0F3U, a lemma

[Tag 0F3U](https://stacks.math.columbia.edu/tag/0F3U) in the Stacks Project.

**`AlgebraicGeometry.isSeparated_of_sup_eq_top_of_isClosedImmersion_mapDesc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Compactification/SeparatedTwoOpens.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Compactification/SeparatedTwoOpens.lean#L47).

> **Stacks Project, Tag 0F3U.** Two separated open subschemes covering the source, whose
> overlap is closed in their fibre product over the base, give a separated morphism.

```lean
theorem isSeparated_of_sup_eq_top_of_isClosedImmersion_mapDesc
    {X S : Scheme.{u}} (f : X ⟶ S) (U V : X.Opens)
    (hcover : U ⊔ V = ⊤)
    [IsSeparated (U.ι ≫ f)] [IsSeparated (V.ι ≫ f)]
    (hUV : IsClosedImmersion (pullback.mapDesc U.ι V.ι f)) :
    IsSeparated f
```

## Tag 0F3V, a lemma

[Tag 0F3V](https://stacks.math.columbia.edu/tag/0F3V) in the Stacks Project.

**`AlgebraicGeometry.exists_isAdmissibleBlowup_disjoint_strictTransforms`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/Separation.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/Separation.lean#L331). The attribute's comment: “separate\_strict\_transforms”.

> **Stacks Project, Tag 0F3V, part (1).** Let `X` be a quasi-compact and quasi-separated scheme
> and `U ⊆ X` an open. Let `Z₁ = V(ℐ₁)` and `Z₂ = V(ℐ₂)` be closed subschemes of finite
> presentation which do not meet inside `U`. Then there is a centre of finite presentation disjoint
> from `U` — so that the blowup of `X` in it is a `U`-admissible blowup — on which the strict
> transforms of `Z₁` and `Z₂` are disjoint.
>
> Quasi-compactness of `U` is not needed; see the implementation notes of this file.

```lean
theorem exists_isAdmissibleBlowup_disjoint_strictTransforms [CompactSpace X]
    [QuasiSeparatedSpace X] (U : X.Opens) (I₁ I₂ : X.IdealSheafData)
    (h₁ : FinitePresentation I₁.subschemeι) (h₂ : FinitePresentation I₂.subschemeι)
    (hdisj : Disjoint ((U : Set X) ∩ (I₁.support : Set X)) (I₂.support : Set X)) :
    ∃ I : X.IdealSheafData, Stacks.Blowup.IsAdmissibleBlowup U (blowUpToBase I) ∧
      Disjoint (U : Set X) (I.support : Set X) ∧
        Disjoint (Set.range (strictTransformToBlowUp I₁.subschemeι I).base)
          (Set.range (strictTransformToBlowUp I₂.subschemeι I).base)
```

**`AlgebraicGeometry.exists_isAdmissibleBlowup_disjoint_closures`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/Separation.lean, line 474](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/Separation.lean#L474). The attribute's comment: “separate\_constructible\_closures”.

> **Stacks Project, Tag 0F3V, part (2).** Let `X` be a quasi-compact and quasi-separated scheme,
> let `U ⊆ X` be a quasi-compact open and let `T₁, T₂ ⊆ U` be disjoint constructible closed subsets.
> Then there is a `U`-admissible blowup `X' ⟶ X` in which the closures of `T₁` and `T₂` are
> disjoint.
>
> This is part (1) applied to closed subschemes of `X` cutting out `T₁` and `T₂` on `U`: the closure
> of the preimage of `Tᵢ` is contained in the strict transform of the `i`-th subscheme, which is
> closed because the subscheme is a closed subscheme of `X`.

```lean
theorem exists_isAdmissibleBlowup_disjoint_closures [CompactSpace X] [QuasiSeparatedSpace X]
    (U : X.Opens) (hU : IsCompact (U : Set X)) (T₁ T₂ : Set U.toScheme)
    (hT₁ : IsClosed T₁) (hT₂ : IsClosed T₂) (hc₁ : Topology.IsConstructible T₁)
    (hc₂ : Topology.IsConstructible T₂) (hdisj : Disjoint T₁ T₂) :
    ∃ (X' : Scheme.{u}) (f : X' ⟶ X), Stacks.Blowup.IsAdmissibleBlowup U f ∧
      Disjoint (closure (f.base ⁻¹' (U.ι.base '' T₁)))
        (closure (f.base ⁻¹' (U.ι.base '' T₂)))
```

## Tag 0F3W, a lemma

[Tag 0F3W](https://stacks.math.columbia.edu/tag/0F3W) in the Stacks Project.

**`AlgebraicGeometry.exists_isAdmissibleBlowup_strictTransform_isIso_near_closure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Compactification/IsoNearClosure.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Compactification/IsoNearClosure.lean#L178).

> **Stacks Project, Tag 0F3W.** A proper morphism which is an isomorphism over an open
> containing a subset `T` closed in a quasi-compact open `V` becomes, after a `V`-admissible
> blowup, a morphism whose strict transform is an isomorphism over an open neighbourhood of the
> closure of the inverse image of `T`.

```lean
theorem exists_isAdmissibleBlowup_strictTransform_isIso_near_closure
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsProper f]
    [CompactSpace X] [QuasiSeparatedSpace X]
    [CompactSpace Y] [QuasiSeparatedSpace Y]
    (V : Y.Opens) (hV : IsCompact (V : Set Y))
    (T : Set Y) (hTV : T ⊆ (V : Set Y))
    (hT : IsClosed (V.ι.base ⁻¹' T))
    (hiso : ∃ W : Y.Opens, W ≤ V ∧ T ⊆ (W : Set Y) ∧ IsIso (f ∣_ W)) :
    ∃ I : Y.IdealSheafData,
      FinitePresentation I.subschemeι ∧
      Disjoint (V : Set Y) (I.support : Set Y) ∧
      ∃ W : (blowUp I).Opens,
        closure ((blowUpToBase I).base ⁻¹' T) ⊆ (W : Set (blowUp I)) ∧
        IsIso (strictTransformToBlowUp f I ∣_ W)
```

## Tag 0F3X, a lemma

[Tag 0F3X](https://stacks.math.columbia.edu/tag/0F3X) in the Stacks Project.

**`AlgebraicGeometry.exists_common_isAdmissibleBlowup_isOpenImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Compactification/CommonAdmissibleBlowups.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Compactification/CommonAdmissibleBlowups.lean#L214).

> **Stacks Project, Tag 0F3X.** Let `S` be a quasi-compact and quasi-separated scheme and let
> `u₁ : U ⟶ X₁` and `u₂ : U ⟶ X₂` be open immersions of schemes over `S`, with `U`, `X₁` and `X₂`
> of finite type and separated over `S`. Then there is a commutative diagram of schemes over `S`
> in which `Xᵢ' ⟶ Xᵢ` is a `U`-admissible blowup, `Xᵢ' ⟶ X` is an open immersion, and `X` is
> separated and of finite type over `S`.

```lean
theorem exists_common_isAdmissibleBlowup_isOpenImmersion {S U X₁ X₂ : Scheme.{u}}
    [CompactSpace S] [QuasiSeparatedSpace S]
    (fU : U ⟶ S) (f₁ : X₁ ⟶ S) (f₂ : X₂ ⟶ S)
    [LocallyOfFiniteType fU] [QuasiCompact fU] [IsSeparated fU]
    [LocallyOfFiniteType f₁] [QuasiCompact f₁] [IsSeparated f₁]
    [LocallyOfFiniteType f₂] [QuasiCompact f₂] [IsSeparated f₂]
    (u₁ : U ⟶ X₁) (u₂ : U ⟶ X₂) [IsOpenImmersion u₁] [IsOpenImmersion u₂]
    (hu₁ : u₁ ≫ f₁ = fU) (hu₂ : u₂ ≫ f₂ = fU) :
    ∃ (X₁' X₂' X : Scheme.{u}) (b₁ : X₁' ⟶ X₁) (b₂ : X₂' ⟶ X₂)
      (j₁ : X₁' ⟶ X) (j₂ : X₂' ⟶ X)
      (v₁ : U ⟶ X₁') (v₂ : U ⟶ X₂') (v : U ⟶ X) (f : X ⟶ S),
      Stacks.Blowup.IsAdmissibleBlowup u₁.opensRange b₁ ∧
        Stacks.Blowup.IsAdmissibleBlowup u₂.opensRange b₂ ∧
          IsOpenImmersion j₁ ∧ IsOpenImmersion j₂ ∧
            LocallyOfFiniteType f ∧ QuasiCompact f ∧ IsSeparated f ∧
              (v₁ ≫ b₁ = u₁) ∧ (v₂ ≫ b₂ = u₂) ∧
                (v₁ ≫ j₁ = v) ∧ (v₂ ≫ j₂ = v) ∧
                  (b₁ ≫ f₁ = j₁ ≫ f) ∧ (b₂ ≫ f₂ = j₂ ≫ f) ∧ (v ≫ f = fU)
```

## Tag 0F3Y, a lemma

[Tag 0F3Y](https://stacks.math.columbia.edu/tag/0F3Y) in the Stacks Project.

**`Stacks.Blowup.exists_iso_image_strictTransform`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/StrictTransformImage.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/StrictTransformImage.lean#L242).

> **Stacks Project, Tag 0F3Y.** For `f : V ⟶ X ×_S Y` quasi-compact with first projection landing
> in an open `U ⊆ X`, a `U`-admissible blowup `b : X' ⟶ X` and a lift `g : V ⟶ X' ×_S Y` of `f`, the
> scheme-theoretic image of `g` is the strict transform along `b` of that of `f`.

```lean
theorem exists_iso_image_strictTransform
    {X Y S V X' : Scheme.{u}} (p : X ⟶ S) (q : Y ⟶ S)
    (U : X.Opens) (b : X' ⟶ X)
    (f : V ⟶ pullback p q) [QuasiCompact f]
    (g : V ⟶ pullback (b ≫ p) q)
    (hfU : Set.range (f ≫ pullback.fst p q).base ⊆ (U : Set X))
    (hbgX : g ≫ pullback.fst (b ≫ p) q ≫ b = f ≫ pullback.fst p q)
    (hbgY : g ≫ pullback.snd (b ≫ p) q = f ≫ pullback.snd p q)
    (hb : IsAdmissibleBlowup U b) :
    ∃ I : X.IdealSheafData,
      ∃ e : X' ≅ blowUp I,
        e.hom ≫ blowUpToBase I = b ∧
        Disjoint (U : Set X) (I.support : Set X) ∧
        ∃ (j : strictTransform (f.imageι ≫ pullback.fst p q) I ⟶ pullback (b ≫ p) q)
          (a : g.image ≅ strictTransform (f.imageι ≫ pullback.fst p q) I),
          j ≫ pullback.fst (b ≫ p) q ≫ e.hom =
            strictTransformι (f.imageι ≫ pullback.fst p q) I ≫
              pullback.snd (f.imageι ≫ pullback.fst p q) (blowUpToBase I) ∧
          j ≫ pullback.snd (b ≫ p) q =
            strictTransformι (f.imageι ≫ pullback.fst p q) I ≫
              pullback.fst (f.imageι ≫ pullback.fst p q) (blowUpToBase I) ≫
                f.imageι ≫ pullback.snd p q ∧
          a.hom ≫ j = g.imageι
```

## Tag 0F3Z, a lemma

[Tag 0F3Z](https://stacks.math.columbia.edu/tag/0F3Z) in the Stacks Project.

**`AlgebraicGeometry.exists_isAdmissibleBlowup_properExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Compactification/ProperExtension.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Compactification/ProperExtension.lean#L62).

> **Stacks Project, Tag 0F3Z.** After a `V`-admissible blowup `b : Y' ⟶ Y` of a
> compactification `j` of a quasi-compact open subscheme `V` of `U`, the blowup contains an open
> subscheme `V'` which maps properly to `U`, extending the inclusion of `V`, and whose copy of `V`
> is exactly the inverse image of the interior of the compactification.

```lean
theorem exists_isAdmissibleBlowup_properExtension
    {S U : Scheme.{u}} (f : U ⟶ S)
    [CompactSpace S] [QuasiSeparatedSpace S]
    [LocallyOfFiniteType f] [QuasiCompact f] [IsSeparated f]
    (V : U.Opens) [QuasiCompact V.ι]
    (j : CompactificationOf (Over.mk (V.ι ≫ f))) :
    ∃ (Y' : Scheme.{u}) (b : Y' ⟶ j.space) (V' : Y'.Opens)
      (e : V.toScheme ⟶ V'.toScheme) (p : V'.toScheme ⟶ U),
      Stacks.Blowup.IsAdmissibleBlowup j.immersion.opensRange b ∧
        IsOpenImmersion e ∧
        Set.range (e ≫ V'.ι).base =
          (b ⁻¹ᵁ j.immersion.opensRange : Y'.Opens) ∧
        e ≫ V'.ι ≫ b = j.immersion ∧
        IsProper p ∧
        e ≫ p = V.ι ∧ p ≫ f = V'.ι ≫ b ≫ j.toBase
```

## Tag 0F40, a lemma

[Tag 0F40](https://stacks.math.columbia.edu/tag/0F40) in the Stacks Project.

**`AlgebraicGeometry.hasCompactification_of_two_opens`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Compactification/TwoOpens.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Compactification/TwoOpens.lean#L162).

> **Stacks Project, Tag 0F40.** A separated finite-type scheme over a Noetherian base has a
> compactification as soon as it is covered by two compactifiable open subschemes whose
> intersection is dense.

```lean
theorem hasCompactification_of_two_opens
    {S U : Scheme.{u}} (f : U ⟶ S)
    [IsNoetherian S] [LocallyOfFiniteType f] [QuasiCompact f] [IsSeparated f]
    (U₁ U₂ : U.Opens) (hcover : U₁ ⊔ U₂ = ⊤)
    (hdense : Dense ((U₁ ⊓ U₂ : U.Opens) : Set U))
    (h₁ : HasCompactification (U₁.ι ≫ f)) (h₂ : HasCompactification (U₂.ι ≫ f)) :
    HasCompactification f
```

## Tag 0F41, a theorem

[Tag 0F41](https://stacks.math.columbia.edu/tag/0F41) in the Stacks Project.

**`AlgebraicGeometry.exists_quasiCompact_compactificationOf_of_isQuasiAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Compactification/QuasiAffineSource.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Compactification/QuasiAffineSource.lean#L86). The attribute's comment: “the case of a quasi-affine source”. References: SGA 4½ Arcata (4.5.3), “special case”; SGA 4½ Th finitude (2.8), “more general”; SGA 7 XIII (2.1.6), “2.1.6 c), special case”.

> **Nagata compactification for a quasi-affine source (Stacks Project, Tag 0F41).** A
> separated morphism of finite type from a quasi-affine scheme to a quasi-compact and
> quasi-separated scheme admits a compactification: a quasi-compact open immersion into a scheme
> proper over the base.
>
> The source statement has no quasi-affineness hypothesis; this is the case of its proof in which
> the source immerses into relative projective space directly, with no gluing along a covering.

```lean
theorem exists_quasiCompact_compactificationOf_of_isQuasiAffine
    {X S : Scheme.{u}} (f : X ⟶ S)
    [CompactSpace S] [QuasiSeparatedSpace S] [IsSeparated f]
    [LocallyOfFiniteType f] [QuasiCompact f] [X.IsQuasiAffine] :
    ∃ j : CompactificationOf (Over.mk f), QuasiCompact j.immersion
```

**`AlgebraicGeometry.hasCompactification_of_compactSpace_quasiSeparatedSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NagataCompactification/Basic.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NagataCompactification/Basic.lean#L152). References: SGA 4 XVII (3.2.2), “more general”; SGA 4 XVII (3.2.3), “(iii), special case”; SGA 4½ Th finitude (2.8), “more general”; SGA 7 XIII (2.1.6), “more general”.

> **Nagata compactification (Stacks Project, Tag 0F41).** Let `S` be a quasi-compact and
> quasi-separated scheme and let `f : X ⟶ S` be a separated morphism of finite type. Then `X` has a
> compactification over `S`: `f` factors as a quasi-compact open immersion of `X` into a scheme
> proper over `S`.
>
> [Stacks, Tag 01ZJ] factors `f` through a closed immersion into a separated morphism of finite
> presentation, and compactifiability descends along a closed immersion.

```lean
theorem hasCompactification_of_compactSpace_quasiSeparatedSpace {X S : Scheme.{u}} (f : X ⟶ S)
    [CompactSpace S] [QuasiSeparatedSpace S] [IsSeparated f] [LocallyOfFiniteType f]
    [QuasiCompact f] : HasCompactification f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.33, Tag 0F3T](https://stacks.math.columbia.edu/tag/0F3T)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
