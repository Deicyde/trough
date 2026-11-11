---
declaration: section
origin: cited
lean: Cslib.Bioinformatics.HMM.ProfileState, Cslib.Bioinformatics.HMM.ProfileHMM, Cslib.Bioinformatics.HMM.ProfileHMM.columns, Cslib.Bioinformatics.HMM.ProfileHMM.IsPlan7, Cslib.Bioinformatics.HMM.ProfileHMM.toAutomaton, Cslib.Bioinformatics.HMM.ProfileHMM.pathProb, Cslib.Bioinformatics.HMM.ProfileHMM.forward, Cslib.Bioinformatics.HMM.ProfileHMM.forward_eq_sum
statement: formalized
---

# Profile hidden Markov models

16 results, 15 proved and 1 with `sorry` in its value, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/profile-hidden-markov-models/index.html).

## State types of a profile HMM node

The state types of a profile HMM node: match, insert, delete.

Formalized by `Cslib.Bioinformatics.HMM.ProfileState`, an inductive type declared in [CSLibExt/Bioinformatics/HMM/ProfileHMM.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/HMM/ProfileHMM.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/profile-hidden-markov-models/index.html#profile-state).

## Profile hidden Markov model

A profile HMM with `L` consensus columns over the alphabet `α`, with weights in `R`.
`trans k s t` is the weight of a transition from the state of type `s` at node `k`
(`0 ≤ k ≤ L`; node `0` is the begin state, read as type `M`) to a state of type `t`: to `M`
or `D` at node `k + 1`, or to `I` at node `k`. `stop s` is the weight of the transition from the
state of type `s` at node `L` to the end state.

Formalized by `Cslib.Bioinformatics.HMM.ProfileHMM`, a structure declared in [CSLibExt/Bioinformatics/HMM/ProfileHMM.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/HMM/ProfileHMM.lean#L95). Its value contains `sorry`. [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/profile-hidden-markov-models/index.html#profile-hmm).

## Consensus columns of a profile HMM

The consensus columns `[1, …, L]`.

Formalized by `Cslib.Bioinformatics.HMM.ProfileHMM.columns`, a definition declared in [CSLibExt/Bioinformatics/HMM/ProfileHMM.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/HMM/ProfileHMM.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/profile-hidden-markov-models/index.html#columns).

## HMMER Plan 7 restrictions

HMMER's Plan 7 restrictions (Eddy 1998): no delete-to-insert and no insert-to-delete
transitions, and no insert states at node `0` (the begin state) or node `L`.

Formalized by `Cslib.Bioinformatics.HMM.ProfileHMM.IsPlan7`, a structure declared in [CSLibExt/Bioinformatics/HMM/ProfileHMM.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/HMM/ProfileHMM.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/profile-hidden-markov-models/index.html#is-plan7).

## Profile HMM as an alignment automaton

The profile HMM as an alignment automaton reading alignments of a sequence to the columns
`[1, …, L]`. The control state is the type of the previous state and the current node (the last
column consumed); it starts at `(M, 0)`, the begin state. Reading `(some a, some j)` visits `M j`,
`(some a, none)` visits the insert state of the current node, `(none, some j)` visits `D j`; the
invalid column `(none, none)` has weight `0`.

Formalized by `Cslib.Bioinformatics.HMM.ProfileHMM.toAutomaton`, a definition declared in [CSLibExt/Bioinformatics/HMM/ProfileHMM.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/HMM/ProfileHMM.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/profile-hidden-markov-models/index.html#to-automaton).

## Weight of a path through a profile HMM

The weight of a path through the model, given as an alignment `A` of the sequence to the
columns: the product of its transition and emission weights from the begin state to the end
state.

Formalized by `Cslib.Bioinformatics.HMM.ProfileHMM.pathProb`, a definition declared in [CSLibExt/Bioinformatics/HMM/ProfileHMM.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/HMM/ProfileHMM.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/profile-hidden-markov-models/index.html#path-prob).

## Forward value of a sequence under a profile HMM

The forward value of a sequence `x`: the total weight of all paths through the model that
emit `x` (`forward_eq_sum`), by the recursion on one residue and one column.

Formalized by `Cslib.Bioinformatics.HMM.ProfileHMM.forward`, a definition declared in [CSLibExt/Bioinformatics/HMM/ProfileHMM.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/HMM/ProfileHMM.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/profile-hidden-markov-models/index.html#forward).

## Forward computes the total path weight

The sum, over all alignments of `x` to the
columns `[1, …, L]` (all paths through the model emitting `x`, each once), of the path
weights.

Formalized by `Cslib.Bioinformatics.HMM.ProfileHMM.forward_eq_sum`, a theorem declared in [CSLibExt/Bioinformatics/HMM/ProfileHMM.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/HMM/ProfileHMM.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/profile-hidden-markov-models/index.html#forward-eq-sum).

## Viterbi value of a sequence under a profile HMM

The Viterbi value of a sequence `x`: the value selected by the max recursion
(`pathProb_le_viterbi`, `exists_pathProb_eq_viterbi`). Under nonnegative weights it is the
largest weight of a path through the model emitting `x`.

Formalized by `Cslib.Bioinformatics.HMM.ProfileHMM.viterbi`, a definition declared in [CSLibExt/Bioinformatics/HMM/ProfileHMM.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/HMM/ProfileHMM.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/profile-hidden-markov-models/index.html#viterbi).

## Nonnegative weights of a profile HMM

Nonnegative transition and emission weights (the transitions to the end state may have any
sign: the Viterbi bound does not need them).

Formalized by `Cslib.Bioinformatics.HMM.ProfileHMM.Nonneg`, a structure declared in [CSLibExt/Bioinformatics/HMM/ProfileHMM.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/HMM/ProfileHMM.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/profile-hidden-markov-models/index.html#nonneg).

## Nonnegative profile HMM gives a nonnegative alignment automaton

A profile HMM with nonnegative weights is a nonnegative alignment automaton.

Formalized by `Cslib.Bioinformatics.HMM.ProfileHMM.toAutomaton_nonneg`, a theorem declared in [CSLibExt/Bioinformatics/HMM/ProfileHMM.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/HMM/ProfileHMM.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/profile-hidden-markov-models/index.html#to-automaton-nonneg).

## Every path weighs at most the Viterbi value

**Every path weighs at most the Viterbi value.**

Formalized by `Cslib.Bioinformatics.HMM.ProfileHMM.pathProb_le_viterbi`, a theorem declared in [CSLibExt/Bioinformatics/HMM/ProfileHMM.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/HMM/ProfileHMM.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/profile-hidden-markov-models/index.html#path-prob-le-viterbi).

## The Viterbi value is attained

Some path (alignment of `x` to the profile) has
weight equal to the Viterbi value. Under nonnegative weights this attained value is the
largest path weight (`pathProb_le_viterbi`); without that hypothesis attainment alone
does not imply maximality.

Formalized by `Cslib.Bioinformatics.HMM.ProfileHMM.exists_pathProb_eq_viterbi`, a theorem declared in [CSLibExt/Bioinformatics/HMM/ProfileHMM.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/HMM/ProfileHMM.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/profile-hidden-markov-models/index.html#exists-path-prob-eq-viterbi).

## Pseudocount emission estimate of a match state

The emission estimate of a match state from the residues `col` that a multiple alignment
places in its column (gaps omitted), with pseudocounts `pc` (Durbin et al., chapter 5;
Laplace's rule is `pc = 1`): `(count a + pc a) / (|col| + ∑ b, pc b)`.

Formalized by `Cslib.Bioinformatics.HMM.ProfileHMM.pseudocountEmission`, a definition declared in [CSLibExt/Bioinformatics/HMM/ProfileHMM.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/HMM/ProfileHMM.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/profile-hidden-markov-models/index.html#pseudocount-emission).

## Pseudocount emission estimates sum to one

With positive pseudocounts, the estimated emissions sum to one.

Formalized by `Cslib.Bioinformatics.HMM.ProfileHMM.sum_pseudocountEmission`, a theorem declared in [CSLibExt/Bioinformatics/HMM/ProfileHMM.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/HMM/ProfileHMM.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/profile-hidden-markov-models/index.html#sum-pseudocount-emission).

## Pseudocount emission estimates are positive

With positive pseudocounts, every residue gets a positive emission estimate, including
residues absent from the column.

Formalized by `Cslib.Bioinformatics.HMM.ProfileHMM.pseudocountEmission_pos`, a theorem declared in [CSLibExt/Bioinformatics/HMM/ProfileHMM.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/HMM/ProfileHMM.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/profile-hidden-markov-models/index.html#pseudocount-emission-pos).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Profile hidden Markov models](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/profile-hidden-markov-models/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/bioinformatics/sequence-alignment/profile-hidden-markov-models)
