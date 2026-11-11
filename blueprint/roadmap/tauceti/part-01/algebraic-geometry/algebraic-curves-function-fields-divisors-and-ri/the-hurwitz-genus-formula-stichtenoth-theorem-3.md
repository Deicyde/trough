---
declaration: theorem
origin: cited
lean: TauCeti.hurwitz_genus_formula, TauCeti.hurwitz_genus_formula_ratFunc, TauCeti.hurwitz_genus_formula_geometricDegree, TauCeti.two_mul_genus_sub_two_eq_iff_forall_isTame, TauCeti.geometricDegree_mul_add_degree_tameDifferent_le
statement: formalized
proof: formalized
---

# The Hurwitz genus formula (Stichtenoth, Theorem 3.4.13)

for a finite separable extension
`F' / k'` of the function field `F / k`, both with exact constants and with `k' / k` finite
separable, `[k' : k] · (2g' - 2) = [F' : F] · (2g - 2) + [k' : k] · deg Diff(F'/F)`.

```lean
TauCeti.hurwitz_genus_formula.{u, u', v, v'} {k : Type u} {k' : Type u'} {F : Type v} {F' : Type v'}
  [Field k] [Field k'] [Field F] [Field F'] [Algebra k k'] [Algebra k F] [Algebra k' F']
  [Algebra F F'] [Algebra k F'] [IsScalarTower k k' F'] [IsScalarTower k F F']
  [FiniteDimensional F F'] [Algebra.IsSeparable F F'] [FiniteDimensional k k']
  [Algebra.IsSeparable k k'] (hF : TauCeti.IsFunctionField k F)
  (hF' : TauCeti.IsFunctionField k' F') (hex : IsIntegrallyClosedIn k F)
  (hex' : IsIntegrallyClosedIn k' F') :
  ↑(Module.finrank k k') * (2 * ↑(TauCeti.genus k' F') - 2) =
    ↑(Module.finrank F F') * (2 * ↑(TauCeti.genus k F) - 2) +
      ↑(Module.finrank k k') * TauCeti.Divisor.degree (TauCeti.Divisor.different k' F' hF)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Dedekind's different theorem, first part (Stichtenoth, Theorem 3.5.1(a))](../../field-theory/function-field/part-01/dedekinds-different-theorem-first-part-stichteno.md)
- [The fundamental identity](../../field-theory/function-field/part-01/the-fundamental-identity.md)
- [The fundamental inequality (Stichtenoth, Theorem 3.1.11)](../../field-theory/function-field/part-01/the-fundamental-inequality-stichtenoth-theorem-3.md)
- [Riemann's theorem](../../field-theory/function-field/part-02/riemanns-theorem.md)
- [The Riemann–Roch theorem (Stichtenoth, Theorem 1.5.15), for the divisor `(ω)` itself](the-riemann-roch-theorem-stichtenoth-theorem-1-5.md)
- [The weak approximation theorem](../../field-theory/function-field/part-02/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.hurwitz_genus_formula`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Different/Hurwitz.html#TauCeti.hurwitz_genus_formula).

## Other forms

