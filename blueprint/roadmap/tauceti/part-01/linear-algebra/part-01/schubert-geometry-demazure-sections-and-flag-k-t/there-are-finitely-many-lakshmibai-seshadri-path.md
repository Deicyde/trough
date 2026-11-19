---
declaration: theorem
origin: cited
lean: TauCeti.LSPath.finite
statement: formalized
proof: formalized
---

# There are finitely many Lakshmibai–Seshadri paths of a dominant shape `λ`

The
directions strictly decrease in the finite parabolic quotient `W / W_λ`, and the times are
rationals in `[0, 1]` whose denominators are bounded by the bonds `b_λ(x, y)`.

```lean
TauCeti.LSPath.finite.{u, w, x} {ι : Type u} {M : Type w} {N : Type x} [AddCommGroup M]
  [AddCommGroup N] {P : RootPairing ι ℤ M N} {b : P.Base} [Finite ι] [P.IsReduced] {lam : M}
  (hlam : lam ∈ P.dominantChamber b) : Finite (TauCeti.LSPath P b lam)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.LSPath.finite`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/LSPath/Basic.html#TauCeti.LSPath.finite).

## Sources

- [Tau Ceti documentation: `TauCeti.LSPath.finite`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/LSPath/Basic.html#TauCeti.LSPath.finite)
- [Source of `TauCeti.LSPath.finite` in TauCeti/RepresentationTheory/LSPath/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RepresentationTheory/LSPath/Basic.lean#L385)
- [Tau Ceti roadmap status: Schubert geometry, Demazure sections and flag K-theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SchubertGeometry/STATUS.md)
