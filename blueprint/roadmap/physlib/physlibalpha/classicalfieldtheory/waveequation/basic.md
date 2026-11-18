---
declaration: module
origin: cited
lean: WaveEquation.smoothWaveOperator, WaveEquation.smoothWaveOperator_coe, WaveEquation.smoothWaveOperator_support, WaveEquation.smoothFiberMap_waveOperator, WaveEquation.distributionWaveOperator, WaveEquation.testWaveOperator, WaveEquation.distributionWaveOperator_apply
statement: formalized
proof: formalized
---

# The wave operator

The module `PhyslibAlpha.ClassicalFieldTheory.WaveEquation.Basic`, [PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Basic.lean): 7 declarations, 6 with a docstring.

## i. Overview

> The wave operator on smooth fields and on distributions on spacetime.

## ii. Key results

> - `smoothWaveOperator` : The smooth wave operator as the Minkowski metric trace of the second
>   derivative.
> - `distributionWaveOperator` : The wave operator on all distributions is the metric trace of weak
>   second derivatives.
> - `testWaveOperator` : The transpose wave operator on native smooth compact test functions.
> - `smoothFiberMap_waveOperator` : Constant fibre transformations commute with the metric-trace wave
>   operator.

## iv. References

> None.

## A. The Minkowski wave equation

> - `smoothWaveOperator` : The smooth wave operator as the Minkowski metric trace of the second
>   derivative.
>
> Lemmas: `smoothWaveOperator_coe`, `smoothWaveOperator_support`, `smoothFiberMap_waveOperator`.

## B. The distributional wave operator

> - `distributionWaveOperator` : The wave operator on all distributions is the metric trace of weak
>   second derivatives.
> - `testWaveOperator` : The transpose wave operator on native smooth compact test functions.
>
> Lemmas: `distributionWaveOperator_apply`.

**`WaveEquation.smoothWaveOperator`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Basic.lean#L66).

> The smooth wave operator as the Minkowski metric trace of the second derivative.

```lean
def smoothWaveOperator : smoothFields d V →ₗ[ℝ] smoothFields d V
```

**`WaveEquation.smoothWaveOperator_coe`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Basic.lean#L69).

```lean
lemma smoothWaveOperator_coe (u : smoothFields d V) :
    (smoothWaveOperator u : SpaceTime d → V) =
      ∑ μ : Fin 1 ⊕ Fin d, (η μ μ : ℝ) •
        (SpaceTime.deriv μ (SpaceTime.deriv μ u.val))
```

**`WaveEquation.smoothWaveOperator_support`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Basic.lean#L77).

> Taking the metric trace does not enlarge field support.

```lean
lemma smoothWaveOperator_support (u : smoothFields d V) :
    tsupport (smoothWaveOperator u : SpaceTime d → V) ⊆ tsupport (u : SpaceTime d → V)
```

**`WaveEquation.smoothFiberMap_waveOperator`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Basic.lean#L86).

> Constant fibre transformations commute with the metric-trace wave operator.

```lean
lemma smoothFiberMap_waveOperator {W : Type} [NormedAddCommGroup W] [NormedSpace ℝ W]
    (L : V →L[ℝ] W) (u : smoothFields d V) :
    smoothWaveOperator (smoothFiberMap L u) = smoothFiberMap L (smoothWaveOperator u)
```

**`WaveEquation.distributionWaveOperator`**, a def, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Basic.lean#L94).

> The wave operator on all distributions is the metric trace of weak second derivatives.

```lean
def distributionWaveOperator : DistributionField d V →L[ℝ] DistributionField d V
```

**`WaveEquation.testWaveOperator`**, a def, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Basic.lean#L100).

> The transpose wave operator on native smooth compact test functions.

```lean
def testWaveOperator :
    _root_.TestFunction (⊤ : TopologicalSpace.Opens (SpaceTime d)) ℝ ⊤ →L[ℝ]
      _root_.TestFunction (⊤ : TopologicalSpace.Opens (SpaceTime d)) ℝ ⊤
```

**`WaveEquation.distributionWaveOperator_apply`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Basic.lean#L108).

> Two weak derivatives give the positive transpose wave operator on tests.

```lean
lemma distributionWaveOperator_apply (T : DistributionField d V)
    (φ : _root_.TestFunction (⊤ : TopologicalSpace.Opens (SpaceTime d)) ℝ ⊤) :
    distributionWaveOperator T φ = T (testWaveOperator φ)
```

## Depends on

- [Smooth fields and distributions on spacetime](../../spaceandtime/spacetime/fields.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Basic.lean)
