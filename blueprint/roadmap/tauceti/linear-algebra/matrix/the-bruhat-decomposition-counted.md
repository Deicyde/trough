---
declaration: theorem
origin: cited
lean: TauCeti.GL2Borel.card_doubleCosetQuotient_eq_two, TauCeti.GL2Borel.union_doubleCoset_weyl_eq_univ, TauCeti.GL2Borel.disjoint_doubleCoset_weyl
statement: formalized
proof: formalized
---

# The Bruhat decomposition, counted

the Borel subgroup of `GL₂` over a field has exactly two
double cosets, indexed by the Weyl group `S₂` of `GL₂`. This is the input to the Mackey
irreducibility criterion for the principal series.

```lean
TauCeti.GL2Borel.card_doubleCosetQuotient_eq_two.{u} (F : Type u) [Field F] :
  Nat.card (DoubleCoset.Quotient ↑(TauCeti.GL2Borel F) ↑(TauCeti.GL2Borel F)) = 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GL2Borel.card_doubleCosetQuotient_eq_two`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/GeneralLinearGroup/Bruhat.html#TauCeti.GL2Borel.card_doubleCosetQuotient_eq_two).

## Other forms

**The Bruhat decomposition of `GL₂`, covering half.** Formalized in Tau Ceti as [`TauCeti.GL2Borel.union_doubleCoset_weyl_eq_univ`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/GeneralLinearGroup/Bruhat.html#TauCeti.GL2Borel.union_doubleCoset_weyl_eq_univ).

```lean
TauCeti.GL2Borel.union_doubleCoset_weyl_eq_univ.{u} (F : Type u) [Field F] :
  ↑(TauCeti.GL2Borel F) ∪
      DoubleCoset.doubleCoset (TauCeti.GL2WeylElement F) ↑(TauCeti.GL2Borel F)
        ↑(TauCeti.GL2Borel F) =
    Set.univ
```

**The Bruhat decomposition of `GL₂`, disjointness half.** Formalized in Tau Ceti as [`TauCeti.GL2Borel.disjoint_doubleCoset_weyl`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/GeneralLinearGroup/Bruhat.html#TauCeti.GL2Borel.disjoint_doubleCoset_weyl).

```lean
TauCeti.GL2Borel.disjoint_doubleCoset_weyl.{u} (F : Type u) [Field F] :
  Disjoint (↑(TauCeti.GL2Borel F))
    (DoubleCoset.doubleCoset (TauCeti.GL2WeylElement F) ↑(TauCeti.GL2Borel F) ↑(TauCeti.GL2Borel F))
```

## Sources

- [Tau Ceti documentation: `TauCeti.GL2Borel.card_doubleCosetQuotient_eq_two`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/GeneralLinearGroup/Bruhat.html#TauCeti.GL2Borel.card_doubleCosetQuotient_eq_two)
- [Source of `TauCeti.GL2Borel.card_doubleCosetQuotient_eq_two` in TauCeti/LinearAlgebra/Matrix/GeneralLinearGroup/Bruhat.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/Matrix/GeneralLinearGroup/Bruhat.lean#L314)
