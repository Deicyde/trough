---
declaration: module
origin: cited
lean: Fermion.Dirac.Slash.slash, Fermion.Dirac.Slash.slashLinear, Fermion.Dirac.Slash.slashLinear_apply, Fermion.Dirac.Slash.slash_eq_sum, Fermion.Dirac.Slash.slash_zero, Fermion.Dirac.Slash.slash_add, Fermion.Dirac.Slash.slash_smul, Fermion.Dirac.Slash.slashMulLeft
statement: formalized
proof: formalized
---

# The Dirac slash operator

The module `Physlib.Relativity.Fermions.Dirac.Slash`, [Physlib/Relativity/Fermions/Dirac/Slash.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/Slash.lean): 11 declarations, 5 with a docstring.

> This file defines the Dirac slash `k̸ = k_μ γ^μ` of a Lorentz vector, in the Dirac
> representation obtained from the gamma endomorphisms `Fermion.Dirac.gamma` via the change of
> coordinates `Fermion.Dirac.endEquivMatrix`. The slash is the Dirac representation of Clifford
> multiplication `Fermion.Dirac.gammaMatrix`, and so contracts the lowered coordinates of a
> Lorentz vector with the gamma matrices.

## Main Definitions

> - `Slash.slash`: The Dirac slash `k̸ = k_μ γ^μ` of a Lorentz vector
> - `Slash.slashProd`: The product of the Dirac slashes of a list of Lorentz vectors

**`Fermion.Dirac.Slash.slash`**, a def, [line 36](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/Slash.lean#L36).

> The Dirac slash `k̸ = k_μ γ^μ` of a Lorentz vector, in the Dirac representation.
> It is the Dirac representation of Clifford multiplication `Fermion.Dirac.gammaMatrix`,
> and so contracts the lowered coordinates of `k` with the gamma matrices.

```lean
def slash (k : Lorentz.Vector) : Matrix (Fin 4) (Fin 4) ℂ
```

**`Fermion.Dirac.Slash.slashLinear`**, a def, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/Slash.lean#L43).

> The Dirac slash as an `ℝ`-linear map, which it inherits from Clifford multiplication.

```lean
def slashLinear : Lorentz.Vector →ₗ[ℝ] Matrix (Fin 4) (Fin 4) ℂ
```

**`Fermion.Dirac.Slash.slashLinear_apply`**, a lemma, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/Slash.lean#L47).

```lean
lemma slashLinear_apply (k : Lorentz.Vector) : slashLinear k = slash k
```

**`Fermion.Dirac.Slash.slash_eq_sum`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/Slash.lean#L50).

> The Dirac slash contracts the lowered vector coordinates with the gamma matrices.

```lean
lemma slash_eq_sum (k : Lorentz.Vector) :
    slash k = ∑ μ, ((minkowskiMatrix μ μ * k μ : ℝ) : ℂ) • endEquivMatrix (gamma μ)
```

**`Fermion.Dirac.Slash.slash_zero`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/Slash.lean#L56).

```lean
lemma slash_zero : slash (0 : Lorentz.Vector) = 0
```

**`Fermion.Dirac.Slash.slash_add`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/Slash.lean#L60).

```lean
lemma slash_add (k l : Lorentz.Vector) : slash (k + l) = slash k + slash l
```

**`Fermion.Dirac.Slash.slash_smul`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/Slash.lean#L64).

```lean
lemma slash_smul (c : ℝ) (k : Lorentz.Vector) : slash (c • k) = c • slash k
```

**`Fermion.Dirac.Slash.slashMulLeft`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/Slash.lean#L68).

> Left multiplication by a slash matrix as a linear endomorphism.

```lean
def slashMulLeft (k : Lorentz.Vector) :
    Matrix (Fin 4) (Fin 4) ℂ →ₗ[ℂ] Matrix (Fin 4) (Fin 4) ℂ
```

**`Fermion.Dirac.Slash.slashProd`**, a def, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/Slash.lean#L73).

> Product of a list of slash factors, in left-to-right order.

```lean
def slashProd (ks : List Lorentz.Vector) : Matrix (Fin 4) (Fin 4) ℂ
```

**`Fermion.Dirac.Slash.slashProd_nil`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/Slash.lean#L77).

```lean
lemma slashProd_nil : slashProd [] = 1
```

**`Fermion.Dirac.Slash.slashProd_cons`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/Slash.lean#L81).

```lean
lemma slashProd_cons (k : Lorentz.Vector) (ks : List Lorentz.Vector) :
    slashProd (k :: ks) = slash k * slashProd ks
```

## Depends on

- [Gamma endomorphisms of Dirac fermions](gammamatrices.md)

## Sources

- [Physlib/Relativity/Fermions/Dirac/Slash.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/Slash.lean)
