---
declaration: theorem
origin: cited
lean: TauCeti.range_brauerActionOrth_two_eq_centralizer
statement: formalized
proof: formalized
---

# Brauer duality on the tensor square in characteristic zero

Over a field of
characteristic zero, the image of the Brauer algebra `B₂(n)` in the endomorphisms of `(Kⁿ)^{⊗2}`
is the commutant of the diagonal action of the orthogonal group.

```lean
TauCeti.range_brauerActionOrth_two_eq_centralizer.{u_1} (K : Type u_1) [Field K] [CharZero K]
  (n : ℕ) :
  (TauCeti.brauerActionOrth K n 2).range =
    Subalgebra.centralizer K (Set.range ⇑((TauCeti.stdOrthogonalRep K n).tensorPower 2))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Brauer duality on the tensor square](brauer-duality-on-the-tensor-square.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.range_brauerActionOrth_two_eq_centralizer`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/ClassicalGroups/BrauerGenerators/Orthogonal/Commutant.html#TauCeti.range_brauerActionOrth_two_eq_centralizer).

## Sources

- [Tau Ceti documentation: `TauCeti.range_brauerActionOrth_two_eq_centralizer`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/ClassicalGroups/BrauerGenerators/Orthogonal/Commutant.html#TauCeti.range_brauerActionOrth_two_eq_centralizer)
- [Source of `TauCeti.range_brauerActionOrth_two_eq_centralizer` in TauCeti/RepresentationTheory/ClassicalGroups/BrauerGenerators/Orthogonal/Commutant.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/ClassicalGroups/BrauerGenerators/Orthogonal/Commutant.lean#L320)
