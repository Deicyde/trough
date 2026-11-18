---
declaration: module
origin: cited
lean: PhyslibAlpha.Sl2.diagEnd, PhyslibAlpha.Sl2.diagEnd_tmul, PhyslibAlpha.Sl2.lie_diagEnd, PhyslibAlpha.Sl2.diagEnd_smul, PhyslibAlpha.Sl2.diagEnd_add, PhyslibAlpha.Sl2.diagEnd_sub, PhyslibAlpha.Sl2.StandardSl2Module.vNat, PhyslibAlpha.Sl2.StandardSl2Module.vNat_apply
statement: formalized
proof: formalized
---

# Highest-weight vectors in tensor products of standard sl₂ modules

The module `PhyslibAlpha.Mathematics.RepresentationTheory.Sl2.TensorHighestWeight`, [PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorHighestWeight.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorHighestWeight.lean): 30 declarations, 20 with a docstring.

> Equips `V(m) ⊗ V(n)` with the diagonal `sl₂` action and writes down its highest-weight vectors.

## i. Overview

> The raising, lowering and weight operators of two standard modules act on their tensor
> product by `A ⊗ 1 + 1 ⊗ A`. These diagonal operators form an `sl₂` triple as soon as
> `m + n > 0`. For every `k ≤ min m n` the vector
> `w_k = ∑_{a=0}^{k} (-1)^a (k choose a) (n-k+a)! (m-a)! • v_a ⊗ v_{k-a}`
> is killed by the diagonal raising operator and has weight `m + n - 2k`. The lowering string of
> `w_k` has exactly `m + n - 2k + 1` nonzero members.
>
> In physics notation, with `m = 2j₁`, `n = 2j₂` and `J = j₁ + j₂ - k`, the coefficients of `w_k`
> are, up to a common factor and the change from the bases `v_a = f^a v_0` to normalised bases,
> the Clebsch–Gordan coefficients of the top state `|J, J⟩`. This file does not show that the
> lowering strings of the `w_k` together form a basis of `V(m) ⊗ V(n)`.

## ii. Key results

> - `isSl2Triple_tensor` shows that the diagonal operators form an `sl₂` triple.
> - `tensorE_hwVec` and `tensorH_hwVec` show that `hwVec m n k` is a highest-weight vector.
> - `hwVec_hasPrimitiveVectorWith` packages this as a primitive vector of weight `m + n - 2k`.
> - `tensorF_pow_hwVec_ne_zero` and `tensorF_pow_hwVec_eq_zero` give the length of its
>   lowering string.

## iv. References

> - Mathlib, `Mathlib.Algebra.Lie.Sl2`.

## A. The diagonal action

**`PhyslibAlpha.Sl2.diagEnd`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorHighestWeight.lean#L72).

> The diagonal action `A ⊗ 1 + 1 ⊗ B` of two endomorphisms on `M ⊗ N`.

```lean
def diagEnd (A : Module.End K M) (B : Module.End K N) : Module.End K (M ⊗[K] N)
```

**`PhyslibAlpha.Sl2.diagEnd_tmul`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorHighestWeight.lean#L75).

```lean
lemma diagEnd_tmul (A : Module.End K M) (B : Module.End K N) (x : M) (y : N) :
    diagEnd A B (x ⊗ₜ y) = A x ⊗ₜ y + x ⊗ₜ B y
```

**`PhyslibAlpha.Sl2.lie_diagEnd`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorHighestWeight.lean#L80).

> The diagonal action respects commutators.

```lean
lemma lie_diagEnd (A A' : Module.End K M) (B B' : Module.End K N) :
    ⁅diagEnd A B, diagEnd A' B'⁆ = diagEnd ⁅A, A'⁆ ⁅B, B'⁆
```

**`PhyslibAlpha.Sl2.diagEnd_smul`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorHighestWeight.lean#L88).

```lean
lemma diagEnd_smul (c : K) (A : Module.End K M) (B : Module.End K N) :
    diagEnd (c • A) (c • B) = c • diagEnd A B
```

**`PhyslibAlpha.Sl2.diagEnd_add`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorHighestWeight.lean#L96).

> The diagonal action is additive in both endomorphisms.

```lean
lemma diagEnd_add (A A' : Module.End K M) (B B' : Module.End K N) :
    diagEnd (A + A') (B + B') = diagEnd A B + diagEnd A' B'
```

**`PhyslibAlpha.Sl2.diagEnd_sub`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorHighestWeight.lean#L104).

> The diagonal action respects differences.

```lean
lemma diagEnd_sub (A A' : Module.End K M) (B B' : Module.End K N) :
    diagEnd (A - A') (B - B') = diagEnd A B - diagEnd A' B'
```

### A.1. Coordinate vectors indexed by natural numbers

> `StandardSl2Module.vNat n i` is the coordinate vector `v_i` for `i ≤ n` and zero for `i > n`.
> With this convention the raising, lowering and weight formulas hold for every `i : ℕ`, which
> keeps the index bookkeeping in sums over `Finset.range` free of side conditions.

