---
declaration: section
origin: cited
lean: CochainComplex.toLimitOfTruncGEResolutions, Stacks.Cohomology.quasiIso_to_limit_of_truncGE_resolutions, Stacks.Cohomology.InverseLimits.homology_isLimit_of_local_rlim_vanishing, Stacks.Cohomology.InverseLimits.homology_limit_projection_isIso_of_local_rlim_vanishing
statement: formalized
proof: formalized
---

# 21.24 Producing K-injective resolutions

Section 21.24 of the Stacks Project, [Tag 070N](https://stacks.math.columbia.edu/tag/070N). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 070P, an equation

[Tag 070P](https://stacks.math.columbia.edu/tag/070P) in the Stacks Project.

**`CochainComplex.toLimitOfTruncGEResolutions`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/IntoCandidateKInjective.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/IntoCandidateKInjective.lean#L55).

> **Stacks Project, Tag 070P**, the displayed arrow `ℱ• → ℐ•`. Given an inverse system `𝓘` of
> cochain complexes and maps `f n : τ_{≥ -n} K ⟶ 𝓘ₙ` commuting with the canonical truncation maps
> of `K`, this is the induced map `K ⟶ lim 𝓘`. For the tower of Stacks 070F the target is the
> candidate K-injective complex of Stacks 070L.

```lean
def toLimitOfTruncGEResolutions (𝓘 : ℕᵒᵖ ⥤ CochainComplex A ℤ) [HasLimit 𝓘]
    (K : CochainComplex A ℤ) (f : ∀ n : ℕ, K.truncGE (-(n : ℤ)) ⟶ 𝓘.obj ⟨n⟩)
    (hladder : ∀ n : ℕ, K.πTruncGE (-((n + 1 : ℕ) : ℤ)) ≫ f (n + 1) ≫
      𝓘.map (homOfLE (Nat.le_succ n)).op = K.πTruncGE (-(n : ℤ)) ≫ f n) :
    K ⟶ limit 𝓘
```

## Tag 070Q, a lemma

[Tag 070Q](https://stacks.math.columbia.edu/tag/070Q) in the Stacks Project.

**`Stacks.Cohomology.quasiIso_to_limit_of_truncGE_resolutions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/KInjectiveTowerQuasiIso.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/KInjectiveTowerQuasiIso.lean#L127).

> Let `O` be a sheaf of rings on a site, let `K` be a cochain complex of `O`-modules, and let
> `𝓘` be an inverse system of K-injective complexes with degreewise split-epimorphic transition
> maps resolving the truncations `τ_{≥ -n} K` compatibly with the canonical maps
> `K ⟶ τ_{≥ -n} K`. If a subset `B` of the objects of the site covers every object and
> `H^p(V, H^q(K)) = 0` for every `V ∈ B`, every `p > d` and every `q < 0`, then the canonical map
> `γ : K ⟶ lim 𝓘` is a quasi-isomorphism.

```lean
theorem quasiIso_to_limit_of_truncGE_resolutions {C : Type u} [Category.{u} C]
    {J : GrothendieckTopology C} (O : Sheaf J RingCat.{u})
    [HasSheafify J AddCommGrpCat.{u}]
    [J.WEqualsLocallyBijective AddCommGrpCat.{u}]
    [EnoughInjectives (SheafOfModules.{u} O)]
    (K : CochainComplex (SheafOfModules.{u} O) ℤ)
    (𝓘 : ℕᵒᵖ ⥤ CochainComplex (SheafOfModules.{u} O) ℤ)
    (f : ∀ n : ℕ, K.truncGE (-(n : ℤ)) ⟶ 𝓘.obj ⟨n⟩)
    (hf : ∀ n : ℕ, QuasiIso (f n))
    (hcompat : ∀ n : ℕ,
      K.πTruncGE (-((n + 1 : ℕ) : ℤ)) ≫ f (n + 1) ≫ 𝓘.map (homOfLE (Nat.le_succ n)).op =
        K.πTruncGE (-(n : ℤ)) ≫ f n)
    (h𝓘 : ∀ n : ℕ, (𝓘.obj ⟨n⟩).IsKInjective)
    (hsplit : ∀ (n : ℕ) (i : ℤ), IsSplitEpi ((𝓘.map (homOfLE (Nat.le_succ n)).op).f i))
    [HasLimit 𝓘] (γ : K ⟶ limit 𝓘)
    (hγ : ∀ n : ℕ, γ ≫ limit.π 𝓘 ⟨n⟩ = K.πTruncGE (-(n : ℤ)) ≫ f n)
    (B : Set C) (d : ℕ)
    (hB : ∀ U : C, ∃ 𝒰 : PreZeroHypercover.{u} U, 𝒰.sieve₀ ∈ J U ∧ ∀ i, B (𝒰.X i))
    (hvan : ∀ V : C, B V → ∀ p : ℕ, d < p → ∀ q : ℤ, q < 0 →
      IsZero (moduleCohomology O V p
        ((DerivedCategory.homologyFunctor (SheafOfModules.{u} O) q).obj
          (DerivedCategory.Q.obj K)))) :
    QuasiIso γ
```

## Tag 08CT, a lemma

[Tag 08CT](https://stacks.math.columbia.edu/tag/08CT) in the Stacks Project.

**`Stacks.Cohomology.InverseLimits.homology_isLimit_of_local_rlim_vanishing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/CohomologyOfInverseLimits.lean, line 536](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/CohomologyOfInverseLimits.lean#L536). The attribute's comment: “canonical cohomology-limit comparison”.

> **Stacks 08CT.** The canonical cone from the degree-`m` cohomology of the termwise
> inverse limit of an inverse system of complexes of modules on a ringed site to the
> degree-`m` cohomologies is a limit cone, provided the first derived limits of the sections
> vanish in degrees `m - 2` and `m - 1` and on the degree `m - 1` cohomology over a generating
> family, and the degree-`m` cohomology of sections is constant from stage `n₀` on.

```lean
public theorem homology_isLimit_of_local_rlim_vanishing
    (X : AlgebraicGeometry.RingedSite.{u, v, w})
    [HasSheafify X.J AddCommGrpCat.{t}]
    [X.J.WEqualsLocallyBijective AddCommGrpCat.{t}]
    (F : ℕᵒᵖ ⥤ CochainComplex (SheafOfModules.{t}
      (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ)
    (m : ℤ) (B : Set X.C) (hB : X.J.HasEnoughObjects (· ∈ B))
    (hneg2 : ∀ U ∈ B, IsZero (Rlim.firstDerivedLimit
      (F ⋙ sectionsComplexFunctor (Stacks.SheafOfModules.Tensor.ringSheaf X.O) U ⋙
        HomologicalComplex.eval Ab.{t} (ComplexShape.up ℤ) (m - 2))))
    (hneg1 : ∀ U ∈ B, IsZero (Rlim.firstDerivedLimit
      (F ⋙ sectionsComplexFunctor (Stacks.SheafOfModules.Tensor.ringSheaf X.O) U ⋙
        HomologicalComplex.eval Ab.{t} (ComplexShape.up ℤ) (m - 1))))
    (hHneg1 : ∀ U ∈ B, IsZero (Rlim.firstDerivedLimit
      (F ⋙ sectionsComplexFunctor (Stacks.SheafOfModules.Tensor.ringSheaf X.O) U ⋙
        HomologicalComplex.homologyFunctor Ab.{t} (ComplexShape.up ℤ) (m - 1))))
    (n₀ : ℕ)
    (hstable : ∀ U ∈ B, ∀ (n : ℕ) (hn : n₀ ≤ n), IsIso
      ((HomologicalComplex.homologyFunctor Ab.{t} (ComplexShape.up ℤ) m).map
        ((sectionsComplexFunctor (Stacks.SheafOfModules.Tensor.ringSheaf X.O) U).map
          (F.map (homOfLE hn).op)))) :
    Nonempty (IsLimit
      ((HomologicalComplex.homologyFunctor
        (SheafOfModules.{t} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
        (ComplexShape.up ℤ) m).mapCone (limit.cone F)))
```

**`Stacks.Cohomology.InverseLimits.homology_limit_projection_isIso_of_local_rlim_vanishing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/CohomologyOfInverseLimits.lean, line 588](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/CohomologyOfInverseLimits.lean#L588). The attribute's comment: “projection to a stable stage”.

> **Stacks 08CT.** The limit of the degree-`m` cohomology sheaves of an inverse system of
> complexes of modules on a ringed site projects isomorphically to any stage from which the
> degree-`m` cohomology of sections over a generating family is constant.

```lean
public theorem homology_limit_projection_isIso_of_local_rlim_vanishing
    (X : AlgebraicGeometry.RingedSite.{u, v, w})
    [HasSheafify X.J AddCommGrpCat.{t}]
    [X.J.WEqualsLocallyBijective AddCommGrpCat.{t}]
    (F : ℕᵒᵖ ⥤ CochainComplex (SheafOfModules.{t}
      (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ)
    (m : ℤ) (B : Set X.C) (hB : X.J.HasEnoughObjects (· ∈ B)) (n₀ : ℕ)
    (hstable : ∀ U ∈ B, ∀ (n : ℕ) (hn : n₀ ≤ n), IsIso
      ((HomologicalComplex.homologyFunctor Ab.{t} (ComplexShape.up ℤ) m).map
        ((sectionsComplexFunctor (Stacks.SheafOfModules.Tensor.ringSheaf X.O) U).map
          (F.map (homOfLE hn).op)))) :
    IsIso (limit.π (F ⋙ HomologicalComplex.homologyFunctor
      (SheafOfModules.{t} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
      (ComplexShape.up ℤ) m) (op n₀))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.24, Tag 070N](https://stacks.math.columbia.edu/tag/070N)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
