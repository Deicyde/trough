---
declaration: theorem
origin: cited
lean: NumberField.exists_finset_superset_forall_exists_mulHeight_eq
statement: formalized
proof: formalized
---

# The height of every point is computed by finitely many places

Every finite set `S` of
finite places is contained in a finite set `S'` such that every nonzero finite tuple has a nonzero
scalar multiple `c • x` which is `S'`-primitive, so that the height of `x` is the product of the
local sup norms of `c • x` over the infinite places and the places of `S'`. One may take any `S'`
whose `S'`-integers are a principal ideal domain.

```lean
NumberField.exists_finset_superset_forall_exists_mulHeight_eq.{u_1, u_2} {K : Type u_1} [Field K]
  [NumberField K] {ι : Type u_2} [Finite ι]
  (S : Finset (IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers K))) :
  ∃ S',
    S ⊆ S' ∧
      ∀ (x : ι → K),
        x ≠ 0 →
          ∃ c,
            c ≠ 0 ∧
              (↑S').IsPrimitive (c • x) ∧
                Height.mulHeight x =
                  (∏ v, (⨆ i, v (c * x i)) ^ v.mult) *
                    ∏ v ∈ S', ⨆ i, (NumberField.FinitePlace.mk v) (c * x i)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`NumberField.exists_finset_superset_forall_exists_mulHeight_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Primitive.html#NumberField.exists_finset_superset_forall_exists_mulHeight_eq).

## Sources

- [Tau Ceti documentation: `NumberField.exists_finset_superset_forall_exists_mulHeight_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Primitive.html#NumberField.exists_finset_superset_forall_exists_mulHeight_eq)
- [Source of `NumberField.exists_finset_superset_forall_exists_mulHeight_eq` in TauCeti/NumberTheory/Height/Primitive.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/Height/Primitive.lean#L164)
- [Tau Ceti roadmap status: Roth's theorem and the Subspace Theorem over number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SubspaceTheorem/STATUS.md)
