---
declaration: section
origin: cited
lean: Stacks.CategoryTheory.CechComplex.d_comp_π, Stacks.CechGaps.cech_d_apply, CategoryTheory.cechComplexFunctor, HomologicalComplex.homology, Stacks.Cohomology.CechDegreeZero.isSheaf_iff_existsUnique_cechRestrictionHomologyMap, Stacks.Cech.cechComplex_augment_homotopyEquiv_zero_of_eq
statement: formalized
proof: formalized
---

# 20.9 The Čech complex and Čech cohomology

Section 20.9 of the Stacks Project, [Tag 01ED](https://stacks.math.columbia.edu/tag/01ED). 4 tags here are carried by 2 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01EE, an equation

[Tag 01EE](https://stacks.math.columbia.edu/tag/01EE) in the Stacks Project.

Declarations registered for the tag:

- [`Stacks.CategoryTheory.CechComplex.d_comp_π`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/CechComplex.lean#L251), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/CechComplexDifferential.lean, line 36](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/CechComplexDifferential.lean#L36) (StacksFrontier): “the components of the Čech differential, for a presheaf with values in a preadditive category on a category with finite products”.
- [`Stacks.CechGaps.cech_d_apply`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/CechGaps/Decode.lean#L184), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/CechComplexDifferential.lean, line 40](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/CechComplexDifferential.lean#L40) (StacksFrontier): “the Čech differential evaluated on a cochain, for an abelian presheaf on a topological space”.

## Tag 01EF, a definition

[Tag 01EF](https://stacks.math.columbia.edu/tag/01EF) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.cechComplexFunctor`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.cechComplexFunctor#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch20.lean, line 28](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch20.lean#L28) (StacksFrontier): “the Čech complex `Č^•(𝒰, F)`: for `C = Opens X`, a family `U : ι → Opens X` and an abelian presheaf `F`, `(cechComplexFunctor U).obj F` has degree `p` term `∏_{x : Fin (p + 1) → ι} F(U_{x 0} ⊓ ⋯ ⊓ U_{x p})` and the alternating coface differential”. References: SGA 4 V (2.4.3), “more general”; SGA 7 VI (3.1(b)), “partial”.
- [`HomologicalComplex.homology`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex.homology#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch20.lean, line 33](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch20.lean#L33) (StacksFrontier): “the Čech cohomology groups `Ȟ^i(𝒰, F) = H^i(Č^•(𝒰, F))`, as the homology of `(cechComplexFunctor U).obj F`”. References: EGA 0 (11.2.1); EGA 0 (11.3.1), “more general”; EGA 0 (11.3.5); EGA III (7.6.11).

## Tag 01EG, a lemma

[Tag 01EG](https://stacks.math.columbia.edu/tag/01EG) in the Stacks Project.

**`Stacks.Cohomology.CechDegreeZero.isSheaf_iff_existsUnique_cechRestrictionHomologyMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Cech/DegreeZeroAndTheSheafCondition.lean, line 445](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/Cech/DegreeZeroAndTheSheafCondition.lean#L445).

> An abelian presheaf is a sheaf if and only if, for every open covering, the
> canonical restriction-induced map from sections on the covered open to zeroth
> Čech cohomology is an isomorphism.

```lean
public theorem isSheaf_iff_existsUnique_cechRestrictionHomologyMap
    (F : TopCat.Presheaf AddCommGrpCat.{u} X) :
    F.IsSheaf ↔
      ∀ (ι : Type u) (V : Opens X) (U : ι → Opens X) (hU : V = iSup U),
        ∃! f : F.obj (op V) ⟶
            ((CategoryTheory.cechComplexFunctor U).obj F).homology 0,
          IsIso f ∧
            f ≫ ((CategoryTheory.cechComplexFunctor U).obj F).homologyι 0 =
              cechDegreeZeroRestriction F V U hU ≫
                ((CategoryTheory.cechComplexFunctor U).obj F).pOpcycles 0
```

## Tag 0G6S, a lemma

[Tag 0G6S](https://stacks.math.columbia.edu/tag/0G6S) in the Stacks Project.

**`Stacks.Cech.cechComplex_augment_homotopyEquiv_zero_of_eq`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechAndResolutions/ContractibleCech.lean, line 558](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/CechAndResolutions/ContractibleCech.lean#L558).

> If a family of open subsets of `U` contains `U`, its extended Čech complex is homotopy
> equivalent to zero. The existential proof is precisely the fact that the canonical augmentation
> squares to zero; the resulting augmented complex is independent of that proof by proof
> irrelevance.

```lean
lemma cechComplex_augment_homotopyEquiv_zero_of_eq
    (X : TopCat.{u}) (F : TopCat.Presheaf Ab.{u} X)
    {I : Type u} {U : Opens X} (V : I → Opens X) (hV : ∀ i, V i ≤ U)
    (i : I) (hi : V i = U) :
    ∃ (w : cechAugmentation X F V hV ≫
        ((cechComplexFunctor V).obj F).d 0 1 = 0),
      Nonempty (HomotopyEquiv
        (((cechComplexFunctor V).obj F).augment
          (cechAugmentation X F V hV) w)
        (HomologicalComplex.zero : CochainComplex Ab.{u} ℕ))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.9, Tag 01ED](https://stacks.math.columbia.edu/tag/01ED)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
