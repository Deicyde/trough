---
declaration: def
origin: cited
lean: TLA.always, TLA.eventually, TLA.always_induction, TLA.wf1
statement: formalized
---

# Lentil: Temporal Logic of Actions in Lean 4

> A shallow embedding of Leslie Lamport's Temporal Logic of Actions (TLA) in Lean 4, with the temporal modalities, standard propositional and temporal proof rules, weak-fairness and leads-to reasoning, and an interactive proof mode for TLA judgments.

*Quoted from the card [LeanPool/projects/lentil.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/lentil.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 6 main results, each with its informal statement quoted from the card. The scan finds 6 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`TLA.always`](https://leanpool.github.io/lean-pool/LeanPool/Lentil/Basic.html#TLA.always) (def; a main declaration), declared in [LeanPool/Lentil/Basic.lean, line 89](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Lentil/Basic.lean#L89): “Defines the TLA "always" (box) temporal modality, asserting a predicate holds on every suffix of an execution.”
- [`TLA.eventually`](https://leanpool.github.io/lean-pool/LeanPool/Lentil/Basic.html#TLA.eventually) (def; a main declaration), declared in [LeanPool/Lentil/Basic.lean, line 91](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Lentil/Basic.lean#L91): “Defines the TLA "eventually" (diamond) temporal modality, asserting a predicate holds on some suffix of an execution.”
- [`TLA.always_induction`](https://leanpool.github.io/lean-pool/LeanPool/Lentil/Rules/Basic.html#TLA.always_induction) (theorem; a main declaration), declared in [LeanPool/Lentil/Rules/Basic.lean, line 154](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Lentil/Rules/Basic.lean#L154): “The always-induction rule, equating `□ p` with `p` together with `□ (p → ◯ p)`.”
- [`TLA.wf1`](https://leanpool.github.io/lean-pool/LeanPool/Lentil/Rules/WF.html#TLA.wf1) (theorem; a main declaration), declared in [LeanPool/Lentil/Rules/WF.lean, line 54](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Lentil/Rules/WF.lean#L54): “The WF1 weak-fairness proof rule deriving a leads-to property from a next-state action under weak fairness.”
- [`TLA.wf_as_leads_to`](https://leanpool.github.io/lean-pool/LeanPool/Lentil/Rules/WF.html#TLA.wf_as_leads_to) (theorem), declared in [LeanPool/Lentil/Rules/WF.lean, line 37](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Lentil/Rules/WF.lean#L37): “Characterizes weak fairness of an action as a leads-to property between its enabledness and its occurrence.”
- [`TLA.leads_to_trans`](https://leanpool.github.io/lean-pool/LeanPool/Lentil/Rules/LeadsTo.html#TLA.leads_to_trans) (theorem), declared in [LeanPool/Lentil/Rules/LeadsTo.lean, line 43](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Lentil/Rules/LeadsTo.lean#L43): “Transitivity of the leads-to relation.”

## Project

- Authors: Qiyuan Zhao.
- Project repository: [verse-lab/Lentil](https://github.com/verse-lab/Lentil).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 03B44, 68Q60.
- In Lean Pool: [LeanPool/Lentil](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Lentil), from the card [LeanPool/projects/lentil.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/lentil.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/lentil.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/lentil.yaml)
- [Lean Pool at 2b205bf9: LeanPool/Lentil](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Lentil)
