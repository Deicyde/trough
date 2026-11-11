---
declaration: structure
origin: cited
lean: TauCeti.CoefficientSemifieldHom
statement: formalized
---

# TauCeti.CoefficientSemifieldHom

A homomorphism of coefficient semifields is a group homomorphism that preserves the
auxiliary addition.

```lean
TauCeti.CoefficientSemifieldHom.{u_1, u_2} (P : Type u_1) (Q : Type u_2)
  [TauCeti.CoefficientSemifield P] [TauCeti.CoefficientSemifield Q] : Type (max u_1 u_2)
```

## Depends on

- [TauCeti.CoefficientSemifield](tauceti-coefficientsemifield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CoefficientSemifieldHom`](https://taucetiproject.org/docs/TauCeti/Algebra/Cluster/CoefficientSemifield/Hom.html#TauCeti.CoefficientSemifieldHom).

## Sources

- [Tau Ceti documentation: `TauCeti.CoefficientSemifieldHom`](https://taucetiproject.org/docs/TauCeti/Algebra/Cluster/CoefficientSemifield/Hom.html#TauCeti.CoefficientSemifieldHom)
- [Source of `TauCeti.CoefficientSemifieldHom` in TauCeti/Algebra/Cluster/CoefficientSemifield/Hom.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Cluster/CoefficientSemifield/Hom.lean#L42)
- [Tau Ceti roadmap status: Cluster algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ClusterAlgebras/STATUS.md)
