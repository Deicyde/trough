---
declaration: theorem
origin: cited
lean: TauCeti.CoefficientSemifield.instHasUniqueRoots
statement: formalized
proof: formalized
---

# TauCeti.CoefficientSemifield.instHasUniqueRoots

A coefficient semifield is torsion-free as a group: taking `n`-th powers is injective for
`n ≠ 0`.

```lean
TauCeti.CoefficientSemifield.instHasUniqueRoots.{u_1} {P : Type u_1}
  [TauCeti.CoefficientSemifield P] : HasUniqueRoots P
```

## Depends on

- [TauCeti.CoefficientSemifield](tauceti-coefficientsemifield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CoefficientSemifield.instHasUniqueRoots`](https://taucetiproject.org/docs/TauCeti/Algebra/Cluster/CoefficientSemifield/Basic.html#TauCeti.CoefficientSemifield.instHasUniqueRoots).

## Sources

- [Tau Ceti documentation: `TauCeti.CoefficientSemifield.instHasUniqueRoots`](https://taucetiproject.org/docs/TauCeti/Algebra/Cluster/CoefficientSemifield/Basic.html#TauCeti.CoefficientSemifield.instHasUniqueRoots)
- [Source of `TauCeti.CoefficientSemifield.instHasUniqueRoots` in TauCeti/Algebra/Cluster/CoefficientSemifield/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Cluster/CoefficientSemifield/Basic.lean#L94)
- [Tau Ceti roadmap status: Cluster algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ClusterAlgebras/STATUS.md)
