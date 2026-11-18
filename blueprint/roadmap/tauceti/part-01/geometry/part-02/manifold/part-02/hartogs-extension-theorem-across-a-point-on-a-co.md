---
declaration: theorem
origin: cited
lean: TauCeti.exists_mdifferentiableOn_eqOn_sdiff_singleton, TauCeti.exists_mdifferentiableOn_eqOn_sdiff_of_isDiscrete, TauCeti.exists_mdifferentiableOn_eqOn_sdiff_of_finite
statement: formalized
proof: formalized
---

# Hartogs' extension theorem across a point on a complex manifold

If
`2 ≤ Module.finrank ℂ E` and `U ⊆ M` is open, every map `f : M → F` holomorphic on `U \ {p}`
extends to a holomorphic map on `U`.

```lean
TauCeti.exists_mdifferentiableOn_eqOn_sdiff_singleton.{u_1, u_2, u_3, u_4} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℂ E] [FiniteDimensional ℂ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℂ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 1 M] {F : Type u_4} [NormedAddCommGroup F]
  [NormedSpace ℂ F] [CompleteSpace F] (hE : 2 ≤ Module.finrank ℂ E) {f : M → F} {U : Set M}
  (hU : IsOpen U) (p : M) (hf : MDiff[U \ {p}] f) : ∃ g, MDiff[U] g ∧ Set.EqOn g f (U \ {p})
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hartogs' local removable singularity theorem on complex manifolds](hartogs-local-removable-singularity-theorem-on-c.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_mdifferentiableOn_eqOn_sdiff_singleton`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/Hartogs.html#TauCeti.exists_mdifferentiableOn_eqOn_sdiff_singleton).

## Other forms

**Hartogs' extension theorem across a closed discrete set on a complex manifold.** Formalized in Tau Ceti as [`TauCeti.exists_mdifferentiableOn_eqOn_sdiff_of_isDiscrete`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/Hartogs.html#TauCeti.exists_mdifferentiableOn_eqOn_sdiff_of_isDiscrete).

```lean
TauCeti.exists_mdifferentiableOn_eqOn_sdiff_of_isDiscrete.{u_1, u_2, u_3, u_4} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℂ E] [FiniteDimensional ℂ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℂ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 1 M] {F : Type u_4} [NormedAddCommGroup F]
  [NormedSpace ℂ F] [CompleteSpace F] (hE : 2 ≤ Module.finrank ℂ E) {f : M → F} {U S : Set M}
  (hU : IsOpen U) (hUS : IsOpen (U \ S)) (hS : IsDiscrete (U ∩ S)) (hf : MDiff[U \ S] f) :
  ∃ g, MDiff[U] g ∧ Set.EqOn g f (U \ S)
```

**Hartogs' extension theorem across a finite set on a complex manifold.** Formalized in Tau Ceti as [`TauCeti.exists_mdifferentiableOn_eqOn_sdiff_of_finite`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/Hartogs.html#TauCeti.exists_mdifferentiableOn_eqOn_sdiff_of_finite).

```lean
TauCeti.exists_mdifferentiableOn_eqOn_sdiff_of_finite.{u_1, u_2, u_3, u_4} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℂ E] [FiniteDimensional ℂ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℂ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 1 M] {F : Type u_4} [NormedAddCommGroup F]
  [NormedSpace ℂ F] [CompleteSpace F] (hE : 2 ≤ Module.finrank ℂ E) {f : M → F} {U S : Set M}
  (hU : IsOpen U) (hS : S.Finite) (hf : MDiff[U \ S] f) : ∃ g, MDiff[U] g ∧ Set.EqOn g f (U \ S)
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_mdifferentiableOn_eqOn_sdiff_singleton`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/Hartogs.html#TauCeti.exists_mdifferentiableOn_eqOn_sdiff_singleton)
- [Source of `TauCeti.exists_mdifferentiableOn_eqOn_sdiff_singleton` in TauCeti/Geometry/Manifold/Complex/Hartogs.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Complex/Hartogs.lean#L166)
