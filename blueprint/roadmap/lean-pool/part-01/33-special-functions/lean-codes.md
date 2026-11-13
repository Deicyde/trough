---
declaration: theorem
origin: cited
lean: PalomarSnapshot.r_first_quadratic, PalomarSnapshot.joint_average_continuation
statement: formalized
proof: formalized
---

# Carlson special functions and complex Dirichlet averages

> Formalizes Carlson special functions through complex Dirichlet averages, with simplex measures, Gamma-regularized analytic continuation, Euler inversion, Euler–Poisson equations, and quadratic transformations. Includes the complete supporting several-complex-variable and special-function libraries.

*Quoted from the card [LeanPool/projects/lean-codes.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/lean-codes.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`PalomarSnapshot.r_first_quadratic`](https://leanpool.github.io/lean-pool/LeanPool/CarlsonFunctions/Solution.html#PalomarSnapshot.r_first_quadratic) (theorem; a main declaration), declared in [LeanPool/CarlsonFunctions/Solution.lean, line 209](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CarlsonFunctions/Solution.lean#L209): “The Gamma-regularized Carlson R function satisfies the first quadratic transformation for complex exponent and Dirichlet parameters with positive-real-part unsquared variables.”
- [`PalomarSnapshot.joint_average_continuation`](https://leanpool.github.io/lean-pool/LeanPool/CarlsonFunctions/Solution.html#PalomarSnapshot.joint_average_continuation) (theorem; a main declaration), declared in [LeanPool/CarlsonFunctions/Solution.lean, line 163](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CarlsonFunctions/Solution.lean#L163): “For a holomorphic scalar function on a convex open domain D, its Gamma-regularized Dirichlet average extends jointly holomorphically to all complex Dirichlet parameters and all node vectors in D. The extension agrees with the regularized simplex integral when every parameter has positive real part; the ordinary normalized average differs by the factor Gamma of the parameter sum.”

## Project

- Authors: Bastiaan J Braams.
- Project repository: [bjbraams/lean-codes](https://github.com/bjbraams/lean-codes), at commit [fcc2be9a](https://github.com/bjbraams/lean-codes/tree/fcc2be9a086c1bdd572db91f005e868b80a8d644).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 33C65, 32A10.
- In Lean Pool: [LeanPool/CarlsonFunctions](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CarlsonFunctions), from the card [LeanPool/projects/lean-codes.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/lean-codes.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/lean-codes.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/lean-codes.yaml)
- [Lean Pool at 701389c0: LeanPool/CarlsonFunctions](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CarlsonFunctions)
