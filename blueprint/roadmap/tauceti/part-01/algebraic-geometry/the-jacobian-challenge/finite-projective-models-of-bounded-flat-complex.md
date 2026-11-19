---
declaration: theorem
origin: cited
lean: CochainComplex.exists_quasiIso_finite_projective
statement: formalized
proof: formalized
---

# Finite projective models of bounded flat complexes (Mumford)

Let `R` be a Noetherian ring
and `K` a complex of flat `R`-modules concentrated in degrees `[a, b]` whose cohomology is finitely
generated. Then there is a quasi-isomorphism `ψ : P ⟶ K` from a complex `P` of finitely generated
projective `R`-modules, also concentrated in degrees `[a, b]`, which remains a quasi-isomorphism
after extension of scalars along every `f : R →+* S`. In particular the cohomology of every base
change `S ⊗_R K` is that of `S ⊗_R P`.

```lean
CochainComplex.exists_quasiIso_finite_projective.{u, v} {R : Type u} [CommRing R]
  [IsNoetherianRing R] (K : CochainComplex (ModuleCat R) ℤ) (a b : ℤ) [K.IsStrictlyGE a]
  [K.IsStrictlyLE b] (hflat : ∀ (i : ℤ), Module.Flat R ↑(K.X i))
  (hK : ∀ (i : ℤ), Module.Finite R ↑(HomologicalComplex.homology K i)) :
  ∃ P ψ,
    P.IsStrictlyGE a ∧
      P.IsStrictlyLE b ∧
        (∀ (i : ℤ), Module.Finite R ↑(P.X i) ∧ Module.Projective R ↑(P.X i)) ∧
          QuasiIso ψ ∧
            ∀ (S : Type v) [inst : CommRing S] (f : R →+* S),
              QuasiIso
                (((ModuleCat.extendScalars f).mapHomologicalComplex (ComplexShape.up ℤ)).map ψ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CochainComplex.exists_quasiIso_finite_projective`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/ModuleCat/BaseChange.html#CochainComplex.exists_quasiIso_finite_projective).

## Sources

- [Tau Ceti documentation: `CochainComplex.exists_quasiIso_finite_projective`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/ModuleCat/BaseChange.html#CochainComplex.exists_quasiIso_finite_projective)
- [Source of `CochainComplex.exists_quasiIso_finite_projective` in TauCeti/Algebra/Homology/ModuleCat/BaseChange.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Homology/ModuleCat/BaseChange.lean#L192)
- [Tau Ceti roadmap status: The Jacobian challenge](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/JacobianChallenge/STATUS.md)
