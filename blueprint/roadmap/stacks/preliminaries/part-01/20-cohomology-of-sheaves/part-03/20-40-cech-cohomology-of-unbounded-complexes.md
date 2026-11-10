---
declaration: section
origin: cited
lean: Stacks.Cech.globalSectionsToAlternatingCech, Stacks.Cech.globalSectionsToAlternatingCech_app_f, Stacks.Cech.alternatingCechToDerivedGlobalSections, Stacks.Cech.isIso_alternatingCechToDerivedComparison_of_acyclicBasis
statement: formalized
proof: formalized
---

# 20.40 Čech cohomology of unbounded complexes

Section 20.40 of the Stacks Project, [Tag 08BZ](https://stacks.math.columbia.edu/tag/08BZ). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08C0, an equation

[Tag 08C0](https://stacks.math.columbia.edu/tag/08C0) in the Stacks Project.

**`Stacks.Cech.globalSectionsToAlternatingCech`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Cech/AlternatingGlobalSections.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/Cech/AlternatingGlobalSections.lean#L180).

> **Stacks Project, Tag 08C0.** The functorial map from the complex of global sections to the
> total alternating Čech complex: in each cohomological degree a section is sent, in Čech degree
> zero, to its restrictions to the members of the family.

```lean
noncomputable def globalSectionsToAlternatingCech :
    globalSectionsUliftComplexFunctor.{u, v, w} X ⟶ alternatingCechTotalComplexFunctor U
```

**`Stacks.Cech.globalSectionsToAlternatingCech_app_f`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Cech/AlternatingGlobalSections.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/Cech/AlternatingGlobalSections.lean#L208). The attribute's comment: “degree-zero restrictions and vanishing higher components”.

> **Stacks Project, Tag 08C0.** In every cohomological degree the canonical map restricts a
> global section into alternating Čech degree zero and includes that summand into the total
> complex; in particular all of its positive Čech components vanish.

```lean
lemma globalSectionsToAlternatingCech_app_f
    (K : CochainComplex ((Opens X)ᵒᵖ ⥤ AddCommGrpCat.{w}) ℤ) (n : ℤ) :
    ((globalSectionsToAlternatingCech X U).app K).f n =
      globalSectionsAlternatingCechRestrictionInt X U (K.X n) ≫
        ((alternatingCechBicomplexFunctor U).obj K).ιTotal (up ℤ) 0 n n (by simp)
```

## Tag 08C1, a lemma

[Tag 08C1](https://stacks.math.columbia.edu/tag/08C1) in the Stacks Project.

**`Stacks.Cech.alternatingCechToDerivedGlobalSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechTotalComplex/AlternatingDerivedGlobalSections.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechTotalComplex/AlternatingDerivedGlobalSections.lean#L275).

> **Stacks Project, Tag 08C1.** For a ringed space `(X, O_X)` and a finite open covering `U`
> of `X`, the total alternating Čech complex of an unbounded complex of `O_X`-modules has a
> canonical map to its derived global sections, functorial in the complex and compatible with
> the augmentation of Tag 08C0.

```lean
noncomputable def alternatingCechToDerivedGlobalSections :
    AlternatingCechToDerivedGlobalSections X R
```

## Tag 08C2, a lemma

[Tag 08C2](https://stacks.math.columbia.edu/tag/08C2) in the Stacks Project.

**`Stacks.Cech.isIso_alternatingCechToDerivedComparison_of_acyclicBasis`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechTotalComplex/AlternatingCechComputesDerivedSections.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechTotalComplex/AlternatingCechComputesDerivedSections.lean#L93).

> **[Stacks, Tag 08C2]** Let `(X, O_X)` be a ringed space, let `U : I → Opens X` be a finite
> open covering of `X` and let `F^•` be a complex of `O_X`-modules. Let `B` be a set of open
> subsets of `X` such that every open of `X` is a union of members of `B`, such that every finite
> intersection of members of the covering lies in `B`, and such that for every `W ∈ B` and every
> `p > 0` the cohomology groups `H^p(W, F^q)`, `H^p(W, Coker(F^{q-1} → F^q))` and
> `H^p(W, H^q(F))` all vanish. Then the comparison map
> `Tot(Č_alt^•(U, F^•)) ⟶ RΓ(X, F^•)` of Tag 08C1 is an isomorphism in `D(Ab)`.

```lean
theorem isIso_alternatingCechToDerivedComparison_of_acyclicBasis
    {I : Type u} [Finite I] (U : I → Opens X) (hU : (⊤ : Opens X) = iSup U)
    (F : CochainComplex (SheafOfModules.{u} R) ℤ)
    (B : Set (Opens X)) (hB : Opens.IsBasis B)
    (h_inter : ∀ (p : ℕ) (s : Fin (p + 1) → I), (⨅ k, U (s k)) ∈ B)
    (h_terms : ∀ W ∈ B, ∀ (q : ℤ) (p : ℕ), 0 < p →
      IsZero (((SheafOfModules.evaluation R (op W)).rightDerived p).obj (F.X q)))
    (h_cokernels : ∀ W ∈ B, ∀ (q : ℤ) (p : ℕ), 0 < p →
      IsZero (((SheafOfModules.evaluation R (op W)).rightDerived p).obj
        (cokernel (F.d (q - 1) q))))
    (h_homology : ∀ W ∈ B, ∀ (q : ℤ) (p : ℕ), 0 < p →
      IsZero (((SheafOfModules.evaluation R (op W)).rightDerived p).obj (F.homology q))) :
    IsIso ((alternatingCechToDerivedComparison X R U hU).app F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.40, Tag 08BZ](https://stacks.math.columbia.edu/tag/08BZ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
