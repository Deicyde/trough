---
declaration: section
origin: cited
lean: Cslib.Bioinformatics.HMM.alignmentsOfAux, Cslib.Bioinformatics.HMM.alignmentsOf, Cslib.Bioinformatics.HMM.alignmentsOf_cons_cons, Cslib.Bioinformatics.HMM.alignmentsOf_nil_cons, Cslib.Bioinformatics.HMM.alignmentsOf_cons_nil, Cslib.Bioinformatics.HMM.mem_alignmentsOf, Cslib.Bioinformatics.HMM.nodup_alignmentsOf, Cslib.Bioinformatics.HMM.alignmentsOf_eq_alignments
statement: formalized
---

# Pair hidden Markov models

44 results, 42 proved and 2 with `sorry` in their value, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html).

## Fuel-bounded enumeration of two-alphabet alignments

All alignments of `xs : List α` with `ys : List β`, by fuel recursion on the first column
(the same recursion as `Cslib.Algorithms.Lean.alignmentsAux`, for two alphabets). Implementation
detail: use `alignmentsOf`, whose fuel `xs.length + ys.length + 1` is enough.

Formalized by `Cslib.Bioinformatics.HMM.alignmentsOfAux`, a definition declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#alignments-of-aux).

## All alignments of sequences over two alphabets

All alignments of a sequence over `α` with a sequence over `β`: lists of columns
`Option α × Option β` with no `(none, none)` column whose rows filter to `xs` and `ys`
(`mem_alignmentsOf`), each listed once (`nodup_alignmentsOf`). For `β = α` this is
`Cslib.Algorithms.Lean.alignments` (`alignmentsOf_eq_alignments`).

Formalized by `Cslib.Bioinformatics.HMM.alignmentsOf`, a definition declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#alignments-of).

## Alignments of two nonempty sequences by first column

The alignments of two nonempty sequences, by their first column.

Formalized by `Cslib.Bioinformatics.HMM.alignmentsOf_cons_cons`, a theorem declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#alignments-of-cons-cons).

## Alignments of the empty sequence with a nonempty one

The alignments of the empty sequence with a nonempty one.

Formalized by `Cslib.Bioinformatics.HMM.alignmentsOf_nil_cons`, a theorem declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#alignments-of-nil-cons).

## Alignments of a nonempty sequence with the empty one

The alignments of a nonempty sequence with the empty one.

Formalized by `Cslib.Bioinformatics.HMM.alignmentsOf_cons_nil`, a theorem declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#alignments-of-cons-nil).

## Membership in `alignmentsOf` is validity

No `(none, none)` column, and the rows filter
to the two sequences.

Formalized by `Cslib.Bioinformatics.HMM.mem_alignmentsOf`, a theorem declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#mem-alignments-of).

## Each alignment is listed once

**Each alignment is listed once.**

Formalized by `Cslib.Bioinformatics.HMM.nodup_alignmentsOf`, a theorem declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#nodup-alignments-of).

## Two-alphabet alignments agree with single-alphabet alignments

On one alphabet, `alignmentsOf` is `Cslib.Algorithms.Lean.alignments`.

Formalized by `Cslib.Bioinformatics.HMM.alignmentsOf_eq_alignments`, a theorem declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#alignments-of-eq-alignments).

## Weighted alignment automaton

A weighted automaton reading an alignment of a sequence over `α` with a sequence over `β`
column by column with a control state in `Q`: the weight of reading a column in a control
state, the next control state, and the final weight of a control state. Weights are in `R`.

Formalized by `Cslib.Bioinformatics.HMM.AlignmentAutomaton`, a structure declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#alignment-automaton).

## Weight of an alignment read by an automaton

The weight of an alignment read from control state `q`: the product of the column weights
along the alignment, then the final weight.

Formalized by `Cslib.Bioinformatics.HMM.AlignmentAutomaton.alignWeight`, a definition declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#align-weight).

## Fuel-bounded sum recursion over alignments

The sum recursion with fuel (the fuel bounds the recursion depth). Implementation detail:
use `sumDP`, whose fuel `xs.length + ys.length + 1` is enough.

Formalized by `Cslib.Bioinformatics.HMM.AlignmentAutomaton.sumDPAux`, a definition declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#sum-dpaux).

## Total alignment weight by first-column recursion

The total weight of all alignments of `xs` and `ys` read from control state `q`, by the
first-column recursion (`sumDP_eq_sum`).

Formalized by `Cslib.Bioinformatics.HMM.AlignmentAutomaton.sumDP`, a definition declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#sum-dp).

## The sum recursion is the sum over alignments

**The sum recursion is the sum over alignments.**

Formalized by `Cslib.Bioinformatics.HMM.AlignmentAutomaton.sumDP_eq_sum`, a theorem declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#sum-dp-eq-sum).

## Sum recursion on two nonempty sequences

The sum recursion on two nonempty sequences.

Formalized by `Cslib.Bioinformatics.HMM.AlignmentAutomaton.sumDP_cons_cons`, a theorem declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 330](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L330). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#sum-dp-cons-cons).

## Sum recursion with an empty first sequence

