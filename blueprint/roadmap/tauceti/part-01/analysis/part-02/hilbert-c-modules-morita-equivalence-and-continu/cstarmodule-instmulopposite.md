---
declaration: instance
origin: cited
lean: CStarModule.instMulOpposite
statement: formalized
---

# CStarModule.instMulOpposite

A C⋆-algebra `A` is a right Hilbert `A`-module over itself, with right action
`MulOpposite.op b • a = a * b` and `A`-valued inner product `⟨a, b⟩_A = star a * b`. Its module
norm is the C⋆-norm of `A`.

```lean
CStarModule.instMulOpposite.{u_1} {A : Type u_1} [NonUnitalCStarAlgebra A] [PartialOrder A]
  [StarOrderedRing A] : CStarModule Aᵐᵒᵖ A
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CStarModule.instMulOpposite`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Module/Self.html#CStarModule.instMulOpposite).

## Sources

- [Tau Ceti documentation: `CStarModule.instMulOpposite`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Module/Self.html#CStarModule.instMulOpposite)
- [Source of `CStarModule.instMulOpposite` in TauCeti/Analysis/CStarAlgebra/Module/Self.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/CStarAlgebra/Module/Self.lean#L51)
- [Tau Ceti roadmap status: Hilbert C*-modules, Morita equivalence, and continuous trace](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/HilbertModules/STATUS.md)
