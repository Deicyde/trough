---
catalog: module
lean: CompPoly.CPolynomial.equiv_refl, CompPoly.CPolynomial.equiv_symm, CompPoly.CPolynomial.equiv_trans, CompPoly.CPolynomial.instEquivalenceEquiv, CompPoly.CPolynomial.Raw.instSetoidCPolynomial, CompPoly.CPolynomial.QuotientCPolynomial, CompPoly.CPolynomial.QuotientCPolynomial.eq_to_equiv, CompPoly.CPolynomial.QuotientCPolynomial.smul_zero_equiv, CompPoly.CPolynomial.QuotientCPolynomial.add_equiv, CompPoly.CPolynomial.QuotientCPolynomial.mulPowX_equiv, CompPoly.CPolynomial.QuotientCPolynomial.add_zero_equiv, CompPoly.CPolynomial.QuotientCPolynomial.mulPowX_zero_equiv, CompPoly.CPolynomial.QuotientCPolynomial.mulStep, CompPoly.CPolynomial.QuotientCPolynomial.mulStep_equiv, CompPoly.CPolynomial.QuotientCPolynomial.mulStep_zero, CompPoly.CPolynomial.QuotientCPolynomial.foldl_mulStep_zeros, CompPoly.CPolynomial.QuotientCPolynomial.zipIdx_trim_append, CompPoly.CPolynomial.QuotientCPolynomial.mul_trim_equiv, CompPoly.CPolynomial.QuotientCPolynomial.mul_equiv, CompPoly.CPolynomial.QuotientCPolynomial.mul_equiv₂, CompPoly.CPolynomial.QuotientCPolynomial.addDescending, CompPoly.CPolynomial.QuotientCPolynomial.add_descends, CompPoly.CPolynomial.QuotientCPolynomial.add, CompPoly.CPolynomial.QuotientCPolynomial.smulDescending, CompPoly.CPolynomial.QuotientCPolynomial.smul_descends, CompPoly.CPolynomial.QuotientCPolynomial.smul, CompPoly.CPolynomial.QuotientCPolynomial.nsmulDescending, CompPoly.CPolynomial.QuotientCPolynomial.nsmul_descends, CompPoly.CPolynomial.QuotientCPolynomial.nsmul, CompPoly.CPolynomial.QuotientCPolynomial.negDescending, CompPoly.CPolynomial.QuotientCPolynomial.neg_descends, CompPoly.CPolynomial.QuotientCPolynomial.neg, CompPoly.CPolynomial.QuotientCPolynomial.subDescending, CompPoly.CPolynomial.QuotientCPolynomial.sub_descends, CompPoly.CPolynomial.QuotientCPolynomial.sub, CompPoly.CPolynomial.QuotientCPolynomial.mulPowXDescending, CompPoly.CPolynomial.QuotientCPolynomial.mulPowX_descends, CompPoly.CPolynomial.QuotientCPolynomial.mulPowX, CompPoly.CPolynomial.QuotientCPolynomial.mulX, CompPoly.CPolynomial.QuotientCPolynomial.mulDescending, CompPoly.CPolynomial.QuotientCPolynomial.mul_descends, CompPoly.CPolynomial.QuotientCPolynomial.mul, CompPoly.CPolynomial.QuotientCPolynomial.powDescending, CompPoly.CPolynomial.QuotientCPolynomial.pow_descends, CompPoly.CPolynomial.QuotientCPolynomial.pow, CompPoly.CPolynomial.QuotientCPolynomial.add_assoc, CompPoly.CPolynomial.QuotientCPolynomial.zero_add_equiv, CompPoly.CPolynomial.QuotientCPolynomial.zero_add, CompPoly.CPolynomial.QuotientCPolynomial.add_zero, CompPoly.CPolynomial.QuotientCPolynomial.add_comm, CompPoly.CPolynomial.QuotientCPolynomial.nsmul_zero, CompPoly.CPolynomial.QuotientCPolynomial.nsmul_succ, CompPoly.CPolynomial.QuotientCPolynomial.neg_add_cancel, CompPoly.CPolynomial.QuotientCPolynomial.sub_eq_add_neg, CompPoly.CPolynomial.QuotientCPolynomial.mul_assoc, CompPoly.CPolynomial.QuotientCPolynomial.one_mul, CompPoly.CPolynomial.QuotientCPolynomial.mul_one, CompPoly.CPolynomial.QuotientCPolynomial.zero_mul, CompPoly.CPolynomial.QuotientCPolynomial.mul_zero, CompPoly.CPolynomial.QuotientCPolynomial.mul_add, CompPoly.CPolynomial.QuotientCPolynomial.add_mul, CompPoly.CPolynomial.QuotientCPolynomial.npow_zero, CompPoly.CPolynomial.QuotientCPolynomial.const_sum, CompPoly.CPolynomial.QuotientCPolynomial.pow_succ_left, CompPoly.CPolynomial.QuotientCPolynomial.commute_pow_self, CompPoly.CPolynomial.QuotientCPolynomial.npow_succ, CompPoly.CPolynomial.QuotientCPolynomial.mul_comm
statement: formalized
proof: formalized
---

