---
declaration: section
origin: cited
lean: MathlibExt.Probability.BlumenthalZeroOne.germSigmaAlgebraZero, MathlibExt.Probability.BlumenthalZeroOne.IsContinuousIndependentIncrementProcess, MathlibExt.Probability.BlumenthalZeroOne.IsContinuousIndependentIncrementProcess.measurable, MathlibExt.Probability.BlumenthalZeroOne.naturalFiltration, MathlibExt.Probability.BlumenthalZeroOne.naturalGerm, MathlibExt.Probability.BlumenthalZeroOne.measurable_naturalFiltration, MathlibExt.Probability.BlumenthalZeroOne.naturalFiltration_le, MathlibExt.Probability.BlumenthalZeroOne.germ_le_of_pos
statement: formalized
proof: formalized
---

# Blumenthal zero–one law

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/blumenthal-zero-one-law/index.html).

## Germ sigma-algebra at time zero

The *germ σ-algebra at `0`* of a filtration `𝓕` indexed by `NNReal`,
defined as the intersection `⨅_{t > 0} 𝓕_t`. For Brownian motion this is the
`𝓕_0^+` σ-algebra of events observable "immediately after" time `0`. Ported
verbatim from `v1/Atlas/TheoryOfProbability/code/Blumenthal01.lean`.

Formalized by `MathlibExt.Probability.BlumenthalZeroOne.germSigmaAlgebraZero`, a definition declared in [MathlibExt/Probability/BlumenthalZeroOne.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BlumenthalZeroOne.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/blumenthal-zero-one-law/index.html#germ-sigma-algebra-zero).

## Continuous process with independent increments

A continuous process `B : NNReal → Ω → E` with independent increments,
started at `x` and adapted to `𝓕`. The measure is a probability measure,
`B 0 = x` a.e., each increment after `s` is independent of `𝓕 s`, and a.e.
paths are continuous. These are the five meaningful fields of the archived
v1 specification; its tautological pushforward-law field is omitted.
No Gaussian-law or stationary-increment condition is encoded.

Formalized by `MathlibExt.Probability.BlumenthalZeroOne.IsContinuousIndependentIncrementProcess`, a structure declared in [MathlibExt/Probability/BlumenthalZeroOne.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BlumenthalZeroOne.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/blumenthal-zero-one-law/index.html#is-continuous-independent-increment-proc).

## Coordinates of a continuous independent-increment process are measurable

Each coordinate of the adapted continuous process is measurable.

Formalized by `MathlibExt.Probability.BlumenthalZeroOne.IsContinuousIndependentIncrementProcess.measurable`, a theorem declared in [MathlibExt/Probability/BlumenthalZeroOne.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BlumenthalZeroOne.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/blumenthal-zero-one-law/index.html#measurable).

## Natural filtration of a process

The natural filtration of a process: `𝓕^nat_t = σ(B_u : u ≤ t)`. Unlike
Mathlib's `Filtration.natural`, this is built from measurability rather than
strong measurability, which is all that is available from adaptedness.

Formalized by `MathlibExt.Probability.BlumenthalZeroOne.naturalFiltration`, a definition declared in [MathlibExt/Probability/BlumenthalZeroOne.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BlumenthalZeroOne.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/blumenthal-zero-one-law/index.html#natural-filtration).

## Germ sigma-algebra of the natural filtration

The germ σ-algebra of the natural filtration of `B`.

Formalized by `MathlibExt.Probability.BlumenthalZeroOne.naturalGerm`, a definition declared in [MathlibExt/Probability/BlumenthalZeroOne.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BlumenthalZeroOne.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/blumenthal-zero-one-law/index.html#natural-germ).

## Process is measurable for its natural filtration at later times

Each `B u` is measurable with respect to the natural filtration at any
later time `t`.

Formalized by `MathlibExt.Probability.BlumenthalZeroOne.measurable_naturalFiltration`, a theorem declared in [MathlibExt/Probability/BlumenthalZeroOne.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BlumenthalZeroOne.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/blumenthal-zero-one-law/index.html#measurable-natural-filtration).

## Natural filtration is the smallest adapted filtration

The natural filtration is contained in any filtration to which `B` is
adapted.

Formalized by `MathlibExt.Probability.BlumenthalZeroOne.naturalFiltration_le`, a theorem declared in [MathlibExt/Probability/BlumenthalZeroOne.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BlumenthalZeroOne.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/blumenthal-zero-one-law/index.html#natural-filtration-le).

## Germ sigma-algebra lies in every positive-time level

The germ σ-algebra is contained in every positive-time component of the
filtration.

Formalized by `MathlibExt.Probability.BlumenthalZeroOne.germ_le_of_pos`, a theorem declared in [MathlibExt/Probability/BlumenthalZeroOne.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BlumenthalZeroOne.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/blumenthal-zero-one-law/index.html#germ-le-of-pos).

## Blumenthal zero-one law

Every event in the natural germ of a continuous process with independent
increments and a deterministic a.e. initial value has probability `0` or `1`.
This general form includes the classical Brownian natural-filtration law.

Formalized by `MathlibExt.Probability.BlumenthalZeroOne.zero_one_naturalGerm`, a theorem declared in [MathlibExt/Probability/BlumenthalZeroOne.lean, line 1014](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BlumenthalZeroOne.lean#L1014). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/blumenthal-zero-one-law/index.html#zero-one-natural-germ).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Blumenthal zero–one law](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/blumenthal-zero-one-law/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/stochastic-calculus/blumenthal-zero-one-law)
