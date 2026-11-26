---
declaration: module
origin: cited
lean: ClassicalMechanics.ReferenceFrame, ClassicalMechanics.ReferenceFrame.timeEquiv, ClassicalMechanics.ReferenceFrame.Orthonormal, ClassicalMechanics.ReferenceFrame.velocity, ClassicalMechanics.ReferenceFrame.IsInertial, ClassicalMechanics.ReferenceFrame.IsInertial.velocity, ClassicalMechanics.ReferenceFrame.IsInertial.origin_vsub_eq, ClassicalMechanics.ReferenceFrame.IsInertial.of_relative_motion
statement: formalized
proof: formalized
---

# Reference frames

The module `Physlib.SpaceAndTime.ReferenceFrame`, [Physlib/SpaceAndTime/ReferenceFrame.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/ReferenceFrame.lean): 23 declarations (6 instances with no name), 18 with a docstring.

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

**`ClassicalMechanics.ReferenceFrame`**, a structure, [line 52](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/ReferenceFrame.lean#L52).

> A time origin and a time-indexed spatial origin and basis in `d`-dimensional space.

```lean
structure ReferenceFrame (d : ℕ) where
  /-- The instant assigned time coordinate zero. -/
  timeOrigin : Time
  /-- The point assigned coordinate zero at each time. -/
  origin : Time → Space d
  /-- The spatial origin is smooth. -/
  origin_smooth : ContMDiff 𝓘(ℝ) (𝓡 d) ∞ origin
  /-- The basis used to turn displacement vectors into coordinate components at each time. -/
  basis : Time → Module.Basis (Fin d) ℝ (EuclideanSpace ℝ (Fin d))
  /-- Each basis vector is smooth. -/
  basis_smooth : ∀ i, ContMDiff 𝓘(ℝ) (𝓡 d) ∞ (basis · i)
  /-- The pairwise inner products of the basis vectors are constant in time. -/
  gram_matrix_constant : (Matrix.gram ℝ <| basis ·).IsConst
```

**`ClassicalMechanics.ReferenceFrame.timeEquiv`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/ReferenceFrame.lean#L71).

> Convert a frame's real-valued time coordinate into an instant in affine time.

```lean
def timeEquiv : ℝ ≃ᵃ[ℝ] Time
```

**`ClassicalMechanics.ReferenceFrame.Orthonormal`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/ReferenceFrame.lean#L75).

> Whether the frame's coordinate basis is orthonormal at every time.

```lean
def Orthonormal : Prop
```

**`ClassicalMechanics.ReferenceFrame.velocity`**, a def, [line 79](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/ReferenceFrame.lean#L79).

> The geometric velocity of the frame's origin at time coordinate `t`.

```lean
def velocity (t : ℝ) : EuclideanSpace ℝ (Fin d)
```

## B. Inertial reference frames

> In Newtonian mechanics, an inertial coordinate grid does not rotate or change scale, and its origin
> moves in a straight line at constant velocity. These conditions restrict the frame, not the
> particles described in that frame.

**`ClassicalMechanics.ReferenceFrame.IsInertial`**, a structure, [line 91](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/ReferenceFrame.lean#L91).

> Whether a reference frame is related to its initial grid by uniform translation alone.

```lean
structure IsInertial (frame : ReferenceFrame d) : Prop where
  /-- The spatial origin has constant velocity. -/
  velocity_constant : frame.velocity.IsConst
  /-- The coordinate axes neither rotate nor change scale with time. -/
  basis_constant : frame.basis.IsConst
```

**`ClassicalMechanics.ReferenceFrame.IsInertial.velocity`**, a def, [line 102](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/ReferenceFrame.lean#L102).

> The time-independent velocity of an inertial frame's coordinate origin.

```lean
def velocity : EuclideanSpace ℝ (Fin d)
```

**`ClassicalMechanics.ReferenceFrame.IsInertial.origin_vsub_eq`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/ReferenceFrame.lean#L106).

> The origin of an inertial frame moves by elapsed time times its constant velocity.

```lean
lemma origin_vsub_eq (t₁ t₂ : Time) :
    frame.origin t₂ -ᵥ frame.origin t₁ = (t₂ -ᵥ t₁) • h.velocity
```

**`ClassicalMechanics.ReferenceFrame.IsInertial.of_relative_motion`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/ReferenceFrame.lean#L118).

> A frame with fixed axes moving uniformly relative to an inertial frame is inertial,
> with velocity given by addition of the ambient velocities.

```lean
lemma of_relative_motion {other : ReferenceFrame d} {u : EuclideanSpace ℝ (Fin d)}
    (hrel : ∀ t₁ t₂, (other.origin t₂ -ᵥ frame.origin t₂) -
      (other.origin t₁ -ᵥ frame.origin t₁) = (t₂ -ᵥ t₁) • u)
    (hbasis : ∀ t₁ t₂, other.basis t₁ = other.basis t₂) :
    ∃ h' : other.IsInertial, h'.velocity = h.velocity + u
```

## C. Vectors in a reference frame

> `frame.Vector` is the common coordinate carrier for vector quantities expressed relative to
> `frame`. It intentionally records the coordinate frame but not the physical dimension, so relative
> position, velocity, acceleration, force, momentum, and similar quantities can use the same
> componentwise calculations. Their different physical roles, units, and transformation laws must be
> supplied by the surrounding definitions. When a vector represents a displacement, `dispEquiv`
> converts its coordinates into the corresponding geometric displacement at a given time.

**`ClassicalMechanics.ReferenceFrame.Vector`**, a structure, [line 148](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/ReferenceFrame.lean#L148).

> The `d` real components used to express a vector quantity relative to `frame`.

```lean
structure Vector (frame : ReferenceFrame d) where
  /-- One scalar coefficient for each axis of the frame. -/
  components : Fin d → ℝ
```

**`ClassicalMechanics.ReferenceFrame.Vector.componentEquiv`**, a def, [line 157](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/ReferenceFrame.lean#L157).

> Equivalence between frame vectors and coordinate components

```lean
def componentEquiv : frame.Vector ≃ (Fin d → ℝ)
```

**An instance with no name**, [line 160](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/ReferenceFrame.lean#L160).

```lean
instance : AddCommGroup frame.Vector
```

**An instance with no name**, [line 162](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/ReferenceFrame.lean#L162).

```lean
instance : Module ℝ frame.Vector
```

**An instance with no name**, [line 166](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/ReferenceFrame.lean#L166).

> Scalar multiplication by a positive real.

```lean
instance : SMul {x : ℝ // 0 < x} frame.Vector
```

**`ClassicalMechanics.ReferenceFrame.Vector.componentLinearEquiv`**, a def, [line 170](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/ReferenceFrame.lean#L170).

> Linear equivalence between frame vectors and coordinate components.

```lean
def componentLinearEquiv : frame.Vector ≃ₗ[ℝ] (Fin d → ℝ)
```

**An instance with no name**, [line 173](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/ReferenceFrame.lean#L173).

```lean
instance : FiniteDimensional ℝ frame.Vector
```

**`ClassicalMechanics.ReferenceFrame.Vector.dispEquiv`**, a def, [line 178](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/ReferenceFrame.lean#L178).

> Equivalence between frame vectors and geometric displacements in space,
> defined by the frame's basis at time coordinate `t`.

```lean
def dispEquiv (t : ℝ) : frame.Vector ≃ₗ[ℝ] EuclideanSpace ℝ (Fin d)
```

**`ClassicalMechanics.ReferenceFrame.Vector.inducedInnerProduct`**, a def, [line 182](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/ReferenceFrame.lean#L182).

> The geometric inner product pulled back to frame vectors at time coordinate `t`.

```lean
def inducedInnerProduct (t : ℝ) : InnerProductSpace.Core ℝ frame.Vector
```

**`ClassicalMechanics.ReferenceFrame.Vector.inner_product_conserved`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/ReferenceFrame.lean#L191).

> The frame's constant Gram matrix makes the induced inner product independent of time.

```lean
lemma inner_product_conserved : inducedInnerProduct (frame := frame) |>.IsConst
```

**An instance with no name**, [line 197](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/ReferenceFrame.lean#L197).

```lean
instance : NormedAddCommGroup frame.Vector
```

**An instance with no name**, [line 200](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/ReferenceFrame.lean#L200).

```lean
instance : InnerProductSpace ℝ frame.Vector
```

**`ClassicalMechanics.ReferenceFrame.Vector.dispIsometry`**, a def, [line 204](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/ReferenceFrame.lean#L204).

> The linear isometry from frame vectors to geometric displacements at time `t`.

```lean
def dispIsometry (t : ℝ) : frame.Vector ≃ₗᵢ[ℝ] EuclideanSpace ℝ (Fin d)
```

**`ClassicalMechanics.ReferenceFrame.Vector.inner_euclidean_if_orthonormal`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/ReferenceFrame.lean#L208).

> In an orthonormal frame, the inner product is the sum of component products.

```lean
lemma inner_euclidean_if_orthonormal : frame.Orthonormal →
    ∀ v w : frame.Vector, ⟪v, w⟫ = ∑ i, v.components i * w.components i
```

**`ClassicalMechanics.ReferenceFrame.Vector.norm_euclidean_if_orthonormal`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/ReferenceFrame.lean#L218).

> In an orthonormal frame, the squared norm is the sum of squared components.

```lean
lemma norm_euclidean_if_orthonormal : frame.Orthonormal →
    ∀ v : frame.Vector, ‖v‖^2 = ∑ i, (v.components i)^2
```

## Depends on

- [The value of a constant function](../mathematics/formathlib/part-01/isconst.md)
- [Space](space/part-01/basic.md)
- [Time](time/basic.md)

## Sources

- [Physlib/SpaceAndTime/ReferenceFrame.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/ReferenceFrame.lean)
