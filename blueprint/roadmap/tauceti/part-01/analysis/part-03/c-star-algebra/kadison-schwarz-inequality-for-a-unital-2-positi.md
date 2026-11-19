---
declaration: theorem
origin: cited
lean: TauCeti.IsNPositive.star_map_mul_map_le_of_map_one, CompletelyPositiveMapClass.star_map_mul_map_le, CompletelyPositiveMapClass.star_map_mul_map_le_of_map_one, TauCeti.IsNPositive.star_map_mul_map_le
statement: formalized
proof: formalized
---

# Kadison–Schwarz inequality for a unital `2`-positive map

`φ(a)⋆ φ(a) ≤ φ(a⋆a)`.

```lean
TauCeti.IsNPositive.star_map_mul_map_le_of_map_one.{u_1, u_2} {A : Type u_1} {B : Type u_2}
  [CStarAlgebra A] [PartialOrder A] [StarOrderedRing A] [CStarAlgebra B] [PartialOrder B]
  [StarOrderedRing B] {φ : A →ₗ[ℂ] B} (hφ : TauCeti.IsNPositive 2 φ) (h1 : φ 1 = 1) (a : A) :
  star (φ a) * φ a ≤ φ (star a * a)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [CStarMatrix.nonneg_iff_forall_sum_nonneg](../../part-02/hilbert-c-modules-morita-equivalence-and-continu/cstarmatrix-nonneg-iff-forall-sum-nonneg.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsNPositive.star_map_mul_map_le_of_map_one`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/CompletelyPositiveMap.html#TauCeti.IsNPositive.star_map_mul_map_le_of_map_one).

## Other forms

**Kadison–Schwarz inequality for a completely positive map with unital domain.** Formalized in Tau Ceti as [`CompletelyPositiveMapClass.star_map_mul_map_le`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/CompletelyPositiveMap.html#CompletelyPositiveMapClass.star_map_mul_map_le).

```lean
CompletelyPositiveMapClass.star_map_mul_map_le.{u_1, u_2, u_3} {A : Type u_1} {B : Type u_2}
  {F : Type u_3} [CStarAlgebra A] [PartialOrder A] [StarOrderedRing A] [NonUnitalCStarAlgebra B]
  [PartialOrder B] [StarOrderedRing B] [FunLike F A B] [LinearMapClass F ℂ A B]
  [CompletelyPositiveMapClass F A B] (φ : F) (a : A) : star (φ a) * φ a ≤ ‖φ 1‖ • φ (star a * a)
```

**Kadison–Schwarz inequality for a unital completely positive map.** Formalized in Tau Ceti as [`CompletelyPositiveMapClass.star_map_mul_map_le_of_map_one`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/CompletelyPositiveMap.html#CompletelyPositiveMapClass.star_map_mul_map_le_of_map_one).

```lean
CompletelyPositiveMapClass.star_map_mul_map_le_of_map_one.{u_1, u_2, u_3} {A : Type u_1}
  {B : Type u_2} {F : Type u_3} [CStarAlgebra A] [PartialOrder A] [StarOrderedRing A]
  [CStarAlgebra B] [PartialOrder B] [StarOrderedRing B] [FunLike F A B] [LinearMapClass F ℂ A B]
  [CompletelyPositiveMapClass F A B] (φ : F) (hφ : φ 1 = 1) (a : A) :
  star (φ a) * φ a ≤ φ (star a * a)
```

**Kadison–Schwarz inequality for a `2`-positive map with unital domain.** Formalized in Tau Ceti as [`TauCeti.IsNPositive.star_map_mul_map_le`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/CompletelyPositiveMap.html#TauCeti.IsNPositive.star_map_mul_map_le).

```lean
TauCeti.IsNPositive.star_map_mul_map_le.{u_1, u_2} {A : Type u_1} {B : Type u_2} [CStarAlgebra A]
  [PartialOrder A] [StarOrderedRing A] [NonUnitalCStarAlgebra B] [PartialOrder B]
  [StarOrderedRing B] {φ : A →ₗ[ℂ] B} (hφ : TauCeti.IsNPositive 2 φ) (a : A) :
  star (φ a) * φ a ≤ ‖φ 1‖ • φ (star a * a)
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsNPositive.star_map_mul_map_le_of_map_one`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/CompletelyPositiveMap.html#TauCeti.IsNPositive.star_map_mul_map_le_of_map_one)
- [Source of `TauCeti.IsNPositive.star_map_mul_map_le_of_map_one` in TauCeti/Analysis/CStarAlgebra/CompletelyPositiveMap.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/CStarAlgebra/CompletelyPositiveMap.lean#L263)
