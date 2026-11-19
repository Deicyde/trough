---
declaration: theorem
origin: cited
lean: TauCeti.TemperleyLieb.IsMarkovTrace.apply_jonesWenzl
statement: formalized
proof: formalized
---

# TauCeti.TemperleyLieb.IsMarkovTrace.apply_jonesWenzl

The quantum-dimension formula for any element of augmentation `1` annihilated on the
left by the generators. One-sided annihilation already characterizes the Jones–Wenzl projection.

```lean
TauCeti.TemperleyLieb.IsMarkovTrace.apply_jonesWenzl.{u_1} {R : Type u_1} [CommRing R] {δ : R}
  {tr : (n : ℕ) → TauCeti.TemperleyLieb R δ n →ₗ[R] R}
  (htr : TauCeti.TemperleyLieb.IsMarkovTrace R δ tr) {n : ℕ}
  (h : ∀ k ∈ Finset.Icc 1 n, IsUnit (TauCeti.qInt R δ k)) (f : TauCeti.TemperleyLieb R δ n)
  (hf : TauCeti.TemperleyLieb.aug f = 1)
  (hfe : ∀ (i : Fin (n - 1)), TauCeti.TemperleyLieb.e δ i * f = 0) :
  (tr n) f = TauCeti.qInt R δ (n + 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.TemperleyLieb.IsMarkovTrace.apply_jonesWenzl`](https://taucetiproject.org/docs/TauCeti/Algebra/TemperleyLieb/QuantumDimension.html#TauCeti.TemperleyLieb.IsMarkovTrace.apply_jonesWenzl).

## Sources

- [Tau Ceti documentation: `TauCeti.TemperleyLieb.IsMarkovTrace.apply_jonesWenzl`](https://taucetiproject.org/docs/TauCeti/Algebra/TemperleyLieb/QuantumDimension.html#TauCeti.TemperleyLieb.IsMarkovTrace.apply_jonesWenzl)
- [Source of `TauCeti.TemperleyLieb.IsMarkovTrace.apply_jonesWenzl` in TauCeti/Algebra/TemperleyLieb/QuantumDimension.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/TemperleyLieb/QuantumDimension.lean#L57)
- [Tau Ceti roadmap status: Temperley–Lieb diagrams, categories, and algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TemperleyLieb/STATUS.md)
