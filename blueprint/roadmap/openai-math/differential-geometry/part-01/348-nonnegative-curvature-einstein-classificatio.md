---
declaration: section
origin: cited
lean: OAI.PositiveEinsteinFour.orientedClassification, OAI.PositiveEinsteinFour.classificationOn, OAI.PositiveEinsteinFour.classification
statement: formalized
proof: formalized
---

# 348. Nonnegative-curvature Einstein classification and an $L^{2}$ topological gap

3 manuscripts and 3 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Classifies closed connected Einstein four-manifolds with positive Einstein constant and nonnegative sectional curvature: up to scaling, their universal Riemannian covers are the round $S^{4}$, Fubini–Study $\mathbb{CP}^2$, or a product of equal round two-spheres. A closed simply connected nonnegatively curved four-manifold is diffeomorphic to one of these whenever the scale-invariant $L^{2}$ norm of its trace-free Ricci curvature lies below a universal positive constant.

## Zero-Plane Rigidity for Einstein Four-Manifolds

We prove that a closed Einstein four-manifold with positive Einstein constant, nonnegative sectional curvature, and a zero-curvature plane has universal Riemannian cover isometric to a product of two round two-spheres. Under the normalization $\mathop{\mathrm{Ric}}\nolimits =3g$, both spheres have radius $1/\sqrt3$. The proof extends coupled estimates for the two Weyl curvature blocks to the boundary of the sectional-curvature cone and determines their equality case.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/einstein-boundary.pdf).

## An L² Einstein Gap for Nonnegatively Curved Four-Manifolds

We prove a universal, scale-invariant $L^{2}$ gap for the trace-free Ricci tensor on simply connected closed four-manifolds with nonnegative sectional curvature. If the trace-free Ricci energy is sufficiently small, the manifold is diffeomorphic to $S^{4}$, $\mathbb{CP}^2$, or $S^2\times S^2$. The proof uses the classification of positive-Einstein, nonnegatively curved four-manifolds supplied by the companion zero-plane rigidity theorem, stated explicitly as the classification premise of our result. No auxiliary curvature, volume, diameter, injectivity-radius, or Sobolev bound is required. The conclusion concerns the smooth manifold, not an isometry of the original metric.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/An-L2-Einstein-Gap-for-Nonnegatively-Curved-Four-Manifolds-October-5-2026/einstein-gap.pdf).

## Positively curved Einstein four-manifolds

We prove the classification conjecture for connected smooth closed Einstein four-manifolds with strictly positive sectional curvature. Up to positive scaling and isometry, every such manifold is the round four-sphere, the complex projective plane with its Fubini–Study metric, or real projective four-space with its round metric. No orientability assumption is needed.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization classifies connected smooth closed Einstein four-manifolds with strictly positive sectional curvature. Up to positive scaling and isometry, every such manifold is the round four-sphere, the complex projective plane with its Fubini–Study metric, or round real projective four-space. No orientability hypothesis is required. In the oriented case, only the sphere and complex projective plane occur.

## Lean: Classification of positively curved Einstein four-manifolds

Stated in [EinsteinFour.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/EinsteinFour.lean).

```lean
theorem orientedClassification (X : ClosedOrientedMetricFour.{u})
    (hEinstein : IsEinstein X.metric) (hpositive : HasPositiveSectionalCurvature X.metric) :
    ∃ a : ℝ, 0 < a ∧ (ScaledIsometricTo X.metric a roundDistance ∨
      ScaledIsometricTo X.metric a fubiniStudyDistance)
```

Proved in [lean/OAI/Geometry/EinsteinFour/ActualModelIdentification.lean, line 63](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/EinsteinFour/ActualModelIdentification.lean#L63).

```lean
theorem classificationOn : ClassificationOn M
```

Proved in [lean/OAI/Geometry/EinsteinFour/ActualModelIdentification.lean, line 78](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/EinsteinFour/ActualModelIdentification.lean#L78).

```lean
theorem classification (M : Type*) [TopologicalSpace M] [ChartedSpace FourSpace M]
    [IsManifold I4 ∞ M] [T2Space M] [SecondCountableTopology M]
    [CompactSpace M] [ConnectedSpace M] (g : SmoothMetric M)
    (hEinstein : IsEinstein g) (hpositive : HasPositiveSectionalCurvature g) :
    ∃ a : ℝ, 0 < a ∧
      (ScaledIsometricTo g a roundDistance ∨
        ScaledIsometricTo g a fubiniStudyDistance ∨
        ScaledIsometricTo g a realProjectiveDistance)
```

Proved in [lean/OAI/Geometry/EinsteinFour/Classification.lean, line 13](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/EinsteinFour/Classification.lean#L13).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/348.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/348.md)