**`PhyslibAlpha.Sl2.StandardSl2Module.vNat`**, a def, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorHighestWeight.lean#L121).

> The coordinate vector `v_i` of `StandardSl2Module K n`, indexed by a natural number;
> it is zero for `i > n`.

```lean
def StandardSl2Module.vNat (n i : ℕ) : StandardSl2Module K n
```

**`PhyslibAlpha.Sl2.StandardSl2Module.vNat_apply`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorHighestWeight.lean#L128).

```lean
lemma vNat_apply (i : ℕ) (k : Fin (n + 1)) :
    vNat (K := K) n i k = if (k : ℕ) = i then 1 else 0
```

**`PhyslibAlpha.Sl2.StandardSl2Module.vNat_eq_v`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorHighestWeight.lean#L131).

```lean
lemma vNat_eq_v {i : ℕ} (hi : i ≤ n) : vNat (K := K) n i = v ⟨i, by omega⟩
```

**`PhyslibAlpha.Sl2.StandardSl2Module.vNat_of_lt`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorHighestWeight.lean#L135).

```lean
lemma vNat_of_lt {i : ℕ} (hi : n < i) : vNat (K := K) n i = 0
```

**`PhyslibAlpha.Sl2.ρH_vNat`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorHighestWeight.lean#L149).

```lean
lemma ρH_vNat (i : ℕ) :
    (ρH : Module.End K (StandardSl2Module K n)) (vNat n i) = ((n : K) - 2 * i) • vNat n i
```

**`PhyslibAlpha.Sl2.ρF_vNat`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorHighestWeight.lean#L155).

```lean
lemma ρF_vNat (i : ℕ) :
    (ρF : Module.End K (StandardSl2Module K n)) (vNat n i) = vNat n (i + 1)
```

**`PhyslibAlpha.Sl2.ρE_vNat_zero`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorHighestWeight.lean#L163).

```lean
lemma ρE_vNat_zero :
    (ρE : Module.End K (StandardSl2Module K n)) (vNat n 0) = 0
```

**`PhyslibAlpha.Sl2.ρE_vNat_succ`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorHighestWeight.lean#L168).

```lean
lemma ρE_vNat_succ [CharZero K] (i : ℕ) :
    (ρE : Module.End K (StandardSl2Module K n)) (vNat n (i + 1)) =
      (((i : K) + 1) * ((n : K) - i)) • vNat n i
```

### A.2. The diagonal operators on `V(m) ⊗ V(n)`

**`PhyslibAlpha.Sl2.tensorE`**, a def, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorHighestWeight.lean#L187).

> The diagonal raising operator on `V(m) ⊗ V(n)`.

```lean
def tensorE (m n : ℕ) : Module.End K (StandardSl2Module K m ⊗[K] StandardSl2Module K n)
```

**`PhyslibAlpha.Sl2.tensorF`**, a def, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorHighestWeight.lean#L191).

> The diagonal lowering operator on `V(m) ⊗ V(n)`.

```lean
def tensorF (m n : ℕ) : Module.End K (StandardSl2Module K m ⊗[K] StandardSl2Module K n)
```

**`PhyslibAlpha.Sl2.tensorH`**, a def, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorHighestWeight.lean#L195).

> The diagonal weight operator on `V(m) ⊗ V(n)`.

```lean
def tensorH (m n : ℕ) : Module.End K (StandardSl2Module K m ⊗[K] StandardSl2Module K n)
```

**`PhyslibAlpha.Sl2.tensorCoord`**, a def, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorHighestWeight.lean#L199).

> The coefficient of `v_i ⊗ v_j` in an element of `V(m) ⊗ V(n)`.

```lean
def tensorCoord (m n : ℕ) (i : Fin (m + 1)) (j : Fin (n + 1)) :
    StandardSl2Module K m ⊗[K] StandardSl2Module K n →ₗ[K] K
```

**`PhyslibAlpha.Sl2.tensorCoord_tmul`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorHighestWeight.lean#L205).

```lean
lemma tensorCoord_tmul (i : Fin (m + 1)) (j : Fin (n + 1)) (x : StandardSl2Module K m)
    (y : StandardSl2Module K n) : tensorCoord m n i j (x ⊗ₜ y) = x i * y j
```

**`PhyslibAlpha.Sl2.tensorH_tmul_vNat`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorHighestWeight.lean#L210).

> The diagonal weight operator on a product of coordinate vectors.

```lean
lemma tensorH_tmul_vNat (a b : ℕ) :
    tensorH (K := K) m n (vNat m a ⊗ₜ vNat n b) =
      ((m : K) + n - 2 * (a + b)) • (vNat m a ⊗ₜ vNat n b)
```

**`PhyslibAlpha.Sl2.isSl2Triple_tensor`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorHighestWeight.lean#L219).

> The diagonal operators on `V(m) ⊗ V(n)` form an `sl₂` triple when `m + n > 0`.

