---
declaration: theorem
origin: cited
lean: FQFP.BCH.norm_suzukiProduct_pow_sub_septic_midpoint_le_of_skewAdjoint, FQFP.BCH.isBigO_fiveStageStrangProduct_pow_sub_septic_midpoint, FQFP.BCH.tendsto_nat_pow_four_mul_norm_suzukiProduct_pow_sub_exp_of_skewAdjoint
statement: formalized
proof: formalized
---

# Cancellation-aware error bounds for the fourth-order Suzuki formula

> In complete normed algebras with two-sided contractive exponentials, the binary fourth-order Suzuki splitting has a global error expansion through the centered septic term and an eighth-order remainder at fixed nonnegative time. For skew-adjoint generators in a complete C\*-algebra, the integral of the transported quintic coefficient determines the leading error norm.

*Quoted from the card [LeanPool/projects/suzuki-cancellation.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/suzuki-cancellation.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`FQFP.BCH.norm_suzukiProduct_pow_sub_septic_midpoint_le_of_skewAdjoint`](https://leanpool.github.io/lean-pool/LeanPool/SuzukiCancellation/Analysis/Normed/Algebra/ProductFormula/SuzukiSepticGlobalError.html#FQFP.BCH.norm_suzukiProduct_pow_sub_septic_midpoint_le_of_skewAdjoint) (theorem; a main declaration), declared in [LeanPool/SuzukiCancellation/Analysis/Normed/Algebra/ProductFormula/SuzukiSepticGlobalError.lean, line 137](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/SuzukiCancellation/Analysis/Normed/Algebra/ProductFormula/SuzukiSepticGlobalError.lean#L137): “For two skew-adjoint generators in a complete C\*-algebra with compatible real scalars, a nonnegative final time, and any positive number of steps, the left-normalized Suzuki product error differs from the sum of the transported quintic and centered septic terms by at most an explicit remainder.”
- [`FQFP.BCH.isBigO_fiveStageStrangProduct_pow_sub_septic_midpoint`](https://leanpool.github.io/lean-pool/LeanPool/SuzukiCancellation/Analysis/Normed/Algebra/ProductFormula/SuzukiSepticGlobalError.html#FQFP.BCH.isBigO_fiveStageStrangProduct_pow_sub_septic_midpoint) (theorem; a main declaration), declared in [LeanPool/SuzukiCancellation/Analysis/Normed/Algebra/ProductFormula/SuzukiSepticGlobalError.lean, line 108](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/SuzukiCancellation/Analysis/Normed/Algebra/ProductFormula/SuzukiSepticGlobalError.lean#L108): “In a complete normed algebra, with the Suzuki cubic relation and contractive exponentials for both generators and their sum at every real time, the refined operator remainder at fixed nonnegative final time is big O of the inverse eighth power of the number of steps.”
- [`FQFP.BCH.tendsto_nat_pow_four_mul_norm_suzukiProduct_pow_sub_exp_of_skewAdjoint`](https://leanpool.github.io/lean-pool/LeanPool/SuzukiCancellation/Analysis/Normed/Algebra/ProductFormula/SuzukiGlobalError.html#FQFP.BCH.tendsto_nat_pow_four_mul_norm_suzukiProduct_pow_sub_exp_of_skewAdjoint) (theorem; a main declaration), declared in [LeanPool/SuzukiCancellation/Analysis/Normed/Algebra/ProductFormula/SuzukiGlobalError.lean, line 208](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/SuzukiCancellation/Analysis/Normed/Algebra/ProductFormula/SuzukiGlobalError.lean#L208): “For skew-adjoint generators in a complete C\*-algebra with compatible real scalars and fixed nonnegative final time, the global Suzuki error norm scaled by the fourth power of the step count converges to the fourth power of the final time times the norm of the integrated conjugated quintic coefficient as the natural-number step count tends to infinity.”

## Project

- Authors: Bingyu Xia, Jue Xu, Yue Wang.
- Source: *Trotter Error Bounds in Lean 4 with a Cancellation-Aware Analysis of the Fourth-Order Suzuki Formula*, [arXiv:2611.27359](https://arxiv.org/abs/2611.27359).
- Project repository: [BryceT233/Foresight-Quantum-Formalization-Projects](https://github.com/BryceT233/Foresight-Quantum-Formalization-Projects), at commit [40b042ff](https://github.com/BryceT233/Foresight-Quantum-Formalization-Projects/tree/40b042ff69f569bbc8d94273620ee0b59d272455).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 47D06, 65J10, 46H30.
- In Lean Pool: [LeanPool/SuzukiCancellation](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/SuzukiCancellation), from the card [LeanPool/projects/suzuki-cancellation.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/suzuki-cancellation.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/suzuki-cancellation.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/suzuki-cancellation.yaml)
- [Lean Pool at bb99e52c: LeanPool/SuzukiCancellation](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/SuzukiCancellation)
