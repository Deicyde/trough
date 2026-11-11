---
declaration: section
origin: cited
lean: Cslib.IMP.ACmd, Cslib.IMP.ACmd.strip, Cslib.IMP.ACmd.pre, Cslib.IMP.ACmd.vc, Cslib.IMP.ACmd.vc_sound, Cslib.IMP.ACmd.vc_valid, Cslib.IMP.ACmd.pre_entails_vc, Cslib.IMP.ACmd.vc_complete
statement: formalized
proof: formalized
---

# Verification-condition generation

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/verification-condition-generation/index.html).

## IMP

## Annotated commands

An annotated command is built like an IMP command, from skip,
assignments $x := a$ of an arithmetic expression $a$ to a variable $x$ (a natural number),
sequential composition $C_1;\,C_2$ and conditionals
$\mathrm{if}\ b\ \mathrm{then}\ C_1\ \mathrm{else}\ C_2$ on a boolean expression $b$, except that
every while loop $\{I\}\ \mathrm{while}\ b\ \mathrm{do}\ C$ also carries an assertion $I$, its
invariant.

Formalized by `Cslib.IMP.ACmd`, an inductive type declared in [CSLibExt/Languages/IMP/VCG.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/VCG.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/verification-condition-generation/index.html#acmd).

## Erasing annotations

The IMP command $\mathrm{strip}(C)$ underlying an annotated command
$C$ is obtained by deleting the invariant of every while loop: skip, assignments, sequential
composition and conditionals are kept with their parts stripped, and
$\{I\}\ \mathrm{while}\ b\ \mathrm{do}\ C'$ becomes
$\mathrm{while}\ b\ \mathrm{do}\ \mathrm{strip}(C')$.

Formalized by `Cslib.IMP.ACmd.strip`, a definition declared in [CSLibExt/Languages/IMP/VCG.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/VCG.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/verification-condition-generation/index.html#strip).

## Precondition of an annotated command

For an annotated command $C$ and an assertion $Q$
(the postcondition), the precondition $\mathrm{pre}(C, Q)$ is the assertion computed backwards
as follows: $\mathrm{pre}(\mathrm{skip}, Q) = Q$; $\mathrm{pre}(x := a, Q)$ holds in a state $s$
iff $Q$ holds in the state obtained from $s$ by giving $x$ the value of $a$ in $s$;
$\mathrm{pre}(C_1;\,C_2, Q) = \mathrm{pre}(C_1, \mathrm{pre}(C_2, Q))$; the precondition of
$\mathrm{if}\ b\ \mathrm{then}\ C_1\ \mathrm{else}\ C_2$ for $Q$ holds in a state $s$ iff
$\mathrm{pre}(C_1, Q)$ holds in $s$ when $b$ is true in $s$, and $\mathrm{pre}(C_2, Q)$ holds in
$s$ when $b$ is false in $s$; and the precondition of a loop
$\{I\}\ \mathrm{while}\ b\ \mathrm{do}\ C$ is its invariant $I$, whatever $Q$ is.

Formalized by `Cslib.IMP.ACmd.pre`, a definition declared in [CSLibExt/Languages/IMP/VCG.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/VCG.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/verification-condition-generation/index.html#pre).

## Verification condition of an annotated command

For an annotated command $C$ and an
assertion $Q$ (the postcondition), the verification condition $\mathrm{vc}(C, Q)$ is the
proposition defined as follows, where $\mathrm{pre}$ is the precondition of an annotated
command: $\mathrm{vc}(\mathrm{skip}, Q)$ and $\mathrm{vc}(x := a, Q)$ are true;
$\mathrm{vc}(C_1;\,C_2, Q)$ holds iff $\mathrm{vc}(C_1, \mathrm{pre}(C_2, Q))$ and
$\mathrm{vc}(C_2, Q)$ hold; the verification condition of
$\mathrm{if}\ b\ \mathrm{then}\ C_1\ \mathrm{else}\ C_2$ for $Q$ holds iff $\mathrm{vc}(C_1, Q)$
and $\mathrm{vc}(C_2, Q)$ hold; and for a loop $\{I\}\ \mathrm{while}\ b\ \mathrm{do}\ C'$, the
verification condition for $Q$ holds iff every state satisfying $I$ in which $b$ is true
satisfies $\mathrm{pre}(C', I)$, every state satisfying $I$ in which $b$ is false satisfies
$Q$, and $\mathrm{vc}(C', I)$ holds.

Formalized by `Cslib.IMP.ACmd.vc`, a definition declared in [CSLibExt/Languages/IMP/VCG.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/VCG.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/verification-condition-generation/index.html#vc).

## Soundness of verification conditions

For an annotated command $C$ and an assertion $Q$,
write $\mathrm{pre}(C, Q)$ and $\mathrm{vc}(C, Q)$ for the precondition and the verification
condition of $C$ for the postcondition $Q$, and $\mathrm{strip}(C)$ for the IMP command obtained
from $C$ by erasing its loop invariants. For every such $C$ and $Q$, if $\mathrm{vc}(C, Q)$
holds, then the Hoare triple $\{\mathrm{pre}(C, Q)\}\ \mathrm{strip}(C)\ \{Q\}$ is derivable in
the partial-correctness Hoare logic.

Formalized by `Cslib.IMP.ACmd.vc_sound`, a theorem declared in [CSLibExt/Languages/IMP/VCG.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/VCG.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/verification-condition-generation/index.html#vc-sound).

## Verification conditions yield valid Hoare triples

Let $C$ be an annotated command, let
$\mathrm{strip}(C)$ be the IMP command obtained from $C$ by erasing its loop invariants, and let
$P$, $Q$ be assertions. If the verification condition $\mathrm{vc}(C, Q)$ holds and $P$ entails
the precondition $\mathrm{pre}(C, Q)$, then the partial-correctness Hoare triple
$\{P\}\ \mathrm{strip}(C)\ \{Q\}$ is valid.

Formalized by `Cslib.IMP.ACmd.vc_valid`, a theorem declared in [CSLibExt/Languages/IMP/VCG.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/VCG.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/verification-condition-generation/index.html#vc-valid).

## Weakening the postcondition of an annotated command

Let $C$ be an annotated command and
$Q$, $Q'$ assertions such that $Q$ entails $Q'$, and write $\mathrm{pre}(C, Q)$ and
$\mathrm{vc}(C, Q)$ for the precondition and the verification condition of $C$ for the
postcondition $Q$. If $\mathrm{vc}(C, Q)$ holds, then $\mathrm{pre}(C, Q)$ entails
$\mathrm{pre}(C, Q')$ and $\mathrm{vc}(C, Q')$ holds.

Formalized by `Cslib.IMP.ACmd.pre_entails_vc`, a theorem declared in [CSLibExt/Languages/IMP/VCG.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/VCG.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/verification-condition-generation/index.html#pre-entails-vc).

## Completeness of verification conditions for derivable triples

Let $c$ be an IMP command
and $P$, $Q$ assertions such that the Hoare triple $\{P\}\ c\ \{Q\}$ is derivable in the
partial-correctness Hoare logic. Then there is an annotated command $C$ such that erasing its
loop invariants gives $c$, that is $\mathrm{strip}(C) = c$, the verification condition
$\mathrm{vc}(C, Q)$ holds, and $P$ entails the precondition $\mathrm{pre}(C, Q)$.

Formalized by `Cslib.IMP.ACmd.vc_complete`, a theorem declared in [CSLibExt/Languages/IMP/VCG.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/VCG.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/verification-condition-generation/index.html#vc-complete).

## Completeness of verification conditions for valid triples

Let $c$ be an IMP command and
$P$, $Q$ assertions such that the partial-correctness Hoare triple $\{P\}\ c\ \{Q\}$ is valid.
Then there is an annotated command $C$ such that erasing its loop invariants gives $c$, that is
$\mathrm{strip}(C) = c$, the verification condition $\mathrm{vc}(C, Q)$ holds, and $P$ entails
the precondition $\mathrm{pre}(C, Q)$.

The proof goes through relative completeness of the Hoare logic.

Formalized by `Cslib.IMP.ACmd.vc_complete_of_valid`, a theorem declared in [CSLibExt/Languages/IMP/VCG.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/IMP/VCG.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/verification-condition-generation/index.html#vc-complete-of-valid).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Verification-condition generation](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/verification-condition-generation/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/program-logics-and-verification/verification-condition-generation)