The sum recursion when the first sequence is empty.

Formalized by `Cslib.Bioinformatics.HMM.AlignmentAutomaton.sumDP_nil_cons`, a theorem declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 339](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L339). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#sum-dp-nil-cons).

## Sum recursion with an empty second sequence

The sum recursion when the second sequence is empty.

Formalized by `Cslib.Bioinformatics.HMM.AlignmentAutomaton.sumDP_cons_nil`, a theorem declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 346](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L346). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#sum-dp-cons-nil).

## Sum recursion on two empty sequences is the final weight

The sum recursion on two empty sequences is the final weight.

Formalized by `Cslib.Bioinformatics.HMM.AlignmentAutomaton.sumDP_nil_nil`, a theorem declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 353](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L353). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#sum-dp-nil-nil).

## Fuel-bounded max recursion over alignments

The max recursion with fuel. Implementation detail: use `maxDP`.

Formalized by `Cslib.Bioinformatics.HMM.AlignmentAutomaton.maxDPAux`, a definition declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 362](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L362). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#max-dpaux).

## Max-recursion alignment value from a control state

The max-recursion value of an alignment of `xs` and `ys` read from control state `q`, by
the first-column recursion (`alignWeight_le_maxDP`, `exists_alignWeight_eq_maxDP`). It is the
largest alignment weight only when the weights are nonnegative; in general it is the value of
the recursively chosen alignment.

Formalized by `Cslib.Bioinformatics.HMM.AlignmentAutomaton.maxDP`, a definition declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 378](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L378). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#max-dp).

## Nonnegative column weights of an alignment automaton

Nonnegative column weights. The final weights may have any sign: the max recursion bounds
every alignment weight without that (`alignWeight_le_maxDP`).

Formalized by `Cslib.Bioinformatics.HMM.AlignmentAutomaton.Nonneg`, a definition declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 383](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L383). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#nonneg).

## Every alignment weighs at most the max recursion

**Every alignment weighs at most the max recursion** (nonnegative weights).

Formalized by `Cslib.Bioinformatics.HMM.AlignmentAutomaton.alignWeight_le_maxDP`, a theorem declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 473](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L473). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#align-weight-le-max-dp).

## The max recursion is attained

**The max recursion is attained** by an alignment.

Formalized by `Cslib.Bioinformatics.HMM.AlignmentAutomaton.exists_alignWeight_eq_maxDP`, a theorem declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 480](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L480). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#exists-align-weight-eq-max-dp).

## Max recursion on two nonempty sequences

The max recursion on two nonempty sequences.

Formalized by `Cslib.Bioinformatics.HMM.AlignmentAutomaton.maxDP_cons_cons`, a theorem declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 485](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L485). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#max-dp-cons-cons).

## Max recursion with an empty first sequence

The max recursion when the first sequence is empty.

Formalized by `Cslib.Bioinformatics.HMM.AlignmentAutomaton.maxDP_nil_cons`, a theorem declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 496](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L496). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#max-dp-nil-cons).

## Max recursion with an empty second sequence

The max recursion when the second sequence is empty.

Formalized by `Cslib.Bioinformatics.HMM.AlignmentAutomaton.maxDP_cons_nil`, a theorem declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 503](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L503). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#max-dp-cons-nil).

## Max recursion on two empty sequences is the final weight

The max recursion on two empty sequences is the final weight.

Formalized by `Cslib.Bioinformatics.HMM.AlignmentAutomaton.maxDP_nil_nil`, a theorem declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 510](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L510). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#max-dp-nil-nil).

## Emitting states of a pair HMM

The emitting states of a pair HMM: `M` emits an aligned pair, `X` a letter of the first
sequence only, `Y` a letter of the second sequence only.

Formalized by `Cslib.Bioinformatics.HMM.PairState`, an inductive type declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 520](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L520). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#pair-state).

## Pair HMM state emitting an alignment column

The state that emits an alignment column: `M` for `(some a, some b)`, `X` for
`(some a, none)`, `Y` for `(none, some b)` (and `M`, unused, for the invalid `(none, none)`).

Formalized by `Cslib.Bioinformatics.HMM.colState`, a definition declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 531](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L531). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#col-state).

## Pair hidden Markov model

A pair HMM over the alphabet `α` with weights in `R` (Durbin et al., chapter 4): the
transition weights from the silent begin state (`start`) and between emitting states (`trans`),
to the silent end state (`stop` from an emitting state, `startStop` for the empty alignment),
and the emission weights of the three emitting states.

Formalized by `Cslib.Bioinformatics.HMM.PairHMM`, a structure declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 540](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L540). Its value contains `sorry`. [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#pair-hmm).

## Emission weight of an alignment column

The emission weight of an alignment column (`0` for the invalid `(none, none)`).

Formalized by `Cslib.Bioinformatics.HMM.PairHMM.emitCol`, a definition declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 565](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L565). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#emit-col).

## Pair HMM as an alignment automaton

The pair HMM as an alignment automaton: the control state is the previous HMM state
(`none` for the begin state).

