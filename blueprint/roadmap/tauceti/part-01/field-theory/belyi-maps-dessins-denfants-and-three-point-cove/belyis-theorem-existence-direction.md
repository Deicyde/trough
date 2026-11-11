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

Its statement uses no other declaration mapped here.

## Proof depends on

- [Dedekind's different theorem, first part (Stichtenoth, Theorem 3.5.1(a))](../function-field/part-01/dedekinds-different-theorem-first-part-stichteno.md)
- [The fundamental inequality (Stichtenoth, Theorem 3.1.11)](../function-field/part-01/the-fundamental-inequality-stichtenoth-theorem-3.md)
- [The weak approximation theorem](../function-field/part-02/the-weak-approximation-theorem.md)

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
- [Source of `TauCeti.IsFunctionField.exists_isAlgebraicBelyiPair` in TauCeti/FieldTheory/FunctionField/Belyi/Existence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/FieldTheory/FunctionField/Belyi/Existence.lean#L159)
- [Tau Ceti roadmap status: Belyi maps, dessins d'enfants, and three-point covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/BelyiMaps/STATUS.md)
