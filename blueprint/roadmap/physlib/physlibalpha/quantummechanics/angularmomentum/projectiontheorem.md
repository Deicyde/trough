---
declaration: module
origin: cited
lean: PhyslibAlpha.Sl2.IsTensorIntertwiner.exists_eq_smul_of_ne_zero, PhyslibAlpha.Sl2.IsTensorOperator.exists_eq_smul_of_ne_zero, PhyslibAlpha.Sl2.sl2Operator, PhyslibAlpha.Sl2.sl2Operator_vNat_zero, PhyslibAlpha.Sl2.sl2Operator_vNat_one, PhyslibAlpha.Sl2.sl2Operator_vNat_two, PhyslibAlpha.Sl2.sl2Operator_vNat_of_lt, PhyslibAlpha.Sl2.ρE_mul_ρF'
statement: formalized
proof: formalized
---

# The projection theorem for vector operators

The module `PhyslibAlpha.QuantumMechanics.AngularMomentum.ProjectionTheorem`, [PhyslibAlpha/QuantumMechanics/AngularMomentum/ProjectionTheorem.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ProjectionTheorem.lean): 19 declarations, 7 with a docstring.

> Tensor operators are unique up to a scalar, and every vector operator on an irreducible
> multiplet is a multiple of the angular momentum itself.

## i. Overview

> By the Wigner–Eckart theorem the tensor operators of rank `k` from `V(m)` to `V(p)` form a space
> of dimension at most one. So if one nonzero tensor operator is known, every other one is a scalar
> multiple of it.
>
> For rank `k = 2` (vector operators, `κ = 1` in physics notation) and `m = p = n` there is a
> canonical nonzero tensor operator: the `sl₂` action itself, `v_0 ↦ e`, `v_1 ↦ -h`, `v_2 ↦ -2f`,
> corresponding to the spherical components of the angular momentum `J`. Hence every vector
> operator `T` on the multiplet `V(n)` satisfies `T = c • J` for a single scalar `c`. This is the
> projection theorem behind the Landé `g`-factor; the usual formula
> `c = ⟨J · V⟩ / (j(j+1))` for the scalar is not part of this file.

## ii. Key results

> - `IsTensorIntertwiner.exists_eq_smul_of_ne_zero` and `IsTensorOperator.exists_eq_smul_of_ne_zero`
>   give uniqueness up to a scalar.
> - `sl2Operator` is the `sl₂` action as a rank-2 tensor operator, see `isTensorOperator_sl2Operator`.
> - `IsTensorOperator.exists_eq_smul_sl2Operator` is the projection theorem.

## iv. References

> - J. J. Sakurai and J. Napolitano, *Modern Quantum Mechanics*, 3rd ed., Cambridge University
>   Press (2020), section 3.11.

## A. Uniqueness up to a scalar

**`PhyslibAlpha.Sl2.IsTensorIntertwiner.exists_eq_smul_of_ne_zero`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ProjectionTheorem.lean#L68).

> Two tensor intertwiners into the same `V(p)` are proportional, provided the second one is
> nonzero.

```lean
lemma IsTensorIntertwiner.exists_eq_smul_of_ne_zero (hmn : 0 < m + n)
    {φ ψ : StandardSl2Module K m ⊗[K] StandardSl2Module K n →ₗ[K] StandardSl2Module K p}
    (hφ : IsTensorIntertwiner φ) (hψ : IsTensorIntertwiner ψ) (hψ0 : ψ ≠ 0) :
    ∃ c : K, φ = c • ψ
```

**`PhyslibAlpha.Sl2.IsTensorOperator.exists_eq_smul_of_ne_zero`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ProjectionTheorem.lean#L85).

> Two tensor operators of rank `k` from `V(m)` to `V(p)` are proportional, provided the second
> one is nonzero.

```lean
lemma IsTensorOperator.exists_eq_smul_of_ne_zero (hkm : 0 < k + m)
    {T S : StandardSl2Module K k →ₗ[K] StandardSl2Module K m →ₗ[K] StandardSl2Module K p}
    (hT : IsTensorOperator T) (hS : IsTensorOperator S) (hS0 : S ≠ 0) :
    ∃ c : K, T = c • S
```

## B. The angular momentum as a vector operator

### B.1. Definition and values

**`PhyslibAlpha.Sl2.sl2Operator`**, a def, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ProjectionTheorem.lean#L112).

> The `sl₂` action on `V(n)` as a tensor operator of rank 2: `v_0 ↦ e`, `v_1 ↦ -h`,
> `v_2 ↦ -2f`. These are the spherical components of the angular momentum, up to normalisation.

```lean
def sl2Operator : StandardSl2Module K 2 →ₗ[K] Module.End K (StandardSl2Module K n)
```

**`PhyslibAlpha.Sl2.sl2Operator_vNat_zero`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ProjectionTheorem.lean#L118).

```lean
lemma sl2Operator_vNat_zero : sl2Operator (K := K) n (vNat 2 0) = ρE
```

**`PhyslibAlpha.Sl2.sl2Operator_vNat_one`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ProjectionTheorem.lean#L122).

```lean
lemma sl2Operator_vNat_one : sl2Operator (K := K) n (vNat 2 1) = (-1 : K) • ρH
```

