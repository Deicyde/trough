---
declaration: theorem
origin: cited
lean: TauCeti.AbelianK0.eulerChar_eq_of_quasiIso
statement: formalized
proof: formalized
---

# The Euler characteristic is a quasi-isomorphism invariant

Two bounded complexes joined by
a quasi-isomorphism have the same alternating class of terms, over any finite range of degrees
containing both supports; this is what makes the Euler characteristic a function of the image of
the complex in the derived category.

```lean
TauCeti.AbelianK0.eulerChar_eq_of_quasiIso.{w, v, u} {A : Type u} [CategoryTheory.Category.{v, u} A]
  [CategoryTheory.Abelian A] [CategoryTheory.EssentiallySmall.{w, v, u} A]
  {K L : CochainComplex A ℤ} (f : K ⟶ L) [QuasiIso f] (aK bK aL bL : ℤ) [K.IsStrictlyGE aK]
  [K.IsStrictlyLE bK] [L.IsStrictlyGE aL] [L.IsStrictlyLE bL] {s : Finset ℤ}
  (hK : Finset.Icc aK bK ⊆ s) (hL : Finset.Icc aL bL ⊆ s) :
  TauCeti.AbelianK0.eulerChar K s = TauCeti.AbelianK0.eulerChar L s
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Euler–Poincaré theorem in abelian `K₀`](the-euler-poincare-theorem-in-abelian-k0.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AbelianK0.eulerChar_eq_of_quasiIso`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/GrothendieckGroup/EulerCharacteristic.html#TauCeti.AbelianK0.eulerChar_eq_of_quasiIso).

## Sources

- [Tau Ceti documentation: `TauCeti.AbelianK0.eulerChar_eq_of_quasiIso`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/GrothendieckGroup/EulerCharacteristic.html#TauCeti.AbelianK0.eulerChar_eq_of_quasiIso)
- [Source of `TauCeti.AbelianK0.eulerChar_eq_of_quasiIso` in TauCeti/CategoryTheory/GrothendieckGroup/EulerCharacteristic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/CategoryTheory/GrothendieckGroup/EulerCharacteristic.lean#L399)
