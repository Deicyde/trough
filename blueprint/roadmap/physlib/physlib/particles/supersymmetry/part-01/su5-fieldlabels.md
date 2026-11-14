---
declaration: module
origin: cited
lean: SuperSymmetry.SU5.FieldLabel, SuperSymmetry.SU5.FieldLabel.RParity
statement: formalized
proof: formalized
---

# The field labels

The module `Physlib.Particles.SuperSymmetry.SU5.FieldLabels`, [Physlib/Particles/SuperSymmetry/SU5/FieldLabels.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/FieldLabels.lean): 3 declarations (1 instance with no name), 2 with a docstring.

## i. Overview

> To each field and it's conjugate in the `SU(5)` SUSY GUT we assign a label,
> namely an element of the inductive type `FieldLabel`.
>
> This field label will be used to specify the representations of fields present in
> terms of the lagrangian.

## ii. Key results

> The key results are
> - `FieldLabel` : the inductive type of field labels.
> - `FieldLabel.RParity` : the R-parity of a field label, being `1` if it is in
>   the non-trivial representation and `0` otherwise.

## iv. References

> * None.

## A. The field labels

> The inductive type `FieldLabel` is defined, with one constructor for each field
> and it's conjugate present in the `SU(5)` SUSY GUT.
>
> Note that there is only one `10` representation, as it is self-conjugate.

**`SuperSymmetry.SU5.FieldLabel`**, an inductive, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/FieldLabels.lean#L56).

> The types of field present in an SU(5) GUT.

```lean
inductive FieldLabel
  | fiveBarHu
  | fiveHu
  | fiveBarHd
  | fiveHd
  | fiveBarMatter
  | fiveMatter
  | tenMatter
deriving DecidableEq
```

**An instance with no name**, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/FieldLabels.lean#L66).

```lean
instance : Fintype FieldLabel
```

## B. R-parity of a field label

> We define the R-parity of a field label, being `1` if it is in the non-trivial
> representation and `0` otherwise.

**`SuperSymmetry.SU5.FieldLabel.RParity`**, a def, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/FieldLabels.lean#L81).

> The R-Parity of a field, landing on `1` if it is in the non-trivial representation
> and `0` otherwise.

```lean
def FieldLabel.RParity : FieldLabel → Fin 2
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Particles/SuperSymmetry/SU5/FieldLabels.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/FieldLabels.lean)
