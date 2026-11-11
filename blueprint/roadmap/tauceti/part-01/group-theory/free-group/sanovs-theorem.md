---
declaration: theorem
origin: cited
lean: TauCeti.injective_freeGroup_lift_transvection_of_two_le_abs, TauCeti.injective_freeGroup_lift_transvection_two
statement: formalized
proof: formalized
---

# Sanov's theorem

**Sanov's theorem**, in the general form over a linearly ordered commutative ring `R`: for
`c, d : R` with `2 ≤ |c|` and `2 ≤ |d|`, the matrices `[[1, c], [0, 1]]` and `[[1, 0], [d, 1]]`
freely generate a free subgroup of rank two of `SL(2, R)`.

```lean
TauCeti.injective_freeGroup_lift_transvection_of_two_le_abs.{u_1} {R : Type u_1} [CommRing R]
  [LinearOrder R] [IsStrictOrderedRing R] {c d : R} (hc : 2 ≤ |c|) (hd : 2 ≤ |d|) :
  Function.Injective
    ⇑(FreeGroup.lift
        ![Matrix.SpecialLinearGroup.transvection ⋯ c, Matrix.SpecialLinearGroup.transvection ⋯ d])
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.injective_freeGroup_lift_transvection_of_two_le_abs`](https://taucetiproject.org/docs/TauCeti/GroupTheory/FreeGroup/Linear.html#TauCeti.injective_freeGroup_lift_transvection_of_two_le_abs).

## Other forms

**Sanov's theorem.** Formalized in Tau Ceti as [`TauCeti.injective_freeGroup_lift_transvection_two`](https://taucetiproject.org/docs/TauCeti/GroupTheory/FreeGroup/Linear.html#TauCeti.injective_freeGroup_lift_transvection_two).

```lean
TauCeti.injective_freeGroup_lift_transvection_two :
  Function.Injective
    ⇑(FreeGroup.lift
        ![Matrix.SpecialLinearGroup.transvection ⋯ 2, Matrix.SpecialLinearGroup.transvection ⋯ 2])
```

## Sources

- [Tau Ceti documentation: `TauCeti.injective_freeGroup_lift_transvection_of_two_le_abs`](https://taucetiproject.org/docs/TauCeti/GroupTheory/FreeGroup/Linear.html#TauCeti.injective_freeGroup_lift_transvection_of_two_le_abs)
- [Source of `TauCeti.injective_freeGroup_lift_transvection_of_two_le_abs` in TauCeti/GroupTheory/FreeGroup/Linear.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/FreeGroup/Linear.lean#L98)
