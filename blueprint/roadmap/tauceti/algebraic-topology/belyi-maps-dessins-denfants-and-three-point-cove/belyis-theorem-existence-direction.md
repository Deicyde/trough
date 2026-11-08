---
declaration: theorem
origin: cited
lean: TauCeti.IsFunctionField.exists_isAlgebraicBelyiPair, TauCeti.IsFunctionField.exists_polynomial_isAlgebraicBelyiPair
statement: formalized
proof: formalized
---

# Belyi's theorem, existence direction

over a field `k` algebraic over `ℚ`, such as an
algebraic closure of `ℚ` or a number field, every function field `F / k` with exact constant field
`k` admits a Belyi map: there is `β ∈ F` transcendental over `k` such that `F` over `k(t)`, with
`t` acting as `β`, is an algebraic Belyi pair.

```lean
TauCeti.IsFunctionField.exists_isAlgebraicBelyiPair.{u, v} {k : Type u} {F : Type v} [Field k]
  [CharZero k] [Field F] [Algebra k F] [Algebra.IsAlgebraic ℚ k] (hF : TauCeti.IsFunctionField k F)
  (hc : IsIntegrallyClosedIn k F) :
  ∃ β, ∃ (hβ : Transcendental k β), TauCeti.IsAlgebraicBelyiPair k F
```

## Depends on

- [TauCeti.IsAlgebraicBelyiPair](tauceti-isalgebraicbelyipair.md)

## Proof depends on

- [Dedekind's different theorem, first part (Stichtenoth, Theorem 3.5.1(a))](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/part-01/dedekinds-different-theorem-first-part-stichteno.md)
- [The fundamental inequality (Stichtenoth, Theorem 3.1.11)](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/part-01/the-fundamental-inequality-stichtenoth-theorem-3.md)
- [Polynomial Belyification of algebraic numbers](polynomial-belyification-of-algebraic-numbers.md)
- [The weak approximation theorem for the places of an algebraic function field (Stichtenoth, Theorem 1.3.1), in the equality form](../../field-theory/function-field/the-weak-approximation-theorem-for-the-places-of.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsFunctionField.exists_isAlgebraicBelyiPair`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Belyi/Existence.html#TauCeti.IsFunctionField.exists_isAlgebraicBelyiPair).

## Other forms

**Belyi's theorem, existence direction, for a given function.** Formalized in Tau Ceti as [`TauCeti.IsFunctionField.exists_polynomial_isAlgebraicBelyiPair`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Belyi/Existence.html#TauCeti.IsFunctionField.exists_polynomial_isAlgebraicBelyiPair).

```lean
TauCeti.IsFunctionField.exists_polynomial_isAlgebraicBelyiPair.{u, v} {k : Type u} {F : Type v}
  [Field k] [CharZero k] [Field F] [Algebra k F] [Algebra.IsAlgebraic ℚ k]
  (hF : TauCeti.IsFunctionField k F) (hc : IsIntegrallyClosedIn k F) {x : F}
  (hx : Transcendental k x) :
  ∃ q,
    0 < q.natDegree ∧
      ∀ [inst : Algebra (RatFunc k) F] [inst_1 : IsScalarTower k (RatFunc k) F]
        [inst_2 : FiniteDimensional (RatFunc k) F],
        (algebraMap (RatFunc k) F) RatFunc.X =
            (Polynomial.aeval x) (Polynomial.map (algebraMap ℚ k) q) →
          TauCeti.IsAlgebraicBelyiPair k F
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsFunctionField.exists_isAlgebraicBelyiPair`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Belyi/Existence.html#TauCeti.IsFunctionField.exists_isAlgebraicBelyiPair)
- [Source of `TauCeti.IsFunctionField.exists_isAlgebraicBelyiPair` in TauCeti/FieldTheory/FunctionField/Belyi/Existence.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/FunctionField/Belyi/Existence.lean#L159)
