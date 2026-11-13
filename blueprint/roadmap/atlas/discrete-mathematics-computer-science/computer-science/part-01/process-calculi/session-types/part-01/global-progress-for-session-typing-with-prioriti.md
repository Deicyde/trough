---
declaration: section
origin: cited
lean: Cslib.SessionTypes.Endpoint.GuardMin, Cslib.SessionTypes.Endpoint.guardMin_rejects_peer, Cslib.SessionTypes.Endpoint.GuardMin.rekey, Cslib.SessionTypes.Endpoint.guardMin_singleton, Cslib.SessionTypes.Endpoint.GuardMin.insert_completed, Cslib.SessionTypes.Endpoint.RankedType, Cslib.SessionTypes.Endpoint.RankedType.hasType, Cslib.SessionTypes.Endpoint.RankedType.out_guard
statement: formalized
proof: formalized
---

# Global progress for session typing with priorities

71 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html).

## Guard priority condition on active endpoints

A guard precedes every other active owned endpoint. Transferred payloads
are included in ownership until transfer; no enabled edge is assumed.

Formalized by `Cslib.SessionTypes.Endpoint.GuardMin`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/Priority.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Priority.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#guard-min).

## An active same-rank peer violates the guard condition

Owning an active peer of the guard at the same rank violates the discipline.

Formalized by `Cslib.SessionTypes.Endpoint.guardMin_rejects_peer`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Priority.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Priority.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#guard-min-rejects-peer).

## Injective rekeying preserves the guard condition

Collision-free rekeying preserves guard inequalities and the exact
same-endpoint exemption; it cannot silently identify the peer role.

Formalized by `Cslib.SessionTypes.Endpoint.GuardMin.rekey`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Priority.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Priority.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#rekey).

## A guard owning only its own endpoint satisfies the condition

A guard with only its own endpoint is permitted to keep using that
endpoint sequentially at the same rank. Only DIFFERENT keys must rank later.

Formalized by `Cslib.SessionTypes.Endpoint.guardMin_singleton`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Priority.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Priority.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#guard-min-singleton).

## Adding a completed role preserves the guard condition

Adding a genuinely completed role introduces no guard dependency.
Completion is checked by the actual unfolded protocol, not a key exemption.

Formalized by `Cslib.SessionTypes.Endpoint.GuardMin.insert_completed`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Priority.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Priority.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#insert-completed).

## Priority-ranked endpoint typing judgement

Linear ownership typing with a strict priority check at every guard.
There is no reduction, enabled-edge, progress or preservation field.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType`, an inductive type declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedTyping.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedTyping.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#ranked-type).

## Forgetting priorities recovers endpoint typing

Forgetting priorities recovers the exact existing ownership judgement.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.hasType`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedTyping.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedTyping.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#has-type).

## Ranked output exposes its subject's guard condition

Output inversion exposes the priority constraint for the actual owned subject.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.out_guard`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedTyping.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedTyping.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#out-guard).

## Ranked input exposes its subject's guard condition

Input inversion exposes the priority constraint before either kind of receive.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.inp_guard`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedTyping.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedTyping.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#inp-guard).

## Nil typing lifts to ranked typing

Nil has no guard: its refinement is exactly the base completed/scoped context.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.nil_of_hasType`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedTyping.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedTyping.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#nil-of-has-type).

## Active roles on other names rank after an input subject

Every other active owned role must rank strictly after an input subject.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.input_other_rank`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedTyping.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedTyping.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#input-other-rank).

## Parallel inversion for ranked typing

Refinement preserves the original disjoint parallel ownership split.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.par_inv`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedTyping.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedTyping.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#par-inv).

## Restriction inversion for ranked typing

Refinement retains the exact protocol/rank pair installed by restriction.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.nu_inv`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedTyping.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedTyping.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#nu-inv).

## Active delegated payloads rank after the guard

Every active delegated payload is included in the pre-transfer guard check.

Formalized by `Cslib.SessionTypes.Endpoint.GuardMin.active_payload_rank`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedTyping.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedTyping.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#active-payload-rank).

## Weakening ranked typing by a completed capability

Adding a fresh completed capability preserves every guard inequality
through all seven rules. No active capability can be added by this theorem.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.weaken_completed`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedResources.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedResources.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#weaken-completed).

## Erasing a role preserves the guard condition

Erasing a role can only remove a dependency from a guard check.

Formalized by `Cslib.SessionTypes.Endpoint.GuardMin.erase`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedResources.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedResources.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#erase).

## Erasing a key whose name is absent preserves ranked typing

Actual all-position physical-name absence permits erasure in the
refinement too. Subject and payload lookup obligations are never discarded.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.erase_nameAbsent`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedResources.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedResources.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#erase-name-absent).

## Weakening ranked typing by a disjoint completed context

