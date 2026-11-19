---
declaration: theorem
origin: cited
lean: TauCeti.quasiIso_chainComplexMap_smoothSingularSubcomplex_ι_iSup
statement: formalized
proof: formalized
---

# The disjoint-union step of the smoothing theorem

If coproducts indexed by `ι` are exact
in `C` and, for every member of a family of pairwise disjoint open sets `s i`, the inclusion of
smooth singular chains into singular chains with coefficients in `R` is a quasi-isomorphism, then
so is the inclusion for the union `⨆ i, s i`.

```lean
TauCeti.quasiIso_chainComplexMap_smoothSingularSubcomplex_ι_iSup.{u, v, w, u_1, u_2} {E : Type u_1}
  {H : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u} [TopologicalSpace M] [ChartedSpace H M] {ι : Type u}
  (s : ι → TopologicalSpace.Opens M) (C : Type v) [CategoryTheory.Category.{w, v} C]
  [CategoryTheory.Limits.HasCoproducts C] [CategoryTheory.Abelian C]
  [CategoryTheory.HasExactColimitsOfShape (CategoryTheory.Discrete ι) C] (R : C)
  (hs : Pairwise (Function.onFun Disjoint s))
  (h : ∀ (i : ι), QuasiIso (SSet.chainComplexMap (TauCeti.smoothSingularSubcomplex I ↥(s i)).ι R)) :
  QuasiIso (SSet.chainComplexMap (TauCeti.smoothSingularSubcomplex I ↥(⨆ i, s i)).ι R)
```

## Depends on

- [TauCeti.smoothSingularSubcomplex](tauceti-smoothsingularsubcomplex.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.quasiIso_chainComplexMap_smoothSingularSubcomplex_ι_iSup`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothSingular/Additivity.html#TauCeti.quasiIso_chainComplexMap_smoothSingularSubcomplex_%CE%B9_iSup).

## Sources

- [Tau Ceti documentation: `TauCeti.quasiIso_chainComplexMap_smoothSingularSubcomplex_ι_iSup`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothSingular/Additivity.html#TauCeti.quasiIso_chainComplexMap_smoothSingularSubcomplex_%CE%B9_iSup)
- [Source of `TauCeti.quasiIso_chainComplexMap_smoothSingularSubcomplex_ι_iSup` in TauCeti/Geometry/Manifold/SmoothSingular/Additivity.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/SmoothSingular/Additivity.lean#L146)
