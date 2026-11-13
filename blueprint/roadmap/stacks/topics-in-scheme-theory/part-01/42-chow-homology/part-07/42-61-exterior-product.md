---
declaration: section
origin: cited
lean: Stacks.Chow.exteriorProduct_mem_rationalEquivalences_right, Stacks.Chow.exteriorProduct_mem_rationalEquivalences_left, Stacks.Chow.chowExteriorProduct, Stacks.Chow.bivariantToBaseEval, Stacks.Chow.bivariantToBaseEval_injective, Stacks.Chow.bivariantToBaseEval_bijective_field, Stacks.Chow.bivariantToBaseEquivField, Stacks.Chow.bivariantChowClassToBaseEquivField
statement: formalized
proof: formalized
---

# 42.61 Exterior product

Section 42.61 of the Stacks Project, [Tag 0FBU](https://stacks.math.columbia.edu/tag/0FBU). 5 tags here are carried by 22 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FBV, a lemma

[Tag 0FBV](https://stacks.math.columbia.edu/tag/0FBV) in the Stacks Project.

**`Stacks.Chow.exteriorProduct_mem_rationalEquivalences_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductRationalEquivalence.lean, line 521](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductRationalEquivalence.lean#L521). The attribute's comment: “well defined in the second variable, unconditionally”.

> The exterior product of an `n`-cycle on `X` with an `m`-cycle on `Y` which is rationally
> equivalent to zero is rationally equivalent to zero.

```lean
theorem exteriorProduct_mem_rationalEquivalences_right (C : ChowSituation.{u}) [Subsingleton C.S]
    [IsIntegral C.S] [JacobsonSpace C.S]
    (hδ : ∀ s : C.S, IsClosed ({s} : Set C.S) → C.dimensionFunction s = 0)
    {X Y : Scheme.{u}} (f : X ⟶ C.S) [LocallyOfFiniteType f] (g : Y ⟶ C.S)
    [LocallyOfFiniteType g] (n m : ℤ)
    (α : CycleGroup C f n) {β : CycleGroup C g m} (hβ : β ∈ rationalEquivalences C g m) :
    exteriorProduct C f g n m α β ∈ rationalEquivalences C (pullback.fst f g ≫ f) (n + m)
```

**`Stacks.Chow.exteriorProduct_mem_rationalEquivalences_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductRationalEquivalence.lean, line 618](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductRationalEquivalence.lean#L618). The attribute's comment: “well defined in the first variable, unconditionally”.

> The exterior product of an `n`-cycle on `X` which is rationally equivalent to zero with an
> `m`-cycle on `Y` is rationally equivalent to zero.

```lean
theorem exteriorProduct_mem_rationalEquivalences_left (C : ChowSituation.{u}) [Subsingleton C.S]
    [IsIntegral C.S] [JacobsonSpace C.S]
    (hδ : ∀ s : C.S, IsClosed ({s} : Set C.S) → C.dimensionFunction s = 0)
    {X Y : Scheme.{u}} (f : X ⟶ C.S) [LocallyOfFiniteType f] (g : Y ⟶ C.S)
    [LocallyOfFiniteType g] (n m : ℤ)
    {α : CycleGroup C f n} (hα : α ∈ rationalEquivalences C f n) (β : CycleGroup C g m) :
    exteriorProduct C f g n m α β ∈ rationalEquivalences C (pullback.fst f g ≫ f) (n + m)
```

**`Stacks.Chow.chowExteriorProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductRationalEquivalence.lean, line 707](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductRationalEquivalence.lean#L707).

> The exterior product on Chow groups,
>
>   `× : CH_n(X) ⊗_ℤ CH_m(Y) ⟶ CH_{n+m}(X ×_k Y)`,
>
> for `X` and `Y` locally of finite type over a field: the exterior product of cycles,
> `Stacks.Chow.exteriorProduct`, read modulo rational equivalence.

```lean
def chowExteriorProduct (C : ChowSituation.{u}) [Subsingleton C.S] [IsIntegral C.S]
    [JacobsonSpace C.S] (hδ : ∀ s : C.S, IsClosed ({s} : Set C.S) → C.dimensionFunction s = 0)
    {X Y : Scheme.{u}} (f : X ⟶ C.S) [LocallyOfFiniteType f] (g : Y ⟶ C.S)
    [LocallyOfFiniteType g] (n m : ℤ) :
    TensorProduct ℤ (chowGroup C f n) (chowGroup C g m) →+
      chowGroup C (pullback.fst f g ≫ f) (n + m)
```

## Tag 0FBW, a lemma

[Tag 0FBW](https://stacks.math.columbia.edu/tag/0FBW) in the Stacks Project.

**`Stacks.Chow.bivariantToBaseEval`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyOverField.lean, line 186](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyOverField.lean#L186). The attribute's comment: “the canonical map A^p(X → Spec k) → CH\_\{-p}(X), cap product with the fundamental class of the point”.

> **Stacks 0FBW.** The canonical map `A^p(X ⟶ Spec k) ⟶ CH_{-p}(X)`: cap product with the
> fundamental class of the point, read through the collapse of `X ×_{Spec k} Spec k` onto `X` along
> its first projection. It is injective by `Stacks.Chow.bivariantToBaseEval_injective`;
> surjectivity is not proved here, see the implementation notes of this module.

```lean
def bivariantToBaseEval : bivariantToBase C G sX p →+ chowGroup C sX (-p)
```

**`Stacks.Chow.bivariantToBaseEval_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyOverField.lean, line 303](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyOverField.lean#L303). The attribute's comment: “injectivity of the canonical identification, for the base being the spectrum of a field; hS1 is Stacks 02S1 and hfund is Stacks 02NK with Stacks 02R4”.

> **Stacks 0FBW, injectivity.** The canonical map `A^p(X ⟶ Spec k) ⟶ CH_{-p}(X)` of Stacks 0FBW
> is injective: a bivariant class of degree `p` for the structure morphism of `X` is determined by
> its cap product with the fundamental class of the point. Surjectivity is not proved here; see the
> implementation notes of this module.

```lean
theorem bivariantToBaseEval_injective
    [Subsingleton C.S] [IsIntegral C.S] (hS1 : FlatPullbackDescends C)
    (hfund : IntegralFundamentalClassIsFlatPullback C hS1) :
    Function.Injective (bivariantToBaseEval C G sX p)
```

**`Stacks.Chow.bivariantToBaseEval_bijective_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyOverFieldIso.lean, line 412](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyOverFieldIso.lean#L412). The attribute's comment: “the canonical map A^p(X → Spec k) → CH\_\{-p}(X), c ↦ c ∩ [Spec k], is bijective”.

> Let `k` be a field and `X` a scheme locally of finite type over `k`. For
> every `p ∈ ℤ` the canonical map `A^p(X ⟶ Spec k) ⟶ CH_{-p}(X)`, `c ↦ c ∩ [Spec k]`, is
> bijective. Here `A^p(X ⟶ Spec k)` is the group of bivariant classes of degree `p` for the
> structure morphism (Stacks 0B76), read at the Gysin system of the first Chern class of an
> invertible module, and the cap product with the fundamental class of the point is read on `X`
> through the first projection `X ×_{Spec k} Spec k ≅ X`.

```lean
theorem bivariantToBaseEval_bijective_field (p : ℤ) :
    Function.Bijective
      (bivariantToBaseEval (fieldChowSituation k)
        (gysinSystemOfInvertible (fieldChowSituation k)) sX p)
```

**`Stacks.Chow.bivariantToBaseEquivField`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyOverFieldIso.lean, line 426](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyOverFieldIso.lean#L426). The attribute's comment: “the canonical identification A^p(X → Spec k) = CH\_\{-p}(X) as an isomorphism of groups”.

> The canonical identification `A^p(X ⟶ Spec k) = CH_{-p}(X)` over a field,
> as an isomorphism of abelian groups: cap product with the fundamental class of the point.

```lean
def bivariantToBaseEquivField (p : ℤ) :
    bivariantToBase (fieldChowSituation k) (gysinSystemOfInvertible (fieldChowSituation k)) sX p ≃+
      chowGroup (fieldChowSituation k) sX (-p)
```

**`Stacks.Chow.bivariantChowClassToBaseEquivField`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyOverFieldIso.lean, line 446](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyOverFieldIso.lean#L446). The attribute's comment: “the canonical identification A^p(X → Spec k) = CH\_\{-p}(X), c ↦ c ∩ [Spec k], for the bivariant group of Stacks 0B76 whose cap operations are maps”.

> For the bivariant group `A^p(X ⟶ Spec k)` of Stacks 0B76 in the form
> `Stacks.Chow.BivariantChowClass`, whose cap operations are plain maps, cap product with the
> fundamental class of the point is an isomorphism `A^p(X ⟶ Spec k) ≃ CH_{-p}(X)`.

```lean
def bivariantChowClassToBaseEquivField (p : ℤ) :
    BivariantChowClass (fieldChowSituation k) sX (𝟙 (fieldChowSituation k).S) sX
        (Category.comp_id sX) p ≃+
      chowGroup (fieldChowSituation k) sX (-p)
```

**`Stacks.Chow.bivariantToBaseEval_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyOverFieldSurjective.lean, line 246](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyOverFieldSurjective.lean#L246). The attribute's comment: “surjectivity of the canonical identification; hEPK is Stacks 0EPK, hgen is the generation of Chow homology by proper pushforwards of flat pullbacks of the class of the point (Stacks 02UC with Stacks 02R4), hS1 is Stacks 02S1, hpp is Stacks 02S2, hRG is Stacks 02RG and h71 is Stacks 0B71 in every relative dimension”.

> The canonical map `A^p(X ⟶ Spec k) ⟶ CH_{-p}(X)`, cap product with the fundamental class of the
> point, is surjective. The hypotheses are the existence of proper pushforwards of bivariant classes
> (`hEPK`, Stacks 0EPK), the generation of `CH_{-p}(X)` by proper pushforwards of flat pullbacks of
> `[Spec k]` (`hgen`), the descent of flat pullback and proper pushforward to Chow groups (`hS1`,
> `hpp`), Stacks 02RG (`hRG`) and Stacks 0B71 in every relative dimension (`h71`).

```lean
theorem bivariantToBaseEval_surjective (hS1 : FlatPullbackDescends C)
    (hRG : ProperPushforwardFlatPullbackBaseChange C) (hpp : ProperPushforwardDescends C)
    (h71 : ∀ r : ℕ, G.FlatPullbackNaturality r)
    (hEPK : BivariantProperPushforwardExists C G)
    (hgen : ChowClassesGeneratedByBaseFlatPullbacks C hS1 hpp) :
    Function.Surjective (bivariantToBaseEval C G sX p)
```

**`Stacks.Chow.bivariantToBaseEval_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyOverFieldSurjective.lean, line 270](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyOverFieldSurjective.lean#L270). The attribute's comment: “the canonical identification A^p(X → Spec k) = CH\_\{-p}(X), for the base being the spectrum of a field; hEPK is Stacks 0EPK, hgen is Stacks 02R4, hS1 is Stacks 02S1, hpp is Stacks 02S2, hRG is Stacks 02RG, h71 is Stacks 0B71 and hfund is Stacks 02NK with Stacks 02R4”.

> The canonical map `A^p(X ⟶ Spec k) ⟶ CH_{-p}(X)` is bijective when the base has one point and
> is integral, that is, is the spectrum of a field: cap product with the fundamental class of the
> point identifies the bivariant classes of degree `p` for the structure morphism of `X` with the
> Chow homology of `X` in degree `-p`. The hypotheses are those of
> `Stacks.Chow.bivariantToBaseEval_injective` and `Stacks.Chow.bivariantToBaseEval_surjective`.

```lean
theorem bivariantToBaseEval_bijective
    [Subsingleton C.S] [IsIntegral C.S] (hS1 : FlatPullbackDescends C)
    (hfund : IntegralFundamentalClassIsFlatPullback C hS1)
    (hRG : ProperPushforwardFlatPullbackBaseChange C) (hpp : ProperPushforwardDescends C)
    (h71 : ∀ r : ℕ, G.FlatPullbackNaturality r)
    (hEPK : BivariantProperPushforwardExists C G)
    (hgen : ChowClassesGeneratedByBaseFlatPullbacks C hS1 hpp) :
    Function.Bijective (bivariantToBaseEval C G sX p)
```

**`Stacks.Chow.bivariantToBaseEval_bijective_of_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyOverFieldUnconditional.lean, line 384](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyOverFieldUnconditional.lean#L384). The attribute's comment: “the bivariant classes are those of the Gysin system of invertible modules, `Stacks.Chow.gysinSystemOfInvertible`”.

> **Stacks 0FBW.** Let `X` be locally of finite type over a field `k`. Cap product with the
> fundamental class of the point, `A^p(X ⟶ Spec k) ⟶ CH_{-p}(X)`, is bijective.

```lean
theorem bivariantToBaseEval_bijective_of_field :
    Function.Bijective (bivariantToBaseEval (fieldChowSituation k)
      (gysinSystemOfInvertible (fieldChowSituation k)) sX p)
```

**`Stacks.Chow.bivariantToBaseEquivOfField`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyOverFieldUnconditional.lean, line 399](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyOverFieldUnconditional.lean#L399). The attribute's comment: “the bivariant classes are those of the Gysin system of invertible modules, `Stacks.Chow.gysinSystemOfInvertible`”.

> **Stacks 0FBW.** For `X` locally of finite type over a field `k`, the identification
> `A^p(X ⟶ Spec k) ≃ CH_{-p}(X)`, `c ↦ c ∩ [Spec k]`, as an isomorphism of groups.

```lean
def bivariantToBaseEquivOfField :
    bivariantToBase (fieldChowSituation k) (gysinSystemOfInvertible (fieldChowSituation k)) sX p ≃+
      chowGroup (fieldChowSituation k) sX (-p)
```

## Tag 0FBX, a lemma

[Tag 0FBX](https://stacks.math.columbia.edu/tag/0FBX) in the Stacks Project.

**`Stacks.Chow.bivariantCommute_bivariantToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/PointClassCommuting.lean, line 649](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/PointClassCommuting.lean#L649). The attribute's comment: “a bivariant class towards the point commutes with every bivariant class, in the form of Stacks 0FA2, for the base being the spectrum of a field; hfund, hEPK and hgen are the prerequisites of Stacks 0FBW, hS1 is Stacks 02S1, hpp is Stacks 02S2, hRG is Stacks 02RG, h71 is Stacks 0B71 and hgys is the isomorphism case of Stacks 02TA”.

> **Stacks 0FBX.** Let `c ∈ A^p(X ⟶ S)` be a bivariant class towards the point and let
> `c' ∈ A^q(Y ⟶ Z)` be an arbitrary bivariant class, for an arbitrary morphism `f : Y ⟶ Z` of
> schemes locally of finite type over the base. Then the base change of `c` to `Z` and `c'`
> commute, in the sense of Stacks 0FA2.
>
> The proof is the source's. By Stacks 0FBW the map `c ↦ c ∩ [Spec k]` is a bijection of
> `A^p(X ⟶ S)` with `CH_{-p}(X)`, and `CH_{-p}(X)` is generated by proper pushforwards of flat
> pullbacks of the class of the point; so `c` is a `ℤ`-combination of classes `g\_* ∘ (flat
> pullback)`. Commuting with `c'` is preserved by `ℤ`-combinations, so it is enough to treat one
> such class. Its base change to `Z` is again a proper pushforward of a flat-pullback class, by
> `Stacks.Chow.isBivariantProperPushforward_bivariantToBaseRestriction`; that flat-pullback class
> commutes with `c'` by the flat law of Stacks 0B76, which is
> `Stacks.Chow.bivariantCommute_flatPullbackBivariantClass`; and proper pushforward preserves
> commuting by `Stacks.Chow.bivariantCommute_of_isBivariantProperPushforward`.
>
> Nothing here assumes that `c` and `c'` commute, nor that any other pair of classes does; the
> hypotheses are the prerequisites of Stacks 0FBW together with the descent statements this part of
> the library quantifies rather than parameterizes.

```lean
theorem bivariantCommute_bivariantToBase [Subsingleton C.S] [IsIntegral C.S]
    (c : bivariantToBase C G sX p)
    (c' : BivariantClass C G (f ≫ sZ) sZ f rfl q)
    (hpp : ProperPushforwardDescends C) (hS1 : FlatPullbackDescends C)
    (hRG : ProperPushforwardFlatPullbackBaseChange C)
    (h71 : ∀ r : ℕ, G.FlatPullbackNaturality r)
    (hEPK : BivariantProperPushforwardExists C G)
    (hgen : ChowClassesGeneratedByBaseFlatPullbacks C hS1 hpp)
    (hfund : IntegralFundamentalClassIsFlatPullback C hS1) :
    BivariantCommute C G sZ (pullback.snd sX sZ) f p q
      (bivariantToBaseRestrictionHom C G sX sZ p hgys c) c'
```

**`Stacks.Chow.bivariantToBase_commuteCompositeCap_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/PointClassCommuting.lean, line 722](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/PointClassCommuting.lean#L722). The attribute's comment: “the equality of the two composites c ∘ c' = c' ∘ c of the tag, as operations on every test Chow group; the hypotheses are those of Stacks.Chow.bivariantCommute\_bivariantToBase”.

> **Stacks 0FBX, in the shape the tag states it.** The two composites `c ∘ c'` and `c' ∘ c`,
> both bivariant classes of degree `p + q` for `X ×_S Y ⟶ Z`, agree as operations on every test
> Chow group, under the canonical identification of their sources and the equality `p + q = q + p`
> of their degrees.
>
> This is `Stacks.Chow.bivariantCommute_bivariantToBase` read through
> `Stacks.Chow.bivariantCommute_iff_commuteCompositeCap_eq`, the equivalence of Stacks 0FA2 between
> commuting and the equality of the two composites.

```lean
theorem bivariantToBase_commuteCompositeCap_eq [Subsingleton C.S] [IsIntegral C.S]
    (c : bivariantToBase C G sX p)
    (c' : BivariantClass C G (f ≫ sZ) sZ f rfl q)
    (hpp : ProperPushforwardDescends C) (hS1 : FlatPullbackDescends C)
    (hRG : ProperPushforwardFlatPullbackBaseChange C)
    (h71 : ∀ r : ℕ, G.FlatPullbackNaturality r)
    (hEPK : BivariantProperPushforwardExists C G)
    (hgen : ChowClassesGeneratedByBaseFlatPullbacks C hS1 hpp)
    (hfund : IntegralFundamentalClassIsFlatPullback C hS1) :
    ∀ {T : Scheme.{u}} (t : T ⟶ Z) [LocallyOfFiniteType t] (k : ℤ)
      (α : chowGroup C (t ≫ sZ) k),
      chowPushforwardOfIso C
          (pullback.fst (pullback.snd (pullback.snd sX sZ) f ≫ f) t ≫
            (pullback.fst (pullback.snd sX sZ) f ≫ (pullback.snd sX sZ ≫ sZ)))
          (pullback.fst (pullback.snd f (pullback.snd sX sZ) ≫ pullback.snd sX sZ) t ≫
            (pullback.fst f (pullback.snd sX sZ) ≫ (f ≫ sZ)))
          (compositeComparisonHom (pullback.snd sX sZ) f t)
          (compositeComparisonHom_comp_structureMorphism C sZ (pullback.snd sX sZ) f t)
          ((k - q) - p)
          (commuteCompositeCap C G sZ (pullback.snd sX sZ) f p q
            (bivariantToBaseRestrictionHom C G sX sZ p hgys c) c' hgys hpp t k α) =
        chowGroupDegreeEquiv C
          (pullback.fst (pullback.snd f (pullback.snd sX sZ) ≫ pullback.snd sX sZ) t ≫
            (pullback.fst f (pullback.snd sX sZ) ≫ (f ≫ sZ)))
          (by ring : (k - p) - q = (k - q) - p)
          (commuteCompositeCap C G sZ f (pullback.snd sX sZ) q p c'
            (bivariantToBaseRestrictionHom C G sX sZ p hgys c) hgys hpp t k α)
```

**`Stacks.Chow.BivariantChowClass.comp_comm_of_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/PointClassCommutingField.lean, line 773](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/PointClassCommutingField.lean#L773). The attribute's comment: “c ∘ c' = c' ∘ c in A^\{p+q}(X ×\_k Y → Z) for c ∈ A^p(X → Spec k) and c' ∈ A^q(Y → Z), the composites read as in Stacks 0FA2”.

> **Stacks 0FBX.** Let `k` be a field and let `X` be a scheme locally of finite type over `k`.
> Let `c ∈ A^p(X ⟶ Spec k)`. Let `f : Y ⟶ Z` be a morphism of schemes locally of finite type over
> `k` and let `c' ∈ A^q(Y ⟶ Z)`. Then `c ∘ c' = c' ∘ c` in `A^{p+q}(X ×_k Y ⟶ Z)`.
>
> Here `c ∘ c' = res(c) ∘ c'` with `res(c) ∈ A^p(X ×_k Y ⟶ Y)` the restriction of `c` along
> `Y ⟶ Spec k`, and `c' ∘ c = res(c') ∘ res(c)` with `res(c) ∈ A^p(X ×_k Z ⟶ Z)` the restriction of
> `c` along `Z ⟶ Spec k` and `res(c') ∈ A^q(Y ×_Z (X ×_k Z) ⟶ X ×_k Z)` the restriction of `c'`
> along `X ×_k Z ⟶ Z` (Stacks 0F9Z, 0FA2). The second composite lives on `Y ×_Z (X ×_k Z)` and in
> degree `q + p`; it is read on `X ×_k Y` through the canonical isomorphism and in degree `p + q`.

```lean
theorem BivariantChowClass.comp_comm_of_field
    (c : BivariantChowClass (fieldChowSituation k) sX (𝟙 (fieldChowSituation k).S) sX
      (Category.comp_id sX) p)
    (c' : BivariantChowClass (fieldChowSituation k) sY sZ f hf q) :
    (c.restrict sY (Category.comp_id sY)).comp c' =
      (((c'.restrict (pullback.snd sX sZ)
          (BivariantChowClass.restrict_structure_eq (Category.comp_id sX) sZ
            (Category.comp_id sZ))).comp
        (c.restrict sZ (Category.comp_id sZ))).degreeCongr (add_comm q p)).transport
        (comp_comp_structureMorphism_eq
          (BivariantChowClass.restrict_structure_eq (Category.comp_id sX) sY
            (Category.comp_id sY)) hf)
        (pointClassCompositeIso (fieldChowSituation k) sX sZ f hf)
        (pointClassCompositeIso_hom_comp (fieldChowSituation k) sX sZ f hf)
```

## Tag 0FBY, a remark

[Tag 0FBY](https://stacks.math.columbia.edu/tag/0FBY) in the Stacks Project.

**`Stacks.Chow.commutesExteriorProductCapAt_fundamentalChowClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductCapCommuting.lean, line 633](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductCapCommuting.lean#L633). The attribute's comment: “the equation α × (c ∩ β) = c ∩ (α × β) of the tag, for α the fundamental class of an integral scheme X flat of relative dimension d over the base — NOT for a general α ∈ CH\_n(X), for which the missing inputs are recorded in the module notes; carries Stacks 02S1 as hfp, Stacks 02RG on Chow groups as hRG, and Stacks 0B71 with the identification of Stacks 0B6Y as h71, these being exactly the hypotheses of Stacks 0B78 in this repository”.

> **Stacks 0FBY for the fundamental class of an integral scheme flat over the base.** Let the
> base be the spectrum of a field, let `X` be integral and flat over it of relative dimension `d`,
> let `u : Y ⟶ Z` be a morphism of schemes locally of finite type over the base and let
> `c ∈ A^p(Y ⟶ Z)` be a bivariant class. Then for every `β ∈ CH_m(Z)`
>
>   `[X] × (c ∩ β) = c ∩ ([X] × β)`
>
> in `CH_{d + (m - p)}(X ×_S Y)`, where `[X] ∈ CH_d(X)` is the fundamental class of `X` and the two
> sides are read through the canonical identifications of `Stacks.Chow.exteriorProductCap` and
> `Stacks.Chow.capExteriorProduct`.
>
> The first variable is a fundamental class and not a general `α ∈ CH_n(X)`; see the implementation
> notes of `StacksFrontier.AlgebraicGeometry.Chow.ExteriorProductCapCommuting` for what the general
> case needs and for why it is unavailable here.
>
> The proof replaces `[X] × -` by the cap operation of the flat-pullback class of Stacks 0B78 for
> the structure morphism of `X`, whose base change to `Z` is the flat-pullback class for
> `pr_Z : X ×_S Z ⟶ Z`, and that class commutes with `c` by the smooth half of Stacks 0FF6. The
> commuting identity is then instantiated at the test scheme `𝟙 Z` and both of its sides are
> transported to `X ×_S Y`.

```lean
theorem commutesExteriorProductCapAt_fundamentalChowClass
    (c : BivariantClass C G sY sZ u hu p)
    (hfr : AlgebraicGeometry.RelativeDimension sX d)
    (hd : relativeDimension C.dimensionFunction sX (genericPoint X) = (d : ℤ))
    (hRG : ProperPushforwardFlatPullbackBaseChange C) (h71 : G.FlatPullbackNaturality d) :
    CommutesExteriorProductCapAt C hδ G sX sY sZ u hu p c (d : ℤ) m
      (fundamentalChowClass C sX (d : ℤ))
```

**`Stacks.Chow.commutesExteriorProductCap_of_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductCapCommutingEveryCap.lean, line 889](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductCapCommutingEveryCap.lean#L889). The attribute's comment: “the bivariant classes are those of the Gysin system of invertible modules, `Stacks.Chow.gysinSystemOfInvertible`”.

> **Stacks 0FBY over a field.** Let `k` be a field, `X` locally of finite type over `k`,
> `u : Y ⟶ Z` a morphism of schemes locally of finite type over `k`, and `c ∈ A^p(Y ⟶ Z)`. Then
>
>   `α × (c ∩ β) = c ∩ (α × β)`   in   `CH_{n + (m - p)}(X ×_k Y)`
>
> for every `α ∈ CH_n(X)` and every `β ∈ CH_m(Z)`.

```lean
theorem commutesExteriorProductCap_of_field (n m : ℤ) :
    CommutesExteriorProductCap (fieldChowSituation k) (fun _ _ ↦ rfl)
      (gysinSystemOfInvertible (fieldChowSituation k)) sX sY sZ u hu p c n m
```

**`Stacks.Chow.commutesExteriorProductCap_of_subsingleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductCapCommutingGeneral.lean, line 429](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductCapCommutingGeneral.lean#L429). The attribute's comment: “α × (c ∩ β) = c ∩ (α × β) in CH\_*(X ×\_S Y), over a base which is a point with dimension function zero (in particular Spec k), for bivariant classes at any Gysin system”.

> **Stacks 0FBY over a point.** Let the base be a point with dimension function zero, for
> instance the spectrum of a field, let `X` be locally of finite type over it, let `u : Y ⟶ Z` be a
> morphism of schemes locally of finite type over it and let `c ∈ A^p(Y ⟶ Z)` be a bivariant class
> for any Gysin system. Then for all `α ∈ CH_n(X)` and `β ∈ CH_m(Z)`
>
>   `α × (c ∩ β) = c ∩ (α × β)`   in   `CH_{n + (m - p)}(X ×_S Y)`.
>
> Write `α = ∑ₓ nₓ [closure {x}]`. Then `α × β` is the locally finite sum over the points `x` of the
> support of `α` of the pushforwards along `closure {x} ×_S Z ⟶ X ×_S Z` of the flat pullbacks of
> `nₓ β` along the flat projections `closure {x} ×_S Z ⟶ Z`. Capping with `c` commutes with each of
> these flat pullbacks by the flat-pullback axiom of Stacks 0B76, and with the locally finite sum by
> `Stacks.Chow.BivariantClass.cap_chowGroupCongr_mk_eq_mk_of_locallyFinite`; the result is the
> corresponding decomposition of `α × (c ∩ β)`.

```lean
theorem commutesExteriorProductCap_of_subsingleton (c : BivariantClass C G sY sZ u hu p)
    (n m : ℤ) : CommutesExteriorProductCap C hδ G sX sY sZ u hu p c n m
```

**`Stacks.Chow.exteriorProductCap_eq_capExteriorProduct_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductCapCommutingGeneral.lean, line 571](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductCapCommutingGeneral.lean#L571). The attribute's comment: “α × (c' ∩ β) = c' ∩ (α × β) in CH\_*(X ×\_k Y), for k a field and c' ∈ A^q(Y → Z) of Stacks 0B76”.

> **Stacks 0FBY.** Let `k` be a field, let `X` be a scheme locally of finite type over `k`, let
> `u : Y ⟶ Z` be a morphism of schemes locally of finite type over `k` and let
> `c' ∈ A^q(Y ⟶ Z)`. Then for `α ∈ CH_n(X)` and `β ∈ CH_m(Z)`
>
>   `α × (c' ∩ β) = c' ∩ (α × β)`   in   `CH_{n + (m - q)}(X ×_k Y)`.
>
> Here `A^q(Y ⟶ Z)` is the group of bivariant classes of Stacks 0B76, the exterior product is that
> of Stacks 0FBV, and the two sides are those of `Stacks.Chow.exteriorProductCap` and
> `Stacks.Chow.capExteriorProduct`: `c' ∩ β` is read on `Y ≅ Y ×_Z Z`, and `c' ∩ (α × β)` is the
> cap at the test scheme `X ×_k Z ⟶ Z`, read on `X ×_k Y ≅ Y ×_Z (X ×_k Z)`.

```lean
theorem exteriorProductCap_eq_capExteriorProduct_field
    (c' : BivariantChowClass (fieldChowSituation k) sY sZ u hu q) (n m : ℤ)
    (α : chowGroup (fieldChowSituation k) sX n) (β : chowGroup (fieldChowSituation k) sZ m) :
    haveI := BivariantChowClass.locallyOfFiniteType_of_structure sZ u hu
    exteriorProductCap (fieldChowSituation k) (fun _ _ ↦ rfl)
        (gysinSystemOfInvertible (fieldChowSituation k)) sX sY sZ u hu q
        (BivariantChowClass.equivBivariantClass c') n m α β =
      capExteriorProduct (fieldChowSituation k) (fun _ _ ↦ rfl)
        (gysinSystemOfInvertible (fieldChowSituation k)) sX sY sZ u hu q
        (BivariantChowClass.equivBivariantClass c') n m α β
```

## Tag 0FBZ, a lemma

[Tag 0FBZ](https://stacks.math.columbia.edu/tag/0FBZ) in the Stacks Project.

**`Stacks.Chow.chowExteriorProduct_assoc_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductAssociativity.lean, line 1105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductAssociativity.lean#L1105).

> **Stacks 0FBZ.** The exterior product on Chow groups is associative. Let `k` be a field, let
> `X`, `Y` and `Z` be schemes locally of finite type over `k` and let `a ∈ CH_n(X)`,
> `b ∈ CH_m(Y)`, `c ∈ CH_l(Z)`. Then
>
>   `(a × b) × c = a × (b × c)`
>
> in `CH_{n + m + l}(X ×_k Y ×_k Z)`.
>
> The two sides are formed on the two bracketings of the triple product and in the two bracketings
> of the degree, so the left-hand side is carried into the group of the right-hand side by
> pushforward along the associator `Stacks.Chow.tripleProductAssoc`, which is an isomorphism over
> the base by `Stacks.Chow.tripleProductAssoc_hom_comp_base`, followed by
> `Stacks.Chow.chowGroupDegreeEquiv` for the degrees `(n + m) + l` and `n + (m + l)`. Both of those
> transports are the identity on cycle coefficients, so what is asserted is the source's identity.
>
> On classes of cycles it is `Stacks.Chow.exteriorProduct_assoc`, the cycle-level identity, read
> modulo rational equivalence. Nothing is assumed beyond the base being the spectrum of a field:
> the exterior product on Chow groups, `Stacks.Chow.chowExteriorProduct`, is itself unconditional
> over such a base, the instances of Stacks 02S1 that make it well defined being discharged inside
> it by `Stacks.Chow.flatPullbackFactorsThroughRationalEquivalenceOnPointClosureFibres_holds`.

```lean
theorem chowExteriorProduct_assoc_unconditional (k : Type u) [Field k] {X Y Z : Scheme.{u}}
    (f : X ⟶ (fieldChowSituation k).S) [LocallyOfFiniteType f]
    (g : Y ⟶ (fieldChowSituation k).S) [LocallyOfFiniteType g]
    (h : Z ⟶ (fieldChowSituation k).S) [LocallyOfFiniteType h] (n m l : ℤ)
    (a : chowGroup (fieldChowSituation k) f n)
    (b : chowGroup (fieldChowSituation k) g m)
    (c : chowGroup (fieldChowSituation k) h l) :
    chowGroupDegreeEquiv (fieldChowSituation k)
        (pullback.fst f (pullback.fst g h ≫ g) ≫ f) (add_assoc n m l)
        (chowPushforwardOfIso (fieldChowSituation k)
          (pullback.fst (pullback.fst f g ≫ f) h ≫ pullback.fst f g ≫ f)
          (pullback.fst f (pullback.fst g h ≫ g) ≫ f) (tripleProductAssoc f g h).hom
          (tripleProductAssoc_hom_comp_base f g h) (n + m + l)
          (chowExteriorProduct (fieldChowSituation k) (fun _ _ ↦ rfl)
            (pullback.fst f g ≫ f) h (n + m) l
            (TensorProduct.tmul ℤ
              (chowExteriorProduct (fieldChowSituation k) (fun _ _ ↦ rfl) f g n m
                (TensorProduct.tmul ℤ a b)) c))) =
      chowExteriorProduct (fieldChowSituation k) (fun _ _ ↦ rfl) f (pullback.fst g h ≫ g) n
        (m + l)
        (TensorProduct.tmul ℤ a
          (chowExteriorProduct (fieldChowSituation k) (fun _ _ ↦ rfl) g h m l
            (TensorProduct.tmul ℤ b c)))
```

**`Stacks.Chow.chowExteriorProduct_assoc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductAssociativity.lean, line 1175](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductAssociativity.lean#L1175).

> **Stacks 0FBZ.** The exterior product on Chow groups is associative. Let `k` be a field, let
> `X`, `Y` and `Z` be schemes locally of finite type over `k` and let `a ∈ CH_n(X)`,
> `b ∈ CH_m(Y)`, `c ∈ CH_l(Z)`. Then
>
>   `(a × b) × c = a × (b × c)`
>
> in `CH_{n + m + l}(X ×_k Y ×_k Z)`.
>
> The two sides are formed on the two bracketings of the triple product and in the two bracketings
> of the degree, so the left-hand side is carried into the group of the right-hand side by
> pushforward along the associator `Stacks.Chow.tripleProductAssoc`, which is an isomorphism over
> the base by `Stacks.Chow.tripleProductAssoc_hom_comp_base`, followed by
> `Stacks.Chow.chowGroupDegreeEquiv` for the degrees `(n + m) + l` and `n + (m + l)`. Both of those
> transports are the identity on cycle coefficients, so what is asserted is the source's identity.
>
> On classes of cycles it is `Stacks.Chow.exteriorProduct_assoc`, the cycle-level identity, read
> modulo rational equivalence. Nothing is assumed: it is
> `Stacks.Chow.chowExteriorProduct_assoc_unconditional`.

```lean
theorem chowExteriorProduct_assoc (k : Type u) [Field k] {X Y Z : Scheme.{u}}
    (f : X ⟶ (fieldChowSituation k).S) [LocallyOfFiniteType f]
    (g : Y ⟶ (fieldChowSituation k).S) [LocallyOfFiniteType g]
    (h : Z ⟶ (fieldChowSituation k).S) [LocallyOfFiniteType h] (n m l : ℤ)
    (a : chowGroup (fieldChowSituation k) f n)
    (b : chowGroup (fieldChowSituation k) g m)
    (c : chowGroup (fieldChowSituation k) h l) :
    chowGroupDegreeEquiv (fieldChowSituation k)
        (pullback.fst f (pullback.fst g h ≫ g) ≫ f) (add_assoc n m l)
        (chowPushforwardOfIso (fieldChowSituation k)
          (pullback.fst (pullback.fst f g ≫ f) h ≫ pullback.fst f g ≫ f)
          (pullback.fst f (pullback.fst g h ≫ g) ≫ f) (tripleProductAssoc f g h).hom
          (tripleProductAssoc_hom_comp_base f g h) (n + m + l)
          (chowExteriorProduct (fieldChowSituation k) (fun _ _ ↦ rfl)
            (pullback.fst f g ≫ f) h (n + m) l
            (TensorProduct.tmul ℤ
              (chowExteriorProduct (fieldChowSituation k) (fun _ _ ↦ rfl) f g n m
                (TensorProduct.tmul ℤ a b)) c))) =
      chowExteriorProduct (fieldChowSituation k) (fun _ _ ↦ rfl) f (pullback.fst g h ≫ g) n
        (m + l)
        (TensorProduct.tmul ℤ a
          (chowExteriorProduct (fieldChowSituation k) (fun _ _ ↦ rfl) g h m l
            (TensorProduct.tmul ℤ b c)))
```

**`Stacks.Chow.totalChowExteriorProduct_assoc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductTotalAssociativity.lean, line 154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductTotalAssociativity.lean#L154).

> **Stacks 0FBZ.** Exterior product is associative. Let `k` be a field, let `X`, `Y`, `Z` be
> schemes locally of finite type over `k`, and let `α ∈ CH_*(X)`, `β ∈ CH_*(Y)`, `γ ∈ CH_*(Z)`.
> Then `(α × β) × γ = α × (β × γ)` in `CH_*(X ×_k Y ×_k Z)`, the left-hand side being carried
> from `(X ×_k Y) ×_k Z` to `X ×_k (Y ×_k Z)` by pushforward along the associator of the fibre
> product.

```lean
theorem totalChowExteriorProduct_assoc (k : Type u) [Field k] {X Y Z : Scheme.{u}}
    (f : X ⟶ (fieldChowSituation k).S) [LocallyOfFiniteType f]
    (g : Y ⟶ (fieldChowSituation k).S) [LocallyOfFiniteType g]
    (h : Z ⟶ (fieldChowSituation k).S) [LocallyOfFiniteType h]
    (α : DirectSum ℤ fun n : ℤ ↦ chowGroup (fieldChowSituation k) f n)
    (β : DirectSum ℤ fun m : ℤ ↦ chowGroup (fieldChowSituation k) g m)
    (γ : DirectSum ℤ fun l : ℤ ↦ chowGroup (fieldChowSituation k) h l) :
    totalChowPushforwardOfIso (fieldChowSituation k)
        (pullback.fst (pullback.fst f g ≫ f) h ≫ pullback.fst f g ≫ f)
        (pullback.fst f (pullback.fst g h ≫ g) ≫ f) (tripleProductAssoc f g h).hom
        (tripleProductAssoc_hom_comp_base f g h)
        (totalChowExteriorProduct (fieldChowSituation k) (dimensionFunction_eq_zero_of_isClosed k)
          (pullback.fst f g ≫ f) h
          (totalChowExteriorProduct (fieldChowSituation k)
            (dimensionFunction_eq_zero_of_isClosed k) f g α β) γ) =
      totalChowExteriorProduct (fieldChowSituation k) (dimensionFunction_eq_zero_of_isClosed k) f
        (pullback.fst g h ≫ g) α
        (totalChowExteriorProduct (fieldChowSituation k)
          (dimensionFunction_eq_zero_of_isClosed k) g h β γ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.61, Tag 0FBU](https://stacks.math.columbia.edu/tag/0FBU)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
