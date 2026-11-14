---
declaration: module
origin: cited
lean: PhyslibAlpha.Sl2.IsIntertwiner, PhyslibAlpha.Sl2.IsIntertwiner.apply_ρE, PhyslibAlpha.Sl2.IsIntertwiner.apply_ρF, PhyslibAlpha.Sl2.IsIntertwiner.apply_ρH, PhyslibAlpha.Sl2.IsIntertwiner.apply_ρF_pow, PhyslibAlpha.Sl2.IsIntertwiner.id, PhyslibAlpha.Sl2.IsIntertwiner.smul, PhyslibAlpha.Sl2.IsIntertwiner.add
statement: formalized
proof: formalized
---

# Schur's lemma for the standard sl₂ modules

The module `PhyslibAlpha.Mathematics.RepresentationTheory.Sl2.Schur`, [PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Schur.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Schur.lean): 16 declarations, 12 with a docstring.

> Linear maps between standard modules that commute with the `sl₂` action.

## i. Overview

> A linear map `φ : V(a) → V(b)` between standard modules is an intertwiner if it commutes with
> the raising, lowering and weight operators. The image of the highest-weight vector `v_0` is then
> killed by the raising operator and has weight `a`. In `V(b)` the only vectors killed by the raising
> operator are the multiples of `v_0`, which have weight `b`. Hence `φ v_0 = c • v_0` with `c = 0`
> unless `a = b`, and since `v_l = f^l v_0` this determines `φ` completely. This is Schur's lemma
> for the standard modules: an intertwiner `V(a) → V(b)` is zero for `a ≠ b` and a scalar multiple of
> the identity for `a = b`.

## ii. Key results

> - `IsIntertwiner` is the predicate for linear maps commuting with `ρE`, `ρF` and `ρH`.
> - `IsIntertwiner.apply_vNat` shows that an intertwiner sends `v_l` to `c • v_l` for a fixed `c`.
> - `IsIntertwiner.eq_zero_of_ne` shows that an intertwiner `V(a) → V(b)` with `a ≠ b` vanishes.
> - `IsIntertwiner.eq_smul_id` shows that an intertwiner `V(n) → V(n)` is a scalar multiple of the
>   identity.

## iv. References

> - Mathlib, `Mathlib.Algebra.Lie.Sl2`.

## A. Intertwiners

### A.1. Definition and closure properties

**`PhyslibAlpha.Sl2.IsIntertwiner`**, a structure, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Schur.lean#L63).

> A linear map between standard modules is an intertwiner if it commutes with the raising,
> lowering and weight operators.

```lean
structure IsIntertwiner (φ : StandardSl2Module K a →ₗ[K] StandardSl2Module K b) : Prop where
  comm_ρE : φ ∘ₗ ρE = ρE ∘ₗ φ
  comm_ρF : φ ∘ₗ ρF = ρF ∘ₗ φ
  comm_ρH : φ ∘ₗ ρH = ρH ∘ₗ φ
```

**`PhyslibAlpha.Sl2.IsIntertwiner.apply_ρE`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Schur.lean#L72).

```lean
lemma apply_ρE (hφ : IsIntertwiner φ) (x : StandardSl2Module K a) : φ (ρE x) = ρE (φ x)
```

**`PhyslibAlpha.Sl2.IsIntertwiner.apply_ρF`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Schur.lean#L75).

```lean
lemma apply_ρF (hφ : IsIntertwiner φ) (x : StandardSl2Module K a) : φ (ρF x) = ρF (φ x)
```

**`PhyslibAlpha.Sl2.IsIntertwiner.apply_ρH`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Schur.lean#L78).

```lean
lemma apply_ρH (hφ : IsIntertwiner φ) (x : StandardSl2Module K a) : φ (ρH x) = ρH (φ x)
```

**`PhyslibAlpha.Sl2.IsIntertwiner.apply_ρF_pow`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Schur.lean#L81).

```lean
lemma apply_ρF_pow (hφ : IsIntertwiner φ) (l : ℕ) (x : StandardSl2Module K a) :
    φ ((ρF ^ l) x) = (ρF ^ l) (φ x)
```

**`PhyslibAlpha.Sl2.IsIntertwiner.id`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Schur.lean#L89).

> The identity is an intertwiner.

```lean
lemma id : IsIntertwiner (LinearMap.id : StandardSl2Module K n →ₗ[K] StandardSl2Module K n)
```

