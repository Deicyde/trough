---
declaration: theorem
origin: cited
lean: TauCeti.conormClassGroup_injective_of_genus_eq
statement: formalized
proof: formalized
---

# The conorm is injective on divisor classes when the genus does not drop

**The conorm is injective on divisor classes when the genus does not drop** (Stichtenoth,
Theorem 3.6.3(f), without separability of `k' / k`): under a finite constant field extension
`F' = F · k'` with exact constants on both sides, `[F' : F] = [k' : k]` and
`g(F' / k') = g(F / k)`, a divisor of `F / k` whose conorm is principal is itself principal.

```lean
TauCeti.conormClassGroup_injective_of_genus_eq.{u, u', v, v'} {k : Type u} {k' : Type u'}
  {F : Type v} {F' : Type v'} [Field k] [Field k'] [Field F] [Field F'] [Algebra k k'] [Algebra k F]
  [Algebra k F'] [Algebra k' F'] [Algebra F F'] [IsScalarTower k k' F'] [IsScalarTower k F F']
  [FiniteDimensional k k'] [FiniteDimensional F F'] (h : TauCeti.constantCompositum F k' F' = ⊤)
  (hn : Module.finrank F F' = Module.finrank k k') (hF : TauCeti.IsFunctionField k F)
  (hex : IsIntegrallyClosedIn k F) (hex' : IsIntegrallyClosedIn k' F')
  (hg : TauCeti.genus k' F' = TauCeti.genus k F) :
  Function.Injective ⇑(TauCeti.Divisor.conormClassGroup k' F' hF ⋯)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The fundamental identity](../function-field/part-01/the-fundamental-identity.md)
- [The fundamental inequality (Stichtenoth, Theorem 3.1.11)](../function-field/part-01/the-fundamental-inequality-stichtenoth-theorem-3.md)
- [The genus drop is the sum of the singularity degrees](the-genus-drop-is-the-sum-of-the-singularity-deg.md)
- [Riemann's theorem](../function-field/part-02/riemanns-theorem.md)
- [TauCeti.Place.singularityDegree](tauceti-place-singularitydegree.md)
- [The weak approximation theorem](../function-field/part-02/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.conormClassGroup_injective_of_genus_eq`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/ConstantExtension/Genus/Change.html#TauCeti.conormClassGroup_injective_of_genus_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.conormClassGroup_injective_of_genus_eq`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/ConstantExtension/Genus/Change.html#TauCeti.conormClassGroup_injective_of_genus_eq)
- [Source of `TauCeti.conormClassGroup_injective_of_genus_eq` in TauCeti/FieldTheory/FunctionField/ConstantExtension/Genus/Change.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/FieldTheory/FunctionField/ConstantExtension/Genus/Change.lean#L543)
- [Tau Ceti roadmap status: Algebraic curves — function fields, divisors, and Riemann–Roch](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AlgebraicCurves/STATUS.md)
