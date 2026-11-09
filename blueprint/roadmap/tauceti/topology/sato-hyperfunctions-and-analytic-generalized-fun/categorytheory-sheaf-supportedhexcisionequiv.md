---
declaration: def
origin: cited
lean: CategoryTheory.Sheaf.supportedHExcisionEquiv
statement: formalized
---

# CategoryTheory.Sheaf.supportedHExcisionEquiv

Excision for cohomology with supports: if `W' ≤ W` and `S ∩ W ⊆ W'` (that is,
`W ≤ W' ⊔ (X ∖ S)`), restriction is an isomorphism `H_Sⁿ(W, F) ≃+ H_Sⁿ(W', F)`.

```lean
CategoryTheory.Sheaf.supportedHExcisionEquiv.{u} {X : TopCat}
  (F : CategoryTheory.Sheaf (Opens.grothendieckTopology ↑X) AddCommGrpCat)
  (S : TopologicalSpace.Closeds ↑X) {W' W : TopologicalSpace.Opens ↑X} (h : W' ≤ W)
  (hW : W ≤ W' ⊔ S.compl) (n : ℕ) : F.supportedH S W n ≃+ F.supportedH S W' n
```

## Depends on

- [CategoryTheory.Sheaf.supportedH](categorytheory-sheaf-supportedh.md)

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Sheaf.supportedHExcisionEquiv`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/SupportedCohomology.html#CategoryTheory.Sheaf.supportedHExcisionEquiv).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Sheaf.supportedHExcisionEquiv`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/SupportedCohomology.html#CategoryTheory.Sheaf.supportedHExcisionEquiv)
- [Source of `CategoryTheory.Sheaf.supportedHExcisionEquiv` in TauCeti/Topology/Sheaves/SupportedCohomology.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Sheaves/SupportedCohomology.lean#L281)
- [Tau Ceti roadmap status: Sato hyperfunctions and analytic generalized functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/Hyperfunctions/STATUS.md)
