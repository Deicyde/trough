---
declaration: section
origin: cited
lean: OAI.WeakHessian.every_geodesic
statement: formalized
proof: formalized
---

# 356. Gigli’s characterization of Alexandrov curvature

2 manuscripts and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves Gigli's conjecture: in every integer dimension *n* ≥ 2, Alexandrov curvature at least *κ* is characterized by the full-support $\mathop{\mathrm{RCD}}\nolimits ((n-1)\kappa,n)$ condition with reference measure $\mathcal H^n$ and distributional sectional curvature at least *κ* in the original global test classes. The RCD condition is unreduced.

## Gigli’s distributional curvature characterization of Alexandrov spaces

For every integer *n* ≥ 2 and *κ* ∈ ℝ, we prove that a complete separable metric space is an *n*-dimensional Alexandrov space of curvature at least *κ* if and only if, with reference measure $\mathcal H^n$, it is a full-support $\mathrm{RCD}((n-1)\kappa,n)$ space whose distributional sectional curvature is at least *κ* in Gigli's original global test classes. This resolves Gigli's characterization conjecture in dimensions at least two.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Giglis-distributional-curvature-characterization-of-Alexandrov-spaces-September-24-2026/main.pdf).

## Weak Hessian bounds along every geodesic in RCD spaces

On a full-support $\mathrm{RCD}(K,N)$ space with $1\lt N\lt \infty$, we prove that a bounded globally Lipschitz function whose distributional Hessian is bounded above by a bounded continuous function satisfies the corresponding second-derivative inequality along every minimizing geodesic.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Weak-Hessian-bounds-along-every-geodesic-in-RCD-spaces-September-24-2026/weak-hessian-geodesics.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization transfers a weak Hessian upper bound to every prescribed minimizing geodesic in an $\mathrm{RCD}(K,N)$ space with finite $N>1$. If a bounded globally Lipschitz function $F$ has weak Hessian bounded above by $G$ times the metric, where $G$ is bounded and continuous, then every constant-speed geodesic $\gamma:[0,1]\to X$ satisfies $(F\circ\gamma)''\le G(\gamma)\,d(\gamma(0),\gamma(1))^2$ in the distributional sense. Constant geodesics are included. The space is complete and separable with full support and measure finite on bounded sets; compactness and metric nonbranching are not assumed.

## Lean: Weak Hessian bounds along every geodesic

```lean
theorem every_geodesic [CompleteSpace X] [TopologicalSpace.SeparableSpace X]
    (m : Measure X) (K N : ℝ) (hN : 1 < N)
    (hfull : FullSupport m) (hfinite : FiniteOnBoundedSets m) (hrcd : RCD m K N)
    (F G : X → ℝ) (hFbound : BoundedFunction F) (hFlip : GloballyLipschitz F)
    (hGbound : BoundedFunction G) (hGcont : Continuous G)
    (hHess : WeakHessianUpperBound m F G)
    (σ : Curve X) (hσ : IsGeodesic σ) : CurveSecondDerivativeBound F G σ
```

Stated in [WeakHessian.lean, line 220](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/WeakHessian.lean#L220). Proved in [lean/OAI/Geometry/WeakHessian/Main.lean, line 38](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/WeakHessian/Main.lean#L38). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/356.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/356.md)
