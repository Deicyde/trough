---
catalog: module
lean: CPoly.Lawful, CPoly.instEmptyCol, CPoly.Lawful.getElem?_eq_val_getElem?, CPoly.Lawful.mem_iff_cast, CPoly.Lawful.mem_iff, CPoly.Lawful.getElem?_ne_some_zero, CPoly.Lawful.getD_getElem?_ne_zero_of_mem, CPoly.Lawful.getElem_eq_getElem, CPoly.Lawful.fromUnlawful, CPoly.Lawful.grind_fromUnlawful_congr, CPoly.Lawful.C, CPoly.Lawful.instOfNat_zero, CPoly.Lawful.zero_def, CPoly.Lawful.instOfNat, CPoly.Lawful.C_zero, CPoly.Lawful.C_zero', CPoly.Lawful.zero_eq_zero, CPoly.Lawful.zero_eq_empty, CPoly.Lawful.not_mem_C_zero, CPoly.Lawful.not_mem_zero, CPoly.Lawful.cast_fromUnlawful, CPoly.Lawful.extend, CPoly.Lawful.add, CPoly.Lawful.grind_add_skip, CPoly.Lawful.grind_add_skip_aggressive, CPoly.Lawful.mul, CPoly.Lawful.npow, CPoly.Lawful.npowBySq, CPoly.Lawful.monomials, CPoly.Lawful.NzConst, CPoly.Lawful.mem_monomials_iff, CPoly.Lawful.fromUnlawful_cast, CPoly.Lawful.neg, CPoly.Lawful.sub, CPoly.Lawful.instDecidableEq, CPoly.Lawful.instBEq, CPoly.Lawful.instLawfulBEq, CPoly.Lawful.X, CPoly.Lawful.align, CPoly.Lawful.liftPoly, CPoly.Lawful.polyCoe
statement: formalized
proof: formalized
---

# 'Lawful' finite supports

`CompPoly.Multivariate.Lawful`, in [CompPoly/Multivariate/Lawful.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean), by Frantisek Silvasi.

> This file defines the `Lawful` subtype, which consists of `Unlawful` polynomials
> where all stored coefficients are guaranteed to be non-zero. This provides a canonical
> representation (similar to `Finsupp`) and is the primary representation used for
> computable multivariate polynomials.
>
> ## Main definitions
>
> * `CPoly.Lawful n R`: The subtype of `Unlawful n R` with no zero coefficients.

`CPoly.Lawful` (definition, [line 35](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L35))

> The subtype of polynomials with no zero coefficients.

```lean
def Lawful (n : ℕ) (R : Type*) [Zero R] : Type _
```

`CPoly.instEmptyCol` (instance, [line 43](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L43))

```lean
instance instEmptyCol : EmptyCollection (Lawful n R)
```

`CPoly.Lawful.getElem?_eq_val_getElem?` (lemma, [line 67](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L67))

```lean
lemma getElem?_eq_val_getElem? : p[m]? = p.1[m]?
```

`CPoly.Lawful.mem_iff_cast` (lemma, [line 70](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L70))

```lean
lemma mem_iff_cast : x ∈ p.1 ↔ x ∈ p
```

`CPoly.Lawful.mem_iff` (lemma, [line 73](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L73))

```lean
lemma mem_iff : x ∈ p ↔ ∃ v, v ≠ 0 ∧ p[x]? = .some v
```

`CPoly.Lawful.getElem?_ne_some_zero` (theorem, [line 80](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L80))

```lean
theorem getElem?_ne_some_zero : p[m]? ≠ some 0
```

`CPoly.Lawful.getD_getElem?_ne_zero_of_mem` (theorem, [line 84](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L84))

```lean
theorem getD_getElem?_ne_zero_of_mem (h : m ∈ p) : p[m]?.getD 0 ≠ 0
```

`CPoly.Lawful.getElem_eq_getElem` (lemma, [line 88](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L88))

```lean
lemma getElem_eq_getElem (h : m ∈ p) : p[m] = p.1[m]
```

