---
declaration: theorem
origin: cited
lean: TauCeti.IsMorse.nonempty_homeomorph_sphere_of_totalCriticalCount_eq_two
statement: formalized
proof: formalized
---

# Reeb's theorem (Milnor, *Morse Theory*, Theorem 4.1)

A compact boundaryless manifold
modelled on a real vector space of dimension `n` which carries a Morse function with exactly two
critical points is homeomorphic to the sphere `Sⁿ`.

```lean
TauCeti.IsMorse.nonempty_homeomorph_sphere_of_totalCriticalCount_eq_two.{u_1, u_2, u_3}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [FiniteDimensional ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless]
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M] [T2Space M] [CompactSpace M]
  {f : M → ℝ} (hf : TauCeti.IsMorse I f) (h2 : TauCeti.totalCriticalCount I f = 2) :
  Nonempty (M ≃ₜ ↑(Metric.sphere 0 1))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Fermat's theorem on a manifold](fermats-theorem-on-a-manifold.md)
- [The normalized Morse lemma on a manifold](the-normalized-morse-lemma-on-a-manifold.md)
- [Sublevels on either side of a band without critical points are diffeomorphic (Milnor, Theorem 3.1)](sublevels-on-either-side-of-a-band-without-criti.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsMorse.nonempty_homeomorph_sphere_of_totalCriticalCount_eq_two`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Reeb.html#TauCeti.IsMorse.nonempty_homeomorph_sphere_of_totalCriticalCount_eq_two).

## Sources

- [Tau Ceti documentation: `TauCeti.IsMorse.nonempty_homeomorph_sphere_of_totalCriticalCount_eq_two`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Reeb.html#TauCeti.IsMorse.nonempty_homeomorph_sphere_of_totalCriticalCount_eq_two)
- [Source of `TauCeti.IsMorse.nonempty_homeomorph_sphere_of_totalCriticalCount_eq_two` in TauCeti/Geometry/Manifold/Morse/Reeb.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Morse/Reeb.lean#L137)
