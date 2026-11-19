---
declaration: def
origin: cited
lean: TauCeti.FiniteEtaleScheme.galContinuousMulEquivAutFiber
statement: formalized
---

# The étale fundamental group of a field is its absolute Galois group

For a separable
closure `Ω` of `K`, the automorphism group of the geometric fibre functor of finite étale
`K`-schemes at `Spec Ω ⟶ Spec K` is `Gal(Ω/K)`, as topological groups.

```lean
TauCeti.FiniteEtaleScheme.galContinuousMulEquivAutFiber.{u} (K Ω : Type u) [Field K] [Field Ω]
  [Algebra K Ω] [IsSepClosed Ω] [IsGalois K Ω] :
  Gal(Ω/K) ≃ₜ*
    CategoryTheory.Aut
      (TauCeti.FiniteEtaleScheme.fiber
        (AlgebraicGeometry.Spec.map (CommRingCat.ofHom (algebraMap K Ω))))
```

## Depends on

- [Finite étale schemes over a connected scheme form a Galois category](finite-etale-schemes-over-a-connected-scheme-for.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.FiniteEtaleScheme.galContinuousMulEquivAutFiber`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FiniteEtale/Galois/FundamentalGroup.html#TauCeti.FiniteEtaleScheme.galContinuousMulEquivAutFiber).

## Sources

- [Tau Ceti documentation: `TauCeti.FiniteEtaleScheme.galContinuousMulEquivAutFiber`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FiniteEtale/Galois/FundamentalGroup.html#TauCeti.FiniteEtaleScheme.galContinuousMulEquivAutFiber)
- [Source of `TauCeti.FiniteEtaleScheme.galContinuousMulEquivAutFiber` in TauCeti/AlgebraicGeometry/FiniteEtale/Galois/FundamentalGroup.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/FiniteEtale/Galois/FundamentalGroup.lean#L191)
- [Tau Ceti roadmap status: Étale cohomology foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EtaleCohomologyFoundations/STATUS.md)
