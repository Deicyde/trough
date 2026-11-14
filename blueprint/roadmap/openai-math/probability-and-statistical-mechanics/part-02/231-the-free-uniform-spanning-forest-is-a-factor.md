---
declaration: section
origin: cited
lean: OAI.Problem336AdditiveD139.finite_strongly_rayleigh_response, OAI.Problem336AdditiveD139.strongly_rayleigh_group_factor, OAI.Problem336AdditiveD139.finite_positive_contraction_dpp_is_strongly_rayleigh, OAI.Problem336AdditiveD139.countable_positive_contraction_dpp_exists_unique, OAI.Problem336AdditiveD139.invariant_positive_contraction_dpp_factor, OAI.Problem336AdditiveD139.translation_invariant_kernel_dpp_factor, OAI.Problem336.fusf_is_factor_iid
statement: formalized
proof: formalized
---

# 231. The free uniform spanning forest is a factor of IID

1 manuscript and 7 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

On every infinite connected locally finite simple unweighted graph, the free uniform spanning forest is a factor of independent vertex labels, by one isomorphism-equivariant rule using no root. Translation-invariant strongly Rayleigh binary processes on every countable group, including invariant determinantal processes with Hermitian positive-contraction kernels, are also factors of IID.

## The free uniform spanning forest is a factor of IID

We prove that the free uniform spanning forest is a factor of IID on every infinite connected locally finite simple unweighted graph. One Borel rule works for all such graphs and uses no root, answering affirmatively the general factor question for unimodular random graphs. We also show that every translation-invariant strongly Rayleigh process indexed by a countable group is a factor of IID, including invariant determinantal processes with Hermitian positive-contraction kernels. This group-action conclusion requires no amenability.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-free-uniform-spanning-forest-is-a-factor-of-IID-September-25-2026/The-free-uniform-spanning-forest-is-a-factor-of-IID-September-25-2026.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves that the free uniform spanning forest is a factor of independent identically distributed vertex labels on every infinite connected locally finite simple unweighted graph. One Borel equivariant rule works for all such graphs and uses no distinguished root.

The linked supplements also give equivariant IID sampling for invariant strongly Rayleigh laws on countable groups and existence, uniqueness, and IID-factor results for determinantal laws with Hermitian positive-contraction kernels on countable index sets. These group results require neither amenability nor finite generation, and the kernels need not be trace class.

## Lean: Strongly Rayleigh and determinantal-process IID factors

```lean
theorem finite_strongly_rayleigh_response :
    ∀ (F : Type u_1) [Fintype F] [Nonempty F] (μ : ProbabilityMeasure (F → Bool)),
      StronglyRayleighFinite μ →
        (∀ (i j : F) (h : F → ℝ),
          HasDerivAt (fun r : ℝ => tiltMean μ (coordinatePerturb h j r) i)
            (tiltCovariance μ h i j) 0) ∧
        (∀ (i : F) (h : F → ℝ),
          (∑ j : F, |tiltCovariance μ h i j|) ≤
              2 * tiltMean μ h i * (1 - tiltMean μ h i) ∧
            2 * tiltMean μ h i * (1 - tiltMean μ h i) ≤ (1 : ℝ) / 2) ∧
        (∀ (i : F) (h h' : F → ℝ) (D : ℝ),
          0 ≤ D → (∀ j : F, |h j - h' j| ≤ D) →
            |tiltMean μ h i - tiltMean μ h' i| ≤ D / 2)
```

Stated in [StronglyRayleighDPP.lean, line 132](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/StronglyRayleighDPP.lean#L132). Proved in [lean/OAI/Probability/StrongRayleigh/Main.lean, line 21](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/StrongRayleigh/Main.lean#L21).

```lean
theorem strongly_rayleigh_group_factor :
    ∀ (Γ : Type u_2) [Group Γ] [Countable Γ] [MeasurableSpace Γ],
      ∀ μ : ProbabilityMeasure (Γ → Bool),
        StronglyRayleighCountable μ → InvariantBinaryLaw μ → HasEquivariantIIDFactor μ
```

Stated in [StronglyRayleighDPP.lean, line 147](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/StronglyRayleighDPP.lean#L147). Proved in [lean/OAI/Probability/StrongRayleigh/Main.lean, line 39](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/StrongRayleigh/Main.lean#L39).

```lean
theorem finite_positive_contraction_dpp_is_strongly_rayleigh :
    ∀ (F : Type u_3) [Fintype F] [Nonempty F] (K : F → F → ℂ),
      PositiveContractionFinite K →
        (∃ μ : ProbabilityMeasure (F → Bool), IsFiniteDeterminantalLaw μ K) ∧
          ∀ μ : ProbabilityMeasure (F → Bool), IsFiniteDeterminantalLaw μ K →
            StronglyRayleighFinite μ
```

Stated in [StronglyRayleighDPP.lean, line 153](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/StronglyRayleighDPP.lean#L153). Proved in [lean/OAI/Probability/StrongRayleigh/Main.lean, line 48](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/StrongRayleigh/Main.lean#L48).

```lean
theorem countable_positive_contraction_dpp_exists_unique :
    ∀ (I : Type u_4) [Countable I] (K : I → I → ℂ),
      PositiveContractionKernel K →
        ∃! μ : ProbabilityMeasure (I → Bool), IsDeterminantalLaw μ K
```

Stated in [StronglyRayleighDPP.lean, line 161](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/StronglyRayleighDPP.lean#L161). Proved in [lean/OAI/Probability/StrongRayleigh/Main.lean, line 57](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/StrongRayleigh/Main.lean#L57).

```lean
theorem invariant_positive_contraction_dpp_factor :
    ∀ (Γ : Type u_5) [Group Γ] [Countable Γ] [MeasurableSpace Γ]
      (K : Γ → Γ → ℂ) (μ : ProbabilityMeasure (Γ → Bool)),
      PositiveContractionKernel K → IsDeterminantalLaw μ K →
        InvariantBinaryLaw μ → HasEquivariantIIDFactor μ
```

Stated in [StronglyRayleighDPP.lean, line 167](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/StronglyRayleighDPP.lean#L167). Proved in [lean/OAI/Probability/StrongRayleigh/Main.lean, line 65](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/StrongRayleigh/Main.lean#L65).

```lean
theorem translation_invariant_kernel_dpp_factor :
    ∀ (Γ : Type u_6) [Group Γ] [Countable Γ] [MeasurableSpace Γ] (K : Γ → Γ → ℂ),
      PositiveContractionKernel K → TranslationInvariantKernel K →
        ∃ μ : ProbabilityMeasure (Γ → Bool),
          IsDeterminantalLaw μ K ∧ InvariantBinaryLaw μ ∧ HasEquivariantIIDFactor μ
```

Stated in [StronglyRayleighDPP.lean, line 174](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/StronglyRayleighDPP.lean#L174). Proved in [lean/OAI/Probability/StrongRayleigh/Main.lean, line 75](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/StrongRayleigh/Main.lean#L75).

## Lean: A universal IID factor for the free uniform spanning forest

```lean
theorem fusf_is_factor_iid :
    ∃ Phi : FactorRule, RuleBorel Phi ∧ RuleEquivariant Phi ∧ ∀ G : GraphCode, WorksOnGraph Phi G
```

Stated in [FreeUniformSpanningForest.lean, line 141](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/FreeUniformSpanningForest.lean#L141). Proved in [lean/OAI/Probability/SpanningForest/Factor.lean, line 13](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/SpanningForest/Factor.lean#L13).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/231.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/231.md)
