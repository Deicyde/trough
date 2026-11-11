---
declaration: theorem
origin: cited
lean: TauCeti.Iwasawa.exists_isPseudoIsomorphism_pi_quotient_pow
statement: formalized
proof: formalized
---

# The structure theorem for torsion modules

Over a noetherian integrally closed domain `A`, a
finitely generated torsion module `M` admits a pseudo-isomorphism `M → ∏ᵢ A ⧸ 𝔭ᵢ ^ nᵢ` onto a
finite product, with each `𝔭ᵢ` a prime of height one and each `nᵢ` positive.
Neukirch–Schmidt–Wingberg, (5.1.10).

```lean
TauCeti.Iwasawa.exists_isPseudoIsomorphism_pi_quotient_pow.{u, v} {A : Type u} [CommRing A]
  {M : Type v} [AddCommGroup M] [_root_.Module A M] [IsDomain A] [IsNoetherianRing A]
  [IsIntegrallyClosed A] [Module.Finite A M] (hM : Module.IsTorsion A M) :
  ∃ ι x 𝔭 n,
    (∀ (i : ι), (𝔭 i).asIdeal.height = 1 ∧ n i ≠ 0) ∧ ∃ f, TauCeti.Iwasawa.IsPseudoIsomorphism f
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Iwasawa.exists_isPseudoIsomorphism_pi_quotient_pow`](https://taucetiproject.org/docs/TauCeti/RingTheory/Iwasawa/StructureTheorem.html#TauCeti.Iwasawa.exists_isPseudoIsomorphism_pi_quotient_pow).

## Sources

- [Tau Ceti documentation: `TauCeti.Iwasawa.exists_isPseudoIsomorphism_pi_quotient_pow`](https://taucetiproject.org/docs/TauCeti/RingTheory/Iwasawa/StructureTheorem.html#TauCeti.Iwasawa.exists_isPseudoIsomorphism_pi_quotient_pow)
- [Source of `TauCeti.Iwasawa.exists_isPseudoIsomorphism_pi_quotient_pow` in TauCeti/RingTheory/Iwasawa/StructureTheorem.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Iwasawa/StructureTheorem.lean#L104)
