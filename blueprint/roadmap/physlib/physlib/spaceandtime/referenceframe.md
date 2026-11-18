---
declaration: module
origin: cited
lean: ClassicalMechanics.ReferenceFrame, ClassicalMechanics.ReferenceFrame.fromReferencePoints, ClassicalMechanics.ReferenceFrame.timeEquiv, ClassicalMechanics.ReferenceFrame.IsMetricConserved, ClassicalMechanics.ReferenceFrame.Orthonormal, ClassicalMechanics.ReferenceFrame.Orthonormal.isMetricConserved, ClassicalMechanics.ReferenceFrame.IsInertial, ClassicalMechanics.ReferenceFrame.IsInertial.velocity
statement: formalized
proof: formalized
---

# Reference frames

The module `Physlib.SpaceAndTime.ReferenceFrame`, [Physlib/SpaceAndTime/ReferenceFrame.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/ReferenceFrame.lean): 26 declarations (9 instances with no name), 22 with a docstring.

> A point in space and a list of coordinates are different kinds of data. Assigning coordinates to a
> point requires an origin and a basis for measuring displacements from that origin. A
> `ReferenceFrame` records those choices at every time.
>
> This distinction is built into `Space d`, which is an affine space. Two points determine a
> displacement, but no point is automatically the zero point. The chosen origin therefore belongs to
> the frame, not to space itself. Similarly, a displacement has coordinate components only after a
> basis has been chosen. Real-valued coordinates in all frames use the same implicit units of space
> and time. Different frames represent different coordinate grids, not different units.
>
> Most applications should use frames that are both inertial and orthonormal. In orthonormal frames,
> the norm and inner product of coordinate vectors are given by the familiar Euclidean formulas. The
> extra generality here also permits nonorthonormal coordinate grids. Giving every coordinate tuple
> the standard Euclidean norm and dot product, independently of its basis, would make coordinate
> transformations involving such a grid non-isometric: the same geometric displacement could acquire
> different lengths, or a pair of displacements a different angle, merely by changing frames. Instead,
> the metric on frame vectors is pulled back from geometric displacement space through the frame
> basis. The usual component formulas are recovered for orthonormal frames.

## A. Reference frames

> A reference frame can be pictured as a coordinate grid carried through time. It is part of how
> motion is described, not an additional physical object moving with the particles.

**`ClassicalMechanics.ReferenceFrame`**, a structure, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/ReferenceFrame.lean#L48).

> A time origin and a time-indexed spatial origin and basis in `d`-dimensional space.

```lean
structure ReferenceFrame (d : ℕ) where
  /-- The instant assigned time coordinate zero. -/
  timeOrigin : Time
  /-- The point assigned coordinate zero at each time. -/
  origin : Time → Space d
  /-- The basis used to turn displacement vectors into coordinate components at each time. -/
  basis : Time → Module.Basis (Fin d) ℝ (EuclideanSpace ℝ (Fin d))
```

**`ClassicalMechanics.ReferenceFrame.fromReferencePoints`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/ReferenceFrame.lean#L62).

> Build a reference frame from the trajectories of a collection of reference points.
>
> At each time, the reference points must form an affine basis: none is redundant, and together they
> span the whole space. One reference point is chosen as the origin, and the displacements from it to
> the remaining points form the coordinate basis. The resulting frame need not be inertial or
> orthonormal.

```lean
def ReferenceFrame.fromReferencePoints
    (timeOrigin : Time)
    (referencePoints : Finset (Time → Space d))
    (independence : ∀ t, AffineIndependent ℝ fun point : referencePoints => point.val t)
    (spans_space : ∀ t, affineSpan ℝ {point.val t | point : referencePoints} = ⊤) :
    ReferenceFrame d
```

**`ClassicalMechanics.ReferenceFrame.timeEquiv`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/ReferenceFrame.lean#L86).

> Convert a frame's real-valued time coordinate into an instant in affine time.

