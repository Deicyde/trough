---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.isRowCompact_iff_isCompletelyContinuous, ContinuousLinearMap.IsCompletelyContinuous.isRowCompact_of_forall_fg_isClosed, ZeroAtInftyContinuousMap.isCompletelyContinuous_diagonalCLM_iff, TauCeti.isONable_iff_free_residueModule
statement: formalized
proof: formalized
---

# Serre's criterion over a field

over a complete ultrametric nontrivially normed field `K`,
a continuous linear map between model spaces is row compact exactly when it is completely
continuous. Neither a discrete valuation nor spherical completeness is needed.

```lean
ContinuousLinearMap.isRowCompact_iff_isCompletelyContinuous.{u_1, u_2, u_4} {I : Type u_1}
  {J : Type u_2} [TopologicalSpace I] [DiscreteTopology I] [TopologicalSpace J] [DiscreteTopology J]
  [DecidableEq J] {K : Type u_4} [NontriviallyNormedField K] [IsUltrametricDist K] [CompleteSpace K]
  {u : ZeroAtInftyContinuousMap J K →L[K] ZeroAtInftyContinuousMap I K} :
  u.IsRowCompact ↔ u.IsCompletelyContinuous
```

## Depends on

- [ContinuousLinearMap.IsRowCompact](continuouslinearmap-isrowcompact.md)

## Proof depends on

- [Quantitative Open Mapping Theorem](../../part-03/normed/part-02/quantitative-open-mapping-theorem.md)
- [Serre's theorem (`TauCeti.ResidueModule.isOrthonormalBasis_iff`)](../../../number-theory/part-02/p-adic-functional-analysis/serres-theorem-tauceti-residuemodule-isorthonorm.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.isRowCompact_iff_isCompletelyContinuous`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/RowCompact/CompletelyContinuous.html#ContinuousLinearMap.isRowCompact_iff_isCompletelyContinuous).

## Other forms

**Serre's criterion.** Formalized in Tau Ceti as [`ContinuousLinearMap.IsCompletelyContinuous.isRowCompact_of_forall_fg_isClosed`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/RowCompact/CompletelyContinuous.html#ContinuousLinearMap.IsCompletelyContinuous.isRowCompact_of_forall_fg_isClosed).

```lean
ContinuousLinearMap.IsCompletelyContinuous.isRowCompact_of_forall_fg_isClosed.{u_1, u_2, u_3}
  {I : Type u_1} {J : Type u_2} {R : Type u_3} [TopologicalSpace I] [DiscreteTopology I]
  [TopologicalSpace J] [DiscreteTopology J] [DecidableEq J] [NormedRing R] [IsUltrametricDist R]
  [CompleteSpace R] [TauCeti.NormedRing.IsTate R]
  {u : ZeroAtInftyContinuousMap J R →L[R] ZeroAtInftyContinuousMap I R}
  (hu : u.IsCompletelyContinuous)
  (hclosed : ∀ (L : Submodule R (ZeroAtInftyContinuousMap I R)), L.FG → IsClosed ↑L) :
  u.IsRowCompact
```

**Serre's criterion for diagonal operators.** Formalized in Tau Ceti as [`ZeroAtInftyContinuousMap.isCompletelyContinuous_diagonalCLM_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/RowCompact/Diagonal.html#ZeroAtInftyContinuousMap.isCompletelyContinuous_diagonalCLM_iff).

```lean
ZeroAtInftyContinuousMap.isCompletelyContinuous_diagonalCLM_iff.{u_1, u_3} {I : Type u_1}
  [TopologicalSpace I] [DiscreteTopology I] {K : Type u_3} [NontriviallyNormedField K]
  [IsUltrametricDist K] [CompleteSpace K] {d : BoundedContinuousFunction I K} :
  (ZeroAtInftyContinuousMap.diagonalCLM d).IsCompletelyContinuous ↔
    Filter.Tendsto (⇑d) Filter.cofinite (nhds 0)
```

**Serre's criterion for orthonormalisability.** Formalized in Tau Ceti as [`TauCeti.isONable_iff_free_residueModule`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Bases/ResidueBasis.html#TauCeti.isONable_iff_free_residueModule).

```lean
TauCeti.isONable_iff_free_residueModule.{u_4, u} {R : Type u_4} [NormedCommRing R]
  [IsUltrametricDist R] [NormOneClass R] [CompleteSpace R] {M : Type u} [NormedAddCommGroup M]
  [IsUltrametricDist M] [_root_.Module R M] [IsBoundedSMul R M] [CompleteSpace M]
  (ϖ : TauCeti.NormedRing.PseudoUniformizer R)
  (hR : ∀ (a : R), TauCeti.zpowCeil ‖↑ϖ.unit‖ ‖a‖ = ‖a‖)
  (hM : ∀ (m : M), TauCeti.zpowCeil ‖↑ϖ.unit‖ ‖m‖ = ‖m‖) :
  TauCeti.IsONable R M ↔
    Module.Free (↥(Subring.unitClosedBall R) ⧸ TauCeti.unitBallIdeal R) (TauCeti.ResidueModule R M)
```

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.isRowCompact_iff_isCompletelyContinuous`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/RowCompact/CompletelyContinuous.html#ContinuousLinearMap.isRowCompact_iff_isCompletelyContinuous)
- [Source of `ContinuousLinearMap.isRowCompact_iff_isCompletelyContinuous` in TauCeti/Analysis/Normed/Operator/RowCompact/CompletelyContinuous.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Operator/RowCompact/CompletelyContinuous.lean#L126)
- [Tau Ceti roadmap status: Compact operators and nonarchimedean Fredholm theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CompactOperators/STATUS.md)
