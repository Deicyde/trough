---
declaration: theorem
origin: cited
lean: IsLocalRing.mem_range_algebraMap_of_two_le_depth
statement: formalized
proof: formalized
---

# Algebraic Hartogs principle for fractions

Let `R` be a Noetherian local ring of depth at
least two with total ring of fractions `K`. An element of `K` that lies in the image of `R_p` for
every prime `p` other than the maximal ideal lies in `R`: if for every such `p` some `t ∉ p` has
`t x ∈ R`, then `x ∈ R`.

```lean
IsLocalRing.mem_range_algebraMap_of_two_le_depth.{u, u_1} {R : Type u} [CommRing R] [IsLocalRing R]
  [IsNoetherianRing R] (K : Type u_1) [CommRing K] [Algebra R K] [IsFractionRing R K]
  (hdepth : 2 ≤ IsLocalRing.depth ↧R) {x : K}
  (hx :
    ∀ (p : Ideal R) [p.IsPrime],
      p ≠ IsLocalRing.maximalIdeal R → ∃ t ∉ p, (algebraMap R K) t * x ∈ (algebraMap R K).range) :
  x ∈ (algebraMap R K).range
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`IsLocalRing.mem_range_algebraMap_of_two_le_depth`](https://taucetiproject.org/docs/TauCeti/RingTheory/Depth/Basic.html#IsLocalRing.mem_range_algebraMap_of_two_le_depth).

## Sources

- [Tau Ceti documentation: `IsLocalRing.mem_range_algebraMap_of_two_le_depth`](https://taucetiproject.org/docs/TauCeti/RingTheory/Depth/Basic.html#IsLocalRing.mem_range_algebraMap_of_two_le_depth)
- [Source of `IsLocalRing.mem_range_algebraMap_of_two_le_depth` in TauCeti/RingTheory/Depth/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Depth/Basic.lean#L625)
