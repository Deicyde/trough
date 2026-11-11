---
declaration: theorem
origin: cited
lean: LinearMap.ker_le_range_of_mapRange_constantCoeff
statement: formalized
proof: formalized
---

# Graded Nakayama lemma for free complexes over a polynomial ring

Let `d` be a square-zero
endomorphism of the free module `ι →₀ R[V_v : v ∈ σ]` which is homogeneous of degree `r` when the
generator `i` has degree `g i` and the variable `V_v` has negative degree `w v`, with the degrees
`g i` bounded above. If the reduction `d₀` of `d` modulo the variables, the endomorphism of
`ι →₀ R` with `d₀ ∘ ρ = ρ ∘ d` for `ρ` the coordinatewise constant coefficient, is exact, then so
is `d`.

```lean
LinearMap.ker_le_range_of_mapRange_constantCoeff.{u_1, u_2, u_3} {R : Type u_1} {σ : Type u_2}
  {ι : Type u_3} [CommRing R] {d₀ : (ι →₀ R) →ₗ[R] ι →₀ R} {w : σ → ℤ} {g : ι → ℤ} {r : ℤ}
  (d : (ι →₀ MvPolynomial σ R) →ₗ[MvPolynomial σ R] ι →₀ MvPolynomial σ R) (hw : ∀ (v : σ), w v < 0)
  (hhom : ∀ (i j : ι), MvPolynomial.IsWeightedHomogeneous w ((d fun₀ | i => 1) j) (g i + r - g j))
  (hd₀ :
    ∀ (x : ι →₀ MvPolynomial σ R),
      d₀ (Finsupp.mapRange ⇑MvPolynomial.constantCoeff ⋯ x) =
        Finsupp.mapRange ⇑MvPolynomial.constantCoeff ⋯ (d x))
  (hg : BddAbove (Set.range g)) (hd : d ∘ₗ d = 0) (hexact : d₀.ker ≤ d₀.range) : d.ker ≤ d.range
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LinearMap.ker_le_range_of_mapRange_constantCoeff`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/ReductionModVariables.html#LinearMap.ker_le_range_of_mapRange_constantCoeff).

## Sources

- [Tau Ceti documentation: `LinearMap.ker_le_range_of_mapRange_constantCoeff`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/ReductionModVariables.html#LinearMap.ker_le_range_of_mapRange_constantCoeff)
- [Source of `LinearMap.ker_le_range_of_mapRange_constantCoeff` in TauCeti/Algebra/Homology/ReductionModVariables.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Homology/ReductionModVariables.lean#L204)
