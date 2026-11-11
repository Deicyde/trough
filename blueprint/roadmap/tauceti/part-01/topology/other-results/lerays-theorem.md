---
declaration: def
origin: cited
lean: TauCeti.Topology.homologyCechComplexIsoH
statement: formalized
---

# Leray's theorem

Let `U` be a finite family of opens covering a topological space `X`, and
let `F` be a sheaf of abelian groups on `X` with no cohomology in positive degrees on any nonempty
finite intersection of members of `U`. Then the Čech cohomology `Hⁿ(U, F)`, the cohomology of the
Čech complex of `F` for `U`, is isomorphic to the sheaf cohomology `Hⁿ(X, F)`, for every `n`,
naturally in `F` (`TauCeti.Topology.homologyMap_comp_homologyCechComplexIsoH_hom`).

```lean
TauCeti.Topology.homologyCechComplexIsoH.{u} {X : TopCat} {ι : Type u}
  (U : ι → TopologicalSpace.Opens ↑X) (hU : ⨆ i, U i = ⊤) [Finite ι]
  (F : CategoryTheory.Sheaf (Opens.grothendieckTopology ↑X) AddCommGrpCat)
  (hF : ∀ (s : Finset ι), s.Nonempty → ∀ (k : ℕ), Subsingleton ↑(F.H' (k + 1) (s.inf U))) (n : ℕ) :
  HomologicalComplex.homology ((CategoryTheory.cechComplexFunctor U).obj F.obj) n ≅ ↧(F.H n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Topology.homologyCechComplexIsoH`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/Leray/Basic.html#TauCeti.Topology.homologyCechComplexIsoH).

## Sources

- [Tau Ceti documentation: `TauCeti.Topology.homologyCechComplexIsoH`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/Leray/Basic.html#TauCeti.Topology.homologyCechComplexIsoH)
- [Source of `TauCeti.Topology.homologyCechComplexIsoH` in TauCeti/Topology/Sheaves/Leray/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Sheaves/Leray/Basic.lean#L310)