`CPoly.Lawful.fromUnlawful` (definition, [line 93](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L93))

> Convert an `Unlawful` polynomial to a `Lawful` one by filtering out zero coefficients.

```lean
def fromUnlawful (p : Unlawful n R) : Lawful n R
```

`CPoly.Lawful.grind_fromUnlawful_congr` (lemma, [line 100](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L100))

```lean
protected lemma grind_fromUnlawful_congr {p₁ p₂ : Unlawful n R}
    (h : p₁ = p₂) : Lawful.fromUnlawful p₁ = Lawful.fromUnlawful p₂
```

`CPoly.Lawful.C` (definition, [line 104](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L104))

> Construct a constant polynomial.

```lean
def C (c : R) : Lawful n R
```

`CPoly.Lawful.instOfNat_zero` (instance, [line 107](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L107))

```lean
instance instOfNat_zero : OfNat (Lawful n R) 0
```

`CPoly.Lawful.zero_def` (lemma, [line 109](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L109))

```lean
lemma zero_def : Zero.zero (α := Lawful n R) = C 0
```

`CPoly.Lawful.instOfNat` (instance, [line 111](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L111))

```lean
instance instOfNat {m : ℕ} [NeZero m] [NatCast R] : OfNat (Lawful n R) m
```

`CPoly.Lawful.C_zero` (lemma, [line 114](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L114))

```lean
lemma C_zero : C (n := n) (0 : R) = 0
```

`CPoly.Lawful.C_zero'` (lemma, [line 117](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L117))

```lean
lemma C_zero' : C (n := n) (0 : ℕ) = 0
```

`CPoly.Lawful.zero_eq_zero` (lemma, [line 119](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L119))

```lean
lemma zero_eq_zero : (0 : Lawful n R) = ⟨0, by grind⟩
```

`CPoly.Lawful.zero_eq_empty` (lemma, [line 121](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L121))

```lean
lemma zero_eq_empty : (0 : Lawful n R) = ∅
```

`CPoly.Lawful.not_mem_C_zero` (lemma, [line 126](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L126))

```lean
lemma not_mem_C_zero : x ∉ C 0
```

`CPoly.Lawful.not_mem_zero` (lemma, [line 129](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L129))

```lean
lemma not_mem_zero : x ∉ (0 : Lawful n R)
```

`CPoly.Lawful.cast_fromUnlawful` (lemma, [line 132](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L132))

```lean
lemma cast_fromUnlawful : (fromUnlawful p.1).1 = p.1
```

`CPoly.Lawful.extend` (definition, [line 141](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L141))

> Extend the number of variables in a polynomial.

```lean
def extend (n' : ℕ) (p : Lawful n R) : Lawful (max n n') R
```

`CPoly.Lawful.add` (definition, [line 145](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L145))

> Addition of polynomials (results in a lawful polynomial).

```lean
def add [Add R] (p₁ p₂ : Lawful n R) : Lawful n R
```

`CPoly.Lawful.grind_add_skip` (lemma, [line 151](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L151))

```lean
protected lemma grind_add_skip [Add R] {p₁ p₂ : Lawful n R} :
    p₁ + p₂ = Lawful.fromUnlawful (p₁.1.add p₂.1)
```

`CPoly.Lawful.grind_add_skip_aggressive` (lemma, [line 158](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L158))

> Note to self: This goes too far.

```lean
protected lemma grind_add_skip_aggressive [Add R] {p₁ p₂ : Lawful n R} :
    p₁ + p₂ = fromUnlawful (ExtTreeMap.mergeWith (fun _ c₁ c₂ => c₁ + c₂) p₁.1 p₂.1)
```

`CPoly.Lawful.mul` (definition, [line 162](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L162))

> Multiplication of polynomials (results in a lawful polynomial).

```lean
def mul [Mul R] [Add R] (p₁ p₂ : Lawful n R) : Lawful n R
```

`CPoly.Lawful.npow` (definition, [line 172](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L172))

> Polynomial exponentiation via repeated multiplication. `O(k)` multiplications.
>
> This is the specification; `npowBySq` is the efficient `O(log k)` implementation
> used by the `NatPow` instance once the equivalence with this naive form has been
> proven.

