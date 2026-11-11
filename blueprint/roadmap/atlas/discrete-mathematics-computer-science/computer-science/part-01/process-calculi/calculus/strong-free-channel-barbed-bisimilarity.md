---
declaration: section
origin: cited
lean: Cslib.PiCalculus.Observable, Cslib.PiCalculus.Offer, Cslib.PiCalculus.Barb, Cslib.PiCalculus.BehaviourLabel, Cslib.PiCalculus.observedLTS, Cslib.PiCalculus.BarbedBisimilar, Cslib.PiCalculus.isBisimulation_observedLTS_iff, Cslib.PiCalculus.Cong.barb_iff
statement: formalized
proof: formalized
---

# Strong free-channel barbed bisimilarity

25 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/strong-free-channel-barbed-bisimilarity/index.html).

## Free-channel input and output observables

A visible input or output subject. Restricted variables are not subjects
of these free-channel observations.

Formalized by `Cslib.PiCalculus.Observable`, an inductive type declared in [CSLibExt/Languages/PiCalculus/Behavioural.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Behavioural.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/strong-free-channel-barbed-bisimilarity/index.html#observable).

## Free-channel guard offered without reduction

A selected free-channel guard exposed without reduction. Restrictions
hide bound subjects but do not hide free constants.

Formalized by `Cslib.PiCalculus.Offer`, an inductive type declared in [CSLibExt/Languages/PiCalculus/Behavioural.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Behavioural.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/strong-free-channel-barbed-bisimilarity/index.html#offer).

## Immediate free-channel barb

Immediate free-channel readiness, up to the existing structural
congruence. A witness performs no `Step`.

Formalized by `Cslib.PiCalculus.Barb`, a definition declared in [CSLibExt/Languages/PiCalculus/Behavioural.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Behavioural.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/strong-free-channel-barbed-bisimilarity/index.html#barb).

## Labels for reductions and barb observations

Labels for reductions and observation-only self-loops.

Formalized by `Cslib.PiCalculus.BehaviourLabel`, an inductive type declared in [CSLibExt/Languages/PiCalculus/Behavioural.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Behavioural.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/strong-free-channel-barbed-bisimilarity/index.html#behaviour-label).

## Reduction LTS decorated with barb observations

The existing reduction semantics decorated with barb tests. The
observation transitions do not consume a prefix or transmit a name.

Formalized by `Cslib.PiCalculus.observedLTS`, a definition declared in [CSLibExt/Languages/PiCalculus/Behavioural.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Behavioural.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/strong-free-channel-barbed-bisimilarity/index.html#observed-lts).

## Strong barbed bisimilarity

Strong barbed bisimilarity, using the canonical CSLib bisimulation API.
No context closure is built into this relation.

Formalized by `Cslib.PiCalculus.BarbedBisimilar`, a definition declared in [CSLibExt/Languages/PiCalculus/Behavioural.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Behavioural.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/strong-free-channel-barbed-bisimilarity/index.html#barbed-bisimilar).

## Decorated-LTS bisimulations are exactly strong barbed bisimulations

The decorated LTS has precisely the strong reduction-matching and
immediate-barb-preservation clauses of a strong barbed bisimulation.

Formalized by `Cslib.PiCalculus.isBisimulation_observedLTS_iff`, a theorem declared in [CSLibExt/Languages/PiCalculus/Behavioural.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Behavioural.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/strong-free-channel-barbed-bisimilarity/index.html#is-bisimulation-observed-lts-iff).

## Structural congruence preserves immediate barbs

Structural congruence preserves immediate barbs.

Formalized by `Cslib.PiCalculus.Cong.barb_iff`, a theorem declared in [CSLibExt/Languages/PiCalculus/Behavioural.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Behavioural.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/strong-free-channel-barbed-bisimilarity/index.html#barb-iff).

## Structural congruence is a strong barbed bisimulation

Structural congruence is a strong barbed bisimulation: reductions
match one for one, while free-channel observations match immediately.

Formalized by `Cslib.PiCalculus.cong_isBarbedBisimulation`, a theorem declared in [CSLibExt/Languages/PiCalculus/Behavioural.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Behavioural.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/strong-free-channel-barbed-bisimilarity/index.html#cong-is-barbed-bisimulation).

## Structurally congruent processes are barbed bisimilar

Every structural law of `Basic` is sound for strong barbed
bisimilarity, including scope extrusion and replication unfolding.

Formalized by `Cslib.PiCalculus.Cong.barbedBisimilar`, a theorem declared in [CSLibExt/Languages/PiCalculus/Behavioural.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Behavioural.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/strong-free-channel-barbed-bisimilarity/index.html#barbed-bisimilar-2).

## Unguarded output in a process

An output not behind a prefix, on any subject (including bound names).
This is an overapproximation for arbitrary unguarded sums, not a barb.

Formalized by `Cslib.PiCalculus.HasUnguardedOutput`, a definition declared in [CSLibExt/Languages/PiCalculus/Behavioural.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Behavioural.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/strong-free-channel-barbed-bisimilarity/index.html#has-unguarded-output).

## Structural congruence preserves unguarded outputs

Structural rearrangement cannot expose an output from an input-guarded
process. This includes arbitrary uses of replication and scope laws.

Formalized by `Cslib.PiCalculus.Cong.hasUnguardedOutput_iff`, a theorem declared in [CSLibExt/Languages/PiCalculus/Behavioural.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Behavioural.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/strong-free-channel-barbed-bisimilarity/index.html#has-unguarded-output-iff).

## Every reduction source has an unguarded output

Every reduction needs an unguarded output in its source, even when
communication is private or structural congruence is used arbitrarily.

Formalized by `Cslib.PiCalculus.Step.hasUnguardedOutput`, a theorem declared in [CSLibExt/Languages/PiCalculus/Behavioural.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Behavioural.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/strong-free-channel-barbed-bisimilarity/index.html#has-unguarded-output-2).

## Processes without unguarded output cannot reduce

Outputless processes cannot reduce. Input guards may still have
observable input barbs; this theorem does not identify them with `nil`.

Formalized by `Cslib.PiCalculus.not_step_of_no_output`, a theorem declared in [CSLibExt/Languages/PiCalculus/Behavioural.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Behavioural.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/strong-free-channel-barbed-bisimilarity/index.html#not-step-of-no-output).

## Exposed guards are barbs

A directly exposed guard is a barb, with the reflexive structural
representative as witness.

Formalized by `Cslib.PiCalculus.Barb.of_offer`, a theorem declared in [CSLibExt/Languages/PiCalculus/Behavioural.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Behavioural.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/strong-free-channel-barbed-bisimilarity/index.html#of-offer).

## The inactive process has no barbs

The inactive process has no barb, even after structural rearrangement.

Formalized by `Cslib.PiCalculus.barb_nil`, a theorem declared in [CSLibExt/Languages/PiCalculus/Behavioural.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Behavioural.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/strong-free-channel-barbed-bisimilarity/index.html#barb-nil).

## Barbs of an output prefix

Output readiness sees only its free subject and direction, not its
object or guarded continuation.

Formalized by `Cslib.PiCalculus.barb_out_iff`, a theorem declared in [CSLibExt/Languages/PiCalculus/Behavioural.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Behavioural.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/strong-free-channel-barbed-bisimilarity/index.html#barb-out-iff).

## Barbs of an input prefix

Waiting inputs are observable, despite being unable to reduce alone.

Formalized by `Cslib.PiCalculus.barb_inp_iff`, a theorem declared in [CSLibExt/Languages/PiCalculus/Behavioural.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Behavioural.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/strong-free-channel-barbed-bisimilarity/index.html#barb-inp-iff).

## Barbs of a restricted output prefix

A restricted output is visible exactly when its subject is free.
Sending the private name on a free subject remains observable.

Formalized by `Cslib.PiCalculus.barb_nu_out_iff`, a theorem declared in [CSLibExt/Languages/PiCalculus/Behavioural.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Behavioural.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/strong-free-channel-barbed-bisimilarity/index.html#barb-nu-out-iff).

## Barbed bisimilar processes have the same barbs

Bisimilar processes have the same immediate free-channel barbs.

Formalized by `Cslib.PiCalculus.BarbedBisimilar.barb_iff`, a theorem declared in [CSLibExt/Languages/PiCalculus/Behavioural.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Behavioural.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/strong-free-channel-barbed-bisimilarity/index.html#barb-iff-2).

## Barbed bisimilarity matches each reduction by one reduction

A reduction from the first process is matched by one reduction,
with strong barbed bisimilar derivatives.

Formalized by `Cslib.PiCalculus.BarbedBisimilar.step`, a theorem declared in [CSLibExt/Languages/PiCalculus/Behavioural.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Behavioural.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/strong-free-channel-barbed-bisimilarity/index.html#step).

## Free-channel input is not barbed bisimilar to nil

Waiting for input is not equivalent to doing nothing. Reduction-only
bisimilarity would miss this distinction.

Formalized by `Cslib.PiCalculus.input_not_barbedBisimilar_nil`, a theorem declared in [CSLibExt/Languages/PiCalculus/Behavioural.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Behavioural.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/strong-free-channel-barbed-bisimilarity/index.html#input-not-barbed-bisimilar-nil).

## May-barb after finitely many reductions

A free-channel barb reachable by finitely many existing reductions,
possibly zero. This is a may observation, not a weak equivalence.

Formalized by `Cslib.PiCalculus.MayBarb`, a definition declared in [CSLibExt/Languages/PiCalculus/Behavioural.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Behavioural.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/strong-free-channel-barbed-bisimilarity/index.html#may-barb).

## Barbed bisimilarity transfers finite reduction paths

A finite reduction path transfers across strong barbed bisimilarity.

Formalized by `Cslib.PiCalculus.BarbedBisimilar.reductionPath`, a theorem declared in [CSLibExt/Languages/PiCalculus/Behavioural.lean, line 307](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Behavioural.lean#L307). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/strong-free-channel-barbed-bisimilarity/index.html#reduction-path).

## Barbed bisimilarity preserves may-barbs

Strong barbed bisimilarity preserves finite may observations.

Formalized by `Cslib.PiCalculus.BarbedBisimilar.mayBarb_iff`, a theorem declared in [CSLibExt/Languages/PiCalculus/Behavioural.lean, line 318](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/PiCalculus/Behavioural.lean#L318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/strong-free-channel-barbed-bisimilarity/index.html#may-barb-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Strong free-channel barbed bisimilarity](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus/strong-free-channel-barbed-bisimilarity/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/process-calculi/calculus/strong-free-channel-barbed-bisimilarity)
