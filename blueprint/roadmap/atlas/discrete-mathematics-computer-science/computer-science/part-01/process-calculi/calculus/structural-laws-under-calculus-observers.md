---
declaration: section
origin: cited
lean: Cslib.PiCalculus.Context, Cslib.PiCalculus.Context.fill, Cslib.PiCalculus.Cong.fill, Cslib.PiCalculus.Context.comp, Cslib.PiCalculus.Context.fill_comp, Cslib.PiCalculus.ContextualBarbedEquiv, Cslib.PiCalculus.Cong.contextualBarbedEquiv, Cslib.PiCalculus.ContextualBarbedEquiv.fill
statement: formalized
proof: formalized
---

# Structural laws under π-calculus observers

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/structural-laws-under-calculus-observers/index.html).

## One-hole lexical process contexts

One-hole lexical contexts, including guards, choice and replication.

Formalized by `Cslib.PiCalculus.Context`, an inductive type declared in [CSLibExt/Languages/PiCalculus/Contextual.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Contextual.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/structural-laws-under-calculus-observers/index.html#context).

## Lexical filling of a process context

Fill the lexical hole. Free constants are never captured; locally
closed hole processes have no references into surrounding binders.

Formalized by `Cslib.PiCalculus.Context.fill`, a definition declared in [CSLibExt/Languages/PiCalculus/Contextual.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Contextual.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/structural-laws-under-calculus-observers/index.html#fill).

## Structural congruence is closed under contexts

Structural congruence survives every one-hole lexical context.

Formalized by `Cslib.PiCalculus.Cong.fill`, a theorem declared in [CSLibExt/Languages/PiCalculus/Contextual.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Contextual.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/structural-laws-under-calculus-observers/index.html#fill-2).

## Composition of process contexts

Substitute a context into the hole of another context.

Formalized by `Cslib.PiCalculus.Context.comp`, a definition declared in [CSLibExt/Languages/PiCalculus/Contextual.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Contextual.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/structural-laws-under-calculus-observers/index.html#comp).

## Filling a composed context is iterated filling

Context composition agrees with iterated filling.

Formalized by `Cslib.PiCalculus.Context.fill_comp`, a theorem declared in [CSLibExt/Languages/PiCalculus/Contextual.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Contextual.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/structural-laws-under-calculus-observers/index.html#fill-comp).

## Contextual strong barbed equivalence

Strong barbed equivalence in every lexical process context. For
capture-avoiding use, both hole processes must satisfy `Proc.ClosedAt 0`.

Formalized by `Cslib.PiCalculus.ContextualBarbedEquiv`, a definition declared in [CSLibExt/Languages/PiCalculus/Contextual.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Contextual.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/structural-laws-under-calculus-observers/index.html#contextual-barbed-equiv).

## Structural congruence implies contextual barbed equivalence

Structural congruence is sound under every observer context, with
one-for-one reduction matching and immediate input/output barbs.

Formalized by `Cslib.PiCalculus.Cong.contextualBarbedEquiv`, a theorem declared in [CSLibExt/Languages/PiCalculus/Contextual.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Contextual.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/structural-laws-under-calculus-observers/index.html#contextual-barbed-equiv-2).

## Contextual barbed equivalence is closed under contexts

Contextual barbed equivalence survives filling a context.

Formalized by `Cslib.PiCalculus.ContextualBarbedEquiv.fill`, a theorem declared in [CSLibExt/Languages/PiCalculus/Contextual.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Contextual.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/structural-laws-under-calculus-observers/index.html#fill-3).

## Contextual barbed equivalence implies barbed bisimilarity

Contextual barbed equivalence implies standalone barbed bisimilarity.

Formalized by `Cslib.PiCalculus.ContextualBarbedEquiv.barbedBisimilar`, a theorem declared in [CSLibExt/Languages/PiCalculus/Contextual.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Contextual.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/structural-laws-under-calculus-observers/index.html#barbed-bisimilar).

## Capture-avoiding filling of a process context

Capture-avoiding filling: each context binder shifts dangling names
of the hole, while binders internal to the hole remain untouched.

Formalized by `Cslib.PiCalculus.Context.fillAvoiding`, a definition declared in [CSLibExt/Languages/PiCalculus/Contextual.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Contextual.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/structural-laws-under-calculus-observers/index.html#fill-avoiding).

## Capture-avoiding and lexical filling agree on locally closed holes

Lexical and capture-avoiding filling agree for locally closed holes.
This is the explicit admissibility condition for the contextual theorem.

Formalized by `Cslib.PiCalculus.Context.fillAvoiding_eq`, a theorem declared in [CSLibExt/Languages/PiCalculus/Contextual.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Contextual.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/structural-laws-under-calculus-observers/index.html#fill-avoiding-eq).

## Structural laws are barbed sound in capture-avoiding contexts

Every structural law is strongly barbed sound under capture-avoiding
contexts, for locally closed hole processes.

Formalized by `Cslib.PiCalculus.Cong.fillAvoiding_barbedBisimilar`, a theorem declared in [CSLibExt/Languages/PiCalculus/Contextual.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Contextual.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/structural-laws-under-calculus-observers/index.html#fill-avoiding-barbed-bisimilar).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Structural laws under π-calculus observers](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/structural-laws-under-calculus-observers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/process-calculi/calculus/structural-laws-under-calculus-observers)
