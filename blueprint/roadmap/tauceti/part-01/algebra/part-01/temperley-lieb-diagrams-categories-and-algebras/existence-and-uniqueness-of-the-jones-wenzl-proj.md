---
declaration: theorem
origin: cited
lean: TauCeti.TemperleyLieb.existsUnique_jonesWenzl
statement: formalized
proof: formalized
---

# Existence and uniqueness of the Jones–Wenzl projection

When `[1], …, [n]` are units,
exactly one element of the Temperley–Lieb algebra on `n` strands is idempotent, has augmentation
`1`, and is killed on both sides by every generator; it is `TauCeti.TemperleyLieb.jonesWenzl`.

```lean
TauCeti.TemperleyLieb.existsUnique_jonesWenzl.{u_1} {R : Type u_1} [CommRing R] {δ : R} {n : ℕ}
  (h : ∀ k ∈ Finset.Icc 1 n, IsUnit (TauCeti.qInt R δ k)) :
  ∃! f,
    IsIdempotentElem f ∧
      TauCeti.TemperleyLieb.aug f = 1 ∧
        ∀ (i : Fin (n - 1)),
          TauCeti.TemperleyLieb.e δ i * f = 0 ∧ f * TauCeti.TemperleyLieb.e δ i = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.TemperleyLieb.existsUnique_jonesWenzl`](https://taucetiproject.org/docs/TauCeti/Algebra/TemperleyLieb/JonesWenzl.html#TauCeti.TemperleyLieb.existsUnique_jonesWenzl).

## Sources

- [Tau Ceti documentation: `TauCeti.TemperleyLieb.existsUnique_jonesWenzl`](https://taucetiproject.org/docs/TauCeti/Algebra/TemperleyLieb/JonesWenzl.html#TauCeti.TemperleyLieb.existsUnique_jonesWenzl)
- [Source of `TauCeti.TemperleyLieb.existsUnique_jonesWenzl` in TauCeti/Algebra/TemperleyLieb/JonesWenzl.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/TemperleyLieb/JonesWenzl.lean#L388)
- [Tau Ceti roadmap status: Temperley–Lieb diagrams, categories, and algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TemperleyLieb/STATUS.md)
