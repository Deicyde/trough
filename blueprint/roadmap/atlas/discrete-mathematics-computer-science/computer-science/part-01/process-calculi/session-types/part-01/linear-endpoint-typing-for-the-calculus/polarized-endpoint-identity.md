---
declaration: section
origin: cited
lean: Cslib.SessionTypes.Endpoint.Role, Cslib.SessionTypes.Endpoint.Key, Cslib.SessionTypes.Endpoint.Role.opposite, Cslib.SessionTypes.Endpoint.Role.opposite_opposite, Cslib.SessionTypes.Endpoint.Key.opposite, Cslib.SessionTypes.Endpoint.Key.opposite_opposite, Cslib.SessionTypes.Endpoint.Key.opposite_ne, Cslib.SessionTypes.Endpoint.Key.mapName
statement: formalized
proof: formalized
---

# Polarized endpoint identity

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/polarized-endpoint-identity/index.html).

## Endpoint role on a π name

Opposite capabilities on a single physical π name.

Formalized by `Cslib.SessionTypes.Endpoint.Role`, an inductive type declared in [CSLibExt/Languages/SessionTypes/Endpoint/Identity.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Identity.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/polarized-endpoint-identity/index.html#role).

## Polarized endpoint key

One endpoint key consists of the existing physical name and a role.

Formalized by `Cslib.SessionTypes.Endpoint.Key`, a structure declared in [CSLibExt/Languages/SessionTypes/Endpoint/Identity.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Identity.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/polarized-endpoint-identity/index.html#key).

## Opposite endpoint role

Reverse the linear role without changing the physical name.

Formalized by `Cslib.SessionTypes.Endpoint.Role.opposite`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/Identity.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Identity.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/polarized-endpoint-identity/index.html#opposite).

## Role reversal is an involution

Role reversal is an involution.

Formalized by `Cslib.SessionTypes.Endpoint.Role.opposite_opposite`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Identity.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Identity.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/polarized-endpoint-identity/index.html#opposite-opposite).

## Peer endpoint key

The peer role on the same physical channel.

Formalized by `Cslib.SessionTypes.Endpoint.Key.opposite`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/Identity.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Identity.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/polarized-endpoint-identity/index.html#opposite-2).

## Key reversal is an involution

Reversing an endpoint twice recovers its entire key.

Formalized by `Cslib.SessionTypes.Endpoint.Key.opposite_opposite`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Identity.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Identity.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/polarized-endpoint-identity/index.html#opposite-opposite-2).

## An endpoint key differs from its peer

Opposite roles cannot collide, even on one physical name.

Formalized by `Cslib.SessionTypes.Endpoint.Key.opposite_ne`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Identity.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Identity.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/polarized-endpoint-identity/index.html#opposite-ne).

## Renaming the physical name of an endpoint key

Apply an existing-name transformation, leaving the role untouched.

Formalized by `Cslib.SessionTypes.Endpoint.Key.mapName`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/Identity.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Identity.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/polarized-endpoint-identity/index.html#map-name).

## Injective renamings act injectively on endpoint keys

Injective physical-name transformations preserve endpoint identity.

Formalized by `Cslib.SessionTypes.Endpoint.Key.mapName_injective`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Identity.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Identity.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/polarized-endpoint-identity/index.html#map-name-injective).

## Extensionality for endpoint keys

Endpoint identity is exactly its physical name and linear role.

Formalized by `Cslib.SessionTypes.Endpoint.Key.ext`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Identity.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Identity.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/polarized-endpoint-identity/index.html#ext).

## Distinct keys on one name are opposite

Distinct keys on one physical name must be opposite endpoint roles.

Formalized by `Cslib.SessionTypes.Endpoint.Key.eq_opposite_of_name_eq`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Identity.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Identity.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/polarized-endpoint-identity/index.html#eq-opposite-of-name-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Polarized endpoint identity](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/polarized-endpoint-identity/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/polarized-endpoint-identity)
