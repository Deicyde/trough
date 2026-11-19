---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.Chow.range_cyclesPushforward_eq_ker_cyclesRestrict
statement: formalized
proof: formalized
---

# The localization sequence for cycles

If the image of a closed immersion `i : Z ⟶ X` is the
complement of the image of an open immersion `j : U ⟶ X`, then a cycle on `X` restricts to zero
on `U` exactly when it is pushed forward from `Z`: the sequence `Z_n(Z) → Z_n(X) → Z_n(U)` is
exact (Fulton, *Intersection Theory*, Proposition 1.8; Stacks, Lemma 42.19.3 (02RX)).

```lean
TauCeti.AlgebraicGeometry.Chow.range_cyclesPushforward_eq_ker_cyclesRestrict.{u} (k : Type u)
  [Field k] {X U : AlgebraicGeometry.Scheme} [X.Over (AlgebraicGeometry.Spec ↧k)]
  [U.Over (AlgebraicGeometry.Spec ↧k)]
  [AlgebraicGeometry.LocallyOfFiniteType (X ↘ AlgebraicGeometry.Spec ↧k)]
  [AlgebraicGeometry.LocallyOfFiniteType (U ↘ AlgebraicGeometry.Spec ↧k)]
  {Z : AlgebraicGeometry.Scheme} (i : Z ⟶ X) [AlgebraicGeometry.IsClosedImmersion i] (j : U ⟶ X)
  [AlgebraicGeometry.IsOpenImmersion j]
  [AlgebraicGeometry.Scheme.Hom.IsOver j (AlgebraicGeometry.Spec ↧k)]
  (hij : Set.range ⇑i = (Set.range ⇑j)ᶜ) {n : ℤ} :
  (TauCeti.AlgebraicGeometry.Chow.cyclesPushforward i).range =
    (TauCeti.AlgebraicGeometry.Chow.cyclesRestrict k j).ker
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.Chow.range_cyclesPushforward_eq_ker_cyclesRestrict`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Chow/OpenRestriction.html#TauCeti.AlgebraicGeometry.Chow.range_cyclesPushforward_eq_ker_cyclesRestrict).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.Chow.range_cyclesPushforward_eq_ker_cyclesRestrict`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Chow/OpenRestriction.html#TauCeti.AlgebraicGeometry.Chow.range_cyclesPushforward_eq_ker_cyclesRestrict)
- [Source of `TauCeti.AlgebraicGeometry.Chow.range_cyclesPushforward_eq_ker_cyclesRestrict` in TauCeti/AlgebraicGeometry/Chow/OpenRestriction.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/Chow/OpenRestriction.lean#L121)
- [Tau Ceti roadmap status: Scheme, stack, cohomology and intersection foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SchemeAndStackFoundations/STATUS.md)
