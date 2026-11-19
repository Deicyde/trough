---
declaration: theorem
origin: cited
lean: CategoryTheory.ShortComplex.ShortExact.isIso_cechCohomologyδ_succ_of_isFlasque
statement: formalized
proof: formalized
---

# Dimension shifting

If the middle term of `0 ⟶ F₁ ⟶ F₂ ⟶ F₃ ⟶ 0` is flasque, the
connecting map `Hⁿ⁺¹(X, F₃) ⟶ Hⁿ⁺²(X, F₁)` is an isomorphism.

```lean
CategoryTheory.ShortComplex.ShortExact.isIso_cechCohomologyδ_succ_of_isFlasque.{u} {X : TopCat}
  {R : Type u} [Ring R]
  {S :
    CategoryTheory.ShortComplex
      (CategoryTheory.Sheaf (Opens.grothendieckTopology ↑X) (ModuleCat R))}
  [CategoryTheory.HasSheafify (Opens.grothendieckTopology ↑X) (ModuleCat R)] [CompactSpace ↑X]
  [NormalSpace ↑X] [(Opens.grothendieckTopology ↑X).WEqualsLocallyBijective (ModuleCat R)]
  (hS : S.ShortExact) [TopCat.Presheaf.IsFlasque S.X₂.obj] (n : ℕ) :
  CategoryTheory.IsIso (hS.cechCohomologyδ (n + 1))
```

## Depends on

- [The connecting map of Čech cohomology](the-connecting-map-of-cech-cohomology.md)
- [TauCeti.Topology.cechCohomology](tauceti-topology-cechcohomology.md)

## Proof depends on

- [Finite covers compute Čech cohomology on a compact space](finite-covers-compute-cech-cohomology-on-a-compa.md)

## Lean

Formalized in Tau Ceti as [`CategoryTheory.ShortComplex.ShortExact.isIso_cechCohomologyδ_succ_of_isFlasque`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/Cech/LongExactSequence.html#CategoryTheory.ShortComplex.ShortExact.isIso_cechCohomology%CE%B4_succ_of_isFlasque).

## Sources

- [Tau Ceti documentation: `CategoryTheory.ShortComplex.ShortExact.isIso_cechCohomologyδ_succ_of_isFlasque`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/Cech/LongExactSequence.html#CategoryTheory.ShortComplex.ShortExact.isIso_cechCohomology%CE%B4_succ_of_isFlasque)
- [Source of `CategoryTheory.ShortComplex.ShortExact.isIso_cechCohomologyδ_succ_of_isFlasque` in TauCeti/Topology/Sheaves/Cech/LongExactSequence.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Sheaves/Cech/LongExactSequence.lean#L271)
- [Tau Ceti roadmap status: Topological sheaf cohomology and native comparison maps](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TopologicalSheafCohomology/STATUS.md)
