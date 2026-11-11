---
declaration: theorem
origin: cited
lean: TauCeti.ValuationSpectrum.exists_mem_spa_le_supp_iff_closure_ne_top
statement: formalized
proof: formalized
---

# Ideals contained in supports

An ideal of a Huber pair is contained in the support of a
point of `Spa (A, A⁺)` exactly when its closure is proper. For `J = 0` this is Wedhorn's
Proposition 7.49(1); over a complete Hausdorff Huber pair it gives Wedhorn's Proposition 7.51,
`exists_mem_spa_le_supp_of_ne_top`.

```lean
TauCeti.ValuationSpectrum.exists_mem_spa_le_supp_iff_closure_ne_top.{u_1} {A : Type u_1}
  [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] [TauCeti.Huber.IsHuberRing A]
  (Aplus : Subring A) (hplus : TauCeti.Huber.IsRingOfIntegralElements Aplus) (J : Ideal A) :
  (∃ v ∈ TauCeti.ValuationSpectrum.spa Aplus, J ≤ v.supp) ↔ J.closure ≠ ⊤
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ValuationSpectrum.exists_mem_spa_le_supp_iff_closure_ne_top`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Spa/Support.html#TauCeti.ValuationSpectrum.exists_mem_spa_le_supp_iff_closure_ne_top).

## Sources

- [Tau Ceti documentation: `TauCeti.ValuationSpectrum.exists_mem_spa_le_supp_iff_closure_ne_top`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Spa/Support.html#TauCeti.ValuationSpectrum.exists_mem_spa_le_supp_iff_closure_ne_top)
- [Source of `TauCeti.ValuationSpectrum.exists_mem_spa_le_supp_iff_closure_ne_top` in TauCeti/AlgebraicGeometry/AdicSpace/Spa/Support.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/AdicSpace/Spa/Support.lean#L110)
- [Tau Ceti roadmap status: Foundations of adic spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/AdicSpaces/STATUS.md)
