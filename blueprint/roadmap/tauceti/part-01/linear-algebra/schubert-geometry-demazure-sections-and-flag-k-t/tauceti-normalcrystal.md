---
declaration: structure
origin: cited
lean: TauCeti.NormalCrystal
statement: formalized
---

# TauCeti.NormalCrystal

A **normal crystal** over the root datum `P` with base `b`: a weight map, partial raising and
lowering operators `e i`, `f i` indexed by the simple roots, and natural string lengths `ε i`,
`φ i`, satisfying Kashiwara's crystal axioms together with normality (`ε i x` and `φ i x` are the
lengths of the `e i`- and `f i`-strings through `x`). The value `none` of `e i` or `f i` stands
for Kashiwara's `0`.

```lean
TauCeti.NormalCrystal.{u, v, w, x₁} {ι : Type u} {X : Type v} {Y : Type w} [AddCommGroup X]
  [AddCommGroup Y] (P : RootDatum ι X Y) (b : RootPairing.Base P) (B : Type x₁) :
  Type (max (max u v) x₁)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.NormalCrystal`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Crystal/Basic.html#TauCeti.NormalCrystal).

## Sources

- [Tau Ceti documentation: `TauCeti.NormalCrystal`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Crystal/Basic.html#TauCeti.NormalCrystal)
- [Source of `TauCeti.NormalCrystal` in TauCeti/RepresentationTheory/Crystal/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Crystal/Basic.lean#L82)
- [Tau Ceti roadmap status: Schubert geometry, Demazure sections and flag K-theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SchubertGeometry/STATUS.md)