# Quotient of Univariate Polynomials

`CompPoly.Univariate.Quotient.Core`, in [CompPoly/Univariate/Quotient/Core.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean), by Quang Dao, Gregor Mitscha-Baude, Derek Sorensen.

> This file defines `QuotientCPolynomial R`, the quotient of `CPolynomial.Raw R` by the equivalence
> relation that identifies polynomials with the same coefficients (allowing zero-padding).
> This quotient is intended to be equivalent to mathlib's `Polynomial R`.
>
> Operations on `CPolynomial.Raw` (addition, multiplication, etc.) are shown to respect the
> equivalence relation and thus descend to the quotient.

`CompPoly.CPolynomial.equiv_refl` (theorem, [line 37](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L37))

> Reflexivity of the equivalence relation.

```lean
theorem equiv_refl [Zero Q] (p : CPolynomial.Raw Q) : equiv p p
```

`CompPoly.CPolynomial.equiv_symm` (theorem, [line 41](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L41))

> Symmetry of the equivalence relation.

```lean
theorem equiv_symm [Zero Q] {p q : CPolynomial.Raw Q} : equiv p q → equiv q p
```

`CompPoly.CPolynomial.equiv_trans` (theorem, [line 47](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L47))

> Transitivity of the equivalence relation.

```lean
theorem equiv_trans [Zero Q] {p q r : CPolynomial.Raw Q} :
    Trim.equiv p q → equiv q r → equiv p r
```

`CompPoly.CPolynomial.instEquivalenceEquiv` (theorem, [line 52](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L52))

> The `CPolynomial.Raw.equiv` is indeed an equivalence relation.

```lean
theorem instEquivalenceEquiv [Zero R] : Equivalence (equiv (R := R))
```

`CompPoly.CPolynomial.Raw.instSetoidCPolynomial` (instance, [line 58](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L58))

> The `Setoid` instance for `CPolynomial.Raw R` induced by `CPolynomial.Raw.equiv`.

```lean
instance Raw.instSetoidCPolynomial [Zero R] : Setoid (CPolynomial.Raw R)
```

`CompPoly.CPolynomial.QuotientCPolynomial` (definition, [line 67](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L67))

> The quotient of `CPolynomial.Raw R` by coefficient-wise equivalence.
>
> This quotient identifies polynomials that differ only by trailing zeros, and is intended
> to be equivalent to mathlib's `Polynomial R`.

```lean
def QuotientCPolynomial (R : Type*) [Zero R]
```

`CompPoly.CPolynomial.QuotientCPolynomial.eq_to_equiv` (lemma, [line 75](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L75))

> Convert propositional equality to equivalence.

```lean
lemma eq_to_equiv [Zero R] (p q : CPolynomial.Raw R) : p = q → p ≈ q
```

