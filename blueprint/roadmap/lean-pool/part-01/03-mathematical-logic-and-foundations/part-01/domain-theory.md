---
declaration: structure
origin: cited
lean: InfoSys, Domain.Neighborhood.NeighborhoodSystem
statement: formalized
---

# DomainTheory

> Formalizes Dana Scott's domain theory through Scott information systems and PRG-19 neighbourhood systems, including approximable maps, products, function spaces, fixed points, recursive presentations, and initial-algebra constructions for denotational semantics.

*Quoted from the card [LeanPool/projects/domain-theory.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/domain-theory.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`InfoSys`](https://leanpool.github.io/lean-pool/LeanPool/DomainTheory/InfoSys.html#InfoSys) (structure; a main declaration), declared in [LeanPool/DomainTheory/InfoSys.lean, line 55](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/DomainTheory/InfoSys.lean#L55): “Defines Scott information systems, with a distinguished bottom token, finite consistency predicate, entailment relation, and Scott's six axioms.”
- [`Domain.Neighborhood.NeighborhoodSystem`](https://leanpool.github.io/lean-pool/LeanPool/DomainTheory/Neighborhood/Basic.html#Domain.Neighborhood.NeighborhoodSystem) (structure; a main declaration), declared in [LeanPool/DomainTheory/Neighborhood/Basic.lean, line 77](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/DomainTheory/Neighborhood/Basic.lean#L77): “Defines PRG-19 neighbourhood systems, Scott's neighbourhood presentation of domains.”
- [`Domain.Neighborhood.ApproximableMap`](https://leanpool.github.io/lean-pool/LeanPool/DomainTheory/Neighborhood/Approximable.html#Domain.Neighborhood.ApproximableMap) (structure), declared in [LeanPool/DomainTheory/Neighborhood/Approximable.lean, line 127](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/DomainTheory/Neighborhood/Approximable.lean#L127): “Defines approximable maps between neighbourhood systems as relations preserving finite approximations.”
- [`Domain.Neighborhood.trianglelefteq_of_isInitial`](https://leanpool.github.io/lean-pool/LeanPool/DomainTheory/Neighborhood/Theorem616.html#Domain.Neighborhood.trianglelefteq_of_isInitial) (theorem), declared in [LeanPool/DomainTheory/Neighborhood/Theorem616.lean, line 118](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/DomainTheory/Neighborhood/Theorem616.lean#L118): “Proves that an initial algebra for a functor embeds into every other solution through Scott's subdomain relation.”
- `ScottMap.fix_eq`, which the scan does not find declared in the project's files at this commit: “Proves the fixed-point equation for Scott-continuous self maps on complete lattices.”

## Project

- Authors: Catskills Research Company.
- Source: *Domains for Denotational Semantics* by Dana Scott, [doi:10.1007/BFb0012801](https://doi.org/10.1007/BFb0012801).
- Project repository: [catskillsresearch/domain_theory](https://github.com/catskillsresearch/domain_theory).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 03B70, 06B35, 68Q55.
- In Lean Pool: [LeanPool/DomainTheory](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/DomainTheory), from the card [LeanPool/projects/domain-theory.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/domain-theory.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/domain-theory.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/domain-theory.yaml)
- [Lean Pool at bb99e52c: LeanPool/DomainTheory](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/DomainTheory)
