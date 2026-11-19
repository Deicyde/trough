---
declaration: def
origin: cited
lean: MIPStarRE.LDT.Test.TwoProverClassicalLIDPassCondition, MIPStarRE.LDT.Test.PolishchukSpielmanClassicalSoundnessStatement, MIPStarRE.LDT.Test.classicalTestSoundness, MIPStarRE.LDT.Test.TwoProverClassicalLIDStrategy.lowIndividualDegreeAcceptanceProbability_eq_branchAverage, MIPStarRE.LDT.ProjStrat.roleRegisterSymmStrategy_is_good_three_mul, MIPStarRE.LDT.Test.mainFormalConclusion, MIPStarRE.LDT.Preliminaries.polynomialAgreement_avg_le_mdq, MIPStarRE.LDT.Preliminaries.completionMissingMassBound
statement: formalized
proof: formalized
---

# MIPStarRE

[LionSR/MIPStarRE](https://github.com/LionSR/MIPStarRE) at commit [62039285](https://github.com/LionSR/MIPStarRE/tree/6203928569d45956b9c3e1f808e8e1a9f0116f70), 2026-11-15.

> Formalization project for mathematics around $\mathrm{MIP}^*=\mathrm{RE}$.

*Quoted from [README.md](https://github.com/LionSR/MIPStarRE/blob/6203928569d45956b9c3e1f808e8e1a9f0116f70/README.md), Apache-2.0.*

## Depends on

- [Polynomial in one indeterminate](../../general-algebra/polynomials-and-power-series/polynomial-in-one-indeterminate.md)

## Proof depends on

- [Local convexity](../../analysis/topological-vector-spaces/local-convexity.md)
- [Binomial law](../random-variables-and-their-laws/binomial-law.md)
- [Distributions](../../analysis/distribution-theory/distributions.md)
- [Bolzano–Weierstrass theorem (1000+ theorems)](../../../thousand-plus/analysis/26-real-functions/part-01/bolzano-weierstrass-theorem.md)
- [Bernoulli law](../random-variables-and-their-laws/bernoulli-law.md)
- [Unitary group](../../../undergraduate/group-theory/classical-automorphism-groups/unitary-group.md)
- [Power functions](../../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-exp/power-functions.md)
- [Rank of a matrix](../../../undergraduate/linear-algebra/matrices/rank-of-a-matrix.md)

## Main results

Its Lean names are 8 of the 20 Lean names of the blueprint nodes that no other node uses, marked \leanok:

- [`MIPStarRE.LDT.Test.TwoProverClassicalLIDPassCondition`](https://github.com/LionSR/MIPStarRE/blob/6203928569d45956b9c3e1f808e8e1a9f0116f70/MIPStarRE/LDT/Test/Classical.lean#L345) (def)
- [`MIPStarRE.LDT.Test.PolishchukSpielmanClassicalSoundnessStatement`](https://github.com/LionSR/MIPStarRE/blob/6203928569d45956b9c3e1f808e8e1a9f0116f70/MIPStarRE/LDT/Test/Classical.lean#L365) (def)
- [`MIPStarRE.LDT.Test.classicalTestSoundness`](https://github.com/LionSR/MIPStarRE/blob/6203928569d45956b9c3e1f808e8e1a9f0116f70/MIPStarRE/LDT/Test/Classical.lean#L380) (theorem)
- [`MIPStarRE.LDT.Test.TwoProverClassicalLIDStrategy.lowIndividualDegreeAcceptanceProbability_eq_branchAverage`](https://github.com/LionSR/MIPStarRE/blob/6203928569d45956b9c3e1f808e8e1a9f0116f70/MIPStarRE/LDT/Test/Classical.lean#L277) (theorem)
- [`MIPStarRE.LDT.ProjStrat.roleRegisterSymmStrategy_is_good_three_mul`](https://github.com/LionSR/MIPStarRE/blob/6203928569d45956b9c3e1f808e8e1a9f0116f70/MIPStarRE/LDT/Test/StrategyBiProjRoleAverage/Final.lean#L136) (theorem)
- [`MIPStarRE.LDT.Test.mainFormalConclusion`](https://github.com/LionSR/MIPStarRE/blob/6203928569d45956b9c3e1f808e8e1a9f0116f70/MIPStarRE/LDT/Test/MainTheorem/MainFormal.lean#L262) (theorem)
- [`MIPStarRE.LDT.Preliminaries.polynomialAgreement_avg_le_mdq`](https://github.com/LionSR/MIPStarRE/blob/6203928569d45956b9c3e1f808e8e1a9f0116f70/MIPStarRE/LDT/Preliminaries/PolynomialAgreement.lean#L104) (lemma)
- [`MIPStarRE.LDT.Preliminaries.completionMissingMassBound`](https://github.com/LionSR/MIPStarRE/blob/6203928569d45956b9c3e1f808e8e1a9f0116f70/MIPStarRE/LDT/Preliminaries/SelfConsistency/Core.lean#L76) (theorem)

No file its headlines import, directly or not (323 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0-rc2, Mathlib at [06535612](https://github.com/leanprover-community/mathlib4/tree/065356127b1dc0016f66b7283ce0ce2c4055aa55).
- 341 .lean files; its Lean libraries `MIPStarRE` hold 338, declaring 3,545 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- License: Apache-2.0 ([LICENSE](https://github.com/LionSR/MIPStarRE/blob/6203928569d45956b9c3e1f808e8e1a9f0116f70/LICENSE)).

## Builds on

- Mathlib, at [06535612](https://github.com/leanprover-community/mathlib4/tree/065356127b1dc0016f66b7283ce0ce2c4055aa55).

## Placement

Of its imports of Mathlib modules in an overview area, 4 of 39 are in Probability Theory, 5.4 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Probability Theory (4 of 39 imports, 5.4×), Analysis (18 of 39 imports, 1.7×), General algebra (10 of 39 imports, 0.7×). *Proof depends on* lists 8 of the 44 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [LionSR/MIPStarRE at 62039285](https://github.com/LionSR/MIPStarRE/tree/6203928569d45956b9c3e1f808e8e1a9f0116f70)
