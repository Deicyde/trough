---
declaration: module
origin: cited
lean: ClassicalMechanics.ReferenceFrame.Force, ClassicalMechanics.ReferenceFrame.InternalForce, ClassicalMechanics.ReferenceFrame.InternalForce.reverse, ClassicalMechanics.ReferenceFrame.netForce
statement: formalized
proof: formalized
---

# Forces

The module `Physlib.ClassicalMechanics.Force`, [Physlib/ClassicalMechanics/Force.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Force.lean): 7 declarations (3 instances with no name), 4 with a docstring.

> This module defines forces acting on objects, expressed in a reference frame.
> A `Force` records its target and its vector value over time. An `InternalForce`
> additionally records a distinct source object.
>
> The time-dependent vector describes the force acting on the target, without
> prescribing how that force is determined. For example, a gravitational force can
> be specified directly from the target's mass, while a constraint force can be
> specified by its relation to the motion of the objects. Representing both by the
> same type allows Newton's laws to be stated independently of the particular
> interactions present.
>
> The reference frame appears in the type of a force's vector values, keeping their
> coordinate dependence explicit. The definition lives in the
> `ClassicalMechanics.ReferenceFrame` namespace to support dot notation such as
> `frame.Force Object`, but also occupies a general name that future non-particle
> Newtonian formalizations may need.
>
> The target type `Object` is therefore deliberately left arbitrary. Newtonian mechanics is
> not limited to point particles, so this force representation is kept independent
> of any particular model of matter, with the intention it may get generalized for
> rigid body mechanics, continuum mechanics, or other Newtonian models in the future.

**`ClassicalMechanics.ReferenceFrame.Force`**, a structure, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Force.lean#L45).

> A time-dependent force acting on an object.

```lean
structure Force (frame : ReferenceFrame d) (Object : Type) where
  /-- The force vector. -/
  value : ℝ → frame.Vector
  /-- The target object. -/
  target : Object
```

**An instance with no name**, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Force.lean#L51).

```lean
instance : CoeFun (frame.Force Object) (fun _ => ℝ → frame.Vector)
```

**`ClassicalMechanics.ReferenceFrame.InternalForce`**, a structure, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Force.lean#L55).

> A force between two objects.

```lean
structure InternalForce (frame : ReferenceFrame d) (Object : Type) extends frame.Force Object where
  /-- The source object. -/
  source : Object
  source_ne_target : source ≠ target
```

**An instance with no name**, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Force.lean#L60).

```lean
instance : CoeFun (frame.InternalForce Object) (fun _ => ℝ → frame.Vector)
```

**An instance with no name**, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Force.lean#L63).

```lean
instance : Coe (frame.InternalForce Object) (frame.Force Object)
```

**`ClassicalMechanics.ReferenceFrame.InternalForce.reverse`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Force.lean#L67).

> The equal-and-opposite force with source and target exchanged.

```lean
def InternalForce.reverse (force : frame.InternalForce Object) : frame.InternalForce Object
```

**`ClassicalMechanics.ReferenceFrame.netForce`**, a def, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Force.lean#L74).

> The net force on `object`.

```lean
def netForce (object : Object) (internalForces : Multiset (frame.InternalForce Object))
    (externalForces : Multiset (frame.Force Object)) (t : ℝ) : frame.Vector
```

## Depends on

- [Reference frames](../spaceandtime/referenceframe.md)

## Sources

- [Physlib/ClassicalMechanics/Force.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Force.lean)
