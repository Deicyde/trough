---
declaration: module
origin: cited
lean: CondensedMatter.QuasiLocal.quantumNet, CondensedMatter.QuasiLocal.CAlg, CondensedMatter.QuasiLocal.classicalIncl, CondensedMatter.QuasiLocal.classicalNet, CondensedMatter.QuasiLocal.diagonalInclusion, CondensedMatter.QuasiLocal.diagonalInclusion_incl
statement: formalized
proof: formalized
---

# The quantum and classical nets of a system with finite site spaces

The module `PhyslibAlpha.CondensedMatter.QuasiLocal.Instances`, [PhyslibAlpha/CondensedMatter/QuasiLocal/Instances.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Instances.lean): 6 declarations, 6 with a docstring.

> The two nets of algebras over a set of sites with finite configuration spaces: operators and
> functions.

## i. Overview

> For sites `s` carrying finite sets `Ω s`, the quantum net assigns to a region the matrices on its
> configurations, with the inclusions `M ↦ M ⊗ 1`. The classical net assigns to a region the complex
> functions on its configurations, which are the diagonal operators, with the inclusions
> `f ↦ f ∘ restr`: a function of the values in `X` is a function of the values in `Y ⊇ X`. Both
> satisfy the axioms of a net, and the classical net sits in the quantum net as diagonal matrices.
> Both have a quasi-local algebra by the construction on any net.
>
> The inclusions are injective as soon as every site space is nonempty.

## ii. Key results

> - `quantumNet` : the net of operators.
> - `classicalNet` : the net of functions of configurations.
> - `diagonalInclusion` : the classical algebra of a region as diagonal operators.
> - `diagonalInclusion_incl` : the classical net is a subnet of the quantum net.

## iv. References

> * O. Bratteli & D. Robinson, Operator Algebras and Quantum Statistical Mechanics 2,
>   Section 6.1.

## A. The quantum net

**`CondensedMatter.QuasiLocal.quantumNet`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Instances.lean#L67).

> **The quantum net**: the matrices on the configurations of each region, with `M ↦ M ⊗ 1` as
> inclusion.

```lean
def quantumNet : AlgebraNet S
```

## B. The classical net

**`CondensedMatter.QuasiLocal.CAlg`**, an abbrev, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Instances.lean#L76).

> The classical algebra of a region: the complex functions on its configurations.

```lean
abbrev CAlg (X : Finset S) : Type _
```

**`CondensedMatter.QuasiLocal.classicalIncl`**, a def, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Instances.lean#L79).

> A function of the values in `X` is a function of the values in a larger region `Y`.

```lean
def classicalIncl {X Y : Finset S} (h : X ≤ Y) : CAlg Ω X →⋆ₐ[ℂ] CAlg Ω Y
```

**`CondensedMatter.QuasiLocal.classicalNet`**, a def, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Instances.lean#L89).

> **The classical net**: the functions on the configurations of each region.

```lean
def classicalNet : AlgebraNet S
```

**`CondensedMatter.QuasiLocal.diagonalInclusion`**, a def, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Instances.lean#L96).

> The classical algebra of a region as the diagonal operators.

```lean
def diagonalInclusion (X : Finset S) : CAlg Ω X →⋆ₐ[ℂ] Alg Ω X
```

**`CondensedMatter.QuasiLocal.diagonalInclusion_incl`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Instances.lean#L114).

> **The classical net is a subnet of the quantum net**: the diagonal inclusion commutes with the
> inclusions of regions.

```lean
lemma diagonalInclusion_incl {X Y : Finset S} (h : X ≤ Y) (f : CAlg Ω X) :
    inclMat h (diagonalInclusion Ω X f) = diagonalInclusion Ω Y (classicalIncl Ω h f)
```

## Depends on

- [Local algebras of a system with a finite configuration space at each site](local.md)
- [Nets of algebras over the finite regions of a lattice and their quasi-local algebra](../../probabilistictheory/quasilocal/algebranet.md)

## Sources

- [PhyslibAlpha/CondensedMatter/QuasiLocal/Instances.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Instances.lean)
