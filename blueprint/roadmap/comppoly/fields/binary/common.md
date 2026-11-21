---
catalog: module
lean: ZMod2Poly.add_self_cancel, ZMod2Poly.sub_eq_add, ZMod2Poly.neg_eq_self, ZMod2Poly.add_eq_sub, ZMod2Poly.two_mul, ZMod2Poly.mul_two, ZMod2Poly.two_eq_zero, ZMod2Poly.three_eq_one, ZMod2Poly.mul_three, ZMod2Poly.natCast_ZMod2, ZMod2_value_eq_zero_or_one, eq_of_associated_ZMod2, ZMod2Poly.fintypeCard_eq_two, ZMod2Poly.frobenius, ZMod2Poly.euclidean_gcd_comm, Polynomial.exists_factor_le_64_of_reducible, BinaryField.BitVec.toNat_of_cast, BinaryField.toPoly, BinaryField.carryLessMul_unfold, BinaryField.clMul_unfold, BinaryField.toPoly_one_shiftLeft, BinaryField.toPoly_one_eq_one, BinaryField.toPoly_zero_eq_zero, BinaryField.toPoly_ne_zero_iff_ne_zero, BinaryField.toPoly_degree_lt_w, BinaryField.toPoly_degree_of_lt_two_pow, BinaryField.BitVec_lt_two_pow_of_toPoly_degree_lt, BinaryField.toPoly_xor, BinaryField.toPoly_fold_xor, BinaryField.toPoly_128_extend_256, BinaryField.BitVec_getLsb_eq_false_of_toNat_lt_two_pow, BinaryField.BitVec_getElem_eq_false_of_toNat_lt_two_pow, BinaryField.BitVec_getLsb_shiftLeft, BinaryField.toPoly_coeff, BinaryField.toPoly_shiftLeft_no_overflow, BinaryField.toPoly_zeroExtendTo, BinaryField.toPoly_carryLessMul, BinaryField.toPoly_clMul, BinaryField.toPoly_eq_range, BinaryField.toPoly_split, BinaryField.chain_step, BinaryField.gcd_eq_gcd_next_step, BinaryField.gcd_one_zero
statement: formalized
proof: formalized
---

# Common Utilities for Binary Fields

`CompPoly.Fields.Binary.Common`, in [CompPoly/Fields/Binary/Common.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean), by Chung Thai Nguyen, Quang Dao, Derek Sorensen, Dimitris Mitsios.

> This file provides shared utilities for binary field implementations (fields of characteristic 2).
> It includes:
>
> 1. **ZMod2Poly lemmas** — Properties of polynomials over GF(2)
> 2. **BitVec operations** — Carry-less multiplication, squaring
> 3. **BitVec ↔ Polynomial isomorphism** — `toPoly` and related lemmas
>
> These utilities are used by both the tower construction (`Tower/`) and the
> direct GF(2^128) implementation (`BF128Ghash/`). Import
> `CompPoly.Fields.Binary.Common.Arithmetic` for word operations without polynomial support.
>
> ## Main Definitions
>
> - `ZMod2Poly.add_self_cancel`: In char 2, `a + a = 0`
> - `toPoly`: Convert a BitVec to a polynomial over GF(2)
> - `clMul`: Carry-less multiplication of bit vectors
> - `toPoly_xor`: `toPoly (a ^^^ b) = toPoly a + toPoly b`
> - `toPoly_clMul`: `toPoly (clMul a b) = toPoly a * toPoly b`
> - `toPoly_one_shiftLeft`: `toPoly (1 <<< n) = X^n`

> ## Section 1: ZMod 2 Polynomial Lemmas

`ZMod2Poly.add_self_cancel` (lemma, [line 48](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L48))

```lean
lemma ZMod2Poly.add_self_cancel (a : Polynomial (ZMod 2)) : a + a = 0
```

`ZMod2Poly.sub_eq_add` (lemma, [line 51](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L51))

```lean
lemma ZMod2Poly.sub_eq_add (a b : Polynomial (ZMod 2)) : a - b = a + b
```

`ZMod2Poly.neg_eq_self` (lemma, [line 54](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L54))

```lean
lemma ZMod2Poly.neg_eq_self (a : Polynomial (ZMod 2)) : -a = a
```

`ZMod2Poly.add_eq_sub` (lemma, [line 57](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L57))

```lean
lemma ZMod2Poly.add_eq_sub (a b : Polynomial (ZMod 2)) : a + b = a - b
```

`ZMod2Poly.two_mul` (lemma, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L60))

```lean
lemma ZMod2Poly.two_mul (a : Polynomial (ZMod 2)) : 2 * a = 0
```

`ZMod2Poly.mul_two` (lemma, [line 63](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L63))

