---
declaration: section
origin: cited
lean: Stacks.Modules.globalSections_equivalence_finiteFreeSummand_finiteProjective, Stacks.Cohomology.InvertibleDerived.hasInvertibleModuleDecomposition_of_isInvertibleObject, Stacks.Cohomology.InvertibleDerived.isInvertibleObject_tfae, Stacks.Cohomology.InvertibleDerived.hasInvertibleModuleDecomposition_iff_hasLocalInvertibleDegree, Stacks.Cohomology.InvertibleDerived.isInvertibleObject_of_hasInvertibleModuleDecomposition_unconditional, Stacks.Cohomology.InvertibleDerived.HasInvertibleModuleDecomposition, Stacks.Cohomology.InvertibleDerived.isPerfect_of_hasInvertibleModuleDecomposition, Stacks.Cohomology.InvertibleDerived.IsInvertibleObject
statement: formalized
proof: formalized
---

# 20.52 Invertible objects in the derived category

Section 20.52 of the Stacks Project, [Tag 0FPE](https://stacks.math.columbia.edu/tag/0FPE). 2 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FPF, a lemma

[Tag 0FPF](https://stacks.math.columbia.edu/tag/0FPF) in the Stacks Project.

**`Stacks.Modules.globalSections_equivalence_finiteFreeSummand_finiteProjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/RecoveryB/FiniteFreeSummandsOnASpace.lean, line 470](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/RecoveryB/FiniteFreeSummandsOnASpace.lean#L470).

> **Stacks Project, Tag 0FPF.** Global sections induce an equivalence from
> direct summands of finite free `𝒪`-modules to finite projective modules over
> the ring of global sections.

```lean
public theorem globalSections_equivalence_finiteFreeSummand_finiteProjective :
    ∃ (e : ObjectProperty.FullSubcategory (IsDirectSummandOfFiniteFree 𝒪) ≌
        ObjectProperty.FullSubcategory
          (fun M : ModuleCat.{u} (𝒪.obj.obj (op (⊤ : Opens X))) =>
            Module.Finite (𝒪.obj.obj (op (⊤ : Opens X))) M ∧
              Module.Projective (𝒪.obj.obj (op (⊤ : Opens X))) M)),
      Nonempty
        (e.functor ⋙ ObjectProperty.ι _ ≅
          ObjectProperty.ι _ ⋙ globalSectionsFunctor 𝒪)
```

## Tag 0FPG, a lemma

[Tag 0FPG](https://stacks.math.columbia.edu/tag/0FPG) in the Stacks Project.

**`Stacks.Cohomology.InvertibleDerived.hasInvertibleModuleDecomposition_of_isInvertibleObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InvertibleDerivedClauseOneToTwo.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InvertibleDerivedClauseOneToTwo.lean#L124). The attribute's comment: “clause (1) implies clause (2): an invertible object of D(𝒪\_X) has a locally finite invertible module decomposition”.

> **The implication `(1) ⟹ (2)` of Stacks 0FPG.** If `M` is an invertible object of `D(𝒪_X)`,
> there is a locally finite direct product decomposition `𝒪_X = ∏ 𝒪_n` and invertible
> `𝒪_n`-modules `ℋ^n` with `M = ⨁ ℋ^n[-n]`.

```lean
public theorem hasInvertibleModuleDecomposition_of_isInvertibleObject
    [inst : HasDerivedCategory.{d} (Mod X.sheaf)] (M : DerivedModules X.sheaf)
    (hM : IsInvertibleObject M) : HasInvertibleModuleDecomposition X M
```

**`Stacks.Cohomology.InvertibleDerived.isInvertibleObject_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InvertibleDerivedClauseOneToTwo.lean, line 181](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InvertibleDerivedClauseOneToTwo.lean#L181).

> **Stacks 0FPG.** Let `(X, 𝒪_X)` be a ringed space and `M` an object of `D(𝒪_X)`. The following
> are equivalent:
> 1. `M` is invertible in `D(𝒪_X)` for the derived tensor product;
> 2. there is a locally finite direct product decomposition `𝒪_X = ∏ 𝒪_n` and for each `n` an
>    invertible `𝒪_n`-module `ℋ^n` with `M = ⨁ ℋ^n[-n]` in `D(𝒪_X)`.
>
> If they hold, `M` is perfect. If every stalk `𝒪_{X,x}` is a local ring, they are also equivalent
> to
> 3. there is an open covering `X = ⋃ U_i` and for each `i` an integer `n_i` such that `M|_{U_i}` is
>    represented by an invertible `𝒪_{U_i}`-module placed in degree `n_i`.

```lean
public theorem isInvertibleObject_tfae [inst : HasDerivedCategory.{d} (Mod X.sheaf)]
    (M : DerivedModules X.sheaf) :
    [IsInvertibleObject M, HasInvertibleModuleDecomposition X M].TFAE ∧
      (IsInvertibleObject M → @Stacks.Cohomology.PerfectComplexes.IsPerfect.{u, u, d} X inst M) ∧
      ((∀ x : X.carrier, IsLocalRing (X.presheaf.stalk x)) →
        [IsInvertibleObject M, HasInvertibleModuleDecomposition X M,
          HasLocalInvertibleDegree M].TFAE)
```

**`Stacks.Cohomology.InvertibleDerived.hasInvertibleModuleDecomposition_iff_hasLocalInvertibleDegree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InvertibleDerivedClauseThreeToTwo.lean, line 356](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InvertibleDerivedClauseThreeToTwo.lean#L356). The attribute's comment: “if every stalk of 𝒪\_X is a local ring, clauses (2) and (3) are equivalent”.

> **Stacks 0FPG, the equivalence of clauses (2) and (3).** Let `(X, 𝒪_X)` be a ringed space all
> of whose stalks `𝒪_{X,x}` are local rings, and let `M` be an object of `D(𝒪_X)`. Then `M` admits a
> locally finite direct product decomposition `𝒪_X = ∏ 𝒪_n` with invertible `𝒪_n`-modules `ℋ^n` and
> `M = ⨁ ℋ^n[-n]` — clause (2) — if and only if there is an open covering `X = ⋃ U_i` and integers
> `n_i` such that `M|_{U_i}` is represented by an invertible `𝒪_{U_i}`-module placed in degree
> `n_i` — clause (3).

```lean
public theorem hasInvertibleModuleDecomposition_iff_hasLocalInvertibleDegree
    [HasDerivedCategory.{d} (Mod X.sheaf)] (M : DerivedModules X.sheaf)
    (hloc : ∀ x : X.carrier, IsLocalRing (X.presheaf.stalk x)) :
    HasInvertibleModuleDecomposition X M ↔ HasLocalInvertibleDegree M
```

**`Stacks.Cohomology.InvertibleDerived.isInvertibleObject_of_hasInvertibleModuleDecomposition_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InvertibleDerivedFlatRestrictScalars.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InvertibleDerivedFlatRestrictScalars.lean#L85). The attribute's comment: “clause (2) implies clause (1): a locally finite invertible module decomposition of M makes M an invertible object of D(𝒪\_X) for the derived tensor product of Stacks 0FPB”.

> If `M` admits a locally finite invertible module decomposition, then `M` is an invertible
> object of `D(𝒪_X)`.

```lean
public theorem isInvertibleObject_of_hasInvertibleModuleDecomposition_unconditional
    [HasDerivedCategory.{d} (Mod X.sheaf)] (M : DerivedModules X.sheaf)
    (hM : HasInvertibleModuleDecomposition X M) :
    IsInvertibleObject M
```

**`Stacks.Cohomology.InvertibleDerived.HasInvertibleModuleDecomposition`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InvertibleDerivedObjects.lean, line 317](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InvertibleDerivedObjects.lean#L317). The attribute's comment: “clause (2) as a condition on M: that there is a locally finite direct product decomposition 𝒪\_X = ∏\_\{n ∈ ℤ} 𝒪\_n and for each n an invertible 𝒪\_n-module ℋ^n, in the sense of Stacks 01CS, with M = ⨁ ℋ^n[-n] in D(𝒪\_X). This is the clause, not an implication between clauses; the decomposition itself is `ProductDecomposition`”.

> **Clause (2) of Stacks 0FPG.** There is a locally finite direct product decomposition
> `𝒪_X = ∏_{n ∈ ℤ} 𝒪_n` of the structure sheaf and for each `n` an invertible `𝒪_n`-module
> `ℋ^n` such that `M = ⨁_{n ∈ ℤ} ℋ^n[-n]` in `D(𝒪_X)`, the `n`-th summand being `ℋ^n` viewed
> as an `𝒪_X`-module and placed in degree `n`.

```lean
public def HasInvertibleModuleDecomposition (M : DerivedModules X.sheaf) : Prop
```

**`Stacks.Cohomology.InvertibleDerived.isPerfect_of_hasInvertibleModuleDecomposition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InvertibleDerivedObjects.lean, line 432](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InvertibleDerivedObjects.lean#L432). The attribute's comment: “clause (2) implies that M is a perfect object of D(𝒪\_X)”.

> **Stacks 0FPG, the perfectness conclusion.** Let `(X, 𝒪_X)` be a ringed space and let `M`
> be an object of `D(𝒪_X)`. If there is a locally finite direct product decomposition
> `𝒪_X = ∏_{n ∈ ℤ} 𝒪_n` and for each `n` an invertible `𝒪_n`-module `ℋ^n` with
> `M = ⨁ ℋ^n[-n]` in `D(𝒪_X)`, then `M` is a perfect object of `D(𝒪_X)`.
>
> Near a point only finitely many factors survive, each `ℋ^n` is locally a direct summand of a
> finite free `𝒪_n`-module and `𝒪_n` is a direct summand of `𝒪_X`, so the complex with `ℋ^n` in
> degree `n` and zero differentials — which represents `⨁ ℋ^n[-n]` — is locally strictly
> perfect.

```lean
public theorem isPerfect_of_hasInvertibleModuleDecomposition (M : DerivedModules X.sheaf)
    (hM : HasInvertibleModuleDecomposition X M) :
    @Stacks.Cohomology.PerfectComplexes.IsPerfect.{u, u, d} X inst M
```

**`Stacks.Cohomology.InvertibleDerived.IsInvertibleObject`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InvertibleDerivedObjects.lean, line 454](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InvertibleDerivedObjects.lean#L454). The attribute's comment: “clause (1) as a condition on M: that M is invertible in D(𝒪\_X) in the sense of Stacks 0FFN, for the derived tensor product of Stacks 0FPB. This is the clause, not an implication between clauses”.

> **Clause (1) of Stacks 0FPG.** `M` is an invertible object of `D(𝒪_X)`: there is an object
> `N` of `D(𝒪_X)` with `M ⊗^L N ≅ 𝒪_X` and `N ⊗^L M ≅ 𝒪_X`, the tensor product being the derived
> tensor product and `𝒪_X` the structure sheaf in degree zero.

```lean
public def IsInvertibleObject (M : DerivedModules X.sheaf) : Prop
```

**`Stacks.Cohomology.InvertibleDerived.HasLocalInvertibleDegree`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InvertibleDerivedObjects.lean, line 516](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InvertibleDerivedObjects.lean#L516). The attribute's comment: “clause (3) as a condition on M: that there is an open covering X = ⋃ U\_i and for each i an integer n\_i with M|\_\{U\_i} represented by an invertible 𝒪\_\{U\_i}-module placed in degree n\_i. The source's condition that every stalk 𝒪\_\{X,x} is a local ring belongs to the equivalence of (3) with the other clauses, which is hasInvertibleModuleDecomposition\_iff\_hasLocalInvertibleDegree”.

> **Clause (3) of Stacks 0FPG.** `M` is represented by a complex which, on each member of
> some open covering of `X`, is quasi-isomorphic to an invertible module placed in a single
> degree — the degree being allowed to vary with the member of the covering.

```lean
public def HasLocalInvertibleDegree (M : DerivedModules X.sheaf) : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.52, Tag 0FPE](https://stacks.math.columbia.edu/tag/0FPE)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
