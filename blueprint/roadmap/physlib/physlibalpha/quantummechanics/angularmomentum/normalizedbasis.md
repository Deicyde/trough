---
declaration: module
origin: cited
lean: PhyslibAlpha.Sl2.normSq, PhyslibAlpha.Sl2.normSq_succ, PhyslibAlpha.Sl2.normSq_pos, PhyslibAlpha.Sl2.invForm, PhyslibAlpha.Sl2.invForm_v, PhyslibAlpha.Sl2.invForm_vNat, PhyslibAlpha.Sl2.bilin_ext_vNat, PhyslibAlpha.Sl2.invForm_comp_ρE
statement: formalized
proof: formalized
---

# The invariant form and the normalised basis of the standard modules

The module `PhyslibAlpha.QuantumMechanics.AngularMomentum.NormalizedBasis`, [PhyslibAlpha/QuantumMechanics/AngularMomentum/NormalizedBasis.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/NormalizedBasis.lean): 16 declarations, 11 with a docstring.

> The contravariant form on `V(n)` and the orthonormal basis `|j, m⟩` with the textbook matrix
> elements of `J₊`, `J₋` and `Jz`.

## i. Overview

> The basis `v_a = f^a v_0` of `V(n)` used throughout is not normalised. There is a symmetric
> bilinear form on `V(n)`, unique up to a scalar, for which the raising and lowering operators are
> adjoint and the weight operator is symmetric:
> `⟨e x, y⟩ = ⟨x, f y⟩`, `⟨h x, y⟩ = ⟨x, h y⟩`. In the basis `v_a` it is diagonal with
> `⟨v_a, v_a⟩ = a! · n!/(n - a)!`.
>
> Over `ℝ` the rescaled vectors `u_a = v_a / √⟨v_a, v_a⟩` are orthonormal. With `j = n/2` and
> `m = j - a` they are the states `|j, m⟩`, and the operators act by the textbook formulas
> (Condon–Shortley phases):
>
> - `J₊ |j, m⟩ = √((j - m)(j + m + 1)) |j, m + 1⟩`, i.e. `e u_{a+1} = √((a+1)(n-a)) u_a`;
> - `J₋ |j, m⟩ = √((j + m)(j - m + 1)) |j, m - 1⟩`, i.e. `f u_a = √((a+1)(n-a)) u_{a+1}`;
> - `2Jz |j, m⟩ = 2m |j, m⟩`, i.e. `h u_a = (n - 2a) u_a`.

## ii. Key results

> - `normSq` is `⟨v_a, v_a⟩` and `invForm` the contravariant form.
> - `invForm_comp_ρE` and `invForm_comp_ρH` express that `e, f` are adjoint and `h` is symmetric.
> - `normVec` is the normalised basis over `ℝ`; `invForm_normVec` is orthonormality.
> - `ρE_normVec_succ`, `ρF_normVec` and `ρH_normVec` are the textbook matrix elements.

## iv. References

> - J. J. Sakurai and J. Napolitano, *Modern Quantum Mechanics*, 3rd ed., Cambridge University
>   Press (2020), section 3.5.

## A. The contravariant form

### A.1. Squared norms

**`PhyslibAlpha.Sl2.normSq`**, a def, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/NormalizedBasis.lean#L70).

> The squared norm `⟨v_a, v_a⟩ = a! · n!/(n - a)!` of the basis vector `v_a` of `V(n)`.

```lean
def normSq (n a : ℕ) : ℕ
```

**`PhyslibAlpha.Sl2.normSq_succ`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/NormalizedBasis.lean#L72).

```lean
lemma normSq_succ (n a : ℕ) : normSq n (a + 1) = normSq n a * ((a + 1) * (n - a))
```

**`PhyslibAlpha.Sl2.normSq_pos`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/NormalizedBasis.lean#L76).

```lean
lemma normSq_pos {n a : ℕ} (ha : a ≤ n) : 0 < normSq n a
```

### A.2. Definition and values

**`PhyslibAlpha.Sl2.invForm`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/NormalizedBasis.lean#L90).

> The contravariant form on `V(n)`: diagonal in the basis `v_a` with entries `normSq n a`.

```lean
def invForm : StandardSl2Module K n →ₗ[K] StandardSl2Module K n →ₗ[K] K
```

**`PhyslibAlpha.Sl2.invForm_v`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/NormalizedBasis.lean#L94).

```lean
lemma invForm_v (i j : Fin (n + 1)) :
    invForm K n (v i) (v j) = if i = j then (normSq n i : K) else 0
```

**`PhyslibAlpha.Sl2.invForm_vNat`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/NormalizedBasis.lean#L102).

```lean
lemma invForm_vNat (a b : ℕ) :
    invForm K n (vNat n a) (vNat n b) = if a = b ∧ a ≤ n then (normSq n a : K) else 0
```