`CompPoly.CPolynomial.QuotientCPolynomial.smul_zero_equiv` (lemma, [line 80](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L80))

> Scalar multiplication by 0 is equivalent to the zero polynomial.

```lean
lemma smul_zero_equiv {R : Type*} [Semiring R] (p : CPolynomial.Raw R) :
    (smul 0 p) ≈ 0
```

`CompPoly.CPolynomial.QuotientCPolynomial.add_equiv` (lemma, [line 88](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L88))

> Addition respects the equivalence relation.

```lean
lemma add_equiv {R : Type*} [Semiring R] [BEq R] [LawfulBEq R]
    (p1 p2 q1 q2 : CPolynomial.Raw R)
  (hp : equiv p1 p2) (hq : equiv q1 q2) :
  equiv (p1.add q1) (p2.add q2)
```

`CompPoly.CPolynomial.QuotientCPolynomial.mulPowX_equiv` (lemma, [line 100](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L100))

> Multiplication by `X^i` respects the equivalence relation.

```lean
lemma mulPowX_equiv {R : Type*} [Zero R]
    (i : ℕ) (p q : CPolynomial.Raw R) (h : equiv p q) :
  equiv (mulPowX i p) (mulPowX i q)
```

`CompPoly.CPolynomial.QuotientCPolynomial.add_zero_equiv` (lemma, [line 112](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L112))

> Adding a polynomial equivalent to zero acts as the identity.

```lean
lemma add_zero_equiv {R : Type*} [Semiring R] [BEq R] [LawfulBEq R]
    (p q : CPolynomial.Raw R) (hq : equiv q 0) :
  equiv (add p q) p
```

`CompPoly.CPolynomial.QuotientCPolynomial.mulPowX_zero_equiv` (lemma, [line 123](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L123))

> Multiplying the zero polynomial by `X^i` results in a polynomial equivalent to zero.

```lean
lemma mulPowX_zero_equiv {R : Type*} [Zero R]
    (i : ℕ) : equiv (mulPowX i (0 : CPolynomial.Raw R)) 0
```

`CompPoly.CPolynomial.QuotientCPolynomial.mulStep` (definition, [line 131](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L131))

> A single step in polynomial multiplication: add `(coefficient * q) * X^power` to accumulator.

```lean
def mulStep {R : Type*} [Semiring R] [BEq R] [LawfulBEq R]
    (q : CPolynomial.Raw R) (acc : CPolynomial.Raw R) (x : R × ℕ) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.QuotientCPolynomial.mulStep_equiv` (lemma, [line 136](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L136))

> The multiplication step respects equivalence of the accumulator.

```lean
lemma mulStep_equiv {R : Type*} [Semiring R] [BEq R] [LawfulBEq R]
    (q : CPolynomial.Raw R) (acc1 acc2 : CPolynomial.Raw R) (x : R × ℕ)
  (h : equiv acc1 acc2) :
  equiv (mulStep q acc1 x) (mulStep q acc2 x)
```

`CompPoly.CPolynomial.QuotientCPolynomial.mulStep_zero` (lemma, [line 143](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L143))

> The multiplication step with a zero coefficient acts as the identity modulo equivalence.

```lean
lemma mulStep_zero {R : Type*} [Semiring R] [BEq R] [LawfulBEq R]
    (q : CPolynomial.Raw R) (acc : CPolynomial.Raw R) (i : ℕ) :
  equiv (mulStep q acc (0, i)) acc
```

`CompPoly.CPolynomial.QuotientCPolynomial.foldl_mulStep_zeros` (lemma, [line 152](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L152))

> Folding `mulStep` over a list of zero coefficients preserves equivalence.

```lean
lemma foldl_mulStep_zeros {R : Type*} [Semiring R] [BEq R] [LawfulBEq R]
    (q : CPolynomial.Raw R) (acc : CPolynomial.Raw R) (l : List (R × ℕ))
  (hl : ∀ x ∈ l, x.1 = 0) :
  equiv (l.foldl (mulStep q) acc) acc
```

