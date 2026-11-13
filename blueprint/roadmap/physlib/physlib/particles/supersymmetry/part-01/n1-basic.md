---
declaration: module
origin: cited
lean: SUSY.N1.ChiralScalarConfiguration, SUSY.N1.ChiralColor, SUSY.N1.ChiralColor.tau, SUSY.N1.ChiralColor.bar, SUSY.N1.ChiralColor.bar_bar, SUSY.N1.ChiralColor.bar_tau, SUSY.N1.chiralModule, SUSY.N1.instAddCommGroupChiralModule
statement: formalized
proof: formalized
---

# SUSY N=1 chiral sector: index, configuration, and conjugation data

The module `Physlib.Particles.SuperSymmetry.N1.Basic`, [Physlib/Particles/SuperSymmetry/N1/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Basic.lean): 33 declarations, 29 with a docstring.

> The index data, field configuration and conjugation of the N=1 chiral sector, as a tensor species.

## i. Overview

> The chiral scalars are indexed by a finite type `ι`, and a configuration is a point of `ι → ℂ`
> (`ChiralScalarConfiguration`). The anti-chiral scalars are the complex conjugates of this
> configuration, not independent field data. A tensor index carries one of four colours
> (`ChiralColor`): holomorphic or anti-holomorphic, crossed with up or down. The four colours have
> four carriers: `chiralUp` the vectors `ι → ℂ`, `chiralDown` their dual, and `antiUp` and
> `antiDown` the conjugate modules of these two (`ConjModule`, in which `i` acts as `−i`).
>
> The dual colour `τ` flips variance and keeps holomorphy, and two indices contract only when their
> colours are `τ`-related, so `g^{IJ̄} D_I W D̄_J̄ W̄` type-checks. The conjugate colour `bar` flips
> holomorphy and keeps variance. Contraction is the δ pairing of coordinate vectors: the basis at
> `τ c` is the dual basis of the basis at `c` (`chiralTensor.instHasContrDualBases`), so a
> contraction is a sum over `ι`. Every colour carries the trivial representation of `Unit`.
>
> `chiralTensor` packages this data as a `ConjTensorSpecies`. It gives the chiral sector the generic
> tensor API, and the conjugation map `conjT` in which reality and Hermiticity are stated.

## ii. Key results

> - `SUSY.N1.ChiralScalarConfiguration` : the configuration space `ι → ℂ`.
> - `SUSY.N1.ChiralColor` : the four colours, with the dual involution `ChiralColor.tau`.
> - `SUSY.N1.chiralTensor` : the chiral sector as a `ConjTensorSpecies`.
> - `SUSY.N1.chiralTensor.instHasContrDualBases` : the chiral species has dual bases at dual
>     colours, matched by the identity on `ι`.

## iv. References

> * None.

## A. The chiral scalar configuration

**`SUSY.N1.ChiralScalarConfiguration`**, an abbrev, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Basic.lean#L70).

> The chiral scalar configuration: a complex value for each chiral label, the sector's only field
> data. An `abbrev`, so Mathlib's function-space lemmas apply to it directly.

```lean
abbrev ChiralScalarConfiguration (ChiralIndexingType : Type*)
```

## B. The chiral colours and the dual involution

**`SUSY.N1.ChiralColor`**, an inductive, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Basic.lean#L81).

> The four colours of a chiral-sector index: holomorphy (`chiral` or `anti`) crossed with
> variance (`up` or `down`).

```lean
inductive ChiralColor | chiralUp | chiralDown | antiUp | antiDown
```

**`SUSY.N1.ChiralColor.tau`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Basic.lean#L88).

> The dual colour: flips variance and keeps holomorphy. Two indices contract exactly when their
> colours are `τ`-related.

```lean
def tau : ChiralColor → ChiralColor
```

**`SUSY.N1.ChiralColor.bar`**, a def, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Basic.lean#L96).

> The conjugate colour: flips holomorphy and keeps variance. It commutes with `tau`
> (`bar_tau`).

```lean
def bar : ChiralColor → ChiralColor
```

**`SUSY.N1.ChiralColor.bar_bar`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Basic.lean#L102).

```lean
lemma bar_bar (c : ChiralColor) : bar (bar c) = c
```

**`SUSY.N1.ChiralColor.bar_tau`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Basic.lean#L104).

```lean
lemma bar_tau (c : ChiralColor) : bar (tau c) = tau (bar c)
```

## C. Carrier, representation, and basis

