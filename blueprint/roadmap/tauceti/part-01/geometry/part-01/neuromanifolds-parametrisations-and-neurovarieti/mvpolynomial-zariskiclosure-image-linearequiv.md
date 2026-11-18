---
declaration: theorem
origin: cited
lean: MvPolynomial.zariskiClosure_image_linearEquiv
statement: formalized
proof: formalized
---

# MvPolynomial.zariskiClosure_image_linearEquiv

An invertible `K`-linear change of finitely many coordinates commutes with the Zariski
closure.

```lean
MvPolynomial.zariskiClosure_image_linearEquiv.{u_2, u_3, u_4} {K : Type u_2} {σ : Type u_3}
  {τ : Type u_4} [Field K] [Finite σ] (e : (σ → K) ≃ₗ[K] τ → K) (S : Set (σ → K)) :
  (MvPolynomial.zariskiClosure K) (⇑e '' S) = ⇑e '' (MvPolynomial.zariskiClosure K) S
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MvPolynomial.zariskiClosure_image_linearEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/ZariskiClosure.html#MvPolynomial.zariskiClosure_image_linearEquiv).

## Sources

- [Tau Ceti documentation: `MvPolynomial.zariskiClosure_image_linearEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/ZariskiClosure.html#MvPolynomial.zariskiClosure_image_linearEquiv)
- [Source of `MvPolynomial.zariskiClosure_image_linearEquiv` in TauCeti/RingTheory/MvPolynomial/ZariskiClosure.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/MvPolynomial/ZariskiClosure.lean#L212)
- [Tau Ceti roadmap status: Neuromanifolds, parametrisations, and neurovarieties](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Neuromanifolds/STATUS.md)
