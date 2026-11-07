---
declaration: def
origin: cited
lean: TauCeti.signedCheckedRep
statement: formalized
---

# TauCeti.signedCheckedRep

The signed checked representation of the braid group on the word space `(Fin n → ι) →₀ R`:
the elementary braid `σ i` acts by the signed checked R-matrix on the strands `i` and `i + 1`.

```lean
TauCeti.signedCheckedRep.{u_1, u_2} {R : Type u_1} [CommRing R] {ι : Type u_2} [LinearOrder ι]
  (pos : ι → Prop) [DecidablePred pos] {n : ℕ} (s : Rˣ) :
  TauCeti.BraidGroup n →* (Module.End R ((Fin n → ι) →₀ R))ˣ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.signedCheckedR\_braid](tauceti-signedcheckedr-braid.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.signedCheckedRep`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/SignedCheckedR.html#TauCeti.signedCheckedRep).

## Sources

- [Tau Ceti documentation: `TauCeti.signedCheckedRep`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/SignedCheckedR.html#TauCeti.signedCheckedRep)
- [Source of `TauCeti.signedCheckedRep` in TauCeti/Algebra/TypeAHeckeAlgebra/SignedCheckedR.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/TypeAHeckeAlgebra/SignedCheckedR.lean#L353)
- [Tau Ceti roadmap status: Type-A Hecke algebras, braid traces, and positive quotients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/TypeAHeckeAlgebras/STATUS.md)
