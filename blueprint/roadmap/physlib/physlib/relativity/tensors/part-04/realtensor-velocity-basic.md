---
declaration: module
origin: cited
lean: Lorentz.Velocity, Lorentz.Velocity.ext, Lorentz.Velocity.mem_iff, Lorentz.Velocity.minkowskiProduct_self_eq_one, Lorentz.Velocity.timeComponent_pos, Lorentz.Velocity.timeComponent_nonneg, Lorentz.Velocity.timeComponent_abs, Lorentz.Velocity.norm_spatialPart_le_timeComponent
statement: formalized
proof: formalized
---

# Lorentz Velocities

The module `Physlib.Relativity.Tensors.RealTensor.Velocity.Basic`, [Physlib/Relativity/Tensors/RealTensor/Velocity/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Velocity/Basic.lean): 25 declarations (2 instances with no name), 8 with a docstring.

> In this module we define Lorentz velocities to be
> Lorentz vectors which have norm equal to one and which are future-directed.

**`Lorentz.Velocity`**, a def, [line 27](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Velocity/Basic.lean#L27).

> A Lorentz Velocity is a Lorentz vector which has norm equal to one
> and which is future-directed.

```lean
def Velocity (d : ℕ := 3) : Set (Vector d)
```

**An instance with no name**, [line 35](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Velocity/Basic.lean#L35).

> The instance of a topological space on `Velocity d` defined as the subspace topology.

```lean
noncomputable instance : TopologicalSpace (Velocity d)
```

**`Lorentz.Velocity.ext`**, a lemma, [line 38](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Velocity/Basic.lean#L38).

```lean
lemma ext {v w : Velocity d} (h : v.1 = w.1) : v = w
```

**`Lorentz.Velocity.mem_iff`**, a lemma, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Velocity/Basic.lean#L41).

```lean
lemma mem_iff {v : Vector d} : v ∈ Velocity d ↔ ⟪v, v⟫ₘ = (1 : ℝ) ∧ 0 < v.timeComponent
```

**`Lorentz.Velocity.minkowskiProduct_self_eq_one`**, a lemma, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Velocity/Basic.lean#L45).

```lean
lemma minkowskiProduct_self_eq_one (v : Velocity d) : ⟪v.1, v.1⟫ₘ = (1 : ℝ)
```

**`Lorentz.Velocity.timeComponent_pos`**, a lemma, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Velocity/Basic.lean#L48).

```lean
lemma timeComponent_pos (v : Velocity d) : 0 < v.1.timeComponent
```

**`Lorentz.Velocity.timeComponent_nonneg`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Velocity/Basic.lean#L51).

```lean
lemma timeComponent_nonneg (v : Velocity d) : 0 ≤ v.1.timeComponent
```

**`Lorentz.Velocity.timeComponent_abs`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Velocity/Basic.lean#L55).

```lean
lemma timeComponent_abs (v : Velocity d) :
    |v.1.timeComponent| = v.1.timeComponent
```

**`Lorentz.Velocity.norm_spatialPart_le_timeComponent`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Velocity/Basic.lean#L59).

```lean
lemma norm_spatialPart_le_timeComponent (v : Velocity d) :
    ‖v.1.spatialPart‖ ≤ ‖v.1.timeComponent‖
```

**`Lorentz.Velocity.norm_spatialPart_sq_eq`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Velocity/Basic.lean#L69).

```lean
lemma norm_spatialPart_sq_eq (v : Velocity d) :
    ‖v.1.spatialPart‖ ^ 2 = (v.1 (Sum.inl 0))^2 - 1
```

**`Lorentz.Velocity.ofSpatialPart`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Velocity/Basic.lean#L77).

> The unit future four-velocity with spatial part `p` and time component
> `Real.sqrt (1 + ‖p‖ ^ 2)`. The spatial part is unrestricted.

```lean
noncomputable def ofSpatialPart (p : EuclideanSpace ℝ (Fin d)) : Velocity d
```

**`Lorentz.Velocity.spatialPart_ofSpatialPart`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Velocity/Basic.lean#L93).

```lean
lemma spatialPart_ofSpatialPart (p : EuclideanSpace ℝ (Fin d)) :
    (ofSpatialPart p).1.spatialPart = p
```

**`Lorentz.Velocity.timeComponent_ofSpatialPart`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Velocity/Basic.lean#L99).

```lean
lemma timeComponent_ofSpatialPart (p : EuclideanSpace ℝ (Fin d)) :
    (ofSpatialPart p).1.timeComponent = Real.sqrt (1 + ‖p‖ ^ 2)
```

**`Lorentz.Velocity.ofSpatialPart_spatialPart`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Velocity/Basic.lean#L104).

> A future unit four-velocity is determined by its spatial part.

```lean
lemma ofSpatialPart_spatialPart (u : Velocity d) : ofSpatialPart u.1.spatialPart = u
```

**`Lorentz.Velocity.continuous_ofSpatialPart`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Velocity/Basic.lean#L120).

> The spatial-coordinate parametrization of future unit four-velocities is continuous.

```lean
lemma continuous_ofSpatialPart : Continuous (ofSpatialPart (d := d))
```

**`Lorentz.Velocity.norm_spatialPart_le_of_orthogonal`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Velocity/Basic.lean#L132).

> A bound on the proper norm of a vector orthogonal to a unit future
> four-velocity controls its spatial norm in the chosen frame.

```lean
lemma norm_spatialPart_le_of_orthogonal (u : Velocity d) (A : Vector d)
    {C : ℝ} (hC : 0 ≤ C) (horth : ⟪u.1, A⟫ₘ = 0) (hacc : -⟪A, A⟫ₘ ≤ C ^ 2) :
    ‖A.spatialPart‖ ≤ C * u.1.timeComponent
```

**`Lorentz.Velocity.zero_le_minkowskiProduct`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Velocity/Basic.lean#L150).

```lean
lemma zero_le_minkowskiProduct (u v : Velocity d) :
    0 ≤ ⟪u.1, v.1⟫ₘ
```

**`Lorentz.Velocity.one_add_minkowskiProduct_ne_zero`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Velocity/Basic.lean#L164).

```lean
lemma one_add_minkowskiProduct_ne_zero (u v : Velocity d) :
    1 + ⟪u.1, v.1⟫ₘ ≠ 0
```

**`Lorentz.Velocity.minkowskiProduct_continuous_snd`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Velocity/Basic.lean#L168).

```lean
lemma minkowskiProduct_continuous_snd (u : Vector d) :
    Continuous fun (x : Velocity d) => ⟪u, x.1⟫ₘ
```

**`Lorentz.Velocity.minkowskiProduct_continuous_fst`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Velocity/Basic.lean#L173).

```lean
lemma minkowskiProduct_continuous_fst (u : Vector d) :
    Continuous fun (x : Velocity d) => ⟪x.1, u⟫ₘ
```

## Zero

**`Lorentz.Velocity.zero`**, a def, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Velocity/Basic.lean#L189).

> The `Velocity d` which has all space components zero.

```lean
noncomputable def zero : Velocity d
```

**An instance with no name**, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Velocity/Basic.lean#L192).

```lean
noncomputable instance : Zero (Velocity d)
```

**`Lorentz.Velocity.zero_timeComponent`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Velocity/Basic.lean#L195).

```lean
lemma zero_timeComponent : (0 : Velocity d).1.timeComponent = 1
```

**`Lorentz.Velocity.pathFromZero`**, a def, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Velocity/Basic.lean#L200).

> A continuous path from a velocity `u` to the zero velocity.

```lean
noncomputable def pathFromZero (u : Velocity d) : Path zero u
```

## Topology

**`Lorentz.Velocity.isPathConnected`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Velocity/Basic.lean#L251).

```lean
lemma isPathConnected : IsPathConnected (@Set.univ (Velocity d))
```

## Depends on

- [Minkowski product on Lorentz vectors](../part-03/realtensor-vector-minkowskiproduct.md)

## Sources

- [Physlib/Relativity/Tensors/RealTensor/Velocity/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Velocity/Basic.lean)
