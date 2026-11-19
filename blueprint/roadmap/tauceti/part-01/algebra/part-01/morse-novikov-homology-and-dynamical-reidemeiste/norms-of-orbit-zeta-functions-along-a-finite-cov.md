---
declaration: theorem
origin: cited
lean: TauCeti.NovikovSeries.algebraNorm_orbitZeta
statement: formalized
proof: formalized
---

# Norms of orbit zeta functions along a finite cover

Let `K` be a finite-index subgroup of
`H`, and for each orbit class `γ i` let `d i` be the order of its image in `H ⧸ K`. The norm of
the orbit zeta function over `Nov(R, K, N|K)` is the orbit zeta function of the family that lists
`[H : K] / d i` copies of the class `d i • γ i ∈ K`, whose `n`-th iterates carry the signs
`ε i (d i * n)`. Geometrically, these are the primitive lifts of the `i`-th orbit to the covering
with deck group `H ⧸ K`, the `n`-th iterate of a lift being the `(d i * n)`-th iterate of the
orbit.

```lean
TauCeti.NovikovSeries.algebraNorm_orbitZeta.{u_1, u_2, u_3} {ι : Type u_1} {H : Type u_2}
  {R : Type u_3} [AddCommGroup H] {N : H →+ ℝ} {γ : ι → H} [CommRing R] [Algebra ℚ R]
  (K : AddSubgroup H) [K.FiniteIndex] (hpos : ∀ (i : ι), 0 < N (γ i))
  (hfin : Filter.Tendsto (fun i => N (γ i)) Filter.cofinite Filter.atTop) (ε : ι → ℕ → ℤ) :
  (Algebra.norm (TauCeti.NovikovSeries R (↥K) (N.comp K.subtype)))
      (TauCeti.NovikovSeries.orbitZeta R N γ ε) =
    TauCeti.NovikovSeries.orbitZeta R (N.comp K.subtype) (fun p => K.liftClass (γ p.fst)) fun p n =>
      ε p.fst (addOrderOf ↑(γ p.fst) * n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Jacobi's formula](../../../ring-theory/part-02/other-results/part-01/jacobis-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NovikovSeries.algebraNorm_orbitZeta`](https://taucetiproject.org/docs/TauCeti/RingTheory/NovikovSeries/OrbitZeta/Norm.html#TauCeti.NovikovSeries.algebraNorm_orbitZeta).

## Sources

- [Tau Ceti documentation: `TauCeti.NovikovSeries.algebraNorm_orbitZeta`](https://taucetiproject.org/docs/TauCeti/RingTheory/NovikovSeries/OrbitZeta/Norm.html#TauCeti.NovikovSeries.algebraNorm_orbitZeta)
- [Source of `TauCeti.NovikovSeries.algebraNorm_orbitZeta` in TauCeti/RingTheory/NovikovSeries/OrbitZeta/Norm.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/NovikovSeries/OrbitZeta/Norm.lean#L119)
- [Tau Ceti roadmap status: Morse–Novikov homology and dynamical Reidemeister torsion](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/MorseNovikov/STATUS.md)
