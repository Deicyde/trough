---
declaration: section
origin: cited
lean: Cslib.PiCalculus.Name.ClosedAt, Cslib.PiCalculus.Proc.ClosedAt, Cslib.PiCalculus.liftName_eq_of_closedAt, Cslib.PiCalculus.liftProc_eq_of_closedAt, Cslib.PiCalculus.Name.ClosedAt.lift, Cslib.PiCalculus.Name.ClosedAt.subst, Cslib.PiCalculus.Proc.ClosedAt.lift, Cslib.PiCalculus.Proc.ClosedAt.substProc
statement: formalized
proof: formalized
---

# Scope preservation for π-calculus names and processes

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/scope-preservation-for-calculus-names-and-proces/index.html).

## Name scoped at a binder depth

A name refers only to the `depth` surrounding binders or to a free
constant. At depth zero, no variable is permitted.

Formalized by `Cslib.PiCalculus.Name.ClosedAt`, a definition declared in [CSLibExt/Languages/PiCalculus/Scoping.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Scoping.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/scope-preservation-for-calculus-names-and-proces/index.html#closed-at).

## Locally closed processes at a binder depth

Every variable refers to an enclosing input/restriction binder.
`ClosedAt 0` permits free constants, but no dangling de Bruijn variables.

Formalized by `Cslib.PiCalculus.Proc.ClosedAt`, a definition declared in [CSLibExt/Languages/PiCalculus/Scoping.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Scoping.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/scope-preservation-for-calculus-names-and-proces/index.html#closed-at-2).

## Lifting fixes an in-scope name

Lifting above the ambient binder depth fixes an in-scope name.

Formalized by `Cslib.PiCalculus.liftName_eq_of_closedAt`, a theorem declared in [CSLibExt/Languages/PiCalculus/Scoping.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Scoping.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/scope-preservation-for-calculus-names-and-proces/index.html#lift-name-eq-of-closed-at).

## Lifting fixes a locally closed process

Lifting above the surrounding binders fixes a locally closed process.
At depth zero, insertion under a fresh binder cannot capture its names.

Formalized by `Cslib.PiCalculus.liftProc_eq_of_closedAt`, a theorem declared in [CSLibExt/Languages/PiCalculus/Scoping.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Scoping.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/scope-preservation-for-calculus-names-and-proces/index.html#lift-proc-eq-of-closed-at).

## Lifting preserves name scoping

Inserting a binder at any cutoff preserves name scoping in the
larger environment.

Formalized by `Cslib.PiCalculus.Name.ClosedAt.lift`, a theorem declared in [CSLibExt/Languages/PiCalculus/Scoping.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Scoping.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/scope-preservation-for-calculus-names-and-proces/index.html#lift).

## Name substitution preserves scoping

Removing the binder at `k ≤ n` preserves name scoping when its
replacement is scoped in the remaining environment.

Formalized by `Cslib.PiCalculus.Name.ClosedAt.subst`, a theorem declared in [CSLibExt/Languages/PiCalculus/Scoping.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Scoping.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/scope-preservation-for-calculus-names-and-proces/index.html#subst).

## Lifting preserves process scoping

Shifting a process past a new binder preserves scoping. Inner input
and restriction binders increase the cutoff as in `Basic.liftProc`.

Formalized by `Cslib.PiCalculus.Proc.ClosedAt.lift`, a theorem declared in [CSLibExt/Languages/PiCalculus/Scoping.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Scoping.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/scope-preservation-for-calculus-names-and-proces/index.html#lift-2).

## Substitution at any cutoff preserves process scoping

Capture-avoiding substitution removes one ambient binder while
preserving every name's scope, including under input and restriction.

Formalized by `Cslib.PiCalculus.Proc.ClosedAt.substProc`, a theorem declared in [CSLibExt/Languages/PiCalculus/Scoping.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Scoping.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/scope-preservation-for-calculus-names-and-proces/index.html#subst-proc).

## Instantiating the innermost binder preserves process scoping

Instantiating the innermost binder preserves process scoping.

Formalized by `Cslib.PiCalculus.Proc.ClosedAt.subst`, a theorem declared in [CSLibExt/Languages/PiCalculus/Scoping.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Scoping.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/scope-preservation-for-calculus-names-and-proces/index.html#subst-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Scope preservation for π-calculus names and processes](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/scope-preservation-for-calculus-names-and-proces/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/process-calculi/calculus/scope-preservation-for-calculus-names-and-proces)
