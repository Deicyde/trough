---
declaration: module
origin: cited
lean: KleinGordon.Spacetime.operator, KleinGordon.Spacetime.equation, KleinGordon.Spacetime.distributionOperator, KleinGordon.Spacetime.testOperator, KleinGordon.Spacetime.distributionOperator_apply
statement: formalized
proof: formalized
---

# The Klein–Gordon equation

The module `PhyslibAlpha.ClassicalFieldTheory.KleinGordon.Basic`, [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Basic.lean): 5 declarations, 5 with a docstring.

> This file sets up the Klein–Gordon equation on spacetime for smooth fields and for distributions.

## i. Overview

> Spacetime is `SpaceTime d` with the speed of light equal to one. The operator `operator m` is the
> wave operator plus `m ^ 2` on smooth fields. The mass parameter `m` is any real number. The
> operator does not enlarge support, so `equation m` packages it as a local operator. The operator
> extends to distributions as `distributionOperator m`. The file `Solution` states the solution.

## ii. Key results

> - `operator` : the Klein–Gordon operator on smooth fields.
> - `equation` : the Klein–Gordon operator as a local operator.
> - `distributionOperator` : the Klein–Gordon operator on distributions.
> - `testOperator` : the Klein–Gordon operator on compactly supported smooth test functions.

## iv. References

> None.

## A. The operator on smooth fields

> `operator m` is `smoothWaveOperator + m ^ 2 • id`. The mass enters as a zeroth order term. The
> field type and the dimension are unchanged. `equation m` records that the operator does not
> enlarge support.

## B. The operator on distributions

> `distributionOperator m` is the wave operator plus `m ^ 2` on `DistributionField d V`. On a test
> function it is given by the same operator `testOperator m`, and `distributionOperator_apply`
> states this.

**`KleinGordon.Spacetime.operator`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Basic.lean#L64).

> The massive wave operator, with mass measured in inverse spacetime-length units.

```lean
def operator (m : ℝ) : smoothFields d V →ₗ[ℝ] smoothFields d V
```

**`KleinGordon.Spacetime.equation`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Basic.lean#L68).

> Klein–Gordon is a local equation on the existing smooth spacetime field class.

```lean
def equation (m : ℝ) : LocalOperator (smoothFields d V)
```

**`KleinGordon.Spacetime.distributionOperator`**, a def, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Basic.lean#L74).

> The Klein–Gordon operator on native distributions.

```lean
def distributionOperator (m : ℝ) : DistributionField d V →L[ℝ] DistributionField d V
```

**`KleinGordon.Spacetime.testOperator`**, a def, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Basic.lean#L78).

> The Klein–Gordon operator on native compact smooth test functions.

```lean
def testOperator (m : ℝ) :
    _root_.TestFunction (⊤ : TopologicalSpace.Opens (SpaceTime d)) ℝ ⊤ →L[ℝ]
      _root_.TestFunction (⊤ : TopologicalSpace.Opens (SpaceTime d)) ℝ ⊤
```

**`KleinGordon.Spacetime.distributionOperator_apply`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Basic.lean#L84).

> The positive second-order operator has the same transpose on test functions.

```lean
lemma distributionOperator_apply (m : ℝ) (T : DistributionField d V)
    (φ : _root_.TestFunction (⊤ : TopologicalSpace.Opens (SpaceTime d)) ℝ ⊤) :
    distributionOperator m T φ = T (testOperator m φ)
```

## Depends on

- [The wave operator](../../waveequation/basic.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Basic.lean)
