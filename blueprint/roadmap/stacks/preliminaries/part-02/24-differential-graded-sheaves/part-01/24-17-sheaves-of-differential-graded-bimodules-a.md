---
declaration: section
origin: cited
lean: SheafOfModules.DifferentialGradedBimodule.equivLeftStructure, SheafOfModules.DifferentialGradedAlgebra.asBimodule, SheafOfModules.DifferentialGradedModule.restrictScalars, SheafOfModules.DifferentialGradedAlgebra.Hom.toBimodule, SheafOfModules.DifferentialGradedModule.restrictionObj, SheafOfModules.DifferentialGradedModule.restrictionMap, SheafOfModules.DifferentialGradedModule.restriction, SheafOfModules.DifferentialGradedModule.extensionRestrictionAdjunction
statement: formalized
proof: formalized
---

# 24.17 Sheaves of differential graded bimodules and tensor-hom adjunction

Section 24.17 of the Stacks Project, [Tag 0FRP](https://stacks.math.columbia.edu/tag/0FRP). 4 tags here are carried by 25 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FRP, the section

[Tag 0FRP](https://stacks.math.columbia.edu/tag/0FRP) in the Stacks Project.

**`SheafOfModules.DifferentialGradedBimodule.equivLeftStructure`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedBimoduleStructures.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedBimoduleStructures.lean#L182). The attribute's comment: “a dg (A,B)-bimodule is a right dg B-module with a commuting left dg A-structure”.

> **A differential graded `(A, B)`-bimodule is exactly a right differential graded `B`-module
> which is also a left differential graded `A`-module on the same complex, the two actions
> commuting.**

```lean
def equivLeftStructure (A B : DifferentialGradedAlgebra.{t, a} R) :
    DifferentialGradedBimodule.{t, a, m} A B ≃
      Σ M : DifferentialGradedModule.{t, a, m} B, LeftStructure A M
```

**`SheafOfModules.DifferentialGradedAlgebra.asBimodule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedBimoduleStructures.lean, line 240](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedBimoduleStructures.lean#L240). The attribute's comment: “B as a differential graded (A,B)-bimodule through a homomorphism φ : A ⟶ B”.

> **`{}_A B_B`: a sheaf of differential graded algebras `B` is a differential graded
> `(A, B)`-bimodule** through a unital homomorphism `φ : A ⟶ B`, with `a` acting on the left as
> `φ a` and `B` acting on the right by its own multiplication.

```lean
def asBimodule (φ : A ⟶ B) (hφ : φ.IsUnital) : DifferentialGradedBimodule.{t, a, a} A B
```

**`SheafOfModules.DifferentialGradedModule.restrictScalars`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedBimoduleStructures.lean, line 354](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedBimoduleStructures.lean#L354). The attribute's comment: “restriction res_φ along a homomorphism of sheaves of differential graded algebras”.

> **The restriction functor `res_φ : Mod^dg(B, d) ⥤ Mod^dg(A, d)`** attached to a unital
> homomorphism `φ : A ⟶ B` of sheaves of differential graded algebras.

```lean
def restrictScalars (φ : A ⟶ B) (hφ : φ.IsUnital) :
    DifferentialGradedModule.{t, a, m} B ⥤ DifferentialGradedModule.{t, a, m} A
```

**`SheafOfModules.DifferentialGradedAlgebra.Hom.toBimodule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedRestriction.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedRestriction.lean#L205). The attribute's comment: “the bimodule _A B_B attached to a homomorphism of differential graded algebras”.

> The target of a unit-preserving homomorphism `φ : A ⟶ B` of sheaves of differential graded
> algebras, read as a differential graded `(A, B)`-bimodule `{}_A B_B`: the underlying complex is
> that of `B`, the right action is the multiplication of `B`, and a homogeneous local section `a`
> of `A` acts on the left through `φ(a)`.
>
> This is `SheafOfModules.DifferentialGradedAlgebra.asBimodule`.

```lean
def Hom.toBimodule (φ : A ⟶ B) (hφ : φ.PreservesOne) :
    DifferentialGradedBimodule.{t, a, a} A B
```

**`SheafOfModules.DifferentialGradedModule.restrictionObj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedRestriction.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedRestriction.lean#L245). The attribute's comment: “the restriction functor res_φ on objects”. References: EGA II (2.8.6), “more general”.

> Restriction of scalars of a right differential graded `B`-module along a unit-preserving
> homomorphism `φ : A ⟶ B` of sheaves of differential graded algebras: the underlying cochain
> complex of sheaves of modules is unchanged and a homogeneous local section `a` of `A` acts
> through `φ(a)`.
>
> This is `SheafOfModules.DifferentialGradedModule.restrictScalarsObj`.

```lean
def restrictionObj (φ : A ⟶ B) (hφ : φ.PreservesOne)
    (N : DifferentialGradedModule.{t, a, m} B) : DifferentialGradedModule.{t, a, m} A
```

**`SheafOfModules.DifferentialGradedModule.restrictionMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedRestriction.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedRestriction.lean#L268). The attribute's comment: “the restriction functor res_φ on homomorphisms”.

> Restriction of scalars of a homomorphism of right differential graded `B`-modules: the same
> morphism of underlying cochain complexes.

```lean
def restrictionMap (φ : A ⟶ B) (hφ : φ.PreservesOne)
    {M N : DifferentialGradedModule.{t, a, m} B} (g : M ⟶ N) :
    restrictionObj φ hφ M ⟶ restrictionObj φ hφ N
```

**`SheafOfModules.DifferentialGradedModule.restriction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedRestriction.lean, line 285](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedRestriction.lean#L285). The attribute's comment: “the restriction functor res_φ”.

> **Restriction of scalars** `res_φ : Mod(B, d) ⥤ Mod(A, d)` along a unit-preserving
> homomorphism `φ : A ⟶ B` of sheaves of differential graded algebras.
>
> This is `SheafOfModules.DifferentialGradedModule.restrictScalars`.

```lean
def restriction (φ : A ⟶ B) (hφ : φ.PreservesOne) :
    DifferentialGradedModule.{t, a, m} B ⥤ DifferentialGradedModule.{t, a, m} A
```

**`SheafOfModules.DifferentialGradedModule.extensionRestrictionAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedRestrictionAdjunction.lean, line 836](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedRestrictionAdjunction.lean#L836). The attribute's comment: “base change is left adjoint to res_phi, given a TensorFunctorData of 0FTE”.

> **Extension of scalars is left adjoint to restriction of scalars.** For a unit-preserving
> homomorphism `φ : A ⟶ B` of sheaves of differential graded `R`-algebras and a tensor product
> functor `- ⊗_{A, φ} B` with the bimodule `{}_A B_B`, that functor is left adjoint to `res_φ`.
> This is the adjunction of [Stacks, Tag 0FRP](https://stacks.math.columbia.edu/tag/0FRP).

```lean
def extensionRestrictionAdjunction : D.functor ⊣ restriction.{t, a, m} φ hφ
```

## Tag 0FRQ, a definition

[Tag 0FRQ](https://stacks.math.columbia.edu/tag/0FRQ) in the Stacks Project.

**`SheafOfModules.DifferentialGradedBimodule`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedBimodule.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedBimodule.lean#L65). The attribute's comment: “differential graded bimodules”.

> A differential graded bimodule between two sheaves of differential graded algebras: a
> cochain complex of sheaves of modules with commuting unital left and right actions, each
> obeying the signed Leibniz rule.

```lean
structure DifferentialGradedBimodule (A B : DifferentialGradedAlgebra.{t, a} R)
```

**`SheafOfModules.DifferentialGradedBimodule.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedBimodule.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedBimodule.lean#L119). The attribute's comment: “homomorphisms of differential graded bimodules”.

> A homomorphism of differential graded bimodules: a morphism of the underlying complexes
> compatible with both actions.

```lean
structure Hom (M N : DifferentialGradedBimodule.{t, a, m} A B)
```

## Tag 0FRR, a lemma

[Tag 0FRR](https://stacks.math.columbia.edu/tag/0FRR) in the Stacks Project.

**`SheafOfModules.isEndomorphismAlgebra_endomorphismAlgebraOfIsInternalHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedEndomorphismAlgebra.lean, line 485](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedEndomorphismAlgebra.lean#L485). The attribute's comment: “the differential graded endomorphism algebra”.

> The sheafified differential graded endomorphisms of a right differential graded `B`-module
> `N` carry a differential graded `R`-algebra structure, with composition of local endomorphisms
> as multiplication and the identity as unit.

```lean
noncomputable def isEndomorphismAlgebra_endomorphismAlgebraOfIsInternalHom
    (hH : IsInternalHom N N H) :
    IsEndomorphismAlgebra N (endomorphismAlgebraOfIsInternalHom hH)
```

**`SheafOfModules.bimoduleStructureEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedEndomorphismAlgebra.lean, line 1004](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedEndomorphismAlgebra.lean#L1004). The attribute's comment: “bimodule structures correspond to maps into the endomorphism algebra”.

> Compatible `(A, B)`-bimodule structures on a right differential graded `B`-module `N` are in
> one-to-one correspondence with identity-preserving homomorphisms of sheaves of differential
> graded `R`-algebras `A ⟶ SheafHom^dg_B(N, N)`.

```lean
noncomputable def bimoduleStructureEquiv (hE : IsEndomorphismAlgebra N E) :
    BimoduleStructure A N ≃ UnitalHom A E
```

**`SheafOfModules.bimoduleStructureEquiv_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedEndomorphismAlgebra.lean, line 1016](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedEndomorphismAlgebra.lean#L1016). The attribute's comment: “bimodule structures correspond to maps into the endomorphism algebra”.

> The correspondence between compatible bimodule structures and identity-preserving
> homomorphisms into the endomorphism algebra is pinned down by the requirement that the
> homomorphism attached to a structure act on local sections of `N` by left multiplication for
> that structure.

```lean
theorem bimoduleStructureEquiv_app (hE : IsEndomorphismAlgebra N E) (s : BimoduleStructure A N)
    (n i j : ℤ) (hij : i + n = j) (U : C) (V : Over U)
    (a : (A.complex.X n).val.obj (Opposite.op U))
    (x : (N.complex.X i).val.obj (Opposite.op V.left)) :
    HEq ((hE.isInternalHom.sectionsEquiv n U
        (((bimoduleStructureEquiv hE s).toHom.toHomologicalComplex.f n).val.app
          (Opposite.op U) a)).app i j hij V x)
      ((s.leftMul n i).app (Opposite.op V.left) ((A.complex.X n).val.map V.hom.op a) x)
```

## Tag 0FRS, a lemma

[Tag 0FRS](https://stacks.math.columbia.edu/tag/0FRS) in the Stacks Project.

**`SheafOfModules.isInternalHom_tensor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedTensorHomAdjunction.lean, line 787](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedTensorHomAdjunction.lean#L787). The attribute's comment: “SheafHom^dg_B(M ⊗_A N, L) = SheafHom^dg_A(M, SheafHom^dg_B(N, L))”.

> **Tensor-hom adjunction for sheaves of differential graded modules**, second identity: a
> complex of sheaves of `R`-modules which is the internal hom `SheafHom^dg_B(M ⊗_A N, L)` is also
> the internal hom `SheafHom^dg_A(M, SheafHom^dg_B(N, L))`, differentials included.

```lean
noncomputable def isInternalHom_tensor (hT : IsTensorProduct M N T)
    (hH : IsSheafHom N L H) (hG : IsInternalHom T L G) :
    IsInternalHom M H G
```

**`SheafOfModules.tensorSectionsEquiv_naturality_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedTensorHomAdjunction.lean, line 841](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedTensorHomAdjunction.lean#L841). The attribute's comment: “functoriality of the internal-hom identity in M, on local sections”.

> **Tensor-hom adjunction for sheaves of differential graded modules**, second identity,
> functoriality in `M`: a morphism `u : M' ⟶ M` of right differential graded `A`-modules induces
> `t : M' ⊗_A N ⟶ M ⊗_A N` and hence `α : SheafHom^dg_B(M ⊗_A N, L) ⟶ SheafHom^dg_B(M' ⊗_A N, L)`,
> and `α` is also the map that the second identity attaches to `u`, namely precomposition with
> `u` on `SheafHom^dg_A(M, SheafHom^dg_B(N, L))`.

```lean
theorem tensorSectionsEquiv_naturality_left (hT : IsTensorProduct M N T)
    (hT' : IsTensorProduct M' N T') (hH : IsSheafHom N L H) (hG : IsInternalHom T L G)
    (hG' : IsInternalHom T' L G') (u : M' ⟶ M) (t : T' ⟶ T) (α : G ⟶ G')
    (ht : ∀ (i j : ℤ) (U : Cᵒᵖ) (x : (M'.complex.X i).val.obj U)
      (y : (N.complex.X j).val.obj U),
      (t.toHomologicalComplex.f (i + j)).val.app U (hT'.tmul i j U x y) =
        hT.tmul i j U ((u.toHomologicalComplex.f i).val.app U x) y)
    (hα : ∀ (n : ℤ) (U : C) (p : (G.X n).val.obj (Opposite.op U)) (i j : ℤ) (hij : i + n = j)
      (V : Over U) (x : (T'.complex.X i).val.obj (Opposite.op V.left)),
      (hG'.sectionsEquiv n U ((α.f n).val.app (Opposite.op U) p)).app i j hij V x =
        (hG.sectionsEquiv n U p).app i j hij V
          ((t.toHomologicalComplex.f i).val.app (Opposite.op V.left) x))
    (n : ℤ) (U : C) (p : (G.X n).val.obj (Opposite.op U)) (i j : ℤ) (hij : i + n = j)
    (V : Over U) (x : (M'.complex.X i).val.obj (Opposite.op V.left)) :
    (tensorSectionsEquiv hT' hH hG' n U ((α.f n).val.app (Opposite.op U) p)).app i j hij V x =
      (tensorSectionsEquiv hT hH hG n U p).app i j hij V
        ((u.toHomologicalComplex.f i).val.app (Opposite.op V.left) x)
```

**`SheafOfModules.tensorSectionsEquiv_naturality_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedTensorHomAdjunction.lean, line 877](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedTensorHomAdjunction.lean#L877). The attribute's comment: “functoriality of the internal-hom identity in L, on local sections”.

> **Tensor-hom adjunction for sheaves of differential graded modules**, second identity,
> functoriality in `L`: a morphism `k : L ⟶ L'` of right differential graded `B`-modules induces
> `α : SheafHom^dg_B(M ⊗_A N, L) ⟶ SheafHom^dg_B(M ⊗_A N, L')` and
> `g : SheafHom^dg_B(N, L) ⟶ SheafHom^dg_B(N, L')`, and under the second identity `α` is
> postcomposition with `g`.

```lean
theorem tensorSectionsEquiv_naturality_right (hT : IsTensorProduct M N T)
    (hH : IsSheafHom N L H) (hH' : IsSheafHom N L' H') (hG : IsInternalHom T L G)
    (hG' : IsInternalHom T L' G') (k : L ⟶ L') (g : H ⟶ H') (α : G ⟶ G')
    (hg : ∀ (m : ℤ) (U : C) (q : (H.complex.X m).val.obj (Opposite.op U)) (i j : ℤ)
      (hij : i + m = j) (V : Over U)
      (y : (N.complex.X i).val.obj (Opposite.op V.left)),
      (hH'.isInternalHom.sectionsEquiv m U
          ((g.toHomologicalComplex.f m).val.app (Opposite.op U) q)).app i j hij V y =
        (k.toHomologicalComplex.f j).val.app (Opposite.op V.left)
          ((hH.isInternalHom.sectionsEquiv m U q).app i j hij V y))
    (hα : ∀ (n : ℤ) (U : C) (p : (G.X n).val.obj (Opposite.op U)) (i j : ℤ) (hij : i + n = j)
      (V : Over U) (x : (T.complex.X i).val.obj (Opposite.op V.left)),
      (hG'.sectionsEquiv n U ((α.f n).val.app (Opposite.op U) p)).app i j hij V x =
        (k.toHomologicalComplex.f j).val.app (Opposite.op V.left)
          ((hG.sectionsEquiv n U p).app i j hij V x))
    (n : ℤ) (U : C) (p : (G.X n).val.obj (Opposite.op U)) (i j : ℤ) (hij : i + n = j)
    (V : Over U) (x : (M.complex.X i).val.obj (Opposite.op V.left)) :
    (tensorSectionsEquiv hT hH' hG' n U ((α.f n).val.app (Opposite.op U) p)).app i j hij V x =
      (g.toHomologicalComplex.f j).val.app (Opposite.op V.left)
        ((tensorSectionsEquiv hT hH hG n U p).app i j hij V x)
```

**`SheafOfModules.tensorSectionsEquiv_naturality_bimodule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedTensorHomAdjunction.lean, line 910](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedTensorHomAdjunction.lean#L910). The attribute's comment: “functoriality of the internal-hom identity in N, on local sections”.

> **Tensor-hom adjunction for sheaves of differential graded modules**, second identity,
> functoriality in `N`: a morphism `σ : N ⟶ N'` of differential graded `(A, B)`-bimodules induces
> `t : M ⊗_A N ⟶ M ⊗_A N'`, hence `α : SheafHom^dg_B(M ⊗_A N', L) ⟶ SheafHom^dg_B(M ⊗_A N, L)`,
> and `g : SheafHom^dg_B(N', L) ⟶ SheafHom^dg_B(N, L)`; under the second identity `α` is
> postcomposition with `g`.

```lean
theorem tensorSectionsEquiv_naturality_bimodule (hT : IsTensorProduct M N T)
    (hT' : IsTensorProduct M N' T') (hH : IsSheafHom N L H) (hH' : IsSheafHom N' L H')
    (hG : IsInternalHom T L G) (hG' : IsInternalHom T' L G')
    (σ : N ⟶ N') (t : T ⟶ T') (g : H' ⟶ H) (α : G' ⟶ G)
    (ht : ∀ (i j : ℤ) (U : Cᵒᵖ) (x : (M.complex.X i).val.obj U)
      (y : (N.complex.X j).val.obj U),
      (t.toHomologicalComplex.f (i + j)).val.app U (hT.tmul i j U x y) =
        hT'.tmul i j U x ((σ.toHomologicalComplex.f j).val.app U y))
    (hg : ∀ (m : ℤ) (U : C) (q : (H'.complex.X m).val.obj (Opposite.op U)) (i j : ℤ)
      (hij : i + m = j) (V : Over U)
      (y : (N.complex.X i).val.obj (Opposite.op V.left)),
      (hH.isInternalHom.sectionsEquiv m U
          ((g.toHomologicalComplex.f m).val.app (Opposite.op U) q)).app i j hij V y =
        (hH'.isInternalHom.sectionsEquiv m U q).app i j hij V
          ((σ.toHomologicalComplex.f i).val.app (Opposite.op V.left) y))
    (hα : ∀ (n : ℤ) (U : C) (p : (G'.X n).val.obj (Opposite.op U)) (i j : ℤ) (hij : i + n = j)
      (V : Over U) (x : (T.complex.X i).val.obj (Opposite.op V.left)),
      (hG.sectionsEquiv n U ((α.f n).val.app (Opposite.op U) p)).app i j hij V x =
        (hG'.sectionsEquiv n U p).app i j hij V
          ((t.toHomologicalComplex.f i).val.app (Opposite.op V.left) x))
    (n : ℤ) (U : C) (p : (G'.X n).val.obj (Opposite.op U)) (i j : ℤ) (hij : i + n = j)
    (V : Over U) (x : (M.complex.X i).val.obj (Opposite.op V.left)) :
    (tensorSectionsEquiv hT hH hG n U ((α.f n).val.app (Opposite.op U) p)).app i j hij V x =
      (g.toHomologicalComplex.f j).val.app (Opposite.op V.left)
        ((tensorSectionsEquiv hT' hH' hG' n U p).app i j hij V x)
```

**`SheafOfModules.DifferentialGradedModule.tensorHomHomogeneousEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedTensorHomHomComplex.lean, line 328](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedTensorHomHomComplex.lean#L328). The attribute's comment: “Hom_{Mod^dg(B, d)}(M ⊗_A N, L) = Hom_{Mod^dg(A, d)}(M, SheafHom^dg_B(N, L)) as hom-complexes: degreewise, additively, and compatibly with the differentials”.

> **Tensor-hom adjunction for sheaves of differential graded modules**, first identity, in a
> fixed degree: the degree-`n` homogeneous right-linear maps `M ⊗_A N → L` of right differential
> graded `B`-modules are the degree-`n` homogeneous right-linear maps
> `M → SheafHom^dg_B(N, L)` of right differential graded `A`-modules.

```lean
noncomputable def tensorHomHomogeneousEquiv (hT : IsTensorProduct M N T) (hH : IsSheafHom N L H)
    (n : ℤ) : HomogeneousMap B T L n ≃ HomogeneousMap A M H n
```

**`SheafOfModules.DifferentialGradedModule.homogeneousEquiv_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedTensorHomHomComplex.lean, line 420](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedTensorHomHomComplex.lean#L420). The attribute's comment: “Hom_{Mod^dg(B, d)}(M ⊗_A N, L) = Hom_{Mod^dg(A, d)}(M, SheafHom^dg_B(N, L)) as hom-complexes: degreewise, additively, and compatibly with the differentials”.

> **Tensor-hom adjunction for sheaves of differential graded modules**, first identity, on
> the additions: the identification of the homogeneous morphisms is additive, so each degree of
> the two hom-complexes is identified as an abelian group.

```lean
theorem homogeneousEquiv_add (hT : IsTensorProduct M N T) (hH : IsSheafHom N L H) (n : ℤ)
    (φ φ' χ : HomogeneousMap B T L n) (hχ : χ.val = φ.val + φ'.val) :
    (tensorHomHomogeneousEquiv hT hH n χ).val =
      (tensorHomHomogeneousEquiv hT hH n φ).val + (tensorHomHomogeneousEquiv hT hH n φ').val
```

**`SheafOfModules.DifferentialGradedModule.homogeneousEquiv_delta`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedTensorHomHomComplex.lean, line 438](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedTensorHomHomComplex.lean#L438). The attribute's comment: “Hom_{Mod^dg(B, d)}(M ⊗_A N, L) = Hom_{Mod^dg(A, d)}(M, SheafHom^dg_B(N, L)) as hom-complexes: degreewise, additively, and compatibly with the differentials”.

> **Tensor-hom adjunction for sheaves of differential graded modules**, first identity, on
> the differentials: the identification of the homogeneous morphisms commutes with the commutator
> differential of the two hom-complexes.

```lean
theorem homogeneousEquiv_delta (hT : IsTensorProduct M N T) (hH : IsSheafHom N L H) (n : ℤ)
    (φ : HomogeneousMap B T L n) (ψ : HomogeneousMap B T L (n + 1))
    (hψ : ψ.val = δ n (n + 1) φ.val) :
    (tensorHomHomogeneousEquiv hT hH (n + 1) ψ).val =
      δ n (n + 1) (tensorHomHomogeneousEquiv hT hH n φ).val
```

**`SheafOfModules.DifferentialGradedModule.dgHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedTensorHomHomComplex.lean, line 490](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedTensorHomHomComplex.lean#L490). The attribute's comment: “Hom_{Mod^dg(B, d)}(M ⊗_A N, L) = Hom_{Mod^dg(A, d)}(M, SheafHom^dg_B(N, L)) as hom-complexes: degreewise, additively, and compatibly with the differentials”.

> **Tensor-hom adjunction for sheaves of differential graded modules**, first identity: the
> degree-`n` homogeneous morphisms `M ⊗_A N → L` of the differential graded category
> `Mod^dg(B, d)` are the degree-`n` homogeneous morphisms `M → SheafHom^dg_B(N, L)` of the
> differential graded category `Mod^dg(A, d)`.

```lean
noncomputable def dgHomEquiv (hT : IsTensorProduct M N T) (hH : IsSheafHom N L H) (n : ℤ) :
    (dgCategoryData B).category.Hom (moduleObject B (dgCategoryData B) T)
        (moduleObject B (dgCategoryData B) L) n ≃
      (dgCategoryData A).category.Hom (moduleObject A (dgCategoryData A) M)
        (moduleObject A (dgCategoryData A) H) n
```

**`SheafOfModules.DifferentialGradedModule.dgHomEquiv_d`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedTensorHomHomComplex.lean, line 503](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedTensorHomHomComplex.lean#L503). The attribute's comment: “Hom_{Mod^dg(B, d)}(M ⊗_A N, L) = Hom_{Mod^dg(A, d)}(M, SheafHom^dg_B(N, L)) as hom-complexes: degreewise, additively, and compatibly with the differentials”.

> **Tensor-hom adjunction for sheaves of differential graded modules**, first identity: the
> identification of the two hom-complexes commutes with their differentials, so it is an equality
> of complexes and not only of their degreewise components.

```lean
theorem dgHomEquiv_d (hT : IsTensorProduct M N T) (hH : IsSheafHom N L H) (n : ℤ)
    (f : (dgCategoryData B).category.Hom (moduleObject B (dgCategoryData B) T)
      (moduleObject B (dgCategoryData B) L) n) :
    (dgCategoryData A).category.d (dgHomEquiv hT hH n f) =
      dgHomEquiv hT hH (n + 1) ((dgCategoryData B).category.d f)
```

**`SheafOfModules.DifferentialGradedModule.homogeneousEquiv_naturality_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedTensorHomHomComplex.lean, line 535](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedTensorHomHomComplex.lean#L535). The attribute's comment: “functoriality of the hom-complex identity in M: a morphism M' ⟶ M compatible with the tensor products carries the identification at M to the one at M'”.

> **Tensor-hom adjunction for sheaves of differential graded modules**, first identity,
> functoriality in `M`: a morphism `u : M' ⟶ M` of right differential graded `A`-modules induces
> `t : M' ⊗_A N ⟶ M ⊗_A N`, and the identification of the hom-complexes carries precomposition
> with `t` to precomposition with `u`.

```lean
theorem homogeneousEquiv_naturality_left (hT : IsTensorProduct M N T)
    (hT' : IsTensorProduct M' N T') (hH : IsSheafHom N L H) (u : M' ⟶ M) (t : T' ⟶ T)
    (ht : ∀ (i j : ℤ) (U : X.Cᵒᵖ) (x : (M'.complex.X i).val.obj U)
      (y : (N.complex.X j).val.obj U),
      (t.toHomologicalComplex.f (i + j)).val.app U (hT'.tmul i j U x y) =
        hT.tmul i j U ((u.toHomologicalComplex.f i).val.app U x) y)
    (n : ℤ) (φ : HomogeneousMap B T L n) (φ' : HomogeneousMap B T' L n)
    (hφ' : φ'.val = (Cochain.ofHom t.toHomologicalComplex).comp φ.val (zero_add n)) :
    (tensorHomHomogeneousEquiv hT' hH n φ').val =
      (Cochain.ofHom u.toHomologicalComplex).comp
        (tensorHomHomogeneousEquiv hT hH n φ).val (zero_add n)
```

**`SheafOfModules.DifferentialGradedModule.homogeneousEquiv_naturality_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedTensorHomHomComplex.lean, line 567](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedTensorHomHomComplex.lean#L567). The attribute's comment: “functoriality of the hom-complex identity in L: a morphism L ⟶ L', with the induced map of internal homs, commutes with the identification”.

> **Tensor-hom adjunction for sheaves of differential graded modules**, first identity,
> functoriality in `L`: a morphism `k : L ⟶ L'` of right differential graded `B`-modules induces
> `g : SheafHom^dg_B(N, L) ⟶ SheafHom^dg_B(N, L')`, and the identification of the hom-complexes
> carries postcomposition with `k` to postcomposition with `g`.

```lean
theorem homogeneousEquiv_naturality_right (hT : IsTensorProduct M N T)
    (hH : IsSheafHom N L H) (hH' : IsSheafHom N L' H') (k : L ⟶ L') (g : H ⟶ H')
    (hg : ∀ (m : ℤ) (U : X.C) (p : (H.complex.X m).val.obj (Opposite.op U)) (i j : ℤ)
      (hij : i + m = j) (V : Over U) (y : (N.complex.X i).val.obj (Opposite.op V.left)),
      (hH'.isInternalHom.sectionsEquiv m U
          ((g.toHomologicalComplex.f m).val.app (Opposite.op U) p)).app i j hij V y =
        (k.toHomologicalComplex.f j).val.app (Opposite.op V.left)
          ((hH.isInternalHom.sectionsEquiv m U p).app i j hij V y))
    (n : ℤ) (φ : HomogeneousMap B T L n) (φ' : HomogeneousMap B T L' n)
    (hφ' : φ'.val = φ.val.comp (Cochain.ofHom k.toHomologicalComplex) (add_zero n)) :
    (tensorHomHomogeneousEquiv hT hH' n φ').val =
      (tensorHomHomogeneousEquiv hT hH n φ).val.comp
        (Cochain.ofHom g.toHomologicalComplex) (add_zero n)
```

**`SheafOfModules.DifferentialGradedModule.homogeneousEquiv_naturality_bimodule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedTensorHomHomComplex.lean, line 596](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedTensorHomHomComplex.lean#L596). The attribute's comment: “functoriality of the hom-complex identity in N: a morphism N ⟶ N' of bimodules, compatible with the tensor products and the internal homs, commutes with the identification”.

> **Tensor-hom adjunction for sheaves of differential graded modules**, first identity,
> functoriality in `N`: a morphism `σ : N ⟶ N'` of differential graded `(A, B)`-bimodules induces
> `t : M ⊗_A N ⟶ M ⊗_A N'` and `g : SheafHom^dg_B(N', L) ⟶ SheafHom^dg_B(N, L)`, and the
> identification of the hom-complexes carries precomposition with `t` to postcomposition with
> `g`.

```lean
theorem homogeneousEquiv_naturality_bimodule (hT : IsTensorProduct M N T)
    (hT' : IsTensorProduct M N' T') (hH : IsSheafHom N L H) (hH' : IsSheafHom N' L H')
    (σ : N ⟶ N') (t : T ⟶ T') (g : H' ⟶ H)
    (ht : ∀ (i j : ℤ) (U : X.Cᵒᵖ) (x : (M.complex.X i).val.obj U)
      (y : (N.complex.X j).val.obj U),
      (t.toHomologicalComplex.f (i + j)).val.app U (hT.tmul i j U x y) =
        hT'.tmul i j U x ((σ.toHomologicalComplex.f j).val.app U y))
    (hg : ∀ (m : ℤ) (U : X.C) (p : (H'.complex.X m).val.obj (Opposite.op U)) (i j : ℤ)
      (hij : i + m = j) (V : Over U) (y : (N.complex.X i).val.obj (Opposite.op V.left)),
      (hH.isInternalHom.sectionsEquiv m U
          ((g.toHomologicalComplex.f m).val.app (Opposite.op U) p)).app i j hij V y =
        (hH'.isInternalHom.sectionsEquiv m U p).app i j hij V
          ((σ.toHomologicalComplex.f i).val.app (Opposite.op V.left) y))
    (n : ℤ) (φ : HomogeneousMap B T L n) (φ' : HomogeneousMap B T' L n)
    (hφ : φ.val = (Cochain.ofHom t.toHomologicalComplex).comp φ'.val (zero_add n)) :
    (tensorHomHomogeneousEquiv hT hH n φ).val =
      (tensorHomHomogeneousEquiv hT' hH' n φ').val.comp
        (Cochain.ofHom g.toHomologicalComplex) (add_zero n)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 24.17, Tag 0FRP](https://stacks.math.columbia.edu/tag/0FRP)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
