---
declaration: section
origin: cited
lean: Stacks.Chow.LocalizedSituation, Stacks.Chow.LocalizedChernSituation, Stacks.Chow.LocalizedSituation.localizedPowerSum, Stacks.Chow.LocalizedSituation.localizedChern, Stacks.Chow.LocalizedSituation.properPushforwardChowCohomology_localizedPowerSum, Stacks.Chow.LocalizedSituation.properPushforwardChowCohomology_localizedChern, Stacks.Chow.LocalizedSituation.localizedChernChar, Stacks.Chow.LocalizedSituation.bivariantRestriction_localizedPowerSum
statement: formalized
proof: formalized
---

# 42.50 Localized Chern classes

Section 42.50 of the Stacks Project, [Tag 0FB0](https://stacks.math.columbia.edu/tag/0FB0). 9 tags here are carried by 24 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GUJ, a situation

[Tag 0GUJ](https://stacks.math.columbia.edu/tag/0GUJ) in the Stacks Project.

**`Stacks.Chow.LocalizedSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedChernData.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedChernData.lean#L95).

> The standing situation for the localized Chern classes and localized Chern character components
> of chapter 42 of the Stacks Project: a scheme locally of finite type over the base, a closed
> subscheme, a perfect object of the derived category of the ambient scheme which away from the
> closed subscheme is zero or a finite locally free module of rank below the chosen degree (the data
> `Stacks.Chow.LocalizedChernData`), and one of the four finiteness alternatives of the source.

```lean
structure LocalizedSituation extends LocalizedChernData.{u}
```

**`Stacks.Chow.LocalizedChernSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedChernSetup.lean, line 154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedChernSetup.lean#L154).

> The standing situation for the localized Chern classes and localized Chern character
> components of chapter 42 of the Stacks Project: a scheme locally of finite type over the base, a
> closed subscheme, a perfect object of the derived category of the ambient scheme which away from
> the closed subscheme is zero or a finite locally free module of rank below the chosen degree, and
> one of four finiteness alternatives.

```lean
structure LocalizedChernSituation
```

## Tag 0FB2, a lemma

[Tag 0FB2](https://stacks.math.columbia.edu/tag/0FB2) in the Stacks Project.

**`Stacks.Chow.LocalizedSituation.localizedPowerSum`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/Localized.lean, line 289](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/Localized.lean#L289). The attribute's comment: “P\_p(Z → X, E) ∈ A^p(Z → X), when E|\_\{X ∖ Z} is zero”.

> **The localized class `P_p(Z ⟶ X, E) ∈ A^p(Z ⟶ X)` of Stacks 0FB2 and Definition 0FB5 (1)**,
> when `E|_{X ∖ Z}` is zero, for every `p ≥ 0`: the class `P'_p(Q)` of Stacks 0F9K for the graph
> construction `b : W ⟶ 𝐏¹_X`, `Q` of `E` and the open and closed `T' ⊆ T ⊆ W_∞` on which `Q` is
> zero, where `T ⊆ W_∞` is the closed subscheme of Stacks 0F90 (3), (4). The Chern classes of `Q`
> are defined in Situation 0GUJ (`Stacks.Chow.LocalizedSituation.hasDefinedChernClasses_graphObject`,
> from condition (3)).

```lean
abbrev localizedPowerSum (h : S.IsZeroOnComplement) (p : ℕ) :
    BivariantClass S.base (gysinSystemOfInvertible S.base) (S.i ≫ S.a) S.a S.i rfl p
```

**`Stacks.Chow.LocalizedSituation.localizedChern`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/Localized.lean, line 306](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/Localized.lean#L306). The attribute's comment: “c\_p(Z → X, E) ∈ A^p(Z → X), when E|\_\{X ∖ Z} is finite locally free of rank < p in degree 0”.

> **The localized Chern class `c_p(Z ⟶ X, E) ∈ A^p(Z ⟶ X)` of Stacks 0FB2 and
> Definition 0FB5 (2)**, when `E|_{X ∖ Z}` is finite locally free of rank `< p` in degree `0`: the
> class `c'_p(Q)` of Stacks 0F9K for the graph construction `b : W ⟶ 𝐏¹_X`, `Q` of `E` and the open
> and closed `T' ⊆ T ⊆ W_∞` on which `Q` is finite locally free of rank `< p` in degree `0`, where
> `T ⊆ W_∞` is the closed subscheme of Stacks 0F90 (3), (4). The Chern classes of `Q` are defined in
> Situation 0GUJ (`Stacks.Chow.LocalizedSituation.hasDefinedChernClasses_graphObject`, from
> condition (3)).

```lean
abbrev localizedChern (h : S.IsFiniteLocallyFreeOfRankLTOnComplement) :
    BivariantClass S.base (gysinSystemOfInvertible S.base) (S.i ≫ S.a) S.a S.i rfl S.p
```

**`Stacks.Chow.LocalizedSituation.properPushforwardChowCohomology_localizedPowerSum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/Localized.lean, line 330](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/Localized.lean#L330). The attribute's comment: “i\_* ∘ P\_p(Z → X, E) = P\_p(E), when E|\_\{X ∖ Z} is zero”.

> **`i_* ∘ P_p(Z ⟶ X, E) = P_p(E)`** (Stacks 0FB2, equation 0FB1) as bivariant classes on `X`,
> with `∘` the pushforward of Stacks 0EPK, when `E|_{X ∖ Z}` is zero.

```lean
theorem properPushforwardChowCohomology_localizedPowerSum (h : S.IsZeroOnComplement) (p : ℕ) :
    properPushforwardChowCohomology S.base S.a (S.i ≫ S.a) S.i rfl (S.localizedPowerSum h p) =
      perfectPowerSumComponent S.base S.a S.hasDefinedChernClasses_E p
```

**`Stacks.Chow.LocalizedSituation.properPushforwardChowCohomology_localizedChern`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/Localized.lean, line 343](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/Localized.lean#L343). The attribute's comment: “i\_* ∘ c\_p(Z → X, E) = c\_p(E), when E|\_\{X ∖ Z} is finite locally free of rank < p in degree 0”.

> **`i_* ∘ c_p(Z ⟶ X, E) = c_p(E)`** (Stacks 0FB2, equation 0FB1) as bivariant classes on `X`,
> with `∘` the pushforward of Stacks 0EPK, when `E|_{X ∖ Z}` is finite locally free of rank `< p`
> in degree `0`.

```lean
theorem properPushforwardChowCohomology_localizedChern
    (h : S.IsFiniteLocallyFreeOfRankLTOnComplement) :
    properPushforwardChowCohomology S.base S.a (S.i ≫ S.a) S.i rfl (S.localizedChern h) =
      perfectChernClass S.base S.a S.hasDefinedChernClasses_E S.p
```

## Tag 0FB5, a definition

[Tag 0FB5](https://stacks.math.columbia.edu/tag/0FB5) in the Stacks Project.

**`Stacks.Chow.LocalizedSituation.localizedPowerSum`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/Localized.lean, line 289](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/Localized.lean#L289). The attribute's comment: “(1): P\_p(Z → X, E) for every p ≥ 0, when E|\_\{X ∖ Z} is zero”.

> **The localized class `P_p(Z ⟶ X, E) ∈ A^p(Z ⟶ X)` of Stacks 0FB2 and Definition 0FB5 (1)**,
> when `E|_{X ∖ Z}` is zero, for every `p ≥ 0`: the class `P'_p(Q)` of Stacks 0F9K for the graph
> construction `b : W ⟶ 𝐏¹_X`, `Q` of `E` and the open and closed `T' ⊆ T ⊆ W_∞` on which `Q` is
> zero, where `T ⊆ W_∞` is the closed subscheme of Stacks 0F90 (3), (4). The Chern classes of `Q`
> are defined in Situation 0GUJ (`Stacks.Chow.LocalizedSituation.hasDefinedChernClasses_graphObject`,
> from condition (3)).

```lean
abbrev localizedPowerSum (h : S.IsZeroOnComplement) (p : ℕ) :
    BivariantClass S.base (gysinSystemOfInvertible S.base) (S.i ≫ S.a) S.a S.i rfl p
```

**`Stacks.Chow.LocalizedSituation.localizedChern`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/Localized.lean, line 306](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/Localized.lean#L306). The attribute's comment: “(2): the localized pth Chern class c\_p(Z → X, E), when E|\_\{X ∖ Z} is finite locally free of rank < p in degree 0”.

> **The localized Chern class `c_p(Z ⟶ X, E) ∈ A^p(Z ⟶ X)` of Stacks 0FB2 and
> Definition 0FB5 (2)**, when `E|_{X ∖ Z}` is finite locally free of rank `< p` in degree `0`: the
> class `c'_p(Q)` of Stacks 0F9K for the graph construction `b : W ⟶ 𝐏¹_X`, `Q` of `E` and the open
> and closed `T' ⊆ T ⊆ W_∞` on which `Q` is finite locally free of rank `< p` in degree `0`, where
> `T ⊆ W_∞` is the closed subscheme of Stacks 0F90 (3), (4). The Chern classes of `Q` are defined in
> Situation 0GUJ (`Stacks.Chow.LocalizedSituation.hasDefinedChernClasses_graphObject`, from
> condition (3)).

```lean
abbrev localizedChern (h : S.IsFiniteLocallyFreeOfRankLTOnComplement) :
    BivariantClass S.base (gysinSystemOfInvertible S.base) (S.i ≫ S.a) S.a S.i rfl S.p
```

**`Stacks.Chow.LocalizedSituation.localizedChernChar`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/Localized.lean, line 317](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/Localized.lean#L317). The attribute's comment: “(1): the localized Chern character ch(Z → X, E) = Σ\_p P\_p(Z → X, E)/p! in Π\_\{p ≥ 0} A^p(Z → X) ⊗ Q, when E|\_\{X ∖ Z} is zero”.

> **The localized Chern character `ch(Z ⟶ X, E) = ∑_p P_p(Z ⟶ X, E)/p!` of
> Definition 0FB5 (1)**, when `E|_{X ∖ Z}` is zero, as an element of
> `∏_{p ≥ 0} A^p(Z ⟶ X) ⊗ 𝐐`, built from `Stacks.Chow.LocalizedSituation.localizedPowerSum`.

```lean
abbrev localizedChernChar (h : S.IsZeroOnComplement) (p : ℕ) :
    TensorProduct ℤ ℚ
      (BivariantClass S.base (gysinSystemOfInvertible S.base) (S.i ≫ S.a) S.a S.i rfl (p : ℤ))
```

## Tag 0FB3, a lemma

[Tag 0FB3](https://stacks.math.columbia.edu/tag/0FB3) in the Stacks Project.

**`Stacks.Chow.LocalizedSituation.bivariantRestriction_localizedPowerSum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedRestriction.lean, line 549](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedRestriction.lean#L549). The attribute's comment: “for P\_p: the class P\_p(Z' → X', E') of Lemma 0FB2 for X', Z' = f^\{-1}(Z) and E' = f^*E is the restriction (Remark 0F9Z) of P\_p(Z → X, E)”.

> In Situation 0GUJ with `E|_{X ∖ Z}` zero, let `f : X' ⟶ X` be
> locally of finite type, `E' = Lf^*E` and `Z' = f^{-1}(Z) = Z ×_X X'`. Then the class
> `P_p(Z' ⟶ X', E') ∈ A^p(Z' ⟶ X')` of Stacks 0FB2, constructed from `X'`, `Z'`, `E'` (the
> situation `Stacks.Chow.LocalizedSituation.pullback`), is the restriction (Remark 0F9Z) of
> `P_p(Z ⟶ X, E) ∈ A^p(Z ⟶ X)`.

```lean
theorem bivariantRestriction_localizedPowerSum (h : S.IsZeroOnComplement) (p : ℕ) :
    bivariantClassCongrBase S.base (gysinSystemOfInvertible S.base) (Limits.pullback.snd S.i f)
        (pullbackSnd_comp_structureMorphism_eq S.base (S.i ≫ S.a) S.a S.i rfl f).symm rfl
        (hv := pullbackSnd_comp_structureMorphism_eq S.base (S.i ≫ S.a) S.a S.i rfl f)
        (hv' := rfl) p
        (bivariantRestriction S.base (gysinSystemOfInvertible S.base) (S.i ≫ S.a) S.a S.i rfl f p
          (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso S.base)
          (S.localizedPowerSum h p)) =
      (S.pullback f).localizedPowerSum h.pullback p
```

**`Stacks.Chow.LocalizedSituation.bivariantRestriction_localizedChern`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedRestriction.lean, line 577](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedRestriction.lean#L577). The attribute's comment: “for c\_p: the class c\_p(Z' → X', E') of Lemma 0FB2 for X', Z' = f^\{-1}(Z) and E' = f^*E is the restriction (Remark 0F9Z) of c\_p(Z → X, E)”.

> In Situation 0GUJ with `E|_{X ∖ Z}` finite locally free of rank
> `< p` in degree `0`, let `f : X' ⟶ X` be locally of finite type, `E' = Lf^*E` and
> `Z' = f^{-1}(Z) = Z ×_X X'`. Then the class `c_p(Z' ⟶ X', E') ∈ A^p(Z' ⟶ X')` of Stacks 0FB2,
> constructed from `X'`, `Z'`, `E'` (the situation `Stacks.Chow.LocalizedSituation.pullback`),
> is the restriction (Remark 0F9Z) of `c_p(Z ⟶ X, E) ∈ A^p(Z ⟶ X)`.

```lean
theorem bivariantRestriction_localizedChern (h : S.IsFiniteLocallyFreeOfRankLTOnComplement) :
    bivariantClassCongrBase S.base (gysinSystemOfInvertible S.base) (Limits.pullback.snd S.i f)
        (pullbackSnd_comp_structureMorphism_eq S.base (S.i ≫ S.a) S.a S.i rfl f).symm rfl
        (hv := pullbackSnd_comp_structureMorphism_eq S.base (S.i ≫ S.a) S.a S.i rfl f)
        (hv' := rfl) S.p
        (bivariantRestriction S.base (gysinSystemOfInvertible S.base) (S.i ≫ S.a) S.a S.i rfl f
          S.p (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso S.base)
          (S.localizedChern h)) =
      (S.pullback f).localizedChern h.pullback
```

## Tag 0GUK, a remark

[Tag 0GUK](https://stacks.math.columbia.edu/tag/0GUK) in the Stacks Project.

**`Stacks.Chow.LocalizedChernData.localizedPowerSum`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/DefinedChernClasses.lean, line 589](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/DefinedChernClasses.lean#L589). The attribute's comment: “P\_p(Z → X, E) in A^p(Z → X) for E perfect with E|\_\{X ∖ Z} zero whose Chern classes are defined, by descent (0GUC) of the classes of 0FB2 along an envelope; in Situation 0GUJ it is the class of 0FB2 (localizedPowerSum\_toLocalizedChernData)”.

> **The localized class `P_p(Z ⟶ X, E) ∈ A^p(Z ⟶ X)` when the Chern classes of `E` are
> defined** (Remark 0GUK), when `E|_{X ∖ Z}` is zero, for every degree `p`: the unique class whose
> restriction along the envelope `g : Y ⟶ X` of a presentation of `E` by a locally bounded complex of
> finite locally free modules is the class `P_p(Z ×_X Y ⟶ Y, Lg^*E)` of Stacks 0FB2 (Stacks 0GUC).
> In Situation 0GUJ it is the class of Stacks 0FB2
> (`Stacks.Chow.LocalizedSituation.localizedPowerSum_toLocalizedChernData`).

```lean
def localizedPowerSum (hE : HasDefinedChernClasses D.E) (h : D.IsZeroOnComplement) (p : ℕ) :
    BivariantClass D.base (gysinSystemOfInvertible D.base) (D.i ≫ D.a) D.a D.i rfl p
```

**`Stacks.Chow.LocalizedChernData.localizedChern`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/DefinedChernClasses.lean, line 623](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/DefinedChernClasses.lean#L623). The attribute's comment: “c\_p(Z → X, E) in A^p(Z → X) for E perfect with E|\_\{X ∖ Z} finite locally free of rank < p in degree 0 whose Chern classes are defined, by descent (0GUC) of the classes of 0FB2 along an envelope; in Situation 0GUJ it is the class of 0FB2 (localizedChern\_toLocalizedChernData)”.

> **The localized Chern class `c_p(Z ⟶ X, E) ∈ A^p(Z ⟶ X)` when the Chern classes of `E` are
> defined** (Remark 0GUK), when `E|_{X ∖ Z}` is finite locally free of rank `< p` in degree `0`: the
> unique class whose restriction along the envelope `g : Y ⟶ X` of a presentation of `E` is the class
> `c_p(Z ×_X Y ⟶ Y, Lg^*E)` of Stacks 0FB2 (Stacks 0GUC). In Situation 0GUJ it is the class of
> Stacks 0FB2 (`Stacks.Chow.LocalizedSituation.localizedChern_toLocalizedChernData`).

```lean
def localizedChern (hE : HasDefinedChernClasses D.E)
    (h : D.IsFiniteLocallyFreeOfRankLTOnComplement) :
    BivariantClass D.base (gysinSystemOfInvertible D.base) (D.i ≫ D.a) D.a D.i rfl D.p
```

**`Stacks.Chow.LocalizedChernData.localizedChernChar`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/DefinedChernClasses.lean, line 633](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/DefinedChernClasses.lean#L633). The attribute's comment: “the localized Chern character ch(Z → X, E) = Σ\_p P\_p(Z → X, E)/p! of 0FB5 (1) for E perfect with E|\_\{X ∖ Z} zero whose Chern classes are defined”.

> **The localized Chern character `ch(Z ⟶ X, E) = ∑_p P_p(Z ⟶ X, E)/p!` when the Chern classes
> of `E` are defined** (Definition 0FB5 (1) and Remark 0GUK), when `E|_{X ∖ Z}` is zero, as an
> element of `∏_{p ≥ 0} A^p(Z ⟶ X) ⊗ 𝐐`.

```lean
def localizedChernChar (hE : HasDefinedChernClasses D.E) (h : D.IsZeroOnComplement) (p : ℕ) :
    TensorProduct ℤ ℚ
      (BivariantClass D.base (gysinSystemOfInvertible D.base) (D.i ≫ D.a) D.a D.i rfl (p : ℤ))
```

**`Stacks.Chow.LocalizedSituation.localizedPowerSum_toLocalizedChernData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/DefinedChernClasses.lean, line 912](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/DefinedChernClasses.lean#L912). The attribute's comment: “the extension agrees with the definition: in Situation 0GUJ the class P\_p(Z → X, E) of the remark is the class of 0FB2”.

> **In Situation 0GUJ the class of Remark 0GUK is the class `P_p(Z ⟶ X, E)` of Stacks 0FB2**:
> both restrict to `P_p(Z ×_X Y ⟶ Y, Lg^*E)` along an envelope (Stacks 0FB3), and the uniqueness
> in Stacks 0GUC applies.

```lean
theorem localizedPowerSum_toLocalizedChernData (h : S.IsZeroOnComplement) (p : ℕ) :
    S.toLocalizedChernData.localizedPowerSum S.hasDefinedChernClasses_E h p =
      S.localizedPowerSum h p
```

**`Stacks.Chow.LocalizedSituation.localizedChern_toLocalizedChernData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/DefinedChernClasses.lean, line 939](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/DefinedChernClasses.lean#L939). The attribute's comment: “the extension agrees with the definition: in Situation 0GUJ the class c\_p(Z → X, E) of the remark is the class of 0FB2”.

> **In Situation 0GUJ the class of Remark 0GUK is the class `c_p(Z ⟶ X, E)` of Stacks 0FB2**,
> as `Stacks.Chow.LocalizedSituation.localizedPowerSum_toLocalizedChernData`.

```lean
theorem localizedChern_toLocalizedChernData (h : S.IsFiniteLocallyFreeOfRankLTOnComplement) :
    S.toLocalizedChernData.localizedChern S.hasDefinedChernClasses_E h =
      S.localizedChern h
```

## Tag 0FB4, a lemma

[Tag 0FB4](https://stacks.math.columbia.edu/tag/0FB4) in the Stacks Project.

**`Stacks.Chow.LocalizedSituation.localizedPowerSum_cap_chowPush`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedCap.lean, line 213](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedCap.lean#L213). The attribute's comment: “P\_p(Z ⟶ X, E) ∩ i\_* α = P\_p(E|\_Z) ∩ α, after every base change”.

> **Stacks 0FB4, for `P_p(Z ⟶ X, E)`.** In Situation 0GUJ, when `E|_{X ∖ Z}` is zero,
> `P_p(Z ⟶ X, E) ∩ i_* α = P_p(E|_Z) ∩ α` for `α ∈ CH_*(Z)`, and similarly after every base change:
> on every test scheme `g : T ⟶ X`, the cap product of `P_p(Z ⟶ X, E)` with a class pushed forward
> from `T ×_X Z` is the operation of `P_p(Li^*E) ∈ A^p(Z)` on it. This is the first formula of the
> characterization of Stacks 0F9H. The Chern classes of `Li^*E` are defined by Stacks 0GUE (5), from
> those of `E` (`Stacks.Chow.LocalizedSituation.hasDefinedChernClasses_E`).

```lean
theorem localizedPowerSum_cap_chowPush (h : S.IsZeroOnComplement) (p : ℕ)
    {T : Scheme.{u}} (g : T ⟶ S.X) [LocallyOfFiniteType g] (k : ℤ)
    (α : chowGroup S.base (pullback.fst S.i g ≫ (S.i ≫ S.a)) k) :
    (S.localizedPowerSum h p).cap g k
        (chowPush S.base _ _ (pullback.snd S.i g) (pullbackSnd_comp_structureMorphism rfl g) k
          α) =
      (perfectPowerSumComponent S.base (S.i ≫ S.a)
          (hasDefinedChernClasses_of_derivedPullback S.i _ S.E S.hasDefinedChernClasses_E
            (Iso.refl _)) p).idRule S.base (S.i ≫ S.a)
        (gysinSystemOfInvertible S.base) (pullback.fst S.i g) k α
```

**`Stacks.Chow.LocalizedSituation.localizedChern_cap_chowPush`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedCap.lean, line 239](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedCap.lean#L239). The attribute's comment: “c\_p(Z ⟶ X, E) ∩ i\_* α = c\_p(E|\_Z) ∩ α, after every base change”.

> **Stacks 0FB4, for `c_p(Z ⟶ X, E)`.** In Situation 0GUJ, when `E|_{X ∖ Z}` is finite locally
> free of rank `< p` in degree `0`, `c_p(Z ⟶ X, E) ∩ i_* α = c_p(E|_Z) ∩ α` for `α ∈ CH_*(Z)`, and
> similarly after every base change: on every test scheme `g : T ⟶ X`, the cap product of
> `c_p(Z ⟶ X, E)` with a class pushed forward from `T ×_X Z` is the operation of
> `c_p(Li^*E) ∈ A^p(Z)` on it. This is the first formula of the characterization of Stacks 0F9H.
> The Chern classes of `Li^*E` are defined by Stacks 0GUE (5), from those of `E`
> (`Stacks.Chow.LocalizedSituation.hasDefinedChernClasses_E`).

```lean
theorem localizedChern_cap_chowPush (h : S.IsFiniteLocallyFreeOfRankLTOnComplement)
    {T : Scheme.{u}} (g : T ⟶ S.X) [LocallyOfFiniteType g] (k : ℤ)
    (α : chowGroup S.base (pullback.fst S.i g ≫ (S.i ≫ S.a)) k) :
    (S.localizedChern h).cap g k
        (chowPush S.base _ _ (pullback.snd S.i g) (pullbackSnd_comp_structureMorphism rfl g) k
          α) =
      (perfectChernClass S.base (S.i ≫ S.a)
          (hasDefinedChernClasses_of_derivedPullback S.i _ S.E S.hasDefinedChernClasses_E
            (Iso.refl _)) S.p).idRule S.base (S.i ≫ S.a)
        (gysinSystemOfInvertible S.base) (pullback.fst S.i g) k α
```

## Tag 0FB6, a lemma

[Tag 0FB6](https://stacks.math.columbia.edu/tag/0FB6) in the Stacks Project.

**`Stacks.Chow.LocalizedSituation.localizedPowerSum_capVanishesOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedCap.lean, line 264](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedCap.lean#L264). The attribute's comment: “P\_p(Z ⟶ X, E) ∩ α = 0 for α supported away from Z, after every base change”.

> **Stacks 0FB6, for `P_p(Z ⟶ X, E)`.** In Situation 0GUJ, when `E|_{X ∖ Z}` is zero: if
> `α ∈ CH_k(X)` has support disjoint from `Z`, then `P_p(Z ⟶ X, E) ∩ α = 0`, and similarly after
> every base change: the class caps to zero over every `z : V ⟶ X` whose image is disjoint from `Z`.
> This is the second formula of the characterization of Stacks 0F9H.

```lean
theorem localizedPowerSum_capVanishesOver (h : S.IsZeroOnComplement) (p : ℕ)
    {V : Scheme.{u}} (z : V ⟶ S.X) (hz : Disjoint (Set.range z) (Set.range S.i)) :
    (S.localizedPowerSum h p).CapVanishesOver z
```

**`Stacks.Chow.LocalizedSituation.localizedChern_capVanishesOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedCap.lean, line 275](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedCap.lean#L275). The attribute's comment: “c\_p(Z ⟶ X, E) ∩ α = 0 for α supported away from Z, after every base change”.

> **Stacks 0FB6, for `c_p(Z ⟶ X, E)`.** In Situation 0GUJ, when `E|_{X ∖ Z}` is finite locally
> free of rank `< p` in degree `0`: if `α ∈ CH_k(X)` has support disjoint from `Z`, then
> `c_p(Z ⟶ X, E) ∩ α = 0`, and similarly after every base change: the class caps to zero over every
> `z : V ⟶ X` whose image is disjoint from `Z`. This is the second formula of the characterization
> of Stacks 0F9H.

```lean
theorem localizedChern_capVanishesOver (h : S.IsFiniteLocallyFreeOfRankLTOnComplement)
    {V : Scheme.{u}} (z : V ⟶ S.X) (hz : Disjoint (Set.range z) (Set.range S.i)) :
    (S.localizedChern h).CapVanishesOver z
```

## Tag 0FB7, a lemma

[Tag 0FB7](https://stacks.math.columbia.edu/tag/0FB7) in the Stacks Project.

**`Stacks.Chow.LocalizedSituation.localizedPowerSum_withLargerClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LargerClosedSubscheme.lean, line 530](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LargerClosedSubscheme.lean#L530). The attribute's comment: “for P\_p”.

> **Stacks 0FB7** (Lemma 42.50.8), for `P_p`. In Situation 0GUJ with `E|_{X ∖ Z}` zero, let
> `Z ⊆ Z' ⊆ X` be closed, with `j : Z ⟶ Z'`. Then
> `P_p(Z' ⟶ X, E) = (Z ⟶ Z')_* ∘ P_p(Z ⟶ X, E)` in `A^p(Z' ⟶ X)`, with `∘` as in Stacks 0EPK; the
> class `P_p(Z' ⟶ X, E)` is that of the situation
> `Stacks.Chow.LocalizedSituation.withLargerClosed` for `Z'`.

```lean
theorem localizedPowerSum_withLargerClosed (h : S.IsZeroOnComplement) (p : ℕ) :
    (S.withLargerClosed i' j hj).localizedPowerSum h.withLargerClosed p =
      bivariantProperPushforwardOfInvertible S.base (S.i ≫ S.a) (i' ≫ S.a) S.a j i'
        (by rw [← Category.assoc, hj]) rfl p
        ((S.localizedPowerSum h p).congrHom hj.symm (by rw [hj]))
```

**`Stacks.Chow.LocalizedSituation.localizedChern_withLargerClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LargerClosedSubscheme.lean, line 546](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LargerClosedSubscheme.lean#L546). The attribute's comment: “for c\_p”.

> **Stacks 0FB7** (Lemma 42.50.8), for `c_p`. In Situation 0GUJ with `E|_{X ∖ Z}` finite
> locally free of rank `< p` in degree `0`, let `Z ⊆ Z' ⊆ X` be closed, with `j : Z ⟶ Z'`. Then
> `c_p(Z' ⟶ X, E) = (Z ⟶ Z')_* ∘ c_p(Z ⟶ X, E)` in `A^p(Z' ⟶ X)`, with `∘` as in Stacks 0EPK; the
> class `c_p(Z' ⟶ X, E)` is that of the situation
> `Stacks.Chow.LocalizedSituation.withLargerClosed` for `Z'`.

```lean
theorem localizedChern_withLargerClosed (h : S.IsFiniteLocallyFreeOfRankLTOnComplement) :
    (S.withLargerClosed i' j hj).localizedChern h.withLargerClosed =
      bivariantProperPushforwardOfInvertible S.base (S.i ≫ S.a) (i' ≫ S.a) S.a j i'
        (by rw [← Category.assoc, hj]) rfl S.p
        ((S.localizedChern h).congrHom hj.symm (by rw [hj]))
```

## Tag 0FB8, a lemma

[Tag 0FB8](https://stacks.math.columbia.edu/tag/0FB8) in the Stacks Project.

**`Stacks.Chow.LocalizedSituation.closedCoverPowerSum_eq_localizedPowerSum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedClosedCover.lean, line 779](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedClosedCover.lean#L779). The attribute's comment: “for P\_p: P'\_p(E₂) = P\_p(X₂ → X, E) when E|\_\{X₁} is zero”.

> **Stacks 0FB8, for `P_p`.** Let `X = X₁ ∪ X₂` be a closed cover, let `E` be a perfect object
> of `D(𝒪_X)` whose restriction to `X₁` is zero, and let `(X, X₂, E)` satisfy the finiteness
> condition (3) of Situation 0GUJ, i.e. form a situation `S` with `S.Z = X₂`. Then the class
> `P'_p(E|_{X₂}) ∈ A^p(X₂ ⟶ X)` of Stacks 0F9H agrees with the localized class
> `P_p(X₂ ⟶ X, E)` of Definition 0FB5. Condition (2) of Situation 0GUJ for `X₂` is
> `Stacks.Chow.LocalizedSituation.isZeroOnComplement_of_isZero_derivedPullback`, and the
> vanishing of `E|_{X₂}` on `X₁ ∩ X₂` is that of `E|_{X₁}`.
>
> By Stacks 0BCD `E` vanishes on an open `U ⊇ X₁`; let `Z` be the reduced closed subscheme on
> `X ∖ U`, so that `Z ⊆ X₂` and `Z ∩ X₁ = ∅`. By Stacks 0FB7 `P_p(X₂ ⟶ X, E)` is pushed forward from
> `P_p(Z ⟶ X, E)`, which kills the classes from `X₁` by Stacks 0FB6; and it caps the classes from
> `X₂` as `P_p(E|_{X₂})` does by Stacks 0FB4. Uniqueness in Stacks 0F9H concludes.

```lean
theorem closedCoverPowerSum_eq_localizedPowerSum
    (hzero : IsZero ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
      i₁.toLRSHom.toShHom).obj (S.E : DerivedCategory S.X.Modules))) (p : ℕ) :
    closedCoverPowerSum S.base S.a i₁ S.i (S.i ≫ S.a) rfl
        (S.hasDefinedChernClasses_E.derivedPullback S.i) p hcover
        (isZero_derivedPullback_of_isZero_of_comp_eq pullback.condition hzero) =
      S.localizedPowerSum (S.isZeroOnComplement_of_isZero_derivedPullback i₁ hcover hzero) p
```

**`Stacks.Chow.LocalizedSituation.closedCoverChernClass_eq_localizedChern`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedClosedCover.lean, line 818](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedClosedCover.lean#L818). The attribute's comment: “for c\_p: c'\_p(E₂) = c\_p(X₂ → X, E) when E|\_\{X₁} is finite locally free of rank < p in degree 0”.

> **Stacks 0FB8, for `c_p`.** Let `X = X₁ ∪ X₂` be a closed cover, let `E` be a perfect object
> of `D(𝒪_X)` whose restriction to `X₁` is a finite locally free module of rank `< p` placed in
> degree `0`, and let `(X, X₂, E)` satisfy the finiteness condition (3) of Situation 0GUJ, i.e.
> form a situation `S` with `S.Z = X₂` and `S.p = p`. Then the class `c'_p(E|_{X₂}) ∈ A^p(X₂ ⟶ X)`
> of Stacks 0F9H agrees with the localized Chern class `c_p(X₂ ⟶ X, E)` of Definition 0FB5.
> Condition (2) of Situation 0GUJ for `X₂` is
> `Stacks.Chow.LocalizedSituation.isFiniteLocallyFreeOfRankLTOnComplement_of_iso_singleFunctor`,
> and the hypothesis of Stacks 0F9H on `E|_{X₂}` along `X₁ ∩ X₂` is the restriction of that on
> `E|_{X₁}`.
>
> By Stacks 0BCD `E` is a finite locally free module of rank `< p` in degree `0` on an open
> `U ⊇ X₁`; let `Z` be the reduced closed subscheme on `X ∖ U`, so that `Z ⊆ X₂` and `Z ∩ X₁ = ∅`.
> By Stacks 0FB7 `c_p(X₂ ⟶ X, E)` is pushed forward from `c_p(Z ⟶ X, E)`, which kills the classes
> from `X₁` by Stacks 0FB6; and it caps the classes from `X₂` as `c_p(E|_{X₂})` does by
> Stacks 0FB4. Uniqueness in Stacks 0F9H concludes.

```lean
theorem closedCoverChernClass_eq_localizedChern
    (hrank : ∃ M : X₁.Modules, IsFiniteLocallyFreeOfRankLT M S.p ∧
      Nonempty ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
        i₁.toLRSHom.toShHom).obj (S.E : DerivedCategory S.X.Modules) ≅
          (DerivedCategory.singleFunctor _ 0).obj M)) :
    closedCoverChernClass S.base S.a i₁ S.i (S.i ≫ S.a) rfl
        (S.hasDefinedChernClasses_E.derivedPullback S.i) S.p hcover
        (exists_isFiniteLocallyFreeOfRankLT_derivedPullback_pullbackSnd i₁ S.i hrank) =
      S.localizedChern
        (S.isFiniteLocallyFreeOfRankLTOnComplement_of_iso_singleFunctor i₁ hcover hrank)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.50, Tag 0FB0](https://stacks.math.columbia.edu/tag/0FB0)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