> `chiralUp` and `chiralDown` carry `ι → ℂ` and its dual; `antiUp` and `antiDown` carry their
> conjugate modules. The representation is trivial over `Unit`, and every basis is indexed by `ι`.

**`SUSY.N1.chiralModule`**, an abbrev, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Basic.lean#L120).

> The carrier of each colour: `ι → ℂ` and its dual on the holomorphic side, and their conjugate
> modules (`ConjModule`, where `i` acts as `−i`) on the anti-holomorphic side.

```lean
abbrev chiralModule : ChiralColor → Type
```

**`SUSY.N1.instAddCommGroupChiralModule`**, an instance, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Basic.lean#L126).

```lean
instance instAddCommGroupChiralModule : ∀ c, AddCommGroup (chiralModule (ι := ι) c)
```

**`SUSY.N1.instModuleChiralModule`**, an instance, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Basic.lean#L129).

```lean
noncomputable instance instModuleChiralModule : ∀ c, Module ℂ (chiralModule (ι := ι) c)
```

**`SUSY.N1.chiralRep`**, a def, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Basic.lean#L133).

> The representation of each colour: trivial, over the trivial group `Unit`.

```lean
def chiralRep : (c : ChiralColor) → Representation ℂ Unit (chiralModule (ι := ι) c)
```

**`SUSY.N1.piBasis`**, a def, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Basic.lean#L137).

> The standard basis of `ι → ℂ`.

```lean
def piBasis : Basis ι ℂ (ι → ℂ)
```

**`SUSY.N1.chiralBasis`**, a def, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Basic.lean#L141).

> The basis of each colour's carrier, indexed by `ι`: `piBasis`, its dual basis, and the
> conjugate of each.

```lean
noncomputable def chiralBasis : (c : ChiralColor) → Basis ι ℂ (chiralModule (ι := ι) c)
```

## D. The δ structure on based finite modules

> The contraction and unit of the species are the δ structure in basis coordinates. A contraction
> pairs two based modules `(M, b)` and `(N, b')` sharing the index `ι`:
> `(x, y) ↦ ∑_I (b x)_I (b' y)_I` (`deltaContr₂`), with cap `∑_I b_I ⊗ b'_I` (`deltaCap₂`). The
> species has no `WithMetric` instance: the metric of the chiral sector is the Kähler metric
> `g_{IJ̄}`, built downstream.

**`SUSY.N1.deltaBil₂`**, a def, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Basic.lean#L164).

> The δ pairing `(x, y) ↦ ∑_I (b x)_I (b' y)_I` of two based modules sharing the index `ι`,
> built from Mathlib's `Basis.toDual`.

```lean
def deltaBil₂ (b : Basis ι ℂ M) (b' : Basis ι ℂ N) : M →ₗ[ℂ] N →ₗ[ℂ] ℂ
```

**`SUSY.N1.deltaBil₂_apply`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Basic.lean#L168).

> `deltaBil₂ b b' x y = ∑_I (b x)_I (b' y)_I`.

```lean
lemma deltaBil₂_apply (b : Basis ι ℂ M) (b' : Basis ι ℂ N) (x : M) (y : N) :
    deltaBil₂ b b' x y = ∑ I, b.equivFun x I * b'.equivFun y I
```

**`SUSY.N1.deltaContr₂`**, a def, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Basic.lean#L177).

> The two-module δ contraction `M ⊗ N → ℂ`.

```lean
def deltaContr₂ (b : Basis ι ℂ M) (b' : Basis ι ℂ N) : M ⊗[ℂ] N →ₗ[ℂ] ℂ
```

**`SUSY.N1.deltaContr₂_tmul`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Basic.lean#L181).

> `deltaContr₂ b b' (x ⊗ₜ y) = ∑_I (b x)_I (b' y)_I`.

```lean
lemma deltaContr₂_tmul (b : Basis ι ℂ M) (b' : Basis ι ℂ N) (x : M) (y : N) :
    deltaContr₂ b b' (x ⊗ₜ[ℂ] y) = ∑ I, b.equivFun x I * b'.equivFun y I
```

**`SUSY.N1.deltaContr₂_tmul_basis`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Basic.lean#L186).

> `deltaContr₂ b b' (x ⊗ₜ b' J) = x_J`: pairing with the second basis reads off a coordinate.