`CompPoly.CPolynomial.QuotientCPolynomial.zipIdx_trim_append` (lemma, [line 168](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L168))

> The `zipIdx` of a polynomial is the `zipIdx` of its trim followed by zero coefficients.

```lean
lemma zipIdx_trim_append {R : Type*} [Zero R] [BEq R] [LawfulBEq R]
    (p : CPolynomial.Raw R) :
    ∃ l, p.zipIdx.toList = p.trim.zipIdx.toList ++ l ∧ ∀ x ∈ l, x.1 = 0
```

`CompPoly.CPolynomial.QuotientCPolynomial.mul_trim_equiv` (lemma, [line 199](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L199))

> Multiplication by a trimmed polynomial is equivalent to multiplication by the original.

```lean
lemma mul_trim_equiv [Semiring R] [BEq R] [LawfulBEq R] (a b : CPolynomial.Raw R) :
    a.mul b ≈ a.trim.mul b
```

`CompPoly.CPolynomial.QuotientCPolynomial.mul_equiv` (lemma, [line 215](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L215))

> Multiplication is well-defined on the left with respect to equivalence.

```lean
lemma mul_equiv [Semiring R] [BEq R] [LawfulBEq R] (a₁ a₂ b : CPolynomial.Raw R) :
    a₁ ≈ a₂ → a₁.mul b ≈ a₂.mul b
```

`CompPoly.CPolynomial.QuotientCPolynomial.mul_equiv₂` (lemma, [line 224](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L224))

> Multiplication is well-defined on the right with respect to equivalence.

```lean
lemma mul_equiv₂ [Semiring R] [BEq R] [LawfulBEq R] (a b₁ b₂ : CPolynomial.Raw R) :
    b₁ ≈ b₂ → a.mul b₁ ≈ a.mul b₂
```

`CompPoly.CPolynomial.QuotientCPolynomial.addDescending` (definition, [line 249](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L249))

> Helper function showing addition descends to the quotient.

```lean
def addDescending [Semiring R] [BEq R] [LawfulBEq R]
    (p q : CPolynomial.Raw R) : QuotientCPolynomial R
```

`CompPoly.CPolynomial.QuotientCPolynomial.add_descends` (lemma, [line 253](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L253))

```lean
lemma add_descends [Semiring R] [BEq R] [LawfulBEq R] (a₁ b₁ a₂ b₂ : CPolynomial.Raw R) :
    equiv a₁ a₂ → equiv b₁ b₂ → addDescending a₁ b₁ = addDescending a₂ b₂
```

`CompPoly.CPolynomial.QuotientCPolynomial.add` (definition, [line 267](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L267))

> Addition on the quotient.

```lean
def add {R : Type*} [Semiring R] [BEq R] [LawfulBEq R] (p q : QuotientCPolynomial R) :
    QuotientCPolynomial R
```

`CompPoly.CPolynomial.QuotientCPolynomial.smulDescending` (definition, [line 272](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L272))

> Helper function showing scalar multiplication descends to the quotient.

```lean
def smulDescending [Semiring R] (r : R) (p : CPolynomial.Raw R) : QuotientCPolynomial R
```

`CompPoly.CPolynomial.QuotientCPolynomial.smul_descends` (lemma, [line 275](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L275))

```lean
lemma smul_descends [Semiring R] (r : R) (p₁ p₂ : CPolynomial.Raw R) :
    equiv p₁ p₂ → smulDescending r p₁ = smulDescending r p₂
```

`CompPoly.CPolynomial.QuotientCPolynomial.smul` (definition, [line 285](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L285))

> Scalar multiplication on the quotient.

```lean
def smul {R : Type*} [Semiring R] (r : R) (p : QuotientCPolynomial R) :
    QuotientCPolynomial R
```

`CompPoly.CPolynomial.QuotientCPolynomial.nsmulDescending` (definition, [line 290](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L290))

