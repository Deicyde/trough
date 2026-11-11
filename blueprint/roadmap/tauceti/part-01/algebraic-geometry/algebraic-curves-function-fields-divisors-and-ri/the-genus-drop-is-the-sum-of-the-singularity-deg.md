---
declaration: theorem
origin: cited
lean: TauCeti.genus_eq_genus_add_finsum_singularityDegree
statement: formalized
proof: formalized
---

# The genus drop is the sum of the singularity degrees

if `k` is the exact constant field of
`F`, `k'` the exact constant field of `F' = F · k'` and `[F' : F] = [k' : k]`, then

`g(F / k) = g(F' / k') + ∑_P δ_P`,

where `δ_P = dim_{k'} (𝒪'_P ⧸ 𝒪_P ⊗_k k')` vanishes at all but finitely many places.

```lean
TauCeti.genus_eq_genus_add_finsum_singularityDegree.{u, u', v, v'} {k : Type u} {k' : Type u'}
  {F : Type v} {F' : Type v'} [Field k] [Field k'] [Field F] [Field F'] [Algebra k k'] [Algebra k F]
  [Algebra k F'] [Algebra k' F'] [Algebra F F'] [IsScalarTower k k' F'] [IsScalarTower k F F']
  [FiniteDimensional k k'] (hF : TauCeti.IsFunctionField k F) (hex : IsIntegrallyClosedIn k F)
  (h : TauCeti.constantCompositum F k' F' = ⊤) (hex' : IsIntegrallyClosedIn k' F')
  (hn : Module.finrank F F' = Module.finrank k k') :
  TauCeti.genus k F =
    TauCeti.genus k' F' + ∑ᶠ (P : TauCeti.Place k F), TauCeti.Place.singularityDegree k' F' P
```

## Depends on

- [TauCeti.Place.singularityDegree](tauceti-place-singularitydegree.md)

## Proof depends on

- [The fundamental identity](../../field-theory/function-field/part-01/the-fundamental-identity.md)
- [The fundamental inequality (Stichtenoth, Theorem 3.1.11)](../../field-theory/function-field/part-01/the-fundamental-inequality-stichtenoth-theorem-3.md)
- [Riemann's theorem](../../field-theory/function-field/part-02/riemanns-theorem.md)
- [The weak approximation theorem](../../field-theory/function-field/part-02/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.genus_eq_genus_add_finsum_singularityDegree`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/ConstantExtension/Genus/Change.html#TauCeti.genus_eq_genus_add_finsum_singularityDegree).

## Sources

- [Tau Ceti documentation: `TauCeti.genus_eq_genus_add_finsum_singularityDegree`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/ConstantExtension/Genus/Change.html#TauCeti.genus_eq_genus_add_finsum_singularityDegree)
- [Source of `TauCeti.genus_eq_genus_add_finsum_singularityDegree` in TauCeti/FieldTheory/FunctionField/ConstantExtension/Genus/Change.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/FieldTheory/FunctionField/ConstantExtension/Genus/Change.lean#L423)
- [Tau Ceti roadmap status: Algebraic curves — function fields, divisors, and Riemann–Roch](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AlgebraicCurves/STATUS.md)
