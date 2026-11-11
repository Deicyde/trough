---
declaration: theorem
origin: cited
lean: TauCeti.weylCoxeterHom_injective
statement: formalized
proof: formalized
---

# Tits' theorem: the braid relations are the only relations among the simple reflections

The canonical homomorphism from the Coxeter group of a base to the Weyl group is injective.

```lean
TauCeti.weylCoxeterHom_injective.{u, v, w, x} {ι : Type u} {R : Type v} {M : Type w} {N : Type x}
  [CommRing R] [AddCommGroup M] [_root_.Module R M] [AddCommGroup N] [_root_.Module R N]
  (P : RootPairing ι R M N) [Finite ι] [CharZero R] [IsDomain R] [P.IsCrystallographic] (b : P.Base)
  [P.IsReduced] : Function.Injective ⇑(TauCeti.weylCoxeterHom P b)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.weylCoxeterHom_injective`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/Coxeter/Presentation.html#TauCeti.weylCoxeterHom_injective).

## Sources

- [Tau Ceti documentation: `TauCeti.weylCoxeterHom_injective`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/Coxeter/Presentation.html#TauCeti.weylCoxeterHom_injective)
- [Source of `TauCeti.weylCoxeterHom_injective` in TauCeti/LinearAlgebra/RootSystem/Coxeter/Presentation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/RootSystem/Coxeter/Presentation.lean#L156)
