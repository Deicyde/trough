---
declaration: theorem
origin: cited
lean: Bruck.bruck_conjecture, Bruck.exists_uniform_maximumModulus_lower_bound, Bruck.hyperOrder_eq_limsup_circleAverage_posLog
statement: formalized
proof: formalized
---

# Brück's conjecture for entire functions

> Proves Brück's conjecture for nonconstant entire functions of finite hyper-order outside the positive integers. The proof combines analytic zero multiplicities with growth bounds for solutions of a first-order complex differential equation.

*Quoted from the card [LeanPool/projects/bruck-conjecture.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/bruck-conjecture.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Bruck.bruck_conjecture`](https://leanpool.github.io/lean-pool/LeanPool/Bruck/Main.html#Bruck.bruck_conjecture) (theorem; a main declaration), declared in [LeanPool/Bruck/Main.lean, line 36](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Bruck/Main.lean#L36): “If a nonconstant entire function of finite hyper-order outside the positive integers shares a complex value with its derivative counting multiplicities, then the derivative minus that value is a nonzero constant multiple of the function minus that value.” Its source, as the card gives it: “Theorem 1.1 of the cited preprint. The pinned Lean proof formalizes the earlier unpublished manuscript Value Sharing and a First-Order Complex Differential Equation by Yixin He, Tao Hu, and Quanyu Tang.”
- [`Bruck.exists_uniform_maximumModulus_lower_bound`](https://leanpool.github.io/lean-pool/LeanPool/Bruck/GlobalGrowth.html#Bruck.exists_uniform_maximumModulus_lower_bound) (theorem; a main declaration), declared in [LeanPool/Bruck/GlobalGrowth.lean, line 59](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Bruck/GlobalGrowth.lean#L59): “For every nonconstant entire h there are arbitrarily large radii r, chosen independently of the solution, such that every entire solution y of y′ = exp(h)y + 1 has maximum modulus at 2r at least exp(exp(M(r, h) / 2200)), with the numerical constant supplied by the pinned Lean formalization.” Its source, as the card gives it: “Theorem 1.3, explicit quantitative variant from the pinned Lean formalization”
- [`Bruck.hyperOrder_eq_limsup_circleAverage_posLog`](https://leanpool.github.io/lean-pool/LeanPool/Bruck/StatementChecks.html#Bruck.hyperOrder_eq_limsup_circleAverage_posLog) (theorem; a main declaration), declared in [LeanPool/Bruck/StatementChecks.lean, line 45](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Bruck/StatementChecks.lean#L45): “For a nonconstant entire function, the formal hyper-order equals the classical limsup defined from the circle mean of the positive logarithm of its norm.”

## Project

- Authors: Pengcheng Fang, Tao Hu, Yanyang Li, Quanyu Tang, Haiqi Zhang.
- Source: *The Brück conjecture and the growth of entire solutions of a differential equation* by Pengcheng Fang, Tao Hu, Yanyang Li, Quanyu Tang, Haiqi Zhang, [https://hexagonmath.org/2611.00826v1](https://hexagonmath.org/2611.00826v1).
- Project repository: [QuanyuTang/bruck-conjecture-formalization](https://github.com/QuanyuTang/bruck-conjecture-formalization), at commit [00f71637](https://github.com/QuanyuTang/bruck-conjecture-formalization/tree/00f71637fc70ed8d12f51d79f6ff2f211592d6b4).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 30D35, 30D15, 34M10.
- In Lean Pool: [LeanPool/Bruck](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Bruck), from the card [LeanPool/projects/bruck-conjecture.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/bruck-conjecture.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/bruck-conjecture.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/bruck-conjecture.yaml)
- [Lean Pool at bb99e52c: LeanPool/Bruck](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Bruck)
