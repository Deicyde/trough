---
declaration: def
origin: cited
lean: CategoryTheory.Sheaf.supportedModuleHEdgeEquiv
statement: formalized
---

# Degenerate edge comparison

If the local cohomology sheaves `𝓗_S^q(F)` vanish for all
`q < n`, then for every closed `Z ≤ S` the cohomology `H_Zⁿ(W, F)` with supports in `Z` is the
module `Γ_Z(W, 𝓗_Sⁿ(F))` of sections of `𝓗_Sⁿ(F)` over `W` supported in `Z`, through enlarging
the support to `S` and the sheafification map.

```lean
CategoryTheory.Sheaf.supportedModuleHEdgeEquiv.{u} {X : TopCat} {R : Type u} [CommRing R]
  (F : CategoryTheory.Sheaf (Opens.grothendieckTopology ↑X) (ModuleCat R))
  {S : TopologicalSpace.Closeds ↑X} {n : ℕ} {Z : TopologicalSpace.Closeds ↑X}
  (h : ∀ q < n, CategoryTheory.Limits.IsZero (F.supportedModuleHSheaf S q)) (hZS : Z ≤ S)
  (W : TopologicalSpace.Opens ↑X) :
  F.supportedModuleH Z W n ≃ₗ[R] ↥((F.supportedModuleHSheaf S n).supportedSubmodule Z W)
```

## Depends on

- [CategoryTheory.Sheaf.supportedModuleH](categorytheory-sheaf-supportedmoduleh.md)
- [CategoryTheory.Sheaf.supportedModuleHSheaf](categorytheory-sheaf-supportedmodulehsheaf.md)

## Proof depends on

- [Support truncation](support-truncation.md)

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Sheaf.supportedModuleHEdgeEquiv`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/LocalCohomology/Edge.html#CategoryTheory.Sheaf.supportedModuleHEdgeEquiv).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Sheaf.supportedModuleHEdgeEquiv`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/LocalCohomology/Edge.html#CategoryTheory.Sheaf.supportedModuleHEdgeEquiv)
- [Source of `CategoryTheory.Sheaf.supportedModuleHEdgeEquiv` in TauCeti/Topology/Sheaves/LocalCohomology/Edge.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Sheaves/LocalCohomology/Edge.lean#L309)
- [Tau Ceti roadmap status: Sato hyperfunctions and analytic generalized functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Hyperfunctions/STATUS.md)
