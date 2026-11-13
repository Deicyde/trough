---
declaration: section
origin: cited
lean: Stacks.Chow.GysinAtInfinity.properPushforward_localizedPowerSumClassAtInfinity, Stacks.Chow.modificationPowerSum, Stacks.Chow.modificationChernClass, Stacks.Chow.properPushforwardChowCohomology_modificationPowerSum, Stacks.Chow.properPushforwardChowCohomology_modificationChernClass, Stacks.Chow.GysinAtInfinity.properPushforward_localizedChernClassAtInfinity, Stacks.Chow.GysinAtInfinity.localizedChernClassAtInfinity_baseChange, Stacks.Chow.GysinAtInfinity.localizedPowerSumClassAtInfinity_baseChange
statement: formalized
proof: formalized
---

# 42.49 Preparation for localized Chern classes

Section 42.49 of the Stacks Project, [Tag 0FAT](https://stacks.math.columbia.edu/tag/0FAT). 8 tags here are carried by 25 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0F9K, a lemma

[Tag 0F9K](https://stacks.math.columbia.edu/tag/0F9K) in the Stacks Project.

**`Stacks.Chow.GysinAtInfinity.properPushforward_localizedPowerSumClassAtInfinity`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BabyLocalizedChern/LocalizedPowerSumAtInfinity.lean, line 310](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BabyLocalizedChern/LocalizedPowerSumAtInfinity.lean#L310). The attribute's comment: “the classes P'\_p: the class P'\_p(Q) = (E ⟶ Z)\_* ∘ P'\_p(Q|\_E) ∘ C in A^p(Z ⟶ X), for Q|\_T zero, satisfies (Z ⟶ X)\_* ∘ P'\_p(Q) = P\_p(Q|\_\{X × \{0}})”.

> **Stacks 0F9K, for the classes `P'_p`.** Let `X` be locally of finite type over the base of
> chapter 42, let `Z ⊆ X` be a closed subscheme, let `b : W ⟶ 𝐏¹_X` be a proper morphism which is
> an isomorphism over `𝐀¹_X` (assumption (A1)), and let `Q ∈ D(𝒪_W)` be a perfect object whose
> Chern classes are defined (assumption (A0)). Let `T ⊆ W_∞` be a closed subscheme containing all
> points of `W_∞` lying over `X \ Z` such that `Q|_T` is zero (assumption (A2)). Then the class
> `P'_p(Q) = (E ⟶ Z)_* ∘ P'_p(Q|_E) ∘ C ∈ A^p(Z ⟶ X)` satisfies
>
>   `(Z ⟶ X)_* ∘ P'_p(Q) = P_p(Q|_{X × {0}})`
>
> in `A^p(X)`, where `X × {0}` is identified with `X` by the section at zero and `(Z ⟶ X)_* ∘ -` is
> the pushforward of Stacks 0EPK.

```lean
theorem properPushforward_localizedPowerSumClassAtInfinity
    (hV : ∀ w, (modificationProjectionAtInfinity f b).base w ∉ Set.range jZ.base →
      w ∈ Set.range iV.base)
    (hzero : IsZero ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
      iV.toLRSHom.toShHom).obj (restrictionAtInfinity f b Q))) :
    properPushforwardLocalizedPowerSumClassAtInfinity C hA jZ hQ perfect hV hzero =
      powerSumAtZero C f b hA hQ p
```

**`Stacks.Chow.modificationPowerSum`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/Preparation.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/Preparation.lean#L124). The attribute's comment: “the class P'\_p(Q) in A^p(Z ⟶ X), for Q|\_T zero”.

> **The class `P'_p(Q)` of Stacks 0F9K.** Let `b : W ⟶ 𝐏¹_X` be proper and an isomorphism over
> `𝐀¹_X`, let `Z ⊆ X` be closed, let `Q ∈ D(𝒪_W)` have defined Chern classes, and let `T ⊆ W_∞` be
> closed, contain every point of `W_∞` over `X ∖ Z`, and be such that `Q|_T` is zero. The class is
> `(E ⟶ Z)_* ∘ P'_p(Q|_E) ∘ C ∈ A^p(Z ⟶ X)`, where `E = W_∞ ×_X Z`, `P'_p(Q|_E)` is the extension
> of `P_p(Q)|_E` along the closed cover `W_∞ = T ∪ E`, and `C` is the class of Stacks 0F9J
> (`Stacks.Chow.gysinAtInfinityData`).

```lean
def modificationPowerSum
    (hT : ∀ w, modificationProjectionAtInfinity f b w ∉ Set.range z → w ∈ Set.range t)
    (hzero : IsZero ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
      (t ≫ modificationInclusionAtInfinity f b).toLRSHom.toShHom).obj Q)) :
    BivariantClass C (gysinSystemOfInvertible C) (z ≫ f) f z rfl p
```

**`Stacks.Chow.modificationChernClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/Preparation.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/Preparation.lean#L141). The attribute's comment: “the class c'\_p(Q) in A^p(Z ⟶ X), for Q|\_T finite locally free of rank < p in degree 0”.

> **The class `c'_p(Q)` of Stacks 0F9K.** Let `b : W ⟶ 𝐏¹_X` be proper and an isomorphism over
> `𝐀¹_X`, let `Z ⊆ X` be closed, let `Q ∈ D(𝒪_W)` have defined Chern classes, and let `T ⊆ W_∞` be
> closed, contain every point of `W_∞` over `X ∖ Z`, and be such that `Q|_T` is finite locally free
> of rank `< p` in degree `0`. The class is `(E ⟶ Z)_* ∘ c'_p(Q|_E) ∘ C ∈ A^p(Z ⟶ X)`, where
> `E = W_∞ ×_X Z`, `c'_p(Q|_E)` is the extension of `c_p(Q)|_E` along the closed cover
> `W_∞ = T ∪ E`, and `C` is the class of Stacks 0F9J (`Stacks.Chow.gysinAtInfinityData`).

```lean
def modificationChernClass
    (hT : ∀ w, modificationProjectionAtInfinity f b w ∉ Set.range z → w ∈ Set.range t)
    (hrank : ∃ M : T.Modules, IsFiniteLocallyFreeOfRankLT M p ∧
      Nonempty ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
        (t ≫ modificationInclusionAtInfinity f b).toLRSHom.toShHom).obj Q ≅
          (DerivedCategory.singleFunctor _ 0).obj M)) :
    BivariantClass C (gysinSystemOfInvertible C) (z ≫ f) f z rfl p
```

**`Stacks.Chow.properPushforwardChowCohomology_modificationPowerSum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/Preparation.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/Preparation.lean#L157). The attribute's comment: “the case of P'\_p: (Z ⟶ X)\_* ∘ P'\_p(Q) = P\_p(Q|\_\{X × \{0}})”.

> In the situation of `Stacks.Chow.modificationPowerSum`,
> `(Z ⟶ X)_* ∘ P'_p(Q) = P_p(Q|_{X × {0}})` in `A^p(X)`, where `(Z ⟶ X)_* ∘ -` is the pushforward
> of Stacks 0EPK and `Q|_{X × {0}}` is the derived pullback of `Q` along the section at zero
> `i_0 : X ⟶ W`.

```lean
theorem properPushforwardChowCohomology_modificationPowerSum
    (hT : ∀ w, modificationProjectionAtInfinity f b w ∉ Set.range z → w ∈ Set.range t)
    (hzero : IsZero ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
      (t ≫ modificationInclusionAtInfinity f b).toLRSHom.toShHom).obj Q)) :
    properPushforwardChowCohomology C f (z ≫ f) z rfl
        (modificationPowerSum C f b hA z t hQ p hT hzero) =
      perfectPowerSumComponent C f (hQ.derivedPullback
        (modificationSectionAtZero f b (isIso_modificationFibreAtZeroProjection f b hA))) p
```

**`Stacks.Chow.properPushforwardChowCohomology_modificationChernClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/Preparation.lean, line 181](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/Preparation.lean#L181). The attribute's comment: “the case of c'\_p: (Z ⟶ X)\_* ∘ c'\_p(Q) = c\_p(Q|\_\{X × \{0}})”.

> In the situation of `Stacks.Chow.modificationChernClass`,
> `(Z ⟶ X)_* ∘ c'_p(Q) = c_p(Q|_{X × {0}})` in `A^p(X)`, where `(Z ⟶ X)_* ∘ -` is the pushforward
> of Stacks 0EPK and `Q|_{X × {0}}` is the derived pullback of `Q` along the section at zero
> `i_0 : X ⟶ W`.

```lean
theorem properPushforwardChowCohomology_modificationChernClass
    (hT : ∀ w, modificationProjectionAtInfinity f b w ∉ Set.range z → w ∈ Set.range t)
    (hrank : ∃ M : T.Modules, IsFiniteLocallyFreeOfRankLT M p ∧
      Nonempty ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
        (t ≫ modificationInclusionAtInfinity f b).toLRSHom.toShHom).obj Q ≅
          (DerivedCategory.singleFunctor _ 0).obj M)) :
    properPushforwardChowCohomology C f (z ≫ f) z rfl
        (modificationChernClass C f b hA z t hQ p hT hrank) =
      perfectChernClass C f (hQ.derivedPullback
        (modificationSectionAtZero f b (isIso_modificationFibreAtZeroProjection f b hA))) p
```

Declarations registered for the tag:

- [`Stacks.Chow.GysinAtInfinity.properPushforward_localizedChernClassAtInfinity`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BabyLocalizedChern/LocalizedChernGysinCommute.lean#L404), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Chow/BabyLocalizedChern/LocalizedPowerSumAtInfinity.lean, line 421](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BabyLocalizedChern/LocalizedPowerSumAtInfinity.lean#L421) (StacksFrontier): “the classes c'\_p: the class c'\_p(Q) = (E ⟶ Z)\_* ∘ c'\_p(Q|\_E) ∘ C in A^p(Z ⟶ X), for Q|\_T finite locally free of rank < p in degree 0, satisfies (Z ⟶ X)\_* ∘ c'\_p(Q) = c\_p(Q|\_\{X × \{0}})”.

## Tag 0GUI, a lemma

[Tag 0GUI](https://stacks.math.columbia.edu/tag/0GUI) in the Stacks Project.

**`Stacks.Chow.GysinAtInfinity.localizedChernClassAtInfinity_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BabyLocalizedChern/LocalizedClassAtInfinityBaseChange.lean, line 717](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BabyLocalizedChern/LocalizedClassAtInfinityBaseChange.lean#L717). The attribute's comment: “the classes c'\_p: c'\_p(Q') built as in Stacks 0F9K from b', Q' and T' is the restriction of c'\_p(Q)”.

> **Stacks 0GUI, for the Chern classes.** In the situation of Stacks 0F9K, with `Q|_T` finite
> locally free of rank `< p` in degree `0`, let `q : X' ⟶ X` be a morphism locally of finite type.
> Let `Z' = Z ×_X X'`, `b' : W' = W ×_{𝐏¹_X} 𝐏¹_{X'} ⟶ 𝐏¹_{X'}` and `T' = T ×_{W_∞} W'_∞ ⊆ W'_∞`
> be the base changes of `Z`, `b` and `T`, and let `Q' = (W' ⟶ W)^*Q`. Then `b'`, `Q'` and `T'`
> satisfy the assumptions of Stacks 0F9K, and the class `c'_p(Q') ∈ A^p(Z' ⟶ X')` constructed as in
> Stacks 0F9K using `b'`, `Q'` and `T'` is the restriction (Remark 0F9Z) of
> `c'_p(Q) ∈ A^p(Z ⟶ X)`.
>
> The restriction is a class for `Z' ⟶ X'` whose source carries the structure morphism
> `Z' ⟶ Z ⟶ S`, while the class constructed at `X'` carries `Z' ⟶ X' ⟶ S`; the two are equal, and
> the restriction is read with the second one by `Stacks.Chow.bivariantTransport` along the
> identity.

```lean
theorem localizedChernClassAtInfinity_baseChange
    (hV : ∀ w, (modificationProjectionAtInfinity f b).base w ∉ Set.range jZ.base →
      w ∈ Set.range iV.base)
    (hres : RestrictionIsLocallyFreeOfRankLT f b iV Q p) :
    localizedChernClassAtInfinity C (haveI := hA; isIso_baseChangedModification_chart f b q)
        (pullback.snd jZ q)
        (hasDefinedChernClasses_derivedPullback (pullback.fst b (familyBaseChange f q)) hQ)
        (baseChange_mem_range f b jZ iV q hV)
        (restrictionIsLocallyFreeOfRankLT_baseChange f b iV q hres) =
      bivariantTransport C (gysinSystemOfInvertible C) (pullback.fst jZ q ≫ jZ ≫ f)
        (pullback.snd jZ q ≫ q ≫ f) (q ≫ f) (pullback.snd jZ q)
        (pullbackSnd_comp_structureMorphism_eq C (jZ ≫ f) f jZ rfl q) (pullback.snd jZ q) rfl
        (Iso.refl _) (Category.id_comp _) (p : ℤ)
        (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso C)
        (bivariantRestrictionOfInvertible C (jZ ≫ f) f jZ rfl q (p : ℤ)
          (localizedChernClassAtInfinity C hA jZ hQ hV hres))
```

**`Stacks.Chow.GysinAtInfinity.localizedPowerSumClassAtInfinity_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BabyLocalizedChern/LocalizedClassAtInfinityBaseChange.lean, line 766](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BabyLocalizedChern/LocalizedClassAtInfinityBaseChange.lean#L766). The attribute's comment: “the classes P'\_p: P'\_p(Q') built as in Stacks 0F9K from b', Q' and T' is the restriction of P'\_p(Q)”.

> **Stacks 0GUI, for the classes `P_p`.** In the situation of Stacks 0F9K, with `Q|_T` zero,
> let `q : X' ⟶ X` be a morphism locally of finite type. Let `Z' = Z ×_X X'`,
> `b' : W' = W ×_{𝐏¹_X} 𝐏¹_{X'} ⟶ 𝐏¹_{X'}` and `T' = T ×_{W_∞} W'_∞ ⊆ W'_∞` be the base changes of
> `Z`, `b` and `T`, and let `Q' = (W' ⟶ W)^*Q`. Then `b'`, `Q'` and `T'` satisfy the assumptions of
> Stacks 0F9K, and the class `P'_p(Q') ∈ A^p(Z' ⟶ X')` constructed as in Stacks 0F9K using `b'`,
> `Q'` and `T'` is the restriction (Remark 0F9Z) of `P'_p(Q) ∈ A^p(Z ⟶ X)`, read with the structure
> morphism `Z' ⟶ X' ⟶ S` as in `localizedChernClassAtInfinity_baseChange`.

```lean
theorem localizedPowerSumClassAtInfinity_baseChange
    (perfect : RingedSpace.IsPerfect.{u, u + 1} (X := W.toRingedSpace) Q)
    (hV : ∀ w, (modificationProjectionAtInfinity f b).base w ∉ Set.range jZ.base →
      w ∈ Set.range iV.base)
    (hzero : IsZero ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
      iV.toLRSHom.toShHom).obj (restrictionAtInfinity f b Q))) :
    localizedPowerSumClassAtInfinity C (haveI := hA; isIso_baseChangedModification_chart f b q)
        (pullback.snd jZ q)
        (hasDefinedChernClasses_derivedPullback (pullback.fst b (familyBaseChange f q)) hQ)
        (RingedSpace.KFlatDerivedPullback.isPerfect_derivedPullback _ Q perfect)
        (baseChange_mem_range f b jZ iV q hV) (isZero_restriction_baseChange f b iV q hzero)
        (p := p) =
      bivariantTransport C (gysinSystemOfInvertible C) (pullback.fst jZ q ≫ jZ ≫ f)
        (pullback.snd jZ q ≫ q ≫ f) (q ≫ f) (pullback.snd jZ q)
        (pullbackSnd_comp_structureMorphism_eq C (jZ ≫ f) f jZ rfl q) (pullback.snd jZ q) rfl
        (Iso.refl _) (Category.id_comp _) (p : ℤ)
        (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso C)
        (bivariantRestrictionOfInvertible C (jZ ≫ f) f jZ rfl q (p : ℤ)
          (localizedPowerSumClassAtInfinity C hA jZ hQ perfect hV hzero (p := p)))
```

**`Stacks.Chow.bivariantRestriction_modificationPowerSum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/ModificationBaseChange.lean, line 457](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/ModificationBaseChange.lean#L457). The attribute's comment: “the case of P'\_p: the class P'\_p(Q') of Lemma 0F9K for the base change is the restriction of P'\_p(Q)”.

> In the setting of Stacks 0F9K let `h : X' ⟶ X` be locally of finite type, let
> `b' : W' = W ×_{𝐏¹_X} 𝐏¹_{X'} ⟶ 𝐏¹_{X'}` and `Z' = Z ×_X X'` be the base changes, and set
> `Q' = (W' ⟶ W)^* Q`. Then the class `P'_p(Q') ∈ A^p(Z' ⟶ X')` constructed as in Stacks 0F9K from
> `b'`, `Q'` and any closed `T' ⊆ W'_∞` with the properties used there (for instance the base change
> of `T`) is the restriction (Remark 0F9Z) of `P'_p(Q) ∈ A^p(Z ⟶ X)`.

```lean
theorem bivariantRestriction_modificationPowerSum
    (hT : ∀ w, modificationProjectionAtInfinity f b w ∉ Set.range z → w ∈ Set.range t)
    (hT' : ∀ w, modificationProjectionAtInfinity (h ≫ f) (baseChangedModification f b h) w ∉
      Set.range (pullback.snd z h) → w ∈ Set.range t')
    (hzero : IsZero ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
      (t ≫ modificationInclusionAtInfinity f b).toLRSHom.toShHom).obj Q))
    (hzero' : IsZero ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
      (t' ≫ modificationInclusionAtInfinity (h ≫ f)
        (baseChangedModification f b h)).toLRSHom.toShHom).obj
      ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
        (pullback.fst b (familyBaseChange f h)).toLRSHom.toShHom).obj Q))) :
    bivariantClassCongrBase C (gysinSystemOfInvertible C) (pullback.snd z h)
        (pullbackSnd_comp_structureMorphism_eq C (z ≫ f) f z rfl h).symm rfl
        (hv := pullbackSnd_comp_structureMorphism_eq C (z ≫ f) f z rfl h) (hv' := rfl) p
        (bivariantRestriction C (gysinSystemOfInvertible C) (z ≫ f) f z rfl h p
          (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso C)
          (modificationPowerSum C f b hA z t hQ p hT hzero)) =
      modificationPowerSum C (h ≫ f) (baseChangedModification f b h)
        (isIso_restrictedModification_affineChart f b h hA) (pullback.snd z h) t'
        (hQ.derivedPullback (pullback.fst b (familyBaseChange f h))) p hT' hzero'
```

**`Stacks.Chow.bivariantRestriction_modificationChernClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/ModificationBaseChange.lean, line 493](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/ModificationBaseChange.lean#L493). The attribute's comment: “the case of c'\_p: the class c'\_p(Q') of Lemma 0F9K for the base change is the restriction of c'\_p(Q)”.

> In the setting of Stacks 0F9K let `h : X' ⟶ X` be locally of finite type, let
> `b' : W' = W ×_{𝐏¹_X} 𝐏¹_{X'} ⟶ 𝐏¹_{X'}` and `Z' = Z ×_X X'` be the base changes, and set
> `Q' = (W' ⟶ W)^* Q`. Then the class `c'_p(Q') ∈ A^p(Z' ⟶ X')` constructed as in Stacks 0F9K from
> `b'`, `Q'` and any closed `T' ⊆ W'_∞` with the properties used there (for instance the base change
> of `T`) is the restriction (Remark 0F9Z) of `c'_p(Q) ∈ A^p(Z ⟶ X)`.

```lean
theorem bivariantRestriction_modificationChernClass
    (hT : ∀ w, modificationProjectionAtInfinity f b w ∉ Set.range z → w ∈ Set.range t)
    (hT' : ∀ w, modificationProjectionAtInfinity (h ≫ f) (baseChangedModification f b h) w ∉
      Set.range (pullback.snd z h) → w ∈ Set.range t')
    (hrank : ∃ M : T.Modules, IsFiniteLocallyFreeOfRankLT M p ∧
      Nonempty ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
        (t ≫ modificationInclusionAtInfinity f b).toLRSHom.toShHom).obj Q ≅
          (DerivedCategory.singleFunctor _ 0).obj M))
    (hrank' : ∃ M : T'.Modules, IsFiniteLocallyFreeOfRankLT M p ∧
      Nonempty ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
        (t' ≫ modificationInclusionAtInfinity (h ≫ f)
          (baseChangedModification f b h)).toLRSHom.toShHom).obj
        ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
          (pullback.fst b (familyBaseChange f h)).toLRSHom.toShHom).obj Q) ≅
          (DerivedCategory.singleFunctor _ 0).obj M)) :
    bivariantClassCongrBase C (gysinSystemOfInvertible C) (pullback.snd z h)
        (pullbackSnd_comp_structureMorphism_eq C (z ≫ f) f z rfl h).symm rfl
        (hv := pullbackSnd_comp_structureMorphism_eq C (z ≫ f) f z rfl h) (hv' := rfl) p
        (bivariantRestriction C (gysinSystemOfInvertible C) (z ≫ f) f z rfl h p
          (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso C)
          (modificationChernClass C f b hA z t hQ p hT hrank)) =
      modificationChernClass C (h ≫ f) (baseChangedModification f b h)
        (isIso_restrictedModification_affineChart f b h hA) (pullback.snd z h) t'
        (hQ.derivedPullback (pullback.fst b (familyBaseChange f h))) p hT' hrank'
```

## Tag 0FAU, a lemma

[Tag 0FAU](https://stacks.math.columbia.edu/tag/0FAU) in the Stacks Project.

**`Stacks.Chow.localizedModificationClass_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/Modification.lean, line 396](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/Modification.lean#L396). The attribute's comment: “first assertion: P'\_p(Q), resp. c'\_p(Q), is independent of the closed subscheme T, for a general class q in place of P\_p(Q), resp. c\_p(Q)”.

> **The localized class does not depend on `T`**, for a general class. Two closed subschemes
> `T, T' ⊆ W_∞` containing every point of `W_∞` over `X ∖ Z`, over both of which `q` vanishes, give
> the same localized class; for `q = P_p(Q)`, resp. `q = c_p(Q)`, this is the independence of
> `P'_p(Q)`, resp. `c'_p(Q)`, of the choice of `T`.

```lean
theorem localizedModificationClass_eq {T' : Scheme.{u}} (t' : T' ⟶ modificationFibreAtInfinity f b)
    [IsClosedImmersion t']
    (hT : ∀ w, modificationProjectionAtInfinity f b w ∉ Set.range z → w ∈ Set.range t)
    (hT' : ∀ w, modificationProjectionAtInfinity f b w ∉ Set.range z → w ∈ Set.range t')
    (hq : BivariantClass.VanishesOver q (t ≫ modificationInclusionAtInfinity f b))
    (hq' : BivariantClass.VanishesOver q (t' ≫ modificationInclusionAtInfinity f b)) :
    localizedModificationClass D z t hT hq = localizedModificationClass D z t' hT' hq'
```

**`Stacks.Chow.modificationPowerSum_eq_of_modification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/ModificationComparison.lean, line 853](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/ModificationComparison.lean#L853). The attribute's comment: “second assertion, for P'\_p: for g : W' ⟶ W proper with b ∘ g an isomorphism over A^1\_X (as when g is one), P'\_p(g^*Q) = P'\_p(Q)”.

> **The second assertion of Stacks 0FAU, for `P'_p`.** Let `b : W ⟶ 𝐏¹_X` be proper and an
> isomorphism over `𝐀¹_X`, let `g : W' ⟶ W` be proper with `b' = b ∘ g` an isomorphism over `𝐀¹_X`
> (as it is when `g` is one, `Stacks.Chow.isIso_pullbackSnd_comp_projectiveLineAffineChart`), and
> set `Q' = Lg^*Q`. Then `P'_p(Q') = P'_p(Q)` in `A^p(Z ⟶ X)`, the left side built from
> `b'`, `Q'` and any closed `T' ⊆ W'_∞` with the properties of Stacks 0F9K, the right side from `b`,
> `Q` and `T ⊆ W_∞`.

```lean
theorem modificationPowerSum_eq_of_modification
    (hT : ∀ w, modificationProjectionAtInfinity f b w ∉ Set.range z → w ∈ Set.range t)
    (hT' : ∀ w, modificationProjectionAtInfinity f b' w ∉ Set.range z → w ∈ Set.range t')
    (hzero : IsZero ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
      (t ≫ modificationInclusionAtInfinity f b).toLRSHom.toShHom).obj Q))
    (hzero' : IsZero ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
      (t' ≫ modificationInclusionAtInfinity f b').toLRSHom.toShHom).obj
        ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback g.toLRSHom.toShHom).obj Q))) :
    modificationPowerSum C f b' hA' z t' (hQ.derivedPullback g) p hT' hzero' =
      modificationPowerSum C f b hA z t hQ p hT hzero
```

**`Stacks.Chow.modificationChernClass_eq_of_modification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/ModificationComparison.lean, line 880](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/ModificationComparison.lean#L880). The attribute's comment: “second assertion, for c'\_p: for g : W' ⟶ W proper with b ∘ g an isomorphism over A^1\_X (as when g is one), c'\_p(g^*Q) = c'\_p(Q)”.

> **The second assertion of Stacks 0FAU, for `c'_p`.** Let `b : W ⟶ 𝐏¹_X` be proper and an
> isomorphism over `𝐀¹_X`, let `g : W' ⟶ W` be proper with `b' = b ∘ g` an isomorphism over `𝐀¹_X`
> (as it is when `g` is one, `Stacks.Chow.isIso_pullbackSnd_comp_projectiveLineAffineChart`), and
> set `Q' = Lg^*Q`. Then `c'_p(Q') = c'_p(Q)` in `A^p(Z ⟶ X)`, the left side built from
> `b'`, `Q'` and any closed `T' ⊆ W'_∞` with the properties of Stacks 0F9K, the right side from `b`,
> `Q` and `T ⊆ W_∞`.

```lean
theorem modificationChernClass_eq_of_modification
    (hT : ∀ w, modificationProjectionAtInfinity f b w ∉ Set.range z → w ∈ Set.range t)
    (hT' : ∀ w, modificationProjectionAtInfinity f b' w ∉ Set.range z → w ∈ Set.range t')
    (hrank : ∃ M : T.Modules, IsFiniteLocallyFreeOfRankLT M p ∧
      Nonempty ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
        (t ≫ modificationInclusionAtInfinity f b).toLRSHom.toShHom).obj Q ≅
          (DerivedCategory.singleFunctor _ 0).obj M))
    (hrank' : ∃ M : T'.Modules, IsFiniteLocallyFreeOfRankLT M p ∧
      Nonempty ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
        (t' ≫ modificationInclusionAtInfinity f b').toLRSHom.toShHom).obj
          ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback g.toLRSHom.toShHom).obj Q) ≅
          (DerivedCategory.singleFunctor _ 0).obj M)) :
    modificationChernClass C f b' hA' z t' (hQ.derivedPullback g) p hT' hrank' =
      modificationChernClass C f b hA z t hQ p hT hrank
```

**`Stacks.Chow.GysinAtInfinity.localizedPowerSumAtInfinity_invariance`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedClassAtInfinity/Chern.lean, line 707](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedClassAtInfinity/Chern.lean#L707). The attribute's comment: “the P'\_p(Q) half: independence of the choice of the closed subscheme T, and P'\_p(Q) = P'\_p(Q') for a proper g : W' ⟶ W which is an isomorphism over 𝐀¹\_X and Q' = g^*Q”.

> **Stacks 0FAU, for `P'_p(Q)`.** In the situation of Stacks 0F9K — `X` locally of finite type
> over `S`, `Z ⊆ X` closed, `b : W ⟶ 𝐏¹_X` proper and an isomorphism over `𝐀¹_X` (A1), `Q ∈ D(𝒪_W)`
> perfect with Chern classes defined (A0) — the class `P'_p(Q) ∈ A^p(Z ⟶ X)`
>
> 1. is independent of the choice of the closed subscheme `T ⊆ W_∞` containing all points of `W_∞`
>    lying over `X \ Z` with `Q|_T = 0` (A2);
> 2. is unchanged when `b` is replaced by `b ∘ g` and `Q` by `Q' = g^*Q`, for `g : W' ⟶ W` proper
>    and an isomorphism over `𝐀¹_X`: `T' = g^{-1}(T)` satisfies (A2) for `b ∘ g` and `Q'`, so that
>    `P'_p(Q')` is defined, and `P'_p(Q) = P'_p(Q')`, the right side computed with any closed
>    subscheme `T' ⊆ W'_∞` satisfying (A2) for `b ∘ g` and `Q'`.

```lean
theorem localizedPowerSumAtInfinity_invariance
    (perfect : RingedSpace.IsPerfect.{u, u + 1} (X := W.toRingedSpace) Q)
    (hQ : HasDefinedChernClasses Q) (p : ℕ) :
    (∀ {T₁ : Scheme.{u}} (iT₁ : T₁ ⟶ modificationFibreAtInfinity f b) [IsClosedImmersion iT₁]
      (hT₁ : ∀ w : modificationFibreAtInfinity f b,
        (modificationProjectionAtInfinity f b).base w ∉ Set.range iZ.base →
          w ∈ Set.range iT₁.base)
      (hzero₁ : IsZero (restrictToInfinity C f b Q iT₁))
      {T₂ : Scheme.{u}} (iT₂ : T₂ ⟶ modificationFibreAtInfinity f b) [IsClosedImmersion iT₂]
      (hT₂ : ∀ w : modificationFibreAtInfinity f b,
        (modificationProjectionAtInfinity f b).base w ∉ Set.range iZ.base →
          w ∈ Set.range iT₂.base)
      (hzero₂ : IsZero (restrictToInfinity C f b Q iT₂)),
      localizedPowerSumClassAtInfinity (p := p) C hA iZ hQ perfect hT₁ hzero₁ =
        localizedPowerSumClassAtInfinity (p := p) C hA iZ hQ perfect hT₂ hzero₂) ∧
    (∀ {T : Scheme.{u}} (iT : T ⟶ modificationFibreAtInfinity f b) [IsClosedImmersion iT]
      (hT : ∀ w : modificationFibreAtInfinity f b,
        (modificationProjectionAtInfinity f b).base w ∉ Set.range iZ.base → w ∈ Set.range iT.base)
      (hzero : IsZero (restrictToInfinity C f b Q iT))
      {W' : Scheme.{u}} (g : W' ⟶ W) [IsProper g]
      (hg : IsIso (pullback.snd g (chartInclusion f b))),
      ((∀ w : modificationFibreAtInfinity f (g ≫ b),
          (modificationProjectionAtInfinity f (g ≫ b)).base w ∉ Set.range iZ.base →
            w ∈ Set.range (pullback.snd iT (infinityMap f b g)).base) ∧
        IsZero (restrictToInfinity C f (g ≫ b)
          ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback g.toLRSHom.toShHom).obj Q)
          (pullback.snd iT (infinityMap f b g)))) ∧
      ∀ {T' : Scheme.{u}} (iT' : T' ⟶ modificationFibreAtInfinity f (g ≫ b))
        [IsClosedImmersion iT']
        (hT' : ∀ w : modificationFibreAtInfinity f (g ≫ b),
          (modificationProjectionAtInfinity f (g ≫ b)).base w ∉ Set.range iZ.base →
            w ∈ Set.range iT'.base)
        (hzero' : IsZero (restrictToInfinity C f (g ≫ b)
          ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback g.toLRSHom.toShHom).obj Q)
          iT')),
        haveI := hA
        haveI := hg
        localizedPowerSumClassAtInfinity (p := p) C (isIso_pullbackSnd_comp f b g) iZ
            (hasDefinedChernClasses_derivedPullback g hQ)
            (RingedSpace.KFlatDerivedPullback.isPerfect_derivedPullback g.toLRSHom.toShHom Q
              perfect)
            hT' hzero' =
          localizedPowerSumClassAtInfinity (p := p) C hA iZ hQ perfect hT hzero)
```

**`Stacks.Chow.GysinAtInfinity.localizedChernClassAtInfinity_invariance`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedClassAtInfinity/Chern.lean, line 772](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedClassAtInfinity/Chern.lean#L772). The attribute's comment: “the c'\_p(Q) half: independence of the choice of the closed subscheme T, and c'\_p(Q) = c'\_p(Q') for a proper g : W' ⟶ W which is an isomorphism over 𝐀¹\_X and Q' = g^*Q”.

> **Stacks 0FAU, for `c'_p(Q)`.** In the situation of Stacks 0F9K — `X` locally of finite type
> over `S`, `Z ⊆ X` closed, `b : W ⟶ 𝐏¹_X` proper and an isomorphism over `𝐀¹_X` (A1), `Q ∈ D(𝒪_W)`
> perfect with Chern classes defined (A0) — the class `c'_p(Q) ∈ A^p(Z ⟶ X)`
>
> 1. is independent of the choice of the closed subscheme `T ⊆ W_∞` containing all points of `W_∞`
>    lying over `X \ Z` with `Q|_T` isomorphic to a finite locally free `𝒪_T`-module of rank `< p`
>    in degree `0` (A2);
> 2. is unchanged when `b` is replaced by `b ∘ g` and `Q` by `Q' = g^*Q`, for `g : W' ⟶ W` proper
>    and an isomorphism over `𝐀¹_X`: `T' = g^{-1}(T)` satisfies (A2) for `b ∘ g` and `Q'`, so that
>    `c'_p(Q')` is defined, and `c'_p(Q) = c'_p(Q')`, the right side computed with any closed
>    subscheme `T' ⊆ W'_∞` satisfying (A2) for `b ∘ g` and `Q'`.
>
> Perfectness of `Q` is a hypothesis of the source; the construction of `c'_p(Q)` does not use it.

```lean
theorem localizedChernClassAtInfinity_invariance
    (_perfect : RingedSpace.IsPerfect.{u, u + 1} (X := W.toRingedSpace) Q)
    (hQ : HasDefinedChernClasses Q) (p : ℕ) :
    (∀ {T₁ : Scheme.{u}} (iT₁ : T₁ ⟶ modificationFibreAtInfinity f b) [IsClosedImmersion iT₁]
      (hT₁ : ∀ w : modificationFibreAtInfinity f b,
        (modificationProjectionAtInfinity f b).base w ∉ Set.range iZ.base →
          w ∈ Set.range iT₁.base)
      (hsmall₁ : RestrictionIsLocallyFreeOfRankLT f b iT₁ Q p)
      {T₂ : Scheme.{u}} (iT₂ : T₂ ⟶ modificationFibreAtInfinity f b) [IsClosedImmersion iT₂]
      (hT₂ : ∀ w : modificationFibreAtInfinity f b,
        (modificationProjectionAtInfinity f b).base w ∉ Set.range iZ.base →
          w ∈ Set.range iT₂.base)
      (hsmall₂ : RestrictionIsLocallyFreeOfRankLT f b iT₂ Q p),
      localizedChernClassAtInfinity C hA iZ hQ hT₁ hsmall₁ =
        localizedChernClassAtInfinity C hA iZ hQ hT₂ hsmall₂) ∧
    (∀ {T : Scheme.{u}} (iT : T ⟶ modificationFibreAtInfinity f b) [IsClosedImmersion iT]
      (hT : ∀ w : modificationFibreAtInfinity f b,
        (modificationProjectionAtInfinity f b).base w ∉ Set.range iZ.base → w ∈ Set.range iT.base)
      (hsmall : RestrictionIsLocallyFreeOfRankLT f b iT Q p)
      {W' : Scheme.{u}} (g : W' ⟶ W) [IsProper g]
      (hg : IsIso (pullback.snd g (chartInclusion f b))),
      ((∀ w : modificationFibreAtInfinity f (g ≫ b),
          (modificationProjectionAtInfinity f (g ≫ b)).base w ∉ Set.range iZ.base →
            w ∈ Set.range (pullback.snd iT (infinityMap f b g)).base) ∧
        RestrictionIsLocallyFreeOfRankLT f (g ≫ b) (pullback.snd iT (infinityMap f b g))
          ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback g.toLRSHom.toShHom).obj Q)
          p) ∧
      ∀ {T' : Scheme.{u}} (iT' : T' ⟶ modificationFibreAtInfinity f (g ≫ b))
        [IsClosedImmersion iT']
        (hT' : ∀ w : modificationFibreAtInfinity f (g ≫ b),
          (modificationProjectionAtInfinity f (g ≫ b)).base w ∉ Set.range iZ.base →
            w ∈ Set.range iT'.base)
        (hsmall' : RestrictionIsLocallyFreeOfRankLT f (g ≫ b) iT'
          ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback g.toLRSHom.toShHom).obj Q)
          p),
        haveI := hA
        haveI := hg
        localizedChernClassAtInfinity C (isIso_pullbackSnd_comp f b g) iZ
            (hasDefinedChernClasses_derivedPullback g hQ) hT' hsmall' =
          localizedChernClassAtInfinity C hA iZ hQ hT hsmall)
```

## Tag 0FAV, a lemma

[Tag 0FAV](https://stacks.math.columbia.edu/tag/0FAV) in the Stacks Project.

**`Stacks.Chow.GysinAtInfinity.gysinAtInfinity_comp_localizedChernClassAtInfinity`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BabyLocalizedChern/LocalizedChernGysinCommute.lean, line 516](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BabyLocalizedChern/LocalizedChernGysinCommute.lean#L516).

> **Stacks 0FAV.** Let `(S, δ)` be as in Situation 02QL, let `X` be locally of finite type over
> `S`, let `Z ⊆ X` be a closed subscheme, let `b : W ⟶ 𝐏¹_X` be a proper morphism which is an
> isomorphism over `𝐀¹_X` (assumption (A1)), and let `Q ∈ D(𝒪_W)` be a perfect object whose Chern
> classes are defined (assumption (A0)). Let `T ⊆ W_∞` be a closed subscheme containing all points
> of `W_∞` lying over `X \ Z` such that `Q|_T` is isomorphic to a finite locally free
> `𝒪_T`-module of rank `< p` sitting in cohomological degree `0` (assumption (A2), in the case of
> the lemma). Let `C ∈ A⁰(W_∞ ⟶ X)` be the class of Stacks 0F9J and `c'_p(Q) ∈ A^p(Z ⟶ X)` the
> class of Stacks 0F9K. Then
>
>   `C ∘ c_p(Q|_{X × {0}}) = C ∘ (Z ⟶ X)_* ∘ c'_p(Q) = c_p(Q|_{W_∞}) ∘ C`
>
> in `A^p(W_∞ ⟶ X)`. Here `X × {0}` is identified with `X` by the section at zero, the classes
> `c_p` are those of Stacks 0GUD, the composites are those of Stacks 0B75 read at `W_∞ ⟶ X` in
> degree `0 + p`, and `(Z ⟶ X)_* ∘ c'_p(Q) ∈ A^p(X)` is the pushforward of Stacks 0EPK.

```lean
theorem gysinAtInfinity_comp_localizedChernClassAtInfinity
    (hA : IsIso (pullback.snd b (projectiveLineAffineChart f)))
    (jZ : Z ⟶ X) [IsClosedImmersion jZ]
    (iV : V ⟶ modificationFibreAtInfinity f b) [IsClosedImmersion iV]
    (hV : ∀ w, (modificationProjectionAtInfinity f b).base w ∉ Set.range jZ.base →
      w ∈ Set.range iV.base)
    {Q : DerivedCategory W.Modules}
    (_perfect : RingedSpace.IsPerfect.{u, u + 1} (X := W.toRingedSpace) Q)
    (hQ : HasDefinedChernClasses Q) (p : ℕ)
    (hres : RestrictionIsLocallyFreeOfRankLT f b iV Q p) :
    bivariantCompositeIdRightHom C (gysinSystemOfInvertible C) f
        (modificationProjectionAtInfinity f b)
        (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso C)
        (gysinSystemOfInvertible_isNaturalUnderPullbackCompPushforward C) (p : ℤ) 0
        (gysinAtInfinityClass C f b hA) (chernClassAtZero C f b hA hQ p) =
      bivariantCompositeIdRightHom C (gysinSystemOfInvertible C) f
        (modificationProjectionAtInfinity f b)
        (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso C)
        (gysinSystemOfInvertible_isNaturalUnderPullbackCompPushforward C) (p : ℤ) 0
        (gysinAtInfinityClass C f b hA)
        (properPushforwardLocalizedChernClassAtInfinity C hA jZ hQ hV hres) ∧
    bivariantCompositeIdRightHom C (gysinSystemOfInvertible C) f
        (modificationProjectionAtInfinity f b)
        (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso C)
        (gysinSystemOfInvertible_isNaturalUnderPullbackCompPushforward C) (p : ℤ) 0
        (gysinAtInfinityClass C f b hA)
        (properPushforwardLocalizedChernClassAtInfinity C hA jZ hQ hV hres) =
      bivariantCompositeIdLeftHom C (gysinSystemOfInvertible C) f
        (modificationProjectionAtInfinity f b)
        (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso C)
        (gysinSystemOfInvertible_isNaturalUnderPullbackCompPushforward C) (p : ℤ) 0
        (gysinAtInfinityClass C f b hA) (chernClassAtInfinity C f b hQ p)
```

**`Stacks.Chow.gysinAtInfinityClass_comp_modificationChernClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/GysinAtInfinityRestriction.lean, line 547](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/GysinAtInfinityRestriction.lean#L547). The attribute's comment: “C ∘ c\_p(Q|\_\{X × \{0}}) = C ∘ (Z ⟶ X)\_* ∘ c'\_p(Q) = c\_p(Q|\_\{W\_∞}) ∘ C, for Q|\_T finite locally free of rank < p in degree 0, the composites read in A^p(W\_∞ ⟶ X)”.

> In the situation of Stacks 0F9K, let `Q|_T` be finite locally free of rank `< p` in degree
> `0`, and let `C ∈ A⁰(W_∞ ⟶ X)` be the class of Stacks 0F9J (`Stacks.Chow.gysinAtInfinityClass`).
> Then
>
>   `C ∘ c_p(Q|_{X × {0}}) = C ∘ (Z ⟶ X)_* ∘ c'_p(Q) = c_p(Q|_{W_∞}) ∘ C`   in   `A^p(W_∞ ⟶ X)`,
>
> where `c'_p(Q)` is `Stacks.Chow.modificationChernClass`, `Q|_{X × {0}}` and `Q|_{W_∞}` are the
> derived pullbacks of `Q` along the section at zero and the inclusion of the fibre at infinity,
> and `∘` is the composition of Stacks 0B75. The composites, of degrees `0 + p` and `p + 0` for
> `W_∞ ⟶ X ⟶ X` and `W_∞ ⟶ W_∞ ⟶ X`, are read as classes of degree `p` for `W_∞ ⟶ X`.

```lean
theorem gysinAtInfinityClass_comp_modificationChernClass
    (hT : ∀ w, modificationProjectionAtInfinity f b w ∉ Set.range z → w ∈ Set.range t)
    (hrank : ∃ M : T.Modules, IsFiniteLocallyFreeOfRankLT M p ∧
      Nonempty ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
        (t ≫ modificationInclusionAtInfinity f b).toLRSHom.toShHom).obj Q ≅
          (DerivedCategory.singleFunctor _ 0).obj M)) :
    BivariantClass.copy C (gysinSystemOfInvertible C) (modificationProjectionAtInfinity f b ≫ f) f
        (Category.comp_id (modificationProjectionAtInfinity f b))
        (comp_comp_structureMorphism_eq rfl (Category.id_comp f)) rfl (zero_add (p : ℤ))
        (bivariantCompositeOfInvertible C (modificationProjectionAtInfinity f b ≫ f) f f
          (modificationProjectionAtInfinity f b) (𝟙 X) rfl (Category.id_comp f) 0 p
          (gysinAtInfinityClass C f b hA)
          (perfectChernClass C f (hQ.derivedPullback
            (modificationSectionAtZero f b (isIso_modificationFibreAtZeroProjection f b hA))) p)) =
      BivariantClass.copy C (gysinSystemOfInvertible C) (modificationProjectionAtInfinity f b ≫ f)
        f (Category.comp_id (modificationProjectionAtInfinity f b))
        (comp_comp_structureMorphism_eq rfl (Category.id_comp f)) rfl (zero_add (p : ℤ))
        (bivariantCompositeOfInvertible C (modificationProjectionAtInfinity f b ≫ f) f f
          (modificationProjectionAtInfinity f b) (𝟙 X) rfl (Category.id_comp f) 0 p
          (gysinAtInfinityClass C f b hA)
          (properPushforwardChowCohomology C f (z ≫ f) z rfl
            (modificationChernClass C f b hA z t hQ p hT hrank))) ∧
    BivariantClass.copy C (gysinSystemOfInvertible C) (modificationProjectionAtInfinity f b ≫ f) f
        (Category.comp_id (modificationProjectionAtInfinity f b))
        (comp_comp_structureMorphism_eq rfl (Category.id_comp f)) rfl (zero_add (p : ℤ))
        (bivariantCompositeOfInvertible C (modificationProjectionAtInfinity f b ≫ f) f f
          (modificationProjectionAtInfinity f b) (𝟙 X) rfl (Category.id_comp f) 0 p
          (gysinAtInfinityClass C f b hA)
          (properPushforwardChowCohomology C f (z ≫ f) z rfl
            (modificationChernClass C f b hA z t hQ p hT hrank))) =
      BivariantClass.copy C (gysinSystemOfInvertible C)
        (modificationProjectionAtInfinity f b ≫ f) f
        (Category.id_comp (modificationProjectionAtInfinity f b))
        (comp_comp_structureMorphism_eq (Category.id_comp _) rfl) rfl (add_zero (p : ℤ))
        (bivariantCompositeOfInvertible C (modificationProjectionAtInfinity f b ≫ f)
          (modificationProjectionAtInfinity f b ≫ f) f (𝟙 _)
          (modificationProjectionAtInfinity f b) (Category.id_comp _) rfl p 0
          (perfectChernClass C (modificationProjectionAtInfinity f b ≫ f)
            (hQ.derivedPullback (modificationInclusionAtInfinity f b)) p)
          (gysinAtInfinityClass C f b hA))
```

## Tag 0FAW, a lemma

[Tag 0FAW](https://stacks.math.columbia.edu/tag/0FAW) in the Stacks Project.

**`Stacks.Chow.nonhomogeneousBivariantTransport_compositeOfInvertible_modificationPowerSum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/Commutation.lean, line 379](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/Commutation.lean#L379). The attribute's comment: “for P'\_p: P'\_p(Q) ∘ c = c ∘ P'\_p(Q) in A^*(Y ×\_X Z → X), for every c in A^*(Y → X)”.

> In the situation of Stacks 0F9K with `Q|_T` zero, let `g : Y ⟶ X` be locally of finite type and
> let `c ∈ A^*(Y ⟶ X)`. Then
>
>   `P'_p(Q) ∘ c = c ∘ P'_p(Q)`   in   `A^*(Y ×_X Z ⟶ X)`,
>
> where `P'_p(Q) ∘ c = res(P'_p(Q)) ∘ c` is a class for `Z ×_X Y ⟶ X`, carried to `Y ×_X Z` along
> the symmetry of the fibre product, and `c ∘ P'_p(Q) = res(c) ∘ P'_p(Q)`.

```lean
theorem nonhomogeneousBivariantTransport_compositeOfInvertible_modificationPowerSum
    (hT : ∀ w, modificationProjectionAtInfinity f b w ∉ Set.range z → w ∈ Set.range t)
    (hzero : IsZero ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
      (t ≫ modificationInclusionAtInfinity f b).toLRSHom.toShHom).obj Q))
    (c : nonhomogeneousBivariantGroup C (gysinSystemOfInvertible C) (g ≫ f) f g rfl) :
    nonhomogeneousBivariantTransport C (gysinSystemOfInvertible C) (pullback.fst z g ≫ (z ≫ f))
        (pullback.fst g z ≫ (g ≫ f)) f (pullback.snd z g ≫ g)
        (comp_comp_structureMorphism_eq
          (pullbackSnd_comp_structureMorphism_eq C (z ≫ f) f z rfl g) rfl)
        (pullback.snd g z ≫ z)
        (comp_comp_structureMorphism_eq
          (pullbackSnd_comp_structureMorphism_eq C (g ≫ f) f g rfl z) rfl)
        (pullbackSymmetry z g) (by simp [pullback.condition])
        (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso C)
        (nonhomogeneousBivariantCompositeOfInvertible C (pullback.fst z g ≫ (z ≫ f)) (g ≫ f) f
          (pullback.snd z g) g
          (pullbackSnd_comp_structureMorphism_eq C (z ≫ f) f z rfl g) rfl
          (DirectSum.of _ (p : ℤ)
            (bivariantRestriction C (gysinSystemOfInvertible C) (z ≫ f) f z rfl g p
              (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso C)
              (modificationPowerSum C f b hA z t hQ p hT hzero))) c) =
      nonhomogeneousBivariantCompositeOfInvertible C (pullback.fst g z ≫ (g ≫ f)) (z ≫ f) f
        (pullback.snd g z) z
        (pullbackSnd_comp_structureMorphism_eq C (g ≫ f) f g rfl z) rfl
        (nonhomogeneousBivariantRestriction C (gysinSystemOfInvertible C) (g ≫ f) f g rfl z
          (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso C) c)
        (DirectSum.of _ (p : ℤ) (modificationPowerSum C f b hA z t hQ p hT hzero))
```

**`Stacks.Chow.nonhomogeneousBivariantTransport_compositeOfInvertible_modificationChernClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/Commutation.lean, line 422](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/Commutation.lean#L422). The attribute's comment: “for c'\_p: c'\_p(Q) ∘ c = c ∘ c'\_p(Q) in A^*(Y ×\_X Z → X), for every c in A^*(Y → X)”.

> In the situation of Stacks 0F9K with `Q|_T` finite locally free of rank `< p` in degree `0`,
> let `g : Y ⟶ X` be locally of finite type and let `c ∈ A^*(Y ⟶ X)`. Then
>
>   `c'_p(Q) ∘ c = c ∘ c'_p(Q)`   in   `A^*(Y ×_X Z ⟶ X)`,
>
> where `c'_p(Q) ∘ c = res(c'_p(Q)) ∘ c` is a class for `Z ×_X Y ⟶ X`, carried to `Y ×_X Z` along
> the symmetry of the fibre product, and `c ∘ c'_p(Q) = res(c) ∘ c'_p(Q)`.

```lean
theorem nonhomogeneousBivariantTransport_compositeOfInvertible_modificationChernClass
    (hT : ∀ w, modificationProjectionAtInfinity f b w ∉ Set.range z → w ∈ Set.range t)
    (hrank : ∃ M : T.Modules, IsFiniteLocallyFreeOfRankLT M p ∧
      Nonempty ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
        (t ≫ modificationInclusionAtInfinity f b).toLRSHom.toShHom).obj Q ≅
          (DerivedCategory.singleFunctor _ 0).obj M))
    (c : nonhomogeneousBivariantGroup C (gysinSystemOfInvertible C) (g ≫ f) f g rfl) :
    nonhomogeneousBivariantTransport C (gysinSystemOfInvertible C) (pullback.fst z g ≫ (z ≫ f))
        (pullback.fst g z ≫ (g ≫ f)) f (pullback.snd z g ≫ g)
        (comp_comp_structureMorphism_eq
          (pullbackSnd_comp_structureMorphism_eq C (z ≫ f) f z rfl g) rfl)
        (pullback.snd g z ≫ z)
        (comp_comp_structureMorphism_eq
          (pullbackSnd_comp_structureMorphism_eq C (g ≫ f) f g rfl z) rfl)
        (pullbackSymmetry z g) (by simp [pullback.condition])
        (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso C)
        (nonhomogeneousBivariantCompositeOfInvertible C (pullback.fst z g ≫ (z ≫ f)) (g ≫ f) f
          (pullback.snd z g) g
          (pullbackSnd_comp_structureMorphism_eq C (z ≫ f) f z rfl g) rfl
          (DirectSum.of _ (p : ℤ)
            (bivariantRestriction C (gysinSystemOfInvertible C) (z ≫ f) f z rfl g p
              (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso C)
              (modificationChernClass C f b hA z t hQ p hT hrank))) c) =
      nonhomogeneousBivariantCompositeOfInvertible C (pullback.fst g z ≫ (g ≫ f)) (z ≫ f) f
        (pullback.snd g z) z
        (pullbackSnd_comp_structureMorphism_eq C (g ≫ f) f g rfl z) rfl
        (nonhomogeneousBivariantRestriction C (gysinSystemOfInvertible C) (g ≫ f) f g rfl z
          (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso C) c)
        (DirectSum.of _ (p : ℤ) (modificationChernClass C f b hA z t hQ p hT hrank))
```

**`Stacks.Chow.GysinAtInfinity.localizedPowerSumAtInfinity_comp_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedClassAtInfinity/Commuting.lean, line 333](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedClassAtInfinity/Commuting.lean#L333). The attribute's comment: “the classes P'\_p: P'\_p(Q) ∘ c = c ∘ P'\_p(Q) for every bivariant class c”.

> **Stacks 0FAW, for the classes `P'_p`.** Let `(S, δ)` be as in Situation 02QL, let `X` be
> locally of finite type over `S`, let `Z ⊆ X` be a closed subscheme, let `b : W ⟶ 𝐏¹_X` be a
> proper morphism which is an isomorphism over `𝐀¹_X` (A1), let `Q ∈ D(𝒪_W)` be perfect with
> defined Chern classes (A0), and let `T ⊆ W_∞` be a closed subscheme containing all points of
> `W_∞` lying over `X \ Z` with `Q|_T` zero (A2). Let `fY : Y ⟶ X` be locally of finite type and
> `c ∈ A^r(Y ⟶ X)`. Then
>
>   `P'_p(Q) ∘ c = c ∘ P'_p(Q)`   in   `A^{p+r}(Y ×_X Z ⟶ X)`,
>
> where `P'_p(Q) ∈ A^p(Z ⟶ X)` is the class of Stacks 0F9K. As in Remark 0FA2 (and Stacks 0FAS),
> `P'_p(Q) ∘ c = res(P'_p(Q)) ∘ c` with `res(P'_p(Q)) ∈ A^p(Z ×_X Y ⟶ Y)` the restriction along
> `fY` (Remark 0F9Z), and `c ∘ P'_p(Q) = res(c) ∘ P'_p(Q)` with `res(c) ∈ A^r(Y ×_X Z ⟶ Z)`; the
> second composite is read on `Z ×_X Y` through the canonical isomorphism and in degree `p + r`.
> The bivariant classes are those of Stacks 0B76, `Stacks.Chow.BivariantChowClass`.

```lean
theorem localizedPowerSumAtInfinity_comp_comm
    (perfect : RingedSpace.IsPerfect.{u, u + 1} (X := W.toRingedSpace) Q)
    (hQ : HasDefinedChernClasses Q)
    (hT : ∀ w : modificationFibreAtInfinity f b,
      (modificationProjectionAtInfinity f b).base w ∉ Set.range iZ.base → w ∈ Set.range iT.base)
    (p : ℕ) (hzero : IsZero (restrictToInfinity C f b Q iT)) {r : ℤ} {sY : Y ⟶ C.S}
    [LocallyOfFiniteType sY] (hY : fY ≫ f = sY) (c : BivariantChowClass C sY f fY hY r) :
    ((BivariantChowClass.equivBivariantClass.symm
        (localizedPowerSumClassAtInfinity (p := p) C hA iZ hQ perfect hT
          hzero)).restrict fY hY).comp c =
      (((c.restrict iZ rfl).comp (BivariantChowClass.equivBivariantClass.symm
          (localizedPowerSumClassAtInfinity (p := p) C hA iZ hQ perfect hT hzero))).degreeCongr
        (add_comm r (p : ℤ))).transport
        (comp_comp_structureMorphism_eq (BivariantChowClass.restrict_structure_eq rfl fY hY) hY)
        (pullbackSymmetry fY iZ) (pullbackSymmetry_hom_comp_snd_comp iZ fY)
```

**`Stacks.Chow.GysinAtInfinity.localizedChernClassAtInfinity_comp_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedClassAtInfinity/Commuting.lean, line 366](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedClassAtInfinity/Commuting.lean#L366). The attribute's comment: “the classes c'\_p: c'\_p(Q) ∘ c = c ∘ c'\_p(Q) for every bivariant class c”.

> **Stacks 0FAW, for the classes `c'_p`.** Let `(S, δ)` be as in Situation 02QL, let `X` be
> locally of finite type over `S`, let `Z ⊆ X` be a closed subscheme, let `b : W ⟶ 𝐏¹_X` be a
> proper morphism which is an isomorphism over `𝐀¹_X` (A1), let `Q ∈ D(𝒪_W)` be perfect with
> defined Chern classes (A0), and let `T ⊆ W_∞` be a closed subscheme containing all points of
> `W_∞` lying over `X \ Z` with `Q|_T` isomorphic to a finite locally free `𝒪_T`-module of
> rank `< p` sitting in cohomological degree `0` (A2). Let `fY : Y ⟶ X` be locally of finite type
> and `c ∈ A^r(Y ⟶ X)`. Then
>
>   `c'_p(Q) ∘ c = c ∘ c'_p(Q)`   in   `A^{p+r}(Y ×_X Z ⟶ X)`,
>
> where `c'_p(Q) ∈ A^p(Z ⟶ X)` is the class of Stacks 0F9K, the composites being read as in
> `Stacks.Chow.GysinAtInfinity.localizedPowerSumAtInfinity_comp_comm`.

```lean
theorem localizedChernClassAtInfinity_comp_comm
    (_perfect : RingedSpace.IsPerfect.{u, u + 1} (X := W.toRingedSpace) Q)
    (hQ : HasDefinedChernClasses Q)
    (hT : ∀ w : modificationFibreAtInfinity f b,
      (modificationProjectionAtInfinity f b).base w ∉ Set.range iZ.base → w ∈ Set.range iT.base)
    (p : ℕ)
    (hsmall : RestrictionIsLocallyFreeOfRankLT f b iT Q p)
    {r : ℤ} {sY : Y ⟶ C.S} [LocallyOfFiniteType sY] (hY : fY ≫ f = sY)
    (c : BivariantChowClass C sY f fY hY r) :
    ((BivariantChowClass.equivBivariantClass.symm
        (localizedChernClassAtInfinity C hA iZ hQ hT hsmall)).restrict fY hY).comp c =
      (((c.restrict iZ rfl).comp (BivariantChowClass.equivBivariantClass.symm
          (localizedChernClassAtInfinity C hA iZ hQ hT hsmall))).degreeCongr
        (add_comm r (p : ℤ))).transport
        (comp_comp_structureMorphism_eq (BivariantChowClass.restrict_structure_eq rfl fY hY) hY)
        (pullbackSymmetry fY iZ) (pullbackSymmetry_hom_comp_snd_comp iZ fY)
```

## Tag 0FAX, a lemma

[Tag 0FAX](https://stacks.math.columbia.edu/tag/0FAX) in the Stacks Project.

**`Stacks.Chow.modificationPowerSum_succ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/PreparationNewton.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/PreparationNewton.lean#L123). The attribute's comment: “Newton's recursion P'\_\{p+1} = ∑\_\{j`<`p} (-1)^j c'\_\{j+1} P'\_\{p-j} + (-1)^p (p+1) c'\_\{p+1}, for every p ≥ 0, with the multiplication of 0FA0; it determines every displayed identity and the ones after it (and so on)”.

> In the situation of Stacks 0F9K, assume that `Q|_T` is zero, so that `c'_p(Q)` is defined
> for every `p ≥ 1`. Then the classes `P'_p(Q) ∈ A^p(Z ⟶ X)` are Newton's
> polynomials in the classes `c'_i(Q)`, with the multiplication of Stacks 0FA0
> (`(c, c') ↦ res(c) ∘ c'`, `Stacks.Chow.supportedMul`):
>
>   `P'_{p+1}(Q) = ∑_{j < p} (-1)^j c'_{j+1}(Q) P'_{p-j}(Q) + (-1)^p (p + 1) c'_{p+1}(Q)`
>
> for every `p ≥ 0`. This is the recursion defining the universal power-sum polynomials, so
> `P'_1 = c'_1`, `P'_2 = c'_1² - 2c'_2`, `P'_3 = c'_1³ - 3c'_1c'_2 + 3c'_3`, and so on. The summand
> `c'_{j+1} P'_{p-j}` lies in `A^{(j+1)+(p-j)}(Z ⟶ X)`, read in degree `p + 1`.

```lean
theorem modificationPowerSum_succ (q : ℕ) :
    modificationPowerSum C f b hA z t hQ (q + 1) hT hzero =
      ∑ j ∈ (Finset.range q).attach, ((-1 : ℤ) ^ (j : ℕ)) •
          bivariantClassDegreeCongr C _ (z ≫ f) f z rfl
            (newton_degree_eq (Finset.mem_range.mp j.2))
            (supportedMul C (z ≫ f) f z rfl
              (modificationChernClassOfIsZero C f b hA z t hQ hT hzero ((j : ℕ) + 1)
                (Nat.succ_pos _))
              (modificationPowerSum C f b hA z t hQ (q - j) hT hzero)) +
        ((-1 : ℤ) ^ q * ((q : ℤ) + 1)) •
          modificationChernClassOfIsZero C f b hA z t hQ hT hzero (q + 1) (Nat.succ_pos _)
```

**`Stacks.Chow.modificationPowerSum_first_four`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/PreparationNewton.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/PreparationNewton.lean#L152). The attribute's comment: “the four displayed identities, with the multiplication of 0FA0”.

> In the situation of Stacks 0F9K, with `Q|_T` zero,
>
> * `P'_1 = c'_1`,
> * `P'_2 = c'_1² - 2c'_2`,
> * `P'_3 = c'_1³ - 3c'_1c'_2 + 3c'_3`,
> * `P'_4 = c'_1⁴ - 4c'_1²c'_2 + 4c'_1c'_3 + 2c'_2² - 4c'_4`
>
> in `A^p(Z ⟶ X)`, with the multiplication `(c, c') ↦ res(c) ∘ c'` of Stacks 0FA0
> (`Stacks.Chow.supportedMul`), products bracketed to the right and read in the degree of the
> left-hand side. The general case ("and so on") is `Stacks.Chow.modificationPowerSum_succ`.

```lean
theorem modificationPowerSum_first_four :
    let c := fun i (hi : 0 < i) =>
      modificationChernClassOfIsZero C f b hA z t hQ hT hzero i hi
    let m := fun {a b : ℤ} (x : BivariantClass C (gysinSystemOfInvertible C) (z ≫ f) f z rfl a)
      (y : BivariantClass C (gysinSystemOfInvertible C) (z ≫ f) f z rfl b) =>
        supportedMul C (z ≫ f) f z rfl x y
    let P := fun q => modificationPowerSum C f b hA z t hQ q hT hzero
    let d := fun {a b : ℤ} (h : a = b) =>
      bivariantClassDegreeCongr C (gysinSystemOfInvertible C) (z ≫ f) f z rfl h
    P 1 = c 1 (by norm_num) ∧
    P 2 = d (by norm_num) (m (c 1 (by norm_num)) (c 1 (by norm_num))) -
      (2 : ℤ) • c 2 (by norm_num) ∧
    P 3 = d (by norm_num) (m (c 1 (by norm_num)) (d (by norm_num : (1 : ℤ) + 1 = 2)
        (m (c 1 (by norm_num)) (c 1 (by norm_num))))) -
      (3 : ℤ) • d (by norm_num) (m (c 1 (by norm_num)) (c 2 (by norm_num))) +
      (3 : ℤ) • c 3 (by norm_num) ∧
    P 4 = d (by norm_num) (m (c 1 (by norm_num)) (d (by norm_num : (1 : ℤ) + 2 = 3)
        (m (c 1 (by norm_num)) (d (by norm_num : (1 : ℤ) + 1 = 2)
          (m (c 1 (by norm_num)) (c 1 (by norm_num))))))) -
      (4 : ℤ) • d (by norm_num) (m (c 1 (by norm_num)) (d (by norm_num : (1 : ℤ) + 2 = 3)
        (m (c 1 (by norm_num)) (c 2 (by norm_num))))) +
      (4 : ℤ) • d (by norm_num) (m (c 1 (by norm_num)) (c 3 (by norm_num))) +
      (2 : ℤ) • d (by norm_num) (m (c 2 (by norm_num)) (c 2 (by norm_num))) -
      (4 : ℤ) • c 4 (by norm_num)
```

## Tag 0FAY, a lemma

[Tag 0FAY](https://stacks.math.columbia.edu/tag/0FAY) in the Stacks Project.

**`Stacks.Chow.modificationTotalChernClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/PreparationWhitney.lean, line 220](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/PreparationWhitney.lean#L220). The attribute's comment: “the class c^(p)(Q) in A^(p)(Z → X)”.

> **The class `c^{(p)}(Q) ∈ A^{(p)}(Z ⟶ X)` of Stacks 0FAY.** In the situation of Stacks 0F9K
> (`Stacks.Chow.modificationChernClass`), with `Q|_T` isomorphic to a finite locally free module of
> rank `< p` placed in degree `0`,
>
>   `c^{(p)}(Q) = 1 + c_1(Q|_{X × {0}}) + … + c_{p-1}(Q|_{X × {0}}) + c'_p(Q) + c'_{p+1}(Q) + …`:
>
> its component in a degree `0 ≤ i < p` is `c_i(Q|_{X × {0}}) ∈ A^i(X)`, with `Q|_{X × {0}}` the
> derived pullback along the section at zero, in a negative degree it is `0`, and in a degree
> `i ≥ p` it is the class `c'_i(Q) ∈ A^i(Z ⟶ X)` of Stacks 0F9K, which is defined since a rank
> `< p` is a rank `< i`.

```lean
def modificationTotalChernClass (p : ℕ)
    (hT : ∀ w, modificationProjectionAtInfinity f b w ∉ Set.range z → w ∈ Set.range t)
    (hrank : ∃ M : T.Modules, IsFiniteLocallyFreeOfRankLT M p ∧
      Nonempty ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
        (t ≫ modificationInclusionAtInfinity f b).toLRSHom.toShHom).obj Q ≅
          (DerivedCategory.singleFunctor _ 0).obj M)) :
    localizedBivariantGrading C (gysinSystemOfInvertible C) (z ≫ f) f z rfl p
```

**`Stacks.Chow.modificationTotalChernClass_biprod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/PreparationWhitney.lean, line 304](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/PreparationWhitney.lean#L304). The attribute's comment: “c^(p+p')(Q ⊕ Q') = c^(p)(Q) c^(p')(Q') in A^(p+p')(Z → X), with the multiplication of 0FA0”.

> In the situation of Stacks 0F9K, let `Q, Q' ∈ D(𝒪_W)` have defined Chern classes, with `Q|_T`
> and `Q'|_T` isomorphic to finite locally free modules of ranks `< p` and `< p'` placed in degree
> `0`. Then
>
>   `c^{(p+p')}(Q ⊕ Q') = c^{(p)}(Q) c^{(p')}(Q')`   in `A^{(p+p')}(Z ⟶ X)`,
>
> with the classes of `Stacks.Chow.modificationTotalChernClass` and the multiplication of
> Stacks 0FA0 (`Stacks.Chow.localizedGradingMul`). The hypothesis on `(Q ⊕ Q')|_T`, under which
> `c^{(p+p')}(Q ⊕ Q')` is defined, follows from those on `Q|_T` and `Q'|_T`
> (`Stacks.Chow.exists_isFiniteLocallyFreeOfRankLT_derivedPullback_biprod`), and so does the
> definedness of the Chern classes of `Q ⊕ Q'` (`Stacks.Chow.hasDefinedChernClasses_biprod`).
> Perfectness of `Q`, `Q'` is not used, only that their Chern classes are defined.

```lean
theorem modificationTotalChernClass_biprod
    (hrank : ∃ M : T.Modules, IsFiniteLocallyFreeOfRankLT M p ∧
      Nonempty ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
        (t ≫ modificationInclusionAtInfinity f b).toLRSHom.toShHom).obj Q ≅
          (DerivedCategory.singleFunctor _ 0).obj M))
    (hrank' : ∃ M : T.Modules, IsFiniteLocallyFreeOfRankLT M p' ∧
      Nonempty ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
        (t ≫ modificationInclusionAtInfinity f b).toLRSHom.toShHom).obj Q' ≅
          (DerivedCategory.singleFunctor _ 0).obj M)) :
    modificationTotalChernClass C f b hA z t (hasDefinedChernClasses_biprod hQ hQ') (p + p') hT
        (exists_isFiniteLocallyFreeOfRankLT_derivedPullback_biprod _ hrank hrank') =
      localizedGradingMul C (z ≫ f) f z rfl
        (modificationTotalChernClass C f b hA z t hQ p hT hrank)
        (modificationTotalChernClass C f b hA z t hQ' p' hT hrank')
```

## Tag 0FAZ, a lemma

[Tag 0FAZ](https://stacks.math.columbia.edu/tag/0FAZ) in the Stacks Project.

**`Stacks.Chow.modificationPowerSum_biprod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/PreparationSum.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/PreparationSum.lean#L66).

> **Stacks 0FAZ.** In the situation of Stacks 0F9K, let `Q, Q' ∈ D(𝒪_W)` have defined Chern
> classes, and let `T ⊆ W_∞` be closed, contain every point of `W_∞` lying over `X ∖ Z`, and be such
> that `Q|_T` and `Q'|_T` are zero. Then the classes `P'_p(Q)`, `P'_p(Q')`, `P'_p(Q ⊕ Q')` of
> `A^p(Z ⟶ X)` constructed in Stacks 0F9K (`Stacks.Chow.modificationPowerSum`) satisfy
> `P'_p(Q ⊕ Q') = P'_p(Q) + P'_p(Q')`.

```lean
theorem modificationPowerSum_biprod (hQ : HasDefinedChernClasses Q)
    (hQ' : HasDefinedChernClasses Q') (p : ℕ)
    (hT : ∀ w, modificationProjectionAtInfinity f b w ∉ Set.range z → w ∈ Set.range t)
    (hzero : IsZero ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
      (t ≫ modificationInclusionAtInfinity f b).toLRSHom.toShHom).obj Q))
    (hzero' : IsZero ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
      (t ≫ modificationInclusionAtInfinity f b).toLRSHom.toShHom).obj Q')) :
    modificationPowerSum C f b hA z t (hasDefinedChernClasses_biprod hQ hQ') p hT
        (isZero_derivedPullback_biprod _ hzero hzero') =
      modificationPowerSum C f b hA z t hQ p hT hzero +
        modificationPowerSum C f b hA z t hQ' p hT hzero'
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.49, Tag 0FAT](https://stacks.math.columbia.edu/tag/0FAT)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
