---
declaration: theorem
origin: cited
lean: TauCeti.PLPath.isSome_raiseIter_iff_of_eq_natCast
statement: formalized
proof: formalized
---

# The string-length identity `ε_α = -min H`

when `-min H` is a natural number `ε`, the
raising string through the path has length exactly `ε`.

```lean
TauCeti.PLPath.isSome_raiseIter_iff_of_eq_natCast.{u_1, u_2} {𝕜 : Type u_1} {V : Type u_2} [Field 𝕜]
  [LinearOrder 𝕜] [IsStrictOrderedRing 𝕜] [AddCommGroup V] [_root_.Module 𝕜 V] {f : Module.Dual 𝕜 V}
  {x : V} {p : TauCeti.PLPath 𝕜 V} (hx : f x = 2) {ε : ℕ} (hε : -TauCeti.PLPath.minHeight f p = ↑ε)
  (n : ℕ) : (TauCeti.PLPath.raiseIter f x n p).isSome = true ↔ n ≤ ε
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.PLPath.isSome_raiseIter_iff_of_eq_natCast`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/LSPath/StringLength.html#TauCeti.PLPath.isSome_raiseIter_iff_of_eq_natCast).

## Sources

- [Tau Ceti documentation: `TauCeti.PLPath.isSome_raiseIter_iff_of_eq_natCast`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/LSPath/StringLength.html#TauCeti.PLPath.isSome_raiseIter_iff_of_eq_natCast)
- [Source of `TauCeti.PLPath.isSome_raiseIter_iff_of_eq_natCast` in TauCeti/RepresentationTheory/LSPath/StringLength.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RepresentationTheory/LSPath/StringLength.lean#L226)
- [Tau Ceti roadmap status: Schubert geometry, Demazure sections and flag K-theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SchubertGeometry/STATUS.md)
