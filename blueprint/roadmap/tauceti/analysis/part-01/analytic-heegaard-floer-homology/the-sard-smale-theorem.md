---
declaration: theorem
origin: cited
lean: TauCeti.isMeagre_image_criticalPoints_of_isFredholm
statement: formalized
proof: formalized
---

# The Sard--Smale theorem

The critical values of a sufficiently smooth Fredholm map on a
Lindelöf subset of a Banach space form a meagre set. The subset need not be open; smoothness
is assumed at each of its points in the ambient space. Every subset of a separable Banach space
is Lindelöf.

Sard's theorem itself is false in infinite dimensions, and "measure zero" has no meaning there;
what survives is that the Fredholm condition confines the failure of regularity to a
finite-dimensional direction, in which the finite-dimensional theorem applies fibrewise.

The regularity threshold is the pointwise one of
`TauCeti.exists_mem_nhds_isClosed_isNowhereDense_image_criticalPoints`: at each point `C^k` with
`k ≥ (dim ker)² + 1`. In particular `n = ∞` needs no side condition.

```lean
TauCeti.isMeagre_image_criticalPoints_of_isFredholm.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F]
  [CompleteSpace E] [CompleteSpace F] {U : Set E} [LindelofSpace ↑U] {f : E → F} {n : WithTop ℕ∞}
  (hf : ∀ x ∈ U, ContDiffAt ℝ n f x) (hFred : ∀ x ∈ U, (fderiv ℝ f x).IsFredholm)
  (hn :
    ∀ x ∈ U,
      ↑(Module.finrank ℝ ↥(↑(fderiv ℝ f x)).ker * Module.finrank ℝ ↥(↑(fderiv ℝ f x)).ker + 1) ≤
        n) :
  IsMeagre (f '' (U ∩ {x | ¬Function.Surjective ⇑(fderiv ℝ f x)}))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Morse--Sard theorem](the-morse-sard-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isMeagre_image_criticalPoints_of_isFredholm`](https://taucetiproject.org/docs/TauCeti/Analysis/Fredholm/SardSmale.html#TauCeti.isMeagre_image_criticalPoints_of_isFredholm).

## Sources

- [Tau Ceti documentation: `TauCeti.isMeagre_image_criticalPoints_of_isFredholm`](https://taucetiproject.org/docs/TauCeti/Analysis/Fredholm/SardSmale.html#TauCeti.isMeagre_image_criticalPoints_of_isFredholm)
- [Source of `TauCeti.isMeagre_image_criticalPoints_of_isFredholm` in TauCeti/Analysis/Fredholm/SardSmale.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Fredholm/SardSmale.lean#L397)
- [Tau Ceti roadmap status: Analytic Heegaard Floer homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/HeegaardFloer/STATUS.md)
