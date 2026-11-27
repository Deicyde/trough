---
declaration: alias
origin: cited
lean: Cutfast.cutoff_wassersteinSq, Cutfast.cutoff_relEntropy, Cutfast.cutoff_fisherInfo, Cutfast.cutoff_fixedExponent_wassersteinSq, Cutfast.cutoff_fixedExponent_relEntropy, Cutfast.cutoff_fixedExponent_fisherInfo
statement: formalized
proof: formalized
---

# Cutoff for fast diffusion and porous medium equations

> Proves high-dimensional cutoff in quadratic Wasserstein distance, relative entropy and Fisher information for the explicit Barenblatt flow started from a point, using exact radial beta integrals, moments and transport formulas. The development also describes heavy tails and the Gaussian diffusion limit. All six cutoff results extend the paper's late-time limits to every ε > 0.

*Quoted from the card [LeanPool/projects/cutoff-fast-diffusion.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/cutoff-fast-diffusion.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 6 main results, each with its informal statement quoted from the card. The scan finds 6 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Cutfast.cutoff_wassersteinSq`](https://leanpool.github.io/lean-pool/LeanPool/Cutfast/CutoffRadius.html#Cutfast.cutoff_wassersteinSq) (alias; a main declaration), declared in [LeanPool/Cutfast/CutoffRadius.lean, line 560](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Cutfast/CutoffRadius.lean#L560): “Fix α > 0 with α ≠ 1/2 and r > 0, and set m = ((d − 2)α + 1)/(dα). The supremum of squared Wasserstein distance over initial points in the closed ball of radius r√d tends to infinity at (1 − ε)t\* for fixed 0 < ε < 1 and to zero at (1 + ε)t\* for fixed ε > 0, with t\* = max(1, α) log d / 2.”
- [`Cutfast.cutoff_relEntropy`](https://leanpool.github.io/lean-pool/LeanPool/Cutfast/CutoffRadius.html#Cutfast.cutoff_relEntropy) (alias; a main declaration), declared in [LeanPool/Cutfast/CutoffRadius.lean, line 567](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Cutfast/CutoffRadius.lean#L567): “Fix α > 0 with α ≠ 1/2 and r > 0, and set m = ((d − 2)α + 1)/(dα). The supremum of relative entropy over the closed ball of initial points of radius r√d tends to infinity at (1 − ε)t\* for fixed 0 < ε < 1 and to zero at (1 + ε)t\* for fixed ε > 0, with t\* = max(1, α) log d / 2. In sufficiently large dimension its defining integrand is integrable for every positive time and every initial point in this ball.”
- [`Cutfast.cutoff_fisherInfo`](https://leanpool.github.io/lean-pool/LeanPool/Cutfast/CutoffRadius.html#Cutfast.cutoff_fisherInfo) (alias; a main declaration), declared in [LeanPool/Cutfast/CutoffRadius.lean, line 573](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Cutfast/CutoffRadius.lean#L573): “Fix α > 0 with α ≠ 1/2 and r > 0, and set m = ((d − 2)α + 1)/(dα). The supremum of relative Fisher information over the closed ball of initial points of radius r√d tends to infinity at (1 − ε)t\* for fixed 0 < ε < 1 and to zero at (1 + ε)t\* for fixed ε > 0, with t\* = max(1, α) log d / 2.”
- [`Cutfast.cutoff_fixedExponent_wassersteinSq`](https://leanpool.github.io/lean-pool/LeanPool/Cutfast/CutoffRadius.html#Cutfast.cutoff_fixedExponent_wassersteinSq) (alias; a main declaration), declared in [LeanPool/Cutfast/CutoffRadius.lean, line 579](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Cutfast/CutoffRadius.lean#L579): “For fixed porous medium exponent m > 1 and r > 0, the supremum of squared Wasserstein distance over initial points in the closed ball of radius r√d tends to infinity at (1 − ε)t\* for fixed 0 < ε < 1 and to zero at (1 + ε)t\* for fixed ε > 0, with t\* = log d / 2.”
- [`Cutfast.cutoff_fixedExponent_relEntropy`](https://leanpool.github.io/lean-pool/LeanPool/Cutfast/CutoffRadius.html#Cutfast.cutoff_fixedExponent_relEntropy) (alias; a main declaration), declared in [LeanPool/Cutfast/CutoffRadius.lean, line 584](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Cutfast/CutoffRadius.lean#L584): “For fixed porous medium exponent m > 1 and r > 0, the supremum of relative entropy over the closed ball of initial points of radius r√d tends to infinity at (1 − ε)t\* for fixed 0 < ε < 1 and to zero at (1 + ε)t\* for fixed ε > 0, with t\* = log d / 2. In sufficiently large dimension its defining integrand is integrable for every positive time and every initial point in this ball.”
- [`Cutfast.cutoff_fixedExponent_fisherInfo`](https://leanpool.github.io/lean-pool/LeanPool/Cutfast/CutoffRadius.html#Cutfast.cutoff_fixedExponent_fisherInfo) (alias; a main declaration), declared in [LeanPool/Cutfast/CutoffRadius.lean, line 588](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Cutfast/CutoffRadius.lean#L588): “For fixed porous medium exponent m > 1 and r > 0, the supremum of relative Fisher information over the closed ball of initial points of radius r√d tends to infinity at (1 − ε)t\* for fixed 0 < ε < 1 and to zero at (1 + ε)t\* for fixed ε > 0, with t\* = log d / 2.”

## Project

- Authors: Djalil Chafaï.
- Source: *On the cutoff phenomenon for fast diffusion and porous medium equations*, [arXiv:2503.11770v2](https://arxiv.org/abs/2503.11770v2).
- Project repository: [djalilchafai/cutoff-fastdiff](https://github.com/djalilchafai/cutoff-fastdiff), at commit [6621bf2a](https://github.com/djalilchafai/cutoff-fastdiff/tree/6621bf2a7779c7fb7cbda04bb7c860d853c5c516).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 35K55, 35B40, 49Q22, 60J60.
- In Lean Pool: [LeanPool/Cutfast](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Cutfast), from the card [LeanPool/projects/cutoff-fast-diffusion.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/cutoff-fast-diffusion.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/cutoff-fast-diffusion.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/cutoff-fast-diffusion.yaml)
- [Lean Pool at bb99e52c: LeanPool/Cutfast](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Cutfast)
