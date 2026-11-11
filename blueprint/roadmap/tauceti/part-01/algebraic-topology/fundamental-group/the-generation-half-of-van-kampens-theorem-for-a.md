---
declaration: theorem
origin: cited
lean: TauCeti.vanKampenWideLift_surjective
statement: formalized
proof: formalized
---

# The generation half of van Kampen's theorem for a family

Every loop class is the image
of an element of the indexed free product when all pairwise intersections of the cover members
are path connected.

```lean
TauCeti.vanKampenWideLift_surjective.{u_1, u_2} {X : Type u_1} [TopologicalSpace X] {ι : Type u_2}
  {U : ι → Set X} {x : X} (hU : ∀ (y : X), ∃ i, U i ∈ nhds y) (hxU : ∀ (i : ι), x ∈ U i)
  (hpc : ∀ (i j : ι), IsPathConnected (U i ∩ U j)) :
  Function.Surjective ⇑(TauCeti.vanKampenWideLift U x hxU)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.vanKampenWideLift_surjective`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/FundamentalGroup/VanKampen/Basic.html#TauCeti.vanKampenWideLift_surjective).

## Sources

- [Tau Ceti documentation: `TauCeti.vanKampenWideLift_surjective`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/FundamentalGroup/VanKampen/Basic.html#TauCeti.vanKampenWideLift_surjective)
- [Source of `TauCeti.vanKampenWideLift_surjective` in TauCeti/AlgebraicTopology/FundamentalGroup/VanKampen/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/FundamentalGroup/VanKampen/Basic.lean#L765)
