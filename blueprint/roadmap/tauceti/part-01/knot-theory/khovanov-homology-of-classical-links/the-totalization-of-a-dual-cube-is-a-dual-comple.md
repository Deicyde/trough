---
declaration: def
origin: cited
lean: CategoryTheory.Functor.dualCubeComplexIso
statement: formalized
---

# The totalization of a dual cube is a dual complex

For integers `a` and `b` with
`a + b = #ι`, the shift by `b` of the totalization of the dual cube `F.dualCube` is isomorphic to
the dual `Hom(C⟦a⟧, R)` of the shift by `a` of the totalization `C` of `F`. On the vertex `S` of
height `i + b` it sends a linear form on `F(Sᶜ)` to its composite with the projection of `C⁻ⁱ⁺ᵃ`
onto `F(Sᶜ)`, multiplied by `Finset.dualCubeSign S a`
(`CategoryTheory.Functor.dualCubeComplexIso_hom_f_apply`).

```lean
CategoryTheory.Functor.dualCubeComplexIso.{w, u} {ι : Type w} [Fintype ι] [LinearOrder ι]
  {R : Type u} [CommRing R] (F : CategoryTheory.Functor (Finset ι) (ModuleCat R)) {a b : ℤ}
  (hab : a + b = ↑(Fintype.card ι)) :
  F.dualCube.cubeComplex⟦b⟧ ≅
    CochainComplex.linearHomComplex R (F.cubeComplex⟦a⟧)
      ((CochainComplex.singleFunctor (ModuleCat R) 0).obj ↧R)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Functor.dualCubeComplexIso`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/Cube/Dual/Complex.html#CategoryTheory.Functor.dualCubeComplexIso).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Functor.dualCubeComplexIso`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/Cube/Dual/Complex.html#CategoryTheory.Functor.dualCubeComplexIso)
- [Source of `CategoryTheory.Functor.dualCubeComplexIso` in TauCeti/Algebra/Homology/Cube/Dual/Complex.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Homology/Cube/Dual/Complex.lean#L293)
- [Tau Ceti roadmap status: Khovanov homology of classical links](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/KhovanovHomology/STATUS.md)
