---
declaration: section
origin: cited
lean: Stacks.PseudoCoherentHocolim.isPseudoCoherent_iff_exists_perfect_hocolim, Stacks.PseudoCoherentHocolim.isPseudoCoherent_iff_exists_supported_perfect_hocolim
statement: formalized
proof: formalized
---

# 36.19 Characterizing pseudo-coherent complexes, I

Section 36.19 of the Stacks Project, [Tag 0DJM](https://stacks.math.columbia.edu/tag/0DJM). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DJN, a lemma

[Tag 0DJN](https://stacks.math.columbia.edu/tag/0DJN) in the Stacks Project.

**`Stacks.PseudoCoherentHocolim.isPseudoCoherent_iff_exists_perfect_hocolim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/PseudoCoherentHocolim.lean, line 672](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/PseudoCoherentHocolim.lean#L672).

> **[Stacks, Tag 0DJN].** Let `X` be a quasi-compact and quasi-separated scheme and let `K` be an
> object of `D(𝒪_X)`. The following are equivalent:
> 1. `K` is pseudo-coherent;
> 2. `K = hocolim Kₙ` where each `Kₙ` is perfect and `τ_{≥ -n} Kₙ ⟶ τ_{≥ -n} K` is an
>    isomorphism for all `n`.
>
> Here `K = hocolim Kₙ` is `CategoryTheory.Pretriangulated.IsHomotopyColimitWith F K c` (Definition
> 090Z, recording the coprojections `cₙ : Kₙ ⟶ K`), the map `τ_{≥ -n} Kₙ ⟶ τ_{≥ -n} K` is the
> truncation of the coprojection `cₙ`, and the derived category is an arbitrary model of `D(𝒪_X)`.
> The system is indexed by `n = 0, 1, 2, …`, as in Definition 090Z; a system `K₁ ⟶ K₂ ⟶ ⋯` indexed
> from `1` as in the source's proof is the case `Kₙ ↦ Kₙ₊₁`, which satisfies the condition at `n`
> because it does at `n + 1`.

```lean
theorem isPseudoCoherent_iff_exists_perfect_hocolim [CompactSpace X] [QuasiSeparatedSpace X]
    (K : DerivedCategory X.Modules) :
    @RingedSpace.IsPseudoCoherent X.toRingedSpace h K ↔
      ∃ (F : ℕ ⥤ DerivedCategory X.Modules) (_ : HasCoproduct F.obj) (c : ∀ n, F.obj n ⟶ K),
        (∀ n, @Stacks.Cohomology.PerfectComplexes.IsPerfect X.toRingedSpace h (F.obj n)) ∧
        IsHomotopyColimitWith F K c ∧
        ∀ n : ℕ, IsIso ((DerivedCategory.TStructure.t.truncGE (-(n : ℤ))).map (c n))
```

## Tag 0DJP, a lemma

[Tag 0DJP](https://stacks.math.columbia.edu/tag/0DJP) in the Stacks Project.

**`Stacks.PseudoCoherentHocolim.isPseudoCoherent_iff_exists_supported_perfect_hocolim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/PseudoCoherentHocolimSupported.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/PseudoCoherentHocolimSupported.lean#L55).

> **[Stacks, Tag 0DJP].** Let `X` be a quasi-compact and quasi-separated scheme, let `T ⊆ X` be
> a closed subset with `X \ T` quasi-compact and let `K ∈ D(𝒪_X)` be supported on `T`. Then `K` is
> pseudo-coherent if and only if `K = hocolim Kₙ` for a system `F` of perfect objects `Kₙ`, each
> supported on `T`, such that `τ_{≥ -n} Kₙ ⟶ τ_{≥ -n} K` is an isomorphism for every `n`; here
> `c n : Kₙ ⟶ K` are the coprojections of the homotopy colimit. The derived category is an
> arbitrary model of `D(𝒪_X)`.

```lean
theorem isPseudoCoherent_iff_exists_supported_perfect_hocolim (X : Scheme.{u})
    [CompactSpace X] [QuasiSeparatedSpace X] [h : HasDerivedCategory.{w} X.Modules]
    (T : Set X) (hT : IsClosed T) (hTc : IsCompact Tᶜ) (K : DerivedCategory X.Modules)
    (hK : @Stacks.Cohomology.PushforwardRestriction.CohomologySupportedOn _ X.ringCatSheaf h T K) :
    @RingedSpace.IsPseudoCoherent X.toRingedSpace h K ↔
      ∃ (F : ℕ ⥤ DerivedCategory X.Modules) (_ : HasCoproduct F.obj) (c : ∀ n, F.obj n ⟶ K),
        (∀ n, @Stacks.Cohomology.PerfectComplexes.IsPerfect X.toRingedSpace h (F.obj n)) ∧
        (∀ n, @Stacks.Cohomology.PushforwardRestriction.CohomologySupportedOn _ X.ringCatSheaf h
          T (F.obj n)) ∧
        IsHomotopyColimitWith F K c ∧
        ∀ n : ℕ, IsIso ((DerivedCategory.TStructure.t.truncGE (-(n : ℤ))).map (c n))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.19, Tag 0DJM](https://stacks.math.columbia.edu/tag/0DJM)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
