---
declaration: module
origin: cited
lean: ClassicalMechanics.HarmonicOscillator.ConfigurationSpace, ClassicalMechanics.HarmonicOscillator.ConfigurationSpace.ext, ClassicalMechanics.HarmonicOscillator.ConfigurationSpace.coe_apply, ClassicalMechanics.HarmonicOscillator.ConfigurationSpace.valEquiv, ClassicalMechanics.HarmonicOscillator.ConfigurationSpace.valHomeomorphism, ClassicalMechanics.HarmonicOscillator.ConfigurationSpace.valDiffeomorph, ClassicalMechanics.HarmonicOscillator.instNormedAddCommGroupTangent, ClassicalMechanics.HarmonicOscillator.instNormedSpaceTangent
statement: formalized
proof: formalized
---

# Configuration space of the harmonic oscillator

The module `Physlib.ClassicalMechanics.HarmonicOscillator.Geometric.Basic`, [Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/Basic.lean): 18 declarations (6 instances with no name), 18 with a docstring.

## i. Overview

> The configuration space `Q` of the one-dimensional harmonic oscillator is the space of
> possible positions of the oscillator, formalised here as a one-dimensional smooth manifold.
>
> `Q` carries a single chosen global coordinate, modeled by `EuclideanSpace ℝ (Fin 1)`. This
> coordinate supplies the topology and the smooth-manifold structure through a single global
> chart.
>
> The global coordinate also identifies each tangent space with the same Euclidean model. The
> map `tangentCoord q` records the coordinate representative of a tangent vector at `q`; this
> tangent-coordinate infrastructure is used by later geometric constructions on the oscillator.

## ii. Key results

> - `ConfigurationSpace` : the configuration manifold `Q` of the harmonic oscillator, wrapping
>   the chosen `EuclideanSpace ℝ (Fin 1)` coordinate.
> - `ConfigurationSpace.valEquiv` : the coordinate equivalence identifying `Q` with its
>   `EuclideanSpace ℝ (Fin 1)` model.
> - `ConfigurationSpace.valHomeomorphism` : the global coordinate homeomorphism underlying the
>   manifold chart.
> - `ConfigurationSpace.valDiffeomorph` : the global coordinate chart as an analytic
>   diffeomorphism, upgrading `valHomeomorphism` to a smooth identification of `Q` with its model.
> - the `ChartedSpace` and `IsManifold` instances, exhibiting `Q` as a one-dimensional analytic
>   manifold modeled on `EuclideanSpace ℝ (Fin 1)`.
> - `tangentCoord` : the chart-induced continuous linear equivalence from the tangent space at a
>   configuration to `EuclideanSpace ℝ (Fin 1)`.
> - `instNormedAddCommGroupTangent` and `instNormedSpaceTangent` : the normed real vector-space
>   structure on tangent spaces, supplied through the global coordinate model.
> - `instFiniteDimensionalTangent` : finite-dimensionality of each tangent space, transported
>   through `tangentCoord`.
> - `ConfigurationSpace.toSpace` : the point of physical `Space 1` determined by a
>   configuration.

## iv. References

> * Ivo Terek, Introductory Variational Calculus on Manifolds, page 1 (Section 1, Basic definitions
>   and examples). [ref: terek\_variational\_manifolds]

## A. The configuration space type

> `ConfigurationSpace` wraps a single chosen global coordinate valued in
> `EuclideanSpace ℝ (Fin 1)`. We record extensionality in this coordinate together with a
> function-like coordinate access mirroring that of `EuclideanSpace ℝ (Fin 1)`.

**`ClassicalMechanics.HarmonicOscillator.ConfigurationSpace`**, a structure, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/Basic.lean#L86).

> The one-dimensional configuration space `Q` of the harmonic oscillator: the space of
> possible positions of the oscillator, equipped with a single chosen global coordinate
> modeled by `EuclideanSpace ℝ (Fin 1)`.

```lean
structure ConfigurationSpace where
  /-- The chosen global coordinate of the configuration, valued in
  `EuclideanSpace ℝ (Fin 1)`. -/
  val : EuclideanSpace ℝ (Fin 1)
```

**`ClassicalMechanics.HarmonicOscillator.ConfigurationSpace.ext`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/Basic.lean#L95).

