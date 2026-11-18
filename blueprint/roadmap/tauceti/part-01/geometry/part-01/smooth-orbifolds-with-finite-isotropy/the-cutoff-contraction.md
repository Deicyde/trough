---
declaration: def
origin: cited
lean: TauCeti.nerveCochainComplex.cutoffHomotopy
statement: formalized
---

# The cutoff contraction

The identity of the cochain complex of the nerve is homotopic to
the cutoff average placed in degree `0`, through the homotopy whose component from degree `n + 1`
to degree `n` prepends an arrow weighted by `c`
(`TauCeti.nerveCochainComplex.cutoffHomotopy_hom_succ`).

```lean
TauCeti.nerveCochainComplex.cutoffHomotopy.{w} {C : Type w} [CategoryTheory.Category.{w, w} C]
  {k : Type w} [CommRing k] {M : ModuleCat k} {c : C → k}
  (hc : ∀ (x : C), ∑ᶠ (b : Quiver.Costar x), c b.fst = 1) [CategoryTheory.IsGroupoid C] :
  Homotopy (CategoryTheory.CategoryStruct.id (TauCeti.nerveCochainComplex C k M))
    (TauCeti.nerveCochainComplex.cutoffCochainMap hc)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.nerveCochainComplex.cutoffHomotopy`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/SimplicialSet/Nerve/Cutoff.html#TauCeti.nerveCochainComplex.cutoffHomotopy).

## Sources

- [Tau Ceti documentation: `TauCeti.nerveCochainComplex.cutoffHomotopy`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/SimplicialSet/Nerve/Cutoff.html#TauCeti.nerveCochainComplex.cutoffHomotopy)
- [Source of `TauCeti.nerveCochainComplex.cutoffHomotopy` in TauCeti/AlgebraicTopology/SimplicialSet/Nerve/Cutoff.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/SimplicialSet/Nerve/Cutoff.lean#L309)
- [Tau Ceti roadmap status: Smooth orbifolds with finite isotropy](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Orbifolds/STATUS.md)
