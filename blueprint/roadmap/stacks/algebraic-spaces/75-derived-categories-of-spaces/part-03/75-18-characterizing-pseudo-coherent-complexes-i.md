---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isPseudoCoherent_iff_exists_isHomotopyColimitWith, AlgebraicGeometry.PerfectApproximation.isPseudoCoherent_iff_exists_isHomotopyColimitWith
statement: formalized
proof: formalized
---

# 75.18 Characterizing pseudo-coherent complexes, I

Section 75.18 of the Stacks Project, [Tag 0DKA](https://stacks.math.columbia.edu/tag/0DKA). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DKB, a lemma

[Tag 0DKB](https://stacks.math.columbia.edu/tag/0DKB) in the Stacks Project.

**`AlgebraicGeometry.Space.isPseudoCoherent_iff_exists_isHomotopyColimitWith`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PseudoCoherentHomotopyColimit.lean, line 390](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PseudoCoherentHomotopyColimit.lean#L390).

> **Stacks 0DKB.**  Let `S` be a scheme, let `X` be a quasi-compact and quasi-separated
> algebraic space over `S` and let `K ∈ D(𝒪_X)`.  The following are equivalent:
> 1. `K` is pseudo-coherent;
> 2. `K = hocolim Kₙ` where `Kₙ` is perfect and `τ_{≥-n}Kₙ ⟶ τ_{≥-n}K` is an isomorphism for all
>    `n`.
>
> The model of `D(𝒪_X)` is arbitrary.  The system is `F : ℕ ⥤ D(𝒪_X)`, indexed from `0`, its
> member `F.obj n` being the source's `K_{n+1}`; so the truncation condition at index `n` is in
> degree `-(n + 1)`.  The maps `Kₙ ⟶ K` are the coprojections `c n` of the derived colimit
> (`CategoryTheory.Pretriangulated.IsHomotopyColimitWith`), whose direct sum `⊕ Kₙ` exists because
> the `𝒪_X`-modules form a Grothendieck abelian category.

```lean
theorem isPseudoCoherent_iff_exists_isHomotopyColimitWith
    (hqc : IsQuasiCompactSpace B S hS X) (hqs : IsAbsolutelyQuasiSeparated B S hS hZ X)
    [HasDerivedCategory.{w} (Modules.{u, u} B S hS X hX)]
    (K : DerivedCategory (Modules.{u, u} B S hS X hX)) :
    haveI := hasColimitsOfShape_discrete_nat_derivedCategory_modules B S hS X hX
    (smallEtaleRingedSite B S hS X hX).IsPseudoCoherent K ↔
      ∃ (F : ℕ ⥤ DerivedCategory (Modules.{u, u} B S hS X hX)) (c : ∀ n, F.obj n ⟶ K),
        (∀ n, (smallEtaleRingedSite B S hS X hX).IsPerfect (F.obj n)) ∧
          (∀ n : ℕ,
            IsIso ((DerivedCategory.TStructure.t.truncGE (-((n : ℤ) + 1))).map (c n))) ∧
            IsHomotopyColimitWith F K c
```

## Tag 0DKC, a lemma

[Tag 0DKC](https://stacks.math.columbia.edu/tag/0DKC) in the Stacks Project.

**`AlgebraicGeometry.PerfectApproximation.isPseudoCoherent_iff_exists_isHomotopyColimitWith`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/PseudoCoherentComplex/HomotopyColimitSupported.lean, line 360](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/PseudoCoherentComplex/HomotopyColimitSupported.lean#L360).

> **[Stacks, Tag 0DKC].** Let `X` be a quasi-compact and quasi-separated scheme, let `T ⊆ X`
> be a closed subset such that `X \ T` is quasi-compact, and let `K ∈ D(𝒪_X)` be supported on `T`.
> The following are equivalent:
> 1. `K` is pseudo-coherent;
> 2. `K = hocolim Kₙ` where `Kₙ` is perfect, supported on `T`, and `τ_{≥-n}Kₙ ⟶ τ_{≥-n}K` is an
>    isomorphism for all `n`.
>
> The system is `F : ℕ ⥤ D(𝒪_X)`, indexed from `0`, its member `F.obj n` being the source's
> `K_{n+1}`; so the truncation condition at index `n` is in degree `-(n + 1)`. The maps
> `Kₙ ⟶ K` are the coprojections `c n` of the derived colimit
> (`CategoryTheory.Pretriangulated.IsHomotopyColimitWith`). The same statement is
> [Stacks, Tag 0DJP].

```lean
theorem isPseudoCoherent_iff_exists_isHomotopyColimitWith [CompactSpace X]
    [QuasiSeparatedSpace X] (T : Set X) (hT : IsClosed T) (hTc : IsCompact Tᶜ)
    (K : DerivedCategory X.Modules)
    (hK : Stacks.Cohomology.PushforwardRestriction.CohomologySupportedOn X.ringCatSheaf T K) :
    RingedSpace.IsPseudoCoherent (X := X.toRingedSpace) K ↔
      ∃ (F : ℕ ⥤ DerivedCategory X.Modules) (c : ∀ n, F.obj n ⟶ K),
        (∀ n, IsPerfect (X := X.toRingedSpace) (F.obj n)) ∧
          (∀ n, Stacks.Cohomology.PushforwardRestriction.CohomologySupportedOn X.ringCatSheaf T
            (F.obj n)) ∧
            (∀ n : ℕ,
              IsIso ((DerivedCategory.TStructure.t.truncGE (-((n : ℤ) + 1))).map (c n))) ∧
              IsHomotopyColimitWith F K c
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 75.18, Tag 0DKA](https://stacks.math.columbia.edu/tag/0DKA)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
