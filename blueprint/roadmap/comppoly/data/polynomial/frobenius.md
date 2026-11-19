---
catalog: module
lean: instExpCharOfAlgebra, Polynomial.prod_X_sub_C_eq_X_pow_card_sub_X, Polynomial.prod_X_sub_C_eq_X_pow_card_sub_X_in_L, Polynomial.prod_poly_sub_C_eq_poly_pow_card_sub_poly_in_L, Polynomial.frobenius_identity_in_ground_field, Polynomial.frobenius_identity_in_algebra, Polynomial.linear_map_of_comp_to_linear_map_of_eval, Polynomial.aeval_pow_card_eq_aeval_pow_card, Polynomial.aeval_pow_card_pow_eq_aeval_pow_card_pow, Polynomial.X_pow_sub_one_dvd_X_pow_sub_one_of_dvd, Polynomial.X_pow_card_pow_dvd_X_pow_card_pow_of_dvd, Polynomial.irreducible_dvd_X_pow_card_pow_sub_X, Polynomial.degree_dvd_of_irreducible_dvd_X_pow_card_pow_sub_X, Polynomial.irreducible_dvd_X_pow_sub_X_iff_natDegree_dvd, Polynomial.irreducible_dvd_X_pow_add_X_iff_natDegree_dvd
statement: formalized
proof: formalized
---

# Frobenius polynomial identities

`CompPoly.Data.Polynomial.Frobenius`, in [CompPoly/Data/Polynomial/Frobenius.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/Frobenius.lean), by Chung Thai Nguyen, Quang Dao.

