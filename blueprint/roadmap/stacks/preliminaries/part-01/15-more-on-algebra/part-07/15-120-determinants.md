---
declaration: section
origin: cited
lean: ProjectiveDeterminant.determinant_submodule_eq_annihilator, ProjectiveDeterminant.determinantTensorDeterminantEquiv_of_exact, ProjectiveDeterminant.determinantTensorDeterminantEquiv_naturality, ProjectiveDeterminant.determinantEquiv_filtration, ProjectiveDeterminant.determinantTensorDeterminantEquiv_prodComm, ProjectiveDeterminant.det_one_add_comp_comm, K0.exists_determinant_hom
statement: formalized
proof: formalized
---

# 15.120 Determinants

Section 15.120 of the Stacks Project, [Tag 0FJ9](https://stacks.math.columbia.edu/tag/0FJ9). 7 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FJA, a remark

[Tag 0FJA](https://stacks.math.columbia.edu/tag/0FJA) in the Stacks Project.

**`ProjectiveDeterminant.determinant_submodule_eq_annihilator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Projective/Determinant/Basic/Localization.lean, line 728](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Projective/Determinant/Basic/Localization.lean#L728).

> **Stacks 0FJA.** The determinant line of a finite projective module is the
> annihilator of the degree-one elements in its exterior algebra.

```lean
public theorem determinant_submodule_eq_annihilator (R : Type u) (M : Type v)
    [CommRing R] [AddCommGroup M] [Module R M]
    [Module.Finite R M] [Module.Projective R M] :
    ProjectiveDeterminant.submodule (R := R) (M := M) =
      ⨅ m : M, LinearMap.ker (LinearMap.mulLeft R (ExteriorAlgebra.ι R m))
```

## Tag 0FJB, a lemma

[Tag 0FJB](https://stacks.math.columbia.edu/tag/0FJB) in the Stacks Project.

**`ProjectiveDeterminant.determinantTensorDeterminantEquiv_of_exact`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Projective/Determinant/ShortExact/Construction.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Projective/Determinant/ShortExact/Construction.lean#L157). References: SGA 6 X (5.1), “affine case”.

> A short exact sequence `0 → M' → M → M'' → 0` of finite projective modules has a canonical
> determinant isomorphism. Its value on `x' ⊗ x''` is the wedge of the image of `x'` with any lift of
> `x''` to the exterior algebra of `M`.

```lean
public noncomputable def determinantTensorDeterminantEquiv_of_exact
    {R : Type u} [CommRing R]
    {M' : Type v} {M : Type w} {M'' : Type x}
    [AddCommGroup M'] [Module R M'] [Module.Finite R M'] [Module.Projective R M']
    [AddCommGroup M] [Module R M] [Module.Finite R M] [Module.Projective R M]
    [AddCommGroup M''] [Module R M''] [Module.Finite R M''] [Module.Projective R M'']
    (f : M' →ₗ[R] M) (g : M →ₗ[R] M'')
    (hf : Function.Injective f) (hfg : Function.Exact f g) (hg : Function.Surjective g) :
    { γ : TensorProduct R
          (↥(⨅ m : M', LinearMap.ker
            (LinearMap.mulLeft R (ExteriorAlgebra.ι R m))))
          (↥(⨅ m : M'', LinearMap.ker
            (LinearMap.mulLeft R (ExteriorAlgebra.ι R m)))) ≃ₗ[R]
        ↥(⨅ m : M, LinearMap.ker
          (LinearMap.mulLeft R (ExteriorAlgebra.ι R m))) //
      ∀ (x' : ↥(⨅ m : M', LinearMap.ker
            (LinearMap.mulLeft R (ExteriorAlgebra.ι R m))))
        (x'' : ↥(⨅ m : M'', LinearMap.ker
            (LinearMap.mulLeft R (ExteriorAlgebra.ι R m))))
        (y'' : ExteriorAlgebra R M),
        ExteriorAlgebra.map g y'' = (x'' : ExteriorAlgebra R M'') →
          ((γ (x' ⊗ₜ[R] x'') : ↥(⨅ m : M, LinearMap.ker
              (LinearMap.mulLeft R (ExteriorAlgebra.ι R m)))) : ExteriorAlgebra R M) =
            ExteriorAlgebra.map f (x' : ExteriorAlgebra R M') * y'' }
```

## Tag 0FJC, a lemma

[Tag 0FJC](https://stacks.math.columbia.edu/tag/0FJC) in the Stacks Project.

**`ProjectiveDeterminant.determinantTensorDeterminantEquiv_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Projective/Determinant/ShortExact/Construction.lean, line 364](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Projective/Determinant/ShortExact/Construction.lean#L364).

> The canonical determinant isomorphism of a short exact sequence of finite projective modules is
> natural under an isomorphism of short exact sequences.

```lean
public theorem determinantTensorDeterminantEquiv_naturality
    {R : Type u} [CommRing R]
    {M' : Type v₁} {M : Type v₂} {M'' : Type v₃}
    {K' : Type w₁} {K : Type w₂} {K'' : Type w₃}
    [AddCommGroup M'] [Module R M'] [Module.Finite R M'] [Module.Projective R M']
    [AddCommGroup M] [Module R M] [Module.Finite R M] [Module.Projective R M]
    [AddCommGroup M''] [Module R M''] [Module.Finite R M''] [Module.Projective R M'']
    [AddCommGroup K'] [Module R K'] [Module.Finite R K'] [Module.Projective R K']
    [AddCommGroup K] [Module R K] [Module.Finite R K] [Module.Projective R K]
    [AddCommGroup K''] [Module R K''] [Module.Finite R K''] [Module.Projective R K'']
    (f : M' →ₗ[R] M) (g : M →ₗ[R] M'')
    (fK : K' →ₗ[R] K) (gK : K →ₗ[R] K'')
    (hf : Function.Injective f) (hfg : Function.Exact f g) (hg : Function.Surjective g)
    (hfK : Function.Injective fK) (hfgK : Function.Exact fK gK)
    (hgK : Function.Surjective gK)
    (a : M' ≃ₗ[R] K') (b : M ≃ₗ[R] K) (c : M'' ≃ₗ[R] K'')
    (hab : ∀ x : M', b (f x) = fK (a x))
    (hbc : ∀ x : M, c (g x) = gK (b x)) :
    let D_M' : Submodule R (ExteriorAlgebra R M') :=
      ⨅ x : M', LinearMap.ker (LinearMap.mulLeft R (ExteriorAlgebra.ι R x))
    let D_M : Submodule R (ExteriorAlgebra R M) :=
      ⨅ x : M, LinearMap.ker (LinearMap.mulLeft R (ExteriorAlgebra.ι R x))
    let D_M'' : Submodule R (ExteriorAlgebra R M'') :=
      ⨅ x : M'', LinearMap.ker (LinearMap.mulLeft R (ExteriorAlgebra.ι R x))
    let D_K' : Submodule R (ExteriorAlgebra R K') :=
      ⨅ x : K', LinearMap.ker (LinearMap.mulLeft R (ExteriorAlgebra.ι R x))
    let D_K : Submodule R (ExteriorAlgebra R K) :=
      ⨅ x : K, LinearMap.ker (LinearMap.mulLeft R (ExteriorAlgebra.ι R x))
    let D_K'' : Submodule R (ExteriorAlgebra R K'') :=
      ⨅ x : K'', LinearMap.ker (LinearMap.mulLeft R (ExteriorAlgebra.ι R x))
    let γM := (determinantTensorDeterminantEquiv_of_exact f g hf hfg hg).val
    let γK := (determinantTensorDeterminantEquiv_of_exact fK gK hfK hfgK hgK).val
    Set.BijOn (ExteriorAlgebra.map a)
        (D_M' : Set (ExteriorAlgebra R M')) (D_K' : Set (ExteriorAlgebra R K')) ∧
      Set.BijOn (ExteriorAlgebra.map b)
        (D_M : Set (ExteriorAlgebra R M)) (D_K : Set (ExteriorAlgebra R K)) ∧
      Set.BijOn (ExteriorAlgebra.map c)
        (D_M'' : Set (ExteriorAlgebra R M'')) (D_K'' : Set (ExteriorAlgebra R K'')) ∧
      ∀ (x' : D_M') (x'' : D_M'') (y' : D_K') (y'' : D_K''),
        ExteriorAlgebra.map a (x' : ExteriorAlgebra R M') =
          (y' : ExteriorAlgebra R K') →
        ExteriorAlgebra.map c (x'' : ExteriorAlgebra R M'') =
          (y'' : ExteriorAlgebra R K'') →
        ExteriorAlgebra.map b
            ((γM (x' ⊗ₜ[R] x'') : D_M) : ExteriorAlgebra R M) =
          ((γK (y' ⊗ₜ[R] y'') : D_K) : ExteriorAlgebra R K)
```

## Tag 0FJD, a lemma

[Tag 0FJD](https://stacks.math.columbia.edu/tag/0FJD) in the Stacks Project.

**`ProjectiveDeterminant.determinantEquiv_filtration`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Projective/Determinant/ShortExact/Filtration.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Projective/Determinant/ShortExact/Filtration.lean#L94).

> For finite projective successive quotients of a filtration `K ≤ L ≤ M`, combining the canonical
> determinant equivalences first across `K ≤ L` or first across the induced sequence
> `L / K → M / K → M / L` gives the same equivalence to the determinant line of `M`.

```lean
public theorem determinantEquiv_filtration
    {R : Type u} [CommRing R] {M : Type v} [AddCommGroup M] [Module R M]
    (K L : Submodule R M) (hKL : K ≤ L)
    [Module.Finite R K] [Module.Projective R K]
    [Module.Finite R (L ⧸ K.submoduleOf L)]
    [Module.Projective R (L ⧸ K.submoduleOf L)]
    [Module.Finite R (M ⧸ L)] [Module.Projective R (M ⧸ L)] :
    let iQ : (L ⧸ K.submoduleOf L) →ₗ[R] (M ⧸ K) :=
      (K.submoduleOf L).mapQ K L.subtype (by
        intro x hx
        exact hx)
    let pQ : (M ⧸ K) →ₗ[R] (M ⧸ L) :=
      K.mapQ L LinearMap.id (by simpa using hKL)
    ∃ hLfin : Module.Finite R L,
      ∃ hLproj : Module.Projective R L,
        ∃ hMKfin : Module.Finite R (M ⧸ K),
          ∃ hMKproj : Module.Projective R (M ⧸ K),
            ∃ hMfin : Module.Finite R M,
              ∃ hMproj : Module.Projective R M,
                let _ : Module.Finite R L := hLfin
                let _ : Module.Projective R L := hLproj
                let _ : Module.Finite R (M ⧸ K) := hMKfin
                let _ : Module.Projective R (M ⧸ K) := hMKproj
                let _ : Module.Finite R M := hMfin
                let _ : Module.Projective R M := hMproj
                let hiQ : Function.Injective iQ
    := by
                  intro x y hxy
                  obtain ⟨x, rfl⟩
```

## Tag 0FJE, a lemma

[Tag 0FJE](https://stacks.math.columbia.edu/tag/0FJE) in the Stacks Project.

**`ProjectiveDeterminant.determinantTensorDeterminantEquiv_prodComm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Projective/Determinant/ShortExact/ProdComm.lean, line 366](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Projective/Determinant/ShortExact/ProdComm.lean#L366).

> Switching the summands in a direct sum is compatible with the canonical isomorphism from the
> tensor product of their determinant lines, up to the determinant of minus the identity on the
> tensor product of the summands.

```lean
public theorem determinantTensorDeterminantEquiv_prodComm
    {R : Type u} [CommRing R]
    (M' : Type v) (M'' : Type w)
    [AddCommGroup M'] [Module R M'] [Module.Finite R M'] [Module.Projective R M']
    [AddCommGroup M''] [Module R M''] [Module.Finite R M''] [Module.Projective R M''] :
    let D' : Submodule R (ExteriorAlgebra R M') :=
      ⨅ m : M', LinearMap.ker (LinearMap.mulLeft R (ExteriorAlgebra.ι R m))
    let D'' : Submodule R (ExteriorAlgebra R M'') :=
      ⨅ m : M'', LinearMap.ker (LinearMap.mulLeft R (ExteriorAlgebra.ι R m))
    let D'_prod_D'' : Submodule R (ExteriorAlgebra R (M' × M'')) :=
      ⨅ m : M' × M'', LinearMap.ker (LinearMap.mulLeft R (ExteriorAlgebra.ι R m))
    let D''_prod_D' : Submodule R (ExteriorAlgebra R (M'' × M')) :=
      ⨅ m : M'' × M', LinearMap.ker (LinearMap.mulLeft R (ExteriorAlgebra.ι R m))
    let γ' := (determinantTensorDeterminantEquiv_of_exact
      (LinearMap.inl R M' M'') (LinearMap.snd R M' M'')
      LinearMap.inl_injective Function.Exact.inl_snd LinearMap.snd_surjective).val
    let γ'' := (determinantTensorDeterminantEquiv_of_exact
      (LinearMap.inl R M'' M') (LinearMap.snd R M'' M')
      LinearMap.inl_injective Function.Exact.inl_snd LinearMap.snd_surjective).val
    ∃ ε : Rˣ,
      (ε : R) = ProjectiveDeterminant.det
        (-(LinearMap.id : TensorProduct R M' M'' →ₗ[R] TensorProduct R M' M'')) ∧
      ∀ x : TensorProduct R D' D'',
        ExteriorAlgebra.map (LinearEquiv.prodComm R M' M'')
            ((γ' x : D'_prod_D'') : ExteriorAlgebra R (M' × M'')) =
          ((γ'' ((ε : R) • TensorProduct.comm R D' D'' x) : D''_prod_D') :
            ExteriorAlgebra R (M'' × M'))
```

## Tag 0FJF, a lemma

[Tag 0FJF](https://stacks.math.columbia.edu/tag/0FJF) in the Stacks Project.

**`ProjectiveDeterminant.det_one_add_comp_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Projective/Determinant/Basic/Localization.lean, line 782](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Projective/Determinant/Basic/Localization.lean#L782).

> **Stacks 0FJF.** For maps in opposite directions between finite projective modules, the
> determinants of the identity plus the two possible composites agree.

```lean
public theorem det_one_add_comp_comm
    {R : Type u} [CommRing R]
    {M : Type v} [AddCommGroup M] [Module R M] [Module.Finite R M] [Module.Projective R M]
    {N : Type w} [AddCommGroup N] [Module R N] [Module.Finite R N] [Module.Projective R N]
    (a : M →ₗ[R] N) (b : N →ₗ[R] M) :
    ProjectiveDeterminant.det (LinearMap.id + a.comp b) =
      ProjectiveDeterminant.det (LinearMap.id + b.comp a)
```

## Tag 0AFX, a lemma

[Tag 0AFX](https://stacks.math.columbia.edu/tag/0AFX) in the Stacks Project.

**`K0.exists_determinant_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/KTheory/Grothendieck/Determinant.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/KTheory/Grothendieck/Determinant.lean#L155). References: SGA 6 X (5.1), “affine case”.

> **Stacks 0AFX.** The determinant gives a homomorphism from `K₀(R)` to the Picard group.
> For a finite locally free module of constant rank `n`, it sends its class to the class of its
> `n`th exterior power.

```lean
public theorem K0.exists_determinant_hom (R : Type u) [CommRing R] :
    ∃ det : K0 R →+ Additive (CommRing.Pic R),
      ∀ (M : FGProj R) (n : ℕ),
        Module.rankAtStalk M.carrier = Function.const (PrimeSpectrum R) n →
          ∃ h : Module.Invertible R (⋀[R]^n M.carrier),
            det (K0.mk M) =
              Additive.ofMul (@CommRing.Pic.mk R (⋀[R]^n M.carrier) inferInstance
                inferInstance inferInstance h)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.120, Tag 0FJ9](https://stacks.math.columbia.edu/tag/0FJ9)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
