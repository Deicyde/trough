---
declaration: section
origin: cited
lean: AlgebraicGeometry.DiagonalResolution.originalComplex, AlgebraicGeometry.DiagonalResolution.transformedTerm, AlgebraicGeometry.DiagonalResolution.HomTransport.complex, AlgebraicGeometry.DiagonalResolution.HomTransport.complex_d, AlgebraicGeometry.exists_transformedDiagonalComplex, AlgebraicGeometry.exists_fourierMukai_areSiblingsPerfect, AlgebraicGeometry.exists_iso_perfectFourierMukaiOver_of_isProjective, AlgebraicGeometry.exists_fourierMukai_isEquivalence_areSiblingsPerfect
statement: formalized
proof: formalized
---

# 57.13 Fully faithful functors

Section 57.13 of the Stacks Project, [Tag 0G07](https://stacks.math.columbia.edu/tag/0G07). 6 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0G09, an equation

[Tag 0G09](https://stacks.math.columbia.edu/tag/0G09) in the Stacks Project.

**`AlgebraicGeometry.DiagonalResolution.originalComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/DiagonalResolution.lean, line 209](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/DiagonalResolution.lean#L209).

> **The complex `… → ℰ₂ ⊠ 𝒢₂ → ℰ₁ ⊠ 𝒢₁ → ℰ₀ ⊠ 𝒢₀` of external tensor products underlying a
> resolution of the diagonal.** It is the augmented resolution with its degree-zero term `𝒪_Δ`
> discarded, so its term in degree `i` is the external tensor product indexed by `i`.

```lean
def originalComplex : ChainComplex (pullback f f).Modules ℕ
```

## Tag 0G0A, an equation

[Tag 0G0A](https://stacks.math.columbia.edu/tag/0G0A) in the Stacks Project.

**`AlgebraicGeometry.DiagonalResolution.transformedTerm`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/TransformedDiagonal/Basic.lean, line 135](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/TransformedDiagonal/Basic.lean#L135). The attribute's comment: “the terms of the complex”.

> The term `ℰᵢ ⊠ F(𝒢ᵢ)`: the derived external tensor product, on `X ×_A Y`, of the `i`-th first
> factor of a resolution of the diagonal with the value of `F` at the `i`-th second factor.

```lean
def transformedTerm (hG : ∀ i, IsPerfect (X := X.toRingedSpace)
      ((DerivedCategory.singleFunctor X.Modules 0).obj (R.right i))) (i : ℕ) :
    DerivedCategory (pullback f g).Modules
```

**`AlgebraicGeometry.DiagonalResolution.HomTransport.complex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/TransformedDiagonal/Basic.lean, line 165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/TransformedDiagonal/Basic.lean#L165). The attribute's comment: “the complex”.

> The complex `… → ℰ₂ ⊠ F(𝒢₂) → ℰ₁ ⊠ F(𝒢₁) → ℰ₀ ⊠ F(𝒢₀)` on `X ×_A Y` obtained from a
> resolution of the diagonal of `X` by transforming its second factors by `F`. Its differentials
> are those of the resolution, transported along the given identification of Hom groups.

```lean
def complex (T : HomTransport R g F hG) :
    ChainComplex (DerivedCategory (pullback f g).Modules) ℕ
```

**`AlgebraicGeometry.DiagonalResolution.HomTransport.complex_d`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/TransformedDiagonal/Basic.lean, line 180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/TransformedDiagonal/Basic.lean#L180). The attribute's comment: “the differentials of the complex”.

> The differential of the transformed complex from index `i + 1` to index `i` is the
> differential `ℰᵢ₊₁ ⊠ 𝒢ᵢ₊₁ ⟶ ℰᵢ ⊠ 𝒢ᵢ` of the resolution of the diagonal, transported along the
> identification of Hom groups.

```lean
theorem complex_d (T : HomTransport R g F hG) (i : ℕ) :
    T.complex.d (i + 1) i = T.hom (i + 1) i (R.boxDifferential i)
```

**`AlgebraicGeometry.exists_transformedDiagonalComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/TransformedDiagonal/SituationUnconditional.lean, line 122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/TransformedDiagonal/SituationUnconditional.lean#L122).

> **(0G0A).** For `X`, `Y` proper smooth over a field `k`, `F : D_perf(𝒪_X) ⥤ D_perf(𝒪_Y)`
> `k`-linear exact fully faithful and `R` a resolution of the diagonal by `ℰᵢ ⊠ 𝒢ᵢ`, there is a
> complex `… ⟶ ℰ₁ ⊠ F(𝒢₁) ⟶ ℰ₀ ⊠ F(𝒢₀)` in `D_perf(𝒪_{X ×_k Y})` whose differentials are those of
> `R` transported by the identification of Hom groups sending `a ⊠ b` to `a ⊠ F(b)`.

```lean
theorem exists_transformedDiagonalComplex (k : Type u) [Field k]
    (X Y : Over (Spec (.of k))) [Smooth X.hom] [Smooth Y.hom]
    [IsProper X.hom] [IsProper Y.hom] :
    letI : Linear k X.left.Modules := modulesLinear k X
    letI : Linear k Y.left.Modules := modulesLinear k Y
    ∀ (F : perfectDerived X.left ⥤ perfectDerived Y.left) [F.CommShift ℤ] [F.IsTriangulated],
      F.Linear k → Nonempty F.FullyFaithful →
      ∀ (R : DiagonalResolution X.hom),
        ∃ T : ImageHomTransport R Y.hom F,
          (∀ i, T.complex.X i = R.imageTerm Y.hom F i) ∧
          (∀ i, IsPerfect (X := (pullback X.hom Y.hom).toRingedSpace) (T.complex.X i)) ∧
          (∀ i, T.complex.d (i + 1) i = T.hom (i + 1) i (R.boxDifferential i)) ∧
          ∀ (i j : ℕ) (a : R.left i ⟶ R.left j) (b : R.right i ⟶ R.right j),
            T.hom i j (externalTensorProductMap X.hom X.hom a b) =
              R.transformedMap Y.hom F a b
```

## Tag 0G0B, a lemma

[Tag 0G0B](https://stacks.math.columbia.edu/tag/0G0B) in the Stacks Project.

**`AlgebraicGeometry.exists_fourierMukai_areSiblingsPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/Orlov/TwistOfFixing.lean, line 518](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/Orlov/TwistOfFixing.lean#L518).

> **Stacks Project, Tag 0G0B.** Let `k` be a field and `X`, `Y` smooth proper `k`-schemes.
> Every `k`-linear exact fully faithful functor `F : D_perf(𝒪_X) ⥤ D_perf(𝒪_Y)` has a sibling
> ([Stacks, Tag 0FZZ]) which is a Fourier-Mukai functor `Φ_K : D_perf(𝒪_X) ⥤ D_perf(𝒪_Y)` whose
> kernel `K` is a perfect object of `D(𝒪_{X ×_k Y})`.
>
> The proof is the source's: [Stacks, Tag 0G06] applied to `F` and the Fourier-Mukai functor `G`
> of [Stacks, Section 0G07]
> (`AlgebraicGeometry.exists_perfectFourierMukaiOver_agrees_zeroDimensional`), which agrees with
> `F` on the coherent modules with zero-dimensional support.

```lean
theorem _root_.AlgebraicGeometry.exists_fourierMukai_areSiblingsPerfect
    (F : PerfectDerivedCategory X.left ⥤ PerfectDerivedCategory Y.left)
    [hFs : F.CommShift ℤ] [hFt : F.IsTriangulated]
    (hlin : letI : Linear k X.left.Modules := modulesLinear k X
      letI : Linear k Y.left.Modules := modulesLinear k Y
      F.Linear k)
    (hF : Nonempty F.FullyFaithful) :
    haveI : CompactSpace X.left := (quasiCompact_iff_compactSpace X.hom).mp inferInstance
    haveI : CompactSpace Y.left := (quasiCompact_iff_compactSpace Y.hom).mp inferInstance
    haveI : IsNoetherian Y.left := isNoetherian_of_locallyOfFiniteType Y.hom
    ∃ (K : DerivedCategory (pullback X.hom Y.hom).Modules)
      (hK : IsPerfect (X := (pullback X.hom Y.hom).toRingedSpace) K),
      @AreSiblingsPerfect X.left Y.left (isRegular_of_smooth_over_field X.hom)
        (isRegular_of_smooth_over_field Y.hom) _ _ F (perfectFourierMukaiOver k X Y hK) hFs hFt
        (commShift_fourierMukaiOn _ _ _ _ _ _) (isTriangulated_fourierMukaiOn _ _ _ _ _ _)
```

## Tag 0G0C, a theorem

[Tag 0G0C](https://stacks.math.columbia.edu/tag/0G0C) in the Stacks Project.

**`AlgebraicGeometry.exists_iso_perfectFourierMukaiOver_of_isProjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/Orlov/TwistOfFixing.lean, line 768](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/Orlov/TwistOfFixing.lean#L768).

> **Stacks Project, Tag 0G0C** (Orlov). Let `k` be a field and `X`, `Y` smooth proper schemes
> over `k` with `X` projective over `k` (`AlgebraicGeometry.IsProjective X.hom`, the first condition
> of [Stacks, Tag 01W8]). Every `k`-linear exact fully faithful functor
> `F : D_perf(𝒪_X) ⥤ D_perf(𝒪_Y)` is a Fourier-Mukai functor: there is a perfect object `K` of
> `D(𝒪_{X ×_k Y})` with `F ≅ Φ_K` as functors.
>
> A projective `k`-scheme carries an ample invertible module
> (`AlgebraicGeometry.IsProjective.isProper_and_exists_isAmple_of_isAffine`), and for those this is
> `AlgebraicGeometry.exists_iso_perfectFourierMukaiOver`, whose proof is the source's: a
> Fourier-Mukai sibling from [Stacks, Tag 0G0B], made isomorphic to `F` by [Stacks, Tag 0FZW].

```lean
theorem _root_.AlgebraicGeometry.exists_iso_perfectFourierMukaiOver_of_isProjective
    (hX : AlgebraicGeometry.IsProjective X.hom)
    (F : PerfectDerivedCategory X.left ⥤ PerfectDerivedCategory Y.left)
    [hFs : F.CommShift ℤ] [hFt : F.IsTriangulated]
    (hlin : letI : Linear k X.left.Modules := modulesLinear k X
      letI : Linear k Y.left.Modules := modulesLinear k Y
      F.Linear k)
    (hF : Nonempty F.FullyFaithful) :
    haveI : IsNoetherian Y.left := isNoetherian_of_locallyOfFiniteType Y.hom
    ∃ (K : DerivedCategory (pullback X.hom Y.hom).Modules)
      (hK : IsPerfect (X := (pullback X.hom Y.hom).toRingedSpace) K),
      Nonempty (F ≅ perfectFourierMukaiOver k X Y hK)
```

## Tag 0G0D, a proposition

[Tag 0G0D](https://stacks.math.columbia.edu/tag/0G0D) in the Stacks Project.

**`AlgebraicGeometry.exists_fourierMukai_isEquivalence_areSiblingsPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/Orlov/TwistOfFixing.lean, line 549](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/Orlov/TwistOfFixing.lean#L549).

> **Stacks Project, Tag 0G0D.** Let `k` be a field and `X`, `Y` smooth proper `k`-schemes. If
> `F : D_perf(𝒪_X) ⥤ D_perf(𝒪_Y)` is a `k`-linear exact equivalence, then there is a Fourier-Mukai
> functor `F' = Φ_K : D_perf(𝒪_X) ⥤ D_perf(𝒪_Y)` with kernel `K ∈ D_perf(𝒪_{X ×_k Y})` which is
> an equivalence and a sibling of `F`. The functor of [Stacks, Tag 0G0B] is a sibling of `F`, and a
> sibling of an equivalence is an equivalence by [Stacks, Tag 0FZV]
> (`AlgebraicGeometry.AreSiblingsPerfect.isEquivalence`).

```lean
theorem _root_.AlgebraicGeometry.exists_fourierMukai_isEquivalence_areSiblingsPerfect
    (F : PerfectDerivedCategory X.left ⥤ PerfectDerivedCategory Y.left)
    [hFs : F.CommShift ℤ] [hFt : F.IsTriangulated]
    (hlin : letI : Linear k X.left.Modules := modulesLinear k X
      letI : Linear k Y.left.Modules := modulesLinear k Y
      F.Linear k)
    [F.IsEquivalence] :
    haveI : CompactSpace X.left := (quasiCompact_iff_compactSpace X.hom).mp inferInstance
    haveI : CompactSpace Y.left := (quasiCompact_iff_compactSpace Y.hom).mp inferInstance
    haveI : IsNoetherian Y.left := isNoetherian_of_locallyOfFiniteType Y.hom
    ∃ (K : DerivedCategory (pullback X.hom Y.hom).Modules)
      (hK : IsPerfect (X := (pullback X.hom Y.hom).toRingedSpace) K),
      (perfectFourierMukaiOver k X Y hK).IsEquivalence ∧
        @AreSiblingsPerfect X.left Y.left (isRegular_of_smooth_over_field X.hom)
          (isRegular_of_smooth_over_field Y.hom) _ _ F (perfectFourierMukaiOver k X Y hK) hFs hFt
          (commShift_fourierMukaiOn _ _ _ _ _ _) (isTriangulated_fourierMukaiOn _ _ _ _ _ _)
```

## Tag 0G0E, a lemma

[Tag 0G0E](https://stacks.math.columbia.edu/tag/0G0E) in the Stacks Project.

**`Stacks.Duality.nonempty_iso_diagonalFourierMukaiKernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/IdentityKernelStepThree.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/IdentityKernelStepThree.lean#L150).

> **[Stacks, Tag 0G0E].**  Let `k` be a field, let `X` be a smooth proper scheme over `k` and
> let `K` be a perfect object of `D(𝒪_{X ×_k X})`.  If the Fourier-Mukai functor
> `Φ_K : D_perf(𝒪_X) ⟶ D_perf(𝒪_X)` of [Stacks, Tag 0FYQ] is isomorphic to the identity functor,
> then `K ≅ Δ_*𝒪_X`.

```lean
theorem nonempty_iso_diagonalFourierMukaiKernel
    (K : DerivedCategory (Limits.pullback f f).Modules)
    (hK : perfectDerivedObjects (Limits.pullback f f) K)
    (hΦ : RepresentsIdentityOnPerfect f K) :
    Nonempty (K ≅ diagonalFourierMukaiKernel f)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 57.13, Tag 0G07](https://stacks.math.columbia.edu/tag/0G07)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
