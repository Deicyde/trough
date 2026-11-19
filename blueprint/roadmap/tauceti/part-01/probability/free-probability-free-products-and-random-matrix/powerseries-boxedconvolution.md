---
declaration: def
origin: cited
lean: PowerSeries.boxedConvolution
statement: formalized
---

# PowerSeries.boxedConvolution

The *boxed convolution* of the power series `f` and `g`: its coefficient of index `n ≥ 1` is
`∑_{π ∈ NC(n)} (∏_{B ∈ π} f_{|B|}) (∏_{B ∈ K(π)} g_{|B|})`, with `K(π)` the Kreweras complement
of `π`, and its constant coefficient is `f₀ g₀`.

```lean
PowerSeries.boxedConvolution.{u_1} {R : Type u_1} [CommSemiring R] (f g : PowerSeries R) :
  PowerSeries R
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`PowerSeries.boxedConvolution`](https://taucetiproject.org/docs/TauCeti/Combinatorics/NoncrossingPartition/BoxedConvolution.html#PowerSeries.boxedConvolution).

## Sources

- [Tau Ceti documentation: `PowerSeries.boxedConvolution`](https://taucetiproject.org/docs/TauCeti/Combinatorics/NoncrossingPartition/BoxedConvolution.html#PowerSeries.boxedConvolution)
- [Source of `PowerSeries.boxedConvolution` in TauCeti/Combinatorics/NoncrossingPartition/BoxedConvolution.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Combinatorics/NoncrossingPartition/BoxedConvolution.lean#L77)
- [Tau Ceti roadmap status: Free probability, free products, and random matrix models](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FreeProbability/STATUS.md)
