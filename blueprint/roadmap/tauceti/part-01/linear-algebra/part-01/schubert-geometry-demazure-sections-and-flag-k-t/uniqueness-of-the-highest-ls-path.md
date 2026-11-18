---
declaration: theorem
origin: cited
lean: TauCeti.LSPath.forall_raise_eq_none_iff
statement: formalized
proof: formalized
---

# Uniqueness of the highest LS path

For a dominant shape, all actual simple-root raising
operators vanish exactly on the straight path. No operator-stability assumption is needed.

```lean
TauCeti.LSPath.forall_raise_eq_none_iff.{u_1, u_2, u_3, u_4, u_5} {ι : Type u_1} {M : Type u_2}
  {N : Type u_3} [AddCommGroup M] [AddCommGroup N] {P : RootPairing ι ℤ M N} {b : P.Base} [Finite ι]
  [P.IsReduced] {lam : M} {𝕜 : Type u_4} {V : Type u_5} [Field 𝕜] [LinearOrder 𝕜]
  [IsStrictOrderedRing 𝕜] [AddCommGroup V] [_root_.Module 𝕜 V] [P.flip.IsReduced]
  (π : TauCeti.LSPath P b lam) (hlam : lam ∈ P.dominantChamber b) (f : M →+ V)
  (F : ↥b.support → Module.Dual 𝕜 V)
  (hF : ∀ (i : ↥b.support) (m : M), (F i) (f m) = ↑((P.coroot' ↑i) m)) :
  (∀ (i : ↥b.support),
      TauCeti.PLPath.raise (F i) (f (P.root ↑i)) (TauCeti.LSPath.toPLPath 𝕜 f π) = none) ↔
    π = TauCeti.LSPath.straight lam
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.LSPath.forall_raise_eq_none_iff`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/LSPath/Highest.html#TauCeti.LSPath.forall_raise_eq_none_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.LSPath.forall_raise_eq_none_iff`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/LSPath/Highest.html#TauCeti.LSPath.forall_raise_eq_none_iff)
- [Source of `TauCeti.LSPath.forall_raise_eq_none_iff` in TauCeti/RepresentationTheory/LSPath/Highest.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RepresentationTheory/LSPath/Highest.lean#L71)
- [Tau Ceti roadmap status: Schubert geometry, Demazure sections and flag K-theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SchubertGeometry/STATUS.md)
