---
declaration: section
origin: cited
lean: Cslib.SessionTypes.Endpoint.Key.under_lift, Cslib.SessionTypes.Endpoint.Context.injOn_under_lift, Cslib.SessionTypes.Endpoint.Context.rekey_under_lift, Cslib.SessionTypes.Endpoint.Key.under_fixed, Cslib.SessionTypes.Endpoint.Context.injOn_under_binder, Cslib.SessionTypes.Endpoint.Context.injOn_insert_owned, Cslib.SessionTypes.Endpoint.Context.injOn_under_bind, Cslib.SessionTypes.Endpoint.Context.lookup_received
statement: formalized
proof: formalized
---

# Capture-safe finite ownership transport

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/capture-safe-finite-ownership-transport/index.html).

## Binder extension commutes with lifting on endpoint keys

Entering a binder commutes with endpoint rekeying and retains its role.

Formalized by `Cslib.SessionTypes.Endpoint.Key.under_lift`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypingTransport.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/TypingTransport.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/capture-safe-finite-ownership-transport/index.html#under-lift).

## Injectivity of rekeying passes under a binder

Collision freedom of owned keys is stable when entering a binder.

Formalized by `Cslib.SessionTypes.Endpoint.Context.injOn_under_lift`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypingTransport.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/TypingTransport.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/capture-safe-finite-ownership-transport/index.html#inj-on-under-lift).

## Rekeying under a binder is the lift of the outer rekeying

Rekeying under a binder is exactly the lift of the outer rekeying.

Formalized by `Cslib.SessionTypes.Endpoint.Context.rekey_under_lift`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypingTransport.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/TypingTransport.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/capture-safe-finite-ownership-transport/index.html#rekey-under-lift).

## Binder extension fixes the fresh binder's endpoint keys

The fresh binder's endpoint roles are fixed under name transformation.

Formalized by `Cslib.SessionTypes.Endpoint.Key.under_fixed`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypingTransport.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/TypingTransport.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/capture-safe-finite-ownership-transport/index.html#under-fixed).

## Rekeying under a binder is injective on fresh and lifted keys

Rekeying under a binder is injective on both fresh roles and all lifted
outer ownership, not just on endpoint keys with different physical names.

Formalized by `Cslib.SessionTypes.Endpoint.Context.injOn_under_binder`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypingTransport.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/TypingTransport.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/capture-safe-finite-ownership-transport/index.html#inj-on-under-binder).

## Injectivity of rekeying survives updating an owned key

Updating an already-owned key introduces no new aliasing obligation.

Formalized by `Cslib.SessionTypes.Endpoint.Context.injOn_insert_owned`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypingTransport.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/TypingTransport.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/capture-safe-finite-ownership-transport/index.html#inj-on-insert-owned).

## Injectivity of rekeying under a restriction binding

Both newly restricted roles lie in the collision-free binder domain.

Formalized by `Cslib.SessionTypes.Endpoint.Context.injOn_under_bind`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypingTransport.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/TypingTransport.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/capture-safe-finite-ownership-transport/index.html#inj-on-under-bind).

## Linear input installs the received role on the bound name

Linear input installs precisely the transmitted role on its bound name.

Formalized by `Cslib.SessionTypes.Endpoint.Context.lookup_received`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypingTransport.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/TypingTransport.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/capture-safe-finite-ownership-transport/index.html#lookup-received).

## Rekeying commutes with binding a private pair

Restriction rekeying fixes its newly bound pair and transports exactly
the outer context; it cannot alias either fresh role with an outer key.

Formalized by `Cslib.SessionTypes.Endpoint.Context.rekey_bind`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypingTransport.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/TypingTransport.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/capture-safe-finite-ownership-transport/index.html#rekey-bind).

## Received role's opposite is absent at the bound name

A received role cannot duplicate an existing key of the opposite role.

Formalized by `Cslib.SessionTypes.Endpoint.Context.lookup_received_opposite`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypingTransport.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/TypingTransport.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/capture-safe-finite-ownership-transport/index.html#lookup-received-opposite).

## Injectivity of rekeying after receiving a fresh role

A linear input's fresh variable role preserves collision freedom of
all lifted outer keys, including outer keys of the opposite role.

Formalized by `Cslib.SessionTypes.Endpoint.Context.injOn_under_received`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypingTransport.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/TypingTransport.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/capture-safe-finite-ownership-transport/index.html#inj-on-under-received).

## Injectivity of rekeying survives erasing a key

Erasing an owned key cannot create a rekeying collision.

Formalized by `Cslib.SessionTypes.Endpoint.Context.injOn_erase`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypingTransport.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/TypingTransport.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/capture-safe-finite-ownership-transport/index.html#inj-on-erase).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Capture-safe finite ownership transport](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/capture-safe-finite-ownership-transport/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/capture-safe-finite-ownership-transport)
