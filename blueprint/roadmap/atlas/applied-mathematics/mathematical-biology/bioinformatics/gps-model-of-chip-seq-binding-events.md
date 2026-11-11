---
declaration: section
origin: cited
lean: Cslib.Bioinformatics.Regulatory.GPS.survivorWeight, Cslib.Bioinformatics.Regulatory.GPS.mStep, Cslib.Bioinformatics.Regulatory.GPS.penalizedQ, Cslib.Bioinformatics.Regulatory.GPS.truncatedQ, Cslib.Bioinformatics.Regulatory.GPS.survivorWeight_nonneg, Cslib.Bioinformatics.Regulatory.GPS.sum_survivorWeight_pos, Cslib.Bioinformatics.Regulatory.GPS.mStep_nonneg, Cslib.Bioinformatics.Regulatory.GPS.sum_mStep
statement: formalized
proof: formalized
---

# GPS model of ChIP-seq binding events

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/gps-model-of-chip-seq-binding-events/index.html).

## Surviving weight of a GPS event

The surviving weight `max (N j - α) 0` of event `j`, for expected read counts `N` and
sparseness parameter `α`.

Formalized by `Cslib.Bioinformatics.Regulatory.GPS.survivorWeight`, a definition declared in [CSLibExt/Bioinformatics/Regulatory/GPSMStep.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Regulatory/GPSMStep.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/gps-model-of-chip-seq-binding-events/index.html#survivor-weight).

## The GPS M-step with component elimination

`π j = max (N j - α) 0 / ∑ k, max (N k - α) 0`.

Formalized by `Cslib.Bioinformatics.Regulatory.GPS.mStep`, a definition declared in [CSLibExt/Bioinformatics/Regulatory/GPSMStep.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Regulatory/GPSMStep.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/gps-model-of-chip-seq-binding-events/index.html#m-step).

## Expected penalized complete-data log-likelihood of GPS

The expected complete-data log penalized likelihood of GPS, up to an additive constant:
`∑ j, (N j - α) log (π j)` (the expected log-likelihood `∑ j, N j log (π j)` plus the log of the
negative Dirichlet prior). Meaningful for positive `π`.

Formalized by `Cslib.Bioinformatics.Regulatory.GPS.penalizedQ`, a definition declared in [CSLibExt/Bioinformatics/Regulatory/GPSMStep.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Regulatory/GPSMStep.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/gps-model-of-chip-seq-binding-events/index.html#penalized-q).

## Truncated GPS objective

The truncated objective `∑ j, max (N j - α) 0 * log (π j)`.

Formalized by `Cslib.Bioinformatics.Regulatory.GPS.truncatedQ`, a definition declared in [CSLibExt/Bioinformatics/Regulatory/GPSMStep.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Regulatory/GPSMStep.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/gps-model-of-chip-seq-binding-events/index.html#truncated-q).

## Nonnegativity of surviving weights

Surviving weights are nonnegative.

Formalized by `Cslib.Bioinformatics.Regulatory.GPS.survivorWeight_nonneg`, a theorem declared in [CSLibExt/Bioinformatics/Regulatory/GPSMStep.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Regulatory/GPSMStep.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/gps-model-of-chip-seq-binding-events/index.html#survivor-weight-nonneg).

## Total surviving weight is positive iff some event survives

The total surviving weight is positive iff some event has `α < N j`.

Formalized by `Cslib.Bioinformatics.Regulatory.GPS.sum_survivorWeight_pos`, a theorem declared in [CSLibExt/Bioinformatics/Regulatory/GPSMStep.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Regulatory/GPSMStep.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/gps-model-of-chip-seq-binding-events/index.html#sum-survivor-weight-pos).

## Nonnegativity of the GPS M-step update

The update is nonnegative.

Formalized by `Cslib.Bioinformatics.Regulatory.GPS.mStep_nonneg`, a theorem declared in [CSLibExt/Bioinformatics/Regulatory/GPSMStep.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Regulatory/GPSMStep.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/gps-model-of-chip-seq-binding-events/index.html#m-step-nonneg).

## GPS M-step update sums to one when some event survives

The update sums to one when some event survives.

Formalized by `Cslib.Bioinformatics.Regulatory.GPS.sum_mStep`, a theorem declared in [CSLibExt/Bioinformatics/Regulatory/GPSMStep.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Regulatory/GPSMStep.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/gps-model-of-chip-seq-binding-events/index.html#sum-m-step).

## Elimination

When some event survives, event `j` gets probability zero iff
`N j ≤ α`.

Formalized by `Cslib.Bioinformatics.Regulatory.GPS.mStep_eq_zero_iff`, a theorem declared in [CSLibExt/Bioinformatics/Regulatory/GPSMStep.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Regulatory/GPSMStep.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/gps-model-of-chip-seq-binding-events/index.html#m-step-eq-zero-iff).

## GPS M-step keeps positive probability exactly on surviving events

When some event survives, event `j` keeps positive probability iff `α < N j`.

Formalized by `Cslib.Bioinformatics.Regulatory.GPS.mStep_pos_iff`, a theorem declared in [CSLibExt/Bioinformatics/Regulatory/GPSMStep.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Regulatory/GPSMStep.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/gps-model-of-chip-seq-binding-events/index.html#m-step-pos-iff).

## GPS M-step at zero sparseness is the ordinary mixture M-step

With `α = 0` and nonnegative counts the update is the ordinary mixture M-step
`N j / ∑ N`.

Formalized by `Cslib.Bioinformatics.Regulatory.GPS.mStep_zero`, a theorem declared in [CSLibExt/Bioinformatics/Regulatory/GPSMStep.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Regulatory/GPSMStep.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/gps-model-of-chip-seq-binding-events/index.html#m-step-zero).

## The update is an upper bound for the truncated objective

**The update is an upper bound for the truncated objective** over the positive
probability vectors (derived characterization of the elimination rule). Upper-bound
statement only: this does not prove the value at `mStep` is the supremum (no
approximation or `sSup` theorem is given). When elimination occurs `mStep` itself is not
a positive vector (eliminated coordinates are zero), so it is the boundary point on the
face where eliminated coordinates vanish, not a maximizer inside the positive simplex.

Formalized by `Cslib.Bioinformatics.Regulatory.GPS.truncatedQ_le_mStep`, a theorem declared in [CSLibExt/Bioinformatics/Regulatory/GPSMStep.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Regulatory/GPSMStep.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/gps-model-of-chip-seq-binding-events/index.html#truncated-q-le-m-step).

## Truncated and penalized objectives agree when every event survives

When every event survives, the penalized and truncated objectives agree.

Formalized by `Cslib.Bioinformatics.Regulatory.GPS.truncatedQ_eq_penalizedQ`, a theorem declared in [CSLibExt/Bioinformatics/Regulatory/GPSMStep.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Regulatory/GPSMStep.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/gps-model-of-chip-seq-binding-events/index.html#truncated-q-eq-penalized-q).

## GPS M-step formula when every event survives

When every event survives, the update is `(N j - α) / ∑ k, (N k - α)`.

Formalized by `Cslib.Bioinformatics.Regulatory.GPS.mStep_of_forall_lt`, a theorem declared in [CSLibExt/Bioinformatics/Regulatory/GPSMStep.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Regulatory/GPSMStep.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/gps-model-of-chip-seq-binding-events/index.html#m-step-of-forall-lt).

## The M-step of the restructured model

When every remaining event survives
(`α < N j` for all `j`), the update maximizes the GPS expected complete-data log penalized
likelihood over the positive probability vectors.

Formalized by `Cslib.Bioinformatics.Regulatory.GPS.penalizedQ_le_mStep`, a theorem declared in [CSLibExt/Bioinformatics/Regulatory/GPSMStep.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Regulatory/GPSMStep.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/gps-model-of-chip-seq-binding-events/index.html#penalized-q-le-m-step).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: GPS model of ChIP-seq binding events](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/gps-model-of-chip-seq-binding-events/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/bioinformatics/gps-model-of-chip-seq-binding-events)
