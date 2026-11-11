---
declaration: section
origin: cited
lean: SheafOfModules.DifferentialGradedModule.Chaotic.QC, SheafOfModules.DifferentialGradedModule.Chaotic.qc_isClosedUnderIsomorphisms_isSaturated_isTriangulated_isClosedUnderCoproducts, SheafOfModules.DifferentialGradedModule.qc_chaoticDerivedPullback_chaotic
statement: formalized
proof: formalized
---

# 24.33 Differential graded modules on a category

Section 24.33 of the Stacks Project, [Tag 0GZ8](https://stacks.math.columbia.edu/tag/0GZ8). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GZ9, a definition

[Tag 0GZ9](https://stacks.math.columbia.edu/tag/0GZ9) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.Chaotic.QC`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedSectionQuasiCoherent.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedSectionQuasiCoherent.lean#L125). The attribute's comment: “the full subcategory QC(A, d) of D(A, d)”.

> **The full subcategory `QC(A, d)` of `D(A, d)`**: an object `X` lies in it when, for every
> right differential graded `A`-module `M` computing `X` and every morphism `U → V` of the chaotic
> site `C`, the canonical map
>
> `RΓ(V, X) ⊗^𝐋_{A(V)} A(U) ⟶ RΓ(U, X)`
>
> is an isomorphism of `D(A(U), d)`. The derived sections `RΓ(U, X)` are the sections `M(U)` over
> `U` of such a module, which is what they are on a chaotic site, and the canonical map is the
> adjoint transpose of restriction of sections under the adjunction between derived extension of
> scalars along `A(V) ⟶ A(U)` and derived restriction of scalars.

```lean
def QC : ObjectProperty (derivedCategory.{t, a, a} A)
```

## Tag 0GZA, a lemma

[Tag 0GZA](https://stacks.math.columbia.edu/tag/0GZA) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.Chaotic.qc_isClosedUnderIsomorphisms_isSaturated_isTriangulated_isClosedUnderCoproducts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedSectionQuasiCoherentSubcategory.lean, line 251](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedSectionQuasiCoherentSubcategory.lean#L251).

> **Stacks 0GZA.** *Let `C` be a category, viewed as a site with the chaotic topology, let `O`
> be a sheaf of rings on `C` and let `(A, d)` be a sheaf of differential graded `O`-algebras. The
> subcategory `QC(A, d)` is a strictly full, saturated, triangulated subcategory of `D(A, d)`
> preserved by arbitrary direct sums.*
>
> Here `D(A, d)` is the derived category `SheafOfModules.DifferentialGradedModule.derivedCategory`
> of Tag 0FT5 with its triangulated structure of Tag 0FT4, and `QC(A, d)` is
> `SheafOfModules.DifferentialGradedModule.Chaotic.QC` of Tag 0GZ9. The four conjuncts are, in
> order: strict fullness (closure under isomorphisms), saturation (closure under direct summands),
> triangulatedness, and closure under the direct sums indexed by an arbitrary type of the universe
> of the modules.

```lean
theorem qc_isClosedUnderIsomorphisms_isSaturated_isTriangulated_isClosedUnderCoproducts :
    (QC A).IsClosedUnderIsomorphisms ∧ (QC A).IsSaturated ∧ (QC A).IsTriangulated ∧
      ∀ J : Type (max u v), (QC A).IsClosedUnderColimitsOfShape (Discrete J)
```

## Tag 0GZC, a lemma

[Tag 0GZC](https://stacks.math.columbia.edu/tag/0GZC) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.qc_chaoticDerivedPullback_chaotic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedChaoticPullbackQuasiCoherent.lean, line 315](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedChaoticPullbackQuasiCoherent.lean#L315).

> **Stacks 0GZC.** Let `u : C' ⥤ C` be a functor of categories with the chaotic topology,
> `g : (Sh(C'), O') → (Sh(C), O)` the induced morphism of ringed topoi together with
> `σ : g⁻¹O ⟶ O'`, and `φ : g^*A → A'` a map of sheaves of differential graded `O'`-algebras. Then
> the derived pullback `Lg^* : D(A, d) ⥤ D(A', d)` maps `QC(A, d)` into `QC(A', d)`.

```lean
theorem qc_chaoticDerivedPullback_chaotic {C : Type u} [Category.{u} C] {C' : Type u}
    [Category.{u} C'] {Osharp : Sheaf (⊥ : GrothendieckTopology C) CommRingCat.{u}}
    {Osharp' : Sheaf (⊥ : GrothendieckTopology C') CommRingCat.{u}} {F : C' ⥤ C}
    {σ : F.op ⋙ (Stacks.SheafOfModules.Tensor.ringSheaf Osharp).obj ⟶
      (Stacks.SheafOfModules.Tensor.ringSheaf Osharp').obj}
    {A : DifferentialGradedAlgebra.{u, m} (Stacks.SheafOfModules.Tensor.ringSheaf Osharp)}
    {A' : DifferentialGradedAlgebra.{u, m} (Stacks.SheafOfModules.Tensor.ringSheaf Osharp')}
    (φ : DifferentialGradedAlgebra.InverseImageHom F σ A A') (K : derivedCategory.{u, m, m} A) :
    Chaotic.QC A K → Chaotic.QC A' ((chaoticDerivedPullback φ).obj K)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 24.33, Tag 0GZ8](https://stacks.math.columbia.edu/tag/0GZ8)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
