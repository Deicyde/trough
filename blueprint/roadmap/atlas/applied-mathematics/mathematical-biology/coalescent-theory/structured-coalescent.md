---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.StructuredCoalescent.PairState, MathlibExt.Biology.PopulationGenetics.StructuredCoalescent.PairState.sum_eq, MathlibExt.Biology.PopulationGenetics.StructuredCoalescent.rate, MathlibExt.Biology.PopulationGenetics.StructuredCoalescent.exitRate, MathlibExt.Biology.PopulationGenetics.StructuredCoalescent.FirstStepEquations, MathlibExt.Biology.PopulationGenetics.StructuredCoalescent.withinTime, MathlibExt.Biology.PopulationGenetics.StructuredCoalescent.betweenTime, MathlibExt.Biology.PopulationGenetics.StructuredCoalescent.meanCoalescenceTime
statement: formalized
proof: formalized
---

# Structured coalescent

17 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/structured-coalescent/index.html).

## Structured Coalescent

## State of two lineages in the island model

The state of two ancestral lineages in the island model: in the same deme, in different
demes, or coalesced (absorbing).

Formalized by `MathlibExt.Biology.PopulationGenetics.StructuredCoalescent.PairState`, an inductive type declared in [MathlibExt/Biology/PopulationGenetics/StructuredCoalescent.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/StructuredCoalescent.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/structured-coalescent/index.html#pair-state).

## Sum over the island-model pair states

A sum over the three states.

Formalized by `MathlibExt.Biology.PopulationGenetics.StructuredCoalescent.PairState.sum_eq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/StructuredCoalescent.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/StructuredCoalescent.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/structured-coalescent/index.html#sum-eq).

## Transition rates of the two-lineage structured coalescent

The transition rates `q(s, t)` (`s ≠ t`) of the two-lineage structured coalescent in the
finite island model with `d` demes and `M = 4Nm`, time in units of `2N` generations: same deme →
coalesced at rate `1`, same deme → different demes at rate `M`, different demes → same deme at
rate `M / (d - 1)`; all other rates (and the diagonal) are `0`. Meaningful for `d ≥ 2` and
`M ≥ 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.StructuredCoalescent.rate`, a definition declared in [MathlibExt/Biology/PopulationGenetics/StructuredCoalescent.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/StructuredCoalescent.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/structured-coalescent/index.html#rate).

## Exit rate of a structured-coalescent state

The total rate `qₛ = ∑ₜ q(s, t)` of leaving the state `s`.

Formalized by `MathlibExt.Biology.PopulationGenetics.StructuredCoalescent.exitRate`, a definition declared in [MathlibExt/Biology/PopulationGenetics/StructuredCoalescent.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/StructuredCoalescent.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/structured-coalescent/index.html#exit-rate).

## First-step equations for mean coalescence time

The first-step (backward Kolmogorov) equations for the mean time to coalescence:
`h coalesced = 0`, and at each transient state `s`, `∑ₜ q(s, t) (h t - h s) = -1`. (The vector
of mean absorption times of a finite absorbing continuous-time Markov chain satisfies these
equations; this file does not construct the chain.)

Formalized by `MathlibExt.Biology.PopulationGenetics.StructuredCoalescent.FirstStepEquations`, a definition declared in [MathlibExt/Biology/PopulationGenetics/StructuredCoalescent.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/StructuredCoalescent.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/structured-coalescent/index.html#first-step-equations).

## Mean coalescence time within a deme

The mean coalescence time `T₀ = d` of two lineages in the same deme (units of `2N`
generations).

Formalized by `MathlibExt.Biology.PopulationGenetics.StructuredCoalescent.withinTime`, a definition declared in [MathlibExt/Biology/PopulationGenetics/StructuredCoalescent.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/StructuredCoalescent.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/structured-coalescent/index.html#within-time).

## Mean coalescence time between demes

The mean coalescence time `T₁ = d + (d - 1) / M` of two lineages in different demes (units of
`2N` generations). Meaningful for `M > 0`; `betweenTime d 0 = d` is a junk value (the true mean
is infinite).

Formalized by `MathlibExt.Biology.PopulationGenetics.StructuredCoalescent.betweenTime`, a definition declared in [MathlibExt/Biology/PopulationGenetics/StructuredCoalescent.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/StructuredCoalescent.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/structured-coalescent/index.html#between-time).

## Closed-form mean coalescence times in the island model

The closed-form mean time to coalescence from each state: `T₀`, `T₁`, and `0` once
coalesced. `firstStepEquations_iff` shows it is the unique solution of the first-step
equations.

Formalized by `MathlibExt.Biology.PopulationGenetics.StructuredCoalescent.meanCoalescenceTime`, a definition declared in [MathlibExt/Biology/PopulationGenetics/StructuredCoalescent.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/StructuredCoalescent.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/structured-coalescent/index.html#mean-coalescence-time).

## Mean coalescence times in the finite island model (Strobeck 1987; Slatkin 1991)

For
`d ≥ 2` demes and `M = 4Nm > 0`, the first-step equations have the unique solution
`T₀ = d`, `T₁ = d + (d - 1) / M`. In particular `T₀` does not depend on the migration rate.

Formalized by `MathlibExt.Biology.PopulationGenetics.StructuredCoalescent.firstStepEquations_iff`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/StructuredCoalescent.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/StructuredCoalescent.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/structured-coalescent/index.html#first-step-equations-iff).

## First-step analysis in jump-chain form

At each transient state `s` the exit rate is
positive and the mean coalescence time is the mean holding time `1 / qₛ` plus the mean time from
the next state, `h s = 1 / qₛ + ∑ₜ (q(s, t) / qₛ) h t`.

Formalized by `MathlibExt.Biology.PopulationGenetics.StructuredCoalescent.meanCoalescenceTime_eq_firstStep`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/StructuredCoalescent.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/StructuredCoalescent.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/structured-coalescent/index.html#mean-coalescence-time-eq-first-step).

## Slatkin's mean total coalescence time

Slatkin's mean coalescence time `T̄ = T₀ / d + (d - 1) T₁ / d` of two genes drawn from two
demes chosen independently and uniformly at random.

Formalized by `MathlibExt.Biology.PopulationGenetics.StructuredCoalescent.totalTime`, a definition declared in [MathlibExt/Biology/PopulationGenetics/StructuredCoalescent.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/StructuredCoalescent.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/structured-coalescent/index.html#total-time).

## Slatkin's F_ST for the finite island model

Slatkin's (1991) `F_ST = (T̄ - T₀) / T̄` for the finite island model.

Formalized by `MathlibExt.Biology.PopulationGenetics.StructuredCoalescent.slatkinFST`, a definition declared in [MathlibExt/Biology/PopulationGenetics/StructuredCoalescent.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/StructuredCoalescent.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/structured-coalescent/index.html#slatkin-fst).

## Closed form of Slatkin's mean total coalescence time

`T̄ = d + (d - 1)² / (d M)` for `d ≥ 1`.

Formalized by `MathlibExt.Biology.PopulationGenetics.StructuredCoalescent.totalTime_eq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/StructuredCoalescent.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/StructuredCoalescent.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/structured-coalescent/index.html#total-time-eq).

## Positivity of Slatkin's mean total coalescence time

The denominator of Slatkin's `F_ST` is positive: `0 < T̄` for `d ≥ 1` and `M > 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.StructuredCoalescent.totalTime_pos`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/StructuredCoalescent.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/StructuredCoalescent.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/structured-coalescent/index.html#total-time-pos).

## Slatkin's `F_ST` for the finite island model (Slatkin 1991)

For `d ≥ 2` demes and
`M = 4Nm > 0`, `F_ST = 1 / (1 + M d² / (d - 1)²)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.StructuredCoalescent.slatkinFST_eq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/StructuredCoalescent.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/StructuredCoalescent.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/structured-coalescent/index.html#slatkin-fst-eq).

## Slatkin's F_ST lies strictly between 0 and 1

Slatkin's `F_ST` lies in `(0, 1)` for `d ≥ 2` and `M > 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.StructuredCoalescent.slatkinFST_mem_Ioo`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/StructuredCoalescent.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/StructuredCoalescent.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/structured-coalescent/index.html#slatkin-fst-mem-ioo).

## Many demes (Slatkin 1991)

As the number of demes grows, Slatkin's `F_ST` tends to
Wright's `1 / (1 + M) = 1 / (1 + 4Nm)` for every `M > 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.StructuredCoalescent.tendsto_slatkinFST`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/StructuredCoalescent.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/StructuredCoalescent.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/structured-coalescent/index.html#tendsto-slatkin-fst).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Structured coalescent](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/structured-coalescent/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/coalescent-theory/structured-coalescent)
