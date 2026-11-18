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
- [Source of `AddTorsor` in Mathlib/Algebra/Torsor/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Algebra/Torsor/Defs.lean#L51)
- [Mathlib overview: Geometry › Affine and Euclidean geometry](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L431)
- [Mathlib undergraduate list: Affine and Euclidean Geometry › General definitions](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L244)
