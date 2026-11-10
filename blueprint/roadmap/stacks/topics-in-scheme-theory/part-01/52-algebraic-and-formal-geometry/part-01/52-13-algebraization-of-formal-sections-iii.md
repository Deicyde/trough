---
declaration: section
origin: cited
lean: Stacks.Algebraization.adicLimit_allDegrees, Stacks.Algebraization.isIso_comparisonMap_of_sourceSheafDepthHypothesis, Stacks.Algebraization.HigherComplementTower.bijective_toTowerSections
statement: formalized
proof: formalized
---

# 52.13 Algebraization of formal sections, III

Section 52.13 of the Stacks Project, [Tag 0EIJ](https://stacks.math.columbia.edu/tag/0EIJ). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EG4, a proposition

[Tag 0EG4](https://stacks.math.columbia.edu/tag/0EG4) in the Stacks Project.

**`Stacks.Algebraization.adicLimit_allDegrees`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSectionsAlgebraization/AdicLimitTheorem.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSectionsAlgebraization/AdicLimitTheorem.lean#L152).

> **Stacks Project, Tag 0EG4.** Let `I ⊆ 𝔞` be ideals of a Noetherian ring `A`, let `F` be a
> coherent module on `U = Spec(A) ∖ V(𝔞)` and let `s ≥ 0`. Assume
>
> 1. `A` is `I`-adically complete and has a dualizing complex,
> 2. `Stacks.Algebraization.SourceSheafDepthHypothesis`: for `x ∈ U ∖ V(I)`, `depth(F_x) > s` or
>    `depth(F_x) + dim(𝒪_{closure {x}, z}) > cd(A, I) + s + 1` for all `z ∈ V(𝔞) ∩ closure {x}`,
> 3. `Stacks.Algebraization.SourceSerreOrDimensionHypothesis`: the restriction of `F` to
>    `U ∖ V(I)` is `(S_{s+1})`, or the difference of the maximal and minimal values of a dimension
>    function on `V(𝔞)` is at most `2`.
>
> Then the maps `H^i(U, F) → lim H^i(U, F/IⁿF)` are isomorphisms for `i < s`, and
> `colim_V H^s(V, F) → lim H^s(U, F/IⁿF)` is an isomorphism, the colimit being over the opens
> `V ⊆ U` containing `U ∩ V(I)`.
>
> Here `H^i(V, -)` is `Stacks.LocalCohomology.complementOpenCohomology`, the `i`-th right derived
> functor of the sections over `V` of `𝒪_U`-modules, read over `A`; the first map is the comparison
> induced by the quotient maps `F → F/IⁿF`; the second is the descent of
> `Stacks.Algebraization.nearVanishingCocone`, whose component at `V` is reduction modulo `Iⁿ` on
> `V` followed by the inverse of the restriction isomorphism `H^s(U, F/IⁿF) ≅ H^s(V, F/IⁿF)`.

```lean
theorem adicLimit_allDegrees
    (F : (complementZeroLocus A a : Scheme).Modules) [F.IsCoherent] (s : ℕ)
    (hcomplete : IsAdicComplete I A)
    (hdual : ∃ K : DerivedCategory (ModuleCat.{u} A), Dualizing.IsDualizingComplex K)
    (hdepth : SourceSheafDepthHypothesis A I a F s)
    (h3 : SourceSerreOrDimensionHypothesis A I a F s) :
    (∀ i : ℕ, i < s →
      IsIso (limit.lift (quotientSystemNearVanishing A I a F ⋙ complementOpenCohomology A a ⊤ i)
        ((complementOpenCohomology A a ⊤ i).mapCone
          (adicQuotientCone (idealSheafNearVanishing A I a) F)))) ∧
    IsIso (colimit.desc (nearVanishingCohomology A I a F s) (nearVanishingCocone A I a F s))
```

**`Stacks.Algebraization.isIso_comparisonMap_of_sourceSheafDepthHypothesis`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSectionsAlgebraization/DegreeZeroAdicLimit.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSectionsAlgebraization/DegreeZeroAdicLimit.lean#L213). The attribute's comment: “the case s = 0: the first assertion is empty there and the colim/lim assertion in degree 0 is IsIso (comparisonMap A I a F), by Proposition 0EG2 as in the source. Hypotheses (1) and (2) of the source are present, (2) at s = 0 in the source's shape; hypothesis (3) is absent because 0EG2 removes it. Every s, with every conclusion, is Stacks.Algebraization.adicLimit\_allDegrees in AdicLimitTheorem.lean”.

> **Stacks Project, Tag 0EG4 for `s = 0`.** Let `I ⊆ 𝔞` be ideals of a Noetherian ring `A` and
> let `F` be a coherent module on `U = Spec(A) ∖ V(𝔞)`. Assume `A` is `I`-adically complete and has
> a dualizing complex, and assume hypothesis (2) of the source at `s = 0`. Then
>
> `colim_V H^0(V, F) ⟶ lim H^0(U, F/IⁿF)`
>
> is an isomorphism, the colimit being over the opens `V ⊆ U` containing `U ∩ V(I)`; that map is
> `Stacks.Algebraization.comparisonMap A I 𝔞 F`.
>
> This is the proposition's `colim`/`lim` assertion in degree `s = 0`, the first assertion being
> empty for `s = 0`. It is the case the source disposes of by citing Proposition 0EG2, and the
> proof is that citation: hypothesis (2) at `s = 0` gives condition (2) of 0EG2 because the depth
> of a stalk at an associated point is zero. Hypothesis (3) of the source is absent, being the
> condition 0EG2 removes.

```lean
public theorem isIso_comparisonMap_of_sourceSheafDepthHypothesis [F.IsCoherent] (hIa : I ≤ a)
    (hcomplete : IsAdicComplete I A)
    (hdual : ∃ K : DerivedCategory (ModuleCat.{u} A), Dualizing.IsDualizingComplex K)
    (hdepth : SourceSheafDepthHypothesis A I a F 0) :
    IsIso (comparisonMap A I a F)
```

## Tag 0EKM, a lemma

[Tag 0EKM](https://stacks.math.columbia.edu/tag/0EKM) in the Stacks Project.

**`Stacks.Algebraization.HigherComplementTower.bijective_toTowerSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/ComplementFormalFunctionsHigher.lean, line 398](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/ComplementFormalFunctionsHigher.lean#L398). The attribute's comment: “with H^i(U, -) the cohomology of derived sections on U = Spec(A) ∖ V(𝔞) in the Čech model of a finite generating family of 𝔞, and the inverse limit taken as the compatible sequences of the tower of the H^i(U, (M/fⁿM)~)”.

> Let `A` be a Noetherian ring, let `f ∈ 𝔞` be an element of a finitely generated ideal of `A`,
> let `M` be a finite `A`-module and let `s ≥ 0`. Assume `A` is `f`-adically complete and `H^k_𝔞(M)`
> is annihilated by a power of `f` for `k ≤ s + 1`. Then with `U = Spec(A) ∖ V(𝔞)` the canonical map
> `H^i(U, M̃) ⟶ lim_n H^i(U, (M/fⁿM)̃)` is a bijection for every `i < s`.
>
> In degree zero the source is complete by the extension argument of Stacks 0EII; in a positive
> degree `i < s` it equals `H^{i+1}_𝔞(M)`, which is killed by a power of `f` because `i + 1 ≤ s + 1`,
> and a module killed by a power of `f` is complete. In both cases `H^{i+1}(U, M̃) = H^{i+2}_𝔞(M)` is
> killed by a power of `f` because `i + 2 ≤ s + 1`.

```lean
theorem bijective_toTowerSections {A : Type u} [CommRing A] [IsNoetherianRing A]
    {I : Ideal A} (hI : I.FG) {r : ℕ} (fam : Fin r → A)
    (hfam : Ideal.span (Set.range fam) = I) (f : A) (hf : f ∈ I) (M : ModuleCat.{u} A)
    [Module.Finite A M] [IsAdicComplete (Ideal.span {f}) A] (s : ℕ)
    (hann : ∀ k : ℕ, k ≤ s + 1 →
      ∃ c : ℕ, ∀ x : localCohomologyModule A I hI M (k : ℤ), f ^ c • x = 0)
    (i : ℕ) (hi : i < s) :
    Function.Bijective (toTowerSections fam f M (i : ℤ))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 52.13, Tag 0EIJ](https://stacks.math.columbia.edu/tag/0EIJ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