**`PhyslibAlpha.Sl2.IsIntertwiner.smul`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Schur.lean#L93).

> Scalar multiples of intertwiners are intertwiners.

```lean
lemma smul (hφ : IsIntertwiner φ) (c : K) : IsIntertwiner (c • φ)
```

**`PhyslibAlpha.Sl2.IsIntertwiner.add`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Schur.lean#L99).

> Sums of intertwiners are intertwiners.

```lean
lemma add (hφ : IsIntertwiner φ) (hψ : IsIntertwiner ψ) : IsIntertwiner (φ + ψ)
```

### A.2. Coordinate vectors and vectors killed by the raising operator

**`PhyslibAlpha.Sl2.ρF_pow_vNat_zero`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Schur.lean#L113).

> The lowering string of `v_0` runs through the coordinate vectors: `f^l v_0 = v_l`.

```lean
lemma ρF_pow_vNat_zero (l : ℕ) :
    ((ρF : Module.End K (StandardSl2Module K n)) ^ l) (vNat n 0) = vNat n l
```

**`PhyslibAlpha.Sl2.StandardSl2Module.linearMap_ext_vNat`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Schur.lean#L120).

> Two linear maps out of a standard module agree if they agree on all `v_l`.

```lean
lemma StandardSl2Module.linearMap_ext_vNat {M : Type*} [AddCommGroup M]
    [Module K M] {α β : StandardSl2Module K a →ₗ[K] M} (h : ∀ l, α (vNat a l) = β (vNat a l)) :
    α = β
```

**`PhyslibAlpha.Sl2.eq_smul_vNat_zero_of_ρE_eq_zero`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Schur.lean#L131).

> A vector of `V(n)` killed by the raising operator is a multiple of `v_0`.

```lean
lemma eq_smul_vNat_zero_of_ρE_eq_zero [CharZero K] {w : StandardSl2Module K n}
    (hw : (ρE : Module.End K (StandardSl2Module K n)) w = 0) :
    w = w ⟨0, Nat.succ_pos n⟩ • vNat n 0
```

### A.3. Schur's lemma

**`PhyslibAlpha.Sl2.IsIntertwiner.apply_vNat_zero`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Schur.lean#L163).

> The image of `v_0` under an intertwiner is a multiple of `v_0`.

```lean
lemma apply_vNat_zero (hφ : IsIntertwiner φ) :
    φ (vNat a 0) = φ (vNat a 0) ⟨0, Nat.succ_pos b⟩ • vNat b 0
```

**`PhyslibAlpha.Sl2.IsIntertwiner.apply_vNat`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Schur.lean#L170).

> An intertwiner sends every coordinate vector `v_l` to the same multiple `c • v_l`, where `c`
> is the `v_0`-coordinate of the image of `v_0`.

```lean
lemma apply_vNat (hφ : IsIntertwiner φ) (l : ℕ) :
    φ (vNat a l) = φ (vNat a 0) ⟨0, Nat.succ_pos b⟩ • vNat b l
```

**`PhyslibAlpha.Sl2.IsIntertwiner.coeff_eq_zero_of_ne`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Schur.lean#L177).

> The scalar of an intertwiner vanishes unless the two highest weights agree.

```lean
lemma coeff_eq_zero_of_ne (hφ : IsIntertwiner φ) (hab : a ≠ b) :
    φ (vNat a 0) ⟨0, Nat.succ_pos b⟩ = 0
```

**`PhyslibAlpha.Sl2.IsIntertwiner.eq_zero_of_ne`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Schur.lean#L190).

> **Schur's lemma**, first half: an intertwiner `V(a) → V(b)` with `a ≠ b` is zero.

```lean
lemma eq_zero_of_ne (hφ : IsIntertwiner φ) (hab : a ≠ b) : φ = 0
```

**`PhyslibAlpha.Sl2.IsIntertwiner.eq_smul_id`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Schur.lean#L196).

> **Schur's lemma**, second half: an intertwiner `V(n) → V(n)` is a scalar multiple of the
> identity.

```lean
lemma eq_smul_id {φ : StandardSl2Module K n →ₗ[K] StandardSl2Module K n} (hφ : IsIntertwiner φ) :
    φ = φ (vNat n 0) ⟨0, Nat.succ_pos n⟩ • LinearMap.id
```

## Depends on

- [Highest-weight vectors in tensor products of standard sl₂ modules](sl2-tensorhighestweight.md)

## Sources

- [PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Schur.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Schur.lean)
