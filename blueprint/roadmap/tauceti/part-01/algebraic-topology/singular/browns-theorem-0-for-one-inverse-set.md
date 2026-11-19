---
declaration: theorem
origin: cited
lean: IsOpen.image_of_continuousOn_of_injOn_sdiff
statement: formalized
proof: formalized
---

# Brown's Theorem 0, for one inverse set

Let `E` and `F` be finite-dimensional real normed
spaces of the same dimension, and let `f : E → F` be continuous on an open set `U` and injective
on `U` away from the fibre `U ∩ f ⁻¹' {p}`. If this fibre is compact, then `f` maps `U` onto an
open set. For an empty fibre this is invariance of domain,
`IsOpen.image_of_continuousOn_of_injOn`.

```lean
IsOpen.image_of_continuousOn_of_injOn_sdiff.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [NormedAddCommGroup F]
  [NormedSpace ℝ F] [FiniteDimensional ℝ F] {f : E → F} {p : F} {U : Set E} (hU : IsOpen U)
  (hf : ContinuousOn f U) (hinj : Set.InjOn f (U \ f ⁻¹' {p})) (hM : IsCompact (U ∩ f ⁻¹' {p}))
  (hEF : Module.finrank ℝ E = Module.finrank ℝ F) : IsOpen (f '' U)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Jordan–Brouwer separation theorem](the-jordan-brouwer-separation-theorem.md)

## Lean

Formalized in Tau Ceti as [`IsOpen.image_of_continuousOn_of_injOn_sdiff`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/InvarianceOfDomain.html#IsOpen.image_of_continuousOn_of_injOn_sdiff).

## Sources

- [Tau Ceti documentation: `IsOpen.image_of_continuousOn_of_injOn_sdiff`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/InvarianceOfDomain.html#IsOpen.image_of_continuousOn_of_injOn_sdiff)
- [Source of `IsOpen.image_of_continuousOn_of_injOn_sdiff` in TauCeti/AlgebraicTopology/Singular/InvarianceOfDomain.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/Singular/InvarianceOfDomain.lean#L485)
