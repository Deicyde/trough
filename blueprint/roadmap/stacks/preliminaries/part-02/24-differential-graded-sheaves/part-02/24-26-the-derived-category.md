---
declaration: section
origin: cited
lean: SheafOfModules.DifferentialGradedModule.zerothCohomology_map_eq_of_homotopic, SheafOfModules.DifferentialGradedModule.HomotopyCategory.zerothCohomologyFunctor, SheafOfModules.DifferentialGradedModule.HomotopyCategory.zerothCohomologyFunctor_isHomological, SheafOfModules.DifferentialGradedModule.acyclic, SheafOfModules.DifferentialGradedModule.acyclic_isClosedUnderIsomorphisms, SheafOfModules.DifferentialGradedModule.acyclic_isTriangulated, SheafOfModules.DifferentialGradedModule.acyclic_isSaturated, SheafOfModules.DifferentialGradedModule.acyclic_trW_eq_quasiIsomorphisms
statement: formalized
proof: formalized
---

# 24.26 The derived category

Section 24.26 of the Stacks Project, [Tag 0FT1](https://stacks.math.columbia.edu/tag/0FT1). 8 tags here are carried by 25 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FT2, a lemma

[Tag 0FT2](https://stacks.math.columbia.edu/tag/0FT2) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.zerothCohomology_map_eq_of_homotopic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedZerothCohomology.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedZerothCohomology.lean#L61). The attribute's comment: “h0\_factors”.

> Homotopic morphisms of right differential graded modules act identically on zeroth
> cohomology.

```lean
theorem zerothCohomology_map_eq_of_homotopic (A : DifferentialGradedAlgebra.{t, a} R)
    (M N : DifferentialGradedModule.{t, a, m} A) (f g : M ⟶ N) (h : Homotopic f g) :
    (zerothCohomologyFunctor A).map f = (zerothCohomologyFunctor A).map g
```

**`SheafOfModules.DifferentialGradedModule.HomotopyCategory.zerothCohomologyFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedZerothCohomology.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedZerothCohomology.lean#L85). The attribute's comment: “h0\_factors”.

> Zeroth cohomology on the homotopy category of right differential graded modules.

```lean
noncomputable def zerothCohomologyFunctor (A : DifferentialGradedAlgebra.{t, a} R) :
    HomotopyCategory.{t, a, m} A ⥤ SheafOfModules.{m} R
```

**`SheafOfModules.DifferentialGradedModule.HomotopyCategory.zerothCohomologyFunctor_isHomological`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedZerothCohomologyHomological.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedZerothCohomologyHomological.lean#L239). The attribute's comment: “H^0 on the homotopy category is a homological functor”.

> Zeroth cohomology on the homotopy category of right differential graded `A`-modules is a
> homological functor: it takes a distinguished triangle of `K(Mod(A, d))` to an exact sequence of
> sheaves of `O`-modules.

```lean
instance zerothCohomologyFunctor_isHomological :
    (HomotopyCategory.zerothCohomologyFunctor.{u, v, w} A).IsHomological
```

## Tag 0FT3, a lemma

[Tag 0FT3](https://stacks.math.columbia.edu/tag/0FT3) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.acyclic`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAcyclic.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAcyclic.lean#L103). The attribute's comment: “the full subcategory of acyclic modules”.

> **Stacks Project, Tag 0FT3.** The acyclic objects of the homotopy category of right
> differential graded `A`-modules: those whose underlying complex of sheaves of `O`-modules has
> vanishing cohomology in every degree.

```lean
def acyclic : ObjectProperty (HomotopyCategory.{u, v, w} A)
```

**`SheafOfModules.DifferentialGradedModule.acyclic_isClosedUnderIsomorphisms`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAcyclic.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAcyclic.lean#L150). The attribute's comment: “strict fullness”.

> **Stacks Project, Tag 0FT3.** The subcategory of acyclic objects is strictly full: it is the
> homological kernel of a functor, which is closed under isomorphisms.

```lean
instance acyclic_isClosedUnderIsomorphisms :
    (acyclic.{u, v, w} A).IsClosedUnderIsomorphisms
```

**`SheafOfModules.DifferentialGradedModule.acyclic_isTriangulated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAcyclic.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAcyclic.lean#L159). The attribute's comment: “triangulated subcategory”.

> **Stacks Project, Tag 0FT3.** The acyclic objects form a triangulated subcategory of the
> homotopy category: they are the homological kernel of zeroth cohomology, which is a homological
> functor on a triangulated category.

```lean
instance acyclic_isTriangulated : (acyclic.{u, v, w} A).IsTriangulated
```

**`SheafOfModules.DifferentialGradedModule.acyclic_isSaturated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAcyclic.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAcyclic.lean#L168). The attribute's comment: “saturation”.

> **Stacks Project, Tag 0FT3.** The triangulated subcategory of acyclic objects is saturated:
> the homological kernel of a homological functor is stable under retracts, and a direct summand is
> a retract.

```lean
instance acyclic_isSaturated : (acyclic.{u, v, w} A).IsSaturated
```

## Tag 0FT4, a lemma

[Tag 0FT4](https://stacks.math.columbia.edu/tag/0FT4) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.acyclic_trW_eq_quasiIsomorphisms`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedCategoryLocalization.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedCategoryLocalization.lean#L190). The attribute's comment: “Qis is the class of arrows attached to Ac”.

> **Stacks Project, Tag 0FT4.** The quasi-isomorphisms of `K(Mod(A, d))` are exactly the
> arrows whose cone is acyclic, that is, the class of arrows attached to the triangulated
> subcategory `Ac` of acyclic objects.
>
> Both inclusions are read off one distinguished triangle on the given arrow: such a triangle is
> isomorphic to the triangle of an admissible short exact sequence `M → N → P` of right
> differential graded modules, whose underlying sequence of complexes of sheaves of modules is
> short exact, and for a short exact sequence of complexes the first map is a quasi-isomorphism
> exactly when the third term is acyclic.

```lean
theorem acyclic_trW_eq_quasiIsomorphisms :
    (acyclic.{u, v, w} A).trW = quasiIsomorphisms A
```

**`SheafOfModules.DifferentialGradedModule.quasiIsomorphisms_isCompatibleWithTriangulation`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedCategoryTriangulated.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedCategoryTriangulated.lean#L82). The attribute's comment: “Qis is compatible with the triangulation of K(Mod(A,d))”.

> **Stacks Project, Tag 0FT4.** The quasi-isomorphisms are compatible with the triangulation
> of `K(Mod(A, d))`: they are the class of arrows attached to the triangulated subcategory of
> acyclic objects.

```lean
instance quasiIsomorphisms_isCompatibleWithTriangulation :
    (quasiIsomorphisms.{u, v, w} A).IsCompatibleWithTriangulation
```

**`SheafOfModules.DifferentialGradedModule.derivedCategory_isTriangulated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedCategoryTriangulated.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedCategoryTriangulated.lean#L93). The attribute's comment: “D(A,d) is pre-triangulated, and triangulated”.

> **The derived category `D(A, d)` is a triangulated category**, with the images of the
> distinguished triangles of `K(Mod(A, d))` as its distinguished triangles. Its pre-triangulated
> structure is the one Mathlib puts on a localization at a class of morphisms compatible with the
> triangulation, and is found by instance search; stating this makes that search run, since
> `CategoryTheory.IsTriangulated` presupposes it.

```lean
theorem derivedCategory_isTriangulated : IsTriangulated (derivedCategory.{u, v, w} A)
```

**`SheafOfModules.DifferentialGradedModule.quasiIsomorphisms_mem_of_comp_mem_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedQuasiIsomorphisms.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedQuasiIsomorphisms.lean#L79). The attribute's comment: “axiom MS4: saturation of Qis”.

> Axiom MS4, the saturation axiom: an arrow of the homotopy category of right differential
> graded `A`-modules which becomes a quasi-isomorphism after composing with an arrow on either side
> is a quasi-isomorphism already.

```lean
theorem quasiIsomorphisms_mem_of_comp_mem_comp {X Y Z T : HomotopyCategory.{t, a, m} A}
    (φ : X ⟶ Y) (ψ : Y ⟶ Z) (χ : Z ⟶ T)
    (hφψ : quasiIsomorphisms.{t, a, m} A (φ ≫ ψ))
    (hψχ : quasiIsomorphisms.{t, a, m} A (ψ ≫ χ)) :
    quasiIsomorphisms.{t, a, m} A ψ
```

**`SheafOfModules.DifferentialGradedModule.quasiIsomorphisms_iff_isIso_homotopyForget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedQuasiIsomorphisms.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedQuasiIsomorphisms.lean#L140). The attribute's comment: “Qis is the class of arrows inverted by K(A) ⟶ D(R)”.

> An arrow of the homotopy category of right differential graded `A`-modules is a
> quasi-isomorphism exactly when its image under `homotopyForget` is an isomorphism in the derived
> category of sheaves of `R`-modules.

```lean
theorem quasiIsomorphisms_iff_isIso_homotopyForget {X Y : HomotopyCategory.{t, a, m} A}
    (φ : X ⟶ Y) :
    quasiIsomorphisms.{t, a, m} A φ ↔ IsIso ((homotopyForget.{w, t, a, m} A).map φ)
```

**`SheafOfModules.DifferentialGradedModule.quasiIsomorphisms_hasLeftCalculusOfFractions`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedQuasiIsoMultiplicative.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedQuasiIsoMultiplicative.lean#L150). The attribute's comment: “axioms MS2 and MS3: the left calculus of fractions”.

> **Stacks Project, Tag 0FT4.** Axioms MS2 and MS3 for the quasi-isomorphisms of the homotopy
> category of right differential graded `A`-modules, in their left form: the left Ore condition
> and the left cancellation condition, which together with MS1 are a left calculus of
> fractions.

```lean
instance quasiIsomorphisms_hasLeftCalculusOfFractions :
    (quasiIsomorphisms A).HasLeftCalculusOfFractions
```

**`SheafOfModules.DifferentialGradedModule.quasiIsomorphisms_hasRightCalculusOfFractions`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedQuasiIsoMultiplicative.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedQuasiIsoMultiplicative.lean#L159). The attribute's comment: “axioms MS2 and MS3: the right calculus of fractions”.

> **Stacks Project, Tag 0FT4.** Axioms MS2 and MS3 for the quasi-isomorphisms of the homotopy
> category of right differential graded `A`-modules, in their right form: the right Ore condition
> and the right cancellation condition, which together with MS1 are a right calculus of
> fractions.

```lean
instance quasiIsomorphisms_hasRightCalculusOfFractions :
    (quasiIsomorphisms A).HasRightCalculusOfFractions
```

**`SheafOfModules.DifferentialGradedModule.quasiIsomorphisms_isCompatibleWithTriangulation`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedQuasiIsoMultiplicative.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedQuasiIsoMultiplicative.lean#L168). The attribute's comment: “compatibility with the triangulated structure”.

> **Stacks Project, Tag 0FT4.** The quasi-isomorphisms of the homotopy category of right
> differential graded `A`-modules are compatible with its triangulated structure: a morphism of
> distinguished triangles whose first two components are quasi-isomorphisms may be completed by a
> third which is one as well.

```lean
instance quasiIsomorphisms_isCompatibleWithTriangulation :
    (quasiIsomorphisms A).IsCompatibleWithTriangulation
```

**`SheafOfModules.DifferentialGradedModule.quasiIsomorphisms_isSaturated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedQuasiIsoMultiplicative.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedQuasiIsoMultiplicative.lean#L177). The attribute's comment: “Qis is a saturated multiplicative system”.

> **Stacks Project, Tag 0FT4.** The quasi-isomorphisms of the homotopy category of right
> differential graded `A`-modules are a saturated multiplicative system: MS1, the two Ore
> conditions MS2, the two cancellation conditions MS3 and the saturation axiom MS4. Saturation
> comes from that of the subcategory of acyclic objects, Stacks Project Tag 0FT3.

```lean
theorem quasiIsomorphisms_isSaturated : (quasiIsomorphisms A).IsSaturated
```

Declarations registered for the tag:

- [`CategoryTheory.Triangulated.Localization.isTriangulated_functor`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Triangulated.Localization.isTriangulated_functor#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedCategoryTriangulated.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedCategoryTriangulated.lean#L96) (StacksFrontier): “the localization functor is exact”. References: SGA 4½ Etat 0 (2.3.2), “partial”; SGA 4½ Etat 0 (Problem2), “exactness of Q, partial”.
- [`SheafOfModules.DifferentialGradedModule.quasiIsomorphisms`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedCategory.lean#L110), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedQuasiIsomorphisms.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedQuasiIsomorphisms.lean#L45) (StacksFrontier): “the class Qis of quasi-isomorphisms of K(A)”.
- [`SheafOfModules.DifferentialGradedModule.quasiIsomorphisms_quotient_map_iff`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedCategory.lean#L118), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedQuasiIsomorphisms.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedQuasiIsomorphisms.lean#L48) (StacksFrontier): “well-definedness: Qis may be read off any representing morphism”.
- [`SheafOfModules.DifferentialGradedModule.quasiIsomorphisms_isMultiplicative`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedCategory.lean#L128), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedQuasiIsomorphisms.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedQuasiIsomorphisms.lean#L51) (StacksFrontier): “axiom MS1: Qis contains the identities and is stable under composition”.

## Tag 0FT5, a definition

[Tag 0FT5](https://stacks.math.columbia.edu/tag/0FT5) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.derivedCategory`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedCategory.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedCategory.lean#L149).

> The derived category of a sheaf of differential graded algebras `(A, d)`: the localization
> of the homotopy category of right differential graded `A`-modules at the quasi-isomorphisms.

```lean
abbrev derivedCategory (A : DifferentialGradedAlgebra.{t, a} R) : Type _
```

**`SheafOfModules.DifferentialGradedModule.toDerivedCategory`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedCategory.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedCategory.lean#L155). The attribute's comment: “the localization functor”.

> The canonical functor from the homotopy category of right differential graded `A`-modules to
> the derived category of `(A, d)`, which inverts the quasi-isomorphisms.

```lean
abbrev toDerivedCategory (A : DifferentialGradedAlgebra.{t, a} R) :
    HomotopyCategory.{t, a, m} A ⥤ derivedCategory.{t, a, m} A
```

## Tag 0FT6, a lemma

[Tag 0FT6](https://stacks.math.columbia.edu/tag/0FT6) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.toDerivedCategory_kernel_eq_acyclic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedCategoryLocalization.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedCategoryLocalization.lean#L213). The attribute's comment: “ker(Q) = Ac”.

> **Stacks Project, Tag 0FT6.** The kernel of the localization functor
> `Q : K(Mod(A, d)) ⟶ D(A, d)` is the subcategory `Ac` of acyclic right differential graded
> modules: the quasi-isomorphisms are the class of arrows attached to `Ac`, and a strictly full
> saturated triangulated subcategory is recovered as the objects killed by the localization at
> the class of arrows it determines.

```lean
theorem toDerivedCategory_kernel_eq_acyclic :
    (toDerivedCategory.{u, v, w} A).kernel = acyclic.{u, v, w} A
```

## Tag 0FT7, a lemma

[Tag 0FT7](https://stacks.math.columbia.edu/tag/0FT7) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.derivedZerothCohomologyFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedZerothCohomologyDerived.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedZerothCohomologyDerived.lean#L139). The attribute's comment: “the factorization of H^0 through the derived category”.

> Zeroth cohomology on the derived category of `(A, d)`: the factorization of zeroth
> cohomology on the homotopy category through the localization at the quasi-isomorphisms.

```lean
def derivedZerothCohomologyFunctor (A : DifferentialGradedAlgebra.{t, a} R) :
    derivedCategory.{t, a, m} A ⥤ SheafOfModules.{m} R
```

**`SheafOfModules.DifferentialGradedModule.derivedZerothCohomologyFunctorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedZerothCohomologyDerived.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedZerothCohomologyDerived.lean#L147). The attribute's comment: “the factorization of H^0 through the derived category”.

> Zeroth cohomology on the homotopy category is the restriction of zeroth cohomology on the
> derived category along the localization functor.

```lean
def derivedZerothCohomologyFunctorIso (A : DifferentialGradedAlgebra.{t, a} R) :
    toDerivedCategory.{t, a, m} A ⋙ derivedZerothCohomologyFunctor.{t, a, m} A ≅
      HomotopyCategory.zerothCohomologyFunctor.{t, a, m} A
```

**`SheafOfModules.DifferentialGradedModule.derivedZerothCohomologyFunctor_isHomological`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedZerothCohomologyDerivedHomological.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedZerothCohomologyDerivedHomological.lean#L103). The attribute's comment: “H^0 on the derived category is a homological functor”.

> **Stacks Project, Tag 0FT7.** Zeroth cohomology on the derived category of `(A, d)` is a
> homological functor: it takes a distinguished triangle of `D(A, d)` to an exact sequence of
> sheaves of `O`-modules.
>
> Zeroth cohomology on `D(A, d)` restricts along the localization functor to zeroth cohomology on
> `K(Mod(A, d))`, which is homological by tag 0FT2, and that localization functor is exact and
> essentially surjective on arrows.

```lean
instance derivedZerothCohomologyFunctor_isHomological :
    (derivedZerothCohomologyFunctor.{u, v, w} A).IsHomological
```

## Tag 0FT8, a lemma

[Tag 0FT8](https://stacks.math.columbia.edu/tag/0FT8) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.derivedHomEquivHomotopyHomOfKInjective`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedHomKInjective.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedHomKInjective.lean#L94).

> Let `(A, d)` be a sheaf of differential graded algebras on a ringed site, let `M`, `N` be
> right differential graded `A`-modules and let `N ⟶ I` be a quasi-isomorphism into a graded
> injective and K-injective right differential graded module `I`. Then morphisms `M ⟶ N` in
> `D(A, d)` are the homotopy classes of morphisms `M ⟶ I`.

```lean
def derivedHomEquivHomotopyHomOfKInjective {M N I : DifferentialGradedModule.{u, v, w} A}
    (hI : IsKInjective I) (hI' : GradedInjective I) {b : N ⟶ I}
    (hb : QuasiIso b.toHomologicalComplex) :
    ((toDerivedCategory.{u, v, w} A).obj ((HomotopyCategory.quotient A).obj M) ⟶
        (toDerivedCategory.{u, v, w} A).obj ((HomotopyCategory.quotient A).obj N)) ≃
      ((HomotopyCategory.quotient A).obj M ⟶ (HomotopyCategory.quotient A).obj I)
```

**`SheafOfModules.DifferentialGradedModule.derivedHomEquivHomotopyHomOfKInjective_symm_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedHomKInjective.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedHomKInjective.lean#L108). The attribute's comment: “the identification is the one of the source and not an arbitrary bijection: it sends a homotopy class to its image in D(A, d) composed with the inverse of the given quasi-isomorphism”.

> The identification `derivedHomEquivHomotopyHomOfKInjective` sends a homotopy class
> `f : M ⟶ I` to its image in `D(A, d)` composed with the inverse of the given
> quasi-isomorphism.

```lean
theorem derivedHomEquivHomotopyHomOfKInjective_symm_apply
    {M N I : DifferentialGradedModule.{u, v, w} A}
    (hI : IsKInjective I) (hI' : GradedInjective I) {b : N ⟶ I}
    (hb : QuasiIso b.toHomologicalComplex)
    (f : (HomotopyCategory.quotient A).obj M ⟶ (HomotopyCategory.quotient A).obj I) :
    (derivedHomEquivHomotopyHomOfKInjective (M := M) hI hI' hb).symm f =
      (toDerivedCategory.{u, v, w} A).map f ≫ (toDerivedCategoryIso b hb).inv
```

## Tag 0FT9, a lemma

[Tag 0FT9](https://stacks.math.columbia.edu/tag/0FT9) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.derivedCategory_sumsAndProducts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedKInjectiveExistence.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedKInjectiveExistence.lean#L290).

> Let `(C, O)` be a ringed site and let `(A, d)` be a sheaf of differential graded algebras on
> `(C, O)`. Then (1) `D(A, d)` has both direct sums and products, (2) direct sums are obtained by
> taking direct sums of differential graded `A`-modules, (3) products are obtained by taking
> products of K-injective differential graded modules. The four conjuncts are the three parts, in
> order, the third read in two ways:
>
> 1. the derived category has arbitrary products and arbitrary direct sums;
> 2. for every family `M` of right differential graded `A`-modules, the image of the direct sum
>    `∐ M`, with the images of its canonical inclusions, is a direct sum in `D(A, d)`;
> 3. for every family `I` of K-injective right differential graded `A`-modules, the image of the
>    product `∏ᶜ I`, with the images of its canonical projections, is a product in `D(A, d)`;
>    and, for any family `M` with quasi-isomorphisms `s t : M t ⟶ I t` into K-injective modules,
>    the image of `∏ᶜ I`, with its projections followed by the inverses of the images of the
>    `s t`, is a product of the images of the `M t` in `D(A, d)`.
>
> The modules, and the index sets of the families, lie in any universe `max u v w` containing the
> site and the algebra.

```lean
theorem derivedCategory_sumsAndProducts
    (A : DifferentialGradedAlgebra.{u, v} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) :
    (HasProducts.{max u v w} (derivedCategory.{u, v, max u v w} A) ∧
        HasCoproducts.{max u v w} (derivedCategory.{u, v, max u v w} A)) ∧
      (∀ (T : Type max u v w) (M : T → DifferentialGradedModule.{u, v, max u v w} A),
        Nonempty (IsColimit (Cofan.mk
          ((HomotopyCategory.quotient A ⋙ toDerivedCategory.{u, v, max u v w} A).obj (∐ M))
          (fun t => (HomotopyCategory.quotient A ⋙ toDerivedCategory.{u, v, max u v w} A).map
            (Sigma.ι M t))))) ∧
      (∀ (T : Type max u v w) (I : T → DifferentialGradedModule.{u, v, max u v w} A),
        (∀ t, IsKInjective (I t)) →
          Nonempty (IsLimit (Fan.mk
            ((HomotopyCategory.quotient A ⋙ toDerivedCategory.{u, v, max u v w} A).obj (∏ᶜ I))
            (fun t => (HomotopyCategory.quotient A ⋙ toDerivedCategory.{u, v, max u v w} A).map
              (Pi.π I t))))) ∧
      (∀ (T : Type max u v w) (M I : T → DifferentialGradedModule.{u, v, max u v w} A)
        (s : ∀ t, M t ⟶ I t) (qis : ∀ t, QuasiIso (s t).toHomologicalComplex),
        (∀ t, IsKInjective (I t)) →
          Nonempty (IsLimit (Fan.mk
            ((HomotopyCategory.quotient A ⋙ toDerivedCategory.{u, v, max u v w} A).obj (∏ᶜ I))
            (fun t => (HomotopyCategory.quotient A ⋙ toDerivedCategory.{u, v, max u v w} A).map
                (Pi.π I t) ≫
              (Localization.isoOfHom (toDerivedCategory.{u, v, max u v w} A)
                (quasiIsomorphisms.{u, v, max u v w} A)
                ((HomotopyCategory.quotient A).map (s t))
                ((quasiIsomorphisms_quotient_map_iff (s t)).2 (qis t))).inv))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 24.26, Tag 0FT1](https://stacks.math.columbia.edu/tag/0FT1)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
