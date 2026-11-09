---
declaration: theorem
origin: cited
lean: TauCeti.ClassFieldTheory.dualTensorHom_kummerH1ConjRepresentationEquiv
statement: formalized
proof: formalized
---

# The equivariant Kummer isomorphism on Kummer classes (`TauCeti.ClassFieldTheory.dualTensorHom_kummerH1ConjRepresentationEquiv`)

Under
`kummerH1ConjRepresentationEquiv`, the Kummer class of a power class `x`, read on `V` through
`restrictSubgroupH1Equiv`, corresponds to the homomorphism `M → Lˣ ⧸ (Lˣ)ⁿ` sending `m` to
`log(m) • x`, where `log : M ≃ μₙ ≃ ℤ/n` is `e` followed by `kummerCoeffAddEquivZMod`.

```lean
TauCeti.ClassFieldTheory.dualTensorHom_kummerH1ConjRepresentationEquiv.{u_1} {F : Type} [Field F]
  {L : Type u_1} [Field L] [Algebra F L] [FiniteDimensional F L] (σ : L →ₐ[F] SeparableClosure F)
  {V : OpenNormalSubgroup (Field.absoluteGaloisGroup F)} {n : ℕ} [Normal F L] (hn : IsUnit ↑n)
  (hV : (TauCeti.absoluteGaloisGroupExtend F L σ).range = ↑V.toOpenSubgroup)
  {M : FDRep (ZMod n) (Field.absoluteGaloisGroup F ⧸ ↑V.toOpenSubgroup)}
  (e :
    (TauCeti.ClassFieldTheory.fdGalRepOfQuotient n F V).obj M ≅ TauCeti.ClassFieldTheory.muNRep n F)
  (x : Additive (TauCeti.powerClassQuotient Lˣ n)) (m : ↑M.V) :
  ((dualTensorHom (ZMod n) (↑M.V) (Additive (TauCeti.powerClassQuotient Lˣ n)))
        ((TauCeti.ClassFieldTheory.kummerH1ConjRepresentationEquiv σ hn hV e)
          ((TauCeti.ClassFieldTheory.restrictSubgroupH1Equiv σ n hV)
            ((TauCeti.fixingSubgroupKummerEquivOfTrivial σ hn (TauCeti.kummerCoeffAddEquivZMod hn) ⋯
                ⋯)
              x))))
      m =
    (TauCeti.kummerCoeffAddEquivZMod hn)
        ((TauCeti.ClassFieldTheory.kummerCoeffEquivMuNRep n F).symm
          ((TopRep.Hom.hom (CategoryTheory.eqToIso ⋯ ≪≫ e).hom) m)) •
      x
```

## Depends on

- [The Kummer isomorphism](../../../representation-theory/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.dualTensorHom_kummerH1ConjRepresentationEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/EulerCharacteristic/Kummer/Basic.html#TauCeti.ClassFieldTheory.dualTensorHom_kummerH1ConjRepresentationEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.dualTensorHom_kummerH1ConjRepresentationEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/EulerCharacteristic/Kummer/Basic.html#TauCeti.ClassFieldTheory.dualTensorHom_kummerH1ConjRepresentationEquiv)
- [Source of `TauCeti.ClassFieldTheory.dualTensorHom_kummerH1ConjRepresentationEquiv` in TauCeti/NumberTheory/ClassFieldTheory/Local/EulerCharacteristic/Kummer/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ClassFieldTheory/Local/EulerCharacteristic/Kummer/Basic.lean#L247)
