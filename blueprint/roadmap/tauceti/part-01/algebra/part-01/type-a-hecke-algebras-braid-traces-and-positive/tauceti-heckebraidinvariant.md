---
declaration: def
origin: cited
lean: TauCeti.heckeBraidInvariant
statement: formalized
---

# TauCeti.heckeBraidInvariant

The normalized Hecke invariant on algebraic braid closures, that is, the quotient by
ordinary unframed Markov equivalence. This does not identify that quotient with geometric links.

```lean
TauCeti.heckeBraidInvariant.{u_1} {R : Type u_1} [CommRing R] {q : Rˣ} {z : R}
  {τ : TauCeti.InfiniteTypeAHeckeAlgebra R q →ₗ[R] R}
  (hτ : TauCeti.InfiniteTypeAHeckeAlgebra.IsMarkovTrace z τ) (C : R) (l : Rˣ)
  (hpos : C * ↑l * z = 1) (hneg : C * ↑l⁻¹ * (z - (↑q - ↑q⁻¹)) = 1) : Quot TauCeti.MarkovEquiv → R
```

## Depends on

- [TauCeti.InfiniteTypeAHeckeAlgebra](tauceti-infinitetypeaheckealgebra.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.heckeBraidInvariant`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Hecke/Trace.html#TauCeti.heckeBraidInvariant).

## Sources

- [Tau Ceti documentation: `TauCeti.heckeBraidInvariant`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Hecke/Trace.html#TauCeti.heckeBraidInvariant)
- [Source of `TauCeti.heckeBraidInvariant` in TauCeti/KnotTheory/Hecke/Trace.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/KnotTheory/Hecke/Trace.lean#L205)
- [Tau Ceti roadmap status: Type-A Hecke algebras, braid traces, and positive quotients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TypeAHeckeAlgebras/STATUS.md)
