---
declaration: theorem
origin: cited
lean: TauCeti.natCard_zerothHomotopy_sphere_compl_range_eq_two, TauCeti.not_isPreconnected_compl_range_sphere
statement: formalized
proof: formalized
---

# The Jordan–Brouwer separation theorem

The complement of the image of a continuous injection
of the unit sphere of a finite-dimensional real normed space `E` into the unit sphere of a real
normed space of dimension `dim E + 1` has exactly two path components (Hatcher,
*Algebraic Topology*, Corollary 2B.2).

```lean
TauCeti.natCard_zerothHomotopy_sphere_compl_range_eq_two.{w, u} {F : Type w} [NormedAddCommGroup F]
  [NormedSpace ℝ F] {E : Type u} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  {h : ↑(Metric.sphere 0 1) → ↑(Metric.sphere 0 1)}
  (hEF : Module.finrank ℝ F = Module.finrank ℝ E + 1) (hc : Continuous h)
  (hi : Function.Injective h) : Nat.card (ZerothHomotopy ↑(Set.range h)ᶜ) = 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Mayer–Vietoris isomorphism of a sphere](../../../../algebraic-topology/singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)
- [The reduced Mayer–Vietoris connecting morphism is an isomorphism when both open sets are acyclic in the adjacent degrees](../../../../algebraic-topology/singular/the-reduced-mayer-vietoris-connecting-morphism-i.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.natCard_zerothHomotopy_sphere_compl_range_eq_two`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/JordanBrouwer.html#TauCeti.natCard_zerothHomotopy_sphere_compl_range_eq_two).

## Other forms

**The Jordan–Brouwer separation theorem, connected form.** Formalized in Tau Ceti as [`TauCeti.not_isPreconnected_compl_range_sphere`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/JordanBrouwer.html#TauCeti.not_isPreconnected_compl_range_sphere).

```lean
TauCeti.not_isPreconnected_compl_range_sphere.{w, u} {F : Type w} [NormedAddCommGroup F]
  [NormedSpace ℝ F] {E : Type u} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  {h : ↑(Metric.sphere 0 1) → ↑(Metric.sphere 0 1)}
  (hEF : Module.finrank ℝ F = Module.finrank ℝ E + 1) (hc : Continuous h)
  (hi : Function.Injective h) : ¬IsPreconnected (Set.range h)ᶜ
```

## Sources

- [Tau Ceti documentation: `TauCeti.natCard_zerothHomotopy_sphere_compl_range_eq_two`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/JordanBrouwer.html#TauCeti.natCard_zerothHomotopy_sphere_compl_range_eq_two)
- [Source of `TauCeti.natCard_zerothHomotopy_sphere_compl_range_eq_two` in TauCeti/AlgebraicTopology/Singular/JordanBrouwer.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/Singular/JordanBrouwer.lean#L214)
- [Tau Ceti roadmap status: Conformal mapping and the geometric theory of holomorphic functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ConformalMapping/STATUS.md)
- [Tau Ceti roadmap status: Geometric topology and the solved Kirby-list problems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GeometricTopology/STATUS.md)
