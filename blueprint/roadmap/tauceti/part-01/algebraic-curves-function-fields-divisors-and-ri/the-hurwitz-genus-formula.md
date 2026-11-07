---
declaration: theorem
origin: cited
lean: TauCeti.hurwitz_genus_formula
statement: formalized
proof: formalized
---

# The Hurwitz genus formula

(Stichtenoth, Theorem 3.4.13): for a finite separable extension
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

- [The Riemann–Roch theorem](the-riemann-roch-theorem.md)
- [TauCeti.Ring.IsJapanese](../../part-06/scheme-stack-cohomology-and-intersection-foundat/tauceti-ring-isjapanese.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.hurwitz_genus_formula`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Different/Hurwitz.html#TauCeti.hurwitz_genus_formula).

## Sources

- [Tau Ceti documentation: `TauCeti.hurwitz_genus_formula`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Different/Hurwitz.html#TauCeti.hurwitz_genus_formula)
- [Source of `TauCeti.hurwitz_genus_formula` in TauCeti/FieldTheory/FunctionField/Different/Hurwitz.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/FunctionField/Different/Hurwitz.lean#L69)
- [Tau Ceti roadmap status: Algebraic curves — function fields, divisors, and Riemann–Roch](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AlgebraicCurves/STATUS.md)
