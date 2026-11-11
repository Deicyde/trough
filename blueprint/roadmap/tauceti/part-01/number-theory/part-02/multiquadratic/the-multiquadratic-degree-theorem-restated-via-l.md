---
declaration: theorem
origin: cited
lean: TauCeti.Multiquadratic.finrank_adjoin_range_of_linearIndependent
statement: formalized
proof: formalized
---

# The multiquadratic degree theorem, restated via linear independence

If the square classes
of the radicands `d : ι → Kˣ` are `ZMod 2`-linearly independent, then the field generated over `K`
by their square roots `root i` has degree `2^|ι|`. This is `finrank_adjoin_range` consuming the
structural form of square-class independence.

```lean
TauCeti.Multiquadratic.finrank_adjoin_range_of_linearIndependent.{u_1, u_2, u_3} {K : Type u_1}
  [Field K] {L : Type u_2} [Field L] [Algebra K L] {ι : Type u_3} [Finite ι] {d : ι → Kˣ}
  {root : ι → L} (hroot : ∀ (i : ι), root i ^ 2 = (algebraMap K L) ↑(d i)) [NeZero 2]
  (hli : LinearIndependent (ZMod 2) fun i => TauCeti.squareClass (d i)) :
  Module.finrank K ↥(IntermediateField.adjoin K (Set.range root)) = 2 ^ Nat.card ι
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Degree of a multiquadratic field over a finite index](../../part-01/multiquadratic-fields-and-genus-theory/degree-of-a-multiquadratic-field-over-a-finite-i.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Multiquadratic.finrank_adjoin_range_of_linearIndependent`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Multiquadratic/SquareClass/Independence.html#TauCeti.Multiquadratic.finrank_adjoin_range_of_linearIndependent).

## Sources

- [Tau Ceti documentation: `TauCeti.Multiquadratic.finrank_adjoin_range_of_linearIndependent`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Multiquadratic/SquareClass/Independence.html#TauCeti.Multiquadratic.finrank_adjoin_range_of_linearIndependent)
- [Source of `TauCeti.Multiquadratic.finrank_adjoin_range_of_linearIndependent` in TauCeti/NumberTheory/Multiquadratic/SquareClass/Independence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/Multiquadratic/SquareClass/Independence.lean#L38)
