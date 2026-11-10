---
declaration: theorem
origin: cited
lean: LehmerE10.main_theorem
statement: formalized
proof: formalized
---

# Lehmer's Polynomial and the E10 Coxeter Element

> Proves that Lehmer's degree-10 polynomial — the integer polynomial of smallest known Mahler measure above 1 — is irreducible over the integers, and that it is the characteristic polynomial of a Coxeter element of the E10 Weyl group (the rank-10 instance of McMullen). Against Mathlib's Mahler-measure API it computes M(L) exactly as the Salem root with the unconditional bounds 1 < M(L) < 7/5, states Lehmer's conjecture as a defined Prop (never assumed) with the strong form implying the gap form, and contrasts the E8 Coxeter element (order exactly 30) with the E10 element (infinite order in GL(10,Z)): the E-series crosses from torsion to a Salem matrix at rank 10, and the crossing value is Lehmer's number.

*Quoted from the card [LeanPool/projects/lehmer-e10.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/lehmer-e10.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`LehmerE10.main_theorem`](https://leanpool.github.io/lean-pool/LeanPool/LehmerE10.html#LehmerE10.main_theorem) (theorem; a main declaration), declared in [LeanPool/LehmerE10.lean, line 44](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LehmerE10.lean#L44): “Lehmer's polynomial L(x) = x^10 + x^9 - x^7 - x^6 - x^5 - x^4 - x^3 + x + 1 is irreducible over the integers, and the characteristic polynomial of a Coxeter element of the E10 Weyl group equals L.”
- [`LehmerE10.lehmer_mahlerMeasure`](https://leanpool.github.io/lean-pool/LeanPool/LehmerE10/Mahler.html#LehmerE10.lehmer_mahlerMeasure) (theorem), declared in [LeanPool/LehmerE10/Mahler.lean, line 76](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LehmerE10/Mahler.lean#L76): “The Mahler measure of L equals its Salem root mu, with the unconditional bounds 1 < M(L) < 7/5.”

## Project

- Authors: Dillon Ryan.
- Project repository: [dillon-11/lehmer-E10](https://github.com/dillon-11/lehmer-E10).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 11R06, 11C08, 20F55.
- In Lean Pool: [LeanPool/LehmerE10](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LehmerE10), from the card [LeanPool/projects/lehmer-e10.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/lehmer-e10.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/lehmer-e10.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/lehmer-e10.yaml)
- [Lean Pool at 2b205bf9: LeanPool/LehmerE10](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LehmerE10)
