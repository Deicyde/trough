---
declaration: section
origin: cited
lean: exists_free_resolution, exists_finite_free_resolution, CategoryTheory.ObjectProperty.LeftResolution, ModuleResolution, FreeModuleResolution, FiniteFreeModuleResolution, Homotopy.homologyMap_eq, exists_lift_along_resolution
statement: formalized
proof: formalized
---

# 10.71 Ext groups

Section 10.71 of the Stacks Project, [Tag 00LO](https://stacks.math.columbia.edu/tag/00LO). 9 tags here are carried by 11 declarations of the repository (all in StacksFrontier) and 15 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00LP, a lemma

[Tag 00LP](https://stacks.math.columbia.edu/tag/00LP) in the Stacks Project.

**`exists_free_resolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Resolution/Existence.lean, line 278](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/Resolution/Existence.lean#L278). The attribute's comment: “(1)”.

> **(Existence of a free resolution.)** For any commutative ring `R` and any
> `R`-module `M`, there exists an exact complex of `R`-modules
> `... → F₂ → F₁ → F₀ → M → 0` in which every `Fᵢ` is free.

```lean
theorem exists_free_resolution
    (R : Type u) [CommRing R] (M : Type u) [AddCommGroup M] [Module R M] :
    ∃ P : FreeResolutionData R M, P.IsExact ∧ P.IsFree
```

**`exists_finite_free_resolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Resolution/Existence.lean, line 294](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/Resolution/Existence.lean#L294). The attribute's comment: “(2)”. References: EGA 0 (11.9.2), “special case”; EGA IV (12.3.2), “(i), special case”; SGA 2 VIII (1.2), “partial”; SGA 4 IX (2.3), “partial”; SGA 6 VI (1.6), “partial”.

> **(Finite free resolution in the Noetherian finite case.)** If `R` is a Noetherian
> commutative ring and `M` is a finite `R`-module, then there exists an exact complex of
> `R`-modules `... → F₂ → F₁ → F₀ → M → 0` in which every `Fᵢ` is finite free.

```lean
theorem exists_finite_free_resolution
    (R : Type u) [CommRing R] [IsNoetherianRing R]
    (M : Type u) [AddCommGroup M] [Module R M] [Module.Finite R M] :
    ∃ P : FreeResolutionData R M, P.IsExact ∧ P.IsFiniteFree
```

## Tag 00LQ, a definition

[Tag 00LQ](https://stacks.math.columbia.edu/tag/00LQ) in the Stacks Project.

**`CategoryTheory.ObjectProperty.LeftResolution`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Resolution/Defs/Comparison.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/Resolution/Defs/Comparison.lean#L95).

> A `P.LeftResolution Z` consists of a bundled `ℕ`-indexed chain complex whose terms lie in the
> class `P`, along with a quasi-isomorphism to the complex consisting of just `Z` supported in
> degree `0`; equivalently, an exact complex `… → F₁ → F₀ → Z → 0` with all `Fᵢ` in `P`.

```lean
public structure LeftResolution (P : ObjectProperty C) (Z : C)
```

**`ModuleResolution`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Resolution/Defs/Comparison.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/Resolution/Defs/Comparison.lean#L131). The attribute's comment: “resolution”. References: SGA 4½ Etat 0 (3.1.8), “special case”.

> A (left) *resolution* `F_• → M` of an `R`-module `M`: an exact chain complex
> `… → F₂ → F₁ → F₀ → M → 0` of `R`-modules, encoded as an ℕ-indexed chain
> complex together with a quasi-isomorphism to `M` in degree `0`.

```lean
structure ModuleResolution (R : Type u) [Ring R] (M : Type v)
    [AddCommGroup M] [Module R M]
```

**`FreeModuleResolution`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Resolution/Defs/Comparison.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/Resolution/Defs/Comparison.lean#L146). The attribute's comment: “free resolution”. References: EGA 0 (11.4.1).

> A *resolution of `M` by free `R`-modules*: a resolution `F_• → M` such that
> every `F_i` is a free `R`-module.

```lean
structure FreeModuleResolution (R : Type u) [Ring R] (M : Type v)
    [AddCommGroup M] [Module R M] extends ModuleResolution R M
```

**`FiniteFreeModuleResolution`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Resolution/Defs/Comparison.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/Resolution/Defs/Comparison.lean#L154). The attribute's comment: “finite free resolution”.

> A *resolution of `M` by finite free `R`-modules*: a resolution `F_• → M`
> such that every `F_i` is a free and finitely generated `R`-module.

```lean
structure FiniteFreeModuleResolution (R : Type u) [Ring R] (M : Type v)
    [AddCommGroup M] [Module R M] extends FreeModuleResolution R M
```

## Tag 00LR, a lemma

[Tag 00LR](https://stacks.math.columbia.edu/tag/00LR) in the Stacks Project.

Declarations registered for the tag:

- [`Homotopy.homologyMap_eq`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Homotopy.homologyMap_eq#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Homology/Resolution/Comparison.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/Resolution/Comparison.lean#L230) (StacksFrontier): “Stated for complexes in any preadditive category.”. References: EGA 0 (11.2.3), “abutment clause”; SGA 4½ Etat 0 (1.3.2), “partial”.

## Tag 00LS, a lemma

[Tag 00LS](https://stacks.math.columbia.edu/tag/00LS) in the Stacks Project.

**`exists_lift_along_resolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Resolution/Comparison.lean, line 372](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/Resolution/Comparison.lean#L372). The attribute's comment: “(1)”.

> **Statement (1): Existence of a lift.** Let `φ : M → N` be a map of `R`-modules, let
> `C` be an (arbitrary) resolution of `N`, and let `F` be a complex over `M` whose terms are
> all free `R`-modules. Then there exists a map of complexes `α : F → C` lifting `φ`.

```lean
theorem exists_lift_along_resolution {M N : Type*} [AddCommGroup M] [Module R M] [AddCommGroup N]
    [Module R N]
    (φ : M →ₗ[R] N) (F : ComplexOver R M) (C : ComplexOver R N)
    (hC : IsResolution C) (hF : IsFreeComplex F) :
    ∃ α : ∀ i, F.obj i →ₗ[R] C.obj i, IsLift φ F C α
```

**`lift_unique_up_to_homotopy`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Resolution/Comparison.lean, line 412](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/Resolution/Comparison.lean#L412). The attribute's comment: “(2)”. References: EGA III (6.3.8), “partial”.

> **Statement (2): Uniqueness up to homotopy.** Any two maps of complexes `α, β : F → C`
> lifting the same `φ` are chain homotopic.

```lean
theorem lift_unique_up_to_homotopy {M N : Type*} [AddCommGroup M] [Module R M]
    [AddCommGroup N] [Module R N]
    (φ : M →ₗ[R] N) (F : ComplexOver R M) (C : ComplexOver R N)
    (hC : IsResolution C) (hF : IsFreeComplex F)
    (α β : ∀ i, F.obj i →ₗ[R] C.obj i)
    (hα : IsLift φ F C α) (hβ : IsLift φ F C β) :
    HomotopicComplexOver F C α β
```

## Tag 00LT, a lemma

[Tag 00LT](https://stacks.math.columbia.edu/tag/00LT) in the Stacks Project.

**`ModuleCat.homologyMap_linearYoneda_eq_and_isIso_and_eq_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Resolution/Comparison.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/Resolution/Comparison.lean#L192). The attribute's comment: “A free resolution is an `ObjectProperty.LeftResolution` for the class of free modules (00LQ) and `Hom_R(F_•, N)` is the image of `F_•` under `(linearYoneda R (ModuleCat R)).obj N`, so `H^i(α)` is a `homologyMap`. The source's display has the two cohomology groups interchanged, since `Hom_R(-, N)` is contravariant; see the module docstring.”.

> **Stacks 00LT.** Let `R` be a ring, let `M₁`, `M₂`, `N` be `R`-modules, let `F` be a free
> resolution of `M₁`, let `G` be a free resolution of `M₂`, let `φ : M₁ → M₂` be a module map and
> let `α : F_• → G_•` be a map of complexes inducing `φ`. Then, for every `i`, the map
> `H^i(α) : H^i(Hom_R(G_•, N)) → H^i(Hom_R(F_•, N))` is independent of the choice of `α`; it is an
> isomorphism if `φ` is one; and a map `F_• → F_•` inducing the identity of `M₁` induces the
> identity on `H^i(Hom_R(F_•, N))`.

```lean
public theorem homologyMap_linearYoneda_eq_and_isIso_and_eq_id {R : Type u} [CommRing R]
    {M₁ M₂ : ModuleCat.{v} R} (N : ModuleCat.{v} R)
    (F : ObjectProperty.LeftResolution (fun P : ModuleCat.{v} R => Module.Free R P) M₁)
    (G : ObjectProperty.LeftResolution (fun P : ModuleCat.{v} R => Module.Free R P) M₂)
    (φ : M₁ ⟶ M₂) (α : F.complex ⟶ G.complex)
    (hα : α ≫ G.π = F.π ≫ (ChainComplex.single₀ (ModuleCat.{v} R)).map φ) (i : ℕ) :
    (∀ β : F.complex ⟶ G.complex,
        β ≫ G.π = F.π ≫ (ChainComplex.single₀ (ModuleCat.{v} R)).map φ →
        homologyMap ((opFunctor _ _ ⋙
            ((linearYoneda R (ModuleCat.{v} R)).obj N).mapHomologicalComplex _).map β.op) i =
          homologyMap ((opFunctor _ _ ⋙
            ((linearYoneda R (ModuleCat.{v} R)).obj N).mapHomologicalComplex _).map α.op) i) ∧
      (IsIso φ → IsIso (homologyMap ((opFunctor _ _ ⋙
          ((linearYoneda R (ModuleCat.{v} R)).obj N).mapHomologicalComplex _).map α.op) i)) ∧
      (∀ γ : F.complex ⟶ F.complex, γ ≫ F.π = F.π →
        homologyMap ((opFunctor _ _ ⋙
          ((linearYoneda R (ModuleCat.{v} R)).obj N).mapHomologicalComplex _).map γ.op) i
            = 𝟙 _)
```

## Tag 00LU, a lemma

[Tag 00LU](https://stacks.math.columbia.edu/tag/00LU) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Abelian.Ext.covariantSequence_exact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Abelian.Ext.covariantSequence_exact#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L225) (StacksFrontier): “exactness of Ext^n0 -> ... -> Ext^n1 window (whole long exact sequence for n0+1=n1)”. References: SGA 3 XV (2.10), “more general”; SGA 4 V (6.2), “Exactness of (6.2.1)”; SGA 4½ Etat 0 (1.1.2), “special case”; SGA 4½ Etat 0 (3.2.2), “special case”; SGA 7 VII (3.3.6), “partial”; SGA 7 VII (3.7.5), “special case”.
- [`CategoryTheory.Abelian.Ext.covariantSequence`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Abelian.Ext.covariantSequence#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L227) (StacksFrontier): “the long exact sequence (as composable arrows)”. References: SGA 4 V (6.2); SGA 7 VII (3.7.5).
- [`CategoryTheory.Abelian.Ext.covariant_sequence_exact₂'`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Abelian.Ext.covariant_sequence_exact₂'#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L229) (StacksFrontier): “exactness at Ext^n(M,N)”. References: SGA 3 XV (2.10), “more general”; SGA 7 VII (3.3.6), “Exactness at Extⁿ(L•,A)”.
- [`CategoryTheory.Abelian.Ext.covariant_sequence_exact₃'`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Abelian.Ext.covariant_sequence_exact₃'#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L230) (StacksFrontier): “exactness at Ext^n(M,N'')”. References: SGA 4 V (6.2), “partial”; SGA 4½ Etat 0 (1.1.2), “special case”; SGA 7 VII (3.3.6), “Exactness at Extⁿ(L•,A″)”; SGA 7 VII (3.7.5), “Exactness at Ext^n(P”.
- [`CategoryTheory.Abelian.Ext.covariant_sequence_exact₁'`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Abelian.Ext.covariant_sequence_exact₁'#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L231) (StacksFrontier): “exactness at Ext^(n+1)(M,N')”. References: SGA 4 V (6.2), “partial”; SGA 4½ Etat 0 (1.1.2), “special case”; SGA 4½ Etat 0 (3.2.2), “Exactness at Ext^\{n+1}(V”; SGA 7 VII (3.3.6), “Exactness at Extⁿ⁺¹(L•”; SGA 7 VII (3.7.5), “Exactness at Ext^\{n+1}(P”.
- [`CategoryTheory.Abelian.Ext.postcomp_mk₀_injective_of_mono`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Abelian.Ext.postcomp_mk₀_injective_of_mono#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L233) (StacksFrontier): “leading 0: Hom(M,N') -> Hom(M,N) injective”.
- [`CategoryTheory.Abelian.Ext.addEquiv₀`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Abelian.Ext.addEquiv₀#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L235) (StacksFrontier): “Ext^0(M,N) = Hom(M,N)”. References: SGA 4 V (2.1.1), “more general”; SGA 4 V (6.0), “6.0.3, 6.0.4”; SGA 4 V (6.3), “(6.3.1)”; SGA 7 VII (3.1.7), “special case”.

## Tag 065P, a lemma

[Tag 065P](https://stacks.math.columbia.edu/tag/065P) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Abelian.Ext.contravariantSequence_exact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Abelian.Ext.contravariantSequence_exact#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L103) (StacksFrontier): “exactness of the Ext^n0 -> ... -> Ext^n1 window (whole sequence for 1+n0=n1)”. References: SGA 4 V (2.1.1), “partial”; SGA 4 V (6.2), “Exactness of (6.2.2)”; SGA 4½ Etat 0 (1.1.2), “special case”; SGA 4½ Etat 0 (3.2.2), “special case”; SGA 7 VII (3.4.9), “partial”; SGA 7 VII (3.7.5), “special case”.
- [`CategoryTheory.Abelian.Ext.contravariantSequence`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Abelian.Ext.contravariantSequence#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L105) (StacksFrontier): “the long exact sequence (as composable arrows)”. References: SGA 4 V (6.2); SGA 7 VII (3.4.9), “partial”; SGA 7 VII (3.7.5).
- [`CategoryTheory.Abelian.Ext.contravariant_sequence_exact₂'`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Abelian.Ext.contravariant_sequence_exact₂'#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L107) (StacksFrontier): “exactness at Ext^n(M,N)”. References: SGA 4 V (2.1.1), “Exactness Ext^n(X3”; SGA 4 V (6.2), “partial”; SGA 4½ Etat 0 (1.1.2), “special case”; SGA 7 VII (3.4.9), “partial”; SGA 7 VII (3.7.5), “Exactness at Ext^n(P”.
- [`CategoryTheory.Abelian.Ext.contravariant_sequence_exact₁'`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Abelian.Ext.contravariant_sequence_exact₁'#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L109) (StacksFrontier): “exactness at Ext^n(M',N)”. References: SGA 4 V (2.1.1), “Exactness Ext^n(X2”; SGA 4 V (6.2), “partial”; SGA 4½ Etat 0 (1.1.2), “special case”; SGA 4½ Etat 0 (3.2.2), “Exactness at Ext^n(X”; SGA 7 VII (3.4.9), “partial”.
- [`CategoryTheory.Abelian.Ext.contravariant_sequence_exact₃'`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Abelian.Ext.contravariant_sequence_exact₃'#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L111) (StacksFrontier): “exactness at Ext^(n+1)(M'',N)”. References: SGA 4 V (6.2), “partial”.
- [`CategoryTheory.Abelian.Ext.precomp_mk₀_injective_of_epi`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Abelian.Ext.precomp_mk₀_injective_of_epi#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L113) (StacksFrontier): “leading 0: Hom(M'',N) -> Hom(M,N) injective”.
- [`CategoryTheory.Abelian.Ext.addEquiv₀`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Abelian.Ext.addEquiv₀#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L115) (StacksFrontier): “Ext^0(M,N) = Hom(M,N)”. References: SGA 4 V (2.1.1), “more general”; SGA 4 V (6.0), “6.0.3, 6.0.4”; SGA 4 V (6.3), “(6.3.1)”; SGA 7 VII (3.1.7), “special case”.

## Tag 00LV, a lemma

[Tag 00LV](https://stacks.math.columbia.edu/tag/00LV) in the Stacks Project.

**`ext_annihilated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ext/Finiteness.lean, line 527](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ext/Finiteness.lean#L527).

> **Stacks 00LV**.
> If `x` annihilates `N` or `x` annihilates `M`, then `x` annihilates every Ext group
> $\operatorname{Ext}^i_R(M, N)$.

```lean
theorem ext_annihilated (M N : ModuleCat.{u} R) (x : R)
    (h : x ∈ Module.annihilator R N ∨ x ∈ Module.annihilator R M) (i : ℕ) :
    ∀ ξ : extModule M N i, x • ξ = 0
```

## Tag 08YR, a lemma

[Tag 08YR](https://stacks.math.columbia.edu/tag/08YR) in the Stacks Project.

**`ext_finite_of_noetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ext/Finiteness.lean, line 315](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ext/Finiteness.lean#L315). References: EGA III (4.5.1), “special case”; SGA 6 I (3.7), “Clause b), special case”.

> For a Noetherian ring `R` and finite `R`-modules `M`, `N`, each `Ext^i_R(M, N)` is a
> finite `R`-module.

```lean
theorem ext_finite_of_noetherian (R : Type) [CommRing R] [IsNoetherianRing R]
    (M N : ModuleCat.{0} R) [Module.Finite R M] [Module.Finite R N] (i : ℕ) :
    Module.Finite R (((Ext R (ModuleCat R) i).obj (Opposite.op M)).obj N)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.71, Tag 00LO](https://stacks.math.columbia.edu/tag/00LO)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
