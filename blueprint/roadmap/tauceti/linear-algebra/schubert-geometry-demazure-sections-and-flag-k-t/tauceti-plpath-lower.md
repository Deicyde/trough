---
declaration: def
origin: cited
lean: TauCeti.PLPath.lower
statement: formalized
---

# TauCeti.PLPath.lower

Littelmann's lowering operator `f_α` on paths, for the root `α = x` and the coroot pairing
`f = ⟨-, α^∨⟩`. Let `h` be the minimal height, `t₀` the last time at which the height equals `h`
and `t₁` the first time from which on the height is at least `h + 1`. Between `t₀` and `t₁`, the
pieces along which the height increases and stays at most every later height are reflected by
`Module.preReflection x f`, the equal-height excursions are kept, and the rest of the path after
`t₁` is translated by `-x`. It is `none` when `f (π 1) - h < 1`.

```lean
TauCeti.PLPath.lower.{u_1, u_2} {𝕜 : Type u_1} {V : Type u_2} [Field 𝕜] [LinearOrder 𝕜]
  [IsStrictOrderedRing 𝕜] [AddCommGroup V] [_root_.Module 𝕜 V] (f : Module.Dual 𝕜 V) (x : V)
  (p : TauCeti.PLPath 𝕜 V) : Option (TauCeti.PLPath 𝕜 V)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.PLPath.lower`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/LSPath/RootOperator.html#TauCeti.PLPath.lower).

## Sources

- [Tau Ceti documentation: `TauCeti.PLPath.lower`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/LSPath/RootOperator.html#TauCeti.PLPath.lower)
- [Source of `TauCeti.PLPath.lower` in TauCeti/RepresentationTheory/LSPath/RootOperator.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/LSPath/RootOperator.lean#L738)
- [Tau Ceti roadmap status: Schubert geometry, Demazure sections and flag K-theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SchubertGeometry/STATUS.md)
