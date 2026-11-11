---
declaration: theorem
origin: cited
lean: CStarModule.topologicalClosure_span_range_unop_inner_mulOpposite
statement: formalized
proof: formalized
---

# CStarModule.topologicalClosure_span_range_unop_inner_mulOpposite

The right self-module of `A` is full: the closed complex linear span of its inner products
`⟨x, y⟩_A` is all of `A`.

```lean
CStarModule.topologicalClosure_span_range_unop_inner_mulOpposite.{u_1} {A : Type u_1}
  [NonUnitalCStarAlgebra A] [PartialOrder A] [StarOrderedRing A] :
  (Submodule.span ℂ (Set.range fun p => MulOpposite.unop (inner Aᵐᵒᵖ p.1 p.2))).topologicalClosure =
    ⊤
```

## Depends on

- [CStarModule.instMulOpposite](cstarmodule-instmulopposite.md)

## Lean

Formalized in Tau Ceti as [`CStarModule.topologicalClosure_span_range_unop_inner_mulOpposite`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Module/Self.html#CStarModule.topologicalClosure_span_range_unop_inner_mulOpposite).

## Sources

- [Tau Ceti documentation: `CStarModule.topologicalClosure_span_range_unop_inner_mulOpposite`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Module/Self.html#CStarModule.topologicalClosure_span_range_unop_inner_mulOpposite)
- [Source of `CStarModule.topologicalClosure_span_range_unop_inner_mulOpposite` in TauCeti/Analysis/CStarAlgebra/Module/Self.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/CStarAlgebra/Module/Self.lean#L90)
- [Tau Ceti roadmap status: Hilbert C*-modules, Morita equivalence, and continuous trace](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/HilbertModules/STATUS.md)
