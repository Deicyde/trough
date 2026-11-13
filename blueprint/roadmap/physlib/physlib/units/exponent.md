---
declaration: module
origin: cited
lean: Dimension.Exponent, Dimension.Exponent.equivRat, Dimension.Exponent.ofRat, Dimension.Exponent.ofRat_toRat, Dimension.Exponent.gcdAux, Dimension.Exponent.gcd, Dimension.Exponent.gcd_eq_nat_gcd, Dimension.Exponent.normalize
statement: formalized
proof: formalized
---

# Reducible rational arithmetic for dimension exponents

The module `Physlib.Units.Exponent`, [Physlib/Units/Exponent.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean): 53 declarations (10 instances with no name), 16 with a docstring; 1 private, not shown.

> This module defines `Exponent`, a wrapper around the rational numbers whose arithmetic is
> reducible. This lets concrete arithmetic on dimension exponents hold by definitional equality.
>
> The corresponding rational operations are irreducible in Lean. Locally unsealing them does not
> export their reducibility to downstream modules, while globally changing the reducibility of an
> imported declaration requires `allowUnsafeReducibility`. The wrapper instead owns transparent
> operations while remaining equivalent to `ℚ`.
>
> The reducibility guarantee applies to the custom addition, subtraction, multiplication, inversion,
> and division below. Other operations supplied by the `Field` instance are transferred from `ℚ`.
> In particular, rational scalar multiplication and negative integer powers may require propositional
> reasoning rather than `rfl`.

## A. Definition

**`Dimension.Exponent`**, a structure, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L42).

> A rational dimension exponent with reducible arithmetic.

```lean
structure Exponent where
  /-- The rational number represented by the exponent. -/
  toRat : ℚ
deriving DecidableEq
```

**An instance with no name**, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L49).

```lean
instance : Repr Exponent
```

**`Dimension.Exponent.equivRat`**, a def, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L55).

> The equivalence between `Exponent` and the rational numbers.

```lean
def equivRat : Exponent ≃ ℚ
```

**`Dimension.Exponent.ofRat`**, a def, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L59).

> Regard a rational number as a dimension exponent.

```lean
def ofRat (q : ℚ) : Exponent
```

**`Dimension.Exponent.ofRat_toRat`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L62).

```lean
lemma ofRat_toRat (q : ℚ) : (ofRat q).toRat = q
```

**`Dimension.Exponent.gcdAux`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L65).

> Fuel-bounded Euclidean algorithm used to make exponent normalization reducible.

```lean
def gcdAux : Nat → Nat → Nat → Nat
```

**`Dimension.Exponent.gcd`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L80).

> Reducible greatest common divisor used when normalizing an exponent.

```lean
def gcd (m n : Nat) : Nat
```

**`Dimension.Exponent.gcd_eq_nat_gcd`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L84).

> The reducible exponent GCD agrees with `Nat.gcd`.

```lean
lemma gcd_eq_nat_gcd (m n : Nat) : gcd m n = Nat.gcd m n
```

**`Dimension.Exponent.normalize`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L88).

> Construct an exponent by normalizing a numerator and a nonzero denominator.

```lean
def normalize (num : Int) (den : Nat) (den_ne_zero : den ≠ 0) : Exponent
```

**`Dimension.Exponent.normalize_toRat`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L97).

```lean
lemma normalize_toRat (num : Int) (den : Nat) (den_ne_zero : den ≠ 0) :
    (normalize num den den_ne_zero).toRat = Rat.normalize num den den_ne_zero
```

**`Dimension.Exponent.num`**, a def, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L103).

> The normalized numerator of an exponent.

```lean
def num (x : Exponent) : Int
```

**`Dimension.Exponent.den`**, a def, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L107).

> The normalized denominator of an exponent.

```lean
def den (x : Exponent) : Nat
```

## B. Arithmetic

**`Dimension.Exponent.add`**, a def, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L117).

> Reducible addition of dimension exponents.

```lean
def add (a b : Exponent) : Exponent
```

**An instance with no name**, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L121).

```lean
instance : Add Exponent
```

**`Dimension.Exponent.add_equiv`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L123).

```lean
lemma add_equiv (a b : Exponent) : equivRat (add a b) = equivRat a + equivRat b
```

**`Dimension.Exponent.sub`**, a def, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L128).

> Reducible subtraction of dimension exponents.

```lean
def sub (a b : Exponent) : Exponent
```

**An instance with no name**, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L131).

```lean
instance : Sub Exponent
```

**`Dimension.Exponent.sub_equiv`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L133).

```lean
lemma sub_equiv (a b : Exponent) : equivRat (sub a b) = equivRat a - equivRat b
```

**`Dimension.Exponent.mul`**, a def, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L138).

> Reducible multiplication of dimension exponents.

```lean
def mul (a b : Exponent) : Exponent
```

**An instance with no name**, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L142).

```lean
instance : Mul Exponent
```

**`Dimension.Exponent.mul_equiv`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L144).

```lean
lemma mul_equiv (a b : Exponent) : equivRat (mul a b) = equivRat a * equivRat b
```

**`Dimension.Exponent.inv`**, a def, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L149).

> Reducible inversion of a dimension exponent, with `0⁻¹ = 0`.

```lean
def inv (a : Exponent) : Exponent
```

