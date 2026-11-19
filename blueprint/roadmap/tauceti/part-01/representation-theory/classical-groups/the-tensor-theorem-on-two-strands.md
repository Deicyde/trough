---
declaration: theorem
origin: cited
lean: TauCeti.invariants_eq_span_matchingTensor_two
statement: formalized
proof: formalized
---

# The tensor theorem on two strands

Over a field of characteristic zero, the invariants of
the orthogonal group in the fourth tensor power of the standard module are spanned by the three
matching tensors, by Brauer's duality on the tensor square.

```lean
TauCeti.invariants_eq_span_matchingTensor_two.{u} (K : Type u) [Field K] [CharZero K] (n : ℕ) :
  (Representation.piTensorProduct fun x => TauCeti.stdOrthogonalRep K n).invariants =
    Submodule.span K (Set.range fun D => TauCeti.BrauerDiagram.matchingTensor K n D)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Brauer duality on the tensor square](brauer-duality-on-the-tensor-square.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.invariants_eq_span_matchingTensor_two`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/ClassicalGroups/BrauerGenerators/Orthogonal/InvariantTensor.html#TauCeti.invariants_eq_span_matchingTensor_two).

## Sources

- [Tau Ceti documentation: `TauCeti.invariants_eq_span_matchingTensor_two`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/ClassicalGroups/BrauerGenerators/Orthogonal/InvariantTensor.html#TauCeti.invariants_eq_span_matchingTensor_two)
- [Source of `TauCeti.invariants_eq_span_matchingTensor_two` in TauCeti/RepresentationTheory/ClassicalGroups/BrauerGenerators/Orthogonal/InvariantTensor.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RepresentationTheory/ClassicalGroups/BrauerGenerators/Orthogonal/InvariantTensor.lean#L421)
