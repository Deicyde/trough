---
declaration: section
origin: cited
lean: Cslib.SessionTypes.Endpoint.Runtime.offered_select, Cslib.SessionTypes.Endpoint.Runtime.offered_step, Cslib.SessionTypes.Endpoint.Runtime.Offered.step, Cslib.SessionTypes.Endpoint.Runtime.Offered.reachable, Cslib.SessionTypes.Endpoint.Runtime.Available, Cslib.SessionTypes.Endpoint.Runtime.available_iff_offered, Cslib.SessionTypes.Endpoint.Runtime.Available.cong_iff, Cslib.SessionTypes.Endpoint.Runtime.Available.step
statement: formalized
proof: formalized
---

# Recursive sessions through replicated services

74 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html).

## Selection preserves persistent offers

Choice selection cannot discard a persistent SOURCE offer: sums do not expose
OfferedIn, and selecting an actual communicating guard exposes no persistent offer.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.offered_select`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/PersistentOffers.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/PersistentOffers.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#offered-select).

## Persistent service offers survive one reduction step

ALL5 canonical Step rules retain every actual persistent source service offer.
This is valid for arbitrary Pi syntax, WITHOUT a HasType premise.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.offered_step`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/PersistentOffers.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/PersistentOffers.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#offered-step).

## Declared signature offers survive one reduction step

Exact declared signature lookup plus an actual persistent offer is retained
by every canonical Step, at unchanged shared environment/signature.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.Offered.step`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/PersistentOffers.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/PersistentOffers.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#step).

## Declared signature offers survive finite reduction

Every finite actual reduction preserves each SOURCE persistent signature offer.
No liveness, all-schedules fairness or eventual service invocation is asserted.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.Offered.reachable`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/PersistentOffers.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/PersistentOffers.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#reachable).

## Availability of all declared services

Every declared shared signature has an ACTUAL persistent offer in current syntax.
There is NO typing, Step, future trace, ready pair or step-closure field.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.Available`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/PersistentOffers.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/PersistentOffers.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#available).

## Availability as offers of all declared signatures

Availability is exactly current declared signature lookup plus persistent syntax.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.available_iff_offered`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/PersistentOffers.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/PersistentOffers.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#available-iff-offered).

## Structural congruence preserves service availability

All canonical structural laws preserve current syntactic availability.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.Available.cong_iff`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/PersistentOffers.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/PersistentOffers.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#cong-iff).

## Service availability survives one reduction step

Strong actual syntactic availability survives ANY canonical Step.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.Available.step`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/PersistentOffers.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/PersistentOffers.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#step-2).

## Service availability survives finite reduction

Finite actual reductions preserve source syntactic availability; preservation
is PROVED here, not encoded into its definition. This is not a progress theorem.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.Available.reachable`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/PersistentOffers.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/PersistentOffers.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#reachable-2).

## Idle processes have no unguarded output

Idle is syntax-only and excludes a canonical exposed output, including
inside parallel, restriction and inert replicated templates.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.Idle.no_unguarded_output`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveQuiescence.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveQuiescence.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#no-unguarded-output).

## Idle processes cannot step

Idle services cannot Step, even through arbitrary canonical congruence.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.Idle.no_step`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveQuiescence.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveQuiescence.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#no-step).

## Invoking a replicated service is a reduction step

Canonical replication unfolds and communicates on a real shared trigger.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.service_invocation_step`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#service-invocation-step).

## One-state recurring send graph

Every edge of this reachable one-state graph performs a session send.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.recurringGraph`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#recurring-graph).

## Recurring send protocol

Initial cursor of the one-state recurring send protocol.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.recurringProtocol`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#recurring-protocol).

## Fixed-rank capability of the recurring session

The recurring session keeps one literal static capability rank throughout.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.recurringCap`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#recurring-cap).

## The recurring protocol unfolds to a send of itself

Literal guarded self-loop unfolding, not an unreachable extra graph node.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.recurring_unfold`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#recurring-unfold).

## The dual recurring protocol unfolds to a receive of itself

The peer's literal guarded cursor returns to the same receive protocol.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.recurring_dual_unfold`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#recurring-dual-unfold).

## Sender worker process

Worker code has one session action and a real endpoint-transfer reentry.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.senderWorker`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#sender-worker).

## Receiver worker process

A received session endpoint survives the worker's passive input binder.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.receiverWorker`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#receiver-worker).

## Replicated sender daemon

Sender replication captures only shared constants and its per-invocation formal.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.senderDaemon`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#sender-daemon).

## Replicated receiver daemon

Receiver replication likewise receives, rather than captures, its endpoint.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.receiverDaemon`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#receiver-daemon).

## Sender-role transfer to its trigger

Transfer the actual sender-role endpoint to its shared trigger.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.senderRequest`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#sender-request).

## Receiver-role transfer to its trigger

Transfer the actual opposite-role endpoint to its shared trigger.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.receiverRequest`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#receiver-request).

## Pending state with two role transfers

