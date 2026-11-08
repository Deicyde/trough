---
declaration: theorem
origin: cited
lean: TauCeti.frobenius_reciprocity
statement: formalized
proof: formalized
---

# Frobenius reciprocity as a character identity

The scalar product over `G` of an induced
character with a character of `G` equals the scalar product over `S` of the original character with
the restricted character.

Both sides are written as explicit normalized sums, so the statement does not depend on the name of
any particular pairing; `TauCeti.characterPairing_indFDRep` is the same identity phrased against
`TauCeti.ClassFunction.characterPairing`.  The hypothesis `hG` is what makes the normalizing factors
meaningful; it also supplies the invertibility of `Nat.card S`.

```lean
TauCeti.frobenius_reciprocity.{u, v} {k : Type u} {G : Type v} [Field k] [Group G] {S : Subgroup G}
  [Fintype G] (hG : IsUnit ↑(Nat.card G)) (A : FDRep k ↥S) (B : FDRep k G) :
  (↑(Nat.card G))⁻¹ * ∑ g, (TauCeti.indFDRep A).character g * B.character g⁻¹ =
    (↑(Nat.card ↥S))⁻¹ * ∑ s, A.character s * B.character (↑s)⁻¹
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.frobenius_reciprocity`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/FrobeniusReciprocity.html#TauCeti.frobenius_reciprocity).

## Sources

- [Tau Ceti documentation: `TauCeti.frobenius_reciprocity`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/FrobeniusReciprocity.html#TauCeti.frobenius_reciprocity)
- [Source of `TauCeti.frobenius_reciprocity` in TauCeti/RepresentationTheory/Induction/FrobeniusReciprocity.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Induction/FrobeniusReciprocity.lean#L113)
