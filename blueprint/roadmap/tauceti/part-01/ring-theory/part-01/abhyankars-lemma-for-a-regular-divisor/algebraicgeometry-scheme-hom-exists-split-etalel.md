---
declaration: theorem
origin: cited
lean: AlgebraicGeometry.Scheme.Hom.exists_split_etaleLocally
statement: formalized
proof: formalized
---

# AlgebraicGeometry.Scheme.Hom.exists_split_etaleLocally

A finite étale morphism is a finite disjoint union of copies of the base after passage to
an affine étale neighbourhood of any given base point. The splitting is over that neighbourhood,
and `g a = s` guarantees that the neighbourhood contains a point over the prescribed point.

```lean
AlgebraicGeometry.Scheme.Hom.exists_split_etaleLocally.{u} {X S : AlgebraicGeometry.Scheme}
  (f : X ⟶ S) [AlgebraicGeometry.IsFinite f] [AlgebraicGeometry.Etale f] (s : ↥S) :
  ∃ A g,
    AlgebraicGeometry.Etale g ∧
      ∃ a,
        g a = s ∧
          ∃ n,
            Nonempty
              (CategoryTheory.Over.mk (CategoryTheory.Limits.pullback.snd f g) ≅
                CategoryTheory.Over.mk (AlgebraicGeometry.Spec.algebraMap (↑A) (Fin n → ↑A)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AlgebraicGeometry.Scheme.Hom.exists_split_etaleLocally`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FiniteEtale/EtaleLocallySplit.html#AlgebraicGeometry.Scheme.Hom.exists_split_etaleLocally).

## Sources

- [Tau Ceti documentation: `AlgebraicGeometry.Scheme.Hom.exists_split_etaleLocally`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FiniteEtale/EtaleLocallySplit.html#AlgebraicGeometry.Scheme.Hom.exists_split_etaleLocally)
- [Source of `AlgebraicGeometry.Scheme.Hom.exists_split_etaleLocally` in TauCeti/AlgebraicGeometry/FiniteEtale/EtaleLocallySplit.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/FiniteEtale/EtaleLocallySplit.lean#L38)
- [Tau Ceti roadmap status: Abhyankar's lemma for a regular divisor](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AbhyankarLemma/STATUS.md)