Persistent services plus TWO pending role transfers, on one physical endpoint.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.pending`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#pending).

## State after the sender trigger invocation

After one trigger invocation, the opposite request and both daemons remain.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.sentInvoked`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#sent-invoked).

## State after both trigger invocations

Both received-role workers can now communicate on their actual session name.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.bothInvoked`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#both-invoked).

## Substitution instantiates the sender worker's endpoint

Capture-safe first trigger communication instantiates the actual bound endpoint.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.sender_subst`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#sender-subst).

## Substitution instantiates the receiver worker's endpoint

Receiver preserves the actual endpoint under its inner passive input binder.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.receiver_subst`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#receiver-subst).

## Pending state steps by invoking the sender trigger

The first real trigger Step, leaving both persistent daemons untouched.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.sender_invocation`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#sender-invocation).

## Sender-invoked state steps by invoking the receiver trigger

The second actual trigger Step, not a pre-generated finite unrolling.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.receiver_invocation`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#receiver-invocation).

## Interchange law for four parallel components

Four canonical parallel components regroup without evaluating any body.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.parallel_interchange`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#parallel-interchange).

## Data substitution yields the receiver's return request

A passive input removes ONLY its data binder, retaining the actual endpoint.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.receiver_return_subst`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#receiver-return-subst).

## Session action steps back to the pending state

Actual session action restores BOTH pending endpoint-role transfers and daemons.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.session_and_reentry`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveTrigger.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#session-and-reentry).

## Sender service signature of the recurring example

Static sender and receiver permissions use opposite roles, exact rank7 types.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.senderSignature`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#sender-signature).

## Receiver service signature of the recurring example

Opposite-role receive permission retains the exact literal dual capability.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.receiverSignature`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#receiver-signature).

## Service environment declaring the two triggers

Two distinct declared constant triggers; declaration alone is not an offer.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.services`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#services).

## Endpoint distinct from both service triggers

Session endpoints are physically distinct from BOTH declared shared triggers.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.EndpointFresh`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#endpoint-fresh).

## The sender trigger declares the sender signature

Actual sender signature lookup with literal role, cap rank and raw protocol.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.sender_declared`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#sender-declared).

## The receiver trigger declares the receiver signature

The other trigger declares exactly the opposite-role receive permission.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.receiver_declared`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#receiver-declared).

## Lifting preserves trigger freshness of an endpoint

Actual canonical lifting cannot turn a distinct endpoint into a service constant.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.EndpointFresh.lift`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#lift).

## A fresh endpoint singleton is separated from the triggers

The exact actual-role singleton does not capture a shared trigger as a linear name.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.endpoint_separated`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#endpoint-separated).

## Erasing a singleton's only key leaves the empty map

Erasing the actual sole endpoint leaves exactly the empty ownership map.
Shared by request and delegation consumers instead of duplicating lookup proofs.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.erase_singleton`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#erase-singleton).

## Nil is runtime-typed with empty ownership

Nil embeds the finite ranked fragment with genuinely empty ownership.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.nil_typed`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#nil-typed).

## The sender reentry request is runtime-typed

Reentry transfers the actual sender capability out, preserving role/rank/code.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.sender_request_typed`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#sender-request-typed).

## The receiver reentry request is runtime-typed

Reentry of the opposite role likewise consumes EXACTLY its own linear slot.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.receiver_request_typed`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#receiver-request-typed).

## The sender worker is runtime-typed

One linear session send keeps the same actual guarded protocol cursor and rank.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.sender_worker_typed`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#sender-worker-typed).

## The receiver worker is runtime-typed

One receive retains the outer received endpoint through its passive input binder.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.receiver_worker_typed`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#receiver-worker-typed).

## The sender daemon is typed with empty ownership

The sender daemon starts with NO captured linear capability, only its fresh formal.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.sender_daemon_typed`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#sender-daemon-typed).

## The receiver daemon is typed with empty ownership

The receiver daemon likewise captures no linear endpoint, in either orientation.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.receiver_daemon_typed`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#receiver-daemon-typed).

## Two-role linear interface of the recurring session

Actual linear interface, one sender role and its opposite receiver role.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.recurringInterface`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#recurring-interface).

## The pending state is typed at the two-role interface

The real pending state owns two distinct opposite keys, not daemon captures.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.pending_typed`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#pending-typed).

## The state after the sender invocation is typed

First invocation transfers the exact sender slot into one worker; frame unchanged.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.sentInvoked_typed`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#sent-invoked-typed).

## The state after both trigger invocations is typed

Both workers own their actual distinct roles after the two trigger communications.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.bothInvoked_typed`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveOwnership.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#both-invoked-typed).

## Phases of the repeated-session execution

Three phases of actual execution; this does not generate unrolled Pi code.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.phase`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveRepeatability.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveRepeatability.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#phase).

## Each phase steps to the next

Every consecutive phase has a real canonical Step, including session reentry.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.phase_step`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveRepeatability.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveRepeatability.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#phase-step).

## Every round count has a trace returning to the pending state