> Helper function showing natural number scalar multiplication descends to the quotient.

```lean
def nsmulDescending [Semiring R] [BEq R] (n : ℕ) (p : CPolynomial.Raw R) : QuotientCPolynomial R
```

`CompPoly.CPolynomial.QuotientCPolynomial.nsmul_descends` (lemma, [line 293](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L293))

```lean
lemma nsmul_descends [Semiring R] [BEq R] [LawfulBEq R] (n : ℕ)
    (p₁ p₂ : CPolynomial.Raw R) :
    equiv p₁ p₂ → nsmulDescending n p₁ = nsmulDescending n p₂
```

`CompPoly.CPolynomial.QuotientCPolynomial.nsmul` (definition, [line 308](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L308))

> Natural number scalar multiplication on the quotient.

```lean
def nsmul {R : Type*} [Semiring R] [BEq R] [LawfulBEq R] (n : ℕ)
    (p : QuotientCPolynomial R) :
    QuotientCPolynomial R
```

`CompPoly.CPolynomial.QuotientCPolynomial.negDescending` (definition, [line 314](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L314))

> Helper function showing negation descends to the quotient.

```lean
def negDescending [Zero R] [Neg R] (p : CPolynomial.Raw R) : QuotientCPolynomial R
```

`CompPoly.CPolynomial.QuotientCPolynomial.neg_descends` (lemma, [line 317](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L317))

```lean
lemma neg_descends [NegZeroClass R] (a b : CPolynomial.Raw R) :
    equiv a b → negDescending a = negDescending b
```

`CompPoly.CPolynomial.QuotientCPolynomial.neg` (definition, [line 328](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L328))

> Negation on the quotient.

```lean
def neg {R : Type*} [NegZeroClass R] (p : QuotientCPolynomial R) : QuotientCPolynomial R
```

`CompPoly.CPolynomial.QuotientCPolynomial.subDescending` (definition, [line 332](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L332))

> Helper function showing subtraction descends to the quotient.

```lean
def subDescending [Ring R] [BEq R] [LawfulBEq R]
    (p q : CPolynomial.Raw R) : QuotientCPolynomial R
```

`CompPoly.CPolynomial.QuotientCPolynomial.sub_descends` (lemma, [line 336](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L336))

```lean
lemma sub_descends [Ring R] [BEq R] [LawfulBEq R] (a₁ b₁ a₂ b₂ : CPolynomial.Raw R) :
    equiv a₁ a₂ → equiv b₁ b₂ → subDescending a₁ b₁ = subDescending a₂ b₂
```

`CompPoly.CPolynomial.QuotientCPolynomial.sub` (definition, [line 352](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L352))

> Subtraction on the quotient.

```lean
def sub {R : Type*} [Ring R] [BEq R] [LawfulBEq R] (p q : QuotientCPolynomial R) :
    QuotientCPolynomial R
```

`CompPoly.CPolynomial.QuotientCPolynomial.mulPowXDescending` (definition, [line 357](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L357))

> Helper function showing multiplication by `X^i` descends to the quotient.

```lean
def mulPowXDescending [Zero R] (i : ℕ) (p : CPolynomial.Raw R) : QuotientCPolynomial R
```

`CompPoly.CPolynomial.QuotientCPolynomial.mulPowX_descends` (lemma, [line 360](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L360))

```lean
lemma mulPowX_descends [Zero R] (i : ℕ) (p₁ p₂ : CPolynomial.Raw R) :
    equiv p₁ p₂ → mulPowXDescending i p₁ = mulPowXDescending i p₂
```

`CompPoly.CPolynomial.QuotientCPolynomial.mulPowX` (definition, [line 369](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L369))

> Multiplication by `X^i` on the quotient.

```lean
def mulPowX {R : Type*} [Zero R] (i : ℕ) (p : QuotientCPolynomial R) :
    QuotientCPolynomial R
```

`CompPoly.CPolynomial.QuotientCPolynomial.mulX` (definition, [line 375](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L375))