```lean
lemma isSl2Triple_tensor [CharZero K] (hmn : 0 < m + n) :
    IsSl2Triple (tensorH (K := K) m n) (tensorE m n) (tensorF m n)
```

## B. Highest-weight vectors

### B.1. The coefficients

**`PhyslibAlpha.Sl2.cgCoeff`**, a def, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorHighestWeight.lean#L240).

> The coefficient of `v_a ⊗ v_{k-a}` in the highest-weight vector of weight `m + n - 2k`
> of `V(m) ⊗ V(n)`: `(-1)^a (k choose a) (n-k+a)! (m-a)!`.

```lean
def cgCoeff (m n k a : ℕ) : K
```

**`PhyslibAlpha.Sl2.cgCoeff_rec`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorHighestWeight.lean#L244).

> The two-term recursion of the coefficients that makes the raising operator vanish.

```lean
lemma cgCoeff_rec {j a : ℕ} (hjm : j + 1 ≤ m) (hjn : j + 1 ≤ n) (ha : a ≤ j) :
    cgCoeff (K := K) m n (j + 1) (a + 1) * (((a : K) + 1) * ((m : K) - a)) +
      cgCoeff m n (j + 1) a * ((((j - a : ℕ) : K) + 1) * ((n : K) - ((j - a : ℕ) : K))) = 0
```

**`PhyslibAlpha.Sl2.hwVec`**, a def, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorHighestWeight.lean#L270).

> The highest-weight vector of weight `m + n - 2k` in `V(m) ⊗ V(n)`.

```lean
def hwVec (m n k : ℕ) : StandardSl2Module K m ⊗[K] StandardSl2Module K n
```

### B.2. Weight and raising operator

**`PhyslibAlpha.Sl2.tensorH_hwVec`**, a lemma, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorHighestWeight.lean#L276).

> `hwVec m n k` has weight `m + n - 2k`.

```lean
lemma tensorH_hwVec (k : ℕ) :
    tensorH (K := K) m n (hwVec m n k) = ((m : K) + n - 2 * k) • hwVec m n k
```

**`PhyslibAlpha.Sl2.tensorE_hwVec`**, a lemma, [line 287](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorHighestWeight.lean#L287).

> `hwVec m n k` is killed by the diagonal raising operator when `k ≤ min m n`.

```lean
lemma tensorE_hwVec [CharZero K] {k : ℕ} (hkm : k ≤ m) (hkn : k ≤ n) :
    tensorE (K := K) m n (hwVec m n k) = 0
```

### B.3. Primitive vectors and lowering strings

**`PhyslibAlpha.Sl2.hwVec_ne_zero`**, a lemma, [line 312](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorHighestWeight.lean#L312).

> `hwVec m n k` is nonzero for `k ≤ n`: its `v_0 ⊗ v_k` coefficient is `(n-k)! m!`.

```lean
lemma hwVec_ne_zero [CharZero K] {k : ℕ} (hkn : k ≤ n) :
    hwVec (K := K) m n k ≠ 0
```

**`PhyslibAlpha.Sl2.hwVec_hasPrimitiveVectorWith`**, a lemma, [line 324](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorHighestWeight.lean#L324).

> `hwVec m n k` is a primitive vector of weight `m + n - 2k` for the diagonal action.

```lean
lemma hwVec_hasPrimitiveVectorWith [CharZero K] {k : ℕ} (hmn : 0 < m + n) (hkm : k ≤ m)
    (hkn : k ≤ n) :
    (isSl2Triple_tensor (K := K) hmn).HasPrimitiveVectorWith (hwVec (K := K) m n k)
      ((m + n - 2 * k : ℕ) : K)
```

**`PhyslibAlpha.Sl2.tensorF_pow_hwVec_ne_zero`**, a lemma, [line 336](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorHighestWeight.lean#L336).

> The first `m + n - 2k + 1` members of the lowering string of `hwVec m n k` are nonzero.

```lean
lemma tensorF_pow_hwVec_ne_zero [CharZero K] {k l : ℕ} (hmn : 0 < m + n) (hkm : k ≤ m)
    (hkn : k ≤ n) (hl : l ≤ m + n - 2 * k) :
    (tensorF (K := K) m n ^ l) (hwVec m n k) ≠ 0
```

**`PhyslibAlpha.Sl2.tensorF_pow_hwVec_eq_zero`**, a lemma, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorHighestWeight.lean#L342).

> The lowering string of `hwVec m n k` ends after `m + n - 2k + 1` steps.

```lean
lemma tensorF_pow_hwVec_eq_zero [CharZero K] {k : ℕ} (hmn : 0 < m + n) (hkm : k ≤ m)
    (hkn : k ≤ n) :
    (tensorF (K := K) m n ^ (m + n - 2 * k + 1)) (hwVec m n k) = 0
```

## Depends on

- [Explicit standard sl₂ modules](sl2-construction.md)

## Proof depends on

- [A basis for two commuting sl₂ actions](sl2-bivariatebasis.md)

## Sources

- [PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorHighestWeight.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorHighestWeight.lean)