```lean
lemma ZMod2Poly.mul_two (a : Polynomial (ZMod 2)) : a * 2 = 0
```

`ZMod2Poly.two_eq_zero` (lemma, [line 66](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L66))

```lean
lemma ZMod2Poly.two_eq_zero : (2 : Polynomial (ZMod 2)) = 0
```

`ZMod2Poly.three_eq_one` (lemma, [line 69](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L69))

```lean
lemma ZMod2Poly.three_eq_one : (3 : Polynomial (ZMod 2)) = 1
```

`ZMod2Poly.mul_three` (lemma, [line 71](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L71))

```lean
lemma ZMod2Poly.mul_three (a : Polynomial (ZMod 2)) : a * 3 = a
```

`ZMod2Poly.natCast_ZMod2` (lemma, [line 75](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L75))

```lean
lemma ZMod2Poly.natCast_ZMod2 (n : ℕ) : (n : Polynomial (ZMod 2)) = ((n % 2) : ℕ)
```

`ZMod2_value_eq_zero_or_one` (lemma, [line 79](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L79))

```lean
lemma ZMod2_value_eq_zero_or_one (x : ZMod 2) : x = 0 ∨ x = 1
```

`eq_of_associated_ZMod2` (lemma, [line 88](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L88))

> Helper: In Polynomial (ZMod 2), the only unit is 1.
> Therefore, if two polynomials are Associated (differ by a unit), they must be Equal.

```lean
lemma eq_of_associated_ZMod2 {a b : Polynomial (ZMod 2)} (h : Associated a b) : a = b
```

`ZMod2Poly.fintypeCard_eq_two` (lemma, [line 120](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L120))

```lean
lemma ZMod2Poly.fintypeCard_eq_two : Fintype.card (ZMod 2) = 2
```

`ZMod2Poly.frobenius` (lemma, [line 122](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L122))

```lean
lemma ZMod2Poly.frobenius (a b : Polynomial (ZMod 2)) : (a + b) ^ 2 = a ^ 2 + b ^ 2
```

`ZMod2Poly.euclidean_gcd_comm` (lemma, [line 137](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L137))

> **EuclideanDomain.gcd_comm for Polynomials**
> Commutativity: EuclideanDomain.gcd(a, b) = EuclideanDomain.gcd(b, a)
> Uses the fact that EuclideanDomain provides a GCDMonoid instance, which has gcd_comm'.

```lean
lemma ZMod2Poly.euclidean_gcd_comm (a b : Polynomial (ZMod 2)) :
    EuclideanDomain.gcd a b = EuclideanDomain.gcd b a
```

> ## Section 2: Polynomial Helper Lemmas

`Polynomial.exists_factor_le_64_of_reducible` (lemma, [line 156](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L156))

> Helper Lemma:
> If P is a degree 128 polynomial and is REDUCIBLE,
> then it must have an irreducible factor q with degree ≤ 64.

```lean
lemma Polynomial.exists_factor_le_64_of_reducible.{u} {R : Type u} [Field R] (P : Polynomial R)
    (h_deg : P.natDegree = 128) (h_red : ¬ Irreducible P) :
    ∃ q, Irreducible q ∧ q ∣ P ∧ q.natDegree ≤ 64
```

> ## Section 3: BitVec Operations

`BinaryField.BitVec.toNat_of_cast` (lemma, [line 230](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L230))

```lean
lemma BitVec.toNat_of_cast {w w2 : ℕ} (x : BitVec w) (h_width_eq : w = w2) :
    BitVec.toNat ((cast (h := by rw [h_width_eq]) x) : BitVec w2) = BitVec.toNat x
```

> ## Section 4: BitVec ↔ Polynomial Isomorphism

`BinaryField.toPoly` (definition, [line 243](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L243))

```lean
noncomputable def toPoly {w : Nat} (v : BitVec w) : (ZMod 2)[X]
```

`BinaryField.carryLessMul_unfold` (lemma, [line 248](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L248))

> Unfold `clMul` into an always-XOR form so that `toPoly_fold_xor`
> applies directly in the proof of `toPoly_clMul`.

```lean
lemma carryLessMul_unfold {v w : ℕ} (a b : BitVec v) :
    carryLessMul (w := w) a b = Fin.foldl v
      (fun acc i => acc ^^^ (if a.getLsbD i
        then (zeroExtendTo b : BitVec w) <<< (i : Nat) else 0)) (0 : BitVec w)
```

`BinaryField.clMul_unfold` (lemma, [line 259](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L259))

```lean
lemma clMul_unfold (a b : B128) :
    clMul a b = Fin.foldl 128
      (fun acc i => acc ^^^ (if a.getLsbD i
        then to256 b <<< (i : Nat) else 0)) (0 : B256)
```

