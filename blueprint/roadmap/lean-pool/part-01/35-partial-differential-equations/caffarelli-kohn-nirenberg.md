---
declaration: theorem
origin: cited
lean: CKN.epsilonRegularityL3, CKN.caffarelliKohnNirenberg
statement: formalized
proof: formalized
---

# Caffarelli–Kohn–Nirenberg partial regularity

> Partial regularity for three-dimensional incompressible Navier–Stokes suitable weak solutions with locally L^q forcing, q > 5/2: quantitative epsilon regularity and vanishing parabolic one-dimensional Hausdorff measure of the singular set. Includes the supporting Sobolev, singular integral, pressure, heat-potential and parabolic Morrey infrastructure, equivalence of suitable-solution formulations, and a nonzero shear-flow example. Includes the completed Leray, pressure, and linear regularity support needed by further Navier–Stokes regularity projects.

*Quoted from the card [LeanPool/projects/caffarelli-kohn-nirenberg.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/caffarelli-kohn-nirenberg.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`CKN.epsilonRegularityL3`](https://leanpool.github.io/lean-pool/LeanPool/CaffarelliKohnNirenberg/Statements/TheoremA.html#CKN.epsilonRegularityL3) (theorem; a main declaration), declared in [LeanPool/CaffarelliKohnNirenberg/Statements/TheoremA.lean, line 35](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CaffarelliKohnNirenberg/Statements/TheoremA.lean#L35): “For q > 5/2, sufficiently small unit-cylinder L^3 velocity, L^(3/2) pressure and L^q force masses give an almost-everywhere equal quantitatively bounded parabolic Holder representative on the closed half-cylinder and regularity at each point of its open interior.”
- [`CKN.epsilonRegularityGradient`](https://leanpool.github.io/lean-pool/LeanPool/CaffarelliKohnNirenberg/Statements/TheoremB.html#CKN.epsilonRegularityGradient) (theorem), declared in [LeanPool/CaffarelliKohnNirenberg/Statements/TheoremB.lean, line 34](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CaffarelliKohnNirenberg/Statements/TheoremB.lean#L34): “A sufficiently small extended nonnegative limsup of the normalized squared weak-gradient mass implies regularity at an interior point of a suitable weak solution.”
- [`CKN.caffarelliKohnNirenberg`](https://leanpool.github.io/lean-pool/LeanPool/CaffarelliKohnNirenberg/Statements/TheoremC.html#CKN.caffarelliKohnNirenberg) (theorem; a main declaration), declared in [LeanPool/CaffarelliKohnNirenberg/Statements/TheoremC.lean, line 35](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CaffarelliKohnNirenberg/Statements/TheoremC.lean#L35): “The singular set of a suitable weak solution with locally L^q forcing, q > 5/2, has zero one-dimensional Hausdorff measure in the parabolic metric.”
- [`CKN.isSuitableWeakSolution_iff_integrable`](https://leanpool.github.io/lean-pool/LeanPool/CaffarelliKohnNirenberg/ClassEquivalence/MainTheorems.html#CKN.isSuitableWeakSolution_iff_integrable) (theorem), declared in [LeanPool/CaffarelliKohnNirenberg/ClassEquivalence/MainTheorems.lean, line 87](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CaffarelliKohnNirenberg/ClassEquivalence/MainTheorems.lean#L87): “The manuscript's suitable weak-solution predicate is equivalent to the predicate that explicitly requires integrability of all tested weak-equation and local-energy integrands.”
- [`CKN.isSuitableWeakSolutionIntegrable_shearFlow`](https://leanpool.github.io/lean-pool/LeanPool/CaffarelliKohnNirenberg/Setting/Examples/ShearFlowSuitable.html#CKN.isSuitableWeakSolutionIntegrable_shearFlow) (theorem), declared in [LeanPool/CaffarelliKohnNirenberg/Setting/Examples/ShearFlowSuitable.lean, line 27](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CaffarelliKohnNirenberg/Setting/Examples/ShearFlowSuitable.lean#L27): “The nonzero decaying sinusoidal shear flow with zero pressure and force is a suitable weak solution on all space and times in (0,1).”

## Project

- Authors: Scott Armstrong, Vlad Vicol.
- Project repository: [scottnarmstrong/CaffarelliKohnNirenberg](https://github.com/scottnarmstrong/CaffarelliKohnNirenberg), at commit [381d658e](https://github.com/scottnarmstrong/CaffarelliKohnNirenberg/tree/381d658ead0f03a18361965cc0427ce3fa5844ab).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 35Q30, 35B65, 42B20, 28A78.
- In Lean Pool: [LeanPool/CaffarelliKohnNirenberg](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CaffarelliKohnNirenberg), from the card [LeanPool/projects/caffarelli-kohn-nirenberg.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/caffarelli-kohn-nirenberg.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/caffarelli-kohn-nirenberg.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/caffarelli-kohn-nirenberg.yaml)
- [Lean Pool at 701389c0: LeanPool/CaffarelliKohnNirenberg](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CaffarelliKohnNirenberg)
