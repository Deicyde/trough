---
declaration: module
origin: cited
lean: QuantumMechanics.HarmonicOscillator.toLadderSystem, QuantumMechanics.HarmonicOscillator.toLadderSystem_N_toLinearMap
statement: formalized
proof: formalized
---

# The harmonic oscillator as a ladder system

The module `PhyslibAlpha.QuantumMechanics.HarmonicOscillator.LadderSystem`, [PhyslibAlpha/QuantumMechanics/HarmonicOscillator/LadderSystem.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HarmonicOscillator/LadderSystem.lean): 2 declarations, 1 with a docstring.

> The ladder operators of the d-dimensional harmonic oscillator form a `LadderSystem`.

## i. Overview

> The lowering and raising operators `loweringCLM`/`raisingCLM` of the `d`-dimensional quantum
> harmonic oscillator satisfy the canonical commutation relations, so they form a
> `LadderSystem` on Schwartz space. The number operator of that ladder system is `numberCLM`.

## ii. Key results

> - `toLadderSystem` : the lowering and raising operators bundled as a `LadderSystem`.
> - `toLadderSystem_N_toLinearMap` : the number operators of `toLadderSystem` are `numberCLM`.

## iv. References

> * None.

## A. The ladder system

**`QuantumMechanics.HarmonicOscillator.toLadderSystem`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HarmonicOscillator/LadderSystem.lean#L54).

> The lowering and raising operators on Schwartz space, bundled as a `LadderSystem`.

```lean
def toLadderSystem (Q : HarmonicOscillator d) : LadderSystem ℂ (𝓢(Space d, ℂ)) d
```

**`QuantumMechanics.HarmonicOscillator.toLadderSystem_N_toLinearMap`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HarmonicOscillator/LadderSystem.lean#L78).

```lean
lemma toLadderSystem_N_toLinearMap (Q : HarmonicOscillator d) (i : Fin d) :
    Q.toLadderSystem.N i = (Q.numberCLM i).toLinearMap
```

## Depends on

- [Number operators](../../../physlib/quantummechanics/harmonicoscillator/numberoperator.md)
- [Ladder systems](../../mathematics/part-02/laddersystem/basic.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/HarmonicOscillator/LadderSystem.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HarmonicOscillator/LadderSystem.lean)
