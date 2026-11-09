---
declaration: def
origin: cited
lean: TauCeti.PLPath.raise
statement: formalized
---

# TauCeti.PLPath.raise

Littelmann's raising operator `e_α` on paths, the conjugate of `TauCeti.PLPath.lower` by the
reversal of paths. Let `h` be the minimal height, `t₁` the first time at which the height equals
`h` and `t₀` the last time up to which the height is at least `h + 1`. Between `t₀` and `t₁`, the
pieces along which the height decreases and stays at most every earlier height are reflected by
`Module.preReflection x f`, the equal-height excursions are kept, and the rest of the path after
`t₁` is translated by `x`. It is `none` when `-1 < h`.

```lean
TauCeti.PLPath.raise.{u_1, u_2} {𝕜 : Type u_1} {V : Type u_2} [Field 𝕜] [LinearOrder 𝕜]
  [IsStrictOrderedRing 𝕜] [AddCommGroup V] [_root_.Module 𝕜 V] (f : Module.Dual 𝕜 V) (x : V)
  (p : TauCeti.PLPath 𝕜 V) : Option (TauCeti.PLPath 𝕜 V)
```

## Depends on

- [TauCeti.PLPath.lower](tauceti-plpath-lower.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PLPath.raise`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/LSPath/RootOperator.html#TauCeti.PLPath.raise).

## Sources

- [Tau Ceti documentation: `TauCeti.PLPath.raise`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/LSPath/RootOperator.html#TauCeti.PLPath.raise)
- [Source of `TauCeti.PLPath.raise` in TauCeti/RepresentationTheory/LSPath/RootOperator.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/LSPath/RootOperator.lean#L747)
- [Tau Ceti roadmap status: Schubert geometry, Demazure sections and flag K-theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SchubertGeometry/STATUS.md)
