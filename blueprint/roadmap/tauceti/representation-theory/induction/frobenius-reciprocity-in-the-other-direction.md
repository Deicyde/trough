---
declaration: theorem
origin: cited
lean: TauCeti.frobenius_reciprocity_resFDRep
statement: formalized
proof: formalized
---

# Frobenius reciprocity in the other direction

the scalar product over `S` of a restricted
character with a character of `S` equals the scalar product over `G` of the original character with
the induced character.  This is `characterPairing_resFDRep` with the pairing unfolded.

```lean
TauCeti.frobenius_reciprocity_resFDRep.{u, v} {k : Type u} {G : Type v} [Field k] [Group G]
  {S : Subgroup G} [Fintype G] (hG : IsUnit ↑(Nat.card G)) (A : FDRep k ↥S) (B : FDRep k G) :
  (↑(Nat.card ↥S))⁻¹ * ∑ s, B.character ↑s * A.character s⁻¹ =
    (↑(Nat.card G))⁻¹ * ∑ g, B.character g * (TauCeti.indFDRep A).character g⁻¹
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Frobenius reciprocity as a character identity](frobenius-reciprocity-as-a-character-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.frobenius_reciprocity_resFDRep`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/FrobeniusReciprocity.html#TauCeti.frobenius_reciprocity_resFDRep).

## Sources

- [Tau Ceti documentation: `TauCeti.frobenius_reciprocity_resFDRep`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/FrobeniusReciprocity.html#TauCeti.frobenius_reciprocity_resFDRep)
- [Source of `TauCeti.frobenius_reciprocity_resFDRep` in TauCeti/RepresentationTheory/Induction/FrobeniusReciprocity.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Induction/FrobeniusReciprocity.lean#L167)