Reattaching a disjoint completed finite context preserves all guards.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.weaken_completed_union`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedResources.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedResources.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#weaken-completed-union).

## Collision-free renaming preserves ranked typing

Physical-name rekeying preserves the entire syntax-directed refinement,
including all guard priorities, passive/endpoint payloads and nested binders.
Injectivity is needed only on owned keys, as in the base ownership judgement.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.rename`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedTransport.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedTransport.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#rename).

## Binder lifting preserves ranked typing

Canonical binder lifting preserves every priority and endpoint rank.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.lift`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedTransport.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedTransport.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#lift-3).

## Passive substitution preserves ranked typing

Canonical passive substitution transports all priority guards on lifted
outer ownership. The bound name owns no endpoint capability in this case.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.subst_passive`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedScope.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedScope.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#subst-passive).

## Ranked typing descends from a lifted process

Reflection of an actual lifted term recovers every priority and context entry.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.unlift`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedScope.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedScope.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#unlift).

## Forward scope extrusion preserves ranked typing

Extrusion lifts the partner's real ownership while retaining every guard.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.scope_forward`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedScope.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedScope.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#scope-forward).

## Adding a role unused by the partner preserves ranked typing

Moving a partner-owned role back requires actual absence to DERIVE
completion from plain typing before refined completed weakening is applied.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.insert_from_absent_partner`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedScope.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedScope.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#insert-from-absent-partner).

## Restoring the bound pair preserves ranked typing

Restoring the bound pair adds only absent completed partner roles; all
original active ownership and inequalities of the restricted component remain.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.restore_scope_pair`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedScope.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedScope.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#restore-scope-pair).

## Reverse scope extrusion preserves ranked typing

Reverse extrusion derives the entire outer ownership split from typing,
removes only genuinely absent partner roles and retains all guard inequalities.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.scope_reverse`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedScope.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedScope.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#scope-reverse).

## Ranked typing is invariant under scope extrusion

Exact bidirectional canonical scope transport for the same refinement.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.scope_iff`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedScope.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedScope.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#scope-iff).

## Endpoint substitution preserves ranked typing

Endpoint substitution transports every ranked subject and payload guard
with freshness derived from the actual linear ownership split.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.subst_endpoint`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedCommunication.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedCommunication.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#subst-endpoint).

## Disjoint split supplies freshness for endpoint substitution

The transmitted role's non-aliasing is derived, not a readiness premise.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.subst_endpoint_from_split`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedCommunication.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedCommunication.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#subst-endpoint-from-split).

## Inversion of ranked input typing

Ranked input inversion retains both literal payload sorts and all guards.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.inp_inv`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedCommunication.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedCommunication.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#inp-inv).

## Inversion of ranked output typing

Ranked output inversion retains the pre-transfer active payload check.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.out_inv`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedCommunication.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedCommunication.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#out-inv).

## Passive head communication preserves ranked typing

With the stated disjoint ranked split, scoped passive payload and
compatible combined interface, head communication substitutes through the
ranked input body and retains both residual guard derivations.

Formalized by `Cslib.SessionTypes.Endpoint.ranked_passive_head`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedCommunication.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedCommunication.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#ranked-passive-head).

## Endpoint delegation at the head preserves ranked typing

With the stated disjoint ranked split, owned non-carrier scoped payload
and compatible combined interface, delegation derives substitution freshness
from that split and retains the combined payload value.

Formalized by `Cslib.SessionTypes.Endpoint.ranked_endpoint_head`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedCommunication.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedCommunication.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#ranked-endpoint-head).

## Ranked head communication exposes peers and residual typing

A ranked-typed opposite-head pair at an initially compatible interface
yields the actual subject/dual-peer heads, payload metadata and exact ranked
continuation context after literal communication.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.head_comm_faithful`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedCommunication.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedCommunication.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#head-comm-faithful).

## Ranked head communication yields a dual advance

For a ranked-typed opposite-head pair at a compatible initial interface,
the head result yields one faithful update and compatible ranked residual,
not a typing witness manufactured by forgetting the refinement.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.head_comm_advance`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedCommunication.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedCommunication.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#head-comm-advance).

## Parallel commutation preserves ranked typing

Commutation retains the actual disjoint split and both ranked subterms.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.par_comm`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedCong.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedCong.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#par-comm).

## Parallel reassociation preserves ranked typing

Reassociation derives all pairwise disjointness from actual typing.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.par_assoc`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedCong.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedCong.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#par-assoc).

## Reverse parallel reassociation preserves ranked typing

Reverse reassociation retains exact contexts and guard checks.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.par_assoc_reverse`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedCong.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedCong.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#par-assoc-reverse).

## Removing a parallel nil preserves ranked typing

Nil's actual completed ownership can be reattached without new dependencies.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.par_nil_elim`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedCong.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedCong.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#par-nil-elim).

