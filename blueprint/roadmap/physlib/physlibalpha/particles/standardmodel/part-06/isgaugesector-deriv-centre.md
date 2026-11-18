---
declaration: module
origin: cited
lean: StandardModel.IsGaugeSector.repLorentz_neg_one_F, StandardModel.IsGaugeSector.span_range_F_le_centreEigenspace, StandardModel.IsGaugeSector.derivSubmodule_le_centreEigenspace
statement: formalized
proof: formalized
---

# The centre of `SL(2,ℂ)` on the gauge sector

The module `PhyslibAlpha.Particles.StandardModel.IsGaugeSector.Deriv.Centre`, [PhyslibAlpha/Particles/StandardModel/IsGaugeSector/Deriv/Centre.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/Deriv/Centre.lean): 3 declarations, 3 with a docstring.

## i. Overview

> The field strength is of integer spin, so the centre of `SL(2,ℂ)` acts on its derivative
> submodules by `+1`. Every index a field-strength symbol carries — the two covector indices and
> the covariant-derivative slots — mixes by the Lorentz matrix, and the adjoint value index does
> not see the Lorentz group at all; since `-1` covers the identity Lorentz transformation
> (`SL2C.toLorentzGroup_neg_one`), nothing moves.
>
> This is the integer-spin half of the parity count the gauge-fermion classification runs.
> Paired with `IsFermionSector.derivSubmodule_le_centreEigenspace`, which gives the fermions
> `-1`, it makes the product `F ψ` carry `-1`, and a subspace of sign `-1` carries no Lorentz
> invariant.
>
> Unlike the Higgs and fermion towers, the field-strength symbols are not of the shape
> `IsLorentzCovDerivTransforms` describes — they carry two covector indices beside their
> derivative slots — so the collapse at the centre is run directly on `repLorentz_F`.

## ii. Key results

> - `repLorentz_neg_one_F` : a field-strength symbol is fixed by the centre of `SL(2,ℂ)`: all of its
>   indices mix by the Lorentz matrix, which is the identity there
> - `span_range_F_le_centreEigenspace` : the span of a field-strength symbol family carries the sign
>   `+1`
> - `derivSubmodule_le_centreEigenspace` : the centre of `SL(2,ℂ)` acts on the field-strength
>   derivative submodules by `+1`, for any number of covariant derivatives: the field strength is of
>   integer spin and every one of its indices is inert at the centre

## iv. References

> * None.

## A. The field-strength symbols

> At the centre each of the three sums of `repLorentz_F` is a sum against a row of the identity
> matrix, so each collapses to its diagonal term and the symbol is returned unchanged.

**`StandardModel.IsGaugeSector.repLorentz_neg_one_F`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/Deriv/Centre.lean#L84).

> A field-strength symbol is fixed by the centre of `SL(2,ℂ)`: all of its indices mix by the
> Lorentz matrix, which is the identity there.

```lean
lemma repLorentz_neg_one_F {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ GaugeAlgebra) : repLorentz (-1) (F l μ ν φ) = F l μ ν φ
```

**`StandardModel.IsGaugeSector.span_range_F_le_centreEigenspace`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/Deriv/Centre.lean#L97).

> The span of a field-strength symbol family carries the sign `+1`.

```lean
lemma span_range_F_le_centreEigenspace {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (μ ν : Fin 1 ⊕ Fin 3) :
    Submodule.span ℂ (Set.range (F l μ ν)) ≤ centreEigenspace repLorentz 1
```

## B. The field-strength derivative submodules

> The derivative submodule is the join of the symbol spans over the derivative slots and the two
> covector indices, and an eigenspace is closed under joins.

**`StandardModel.IsGaugeSector.derivSubmodule_le_centreEigenspace`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/Deriv/Centre.lean#L117).

> **The centre of `SL(2,ℂ)` acts on the field-strength derivative submodules by `+1`**, for
> any number of covariant derivatives: the field strength is of integer spin and every one of
> its indices is inert at the centre.

```lean
lemma derivSubmodule_le_centreEigenspace (n : ℕ) :
    h.derivSubmodule n ≤ centreEigenspace repLorentz 1
```

## Depends on

- [The gauge sector](isgaugesector-basic.md)
- [Lorentz invariants of a half-integer spin](../../../relativity/lorentzgroup/invariants-centre.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/IsGaugeSector/Deriv/Centre.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/Deriv/Centre.lean)
