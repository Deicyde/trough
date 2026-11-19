---
declaration: theorem
origin: cited
lean: TauCeti.Multiquadratic.finrank_adjoin_range
statement: formalized
proof: formalized
---

# Degree of a multiquadratic field over a finite index

If no nonempty subset product of
the radicands `d i` is a square in `K`, then `[K(rootᵢ : i) : K] = 2^|ι|`.

```lean
TauCeti.Multiquadratic.finrank_adjoin_range.{u_1, u_2, u_3} {K : Type u_1} {L : Type u_2} [Field K]
  [Field L] [Algebra K L] {ι : Type u_3} [Finite ι] {d : ι → K} {root : ι → L}
  (hroot : ∀ (i : ι), root i ^ 2 = (algebraMap K L) (d i)) [NeZero 2]
  (hindep : ∀ (S : Finset ι), S.Nonempty → ¬IsSquare (∏ i ∈ S, d i)) :
  Module.finrank K ↥(IntermediateField.adjoin K (Set.range root)) = 2 ^ Nat.card ι
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Multiquadratic.finrank_adjoin_range`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Multiquadratic/Degree.html#TauCeti.Multiquadratic.finrank_adjoin_range).

## Sources

- [Tau Ceti documentation: `TauCeti.Multiquadratic.finrank_adjoin_range`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Multiquadratic/Degree.html#TauCeti.Multiquadratic.finrank_adjoin_range)
- [Source of `TauCeti.Multiquadratic.finrank_adjoin_range` in TauCeti/NumberTheory/Multiquadratic/Degree.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Multiquadratic/Degree.lean#L74)
- [Tau Ceti roadmap status: Multiquadratic fields and genus theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/Multiquadratic/STATUS.md)
