---
declaration: theorem
origin: cited
lean: TauCeti.exists_bijective_primeEnd_map_unitDiscPrimeEnd_of_isJordanCurve_frontier
statement: formalized
proof: formalized
---

# The prime ends of a Jordan domain are the points of the circle

Let `Ω` be a bounded
domain whose frontier is a Jordan curve. There is a holomorphic bijection `g` of the unit disc onto
`Ω` that is continuous and injective on the closed disc, and the map of prime ends it induces sends
the radial prime ends of the disc at the points of the unit circle bijectively onto the prime ends
of `Ω`.

```lean
TauCeti.exists_bijective_primeEnd_map_unitDiscPrimeEnd_of_isJordanCurve_frontier {Ω : Set ℂ}
  (hΩo : IsOpen Ω) (hΩc : IsConnected Ω) (hΩb : Bornology.IsBounded Ω)
  (hΩJ : TauCeti.IsJordanCurve (frontier Ω)) :
  ∃ g,
    ∃ (hgc : ContinuousOn g (closure (Metric.ball 0 1))) (hgi :
      Set.InjOn g (closure (Metric.ball 0 1))) (hg : g '' Metric.ball 0 1 = Ω),
      DifferentiableOn ℂ g (Metric.ball 0 1) ∧
        Function.Bijective fun ζ => TauCeti.PrimeEnd.map ⋯ ⋯ hgc hgi hg (TauCeti.unitDiscPrimeEnd ζ)
```

## Depends on

- [TauCeti.PrimeEnd](tauceti-primeend.md)

## Proof depends on

- [The Jordan–Brouwer separation theorem](the-jordan-brouwer-separation-theorem.md)
- [The Riemann map of a Jordan domain extends to a homeomorphism of the closures](the-riemann-map-of-a-jordan-domain-extends-to-a.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_bijective_primeEnd_map_unitDiscPrimeEnd_of_isJordanCurve_frontier`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/PrimeEnd/JordanDomain.html#TauCeti.exists_bijective_primeEnd_map_unitDiscPrimeEnd_of_isJordanCurve_frontier).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_bijective_primeEnd_map_unitDiscPrimeEnd_of_isJordanCurve_frontier`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/PrimeEnd/JordanDomain.html#TauCeti.exists_bijective_primeEnd_map_unitDiscPrimeEnd_of_isJordanCurve_frontier)
- [Source of `TauCeti.exists_bijective_primeEnd_map_unitDiscPrimeEnd_of_isJordanCurve_frontier` in TauCeti/Analysis/Complex/Conformal/PrimeEnd/JordanDomain.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Conformal/PrimeEnd/JordanDomain.lean#L45)
- [Tau Ceti roadmap status: Conformal mapping and the geometric theory of holomorphic functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ConformalMapping/STATUS.md)
