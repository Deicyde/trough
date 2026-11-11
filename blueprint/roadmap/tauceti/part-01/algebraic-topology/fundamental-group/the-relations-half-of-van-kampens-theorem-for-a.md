---
declaration: theorem
origin: cited
lean: TauCeti.ker_vanKampenWideLift
statement: formalized
proof: formalized
---

# The relations half of van Kampen's theorem for a family

The kernel of the canonical map
from the indexed free product is exactly the normal closure of the common-intersection
relators.

```lean
TauCeti.ker_vanKampenWideLift.{u_1, u_2} {X : Type u_1} [TopologicalSpace X] {x : X} {ι : Type u_2}
  {U : ι → Set X} {C : Set X} {hCU : ∀ (i : ι), C ⊆ U i} {hx : x ∈ C}
  (hU : ∀ (y : X), ∃ i, U i ∈ nhds y) (hUp : ∀ (i : ι), IsPathConnected (U i))
  (hC : IsPathConnected C) (hUC : Pairwise fun i j => U i ∩ U j ⊆ C) :
  (TauCeti.vanKampenWideLift U x ⋯).ker = TauCeti.vanKampenWideRelations C hCU hx
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ker_vanKampenWideLift`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/FundamentalGroup/VanKampen/Presentation/Basic.html#TauCeti.ker_vanKampenWideLift).

## Sources

- [Tau Ceti documentation: `TauCeti.ker_vanKampenWideLift`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/FundamentalGroup/VanKampen/Presentation/Basic.html#TauCeti.ker_vanKampenWideLift)
- [Source of `TauCeti.ker_vanKampenWideLift` in TauCeti/AlgebraicTopology/FundamentalGroup/VanKampen/Presentation/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/FundamentalGroup/VanKampen/Presentation/Basic.lean#L241)
