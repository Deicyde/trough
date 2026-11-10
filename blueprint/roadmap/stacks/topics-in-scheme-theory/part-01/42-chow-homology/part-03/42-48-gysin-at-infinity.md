---
declaration: section
origin: cited
lean: Stacks.Chow.gysinCapOfLift, Stacks.Chow.gysinCapOfLift_eq_of_gysin_pushforward_eq_zero, Stacks.Chow.GysinAtInfinityData, Stacks.Chow.GysinAtInfinity.gysinAtInfinity, Stacks.Chow.gysinAtInfinityClass, Stacks.Chow.gysinAtInfinityData, Stacks.Chow.gysinCapAtInfinity, Stacks.Chow.gysinCapAtInfinity_eq_of_isModificationLift
statement: formalized
proof: formalized
---

# 42.48 Gysin at infinity

Section 42.48 of the Stacks Project, [Tag 0FAP](https://stacks.math.columbia.edu/tag/0FAP). 5 tags here are carried by 22 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0F9J, a lemma

[Tag 0F9J](https://stacks.math.columbia.edu/tag/0F9J) in the Stacks Project.

**`Stacks.Chow.gysinCapOfLift`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinAtInfinity.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinAtInfinity.lean#L270). The attribute's comment: “construction of the cap operation from a lift and a zero-scheme presentation”.

> The cap operation `C ∩ - : A_k(T) ⟶ A_k(W_∞ ×_X T)` built
> from a choice of lift: given a homomorphism `lift : A_k(T) ⟶ A_{k+1}(W ×_X T)` and a presentation
> of the base-changed fibre at infinity as the zero scheme of a global section `s` of an invertible
> module `L` on `W ×_X T`, it is `i_∞^* ∘ lift`, where `i_∞^*` is the Gysin map of `s` followed by
> the identification `e` of that zero scheme with `W_∞ ×_X T`.

```lean
def gysinCapOfLift (C : ChowSituation.{u}) (G : GysinSystem C) {X W T : Scheme.{u}}
    (f : X ⟶ C.S) [LocallyOfFiniteType f] (b : W ⟶ projectiveLineProduct f)
    [LocallyOfFiniteType (modificationProjection f b)]
    [LocallyOfFiniteType (modificationProjectionAtInfinity f b)]
    (g : T ⟶ X) [LocallyOfFiniteType g] (k : ℤ)
    (L : (modificationBaseChange f b g).Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible (modificationBaseChange f b g).sheaf.obj
      (modificationBaseChange f b g).ringCatSheaf.property L]
    (s : Γ(L, ⊤))
    (e : (Stacks.Divisors.zeroScheme (modificationBaseChange f b g) L s).subscheme ≅
      pullback (modificationProjectionAtInfinity f b) g)
    (he : e.hom ≫ modificationInfinityBaseChangeOver f b g =
      modificationZeroSchemeOver C f b g L s)
    (lift : chowGroup C (g ≫ f) k →+ chowGroup C (modificationBaseChangeOver f b g) (k + 1)) :
    chowGroup C (g ≫ f) k →+ chowGroup C (modificationInfinityBaseChangeOver f b g) k
```

**`Stacks.Chow.gysinCapOfLift_eq_of_gysin_pushforward_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinAtInfinity.lean, line 315](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinAtInfinity.lean#L315). The attribute's comment: “independence of the chosen lift”.

> Two lifts whose difference is pushed forward from the fibre at infinity give the same cap
> operation, as soon as the Gysin map of `s` kills everything pushed forward from the fibre at
> infinity.

```lean
theorem gysinCapOfLift_eq_of_gysin_pushforward_eq_zero (C : ChowSituation.{u})
    (G : GysinSystem C) {X W T : Scheme.{u}} (f : X ⟶ C.S) [LocallyOfFiniteType f]
    (b : W ⟶ projectiveLineProduct f) [LocallyOfFiniteType (modificationProjection f b)]
    [LocallyOfFiniteType (modificationProjectionAtInfinity f b)]
    (g : T ⟶ X) [LocallyOfFiniteType g] [IsProper (modificationInfinityBaseChange f b g)]
    (k : ℤ) (L : (modificationBaseChange f b g).Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible (modificationBaseChange f b g).sheaf.obj
      (modificationBaseChange f b g).ringCatSheaf.property L]
    (s : Γ(L, ⊤))
    (e : (Stacks.Divisors.zeroScheme (modificationBaseChange f b g) L s).subscheme ≅
      pullback (modificationProjectionAtInfinity f b) g)
    (he : e.hom ≫ modificationInfinityBaseChangeOver f b g =
      modificationZeroSchemeOver C f b g L s)
    (lift lift' : chowGroup C (g ≫ f) k →+
      chowGroup C (modificationBaseChangeOver f b g) (k + 1))
    (hfac : ProperPushforwardFactorsThroughRationalEquivalence C
      (modificationInfinityBaseChangeOver f b g) (modificationBaseChangeOver f b g)
      (modificationInfinityBaseChange f b g) (modificationInfinityBaseChange_over f b g) (k + 1))
    (hvanish : ∀ γ : chowGroup C (modificationInfinityBaseChangeOver f b g) (k + 1),
      G.onChow (modificationBaseChangeOver f b g) L s k
        (properChowPushforward C (modificationInfinityBaseChangeOver f b g)
          (modificationBaseChangeOver f b g) (modificationInfinityBaseChange f b g)
          (modificationInfinityBaseChange_over f b g) (k + 1) hfac γ) = 0)
    (hdiff : ∀ α : chowGroup C (g ≫ f) k,
      ∃ γ : chowGroup C (modificationInfinityBaseChangeOver f b g) (k + 1),
        lift α - lift' α =
          properChowPushforward C (modificationInfinityBaseChangeOver f b g)
            (modificationBaseChangeOver f b g) (modificationInfinityBaseChange f b g)
            (modificationInfinityBaseChange_over f b g) (k + 1) hfac γ) :
    gysinCapOfLift C G f b g k L s e he lift =
      gysinCapOfLift C G f b g k L s e he lift'
```

**`Stacks.Chow.GysinAtInfinityData`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinAtInfinity.lean, line 360](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinAtInfinity.lean#L360). The attribute's comment: “statement: the canonical class in A⁰(W\_∞ ⟶ X) and its pushforward identity”.

> The conclusion of the Gysin-at-infinity lemma, for a proper morphism
> `b : W ⟶ 𝐏¹_X` which is an isomorphism over the standard affine chart `𝐀¹_X`: a degree-zero
> bivariant class `C ∈ A⁰(W_∞ ⟶ X)` for the fibre at infinity, together with the identity
> `i_{∞,*}(C ∩ α) = i_{0,*} α` on every test scheme locally of finite type over `X`.

```lean
structure GysinAtInfinityData (C : ChowSituation.{u}) (G : GysinSystem C) {X W : Scheme.{u}}
    (f : X ⟶ C.S) [LocallyOfFiniteType f] (b : W ⟶ projectiveLineProduct f) [IsProper b]
    (_hA : IsIso (pullback.snd b (projectiveLineAffineChart f)))
```

**`Stacks.Chow.GysinAtInfinity.gysinAtInfinity`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinAtInfinity/Statement.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinAtInfinity/Statement.lean#L109).

> **Stacks 0F9J.** Let `X` be locally of finite type over the base of chapter 42 and let
> `b : W ⟶ 𝐏¹_X` be proper and an isomorphism over `𝐀¹_X`, with fibre at infinity
> `i_∞ : W_∞ ⟶ W`. The class `C = gysinAtInfinityClass ∈ A⁰(W_∞ ⟶ X)`
>
> * is constructed as in the source: `C ∩ α = i_∞^* β` for every lift `β` of `α`;
> * is canonical: it is the only class with that property;
> * satisfies `i_{∞,*}(C ∩ α) = i_{0,*} α` on every test scheme `T ⟶ X` locally of finite type,
>   that is, for `α ∈ A_k(X)` and similarly after any base change by `X' ⟶ X` locally of finite
>   type; here `i_0` and `i_∞` are the base changes of the section at zero and of the inclusion of
>   the fibre at infinity.

```lean
theorem gysinAtInfinity :
    IsGysinAtInfinityCap C f b hA (gysinAtInfinityClass C f b hA) ∧
      (∀ c, IsGysinAtInfinityCap C f b hA c → c = gysinAtInfinityClass C f b hA) ∧
      haveI := hA
      ∀ {T : Scheme.{u}} (g : T ⟶ X) [LocallyOfFiniteType g] (k : ℤ)
        (α : chowGroup C (g ≫ f) k),
        properChowPushforward C (modificationInfinityBaseChangeOver f b g)
            (modificationBaseChangeOver f b g) (modificationInfinityBaseChange f b g)
            (modificationInfinityBaseChange_over f b g) k
            (properPushforwardFactorsThroughRationalEquivalence_of_isProper C _ _ _ _ k)
            (Eq.mp (congrArg (chowGroup C (modificationInfinityBaseChangeOver f b g))
              (sub_zero k)) ((gysinAtInfinityClass C f b hA).cap g k α)) =
          properChowPushforward C (g ≫ f) (modificationBaseChangeOver f b g)
            (modificationSectionAtZeroBaseChange f b inferInstance
              (modificationSectionAtZero_comp f b) g)
            (modificationSectionAtZeroBaseChange_over f b g inferInstance
              (modificationSectionAtZero_comp f b)) k
            (properPushforwardFactorsThroughRationalEquivalence_of_isProper C _ _ _ _ k) α
```

**`Stacks.Chow.gysinAtInfinityClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinAtInfinityClass.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinAtInfinityClass.lean#L64). The attribute's comment: “the canonical bivariant class C in A⁰(W\_∞ ⟶ X)”.

> **Stacks 0F9J, the class at infinity.** The degree-zero bivariant class
> `C ∈ A⁰(W_∞ ⟶ X)` whose cap operation on a test scheme `T ⟶ X` is `α ↦ i_∞^* β` for a lift `β`
> of `α` to `W ×_X T` (`Stacks.Chow.gysinCapAtInfinity`).

```lean
def gysinAtInfinityClass :
    BivariantClass C (gysinSystemOfInvertible C) (modificationProjectionAtInfinity f b ≫ f) f
      (modificationProjectionAtInfinity f b) rfl 0
```

**`Stacks.Chow.gysinAtInfinityData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinAtInfinityClass.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinAtInfinityClass.lean#L112). The attribute's comment: “the class C in A⁰(W\_∞ ⟶ X) with i\_\{∞,*}(C ∩ α) = i\_\{0,*} α, built from the cap operation i\_∞^* of a lift and its three bivariance laws”.

> **Stacks 0F9J.** The class at infinity `C ∈ A⁰(W_∞ ⟶ X)` of `Stacks.Chow.gysinAtInfinityClass`
> together with the identity `i_{∞,*}(C ∩ α) = i_{0,*} α` on every test scheme locally of finite
> type over `X` (`Stacks.Chow.chowPushforward_gysinCapOfLift`).

```lean
def gysinAtInfinityData : GysinAtInfinityData C (gysinSystemOfInvertible C) f b hA
```

**`Stacks.Chow.gysinCapAtInfinity`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinAtInfinityLift.lean, line 702](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinAtInfinityLift.lean#L702). The attribute's comment: “the cap operation of the class at infinity on a test scheme: i\_∞^* of a lift”.

> **Stacks 0F9J, the cap operation.** `C ∩ - : A_k(T) ⟶ A_k(W_∞ ×_X T)`, `α ↦ i_∞^* β` for a
> lift `β` of `α` (`Stacks.Chow.IsModificationLift`). A lift is chosen; by
> `Stacks.Chow.gysinCapAtInfinity_eq_of_isModificationLift` the value is the same for every
> lift, and that independence is what makes the operation additive.

```lean
def gysinCapAtInfinity :
    chowGroup C (g ≫ f) k →+ chowGroup C (modificationInfinityBaseChangeOver f b g) k
```

**`Stacks.Chow.gysinCapAtInfinity_eq_of_isModificationLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinAtInfinityLift.lean, line 726](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinAtInfinityLift.lean#L726). The attribute's comment: “independence of the chosen lift: C ∩ α = i\_∞^* β for every lift β of α”.

> **Stacks 0F9J, independence of the chosen lift.** The cap operation is `i_∞^* β` for *every*
> lift `β` of `α`: two lifts differ by a class supported on the fibre at infinity (Stacks 02RX), and
> the Gysin map at infinity kills such classes because the normal bundle of the divisor at infinity
> is trivial (Remark 0B6Z).

```lean
theorem gysinCapAtInfinity_eq_of_isModificationLift (α : chowGroup C (g ≫ f) k)
    (β : chowGroup C (modificationBaseChangeOver f b g) (k + 1))
    (hβ : IsModificationLift C f b hA g k α β) :
    gysinCapAtInfinity C f b hA g k α = modificationInfinityGysin C f b g k β
```

**`Stacks.Chow.GysinAtInfinityCapPresentation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinAtInfinityPresentation.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinAtInfinityPresentation.lean#L56). The attribute's comment: “the construction of the class at infinity, as a presentation of its cap operation by a lift and a Gysin step”.

> A presentation of the cap operation of the Gysin class at infinity `C ∈ A⁰(W_∞ ⟶ X)` as
> the composite of a lift with the Gysin map of the divisor at infinity: on every test scheme
> `g : T ⟶ X` locally of finite type and in every degree `k`, additive maps
> `lift : CH_k(T) ⟶ CH_{k+1}(W ×_X T)` and `gysinStep : CH_{k+1}(W ×_X T) ⟶ CH_k(W_∞ ×_X T)`
> with `C ∩ α = gysinStep (lift α)`.

```lean
structure GysinAtInfinityCapPresentation (C : ChowSituation.{u}) (G : GysinSystem C)
    {X W : Scheme.{u}} (f : X ⟶ C.S) [LocallyOfFiniteType f]
    (b : W ⟶ projectiveLineProduct f) [IsProper b]
    (hA : IsIso (pullback.snd b (projectiveLineAffineChart f)))
    [LocallyOfFiniteType (modificationProjection f b)]
    [LocallyOfFiniteType (modificationProjectionAtInfinity f b)]
    (D : GysinAtInfinityData C G f b hA)
```

**`Stacks.Chow.chowPushforward_gysinCapOfLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinAtInfinityPushforward.lean, line 736](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinAtInfinityPushforward.lean#L736). The attribute's comment: “the pushforward identity i\_\{∞,*}(C ∩ α) = i\_\{0,*} α on every test scheme locally of finite type over X”.

> **Stacks 0F9J, the pushforward identity.** On every test scheme `g : T ⟶ X` locally of finite
> type, `i_{∞,*}(C ∩ α) = i_{0,*} α` in `A_k(W ×_X T)`, for the cap operation
> `Stacks.Chow.gysinCapAtInfinity` of the class at infinity.
>
> For a lift `β` of `α`, `C ∩ α = i_∞^* β`; the Gysin images `i_∞^* β` and `i_0^* β` have the same
> pushforward to `W ×_X T`, the divisors `D_0` and `D_∞` of `𝐏¹` being rationally equivalent
> (`Stacks.Chow.modificationZeroGysin_eq_infinityGysin`); and `i_0^* β = α`
> (`Stacks.Chow.chowPushforward_zeroGysin_of_isModificationLift`).

```lean
theorem chowPushforward_gysinCapOfLift
    (hA : IsIso (pullback.snd b (projectiveLineAffineChart f))) (k : ℤ)
    (α : chowGroup C (g ≫ f) k) :
    haveI := isClosedImmersion_modificationSectionAtZeroBaseChange f b g hA
    chowPushforwardOfIsClosedImmersion C (modificationInfinityBaseChangeOver f b g)
        (modificationBaseChangeOver f b g) (modificationInfinityBaseChange f b g)
        (modificationInfinityBaseChange_over f b g) k (gysinCapAtInfinity C f b hA g k α) =
      chowPushforwardOfIsClosedImmersion C (g ≫ f) (modificationBaseChangeOver f b g)
        (modificationSectionAtZeroBaseChange f b (isIso_modificationFibreAtZeroProjection f b hA)
          (modificationSectionAtZero_comp_projection f b hA) g)
        (modificationSectionAtZeroBaseChange_over f b g _ _) k α
```

## Tag 0GUH, a lemma

[Tag 0GUH](https://stacks.math.columbia.edu/tag/0GUH) in the Stacks Project.

**`Stacks.Chow.GysinAtInfinity.gysinAtInfinityClass_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinAtInfinity/BaseChange.lean, line 583](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinAtInfinity/BaseChange.lean#L583).

> **Stacks 0GUH.** Let `X` be locally of finite type over the base of chapter 42, let
> `b : W ⟶ 𝐏¹_X` be proper and an isomorphism over `𝐀¹_X`, and let `C ∈ A⁰(W_∞ ⟶ X)` be the class
> of Stacks 0F9J. Let `q : X' ⟶ X` be locally of finite type and let
> `b' : W' = W ×_{𝐏¹_X} 𝐏¹_{X'} ⟶ 𝐏¹_{X'}` be the base change of `b`, with fibre at infinity
> `i'_∞ : W'_∞ ⟶ W'` (the base change of `i_∞`). Then `b'` is again proper and an isomorphism over
> `𝐀¹_{X'}`, and the class `C' ∈ A⁰(W'_∞ ⟶ X')` constructed as in Stacks 0F9J using `b'` is the
> restriction `res(C)` of Remark 0F9Z.
>
> The restriction is a class for the chosen fibre product `W_∞ ×_X X' ⟶ X'`; it is read as a class
> for `W'_∞ ⟶ X'` along the canonical identification `W_∞ ×_X X' ≅ W'_∞` over `X'`.

```lean
theorem gysinAtInfinityClass_baseChange
    (hA : IsIso (pullback.snd b (projectiveLineAffineChart f))) :
    haveI := hA
    gysinAtInfinityClass C (q ≫ f) (baseChangedModification f b q) inferInstance =
      bivariantTransport C (gysinSystemOfInvertible C)
        (pullback.fst (modificationProjectionAtInfinity f b) q ≫
          (modificationProjectionAtInfinity f b ≫ f))
        (modificationProjectionAtInfinity (q ≫ f) (baseChangedModification f b q) ≫ (q ≫ f))
        (q ≫ f) (pullback.snd (modificationProjectionAtInfinity f b) q)
        (pullbackSnd_comp_structureMorphism_eq C (modificationProjectionAtInfinity f b ≫ f) f
          (modificationProjectionAtInfinity f b) rfl q)
        (modificationProjectionAtInfinity (q ≫ f) (baseChangedModification f b q)) rfl
        (baseChangedInfinityIso f b q) (baseChangedInfinityIso_hom_comp f b q) 0
        (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso C)
        (bivariantRestrictionOfInvertible C (modificationProjectionAtInfinity f b ≫ f) f
          (modificationProjectionAtInfinity f b) rfl q 0 (gysinAtInfinityClass C f b hA))
```

**`Stacks.Chow.gysinAtInfinity_baseChange_cap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinAtInfinityBaseChange.lean, line 263](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinAtInfinityBaseChange.lean#L263). The attribute's comment: “on cap operations: given the construction of Stacks 0F9J as a presentation of each cap operation by a lift and a Gysin step, and the compatibility of each of those two factors with the base change (the source's `a similar statement holds for flat pullback and i_infty^*`), the class constructed from the base-changed modification caps as the original one does”.

> **Stacks 0GUH, on cap operations**, conditional on the construction of Stacks 0F9J for both
> modifications and its compatibility with base change.
>
> For every test scheme `g : T ⟶ X'` locally of finite type, `C' ∩ α = C ∩ α` after the canonical
> identification `W_∞ ×_X T ≅ W'_∞ ×_{X'} T` of the two base changes of the fibre at infinity. This
> is the form the source's proof produces; the equality of bivariant classes asserted by the tag is
> `Stacks.Chow.gysinAtInfinity_eq_bivariantTransport_bivariantRestriction`.

```lean
theorem gysinAtInfinity_baseChange_cap
    (hlift : ∀ {T : Scheme.{u}} (g : T ⟶ X') [LocallyOfFiniteType g] (k : ℤ)
        (α : chowGroup C (g ≫ (q ≫ f)) k),
      P'.lift g k α =
        chowPushforwardOfIso C (modificationBaseChangeOver f b (g ≫ q))
          (modificationBaseChangeOver (q ≫ f) b' g)
          (modificationBaseChangeComparison C f b q b' η hη g)
          (modificationBaseChangeComparison_comp_base C f b q b' η hη g) (k + 1)
          (P.lift (g ≫ q) k (chowGroupCongr C (Category.assoc g q f).symm k α)))
    (hgysinStep : ∀ {T : Scheme.{u}} (g : T ⟶ X') [LocallyOfFiniteType g] (k : ℤ)
        (β : chowGroup C (modificationBaseChangeOver f b (g ≫ q)) (k + 1)),
      P'.gysinStep g k
          (chowPushforwardOfIso C (modificationBaseChangeOver f b (g ≫ q))
            (modificationBaseChangeOver (q ≫ f) b' g)
            (modificationBaseChangeComparison C f b q b' η hη g)
            (modificationBaseChangeComparison_comp_base C f b q b' η hη g) (k + 1) β) =
        chowPushforwardOfIso C (modificationInfinityBaseChangeOver f b (g ≫ q))
          (modificationInfinityBaseChangeOver (q ≫ f) b' g)
          (modificationInfinityBaseChangeComparison C f b q b' θ hθ g)
          (modificationInfinityBaseChangeComparison_comp_base C f b q b' θ hθ g) k
          (P.gysinStep (g ≫ q) k β))
    {T : Scheme.{u}} (g : T ⟶ X') [LocallyOfFiniteType g] (k : ℤ)
    (α : chowGroup C (g ≫ (q ≫ f)) k) :
    D'.bivariantClass.cap g k α =
      chowPushforwardOfIso C (modificationInfinityBaseChangeOver f b (g ≫ q))
        (modificationInfinityBaseChangeOver (q ≫ f) b' g)
        (modificationInfinityBaseChangeComparison C f b q b' θ hθ g)
        (modificationInfinityBaseChangeComparison_comp_base C f b q b' θ hθ g) (k - 0)
        (D.bivariantClass.cap (g ≫ q) k
          (chowGroupCongr C (Category.assoc g q f).symm k α))
```

**`Stacks.Chow.gysinAtInfinity_eq_bivariantTransport_bivariantRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinAtInfinityBaseChange.lean, line 345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinAtInfinityBaseChange.lean#L345). The attribute's comment: “given the construction of Stacks 0F9J as a presentation of each cap operation by a lift and a Gysin step, and the compatibility of each of those two factors with the base change (the source's `a similar statement holds for flat pullback and i_infty^*`), together with the isomorphism case of Stacks 02TA for the Gysin system that Stacks 0F9Z needs”.

> **Stacks 0GUH.** In the setting of Stacks 0F9J let `q : X' ⟶ X` be locally of finite type and
> let `b' : W' ⟶ 𝐏¹_{X'}` and `i'_∞ : W'_∞ ⟶ W'` be the base changes of `b` and `i_∞`. Then the
> class `C' ∈ A⁰(W'_∞ ⟶ X')` constructed as in Stacks 0F9J using `b'` is the restriction (Remark
> 0F9Z) of `C`: it equals `Stacks.Chow.bivariantRestriction` of `C` along `q`, carried along the
> identification `W_∞ ×_X X' ≅ W'_∞` by `Stacks.Chow.bivariantTransport`.
>
> The transport is needed only because `Stacks.Chow.bivariantRestriction` produces a class for the
> chosen fibre product `W_∞ ×_X X' ⟶ X'`, whereas `C'` is a class for `W'_∞ ⟶ X'`; the tag
> identifies the two silently. Both constructions are the library's own.
>
> The hypotheses are the base-change witnesses `η`, `θ`, the construction of Stacks 0F9J for both
> modifications, and the compatibility of each of its two factors with the base change; see the
> implementation notes of `StacksFrontier.AlgebraicGeometry.Chow.GysinAtInfinityBaseChange`.

```lean
theorem gysinAtInfinity_eq_bivariantTransport_bivariantRestriction
    (hgys : G.IsNaturalUnderBaseChangeIso)
    (hlift : ∀ {T : Scheme.{u}} (g : T ⟶ X') [LocallyOfFiniteType g] (k : ℤ)
        (α : chowGroup C (g ≫ (q ≫ f)) k),
      P'.lift g k α =
        chowPushforwardOfIso C (modificationBaseChangeOver f b (g ≫ q))
          (modificationBaseChangeOver (q ≫ f) b' g)
          (modificationBaseChangeComparison C f b q b' η hη g)
          (modificationBaseChangeComparison_comp_base C f b q b' η hη g) (k + 1)
          (P.lift (g ≫ q) k (chowGroupCongr C (Category.assoc g q f).symm k α)))
    (hgysinStep : ∀ {T : Scheme.{u}} (g : T ⟶ X') [LocallyOfFiniteType g] (k : ℤ)
        (β : chowGroup C (modificationBaseChangeOver f b (g ≫ q)) (k + 1)),
      P'.gysinStep g k
          (chowPushforwardOfIso C (modificationBaseChangeOver f b (g ≫ q))
            (modificationBaseChangeOver (q ≫ f) b' g)
            (modificationBaseChangeComparison C f b q b' η hη g)
            (modificationBaseChangeComparison_comp_base C f b q b' η hη g) (k + 1) β) =
        chowPushforwardOfIso C (modificationInfinityBaseChangeOver f b (g ≫ q))
          (modificationInfinityBaseChangeOver (q ≫ f) b' g)
          (modificationInfinityBaseChangeComparison C f b q b' θ hθ g)
          (modificationInfinityBaseChangeComparison_comp_base C f b q b' θ hθ g) k
          (P.gysinStep (g ≫ q) k β)) :
    D'.bivariantClass =
      bivariantTransport C G
        (pullback.fst (modificationProjectionAtInfinity f b) q ≫
          (modificationProjectionAtInfinity f b ≫ f))
        (modificationProjectionAtInfinity (q ≫ f) b' ≫ (q ≫ f)) (q ≫ f)
        (pullback.snd (modificationProjectionAtInfinity f b) q)
        (pullbackSnd_comp_structureMorphism_eq C (modificationProjectionAtInfinity f b ≫ f) f
          (modificationProjectionAtInfinity f b) rfl q)
        (modificationProjectionAtInfinity (q ≫ f) b') rfl θ hθ 0 hgys
        (bivariantRestriction C G (modificationProjectionAtInfinity f b ≫ f) f
          (modificationProjectionAtInfinity f b) rfl q 0 hgys D.bivariantClass)
```

**`Stacks.Chow.gysinAtInfinityClass_restrictedModification_eq_bivariantRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinAtInfinityRestrictedBaseChange.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinAtInfinityRestrictedBaseChange.lean#L288). The attribute's comment: “the class C' of Lemma 0F9J for the base change b' is the restriction of C”.

> In the setting of Stacks 0F9J let `q : X' ⟶ X` be locally of finite type and let
> `b' : W' = W ×_{𝐏¹_X} 𝐏¹_{X'} ⟶ 𝐏¹_{X'}` and `i'_∞ : W'_∞ ⟶ W'` be the base changes of `b` and
> `i_∞` (`Stacks.Chow.GysinAtInfinity.baseChangedModification`). Then the class
> `C' ∈ A⁰(W'_∞ ⟶ X')` of Stacks 0F9J for `b'` is the restriction (Remark 0F9Z) of `C`: it equals
> `Stacks.Chow.bivariantRestriction` of `C` along `q`, carried along the canonical identification
> `W_∞ ×_X X' ≅ W'_∞` by `Stacks.Chow.bivariantTransport`.

```lean
theorem gysinAtInfinityClass_restrictedModification_eq_bivariantRestriction :
    gysinAtInfinityClass C (q ≫ f) (baseChangedModification f b q)
        (isIso_restrictedModification_affineChart f b q hA) =
      bivariantTransport C (gysinSystemOfInvertible C)
        (pullback.fst (modificationProjectionAtInfinity f b) q ≫
          (modificationProjectionAtInfinity f b ≫ f))
        (modificationProjectionAtInfinity (q ≫ f) (baseChangedModification f b q) ≫ (q ≫ f))
        (q ≫ f) (pullback.snd (modificationProjectionAtInfinity f b) q)
        (pullbackSnd_comp_structureMorphism_eq C (modificationProjectionAtInfinity f b ≫ f) f
          (modificationProjectionAtInfinity f b) rfl q)
        (modificationProjectionAtInfinity (q ≫ f) (baseChangedModification f b q)) rfl
        (restrictedModificationInfinityIso f b q)
        (restrictedModificationInfinityIso_hom_projection f b q) 0
        (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso C)
        (bivariantRestriction C (gysinSystemOfInvertible C)
          (modificationProjectionAtInfinity f b ≫ f) f (modificationProjectionAtInfinity f b) rfl
          q 0 (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso C)
          (gysinAtInfinityClass C f b hA))
```

## Tag 0FAQ, a lemma

[Tag 0FAQ](https://stacks.math.columbia.edu/tag/0FAQ) in the Stacks Project.

**`Stacks.Chow.gysinAtInfinityClass_properPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/GysinAtInfinityClassProperPushforward.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/GysinAtInfinityClassProperPushforward.lean#L206). The attribute's comment: “g\_\{∞,*} ∘ C' = C for the canonical classes of Lemma 0F9J”.

> **Stacks 0FAQ.** Let `b : W ⟶ 𝐏¹_X` be proper and an isomorphism over `𝐀¹_X`, and let
> `g : W' ⟶ W` be proper and an isomorphism over `𝐀¹_X`. Let `C' ∈ A⁰(W'_∞ ⟶ X)` and
> `C ∈ A⁰(W_∞ ⟶ X)` be the classes of Stacks 0F9J for `b ∘ g` and for `b`
> (`Stacks.Chow.gysinAtInfinityClass`). Then `g_{∞,*} ∘ C' = C`, the left side being the proper
> pushforward of Stacks 0EPK along `g_∞ : W'_∞ ⟶ W_∞`.

```lean
theorem gysinAtInfinityClass_properPushforward :
    bivariantProperPushforwardOfInvertible C (modificationProjectionAtInfinity f (g ≫ b) ≫ f)
        (modificationProjectionAtInfinity f b ≫ f) f (modificationFibreAtInfinityMap f b g)
        (modificationProjectionAtInfinity f b) (modificationFibreAtInfinityMap_comp_over f b g)
        rfl 0
        ((gysinAtInfinityClass C f (g ≫ b)
            (isIso_pullbackSnd_comp_projectiveLineAffineChart f b g hA hg)).congrHom
          (modificationProjectionAtInfinity_comp_eq f b g)
          (comp_comp_structureMorphism_eq (modificationFibreAtInfinityMap_comp_over f b g) rfl)) =
      gysinAtInfinityClass C f b hA
```

**`Stacks.Chow.GysinAtInfinity.properPushforward_gysinAtInfinityClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinAtInfinity/ProperModification.lean, line 606](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinAtInfinity/ProperModification.lean#L606).

> **Stacks 0FAQ.** Let `X` be locally of finite type over the base of chapter 42, let
> `b : W ⟶ 𝐏¹_X` be proper and an isomorphism over `𝐀¹_X`, and let `g : W' ⟶ W` be proper and an
> isomorphism over `𝐀¹_X`, that is, over `b⁻¹(𝐀¹_X)`. Let `C' ∈ A⁰(W'_∞ ⟶ X)` and
> `C ∈ A⁰(W_∞ ⟶ X)` be the classes of Stacks 0F9J for `b ∘ g` and for `b`. Then
>
>   `g_{∞,*} ∘ C' = C`  in  `A⁰(W_∞ ⟶ X)`,
>
> where `g_∞ : W'_∞ ⟶ W_∞` is the restriction of `g` and the left side is the proper pushforward of
> Stacks 0EPK. The class `C'` is read for the morphism `g_∞ ≫ (W_∞ ⟶ X)`, which equals the structure
> morphism `W'_∞ ⟶ X`, through `Stacks.Chow.BivariantClass.copy`.

```lean
theorem properPushforward_gysinAtInfinityClass
    (hA : IsIso (pullback.snd b (projectiveLineAffineChart f)))
    (hg : IsIso (pullback.snd g (chartInclusion f b))) :
    haveI := hA
    haveI := hg
    canonicalBivariantProperPushforward C (modificationProjectionAtInfinity f (g ≫ b) ≫ f)
        (modificationProjectionAtInfinity f b ≫ f) f (infinityMap f b g)
        (modificationProjectionAtInfinity f b)
        (by rw [← Category.assoc, infinityMap_comp_projection]) rfl 0
        (BivariantClass.copy C (canonicalGysinSystem C)
          (modificationProjectionAtInfinity f (g ≫ b) ≫ f) f
          (infinityMap_comp_projection f b g).symm rfl
          (by rw [infinityMap_comp_projection]) rfl
          (gysinAtInfinityClass C f (g ≫ b) (isIso_pullbackSnd_comp f b g))) =
      gysinAtInfinityClass C f b hA
```

## Tag 0FAR, a lemma

[Tag 0FAR](https://stacks.math.columbia.edu/tag/0FAR) in the Stacks Project.

**`Stacks.Chow.GysinAtInfinity.gysinAtInfinity_retraction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinAtInfinity/RetractionClass.lean, line 738](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinAtInfinity/RetractionClass.lean#L738). The attribute's comment: “C ∘ (W\_∞ → X)\_* ∘ i\_∞^* = i\_∞^*: as bivariant classes over W, res(C) ∘ (i\_∞,* ∘ i\_∞^*) = Γ\_* ∘ i\_∞^* in A¹(W\_∞ ×\_X W → W), on every test scheme W' → W; and as the operation β ↦ C ∩ (W\_∞ → X)\_* i\_∞^* β on A\_\{k+1}(W ×\_X T) for T → X”.

> **Stacks 0FAR.** Let `X` be locally of finite type over the base of chapter 42, let
> `b : W ⟶ 𝐏¹_X` be proper and an isomorphism over `𝐀¹_X`, let `i_∞ : W_∞ ⟶ W` be the fibre at
> infinity, `p : W ⟶ X` the projection and `C ∈ A⁰(W_∞ ⟶ X)` the class of Stacks 0F9J. Then
> `C ∘ (W_∞ ⟶ X)_* ∘ i_∞^* = i_∞^*`, in the two readings of the module docstring:
>
> 1. as bivariant classes over `W`, valid on every test scheme `W' ⟶ W`:
>    `res(C) ∘ (i_{∞,*} ∘ i_∞^*) = Γ_* ∘ i_∞^*` in `A¹(W_∞ ×_X W ⟶ W)`, with `res` the restriction
>    of Stacks 0F9Z along `p`, `i_∞^*` the Gysin class of Stacks 0B79, the pushforwards those of
>    Stacks 0EPK along `i_∞` and along the graph `Γ : W_∞ ⟶ W_∞ ×_X W`, and `∘` that of
>    Stacks 0B75;
> 2. as the operation of the source on the test schemes `W ×_X T`, `T ⟶ X` locally of finite type:
>    for `β ∈ A_{k+1}(W ×_X T)`, `C ∩ (W_∞ ×_X T ⟶ T)_*(i_∞^* β) = i_∞^* β` in `A_k(W_∞ ×_X T)`,
>    with `C ∩ -` landing in degree `k - 0`, identified with `k`.

```lean
theorem gysinAtInfinity_retraction :
    bivariantCompositeOfInvertible C
        (pullback.fst (modificationProjectionAtInfinity f b) (modificationProjection f b) ≫
          (modificationProjectionAtInfinity f b ≫ f))
        (modificationProjection f b ≫ f) (modificationProjection f b ≫ f)
        (pullback.snd (modificationProjectionAtInfinity f b) (modificationProjection f b)) (𝟙 W)
        (pullbackSnd_comp_structureMorphism_eq C (modificationProjectionAtInfinity f b ≫ f) f
          (modificationProjectionAtInfinity f b) rfl (modificationProjection f b))
        (Category.id_comp _) 0 1
        (bivariantRestrictionOfInvertible C (modificationProjectionAtInfinity f b ≫ f) f
          (modificationProjectionAtInfinity f b) rfl (modificationProjection f b) 0
          (gysinAtInfinityClass C f b hA))
        (infinityGysinPushforwardClass C f b) =
      BivariantClass.copy C (gysinSystemOfInvertible C) _ _ (Category.comp_id _).symm _ _
        (zero_add 1).symm (infinityGraphPushforwardClass C f b) ∧
    ∀ {T : Scheme.{u}} (g : T ⟶ X) [LocallyOfFiniteType g] (k : ℤ)
      (β : chowGroup C (testStr C f (modificationProjection f b) g) (k + 1)),
      (gysinAtInfinityClass C f b hA).cap g k
          (properChowPushforward C (modificationInfinityBaseChangeOver f b g) (g ≫ f)
            (pullback.snd (modificationProjectionAtInfinity f b) g)
            (modificationInfinityBaseChange_snd_over f b g) k
            (properPushforwardDescends C _ _ _ _ _) (infinityGysin C f b g k β)) =
        chowGroupDegreeEquiv C _ (sub_zero k).symm (infinityGysin C f b g k β)
```

**`Stacks.Chow.gysinCapOfLift_chowPush_modificationInfinityGysin`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/GysinAtInfinityRestriction.lean, line 679](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/GysinAtInfinityRestriction.lean#L679). The attribute's comment: “C ∘ (W\_∞ ⟶ X)\_* ∘ i\_∞^* = i\_∞^*, on every test scheme T ⟶ X”.

> In the situation of Stacks 0F9J, `C ∘ (W_∞ ⟶ X)_* ∘ i_∞^* = i_∞^*`, on every test scheme
> `g : T ⟶ X`: for `β ∈ A_{k+1}(W ×_X T)`, the cap operation of the class `C` of Stacks 0F9J on the
> pushforward of `i_∞^* β` along `W_∞ ×_X T ⟶ T` is `i_∞^* β`. The identity of bivariant classes is
> the case `g = 𝟙 X`.

```lean
theorem gysinCapOfLift_chowPush_modificationInfinityGysin (k : ℤ)
    (β : chowGroup C (modificationBaseChangeOver f b g) (k + 1)) :
    gysinCapAtInfinity C f b hA g k
        (chowPush C (modificationInfinityBaseChangeOver f b g) (g ≫ f)
          (pullback.snd (modificationProjectionAtInfinity f b) g)
          (modificationInfinityBaseChange_snd_over f b g) k
          (modificationInfinityGysin C f b g k β)) =
      modificationInfinityGysin C f b g k β
```

## Tag 0FAS, a lemma

[Tag 0FAS](https://stacks.math.columbia.edu/tag/0FAS) in the Stacks Project.

**`Stacks.Chow.GysinAtInfinity.gysinAtInfinityClass_comp_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinAtInfinity/Commuting.lean, line 789](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinAtInfinity/Commuting.lean#L789).

> **Stacks 0FAS.** Let `(S, δ)` be as in Situation 02QL, let `X` be locally of finite type over
> `S`, let `b : W ⟶ 𝐏¹_X` be a proper morphism which is an isomorphism over `𝐀¹_X`, and let
> `C ∈ A⁰(W_∞ ⟶ X)` be the class of Stacks 0F9J. Let `fY : Y ⟶ X` be a morphism locally of finite
> type and `c ∈ A^p(Y ⟶ X)`. Then
>
>   `C ∘ c = c ∘ C`   in   `A^p(W_∞ ×_X Y ⟶ X)`.
>
> Here, as in Remark 0FA2, `C ∘ c = res(C) ∘ c` with `res(C) ∈ A⁰(W_∞ ×_X Y ⟶ Y)` the restriction
> of `C` along `fY` (Stacks 0F9Z), and `c ∘ C = res(c) ∘ C` with `res(c) ∈ A^p(Y ×_X W_∞ ⟶ W_∞)` the
> restriction of `c` along `W_∞ ⟶ X`; the second composite lives on `Y ×_X W_∞` and in degree
> `p + 0`, and is read on `W_∞ ×_X Y` through the canonical isomorphism and in degree `0 + p`. The
> bivariant classes are those of Stacks 0B76, `Stacks.Chow.BivariantChowClass`, and `C` is
> `Stacks.Chow.GysinAtInfinity.gysinAtInfinityClass` read through the bridge
> `Stacks.Chow.BivariantChowClass.equivBivariantClass`.

```lean
theorem gysinAtInfinityClass_comp_comm {sY : Y ⟶ C.S} [LocallyOfFiniteType sY]
    (hY : fY ≫ f = sY) (c : BivariantChowClass C sY f fY hY p) :
    ((BivariantChowClass.equivBivariantClass.symm (gysinAtInfinityClass C f b hA)).restrict fY
        hY).comp c =
      (((c.restrict (modificationProjectionAtInfinity f b) rfl).comp
          (BivariantChowClass.equivBivariantClass.symm (gysinAtInfinityClass C f b hA))).degreeCongr
        (add_comm p 0)).transport
        (comp_comp_structureMorphism_eq (BivariantChowClass.restrict_structure_eq rfl fY hY) hY)
        (pullbackSymmetry fY (modificationProjectionAtInfinity f b))
        (pullbackSymmetry_hom_comp_snd_comp (modificationProjectionAtInfinity f b) fY)
```

**`Stacks.Chow.gysinAtInfinity_bivariantCommute`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinAtInfinityCommuting.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinAtInfinityCommuting.lean#L206). The attribute's comment: “given the construction of Stacks 0F9J as a presentation of the cap operation of C by a lift and a Gysin step, and the naturality of each of those two factors under c (the first being the source's step that `c ∩ β` lifts `c ∩ α`, resting on Stacks 02RC and 02RX; the second being condition (3) of Stacks 0B76 for c at the divisor at infinity, which needs Stacks 0B6Y to instantiate)”.

> **Stacks 0FAS**, conditional on the construction of Stacks 0F9J and its two naturality
> properties under `c`.
>
> In the setting of Stacks 0F9J, let `fY : Y ⟶ X` be locally of finite type and let
> `c ∈ A^p(Y ⟶ X)`. Then the canonical class `C ∈ A⁰(W_∞ ⟶ X)` and `c` commute, in the sense of
> Remark 0FA2: `C ∩ (c ∩ α) = c ∩ (C ∩ α)` for every `α ∈ CH_k(T)` and every test scheme
> `t : T ⟶ X` locally of finite type, the two sides being compared by the canonical isomorphism
> `W_∞ ×_X (Y ×_X T) ≅ Y ×_X (W_∞ ×_X T)`.
>
> The hypotheses are the source's own proof steps, and none of them is the conclusion:
>
> * `P`, a `Stacks.Chow.GysinAtInfinityCapPresentation`, is the construction of Stacks 0F9J:
>   `C ∩ - = i_∞^* ∘ lift`. It is needed because the pushforward identity recorded by
>   `Stacks.Chow.GysinAtInfinityData` does not determine `C`.
> * `hlift` is "`c ∩ β` is a lift of `c ∩ α`", a statement about the lift alone.
> * `hgysinStep` is condition (3) of Stacks 0B76 for `c` at the divisor at infinity, a statement
>   about the Gysin step alone; it is `Stacks.Chow.BivariantClass.gysin_naturality` modulo the
>   zero-scheme base-change identification of Stacks 0B6Y, which this repository lacks.
>
> See the implementation notes of `StacksFrontier.AlgebraicGeometry.Chow.GysinAtInfinityCommuting`.

```lean
theorem gysinAtInfinity_bivariantCommute
    (hlift : ∀ {T : Scheme.{u}} (t : T ⟶ X) [LocallyOfFiniteType t] (k : ℤ)
        (α : chowGroup C (t ≫ f) k),
      P.lift (pullback.fst fY t ≫ fY) (k - p)
          (chowGroupCongr C (Category.assoc (pullback.fst fY t) fY f).symm (k - p)
            (c.cap t k α)) =
        chowGroupDegreeEquiv C (modificationBaseChangeOver f b (pullback.fst fY t ≫ fY))
          (by ring : k + 1 - p = k - p + 1)
          (commuteCapTransport C G f fY (modificationProjection f b) p c t (k + 1)
            (P.lift t k α)))
    (hgysinStep : ∀ {T : Scheme.{u}} (t : T ⟶ X) [LocallyOfFiniteType t] (k : ℤ)
        (β : chowGroup C (modificationBaseChangeOver f b t) (k + 1)),
      P.gysinStep (pullback.fst fY t ≫ fY) (k - p)
          (chowGroupDegreeEquiv C (modificationBaseChangeOver f b (pullback.fst fY t ≫ fY))
            (by ring : k + 1 - p = k - p + 1)
            (commuteCapTransport C G f fY (modificationProjection f b) p c t (k + 1) β)) =
        commuteCapTransport C G f fY (modificationProjectionAtInfinity f b) p c t k
          (P.gysinStep t k β)) :
    BivariantCommute C G f (modificationProjectionAtInfinity f b) fY 0 p D.bivariantClass c
```

**`Stacks.Chow.gysinAtInfinity_commuteCompositeCap_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinAtInfinityCommuting.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinAtInfinityCommuting.lean#L255). The attribute's comment: “the displayed equality C ∘ c = c ∘ C of the tag, on cap operations, under the same hypotheses as `gysinAtInfinity_bivariantCommute`”.

> **Stacks 0FAS** in the displayed form of the tag: `C ∘ c = c ∘ C` in
> `A^p(W_∞ ×_X Y ⟶ X)`, read on cap operations.
>
> This is `Stacks.Chow.gysinAtInfinity_bivariantCommute` pushed through the equivalence of Remark
> 0FA2, `Stacks.Chow.bivariantCommute_iff_commuteCompositeCap_eq`: the cap operations of the two
> composites `res(C) ∘ c` and `res(c) ∘ C` agree under the canonical identification
> `W_∞ ×_X Y ≅ Y ×_X W_∞` of their sources and the equality `0 + p = p + 0` of their degrees. The
> hypothesis `hgys` is the isomorphism case of Stacks 02TA for the Gysin system, which
> `Stacks.Chow.bivariantRestriction` (Stacks 0F9Z) needs in order to be a bivariant class; the
> Stacks 02S2 hypothesis of `Stacks.Chow.bivariantCompositeCap` is discharged by
> `Stacks.Chow.properPushforwardDescends`.

```lean
theorem gysinAtInfinity_commuteCompositeCap_eq (hgys : G.IsNaturalUnderBaseChangeIso)
    (hlift : ∀ {T : Scheme.{u}} (t : T ⟶ X) [LocallyOfFiniteType t] (k : ℤ)
        (α : chowGroup C (t ≫ f) k),
      P.lift (pullback.fst fY t ≫ fY) (k - p)
          (chowGroupCongr C (Category.assoc (pullback.fst fY t) fY f).symm (k - p)
            (c.cap t k α)) =
        chowGroupDegreeEquiv C (modificationBaseChangeOver f b (pullback.fst fY t ≫ fY))
          (by ring : k + 1 - p = k - p + 1)
          (commuteCapTransport C G f fY (modificationProjection f b) p c t (k + 1)
            (P.lift t k α)))
    (hgysinStep : ∀ {T : Scheme.{u}} (t : T ⟶ X) [LocallyOfFiniteType t] (k : ℤ)
        (β : chowGroup C (modificationBaseChangeOver f b t) (k + 1)),
      P.gysinStep (pullback.fst fY t ≫ fY) (k - p)
          (chowGroupDegreeEquiv C (modificationBaseChangeOver f b (pullback.fst fY t ≫ fY))
            (by ring : k + 1 - p = k - p + 1)
            (commuteCapTransport C G f fY (modificationProjection f b) p c t (k + 1) β)) =
        commuteCapTransport C G f fY (modificationProjectionAtInfinity f b) p c t k
          (P.gysinStep t k β))
    {T : Scheme.{u}} (t : T ⟶ X) [LocallyOfFiniteType t] (k : ℤ)
    (α : chowGroup C (t ≫ f) k) :
    chowPushforwardOfIso C
        (pullback.fst (pullback.snd (modificationProjectionAtInfinity f b) fY ≫ fY) t ≫
          (pullback.fst (modificationProjectionAtInfinity f b) fY ≫
            (modificationProjectionAtInfinity f b ≫ f)))
        (pullback.fst (pullback.snd fY (modificationProjectionAtInfinity f b) ≫
            modificationProjectionAtInfinity f b) t ≫
          (pullback.fst fY (modificationProjectionAtInfinity f b) ≫ (fY ≫ f)))
        (compositeComparisonHom (modificationProjectionAtInfinity f b) fY t)
        (compositeComparisonHom_comp_structureMorphism C f
          (modificationProjectionAtInfinity f b) fY t) (k - p - 0)
        (commuteCompositeCap C G f (modificationProjectionAtInfinity f b) fY 0 p
          D.bivariantClass c hgys (properPushforwardDescends C) t k α) =
      chowGroupDegreeEquiv C
        (pullback.fst (pullback.snd fY (modificationProjectionAtInfinity f b) ≫
            modificationProjectionAtInfinity f b) t ≫
          (pullback.fst fY (modificationProjectionAtInfinity f b) ≫ (fY ≫ f)))
        (by ring : k - 0 - p = k - p - 0)
        (commuteCompositeCap C G f fY (modificationProjectionAtInfinity f b) p 0 c
          D.bivariantClass hgys (properPushforwardDescends C) t k α)
```

**`Stacks.Chow.nonhomogeneousBivariantTransport_compositeOfInvertible_gysinAtInfinityClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/Commutation.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/Commutation.lean#L155). The attribute's comment: “C ∘ c = c ∘ C in A^*(W\_∞ ×\_X Y → X), for every c in A^*(Y → X)”.

> Let `b : W ⟶ 𝐏¹_X` be proper and an isomorphism over `𝐀¹_X`, let `C ∈ A⁰(W_∞ ⟶ X)` be the class
> of Stacks 0F9J, let `fY : Y ⟶ X` be locally of finite type and let `c ∈ A^*(Y ⟶ X)`. Then
>
>   `C ∘ c = c ∘ C`   in   `A^*(W_∞ ×_X Y ⟶ X)`,
>
> where `C ∘ c = res(C) ∘ c` and `c ∘ C = res(c) ∘ C`, the latter a class for `Y ×_X W_∞ ⟶ X`
> carried to `W_∞ ×_X Y` along the symmetry of the fibre product.

```lean
theorem nonhomogeneousBivariantTransport_compositeOfInvertible_gysinAtInfinityClass
    (c : nonhomogeneousBivariantGroup C (gysinSystemOfInvertible C) (fY ≫ f) f fY rfl) :
    nonhomogeneousBivariantTransport C (gysinSystemOfInvertible C)
        (pullback.fst fY (modificationProjectionAtInfinity f b) ≫ (fY ≫ f))
        (pullback.fst (modificationProjectionAtInfinity f b) fY ≫
          (modificationProjectionAtInfinity f b ≫ f)) f
        (pullback.snd fY (modificationProjectionAtInfinity f b) ≫
          modificationProjectionAtInfinity f b)
        (comp_comp_structureMorphism_eq
          (pullbackSnd_comp_structureMorphism_eq C (fY ≫ f) f fY rfl _) rfl)
        (pullback.snd (modificationProjectionAtInfinity f b) fY ≫ fY)
        (comp_comp_structureMorphism_eq
          (pullbackSnd_comp_structureMorphism_eq C _ f (modificationProjectionAtInfinity f b) rfl
            fY) rfl)
        (pullbackSymmetry fY (modificationProjectionAtInfinity f b))
        (by simp [pullback.condition])
        (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso C)
        (nonhomogeneousBivariantCompositeOfInvertible C
          (pullback.fst fY (modificationProjectionAtInfinity f b) ≫ (fY ≫ f))
          (modificationProjectionAtInfinity f b ≫ f) f
          (pullback.snd fY (modificationProjectionAtInfinity f b))
          (modificationProjectionAtInfinity f b)
          (pullbackSnd_comp_structureMorphism_eq C (fY ≫ f) f fY rfl _) rfl
          (nonhomogeneousBivariantRestriction C (gysinSystemOfInvertible C) (fY ≫ f) f fY rfl
            (modificationProjectionAtInfinity f b)
            (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso C) c)
          (DirectSum.of _ 0 (gysinAtInfinityClass C f b hA))) =
      nonhomogeneousBivariantCompositeOfInvertible C
        (pullback.fst (modificationProjectionAtInfinity f b) fY ≫
          (modificationProjectionAtInfinity f b ≫ f)) (fY ≫ f) f
        (pullback.snd (modificationProjectionAtInfinity f b) fY) fY
        (pullbackSnd_comp_structureMorphism_eq C _ f (modificationProjectionAtInfinity f b) rfl
          fY) rfl
        (DirectSum.of _ 0 (bivariantRestriction C (gysinSystemOfInvertible C)
          (modificationProjectionAtInfinity f b ≫ f) f (modificationProjectionAtInfinity f b) rfl
          fY 0 (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso C)
          (gysinAtInfinityClass C f b hA))) c
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.48, Tag 0FAP](https://stacks.math.columbia.edu/tag/0FAP)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