> Multiplication by `X` on the quotient (equivalent to `mulPowX 1`).

```lean
def mulX [Zero R] (p : QuotientCPolynomial R) : QuotientCPolynomial R
```

`CompPoly.CPolynomial.QuotientCPolynomial.mulDescending` (definition, [line 378](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L378))

> Helper function showing multiplication descends to the quotient.

```lean
def mulDescending [Semiring R] [BEq R] [LawfulBEq R]
    (p q : CPolynomial.Raw R) : QuotientCPolynomial R
```

`CompPoly.CPolynomial.QuotientCPolynomial.mul_descends` (lemma, [line 382](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L382))

```lean
lemma mul_descends [Semiring R] [BEq R] [LawfulBEq R] (a₁ b₁ a₂ b₂ : CPolynomial.Raw R) :
    equiv a₁ a₂ → equiv b₁ b₂ → mulDescending a₁ b₁ = mulDescending a₂ b₂
```

`CompPoly.CPolynomial.QuotientCPolynomial.mul` (definition, [line 393](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L393))

> Multiplication on the quotient.

```lean
def mul {R : Type*} [Semiring R] [BEq R] [LawfulBEq R] (p q : QuotientCPolynomial R) :
    QuotientCPolynomial R
```

`CompPoly.CPolynomial.QuotientCPolynomial.powDescending` (definition, [line 398](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L398))

> Helper function showing exponentiation descends to the quotient.

```lean
def powDescending [Semiring R] [BEq R] (p : CPolynomial.Raw R) (n : ℕ) :
    QuotientCPolynomial R
```

`CompPoly.CPolynomial.QuotientCPolynomial.pow_descends` (lemma, [line 402](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L402))

```lean
lemma pow_descends [Semiring R] [BEq R] [LawfulBEq R] (n : ℕ) (p₁ p₂ : CPolynomial.Raw R) :
    equiv p₁ p₂ → powDescending p₁ n = powDescending p₂ n
```

`CompPoly.CPolynomial.QuotientCPolynomial.pow` (definition, [line 422](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L422))

> Exponentiation on the quotient.

```lean
def pow {R : Type*} [Semiring R] [BEq R] [LawfulBEq R]
    (p : QuotientCPolynomial R) (n : ℕ) :
    QuotientCPolynomial R
```

`CompPoly.CPolynomial.QuotientCPolynomial.add_assoc` (lemma, [line 451](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L451))

```lean
lemma add_assoc : ∀ (a b c : QuotientCPolynomial R), a + b + c = a + (b + c)
```

`CompPoly.CPolynomial.QuotientCPolynomial.zero_add_equiv` (lemma, [line 460](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L460))

```lean
lemma zero_add_equiv (p : CPolynomial.Raw R) : 0 + p ≈ p
```

`CompPoly.CPolynomial.QuotientCPolynomial.zero_add` (lemma, [line 469](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L469))

```lean
lemma zero_add : ∀ (a : QuotientCPolynomial R), 0 + a = a
```

`CompPoly.CPolynomial.QuotientCPolynomial.add_zero` (lemma, [line 477](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L477))

```lean
lemma add_zero : ∀ (a : QuotientCPolynomial R), a + 0 = a
```

`CompPoly.CPolynomial.QuotientCPolynomial.add_comm` (lemma, [line 489](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L489))

```lean
lemma add_comm : ∀ (a b : QuotientCPolynomial R), a + b = b + a
```

`CompPoly.CPolynomial.QuotientCPolynomial.nsmul_zero` (lemma, [line 498](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L498))

```lean
lemma nsmul_zero : ∀ (x : QuotientCPolynomial R),
    QuotientCPolynomial.nsmul 0 x = 0
```

`CompPoly.CPolynomial.QuotientCPolynomial.nsmul_succ` (lemma, [line 508](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L508))

```lean
lemma nsmul_succ : ∀ (n : ℕ) (x : QuotientCPolynomial R),
    QuotientCPolynomial.nsmul (n + 1) x = QuotientCPolynomial.nsmul n x + x
```

