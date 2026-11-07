---
declaration: theorem
origin: cited
lean: TauCeti.IsLiouvilleDomain.exists_isRestrictedContactType
statement: formalized
proof: formalized
---

# The boundary of a Liouville domain is of restricted contact type

On a finite-dimensional
manifold without boundary, a Liouville domain `W` is the sublevel set `{f ≤ c}` of a function `f`,
`C¹` along the level `f⁻¹(c)`, of which `c` is a regular value; the frontier of `W` is exactly the
level; and the level, with its atlas `TauCeti.regularLevelChartedSpace`, is a hypersurface
of restricted contact type for the primitive `α`.

```lean
TauCeti.IsLiouvilleDomain.exists_isRestrictedContactType.{u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M]
  {ω : TauCeti.SmoothTwoForm I M} {α : TauCeti.SmoothForm I M ℝ 1} {W : Set M} [I.Boundaryless]
  [FiniteDimensional ℝ E] (h : TauCeti.IsLiouvilleDomain ω α W) :
  ∃ f c,
    ∃ (hf : ∀ (x : M), f x = c → ContMDiffAt I (modelWithCornersSelf ℝ ℝ) 1 f x) (hreg :
      TauCeti.IsRegularValue I (modelWithCornersSelf ℝ ℝ) f c),
      W = {x | f x ≤ c} ∧
        frontier W = {x | f x = c} ∧
          TauCeti.IsRestrictedContactType
            (modelWithCornersSelf ℝ (Fin (Module.finrank ℝ E - 1) → ℝ)) (↑ω) (↑α) Subtype.val
```

## Depends on

- [TauCeti.IsLiouvilleDomain](tauceti-isliouvilledomain.md)

## Proof depends on

- [Homeomorph.pullbackChartedSpace](../../part-02/complex-manifolds-transport-quotients-bundles-an/homeomorph-pullbackchartedspace.md)
- [Homeomorph.pullbackDiffeomorph](../../part-02/complex-manifolds-transport-quotients-bundles-an/homeomorph-pullbackdiffeomorph.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsLiouvilleDomain.exists_isRestrictedContactType`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Liouville/Domain.html#TauCeti.IsLiouvilleDomain.exists_isRestrictedContactType).

## Sources

- [Tau Ceti documentation: `TauCeti.IsLiouvilleDomain.exists_isRestrictedContactType`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Liouville/Domain.html#TauCeti.IsLiouvilleDomain.exists_isRestrictedContactType)
- [Source of `TauCeti.IsLiouvilleDomain.exists_isRestrictedContactType` in TauCeti/Geometry/Symplectic/Liouville/Domain.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Symplectic/Liouville/Domain.lean#L141)
- [Tau Ceti roadmap status: Morse and Floer homology with DG local coefficients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DGFloer/STATUS.md)
