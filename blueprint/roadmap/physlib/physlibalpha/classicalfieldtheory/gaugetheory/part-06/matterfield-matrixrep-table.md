---
declaration: module
origin: cited
lean: LocalGaugeData.SURep, LocalGaugeData.SURep.dim, LocalGaugeData.SURep.rep, LocalGaugeData.Factor.Charge, LocalGaugeData.Charges, LocalGaugeData.IdxOfDims, LocalGaugeData.IdxOfDims.fintype, LocalGaugeData.IdxOfDims.decidableEq
statement: formalized
proof: formalized
---

# Model tables

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.MatrixRep.Table`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean): 68 declarations (4 instances with no name), 48 with a docstring.

## i. Overview

> A gauge-theory model is written down, as in a model-building tool, as a *table*: the gauge
> group as a list of factors, and for each field its number of generations, its Lorentz
> label and one charge per factor — an integer charge under a `U(1)` factor, a
> representation label under an `SU(n)` factor.
>
> This file defines the tables over any local gauge data and compiles them into the general
> theory. A gauge group is a list of `Factor`s of the local gauge data
> (`PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalGaugeData.Factor`); the charges of a field
> form the tuple `Charges Γ` over the list; the charges name a matrix representation
> `Charges.rep`, assembled from the factors by the hypercharge twist and the Kronecker
> product; a field is its Lorentz label and its charges,
> `MatterFieldData Γ`, so that it reads `(.L, .singlet, .fund, -3)`, and compiles to a
> `MatterField`; the field data of a model, `FieldData Γ Fields`, assigns each field its
> number of generations and its data, and compiles to a `GaugeFieldData`.

## ii. Key results

> - `SURep`, `Charges` : the charge labels of a row and the charge tuple.
> - `Charges.rep` : the matrix representation named by a charge tuple.
> - `LorentzLabel`, `MatterFieldData` : the Lorentz label and the data of a field.
> - `LorentzLabel.statistic` : the statistics a table row declares for a label, by convention
>   fermionic for a Weyl spinor and bosonic for a scalar.
> - `MatterFieldData.toMatterField`, `toMatterFieldOn` : the matter field of a datum, on the
>   tensor-product target space or on any target space presented as one.
> - `FieldData`, `FieldData.toGaugeFieldData` : the field data of a model and its compilation.
> - `FieldData.toGaugeFieldData_gaugeLorentzCompatible` : the field content of a model
>   satisfies `GaugeFieldData.GaugeLorentzCompatible`.

## iv. References

> * None.

## A. Charge labels

**`LocalGaugeData.SURep`**, an inductive, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L73).

> **A representation label under `SU(n)`.**

```lean
inductive SURep
  /-- The singlet `1`. -/
  | singlet
  /-- The fundamental `n`. -/
  | fund
  /-- The antifundamental `n̄`. -/
  | antifund
  deriving DecidableEq, Repr
```

**`LocalGaugeData.SURep.dim`**, an abbrev, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L83).

> The dimension of the representation of `SU(n)` a label names.

```lean
abbrev SURep.dim (n : ℕ) : SURep → ℕ
```

**`LocalGaugeData.SURep.rep`**, a def, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L91).

> The matrix representation of an `SU(n)` factor named by a label.

```lean
noncomputable def SURep.rep {n : ℕ} (F : SUFactor jets (Fin n)) :
    (r : SURep) → MatrixRep jets (Fin (r.dim n))