**`PhyslibAlpha.Sl2.sl2Operator_vNat_two`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ProjectionTheorem.lean#L126).

```lean
lemma sl2Operator_vNat_two : sl2Operator (K := K) n (vNat 2 2) = (-2 : K) • ρF
```

**`PhyslibAlpha.Sl2.sl2Operator_vNat_of_lt`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ProjectionTheorem.lean#L130).

```lean
lemma sl2Operator_vNat_of_lt {l : ℕ} (hl : 2 < l) : sl2Operator (K := K) n (vNat 2 l) = 0
```

### B.2. Commutation relations

**`PhyslibAlpha.Sl2.ρE_mul_ρF'`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ProjectionTheorem.lean#L139).

```lean
lemma ρE_mul_ρF' : (ρE : Module.End K (StandardSl2Module K n)) * ρF = ρF * ρE + ρH
```

**`PhyslibAlpha.Sl2.ρH_mul_ρE'`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ProjectionTheorem.lean#L146).

```lean
lemma ρH_mul_ρE' : (ρH : Module.End K (StandardSl2Module K n)) * ρE = ρE * ρH + (2 : K) • ρE
```

**`PhyslibAlpha.Sl2.ρH_mul_ρF'`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ProjectionTheorem.lean#L153).

```lean
lemma ρH_mul_ρF' : (ρH : Module.End K (StandardSl2Module K n)) * ρF = ρF * ρH - (2 : K) • ρF
```

**`PhyslibAlpha.Sl2.ρE_vNat_two_one`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ProjectionTheorem.lean#L159).

```lean
lemma ρE_vNat_two_one : (ρE : Module.End K (StandardSl2Module K 2)) (vNat 2 1) =
    (2 : K) • vNat 2 0
```

**`PhyslibAlpha.Sl2.ρE_vNat_two_two`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ProjectionTheorem.lean#L164).

```lean
lemma ρE_vNat_two_two : (ρE : Module.End K (StandardSl2Module K 2)) (vNat 2 2) =
    (2 : K) • vNat 2 1
```

**`PhyslibAlpha.Sl2.ρH_vNat_two_zero`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ProjectionTheorem.lean#L170).

```lean
lemma ρH_vNat_two_zero : (ρH : Module.End K (StandardSl2Module K 2)) (vNat 2 0) =
    (2 : K) • vNat 2 0
```

**`PhyslibAlpha.Sl2.ρH_vNat_two_one`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ProjectionTheorem.lean#L176).

```lean
lemma ρH_vNat_two_one : (ρH : Module.End K (StandardSl2Module K 2)) (vNat 2 1) = 0
```

**`PhyslibAlpha.Sl2.ρH_vNat_two_two`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ProjectionTheorem.lean#L181).

```lean
lemma ρH_vNat_two_two : (ρH : Module.End K (StandardSl2Module K 2)) (vNat 2 2) =
    (-2 : K) • vNat 2 2
```

**`PhyslibAlpha.Sl2.comm_of_vNat`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ProjectionTheorem.lean#L189).

> A commutation relation `[Y, A x] = A (X x)` for a linear `A` holds for all `x` once it holds
> on the coordinate vectors.

```lean
lemma comm_of_vNat {X : Module.End K (StandardSl2Module K k)}
    {Y : Module.End K (StandardSl2Module K n)}
    {A : StandardSl2Module K k →ₗ[K] Module.End K (StandardSl2Module K n)}
    (h : ∀ l, Y * A (vNat k l) - A (vNat k l) * Y = A (X (vNat k l)))
    (x : StandardSl2Module K k) :
    Y ∘ₗ A x - A x ∘ₗ Y = A (X x)
```

**`PhyslibAlpha.Sl2.isTensorOperator_sl2Operator`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ProjectionTheorem.lean#L204).

> The `sl₂` action is a tensor operator of rank 2 on every `V(n)`.

```lean
lemma isTensorOperator_sl2Operator : IsTensorOperator (sl2Operator (K := K) n)
```

**`PhyslibAlpha.Sl2.sl2Operator_ne_zero`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ProjectionTheorem.lean#L253).

> On `V(n)` with `n > 0` the `sl₂` action is a nonzero tensor operator.

```lean
lemma sl2Operator_ne_zero (hn : 0 < n) : sl2Operator (K := K) n ≠ 0
```

## C. The projection theorem

**`PhyslibAlpha.Sl2.IsTensorOperator.exists_eq_smul_sl2Operator`**, a lemma, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ProjectionTheorem.lean#L273).

> **Projection theorem.** Every vector operator (tensor operator of rank 2) on the multiplet
> `V(n)` is a scalar multiple of the angular momentum `sl2Operator n`.

```lean
lemma IsTensorOperator.exists_eq_smul_sl2Operator
    {T : StandardSl2Module K 2 →ₗ[K] StandardSl2Module K n →ₗ[K] StandardSl2Module K n}
    (hT : IsTensorOperator T) : ∃ c : K, T = c • sl2Operator n
```

## Depends on

- [The Wigner–Eckart theorem for sl₂](wignereckart.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/AngularMomentum/ProjectionTheorem.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ProjectionTheorem.lean)
