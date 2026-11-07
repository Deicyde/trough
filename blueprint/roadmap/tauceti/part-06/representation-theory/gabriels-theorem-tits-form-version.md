---
declaration: theorem
origin: cited
lean: TauCeti.isFiniteRepType_iff_titsForm_posDef
statement: formalized
proof: formalized
---

# Gabriel's theorem, Tits form version

A finite connected quiver has finite
representation type exactly when its Tits form is positive definite.

```lean
TauCeti.isFiniteRepType_iff_titsForm_posDef.{u, v, w} {Q : Type v} [Quiver Q] [Fintype Q]
  [(a b : Q) → Fintype (a ⟶ b)] {k : Type u} [Field k]
  (hconn : (TauCeti.Quiver.underlyingGraph Q).Connected) :
  TauCeti.IsFiniteRepType k Q ↔ (TauCeti.titsForm Q).PosDef
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.isFiniteRepType_iff_titsForm_posDef`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/FiniteRepType/Gabriel.html#TauCeti.isFiniteRepType_iff_titsForm_posDef).

## Sources

- [Tau Ceti documentation: `TauCeti.isFiniteRepType_iff_titsForm_posDef`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/FiniteRepType/Gabriel.html#TauCeti.isFiniteRepType_iff_titsForm_posDef)
- [Source of `TauCeti.isFiniteRepType_iff_titsForm_posDef` in TauCeti/RepresentationTheory/Quiver/FiniteRepType/Gabriel.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Quiver/FiniteRepType/Gabriel.lean#L98)
- [Tau Ceti roadmap status: Representation theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RepresentationTheory/STATUS.md)