```

**`LocalGaugeData.Factor.Charge`**, an abbrev, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L99).

> The charge a field carries under a factor: an integer under `U(1)`, a representation
> label under `SU(n)`.

```lean
abbrev Factor.Charge : Factor jets → Type
```

## B. Charge tuples and their internal index

**`LocalGaugeData.Charges`**, an abbrev, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L111).

> **The charge tuple** of a row: one charge per factor, as a nested pair so that a row
> reads `(1, .fund, .fund)`.

```lean
abbrev Charges : Factors jets → Type
```

**`LocalGaugeData.IdxOfDims`**, an abbrev, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L118).

> **The internal index of a list of dimensions**: the product of the `Fin n` over the
> list, with `Fin 1` for the empty list and no trailing factor for a one-element list.

```lean
abbrev IdxOfDims : List ℕ → Type
```

**`LocalGaugeData.IdxOfDims.fintype`**, a def, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L125).

> The index of a list of dimensions is finite.

```lean
def IdxOfDims.fintype : (ds : List ℕ) → Fintype (IdxOfDims ds)
```

**`LocalGaugeData.IdxOfDims.decidableEq`**, a def, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L134).

> The index of a list of dimensions has decidable equality.

```lean
def IdxOfDims.decidableEq : (ds : List ℕ) → DecidableEq (IdxOfDims ds)
```

**An instance with no name**, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L141).

```lean
instance (ds : List ℕ) : Fintype (IdxOfDims ds)
```

**An instance with no name**, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L143).

```lean
instance (ds : List ℕ) : DecidableEq (IdxOfDims ds)
```

**`LocalGaugeData.SURep.dims`**, an abbrev, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L147).

> The dimensions an `SU(n)` label contributes to the internal index: none for the
> singlet, `n` for the fundamental and the antifundamental.

```lean
abbrev SURep.dims (n : ℕ) : SURep → List ℕ
```

**`LocalGaugeData.Charges.dims`**, an abbrev, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L156).

> **The dimensions of the internal index** of a charge tuple: the sizes of the
> nontrivial `SU(n)` representations it names, in the order of the factors. `U(1)` factors
> and singlets contribute nothing, so that a field charged under a single `SU(n)` factor is
> indexed by `Fin n` alone.

```lean
abbrev Charges.dims : (Γ : Factors jets) → Charges Γ → List ℕ
```

**`LocalGaugeData.Idx`**, an abbrev, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L165).

> **The internal index** of a field with the given charges: the product of the
> nontrivial `SU(n)`-representation indices.

```lean
abbrev Idx (Γ : Factors jets) (c : Charges Γ) : Type
```

## C. The representation named by a charge tuple

> The representation is assembled in two steps. The `SU(n)` labels give a Kronecker product
> of fundamental and antifundamental representations over the nontrivial dimensions,
> `Charges.suRep`, in which a singlet contributes no factor and the trivial representation is
> dropped rather than tensored in; the `U(1)` charges then twist the result, `Charges.twist`.

**`LocalGaugeData.MatrixRep.kronDims`**, a def, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L180).

> The Kronecker product with the representation on the remaining dimensions, with the
> trivial representation dropped when there are none.

```lean
noncomputable def MatrixRep.kronDims {n : ℕ} (R₁ : MatrixRep jets (Fin n)) :
    (ds : List ℕ) → MatrixRep jets (IdxOfDims ds) → MatrixRep jets (IdxOfDims (n :: ds))
```

**`LocalGaugeData.SURep.repDims`**, a def, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L187).

> The matrix representation of an `SU(n)` factor named by a label, on the index of the
> dimensions the label contributes.

```lean
noncomputable def SURep.repDims {n : ℕ} (F : SUFactor jets (Fin n)) :
    (r : SURep) → MatrixRep jets (IdxOfDims (r.dims n))
```

**`LocalGaugeData.Charges.suRep`**, a def, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L195).

> The `SU(n)` part of the representation named by a charge tuple: the Kronecker product
> of the nontrivial representations the labels name.

```lean
noncomputable def Charges.suRep :
    (Γ : Factors jets) → (c : Charges Γ) → MatrixRep jets (IdxOfDims (Charges.dims Γ c))
```

**`LocalGaugeData.Charges.twist`**, a def, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L207).

> The `U(1)` part of the representation named by a charge tuple: the charge twists of
> all the `U(1)` factors, applied to a given representation.

```lean
noncomputable def Charges.twist {ι : Type} [Fintype ι] [DecidableEq ι] :
    (Γ : Factors jets) → Charges Γ → MatrixRep jets ι → MatrixRep jets ι
```

**`LocalGaugeData.Charges.rep`**, a def, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L218).

> **The matrix representation named by a charge tuple**: the Kronecker product of the
> nontrivial `SU(n)` representations the labels name, twisted by the charge powers of the
> `U(1)` jets.

```lean
noncomputable def Charges.rep (Γ : Factors jets) (c : Charges Γ) : MatrixRep jets (Idx Γ c)
```

## D. Matter field data and its matter field

> A field of a model is written down as its Lorentz label and its charge tuple, so that
> `(.L, .singlet, .fund, -3)` is a left-handed doublet of hypercharge `-3`. The datum
> compiles to a `MatterField` on the target space `S ⊗ (Idx → ℂ)` of the label's Lorentz
> factor and the internal index of the charges, or, through an identification `e`, on any
> target space presented as such a tensor product. The label also gives the field its mass
> weight and its declared statistics.

**`LocalGaugeData.LorentzLabel`**, an inductive, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L235).

> **The Lorentz label of a field**: a left- or right-handed Weyl spinor or a scalar.

```lean
inductive LorentzLabel
  /-- A left-handed Weyl spinor. -/
  | L
  /-- A right-handed Weyl spinor. -/
  | R
  /-- A Lorentz scalar. -/
  | scalar
  deriving DecidableEq, Repr
