---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.eulerCharacteristic, AlgebraicGeometry.Space.eulerCharacteristic_add_of_shortExact_of_outer, AlgebraicGeometry.Space.eulerCharacteristic_add_of_shortExact_of_isProper, AlgebraicGeometry.Space.eulerCharacteristic_eq_finsum_eulerCharacteristic_higherDirectImage, AlgebraicGeometry.Space.exists_eulerCharacteristic_eq_finsum_eulerCharacteristic_higherDirectImage
statement: formalized
proof: formalized
---

# 72.17 Euler characteristics

Section 72.17 of the Stacks Project, [Tag 0DN0](https://stacks.math.columbia.edu/tag/0DN0). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DN1, a definition

[Tag 0DN1](https://stacks.math.columbia.edu/tag/0DN1) in the Stacks Project.

**`AlgebraicGeometry.Space.eulerCharacteristic`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EulerCharacteristic.lean, line 296](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EulerCharacteristic.lean#L296).

> **Stacks 0DN1.** The Euler characteristic of a coherent module `F` on a proper algebraic
> space `X` over a field `k`: the alternating sum `∑ᵢ (-1)ⁱ dim_k Hⁱ(X, F)` of the dimensions over
> `k` of the cohomology modules of `F` on the small étale site of `X`.

```lean
def eulerCharacteristic (f : X ⟶ yoneda.obj (baseObject k B hk))
    (_hf : IsProper B (Spec (.of k)) hk f)
    (F : Modules.{u, max (u + 1) w} B (Spec (.of k)) hk X hX)
    [IsCoherent B (Spec (.of k)) hk X hX F] : ℤ
```

## Tag 0DN2, a lemma

[Tag 0DN2](https://stacks.math.columbia.edu/tag/0DN2) in the Stacks Project.

**`AlgebraicGeometry.Space.eulerCharacteristic_add_of_shortExact_of_outer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EulerCharacteristic.lean, line 430](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EulerCharacteristic.lean#L430).

> **Stacks 0DN2.** Let `k` be a field, `X` a proper algebraic space over `k` and
> `0 ⟶ F₁ ⟶ F₂ ⟶ F₃ ⟶ 0` a short exact sequence of coherent `𝒪_X`-modules. Then
> `χ(X, F₂) = χ(X, F₁) + χ(X, F₃)`.
>
> `X` is quasi-compact and quasi-separated, being proper over `Spec k`, so by Stacks 072C there is
> `N` beyond which the cohomology of every coherent module vanishes; below `N` the cohomology of
> `F₁` and `F₃` is finite-dimensional by Stacks 08AS; and the long exact sequence with
> rank-nullity is
> `AlgebraicGeometry.Space.finsum_alternating_finrank_cohomologyOverBase_add_of_shortExact_of_outer`.

```lean
theorem eulerCharacteristic_add_of_shortExact_of_outer
    (f : X ⟶ yoneda.obj (baseObject k B hk)) (hf : IsProper B (Spec (.of k)) hk f)
    {S : ShortComplex (Modules.{u, max (u + 1) w} B (Spec (.of k)) hk X hX)} (hS : S.ShortExact)
    [IsCoherent B (Spec (.of k)) hk X hX S.X₁] [IsCoherent B (Spec (.of k)) hk X hX S.X₂]
    [IsCoherent B (Spec (.of k)) hk X hX S.X₃] :
    eulerCharacteristic.{u, w} k B hk X hX f hf S.X₂ =
      eulerCharacteristic.{u, w} k B hk X hX f hf S.X₁ +
        eulerCharacteristic.{u, w} k B hk X hX f hf S.X₃
```

**`AlgebraicGeometry.Space.eulerCharacteristic_add_of_shortExact_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EulerCharacteristicAdditivity.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EulerCharacteristicAdditivity.lean#L65).

> **Stacks 0DN2.**  Let `k` be a field, `X` a proper algebraic space over `k` and
> `0 ⟶ F₁ ⟶ F₂ ⟶ F₃ ⟶ 0` a short exact sequence of coherent `𝒪_X`-modules.  Then
> `χ(X, F₂) = χ(X, F₁) + χ(X, F₃)`.
>
> This is `AlgebraicGeometry.Space.eulerCharacteristic_add_of_shortExact_of_outer`: the long exact
> sequence of cohomology and rank-nullity, with the finiteness of Stacks 08AS and the uniform
> vanishing of Stacks 072C, for `X` quasi-compact and quasi-separated, being proper over
> `Spec k`.

```lean
theorem eulerCharacteristic_add_of_shortExact_of_isProper
    (X : (BigFppfOver B (Spec (.of k)) hk)ᵒᵖ ⥤ Type u) (hX : IsAlgebraicSpace B (Spec (.of k)) hk X)
    (f : X ⟶ yoneda.obj (baseObject k B hk)) (hf : IsProper B (Spec (.of k)) hk f)
    {S : ShortComplex (Modules.{u, max (u + 1) w} B (Spec (.of k)) hk X hX)} (hS : S.ShortExact)
    [IsCoherent B (Spec (.of k)) hk X hX S.X₁] [IsCoherent B (Spec (.of k)) hk X hX S.X₂]
    [IsCoherent B (Spec (.of k)) hk X hX S.X₃] :
    eulerCharacteristic.{u, w} k B hk X hX f hf S.X₂ =
      eulerCharacteristic.{u, w} k B hk X hX f hf S.X₁ +
        eulerCharacteristic.{u, w} k B hk X hX f hf S.X₃
```

## Tag 0EDD, a lemma

[Tag 0EDD](https://stacks.math.columbia.edu/tag/0EDD) in the Stacks Project.

**`AlgebraicGeometry.Space.eulerCharacteristic_eq_finsum_eulerCharacteristic_higherDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EulerCharacteristicHigherDirectImage.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EulerCharacteristicHigherDirectImage.lean#L140).

> Let `k` be a field, `f : Y ⟶ X` a morphism of algebraic spaces proper over
> `k` and `𝓖` a coherent `𝒪_Y`-module. Then only finitely many of the higher direct images
> `Rⁱf_*𝓖` are nonzero, each is coherent, and
> `χ(Y, 𝓖) = ∑ᵢ (-1)ⁱ χ(X, Rⁱf_*𝓖)`.
>
> Here `𝓖` has sections in the universe of the structure sheaf, where `Rⁱf_*` exists, and both
> Euler characteristics are taken of universe lifts.

```lean
theorem eulerCharacteristic_eq_finsum_eulerCharacteristic_higherDirectImage (f : Y ⟶ X)
    (πX : X.1 ⟶ yoneda.obj (baseObject k B hk)) (hπX : IsProper B (Spec (.of k)) hk πX)
    (πY : Y.1 ⟶ yoneda.obj (baseObject k B hk)) (hπY : IsProper B (Spec (.of k)) hk πY)
    (G : Modules.{u, u} B (Spec (.of k)) hk Y.1 Y.2)
    [hG : IsCoherent B (Spec (.of k)) hk Y.1 Y.2 G] :
    have := hasInjectiveResolutions_modules B (Spec (.of k)) hk Y.1 Y.2
    have := isCoherent_higherDirectImage_of_isProper_toBase k B hk f πX hπX πY hπY G
    {i : ℕ | ¬ IsZero (((modulePushforward B (Spec (.of k)) hk f).rightDerived i).obj G)}.Finite ∧
      eulerCharacteristic.{u, w} k B hk Y.1 Y.2 πY hπY
          (SheafOfModules.uliftForPresentation.{u + 1, u, u, u, max (u + 1) w} G) =
        ∑ᶠ i : ℕ, (-1 : ℤ) ^ i * eulerCharacteristic.{u, w} k B hk X.1 X.2 πX hπX
          (SheafOfModules.uliftForPresentation.{u + 1, u, u, u, max (u + 1) w}
            (((modulePushforward B (Spec (.of k)) hk f).rightDerived i).obj G))
```

**`AlgebraicGeometry.Space.exists_eulerCharacteristic_eq_finsum_eulerCharacteristic_higherDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EulerCharacteristicHigherDirectImage.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EulerCharacteristicHigherDirectImage.lean#L250). The attribute's comment: “for a coherent module in the universe of the Euler characteristic, the higher direct images being taken of its descent to the universe of the structure sheaf”.

> For a coherent module `𝓖'` with sections in the universe of the Euler characteristic: `𝓖'` is
> the universe lift of a coherent module `𝓖` with sections in the universe of the structure sheaf,
> only finitely many `Rⁱf_*𝓖` are nonzero, and `χ(Y, 𝓖') = ∑ᵢ (-1)ⁱ χ(X, Rⁱf_*𝓖)`.

```lean
theorem exists_eulerCharacteristic_eq_finsum_eulerCharacteristic_higherDirectImage (f : Y ⟶ X)
    (πX : X.1 ⟶ yoneda.obj (baseObject k B hk)) (hπX : IsProper B (Spec (.of k)) hk πX)
    (πY : Y.1 ⟶ yoneda.obj (baseObject k B hk)) (hπY : IsProper B (Spec (.of k)) hk πY)
    (G' : Modules.{u, max (u + 1) w} B (Spec (.of k)) hk Y.1 Y.2)
    [IsCoherent B (Spec (.of k)) hk Y.1 Y.2 G'] :
    ∃ (G : Modules.{u, u} B (Spec (.of k)) hk Y.1 Y.2)
      (_ : IsCoherent B (Spec (.of k)) hk Y.1 Y.2 G)
      (_ : SheafOfModules.uliftForPresentation.{u + 1, u, u, u, max (u + 1) w} G ≅ G'),
      have := hasInjectiveResolutions_modules B (Spec (.of k)) hk Y.1 Y.2
      have := isCoherent_higherDirectImage_of_isProper_toBase k B hk f πX hπX πY hπY G
      {i : ℕ | ¬ IsZero (((modulePushforward B (Spec (.of k)) hk f).rightDerived i).obj G)}.Finite ∧
        eulerCharacteristic.{u, w} k B hk Y.1 Y.2 πY hπY G' =
          ∑ᶠ i : ℕ, (-1 : ℤ) ^ i * eulerCharacteristic.{u, w} k B hk X.1 X.2 πX hπX
            (SheafOfModules.uliftForPresentation.{u + 1, u, u, u, max (u + 1) w}
              (((modulePushforward B (Spec (.of k)) hk f).rightDerived i).obj G))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 72.17, Tag 0DN0](https://stacks.math.columbia.edu/tag/0DN0)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