> This file establishes fundamental identities involving the Frobenius endomorphism for polynomials
> over finite fields. The main results include factorization identities, Frobenius polynomial
> identities, and divisibility conditions for irreducible polynomials.
>
> ## Main Definitions and Theorems
>
> 1. **Field Vanishing Polynomial Equality:**
>    - `prod_X_sub_C_eq_X_pow_card_sub_X`: The identity `∏_{c ∈ Fq} (X - c) = X^q - X` in `Fq[X]`
>    - `prod_X_sub_C_eq_X_pow_card_sub_X_in_L`: Lifted version for field extensions `L[X]`
>    - `prod_poly_sub_C_eq_poly_pow_card_sub_poly_in_L`: General version
>      `∏_{c ∈ Fq} (p - c) = p^q - p` for any polynomial `p` in `L[X]`
>
> 2. **Frobenius Polynomial Identity:**
>    - `frobenius_identity_in_ground_field`: `(f + g)^q = f^q + g^q` in `Fq[X]` (Freshman's Dream)
>    - `frobenius_identity_in_algebra`: Lifted version for `Fq`-algebras `L[X]`
>    - `aeval_pow_card_eq_aeval_pow_card`: `(aeval x f)^q = aeval (x^q) f` for polynomial evaluation
>    - `aeval_pow_card_pow_eq_aeval_pow_card_pow`: Iterated version
>      `(aeval x f)^(q^n) = aeval (x^(q^n)) f`
>
> 3. **Frobenius Polynomial Divisibility:**
>    - `X_pow_sub_one_dvd_X_pow_sub_one_of_dvd`: If `k ∣ n`, then `X^k - 1 ∣ X^n - 1`
>    - `X_pow_card_pow_dvd_X_pow_card_pow_of_dvd`: If `d ∣ n`, then `X^(q^d) - X ∣ X^(q^n) - X`
>    - `irreducible_dvd_X_pow_card_pow_sub_X`: An irreducible polynomial `p` of degree `d` divides
>      `X^(q^d) - X`
>    - `degree_dvd_of_irreducible_dvd_X_pow_card_pow_sub_X`: If irreducible `p` divides `X^(q^n) - X`,
>      then `deg(p) ∣ n`
>    - `irreducible_dvd_X_pow_sub_X_iff_natDegree_dvd`: Fundamental theorem:
>      `p ∣ X^(c^n) - X ↔ deg(p) ∣ n`, with the field size as a numeral `c` together with
>      `Fintype.card R = c`
>    - `irreducible_dvd_X_pow_add_X_iff_natDegree_dvd`: its characteristic-two form, stated with
>      `+ X` as the binary fields write it
>
> …

`instExpCharOfAlgebra` (theorem, [line 61](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/Frobenius.lean#L61))

> An algebra over a field of positive characteristic inherits its exponential characteristic:
> if `ringChar Fq ≠ 0`, then `ExpChar K (ringChar Fq)` for any `Fq`-algebra `K` that is a field.
> Named as an instance but kept a theorem deliberately — it is introduced locally where a Frobenius
> argument needs it, rather than added to the instance graph for every algebra.

```lean
theorem instExpCharOfAlgebra {K : Type*} [Field K] [Algebra Fq K]
    {h_ringChar_Fq_pos : (ringChar Fq) ≠ 0} : ExpChar K (ringChar Fq)
```

`Polynomial.prod_X_sub_C_eq_X_pow_card_sub_X` (theorem, [line 84](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/Frobenius.lean#L84))

> The polynomial `X^q - X` factors into the product of `(X - c)` ∀ `c` ∈ `Fq`,
> i.e. `∏_{c ∈ Fq} (X - c) = X^q - X`.

```lean
theorem prod_X_sub_C_eq_X_pow_card_sub_X :
    (∏ c ∈ (Finset.univ : Finset Fq), (Polynomial.X - Polynomial.C c)) =
    Polynomial.X^(Fintype.card Fq) - Polynomial.X
```

`Polynomial.prod_X_sub_C_eq_X_pow_card_sub_X_in_L` (theorem, [line 138](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/Frobenius.lean#L138))

> The identity `∏_{c ∈ Fq} (X - c) = X^q - X` also holds in the polynomial ring `L[X]`,
> where `L` is any field extension of `Fq`.

```lean
theorem prod_X_sub_C_eq_X_pow_card_sub_X_in_L :
    (∏ c ∈ (Finset.univ : Finset Fq), (Polynomial.X - Polynomial.C (algebraMap Fq L c))) =
    Polynomial.X^(Fintype.card Fq) - Polynomial.X
```

`Polynomial.prod_poly_sub_C_eq_poly_pow_card_sub_poly_in_L` (theorem, [line 161](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/Frobenius.lean#L161))

> The identity `∏_{c ∈ Fq} (X - c) = X^q - X` also holds in the polynomial ring `L[X]`,
> where `L` is any field extension of `Fq`.

```lean
theorem prod_poly_sub_C_eq_poly_pow_card_sub_poly_in_L
    (p : L[X]) :
    (∏ c ∈ (Finset.univ : Finset Fq), (p - Polynomial.C (algebraMap Fq L c))) =
    p^(Fintype.card Fq) - p
```

`Polynomial.frobenius_identity_in_ground_field` (theorem, [line 192](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/Frobenius.lean#L192))

> The Frobenius identity for polynomials in `Fq[X]`.
> The `q`-th power of a sum of polynomials is the sum of their `q`-th powers.

```lean
theorem frobenius_identity_in_ground_field
    [Fact (Nat.Prime (ringChar Fq))] (f g : Fq[X]) :
    (f + g)^(Fintype.card Fq) = f^(Fintype.card Fq) + g^(Fintype.card Fq)
```

`Polynomial.frobenius_identity_in_algebra` (theorem, [line 208](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/Frobenius.lean#L208))

> The lifted Frobenius identity for polynomials in `L[X]`, where `L` is an `Fq`-algebra.
> The exponent `q` is the cardinality of the base field `Fq`.

```lean
theorem frobenius_identity_in_algebra [Fact (Nat.Prime (ringChar Fq))]
    (f g : L[X]) : (f + g)^(Fintype.card Fq) = f^(Fintype.card Fq) + g^(Fintype.card Fq)
```

`Polynomial.linear_map_of_comp_to_linear_map_of_eval` (theorem, [line 229](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/Frobenius.lean#L229))

> Restricting a linear map on polynomial composition to a linear map on polynomial evaluation.

```lean
theorem linear_map_of_comp_to_linear_map_of_eval (f : L[X])
    (h_f_linear : IsLinearMap (R := Fq) (M := L[X]) (M₂ := L[X])
      (f := fun inner_p ↦ f.comp inner_p)) :
    IsLinearMap (R := Fq) (M := L) (M₂ := L) (f := fun x ↦ f.eval x)
```

`Polynomial.aeval_pow_card_eq_aeval_pow_card` (theorem, [line 257](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/Frobenius.lean#L257))

> Frobenius endomorphism interaction with polynomial evaluation.
> (aeval x f)^|Fq| = aeval (x^|Fq|) f

```lean
theorem aeval_pow_card_eq_aeval_pow_card {Fq K : Type*} [Field Fq] [Fintype Fq]
    [CommRing K] [Algebra Fq K] [Fact (Nat.Prime (ringChar Fq))] [ExpChar K (ringChar Fq)]
    (f : Fq[X]) (x : K) :
    (aeval x f) ^ (Fintype.card Fq) = aeval (x ^ (Fintype.card Fq)) f
```

`Polynomial.aeval_pow_card_pow_eq_aeval_pow_card_pow` (theorem, [line 287](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/Frobenius.lean#L287))

> Iterated Frobenius endomorphism interaction with polynomial evaluation.
> (aeval x f)^(|Fq|^n) = aeval (x^|Fq|^n) f

```lean
theorem aeval_pow_card_pow_eq_aeval_pow_card_pow {Fq K : Type*} [Field Fq] [Fintype Fq]
    [CommRing K] [Algebra Fq K] [Fact (Nat.Prime (ringChar Fq))] [ExpChar K (ringChar Fq)]
    (f : Fq[X]) (x : K) (n : ℕ) :
    (aeval x f) ^ ((Fintype.card Fq) ^ n) = aeval (x ^ ((Fintype.card Fq) ^ n)) f
```

`Polynomial.X_pow_sub_one_dvd_X_pow_sub_one_of_dvd` (theorem, [line 315](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/Frobenius.lean#L315))

> **Lemma 1: Polynomial Divisibility of Powers**
> If `k` divides `n`, then `X^k - 1` divides `X^n - 1`.
> This is the polynomial version of `a | b => x^a - 1 | x^b - 1`.

```lean
theorem X_pow_sub_one_dvd_X_pow_sub_one_of_dvd (k n : ℕ) (h_dvd : k ∣ n) :
    (X ^ k - 1 : Fq[X]) ∣ (X ^ n - 1)
```

`Polynomial.X_pow_card_pow_dvd_X_pow_card_pow_of_dvd` (theorem, [line 326](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/Frobenius.lean#L326))

> **Lemma 2: Frobenius Divisibility Transitivity**
> If `d` divides `n`, then `X^(q^d) - X` divides `X^(q^n) - X`.
> This allows us to say: "If a poly divides the small Frobenius, it divides the big one."

```lean
theorem X_pow_card_pow_dvd_X_pow_card_pow_of_dvd (d n : ℕ) (h_dvd : d ∣ n) :
    let q := Fintype.card Fq
    (X ^ (q ^ d) - X : Fq[X]) ∣ (X ^ (q ^ n) - X)
```

`Polynomial.irreducible_dvd_X_pow_card_pow_sub_X` (theorem, [line 362](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/Frobenius.lean#L362))

> **Lemma 3: Irreducible Divides Own Frobenius (The Base Case)**
> An irreducible polynomial `p` of degree `d` divides `X^(q^d) - X`.
> Proof:
> 1. Consider the extension `K = Fq[x]/(p)`.
> 2. The group of units `K*` has order `q^d - 1`.
> 3. So every element `α` satisfies `α^(q^d - 1) = 1` (if `α ≠ 0`).
> 4. Thus `α^(q^d) = α` for all `α`.
> 5. `X^(q^d) - X` has `root p` as a root.
> 6. Since `p` is the minimal polynomial of its root, `p` divides the target.

```lean
theorem irreducible_dvd_X_pow_card_pow_sub_X (p : Fq[X]) (hp_irr : Irreducible p) :
    let q := Fintype.card Fq
    let d := p.natDegree
    p ∣ (X ^ (q ^ d) - X)
```

`Polynomial.degree_dvd_of_irreducible_dvd_X_pow_card_pow_sub_X` (theorem, [line 410](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/Frobenius.lean#L410))

> **Theorem: The Rabin Condition (One Direction)**
> If `p` is irreducible, and `p` divides `X^(q^n) - X`, then `deg(p)` divides `n`.

```lean
theorem degree_dvd_of_irreducible_dvd_X_pow_card_pow_sub_X
    [Fact (Nat.Prime (ringChar Fq))]
    (p : Fq[X]) (hp_irr : Irreducible p) (n : ℕ)
    (h_dvd : p ∣ (X ^ ((Fintype.card Fq) ^ n) - X)) :
    p.natDegree ∣ n
```

`Polynomial.irreducible_dvd_X_pow_sub_X_iff_natDegree_dvd` (lemma, [line 489](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/Frobenius.lean#L489))

> **Fundamental Theorem of Irreducible Polynomials over Finite Fields:**
> For an irreducible polynomial `q` over a finite field `R` with `c` elements:
> `q ∣ X^(c^n) - X` ↔ `deg q ∣ n`.
>
> The field size enters as a numeral `c` together with `hcard : Fintype.card R = c`, rather than
> being read off as `Fintype.card R`. A concrete field then states the divisibility at its own
> field-size literal and supplies `hcard` as `ZMod.card _`; a caller with no numeral in hand passes
> `rfl` and recovers the `Fintype.card R` statement verbatim. See the section comment in
> `CompPoly/Data/Polynomial/Rabin.lean` for why every criterion in the library is shaped this way.

```lean
lemma irreducible_dvd_X_pow_sub_X_iff_natDegree_dvd {R : Type*} [Field R]
    [Fact (Nat.Prime (ringChar R))]
    [Fintype R] {c : ℕ} (hcard : Fintype.card R = c) (n : ℕ) (q : Polynomial R)
    (hq_irr : Irreducible q) :
    q ∣ (X ^ (c ^ n) - X) ↔ q.natDegree ∣ n
```

`Polynomial.irreducible_dvd_X_pow_add_X_iff_natDegree_dvd` (lemma, [line 512](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/Frobenius.lean#L512))

> The characteristic-two form of `irreducible_dvd_X_pow_sub_X_iff_natDegree_dvd`, stated with `+ X`
> as a binary field writes it: `q ∣ X^(c^n) + X ↔ deg q ∣ n`.
>
> Over `GF(2)` the two spellings are the same polynomial, but only one of them is *syntactically*
> what a caller has. Absorbing `CharTwo.sub_eq_add` here — once, at a statement generic in `c` and
> `n` — means the concrete caller applies this as a term instead of rewriting a hypothesis whose
> type carries a large exponent such as `X ^ 2 ^ 128`.

```lean
lemma irreducible_dvd_X_pow_add_X_iff_natDegree_dvd {R : Type*} [Field R]
    [Fact (Nat.Prime (ringChar R))]
    [Fintype R] [CharP R 2] {c : ℕ} (hcard : Fintype.card R = c) (n : ℕ) (q : Polynomial R)
    (hq_irr : Irreducible q) :
    q ∣ (X ^ (c ^ n) + X) ↔ q.natDegree ∣ n
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Proof depends on

- [Bit operations on natural numbers](../nat/bitwise.md)

## Sources

- [CompPoly/Data/Polynomial/Frobenius.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/Frobenius.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Data.Polynomial.Frobenius.json)
