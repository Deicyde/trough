---
declaration: theorem
origin: cited
lean: Ideal.isRegularLocalRing_localization_of_derivation_notMem
statement: formalized
proof: formalized
---

# The Jacobian criterion for a hypersurface

Let `f ∈ A` and let `P` be a prime of
`A ⧸ (f)` lying over the prime `Q` of `A`, with `A_Q` a regular local ring. If some derivation `D`
of `A` maps `f` outside `Q`, then the localization of `A ⧸ (f)` at `P` is a regular local ring.

```lean
Ideal.isRegularLocalRing_localization_of_derivation_notMem.{u_1, u_2} {R : Type u_1} {A : Type u_2}
  [CommRing R] [CommRing A] [Algebra R A] {f : A} (P : Ideal (A ⧸ Ideal.span {f})) [P.IsPrime]
  [IsRegularLocalRing (Localization.AtPrime (Ideal.comap (Ideal.Quotient.mk (Ideal.span {f})) P))]
  {D : Derivation R A A} (hD : D f ∉ Ideal.comap (Ideal.Quotient.mk (Ideal.span {f})) P) :
  IsRegularLocalRing (Localization.AtPrime P)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Ideal.isRegularLocalRing_localization_of_derivation_notMem`](https://taucetiproject.org/docs/TauCeti/RingTheory/RegularLocalRing/Hypersurface.html#Ideal.isRegularLocalRing_localization_of_derivation_notMem).

## Sources

- [Tau Ceti documentation: `Ideal.isRegularLocalRing_localization_of_derivation_notMem`](https://taucetiproject.org/docs/TauCeti/RingTheory/RegularLocalRing/Hypersurface.html#Ideal.isRegularLocalRing_localization_of_derivation_notMem)
- [Source of `Ideal.isRegularLocalRing_localization_of_derivation_notMem` in TauCeti/RingTheory/RegularLocalRing/Hypersurface.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/RegularLocalRing/Hypersurface.lean#L62)
