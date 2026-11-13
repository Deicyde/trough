---
declaration: module
origin: cited
lean: StandardModel.HiggsAlgebraCovRealization.range_covH_le_centreEigenspace, StandardModel.HiggsAlgebraCovRealization.range_covBarH_le_centreEigenspace, StandardModel.HiggsAlgebraCovRealization.derivSubmodule_le_centreEigenspace
statement: formalized
proof: formalized
---

# The centre of `SL(2,ℂ)` on the Higgs sector

The module `PhyslibAlpha.Particles.StandardModel.Realization.HiggsCov.DerivSubmodule.Centre`, [PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/DerivSubmodule/Centre.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/DerivSubmodule/Centre.lean): 3 declarations, 3 with a docstring.

## i. Overview

> The Higgs is a Lorentz scalar, so the centre of `SL(2,ℂ)` acts on its derivative submodules by
> `+1`: the covariant-derivative slots mix by the Lorentz matrix, which is the identity at the
> centre, and the value index is inert because the value space carries the trivial
> representation. The conjugate tower is the same, conjugation of the trivial representation
> being trivial again.
>
> This is the integer-spin half of the parity count the Yukawa classification runs. Paired with
> `IsFermionSector.derivSubmodule_le_centreEigenspace`, which gives the fermions `-1`, it makes
> a product with a single fermion factor carry `-1`, and a subspace of sign `-1` carries no
> Lorentz invariant.

## ii. Key results

> - `range_covH_le_centreEigenspace` : the Higgs symbols carry the sign `+1`: their value space is a
>   Lorentz scalar
> - `range_covBarH_le_centreEigenspace` : the conjugate Higgs symbols carry the sign `+1`, for the
>   same reason
> - `derivSubmodule_le_centreEigenspace` : the centre of `SL(2,ℂ)` acts on the Higgs derivative
>   submodules by `+1`, for any number of covariant derivatives: the Higgs is a Lorentz scalar and the
>   derivative slots are inert at the centre

## iv. References

> * None.

## A. The two towers

> Each tower feeds `range_le_centreEigenspace` with its own Lorentz law and the sign of its
> value space, which is `+1` for both: the value space of the Higgs tower carries the trivial
> representation and that of the conjugate tower its conjugate.

**`StandardModel.HiggsAlgebraCovRealization.range_covH_le_centreEigenspace`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/DerivSubmodule/Centre.lean#L73).

> The Higgs symbols carry the sign `+1`: their value space is a Lorentz scalar.

```lean
lemma range_covH_le_centreEigenspace (n : ℕ) (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (h.covH n l) ≤ centreEigenspace repLorentz 1
```

**`StandardModel.HiggsAlgebraCovRealization.range_covBarH_le_centreEigenspace`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/DerivSubmodule/Centre.lean#L79).

> The conjugate Higgs symbols carry the sign `+1`, for the same reason.

```lean
lemma range_covBarH_le_centreEigenspace (n : ℕ) (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (h.covBarH n l) ≤ centreEigenspace repLorentz 1
```

## B. The Higgs derivative submodules

> The derivative submodule is the join of the two towers over the derivative slots, and an
> eigenspace is closed under joins.

**`StandardModel.HiggsAlgebraCovRealization.derivSubmodule_le_centreEigenspace`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/DerivSubmodule/Centre.lean#L96).

> **The centre of `SL(2,ℂ)` acts on the Higgs derivative submodules by `+1`**, for any
> number of covariant derivatives: the Higgs is a Lorentz scalar and the derivative slots are
> inert at the centre.

```lean
lemma derivSubmodule_le_centreEigenspace (n : ℕ) :
    h.derivSubmodule n ≤ centreEigenspace repLorentz 1
```

## Depends on

- [The derivative submodules of the Higgs sector](realization-higgscov-derivsubmodule-basic.md)
- [Lorentz invariants of a half-integer spin](../../../relativity/lorentzgroup/invariants-centre.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/DerivSubmodule/Centre.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/DerivSubmodule/Centre.lean)
