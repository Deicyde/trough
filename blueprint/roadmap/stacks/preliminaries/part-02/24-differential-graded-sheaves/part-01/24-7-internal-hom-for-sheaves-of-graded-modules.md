---
declaration: section
origin: cited
lean: SheafOfModules.gradedLocalHomSheaf, SheafOfModules.gradedSheafHom, SheafOfModules.gradedSheafHomComp, SheafOfModules.gradedSheafHomCompSum, SheafOfModules.gradedHomLinearEquivSections, SheafOfModules.gradedHomLinearEquivSections_comp
statement: formalized
proof: formalized
---

# 24.7 Internal hom for sheaves of graded modules

Section 24.7 of the Stacks Project, [Tag 0FR3](https://stacks.math.columbia.edu/tag/0FR3). 1 tag here is carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FR3, the section

[Tag 0FR3](https://stacks.math.columbia.edu/tag/0FR3) in the Stacks Project.

**`SheafOfModules.gradedLocalHomSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInternalHomSheaf.lean, line 538](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInternalHomSheaf.lean#L538). The attribute's comment: “the degree-`n` term `SheafHom^n_A(M, L)`, a subsheaf of `∏ SheafHom_O(M^i, L^{i + n})`, as a sheaf of `O`-modules”.

> **Stacks 0FR3, the degree-`n` term `SheafHom^n_A(M, L)`.** The sheaf of `R`-modules whose
> sections over `U` are the degree-`n` local homomorphisms `M|_U → L|_U`: the families
> `f = (f_i)` of `R|_U`-linear maps `f_i : M^i|_U → L^{i + n}|_U` with `f_{i + p}(x a) = f_i(x) a`
> for local sections `a` of `A^p`. These are exactly the local sections of
> `∏_i SheafHom_R(M^i, L^{i + n})` satisfying that condition, so this is the subsheaf of the
> product described in the source.

```lean
noncomputable def gradedLocalHomSheaf (M : GradedModule.{t, a, w} A)
    (L : GradedModule.{t, a, z} A) (n : ℤ) : SheafOfModules.{max u v w z} R
```

**`SheafOfModules.gradedSheafHom`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInternalHomSheaf.lean, line 555](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInternalHomSheaf.lean#L555). The attribute's comment: “the graded `O`-module `SheafHom^gr_A(M, L)`”.

> **Stacks 0FR3, the graded `O`-module `SheafHom^gr_A(M, L)`.** The internal hom of two right
> graded `A`-modules, as a graded sheaf of `R`-modules: in degree `n` the sheaf
> `SheafOfModules.gradedLocalHomSheaf M L n` of degree-`n` local homomorphisms.

```lean
noncomputable abbrev gradedSheafHom (M : GradedModule.{t, a, w} A)
    (L : GradedModule.{t, a, z} A) : ℤ → SheafOfModules.{max u v w z} R
```

**`SheafOfModules.gradedSheafHomComp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInternalHomSheaf.lean, line 702](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInternalHomSheaf.lean#L702). The attribute's comment: “the composition map `SheafHom^m_A(L, M) ⊗_O SheafHom^n_A(K, L) → SheafHom^{n + m}_A(K, M)`”.

> **Stacks 0FR3, the composition map.** The morphism of sheaves of `O`-modules
> `SheafHom^m_A(L, M) ⊗_O SheafHom^n_A(K, L) ⟶ SheafHom^{n + m}_A(K, M)` given locally by
> composition, `g ⊗ f ↦ g ∘ f` (`SheafOfModules.gradedSheafHomComp_tmul`).

```lean
noncomputable def gradedSheafHomComp (m n : ℤ) :
    gradedSheafHomTensor O K L M m n ⟶ gradedLocalHomSheaf K M (n + m)
```

**`SheafOfModules.gradedSheafHomCompSum`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInternalHomSheaf.lean, line 733](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInternalHomSheaf.lean#L733). The attribute's comment: “the composition map on degree `k` of `SheafHom^gr_A(L, M) ⊗_O SheafHom^gr_A(K, L)`”.

> **Stacks 0FR3, the composition map of graded `O`-modules.** Degree `k` of the tensor product
> of the graded `O`-modules `SheafHom^gr_A(L, M)` and `SheafHom^gr_A(K, L)` is
> `⨁_{m + n = k} SheafHom^m_A(L, M) ⊗_O SheafHom^n_A(K, L)` (the tensor product of
> [Stacks, Tag 0FR2] over the graded algebra `O`, concentrated in degree `0`), and the composition
> map on it is `SheafOfModules.gradedSheafHomComp m n` on the summand of index `(m, n)`.

```lean
noncomputable def gradedSheafHomCompSum (k : ℤ) :
    (∐ fun p : {p : ℤ × ℤ // p.1 + p.2 = k} =>
      gradedSheafHomTensor O K L M p.1.1 p.1.2) ⟶ gradedLocalHomSheaf K M k
```

**`SheafOfModules.gradedHomLinearEquivSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInternalHomSheaf.lean, line 905](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInternalHomSheaf.lean#L905). The attribute's comment: “`Hom_{Mod^gr(A)}(M, L) = Γ(C, SheafHom^gr_A(M, L))` as graded `Γ(C, O)`-modules, degreewise”.

> **Stacks 0FR3, `Hom_{Mod^gr(A)}(M, L) = Γ(C, SheafHom^gr_A(M, L))`.** In each degree `n`,
> the homomorphisms `M → L` of right graded `A`-modules homogeneous of degree `n` are the global
> sections of `SheafHom^n_A(M, L)`, as modules over the ring `Γ(C, R)` of global sections: a
> homomorphism is sent to the compatible family of its restrictions to the slice sites. Its
> compatibility with composition is `SheafOfModules.gradedHomLinearEquivSections_comp`.

```lean
noncomputable def gradedHomLinearEquivSections (M L : GradedModule.{t, a, w} A) (n : ℤ) :
    GradedHomOfDegree M L n ≃ₗ[Stacks.Cohomology.SiteModules.GlobalSectionRing R]
      Stacks.Cohomology.SiteModules.GlobalSections R (gradedLocalHomSheaf M L n)
```

**`SheafOfModules.gradedHomLinearEquivSections_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInternalHomSheaf.lean, line 952](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInternalHomSheaf.lean#L952). The attribute's comment: “the identification with global sections is compatible with composition”.

> **Stacks 0FR3, compatibility with composition.** Under
> `Hom_{Mod^gr(A)}(-, -) = Γ(C, SheafHom^gr_A(-, -))`, composition `g ∘ f` of homogeneous
> homomorphisms corresponds to the composition map
> `SheafHom^m_A(L, M) ⊗_O SheafHom^n_A(K, L) → SheafHom^{n + m}_A(K, M)` applied to the image of
> the section `g ⊗ f` of the tensor product, over every object.

```lean
theorem gradedHomLinearEquivSections_comp {m n : ℤ} (g : GradedHomOfDegree L M m)
    (f : GradedHomOfDegree K L n) (X : Cᵒᵖ) :
    (gradedHomLinearEquivSections K M (n + m) (g.comp f)).1 X =
      PresheafOfModules.Hom.app (gradedSheafHomComp O (K := K) (L := L) (M := M) m n).val X
        (PresheafOfModules.Hom.app ((PresheafOfModules.sheafificationAdjunction
          (𝟙 (CategoryTheory.Sheaf.toRingCat J O).obj)).unit.app
            (PresheafOfModules.tensorObj (gradedLocalHomPresheafOver O L M m)
              (gradedLocalHomPresheafOver O K L n))) X
          ((show (gradedLocalHomPresheafOver O L M m).obj X from
              (gradedHomLinearEquivSections L M m g).1 X) ⊗ₜ
            (show (gradedLocalHomPresheafOver O K L n).obj X from
              (gradedHomLinearEquivSections K L n f).1 X)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 24.7, Tag 0FR3](https://stacks.math.columbia.edu/tag/0FR3)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
