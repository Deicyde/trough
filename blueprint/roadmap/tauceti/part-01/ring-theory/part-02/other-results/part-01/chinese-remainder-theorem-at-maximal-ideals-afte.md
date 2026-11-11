---
declaration: theorem
origin: cited
lean: TauCeti.Localization.AtPrime.exists_mk_algebraMap_eq_of_isMaximal
statement: formalized
proof: formalized
---

# Chinese remainder theorem at maximal ideals, after localization

For pairwise distinct maximal ideals `p i`, arbitrary residue classes modulo the indicated
powers of the maximal ideals of `R_{p i}` are simultaneously represented by a single element
of `R`. In a Dedekind domain this applies to the ideals of finitely many distinct height-one
primes.

Allowing exponent zero is harmless: the corresponding quotient is the zero ring, so that
component imposes no condition.

```lean
TauCeti.Localization.AtPrime.exists_mk_algebraMap_eq_of_isMaximal.{u_1, u_2} {R : Type u_1}
  {ι : Type u_2} [CommRing R] [Finite ι] (p : ι → Ideal R) [∀ (i : ι), (p i).IsMaximal]
  (hp : Function.Injective p) (n : ι → ℕ)
  (x :
    (i : ι) →
      Localization.AtPrime (p i) ⧸ IsLocalRing.maximalIdeal (Localization.AtPrime (p i)) ^ n i) :
  ∃ a,
    ∀ (i : ι),
      (Ideal.Quotient.mk (IsLocalRing.maximalIdeal (Localization.AtPrime (p i)) ^ n i))
          ((algebraMap R (Localization.AtPrime (p i))) a) =
        x i
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Localization.AtPrime.exists_mk_algebraMap_eq_of_isMaximal`](https://taucetiproject.org/docs/TauCeti/RingTheory/Localization/ChineseRemainder.html#TauCeti.Localization.AtPrime.exists_mk_algebraMap_eq_of_isMaximal).

## Sources

- [Tau Ceti documentation: `TauCeti.Localization.AtPrime.exists_mk_algebraMap_eq_of_isMaximal`](https://taucetiproject.org/docs/TauCeti/RingTheory/Localization/ChineseRemainder.html#TauCeti.Localization.AtPrime.exists_mk_algebraMap_eq_of_isMaximal)
- [Source of `TauCeti.Localization.AtPrime.exists_mk_algebraMap_eq_of_isMaximal` in TauCeti/RingTheory/Localization/ChineseRemainder.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Localization/ChineseRemainder.lean#L36)
