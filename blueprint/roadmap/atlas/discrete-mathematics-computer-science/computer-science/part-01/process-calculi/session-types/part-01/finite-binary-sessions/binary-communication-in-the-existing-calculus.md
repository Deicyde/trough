---
declaration: section
origin: cited
lean: Cslib.SessionTypes.represent, Cslib.SessionTypes.represent_injective, Cslib.SessionTypes.CommStep, Cslib.SessionTypes.represent_step, Cslib.SessionTypes.BinaryTyped, Cslib.SessionTypes.CommStep.preservation
statement: formalized
proof: formalized
---

# Binary communication in the existing π-calculus

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/binary-communication-in-the-existing-calculus/index.html).

## Binary configuration as a parallel composition

Embed a binary configuration without changing either process.

Formalized by `Cslib.SessionTypes.represent`, a definition declared in [CSLibExt/Languages/SessionTypes/Communication.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Communication.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/binary-communication-in-the-existing-calculus/index.html#represent).

## Injectivity of the binary configuration embedding

The representation does not identify distinct configurations.

Formalized by `Cslib.SessionTypes.represent_injective`, a theorem declared in [CSLibExt/Languages/SessionTypes/Communication.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Communication.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/binary-communication-in-the-existing-calculus/index.html#represent-injective).

## Communication step of a binary configuration

Opposite head guards synchronize, in either endpoint orientation.

Formalized by `Cslib.SessionTypes.CommStep`, an inductive type declared in [CSLibExt/Languages/SessionTypes/Communication.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Communication.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/binary-communication-in-the-existing-calculus/index.html#comm-step).

## Session communication steps are π-calculus reductions

Every session communication is a reduction in the unchanged π semantics.

Formalized by `Cslib.SessionTypes.represent_step`, a theorem declared in [CSLibExt/Languages/SessionTypes/Communication.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Communication.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/binary-communication-in-the-existing-calculus/index.html#represent-step).

## Dual session typing of a binary configuration

Locally linear threads owning opposite roles on every channel.
Dual compatibility permits cyclic waits; it does not assert progress.

Formalized by `Cslib.SessionTypes.BinaryTyped`, a definition declared in [CSLibExt/Languages/SessionTypes/Communication.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Communication.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/binary-communication-in-the-existing-calculus/index.html#binary-typed).

## Communication preserves binary session typing

Communication consumes dual heads and preserves linear residual typing;
payload substitution never changes the session context.

Formalized by `Cslib.SessionTypes.CommStep.preservation`, a theorem declared in [CSLibExt/Languages/SessionTypes/Communication.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Communication.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/binary-communication-in-the-existing-calculus/index.html#preservation).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Binary communication in the existing π-calculus](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/binary-communication-in-the-existing-calculus/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/binary-communication-in-the-existing-calculus)
