---
declaration: module
origin: cited
lean: StandardModel.FermionSector.range_d_le_centreEigenspace, StandardModel.FermionSector.range_bard_le_centreEigenspace, StandardModel.FermionSector.range_u_le_centreEigenspace, StandardModel.FermionSector.range_baru_le_centreEigenspace, StandardModel.FermionSector.range_Q_le_centreEigenspace, StandardModel.FermionSector.range_barQ_le_centreEigenspace, StandardModel.FermionSector.range_L_le_centreEigenspace, StandardModel.FermionSector.range_barL_le_centreEigenspace
statement: formalized
proof: formalized
---

# The centre of `SL(2,ℂ)` on the fermion sector

The module `PhyslibAlpha.Particles.StandardModel.LocalFieldAlgebra.FermionSector.Deriv.Centre`, [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/Centre.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/Centre.lean): 11 declarations, 11 with a docstring.

> The centre of `SL(2,ℂ)` acts by `-1` on the fermion derivative submodules.

## i. Overview

> The fermion symbols are the only Standard Model generators of half-integer spin, and this
> file records what that costs them. The element `-1` of `SL(2,ℂ)` acts on every fermion
> derivative submodule by `-1`, where it acts on the Higgs and gauge ones by `+1`.
>
> The mechanism is uniform across the ten species. A fermion symbol `d i l φ` carries `n`
> covariant-derivative slots, each a four-vector index, and one value index in the dual of a
> Weyl-based representation. The derivative slots see `-1` through the Lorentz matrix, which is
> the identity there (`SL2C.toLorentzGroup_neg_one`), so they do not move at all; the value
> index sees it through `rep.dual`, and `repLorentzGroup_neg_one` says that the Weyl factor
> turns it into a sign. `Invariants.range_le_centreEigenspace_neg_one` does this once for an
> arbitrary symbol family; section A applies it to the ten species and section B joins them.
>
> This is the half-integer-spin obstruction of `Invariants/CentreEigenspace.lean` in the form the
> Yukawa and gauge-fermion classifications need. A product with an odd number of fermion factors
> inherits the sign, and a subspace of sign `-1` carries no Lorentz invariant.

## ii. Key results

> - `range_d_le_centreEigenspace`, ..., `range_bare_le_centreEigenspace` : the symbols of each of
>   the ten species carry the sign `-1`.
> - `derivSubmodule_le_centreEigenspace` : the centre of `SL(2,ℂ)` acts on the fermion derivative
>   submodules by `-1`.

## iv. References

> * None.

## A. The ten species

> Each species feeds `range_le_centreEigenspace_neg_one` with its own Lorentz law and the sign
> of its value space. The five unbarred species are Weyl-valued and the five barred ones are
> conjugate Weyl-valued; conjugation does not move a real sign, so all ten carry `-1`.

**`StandardModel.FermionSector.range_d_le_centreEigenspace`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/Centre.lean#L70).

> The `d` symbols carry the sign `-1`.

```lean
lemma range_d_le_centreEigenspace (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (d f l) ≤ centreEigenspace repLorentz (-1)
```

**`StandardModel.FermionSector.range_bard_le_centreEigenspace`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/Centre.lean#L76).

> The `bard` symbols carry the sign `-1`.

```lean
lemma range_bard_le_centreEigenspace (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (bard f l) ≤ centreEigenspace repLorentz (-1)
```

**`StandardModel.FermionSector.range_u_le_centreEigenspace`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/Centre.lean#L82).

> The `u` symbols carry the sign `-1`.

```lean
lemma range_u_le_centreEigenspace (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (u f l) ≤ centreEigenspace repLorentz (-1)
```

**`StandardModel.FermionSector.range_baru_le_centreEigenspace`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/Centre.lean#L88).

> The `baru` symbols carry the sign `-1`.

```lean
lemma range_baru_le_centreEigenspace (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (baru f l) ≤ centreEigenspace repLorentz (-1)
```

**`StandardModel.FermionSector.range_Q_le_centreEigenspace`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/Centre.lean#L94).

> The `Q` symbols carry the sign `-1`.

```lean
lemma range_Q_le_centreEigenspace (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (Q f l) ≤ centreEigenspace repLorentz (-1)
```

**`StandardModel.FermionSector.range_barQ_le_centreEigenspace`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/Centre.lean#L100).

> The `barQ` symbols carry the sign `-1`.

```lean
lemma range_barQ_le_centreEigenspace (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (barQ f l) ≤ centreEigenspace repLorentz (-1)
```

**`StandardModel.FermionSector.range_L_le_centreEigenspace`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/Centre.lean#L106).

> The `L` symbols carry the sign `-1`.

```lean
lemma range_L_le_centreEigenspace (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (L f l) ≤ centreEigenspace repLorentz (-1)
```

**`StandardModel.FermionSector.range_barL_le_centreEigenspace`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/Centre.lean#L112).

> The `barL` symbols carry the sign `-1`.

```lean
lemma range_barL_le_centreEigenspace (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (barL f l) ≤ centreEigenspace repLorentz (-1)
```

**`StandardModel.FermionSector.range_e_le_centreEigenspace`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/Centre.lean#L118).

> The `e` symbols carry the sign `-1`.

```lean
lemma range_e_le_centreEigenspace (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (e f l) ≤ centreEigenspace repLorentz (-1)
```

**`StandardModel.FermionSector.range_bare_le_centreEigenspace`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/Centre.lean#L124).

> The `bare` symbols carry the sign `-1`.

```lean
lemma range_bare_le_centreEigenspace (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (bare f l) ≤ centreEigenspace repLorentz (-1)
```

## B. The fermion derivative submodules

> The derivative submodule is the join over the three families, the derivative slots and the ten
> species of the ranges of section A, and an eigenspace is closed under joins.

**`StandardModel.FermionSector.derivSubmodule_le_centreEigenspace`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/Centre.lean#L141).

> The centre of `SL(2,ℂ)` acts on the fermion derivative submodules by `-1`, for any
> number of covariant derivatives. Every fermion symbol carries one Weyl-spinor value index,
> and the derivative slots are inert at the centre.

```lean
lemma derivSubmodule_le_centreEigenspace (n : ℕ) :
    derivSubmodule n ≤ centreEigenspace repLorentz (-1)
```

## Depends on

- [The fermion sector](../part-02/localfieldalgebra-fermionsector-basic.md)
- [The eigenspaces of the centre of `SL(2,ℂ)`](../../../relativity/lorentzgroup/invariants-centreeigenspace.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/Centre.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/Centre.lean)
