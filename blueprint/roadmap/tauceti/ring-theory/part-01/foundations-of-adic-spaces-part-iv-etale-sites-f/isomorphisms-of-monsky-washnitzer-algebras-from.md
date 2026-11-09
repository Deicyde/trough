---
declaration: def
origin: cited
lean: TauCeti.Dagger.washnitzerAlgebra.substEquiv
statement: formalized
---

# Isomorphisms of Monsky–Washnitzer algebras from inverse substitutions

If two families of
unit-ball polynomials without constant term are inverse to each other under substitution, the
substitutions are mutually inverse `R`-algebra isomorphisms `R⟨X⟩† ≃ R⟨Y⟩†`.

```lean
TauCeti.Dagger.washnitzerAlgebra.substEquiv.{u_1, u_2, u_3} {σ : Type u_1} {τ : Type u_2}
  {R : Type u_3} [NormedCommRing R] [IsUltrametricDist R] [NormOneClass R] [Finite σ]
  (a : σ → MvPolynomial τ R) (ha₀ : ∀ (s : σ), MvPolynomial.constantCoeff (a s) = 0)
  (ha₁ : ∀ (s : σ) (t : τ →₀ ℕ), ‖(a s).coeff t‖ ≤ 1) [Finite τ] (b : τ → MvPolynomial σ R)
  (hb₀ : ∀ (t : τ), MvPolynomial.constantCoeff (b t) = 0)
  (hb₁ : ∀ (t : τ) (u : σ →₀ ℕ), ‖(b t).coeff u‖ ≤ 1)
  (hab : ∀ (s : σ), (MvPolynomial.aeval b) (a s) = MvPolynomial.X s)
  (hba : ∀ (t : τ), (MvPolynomial.aeval a) (b t) = MvPolynomial.X t) :
  ↥(TauCeti.Dagger.washnitzerAlgebra σ R) ≃ₐ[R] ↥(TauCeti.Dagger.washnitzerAlgebra τ R)
```

## Depends on

- [TauCeti.Dagger.washnitzerAlgebra](tauceti-dagger-washnitzeralgebra.md)

## Proof depends on

- [TauCeti.Dagger.washnitzerAlgebra.toTate](tauceti-dagger-washnitzeralgebra-totate.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Dagger.washnitzerAlgebra.substEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/Subst.html#TauCeti.Dagger.washnitzerAlgebra.substEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.Dagger.washnitzerAlgebra.substEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/Subst.html#TauCeti.Dagger.washnitzerAlgebra.substEquiv)
- [Source of `TauCeti.Dagger.washnitzerAlgebra.substEquiv` in TauCeti/RingTheory/Dagger/Subst.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Dagger/Subst.lean#L127)
- [Tau Ceti roadmap status: Foundations of adic spaces, part IV — étale sites, families and dagger geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AdicSpacesPartIV/STATUS.md)
