---
declaration: section
origin: cited
lean: Cslib.SessionTypes.Endpoint.Protocol, Cslib.SessionTypes.Endpoint.Protocol.dual, Cslib.SessionTypes.Endpoint.Protocol.dual_dual, Cslib.SessionTypes.Endpoint.Protocol.unfold, Cslib.SessionTypes.Endpoint.Protocol.unfold_dual, Cslib.SessionTypes.Endpoint.Protocol.unfold_ne_regular, Cslib.SessionTypes.Endpoint.Protocol.unfold_unfold
statement: formalized
proof: formalized
---

# Name and capability protocols with guarded regular recursion

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/name-and-capability-protocols-with-guarded-regul/index.html).

## Endpoint protocol with guarded regular recursion

A protocol with explicit payload sort and guarded graph recursion.
Payload endpoint roles are transmitted unchanged, not dualized.

Formalized by `Cslib.SessionTypes.Endpoint.Protocol`, an inductive type declared in [CSLibExt/Languages/SessionTypes/Endpoint/Protocol.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Protocol.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/name-and-capability-protocols-with-guarded-regul/index.html#protocol).

## Dual of an endpoint protocol

Reverse subject actions and continuations; preserve payload ownership.

Formalized by `Cslib.SessionTypes.Endpoint.Protocol.dual`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/Protocol.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Protocol.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/name-and-capability-protocols-with-guarded-regul/index.html#dual).

## Protocol duality is an involution

Duality is involutive for finite and guarded recursive protocols.

Formalized by `Cslib.SessionTypes.Endpoint.Protocol.dual_dual`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Protocol.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Protocol.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/name-and-capability-protocols-with-guarded-regul/index.html#dual-dual).

## One-step unfolding of a protocol

Expose one communication guard. Graph successors retain their subject
orientation; an endpoint payload retains its independently specified one.

Formalized by `Cslib.SessionTypes.Endpoint.Protocol.unfold`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/Protocol.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Protocol.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/name-and-capability-protocols-with-guarded-regul/index.html#unfold).

## Unfolding commutes with protocol duality

Guarded unfolding commutes with duality, including recursive payloads.

Formalized by `Cslib.SessionTypes.Endpoint.Protocol.unfold_dual`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Protocol.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Protocol.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/name-and-capability-protocols-with-guarded-regul/index.html#unfold-dual).

## Unfolding never yields a regular-cursor protocol

Unfolding always exposes an action or completion, never another silent
regular-cursor wrapper. Cycles therefore cannot consist only of unfolding.

Formalized by `Cslib.SessionTypes.Endpoint.Protocol.unfold_ne_regular`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Protocol.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Protocol.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/name-and-capability-protocols-with-guarded-regul/index.html#unfold-ne-regular).

## Protocol unfolding is idempotent

One root unfolding is enough to expose a guard or completion.

Formalized by `Cslib.SessionTypes.Endpoint.Protocol.unfold_unfold`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Protocol.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Protocol.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/name-and-capability-protocols-with-guarded-regul/index.html#unfold-unfold).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Name and capability protocols with guarded regular recursion](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/name-and-capability-protocols-with-guarded-regul/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/name-and-capability-protocols-with-guarded-regul)
