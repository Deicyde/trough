---
declaration: def
origin: cited
lean: TauCeti.puiseuxField.absoluteGaloisGroupEquivZHat
statement: formalized
---

# The absolute Galois group of `K⸨X⸩` is `ℤ̂`

If `K` is algebraically closed of
characteristic zero and `ζ = (ζₙ)ₙ` is a compatible family of primitive `n`-th roots of unity in
`K`, the absolute Galois group of `K⸨X⸩`, with its Krull topology, is isomorphic as a topological
group to the profinite integers. The canonical generator of `ℤ̂` corresponds to the automorphism
multiplying every `n`-th root of `t` by `ζₙ`
(`TauCeti.puiseuxField.absoluteGaloisGroupEquivZHat_eq_gen_iff`).

```lean
TauCeti.puiseuxField.absoluteGaloisGroupEquivZHat.{u, u_1} (K : Type u_1) [Field K] [IsAlgClosed K]
  [CharZero K] (ζ : TauCeti.PrimeToPTateModule 1 K)
  (hζ :
    ∀ (m : { m // m ≠ 0 ∧ m.Coprime 1 }),
      IsPrimitiveRoot ↑((TauCeti.PrimeToPTateModule.proj m) ζ) ↑m) :
  Field.absoluteGaloisGroup (LaurentSeries K) ≃ₜ* ↑TauCeti.zHat.toProfinite.toTop
```

## Depends on

- [TauCeti.puiseuxField.instIsAlgClosure](tauceti-puiseuxfield-instisalgclosure.md)

## Proof depends on

- [The profinite power](../../../topology/profinite-integers-profinite-powers-and-continuo/the-profinite-power.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.puiseuxField.absoluteGaloisGroupEquivZHat`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/Puiseux/AbsoluteGalois.html#TauCeti.puiseuxField.absoluteGaloisGroupEquivZHat).

## Sources

- [Tau Ceti documentation: `TauCeti.puiseuxField.absoluteGaloisGroupEquivZHat`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/Puiseux/AbsoluteGalois.html#TauCeti.puiseuxField.absoluteGaloisGroupEquivZHat)
- [Source of `TauCeti.puiseuxField.absoluteGaloisGroupEquivZHat` in TauCeti/RingTheory/LaurentSeries/Puiseux/AbsoluteGalois.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/LaurentSeries/Puiseux/AbsoluteGalois.lean#L254)
- [Tau Ceti roadmap status: Formal Laurent fields, Puiseux expansions and continuous differential calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FormalLaurentPuiseux/STATUS.md)
