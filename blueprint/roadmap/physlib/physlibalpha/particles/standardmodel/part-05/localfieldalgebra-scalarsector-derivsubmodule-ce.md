---
declaration: module
origin: cited
lean: StandardModel.ScalarSector.range_covH_le_centreEigenspace, StandardModel.ScalarSector.range_covBarH_le_centreEigenspace, StandardModel.ScalarSector.derivSubmodule_le_centreEigenspace
statement: formalized
proof: formalized
---

# The centre of `SL(2,ℂ)` on the scalar sector

The module `PhyslibAlpha.Particles.StandardModel.LocalFieldAlgebra.ScalarSector.DerivSubmodule.Centre`, [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/DerivSubmodule/Centre.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/DerivSubmodule/Centre.lean): 3 declarations, 3 with a docstring.

> The centre of `SL(2,ℂ)` acts by `+1` on the Higgs derivative submodules.

## i. Overview

> The Higgs is a Lorentz scalar, so the centre of `SL(2,ℂ)` acts on its derivative submodules by
> `+1`. The covariant-derivative slots mix by the Lorentz matrix, which is the identity at the
> centre, and the value index is inert because the value space carries the trivial
> representation. The conjugate tower is the same, conjugation of the trivial representation
> being trivial again.
>
> This is the integer-spin half of the parity count the Yukawa classification runs. Paired with
> `StandardModel.FermionSector.derivSubmodule_le_centreEigenspace`, which gives the fermions
> `-1`, it makes a product with a single fermion factor carry `-1`, and a subspace of sign `-1`
> carries no Lorentz invariant.

## ii. Key results

> - `range_covH_le_centreEigenspace` : the Higgs symbols carry the sign `+1`, their value space
>   being a Lorentz scalar.
> - `range_covBarH_le_centreEigenspace` : the conjugate Higgs symbols carry the sign `+1`, for the
>   same reason.
> - `derivSubmodule_le_centreEigenspace` : the centre of `SL(2,ℂ)` acts on the Higgs derivative
>   submodules by `+1`, for any number of covariant derivatives.

## iv. References

> * None.

## A. The two towers

> Each tower feeds `range_le_centreEigenspace` with its own Lorentz law and the sign of its
> value space, which is `+1` for both. The value space of the Higgs tower carries the trivial
> representation and that of the conjugate tower its conjugate.

**`StandardModel.ScalarSector.range_covH_le_centreEigenspace`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/DerivSubmodule/Centre.lean#L68).

> The Higgs symbols carry the sign `+1`, their value space being a Lorentz scalar.

```lean
lemma range_covH_le_centreEigenspace (n : ℕ) (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (covH n l) ≤ centreEigenspace repLorentzGroup 1
```

**`StandardModel.ScalarSector.range_covBarH_le_centreEigenspace`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/DerivSubmodule/Centre.lean#L73).

> The conjugate Higgs symbols carry the sign `+1`, for the same reason.

```lean
lemma range_covBarH_le_centreEigenspace (n : ℕ) (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (covBarH n l) ≤ centreEigenspace repLorentzGroup 1
```

## B. The Higgs derivative submodules

> The derivative submodule is the join of the two towers over the derivative slots, and an
> eigenspace is closed under joins.

**`StandardModel.ScalarSector.derivSubmodule_le_centreEigenspace`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/DerivSubmodule/Centre.lean#L89).

> The centre of `SL(2,ℂ)` acts on the Higgs derivative submodules by `+1`, for any
> number of covariant derivatives. The Higgs is a Lorentz scalar and the derivative slots are
> inert at the centre.

```lean
lemma derivSubmodule_le_centreEigenspace (n : ℕ) :
    derivSubmodule n ≤ centreEigenspace repLorentzGroup 1
```

## Depends on

- [The derivative submodules of the scalar sector](localfieldalgebra-scalarsector-derivsubmodule-ba.md)
- [The eigenspaces of the centre of `SL(2,ℂ)`](../../../relativity/lorentzgroup/invariants-centreeigenspace.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/DerivSubmodule/Centre.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/DerivSubmodule/Centre.lean)
