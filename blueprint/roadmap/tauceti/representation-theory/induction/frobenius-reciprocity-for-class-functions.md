---
declaration: theorem
origin: cited
lean: TauCeti.frobenius_reciprocity_classFunction, TauCeti.frobenius_reciprocity, TauCeti.frobenius_reciprocity_resFDRep
statement: formalized
proof: formalized
---

# Frobenius reciprocity for class functions

The normalized pairing over `G` of an induced
class function with a class function of `G` is the normalized pairing over `S` of the original
class function with the restricted one.

Both sides are written as explicit normalized sums, so the statement does not depend on the name of
any particular pairing; `TauCeti.characterPairing_ind` is the same identity phrased against
`TauCeti.ClassFunction.characterPairing`.  Specialized to two characters this is
`TauCeti.frobenius_reciprocity`, but no representation is involved here: the identity is a
double count over `G × G` and holds for arbitrary class functions.

```lean
TauCeti.frobenius_reciprocity_classFunction.{u, v} {k : Type u} {G : Type v} [Group G]
  {S : Subgroup G} [Semifield k] [Fintype G] (hG : IsUnit ↑(Nat.card G))
  (f : ↥(TauCeti.ClassFunction k ↥S)) (h : ↥(TauCeti.ClassFunction k G)) :
  (↑(Nat.card G))⁻¹ * ∑ g, S.indClassFun (↑f) g * ↑h g⁻¹ =
    (↑(Nat.card ↥S))⁻¹ * ∑ s, ↑f s * ↑h (↑s)⁻¹
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.frobenius_reciprocity_classFunction`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/FrobeniusReciprocity.html#TauCeti.frobenius_reciprocity_classFunction).

## Other forms

**Frobenius reciprocity as a character identity.** Formalized in Tau Ceti as [`TauCeti.frobenius_reciprocity`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/FrobeniusReciprocity.html#TauCeti.frobenius_reciprocity).

```lean
TauCeti.frobenius_reciprocity.{u, v} {k : Type u} {G : Type v} [Field k] [Group G] {S : Subgroup G}
  [Fintype G] (hG : IsUnit ↑(Nat.card G)) (A : FDRep k ↥S) (B : FDRep k G) :
  (↑(Nat.card G))⁻¹ * ∑ g, (TauCeti.indFDRep A).character g * B.character g⁻¹ =
    (↑(Nat.card ↥S))⁻¹ * ∑ s, A.character s * B.character (↑s)⁻¹
```

**Frobenius reciprocity in the other direction.** Formalized in Tau Ceti as [`TauCeti.frobenius_reciprocity_resFDRep`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/FrobeniusReciprocity.html#TauCeti.frobenius_reciprocity_resFDRep).

```lean
TauCeti.frobenius_reciprocity_resFDRep.{u, v} {k : Type u} {G : Type v} [Field k] [Group G]
  {S : Subgroup G} [Fintype G] (hG : IsUnit ↑(Nat.card G)) (A : FDRep k ↥S) (B : FDRep k G) :
  (↑(Nat.card ↥S))⁻¹ * ∑ s, B.character ↑s * A.character s⁻¹ =
    (↑(Nat.card G))⁻¹ * ∑ g, B.character g * (TauCeti.indFDRep A).character g⁻¹
```

## Sources

- [Tau Ceti documentation: `TauCeti.frobenius_reciprocity_classFunction`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/FrobeniusReciprocity.html#TauCeti.frobenius_reciprocity_classFunction)
- [Source of `TauCeti.frobenius_reciprocity_classFunction` in TauCeti/RepresentationTheory/Induction/FrobeniusReciprocity.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Induction/FrobeniusReciprocity.lean#L266)