> Two configurations are equal when their chosen global coordinates are equal.

```lean
lemma ext {x y : ConfigurationSpace} (h : x.val = y.val) : x = y
```

**An instance with no name**, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/Basic.lean#L103).

> A configuration may be applied like a function `Fin 1 → ℝ`, evaluating its
> underlying coordinate. This mirrors the function-like use of `EuclideanSpace ℝ (Fin 1)`.

```lean
instance : CoeFun ConfigurationSpace (fun _ => Fin 1 → ℝ)
```

**`ClassicalMechanics.HarmonicOscillator.ConfigurationSpace.coe_apply`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/Basic.lean#L108).

> Applying a configuration as a function reads the corresponding component of its global
> coordinate.

```lean
lemma coe_apply (x : ConfigurationSpace) (i : Fin 1) : x i = x.val i
```

## B. Topology and coordinate homeomorphism

> `ConfigurationSpace` carries the topology induced by its chosen coordinate
> `ConfigurationSpace.val`: a set of configurations is open exactly when it is the preimage of
> an open set under `val`. The wrapper/unwrapper pair is the coordinate equivalence `valEquiv`,
> which is a homeomorphism `valHomeomorphism` for this induced topology — its continuity in
> both directions is just the universal property of the induced topology. We transport Hausdorffness
> and second countability across it from the model space, so `Q` is a well-behaved topological
> manifold.

**An instance with no name**, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/Basic.lean#L124).

> The topology on configuration space, induced by the chosen coordinate
> `ConfigurationSpace.val` into `EuclideanSpace ℝ (Fin 1)`.

```lean
instance : TopologicalSpace ConfigurationSpace
```

**`ClassicalMechanics.HarmonicOscillator.ConfigurationSpace.valEquiv`**, a def, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/Basic.lean#L129).

> The coordinate equivalence between configuration space and its `EuclideanSpace ℝ (Fin 1)`
> model, given by `ConfigurationSpace.val` with its wrapper inverse.

```lean
def valEquiv : ConfigurationSpace ≃ EuclideanSpace ℝ (Fin 1)
```

**`ClassicalMechanics.HarmonicOscillator.ConfigurationSpace.valHomeomorphism`**, a def, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/Basic.lean#L139).

> The global coordinate homeomorphism between configuration space and its
> `EuclideanSpace ℝ (Fin 1)` model. Continuity in both directions is exactly the universal
> property of the induced topology, so no norm or isometry structure is involved. This
> homeomorphism underlies the single global chart used for the smooth-manifold structure.

```lean
def valHomeomorphism : ConfigurationSpace ≃ₜ EuclideanSpace ℝ (Fin 1)
```

**An instance with no name**, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/Basic.lean#L148).

> Configuration space is Hausdorff, transported from `EuclideanSpace ℝ (Fin 1)` across the
> coordinate homeomorphism.

```lean
instance : T2Space ConfigurationSpace
```

**An instance with no name**, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/Basic.lean#L152).

> Configuration space is second countable, transported from `EuclideanSpace ℝ (Fin 1)`
> across the coordinate homeomorphism.

```lean
instance : SecondCountableTopology ConfigurationSpace
```

## C. Smooth manifold structure

> `ConfigurationSpace` is an analytic manifold modeled on `EuclideanSpace ℝ (Fin 1)`, via the
> single global chart `valHomeomorphism`. With one chart the only coordinate change is the
> chart's self-transition, which is analytic, so chart compatibility is immediate.

**An instance with no name**, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/Basic.lean#L165).

> The structure of a charted space on `ConfigurationSpace`, modeled on its
> `EuclideanSpace ℝ (Fin 1)` coordinate via the single global chart `valHomeomorphism`.

```lean
instance : ChartedSpace (EuclideanSpace ℝ (Fin 1)) ConfigurationSpace
```

**An instance with no name**, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/Basic.lean#L179).

> The structure of a smooth (indeed analytic) manifold on `ConfigurationSpace`. With a
> single global chart, the only coordinate change is the chart's self-transition, which is
> analytic.

```lean
instance : IsManifold 𝓘(ℝ, EuclideanSpace ℝ (Fin 1)) ω ConfigurationSpace
```

