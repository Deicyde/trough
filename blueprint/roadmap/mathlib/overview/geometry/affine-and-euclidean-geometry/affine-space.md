# Affine space

An `AddTorsor G P` gives a structure to the nonempty type `P`,
acted on by an `AddGroup G` with a transitive and free action given
by the `+ᵥ` operation and a corresponding subtraction given by the
`-ᵥ` operation. In the case of a vector space, it is an affine
space.

```lean
AddTorsor.{u_1, u_2} (G : outParam (Type u_1)) (P : Type u_2) [AddGroup G] : Type (max u_1 u_2)
```

## Depends on

- [Integer](../../general-algebra/numbers/integer.md)

## Sources

- [Mathlib documentation: `AddTorsor`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Torsor/Defs.html#AddTorsor)
- [Source of `AddTorsor` in Mathlib/Algebra/Torsor/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Algebra/Torsor/Defs.lean#L52)
- [Mathlib overview: Geometry › Affine and Euclidean geometry](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L431)
- [Mathlib undergraduate list: Affine and Euclidean Geometry › General definitions](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L244)