```

**`LocalGaugeData.LorentzLabel.statistic`**, a def, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L249).

> The statistics a table row declares for a field with the given label, fermionic for a
> Weyl spinor and bosonic for a scalar. Like `massWeight`, it is a convention of the tables,
> chosen to match the spin–statistics relation.

```lean
def statistic : LorentzLabel → FieldStatistic
```

**`LocalGaugeData.LorentzLabel.Space`**, an abbrev, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L255).

> The Lorentz factor of the target space of a field with the given label.

```lean
abbrev Space : LorentzLabel → Type
```

**An instance with no name**, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L260).

```lean
instance : Module.Finite ℂ Fermion.LeftHandedWeyl
```

**An instance with no name**, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L263).

```lean
instance : Module.Finite ℂ Fermion.RightHandedWeyl
```

**`LocalGaugeData.LorentzLabel.instAddCommGroupSpace`**, an instance, [line 266](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L266).

```lean
instance instAddCommGroupSpace : (l : LorentzLabel) → AddCommGroup l.Space
```

**`LocalGaugeData.LorentzLabel.instModuleSpace`**, an instance, [line 271](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L271).

```lean
instance instModuleSpace : (l : LorentzLabel) → Module ℂ l.Space
```

**`LocalGaugeData.LorentzLabel.instFreeSpace`**, an instance, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L276).

```lean
instance instFreeSpace : (l : LorentzLabel) → Module.Free ℂ l.Space
```

**`LocalGaugeData.LorentzLabel.instFiniteSpace`**, an instance, [line 281](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L281).

```lean
instance instFiniteSpace : (l : LorentzLabel) → Module.Finite ℂ l.Space
```

**`LocalGaugeData.LorentzLabel.rep`**, a def, [line 287](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L287).

> The representation of the Lorentz group on the Lorentz factor of a label.

```lean
noncomputable def rep : (l : LorentzLabel) → Representation ℂ SL(2,ℂ) l.Space
```

**`LocalGaugeData.LorentzLabel.massWeight`**, a def, [line 294](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L294).

> The mass weight of a field with the given label, in the units in which a derivative
> has weight `2`: `3` for a Weyl spinor, `2` for a scalar.

```lean
def massWeight : LorentzLabel → ℕ
```

**`LocalGaugeData.LorentzLabel.basisIndex`**, an abbrev, [line 301](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L301).

> The index of the basis of the Lorentz factor of a label: the two spinor components of
> a Weyl spinor, one component for a scalar.

```lean
abbrev basisIndex : LorentzLabel → Type
```

**`LocalGaugeData.LorentzLabel.instFintypeBasisIndex`**, an instance, [line 306](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L306).

```lean
instance instFintypeBasisIndex : (l : LorentzLabel) → Fintype l.basisIndex
```

**`LocalGaugeData.LorentzLabel.instDecidableEqBasisIndex`**, an instance, [line 311](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L311).

```lean
instance instDecidableEqBasisIndex : (l : LorentzLabel) → DecidableEq l.basisIndex
```

**`LocalGaugeData.LorentzLabel.basis`**, a def, [line 317](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L317).

> The basis of the Lorentz factor of a label: the Weyl basis, or `1` for a scalar.

```lean
noncomputable def basis : (l : LorentzLabel) → Module.Basis l.basisIndex ℂ l.Space
```

**`LocalGaugeData.MatterFieldData`**, an abbrev, [line 326](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L326).

> **The data of a matter field**: its Lorentz label and its charge tuple, so that a
> field reads `(.L, .singlet, .fund, -3)`.

```lean
abbrev MatterFieldData (Γ : Factors jets) : Type
```

**`LocalGaugeData.MatterFieldData.lorentz`**, an abbrev, [line 333](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L333).

> The Lorentz label of the field.

```lean
abbrev lorentz : LorentzLabel
```

**`LocalGaugeData.MatterFieldData.charges`**, an abbrev, [line 336](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L336).

> The charges of the field.

```lean
abbrev charges : Charges Γ
```

**`LocalGaugeData.MatterFieldData.Idx`**, an abbrev, [line 339](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L339).

> The internal index of the field.

```lean
abbrev Idx : Type
```

**`LocalGaugeData.MatterFieldData.rep`**, an abbrev, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L342).

> The matrix representation named by the charges of the field.

```lean
noncomputable abbrev rep : MatrixRep jets M.Idx
```

**`LocalGaugeData.MatterFieldData.massWeight`**, an abbrev, [line 345](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L345).

> The mass weight of the field.

```lean
abbrev massWeight : ℕ
```

**`LocalGaugeData.MatterFieldData.V`**, an abbrev, [line 349](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L349).

> **The target space of the field**: the Lorentz factor of its label tensored with the
> functions on its internal index.

```lean
abbrev V : Type
```

**`LocalGaugeData.MatterFieldData.basis`**, a def, [line 353](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L353).

> **The basis of the target space**: the basis of the Lorentz factor tensored with the
> coordinate basis of the internal index.

```lean
noncomputable def basis : Module.Basis (M.lorentz.basisIndex × M.Idx) ℂ M.V
```

**`LocalGaugeData.MatterFieldData.basis_apply`**, a lemma, [line 359](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L359).

> A basis vector of the target space is a basis vector of the Lorentz factor tensored with
> a coordinate vector of the internal index.

```lean
lemma basis_apply (a : M.lorentz.basisIndex) (i : M.Idx) :
    M.basis (a, i) = M.lorentz.basis a ⊗ₜ Pi.single i 1