**`PhyslibAlpha.Sl2.bilin_ext_vNat`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/NormalizedBasis.lean#L116).

> Two bilinear forms on `V(n)` agree if they agree on all pairs `v_a, v_b`.

```lean
lemma bilin_ext_vNat {B B' : StandardSl2Module K n →ₗ[K] StandardSl2Module K n →ₗ[K] K}
    (h : ∀ a b, B (vNat n a) (vNat n b) = B' (vNat n a) (vNat n b)) : B = B'
```

### A.3. Contravariance

**`PhyslibAlpha.Sl2.invForm_comp_ρE`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/NormalizedBasis.lean#L129).

> The raising and lowering operators are adjoint: `⟨e x, y⟩ = ⟨x, f y⟩`.

```lean
lemma invForm_comp_ρE : (invForm K n).comp ρE = (invForm K n).compl₂ ρF
```

**`PhyslibAlpha.Sl2.invForm_comp_ρH`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/NormalizedBasis.lean#L153).

> The weight operator is symmetric: `⟨h x, y⟩ = ⟨x, h y⟩`.

```lean
lemma invForm_comp_ρH : (invForm K n).comp ρH = (invForm K n).compl₂ ρH
```

**`PhyslibAlpha.Sl2.invForm_comm`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/NormalizedBasis.lean#L163).

> The form is symmetric.

```lean
lemma invForm_comm (x y : StandardSl2Module K n) : invForm K n x y = invForm K n y x
```

## B. The normalised basis over ℝ

**`PhyslibAlpha.Sl2.normVec`**, a def, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/NormalizedBasis.lean#L179).

> The normalised basis vector `u_a = v_a / √(normSq n a)` of `V(n)` over `ℝ`; for `a ≤ n` it
> is the state `|j, m⟩` with `j = n/2`, `m = j - a`.

```lean
def normVec (n a : ℕ) : StandardSl2Module ℝ n
```

**`PhyslibAlpha.Sl2.sqrt_normSq_succ`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/NormalizedBasis.lean#L182).

```lean
lemma sqrt_normSq_succ (n a : ℕ) :
    Real.sqrt (normSq n (a + 1)) =
      Real.sqrt (normSq n a) * Real.sqrt (((a : ℝ) + 1) * ((n : ℝ) - a))
```

**`PhyslibAlpha.Sl2.invForm_normVec`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/NormalizedBasis.lean#L197).

> Orthonormality: `⟨u_a, u_b⟩ = δ_ab` for `a, b ≤ n`.

```lean
lemma invForm_normVec {a b : ℕ} (ha : a ≤ n) (hb : b ≤ n) :
    invForm ℝ n (normVec n a) (normVec n b) = if a = b then 1 else 0
```

**`PhyslibAlpha.Sl2.ρH_normVec`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/NormalizedBasis.lean#L212).

> The weight operator on the normalised basis: `h u_a = (n - 2a) u_a`, i.e.
> `Jz |j, m⟩ = m |j, m⟩`.

```lean
lemma ρH_normVec (a : ℕ) :
    (ρH : Module.End ℝ (StandardSl2Module ℝ n)) (normVec n a) =
      ((n : ℝ) - 2 * a) • normVec n a
```

**`PhyslibAlpha.Sl2.ρF_normVec`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/NormalizedBasis.lean#L219).

> The lowering operator on the normalised basis: `f u_a = √((a+1)(n-a)) u_{a+1}` for `a < n`,
> i.e. `J₋ |j, m⟩ = √((j + m)(j - m + 1)) |j, m - 1⟩`.

```lean
lemma ρF_normVec {a : ℕ} (ha : a < n) :
    (ρF : Module.End ℝ (StandardSl2Module ℝ n)) (normVec n a) =
      Real.sqrt (((a : ℝ) + 1) * ((n : ℝ) - a)) • normVec n (a + 1)
```

**`PhyslibAlpha.Sl2.ρE_normVec_succ`**, a lemma, [line 234](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/NormalizedBasis.lean#L234).

> The raising operator on the normalised basis: `e u_{a+1} = √((a+1)(n-a)) u_a` for `a < n`,
> i.e. `J₊ |j, m⟩ = √((j - m)(j + m + 1)) |j, m + 1⟩`.

```lean
lemma ρE_normVec_succ {a : ℕ} (ha : a < n) :
    (ρE : Module.End ℝ (StandardSl2Module ℝ n)) (normVec n (a + 1)) =
      Real.sqrt (((a : ℝ) + 1) * ((n : ℝ) - a)) • normVec n a
```

## Depends on

- [Highest-weight vectors in tensor products of standard sl₂ modules](../../mathematics/part-02/representationtheory/sl2-tensorhighestweight.md)

## Proof depends on

- [Schur's lemma for the standard sl₂ modules](../../mathematics/part-02/representationtheory/sl2-schur.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/AngularMomentum/NormalizedBasis.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/NormalizedBasis.lean)