## Adding a parallel nil preserves ranked typing

Nil introduction allocates an empty ownership context, not an active frame.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.par_nil_intro`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedCong.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedCong.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#par-nil-intro).

## Removing a restriction around nil preserves ranked typing

Restricting nil is equivalent to its original completed/scoped interface.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.nu_nil_elim`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedCong.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedCong.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#nu-nil-elim).

## Restricting nil preserves ranked typing

A completed fresh pair can be introduced around nil without changing guards.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.nu_nil_intro`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedCong.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedCong.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#nu-nil-intro).

## Swapping two restrictions preserves ranked typing

Swapping the two restrictions preserves all guard constraints by the
GENERAL capture-safe rename theorem and the exact four-role context equation.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.nu_swap`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedCong.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedCong.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#nu-swap).

## Reverse restriction swap preserves ranked typing

Reverse restriction swap uses the canonical process involution.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.nu_swap_reverse`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedCong.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedCong.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#nu-swap-reverse).

## Structural congruence preserves ranked typing

Every canonical Cong constructor preserves the whole priority refinement
at exactly the same context and ambient depth. Unsupported sum/replication
constructors are impossible by the invariant DERIVED from refinement typing.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.cong_iff`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedCong.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedCong.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#cong-iff).

## Parallel guard frontier

A parallel frontier consists of nil and actual input/output guards.
No restriction is hidden under parallel; guarded continuations are unrestricted.