```lean
def timeEquiv (frame : ReferenceFrame d) : ℝ ≃ᵃ[ℝ] Time
```

## B. Inertial reference frames

> In Newtonian mechanics, an inertial coordinate grid does not rotate or change scale, and its origin
> moves in a straight line at constant velocity. These conditions restrict the frame, not the
> particles described in that frame.

**`ClassicalMechanics.ReferenceFrame.IsMetricConserved`**, a def, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/ReferenceFrame.lean#L98).

> Whether the frame basis induces the same inner product on coordinates at every time.

```lean
def IsMetricConserved (frame : ReferenceFrame d) : Prop
```

**`ClassicalMechanics.ReferenceFrame.Orthonormal`**, a def, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/ReferenceFrame.lean#L103).

> Whether the frame's coordinate basis is orthonormal at every time.

```lean
def Orthonormal (frame : ReferenceFrame d) : Prop
```

**`ClassicalMechanics.ReferenceFrame.Orthonormal.isMetricConserved`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/ReferenceFrame.lean#L107).

> An orthonormal frame conserves its coordinate metric.

```lean
lemma Orthonormal.isMetricConserved (h : frame.Orthonormal) : frame.IsMetricConserved
```

**An instance with no name**, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/ReferenceFrame.lean#L111).

```lean
instance [h : Fact frame.Orthonormal] : Fact frame.IsMetricConserved
```

**`ClassicalMechanics.ReferenceFrame.IsInertial`**, a structure, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/ReferenceFrame.lean#L114).

> Whether a reference frame is related to its initial grid by uniform translation alone.

```lean
structure IsInertial (frame : ReferenceFrame d) : Prop where
  /-- Elapsed time times `velocity` is exactly the origin's displacement. -/
  origin_moves_uniformly :
    ∃ velocity, ∀ t₁ t₂, frame.origin t₂ -ᵥ frame.origin t₁ = (t₂ -ᵥ t₁) • velocity
  /-- The coordinate axes neither rotate nor change scale with time. -/
  basis_conserved : ∀ t₁ t₂, frame.basis t₁ = frame.basis t₂
```

**`ClassicalMechanics.ReferenceFrame.IsInertial.velocity`**, a def, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/ReferenceFrame.lean#L122).

> The time-independent velocity of an inertial frame's coordinate origin.

```lean
def IsInertial.velocity (h : frame.IsInertial) : EuclideanSpace ℝ (Fin d)
```

**`ClassicalMechanics.ReferenceFrame.IsInertial.isMetricConserved`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/ReferenceFrame.lean#L126).

> An inertial frame conserves its coordinate metric.

```lean
lemma IsInertial.isMetricConserved (h : frame.IsInertial) : frame.IsMetricConserved
```

**An instance with no name**, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/ReferenceFrame.lean#L131).

> Inertiality provides the conserved metric needed for metric operations on frame vectors.

```lean
instance [h : Fact frame.IsInertial] : Fact frame.IsMetricConserved
```

## C. Vectors in a reference frame

> `frame.Vector` is the common coordinate carrier for vector quantities expressed relative to
> `frame`. It intentionally records the coordinate frame but not the physical dimension, so relative
> position, velocity, acceleration, force, momentum, and similar quantities can use the same
> componentwise calculations. Their different physical roles, units, and transformation laws must be
> supplied by the surrounding definitions. When a vector represents a displacement, `dispEquiv`
> converts its coordinates into the corresponding geometric displacement at a given time.

**`ClassicalMechanics.ReferenceFrame.Vector`**, a structure, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/ReferenceFrame.lean#L145).

> The `d` real components used to express a vector quantity relative to `frame`.

```lean
structure Vector (frame : ReferenceFrame d) where
  /-- One scalar coefficient for each axis of the frame. -/
  components : Fin d → ℝ
```

**`ClassicalMechanics.ReferenceFrame.Vector.componentEquiv`**, a def, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/ReferenceFrame.lean#L152).

