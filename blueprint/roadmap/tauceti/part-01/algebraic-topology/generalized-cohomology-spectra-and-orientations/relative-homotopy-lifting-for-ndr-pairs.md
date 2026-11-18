---
declaration: theorem
origin: cited
lean: TauCeti.IsHurewiczFibration.exists_lift_of_ndrPair
statement: formalized
proof: formalized
---

# Relative homotopy lifting for NDR pairs

Let `(X, A)` be an NDR pair and `p` a Hurewicz
fibration. A homotopy `H : I × X → B` lifts to a homotopy `G : I × X → E` with prescribed initial
lift `f` and prescribed lift `g` over `I × A`, provided `f` and `g` agree at time `0`.

```lean
TauCeti.IsHurewiczFibration.exists_lift_of_ndrPair.{w, u, v} {E : Type u} {B : Type v}
  [TopologicalSpace E] [TopologicalSpace B] {p : E → B} (hp : TauCeti.IsHurewiczFibration p)
  {X : Type w} [TopologicalSpace X] {A : Set X} (N : TauCeti.NDRPair A) (f : C(X, E))
  (H : C(↑unitInterval × X, B)) (hH : ∀ (x : X), H (0, x) = p (f x)) (g : C(↑unitInterval × ↑A, E))
  (hg : ∀ (t : ↑unitInterval) (a : ↑A), p (g (t, a)) = H (t, ↑a))
  (hgf : ∀ (a : ↑A), g (0, a) = f ↑a) :
  ∃ G,
    p ∘ ⇑G = ⇑H ∧ (∀ (x : X), G (0, x) = f x) ∧ ∀ (t : ↑unitInterval) (a : ↑A), G (t, ↑a) = g (t, a)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsHurewiczFibration.exists_lift_of_ndrPair`](https://taucetiproject.org/docs/TauCeti/Topology/Homotopy/HurewiczFibration/RelativeLifting.html#TauCeti.IsHurewiczFibration.exists_lift_of_ndrPair).

## Sources

- [Tau Ceti documentation: `TauCeti.IsHurewiczFibration.exists_lift_of_ndrPair`](https://taucetiproject.org/docs/TauCeti/Topology/Homotopy/HurewiczFibration/RelativeLifting.html#TauCeti.IsHurewiczFibration.exists_lift_of_ndrPair)
- [Source of `TauCeti.IsHurewiczFibration.exists_lift_of_ndrPair` in TauCeti/Topology/Homotopy/HurewiczFibration/RelativeLifting.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Homotopy/HurewiczFibration/RelativeLifting.lean#L44)
- [Tau Ceti roadmap status: Generalized cohomology, spectra and orientations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeneralizedCohomology/STATUS.md)
