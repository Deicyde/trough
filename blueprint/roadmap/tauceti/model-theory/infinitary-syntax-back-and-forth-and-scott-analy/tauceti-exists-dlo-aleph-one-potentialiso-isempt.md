---
declaration: theorem
origin: cited
lean: TauCeti.exists_dlo_aleph_one_potentialIso_isEmpty_equiv
statement: formalized
proof: formalized
---

# TauCeti.exists_dlo_aleph_one_potentialIso_isEmpty_equiv

Potential isomorphism, and hence `L∞ω`-equivalence, does not imply isomorphism for
uncountable structures of the same cardinality: in every universe there are two dense linear
orders without endpoints of cardinality `ℵ₁` that are potentially isomorphic, and so
`L∞ω`-equivalent (`TauCeti.InfEquivW`), but not isomorphic. The witnesses are `ω₁ ×ₗ ℚ` and its
order dual.

```lean
TauCeti.exists_dlo_aleph_one_potentialIso_isEmpty_equiv.{w} :
  ∃ M N x x_1,
    M ⊨ FirstOrder.Language.order.dlo ∧
      N ⊨ FirstOrder.Language.order.dlo ∧
        Cardinal.mk M = Cardinal.aleph 1 ∧
          Cardinal.mk N = Cardinal.aleph 1 ∧
            TauCeti.PotentialIso M N ∧
              TauCeti.InfEquivW M N ∧ IsEmpty (FirstOrder.Language.order.Equiv M N)
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](firstorder-language-boundedformulainf.md)
- [TauCeti.PotentialIso](tauceti-potentialiso.md)

## Proof depends on

- [Karp's theorem](karps-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_dlo_aleph_one_potentialIso_isEmpty_equiv`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Scott/DenseLinearOrder.html#TauCeti.exists_dlo_aleph_one_potentialIso_isEmpty_equiv).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_dlo_aleph_one_potentialIso_isEmpty_equiv`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Scott/DenseLinearOrder.html#TauCeti.exists_dlo_aleph_one_potentialIso_isEmpty_equiv)
- [Source of `TauCeti.exists_dlo_aleph_one_potentialIso_isEmpty_equiv` in TauCeti/ModelTheory/Scott/DenseLinearOrder.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/ModelTheory/Scott/DenseLinearOrder.lean#L167)
- [Tau Ceti roadmap status: Infinitary syntax, back-and-forth, and Scott analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/InfinitaryLogic/STATUS.md)
