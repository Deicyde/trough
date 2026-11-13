---
declaration: module
origin: cited
lean: ProbabilisticTheory.UnitalPositiveLinearMap.IsMeasureAndPrepare
statement: formalized
proof: formalized
---

# Measure-and-prepare channels

The module `PhyslibAlpha.ProbabilisticTheory.Channel.MeasureAndPrepare`, [PhyslibAlpha/ProbabilisticTheory/Channel/MeasureAndPrepare.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/MeasureAndPrepare.lean): 1 declaration, 1 with a docstring.

> Measure-and-prepare channels: channels that factor through a finite classical system.

## i. Overview

> A channel `Channel E₂ E₁` (the Heisenberg picture of a Schrödinger channel `E₁ → E₂`) is
> measure-and-prepare when it factors through a finite classical system: measure the input, then
> prepare a (possibly different) output state for each outcome. Dually, this is exactly
> `Φ = M.comp P` for a measurement `M : Channel (ι → ℝ) E₁` and
> a "preparation" `P : Channel E₂ (FiniteClassicalSystem ι)` — itself a channel into the classical
> system, so a family of states on `E₂` indexed by `ι`, bundled the same way `Measurement` bundles a
> family of effects.
>
> This is the abstract, order-unit-level version of an entanglement-breaking channel. Quantifying
> over the finite outcome type avoids hard-coding a particular classical system.

## ii. Key results

> - `UnitalPositiveLinearMap.IsMeasureAndPrepare` : the channel factors through a finite classical
>   system.

## iv. References

> * None.

## A. Factorization through a finite classical system

**`ProbabilisticTheory.UnitalPositiveLinearMap.IsMeasureAndPrepare`**, a def, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/MeasureAndPrepare.lean#L57).

> A channel is measure-and-prepare when it factors through a finite classical system: measure,
> then prepare a state for each outcome. This is the general-probabilistic-theory abstraction of an
> entanglement-breaking channel.

```lean
def IsMeasureAndPrepare (Φ : Channel E₂ E₁) : Prop
```

## Depends on

- [Finite classical systems](../classical/finitesystem.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Channel/MeasureAndPrepare.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/MeasureAndPrepare.lean)