`BinaryField.toPoly_one_shiftLeft` (lemma, [line 266](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L266))

> A single set bit at position `n` denotes the monomial `X^n`.

```lean
lemma toPoly_one_shiftLeft {w : Nat} (n : Nat) (h : n < w) :
    toPoly (1 <<< n : BitVec w) = X^n
```

`BinaryField.toPoly_one_eq_one` (lemma, [line 305](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L305))

```lean
lemma toPoly_one_eq_one {w : Nat} (h_w_pos : w > 0) : toPoly (BitVec.ofNat w 1) = 1
```

`BinaryField.toPoly_zero_eq_zero` (lemma, [line 332](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L332))

```lean
lemma toPoly_zero_eq_zero {w : Nat} : toPoly (BitVec.ofNat w 0) = 0
```

`BinaryField.toPoly_ne_zero_iff_ne_zero` (lemma, [line 339](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L339))

```lean
lemma toPoly_ne_zero_iff_ne_zero {w : Nat} (v : BitVec w) :
    toPoly v ≠ 0 ↔ v ≠ 0
```

`BinaryField.toPoly_degree_lt_w` (lemma, [line 403](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L403))

> ToPoly degree is less than width

```lean
lemma toPoly_degree_lt_w {w : ℕ} (h_w_pos : w > 0) (v : BitVec w) :
    (toPoly v).degree < w
```

`BinaryField.toPoly_degree_of_lt_two_pow` (lemma, [line 425](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L425))

```lean
lemma toPoly_degree_of_lt_two_pow {w d : ℕ} (v : BitVec w)
    (hv : v.toNat < 2 ^ d) : (toPoly v).degree < d
```

`BinaryField.BitVec_lt_two_pow_of_toPoly_degree_lt` (lemma, [line 455](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L455))

```lean
lemma BitVec_lt_two_pow_of_toPoly_degree_lt {w d : ℕ} (v : BitVec w)
    (h_toPoly_degree_lt : (toPoly v).degree < d) : v.toNat < 2 ^ d
```

`BinaryField.toPoly_xor` (lemma, [line 504](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L504))

```lean
lemma toPoly_xor {w} (a b : BitVec w) : toPoly (a ^^^ b) = toPoly a + toPoly b
```

`BinaryField.toPoly_fold_xor` (lemma, [line 553](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L553))

> The "Homomorphism" Lemma.
> Since toPoly(a ^^^ b) = toPoly a + toPoly b,
> toPoly preserves the structure from Fold-XOR to Sum-Add.
>
> lemma toPoly_fold_xor {α} {w} (s : Finset α) (f : α → (BitVec w)) :
>     toPoly (s.fold BitVec.xor 0 f) = ∑ i ∈ s, toPoly (f i) := by
>   induction s using Finset.cons_induction with
>   | empty =>
>     simp only [BitVec.ofNat_eq_ofNat, Finset.fold_empty, Finset.sum_empty]
>     rw [toPoly_zero_eq_zero]
>   | cons x s h_not_mem ih =>
>     rw [Finset.fold_cons, Finset.sum_cons]
>     change toPoly (f x ^^^ s.fold BitVec.xor 0 f) = toPoly (f x) + ∑ i ∈ s, toPoly (f i)
>     rw [toPoly_xor]
>     rw [ih]

```lean
lemma toPoly_fold_xor {w : Nat} (n : Nat) (f : Nat → (BitVec w)) :
    toPoly (Fin.foldl n (fun acc i => acc ^^^ (f i)) 0) =
    ∑ i ∈ (Finset.range n), toPoly (f i)
```

`BinaryField.toPoly_128_extend_256` (lemma, [line 565](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L565))

```lean
lemma toPoly_128_extend_256 (a : B128) :
    toPoly (to256 a) = toPoly a
```

`BinaryField.BitVec_getLsb_eq_false_of_toNat_lt_two_pow` (theorem, [line 588](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L588))

```lean
theorem BitVec_getLsb_eq_false_of_toNat_lt_two_pow {w d : ℕ} (a : BitVec w) (ha : a.toNat < 2 ^ d)
    (i : Fin w) (hd : d ≤ (i : ℕ)) : a.getLsb i = false
```

`BinaryField.BitVec_getElem_eq_false_of_toNat_lt_two_pow` (theorem, [line 596](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L596))

```lean
theorem BitVec_getElem_eq_false_of_toNat_lt_two_pow {w d : ℕ} (a : BitVec w) (ha : a.toNat < 2 ^ d)
    (n : ℕ) (hn : n < w) (hd : d ≤ n) : a[n] = false
```

`BinaryField.BitVec_getLsb_shiftLeft` (theorem, [line 603](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L603))

