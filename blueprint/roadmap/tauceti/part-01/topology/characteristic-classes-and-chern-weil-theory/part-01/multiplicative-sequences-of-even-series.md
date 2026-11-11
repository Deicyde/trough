---
declaration: theorem
origin: cited
lean: PowerSeries.expand_mk_aeval_multiplicativeSequence
statement: formalized
proof: formalized
---

# Multiplicative sequences of even series

for a multiset `s` of `n` roots,
`∏_{x ∈ s} Q(x² t²)` is obtained from `∑ₖ Kₖ(e₁(s²), …, eₙ(s²)) tᵏ`, where `Kₖ` is the
multiplicative sequence of `Q` and `s²` is the multiset of squares of the roots, by substituting
`t²` for `t`. An even characteristic series is of the form `Q(t²)`; for the `L` and `Â` classes the
roots are one degree-two root per oriented real 2-plane, and the `eᵢ(s²)` are the Pontryagin
classes.

```lean
PowerSeries.expand_mk_aeval_multiplicativeSequence.{u_1, u_2} {R : Type u_1} [CommRing R]
  (Q : PowerSeries R) (n : ℕ) {S : Type u_2} [CommRing S] [Algebra R S] (s : Multiset S)
  (hs : s.card = n) :
  (PowerSeries.expand 2 ⋯)
      (PowerSeries.mk fun k =>
        (MvPolynomial.aeval fun j => (Multiset.map (fun x => x ^ 2) s).esymm (↑j + 1))
          (Q.multiplicativeSequence n k)) =
    (Multiset.map
        (fun x =>
          (PowerSeries.rescale x) ((PowerSeries.map (algebraMap R S)) ((PowerSeries.expand 2 ⋯) Q)))
        s).prod
```

## Depends on

- [PowerSeries.multiplicativeSequence](powerseries-multiplicativesequence.md)

## Lean

Formalized in Tau Ceti as [`PowerSeries.expand_mk_aeval_multiplicativeSequence`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/MultiplicativeSequence.html#PowerSeries.expand_mk_aeval_multiplicativeSequence).

## Sources

- [Tau Ceti documentation: `PowerSeries.expand_mk_aeval_multiplicativeSequence`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/MultiplicativeSequence.html#PowerSeries.expand_mk_aeval_multiplicativeSequence)
- [Source of `PowerSeries.expand_mk_aeval_multiplicativeSequence` in TauCeti/RingTheory/PowerSeries/MultiplicativeSequence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/PowerSeries/MultiplicativeSequence.lean#L278)
- [Tau Ceti roadmap status: Characteristic classes and Chern–Weil theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CharacteristicClasses/STATUS.md)
