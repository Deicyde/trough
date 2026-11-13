---
declaration: section
origin: cited
lean: Cslib.SessionTypes.SessionType, Cslib.SessionTypes.SessionType.dual, Cslib.SessionTypes.SessionType.dual_dual, Cslib.SessionTypes.SessionType.length, Cslib.SessionTypes.SessionType.length_dual, Cslib.SessionTypes.Context, Cslib.SessionTypes.advance, Cslib.SessionTypes.dualContext
statement: formalized
proof: formalized
---

# Finite sessions with unrestricted name data

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/finite-sessions-with-unrestricted-name-data/index.html).

## Finite binary session types

Finite binary protocols carrying unrestricted, passive names.

Formalized by `Cslib.SessionTypes.SessionType`, an inductive type declared in [CSLibExt/Languages/SessionTypes/Basic.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Basic.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/finite-sessions-with-unrestricted-name-data/index.html#session-type).

## Dual of a session type

Exchange the endpoint's send and receive obligations.

Formalized by `Cslib.SessionTypes.SessionType.dual`, a definition declared in [CSLibExt/Languages/SessionTypes/Basic.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Basic.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/finite-sessions-with-unrestricted-name-data/index.html#dual).

## Session type duality is an involution

Duality is an involution, including at completion.

Formalized by `Cslib.SessionTypes.SessionType.dual_dual`, a theorem declared in [CSLibExt/Languages/SessionTypes/Basic.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Basic.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/finite-sessions-with-unrestricted-name-data/index.html#dual-dual).

## Length of a session type

Number of communication actions remaining in a finite protocol.

Formalized by `Cslib.SessionTypes.SessionType.length`, a definition declared in [CSLibExt/Languages/SessionTypes/Basic.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Basic.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/finite-sessions-with-unrestricted-name-data/index.html#length).

## Dual session types have equal length

Opposite endpoint roles have the same number of actions.

Formalized by `Cslib.SessionTypes.SessionType.length_dual`, a theorem declared in [CSLibExt/Languages/SessionTypes/Basic.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Basic.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/finite-sessions-with-unrestricted-name-data/index.html#length-dual).

## Per-channel session context of a thread

One linear endpoint obligation per physical channel in a thread.

Formalized by `Cslib.SessionTypes.Context`, an abbreviation declared in [CSLibExt/Languages/SessionTypes/Basic.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Basic.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/finite-sessions-with-unrestricted-name-data/index.html#context).

## Advancing one endpoint of a session context

Advance just the communicating endpoint; other obligations are unchanged.

Formalized by `Cslib.SessionTypes.advance`, a definition declared in [CSLibExt/Languages/SessionTypes/Basic.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Basic.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/finite-sessions-with-unrestricted-name-data/index.html#advance).

## Pointwise dual of a session context

The opposite endpoint roles, pointwise.

Formalized by `Cslib.SessionTypes.dualContext`, a definition declared in [CSLibExt/Languages/SessionTypes/Basic.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Basic.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/finite-sessions-with-unrestricted-name-data/index.html#dual-context).

## Dualizing a context commutes with advancing an endpoint

Advancing dual endpoints preserves pointwise compatibility.

Formalized by `Cslib.SessionTypes.dualContext_advance`, a theorem declared in [CSLibExt/Languages/SessionTypes/Basic.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Basic.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/finite-sessions-with-unrestricted-name-data/index.html#dual-context-advance).

## Linear session typing of sequential threads

Linear typing of finite sequential threads in the existing π syntax.
`nil` consumes only completed obligations. Input-bound names are unrestricted
payloads, never session subjects; there is no parallel duplication rule.

Formalized by `Cslib.SessionTypes.HasType`, an inductive type declared in [CSLibExt/Languages/SessionTypes/Basic.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Basic.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/finite-sessions-with-unrestricted-name-data/index.html#has-type).

## Payload substitution at any cutoff preserves session typing

Capture-avoiding payload substitution preserves every linear obligation,
including through nested input binders and at nonzero cutoffs.

Formalized by `Cslib.SessionTypes.HasType.substProc`, a theorem declared in [CSLibExt/Languages/SessionTypes/Basic.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Basic.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/finite-sessions-with-unrestricted-name-data/index.html#subst-proc).

## Receiving a closed name preserves session typing

Receiving a closed name preserves the residual thread's typing.

Formalized by `Cslib.SessionTypes.HasType.subst`, a theorem declared in [CSLibExt/Languages/SessionTypes/Basic.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Basic.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/finite-sessions-with-unrestricted-name-data/index.html#subst).

## Session typing derivations have finite support

A derivation has only finitely many active channel obligations: above
some bound every channel is completed. Contexts are total functions.

Formalized by `Cslib.SessionTypes.HasType.finite_support`, a theorem declared in [CSLibExt/Languages/SessionTypes/Basic.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Basic.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/finite-sessions-with-unrestricted-name-data/index.html#finite-support).

## Session-typed threads are well scoped

Every typed thread satisfies the shared π name/process scoping predicate.
Free session constants remain permitted; this is not ν-closedness.

Formalized by `Cslib.SessionTypes.HasType.closedAt`, a theorem declared in [CSLibExt/Languages/SessionTypes/Basic.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Basic.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/finite-sessions-with-unrestricted-name-data/index.html#closed-at).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Finite sessions with unrestricted name data](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/finite-sessions-with-unrestricted-name-data/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/finite-sessions-with-unrestricted-name-data)
