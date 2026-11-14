---
declaration: module
origin: cited
lean: PhyslibAlpha.Sl2.IsTensorOperator, PhyslibAlpha.Sl2.IsTensorOperator.apply_ρE, PhyslibAlpha.Sl2.IsTensorOperator.apply_ρF, PhyslibAlpha.Sl2.IsTensorOperator.apply_ρH, PhyslibAlpha.Sl2.IsTensorOperator.lift_isTensorIntertwiner, PhyslibAlpha.Sl2.IsTensorOperator.eq_zero_of_forall_ne, PhyslibAlpha.Sl2.IsTensorOperator.exists_eq_smul_cgProj, PhyslibAlpha.Sl2.IsTensorOperator.exists_coord_eq
statement: formalized
proof: formalized
---

# The Wigner–Eckart theorem for sl₂

The module `PhyslibAlpha.QuantumMechanics.AngularMomentum.WignerEckart`, [PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckart.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckart.lean): 9 declarations, 9 with a docstring.

> Tensor operators between standard `sl₂` modules and the factorisation of their matrix elements.

## i. Overview

> A tensor operator of rank `k` from `V(m)` to `V(p)` is a linear map
> `T : V(k) → Hom(V(m), V(p))` with `[X, T x] = T (X x)` for the raising, lowering and weight
> operators `X`. In physics notation, with `k = 2κ`, `m = 2j` and `p = 2j'`, the vectors `T v_q` are
> the components `T^{(κ)}_μ` of a spherical tensor operator, and the condition is the usual
> commutator definition.
>
> The map `x ⊗ y ↦ T x y` is then a tensor intertwiner `V(k) ⊗ V(m) → V(p)`. By the results of
> `Sl2.TensorIntertwiner` this gives the Wigner–Eckart theorem: if `p = k + m - 2j`, there is a
> single scalar `c` (the reduced matrix element) with `T x y = c • cgProj (x ⊗ y)` for all `x, y`,
> so every matrix element is `c` times a Clebsch–Gordan coefficient. If `p` is not of this form,
> `T = 0` (the triangle and parity rule). Independently of this, the weight operator alone gives the
> rule for the magnetic quantum numbers: a matrix element vanishes unless the weights add up.
>
> The basis `v_l = f^l v_0` of the standard modules is not normalised, so the Clebsch–Gordan
> coefficients here differ from the usual tabulated values by normalisation factors. The statements
> themselves do not depend on this choice.

## ii. Key results

> - `IsTensorOperator` is the predicate for tensor operators.
> - `IsTensorOperator.lift_isTensorIntertwiner` turns a tensor operator into a tensor intertwiner.
> - `IsTensorOperator.exists_eq_smul_cgProj` is the Wigner–Eckart theorem.
> - `IsTensorOperator.eq_zero_of_forall_ne` is the triangle and parity selection rule.
> - `IsTensorOperator.apply_vNat_eq_zero_of_weight_ne` is the selection rule for the weights.

## iv. References

> - E. P. Wigner, *Group Theory and its Application to the Quantum Mechanics of Atomic Spectra*,
>   Academic Press (1959), chapter 21.
> - C. Eckart, *The application of group theory to the quantum dynamics of monatomic systems*,
>   Rev. Mod. Phys. 2, 305 (1930).

## A. Tensor operators

### A.1. Definition

**`PhyslibAlpha.Sl2.IsTensorOperator`**, a structure, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckart.lean#L79).

> A tensor operator of rank `k` from `V(m)` to `V(p)`: a linear map
> `T : V(k) → Hom(V(m), V(p))` with `[X, T x] = T (X x)` for `X = e, f, h`.

```lean
structure IsTensorOperator
    (T : StandardSl2Module K k →ₗ[K] StandardSl2Module K m →ₗ[K] StandardSl2Module K p) :
    Prop where
  comm_E : ∀ x, ρE ∘ₗ T x - T x ∘ₗ ρE = T (ρE x)
  comm_F : ∀ x, ρF ∘ₗ T x - T x ∘ₗ ρF = T (ρF x)
  comm_H : ∀ x, ρH ∘ₗ T x - T x ∘ₗ ρH = T (ρH x)
```

### A.2. Tensor operators as tensor intertwiners

**`PhyslibAlpha.Sl2.IsTensorOperator.apply_ρE`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckart.lean#L97).

> Leibniz form of the commutation relation for the raising operator.

```lean
lemma apply_ρE (hT : IsTensorOperator T) (x : StandardSl2Module K k)
    (y : StandardSl2Module K m) : ρE (T x y) = T (ρE x) y + T x (ρE y)
```

**`PhyslibAlpha.Sl2.IsTensorOperator.apply_ρF`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckart.lean#L104).

> Leibniz form of the commutation relation for the lowering operator.

