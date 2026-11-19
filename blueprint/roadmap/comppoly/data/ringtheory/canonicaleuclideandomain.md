---
catalog: module
lean: CanonicalEuclideanDomain, Int.instCanonicalEuclideanDomainInt, Polynomial.instCanonicalEuclideanDomainPoly, Field.mod_eq_zero, Field.instCanonicalEuclideanDomainField, CanonicalEuclideanDomain.div_eq_of_canonical_eq_mul_add, CanonicalEuclideanDomain.div_eq_and_mod_eq_iff, CanonicalEuclideanDomain.add_mul_div_right, CanonicalEuclideanDomain.add_mul_mod_right, CanonicalEuclideanDomain.add_mul_mod_left, CanonicalEuclideanDomain.mod_eq_of_eq_add_mul, CanonicalEuclideanDomain.mul_mod_eq_mul_mod_left, CanonicalEuclideanDomain.mul_mod_eq_zero_of_mod_dvd, CanonicalEuclideanDomain.add_mod_eq_add_mod_left, CanonicalEuclideanDomain.add_mod_eq, CanonicalEuclideanDomain.mul_mod_eq, CanonicalEuclideanDomain.mod_mod_eq_mod, CanonicalEuclideanDomain.dvd_sub_mod
statement: formalized
proof: formalized
---

# Canonical Euclidean Domains

`CompPoly.Data.RingTheory.CanonicalEuclideanDomain`, in [CompPoly/Data/RingTheory/CanonicalEuclideanDomain.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/RingTheory/CanonicalEuclideanDomain.lean), by Chung Thai Nguyen, Quang Dao.

> This module defines `CanonicalEuclideanDomain` and provides instances for ℤ, `Polynomial F`,
> and `Field`.

