---
declaration: module
origin: cited
lean: Fermion.Dirac.IsCliffordFamily, Fermion.Dirac.IsCliffordFamily.mul_self, Fermion.Dirac.IsCliffordFamily.mul_comm_of_ne, Fermion.Dirac.IsCliffordFamily.det_ne_zero, Fermion.Dirac.IsCliffordFamily.even, Fermion.Dirac.IsCliffordFamily.involutions, Fermion.Dirac.IsCliffordFamily.involutions_anticomm, Fermion.Dirac.IsCliffordFamily.ne_two
statement: formalized
proof: formalized
---

# The gamma matrices need four dimensions

The module `PhyslibAlpha.Relativity.Fermions.Dirac.MinimalDimension`, [PhyslibAlpha/Relativity/Fermions/Dirac/MinimalDimension.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Fermions/Dirac/MinimalDimension.lean): 11 declarations, 8 with a docstring.

## i. Overview

> A Clifford family is a choice of `n × n` complex matrices `γ^μ`, one for each Lorentz index,
> with `γ^μ γ^ν + γ^ν γ^μ = 2 η^{μν} 1`. Dirac (1928) found one with `n = 4`, and no smaller
> size works. Each `γ^μ` squares to `± 1`, so it is invertible, and `γ^0 γ^1 = -γ^1 γ^0` forces
> `det (γ^0 γ^1) = (-1)ⁿ det (γ^0 γ^1)`: the size is even. Size two is excluded by the three
> Pauli matrices: `γ^0, i γ^1, i γ^2, i γ^3` would be four anticommuting `2 × 2` involutions, and
> `2 × 2` holds at most three. The Dirac endomorphisms `gamma` of Physlib, written as `4 × 4`
> matrices, attain the bound.

## ii. Key results

> - `IsCliffordFamily` : the relation `γ^μ γ^ν + γ^ν γ^μ = 2 η^{μν} 1`.
> - `IsCliffordFamily.even` : a Clifford family has even size.
> - `IsCliffordFamily.ne_two` : there are no `2 × 2` Clifford families.
> - `IsCliffordFamily.four_le` : a nonempty Clifford family has size at least four.
> - `isCliffordFamily_gamma` : the Dirac gamma matrices are a Clifford family.
> - `isLeast_size_isCliffordFamily` : the smallest size of a Clifford family is four.

## iv. References

> * P. A. M. Dirac, *The quantum theory of the electron*, Proc. R. Soc. London A 117 (1928)
>   610–624.

## A. Clifford families

**`Fermion.Dirac.IsCliffordFamily`**, a def, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Fermions/Dirac/MinimalDimension.lean#L60).

> A family of `n × n` matrices with `γ^μ γ^ν + γ^ν γ^μ = 2 η^{μν} 1`.

```lean
def IsCliffordFamily {n : ℕ} (γ : Fin 1 ⊕ Fin 3 → Matrix (Fin n) (Fin n) ℂ) : Prop
```

**`Fermion.Dirac.IsCliffordFamily.mul_self`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Fermions/Dirac/MinimalDimension.lean#L68).

```lean
lemma mul_self (μ : Fin 1 ⊕ Fin 3) : γ μ * γ μ = (minkowskiMatrix μ μ : ℂ) • 1
```

**`Fermion.Dirac.IsCliffordFamily.mul_comm_of_ne`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Fermions/Dirac/MinimalDimension.lean#L73).

```lean
lemma mul_comm_of_ne {μ ν : Fin 1 ⊕ Fin 3} (h : μ ≠ ν) : γ ν * γ μ = -(γ μ * γ ν)
```

**`Fermion.Dirac.IsCliffordFamily.det_ne_zero`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Fermions/Dirac/MinimalDimension.lean#L79).

> Each member squares to `± 1`, so it is invertible.

```lean
lemma det_ne_zero (μ : Fin 1 ⊕ Fin 3) : (γ μ).det ≠ 0
```

## B. The size is even

**`Fermion.Dirac.IsCliffordFamily.even`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Fermions/Dirac/MinimalDimension.lean#L97).

> **A Clifford family has even size.**

```lean
lemma even : Even n
```

## C. Size two is excluded

**`Fermion.Dirac.IsCliffordFamily.involutions`**, a def, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Fermions/Dirac/MinimalDimension.lean#L114).

> `γ^0, i γ^1, i γ^2, i γ^3`: four involutions that anticommute.

```lean
noncomputable def involutions (γ : Fin 1 ⊕ Fin 3 → Matrix (Fin n) (Fin n) ℂ)
    (μ : Fin 1 ⊕ Fin 3) : Matrix (Fin n) (Fin n) ℂ
```

**`Fermion.Dirac.IsCliffordFamily.involutions_anticomm`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Fermions/Dirac/MinimalDimension.lean#L119).

```lean
lemma involutions_anticomm (μ ν : Fin 1 ⊕ Fin 3) :
    involutions γ μ * involutions γ ν + involutions γ ν * involutions γ μ =
      (Sum.elim (fun _ => (1 : ℂ)) (fun _ => I) μ * Sum.elim (fun _ => (1 : ℂ)) (fun _ => I) ν) •
        (γ μ * γ ν + γ ν * γ μ)
```

**`Fermion.Dirac.IsCliffordFamily.ne_two`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Fermions/Dirac/MinimalDimension.lean#L127).

> **There are no `2 × 2` Clifford families**: they would give four anticommuting `2 × 2`
> involutions.

```lean
lemma ne_two : n ≠ 2
```

**`Fermion.Dirac.IsCliffordFamily.four_le`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Fermions/Dirac/MinimalDimension.lean#L145).

> **A nonempty Clifford family has size at least four.**

```lean
lemma four_le (hn : n ≠ 0) : 4 ≤ n
```

## D. Dirac's matrices attain the bound

**`Fermion.Dirac.isCliffordFamily_gamma`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Fermions/Dirac/MinimalDimension.lean#L159).

> The Dirac gamma matrices, written as `4 × 4` matrices, are a Clifford family.

```lean
lemma isCliffordFamily_gamma : IsCliffordFamily fun μ => endEquivMatrix (gamma μ)
```

**`Fermion.Dirac.isLeast_size_isCliffordFamily`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Fermions/Dirac/MinimalDimension.lean#L164).

> **The gamma matrices need four dimensions (Dirac, 1928).** The smallest size of a nonempty
> Clifford family is four.

```lean
lemma isLeast_size_isCliffordFamily :
    IsLeast {n : ℕ | n ≠ 0 ∧ ∃ γ : Fin 1 ⊕ Fin 3 → Matrix (Fin n) (Fin n) ℂ,
      IsCliffordFamily γ} 4
```

## Depends on

- [Gamma endomorphisms of Dirac fermions](../../../physlib/relativity/fermions/dirac/gammamatrices.md)

## Proof depends on

- [Three anticommuting matrices are the most `2 × 2` can hold](../paulimatrices/anticommuting.md)

## Sources

- [PhyslibAlpha/Relativity/Fermions/Dirac/MinimalDimension.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Fermions/Dirac/MinimalDimension.lean)