```lean
theorem BitVec_getLsb_shiftLeft {w : ℕ} (a : BitVec w) (shift n : ℕ) (hn : n < w) :
    (a <<< shift).getLsb ⟨n, hn⟩ =
      (if _ : shift ≤ n then
          a.getLsb ⟨n - shift, lt_of_le_of_lt (Nat.sub_le n shift) hn⟩
        else false)
```

`BinaryField.toPoly_coeff` (theorem, [line 618](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L618))

```lean
theorem toPoly_coeff {w : ℕ} (v : BitVec w) (n : ℕ) :
    (toPoly v).coeff n =
      (if h : n < w then (if v.getLsb ⟨n, h⟩ = true then (1 : ZMod 2) else 0) else 0)
```

`BinaryField.toPoly_shiftLeft_no_overflow` (theorem, [line 676](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L676))

```lean
theorem toPoly_shiftLeft_no_overflow {w d : ℕ} (a : BitVec w) (ha : a.toNat < 2 ^ d) {shift : ℕ}
    (h_no_overflow : d + shift ≤ w) : toPoly (a <<< shift) = (toPoly a) * X^shift
```

`BinaryField.toPoly_zeroExtendTo` (lemma, [line 705](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L705))

> Widening does not change the polynomial denoted.

```lean
lemma toPoly_zeroExtendTo {v w : ℕ} (a : BitVec v) (h : v ≤ w) :
    toPoly (zeroExtendTo (w := w) a) = toPoly a
```

`BinaryField.toPoly_carryLessMul` (lemma, [line 723](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L723))

> `carryLessMul` denotes the product of the denoted polynomials, provided the result
> width admits the full product.

```lean
lemma toPoly_carryLessMul {v w : ℕ} (a b : BitVec v) (h : v + v ≤ w) :
    toPoly (carryLessMul (w := w) a b) = toPoly a * toPoly b
```

`BinaryField.toPoly_clMul` (lemma, [line 746](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L746))

```lean
lemma toPoly_clMul (a b : B128) :
    toPoly (clMul a b) = toPoly a * toPoly b
```

> ### Splitting a bit vector

`BinaryField.toPoly_eq_range` (lemma, [line 753](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L753))

> `toPoly` as a sum over the set bits, indexed by `ℕ`.

```lean
lemma toPoly_eq_range {w : ℕ} (v : BitVec w) :
    toPoly v = ∑ i ∈ Finset.range w, if v.toNat.testBit i then (X : (ZMod 2)[X]) ^ i else 0
```

`BinaryField.toPoly_split` (lemma, [line 761](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L761))

> Splitting the denoted polynomial at bit position `n` into a high part carrying `X ^ n`
> and a low part.

```lean
lemma toPoly_split {w : ℕ} (v : BitVec w) (n : ℕ) (hn : n ≤ w) :
    toPoly v
      = (∑ i ∈ Finset.range (w - n),
          if v.toNat.testBit (n + i) then (X : (ZMod 2)[X]) ^ i else 0) * X ^ n
        + ∑ i ∈ Finset.range n, if v.toNat.testBit i then (X : (ZMod 2)[X]) ^ i else 0
```

`BinaryField.chain_step` (lemma, [line 779](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L779))

> Helper lemma to chain the modular squaring steps.

```lean
lemma chain_step {P : Polynomial (ZMod 2)} (hP : P ≠ 0) {k : ℕ}
    {prev next : Polynomial (ZMod 2)} {q_val : B128}
    (h_prev : X ^ (2 ^ k) % P = prev % P)
    (h_step : prev ^ 2 = (toPoly (to256 q_val)) * P + next) :
    X^(2^(k+1)) % P = next % P
```

> ## Section 5: GCD Verification Helpers

`BinaryField.gcd_eq_gcd_next_step` (lemma, [line 802](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L802))

```lean
lemma gcd_eq_gcd_next_step {a b q r : Polynomial (ZMod 2)} (hb : b ≠ 0) (h : a = q * b + r) :
    EuclideanDomain.gcd a b = EuclideanDomain.gcd b r
```

`BinaryField.gcd_one_zero` (lemma, [line 814](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean#L814))

```lean
lemma gcd_one_zero : EuclideanDomain.gcd (1 : Polynomial (ZMod 2)) 0 = 1
```

## Depends on

- [Binary polynomial word arithmetic](common-2/arithmetic.md)

## Proof depends on

- [Frobenius polynomial identities](../../data/polynomial/frobenius.md)
- [Canonical Euclidean Domains](../../data/ringtheory/canonicaleuclideandomain.md)

## Sources

- [CompPoly/Fields/Binary/Common.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Common.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Binary.Common.json)
