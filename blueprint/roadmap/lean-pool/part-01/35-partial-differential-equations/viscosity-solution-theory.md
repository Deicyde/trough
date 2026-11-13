---
declaration: theorem
origin: cited
lean: ViscositySolns.dirichlet_harmonic_modulus_of_uniformExteriorSphere
statement: formalized
proof: formalized
---

# Viscosity solutions, Aleksandrov differentiability and harmonic Dirichlet problems

> Develops second-order semijets, smooth test-function equivalence, Jensen contact sets, convex Aleksandrov differentiability, the quadratic-penalty Ishii lemma and compact-domain comparison for degenerate elliptic equations. Perron assembly retains explicit comparison, barrier and bumping assumptions; these are discharged for classical harmonic Dirichlet existence on bounded open domains satisfying a uniform exterior sphere condition.

*Quoted from the card [LeanPool/projects/viscosity-solution-theory.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/viscosity-solution-theory.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 6 main results, each with its informal statement quoted from the card. The scan finds 6 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`AleksandrovDifferentiability.convexAleksandrovAE`](https://leanpool.github.io/lean-pool/LeanPool/ViscositySolutionTheory/AleksandrovDifferentiability/Statements/Aleksandrov/Final.html#AleksandrovDifferentiability.convexAleksandrovAE) (theorem), declared in [LeanPool/ViscositySolutionTheory/AleksandrovDifferentiability/Statements/Aleksandrov/Final.lean, line 39](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/ViscositySolutionTheory/AleksandrovDifferentiability/Statements/Aleksandrov/Final.lean#L39): “A convex real-valued function on an open subset of any finite-dimensional real inner product space is second-order differentiable at Lebesgue-almost every point.”
- [`ViscositySolns.JensenContactSetPositiveMeasureOnClosedBallTheorem.proof`](https://leanpool.github.io/lean-pool/LeanPool/ViscositySolutionTheory/ViscositySolns/Analysis/SemiconvexJensen/Jensen/MainTheorems.html#ViscositySolns.JensenContactSetPositiveMeasureOnClosedBallTheorem.proof) (theorem), declared in [LeanPool/ViscositySolutionTheory/ViscositySolns/Analysis/SemiconvexJensen/Jensen/MainTheorems.lean, line 538](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/ViscositySolutionTheory/ViscositySolns/Analysis/SemiconvexJensen/Jensen/MainTheorems.lean#L538): “Under the localized semiconvexity and strict-contact hypotheses, the contact set arising from sufficiently small linear perturbations has positive Lebesgue measure.”
- [`ViscositySolns.QuadraticPenaltyIshiiLemmaOn.proof`](https://leanpool.github.io/lean-pool/LeanPool/ViscositySolutionTheory/ViscositySolns/Comparison/CILMaximumPrinciple.html#ViscositySolns.QuadraticPenaltyIshiiLemmaOn.proof) (theorem), declared in [LeanPool/ViscositySolutionTheory/ViscositySolns/Comparison/CILMaximumPrinciple.lean, line 327](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/ViscositySolutionTheory/ViscositySolns/Comparison/CILMaximumPrinciple.lean#L327): “For an upper semicontinuous function and a lower semicontinuous function on locally compact subsets of real coordinate space, doubled-variable maxima with the quadratic penalty yield closed semijets satisfying the Ishii block-matrix bounds.”
- [`ViscositySolns.comparison_of_constantShift_boundary_proof`](https://leanpool.github.io/lean-pool/LeanPool/ViscositySolutionTheory/ViscositySolns/Comparison/ProperComparison/Compact/ConstantShiftBoundary.html#ViscositySolns.comparison_of_constantShift_boundary_proof) (theorem), declared in [LeanPool/ViscositySolutionTheory/ViscositySolns/Comparison/ProperComparison/Compact/ConstantShiftBoundary.lean, line 521](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/ViscositySolutionTheory/ViscositySolns/Comparison/ProperComparison/Compact/ConstantShiftBoundary.lean#L521): “A viscosity subsolution lies below a supersolution on a nonempty locally compact domain with compact closure, assuming boundary comparison, semicontinuity on the closure, properness, operator continuity, the Ishii structural condition and uniform scalar decrease.”
- [`ViscositySolns.viscositySubsolution_iff_smoothTestFunctionSubsolution`](https://leanpool.github.io/lean-pool/LeanPool/ViscositySolutionTheory/ViscositySolns/TestFunctions/Characterization.html#ViscositySolns.viscositySubsolution_iff_smoothTestFunctionSubsolution) (theorem), declared in [LeanPool/ViscositySolutionTheory/ViscositySolns/TestFunctions/Characterization.lean, line 563](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/ViscositySolutionTheory/ViscositySolns/TestFunctions/Characterization.lean#L563): “On an open domain, semijet and smooth C² test-function formulations of viscosity subsolutions agree for Hessian-continuous, symmetric-part-invariant operators.”
- [`ViscositySolns.dirichlet_harmonic_modulus_of_uniformExteriorSphere`](https://leanpool.github.io/lean-pool/LeanPool/ViscositySolutionTheory/ViscositySolns/Applications/Laplace/Dirichlet.html#ViscositySolns.dirichlet_harmonic_modulus_of_uniformExteriorSphere) (theorem; a main declaration), declared in [LeanPool/ViscositySolutionTheory/ViscositySolns/Applications/Laplace/Dirichlet.lean, line 51](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/ViscositySolutionTheory/ViscositySolns/Applications/Laplace/Dirichlet.lean#L51): “On a bounded open subset of finite-dimensional Euclidean space with a uniform exterior sphere condition, Lipschitz data on its closure admit a continuous extension that agrees on the boundary and is C² and harmonic in the domain, with a boundary modulus depending only on the domain and Lipschitz constant.”

## Project

- Authors: William M. Feldman, AleksandrovDifferentiability contributors, The Tau Ceti contributors.
- Source: [arXiv:math/9207212](https://arxiv.org/abs/math/9207212).
- Project repository: [willmfeldman/viscosity-solution-theory](https://github.com/willmfeldman/viscosity-solution-theory), at commit [067e2540](https://github.com/willmfeldman/viscosity-solution-theory/tree/067e2540ad1594408c0b6145c5bde01b4d5791a9).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 35D40, 35J60, 26B25.
- In Lean Pool: [LeanPool/ViscositySolutionTheory](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/ViscositySolutionTheory), from the card [LeanPool/projects/viscosity-solution-theory.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/viscosity-solution-theory.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/viscosity-solution-theory.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/viscosity-solution-theory.yaml)
- [Lean Pool at 701389c0: LeanPool/ViscositySolutionTheory](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/ViscositySolutionTheory)
