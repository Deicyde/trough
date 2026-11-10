---
declaration: section
origin: cited
lean: Stacks.DifferentialGradedModule.AdmissibleMono.admissibleMono_of_gradedInjective, DifferentialGraded.tensorCharacterBilinearEquiv, DifferentialGraded.homTensorCharacterEquiv, Stacks.DifferentialGradedDual.DGAlgebra.statement_one, Stacks.DifferentialGradedDual.DGAlgebra.statement_two
statement: formalized
proof: formalized
---

# 22.19 Injective modules and differential graded algebras

Section 22.19 of the Stacks Project, [Tag 0FQD](https://stacks.math.columbia.edu/tag/0FQD). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09K2, a lemma

[Tag 09K2](https://stacks.math.columbia.edu/tag/09K2) in the Stacks Project.

**`Stacks.DifferentialGradedModule.AdmissibleMono.admissibleMono_of_gradedInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/AdmissibleSequenceGradedInjective.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DGA/AdmissibleSequenceGradedInjective.lean#L237).

> **Stacks, Tag 09K2 / Lemma 22.19.1.** Let `f : I -> M` be an injective
> homomorphism of differential graded `A`-modules. If `I` is graded injective
> (Definition 3), then `f` is an admissible monomorphism (Definition 4): there is a
> graded `A`-module map `pi : M -> I` with `pi . f = id_I`.
>
> Because the structures `DGAlgebra`, `GradedModule`, `DGModule` bundle all their
> axioms, `A`, `I`, `M` are genuine objects and no extra hypotheses are needed.

```lean
theorem admissibleMono_of_gradedInjective {A : DGAlgebra R}
    {I M : DGModule A} (f : DGModule.Hom I M)
    (hf : f.Injective) (hI : I.GradedInjective) :
    DGModule.AdmissibleMono f
```

## Tag 09K3, a lemma

[Tag 09K3](https://stacks.math.columbia.edu/tag/09K3) in the Stacks Project.

**`DifferentialGraded.tensorCharacterBilinearEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/CharacterDualPairing.lean, line 758](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/CharacterDualPairing.lean#L758). The attribute's comment: “differential graded bilinear maps”.

> **Stacks 09K3, second equality.** For a right differential graded `A`-module `N` and a left
> differential graded `A`-module `M`, maps of complexes of abelian groups `N ⊗_A M → ℚ/ℤ` are
> exactly the differential graded `A`-bilinear pairings `N × M → ℚ/ℤ`.

```lean
def tensorCharacterBilinearEquiv :
    ((CochainComplex.forget₂AddCommGrpCat R).obj (tensorComplex N M) ⟶ characterTarget.{u}) ≃
      CharacterBilinear N M
```

**`DifferentialGraded.homTensorCharacterEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/CharacterDualPairing.lean, line 782](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/CharacterDualPairing.lean#L782). The attribute's comment: “maps into the dual”.

> **Stacks 09K3, first equality.** For a right differential graded `A`-module `N` and a left
> differential graded `A`-module `M`, homomorphisms of right differential graded `A`-modules
> `N → M^∨` into the character dual are exactly the maps of complexes of abelian groups
> `N ⊗_A M → ℚ/ℤ`.

```lean
def homTensorCharacterEquiv :
    DifferentialGradedModule.Hom N (LeftModule.dual M) ≃
      ((CochainComplex.forget₂AddCommGrpCat R).obj (tensorComplex N M) ⟶
        characterTarget.{u})
```

## Tag 09K4, a lemma

[Tag 09K4](https://stacks.math.columbia.edu/tag/09K4) in the Stacks Project.

**`Stacks.DifferentialGradedDual.DGAlgebra.statement_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/Dual/HomIntoDual.lean, line 452](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DGA/Dual/HomIntoDual.lean#L452).

> There is an isomorphism of abelian groups
> `Hom_{Mod_(A,d)}(M, A^vee[k]) ~= Z^k(M^vee)`, natural in `M`: it is compatible with
> precomposition by an arbitrary morphism `phi : M' -> M` on the left and the induced
> map `phi^vee` of dual complexes on the right.

```lean
theorem statement_one (k : ℤ) :
    ∃ Φ : ∀ M : RightModule A,
        RightModuleHom M ((dualModule A).shift k) ≃+ M.cocycles k,
      ∀ {M' M : RightModule A} (φ : RightModuleHom M' M)
        (f : RightModuleHom M ((dualModule A).shift k)),
        Φ M' (precomp φ ((dualModule A).shift k) f)
          = cocyclesMap φ k (Φ M f)
```

**`Stacks.DifferentialGradedDual.DGAlgebra.statement_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/Dual/HomIntoDual.lean, line 722](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DGA/Dual/HomIntoDual.lean#L722).

> There is an isomorphism of abelian groups `Hom_{K(Mod_(A,d))}(M, A^vee[k]) ~= H^k(M^vee)`,
> natural in `M` over the homotopy category: there is a family of group isomorphisms `Ψ M` such
> that, for every morphism `phi : M' -> M`, the precomposition map `homotopyPrecomp phi` on
> homotopy-category Hom groups corresponds under `Ψ` to the map `cohomologyMap phi k` induced on
> cohomology by the dual chain map `dualMap phi`; moreover `cohomologyMap phi k` depends only on
> the homotopy class of `phi`.

```lean
theorem statement_two (k : ℤ) :
    ∃ Ψ : ∀ M : RightModule A, homotopyHom M ((dualModule A).shift k) ≃+ M.cohomology k,
      (∀ {M' M : RightModule A} (φ : RightModuleHom M' M)
          (ξ : homotopyHom M ((dualModule A).shift k)),
          Ψ M' (homotopyPrecomp φ ((dualModule A).shift k) ξ)
            = cohomologyMap φ k (Ψ M ξ))
      ∧ (∀ {M' M : RightModule A} {φ ψ : RightModuleHom M' M},
          Homotopic φ ψ → cohomologyMap φ k = cohomologyMap ψ k)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 22.19, Tag 0FQD](https://stacks.math.columbia.edu/tag/0FQD)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