```

**`LocalGaugeData.MatterFieldData.toMatterFieldOn`**, a def, [line 367](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L367).

> **The matter field of a datum on a presented target space**: a target space `V`
> identified with the Lorentz factor of the label tensored with the internal index of the
> charges, transforming in the representation the charges name, with the mass weight and
> statistic its label assigns.

```lean
noncomputable def toMatterFieldOn {V : Type} [AddCommGroup V] [Module ℂ V]
    [Module.Free ℂ V] [Module.Finite ℂ V]
    (e : V ≃ₗ[ℂ] M.lorentz.Space ⊗[ℂ] (M.Idx → ℂ)) : MatterField jets
```

**`LocalGaugeData.MatterFieldData.toMatterField`**, a def, [line 374](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L374).

> **The matter field of a datum**: the target space is the Lorentz factor of the label
> tensored with the internal index of the charges.

```lean
noncomputable def toMatterField : MatterField jets
```

**`LocalGaugeData.MatterFieldData.toMatterFieldOn_V`**, a lemma, [line 381](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L381).

```lean
lemma toMatterFieldOn_V : (M.toMatterFieldOn e).V = V
```

**`LocalGaugeData.MatterFieldData.toMatterFieldOn_repJet`**, a lemma, [line 384](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L384).

```lean
lemma toMatterFieldOn_repJet : (M.toMatterFieldOn e).repJet = M.rep.repJet e
```

**`LocalGaugeData.MatterFieldData.toMatterFieldOn_repAlgebra`**, a lemma, [line 387](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L387).

```lean
lemma toMatterFieldOn_repAlgebra : (M.toMatterFieldOn e).repAlgebra = M.rep.repAlgebra e
```

**`LocalGaugeData.MatterFieldData.toMatterFieldOn_repLorentz`**, a lemma, [line 391](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L391).

```lean
lemma toMatterFieldOn_repLorentz :
    (M.toMatterFieldOn e).repLorentz = MatrixRep.repLorentz e M.lorentz.rep
```

**`LocalGaugeData.MatterFieldData.toMatterFieldOn_massWeight`**, a lemma, [line 395](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L395).

```lean
lemma toMatterFieldOn_massWeight : (M.toMatterFieldOn e).massWeight = M.massWeight
```

**`LocalGaugeData.MatterFieldData.toMatterField_massWeight`**, a lemma, [line 398](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L398).

```lean
lemma toMatterField_massWeight : M.toMatterField.massWeight = M.massWeight
```

**`LocalGaugeData.MatterFieldData.toMatterFieldOn_statistic`**, a lemma, [line 403](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L403).

> The matter field of a datum on a presented target space has the statistics its Lorentz
> label assigns.

```lean
lemma toMatterFieldOn_statistic : (M.toMatterFieldOn e).statistic = M.lorentz.statistic
```

**`LocalGaugeData.MatterFieldData.toMatterField_statistic`**, a lemma, [line 407](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L407).

> The matter field of a datum has the statistics its Lorentz label assigns.

```lean
lemma toMatterField_statistic : M.toMatterField.statistic = M.lorentz.statistic
```

**`LocalGaugeData.MatterFieldData.toMatterField_V`**, a lemma, [line 411](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L411).

> The target space of the matter field of a datum is the target space of the datum.

```lean
lemma toMatterField_V : M.toMatterField.V = M.V
```

**`LocalGaugeData.MatterFieldData.toMatterFieldOn_gaugeLorentzCompatible`**, a lemma, [line 414](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L414).

> The gauge and Lorentz actions of the matter field of a datum commute.

```lean
lemma toMatterFieldOn_gaugeLorentzCompatible :
    (M.toMatterFieldOn e).GaugeLorentzCompatible
