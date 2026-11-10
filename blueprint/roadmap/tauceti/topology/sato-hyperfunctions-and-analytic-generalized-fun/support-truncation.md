---
declaration: theorem
origin: cited
lean: CategoryTheory.Sheaf.subsingleton_supportedH_of_isZero_supportedHSheaf
statement: formalized
proof: formalized
---

# Support truncation

If the local cohomology sheaves `𝓗_S^q(F)` vanish for all `q < n`,
then the cohomology groups `H_S^q(W, F)` with supports in `S` vanish for all `q < n` and every
open `W`.

```lean
CategoryTheory.Sheaf.subsingleton_supportedH_of_isZero_supportedHSheaf.{u} {X : TopCat}
  (F : CategoryTheory.Sheaf (Opens.grothendieckTopology ↑X) AddCommGrpCat)
  (S : TopologicalSpace.Closeds ↑X) {n : ℕ}
  (h : ∀ q < n, CategoryTheory.Limits.IsZero (F.supportedHSheaf S q)) {q : ℕ} (hq : q < n)
  (W : TopologicalSpace.Opens ↑X) : Subsingleton (F.supportedH S W q)
```

## Depends on

- [CategoryTheory.Sheaf.supportedH](categorytheory-sheaf-supportedh.md)
- [CategoryTheory.Sheaf.supportedHSheaf](categorytheory-sheaf-supportedhsheaf.md)

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Sheaf.subsingleton_supportedH_of_isZero_supportedHSheaf`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/LocalCohomology/Basic.html#CategoryTheory.Sheaf.subsingleton_supportedH_of_isZero_supportedHSheaf).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Sheaf.subsingleton_supportedH_of_isZero_supportedHSheaf`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/LocalCohomology/Basic.html#CategoryTheory.Sheaf.subsingleton_supportedH_of_isZero_supportedHSheaf)
- [Source of `CategoryTheory.Sheaf.subsingleton_supportedH_of_isZero_supportedHSheaf` in TauCeti/Topology/Sheaves/LocalCohomology/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Sheaves/LocalCohomology/Basic.lean#L516)
- [Tau Ceti roadmap status: Sato hyperfunctions and analytic generalized functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/Hyperfunctions/STATUS.md)
