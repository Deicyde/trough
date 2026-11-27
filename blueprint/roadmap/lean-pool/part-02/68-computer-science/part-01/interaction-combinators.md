---
declaration: theorem
origin: cited
lean: INet.Comb.universal, INet.Comb.universal_strict
statement: formalized
proof: formalized
---

# Lafont's interaction combinators

> Formalizes interaction nets, reduction modulo wire substitutions, strong confluence, and Lafont's construction of a strict translation from any well-formed interaction system over a finite signature into the three interaction combinators.

*Quoted from the card [LeanPool/projects/interaction-combinators.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/interaction-combinators.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`INet.Comb.universal`](https://leanpool.github.io/lean-pool/LeanPool/InteractionCombinators/Universality/Theorem1.html#INet.Comb.universal) (theorem; a main declaration), declared in [LeanPool/InteractionCombinators/Universality/Theorem1.lean, line 36](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/InteractionCombinators/Universality/Theorem1.lean#L36): “Every well-formed interaction system over a finite signature translates into Lafont's system of three interaction combinators, with rule reductions simulated up to wire equivalence.”
- [`INet.Comb.universal_strict`](https://leanpool.github.io/lean-pool/LeanPool/InteractionCombinators/Universality/Theorem1.html#INet.Comb.universal_strict) (theorem; a main declaration), declared in [LeanPool/InteractionCombinators/Universality/Theorem1.lean, line 45](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/InteractionCombinators/Universality/Theorem1.lean#L45): “The translation can be chosen so that the image of every source symbol begins with a cell.”

## Project

- Authors: Lorenzo Battistela.
- Source: *Interaction Combinators* by Yves Lafont, [doi:10.1006/inco.1997.2643](https://doi.org/10.1006/inco.1997.2643).
- Project repository: [Lorenzobattistela/interaction-combinators-lean](https://github.com/Lorenzobattistela/interaction-combinators-lean), at commit [7400551e](https://github.com/Lorenzobattistela/interaction-combinators-lean/tree/7400551e918781e674808e0040172118028d2968).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 68Q42, 03B70.
- In Lean Pool: [LeanPool/InteractionCombinators](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/InteractionCombinators), from the card [LeanPool/projects/interaction-combinators.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/interaction-combinators.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/interaction-combinators.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/interaction-combinators.yaml)
- [Lean Pool at bb99e52c: LeanPool/InteractionCombinators](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/InteractionCombinators)