```

**`LocalGaugeData.MatterFieldData.toMatterField_gaugeLorentzCompatible`**, a lemma, [line 419](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L419).

> The gauge and Lorentz actions of the matter field of a datum commute.

```lean
lemma toMatterField_gaugeLorentzCompatible : M.toMatterField.GaugeLorentzCompatible
```

## E. The field data of a model and its field content

**`LocalGaugeData.FieldData`**, an abbrev, [line 432](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L432).

> **The field data of a model**: for each field of the model, its number of generations
> and its matter field data.

```lean
abbrev FieldData (Γ : Factors jets) (Fields : Type) : Type
```

**`LocalGaugeData.FieldData.generations`**, an abbrev, [line 440](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L440).

> The number of generations of a field.

```lean
abbrev generations (f : Fields) : ℕ
```

**`LocalGaugeData.FieldData.data`**, an abbrev, [line 443](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L443).

> The matter field data of a field.

```lean
abbrev data (f : Fields) : MatterFieldData Γ
```

**`LocalGaugeData.FieldData.Fermions`**, an abbrev, [line 446](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L446).

> The fermionic fields of the model: those whose label assigns fermionic statistics.

```lean
abbrev Fermions : Type
```

**`LocalGaugeData.FieldData.Bosons`**, an abbrev, [line 449](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L449).

> The bosonic fields of the model: those whose label assigns bosonic statistics.

```lean
abbrev Bosons : Type
```

**`LocalGaugeData.FieldData.FermionSpecies`**, an abbrev, [line 452](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L452).

> The fermionic species of the model: a fermionic field together with a generation.

```lean
abbrev FermionSpecies : Type
```

**`LocalGaugeData.FieldData.BosonSpecies`**, an abbrev, [line 455](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L455).

> The bosonic species of the model: a bosonic field together with a generation.

```lean
abbrev BosonSpecies : Type
```

**`LocalGaugeData.FieldData.toGaugeFieldData`**, a def, [line 459](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L459).

> **The field content of a model**: one matter field per species, the matter field of the
> species' data.

```lean
noncomputable def toGaugeFieldData : GaugeFieldData jets
```

**`LocalGaugeData.FieldData.toGaugeFieldData_FermionSpecies`**, a lemma, [line 468](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L468).

```lean
lemma toGaugeFieldData_FermionSpecies :
    D.toGaugeFieldData.FermionSpecies = D.FermionSpecies
```

**`LocalGaugeData.FieldData.toGaugeFieldData_fermion`**, a lemma, [line 472](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L472).

```lean
lemma toGaugeFieldData_fermion (s : D.FermionSpecies) :
    D.toGaugeFieldData.fermion s = (D.data s.1.1).toMatterField
```

**`LocalGaugeData.FieldData.toGaugeFieldData_BosonSpecies`**, a lemma, [line 476](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L476).

```lean
lemma toGaugeFieldData_BosonSpecies : D.toGaugeFieldData.BosonSpecies = D.BosonSpecies
```

**`LocalGaugeData.FieldData.toGaugeFieldData_boson`**, a lemma, [line 479](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L479).

```lean
lemma toGaugeFieldData_boson (s : D.BosonSpecies) :
    D.toGaugeFieldData.boson s = (D.data s.1.1).toMatterField
```

**`LocalGaugeData.FieldData.toGaugeFieldData_gaugeLorentzCompatible`**, a lemma, [line 485](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean#L485).

> The field content of a model satisfies `GaugeFieldData.GaugeLorentzCompatible`: every
> species is a matrix representation on the internal index tensored with a Lorentz
> factor.

```lean
lemma toGaugeFieldData_gaugeLorentzCompatible : D.toGaugeFieldData.GaugeLorentzCompatible
```

## Depends on

- [Left handed Weyl fermions](../../../../physlib/relativity/fermions/weyl/lefthanded.md)
- [Right handed Weyl fermions](../../../../physlib/relativity/fermions/weyl/righthanded.md)
- [The field data of a gauge theory](../part-02/gaugefielddata-basic.md)
- [Constructions of matrix representations](matterfield-matrixrep-constructions.md)
- [The factors of a gauge group as matrix representations](matterfield-matrixrep-factors.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Table.lean)
