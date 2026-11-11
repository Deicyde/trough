---
declaration: theorem
origin: cited
lean: TauCeti.PLPath.lower_eq_some_iff
statement: formalized
proof: formalized
---

# TauCeti.PLPath.lower_eq_some_iff

Littelmann's root operators are partial inverses: lowering `p` gives `q` exactly when raising
`q` gives `p`.

```lean
TauCeti.PLPath.lower_eq_some_iff.{u_1, u_2} {𝕜 : Type u_1} {V : Type u_2} [Field 𝕜] [LinearOrder 𝕜]
  [IsStrictOrderedRing 𝕜] [AddCommGroup V] [_root_.Module 𝕜 V] {f : Module.Dual 𝕜 V} {x : V}
  (hx : f x = 2) {p q : TauCeti.PLPath 𝕜 V} :
  TauCeti.PLPath.lower f x p = some q ↔ TauCeti.PLPath.raise f x q = some p
```

## Depends on

- [TauCeti.PLPath.lower](tauceti-plpath-lower.md)
- [TauCeti.PLPath.raise](tauceti-plpath-raise.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PLPath.lower_eq_some_iff`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/LSPath/PartialInverse.html#TauCeti.PLPath.lower_eq_some_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.PLPath.lower_eq_some_iff`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/LSPath/PartialInverse.html#TauCeti.PLPath.lower_eq_some_iff)
- [Source of `TauCeti.PLPath.lower_eq_some_iff` in TauCeti/RepresentationTheory/LSPath/PartialInverse.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/LSPath/PartialInverse.lean#L263)
- [Tau Ceti roadmap status: Schubert geometry, Demazure sections and flag K-theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SchubertGeometry/STATUS.md)
