---
declaration: theorem
origin: cited
lean: LeanPool.Zeta3Irrational.zeta3_irrational
statement: formalized
proof: formalized
---

# Irrationality of ζ(3)

> Formalizes Beukers' proof of Apéry's theorem for ζ(3), including the integral identities, denominator estimates, positivity, upper bounds, and final irrationality contradiction.

*Quoted from the card [LeanPool/projects/zeta_3_irrational.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/zeta_3_irrational.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`LeanPool.Zeta3Irrational.zeta3_irrational`](https://leanpool.github.io/lean-pool/LeanPool/Zeta3Irrational/Basic.html#LeanPool.Zeta3Irrational.zeta3_irrational) (theorem; a main declaration), declared in [LeanPool/Zeta3Irrational/Basic.lean, line 1177](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Zeta3Irrational/Basic.lean#L1177): “Proves that ζ(3) is irrational.”
- [`LeanPool.Zeta3Irrational.linear_int`](https://leanpool.github.io/lean-pool/LeanPool/Zeta3Irrational/Basic.html#LeanPool.Zeta3Irrational.linear_int) (theorem), declared in [LeanPool/Zeta3Irrational/Basic.lean, line 54](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Zeta3Irrational/Basic.lean#L54): “Clears denominators in the Apéry integral to produce a linear form in 1 and ζ(3).”
- [`LeanPool.Zeta3Irrational.JJ_pos`](https://leanpool.github.io/lean-pool/LeanPool/Zeta3Irrational/Basic.html#LeanPool.Zeta3Irrational.JJ_pos) (theorem), declared in [LeanPool/Zeta3Irrational/Basic.lean, line 962](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Zeta3Irrational/Basic.lean#L962): “Proves positivity of the transformed Beukers-Apéry integral.”
- [`LeanPool.Zeta3Irrational.JJ_upper`](https://leanpool.github.io/lean-pool/LeanPool/Zeta3Irrational/Basic.html#LeanPool.Zeta3Irrational.JJ_upper) (theorem), declared in [LeanPool/Zeta3Irrational/Basic.lean, line 1053](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Zeta3Irrational/Basic.lean#L1053): “Bounds the Beukers-Apéry integral by a geometric factor times the ζ(3) series.”
- [`LeanPool.Zeta3Irrational.fun1_tendsto_zero`](https://leanpool.github.io/lean-pool/LeanPool/Zeta3Irrational/Basic.html#LeanPool.Zeta3Irrational.fun1_tendsto_zero) (theorem), declared in [LeanPool/Zeta3Irrational/Basic.lean, line 1119](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Zeta3Irrational/Basic.lean#L1119): “Shows that the denominator-cleared Apéry linear forms tend to zero.”

## Project

- Authors: Junqi Liu, Jujian Zhang.
- Source: *A note on the irrationality of ζ(2) and ζ(3)* by Frits Beukers, [doi:10.1112/blms/11.3.268](https://doi.org/10.1112/blms/11.3.268), [arXiv:2503.07625](https://arxiv.org/abs/2503.07625).
- Project repository: [ahhwuhu/zeta_3_irrational](https://github.com/ahhwuhu/zeta_3_irrational).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 11M06, 11J72.
- In Lean Pool: [LeanPool/Zeta3Irrational](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Zeta3Irrational), from the card [LeanPool/projects/zeta_3_irrational.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/zeta_3_irrational.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/zeta_3_irrational.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/zeta_3_irrational.yaml)
- [Lean Pool at 2b205bf9: LeanPool/Zeta3Irrational](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Zeta3Irrational)
