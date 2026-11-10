---
declaration: theorem
origin: cited
lean: RingHom.isHomeomorph_kerLift, LinearMap.quotKerContinuousLinearEquivOfSurjective
statement: formalized
proof: formalized
---

# The topological first isomorphism theorem for rings

A ring homomorphism that is a
quotient map presents its target as the quotient of its source by its kernel, topologically as
well as algebraically.

A continuous surjection is not enough on its own. Surjectivity of `f` makes the lift bijective and
continuity of `f` makes it continuous, but a continuous bijection is open only when the topology it
lands in is no coarser than the one it carries; that `f` is a quotient map is exactly the statement
that it is not coarser.

`IsHomeomorph.homeomorph` turns this into `R ⧸ ker f ≃ₜ S`. What it bundles is `RingHom.kerLift`,
which is a ring homomorphism, so a consumer needing the isomorphism of rings has it already —
`RingHom.quotientKerEquivOfSurjective` is that same map.

```lean
RingHom.isHomeomorph_kerLift.{u_1, u_2} {R : Type u_1} {S : Type u_2} [TopologicalSpace R]
  [CommRing R] [TopologicalSpace S] [Semiring S] {f : R →+* S} (hq : Topology.IsQuotientMap ⇑f) :
  IsHomeomorph ⇑f.kerLift
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`RingHom.isHomeomorph_kerLift`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Ring/Ideal.html#RingHom.isHomeomorph_kerLift).

## Other forms

**Topological first isomorphism theorem for the module topology.** Formalized in Tau Ceti as [`LinearMap.quotKerContinuousLinearEquivOfSurjective`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Module/ModuleTopology.html#LinearMap.quotKerContinuousLinearEquivOfSurjective).

```lean
LinearMap.quotKerContinuousLinearEquivOfSurjective.{u_1, u_2, u_3} {R : Type u_1} {M : Type u_2}
  {N : Type u_3} [Ring R] [TopologicalSpace R] [AddCommGroup M] [_root_.Module R M]
  [TopologicalSpace M] [IsModuleTopology R M] [AddCommGroup N] [_root_.Module R N]
  [TopologicalSpace N] [IsModuleTopology R N] (f : M →ₗ[R] N) (hf : Function.Surjective ⇑f) :
  (M ⧸ f.ker) ≃L[R] N
```

## Sources

- [Tau Ceti documentation: `RingHom.isHomeomorph_kerLift`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Ring/Ideal.html#RingHom.isHomeomorph_kerLift)
- [Source of `RingHom.isHomeomorph_kerLift` in TauCeti/Topology/Algebra/Ring/Ideal.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Ring/Ideal.lean#L225)
