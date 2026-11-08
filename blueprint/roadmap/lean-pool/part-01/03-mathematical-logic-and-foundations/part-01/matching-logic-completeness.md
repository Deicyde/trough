---
declaration: theorem
origin: cited
lean: MatchingLogic.global_completeness_entryIII
statement: formalized
proof: formalized
---

# Global completeness of one-sorted definedness-free matching logic

> Formalizes the one-sorted case of Chen and Roșu's global-completeness argument and independently discharges its local-completeness oracle by mechanizing the canonical-model construction from their 2019 Matching μ-Logic technical report (Theorem 73, Lemmas 80–81, and strong local completeness Theorem 83). The resulting theorem supplies both local completeness and soundness for countably infinite variable types.

*Quoted from the card [LeanPool/projects/matching-logic-completeness.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/matching-logic-completeness.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`MatchingLogic.locality`](https://leanpool.github.io/lean-pool/LeanPool/MatchingLogic/Locality.html#MatchingLogic.locality) (theorem), declared in [LeanPool/MatchingLogic/Locality.lean, line 73](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MatchingLogic/Locality.lean#L73): “For a backward-closed subset of a matching-logic model, two valuations that agree inside the subset and both stay outside it otherwise give identical denotations after restriction to that subset.”
- [`MatchingLogic.two_copies`](https://leanpool.github.io/lean-pool/LeanPool/MatchingLogic/DoubleCover.html#MatchingLogic.two_copies) (theorem), declared in [LeanPool/MatchingLogic/DoubleCover.lean, line 81](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MatchingLogic/DoubleCover.lean#L81): “The double-cover model over a nonempty backward-closed proper subset has exactly the denotation predicted by each of its two projections back to the original model.”
- [`MatchingLogic.semantic_localization`](https://leanpool.github.io/lean-pool/LeanPool/MatchingLogic/Composite.html#MatchingLogic.semantic_localization) (theorem), declared in [LeanPool/MatchingLogic/Composite.lean, line 151](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MatchingLogic/Composite.lean#L151): “For a closed theory and closed conclusion, global semantic consequence is equivalent to local consequence from the localized theory.”
- [`MatchingLogic.strongLocalCompleteness`](https://leanpool.github.io/lean-pool/LeanPool/MatchingLogic/EntryIII/Conclusion.html#MatchingLogic.strongLocalCompleteness) (theorem), declared in [LeanPool/MatchingLogic/EntryIII/Conclusion.lean, line 58](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MatchingLogic/EntryIII/Conclusion.lean#L58): “One-sorted basic matching logic has strong local completeness over an arbitrary one-sorted finitary signature when the element-variable type is countably infinite.”
- [`MatchingLogic.global_completeness_entryIII`](https://leanpool.github.io/lean-pool/LeanPool/MatchingLogic/EntryIII/Conclusion.html#MatchingLogic.global_completeness_entryIII) (theorem; a main declaration), declared in [LeanPool/MatchingLogic/EntryIII/Conclusion.lean, line 67](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MatchingLogic/EntryIII/Conclusion.lean#L67): “For a one-sorted finitary signature, closed premises and conclusion, and a countably infinite element-variable type, global semantic consequence is equivalent to derivability, with both soundness and local completeness discharged.”

## Project

- Authors: Aurélien Eveil, Anthropic, OpenAI.
- Source: *Completeness and incompleteness of basic matching logic; Matching μ-Logic (2019 technical report)* by Xiaohong Chen, Grigore Roșu, [arXiv:2608.13306](https://arxiv.org/abs/2608.13306), [https://hdl.handle.net/2142/102281](https://hdl.handle.net/2142/102281).
- Project repository: [eveil-labs/matching-logic-lean](https://github.com/eveil-labs/matching-logic-lean), at commit [4628a26b](https://github.com/eveil-labs/matching-logic-lean/tree/4628a26bb2db117de1a11cbedcb620db9124cdb8).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 03B45, 03B70.
- In Lean Pool: [LeanPool/MatchingLogic](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MatchingLogic), from the card [LeanPool/projects/matching-logic-completeness.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/matching-logic-completeness.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/matching-logic-completeness.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/matching-logic-completeness.yaml)
- [Lean Pool at 2b205bf9: LeanPool/MatchingLogic](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MatchingLogic)