## D. The coordinate diffeomorphism

> The single global chart is an analytic diffeomorphism, not merely a homeomorphism, so `Q` is
> identified with its `EuclideanSpace ℝ (Fin 1)` model as a smooth manifold. With one chart this
> is immediate: the only transition is the analytic self-transition already recorded in the
> manifold structure. This smooth identification is what lets smoothness of maps to or from `Q`
> be tested in the chosen global coordinate, the device used for trajectories and their velocities.

**`ClassicalMechanics.HarmonicOscillator.ConfigurationSpace.valDiffeomorph`**, a def, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/Basic.lean#L198).

> The global coordinate chart as an analytic diffeomorphism between `ConfigurationSpace` and
> its `EuclideanSpace ℝ (Fin 1)` model, upgrading `valHomeomorphism` to a smooth identification.

```lean
def valDiffeomorph :
    ConfigurationSpace ≃ₘ^ω⟮𝓘(ℝ, EuclideanSpace ℝ (Fin 1)), 𝓘(ℝ, EuclideanSpace ℝ (Fin 1))⟯
      EuclideanSpace ℝ (Fin 1)
```

## E. Tangent-coordinate infrastructure

> The global coordinate on `ConfigurationSpace` also gives a coordinate representative for tangent
> vectors. The tangent spaces inherit their normed real vector-space structure from the Euclidean
> coordinate model, and `tangentCoord q` records the resulting continuous linear equivalence.

**`ClassicalMechanics.HarmonicOscillator.instNormedAddCommGroupTangent`**, an instance, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/Basic.lean#L231).

> The model-space normed additive group structure on tangent spaces.

```lean
instance instNormedAddCommGroupTangent (q : ConfigurationSpace) :
    NormedAddCommGroup (TangentSpace 𝓘(ℝ, EuclideanSpace ℝ (Fin 1)) q)
```

**`ClassicalMechanics.HarmonicOscillator.instNormedSpaceTangent`**, an instance, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/Basic.lean#L236).

> The model-space real normed vector space structure on tangent spaces.

```lean
instance instNormedSpaceTangent (q : ConfigurationSpace) :
    NormedSpace ℝ (TangentSpace 𝓘(ℝ, EuclideanSpace ℝ (Fin 1)) q)
```

**`ClassicalMechanics.HarmonicOscillator.tangentCoord`**, a def, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/Basic.lean#L242).

> The chart-induced continuous linear equivalence from the tangent space at `q` to the
> Euclidean coordinate model `EuclideanSpace ℝ (Fin 1)`.

```lean
def tangentCoord (q : ConfigurationSpace) :
    TangentSpace 𝓘(ℝ, EuclideanSpace ℝ (Fin 1)) q ≃L[ℝ] EuclideanSpace ℝ (Fin 1)
```

**`ClassicalMechanics.HarmonicOscillator.instFiniteDimensionalTangent`**, an instance, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/Basic.lean#L251).

> Each tangent space is finite-dimensional because it is linearly equivalent to
> `EuclideanSpace ℝ (Fin 1)` through `tangentCoord`.

```lean
instance instFiniteDimensionalTangent (q : ConfigurationSpace) :
    FiniteDimensional ℝ (TangentSpace 𝓘(ℝ, EuclideanSpace ℝ (Fin 1)) q)
```

## F. Map to physical space

> The point of one-dimensional physical `Space 1` determined by a configuration, obtained by
> reading off the underlying coordinate. This links the abstract configuration manifold to the
> concrete coordinate model.

**`ClassicalMechanics.HarmonicOscillator.ConfigurationSpace.toSpace`**, a def, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/Basic.lean#L268).

> The position in one-dimensional space associated to the configuration.

```lean
def toSpace (q : ConfigurationSpace) : Space 1
```

**`ClassicalMechanics.HarmonicOscillator.ConfigurationSpace.toSpace_apply`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/Basic.lean#L272).

> The physical-space coordinate associated to a configuration is its chosen global
> coordinate.

```lean
lemma toSpace_apply (q : ConfigurationSpace) (i : Fin 1) : q.toSpace i = q.val i
```

## Depends on

- [Space](../../../spaceandtime/space/part-01/basic.md)

## Sources

- [Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/Basic.lean)
