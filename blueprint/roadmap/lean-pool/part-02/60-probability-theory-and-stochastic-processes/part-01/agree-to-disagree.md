---
declaration: lemma
origin: cited
lean: AgreeToDisagree.agreeToDisagree, AgreeToDisagree.agreeToDisagree_beliefs
statement: formalized
proof: formalized
---

# Aumann's Agreement Theorem

> Formalizes Aumann's agreement theorem for information partitions and a common-prior setting, together with a p-belief variant bounding posterior disagreement by 2 \* (1 - p).

*Quoted from the card [LeanPool/projects/agree-to-disagree.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/agree-to-disagree.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`AgreeToDisagree.agreeToDisagree`](https://leanpool.github.io/lean-pool/LeanPool/AgreeToDisagree/AgreeToDisagree.html#AgreeToDisagree.agreeToDisagree) (lemma; a main declaration), declared in [LeanPool/AgreeToDisagree/AgreeToDisagree.lean, line 227](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/AgreeToDisagree/AgreeToDisagree.lean#L227): “If it is common knowledge at a state that two agents assign fixed posterior probabilities to an event, and the common-knowledge cell has equal posterior under their priors, then the two posterior probabilities are equal.”
- [`AgreeToDisagree.agreeToDisagree'`](https://leanpool.github.io/lean-pool/LeanPool/AgreeToDisagree/AgreeToDisagree.html#AgreeToDisagree.agreeToDisagree') (lemma), declared in [LeanPool/AgreeToDisagree/AgreeToDisagree.lean, line 241](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/AgreeToDisagree/AgreeToDisagree.lean#L241): “Generalizes the agreement theorem to a family of agents indexed by an arbitrary type.”
- [`AgreeToDisagree.agreeToDisagree_beliefs`](https://leanpool.github.io/lean-pool/LeanPool/AgreeToDisagree/AgreeToDisagreeBeliefs.html#AgreeToDisagree.agreeToDisagree_beliefs) (lemma; a main declaration), declared in [LeanPool/AgreeToDisagree/AgreeToDisagreeBeliefs.lean, line 308](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/AgreeToDisagree/AgreeToDisagreeBeliefs.lean#L308): “Proves that common p-belief of fixed posteriors bounds the difference between any two agents' real-valued posteriors by 2 \* (1 - p).”

## Project

- Authors: Ruiz Chen, Ben Eltschig, Ken Ono, Jujian Zhang.
- Source: *We Can't Agree to Disagree, Formally: Aumann's Theorem and Assumption Accounting in Lean*, [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6837298](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6837298).
- Project repository: [AxiomMath/AgreeToDisagree](https://github.com/AxiomMath/AgreeToDisagree).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0.
- MSC2020: 60A10, 91A40.
- In Lean Pool: [LeanPool/AgreeToDisagree](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/AgreeToDisagree), from the card [LeanPool/projects/agree-to-disagree.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/agree-to-disagree.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/agree-to-disagree.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/agree-to-disagree.yaml)
- [Lean Pool at bb99e52c: LeanPool/AgreeToDisagree](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/AgreeToDisagree)
