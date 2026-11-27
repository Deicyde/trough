---
declaration: theorem
origin: cited
lean: SGPT.NPP.currentProduct_restrict, SGPT.NPP.NonPluripolarCurrent.nonPluripolarProduct_append_bounded, SGPT.Foundations.Analysis.Pending.GlobalNonPluripolar.globalMixedMeasure_isFiniteMeasure
statement: formalized
proof: formalized
---

# Nonpluripolar products of positive currents

> Constructs nonpluripolar products from compatible local potentials on complex manifolds and proves independence of the local presentation. The development also establishes compatibility with locally bounded Bedford–Taylor factors. It reuses results from Mingchen Xia's earlier envelope-property formalization, including finiteness of the mixed measure on compact Kähler manifolds.

*Quoted from the card [LeanPool/projects/nonpluripolar-products.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/nonpluripolar-products.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`SGPT.NPP.currentProduct_restrict`](https://leanpool.github.io/lean-pool/LeanPool/NonpluripolarProducts/NPP/NonPluripolarCurrent3Currents.html#SGPT.NPP.currentProduct_restrict) (theorem; a main declaration), declared in [LeanPool/NonpluripolarProducts/NPP/NonPluripolarCurrent3Currents.lean, line 442](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/NonpluripolarProducts/NPP/NonPluripolarCurrent3Currents.lean#L442): “The nonpluripolar product of a well-defined family of positive currents restricts to the product computed from any local potentials for those currents.”
- [`SGPT.NPP.NonPluripolarCurrent.nonPluripolarProduct_append_bounded`](https://leanpool.github.io/lean-pool/LeanPool/NonpluripolarProducts/NPP/NonPluripolarCurrent4Bounded.html#SGPT.NPP.NonPluripolarCurrent.nonPluripolarProduct_append_bounded) (theorem; a main declaration), declared in [LeanPool/NonpluripolarProducts/NPP/NonPluripolarCurrent4Bounded.lean, line 548](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/NonpluripolarProducts/NPP/NonPluripolarCurrent4Bounded.lean#L548): “Adding locally bounded plurisubharmonic factors to a well-defined local nonpluripolar product agrees with the iterated Bedford–Taylor product.”
- [`SGPT.Foundations.Analysis.Pending.GlobalNonPluripolar.globalMixedMeasure_isFiniteMeasure`](https://leanpool.github.io/lean-pool/LeanPool/NonpluripolarProducts/Foundations/Analysis/Pending/GlobalNonPluripolarKahler.html#SGPT.Foundations.Analysis.Pending.GlobalNonPluripolar.globalMixedMeasure_isFiniteMeasure) (theorem; a main declaration), declared in [LeanPool/NonpluripolarProducts/Foundations/Analysis/Pending/GlobalNonPluripolarKahler.lean, line 91](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/NonpluripolarProducts/Foundations/Analysis/Pending/GlobalNonPluripolarKahler.lean#L91): “The mixed nonpluripolar measure of theta-plurisubharmonic potentials for smooth closed real backgrounds is finite on a compact Kähler manifold.”

## Project

- Authors: Mingchen Xia, Jian Wang, Siqi He, Zayn Blore.
- Source: [arXiv:0812.3674](https://arxiv.org/abs/0812.3674).
- Project repository: [MingchenXia/SGPT-lean](https://github.com/MingchenXia/SGPT-lean), at commit [76cbff42](https://github.com/MingchenXia/SGPT-lean/tree/76cbff42fbefc4c953a0ea0ba5b6948ac20c69b3).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 32U05, 32W20, 32J27.
- In Lean Pool: [LeanPool/NonpluripolarProducts](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/NonpluripolarProducts), from the card [LeanPool/projects/nonpluripolar-products.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/nonpluripolar-products.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/nonpluripolar-products.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/nonpluripolar-products.yaml)
- [Lean Pool at bb99e52c: LeanPool/NonpluripolarProducts](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/NonpluripolarProducts)
