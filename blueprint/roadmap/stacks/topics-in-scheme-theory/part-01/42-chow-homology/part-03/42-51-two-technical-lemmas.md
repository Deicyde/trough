---
declaration: section
origin: cited
lean: Stacks.Chow.supportedComposite_modificationChernClass, Stacks.Chow.supportedComposite_modificationPowerSum, Stacks.Chow.LocalizedSituation.modificationChernClass_eq_localizedChern, Stacks.Chow.LocalizedSituation.modificationPowerSum_eq_localizedPowerSum
statement: formalized
proof: formalized
---

# 42.51 Two technical lemmas

Section 42.51 of the Stacks Project, [Tag 0FE6](https://stacks.math.columbia.edu/tag/0FE6). 2 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FE7, a lemma

[Tag 0FE7](https://stacks.math.columbia.edu/tag/0FE7) in the Stacks Project.

**`Stacks.Chow.supportedComposite_modificationChernClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedComposite.lean, line 503](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedComposite.lean#L503). The attribute's comment: “the statement for c': c'_{p_n}(Q_n) ∘ ⋯ ∘ c'_{p_1}(Q_1) = (W_{n,∞} ∩ ⋯ ∩ W_{1,∞} → Z_n ∩ ⋯ ∩ Z_1)_* ∘ c'_{p_n}(Q_n|_{W_{n,∞}}) ∘ ⋯ ∘ c'_{p_1}(Q_1|_{W_{1,∞}}) ∘ C, for every sequence of indices i_1, …, i_n”.

> **Composites of the classes `c'`.** Let `b : W ⟶ 𝐏¹_X` be proper and an isomorphism over
> `𝐀¹_X`, and for every index `i` let `Z_i ⊆ X` and `T_i ⊆ W_∞` be closed, `Q_i ∈ D(𝒪_W)` perfect
> with defined Chern classes and `p_i ≥ 0`, such that the hypotheses of Stacks 0F9K hold for
> `b, Z_i, Q_i, T_i, p_i` (`T_i` contains every point of `W_∞` over `X ∖ Z_i` and `Q_i|_{T_i}` is
> finite locally free of rank `< p_i` in degree `0`), `Q_i|_{W ∖ W_i}` is finite locally free of rank
> `< p_i` in degree `0` for `W_i = b^{-1}(𝐏¹_{Z_i}) = W ×_X Z_i`, and `Q_i` satisfies condition (3)
> of Situation 0GUJ. Then for every sequence of indices `i_1, …, i_n` (`n ≥ 1`; the list
> `L = [i_n, …, i_2]` and the first index `i_1`)
>
>   `c'_{p_{i_n}}(Q_{i_n}) ∘ ⋯ ∘ c'_{p_{i_1}}(Q_{i_1}) =
>     (W_{i_n,∞} ∩ ⋯ ∩ W_{i_1,∞} ⟶ Z_{i_n} ∩ ⋯ ∩ Z_{i_1})_* ∘
>       c'_{p_{i_n}}(Q_{i_n}|_{W_{i_n,∞}}) ∘ ⋯ ∘ c'_{p_{i_1}}(Q_{i_1}|_{W_{i_1,∞}}) ∘ C`
>
> in `A^{p_{i_n} + ⋯ + p_{i_1}}(Z_{i_n} ∩ ⋯ ∩ Z_{i_1} ⟶ X)`. Here `c'_p(Q)` is the class of
> Stacks 0F9K (`Stacks.Chow.modificationChernClass`), `c'_p(Q|_{W_{i,∞}})` that of Stacks 0F9H
> (`Stacks.Chow.modificationInfinityChernClass`), `C` the class of Stacks 0F9J, the composites are
> the products of classes supported on closed subschemes of Stacks 0FE5
> (`Stacks.Chow.supportedComposite`, `Stacks.Chow.modificationInfinityComposite`), and the right
> side is `Stacks.Chow.modificationLocalization`.

```lean
theorem supportedComposite_modificationChernClass
    (hrank : ∀ i, ∃ M : (T i).Modules, IsFiniteLocallyFreeOfRankLT M (p i) ∧
      Nonempty ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
        (t i ≫ modificationInclusionAtInfinity f b).toLRSHom.toShHom).obj (Q i) ≅
          (DerivedCategory.singleFunctor _ 0).obj M))
    (hperf : ∀ i, Cohomology.PerfectComplexes.IsPerfect (X := W.toRingedSpace) (Q i))
    (hres : ∀ i, ∃ M : OXMod.{u, u, u} (W.toRingedSpace.restrict
          (modificationComplementOpens b (z i)).isOpenEmbedding),
        IsFiniteLocallyFreeOfRankLT M (p i) ∧
          Nonempty ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
            (W.toRingedSpace.ofRestrict (modificationComplementOpens b (z i)).isOpenEmbedding)).obj
              (Q i) ≅ (DerivedCategory.singleFunctor _ 0).obj M))
    (hfin : ∀ i, LocalizedChernFiniteness C (modificationProjection f b ≫ f) (Q i)) (i₁ : ι)
    (L : List ι) :
    supportedComposite z C f (fun i ↦ (p i : ℤ))
        (fun i ↦ modificationChernClass C f b hA (z i) (t i) (hQ i) (p i) (hT i) (hrank i)) i₁ L =
      modificationLocalization C f b hA (iteratedIntersection z i₁ L).2
        (modificationInfinityComposite z C f (fun i ↦ (p i : ℤ)) b
          (fun i ↦ modificationInfinityChernClass C f b (z i) (t i) (hT i) (hQ i) (p i) (hrank i))
          i₁ L)
```

**`Stacks.Chow.supportedComposite_modificationPowerSum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedComposite.lean, line 544](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedComposite.lean#L544). The attribute's comment: “the statement for P': P'_{p_n}(Q_n) ∘ ⋯ ∘ P'_{p_1}(Q_1) = (W_{n,∞} ∩ ⋯ ∩ W_{1,∞} → Z_n ∩ ⋯ ∩ Z_1)_* ∘ P'_{p_n}(Q_n|_{W_{n,∞}}) ∘ ⋯ ∘ P'_{p_1}(Q_1|_{W_{1,∞}}) ∘ C, for every sequence of indices i_1, …, i_n”.

> **Composites of the classes `P'`.** In the situation of
> `Stacks.Chow.supportedComposite_modificationChernClass`, with `Q_i|_{T_i}` and `Q_i|_{W ∖ W_i}`
> zero instead of finite locally free of rank `< p_i`, for every sequence of indices
> `i_1, …, i_n` (`n ≥ 1`)
>
>   `P'_{p_{i_n}}(Q_{i_n}) ∘ ⋯ ∘ P'_{p_{i_1}}(Q_{i_1}) =
>     (W_{i_n,∞} ∩ ⋯ ∩ W_{i_1,∞} ⟶ Z_{i_n} ∩ ⋯ ∩ Z_{i_1})_* ∘
>       P'_{p_{i_n}}(Q_{i_n}|_{W_{i_n,∞}}) ∘ ⋯ ∘ P'_{p_{i_1}}(Q_{i_1}|_{W_{i_1,∞}}) ∘ C`
>
> in `A^{p_{i_n} + ⋯ + p_{i_1}}(Z_{i_n} ∩ ⋯ ∩ Z_{i_1} ⟶ X)`, with `P'_p(Q)` the class of
> Stacks 0F9K (`Stacks.Chow.modificationPowerSum`) and `P'_p(Q|_{W_{i,∞}})` that of Stacks 0F9H
> (`Stacks.Chow.modificationInfinityPowerSum`).

```lean
theorem supportedComposite_modificationPowerSum
    (hzero : ∀ i, IsZero ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
      (t i ≫ modificationInclusionAtInfinity f b).toLRSHom.toShHom).obj (Q i)))
    (hperf : ∀ i, Cohomology.PerfectComplexes.IsPerfect (X := W.toRingedSpace) (Q i))
    (hres : ∀ i, IsZero ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
        (W.toRingedSpace.ofRestrict (modificationComplementOpens b (z i)).isOpenEmbedding)).obj
          (Q i)))
    (hfin : ∀ i, LocalizedChernFiniteness C (modificationProjection f b ≫ f) (Q i)) (i₁ : ι)
    (L : List ι) :
    supportedComposite z C f (fun i ↦ (p i : ℤ))
        (fun i ↦ modificationPowerSum C f b hA (z i) (t i) (hQ i) (p i) (hT i) (hzero i)) i₁ L =
      modificationLocalization C f b hA (iteratedIntersection z i₁ L).2
        (modificationInfinityComposite z C f (fun i ↦ (p i : ℤ)) b
          (fun i ↦ modificationInfinityPowerSum C f b (z i) (t i) (hT i) (hQ i) (p i) (hzero i))
          i₁ L)
```

## Tag 0FE8, a lemma

[Tag 0FE8](https://stacks.math.columbia.edu/tag/0FE8) in the Stacks Project.

**`Stacks.Chow.LocalizedSituation.modificationChernClass_eq_localizedChern`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedModificationComparison.lean, line 745](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedModificationComparison.lean#L745). The attribute's comment: “for c_p: c'_p(Q) = c_p(Z → X, F) when Q|_{b^{-1}(A^1_X)} is the pullback of F and F|_{X ∖ Z} is finite locally free of rank < p in degree 0”.

> In Situation 0GUJ, let `b : W ⟶ 𝐏¹_X` be proper and an
> isomorphism over `𝐀¹_X`, let `Q ∈ D(𝒪_W)` be perfect, and let
> `T ⊆ W_∞` be closed, contain every point of `W_∞` lying over `X ∖ Z`, and be such that `Q|_T` is
> finite locally free of rank `< p` in degree `0`. Assume that `Q|_{b^{-1}(𝐀¹_X)}` is the pullback
> of `F`, that `F|_{X ∖ Z}` is finite locally free of rank `< p` in degree `0`, and that `Q` on `W`
> satisfies condition (3) of Situation 0GUJ, so that the Chern classes of `Q` are defined
> (`Stacks.Chow.hasDefinedChernClasses_of_localizedChernFiniteness`, assumption (A0) of
> Stacks 0F9K). Then the class `c'_p(Q)` of Stacks 0F9K is the localized Chern class
> `c_p(Z ⟶ X, F)` of Stacks 0FB2.

```lean
theorem modificationChernClass_eq_localizedChern
    (hT : ∀ w, modificationProjectionAtInfinity S.a b w ∉ Set.range S.i → w ∈ Set.range t)
    (hrank : ∃ M : T.Modules, IsFiniteLocallyFreeOfRankLT M S.p ∧
      Nonempty ((derivedPullback (t ≫ modificationInclusionAtInfinity S.a b).toLRSHom.toShHom).obj
        Q ≅ (DerivedCategory.singleFunctor _ 0).obj M))
    (h : S.IsFiniteLocallyFreeOfRankLTOnComplement) :
    modificationChernClass S.base S.a b hA S.i t
        (hasDefinedChernClasses_of_localizedChernFiniteness S.base _ Q hQp hfin) S.p hT hrank =
      S.localizedChern h
```

**`Stacks.Chow.LocalizedSituation.modificationPowerSum_eq_localizedPowerSum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedModificationComparison.lean, line 842](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedModificationComparison.lean#L842). The attribute's comment: “for P_p: P'_p(Q) = P_p(Z → X, F) when Q|_{b^{-1}(A^1_X)} is the pullback of F and F|_{X ∖ Z} is zero”.

> In Situation 0GUJ, let `b : W ⟶ 𝐏¹_X` be proper and an
> isomorphism over `𝐀¹_X`, let `Q ∈ D(𝒪_W)` be perfect, and let
> `T ⊆ W_∞` be closed, contain every point of `W_∞` lying over `X ∖ Z`, and be such that `Q|_T` is
> zero. Assume that `Q|_{b^{-1}(𝐀¹_X)}` is the pullback of `F`, that `F|_{X ∖ Z}` is zero, and that
> `Q` on `W` satisfies condition (3) of Situation 0GUJ, so that the Chern classes of `Q` are defined
> (`Stacks.Chow.hasDefinedChernClasses_of_localizedChernFiniteness`, assumption (A0) of
> Stacks 0F9K). Then the class `P'_p(Q)` of Stacks 0F9K is the localized class `P_p(Z ⟶ X, F)` of
> Stacks 0FB2.

```lean
theorem modificationPowerSum_eq_localizedPowerSum (p : ℕ)
    (hT : ∀ w, modificationProjectionAtInfinity S.a b w ∉ Set.range S.i → w ∈ Set.range t)
    (hzero : IsZero ((derivedPullback
      (t ≫ modificationInclusionAtInfinity S.a b).toLRSHom.toShHom).obj Q))
    (h : S.IsZeroOnComplement) :
    modificationPowerSum S.base S.a b hA S.i t
        (hasDefinedChernClasses_of_localizedChernFiniteness S.base _ Q hQp hfin) p hT hzero =
      S.localizedPowerSum h p
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.51, Tag 0FE6](https://stacks.math.columbia.edu/tag/0FE6)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
