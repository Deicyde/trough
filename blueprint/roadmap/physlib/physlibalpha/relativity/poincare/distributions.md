---
declaration: module
origin: cited
lean: PoincareGroup.lorentzCLE, PoincareGroup.abs_det_lorentzCLE, PoincareGroup.actTestFunction, PoincareGroup.actTestFunction_apply, PoincareGroup.actTestFunction_translation_inv, PoincareGroup.actTestFunction_one, PoincareGroup.actTestFunction_mul, PoincareGroup.tsupport_actTestFunction
statement: formalized
proof: formalized
---

# The Poincaré action on test functions and distributions

The module `PhyslibAlpha.Relativity.Poincare.Distributions`, [PhyslibAlpha/Relativity/Poincare/Distributions.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Distributions.lean): 14 declarations, 14 with a docstring.

> The Poincaré group acts on test functions by pullback and on distributions by transposition.

## i. Overview

> A Poincaré element `g` acts on a test function by `(g • φ) x = φ (g⁻¹ x)`. The action is
> continuous on the space of test functions because pullback by a Lorentz transformation and by a
> translation are. A distribution `T` is transformed by `(g • T) φ = T (g⁻¹ • φ)`. Then the
> delta distribution at `p` goes to the delta distribution at `g p`. A distribution that vanishes
> outside a set goes to a distribution that vanishes outside the image of the set.

## ii. Key results

> - `PoincareGroup.actTestFunction` : the action on test functions.
> - `PoincareGroup.actDist` : the action on distributions.
> - `PoincareGroup.isVanishingOn_actDist` : the support of a transformed distribution.
> - `PoincareGroup.actDist_delta` : the action sends a delta distribution to a delta distribution.

## iv. References

> None.

## A. Test functions

> - `PoincareGroup.actTestFunction` : the action on test functions.

## B. Distributions

> - `PoincareGroup.actDist` : the action on distributions.

**`PoincareGroup.lorentzCLE`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Distributions.lean#L63).

> A Lorentz transformation as a continuous linear equivalence of spacetime.

```lean
def lorentzCLE (Λ : LorentzGroup d) : SpaceTime d ≃L[ℝ] SpaceTime d
```

**`PoincareGroup.abs_det_lorentzCLE`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Distributions.lean#L69).

> The determinant of a Lorentz transformation has absolute value one.

```lean
lemma abs_det_lorentzCLE (Λ : LorentzGroup d) :
    |LinearMap.det (lorentzCLE Λ : SpaceTime d →ₗ[ℝ] SpaceTime d)| = 1
```

**`PoincareGroup.actTestFunction`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Distributions.lean#L86).

> The action of the Poincaré group on test functions.

```lean
def actTestFunction (g : PoincareGroup d) :
    𝓓((⊤ : Opens (SpaceTime d)), F) →L[ℝ] 𝓓((⊤ : Opens (SpaceTime d)), F)
```

**`PoincareGroup.actTestFunction_apply`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Distributions.lean#L93).

> The value of a transformed test function.

```lean
lemma actTestFunction_apply (g : PoincareGroup d) (φ : 𝓓((⊤ : Opens (SpaceTime d)), F))
    (x : SpaceTime d) : actTestFunction g φ x = φ (g⁻¹ • x)
```

**`PoincareGroup.actTestFunction_translation_inv`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Distributions.lean#L97).

> The inverse of a pure translation acts on test functions as the translate `x ↦ φ (x + p)`.

```lean
lemma actTestFunction_translation_inv (p : SpaceTime d) (φ : 𝓓((⊤ : Opens (SpaceTime d)), F)) :
    actTestFunction (⟨p, 1⟩ : PoincareGroup d)⁻¹ φ = TestFunction.precompTranslationCLM p φ
```

**`PoincareGroup.actTestFunction_one`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Distributions.lean#L105).

> The identity acts trivially on test functions.

```lean
lemma actTestFunction_one (φ : 𝓓((⊤ : Opens (SpaceTime d)), F)) :
    actTestFunction (1 : PoincareGroup d) φ = φ
```

**`PoincareGroup.actTestFunction_mul`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Distributions.lean#L111).

> The action on test functions is a left action.

```lean
lemma actTestFunction_mul (g h : PoincareGroup d) (φ : 𝓓((⊤ : Opens (SpaceTime d)), F)) :
    actTestFunction (g * h) φ = actTestFunction g (actTestFunction h φ)
```

**`PoincareGroup.tsupport_actTestFunction`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Distributions.lean#L117).

> The support of a transformed test function is the image of the support.

```lean
lemma tsupport_actTestFunction (g : PoincareGroup d) (φ : 𝓓((⊤ : Opens (SpaceTime d)), F)) :
    tsupport (actTestFunction g φ) = g • tsupport φ
```

**`PoincareGroup.actDist`**, a def, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Distributions.lean#L128).

> The action of the Poincaré group on distributions: `(g • T) φ = T (g⁻¹ • φ)`.

```lean
def actDist (g : PoincareGroup d) : DistributionField d V →L[ℝ] DistributionField d V
```

**`PoincareGroup.actDist_apply`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Distributions.lean#L132).

> The value of a transformed distribution.

```lean
lemma actDist_apply (g : PoincareGroup d) (T : DistributionField d V)
    (φ : 𝓓((⊤ : Opens (SpaceTime d)), ℝ)) : actDist g T φ = T (actTestFunction g⁻¹ φ)
```

**`PoincareGroup.actDist_one`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Distributions.lean#L136).

> The identity acts trivially on distributions.

```lean
lemma actDist_one (T : DistributionField d V) : actDist (1 : PoincareGroup d) T = T
```

**`PoincareGroup.actDist_mul`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Distributions.lean#L141).

> The action on distributions is a left action.

```lean
lemma actDist_mul (g h : PoincareGroup d) (T : DistributionField d V) :
    actDist (g * h) T = actDist g (actDist h T)
```

**`PoincareGroup.isVanishingOn_actDist`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Distributions.lean#L147).

> A transformed distribution vanishes outside the image of the set.

```lean
lemma isVanishingOn_actDist (g : PoincareGroup d) {T : DistributionField d V}
    {U : Set (SpaceTime d)} (hT : Distribution.IsVanishingOn T U) :
    Distribution.IsVanishingOn (actDist g T) (g • U)
```

**`PoincareGroup.actDist_delta`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Distributions.lean#L157).

> The action sends a delta distribution to a delta distribution.

```lean
lemma actDist_delta (g : PoincareGroup d) (p : SpaceTime d) :
    actDist g (Distribution.delta p : DistributionField d ℝ) = Distribution.delta (g • p)
```

## Depends on

- [Operations on test functions](../../mathematics/part-02/distribution/testfunction.md)
- [Translation of test functions](../../mathematics/part-02/distribution/translation.md)
- [The Poincaré group](basic.md)
- [Smooth fields and distributions on spacetime](../../spaceandtime/spacetime/fields.md)

## Sources

- [PhyslibAlpha/Relativity/Poincare/Distributions.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Distributions.lean)
