---
declaration: section
origin: cited
lean: Stacks.LocalCohomology.derivationOperator, Stacks.LocalCohomology.localCohomologyOfRing_frobeniusIso, Stacks.EtaleDerivation.subsingleton_sheafDerivation, Stacks.EtaleDerivation.nonempty_twistedDerivation, Stacks.EtaleFrobenius.nonempty_extendScalarsDerived_derivedGlobalSections_iso, Stacks.EtaleFrobenius.nonempty_extendScalarsDerived_derivedGlobalSections_iso_of_etale
statement: formalized
proof: formalized
---

# 51.19 Additional structure on local cohomology

Section 51.19 of the Stacks Project, [Tag 0EC4](https://stacks.math.columbia.edu/tag/0EC4). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0EC5, a lemma

[Tag 0EC5](https://stacks.math.columbia.edu/tag/0EC5) in the Stacks Project.

**`Stacks.LocalCohomology.derivationOperator`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/DerivationAction.lean, line 408](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalCohomology/DerivationAction.lean#L408).

> **Stacks Project, Tag 0EC5.** A derivation `θ` of `A` induces a canonical additive operator on
> each local cohomology module `H^i_{V(I)}(A)`, satisfying the Leibniz rule
> `D (a x) = θ(a) x + a D(x)`. It is characterized on Čech cohomology classes by the unique
> extensions of `θ` to the localizations appearing in the Čech complex, for every finite generating
> family of `I`; `Stacks.LocalCohomology.DerivationOperator.ext` is the uniqueness this
> characterization provides.

```lean
def derivationOperator (A : Type u) [CommRing A] (I : Ideal A) (hI : I.FG)
    (θ : Derivation ℤ A A) (i : ℕ) : DerivationOperator A I hI i θ
```

## Tag 0EC6, a lemma

[Tag 0EC6](https://stacks.math.columbia.edu/tag/0EC6) in the Stacks Project.

**`Stacks.LocalCohomology.localCohomologyOfRing_frobeniusIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/Frobenius.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalCohomology/Frobenius.lean#L134).

> **Stacks Project, Tag 0EC6.** For a commutative ring `A` in which a prime `p` vanishes and a
> finitely generated ideal `I`, derived extension of scalars along the Frobenius endomorphism
> fixes the local cohomology `RΓ_{V(I)}(A)` of the regular module up to isomorphism.

```lean
def localCohomologyOfRing_frobeniusIso (A : Type u) [CommRing A] (p : ℕ) (hp : p.Prime)
    (hp0 : (p : A) = 0) (I : Ideal A) (hI : I.FG) :
    (derivedExtensionScalarsGeneral.{u, u, u} (frobeniusOfNatCastEqZero A p hp hp0)).functor.obj
        ((localCohomologyDerived A I hI).obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj (ModuleCat.of A A))) ≅
      (localCohomologyDerived A I hI).obj
        ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj (ModuleCat.of A A))
```

## Tag 0EC7, a lemma

[Tag 0EC7](https://stacks.math.columbia.edu/tag/0EC7) in the Stacks Project.

**`Stacks.EtaleDerivation.subsingleton_sheafDerivation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/StructureSheafDerivation.lean, line 885](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/StructureSheafDerivation.lean#L885). The attribute's comment: “uniqueness”.

> The affine-normalized, restriction-compatible extension of a base derivation to the
> structure sheaf is unique.

```lean
theorem subsingleton_sheafDerivation {A : Type u} [CommRing A] {V : Scheme.{u}}
    (f : V ⟶ Spec (.of A)) (θ : Derivation ℤ A A) :
    Subsingleton (SheafDerivation f θ)
```

**`Stacks.EtaleDerivation.nonempty_twistedDerivation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/StructureSheafDerivation.lean, line 910](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/StructureSheafDerivation.lean#L910). The attribute's comment: “existence and Leibniz rule”.

> An absolute derivation of the base ring extends to an affine-normalized derivation of the
> structure sheaf of a quasi-compact, quasi-separated étale scheme. In every degree its induced
> additive operator on the canonical cohomology module satisfies the twisted Leibniz rule.

```lean
theorem nonempty_twistedDerivation {A : Type u} [CommRing A] {V : Scheme.{u}}
    (f : V ⟶ Spec (.of A)) [QuasiCompact f] [QuasiSeparated f] [Etale f]
    (θ : Derivation ℤ A A) (i : ℕ) : Nonempty (TwistedDerivation f i θ)
```

## Tag 0EC9, a lemma

[Tag 0EC9](https://stacks.math.columbia.edu/tag/0EC9) in the Stacks Project.

**`Stacks.EtaleFrobenius.nonempty_extendScalarsDerived_derivedGlobalSections_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FrobeniusBaseChange.lean, line 230](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FrobeniusBaseChange.lean#L230). The attribute's comment: “cohomology and base change is the explicit hypothesis `Stacks.EtaleFrobenius.DerivedGlobalSectionsBaseChange A`, namely Stacks 08IB for the structure sheaf over an affine base: for every ring map out of `A` and every Cartesian square over its spectrum whose left-hand morphism is flat, quasi-compact and quasi-separated, derived extension of scalars carries the derived global sections of the source to those of the base change. The library carries the base change morphism of Stacks 08HY but not its invertibility in Tor-independent generality, whose globalization step is Stacks 0DJ9. Everything else is proved: the Cartesian square supplied to that hypothesis is the absolute Frobenius square of `V`, Cartesian by Stacks 0EBS”.

> Let `p` be a prime number, let `A` be a commutative ring in which `p` vanishes and let
> `F : A → A`, `a ↦ aᵖ`, be its Frobenius endomorphism. Assuming cohomology and base change
> `Stacks.EtaleFrobenius.DerivedGlobalSectionsBaseChange A`, for a quasi-compact, quasi-separated,
> étale scheme `V` over `Spec A` there is an isomorphism
>
> `RΓ(V, 𝒪_V) ⊗^L_{A, F} A ≅ RΓ(V, 𝒪_V)`
>
> in `D(A)`.

```lean
theorem nonempty_extendScalarsDerived_derivedGlobalSections_iso
    [QuasiCompact f] [QuasiSeparated f] [Etale f]
    (hbc : DerivedGlobalSectionsBaseChange A) :
    Nonempty ((StacksDraft.PseudoCoherence.extendScalarsDerived
        (Stacks.LocalCohomology.frobeniusOfNatCastEqZero A p Fact.out hp0)).obj
        ((derivedGlobalSectionsOver f).obj (derivedStructureSheaf V)) ≅
      (derivedGlobalSectionsOver f).obj (derivedStructureSheaf V))
```

**`Stacks.EtaleFrobenius.nonempty_extendScalarsDerived_derivedGlobalSections_iso_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FrobeniusCohomologyBaseChange.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FrobeniusCohomologyBaseChange.lean#L79).

> **Stacks Project, Tag 0EC9.** Let `p` be a prime number, let `A` be a commutative ring in
> which `p` vanishes and let `F : A → A`, `a ↦ aᵖ`, be its Frobenius endomorphism. If
> `V ⟶ Spec A` is quasi-compact, quasi-separated and étale, then there exists an isomorphism
>
> `RΓ(V, 𝒪_V) ⊗^L_{A, F} A ≅ RΓ(V, 𝒪_V)`
>
> in `D(A)`.
>
> The relative Frobenius of `V` is an isomorphism ([Stacks, Tag 0EBS]), so the absolute Frobenius
> square of `V` is cartesian, and cohomology and base change for the flat morphism `V ⟶ Spec A`
> (`derivedGlobalSectionsBaseChange`, [Stacks, Tag 08IB]) applies to it.

```lean
theorem nonempty_extendScalarsDerived_derivedGlobalSections_iso_of_etale
    [QuasiCompact f] [QuasiSeparated f] [Etale f] :
    Nonempty ((StacksDraft.PseudoCoherence.extendScalarsDerived
        (Stacks.LocalCohomology.frobeniusOfNatCastEqZero A p Fact.out hp0)).obj
        ((derivedGlobalSectionsOver f).obj (derivedStructureSheaf V)) ≅
      (derivedGlobalSectionsOver f).obj (derivedStructureSheaf V))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 51.19, Tag 0EC4](https://stacks.math.columbia.edu/tag/0EC4)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
