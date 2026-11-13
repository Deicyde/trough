---
declaration: section
origin: cited
lean: MathlibExt.Probability.MarkovSemigroupProjective.finiteChainKernel, MathlibExt.Probability.MarkovSemigroupProjective.finiteChainLaw, MathlibExt.Probability.MarkovSemigroupProjective.finiteChainKernel_comp, MathlibExt.Probability.MarkovSemigroupProjective.eraseCoordinate, MathlibExt.Probability.MarkovSemigroupProjective.finiteChainKernel_map_eraseCoordinate_zero, MathlibExt.Probability.MarkovSemigroupProjective.finiteChainKernel_map_eraseCoordinate, MathlibExt.Probability.MarkovSemigroupProjective.finiteChainKernel_map_strictMono, MathlibExt.Probability.MarkovSemigroupProjective.finiteChainLaw_map_strictMono
statement: formalized
proof: formalized
---

# Markov processes from transition semigroups

25 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/markov-processes-from-transition-semigroups/index.html).

## Finite-dimensional kernel of a Markov semigroup at ordered times

The law, as a kernel in its starting point, at finitely many ordered
times.  `s` is the time of the input state and `t` lists the requested
absolute times.

Formalized by `MathlibExt.Probability.MarkovSemigroupProjective.finiteChainKernel`, a definition declared in [MathlibExt/Probability/MarkovSemigroupProjective.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/MarkovSemigroupProjective.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/markov-processes-from-transition-semigroups/index.html#finite-chain-kernel).

## Finite-dimensional law of a Markov semigroup from a starting point

The ordered finite-dimensional law started from `x` at time `s`.

Formalized by `MathlibExt.Probability.MarkovSemigroupProjective.finiteChainLaw`, a definition declared in [MathlibExt/Probability/MarkovSemigroupProjective.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/MarkovSemigroupProjective.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/markov-processes-from-transition-semigroups/index.html#finite-chain-law).

## Composition rule for finite-chain kernels

Moving the starting time forward and then evolving to the first requested
time gives the same finite chain as evolving there directly.

Formalized by `MathlibExt.Probability.MarkovSemigroupProjective.finiteChainKernel_comp`, a theorem declared in [MathlibExt/Probability/MarkovSemigroupProjective.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/MarkovSemigroupProjective.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/markov-processes-from-transition-semigroups/index.html#finite-chain-kernel-comp).

## Removing one coordinate from a finite vector

Remove one coordinate from a finite vector.

Formalized by `MathlibExt.Probability.MarkovSemigroupProjective.eraseCoordinate`, a definition declared in [MathlibExt/Probability/MarkovSemigroupProjective.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/MarkovSemigroupProjective.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/markov-processes-from-transition-semigroups/index.html#erase-coordinate).

## Deleting the first time from a finite Markov chain kernel

Deleting the first requested time composes the initial transition with
the transition to the next requested time.

Formalized by `MathlibExt.Probability.MarkovSemigroupProjective.finiteChainKernel_map_eraseCoordinate_zero`, a theorem declared in [MathlibExt/Probability/MarkovSemigroupProjective.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/MarkovSemigroupProjective.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/markov-processes-from-transition-semigroups/index.html#finite-chain-kernel-map-erase-coordinate).

## Deleting one time from a finite Markov chain kernel

Deleting one requested time from an ordered finite Markov chain composes
the two adjacent transition kernels.

Formalized by `MathlibExt.Probability.MarkovSemigroupProjective.finiteChainKernel_map_eraseCoordinate`, a theorem declared in [MathlibExt/Probability/MarkovSemigroupProjective.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/MarkovSemigroupProjective.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/markov-processes-from-transition-semigroups/index.html#finite-chain-kernel-map-erase-coordinate-2).

## Restricting a finite Markov kernel along an increasing reindexing

Restrict an ordered finite Markov law along any strictly increasing map
of coordinate sets.

Formalized by `MathlibExt.Probability.MarkovSemigroupProjective.finiteChainKernel_map_strictMono`, a theorem declared in [MathlibExt/Probability/MarkovSemigroupProjective.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/MarkovSemigroupProjective.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/markov-processes-from-transition-semigroups/index.html#finite-chain-kernel-map-strict-mono).

## Restricting a finite Markov law along an increasing reindexing

Measure form of `finiteChainKernel_map_strictMono`.

Formalized by `MathlibExt.Probability.MarkovSemigroupProjective.finiteChainLaw_map_strictMono`, a theorem declared in [MathlibExt/Probability/MarkovSemigroupProjective.lean, line 324](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/MarkovSemigroupProjective.lean#L324). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/markov-processes-from-transition-semigroups/index.html#finite-chain-law-map-strict-mono).

## Reindexing an ordered vector by a finite set

Reindex an ordered vector by the increasing enumeration of a finset.

Formalized by `MathlibExt.Probability.MarkovSemigroupProjective.orderMeasurableEquiv`, a definition declared in [MathlibExt/Probability/MarkovSemigroupProjective.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/MarkovSemigroupProjective.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/markov-processes-from-transition-semigroups/index.html#order-measurable-equiv).

## Increasing reindexing of a subset within a finite set

The increasing reindexing of the elements of `J` among those of a
larger finset `I`.

Formalized by `MathlibExt.Probability.MarkovSemigroupProjective.orderRestriction`, a definition declared in [MathlibExt/Probability/MarkovSemigroupProjective.lean, line 352](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/MarkovSemigroupProjective.lean#L352). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/markov-processes-from-transition-semigroups/index.html#order-restriction).

## Markov law at a finite set of times

The canonical law at an arbitrary finite set of nonnegative times.

The generic construction does not assume `K 0 = Kernel.id`.  Consequently,
when zero is requested its marginal is `K 0 x`; callers that need a
deterministic initial value prove the identity law for their kernel.

Formalized by `MathlibExt.Probability.MarkovSemigroupProjective.finiteLaw`, a definition declared in [MathlibExt/Probability/MarkovSemigroupProjective.lean, line 394](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/MarkovSemigroupProjective.lean#L394). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/markov-processes-from-transition-semigroups/index.html#finite-law).

## Finite Markov laws form a projective family

The finite laws obtained by sorting requested times form a projective
family; projectivity is a consequence of Chapman--Kolmogorov, not a premise.

Formalized by `MathlibExt.Probability.MarkovSemigroupProjective.isProjectiveMeasureFamily_finiteLaw`, a theorem declared in [MathlibExt/Probability/MarkovSemigroupProjective.lean, line 407](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/MarkovSemigroupProjective.lean#L407). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/markov-processes-from-transition-semigroups/index.html#is-projective-measure-family-finite-law).

## Kolmogorov extension for Markov semigroup laws

Kolmogorov extension applied to the proved finite Markov laws.

Formalized by `MathlibExt.Probability.MarkovSemigroupProjective.exists_projectiveLimit`, a theorem declared in [MathlibExt/Probability/MarkovSemigroupProjective.lean, line 463](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/MarkovSemigroupProjective.lean#L463). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/markov-processes-from-transition-semigroups/index.html#exists-projective-limit).

## Path-space measure of a Markov semigroup

The canonical path-space measure selected from Kolmogorov extension.

As for `finiteLaw`, no identity-at-zero hypothesis is built into this generic
object: its time-zero marginal is `K 0 x` unless the caller proves
`K 0 = Kernel.id`.

Formalized by `MathlibExt.Probability.MarkovSemigroupProjective.pathMeasure`, a definition declared in [MathlibExt/Probability/MarkovSemigroupProjective.lean, line 478](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/MarkovSemigroupProjective.lean#L478). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/markov-processes-from-transition-semigroups/index.html#path-measure).

## Path measure is the projective limit of the finite Markov laws

The canonical path measure has exactly the constructed finite laws.

Formalized by `MathlibExt.Probability.MarkovSemigroupProjective.isProjectiveLimit_pathMeasure`, a theorem declared in [MathlibExt/Probability/MarkovSemigroupProjective.lean, line 485](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/MarkovSemigroupProjective.lean#L485). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/markov-processes-from-transition-semigroups/index.html#is-projective-limit-path-measure).

## Finite projections of the Markov path measure

Every finite coordinate projection of the canonical path measure is its
explicit iterated-kernel law.

Formalized by `MathlibExt.Probability.MarkovSemigroupProjective.map_restrict_pathMeasure`, a theorem declared in [MathlibExt/Probability/MarkovSemigroupProjective.lean, line 500](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/MarkovSemigroupProjective.lean#L500). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/markov-processes-from-transition-semigroups/index.html#map-restrict-path-measure).

## Ordered finite projections of the Markov path measure

The coordinates in increasing finset order have exactly the corresponding
iterated-kernel law.

Formalized by `MathlibExt.Probability.MarkovSemigroupProjective.map_ordered_pathMeasure`, a theorem declared in [MathlibExt/Probability/MarkovSemigroupProjective.lean, line 509](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/MarkovSemigroupProjective.lean#L509). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/markov-processes-from-transition-semigroups/index.html#map-ordered-path-measure).

## Representation of positive unital operators by Markov kernels

A positive unital linear map from `C(E, ℝ)` to itself is represented by a Markov kernel.
Continuity of the operator is unnecessary: each output already belongs to `C(E, ℝ)`.

Formalized by `MathlibExt.Probability.PositiveOperatorKernel.exists_markovKernelOfPositiveLinearMap`, a theorem declared in [MathlibExt/Probability/PositiveOperatorKernel.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/PositiveOperatorKernel.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/markov-processes-from-transition-semigroups/index.html#exists-markov-kernel-of-positive-linear).

## Positive-operator-to-Markov-kernel bridge

On a compact metrizable Borel space,
a positive continuous linear operator on `C(E, ℝ)` that fixes `1` is represented by a Markov
kernel. The integral identity holds for every continuous function and every starting state.

Formalized by `MathlibExt.Probability.PositiveOperatorKernel.exists_markovKernelOfPositiveOperator`, a theorem declared in [MathlibExt/Probability/PositiveOperatorKernel.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/PositiveOperatorKernel.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/markov-processes-from-transition-semigroups/index.html#exists-markov-kernel-of-positive-operato).

## Markov kernel of a positive unital operator

The canonical chosen Markov kernel representing `T`. Its characterization theorem is
`integral_markovKernelOfPositiveOperator`; clients should use that theorem rather than unfold this
definition.

Formalized by `MathlibExt.Probability.PositiveOperatorKernel.markovKernelOfPositiveOperator`, a definition declared in [MathlibExt/Probability/PositiveOperatorKernel.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/PositiveOperatorKernel.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/markov-processes-from-transition-semigroups/index.html#markov-kernel-of-positive-operator).

## Kernel of a positive operator represents it on continuous functions

The chosen kernel represents `T` on every real-valued continuous function.

Formalized by `MathlibExt.Probability.PositiveOperatorKernel.integral_markovKernelOfPositiveOperator`, a theorem declared in [MathlibExt/Probability/PositiveOperatorKernel.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/PositiveOperatorKernel.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/markov-processes-from-transition-semigroups/index.html#integral-markov-kernel-of-positive-opera).

## Markov kernels are determined by integrals of continuous functions

Two Markov kernels on a compact metrizable Borel space are equal when they integrate every
real-valued continuous function equally at every starting state.

Formalized by `MathlibExt.Probability.PositiveOperatorKernel.kernel_ext_of_forall_integral_continuous_eq`, a theorem declared in [MathlibExt/Probability/PositiveOperatorKernel.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/PositiveOperatorKernel.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/markov-processes-from-transition-semigroups/index.html#kernel-ext-of-forall-integral-continuous).

## Identity operator gives the identity kernel

The kernel represented by the identity operator is Mathlib's identity kernel.

Formalized by `MathlibExt.Probability.PositiveOperatorKernel.markovKernelOfPositiveOperator_id`, a theorem declared in [MathlibExt/Probability/PositiveOperatorKernel.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/PositiveOperatorKernel.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/markov-processes-from-transition-semigroups/index.html#markov-kernel-of-positive-operator-id).

## Identity operator kernel is pointwise Dirac

Pointwise form of the identity theorem: every transition measure is Dirac.

Formalized by `MathlibExt.Probability.PositiveOperatorKernel.markovKernelOfPositiveOperator_id_apply`, a theorem declared in [MathlibExt/Probability/PositiveOperatorKernel.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/PositiveOperatorKernel.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/markov-processes-from-transition-semigroups/index.html#markov-kernel-of-positive-operator-id-ap).

## Operator composition corresponds to kernel composition

Operator composition is represented by canonical kernel composition. The order is reversed:
`T.comp U` acts as `f ↦ T (U f)`, so the represented kernel first uses `K_T` and then `K_U`.

Formalized by `MathlibExt.Probability.PositiveOperatorKernel.markovKernelOfPositiveOperator_comp`, a theorem declared in [MathlibExt/Probability/PositiveOperatorKernel.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/PositiveOperatorKernel.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/markov-processes-from-transition-semigroups/index.html#markov-kernel-of-positive-operator-comp).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Markov processes from transition semigroups](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/markov-processes-from-transition-semigroups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/markov-chains/markov-processes-from-transition-semigroups)