**An instance with no name**, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L159).

```lean
instance : Inv Exponent
```

**`Dimension.Exponent.inv_equiv`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L161).

```lean
lemma inv_equiv (a : Exponent) : equivRat (inv a) = (equivRat a)⁻¹
```

**`Dimension.Exponent.div`**, a def, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L168).

> Reducible division of dimension exponents.

```lean
def div (a b : Exponent) : Exponent
```

**An instance with no name**, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L171).

```lean
instance : Div Exponent
```

**`Dimension.Exponent.div_equiv`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L173).

```lean
lemma div_equiv (a b : Exponent) : equivRat (div a b) = equivRat a / equivRat b
```

## C. Field structure

**`Dimension.Exponent.instField`**, an instance, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L182).

```lean
instance instField : Field Exponent
```

**`Dimension.Exponent.ringEquivRat`**, a def, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L196).

> The ring equivalence between dimension exponents and rational numbers.

```lean
def ringEquivRat : Exponent ≃+* ℚ
```

**An instance with no name**, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L202).

> Regard a dimension exponent as a rational number.

```lean
instance : Coe Exponent ℚ
```

**`Dimension.Exponent.coe_inj`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L205).

```lean
lemma coe_inj {a b : Exponent} : (a : ℚ) = b ↔ a = b
```

**`Dimension.Exponent.coe_zero`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L209).

```lean
lemma coe_zero : ((0 : Exponent) : ℚ) = 0
```

**`Dimension.Exponent.coe_one`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L212).

```lean
lemma coe_one : ((1 : Exponent) : ℚ) = 1
```

**`Dimension.Exponent.coe_ofNat`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L215).

```lean
lemma coe_ofNat (n : ℕ) [n.AtLeastTwo] : ((ofNat(n) : Exponent) : ℚ) = ofNat(n)
```

**`Dimension.Exponent.coe_add`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L219).

```lean
lemma coe_add (a b : Exponent) : ((a + b : Exponent) : ℚ) = a + b
```

**`Dimension.Exponent.coe_sub`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L223).

```lean
lemma coe_sub (a b : Exponent) : ((a - b : Exponent) : ℚ) = a - b
```

**`Dimension.Exponent.coe_neg`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L227).

```lean
lemma coe_neg (a : Exponent) : ((-a : Exponent) : ℚ) = -a
```

**`Dimension.Exponent.coe_mul`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L231).

```lean
lemma coe_mul (a b : Exponent) : ((a * b : Exponent) : ℚ) = a * b
```

**`Dimension.Exponent.coe_inv`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L235).

```lean
lemma coe_inv (a : Exponent) : ((a⁻¹ : Exponent) : ℚ) = (a : ℚ)⁻¹
```

**`Dimension.Exponent.coe_div`**, a lemma, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L239).

```lean
lemma coe_div (a b : Exponent) : ((a / b : Exponent) : ℚ) = (a : ℚ) / b
```

**An instance with no name**, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L242).

```lean
instance : LinearOrder Exponent
```

**`Dimension.Exponent.coe_le_coe`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L245).

```lean
lemma coe_le_coe {a b : Exponent} : (a : ℚ) ≤ b ↔ a ≤ b
```

**`Dimension.Exponent.coe_lt_coe`**, a lemma, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L248).

```lean
lemma coe_lt_coe {a b : Exponent} : (a : ℚ) < b ↔ a < b
```

**An instance with no name**, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L250).

```lean
instance : IsStrictOrderedRing Exponent
```

**An instance with no name**, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L255).

```lean
instance : CharZero Exponent
```

**`Dimension.Exponent.add_eq_instField_add`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L259).

```lean
lemma add_eq_instField_add : add = instField.add
```

**`Dimension.Exponent.sub_eq_instField_sub`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L260).

```lean
lemma sub_eq_instField_sub : sub = instField.sub
```

**`Dimension.Exponent.inv_eq_instField_inv`**, a lemma, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L261).

```lean
lemma inv_eq_instField_inv : inv = instField.inv
```

**`Dimension.Exponent.mul_eq_instField_mul`**, a lemma, [line 262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L262).

```lean
lemma mul_eq_instField_mul : mul = instField.mul
```

**`Dimension.Exponent.div_eq_instField_div`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L263).

```lean
lemma div_eq_instField_div : div = instField.div
```

## D. Definitional equality tests

**`Dimension.Exponent.tuple_arithmetic_defeq`**, a lemma, [line 271](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L271).

```lean
lemma tuple_arithmetic_defeq :
    let Length : Exponent × Exponent := (1, 0)
    let Time : Exponent × Exponent := (0, 1)
    let Speed := Length - Time
    Length = Time + Speed
```

**`Dimension.Exponent.rational_arithmetic_defeq`**, a lemma, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L277).

```lean
lemma rational_arithmetic_defeq :
    ((2 / 3 + 5 / 7) * (11 / 13 - 1 / 2) : Exponent) = 87 / 182
```

**`Dimension.Exponent.inverse_arithmetic_defeq`**, a lemma, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean#L280).

```lean
lemma inverse_arithmetic_defeq : ((-3 / 4 : Exponent)⁻¹ + 5 / 6) = -1 / 2
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Units/Exponent.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Exponent.lean)