Formalized by `Cslib.SessionTypes.Endpoint.GuardFrontier`, an inductive type declared in [CSLibExt/Languages/SessionTypes/Endpoint/FrontierNormalization.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/FrontierNormalization.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#guard-frontier).

## Frontier normal form of finite networks

A finite network normal form has all unguarded restrictions outside its
parallel frontier. The binder tower can have any finite depth.

Formalized by `Cslib.SessionTypes.Endpoint.FrontierNormal`, an inductive type declared in [CSLibExt/Languages/SessionTypes/Endpoint/FrontierNormalization.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/FrontierNormalization.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#frontier-normal).

## Lifting preserves guard frontiers

Lifting maps every frontier subject, payload and guarded continuation.

Formalized by `Cslib.SessionTypes.Endpoint.GuardFrontier.lift`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/FrontierNormalization.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/FrontierNormalization.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#lift).

## Lifting preserves frontier normal form

Lifting preserves the restriction tower and increments cutoff under binders.

Formalized by `Cslib.SessionTypes.Endpoint.FrontierNormal.lift`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/FrontierNormalization.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/FrontierNormalization.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#lift-2).

## Parallel composition of frontier normal forms normalizes

Two normalized components combine by actual canonical scope extrusion.
Every private restriction, on either side, is retained in the resulting tower.

Formalized by `Cslib.SessionTypes.Endpoint.FrontierNormal.parallel`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/FrontierNormalization.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/FrontierNormalization.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#parallel).

## Every finite linear π term has a frontier normal form

GENERAL normalization of every finite-linear existing π term. Prefix
bodies are not evaluated or replaced, and no complementary ready pair is assumed.

Formalized by `Cslib.SessionTypes.Endpoint.finiteLinear_frontier_normal`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/FrontierNormalization.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/FrontierNormalization.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#finite-linear-frontier-normal).

## Ranked-typed processes have a typed frontier normal form

Ranked normalization is DERIVED from typing, preserving every guard and
all external ownership while exposing all unguarded private restrictions.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.frontier_normal`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/FrontierNormalization.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/FrontierNormalization.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#frontier-normal-2).

## Send heads are active for both payload sorts

Every literal communication head is active, for both payload sorts.

Formalized by `Cslib.SessionTypes.Endpoint.SendsTo.active`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/FrontierMinimum.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/FrontierMinimum.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#active).

## A minimum active role owned by a guard is its subject key

A minimum active role owned by a prefix must be that prefix's exact
subject key, not merely a same-name role. Every other key ranks later.

Formalized by `Cslib.SessionTypes.Endpoint.minimum_guard_key`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/FrontierMinimum.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/FrontierMinimum.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#minimum-guard-key).

## Ranked output subjects are active

Literal output subjects have an active protocol, without any stored
reduction or exposed-ready-pair evidence.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.out_active`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/FrontierMinimum.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/FrontierMinimum.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#out-active).

## Ranked input subjects are active

Literal input subjects likewise own active receive heads.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.inp_active`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/FrontierMinimum.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/FrontierMinimum.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#inp-active).

## Minimum active role is the subject of a frontier leaf

A minimum active role is exposed as the EXACT subject of an actual leaf.
The disjoint ownership split and canonical rearrangement are DERIVED outputs;
no ready guard or normalizing typing result is required from the caller.

Formalized by `Cslib.SessionTypes.Endpoint.GuardFrontier.expose_minimum`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/FrontierMinimum.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/FrontierMinimum.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#expose-minimum).

## Existence of a least-rank active binding

A nonempty collection of active finite-map bindings has a least rank.
The witness ranges over ALL active roles, not only input guards.

Formalized by `Cslib.SessionTypes.Endpoint.Context.active_minimum`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/FrontierMinimum.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/FrontierMinimum.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#active-minimum).

## Completed ranked frontiers are congruent to nil

A frontier with no active ownership cannot contain a live prefix.
Completion is the PROCESS congruence to nil, not a completed empty interface.

Formalized by `Cslib.SessionTypes.Endpoint.GuardFrontier.completed_nil`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/FrontierMinimum.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/FrontierMinimum.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#completed-nil).

## Duality preserves activity of a capability

Activity is preserved by protocol duality, including regular unfolding.

Formalized by `Cslib.SessionTypes.Endpoint.Capability.dual_active`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/FrontierMinimum.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/FrontierMinimum.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#dual-active).

## Minimum guard leaf cannot own its dual peer

A minimum active role's peer cannot be owned by the same guard leaf.
Equal-rank opposite keys violate the actual pre-action GuardMin constraint.

Formalized by `Cslib.SessionTypes.Endpoint.minimum_peer_separate`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/FrontierMinimum.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/FrontierMinimum.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#minimum-peer-separate).

## Same-name ranked guards are opposite and communicate

Given disjoint ranked-typed leaves with literal same-name input/output
guard shapes and a compatible combined interface, their directions are opposite.
The Step is canonical commSelect, possibly after parallel commutation.

Formalized by `Cslib.SessionTypes.Endpoint.same_name_guards_step`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/FrontierProgress.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/FrontierProgress.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#same-name-guards-step).

## Progress for balanced ranked guard frontiers

GENERAL balanced ranked frontier progress. A minimum over ALL active
owned roles exposes two distinct opposite subject leaves, from which actual
canonical communication follows. Completion is process-level Cong to nil.

Formalized by `Cslib.SessionTypes.Endpoint.GuardFrontier.progress`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/FrontierProgress.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/FrontierProgress.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#progress).

## Binding a fresh dual pair preserves balance

A fresh private pair preserves full dual ownership of an outer balanced
interface. Every nonfresh owned role is reflected through canonical lifting.

Formalized by `Cslib.SessionTypes.Endpoint.Balanced.bind`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/FrontierProgress.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/FrontierProgress.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#bind).

## Subject reduction for ranked typing at compatible interfaces

From a ranked-typed source with an initially compatible interface, every
actual canonical step preserves the refinement and compatibility, with zero
or one actual external matched subject advancement.
Private head/continuation changes are derived from faithful bound projection.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.subject_reduction`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedReduction.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedReduction.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#subject-reduction).

## Ranked subject reduction at balanced interfaces

For a ranked-typed source, initial balance supplies compatibility and is
preserved by the actual canonical step and its exact update.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.subject_reduction_balanced`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedReduction.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedReduction.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#subject-reduction-balanced).

## Ranked subject reduction at the empty interface

Empty-interface ranked typing is preserved by any canonical step at any
ambient depth and through pre/post congruence. The empty context supplies
balance and therefore the required compatibility.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.subject_reduction_empty`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedReduction.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RankedReduction.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#subject-reduction-empty).

## Global progress of ranked processes at balanced interfaces

For a ranked-typed process at ANY balanced interface, global progress
holds, including disconnected networks.
All private channels are tracked through the derived restriction tower.
Completion means process congruence to nil, not completion of the interface.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.progress_balanced`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/GlobalProgress.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/GlobalProgress.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#progress-balanced).

## Closed ranked networks are completed or can step

A closed finite ranked network is completed or takes an ACTUAL canonical
step. Ambient passive-name depth is arbitrary; no readiness witness is supplied.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.progress_empty`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/GlobalProgress.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/GlobalProgress.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#progress-empty).

## Reachable states of closed ranked networks stay typed

Every state reached by finitely many actual canonical steps retains exact
empty-interface ranked typing. This is preservation, not finite termination.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.reachable_empty`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/GlobalProgress.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/GlobalProgress.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#reachable-empty).

## Progress at reachable states of closed ranked networks

Global progress holds at every finite reachable state of a closed ranked
network. No fairness, eventual liveness or recursive termination is asserted.

Formalized by `Cslib.SessionTypes.Endpoint.RankedType.reachable_progress`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/GlobalProgress.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/GlobalProgress.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html#reachable-progress).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Global progress for session typing with priorities](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/process-calculi/session-types/global-progress-for-session-typing-with-prioriti)