`CompPoly.CPolynomial.QuotientCPolynomial.neg_add_cancel` (lemma, [line 533](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L533))

```lean
lemma neg_add_cancel : ∀ (a : QuotientCPolynomial R), -a + a = 0
```

`CompPoly.CPolynomial.QuotientCPolynomial.sub_eq_add_neg` (lemma, [line 542](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L542))

```lean
lemma sub_eq_add_neg : ∀ (a b : QuotientCPolynomial R), a - b = a + -b
```

`CompPoly.CPolynomial.QuotientCPolynomial.mul_assoc` (lemma, [line 569](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L569))

```lean
lemma mul_assoc (a b c : QuotientCPolynomial R) :
    a * b * c = a * (b * c)
```

`CompPoly.CPolynomial.QuotientCPolynomial.one_mul` (lemma, [line 576](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L576))

```lean
lemma one_mul : ∀ (a : QuotientCPolynomial R), 1 * a = a
```

`CompPoly.CPolynomial.QuotientCPolynomial.mul_one` (lemma, [line 585](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L585))

```lean
lemma mul_one : ∀ (a : QuotientCPolynomial R), a * 1 = a
```

`CompPoly.CPolynomial.QuotientCPolynomial.zero_mul` (lemma, [line 594](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L594))

```lean
lemma zero_mul : ∀ (a : QuotientCPolynomial R), 0 * a = 0
```

`CompPoly.CPolynomial.QuotientCPolynomial.mul_zero` (lemma, [line 602](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L602))

```lean
lemma mul_zero : ∀ (a : QuotientCPolynomial R), a * 0 = 0
```

`CompPoly.CPolynomial.QuotientCPolynomial.mul_add` (lemma, [line 610](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L610))

```lean
lemma mul_add : ∀ (a b c : QuotientCPolynomial R),
    a * (b + c) = a * b + a * c
```

`CompPoly.CPolynomial.QuotientCPolynomial.add_mul` (lemma, [line 619](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L619))

```lean
lemma add_mul : ∀ (a b c : QuotientCPolynomial R), (a + b) * c = a * c + b * c
```

`CompPoly.CPolynomial.QuotientCPolynomial.npow_zero` (lemma, [line 627](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L627))

```lean
lemma npow_zero : ∀ (x : QuotientCPolynomial R), x.pow 0 = 1
```

`CompPoly.CPolynomial.QuotientCPolynomial.const_sum` (lemma, [line 635](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L635))

```lean
lemma const_sum (r s : R) : (C r).add (C s) ≈ C (r + s)
```

`CompPoly.CPolynomial.QuotientCPolynomial.pow_succ_left` (lemma, [line 644](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L644))

```lean
lemma pow_succ_left (n : ℕ) (x : QuotientCPolynomial R) :
    x.pow (n + 1) = x * x.pow n
```

`CompPoly.CPolynomial.QuotientCPolynomial.commute_pow_self` (lemma, [line 658](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L658))

```lean
lemma commute_pow_self (n : ℕ) (x : QuotientCPolynomial R) :
    x * x.pow n = x.pow n * x
```

`CompPoly.CPolynomial.QuotientCPolynomial.npow_succ` (lemma, [line 667](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L667))

```lean
lemma npow_succ : ∀ (n : ℕ) (x : QuotientCPolynomial R), x.pow (n + 1) = x.pow n * x
```

`CompPoly.CPolynomial.QuotientCPolynomial.mul_comm` (lemma, [line 708](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean#L708))

```lean
lemma mul_comm : ∀ (a b : QuotientCPolynomial R), a * b = b * a
```

## Depends on

- [Raw Univariate Polynomial Operations](../raw/ops.md)

## Proof depends on

- [Raw Univariate Polynomial Proofs](../raw/proofs.md)

## Sources

- [CompPoly/Univariate/Quotient/Core.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Quotient/Core.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.Quotient.Core.json)
