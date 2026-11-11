---
declaration: def
origin: cited
lean: TauCeti.Henselization.integralBaseChangeEquiv
statement: formalized
---

# TauCeti.Henselization.integralBaseChangeEquiv

Henselization commutes with integral base change. The scalar structure on the
tensor product is through its `S` factor.

```lean
TauCeti.Henselization.integralBaseChangeEquiv.{u, v} {R : Type u} [CommRing R] (I : Ideal R)
  (S : Type v) [CommRing S] [Algebra R S] [Algebra.IsIntegral R S] :
  TensorProduct R (↑(TauCeti.Henselization.algebra I)) S ≃ₐ[S]
    ↑(TauCeti.Henselization.algebra (Ideal.map (algebraMap R S) I))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cayley–Hamilton in size two](../../linear-algebra/matrix/cayley-hamilton-in-size-two.md)
- [Nakayama's lemma for an idempotent](../../ring-theory/part-02/other-results/part-02/nakayamas-lemma-for-an-idempotent.md)
- [Zariski's main theorem, global form](../../ring-theory/part-02/other-results/part-03/zariskis-main-theorem-global-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Henselization.integralBaseChangeEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/Henselization/Integral.html#TauCeti.Henselization.integralBaseChangeEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.Henselization.integralBaseChangeEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/Henselization/Integral.html#TauCeti.Henselization.integralBaseChangeEquiv)
- [Source of `TauCeti.Henselization.integralBaseChangeEquiv` in TauCeti/RingTheory/Henselization/Integral.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Henselization/Integral.lean#L103)
- [Tau Ceti roadmap status: Scheme, stack, cohomology and intersection foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SchemeAndStackFoundations/STATUS.md)