`CanonicalEuclideanDomain` (class, [line 96](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/RingTheory/CanonicalEuclideanDomain.lean#L96))

> # Canonical Euclidean Domains
>
> A `CanonicalEuclideanDomain` is a restriction of `EuclideanDomain`. It introduces a selection
> rule for canonical remainders and guarantees there exists exactly one
> `canonical` quotient (`q`) and remainder (`r`) for any pair of dividend (`a`) and divisor (`b`)
> (assuming `b ≠ 0`), no matter how the division is implemented (i.e. the division result is
> unique and consistent across different implementations).
>
> ## Motivation: The unpredictable behaviors of `/` and `%` in `EuclideanDomain`
>
> In a standard `EuclideanDomain`, the operators `/` and `%` are viewed as black-boxes and are
> only required to return *some* valid pair satisfying `a = b * q + r` and `r ≺ b`. This loose
> specification allows implementations to be **unpredictable** and **inconsistent**:
> 1. **Unprovable Algebraic Identities:**
>   An implementation is permitted to switch strategies arbitrarily (e.g., rounding up for input `x`
>   but down for input `y`; or following truncation-towards-zero as in C/Rust/Java, ...).
>   This makes natural identities like `(a + b * k) / b = a / b + k` **false** in the general
>   case, as the term `b * k` might trigger a strategy switch.
> 2. **Non-Determinism Accumulation (Unit Drift):**
>   Algorithms that chain multiple operations (like GCD) accumulate arbitrary unit factors
>   at every step. For example, `gcd(a, b)` is only unique up to a unit.
>     * `gcd(a, gcd(b, c))` might return `g`.
>     * `gcd(gcd(a, b), c)` might return `-g` (or `u * g`).
>     While mathematically equivalent (associates), they are **not equal** as data structures.
>     This breaks any system relying on bit-exact equality (hashing, caching, serialization).
>
> **The Solution:** `CanonicalEuclideanDomain` solves this by enforcing a strict
> `is_canonical_remainder` predicate. This restricts the implementation space to **exactly one**
> valid function, ensuring the `bit-exact` uniqueness of the outputs, no matter what
> implementations are used.
>
> ## Advantages
>
> * **Algebraic Stability:** Restores critical algebraic properties,
>     enabling a suite of powerful rewrite rules (e.g., `add_mod_eq`, `add_mul_div_right`,
>     `mul_mod_eq`, `mod_eq_of_eq_add_mul`) that are unprovable in the normal `EuclideanDomain`
>     setting. This brings **canonical regularity** to domains with **non-unique remainders**
>     (e.g., `ℤ`, `Polynomial F`).
>
> * **Generic Algorithms over Rings:** Guarantees strictly normalized outputs (positive GCDs,
>     monic generators) for high-level algorithms (Smith Normal Form, Hermite Normal Form).
>     It prevents the `unit drift` described above, allowing generic algorithms to run
>     deterministically on complex domains like `Polynomial F`.
>
> * **Protocol Determinism:** Essential for cryptographic protocols (ZK transcripts, Fiat-Shamir)
>     where objects must have bit-exact representations. It ensures that every implementation
>     (Lean, Rust, ZK circuits) converges to the *same* remainder given the same canonical
>     remainder rule, guaranteeing correctness and hash consistency.
>
> ## Supported Instances
>
> This abstraction unifies commonly used mathematical objects under one interface:
> 1.  **Integers (`ℤ`):** The canonical rule enforces **non-negative remainders** (`0 ≤ r < |b|`).
>     This matches the behavior of Python's `%` or Rust's `rem_euclid`.
> 2.  **Polynomials (`Polynomial F`):** Uniqueness is naturally enforced by the degree structure.
>     Any remainder with `degree(r) < degree(b)` is automatically unique due to the ultrametric
>     property of polynomial degrees (i.e., `degree(a - b) ≤ max(degree a, degree b)`).
> 3.  **Fields (`ℚ`, `ℝ`, `ZMod p` where p is prime, ...):** Division is exact; the canonical
>   remainder is always `0`.
> 4.  **Other Euclidean Rings:** Gaussian Integers (`ℤ[i]`), Eisenstein Integers (`ℤ[ω]`), and
>     Discrete Valuation Rings (DVRs) can potentially be adapted to this interface by defining
>     strict geometric or valuation-based selection rules.
>
> ## Definition
> It extends `EuclideanDomain` with:
> 1.  `is_canonical_remainder b r`: A predicate deciding if a remainder `r` is the "chosen one".
> 2.  `remainder_is_canonical`: A proof that the built-in `%` operator satisfies this predicate.
> 3.  `unique_division`: The `Uniqueness Axiom` stating that if `(q1, r1)` and `(q2, r2)`
>     both satisfy the division equation and the canonical rule, they must be equal.

```lean
class CanonicalEuclideanDomain (R : Type u) extends EuclideanDomain R where
  is_canonical_remainder : (b : R) → (r : R) → Prop
  -- The built-in operator `remainder (%)` must obey the rule
  remainder_is_canonical : ∀ (a b : R), (hb : b ≠ 0) → is_canonical_remainder b (remainder a b)

  unique_division : ∀ {a b q₁ q₂ r₁ r₂: R}, (hb : b ≠ 0) → (h_eq_div_mul_add₁ : a = b * q₁ + r₁)
    → (h_eq_div_mul_add₂ : a = b * q₂ + r₂)
    → (is_canonical_remainder₁ : is_canonical_remainder b r₁)
    → (is_canonical_remainder₂ : is_canonical_remainder b r₂)
    → q₁ = q₂ ∧ r₁ = r₂
```

`Int.instCanonicalEuclideanDomainInt` (instance, [line 109](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/RingTheory/CanonicalEuclideanDomain.lean#L109))

```lean
instance Int.instCanonicalEuclideanDomainInt : CanonicalEuclideanDomain ℤ
```

`Polynomial.instCanonicalEuclideanDomainPoly` (instance, [line 200](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/RingTheory/CanonicalEuclideanDomain.lean#L200))

```lean
noncomputable instance Polynomial.instCanonicalEuclideanDomainPoly {F : Type u} [Field F] :
    CanonicalEuclideanDomain (Polynomial F)
```

`Field.mod_eq_zero` (lemma, [line 250](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/RingTheory/CanonicalEuclideanDomain.lean#L250))

```lean
lemma Field.mod_eq_zero {K : Type u} [Field K] (a b : K) (hb : b ≠ 0) :
    a % b = 0
```

`Field.instCanonicalEuclideanDomainField` (instance, [line 255](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/RingTheory/CanonicalEuclideanDomain.lean#L255))

```lean
instance Field.instCanonicalEuclideanDomainField {K : Type u} [Field K] :
    CanonicalEuclideanDomain K
```

`CanonicalEuclideanDomain.div_eq_of_canonical_eq_mul_add` (theorem, [line 290](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/RingTheory/CanonicalEuclideanDomain.lean#L290))

> The Fundamental Theorem of Canonical Euclidean Domains.
> If you find ANY pair (q, r) that satisfies the division equation
> AND the canonical condition, then q MUST be the result of the division operation.

```lean
theorem div_eq_of_canonical_eq_mul_add {a b q r : R} (hb : b ≠ 0)
    (h_eq : a = b * q + r)
    (h_can : is_canonical_remainder b r) :
    a / b = q
```

`CanonicalEuclideanDomain.div_eq_and_mod_eq_iff` (theorem, [line 317](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/RingTheory/CanonicalEuclideanDomain.lean#L317))

> The Fundamental Theorem of CEDs:
> Satisfying the division equation + size constraint is EQUIVALENT
> to being the output of the division function.

```lean
theorem div_eq_and_mod_eq_iff {a b q r : R} (hn : b ≠ 0) :
    (a / b = q ∧ a % b = r) ↔ (a = b * q + r ∧ is_canonical_remainder b r)
```

> # Division Properties

`CanonicalEuclideanDomain.add_mul_div_right` (theorem, [line 349](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/RingTheory/CanonicalEuclideanDomain.lean#L349))

> Generalized `add_mul_div_right`: `(a + b * r) / b = a / b + r`
> In a standard ED, this isn't always true (the quotient is not unique).
> In a CED, it is always true.

```lean
theorem add_mul_div_right (a b r : R) (hb : b ≠ 0) :
    (a + b * r) / b = a / b + r
```

`CanonicalEuclideanDomain.add_mul_mod_right` (theorem, [line 370](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/RingTheory/CanonicalEuclideanDomain.lean#L370))

> Generalized `add_mul_mod_right`: (a + b * r) % b = a % b
> The remainder ignores multiples of the divisor.

```lean
theorem add_mul_mod_right (a b r : R) (hb : b ≠ 0) :
    (a + b * r) % b = a % b
```

`CanonicalEuclideanDomain.add_mul_mod_left` (theorem, [line 388](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/RingTheory/CanonicalEuclideanDomain.lean#L388))

> Generalized `add_mul_mod_left`: (a * r + b) % a = b % a`
> The remainder ignores multiples of the divisor.

```lean
theorem add_mul_mod_left (a b r : R) (hb : a ≠ 0) :
    (a * r + b) % a = b % a
```

`CanonicalEuclideanDomain.mod_eq_of_eq_add_mul` (theorem, [line 394](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/RingTheory/CanonicalEuclideanDomain.lean#L394))

> `If a = b + n * r, then a % n = b % n.`

```lean
theorem mod_eq_of_eq_add_mul {a b n q : R} (h_eq_add_mul : a = b + n * q) (hn : n ≠ 0) :
    a % n = b % n
```

> # Arithmetic Modulo Properties

`CanonicalEuclideanDomain.mul_mod_eq_mul_mod_left` (theorem, [line 402](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/RingTheory/CanonicalEuclideanDomain.lean#L402))

> `(a * b) % n = ((a % n) * b) % n`

```lean
theorem mul_mod_eq_mul_mod_left (a b n : R) (hn : n ≠ 0) :
    (a * b) % n = ((a % n) * b) % n
```

`CanonicalEuclideanDomain.mul_mod_eq_zero_of_mod_dvd` (theorem, [line 412](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/RingTheory/CanonicalEuclideanDomain.lean#L412))

> `(a * b) % n = 0` if `a % n = 0`

```lean
theorem mul_mod_eq_zero_of_mod_dvd (a b n : R) (hn : n ≠ 0)
    (h_mod_eq_zero : a % n = 0) : (a * b) % n = 0
```

`CanonicalEuclideanDomain.add_mod_eq_add_mod_left` (theorem, [line 421](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/RingTheory/CanonicalEuclideanDomain.lean#L421))

> `(a + b) % n = ((a % n) + b) % n`

```lean
theorem add_mod_eq_add_mod_left (a b n : R) (hn : n ≠ 0) :
    (a + b) % n = ((a % n) + b) % n
```

`CanonicalEuclideanDomain.add_mod_eq` (theorem, [line 428](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/RingTheory/CanonicalEuclideanDomain.lean#L428))

> `(a + b) % n = (a % n + b % n) % n`

```lean
theorem add_mod_eq (a b n : R) (hn : n ≠ 0) :
    (a + b) % n = (a % n + b % n) % n
```

`CanonicalEuclideanDomain.mul_mod_eq` (theorem, [line 434](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/RingTheory/CanonicalEuclideanDomain.lean#L434))

> `(a * b) % n = ((a % n) * (b % n)) % n`

```lean
theorem mul_mod_eq (a b n : R) (hn : n ≠ 0) :
    (a * b) % n = ((a % n) * (b % n)) % n
```

`CanonicalEuclideanDomain.mod_mod_eq_mod` (theorem, [line 442](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/RingTheory/CanonicalEuclideanDomain.lean#L442))

> `(a % n) % n = a % n`

```lean
theorem mod_mod_eq_mod (a n : R) (hn : n ≠ 0) :
    (a % n) % n = a % n
```

`CanonicalEuclideanDomain.dvd_sub_mod` (theorem, [line 449](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/RingTheory/CanonicalEuclideanDomain.lean#L449))

> `b | a - (a % b)`

```lean
theorem dvd_sub_mod (a b : R) :
    b ∣ a - (a % b)
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Sources

- [CompPoly/Data/RingTheory/CanonicalEuclideanDomain.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/RingTheory/CanonicalEuclideanDomain.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Data.RingTheory.CanonicalEuclideanDomain.json)
