---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.module_finite_compactlySupportedCohomologyGroup_of_isConstructible, Stacks.EtaleCohomology.isFiniteTypeLocallyConstantModuleSheaf_rightDerived_of_smooth_of_isProper
statement: formalized
proof: formalized
---

# 63.15 Applications

Section 63.15 of the Stacks Project, [Tag 0GLG](https://stacks.math.columbia.edu/tag/0GLG). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GLH, a lemma

[Tag 0GLH](https://stacks.math.columbia.edu/tag/0GLH) in the Stacks Project.

**`Stacks.EtaleCohomology.module_finite_compactlySupportedCohomologyGroup_of_isConstructible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/CompactSupportFinitenessAlgClosed.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/CompactSupportFinitenessAlgClosed.lean#L54). The attribute's comment: “both cases: K in D+\_\{tors,c}(X, Λ), and K in D\_c(X, Λ) when Λ is torsion (m = 0 in Λ for some m > 0; H^i\_c on D(X, Λ) is compactlySupportedCohomologyGroupUnbounded); H^i\_c through any compactification j of X over k”. References: SGA 4 XVII (5.3.8), “special case”.

> Let `k` be an algebraically closed field, `X` a separated scheme of finite type over `k` (a
> scheme of a big étale site `B`, with structure morphism `f`), `j` a compactification of `X` over
> `k`, through which `Hⁱ_c(X, -)` is formed, and `Λ` a Noetherian ring.
> 1. If `K ∈ D⁺(X_étale, Λ)` has constructible torsion cohomology sheaves, every `Hⁱ_c(X, K)` is a
>    finite `Λ`-module.
> 2. If `Λ` is torsion and `K ∈ D(X_étale, Λ)` has constructible cohomology sheaves, every
>    `Hⁱ_c(X, K)` is a finite `Λ`-module.

```lean
theorem module_finite_compactlySupportedCohomologyGroup_of_isConstructible
    {k : Type u} [Field k] [IsAlgClosed k] (B : BigEtaleSite.{u}) (X : B.Scheme)
    (f : X.obj ⟶ Spec (.of k)) [IsSeparated f] [LocallyOfFiniteType f] [QuasiCompact f]
    (j : CompactificationOf (Over.mk f)) (Λ : Type) [CommRing Λ] [IsNoetherianRing Λ] :
    (∀ K : DerivedCategory.Plus (EtaleModules.{u, 0} Λ X.obj),
      (∀ q : ℤ, IsBigSiteConstructibleEtaleModule B X Λ
          ((DerivedCategory.Plus.homologyFunctor _ q).obj K) ∧
        IsTorsionEtaleModule Λ X.obj ((DerivedCategory.Plus.homologyFunctor _ q).obj K)) →
      ∀ i : ℤ, Module.Finite Λ ((compactlySupportedCohomologyGroup.{u, 0} k f j Λ i).obj K)) ∧
    ((∃ m : ℕ, 0 < m ∧ (m : Λ) = 0) →
      ∀ K : DerivedCategory (EtaleModules.{u, 0} Λ X.obj),
        (∀ q : ℤ, IsBigSiteConstructibleEtaleModule B X Λ
          ((DerivedCategory.homologyFunctor _ q).obj K)) →
        ∀ i : ℤ, Module.Finite Λ
          ((compactlySupportedCohomologyGroupUnbounded.{u, 0} k f j Λ i).obj K))
```

## Tag 0GLI, a proposition

[Tag 0GLI](https://stacks.math.columbia.edu/tag/0GLI) in the Stacks Project.

**`Stacks.EtaleCohomology.isFiniteTypeLocallyConstantModuleSheaf_rightDerived_of_smooth_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmoothProperHigherDirectImageLocallyConstant.lean, line 331](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmoothProperHigherDirectImageLocallyConstant.lean#L331). References: SGA 1 XIII (2.9), “special case”; SGA 4 XVI (2.1), “special case”; SGA 4 XVI (2.2), “Abelian torsion case”; SGA 7 I (0.1.5), “special case”.

> Let `f : X ⟶ S` be a smooth proper morphism of schemes, let `Λ` be a Noetherian ring and let
> `F` be a finite type, locally constant sheaf of `Λ`-modules on
> `X_étale` such that for every geometric point `x̄` of `X` the stalk `F_x̄` is annihilated by an
> integer `n > 0` prime to the residue characteristic of `x̄`. Then `Rⁱ f_* F` is a finite type,
> locally constant sheaf of `Λ`-modules on `S_étale` for every `i`.
>
> Here `Rⁱ f_*` is the `i`-th right derived functor of the direct image of sheaves of `Λ`-modules
> for the small étale topologies, `i : ℕ` (for `i < 0` it is zero); the stalk `F_x̄` is that of the
> underlying abelian sheaf, and "prime to the residue characteristic" reads `n` coprime to the
> characteristic of the residue field of `x̄`, a condition void in characteristic zero.

```lean
theorem isFiniteTypeLocallyConstantModuleSheaf_rightDerived_of_smooth_of_isProper
    {X S : Scheme.{u}} (f : X ⟶ S) [Smooth f] [IsProper f] (Λ : Type) [CommRing Λ]
    [IsNoetherianRing Λ] (F : EtaleModules.{u, 0} Λ X)
    (hF : IsFiniteTypeLocallyConstantModuleSheaf.{u, u + 1, 0} X.smallEtaleTopology Λ F)
    (htors : ∀ x : GeometricPoint X, ∃ n : ℕ, 0 < n ∧
      (ringChar x.residueField = 0 ∨ n.Coprime (ringChar x.residueField)) ∧
      ∀ a : (smallEtaleStalkAb x.hom).obj ((etaleModuleForget Λ X).obj F), n • a = 0)
    (i : ℕ) :
    IsFiniteTypeLocallyConstantModuleSheaf.{u, u + 1, 0} S.smallEtaleTopology Λ
      (((etaleModuleDirectImage.{u, 0} Λ f).rightDerived i).obj F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 63.15, Tag 0GLG](https://stacks.math.columbia.edu/tag/0GLG)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
