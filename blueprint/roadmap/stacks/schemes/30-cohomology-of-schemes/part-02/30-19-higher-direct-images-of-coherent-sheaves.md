---
declaration: section
origin: cited
lean: AlgebraicGeometry.ProperCoherenceWitness.higherDirectImageIsCoherent, AlgebraicGeometry.ProperCoherenceWitness.isCoherent_pushforward, AlgebraicGeometry.ProperCoherenceWitness.moduleFinite_cohomology, Stacks.AlgebraicGeometry.GradedProperCohomology.moduleFinite_gradedCohomologySum_and_exists_isZero_pieceTwistCohomology
statement: formalized
proof: formalized
---

# 30.19 Higher direct images of coherent sheaves

Section 30.19 of the Stacks Project, [Tag 02O3](https://stacks.math.columbia.edu/tag/02O3). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02O5, a proposition

[Tag 02O5](https://stacks.math.columbia.edu/tag/02O5) in the Stacks Project.

**`AlgebraicGeometry.ProperCoherenceWitness.higherDirectImageIsCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProperCoherenceWitness/ChowStalk.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProperCoherenceWitness/ChowStalk.lean#L202).

> **Coherence of higher direct images.** Let `S` be a locally Noetherian scheme, let
> `f : X ⟶ S` be proper and let `F` be a coherent `𝒪_X`-module. Then `R ⁱ f_* F` is a coherent
> `𝒪_S`-module for every `i ≥ 0`.

```lean
theorem higherDirectImageIsCoherent : HigherDirectImageIsCoherent.{u}
```

**`AlgebraicGeometry.ProperCoherenceWitness.isCoherent_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProperCoherenceWitness/ChowStalk.lean, line 213](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProperCoherenceWitness/ChowStalk.lean#L213). References: EGA III (2.2.5), “partial”.

> **Coherence of the direct image.** For `f : X ⟶ S` proper onto a locally Noetherian base and
> `F` coherent, `f_* F` is coherent.

```lean
theorem isCoherent_pushforward {X S : Scheme.{u}} (f : X ⟶ S) [IsLocallyNoetherian S]
    [IsProper f] (F : X.Modules) [F.IsCoherent] :
    ((Scheme.Modules.pushforward f).obj F).IsCoherent
```

## Tag 02O6, a lemma

[Tag 02O6](https://stacks.math.columbia.edu/tag/02O6) in the Stacks Project.

**`AlgebraicGeometry.ProperCoherenceWitness.moduleFinite_cohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProperCoherenceWitness/ChowStalk.lean, line 223](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProperCoherenceWitness/ChowStalk.lean#L223). References: EGA III (3.2.3).

> **Finiteness of cohomology.** Let `S = Spec A` with `A` Noetherian, let `f : X ⟶ S` be proper
> and let `F` be a coherent `𝒪_X`-module. Then `Hⁱ(X, F)` is a finite `A`-module for every `i ≥ 0`.
> Here the base is an affine locally Noetherian scheme and `A` is its ring of global sections.

```lean
theorem moduleFinite_cohomology {X S : Scheme.{u}} (f : X ⟶ S) [IsProper f] [IsAffine S]
    [IsLocallyNoetherian S] (F : X.Modules) [F.IsCoherent] (i : ℕ) :
    Module.Finite Γ(S, ⊤) ((ModuleCat.restrictScalars f.appTop.hom).obj
      (((moduleGlobalSections X).rightDerived i).obj F))
```

## Tag 0897, a lemma

[Tag 0897](https://stacks.math.columbia.edu/tag/0897) in the Stacks Project.

**`Stacks.AlgebraicGeometry.GradedProperCohomology.moduleFinite_gradedCohomologySum_and_exists_isZero_pieceTwistCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GradedProperCohomology/FiniteGradedCohomology.lean, line 229](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GradedProperCohomology/FiniteGradedCohomology.lean#L229). The attribute's comment: “both parts, at the hypotheses of the source: A Noetherian, B a finitely generated graded A-algebra, f : X → Spec A proper, F a quasi-coherent graded f^* B-tilde-module of finite type, and L ample invertible in part (2); (1) is finiteness of ⨁\_n H^p(X, F\_n) over B for the degreewise B-action, (2) is H^p(X, F\_n ⊗ L^d) = 0 for p > 0, d ≥ d\_0 and every degree n, which is H^p(X, F ⊗ L^d) = 0 since cohomology on X commutes with direct sums”. References: SGA 2 XII (5.8), “(i), special case”.

> **[Stacks, Tag 0897].** Let `A` be a Noetherian ring, `B` a finitely generated graded
> `A`-algebra, `f : X ⟶ Spec A` a proper morphism and `𝓑 = f^* B̃`. Let `F` be a quasi-coherent
> graded `𝓑`-module of finite type. Then
>
> 1. for every `p` the graded `B`-module `Hᵖ(X, F) = ⨁ₙ Hᵖ(X, Fₙ)` is a finite `B`-module, and
> 2. if `L` is an ample invertible `𝒪_X`-module there is a `d₀` with
>    `Hᵖ(X, Fₙ ⊗ L^{⊗d}) = 0` for all `p > 0` and all `d ≥ d₀`, uniformly in the graded degree
>    `n`.
>
> The `B`-module structure in (1) is `HomogeneousSections.gradedCohomologyModule` for the
> homogeneous-sections datum of `𝓑 = f^* B̃`: a homogeneous `b ∈ 𝒜ₖ` carries the degree-`n` summand
> to the degree-`n + k` summand by `Hᵖ(X, −)` of multiplication by the global section of `𝓑ₖ` that
> `b` names.

```lean
theorem moduleFinite_gradedCohomologySum_and_exists_isZero_pieceTwistCohomology
    [IsNoetherianRing A] [Algebra.FiniteType A B] [_root_.AlgebraicGeometry.IsProper f]
    (F : _root_.SheafOfModules.GradedModule.{u, u, u} (pullbackGradedAlg 𝒜 f))
    (hqc : ∀ n : ℤ, (pieceModule F n).IsQuasicoherent) (hft : F.IsFiniteType) :
    (letI := (pullbackHomogeneousSections 𝒜 f).gradedCohomologyModule F
     ∀ p : ℕ, Module.Finite B (gradedCohomologySum F p)) ∧
      ∀ (L : X.Modules) (_ : IsInvertibleModule X L), IsAmple X L →
        ∃ d₀ : ℕ, ∀ d : ℕ, d₀ ≤ d → ∀ p : ℕ, 0 < p → ∀ n : ℤ,
          IsZero (cohomologyOf X p (pieceTwist F L n (d : ℤ)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 30.19, Tag 02O3](https://stacks.math.columbia.edu/tag/02O3)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
