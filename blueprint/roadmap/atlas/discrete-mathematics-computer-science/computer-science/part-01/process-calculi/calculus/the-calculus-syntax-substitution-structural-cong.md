---
declaration: section
origin: cited
lean: Cslib.PiCalculus.Name, Cslib.PiCalculus.Proc, Cslib.PiCalculus.liftName, Cslib.PiCalculus.liftProc, Cslib.PiCalculus.substName, Cslib.PiCalculus.substProc, Cslib.PiCalculus.subst, Cslib.PiCalculus.swapNameAt
statement: formalized
proof: formalized
---

# The π-calculus: syntax, substitution, structural congruence, reduction

13 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/the-calculus-syntax-substitution-structural-cong/index.html).

## Channel name in the π-calculus

A channel name: a free channel `const n`, or the `i`-th enclosing
binder `var i`.

Formalized by `Cslib.PiCalculus.Name`, an inductive type declared in [CSLibExt/Languages/PiCalculus/Basic.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Basic.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/the-calculus-syntax-substitution-structural-cong/index.html#name).

## Processes of the π-calculus

Processes of the π-calculus. `inp a p` binds variable `0` in `p`;
`nu p` binds variable `0` in `p` as a fresh channel.

Formalized by `Cslib.PiCalculus.Proc`, an inductive type declared in [CSLibExt/Languages/PiCalculus/Basic.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Basic.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/the-calculus-syntax-substitution-structural-cong/index.html#proc).

## Lifting free de Bruijn indices of a π-calculus name

Shift free variables at or above `cutoff` up by one, e.g. when
pushing a process under a binder.

Formalized by `Cslib.PiCalculus.liftName`, a definition declared in [CSLibExt/Languages/PiCalculus/Basic.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Basic.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/the-calculus-syntax-substitution-structural-cong/index.html#lift-name).

## Lifting free de Bruijn indices of a π-calculus process

Shift free variables of a process, entering binders with an
increased cutoff.

Formalized by `Cslib.PiCalculus.liftProc`, a definition declared in [CSLibExt/Languages/PiCalculus/Basic.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Basic.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/the-calculus-syntax-substitution-structural-cong/index.html#lift-proc).

## Substitution of a name into a π-calculus name

Substitute the name `n` for the variable at `cutoff`: variables
below the cutoff are bound by inner binders and untouched, the variable
at the cutoff is replaced by `n`, and variables above shift down by
one.

Formalized by `Cslib.PiCalculus.substName`, a definition declared in [CSLibExt/Languages/PiCalculus/Basic.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Basic.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/the-calculus-syntax-substitution-structural-cong/index.html#subst-name).

## Substitution of a name into a π-calculus process at a cutoff

Substitute the name `n` for the variable at `cutoff` in a
process. Under a binder, `n` is lifted by one at cutoff `0` so it
keeps referring to the same outer names: every free index of `n`
refers to a binder above the substitution point, so all of them shift.
Lifting at the current cutoff would leave indices below the cutoff
captured by the new binder.

Formalized by `Cslib.PiCalculus.substProc`, a definition declared in [CSLibExt/Languages/PiCalculus/Basic.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Basic.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/the-calculus-syntax-substitution-structural-cong/index.html#subst-proc).

## Substitution for the innermost bound variable of a process

Substitute the name `n` for the innermost bound variable of `p`.

Formalized by `Cslib.PiCalculus.subst`, a definition declared in [CSLibExt/Languages/PiCalculus/Basic.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Basic.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/the-calculus-syntax-substitution-structural-cong/index.html#subst).

## Swapping adjacent de Bruijn indices in a name

Swap the two de Bruijn indices `cutoff` and `cutoff + 1` in a name:
the two binders at that depth exchange places.

Formalized by `Cslib.PiCalculus.swapNameAt`, a definition declared in [CSLibExt/Languages/PiCalculus/Basic.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Basic.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/the-calculus-syntax-substitution-structural-cong/index.html#swap-name-at).

## Swapping adjacent binders throughout a process

Swap the two binders at depth `cutoff` throughout a process,
incrementing the cutoff under binders.

Formalized by `Cslib.PiCalculus.swapProc`, a definition declared in [CSLibExt/Languages/PiCalculus/Basic.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Basic.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/the-calculus-syntax-substitution-structural-cong/index.html#swap-proc).

## Substitution leaves constant channels and the empty process unchanged

Substitution leaves a process with no `var 0` untouched: a
constant channel stays constant, and the empty process stays empty.

Formalized by `Cslib.PiCalculus.subst_nil`, a theorem declared in [CSLibExt/Languages/PiCalculus/Basic.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Basic.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/the-calculus-syntax-substitution-structural-cong/index.html#subst-nil).

## Structural congruence of π-calculus processes

Structural congruence: `|` is commutative and associative with
unit `nil`, `ν` extrudes over `|` (lifting the other side, which cannot
mention the fresh name), restriction of `nil` is `nil`, nested
restrictions commute (swapping the two bound indices), and replication
unfolds.

Formalized by `Cslib.PiCalculus.Cong`, an inductive type declared in [CSLibExt/Languages/PiCalculus/Basic.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Basic.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/the-calculus-syntax-substitution-structural-cong/index.html#cong).

## Guarded-choice resolution in the π-calculus

Guarded-choice resolution: discard sum branches to reach a
guarded process. Transitivity handles nested sums.

Formalized by `Cslib.PiCalculus.Select`, an inductive type declared in [CSLibExt/Languages/PiCalculus/Basic.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Basic.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/the-calculus-syntax-substitution-structural-cong/index.html#select).

## Reduction relation of the π-calculus

Reduction: communication (substituting the sent channel for the
input variable) between any selected output and input guards,
reduction under `|` and `ν`, and reduction up to structural
congruence.

Formalized by `Cslib.PiCalculus.Step`, an inductive type declared in [CSLibExt/Languages/PiCalculus/Basic.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Basic.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/the-calculus-syntax-substitution-structural-cong/index.html#step).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The π-calculus: syntax, substitution, structural congruence, reduction](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/the-calculus-syntax-substitution-structural-cong/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/process-calculi/calculus/the-calculus-syntax-substitution-structural-cong)
