---
declaration: theorem
origin: cited
lean: TauCeti.groupHomology.indIso_inv
statement: formalized
proof: formalized
---

# The inverse of Shapiro's isomorphism in homology is corestriction of the unit

The
inverse of the isomorphism `Hₙ(G, Ind_S^G A) ≅ Hₙ(S, A)` of `groupHomology.indIso` is the
change-of-group map along `S ≤ G` induced by the unit `A ⟶ Res_S Ind_S^G A`, `a ↦ 1 ⊗ a`,
of induction–restriction. The `DecidableEq G` instance is the one used by Mathlib's `indIso`;
keeping it caller-supplied ensures that this equality rewrites the caller's isomorphism.

```lean
TauCeti.groupHomology.indIso_inv.{u} {k G : Type u} [CommRing k] [Group G] [DecidableEq G]
  (S : Subgroup G) (A : Rep.{u, u, u} k ↥S) (n : ℕ) :
  (groupHomology.indIso S A n).inv =
    groupHomology.map S.subtype ((Rep.indResAdjunction k S.subtype).unit.app A) n
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.groupHomology.indIso_inv`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupHomology/Shapiro.html#TauCeti.groupHomology.indIso_inv).

## Sources

- [Tau Ceti documentation: `TauCeti.groupHomology.indIso_inv`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupHomology/Shapiro.html#TauCeti.groupHomology.indIso_inv)
- [Source of `TauCeti.groupHomology.indIso_inv` in TauCeti/RepresentationTheory/Homological/GroupHomology/Shapiro.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Homological/GroupHomology/Shapiro.lean#L93)