```lean
lemma deltaContr₂_tmul_basis (b : Basis ι ℂ M) (b' : Basis ι ℂ N) (x : M) (J : ι) :
    deltaContr₂ b b' (x ⊗ₜ[ℂ] b' J) = b.equivFun x J
```

**`SUSY.N1.deltaContr₂_basis_basis`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Basic.lean#L191).

> `deltaContr₂ b b' (b I ⊗ₜ b' J) = δ_{IJ}`: the two bases are δ-dual.

```lean
lemma deltaContr₂_basis_basis (b : Basis ι ℂ M) (b' : Basis ι ℂ N) (I J : ι) :
    deltaContr₂ b b' (b I ⊗ₜ[ℂ] b' J) = if I = J then 1 else 0
```

**`SUSY.N1.deltaContr₂_comm`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Basic.lean#L196).

> `deltaContr₂ b b' (x ⊗ₜ y) = deltaContr₂ b' b (y ⊗ₜ x)`: swapping slots swaps the two bases.

```lean
lemma deltaContr₂_comm (b : Basis ι ℂ M) (b' : Basis ι ℂ N) (x : M) (y : N) :
    deltaContr₂ b b' (x ⊗ₜ[ℂ] y) = deltaContr₂ b' b (y ⊗ₜ[ℂ] x)
```

**`SUSY.N1.deltaCap₂`**, a def, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Basic.lean#L202).

> The two-module δ cap `∑_I b_I ⊗ b'_I ∈ M ⊗ N`.

```lean
def deltaCap₂ (b : Basis ι ℂ M) (b' : Basis ι ℂ N) : M ⊗[ℂ] N
```

**`SUSY.N1.deltaCap₂_comm`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Basic.lean#L206).

> `comm (deltaCap₂ b b') = deltaCap₂ b' b`: swapping the two factors swaps the two bases.

```lean
lemma deltaCap₂_comm (b : Basis ι ℂ M) (b' : Basis ι ℂ N) :
    TensorProduct.comm ℂ M N (deltaCap₂ b b') = deltaCap₂ b' b
```

**`SUSY.N1.deltaUnit₂_symm`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Basic.lean#L214).

> The `unit_symm` law (two-module, `toSpanSingleton` form): `deltaCap₂ b' b` is the swap of
> `deltaCap₂ b b'`.

```lean
lemma deltaUnit₂_symm (b : Basis ι ℂ M) (b' : Basis ι ℂ N) :
    LinearMap.toSpanSingleton ℂ _ (deltaCap₂ b' b) 1 =
      LinearMap.lTensor N (LinearEquiv.refl ℂ M).toLinearMap
        (TensorProduct.comm ℂ M N (LinearMap.toSpanSingleton ℂ _ (deltaCap₂ b b') 1))
```

**`SUSY.N1.deltaContr₂_unit`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Basic.lean#L224).

> The snake identity (two-module, `contr_unit` law): contracting `x ∈ M` into the `M`-leg of
> `deltaCap₂ b' b ∈ N ⊗ M` returns `x`.

```lean
lemma deltaContr₂_unit (b : Basis ι ℂ M) (b' : Basis ι ℂ N) (x : M) :
    (TensorProduct.lid ℂ M) ((deltaContr₂ b b').rTensor M
      ((TensorProduct.assoc ℂ M N M).symm
        (x ⊗ₜ[ℂ] LinearMap.toSpanSingleton ℂ _ (deltaCap₂ b' b) 1))) = x
```

## E. The chiral-index tensor species

**`SUSY.N1.chiralTensor`**, a def, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Basic.lean#L243).

> The chiral-index tensor species with its conjugation. Its contraction is the δ pairing of a
> colour with its dual `τ c`, its unit the δ cap, and its conjugation flips holomorphy by
> `ChiralColor.bar`.

```lean
def chiralTensor : ConjTensorSpecies ℂ ChiralColor Unit (chiralModule (ι := ι)) (fun _ => ι)
    (chiralRep (ι := ι)) (chiralBasis (ι := ι))
```