> Equivalence between frame vectors and coordinate components

```lean
def componentEquiv : frame.Vector ≃ (Fin d → ℝ)
```

**An instance with no name**, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/ReferenceFrame.lean#L155).

```lean
instance : AddCommGroup frame.Vector
```

**An instance with no name**, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/ReferenceFrame.lean#L157).

```lean
instance : Module ℝ frame.Vector
```

**An instance with no name**, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/ReferenceFrame.lean#L161).

> Scalar multiplication by a positive real.

```lean
instance : SMul {x : ℝ // 0 < x} frame.Vector
```

**`ClassicalMechanics.ReferenceFrame.Vector.componentLinearEquiv`**, a def, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/ReferenceFrame.lean#L165).

> Linear equivalence between frame vectors and coordinate components.

```lean
def componentLinearEquiv : frame.Vector ≃ₗ[ℝ] (Fin d → ℝ)
```

**`ClassicalMechanics.ReferenceFrame.Vector.dispEquiv`**, a def, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/ReferenceFrame.lean#L170).

> Equivalence between frame vectors and geometric displacements in space,
> defined by the frame's basis at time coordinate `t`.

```lean
def dispEquiv (t : ℝ) : frame.Vector ≃ₗ[ℝ] EuclideanSpace ℝ (Fin d)
```

**An instance with no name**, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/ReferenceFrame.lean#L174).

> Use the same topology for frame vectors as components' product topology.

```lean
instance : TopologicalSpace frame.Vector
```

**`ClassicalMechanics.ReferenceFrame.Vector.componentContLinearEquiv`**, a def, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/ReferenceFrame.lean#L177).

> Continuous linear equivalence between frame vectors and coordinate components.

```lean
def componentContLinearEquiv (frame : ReferenceFrame d) : frame.Vector ≃L[ℝ] (Fin d → ℝ)
```

**An instance with no name**, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/ReferenceFrame.lean#L182).

```lean
instance : FiniteDimensional ℝ frame.Vector
```

**`ClassicalMechanics.ReferenceFrame.Vector.contDispEquiv`**, a def, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/ReferenceFrame.lean#L187).

> Continuous equivalence between frame vectors and geometric displacements in space,
> defined by the frame's basis at time coordinate `t`.

```lean
def contDispEquiv (t : ℝ) : frame.Vector ≃L[ℝ] EuclideanSpace ℝ (Fin d)
```

**An instance with no name**, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/ReferenceFrame.lean#L192).

> The physical norm on frame vectors, pulled back from geometric displacement space.

```lean
instance [_h : Fact frame.IsMetricConserved] : NormedAddCommGroup frame.Vector
```

**An instance with no name**, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/ReferenceFrame.lean#L200).

> The physical inner product on frame vectors, pulled back from geometric displacement space.

```lean
instance [Fact frame.IsMetricConserved] : InnerProductSpace ℝ frame.Vector
```

**`ClassicalMechanics.ReferenceFrame.Vector.norm_euclidean_if_orthonormal`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/ReferenceFrame.lean#L209).

> In an orthonormal frame, the norm is the square root of squared components.

```lean
lemma norm_euclidean_if_orthonormal [h : Fact frame.Orthonormal] :
    ∀ v : frame.Vector, ‖v‖^2 = ∑ i, (v.components i)^2
```

**`ClassicalMechanics.ReferenceFrame.Vector.inner_euclidean_if_orthonormal`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/ReferenceFrame.lean#L219).

> In an orthonormal frame, the inner product is the sum of component products.

```lean
lemma inner_euclidean_if_orthonormal [h : Fact frame.Orthonormal] :
    ∀ v w : frame.Vector, inner ℝ v w = ∑ i, v.components i * w.components i
```

## Depends on

- [Space](space/part-01/basic.md)
- [Time](time/basic.md)

## Sources

- [Physlib/SpaceAndTime/ReferenceFrame.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/ReferenceFrame.lean)