```lean
def npow [NatCast R] [Add R] [Mul R] : ℕ → Lawful n R → Lawful n R
```

`CPoly.Lawful.npowBySq` (definition, [line 185](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L185))

> Polynomial exponentiation via repeated squaring. `O(log k)` multiplications
> instead of `O(k)`.
>
> For `k > 0`, computes `p ^ k` by recursing on `k / 2`:
> * If `k` is even: `(p ^ (k / 2))²`
> * If `k` is odd:  `p · (p ^ (k / 2))²`
>
> Equivalent to `npow` (see `npowBySq_eq_npow`).

```lean
def npowBySq [NatCast R] [Add R] [Mul R] (p : Lawful n R) : ℕ → Lawful n R
```

`CPoly.Lawful.monomials` (abbreviation, [line 196](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L196))

> The list of monomials in a polynomial.

```lean
abbrev monomials (p : Lawful n R) : List (CMvMonomial n)
```

`CPoly.Lawful.NzConst` (definition, [line 200](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L200))

> Check if a polynomial is a non-zero constant.

```lean
def NzConst {n : ℕ} {R : Type*} [Zero R] (p : Lawful n R) : Prop
```

`CPoly.Lawful.mem_monomials_iff` (lemma, [line 205](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L205))

```lean
lemma mem_monomials_iff {w : CMvMonomial n} : w ∈ Lawful.monomials p ↔ w ∈ p
```

`CPoly.Lawful.fromUnlawful_cast` (lemma, [line 215](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L215))

```lean
lemma fromUnlawful_cast {p : Lawful n R} : fromUnlawful p.1 = p
```

`CPoly.Lawful.neg` (definition, [line 225](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L225))

> Negation of a polynomial.

```lean
def neg [Neg R] (p : Lawful n R) : Lawful n R
```

`CPoly.Lawful.sub` (definition, [line 231](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L231))

> Subtraction of polynomials.

```lean
def sub [Add R] [Neg R] (p₁ p₂ : Lawful n R) : Lawful n R
```

`CPoly.Lawful.instDecidableEq` (instance, [line 239](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L239))

```lean
instance instDecidableEq : DecidableEq (Lawful n R)
```

`CPoly.Lawful.instBEq` (instance, [line 246](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L246))

```lean
instance instBEq : BEq (Lawful n R)
```

`CPoly.Lawful.instLawfulBEq` (instance, [line 248](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L248))

```lean
instance instLawfulBEq : LawfulBEq (Lawful n R)
```

`CPoly.Lawful.X` (definition, [line 253](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L253))

> The $i$-th variable as a polynomial.

```lean
def X (i : ℕ) : Lawful (i + 1) ℤ
```

`CPoly.Lawful.align` (definition, [line 262](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L262))

> Align two polynomials by extending them to have the same number of variables.

```lean
def align
    (p₁ : Lawful n₁ R) (p₂ : Lawful n₂ R) :
    Lawful (n₁ ⊔ n₂) R × Lawful (n₁ ⊔ n₂) R
```

`CPoly.Lawful.liftPoly` (definition, [line 272](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L272))

> Lift a binary polynomial operation to handle polynomials with different numbers of variables.

```lean
def liftPoly
    (f : Lawful (n₁ ⊔ n₂) R →
  Lawful (n₁ ⊔ n₂) R →
  Lawful (n₁ ⊔ n₂) R)
  (p₁ : Lawful n₁ R) (p₂ : Lawful n₂ R) : Lawful (n₁ ⊔ n₂) R
```

`CPoly.Lawful.polyCoe` (definition, [line 279](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean#L279))

```lean
def polyCoe (p : Lawful n R) : Lawful (n + 1) R
```

## Depends on

- [Unlawful multivariate polynomials](unlawful.md)

## Sources

- [CompPoly/Multivariate/Lawful.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/Lawful.lean)
- [Declaration ledger](../../../sources/comppoly/CompPoly.Multivariate.Lawful.json)
