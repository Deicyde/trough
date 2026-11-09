---
declaration: structure
origin: cited
lean: EventStructures.EventStructure, EventStructures.Conf
statement: formalized
---

# Event Structures and Causal-Consistent Reversibility

> Formalizes event structures with binary conflict, their configurations, computations, the trace monoid, and causal-consistent reversibility, proving correctness and causal-safety of rollback, uniqueness of minimal and maximal replays, and conditional replay-existence characterizations.

*Quoted from the card [LeanPool/projects/event-structures.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/event-structures.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 6 main results, each with its informal statement quoted from the card. The scan finds 6 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`EventStructures.EventStructure`](https://leanpool.github.io/lean-pool/LeanPool/EventStructures/Basic.html#EventStructures.EventStructure) (structure; a main declaration), declared in [LeanPool/EventStructures/Basic.lean, line 25](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EventStructures/Basic.lean#L25): “Defines an event structure as a partially ordered set of events with an irreflexive symmetric conflict relation.” Its source, as the card gives it: “M. Nielsen, G. Plotkin, G. Winskel, Petri nets, event structures and domains, part I, Theoretical Computer Science 13 (1981), 85-108, doi:10.1016/0304-3975(81)90112-2.”
- [`EventStructures.Conf`](https://leanpool.github.io/lean-pool/LeanPool/EventStructures/Configuration.html#EventStructures.Conf) (def; a main declaration), declared in [LeanPool/EventStructures/Configuration.lean, line 33](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EventStructures/Configuration.lean#L33): “Defines a configuration as a conflict-free, downward-closed set of events.” Its source, as the card gives it: “G. Winskel, Event structures, Advances in Petri Nets 1986, LNCS 255, Springer, 1987, 325-392, doi:10.1007/3-540-17906-2_31.”
- [`EventStructures.Rollback.rollback_correctness_finite`](https://leanpool.github.io/lean-pool/LeanPool/EventStructures/Rollback.html#EventStructures.Rollback.rollback_correctness_finite) (lemma), declared in [LeanPool/EventStructures/Rollback.lean, line 232](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EventStructures/Rollback.lean#L232): “Proves that the original configuration is reachable from the rollback of an event when the configuration is finitely representable.” Its source, as the card gives it: “Causal-consistent reversibility in the sense of V. Danos, J. Krivine, Reversible communicating systems, CONCUR 2004, LNCS 3170, Springer, 2004, 292-307, doi:10.1007/978-3-540-28644-8_19.”
- [`EventStructures.Rollback.rollback_causal_safety`](https://leanpool.github.io/lean-pool/LeanPool/EventStructures/Rollback.html#EventStructures.Rollback.rollback_causal_safety) (lemma), declared in [LeanPool/EventStructures/Rollback.lean, line 104](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EventStructures/Rollback.lean#L104): “Proves causal safety of rollback - events causally after the rolled-back event are removed.” Its source, as the card gives it: “Causal-consistent reversibility in the sense of V. Danos, J. Krivine, Reversible communicating systems, CONCUR 2004, LNCS 3170, Springer, 2004, 292-307, doi:10.1007/978-3-540-28644-8_19.”
- [`EventStructures.Replay.minReplay_unique`](https://leanpool.github.io/lean-pool/LeanPool/EventStructures/Replay.html#EventStructures.Replay.minReplay_unique) (lemma), declared in [LeanPool/EventStructures/Replay.lean, line 186](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EventStructures/Replay.lean#L186): “Proves uniqueness of the minimal replay of a log - any two minimal replays compatible with the log reach the same configuration.”
- [`EventStructures.Trace.TraceMonoid`](https://leanpool.github.io/lean-pool/LeanPool/EventStructures/Trace.html#EventStructures.Trace.TraceMonoid) (def), declared in [LeanPool/EventStructures/Trace.lean, line 108](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EventStructures/Trace.lean#L108): “Defines the trace monoid as lists of events quotiented by the congruence generated by swapping adjacent concurrent events; paths in the configuration graph are quotiented by the same trace equivalence to form asynchronous paths.” Its source, as the card gives it: “A. Mazurkiewicz, Trace theory, Advances in Petri Nets 1986, LNCS 255, Springer, 1987, 278-324, doi:10.1007/3-540-17906-2_30.”

## Project

- Authors: Vikraman Choudhury.
- Source: [doi:10.1007/3-540-17906-2_31](https://doi.org/10.1007/3-540-17906-2_31).
- Project repository: [vikraman/event-structures](https://github.com/vikraman/event-structures).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 68Q85, 06A06.
- In Lean Pool: [LeanPool/EventStructures](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EventStructures), from the card [LeanPool/projects/event-structures.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/event-structures.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/event-structures.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/event-structures.yaml)
- [Lean Pool at 2b205bf9: LeanPool/EventStructures](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EventStructures)
