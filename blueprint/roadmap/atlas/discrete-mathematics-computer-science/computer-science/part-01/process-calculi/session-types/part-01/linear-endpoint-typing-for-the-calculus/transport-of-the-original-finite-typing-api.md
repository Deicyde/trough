---
declaration: section
origin: cited
lean: Cslib.SessionTypes.Endpoint.Context.lift_ofFinite, Cslib.SessionTypes.Endpoint.HasType.ofFinite
statement: formalized
proof: formalized
---

# Transport of the original finite typing API

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/transport-of-the-original-finite-typing-api/index.html).

## Binder lift fixes the finite ownership map

The finite bridge's constant-only ownership is unaffected by binder lift.

Formalized by `Cslib.SessionTypes.Endpoint.Context.lift_ofFinite`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/FiniteTyping.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/FiniteTyping.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/transport-of-the-original-finite-typing-api/index.html#lift-of-finite).

## Finite passive-name typing embeds into endpoint typing

Every original finite passive-name derivation embeds with its exact
protocol obligations and a bounded finite map of either endpoint role.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.ofFinite`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/FiniteTyping.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/FiniteTyping.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/transport-of-the-original-finite-typing-api/index.html#of-finite).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Transport of the original finite typing API](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/transport-of-the-original-finite-typing-api/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/transport-of-the-original-finite-typing-api)
