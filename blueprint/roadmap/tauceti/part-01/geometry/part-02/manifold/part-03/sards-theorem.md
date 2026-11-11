---
declaration: theorem
origin: cited
lean: ContMDiff.isNullSet_image_criticalPoints, TauCeti.isNullSet_image_of_not_isRegularPoint_of_contMDiffAt, TauCeti.isNullSet_image_criticalPoints, TauCeti.isNullSet_image_of_not_isRegularPoint, TauCeti.isNullSet_image_of_finrank_lt_finrank, TauCeti.isMeagre_image_of_not_isRegularPoint
statement: formalized
proof: formalized
---

# Sard's theorem

The critical values of a `C^k` map from a boundaryless Lindelöf manifold
of dimension `m` to a manifold of dimension `n` form a null set when `k > m - n` and `k ≥ 1`, in
particular when the map is smooth.

```lean
ContMDiff.isNullSet_image_criticalPoints.{u_1, u_2, u_3, u_4, u_5, u_6} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [LindelofSpace M] {E' : Type u_4} [NormedAddCommGroup E'] [NormedSpace ℝ E']
  [FiniteDimensional ℝ E'] [MeasurableSpace E'] [BorelSpace E'] {H' : Type u_5}
  [TopologicalSpace H'] {J : ModelWithCorners ℝ E' H'} {N : Type u_6} [TopologicalSpace N]
  [ChartedSpace H' N] {f : M → N} [I.Boundaryless] {n : WithTop ℕ∞} [IsManifold I n M]
  [IsManifold J n N] (hf : ContMDiff I J n f)
  (hk : ↑(Module.finrank ℝ E - Module.finrank ℝ E' + 1) ≤ n) :
  TauCeti.IsNullSet J (f '' {x | ¬TauCeti.IsRegularPoint I J f x})
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Morse--Sard theorem](../../../../analysis/part-02/calculus/part-01/the-morse-sard-theorem.md)
- [Sard's lemma in equal dimensions](../../../../analysis/part-02/calculus/part-02/sards-lemma-in-equal-dimensions.md)
- [The Sard--Smale theorem](../../../../analysis/part-01/analytic-heegaard-floer-homology/the-sard-smale-theorem.md)

## Lean

Formalized in Tau Ceti as [`ContMDiff.isNullSet_image_criticalPoints`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Sard/Basic.html#ContMDiff.isNullSet_image_criticalPoints).

## Other forms

**Sard's theorem.** Formalized in Tau Ceti as [`TauCeti.isNullSet_image_of_not_isRegularPoint_of_contMDiffAt`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Sard/Basic.html#TauCeti.isNullSet_image_of_not_isRegularPoint_of_contMDiffAt).

```lean
TauCeti.isNullSet_image_of_not_isRegularPoint_of_contMDiffAt.{u_1, u_2, u_3, u_4, u_5, u_6}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [LindelofSpace M] {E' : Type u_4} [NormedAddCommGroup E'] [NormedSpace ℝ E']
  [FiniteDimensional ℝ E'] [MeasurableSpace E'] [BorelSpace E'] {H' : Type u_5}
  [TopologicalSpace H'] {J : ModelWithCorners ℝ E' H'} {N : Type u_6} [TopologicalSpace N]
  [ChartedSpace H' N] {f : M → N} {s : Set M} [I.Boundaryless] {n : WithTop ℕ∞} [IsManifold I n M]
  [IsManifold J n N] (hk : ↑(Module.finrank ℝ E - Module.finrank ℝ E' + 1) ≤ n)
  (hf : ∀ x ∈ s, ContMDiffAt I J n f x) (hs : ∀ x ∈ s, ¬TauCeti.IsRegularPoint I J f x) :
  TauCeti.IsNullSet J (f '' s)
```

**Sard's theorem in equal dimensions.** Formalized in Tau Ceti as [`TauCeti.isNullSet_image_criticalPoints`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Sard/EqualDimension.html#TauCeti.isNullSet_image_criticalPoints).

```lean
TauCeti.isNullSet_image_criticalPoints.{u_1, u_2, u_3, u_4, u_5, u_6} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [IsManifold I 1 M] {E' : Type u_4} [NormedAddCommGroup E'] [NormedSpace ℝ E']
  [FiniteDimensional ℝ E'] {H' : Type u_5} [TopologicalSpace H'] {J : ModelWithCorners ℝ E' H'}
  {N : Type u_6} [TopologicalSpace N] [ChartedSpace H' N] [IsManifold J 1 N] {f : M → N}
  [LindelofSpace M] [MeasurableSpace E'] [BorelSpace E']
  (hdim : Module.finrank ℝ E = Module.finrank ℝ E') (hf : MDiff f) :
  TauCeti.IsNullSet J (f '' {x | ¬TauCeti.IsRegularPoint I J f x})
```

**Sard's theorem in equal dimensions, for a set of non-regular points.** Formalized in Tau Ceti as [`TauCeti.isNullSet_image_of_not_isRegularPoint`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Sard/EqualDimension.html#TauCeti.isNullSet_image_of_not_isRegularPoint).

```lean
TauCeti.isNullSet_image_of_not_isRegularPoint.{u_1, u_2, u_3, u_4, u_5, u_6} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [IsManifold I 1 M] {E' : Type u_4} [NormedAddCommGroup E'] [NormedSpace ℝ E']
  [FiniteDimensional ℝ E'] {H' : Type u_5} [TopologicalSpace H'] {J : ModelWithCorners ℝ E' H'}
  {N : Type u_6} [TopologicalSpace N] [ChartedSpace H' N] [IsManifold J 1 N] {f : M → N} {s : Set M}
  [LindelofSpace M] [MeasurableSpace E'] [BorelSpace E']
  (hdim : Module.finrank ℝ E = Module.finrank ℝ E') (hf : ∀ x ∈ s, MDiffAt f x)
  (hs : ∀ x ∈ s, ¬TauCeti.IsRegularPoint I J f x) : TauCeti.IsNullSet J (f '' s)
```

**Sard's theorem when the source has smaller dimension.** Formalized in Tau Ceti as [`TauCeti.isNullSet_image_of_finrank_lt_finrank`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Sard/Basic.html#TauCeti.isNullSet_image_of_finrank_lt_finrank).

```lean
TauCeti.isNullSet_image_of_finrank_lt_finrank.{u_1, u_2, u_3, u_4, u_5, u_6} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [LindelofSpace M] {E' : Type u_4} [NormedAddCommGroup E'] [NormedSpace ℝ E']
  [MeasurableSpace E'] [BorelSpace E'] {H' : Type u_5} [TopologicalSpace H']
  {J : ModelWithCorners ℝ E' H'} {N : Type u_6} [TopologicalSpace N] [ChartedSpace H' N] {f : M → N}
  {s : Set M} [IsManifold I 1 M] [IsManifold J 1 N]
  (hdim : Module.finrank ℝ E < Module.finrank ℝ E') (hf : ∀ x ∈ s, MDiffAt f x) :
  TauCeti.IsNullSet J (f '' s)
```

**Sard's theorem, in Baire category form.** Formalized in Tau Ceti as [`TauCeti.isMeagre_image_of_not_isRegularPoint`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Sard/Meagre.html#TauCeti.isMeagre_image_of_not_isRegularPoint).

```lean
TauCeti.isMeagre_image_of_not_isRegularPoint.{u_1, u_2, u_3, u_4, u_5, u_6} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M] {E' : Type u_4}
  [NormedAddCommGroup E'] [NormedSpace ℝ E'] [FiniteDimensional ℝ E'] {H' : Type u_5}
  [TopologicalSpace H'] {J : ModelWithCorners ℝ E' H'} [J.Boundaryless] {N : Type u_6}
  [TopologicalSpace N] [ChartedSpace H' N] [IsManifold J (↑⊤) N] {f : M → N} {s : Set M}
  [LindelofSpace ↑s] (hf : ∀ x ∈ s, ContMDiffAt I J (↑⊤) f x)
  (hs : ∀ x ∈ s, ¬TauCeti.IsRegularPoint I J f x) : IsMeagre (f '' s)
```

## Sources

- [Tau Ceti documentation: `ContMDiff.isNullSet_image_criticalPoints`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Sard/Basic.html#ContMDiff.isNullSet_image_criticalPoints)
- [Source of `ContMDiff.isNullSet_image_criticalPoints` in TauCeti/Geometry/Manifold/Sard/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Sard/Basic.lean#L159)