**The Hurwitz genus formula over a rational subfield (Stichtenoth, Corollary 3.4.14).** Formalized in Tau Ceti as [`TauCeti.hurwitz_genus_formula_ratFunc`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Different/Hurwitz.html#TauCeti.hurwitz_genus_formula_ratFunc).

```lean
TauCeti.hurwitz_genus_formula_ratFunc.{u, v} {k : Type u} {F : Type v} [Field k] [Field F]
  [Algebra k F] [Algebra (RatFunc k) F] [IsScalarTower k (RatFunc k) F]
  [FiniteDimensional (RatFunc k) F] [Algebra.IsSeparable (RatFunc k) F]
  (hex : IsIntegrallyClosedIn k F) :
  2 * ↑(TauCeti.genus k F) - 2 =
    -2 * ↑(Module.finrank (RatFunc k) F) + TauCeti.Divisor.degree (TauCeti.Divisor.different k F ⋯)
```

**The Hurwitz genus formula through the geometric degree (Stichtenoth, Theorem 3.4.13).** Formalized in Tau Ceti as [`TauCeti.hurwitz_genus_formula_geometricDegree`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Different/Hurwitz.html#TauCeti.hurwitz_genus_formula_geometricDegree).

```lean
TauCeti.hurwitz_genus_formula_geometricDegree.{u, u', v, v'} {k : Type u} {k' : Type u'}
  {F : Type v} {F' : Type v'} [Field k] [Field k'] [Field F] [Field F'] [Algebra k k'] [Algebra k F]
  [Algebra k' F'] [Algebra F F'] [Algebra k F'] [IsScalarTower k k' F'] [IsScalarTower k F F']
  [FiniteDimensional F F'] [Algebra.IsSeparable F F'] [FiniteDimensional k k']
  [Algebra.IsSeparable k k'] (hF : TauCeti.IsFunctionField k F)
  (hF' : TauCeti.IsFunctionField k' F') (hex : IsIntegrallyClosedIn k F)
  (hex' : IsIntegrallyClosedIn k' F') :
  2 * ↑(TauCeti.genus k' F') - 2 =
    ↑(TauCeti.geometricDegree F k' F') * (2 * ↑(TauCeti.genus k F) - 2) +
      TauCeti.Divisor.degree (TauCeti.Divisor.different k' F' hF)
```

**The Hurwitz genus formula, tame case (Stichtenoth, Corollary 3.5.6(b)).** Formalized in Tau Ceti as [`TauCeti.two_mul_genus_sub_two_eq_iff_forall_isTame`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Different/Hurwitz.html#TauCeti.two_mul_genus_sub_two_eq_iff_forall_isTame).

```lean
TauCeti.two_mul_genus_sub_two_eq_iff_forall_isTame.{u, u', v, v'} {k : Type u} {k' : Type u'}
  {F : Type v} {F' : Type v'} [Field k] [Field k'] [Field F] [Field F'] [Algebra k k'] [Algebra k F]
  [Algebra k' F'] [Algebra F F'] [Algebra k F'] [IsScalarTower k k' F'] [IsScalarTower k F F']
  [FiniteDimensional F F'] [Algebra.IsSeparable F F'] [FiniteDimensional k k']
  [Algebra.IsSeparable k k'] (hF : TauCeti.IsFunctionField k F)
  (hF' : TauCeti.IsFunctionField k' F') (hex : IsIntegrallyClosedIn k F)
  (hex' : IsIntegrallyClosedIn k' F') :
  2 * ↑(TauCeti.genus k' F') - 2 =
      ↑(TauCeti.geometricDegree F k' F') * (2 * ↑(TauCeti.genus k F) - 2) +
        TauCeti.Divisor.degree (TauCeti.Divisor.tameDifferent k' F' hF) ↔
    ∀ (P' : TauCeti.Place k' F'), TauCeti.Place.IsTame k F P'
```

**The Hurwitz genus formula, tame lower bound (Stichtenoth, Corollary 3.5.6(a)).** Formalized in Tau Ceti as [`TauCeti.geometricDegree_mul_add_degree_tameDifferent_le`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Different/Hurwitz.html#TauCeti.geometricDegree_mul_add_degree_tameDifferent_le).

```lean
TauCeti.geometricDegree_mul_add_degree_tameDifferent_le.{u, u', v, v'} {k : Type u} {k' : Type u'}
  {F : Type v} {F' : Type v'} [Field k] [Field k'] [Field F] [Field F'] [Algebra k k'] [Algebra k F]
  [Algebra k' F'] [Algebra F F'] [Algebra k F'] [IsScalarTower k k' F'] [IsScalarTower k F F']
  [FiniteDimensional F F'] [Algebra.IsSeparable F F'] [FiniteDimensional k k']
  [Algebra.IsSeparable k k'] (hF : TauCeti.IsFunctionField k F)
  (hF' : TauCeti.IsFunctionField k' F') (hex : IsIntegrallyClosedIn k F)
  (hex' : IsIntegrallyClosedIn k' F') :
  ↑(TauCeti.geometricDegree F k' F') * (2 * ↑(TauCeti.genus k F) - 2) +
      TauCeti.Divisor.degree (TauCeti.Divisor.tameDifferent k' F' hF) ≤
    2 * ↑(TauCeti.genus k' F') - 2
```

## Sources

- [Tau Ceti documentation: `TauCeti.hurwitz_genus_formula`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Different/Hurwitz.html#TauCeti.hurwitz_genus_formula)
- [Source of `TauCeti.hurwitz_genus_formula` in TauCeti/FieldTheory/FunctionField/Different/Hurwitz.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/FieldTheory/FunctionField/Different/Hurwitz.lean#L69)
- [Tau Ceti roadmap status: Algebraic curves — function fields, divisors, and Riemann–Roch](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AlgebraicCurves/STATUS.md)
