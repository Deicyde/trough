---
declaration: theorem
origin: cited
lean: SiegelThmLib.siegel
statement: formalized
proof: formalized
---

# Siegel's lower bound for real Dirichlet L-functions

> Proves the ineffective uniform lower bound for the value at one of every non-principal real Dirichlet character, including imprimitive characters. Preserves bounded-character-sum and Mellin integral infrastructure, positivity of the auxiliary Dirichlet coefficients, and Goldfeld's exceptional-zero argument.

*Quoted from the card [LeanPool/projects/siegel.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/siegel.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists one main result, with its informal statement quoted from the card. The scan finds its declaration in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`SiegelThmLib.siegel`](https://leanpool.github.io/lean-pool/LeanPool/Siegel/Main.html#SiegelThmLib.siegel) (theorem; a main declaration), declared in [LeanPool/Siegel/Main.lean, line 268](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Siegel/Main.lean#L268): “For every positive epsilon there is a positive constant depending only on epsilon such that the absolute value of L(1, chi) is at least that constant times the modulus to the power minus epsilon, for every non-principal character whose square is principal.”

## Project

- Authors: Juan Pablo Traverso Gianini.
- Source: *A Simple Proof of Siegel's Theorem*, [doi:10.1073/pnas.71.4.1055](https://doi.org/10.1073/pnas.71.4.1055).
- Project repository: [jtraverso/siegel-theorem](https://github.com/jtraverso/siegel-theorem), at commit [dbe93533](https://github.com/jtraverso/siegel-theorem/tree/dbe9353374a11317bdd2d436e264536258c5762f).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 11M20, 11M06.
- In Lean Pool: [LeanPool/Siegel](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Siegel), from the card [LeanPool/projects/siegel.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/siegel.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/siegel.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/siegel.yaml)
- [Lean Pool at bb99e52c: LeanPool/Siegel](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Siegel)
