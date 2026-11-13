---
declaration: section
origin: cited
lean: Cslib.SessionTypes.Endpoint.Protocol.ofFinite, Cslib.SessionTypes.Endpoint.Protocol.ofFinite_dual, Cslib.SessionTypes.Endpoint.Protocol.toFinite?, Cslib.SessionTypes.Endpoint.Protocol.toFinite?_ofFinite, Cslib.SessionTypes.Endpoint.Protocol.ofFinite_injective
statement: formalized
proof: formalized
---

# Lossless finite passive-protocol bridge

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/lossless-finite-passive-protocol-bridge/index.html).

## Embedding of finite passive-name protocols

Embed the original finite passive-name protocol without changing actions.

Formalized by `Cslib.SessionTypes.Endpoint.Protocol.ofFinite`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/FiniteBridge.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/FiniteBridge.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/lossless-finite-passive-protocol-bridge/index.html#of-finite).

## Finite protocol embedding commutes with duality

The finite embedding preserves both protocol orientations.

Formalized by `Cslib.SessionTypes.Endpoint.Protocol.ofFinite_dual`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/FiniteBridge.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/FiniteBridge.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/lossless-finite-passive-protocol-bridge/index.html#of-finite-dual).

## Partial recovery of a finite passive-name protocol

Recover a finite passive protocol; richer payloads and recursion are
not erased into a falsely finite protocol.

Formalized by `Cslib.SessionTypes.Endpoint.Protocol.toFinite?`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/FiniteBridge.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/FiniteBridge.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/lossless-finite-passive-protocol-bridge/index.html#to-finite).

## Recovery is a left inverse of the finite embedding

The finite embedding has a literal left inverse.

Formalized by `Cslib.SessionTypes.Endpoint.Protocol.toFinite?_ofFinite`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/FiniteBridge.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/FiniteBridge.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/lossless-finite-passive-protocol-bridge/index.html#to-finite-of-finite).

## Injectivity of the finite protocol embedding

Different finite protocols remain different in the richer representation.

Formalized by `Cslib.SessionTypes.Endpoint.Protocol.ofFinite_injective`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/FiniteBridge.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/FiniteBridge.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/lossless-finite-passive-protocol-bridge/index.html#of-finite-injective).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lossless finite passive-protocol bridge](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/lossless-finite-passive-protocol-bridge/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/lossless-finite-passive-protocol-bridge)