For EVERY requested count, a nonzero trace returns to the identical pending code.
It has exactly three times (m+1) actual Steps, never a reflexive reachability proof.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.repeatable_trace`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveRepeatability.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveRepeatability.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#repeatable-trace).

## Every round has a session action on the same endpoint

EVERY round contains an actual action on the SAME session endpoint b.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.session_round_phase`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveRepeatability.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveRepeatability.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#session-round-phase).

## Every phase is typed at the two-role interface

Every actual runtime phase retains the same exact two-role linear interface.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.phase_typed`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveRepeatability.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveRepeatability.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#phase-typed).

## Arbitrarily long typed repeated-session traces

Arbitrarily long NONZERO actual execution with ownership at EVERY state.
The conclusion is a trace; no trace/Step/result is part of service admission.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.typed_repeatable_trace`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveRepeatability.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveRepeatability.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#typed-repeatable-trace).

## Every phase is reachable from the pending state

Induction on actual Step count reaches each phase of the persistent runtime code.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.phase_reachable`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveRepeatability.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveRepeatability.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#phase-reachable).

## Both services are offered at every phase

Actual unguarded daemons offer BOTH declared services at EVERY runtime phase.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.phase_offers`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveRepeatability.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveRepeatability.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#phase-offers).

## The recurring interface is balanced

Both literal opposite-role self-loop slots form an ACTUAL balanced initial
interface; balance is derived from lookup/code facts, not a ready-pair hypothesis.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.recurring_balanced`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveReduction.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveReduction.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#recurring-balanced).

## Semantic advances of the recurring interface are the identity

EVERY faithful advance of this actual literal self-loop interface is exact
identity. This is a code-level property of the concrete regular cursors, not a
claim that arbitrary equivalent recursive codes stay syntactically unchanged.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.recurring_advance_identity`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveReduction.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveReduction.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#recurring-advance-identity).

## Steps preserve typing at the recurring interface

ANY actually runtime-typed process at the concrete recurring interface keeps
that EXACT interface after a canonical Step, by GENERAL preservation and the
literal self-loop code property. No phase, readiness or schedule hypothesis.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.recurring_step_preserved`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveReduction.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveReduction.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#recurring-step-preserved).

## Each next phase is typed by subject reduction

GENERAL runtime subject reduction applies to every recursive phase (hence
all THREE phase kinds) in BOTH role orientations, at the exact self-loop interface.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.phase_step_preserved`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveReduction.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveReduction.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#phase-step-preserved).

## Every phase is typed by preservation from the pending state

Every phase's ownership follows from the INITIAL pending typing and GENERAL
finite runtime preservation, not repeated application of concrete phase typing.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.phase_typed_by_preservation`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveReduction.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveReduction.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#phase-typed-by-preservation).

## All declared services are available in the pending state

Initial actual replicated daemons supply EVERY declared signature, not just
requests or shared permissions. Availability remains a syntactic predicate.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.initial_available`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveReduction.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveReduction.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#initial-available).

## Services stay available at every phase

GENERAL persistent-offer reduction closure preserves the real source daemons
through every finite actual prefix of the recursive execution.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.phase_available_by_reduction`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveReduction.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveReduction.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#phase-available-by-reduction).

## Repeated-session traces with preserved typing and availability

EVERY m has one nonzero finite SAME-session trace with all neighbor Steps,
ALL round markers, ownership derived by GENERAL runtime preservation, and actual
persistent availability derived by GENERAL reduction closure at EVERY state.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.repeatable_trace_preserved`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveReduction.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveReduction.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#repeatable-trace-preserved).

## Every phase of the repeated session can step

GENERAL qualified progress produces an ACTUAL Step at every recursive phase,
BOTH roles and arbitrary scoped endpoint. Idle is excluded by exposed output syntax,
not by assuming the previously selected execution or readiness.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.phase_general_step`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveProgress.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveProgress.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#phase-general-step).

## Every phase of the restricted repeated session can step

GENERAL empty-interface progress includes the genuine private session in
BOTH orientations/all phases. Actual output syntax forces its Step branch.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.bound_phase_general_step`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveProgress.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveProgress.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#bound-phase-general-step).

## Repeated-session traces with typing, availability and progress

EVERY m has a SAME-witness counted repeated-session trace, all state types,
actual availability and ALL marked session edges, plus GENERAL progress at EVERY
state (including the last). This is not all-schedules fairness or termination.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.repeatable_trace_global`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RecursiveProgress.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RecursiveProgress.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#repeatable-trace-global).

## Unguarded shared input communicates with a matching output

Actual input syntax supplies an ACTUAL canonical Step with any matching
shared-constant output. Payload and continuation are not finite-unrolled, and
nested private/parallel/replica wrappers are handled by existing Cong/Step.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.accept_invocation_step`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ServiceExposure.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ServiceExposure.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#accept-invocation-step).

## Offered service communicates with a matching shared output

A persistent offered input exposes real canonical communication, including
nested templates and DONE endpoint payloads; no typing or active-key premise.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.offered_invocation_step`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ServiceExposure.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ServiceExposure.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html#offered-invocation-step).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Recursive sessions through replicated services](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/process-calculi/session-types/recursive-sessions-through-replicated-services)
