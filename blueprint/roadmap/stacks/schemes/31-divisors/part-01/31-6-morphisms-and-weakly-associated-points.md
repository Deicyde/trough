---
declaration: section
origin: cited
lean: AlgebraicGeometry.weaklyAssociatedPoints_pushforward_subset_image, AlgebraicGeometry.image_associatedPoints_eq_associatedPoints_pushforward, AlgebraicGeometry.associatedPoints_pushforward_eq_weaklyAssociatedPoints_pushforward, AlgebraicGeometry.weaklyAssociatedPoints_pushforward_eq_image_of_isAffineHom, AlgebraicGeometry.weaklyAssociatedPoints_pushforward_eq_image_of_isFinite, AlgebraicGeometry.isWeaklyAssociatedPoint_pullback_of_isGenericPoint_fiber, Stacks.Divisors.IsWeaklyAssociatedPoint.pullback_of_isGenericPoint_fiber, AlgebraicGeometry.isWeaklyAssociatedPoint_of_baseChange
statement: formalized
proof: formalized
---

# 31.6 Morphisms and weakly associated points

Section 31.6 of the Stacks Project, [Tag 05EW](https://stacks.math.columbia.edu/tag/05EW). 6 tags here are carried by 14 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05EX, a lemma

[Tag 05EX](https://stacks.math.columbia.edu/tag/05EX) in the Stacks Project.

**`AlgebraicGeometry.weaklyAssociatedPoints_pushforward_subset_image`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/Pushforward.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/Pushforward.lean#L112).

> **Stacks Project, Tag 05EX.** Every weakly associated point of the pushforward along an
> affine morphism is the image of a weakly associated point of the original module.

```lean
theorem weaklyAssociatedPoints_pushforward_subset_image
    {X S : Scheme.{u}} (f : X ⟶ S) [IsAffineHom f]
    (F : X.Modules) [F.IsQuasicoherent] :
    Stacks.Divisors.weaklyAssociatedPoints ((Scheme.Modules.pushforward f).obj F) ⊆
      f '' Stacks.Divisors.weaklyAssociatedPoints F
```

## Tag 05EY, a lemma

[Tag 05EY](https://stacks.math.columbia.edu/tag/05EY) in the Stacks Project.

**`AlgebraicGeometry.image_associatedPoints_eq_associatedPoints_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/Pushforward.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/Pushforward.lean#L184). The attribute's comment: “associated points”.

> **Stacks Project, Tag 05EY.** The associated points of a quasi-coherent pushforward along
> an affine morphism are the images of the associated points on the locally Noetherian
> source.

```lean
theorem image_associatedPoints_eq_associatedPoints_pushforward
    {X S : Scheme.{u}} (f : X ⟶ S) [IsAffineHom f] [IsLocallyNoetherian X]
    (F : X.Modules) [F.IsQuasicoherent] :
    f '' Stacks.Divisors.associatedPoints F =
      Stacks.Divisors.associatedPoints ((Scheme.Modules.pushforward f).obj F)
```

**`AlgebraicGeometry.associatedPoints_pushforward_eq_weaklyAssociatedPoints_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/Pushforward.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/Pushforward.lean#L197). The attribute's comment: “associated and weakly associated points of the pushforward”.

> **Stacks Project, Tag 05EY.** The associated and weakly associated points of the pushforward
> along an affine morphism agree when the source is locally Noetherian.

```lean
theorem associatedPoints_pushforward_eq_weaklyAssociatedPoints_pushforward
    {X S : Scheme.{u}} (f : X ⟶ S) [IsAffineHom f] [IsLocallyNoetherian X]
    (F : X.Modules) [F.IsQuasicoherent] :
    Stacks.Divisors.associatedPoints ((Scheme.Modules.pushforward f).obj F) =
      Stacks.Divisors.weaklyAssociatedPoints ((Scheme.Modules.pushforward f).obj F)
```

**`AlgebraicGeometry.weaklyAssociatedPoints_pushforward_eq_image_of_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/Pushforward.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/Pushforward.lean#L212). The attribute's comment: “weakly associated points”.

> **Stacks Project, Tag 05EY.** The weakly associated points of a quasi-coherent pushforward
> along an affine morphism are the images of the weakly associated points on the locally
> Noetherian source.

```lean
theorem weaklyAssociatedPoints_pushforward_eq_image_of_isAffineHom
    {X S : Scheme.{u}} (f : X ⟶ S) [IsAffineHom f] [IsLocallyNoetherian X]
    (F : X.Modules) [F.IsQuasicoherent] :
    Stacks.Divisors.weaklyAssociatedPoints ((Scheme.Modules.pushforward f).obj F) =
      f '' Stacks.Divisors.weaklyAssociatedPoints F
```

## Tag 05EZ, a lemma

[Tag 05EZ](https://stacks.math.columbia.edu/tag/05EZ) in the Stacks Project.

**`AlgebraicGeometry.weaklyAssociatedPoints_pushforward_eq_image_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/Pushforward.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/Pushforward.lean#L224).

> **Stacks Project, Tag 05EZ.** For a finite morphism, the weakly associated points of the
> pushforward of a quasi-coherent module are the images of its weakly associated points.

```lean
theorem weaklyAssociatedPoints_pushforward_eq_image_of_isFinite
    {X S : Scheme.{u}} (f : X ⟶ S) [IsFinite f]
    (F : X.Modules) [F.IsQuasicoherent] :
    Stacks.Divisors.weaklyAssociatedPoints ((Scheme.Modules.pushforward f).obj F) =
      f '' Stacks.Divisors.weaklyAssociatedPoints F
```

## Tag 05F0, a lemma

[Tag 05F0](https://stacks.math.columbia.edu/tag/05F0) in the Stacks Project.

**`AlgebraicGeometry.isWeaklyAssociatedPoint_pullback_of_isGenericPoint_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/FlatPullback.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/FlatPullback.lean#L154).

> **Stacks Project, Tag 05F0.** A point which is generic in its fibre and at which a
> morphism is flat is weakly associated to the pullback of a module whenever
> its image is weakly associated to the original module.

```lean
theorem isWeaklyAssociatedPoint_pullback_of_isGenericPoint_fiber
    {X S : Scheme.{u}} (f : X ⟶ S) (G : S.Modules) (x : X)
    (hflat : IsFlatAt f.toLRSHom.toShHom x)
    (hgeneric : f.asFiber x ∈ genericPoints (f.fiber (f x)))
    (hweak : Stacks.Divisors.IsWeaklyAssociatedPoint G (f x)) :
    Stacks.Divisors.IsWeaklyAssociatedPoint ((Scheme.Modules.pullback f).obj G) x
```

**`Stacks.Divisors.IsWeaklyAssociatedPoint.pullback_of_isGenericPoint_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/WeaklyAssociatedFlatPullback.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/WeaklyAssociatedFlatPullback.lean#L146).

> **Stacks Project, Tag 05F0.** A point which is generic in its fibre and at which a
> morphism is flat is weakly associated to the pullback of a module whenever its image is weakly
> associated to the original module.

```lean
theorem IsWeaklyAssociatedPoint.pullback_of_isGenericPoint_fiber
    {X S : Scheme.{u}} (f : X ⟶ S) (G : S.Modules) (x : X)
    (hflat : IsFlatAt f.toLRSHom.toShHom x)
    (hgeneric : f.asFiber x ∈ genericPoints (f.fiber (f x)))
    (hweak : IsWeaklyAssociatedPoint G (f x)) :
    IsWeaklyAssociatedPoint ((Scheme.Modules.pullback f).obj G) x
```

## Tag 0CUC, a lemma

[Tag 0CUC](https://stacks.math.columbia.edu/tag/0CUC) in the Stacks Project.

**`AlgebraicGeometry.isWeaklyAssociatedPoint_of_baseChange`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/BaseChange.lean, line 303](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/BaseChange.lean#L303).

> **Stacks Project, Tag 0CUC.** If a point of a field base change is weakly associated to the
> pullback of a quasi-coherent module, then its image is weakly associated to the original
> module.

```lean
lemma isWeaklyAssociatedPoint_of_baseChange {k K : Type u} [Field k] [Field K] [Algebra k K]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) (F : X.Modules) [F.IsQuasicoherent]
    (y : (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u})) (x : X)
    (hyx : (pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K)))).base y = x)
    (hy : Stacks.Divisors.IsWeaklyAssociatedPoint
      ((Scheme.Modules.pullback
        (pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K))))).obj F) y) :
    Stacks.Divisors.IsWeaklyAssociatedPoint F x
```

## Tag 0EY0, a lemma

[Tag 0EY0](https://stacks.math.columbia.edu/tag/0EY0) in the Stacks Project.

**`Stacks.AlgebraicGeometry.PushforwardRegularity.isWeaklyRegular_stalk_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PushforwardRegularity/Basic.lean, line 827](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PushforwardRegularity/Basic.lean#L827). The attribute's comment: “pushforward\_two\_step”.

> **[Stacks, Tag 0EY0] part (5).** Let `f : X ⟶ S` be a quasi-compact and quasi-separated
> morphism of schemes and let `F` be a quasi-coherent `𝒪_X`-module flat over `S`. If `a, b` is a
> weakly regular sequence on `𝒪_{S,s}`, then it is weakly regular on the stalk of `f_* F` at `s`:
> `a` is a nonzerodivisor on `(f_* F)_s` and `b` is a nonzerodivisor on
> `(f_* F)_s / a (f_* F)_s`.
>
> The source assumes in addition that `a` and `b` lie in the maximal ideal of `𝒪_{S,s}`; that
> hypothesis is used there only to pass to the depth statements, so it is omitted. The conclusion
> is weak regularity rather than regularity because the pushforward stalk may be zero.
> Quasi-coherence of `F` is recorded because the source assumes it, but the proof does not use it:
> see `isWeaklyRegular_stalk_pushforward'`.

```lean
public theorem isWeaklyRegular_stalk_pushforward [QuasiCompact f] [QuasiSeparated f]
    [F.IsQuasicoherent] (s : S) (hflat : IsFlatOver f.toLRSHom.toShHom F)
    (a b : S.presheaf.stalk s)
    (hab : RingTheory.Sequence.IsWeaklyRegular (S.presheaf.stalk s) [a, b]) :
    RingTheory.Sequence.IsWeaklyRegular (TopCat.Presheaf.stalk (C := Ab.{u})
      ((Scheme.Modules.pushforward f).obj F).val.presheaf s) [a, b]
```

**`Stacks.AlgebraicGeometry.PushforwardRegularity.min_depth_le_depth_stalk_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PushforwardRegularity/Depth.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PushforwardRegularity/Depth.lean#L103). The attribute's comment: “flat\_pushforward\_depth”.

> **[Stacks, Tag 0EY0] part (6).** Let `f : X ⟶ S` be a quasi-compact and quasi-separated
> morphism of schemes and let `F` be a quasi-coherent `𝒪_X`-module flat over `S`. If the stalk
> `(f_* F)_s` is finite over `𝒪_{S,s}`, then
>
> `min(2, depth 𝒪_{S,s}) ≤ depth (f_* F)_s`.
>
> The source assumes `𝒪_{S,s}` Noetherian; that hypothesis is used there only through the
> description of the depth of a finite module as the supremum of the lengths of the weakly regular
> sequences in the maximal ideal, which holds over any commutative ring, so it is omitted.

```lean
public theorem min_depth_le_depth_stalk_pushforward [QuasiCompact f] [QuasiSeparated f]
    [F.IsQuasicoherent] (hflat : IsFlatOver f.toLRSHom.toShHom F) (s : S)
    (hfinite : Module.Finite (S.presheaf.stalk s) (TopCat.Presheaf.stalk (C := Ab.{u})
      ((Scheme.Modules.pushforward f).obj F).val.presheaf s)) :
    min (2 : ℕ∞) (Module.depth (S.presheaf.stalk s)
        (IsLocalRing.maximalIdeal (S.presheaf.stalk s)) (S.presheaf.stalk s)) ≤
      Module.depth (S.presheaf.stalk s) (IsLocalRing.maximalIdeal (S.presheaf.stalk s))
        (TopCat.Presheaf.stalk (C := Ab.{u})
          ((Scheme.Modules.pushforward f).obj F).val.presheaf s)
```

**`Stacks.AlgebraicGeometry.OpenStalkExactness.exists_nbhd_openStalkComparison_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PushforwardRegularity/OpenStalkExactness.lean, line 508](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PushforwardRegularity/OpenStalkExactness.lean#L508). The attribute's comment: “stalk exactness after shrinking the base”.

> **The step inside the proof of [Stacks, Tag 0EY0] that shrinks the base.** For `f`
> quasi-compact and quasi-separated and `F` flat over `S`, every nonzerodivisor `a ∈ 𝒪_{S,s}` is
> the germ of a global section `r` of the structure sheaf of an open neighbourhood `U ∋ s`; the
> stalk comparison map `c : (f_* F)_s ⟶ (f'_* F')_t` for the square cutting out `X ×_S U` is
> semilinear over `U.ι.stalkMap t`; and an element of `(f_* F)_s` dies in `(f'_* (F'/rF'))_t`
> exactly when it is divisible by `a`.
>
> This is the clause of Tag 0EY0 that is stated over a shrunken base; part (4) over `S` itself is
> `isSMulRegular_stalk_pushforward`.

```lean
theorem exists_nbhd_openStalkComparison_exact [QuasiCompact f] [QuasiSeparated f]
    (hflat : IsFlatOver f.toLRSHom.toShHom F) (s : S) (a : S.presheaf.stalk s)
    (ha : IsSMulRegular (S.presheaf.stalk s) a) :
    ∃ (U : S.Opens) (hs : s ∈ U) (r : Γ(U.toScheme, (⊤ : U.toScheme.Opens))),
      let t : U.toScheme := ⟨s, hs⟩
      U.ι.stalkMap t a = U.toScheme.presheaf.germ ⊤ t trivial r ∧
      (∀ (z : S.presheaf.stalk s)
          (x : TopCat.Presheaf.stalk (C := Ab.{u})
            ((Scheme.Modules.pushforward f).obj F).val.presheaf s),
        openStalkComparison f U F t (z • x) =
          U.ι.stalkMap t z • openStalkComparison f U F t x) ∧
      ∀ (m : (Scheme.Modules.pullback (pullback.fst f U.ι)).obj F ⟶
          (Scheme.Modules.pullback (pullback.fst f U.ι)).obj F),
        (∀ (W : (pullback f U.ι).Opens)
          (hW : W ≤ pullback.snd f U.ι ⁻¹ᵁ (⊤ : U.toScheme.Opens))
          (z : Γ((Scheme.Modules.pullback (pullback.fst f U.ι)).obj F, W)),
          m.app W z = ((pullback.snd f U.ι).appLE ⊤ W hW r) • z) →
        ∀ x : TopCat.Presheaf.stalk (C := Ab.{u})
            ((Scheme.Modules.pushforward f).obj F).val.presheaf s,
          (TopCat.Presheaf.stalkFunctor Ab.{u} t).map
              ((Scheme.Modules.pushforward (pullback.snd f U.ι)).map
                (cokernel.π m)).mapPresheaf
              (openStalkComparison f U F t x) = 0 ↔
            ∃ y, x = a • y
```

**`Stacks.AlgebraicGeometry.PushforwardRegularity.not_isAssociatedPoint_pushforward_of_not_mem_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PushforwardRegularity/OutsideImage.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PushforwardRegularity/OutsideImage.lean#L52). The attribute's comment: “outside\_association”.

> Let `f : X ⟶ S` be a quasi-compact and quasi-separated morphism of schemes and let `F` be a
> quasi-coherent `𝒪_X`-module. A point of `S` outside the image of `f` is not an associated point
> of `f_* F`.

```lean
public theorem not_isAssociatedPoint_pushforward_of_not_mem_range {X S : Scheme.{u}} (f : X ⟶ S)
    [QuasiCompact f] [QuasiSeparated f] (F : X.Modules) [F.IsQuasicoherent] (s : S)
    (hs : s ∉ Set.range f) :
    ¬ Stacks.Divisors.IsAssociatedPoint ((Scheme.Modules.pushforward f).obj F) s
```

**`Stacks.AlgebraicGeometry.PushforwardRegularity.two_le_depth_stalk_of_isIso_unit_of_notMem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PushforwardRegularity/OutsideImageDepth.lean, line 492](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PushforwardRegularity/OutsideImageDepth.lean#L492). The attribute's comment: “part (3), for an open immersion rather than a general quasi-compact quasi-separated morphism, and with S locally Noetherian in place of the tag's Noetherian 𝒪\_\{S,s} — which is the form both consumers of hdepthOutside use”.

> **Stacks Project, Tag 0EY0, part (3), for an open immersion.** Let `X` be a locally
> Noetherian scheme, let `V ⊆ X` be open and let `ℋ` be an `𝒪_X`-module of finite type which is
> canonically the pushforward of its restriction to `V`. Then the stalk of `ℋ` at a point outside
> `V` has depth at least two.
>
> Restriction `Hom(𝒪_{X,y}, ℋ_y) → Hom(𝔪_y, ℋ_y)` is bijective, which is the criterion
> `Module.two_le_depth_of_bijective_restrict_maximalIdeal`; its two halves are
> `eq_zero_of_germ_smul_eq_zero` and `exists_germ_smul_eq`.

```lean
public theorem two_le_depth_stalk_of_isIso_unit_of_notMem [IsLocallyNoetherian X]
    [H.IsFiniteType]
    (hunit : IsIso ((Scheme.Modules.pullbackPushforwardAdjunction V.ι).unit.app H))
    (y : X) (hy : y ∉ (V : Set X)) :
    (2 : ℕ∞) ≤ Module.depth (X.presheaf.stalk y)
      (IsLocalRing.maximalIdeal (X.presheaf.stalk y))
      (TopCat.Presheaf.stalk (C := Ab.{u}) H.val.presheaf y)
```

**`Stacks.AlgebraicGeometry.PushforwardRegularity.two_le_depth_stalk_pushforward_of_notMem_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PushforwardRegularity/OutsideImageDepthGeneral.lean, line 579](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PushforwardRegularity/OutsideImageDepthGeneral.lean#L579). The attribute's comment: “part (3)”.

> **[Stacks, Tag 0EY0] part (3).** Let `f : X ⟶ S` be a quasi-compact and quasi-separated
> morphism of schemes and let `F` be a quasi-coherent `𝒪_X`-module. Let `s ∈ S` be a point outside
> the image of `f`. If `(f_* F)_s` is a finite `𝒪_{S,s}`-module and `𝒪_{S,s}` is Noetherian, then
>
> `depth ((f_* F)_s) ≥ 2`.
>
> Restriction `Hom(𝒪_{S,s}, (f_*F)_s) → Hom(𝔪_s, (f_*F)_s)` is bijective, which is the criterion
> `Module.two_le_depth_of_bijective_restrict_maximalIdeal`; its two halves are
> `eq_zero_of_germ_smul_eq_zero` and `exists_germ_smul_eq`, both fed by the covering
> `exists_nbhd_mem_basicOpen` that replaces the source's base change to `Spec 𝒪_{S,s}`.

```lean
public theorem two_le_depth_stalk_pushforward_of_notMem_range [QuasiCompact f] [QuasiSeparated f]
    [F.IsQuasicoherent] (s : S) (hs : s ∉ Set.range f)
    (hnoeth : IsNoetherianRing (S.presheaf.stalk s))
    (hfinite : Module.Finite (S.presheaf.stalk s) (TopCat.Presheaf.stalk (C := Ab.{u})
      ((Scheme.Modules.pushforward f).obj F).val.presheaf s)) :
    (2 : ℕ∞) ≤ Module.depth (S.presheaf.stalk s)
      (IsLocalRing.maximalIdeal (S.presheaf.stalk s))
      (TopCat.Presheaf.stalk (C := Ab.{u})
        ((Scheme.Modules.pushforward f).obj F).val.presheaf s)
```

Declarations registered for the tag:

- [`Stacks.AlgebraicGeometry.PushforwardRegularity.isSMulRegular_stalk_pushforward`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PushforwardRegularity/Basic.lean#L666), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/PushforwardRegularity/Depth.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PushforwardRegularity/Depth.lean#L64) (StacksFrontier): “pushforward\_nonzerodivisor”.
- [`WeakAssPushforward.not_isWeaklyAssociatedPoint_pushforward_of_not_mem_range`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=WeakAssPushforward.not_isWeaklyAssociatedPoint_pushforward_of_not_mem_range#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/PushforwardRegularity/OutsideImageDepthGeneral.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PushforwardRegularity/OutsideImageDepthGeneral.lean#L107) (StacksFrontier): “part (1)”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 31.6, Tag 05EW](https://stacks.math.columbia.edu/tag/05EW)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