```lean
lemma apply_ρF (hT : IsTensorOperator T) (x : StandardSl2Module K k)
    (y : StandardSl2Module K m) : ρF (T x y) = T (ρF x) y + T x (ρF y)
```

**`PhyslibAlpha.Sl2.IsTensorOperator.apply_ρH`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckart.lean#L111).

> Leibniz form of the commutation relation for the weight operator.

```lean
lemma apply_ρH (hT : IsTensorOperator T) (x : StandardSl2Module K k)
    (y : StandardSl2Module K m) : ρH (T x y) = T (ρH x) y + T x (ρH y)
```

**`PhyslibAlpha.Sl2.IsTensorOperator.lift_isTensorIntertwiner`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckart.lean#L118).

> The map `x ⊗ y ↦ T x y` of a tensor operator is a tensor intertwiner.

```lean
lemma lift_isTensorIntertwiner (hT : IsTensorOperator T) :
    IsTensorIntertwiner (TensorProduct.lift T)
```

## B. The Wigner–Eckart theorem

### B.1. Factorisation and the triangle rule

**`PhyslibAlpha.Sl2.IsTensorOperator.eq_zero_of_forall_ne`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckart.lean#L146).

> **Triangle and parity rule.** If `p` is not of the form `k + m - 2j` with `j ≤ min k m`,
> every tensor operator of rank `k` from `V(m)` to `V(p)` is zero.

```lean
lemma eq_zero_of_forall_ne (hkm : 0 < k + m)
    {T : StandardSl2Module K k →ₗ[K] StandardSl2Module K m →ₗ[K] StandardSl2Module K p}
    (hT : IsTensorOperator T) (hp : ∀ j : Fin (min k m + 1), k + m - 2 * (j : ℕ) ≠ p) :
    T = 0
```

**`PhyslibAlpha.Sl2.IsTensorOperator.exists_eq_smul_cgProj`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckart.lean#L158).

> **Wigner–Eckart theorem.** A tensor operator of rank `k` from `V(m)` to `V(k + m - 2j)`
> factorises as `T x y = c • cgProj (x ⊗ y)`: a single reduced matrix element `c` times the
> Clebsch–Gordan projection.

```lean
lemma exists_eq_smul_cgProj (hkm : 0 < k + m) {j : Fin (min k m + 1)}
    {T : StandardSl2Module K k →ₗ[K] StandardSl2Module K m →ₗ[K]
      StandardSl2Module K (k + m - 2 * (j : ℕ))}
    (hT : IsTensorOperator T) :
    ∃ c : K, ∀ x y, T x y = c • cgProj hkm j (x ⊗ₜ y)
```

**`PhyslibAlpha.Sl2.IsTensorOperator.exists_coord_eq`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckart.lean#L171).

> **Wigner–Eckart theorem**, matrix-element form: every matrix element
> `⟨v_s | T v_q | v_r⟩` is the reduced matrix element `c` times the Clebsch–Gordan coefficient, the
> `v_s`-coordinate of `cgProj (v_q ⊗ v_r)`.

```lean
lemma exists_coord_eq (hkm : 0 < k + m) {j : Fin (min k m + 1)}
    {T : StandardSl2Module K k →ₗ[K] StandardSl2Module K m →ₗ[K]
      StandardSl2Module K (k + m - 2 * (j : ℕ))}
    (hT : IsTensorOperator T) :
    ∃ c : K, ∀ (q r : ℕ) (s : Fin (k + m - 2 * (j : ℕ) + 1)),
      T (vNat k q) (vNat m r) s = c * cgProj hkm j (vNat k q ⊗ₜ vNat m r) s
```

### B.2. The weight selection rule

**`PhyslibAlpha.Sl2.IsTensorOperator.apply_vNat_eq_zero_of_weight_ne`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckart.lean#L188).

> **Weight selection rule.** The matrix element `⟨v_s | T v_q | v_r⟩` vanishes unless the
> weights add up, `(k - 2q) + (m - 2r) = p - 2s`. In physics notation this is `μ + m_j = m_{j'}`.

```lean
lemma apply_vNat_eq_zero_of_weight_ne
    {T : StandardSl2Module K k →ₗ[K] StandardSl2Module K m →ₗ[K] StandardSl2Module K p}
    (hT : IsTensorOperator T) (q r : ℕ) (s : Fin (p + 1))
    (hne : (k : ℤ) - 2 * q + ((m : ℤ) - 2 * r) ≠ (p : ℤ) - 2 * (s : ℕ)) :
    T (vNat k q) (vNat m r) s = 0
```

## Depends on

- [Intertwiners out of a tensor product of standard sl₂ modules](../../mathematics/part-02/representationtheory/sl2-tensorintertwiner.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckart.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckart.lean)
