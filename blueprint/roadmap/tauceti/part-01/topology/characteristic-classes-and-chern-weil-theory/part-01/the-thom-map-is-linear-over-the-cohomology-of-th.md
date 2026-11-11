---
declaration: theorem
origin: cited
lean: TauCeti.thomMap_singularCup
statement: formalized
proof: formalized
---

# The Thom map is linear over the cohomology of the base

for `a ∈ H^q(B; K)` and
`b ∈ Hᵖ(B; M)`, `Φ_u(a ⌣ b) = π^*a ⌣ Φ_u(b)`.

```lean
TauCeti.thomMap_singularCup.{w, u_1} {B : Type w} [TopologicalSpace B] (F : Type u_1)
  [TopologicalSpace F] (E : B → Type w) [TopologicalSpace (Bundle.TotalSpace F E)]
  [(b : B) → Zero (E b)] [(b : B) → TopologicalSpace (E b)] [FiberBundle F E] {K : Type w}
  [CommRing K] {M : ModuleCat K} {n p q r m s : ℕ} (h : p + n = m) (hqp : q + p = r)
  (hrn : r + n = s) (hqm : q + m = s)
  (u : ↑((TauCeti.thomPair F E).singularCohomology (↧K) K (↧K) n))
  (a : ↑(TopCat.singularCohomology (↧K) K (↧K) (↧B) q))
  (b : ↑(TopCat.singularCohomology (↧K) K M (↧B) p)) :
  ((TauCeti.thomMap F E M n r s hrn) u)
      ((((↧B).singularCup K
            (CategoryTheory.MonoidalCategoryStruct.leftUnitor
                (CategoryTheory.MonoidalCategoryStruct.tensorUnit (ModuleCat K))).inv
            (CategoryTheory.MonoidalCategoryStruct.leftUnitor M).hom q p r hqp)
          a)
        b) =
    ((TopPair.singularCup K (TauCeti.thomPair F E)
          (CategoryTheory.MonoidalCategoryStruct.leftUnitor
              (CategoryTheory.MonoidalCategoryStruct.tensorUnit (ModuleCat K))).inv
          (CategoryTheory.MonoidalCategoryStruct.leftUnitor M).hom q m s hqm)
        ((CategoryTheory.ConcreteCategory.hom
            (TopCat.singularCohomologyMap (TauCeti.thomPairProj F E) q))
          a))
      (((TauCeti.thomMap F E M n p m h) u) b)
```

## Depends on

- [The Thom map](the-thom-map.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.thomMap_singularCup`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/Thom/Isomorphism.html#TauCeti.thomMap_singularCup).

## Sources

- [Tau Ceti documentation: `TauCeti.thomMap_singularCup`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/Thom/Isomorphism.html#TauCeti.thomMap_singularCup)
- [Source of `TauCeti.thomMap_singularCup` in TauCeti/Topology/VectorBundle/Thom/Isomorphism.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/VectorBundle/Thom/Isomorphism.lean#L155)
- [Tau Ceti roadmap status: Characteristic classes and Chern–Weil theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CharacteristicClasses/STATUS.md)
