---
declaration: theorem
origin: cited
lean: TauCeti.AbelianK0.eulerChar_eq_homologyEulerChar, TauCeti.AbelianK0.AdditiveInvariant.sum_negOnePow_obj_X_eq_sum_negOnePow_obj_homology, TauCeti.ExactK0.AdditiveInvariant.sum_negOnePow_obj_X_eq_sum_negOnePow_obj_homology, TauCeti.ExactK0.sum_negOnePow_of_X_eq_sum_negOnePow_of_homology
statement: formalized
proof: formalized
---

# The Euler–Poincaré theorem in abelian `K₀`

For a cochain complex that is strictly
supported in degrees `a` to `b`, and any finite range of degrees containing `[a, b]`, the
alternating sum of the classes of the terms equals the alternating sum of the classes of the
cohomology objects.

```lean
TauCeti.AbelianK0.eulerChar_eq_homologyEulerChar.{w, v, u} {A : Type u}
  [CategoryTheory.Category.{v, u} A] [CategoryTheory.Abelian A]
  [CategoryTheory.EssentiallySmall.{w, v, u} A] (K : CochainComplex A ℤ) (a b : ℤ)
  [K.IsStrictlyGE a] [K.IsStrictlyLE b] {s : Finset ℤ} (hs : Finset.Icc a b ⊆ s) :
  TauCeti.AbelianK0.eulerChar K s = TauCeti.AbelianK0.homologyEulerChar K s
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The dual Noether isomorphism](../exact/the-dual-noether-isomorphism.md)
- [The Noether isomorphism for exact categories](../exact/the-noether-isomorphism-for-exact-categories.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AbelianK0.eulerChar_eq_homologyEulerChar`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/GrothendieckGroup/EulerCharacteristic.html#TauCeti.AbelianK0.eulerChar_eq_homologyEulerChar).

## Other forms

**The Euler–Poincaré theorem for an additive invariant.** Formalized in Tau Ceti as [`TauCeti.AbelianK0.AdditiveInvariant.sum_negOnePow_obj_X_eq_sum_negOnePow_obj_homology`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/GrothendieckGroup/EulerCharacteristic.html#TauCeti.AbelianK0.AdditiveInvariant.sum_negOnePow_obj_X_eq_sum_negOnePow_obj_homology).

```lean
TauCeti.AbelianK0.AdditiveInvariant.sum_negOnePow_obj_X_eq_sum_negOnePow_obj_homology.{v, u, u_1}
  {A : Type u} [CategoryTheory.Category.{v, u} A] [CategoryTheory.Abelian A] {G : Type u_1}
  [AddCommGroup G] (v : TauCeti.AbelianK0.AdditiveInvariant A G) (K : CochainComplex A ℤ) (a b : ℤ)
  [K.IsStrictlyGE a] [K.IsStrictlyLE b] {s : Finset ℤ} (hs : Finset.Icc a b ⊆ s) :
  ∑ n ∈ s, ↑n.negOnePow • v.obj (K.X n) =
    ∑ n ∈ s, ↑n.negOnePow • v.obj (HomologicalComplex.homology K n)
```

**The Euler–Poincaré theorem in an extension-closed subcategory.** Formalized in Tau Ceti as [`TauCeti.ExactK0.AdditiveInvariant.sum_negOnePow_obj_X_eq_sum_negOnePow_obj_homology`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/GrothendieckGroup/EulerCharacteristic.html#TauCeti.ExactK0.AdditiveInvariant.sum_negOnePow_obj_X_eq_sum_negOnePow_obj_homology).

```lean
TauCeti.ExactK0.AdditiveInvariant.sum_negOnePow_obj_X_eq_sum_negOnePow_obj_homology.{v, u, u_1}
  {A : Type u} [CategoryTheory.Category.{v, u} A] [CategoryTheory.Abelian A]
  {P : CategoryTheory.ObjectProperty A} [P.ContainsZero] [P.IsClosedUnderBinaryProducts]
  {hP : (TauCeti.ExactStructure.abelian A).IsExtensionClosed P} {G : Type u_1} [AddCommGroup G]
  (v : TauCeti.ExactK0.AdditiveInvariant (TauCeti.ExactStructure.fullSubcategory P hP) G)
  {K : CochainComplex A ℤ} (hB : ∀ (n : ℤ), P (CategoryTheory.Abelian.image (K.d n (n + 1))))
  (hH : ∀ (n : ℤ), P (HomologicalComplex.homology K n)) (a b : ℤ) [K.IsStrictlyGE a]
  [K.IsStrictlyLE b] {s : Finset ℤ} (hs : Finset.Icc a b ⊆ s) :
  ∑ n ∈ s, ↑n.negOnePow • v.obj { obj := K.X n, property := ⋯ } =
    ∑ n ∈ s, ↑n.negOnePow • v.obj { obj := HomologicalComplex.homology K n, property := ⋯ }
```

**The Euler–Poincaré theorem in exact `K₀` of an extension-closed subcategory.** Formalized in Tau Ceti as [`TauCeti.ExactK0.sum_negOnePow_of_X_eq_sum_negOnePow_of_homology`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/GrothendieckGroup/EulerCharacteristic.html#TauCeti.ExactK0.sum_negOnePow_of_X_eq_sum_negOnePow_of_homology).

```lean
TauCeti.ExactK0.sum_negOnePow_of_X_eq_sum_negOnePow_of_homology.{w, v, u} {A : Type u}
  [CategoryTheory.Category.{v, u} A] [CategoryTheory.Abelian A]
  {P : CategoryTheory.ObjectProperty A} [P.ContainsZero] [P.IsClosedUnderBinaryProducts]
  (hP : (TauCeti.ExactStructure.abelian A).IsExtensionClosed P)
  [CategoryTheory.EssentiallySmall.{w, v, u} P.FullSubcategory] (K : CochainComplex A ℤ)
  (hB : ∀ (n : ℤ), P (CategoryTheory.Abelian.image (K.d n (n + 1))))
  (hH : ∀ (n : ℤ), P (HomologicalComplex.homology K n)) (a b : ℤ) [K.IsStrictlyGE a]
  [K.IsStrictlyLE b] {s : Finset ℤ} (hs : Finset.Icc a b ⊆ s) :
  ∑ n ∈ s, ↑n.negOnePow • TauCeti.ExactK0.of { obj := K.X n, property := ⋯ } =
    ∑ n ∈ s,
      ↑n.negOnePow • TauCeti.ExactK0.of { obj := HomologicalComplex.homology K n, property := ⋯ }
```

## Sources

- [Tau Ceti documentation: `TauCeti.AbelianK0.eulerChar_eq_homologyEulerChar`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/GrothendieckGroup/EulerCharacteristic.html#TauCeti.AbelianK0.eulerChar_eq_homologyEulerChar)
- [Source of `TauCeti.AbelianK0.eulerChar_eq_homologyEulerChar` in TauCeti/CategoryTheory/GrothendieckGroup/EulerCharacteristic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/CategoryTheory/GrothendieckGroup/EulerCharacteristic.lean#L366)
