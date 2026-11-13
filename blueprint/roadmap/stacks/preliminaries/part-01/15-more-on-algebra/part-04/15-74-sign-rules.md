---
declaration: section
origin: cited
lean: CochainComplex.HomComplex.tensorShiftIso, CochainComplex.HomComplex.tensorShiftHom, CochainComplex.HomComplex.tensorShiftIso_hom_ι_and_naturality, TotalTensorComplex.cochainComplex_symmetricMonoidalCategory, ModuleCat.LeftDual.finite_projective_and_linearDual_equiv_of_exactPairing, CochainComplex.LeftDual.exactPairing_iff_bounded_finiteProjective, CochainComplex.LeftDual.tensorLeftDualIsoHomComplex, CochainComplex.HomComplex.evaluationToDoubleHom_apply
statement: formalized
proof: formalized
---

# 15.74 Sign rules

Section 15.74 of the Stacks Project, [Tag 0FNG](https://stacks.math.columbia.edu/tag/0FNG). 7 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FNH, an item

[Tag 0FNH](https://stacks.math.columbia.edu/tag/0FNH) in the Stacks Project.

**`CochainComplex.HomComplex.tensorShiftIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/ShiftTensor.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/HomComplex/ShiftTensor.lean#L77). The attribute's comment: “canonical isomorphism”.

> **Stacks 0FNH.** The canonical isomorphism from the shift by `a + b` of the tensor product
> `M ⊗ N` to the tensor product `M[a] ⊗ N[b]` of the shifts.
>
> It is the inverse of the composite that removes the shift from the first factor, then from the
> second factor, and finally recombines the two shifts; see
> `CochainComplex.HomComplex.tensorShiftIso_hom_ι_and_naturality` for the homogeneous formula that
> pins it down.

```lean
noncomputable def tensorShiftIso (M N : CochainComplex (ModuleCat R) ℤ) (a b : ℤ) :
    (M ⊗ N)⟦a + b⟧ ≅ M⟦a⟧ ⊗ N⟦b⟧
```

**`CochainComplex.HomComplex.tensorShiftHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/ShiftTensor.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/HomComplex/ShiftTensor.lean#L90). The attribute's comment: “corresponding shifted map”.

> **Stacks 0FNH.** The morphism corresponding to
> `CochainComplex.HomComplex.tensorShiftIso`: its source is the unshifted tensor product and its
> target is the tensor product of the shifts, shifted back by `-a - b`.

```lean
noncomputable def tensorShiftHom (M N : CochainComplex (ModuleCat R) ℤ) (a b : ℤ) :
    M ⊗ N ⟶ (M⟦a⟧ ⊗ N⟦b⟧)⟦-a - b⟧
```

**`CochainComplex.HomComplex.tensorShiftIso_hom_ι_and_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/ShiftTensor.lean, line 225](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/HomComplex/ShiftTensor.lean#L225). The attribute's comment: “homogeneous sign formula and naturality”.

> **Stacks 0FNH.** On the summand `M^p ⊗ N^q`, the simultaneous-shift isomorphism
> `CochainComplex.HomComplex.tensorShiftIso` is multiplication by the Koszul sign `(-1)^(p*b)`
> followed by the canonical inclusion of `M[a]^{p-a} ⊗ N[b]^{q-b}` into the shifted total complex.
> Since the homogeneous summands generate, this determines the isomorphism. It is moreover natural
> in both complexes.

```lean
theorem tensorShiftIso_hom_ι_and_naturality
    (M N : CochainComplex (ModuleCat R) ℤ) (a b : ℤ) :
    (∀ (p q : ℤ),
      HomologicalComplex.ιTensorObj M N p q (p + q) rfl ≫
          (CochainComplex.shiftFunctorObjXIso (M ⊗ N) (a + b)
            (p + q - a - b) (p + q) (by omega)).inv ≫
          (tensorShiftIso M N a b).hom.f (p + q - a - b) =
        ((p * b).negOnePow : ℤˣ) •
          ((CochainComplex.shiftFunctorObjXIso M a (p - a) p (by omega)).inv ⊗ₘ
              (CochainComplex.shiftFunctorObjXIso N b (q - b) q (by omega)).inv) ≫
            HomologicalComplex.ιTensorObj (M⟦a⟧) (N⟦b⟧)
              (p - a) (q - b) (p + q - a - b) (by omega)) ∧
      (∀ (M' N' : CochainComplex (ModuleCat R) ℤ) (f : M ⟶ M') (g : N ⟶ N'),
        (HomologicalComplex.tensorHom f g)⟦a + b⟧' ≫
            (tensorShiftIso M' N' a b).hom =
          (tensorShiftIso M N a b).hom ≫
            HomologicalComplex.tensorHom (f⟦a⟧') (g⟦b⟧'))
```

## Tag 0GWR, an item

[Tag 0GWR](https://stacks.math.columbia.edu/tag/0GWR) in the Stacks Project.

**`TotalTensorComplex.cochainComplex_symmetricMonoidalCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TensorComplex/Monoidal.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/TensorComplex/Monoidal.lean#L116).

> The category of cochain complexes of modules over a commutative ring, with tensor product
> given by the total complex of the degreewise tensor product, is symmetric monoidal. On the
> summand of bidegree `(p, q)`, its braiding is the ordinary symmetry of tensor products multiplied
> by the Koszul sign `(-1)^(p*q)`.

```lean
public theorem cochainComplex_symmetricMonoidalCategory (R : Type u) [CommRing R] :
    ∃ s : SymmetricCategory (CochainComplex (ModuleCat R) ℤ),
      ∀ (K L : CochainComplex (ModuleCat R) ℤ) (p q n : ℤ) (h : p + q = n),
        HomologicalComplex.ιTensorObj K L p q n h ≫
            (s.toBraidedCategory.braiding K L).hom.f n =
          ((p * q).negOnePow : ℤˣ) •
            ((β_ (K.X p) (L.X q)).hom ≫
              HomologicalComplex.ιTensorObj L K q p n (by simpa [add_comm] using h))
```

## Tag 0FNJ, a lemma

[Tag 0FNJ](https://stacks.math.columbia.edu/tag/0FNJ) in the Stacks Project.

**`ModuleCat.LeftDual.finite_projective_and_linearDual_equiv_of_exactPairing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/LeftDual.lean, line 251](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/LeftDual.lean#L251).

> If `N` is a left dual of `M` in the monoidal category of `R`-modules, then `M` and `N` are
> finite projective. Moreover, contraction with the coevaluation identifies `M⁺` with `N`, and
> under this identification the given evaluation map sends `n ⊗ m` to the value at `m` of the
> functional corresponding to `n`.

```lean
theorem finite_projective_and_linearDual_equiv_of_exactPairing :
    Module.Finite R M ∧ Module.Projective R M ∧
      Module.Finite R N ∧ Module.Projective R N ∧
        ∃ e : Module.Dual R M ≃ₗ[R] N,
          e.toLinearMap = linearDualToLeftDual R M N ∧
            ∀ (n : N) (m : M),
              (ε_ (ModuleCat.of R M) (ModuleCat.of R N)).hom (n ⊗ₜ[R] m) = e.symm n m
```

## Tag 0FNK, a lemma

[Tag 0FNK](https://stacks.math.columbia.edu/tag/0FNK) in the Stacks Project.

**`CochainComplex.LeftDual.exactPairing_iff_bounded_finiteProjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/LeftDual.lean, line 1127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/LeftDual.lean#L1127).

> A complex of modules and a chosen left dual are bounded complexes of finite projective
> modules, and the pairing is the termwise linear-dual pairing with signed transpose differential.
> Conversely, every bounded complex of finite projective modules admits exactly this construction
> as a left dual.

```lean
theorem exactPairing_iff_bounded_finiteProjective (R : Type u) [CommRing R] :
    (∀ (M N : CochainComplex (ModuleCat R) ℤ) (p : ExactPairing M N),
      (∃ a b : ℤ, M.IsStrictlyGE a ∧ M.IsStrictlyLE b) ∧
        (∃ a b : ℤ, N.IsStrictlyGE a ∧ N.IsStrictlyLE b) ∧
        (∀ n : ℤ, Module.Finite R (M.X n) ∧ Module.Projective R (M.X n)) ∧
        (∀ n : ℤ, Module.Finite R (N.X n) ∧ Module.Projective R (N.X n)) ∧
        IsLinearDualPairing R M N p) ∧
      (∀ M : CochainComplex (ModuleCat R) ℤ,
        (∃ a b : ℤ, M.IsStrictlyGE a ∧ M.IsStrictlyLE b) →
        (∀ n : ℤ, Module.Finite R (M.X n) ∧ Module.Projective R (M.X n)) →
        ∃ (N : CochainComplex (ModuleCat R) ℤ) (p : ExactPairing M N),
          (∃ a b : ℤ, N.IsStrictlyGE a ∧ N.IsStrictlyLE b) ∧
            IsLinearDualPairing R M N p)
```

## Tag 0FNL, an item

[Tag 0FNL](https://stacks.math.columbia.edu/tag/0FNL) in the Stacks Project.

**`CochainComplex.LeftDual.tensorLeftDualIsoHomComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/LeftDual.lean, line 1261](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/LeftDual.lean#L1261).

> **Stacks 0FNL.** For a complex `M` with left dual `N`, the canonical sign-free tensor–Hom
> morphism is a natural isomorphism `K ⊗ N ≅ Hom^•(M, K)`. On the summand `K^p ⊗ N^q`, its
> component in `Hom(M^{-q}, K^p)` sends `x ⊗ y` to the map `m ↦ ε(y ⊗ m) • x`.

```lean
theorem tensorLeftDualIsoHomComplex
    (M N : CochainComplex (ModuleCat R) ℤ) (pairing : ExactPairing M N) :
    letI := pairing
    ∃ e : ∀ K : CochainComplex (ModuleCat R) ℤ,
        K ⊗ N ≅ HomComplexR R M K,
      (∀ (K : CochainComplex (ModuleCat R) ℤ) (n p q : ℤ) (hpq : p + q = n)
          (x : K.X p) (y : N.X q) (m : M.X (-q)),
        (((((e K).hom.f n).hom
            ((ιTensorObj K N p q n hpq).hom (x ⊗ₜ[R] y))) : Cochain M K n).v
              (-q) p (by omega)).hom m =
          ((ιTensorObj N M q (-q) 0 (by omega) ≫ (ε_ M N).f 0 ≫
              (singleObjXSelf (ComplexShape.up ℤ) 0 (𝟙_ (ModuleCat R))).hom).hom
            (y ⊗ₜ[R] m)) • x) ∧
        ∀ (K L : CochainComplex (ModuleCat R) ℤ) (f : K ⟶ L),
          (e K).hom ≫ Stacks.HomComplex.TensorHomComparison.HomCxMap M M K L (𝟙 M) f =
            (f ▷ N) ≫ (e L).hom
```

## Tag 0FNM, an item

[Tag 0FNM](https://stacks.math.columbia.edu/tag/0FNM) in the Stacks Project.

**`CochainComplex.HomComplex.evaluationToDoubleHom_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/Differentials.lean, line 500](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/HomComplex/Differentials.lean#L500).

> **Stacks 0FNM.** The canonical evaluation into the double Hom complex sends homogeneous
> `x ∈ K^n` and `f ∈ Hom^m(K, M)` to `(-1)^(nm) f(x)`. It is natural in `K` and dinatural in the
> coefficient complex `M`.

```lean
theorem evaluationToDoubleHom_apply :
    (∀ (K M : CochainComplex (ModuleCat.{u} R) ℤ) (n m : ℤ)
        (x : K.X n) (f : Cochain K M m),
      ((((evaluationToDoubleHom K M).f n).hom x).v m (m + n) (by omega)).hom f =
        (n * m).negOnePow • (f.v n (m + n) (by omega)).hom x) ∧
    (∀ (K K' M : CochainComplex (ModuleCat.{u} R) ℤ) (g : K ⟶ K'),
      evaluationToDoubleHom K M ≫
          Stacks.HomComplex.TensorHomMap.precomp R (HomComplexR R K' M) (HomComplexR R K M) M
            (Stacks.HomComplex.TensorHomMap.precomp R K K' M g) =
        g ≫ evaluationToDoubleHom K' M) ∧
    (∀ (K M M' : CochainComplex (ModuleCat.{u} R) ℤ) (g : M ⟶ M'),
      evaluationToDoubleHom K M ≫
          Stacks.HomComplex.TensorHomMap.postcomp R (HomComplexR R K M) M M' g =
        evaluationToDoubleHom K M' ≫
          Stacks.HomComplex.TensorHomMap.precomp R (HomComplexR R K M) (HomComplexR R K M') M'
            (Stacks.HomComplex.TensorHomMap.postcomp R K M M' g))
```

## Tag 0FNN, an item

[Tag 0FNN](https://stacks.math.columbia.edu/tag/0FNN) in the Stacks Project.

**`CochainComplex.HomComplex.homComplexShiftIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/ShiftHom.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/HomComplex/ShiftHom.lean#L191).

> **Stacks 0FNN.** The canonical identification
> `Hom^•(M, K)[a - b] ≅ Hom^•(M[b], K[a])`.
>
> After shifting the identification back to a map `Hom^•(M, K) ⟶ Hom^•(M[b], K[a])[b - a]`, its
> degree-`n` component is the sign `(-1)^(n b)` times the evident reindexing. The final conjunct is
> the homogeneous differential calculation: before inserting this degree-dependent sign, the
> target differential is `(-1)^b` times the reindexed source differential.

```lean
noncomputable def homComplexShiftIso (R : Type*) [CommRing R]
    (M K : CochainComplex (ModuleCat R) ℤ) (a b : ℤ) :
    { e : (CochainComplex.HomComplexR R M K)⟦a - b⟧ ≅
        CochainComplex.HomComplexR R (M⟦b⟧) (K⟦a⟧) //
      let H := CochainComplex.HomComplexR R M K
      let T := CochainComplex.HomComplexR R (M⟦b⟧) (K⟦a⟧)
      let reindex : ∀ n : ℤ, Cochain M K n → Cochain (M⟦b⟧) (K⟦a⟧) (n + (b - a)) :=
        fun n z ↦ Cochain.mk fun p q _ ↦
          (M.shiftFunctorObjXIso b p (p + b) rfl).hom ≫
            z.v (p + b) (q + a) (by omega) ≫
            (K.shiftFunctorObjXIso a q (q + a) rfl).inv
      let g : H ⟶ T⟦b - a⟧ :=
        (shiftFunctorCompIsoId _ (a - b) (b - a) (by omega)).inv.app H ≫ e.hom⟦b - a⟧'
      (∀ (n : ℤ) (z : Cochain M K n),
        (T.shiftFunctorObjXIso (b - a) n (n + (b - a)) rfl).hom.hom ((g.f n).hom z) =
          (n * b).negOnePow • reindex n z) ∧
      (∀ (n : ℤ) (z : Cochain M K n),
        (T.shiftFunctorObjXIso (b - a) (n + 1) (n + 1 + (b - a)) rfl).hom.hom
            (((T⟦b - a⟧).d n (n + 1)).hom
              ((T.shiftFunctorObjXIso (b - a) n (n + (b - a)) rfl).inv.hom
                (reindex n z))) =
          b.negOnePow • reindex (n + 1) (δ n (n + 1) z)) }
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.74, Tag 0FNG](https://stacks.math.columbia.edu/tag/0FNG)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
