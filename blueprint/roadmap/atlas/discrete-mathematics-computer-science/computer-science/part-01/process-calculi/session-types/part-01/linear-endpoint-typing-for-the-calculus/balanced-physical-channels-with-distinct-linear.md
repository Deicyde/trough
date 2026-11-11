---
declaration: section
origin: cited
lean: Cslib.SessionTypes.Endpoint.Balanced, Cslib.SessionTypes.Endpoint.balanced_empty, Cslib.SessionTypes.Endpoint.balanced_bind_empty, Cslib.SessionTypes.Endpoint.Balanced.rekey, Cslib.SessionTypes.Endpoint.Compatible, Cslib.SessionTypes.Endpoint.Balanced.compatible, Cslib.SessionTypes.Endpoint.disjoint_subjects_opposite, Cslib.SessionTypes.Endpoint.Compatible.union_left
statement: formalized
proof: formalized
---

# Balanced physical channels with distinct linear roles

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/balanced-physical-channels-with-distinct-linear/index.html).

## Balanced endpoint ownership

Every owned role has its opposite role at the same physical name, with
the same rank and the dual protocol. This condition may permit deadlocks.

Formalized by `Cslib.SessionTypes.Endpoint.Balanced`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/Balance.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Balance.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/balanced-physical-channels-with-distinct-linear/index.html#balanced).

## The empty interface is balanced

An empty external interface is balanced. Internal ν channels still
require their own balanced ownership and are not thereby completed.

Formalized by `Cslib.SessionTypes.Endpoint.balanced_empty`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Balance.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Balance.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/balanced-physical-channels-with-distinct-linear/index.html#balanced-empty).

## A fresh restriction pair is balanced

A real fresh restriction creates a balanced pair on a single physical name.

Formalized by `Cslib.SessionTypes.Endpoint.balanced_bind_empty`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Balance.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Balance.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/balanced-physical-channels-with-distinct-linear/index.html#balanced-bind-empty).

## Rekeying preserves balance

Capture-safe rekeying transports balance when endpoint roles are retained.
The injectivity condition is on owned keys, not on arbitrary passive data.

Formalized by `Cslib.SessionTypes.Endpoint.Balanced.rekey`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Balance.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Balance.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/balanced-physical-channels-with-distinct-linear/index.html#rekey).

## Compatibility of a partial endpoint interface

A partial interface is compatible if opposite roles, WHEN both are
present, have dual protocols. A missing peer is not an enabled-edge witness.

Formalized by `Cslib.SessionTypes.Endpoint.Compatible`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/Balance.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Balance.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/balanced-physical-channels-with-distinct-linear/index.html#compatible).

## Balanced interfaces are compatible

A balanced complete interface supplies compatibility for every present pair.

Formalized by `Cslib.SessionTypes.Endpoint.Balanced.compatible`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Balance.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Balance.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/balanced-physical-channels-with-distinct-linear/index.html#compatible-2).

## Disjoint owned keys on one name have opposite roles

A dual-compatible pair of physically equal but disjoint owned keys
must be opposite roles. The runtime channel name alone does not supply this.

Formalized by `Cslib.SessionTypes.Endpoint.disjoint_subjects_opposite`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Balance.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Balance.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/balanced-physical-channels-with-distinct-linear/index.html#disjoint-subjects-opposite).

## Compatibility passes to the left part of a union

Any left subcontext of a compatible interface retains compatibility of
its present pairs; no global-progress assumption is involved.

Formalized by `Cslib.SessionTypes.Endpoint.Compatible.union_left`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Balance.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Balance.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/balanced-physical-channels-with-distinct-linear/index.html#union-left).

## Compatibility passes to the right part of a disjoint split

A right child of a disjoint linear split inherits compatibility of
its present pairs from the combined interface.

Formalized by `Cslib.SessionTypes.Endpoint.Compatible.union_right`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Balance.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Balance.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/balanced-physical-channels-with-distinct-linear/index.html#union-right).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Balanced physical channels with distinct linear roles](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/balanced-physical-channels-with-distinct-linear/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/balanced-physical-channels-with-distinct-linear)
