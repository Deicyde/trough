---
declaration: module
origin: cited
lean: TwoHiggsDoublet.EffectivePotential, TwoHiggsDoublet.EffectivePotential.IsInvariant, TwoHiggsDoublet.EffectivePotential.HasMaxMassDimLE, TwoHiggsDoublet.EffectivePotential.HasMaxMassDimLE.exists_comp_linear_poly
statement: formalized
proof: formalized
---

# The effective potential of the two Higgs doublet model

The module `PhyslibAlpha.Particles.BeyondTheStandardModel.TwoHDM.EffectivePotential`, [PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/EffectivePotential.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/EffectivePotential.lean): 4 declarations, 4 with a docstring.

> Effective potentials of the 2HDM, their gauge invariance, and their maximum mass dimension.

## i. Overview

> An *effective potential* of the two Higgs doublet model is a real-valued function
> `V : TwoHiggsDoublet → ℝ` of the field configuration. This file introduces the two physical
> properties of such a potential used when expressing it through the gauge-invariant bilinears:
>
> * `IsInvariant V` — invariance under the global gauge group, and
> * `HasMaxMassDimLE V n` — being a polynomial in the field components of mass dimension `≤ n`.

## ii. Key results

> * `EffectivePotential` — the type of effective potentials.
> * `IsInvariant` — gauge invariance of a potential.
> * `HasMaxMassDimLE` — being a bounded-degree polynomial in the field components.
> * `HasMaxMassDimLE.exists_comp_linear_poly` — a polynomial potential, restricted along any
>   real-linear parametrisation of configurations, is a polynomial in the parameters.

## iv. References

> * None.

**`TwoHiggsDoublet.EffectivePotential`**, an abbrev, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/EffectivePotential.lean#L53).

> A general potential of the Higgs field.

```lean
abbrev EffectivePotential : Type
```

## A. The effective potential and its gauge invariance

**`TwoHiggsDoublet.EffectivePotential.IsInvariant`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/EffectivePotential.lean#L63).

> The proposition that the general potential is invariant under
> the global action of the gauge group.

```lean
def IsInvariant (V : EffectivePotential) : Prop
```

## B. Maximum mass dimension

**`TwoHiggsDoublet.EffectivePotential.HasMaxMassDimLE`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/EffectivePotential.lean#L72).

> The proposition that the potential `V` has a maximum mass dimension
> less then or equal to `n` - also implying it is a polynomial.

```lean
def HasMaxMassDimLE (V : EffectivePotential) (n : ℕ) : Prop
```

**`TwoHiggsDoublet.EffectivePotential.HasMaxMassDimLE.exists_comp_linear_poly`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/EffectivePotential.lean#L79).

> A polynomial potential, restricted along any real-linear parametrisation `L` of field
> configurations, is a genuine polynomial in the parameters. This is the bookkeeping that lets the
> potential be evaluated on the field components of a gauge slice.

```lean
lemma HasMaxMassDimLE.exists_comp_linear_poly {V : EffectivePotential} {n : ℕ}
    (h : HasMaxMassDimLE V n) {ι : Type*} [Fintype ι] [DecidableEq ι]
    (L : (ι → ℝ) →ₗ[ℝ] TwoHiggsDoublet) :
    ∃ P : MvPolynomial ι ℝ, ∀ a : ι → ℝ, V (L a) = P.eval a
```

## Depends on

- [The Module structure on the two Higgs doublet model](twohdm-module.md)

## Sources

- [PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/EffectivePotential.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/EffectivePotential.lean)
