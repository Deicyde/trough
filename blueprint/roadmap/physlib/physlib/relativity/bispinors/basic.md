---
declaration: module
origin: cited
lean: complexLorentzTensor.contrBispinorUp, complexLorentzTensor.contrBispinorDown, complexLorentzTensor.coBispinorUp, complexLorentzTensor.coBispinorDown
statement: formalized
proof: formalized
---

# Physlib.Relativity.Bispinors.Basic

The module `Physlib.Relativity.Bispinors.Basic`, [Physlib/Relativity/Bispinors/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Basic.lean): 4 declarations, 4 with a docstring.

## Bispinors

## Definitions

**`complexLorentzTensor.contrBispinorUp`**, a def, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Basic.lean#L39).

> A bispinor `pᵃᵃ` created from a lorentz vector `p^μ`.

```lean
def contrBispinorUp (p : ℂT[.up]) : ℂT[.upL, .upR]
```

**`complexLorentzTensor.contrBispinorDown`**, a def, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Basic.lean#L43).

> A bispinor `pₐₐ` created from a lorentz vector `p^μ`.

```lean
def contrBispinorDown (p : ℂT[.up]) : ℂT[.downL, .downR]
```

**`complexLorentzTensor.coBispinorUp`**, a def, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Basic.lean#L47).

> A bispinor `pᵃᵃ` created from a lorentz vector `p_μ`.

```lean
def coBispinorUp (p : ℂT[.down]) : ℂT[.upL, .upR]
```

**`complexLorentzTensor.coBispinorDown`**, a def, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Basic.lean#L51).

> A bispinor `pₐₐ` created from a lorentz vector `p_μ`.

```lean
def coBispinorDown (p : ℂT[.down]) : ℂT[.downL, .downR]
```

## Basic equalities.

## Depends on

- [Physlib.Meta.Informal.Basic](../../meta/informal/basic.md)
- [Pauli matrices as a tensor](pauli-totensor.md)

## Sources

- [Physlib/Relativity/Bispinors/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Basic.lean)