Formalized by `Cslib.Bioinformatics.HMM.PairHMM.toAutomaton`, a definition declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 573](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L573). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#to-automaton).

## Joint weight of sequences and an alignment's state path

The joint weight of the sequences and the state path of an alignment `A` (the path visits
`colState c` for each column `c`): the product of the transition and emission weights along the
path, from the begin state to the end state.

Formalized by `Cslib.Bioinformatics.HMM.PairHMM.alignProb`, a definition declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 585](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L585). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#align-prob).

## Total weight of a sequence pair under a pair HMM

The total weight `P(xs, ys)` of a pair HMM: the total weight of all state paths that emit
`xs` and `ys` (`likelihood_eq_sum`), by the first-column recursion.

Formalized by `Cslib.Bioinformatics.HMM.PairHMM.likelihood`, a definition declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 589](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L589). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#likelihood).

## The pair-HMM recursion computes the total weight

The sum over all alignments of
`xs` and `ys` of the joint weight of the sequences and the alignment.

Formalized by `Cslib.Bioinformatics.HMM.PairHMM.likelihood_eq_sum`, a theorem declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 593](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L593). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#likelihood-eq-sum).

## Viterbi value of a pair HMM

The Viterbi value of a pair HMM: the max-recursion value for `xs`, `ys`. It is the
largest joint weight over alignments when the HMM weights are nonnegative
(see `alignProb_le_viterbi`).

Formalized by `Cslib.Bioinformatics.HMM.PairHMM.viterbi`, a definition declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 607](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L607). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#viterbi).

## Nonnegative weights of a pair HMM

Nonnegative transition weights into emitting states and nonnegative emission weights (the
transitions into the end state may have any sign: the Viterbi bound does not need them).

Formalized by `Cslib.Bioinformatics.HMM.PairHMM.Nonneg`, a structure declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 611](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L611). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#nonneg-2).

## Nonnegative pair HMM gives a nonnegative alignment automaton

A pair HMM with nonnegative weights is a nonnegative alignment automaton.

Formalized by `Cslib.Bioinformatics.HMM.PairHMM.toAutomaton_nonneg`, a theorem declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 626](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L626). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#to-automaton-nonneg).

## Every alignment weighs at most the Viterbi value

**Every alignment weighs at most the Viterbi value.**

Formalized by `Cslib.Bioinformatics.HMM.PairHMM.alignProb_le_viterbi`, a theorem declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 635](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L635). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#align-prob-le-viterbi).

## The Viterbi value is attained

**The Viterbi value is attained** by an alignment: the Viterbi alignment.

Formalized by `Cslib.Bioinformatics.HMM.PairHMM.exists_alignProb_eq_viterbi`, a theorem declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 642](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L642). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#exists-align-prob-eq-viterbi).

## Memoryless pair HMM

The pair HMM's transition weights do not depend on the current state: every transition into
an emitting state `s` (from the begin state or from any emitting state) has weight `π s`, and
every transition into the end state has weight `τ`.

Formalized by `Cslib.Bioinformatics.HMM.PairHMM.IsMemoryless`, a structure declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 657](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L657). Its value contains `sorry`. [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#is-memoryless).

## Independence-model weight of a sequence pair

The independence-model weight for `xs` and `ys` (Durbin et al., chapter 4):
`η² (1 - η)^(|xs| + |ys|) ∏ q xs ∏ q ys`. This is a probability when `q` is a
normalized nonnegative distribution and `0 < η < 1`, as required by `LinearGapLogOdds`.

Formalized by `Cslib.Bioinformatics.HMM.PairHMM.background`, a definition declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 670](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L670). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#background).

## Hypotheses of the linear-gap log-odds correspondence

The hypotheses of the log-odds correspondence: a memoryless pair HMM with normalized
positive transition and emission probabilities, normalized positive background frequencies
and `0 < η < 1`, whose per-column log-odds scores against the independence model are the
integer scores `σ a b` (aligned pair) and `gap` (gap column).

Formalized by `Cslib.Bioinformatics.HMM.PairHMM.LinearGapLogOdds`, a structure declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 679](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L679). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#linear-gap-log-odds).

## Log-odds of one alignment

For a memoryless pair HMM, the log-odds of an alignment
against the independence model is its linear-gap alignment score plus `log (τ / η²)`.

Formalized by `Cslib.Bioinformatics.HMM.PairHMM.log_alignProb_div_background`, a theorem declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 823](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L823). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#log-align-prob-div-background).

## Log-odds Viterbi is linear-gap Needleman–Wunsch

For a memoryless pair HMM whose
per-column log-odds scores are `σ a b` and `gap`, the log-odds Viterbi score against the
independence model is the Needleman–Wunsch score with substitution scores `σ` and linear gap
score `gap`, plus the length term `log (τ / η²)`.

Formalized by `Cslib.Bioinformatics.HMM.PairHMM.log_viterbi_div_background`, a theorem declared in [CSLibExt/Bioinformatics/HMM/PairHMM.lean, line 848](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/HMM/PairHMM.lean#L848). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html#log-viterbi-div-background).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pair hidden Markov models](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/bioinformatics/sequence-alignment/pair-hidden-markov-models)
