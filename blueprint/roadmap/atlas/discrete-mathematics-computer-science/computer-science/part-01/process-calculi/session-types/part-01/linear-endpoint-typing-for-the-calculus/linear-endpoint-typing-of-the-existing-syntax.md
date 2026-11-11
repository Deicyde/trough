---
declaration: section
origin: cited
lean: Cslib.SessionTypes.Endpoint.HasType, Cslib.SessionTypes.Endpoint.HasType.closedAt, Cslib.SessionTypes.Endpoint.HasType.finiteLinear, Cslib.SessionTypes.Endpoint.HasType.nil_singleton, Cslib.SessionTypes.Endpoint.HasType.out_owned, Cslib.SessionTypes.Endpoint.HasType.nil_insert, Cslib.SessionTypes.Endpoint.HasType.inp_inv, Cslib.SessionTypes.Endpoint.HasType.out_inv
statement: formalized
proof: formalized
---

# Linear endpoint typing of the existing π syntax

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/linear-endpoint-typing-of-the-existing-syntax/index.html).

## Linear endpoint typing of π-calculus processes

Syntax-directed linear typing. Capabilities never contain preservation
or progress assumptions. Protocol heads may be guarded regular protocols.

Formalized by `Cslib.SessionTypes.Endpoint.HasType`, an inductive type declared in [CSLibExt/Languages/SessionTypes/Endpoint/Typing.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Typing.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/linear-endpoint-typing-of-the-existing-syntax/index.html#has-type).

## Endpoint-typed processes are scoped at the ambient depth

Every endpoint-typed process satisfies the canonical π scope predicate.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.closedAt`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Typing.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Typing.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/linear-endpoint-typing-of-the-existing-syntax/index.html#closed-at).

## Endpoint-typed processes lie in the finite linear fragment

Typed terms stay in the proved Cong/Step-closed finite fragment.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.finiteLinear`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Typing.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Typing.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/linear-endpoint-typing-of-the-existing-syntax/index.html#finite-linear).

## Nil is typed by a single done capability

A recorded completed capability is admissible at nil; an active one
would fail the completed-context premise.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.nil_singleton`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Typing.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Typing.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/linear-endpoint-typing-of-the-existing-syntax/index.html#nil-singleton).

## Output subjects of endpoint-typed processes are owned

Every output subject is backed by an owned role, never merely by a
passive name in the ambient data scope.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.out_owned`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Typing.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Typing.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/linear-endpoint-typing-of-the-existing-syntax/index.html#out-owned).

## Adding a completed capability at nil preserves typing

Completed endpoint slots may be added at nil without creating a
communication obligation; active protocols cannot use this rule.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.nil_insert`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Typing.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Typing.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/linear-endpoint-typing-of-the-existing-syntax/index.html#nil-insert).

## Inversion of endpoint typing for input

Input inversion exposes its owned role, literal payload sort, and
continuation context. Passive and delegated names are not conflated.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.inp_inv`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Typing.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Typing.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/linear-endpoint-typing-of-the-existing-syntax/index.html#inp-inv).

## Inversion of endpoint typing for output

Output inversion exposes the actual owned subject, distinct payload sort,
and literal continuation resources; delegation consumes the payload role.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.out_inv`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Typing.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Typing.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/linear-endpoint-typing-of-the-existing-syntax/index.html#out-inv).

## Inversion of endpoint typing for parallel composition

Parallel typing exposes an actual disjoint ownership split, not a
stored preservation or progress witness.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.par_inv`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Typing.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Typing.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/linear-endpoint-typing-of-the-existing-syntax/index.html#par-inv).

## Inversion of endpoint typing for nil

Nil inversion exposes completion and scope of every recorded endpoint.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.nil_inv`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Typing.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Typing.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/linear-endpoint-typing-of-the-existing-syntax/index.html#nil-inv).

## Nil is typed by a single capability with completed head

Any protocol whose guarded head is completed is admissible at a
single nil-owned slot, including completed regular graph cursors.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.nil_singleton_completed`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Typing.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Typing.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/linear-endpoint-typing-of-the-existing-syntax/index.html#nil-singleton-completed).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Linear endpoint typing of the existing π syntax](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/linear-endpoint-typing-of-the-existing-syntax/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/linear-endpoint-typing-of-the-existing-syntax)
