---
declaration: section
origin: cited
lean: OAI.SharpNodal.Main, OAI.YauCounterexamples.sphere_three, OAI.YauCounterexamples.sphere_two_torus_two, OAI.Yau.Target.yau_nodal_set_upper_bound_counterexample
statement: formalized
proof: formalized
---

# 350. Yau’s nodal bounds: surfaces and higher dimensions

3 manuscripts and 4 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves the sharp $C\sqrt\lambda$ upper bound for nodal length on every fixed smooth closed surface, completing Yau's conjecture there. The upper bound fails for fixed smooth metrics in dimensions three and four, including metrics on $S^{3}$ arbitrarily close to round. In dimension five, nodal measure can grow faster than $\lambda^{1/2+\varepsilon_0}$ for some fixed $\varepsilon_0\gt 0$, ruling out even arbitrarily small power losses.

## Sharp nodal length on smooth surfaces

We prove that a nonzero real Laplace eigenfunction with eigenvalue *λ* > 0 on a fixed smooth closed connected Riemannian surface has nodal length at most $C\sqrt\lambda$. Together with the known lower bound, this proves Yau's conjecture in this setting.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Sharp-nodal-length-on-smooth-surfaces-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## Smooth counterexamples to Yau's nodal upper bound in dimensions three and four

We construct a smooth metric on the three-sphere, arbitrarily close to the round metric in the smooth topology, and a smooth metric on $S^2\times\mathbb T^2$ for which sequences of exact real Laplace eigenfunctions have unbounded nodal measure divided by the square root of the eigenvalue. Each sequence belongs to one fixed metric. Thus the upper-bound part of Yau's nodal conjecture fails for smooth metrics in dimensions three and four.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Smooth-counterexamples-to-Yaus-nodal-upper-bound-in-dimensions-three-and-four-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## Power-law violations of Yau's nodal upper bound

We construct a smooth Riemannian metric on $S^4\times S^1$ and a sequence of real Laplace eigenfunctions whose nodal four-volume grows faster than $\lambda^{1/2+\epsilon_0}$ for one fixed $\epsilon_0\gt 0$. This disproves the smooth upper-bound assertion in Yau's nodal-set conjecture and the proposed bound with an arbitrarily small positive power loss.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Power-law-violations-of-Yaus-nodal-upper-bound-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

Yau's nodal-set conjecture predicts nodal size of order $\sqrt\lambda$ for Laplace eigenfunctions of eigenvalue $\lambda$. The formalization proves the upper bound on every fixed smooth closed connected Riemannian surface: there is a surface-dependent constant $C$ such that the one-dimensional Hausdorff measure of the zero set of every nonzero real eigenfunction with $\lambda>0$ is at most $C\sqrt\lambda$. The known lower bound is not part of this selected statement.

The formalized results contradict Yau's proposed $O(\sqrt\lambda)$ upper bound for nodal measure in dimensions three and four. On $S^3$, every prescribed smooth neighborhood of the round metric contains one fixed smooth metric with an eigenfunction sequence of unbounded nodal-measure ratio. A second fixed metric on $S^2\times T^2$ has the same property. In both cases the eigenvalues tend to infinity and the intrinsic nodal measures are finite.

Yau's nodal upper-bound conjecture predicts that the nodal measure of an eigenfunction is bounded by a constant times the square root of its eigenvalue. The formalized counterexample fixes one smooth metric on $S^4\times S^1$ and a sequence of nonzero smooth eigenfunctions whose positive eigenvalues tend to infinity, while the intrinsic four-dimensional nodal measures divided by the square roots of the eigenvalues tend to infinity. The metric is fixed throughout the sequence.

## Lean: Sharp upper bound for nodal length on smooth surfaces

Stated in [NodalLength.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/NodalLength.lean).

```lean
theorem Main [CompactSpace M] [ConnectedSpace M]
    [IsContMDiffRiemannianBundle 𝓘(ℝ,Plane) ∞ Plane
      (fun x:M=>TangentSpace 𝓘(ℝ,Plane) x)]
    [IsRiemannianManifold 𝓘(ℝ,Plane) M] : MainStatement M
```

Proved in [lean/OAI/Analysis/NodalLength/Main.lean, line 377](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/NodalLength/Main.lean#L377).

## Lean: Nodal counterexamples in dimensions three and four

Stated in [SmoothYau.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SmoothYau.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem sphere_three (gRound : SmoothMetric (Euclidean 3) (Sphere 3))
    (hRound : IsRound gRound) :
    ∀ N : Set (SmoothMetric (Euclidean 3) (Sphere 3)),
      IsSmoothNeighborhood gRound N →
      ∃ g ∈ N, HasUnboundedNodalRatio g 3
```

Proved in [lean/OAI/Geometry/SmoothYau/SphereMetric/ThreeSphere.lean, line 12](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/SmoothYau/SphereMetric/ThreeSphere.lean#L12).

```lean
theorem sphere_two_torus_two :
    ∃ g : SmoothMetric FourModel FourManifold,
      HasUnboundedNodalRatio g 4
```

Proved in [lean/OAI/Geometry/SmoothYau/ProductMetric/SphereProduct.lean, line 75](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/SmoothYau/ProductMetric/SphereProduct.lean#L75).

## Lean: Unbounded nodal ratio on $S^4\times S^1$

Stated in [YauCounterexample.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/YauCounterexample.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem yau_nodal_set_upper_bound_counterexample : MainTarget
```

Proved in [lean/OAI/Geometry/NodalSets/Main.lean, line 8](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/NodalSets/Main.lean#L8).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/350.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/350.md)