**`SUSY.N1.chiralTensor_contr_chiralBasis`**, a lemma, [line 281](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Basic.lean#L281).

> The chiral contraction of two basis vectors is the Kronecker δ.

```lean
lemma chiralTensor_contr_chiralBasis (d : ChiralColor) (x₁ x₂ : ι) :
    (chiralTensor (ι := ι)).contr d
        (chiralBasis (ι := ι) d x₁ ⊗ₜ[ℂ] chiralBasis (ι := ι) ((chiralTensor (ι := ι)).τ d) x₂)
      = if x₁ = x₂ then 1 else 0
```

**`SUSY.N1.chiralTensor.instHasContrDualBases`**, an instance, [line 288](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Basic.lean#L288).

> The chiral species has dual bases at dual colours, matched by the identity on `ι`.

```lean
instance chiralTensor.instHasContrDualBases :
    TensorSpecies.HasContrDualBases (chiralTensor (ι := ι)).toTensorSpecies
```

**`SUSY.N1.contrDualIdxEquiv_eq_refl`**, a lemma, [line 294](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Basic.lean#L294).

> The dual-label matching of the chiral species is the identity.

```lean
lemma contrDualIdxEquiv_eq_refl (c : ChiralColor) :
    TensorSpecies.HasContrDualBases.contrDualIdxEquiv (chiralTensor (ι := ι)).toTensorSpecies c =
      Equiv.refl ι
```

## F. Conjugation

> Conjugation is part of `chiralTensor` (§E), and the framework supplies the map `conjT` and its
> laws (`conjT_conjT`, `conjT_contrT`, `conjT_eq_permT_iff`). This section normalizes `conjT` for
> the two shapes the sector conjugates, the scalar `W` and the holomorphic covector `D_I W`, and
> checks on components that it is complex conjugation.

> The following normalize the output of `(chiralTensor (ι := ι)).conjT` back to the
> canonical colour lists for scalar and anti-holomorphic covector tensors respectively.

**`SUSY.N1.conjScalar`**, a def, [line 321](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Basic.lean#L321).

> Conjugation of a scalar tensor, normalized back to the scalar colour list `![]`.

```lean
def conjScalar (t : (chiralTensor (ι := ι)).Tensor ![]) :
    (chiralTensor (ι := ι)).Tensor ![]
```

**`SUSY.N1.conjChiralCovector`**, a def, [line 328](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Basic.lean#L328).

> Conjugation of a holomorphic covector, normalized to the anti-holomorphic covector colour
> list `![antiDown]`.

```lean
def conjChiralCovector
    (t : (chiralTensor (ι := ι)).Tensor ![chiralDown]) :
    (chiralTensor (ι := ι)).Tensor ![antiDown]
```

**`SUSY.N1.toScalar_conjScalar`**, a lemma, [line 337](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Basic.lean#L337).

> For scalar tensors, `toScalar` of the normalized tensor conjugate is the complex conjugate of
> `toScalar`.

```lean
lemma toScalar_conjScalar (t : (chiralTensor (ι := ι)).Tensor ![]) :
    (conjScalar t).toScalar = star t.toScalar
```

**`SUSY.N1.repr_conjChiralCovector`**, a lemma, [line 350](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Basic.lean#L350).

> Component formula for the holomorphic covector conjugate: the `![I]` basis component of
> `conjChiralCovector t` is the complex conjugate of the `![I]` component of `t`.

```lean
lemma repr_conjChiralCovector
    (t : (chiralTensor (ι := ι)).Tensor ![chiralDown]) (I : ι) :
    (basis (S := (chiralTensor (ι := ι)).toTensorSpecies) ![antiDown]).repr
        (conjChiralCovector t) ![I] =
      star ((basis (S := (chiralTensor (ι := ι)).toTensorSpecies) ![chiralDown]).repr t ![I])
```

**`SUSY.N1.conjChiralCovector_add`**, a lemma, [line 368](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Basic.lean#L368).

> Conjugation of a holomorphic covector is additive.

```lean
lemma conjChiralCovector_add
    (t₁ t₂ : (chiralTensor (ι := ι)).Tensor ![chiralDown]) :
    conjChiralCovector (t₁ + t₂) = conjChiralCovector t₁ + conjChiralCovector t₂
```

**`SUSY.N1.conjChiralCovector_smul`**, a lemma, [line 376](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Basic.lean#L376).

> Conjugation of a holomorphic covector is conjugate-linear: a scalar `r` pulls out as
> `star r`.

```lean
lemma conjChiralCovector_smul (r : ℂ)
    (t : (chiralTensor (ι := ι)).Tensor ![chiralDown]) :
    conjChiralCovector (r • t) = star r • conjChiralCovector t
```

## Depends on

- [Conjugation structure on a tensor species](../../../relativity/tensors/part-02/conjugation-basic.md)

## Sources

- [Physlib/Particles/SuperSymmetry/N1/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/N1/Basic.lean)
