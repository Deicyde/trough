---
declaration: module
origin: cited
lean: StandardModel.IsFermionSector.range_d_le_centreEigenspace, StandardModel.IsFermionSector.range_bard_le_centreEigenspace, StandardModel.IsFermionSector.range_u_le_centreEigenspace, StandardModel.IsFermionSector.range_baru_le_centreEigenspace, StandardModel.IsFermionSector.range_Q_le_centreEigenspace, StandardModel.IsFermionSector.range_barQ_le_centreEigenspace, StandardModel.IsFermionSector.range_L_le_centreEigenspace, StandardModel.IsFermionSector.range_barL_le_centreEigenspace
statement: formalized
proof: formalized
---

# The centre of `SL(2,ℂ)` on the fermion sector

The module `PhyslibAlpha.Particles.StandardModel.IsFermionSector.Deriv.Centre`, [PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/Centre.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/Centre.lean): 11 declarations, 11 with a docstring.

## i. Overview

> The fermion symbols are the only Standard Model generators of half-integer spin, and this
> file records what that costs them: the element `-1` of `SL(2,ℂ)` acts on every fermion
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
> This is the half-integer-spin obstruction of `Invariants/Centre.lean` in the form the Yukawa
> and gauge-fermion classifications need: a product with an odd number of fermion factors
> inherits the sign, and a subspace of sign `-1` carries no Lorentz invariant.

## ii. Key results

> - `range_d_le_centreEigenspace` : the `d` symbols carry the sign `-1`
> - `range_bard_le_centreEigenspace` : the `bard` symbols carry the sign `-1`
> - `range_u_le_centreEigenspace` : the `u` symbols carry the sign `-1`
> - `range_baru_le_centreEigenspace` : the `baru` symbols carry the sign `-1`

## iv. References

> * None.

## A. The ten species

> Each species feeds `range_le_centreEigenspace_neg_one` with its own Lorentz law and the sign
> of its value space. The five unbarred species are Weyl-valued and the five barred ones are
> conjugate Weyl-valued; conjugation does not move a real sign, so all ten carry `-1`.

**`StandardModel.IsFermionSector.range_d_le_centreEigenspace`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/Centre.lean#L100).

> The `d` symbols carry the sign `-1`.

```lean
lemma range_d_le_centreEigenspace (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (d f l) ≤ centreEigenspace repLorentz (-1)
```

**`StandardModel.IsFermionSector.range_bard_le_centreEigenspace`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/Centre.lean#L107).

> The `bard` symbols carry the sign `-1`.

```lean
lemma range_bard_le_centreEigenspace (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (bard f l) ≤ centreEigenspace repLorentz (-1)
```

**`StandardModel.IsFermionSector.range_u_le_centreEigenspace`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/Centre.lean#L114).

> The `u` symbols carry the sign `-1`.

```lean
lemma range_u_le_centreEigenspace (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (u f l) ≤ centreEigenspace repLorentz (-1)
```

**`StandardModel.IsFermionSector.range_baru_le_centreEigenspace`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/Centre.lean#L121).

> The `baru` symbols carry the sign `-1`.

```lean
lemma range_baru_le_centreEigenspace (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (baru f l) ≤ centreEigenspace repLorentz (-1)
```

**`StandardModel.IsFermionSector.range_Q_le_centreEigenspace`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/Centre.lean#L128).

> The `Q` symbols carry the sign `-1`.

```lean
lemma range_Q_le_centreEigenspace (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (Q f l) ≤ centreEigenspace repLorentz (-1)
```

**`StandardModel.IsFermionSector.range_barQ_le_centreEigenspace`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/Centre.lean#L135).

> The `barQ` symbols carry the sign `-1`.

```lean
lemma range_barQ_le_centreEigenspace (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (barQ f l) ≤ centreEigenspace repLorentz (-1)
```

**`StandardModel.IsFermionSector.range_L_le_centreEigenspace`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/Centre.lean#L142).

> The `L` symbols carry the sign `-1`.

```lean
lemma range_L_le_centreEigenspace (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (L f l) ≤ centreEigenspace repLorentz (-1)
```

**`StandardModel.IsFermionSector.range_barL_le_centreEigenspace`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/Centre.lean#L149).

> The `barL` symbols carry the sign `-1`.

```lean
lemma range_barL_le_centreEigenspace (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (barL f l) ≤ centreEigenspace repLorentz (-1)
```

**`StandardModel.IsFermionSector.range_e_le_centreEigenspace`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/Centre.lean#L156).

> The `e` symbols carry the sign `-1`.

```lean
lemma range_e_le_centreEigenspace (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (e f l) ≤ centreEigenspace repLorentz (-1)
```

**`StandardModel.IsFermionSector.range_bare_le_centreEigenspace`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/Centre.lean#L163).

> The `bare` symbols carry the sign `-1`.

```lean
lemma range_bare_le_centreEigenspace (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (bare f l) ≤ centreEigenspace repLorentz (-1)
```

## B. The fermion derivative submodules

> The derivative submodule is the join over the three families, the derivative slots and the ten
> species of the ranges of section A, and an eigenspace is closed under joins.

**`StandardModel.IsFermionSector.derivSubmodule_le_centreEigenspace`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/Centre.lean#L181).

> **The centre of `SL(2,ℂ)` acts on the fermion derivative submodules by `-1`**, for any
> number of covariant derivatives: every fermion symbol carries one Weyl-spinor value index,
> and the derivative slots are inert at the centre.

```lean
lemma derivSubmodule_le_centreEigenspace (n : ℕ) :
    h.derivSubmodule n ≤ centreEigenspace repLorentz (-1)
```

## Depends on

- [The fermion sector](isfermionsector-basic.md)
- [Lorentz invariants of a half-integer spin](../../../relativity/lorentzgroup/invariants-centre.md)

## Proof depends on

- [Down-type singlets (PhyslibAlpha)](../part-03/fermions-downsinglet-basic.md)
- [Charged-lepton singlets (PhyslibAlpha)](../part-03/fermions-leptonsinglet-basic.md)
- [The type corresponding to quark doublets (PhyslibAlpha)](../part-03/fermions-quarkdoublet-basic.md)
- [Up-type singlets (PhyslibAlpha)](../part-03/fermions-upsinglet-basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/Centre.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/Centre.lean)
