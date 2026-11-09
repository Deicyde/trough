# Greatest Common Divisor Algorithm

Mathlib records this with 3 declarations.

`EuclideanDomain.gcd`: `gcd a b` is a (non-unique) element such that `gcd a b ∣ a` `gcd a b ∣ b`, and for
any element `c` such that `c ∣ a` and `c ∣ b`, then `c ∣ gcd a b`

```lean
EuclideanDomain.gcd.{u} {R : Type u} [EuclideanDomain R] [DecidableEq R] (a b : R) : R
```

`EuclideanDomain.gcd_dvd`.

```lean
EuclideanDomain.gcd_dvd.{u} {R : Type u} [EuclideanDomain R] [DecidableEq R] (a b : R) :
  EuclideanDomain.gcd a b ∣ a ∧ EuclideanDomain.gcd a b ∣ b
```

`EuclideanDomain.dvd_gcd`.

```lean
EuclideanDomain.dvd_gcd.{u} {R : Type u} [EuclideanDomain R] [DecidableEq R] {a b c : R} :
  c ∣ a → c ∣ b → c ∣ EuclideanDomain.gcd a b
```

## Depends on

- [Euclidean domain](../../overview/general-algebra/divisibility-in-integral-domains/euclidean-domain.md)
- [Integer](../../overview/general-algebra/numbers/integer.md)

## Sources

- [Mathlib documentation: `EuclideanDomain.gcd`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/EuclideanDomain/Defs.html#EuclideanDomain.gcd)
- [Source of `EuclideanDomain.gcd` in Mathlib/Algebra/EuclideanDomain/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Algebra/EuclideanDomain/Defs.lean#L178)
- [Mathlib documentation: `EuclideanDomain.gcd_dvd`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/EuclideanDomain/Basic.html#EuclideanDomain.gcd_dvd)
- [Source of `EuclideanDomain.gcd_dvd` in Mathlib/Algebra/EuclideanDomain/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Algebra/EuclideanDomain/Basic.lean#L137)
- [Mathlib documentation: `EuclideanDomain.dvd_gcd`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/EuclideanDomain/Basic.html#EuclideanDomain.dvd_gcd)
- [Source of `EuclideanDomain.dvd_gcd` in Mathlib/Algebra/EuclideanDomain/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Algebra/EuclideanDomain/Basic.lean#L157)
- [Freek Wiedijk's 100 theorems, no. 69](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/100.yaml#L347)
