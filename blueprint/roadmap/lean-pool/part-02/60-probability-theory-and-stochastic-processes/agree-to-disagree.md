---
declaration: lemma
origin: cited
lean: AgreeToDisagree.agreeToDisagree, AgreeToDisagree.agreeToDisagree_beliefs
statement: formalized
proof: formalized
---

# Aumann's Agreement Theorem

> Formalizes Aumann's agreement theorem for information partitions and a common-prior setting, together with a p-belief variant bounding posterior disagreement by 2 \* (1 - p).

*Quoted from the card [LeanPool/projects/agree-to-disagree.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/agree-to-disagree.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`AgreeToDisagree.agreeToDisagree`](https://leanpool.github.io/lean-pool/LeanPool/AgreeToDisagree/AgreeToDisagree.html#AgreeToDisagree.agreeToDisagree) (lemma; a main declaration), declared in [LeanPool/AgreeToDisagree/AgreeToDisagree.lean, line 226](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/AgreeToDisagree/AgreeToDisagree.lean#L226): “If it is common knowledge at a state that two agents assign fixed posterior probabilities to an event, and the common-knowledge cell has equal posterior under their priors, then the two posterior probabilities are equal.”
- [`AgreeToDisagree.agreeToDisagree'`](https://leanpool.github.io/lean-pool/LeanPool/AgreeToDisagree/AgreeToDisagree.html#AgreeToDisagree.agreeToDisagree') (lemma), declared in [LeanPool/AgreeToDisagree/AgreeToDisagree.lean, line 240](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/AgreeToDisagree/AgreeToDisagree.lean#L240): “Generalizes the agreement theorem to a family of agents indexed by an arbitrary type.”
- [`AgreeToDisagree.agreeToDisagree_beliefs`](https://leanpool.github.io/lean-pool/LeanPool/AgreeToDisagree/AgreeToDisagreeBeliefs.html#AgreeToDisagree.agreeToDisagree_beliefs) (lemma; a main declaration), declared in [LeanPool/AgreeToDisagree/AgreeToDisagreeBeliefs.lean, line 308](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/AgreeToDisagree/AgreeToDisagreeBeliefs.lean#L308): “Proves that common p-belief of fixed posteriors bounds the difference between any two agents' real-valued posteriors by 2 \* (1 - p).”

## Project

- Authors: Ruiz Chen, Ben Eltschig, Ken Ono, Jujian Zhang.
- Source: *We Can't Agree to Disagree, Formally: Aumann's Theorem and Assumption Accounting in Lean*, [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6837298](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6837298).
- Project repository: [AxiomMath/AgreeToDisagree](https://github.com/AxiomMath/AgreeToDisagree).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0, and its notice file gives no copyright line for it.
- MSC2020: 60A10, 91A40.
- In Lean Pool: [LeanPool/AgreeToDisagree](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/AgreeToDisagree), from the card [LeanPool/projects/agree-to-disagree.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/agree-to-disagree.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/agree-to-disagree.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/agree-to-disagree.yaml)
- [Lean Pool at 2b205bf9: LeanPool/AgreeToDisagree](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/AgreeToDisagree)
