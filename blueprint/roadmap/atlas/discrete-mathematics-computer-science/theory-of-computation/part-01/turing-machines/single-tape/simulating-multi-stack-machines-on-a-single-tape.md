---
declaration: section
origin: cited
lean: MetaMathlibExt.TM2ToTM0.tr, MetaMathlibExt.TM2ToTM0.tr_eval_dom, MetaMathlibExt.TM2ToTM0.tr_supports, MetaMathlibExt.TM2ToTM0.supportsStmt_univ, MetaMathlibExt.TM2ToTM0.supports_univ, MetaMathlibExt.TM2ToTM0.initList_eq_init
statement: formalized
proof: formalized
---

# Simulating multi-stack machines on a single tape

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/simulating-multi-stack-machines-on-a-single-tape/index.html).

## Two-step single-tape translation of a multi-stack machine

For a multi-stack Turing
machine $M$ with stacks indexed by $K$ and stack alphabets $\Gamma_k$, this is the single-tape
machine obtained by translating $M$ first into a single-tape machine with a store and then into a
plain single-tape machine. Its tape alphabet consists of a bottom-of-stack flag together with one
optional symbol of $\Gamma_k$ for each stack $k$. Its states are pairs of an optional statement of
the intermediate machine and a value of the internal state of $M$.

Formalized by `MetaMathlibExt.TM2ToTM0.tr`, an abbreviation declared in [MathlibExt/Computability/TuringMachine/Translation/TM2ToTM0.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Computability/TuringMachine/Translation/TM2ToTM0.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/simulating-multi-stack-machines-on-a-single-tape/index.html#tr).

## The emulation halts iff the multi-stack machine halts

Let $M$ be a multi-stack Turing
machine with stacks indexed by $K$, let $k \in K$, and let $L$ be a list over the alphabet of stack
$k$. The single-tape emulation of $M$, started on the tape encoding of the stacks with $L$ on stack
$k$ and all other stacks empty, halts if and only if $M$, started with $L$ on stack $k$ and all
other stacks empty, halts.

Formalized by `MetaMathlibExt.TM2ToTM0.tr_eval_dom`, a theorem declared in [MathlibExt/Computability/TuringMachine/Translation/TM2ToTM0.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Computability/TuringMachine/Translation/TM2ToTM0.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/simulating-multi-stack-machines-on-a-single-tape/index.html#tr-eval-dom).

## The emulation visits finitely many states

Let $M$ be a multi-stack Turing machine whose
internal state type is finite, and let $S$ be a finite set of labels that supports $M$. Then the
single-tape emulation of $M$ is supported by an explicit finite set of states built from $S$ through
the two translations: this set contains the initial state and is closed under the transitions of the
emulation.

Formalized by `MetaMathlibExt.TM2ToTM0.tr_supports`, a theorem declared in [MathlibExt/Computability/TuringMachine/Translation/TM2ToTM0.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Computability/TuringMachine/Translation/TM2ToTM0.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/simulating-multi-stack-machines-on-a-single-tape/index.html#tr-supports).

## Every statement is supported by all labels

If the label type $\Lambda$ is finite, then
every statement of a multi-stack Turing machine with labels $\Lambda$ is supported by the finite set
of all labels: every label it can jump to lies in this set.

Formalized by `MetaMathlibExt.TM2ToTM0.supportsStmt_univ`, a theorem declared in [MathlibExt/Computability/TuringMachine/Translation/TM2ToTM0.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Computability/TuringMachine/Translation/TM2ToTM0.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/simulating-multi-stack-machines-on-a-single-tape/index.html#supports-stmt-univ).

## A multi-stack machine is supported by all its labels

A multi-stack Turing machine with
finitely many labels is supported by the set of all its labels: this set contains the default label,
and every statement of the machine is supported by it.

Formalized by `MetaMathlibExt.TM2ToTM0.supports_univ`, a theorem declared in [MathlibExt/Computability/TuringMachine/Translation/TM2ToTM0.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Computability/TuringMachine/Translation/TM2ToTM0.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/simulating-multi-stack-machines-on-a-single-tape/index.html#supports-univ).

## The initial configuration of a bundled multi-stack machine

For a bundled multi-stack Turing
machine and every list $l$ over the alphabet of its input stack, the initial configuration of the
bundled machine on $l$ equals the generic multi-stack initial configuration with $l$ on the input
stack, when the main label is taken as the default label.

Formalized by `MetaMathlibExt.TM2ToTM0.initList_eq_init`, a theorem declared in [MathlibExt/Computability/TuringMachine/Translation/TM2ToTM0.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Computability/TuringMachine/Translation/TM2ToTM0.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/simulating-multi-stack-machines-on-a-single-tape/index.html#init-list-eq-init).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Simulating multi-stack machines on a single tape](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/simulating-multi-stack-machines-on-a-single-tape/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/turing-machines/single-tape/simulating-multi-stack-machines-on-a-single-tape)
