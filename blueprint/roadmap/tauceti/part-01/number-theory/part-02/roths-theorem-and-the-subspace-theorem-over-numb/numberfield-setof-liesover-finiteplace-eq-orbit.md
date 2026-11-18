---
declaration: theorem
origin: cited
lean: NumberField.setOf_liesOver_finitePlace_eq_orbit
statement: formalized
proof: formalized
---

# NumberField.setOf_liesOver_finitePlace_eq_orbit

Let `F / K` be a Galois extension of number fields and `v` a finite place of `K`. The absolute
values of `F` lying over `v` form a single orbit of `F ≃ₐ[K] F`.

```lean
NumberField.setOf_liesOver_finitePlace_eq_orbit.{u_1, u_2} {K : Type u_1} {F : Type u_2} [Field K]
  [Field F] [NumberField K] [NumberField F] [Algebra K F] [IsGalois K F]
  (v : NumberField.FinitePlace K) (w : AbsoluteValue F ℝ) [w.LiesOver ↑v] :
  {w' | w'.LiesOver ↑v} = MulAction.orbit Gal(F/K) w
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`NumberField.setOf_liesOver_finitePlace_eq_orbit`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/PlacesOver/Galois.html#NumberField.setOf_liesOver_finitePlace_eq_orbit).

## Sources

- [Tau Ceti documentation: `NumberField.setOf_liesOver_finitePlace_eq_orbit`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/PlacesOver/Galois.html#NumberField.setOf_liesOver_finitePlace_eq_orbit)
- [Source of `NumberField.setOf_liesOver_finitePlace_eq_orbit` in TauCeti/NumberTheory/NumberField/PlacesOver/Galois.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/NumberField/PlacesOver/Galois.lean#L72)
- [Tau Ceti roadmap status: Roth's theorem and the Subspace Theorem over number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SubspaceTheorem/STATUS.md)
