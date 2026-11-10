---
declaration: section
origin: cited
lean: Stacks.ProjectiveBundleDeRham.bijective_sum_cup_projectiveBundle, AlgebraicGeometry.SheafOfModules.iterate_deRhamClassMorphism, AlgebraicGeometry.DeRhamLerayHirsch.ι_lerayHirschPowerMorphism, AlgebraicGeometry.DeRhamLerayHirsch.ι_lerayHirschPowerMorphism_zero, AlgebraicGeometry.DeRhamLerayHirsch.lerayHirschPowerMorphism_comp_classDirectImageEndo, AlgebraicGeometry.DeRhamLerayHirsch.isIso_projectiveBundleLerayHirschMorphism, AlgebraicGeometry.DeRhamLerayHirsch.isIso_biprodDesc_projectiveBundleLerayHirschMorphism
statement: formalized
proof: formalized
---

# 50.14 Projective space bundle formula

Section 50.14 of the Stacks Project, [Tag 0FMS](https://stacks.math.columbia.edu/tag/0FMS). 2 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FMT, a proposition

[Tag 0FMT](https://stacks.math.columbia.edu/tag/0FMT) in the Stacks Project.

**`Stacks.ProjectiveBundleDeRham.bijective_sum_cup_projectiveBundle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LerayHirsch/ProjectiveBundleFormula.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LerayHirsch/ProjectiveBundleFormula.lean#L57). The attribute's comment: “the projective bundle formula: for E locally free of constant rank r on X over S and p : P = P(E) -> X, the map (+)\_\{i = 0, ..., r - 1} H^*\_dR(X/S) -> H^*\_dR(P/S), (a\_i) |-> sum c\_1^dR(O\_P(1))^i cup p^*(a\_i), is an isomorphism, i.e. bijective in every degree k”.

> **[Stacks, Tag 0FMT], the projective bundle formula for de Rham cohomology.** Let
> `g : X ⟶ S` be a morphism of schemes, `ℰ` a quasi-coherent `𝒪_X`-module, locally free of constant
> rank `r`, and `p : P = 𝐏(ℰ) ⟶ X` its projective bundle. Then for every `k` the map
> `⨁_{i = 0}^{r - 1} H^{k - 2i}_{dR}(X/S) ⟶ H^k_{dR}(P/S)`,
> `(a_0, …, a_{r-1}) ↦ ∑_i c₁^{dR}(𝒪_P(1))^i ∪ p^*(a_i)`, is bijective.

```lean
theorem bijective_sum_cup_projectiveBundle (r : ℕ)
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E r] (k : ℤ) :
    Function.Bijective (fun a : ∀ i : Fin r, SheafOfModules.deRhamCohomology
        (Scheme.Hom.deRhamAlgebras g)
        (SheafOfModules.deRhamDifferential (Scheme.Hom.deRhamAlgebras g))
        (k - ((2 * (i : ℕ) : ℕ) : ℤ)) =>
      ∑ i : Fin r, (eqToHom (congrArg (SheafOfModules.deRhamCohomology
          (Scheme.Hom.deRhamAlgebras (projectiveBundleToBase X E ≫ g))
          (SheafOfModules.deRhamDifferential
            (Scheme.Hom.deRhamAlgebras (projectiveBundleToBase X E ≫ g))))
          (add_sub_cancel ((2 * (i : ℕ) : ℕ) : ℤ) k))).hom
        (SheafOfModules.deRhamCohomologyCup _ _ ((2 * (i : ℕ) : ℕ) : ℤ)
          (k - ((2 * (i : ℕ) : ℕ) : ℤ))
          (DeRhamLerayHirsch.classPow (projectiveBundleToBase X E ≫ g) 2
            (DeRhamLerayHirsch.projectiveBundleChernClass g E) i)
          (DeRhamKatzOdaCech.deRhamPullbackModule (projectiveBundleToBase X E) g
            (k - ((2 * (i : ℕ) : ℕ) : ℤ)) (a i))))
```

## Tag 0FUN, a remark

[Tag 0FUN](https://stacks.math.columbia.edu/tag/0FUN) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.iterate_deRhamClassMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/DifferentialGradedAlgebra/ClassMorphismComposition.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/DifferentialGradedAlgebra/ClassMorphismComposition.lean#L243). The attribute's comment: “xi'[2(t-1)] o ... o xi'[2] o xi' is the morphism of Remark 0FU7 attached to xi^t; stated for every class xi of every degree d, the remark's case being xi = c\_1^dR(O\_P(1)), d = 2”.

> **Stacks Project, Tag 0FUN: the composite `ξ'[d(t - 1)] ∘ ⋯ ∘ ξ'[d] ∘ ξ' : Ω^• ⟶ Ω^•[dt]` is
> the morphism of Remark 0FU7 attached to `ξ^t`**, for `ξ ∈ H^d_{dR}`; Remark 0FUN states it for
> `ξ = c₁^{dR}(𝒪_P(1))` and `d = 2`.

```lean
theorem iterate_deRhamClassMorphism (d : ℕ) (ξ : deRhamCohomology B D (d : ℤ)) (t : ℕ) :
    ShiftedHom.iterate d (deRhamClassMorphism B D d ξ) t =
      deRhamClassMorphism B D ((d * t : ℕ) : ℤ) (deRhamCohomologyPow B D d ξ t)
```

**`AlgebraicGeometry.DeRhamLerayHirsch.ι_lerayHirschPowerMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LerayHirsch/PowerSummands.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LerayHirsch/PowerSummands.lean#L138). The attribute's comment: “the restriction of xi~ to the summand Omega\_\{X/S}[-2t] is Rp\_*xi'[-2] o ... o Rp\_*xi'[-2t] o c\_\{P/X}[-2t]; stated for every morphism p : P -> X over S, every class xi of every degree d and every number r of summands”.

> **The summand `t` of `ξ̃` is `Rf_*ξ'[-d] ∘ ⋯ ∘ Rf_*ξ'[-dt] ∘ c[-dt]`.**

```lean
theorem ι_lerayHirschPowerMorphism (t : Fin r) :
    biproduct.ι (fun t : Fin r => (deRhamObject g)⟦-((d * (t : ℕ) : ℕ) : ℤ)⟧) t ≫
        lerayHirschPowerMorphism f g d ξ r =
      (deRhamDirectImageMap f g)⟦-((d * (t : ℕ) : ℕ) : ℤ)⟧' ≫
        ShiftedHom.negIterate d (classDirectImageEndo f g d ξ) t
```

**`AlgebraicGeometry.DeRhamLerayHirsch.ι_lerayHirschPowerMorphism_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LerayHirsch/PowerSummands.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LerayHirsch/PowerSummands.lean#L150). The attribute's comment: “the arrow of xi~ for t = 0 is the canonical map c\_\{P/X} of Section 07HX; stated for every morphism p : P -> X over S and every class xi”.

> **The summand `t = 0` of `ξ̃` is the canonical map `c : Ω^•_{Y/S} ⟶ Rf_*Ω^•_{X/S}`**, read on
> `Ω^•_{Y/S}[0] = Ω^•_{Y/S}`.

```lean
theorem ι_lerayHirschPowerMorphism_zero (hr : 0 < r) :
    biproduct.ι (fun t : Fin r => (deRhamObject g)⟦-((d * (t : ℕ) : ℕ) : ℤ)⟧) ⟨0, hr⟩ ≫
        lerayHirschPowerMorphism f g d ξ r =
      (shiftFunctorZero' _ (-((d * 0 : ℕ) : ℤ)) (by simp)).hom.app (deRhamObject g) ≫
        deRhamDirectImageMap f g
```

**`AlgebraicGeometry.DeRhamLerayHirsch.lerayHirschPowerMorphism_comp_classDirectImageEndo`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LerayHirsch/PowerSummands.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LerayHirsch/PowerSummands.lean#L191). The attribute's comment: “the square K -> M[2], Rp\_*Omega\_\{P/S} -> Rp\_*Omega\_\{P/S}[2] commutes: Rp\_*xi' o xi~|\_K = (xi~|\_M)[2] o id; stated for every morphism p : P -> X over S, every class xi of every degree d and every number r of summands”.

> **The square of Remark 0FUN commutes**: `Rf_*ξ' ∘ ξ̃|_K = (ξ̃|_M)[d] ∘ id`.

```lean
theorem lerayHirschPowerMorphism_comp_classDirectImageEndo :
    powerSummandsInitι g d r ≫ lerayHirschPowerMorphism f g d ξ r ≫ classDirectImageEndo f g d ξ =
      powerSummandsInitIso g d r ≫
        (powerSummandsTailι g d r ≫ lerayHirschPowerMorphism f g d ξ r)⟦(d : ℤ)⟧'
```

**`AlgebraicGeometry.DeRhamLerayHirsch.isIso_projectiveBundleLerayHirschMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LerayHirsch/ProjectiveBundleLerayHirsch.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LerayHirsch/ProjectiveBundleLerayHirsch.lean#L64). The attribute's comment: “in the situation of Proposition 0FMT (E locally free of constant rank r on X, X -> S, p : P = P(E) -> X), the map xi~ : (+)\_\{t = 0, ..., r-1} Omega\_\{X/S}[-2t] -> Rp\_*Omega\_\{P/S} attached to the classes c\_1^dR(O\_P(1))^t is an isomorphism in D(X, (X -> S)^\{-1}O\_S)”.

> **Stacks Project, Remark 0FUN: the Leray--Hirsch morphism of a projective bundle is an
> isomorphism.** For `ℰ` locally free of constant rank `r` and `p : P = 𝐏(ℰ) ⟶ X`, the morphism
> `ξ̃ = ⨁_t ξ̃_t[-2t] : ⨁_{0 ≤ t < r} Ω^•_{X/S}[-2t] ⟶ Rp_*Ω^•_{P/S}` attached to the classes
> `c₁^{dR}(𝒪_P(1))^t ∈ H^{2t}_{dR}(P/S)` is an isomorphism in `D(X, (X ⟶ S)^{-1}𝒪_S)`.

```lean
theorem isIso_projectiveBundleLerayHirschMorphism :
    IsIso (projectiveBundleLerayHirschMorphism g E r)
```

**`AlgebraicGeometry.DeRhamLerayHirsch.isIso_biprodDesc_projectiveBundleLerayHirschMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LerayHirsch/ProjectiveBundleLerayHirsch.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LerayHirsch/ProjectiveBundleLerayHirsch.lean#L88). The attribute's comment: “with M = (+)\_\{t = 1, ..., r-1} Omega\_\{X/S}[-2t], the map c\_\{P/X} (+) xi~|\_M : Omega\_\{X/S} (+) M -> Rp\_*Omega\_\{P/S} is an isomorphism; stated for r >= 1, the remark's arrow for t = 0 presupposing it (for r = 0 and X nonempty the target is 0 and the source is not)”.

> **Stacks Project, Remark 0FUN: `c_{P/X} ⊕ ξ̃|_M` is an isomorphism.** For `ℰ` locally free of
> constant rank `r ≥ 1` and `M = ⨁_{1 ≤ t < r} Ω^•_{X/S}[-2t]`, the morphism
> `c_{P/X} ⊕ ξ̃|_M : Ω^•_{X/S} ⊕ M ⟶ Rp_*Ω^•_{P/S}` is an isomorphism.

```lean
theorem isIso_biprodDesc_projectiveBundleLerayHirschMorphism (hr : 0 < r) :
    IsIso (biprod.desc (deRhamDirectImageMap (projectiveBundleToBase X E) g)
      (powerSummandsTailι g 2 r ≫ projectiveBundleLerayHirschMorphism g E r))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 50.14, Tag 0FMS](https://stacks.math.columbia.edu/tag/0FMS)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
