---
declaration: theorem
origin: cited
lean: MovingSofa.sofaConstant_eq_volume_gerversSofa
statement: formalized
proof: formalized
---

# Optimality of Gerver's sofa

> Formalizes Baek's solution of the moving sofa problem: Gerver's sofa attains the supremum of the areas of closed connected shapes that can move continuously around a right-angled corner in a unit-width hallway. Includes certified Gerver parameters, admissibility, convex cap geometry, Stieltjes curve area, Jordan separation, polygon approximation, and the concave quadratic upper bound.

*Quoted from the card [LeanPool/projects/moving-sofa.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/moving-sofa.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`MovingSofa.sofaConstant_eq_volume_gerversSofa`](https://leanpool.github.io/lean-pool/LeanPool/MovingSofa/Development/Geometry/Applications/Development003.html#MovingSofa.sofaConstant_eq_volume_gerversSofa) (theorem; a main declaration), declared in [LeanPool/MovingSofa/Development/Geometry/Applications/Development003.lean, line 6015](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/MovingSofa/Development/Geometry/Applications/Development003.lean#L6015): “The supremum, in extended nonnegative real numbers, of the areas of all admissible moving sofas equals the area of the explicitly defined Gerver sofa.” Its source, as the card gives it: “Baek, Optimality of Gerver's Sofa, Theorem 1.1. Upstream Lean completion a0753860f1d2b4424e059c35e64ad611be71a415 (2026-09-20 10:55:24 UTC), announced 2026-09-20 18:42:40 UTC at https://x.com/deancureton/status/2101743865392926967. The imported commit has identical Lean sources; its later change is documentation only.”
- [`MovingSofa.GerversSofa.ABφθSpec.existsUnique`](https://leanpool.github.io/lean-pool/LeanPool/MovingSofa/Development/Geometry/Foundations/Development005.html#MovingSofa.GerversSofa.AB%CF%86%CE%B8Spec.existsUnique) (theorem), declared in [LeanPool/MovingSofa/Development/Geometry/Foundations/Development005.lean, line 189](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/MovingSofa/Development/Geometry/Foundations/Development005.lean#L189): “Gerver's four defining equations have exactly one quadruple of parameters with A and B nonnegative and 0 ≤ φ ≤ θ ≤ π/4.” Its source, as the card gives it: “Romik, Differential equations and exact solutions in the moving sofa problem, equations (1)-(4), arXiv:1606.08111. The GerverSofaLean v1.1.0 release archive (MIT, Dawid Trela) has SHA-256 7c496150f709ac709ae01f4836e9a702a18f752450efa69f15cf44264c0c2f77.”
- [`MovingSofa.isMovingSofa_gerversSofa`](https://leanpool.github.io/lean-pool/LeanPool/MovingSofa/Development/Geometry/Foundations/Development005.html#MovingSofa.isMovingSofa_gerversSofa) (theorem), declared in [LeanPool/MovingSofa/Development/Geometry/Foundations/Development005.lean, line 7930](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/MovingSofa/Development/Geometry/Foundations/Development005.lean#L7930): “Gerver's sofa is closed and connected and admits a continuous rigid motion from the horizontal arm to the vertical arm, starting at the identity and remaining within the unit-width hallway throughout.”

## Project

- Authors: Dean Cureton, Dawid Trela, Rado Kirov, Kirill Alkhimov.
- Source: *Optimality of Gerver's Sofa* by Jineon Baek, [arXiv:2411.19826](https://arxiv.org/abs/2411.19826).
- Project repository: [deancureton/MovingSofa](https://github.com/deancureton/MovingSofa), at commit [4d556913](https://github.com/deancureton/MovingSofa/tree/4d5569131940815f47a9ccf3e90a4c5043c56127).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 52A40, 52A10, 49Q10.
- In Lean Pool: [LeanPool/MovingSofa](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/MovingSofa), from the card [LeanPool/projects/moving-sofa.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/moving-sofa.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/moving-sofa.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/moving-sofa.yaml)
- [Lean Pool at 701389c0: LeanPool/MovingSofa](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/MovingSofa)
