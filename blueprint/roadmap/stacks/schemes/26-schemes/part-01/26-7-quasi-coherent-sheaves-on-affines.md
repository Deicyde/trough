---
declaration: section
origin: cited
lean: AlgebraicGeometry.tildeAssociatedSheafNatIso, AlgebraicGeometry.instIsQuasicoherentOpensCarrierCarrierCommRingCatSpecTilde, AlgebraicGeometry.tilde.adjunction, Stacks.AffineExteriorPower.tildeExteriorPowerIso, Stacks.AffineExteriorPower.tildeExteriorPowerIso_natural, Stacks.AffineExteriorPower.tildeExteriorPowerIso_hom_ιMulti, Stacks.SymGraded.tildeSymmetricPowerIso, Stacks.SymGraded.tildeSymmetricPowerIso_unit
statement: formalized
proof: formalized
---

# 26.7 Quasi-coherent sheaves on affines

Section 26.7 of the Stacks Project, [Tag 01I6](https://stacks.math.columbia.edu/tag/01I6). 8 tags here are carried by 42 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01I7, a lemma

[Tag 01I7](https://stacks.math.columbia.edu/tag/01I7) in the Stacks Project.

**`AlgebraicGeometry.tildeAssociatedSheafNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/QuasiCoherentSheaves/Basic.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/QuasiCoherentSheaves/Basic.lean#L60). The attribute's comment: “canonical functorial comparison”. References: EGA I (1.8.6), “u = id on Spec R”.

> The canonical comparison between the affine construction `M ↦ M̃` on `Spec R` and tensor
> sheafification along `R → Γ(Spec R, 𝒪)`: a natural isomorphism of the two functors, together
> with the equation that on global sections it sends `m` to `1 ⊗ m`.

```lean
noncomputable def tildeAssociatedSheafNatIso (R : CommRingCat.{u}) :
    { e : tilde.functor R ≅
        associatedSheafFunctor (Spec R).toRingedSpace
          (Scheme.ΓSpecIso R).inv.hom //
      ∀ (M : ModuleCat R) (m : M),
        (e.hom.app M).val.app (op ⊤) (tilde.toOpen M ⊤ m) =
          tensorUnitSection (X := (Spec R).toRingedSpace)
            (Scheme.ΓSpecIso R).inv.hom M (op ⊤) m }
```

Declarations registered for the tag:

- [`AlgebraicGeometry.instIsQuasicoherentOpensCarrierCarrierCommRingCatSpecTilde`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.instIsQuasicoherentOpensCarrierCarrierCommRingCatSpecTilde#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/QuasiCoherentSheaves/Basic.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/QuasiCoherentSheaves/Basic.lean#L103) (StacksFrontier): “quasi-coherence”. References: EGA I (1.4.1), “a ⇒ c for V = Spec A”; EGA I (4.1.1), “affine case”; SGA 6 0 (2.5), “partial”.
- [`AlgebraicGeometry.tilde.adjunction`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.tilde.adjunction#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/QuasiCoherentSheaves/Basic.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/QuasiCoherentSheaves/Basic.lean#L111) (StacksFrontier): “mapping property”.

## Tag 01I8, a lemma

[Tag 01I8](https://stacks.math.columbia.edu/tag/01I8) in the Stacks Project.

**`Stacks.AffineExteriorPower.tildeExteriorPowerIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineExteriorPowerCompare/Basic.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineExteriorPowerCompare/Basic.lean#L51). The attribute's comment: “exterior_power”.

> **The affine exterior-power comparison.** The associated sheaf of the `n`-th exterior power
> of `M` is the `n`-th exterior power of `M̃`.

```lean
def tildeExteriorPowerIso (n : ℕ) :
    (tilde (ModuleCat.of ↥R ↥(⋀[↥R]^n ↥M)) : SheafOfModules.{u} (Spec R).ringCatSheaf) ≅
      A.exteriorPower n
```

**`Stacks.AffineExteriorPower.tildeExteriorPowerIso_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineExteriorPowerCompare/Natural.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineExteriorPowerCompare/Natural.lean#L156). The attribute's comment: “exterior_power”.

> **The affine exterior-power comparison is natural.** It respects every unital homomorphism of
> exterior algebra sheaves extending the map `M̃ ⟶ Ñ` of generating module sheaves on the
> degree-one generators; the universal property of the exterior algebra makes such a homomorphism
> unique, so this determines the degree-`n` square.

```lean
theorem tildeExteriorPowerIso_natural (n : ℕ)
    (A : SheafOfModules.TensorExteriorSymmetricAlgebras
      (Opens.grothendieckTopology ↥(Spec R)) (tilde M))
    (B : SheafOfModules.TensorExteriorSymmetricAlgebras
      (Opens.grothendieckTopology ↥(Spec R)) (tilde N))
    (g : SheafOfModules.GradedAlgebra.UnitalHom A.exterior B.exterior)
    (hg : A.exteriorGenerator ≫ g.app 1 = tilde.map f ≫ B.exteriorGenerator) :
    tilde.map (ModuleCat.ofHom (R := R)
          (X := ModuleCat.of ↥R ↥(⋀[↥R]^n ↥M)) (Y := ModuleCat.of ↥R ↥(⋀[↥R]^n ↥N))
          (exteriorPower.map n f.hom)) ≫ (tildeExteriorPowerIso N B n).hom =
      (tildeExteriorPowerIso M A n).hom ≫ g.app (n : ℤ)
```

**`Stacks.AffineExteriorPower.tildeExteriorPowerIso_hom_ιMulti`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineExteriorPowerCompare/Wedge.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineExteriorPowerCompare/Wedge.lean#L163). The attribute's comment: “exterior_power”.

> **The affine exterior-power comparison on a wedge of global sections.** The global section of
> `(⋀ⁿ_R M)~` attached to `m₁ ∧ ⋯ ∧ mₙ` is carried to the ordered product, in `⋀(M̃)`, of the
> degree-one generators at the global sections of `M̃` attached to the `mᵢ`.

```lean
theorem tildeExteriorPowerIso_hom_ιMulti
    (A : SheafOfModules.TensorExteriorSymmetricAlgebras
      (Opens.grothendieckTopology ↥(Spec R)) (tilde M)) (s : Fin n → ↥M) :
    (((tilde.adjunction (R := R)).homEquiv (ModuleCat.of ↥R ↥(⋀[↥R]^n ↥M))
          (A.exteriorPower n)) (tildeExteriorPowerIso M A n).hom).hom
        (exteriorPower.ιMulti ↥R n s) =
      A.exterior.toPresheafGradedAlgebra.homogeneousProd (specGlobalOpen R) n
        (fun i => A.exteriorGenerator.val.app (specGlobalOpen R)
          ((tilde.toOpen M ⊤).hom (s i)))
```

**`Stacks.SymGraded.tildeSymmetricPowerIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineSymmetricPowerCompare/Basic.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineSymmetricPowerCompare/Basic.lean#L72). The attribute's comment: “symmetric_power”.

> **The affine symmetric-power comparison.** The associated sheaf of the `n`-th symmetric
> power of `M` is the `n`-th symmetric power of `M̃`.

```lean
def tildeSymmetricPowerIso (n : ℕ) :
    (tilde (ModuleCat.of R (SymPow.symmetricPower n R M)) :
        SheafOfModules.{u} (Spec R).ringCatSheaf) ≅ A.symmetricPower n
```

**`Stacks.SymGraded.tildeSymmetricPowerIso_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineSymmetricPowerCompare/Basic.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineSymmetricPowerCompare/Basic.lean#L124). The attribute's comment: “symmetric_power”.

> **In degree zero the comparison takes the algebraic unit to the unit of the symmetric
> algebra sheaf.**

```lean
theorem tildeSymmetricPowerIso_unit :
    let x : SymPow.symmetricPower 0 R M := ⟨1, one_mem_gradedPiece (R := R) M⟩
    (((tilde.adjunction (R := R)).homEquiv
      (ModuleCat.of R (SymPow.symmetricPower 0 R M))
      (A.symmetricPower 0))
      (tildeSymmetricPowerIso M A 0).hom).hom x =
        A.symmetric.one.eval (.op (⊤ : Opens (Spec R).carrier))
```

**`Stacks.SymGraded.tildeSymmetricPowerIso_generator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineSymmetricPowerCompare/Basic.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineSymmetricPowerCompare/Basic.lean#L144). The attribute's comment: “symmetric_power”.

> **In degree one the comparison takes an algebraic generator to the corresponding generator
> of the symmetric algebra sheaf.**

```lean
theorem tildeSymmetricPowerIso_generator (m : M) :
    let x : SymPow.symmetricPower 1 R M :=
      ⟨SymmetricAlgebra.ι R M m, ι_mem_gradedPiece_one (R := R) M m⟩
    (((tilde.adjunction (R := R)).homEquiv
      (ModuleCat.of R (SymPow.symmetricPower 1 R M))
      (A.symmetricPower 1))
      (tildeSymmetricPowerIso M A 1).hom).hom x =
        (A.symmetricGenerator.val.app (.op (⊤ : Opens (Spec R).carrier)))
          ((tilde.toOpen M ⊤).hom m)
```

**`Stacks.SymGraded.tildeSymmetricPowerIso_mul_generator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineSymmetricPowerCompare/Mul.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineSymmetricPowerCompare/Mul.lean#L99). The attribute's comment: “symmetric_power”.

> **The comparison in degree `n + 1` takes multiplication by an algebraic degree-one generator
> to multiplication by the corresponding sheaf generator.** Together with the degree-one
> normalization this fixes the canonical comparison in every degree.

```lean
theorem tildeSymmetricPowerIso_mul_generator (n : ℕ) (m : M)
    (x : SymPow.symmetricPower n R M) :
    HEq
      ((((tilde.adjunction (R := R)).homEquiv
        (ModuleCat.of R (SymPow.symmetricPower (n + 1) R M))
        (A.symmetricPower (n + 1)))
        (tildeSymmetricPowerIso M A (n + 1)).hom).hom
          (SymPow.symMulMap n (LinearMap.id : M →ₗ[R] M) (m ⊗ₜ[R] x)))
      ((A.symmetric.mul 1 (n : ℤ)).app (.op (⊤ : Opens (Spec R).carrier))
        (A.symmetricGenerator.val.app (.op (⊤ : Opens (Spec R).carrier))
          ((tilde.toOpen M ⊤).hom m))
        ((tildeSymmetricPowerIso M A n).hom.val.app (.op (⊤ : Opens (Spec R).carrier))
          ((tilde.toOpen (ModuleCat.of R (SymPow.symmetricPower n R M)) ⊤).hom x)))
```

**`Stacks.SymGraded.tildeSymmetricPowerIso_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineSymmetricPowerCompare/Natural.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineSymmetricPowerCompare/Natural.lean#L58). The attribute's comment: “symmetric_power”.

> **The affine symmetric-power comparison is natural.** It respects every unital homomorphism
> of symmetric algebra sheaves extending the map of generating module sheaves; the universal
> property of the symmetric algebra makes such a homomorphism unique.

```lean
theorem tildeSymmetricPowerIso_natural (n : ℕ)
    (A : SheafOfModules.TensorExteriorSymmetricAlgebras
      (Opens.grothendieckTopology ↥(Spec R)) (tilde M))
    (B : SheafOfModules.TensorExteriorSymmetricAlgebras
      (Opens.grothendieckTopology ↥(Spec R)) (tilde N))
    (g : SheafOfModules.GradedAlgebra.UnitalHom A.symmetric B.symmetric)
    (hg : A.symmetricGenerator ≫ g.app 1 = tilde.map f ≫ B.symmetricGenerator) :
    tilde.map (ModuleCat.ofHom (R := R)
          (X := ModuleCat.of R (SymPow.symmetricPower n R M))
          (Y := ModuleCat.of R (SymPow.symmetricPower n R N)) (SymPow.symMap n f.hom)) ≫
        (tildeSymmetricPowerIso N B n).hom =
      (tildeSymmetricPowerIso M A n).hom ≫ g.app (n : ℤ)
```

**`Stacks.SymGraded.tildeSymmetricPowerIso_natural_symMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineSymmetricPowerCompare/Natural.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineSymmetricPowerCompare/Natural.lean#L129). The attribute's comment: “symmetric_power”.

> **The affine symmetric-power comparison is natural, for the canonical induced map.** This is
> `Stacks.SymGraded.tildeSymmetricPowerIso_natural` instantiated at `symmetricAlgebraHom`, the
> unital homomorphism the universal property of the symmetric algebra provides, so that the square
> is stated against a canonical map rather than a hypothesised one. The left-hand map is the
> associated sheaf of `SymPow.symMap`, the `n`-th symmetric power of `f`.

```lean
theorem tildeSymmetricPowerIso_natural_symMap (n : ℕ)
    (A : SheafOfModules.TensorExteriorSymmetricAlgebras
      (Opens.grothendieckTopology ↥(Spec R)) (tilde M))
    (B : SheafOfModules.TensorExteriorSymmetricAlgebras
      (Opens.grothendieckTopology ↥(Spec R)) (tilde N)) :
    tilde.map (ModuleCat.ofHom (R := R)
          (X := ModuleCat.of R (SymPow.symmetricPower n R M))
          (Y := ModuleCat.of R (SymPow.symmetricPower n R N)) (SymPow.symMap n f.hom)) ≫
        (tildeSymmetricPowerIso N B n).hom =
      (tildeSymmetricPowerIso M A n).hom ≫ (symmetricAlgebraHom f A B).app (n : ℤ)
```

**`AlgebraicGeometry.InternalHomTildeIso`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Modules/AffineInternalHom.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Modules/AffineInternalHom.lean#L104). The attribute's comment: “internal_hom”.

> An isomorphism from an affine internal Hom to the associated sheaf of the module of linear
> maps, together with the characterization that makes the isomorphism canonical.
>
> The inverse sends the global section associated to `f : M ⟶ N` to the section of the internal
> Hom represented by the sheaf morphism `tilde.map f`. This is the content of
> [Stacks, Tag 01I8].

```lean
structure InternalHomTildeIso (R : CommRingCat.{u}) (M N : ModuleCat.{u} R)
    (H : SheafHom (Spec R).sheaf (tilde M) (tilde N))
```

**`AlgebraicGeometry.internalHomTildeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Modules/AffineInternalHom.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Modules/AffineInternalHom.lean#L121). The attribute's comment: “internal_hom”. References: EGA I (1.3.12), “(ii)”.

> **Stacks Project, Tag 01I8 (`internal_hom`).**
>
> Let `M` and `N` be modules over a commutative ring `R`, with `M` finitely presented. The
> internal Hom between the associated sheaves of `M` and `N` on `Spec R` is canonically
> isomorphic to the sheaf associated to the `R`-module `Hom_R(M, N)`.

```lean
noncomputable def internalHomTildeIso (R : CommRingCat.{u})
    (M N : ModuleCat.{u} R)
    [Module.FinitePresentation R M]
    (H : SheafHom (Spec R).sheaf (tilde M) (tilde N)) :
    InternalHomTildeIso R M N H
```

**`AlgebraicGeometry.internalHomTildeIsoIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Modules/AffineInternalHom.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Modules/AffineInternalHom.lean#L156). The attribute's comment: “internal_hom”.

> **Stacks Project, Tag 01I8 (`internal_hom`).**
>
> The affine internal-Hom isomorphism itself: for `M` finitely presented, the internal Hom of the
> associated sheaves of `M` and `N` on `Spec R` is isomorphic to the associated sheaf of the
> `R`-module `Hom_R(M, N)`. This is the `iso` field of `internalHomTildeIso`, named so that the
> isomorphism asserted by the tag is readable as a type. It is canonical by
> `internalHomTildeIsoIso_inv_app_toOpen`.

```lean
noncomputable def internalHomTildeIsoIso (R : CommRingCat.{u}) (M N : ModuleCat.{u} R)
    [Module.FinitePresentation R M]
    (H : SheafHom (Spec R).sheaf (tilde M) (tilde N)) :
    H.obj ≅ tilde (ModuleCat.of R (M ⟶ N))
```

**`AlgebraicGeometry.internalHomTildeIsoIso_inv_app_toOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Modules/AffineInternalHom.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Modules/AffineInternalHom.lean#L166). The attribute's comment: “internal_hom”.

> **Stacks Project, Tag 01I8 (`internal_hom`).** The affine internal-Hom isomorphism is
> canonical: its inverse sends the global section associated to `f : M ⟶ N` to the section of the
> internal Hom represented by the sheaf morphism `tilde.map f`.

```lean
theorem internalHomTildeIsoIso_inv_app_toOpen (R : CommRingCat.{u}) (M N : ModuleCat.{u} R)
    [Module.FinitePresentation R M]
    (H : SheafHom (Spec R).sheaf (tilde M) (tilde N)) (f : M ⟶ N) :
    H.sectionsEquiv ⊤
        ((internalHomTildeIsoIso R M N H).inv.val.app (op ⊤)
          (tilde.toOpen (ModuleCat.of R (M ⟶ N)) ⊤ f)) =
      (tilde.map f).over ⊤
```

**`AlgebraicGeometry.internalHomTildeIso_natural_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Modules/AffineInternalHomNatural.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Modules/AffineInternalHomNatural.lean#L115). The attribute's comment: “internal_hom”.

> The affine internal-Hom comparison is natural in the target module: a morphism of internal
> Homs exhibited as post-composition with `tilde.map u` is carried to the associated sheaf of
> post-composition with `u`.

```lean
theorem internalHomTildeIso_natural_right (R : CommRingCat.{u}) (M N N' : ModuleCat.{u} R)
    [Module.FinitePresentation R M]
    (H : SheafHom (Spec R).sheaf (tilde M) (tilde N))
    (H' : SheafHom (Spec R).sheaf (tilde M) (tilde N'))
    (u : N ⟶ N') (m : H.obj ⟶ H'.obj)
    (hm : SheafHom.IsPostcomp (Spec R).sheaf (tilde.map u) H H' m) :
    m ≫ (internalHomTildeIso R M N' H').iso.hom =
      (internalHomTildeIso R M N H).iso.hom ≫ tilde.map (ModuleCat.homPostcomp M u)
```

**`AlgebraicGeometry.internalHomTildeIso_natural_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Modules/AffineInternalHomNatural.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Modules/AffineInternalHomNatural.lean#L150). The attribute's comment: “internal_hom”.

> The affine internal-Hom comparison is contravariantly natural in the source module: a
> morphism of internal Homs exhibited as pre-composition with `tilde.map β` is carried to the
> associated sheaf of pre-composition with `β`.

```lean
theorem internalHomTildeIso_natural_left (R : CommRingCat.{u}) (M M' N : ModuleCat.{u} R)
    [Module.FinitePresentation R M] [Module.FinitePresentation R M']
    (H : SheafHom (Spec R).sheaf (tilde M) (tilde N))
    (H' : SheafHom (Spec R).sheaf (tilde M') (tilde N))
    (β : M' ⟶ M) (m : H.obj ⟶ H'.obj)
    (hm : SheafHom.IsPrecomp (Spec R).sheaf (tilde.map β) H H' m) :
    m ≫ (internalHomTildeIso R M' N H').iso.hom =
      (internalHomTildeIso R M N H).iso.hom ≫ tilde.map (ModuleCat.homPrecomp N β)
```

**`AlgebraicGeometry.tildeTensorPowerIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Modules/TildeTensorPower.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Modules/TildeTensorPower.lean#L168). The attribute's comment: “tensor_power”.

> **Stacks Project, Tag 01I8 (tensor-power part).** The associated sheaf of a tensor power is
> canonically the tensor power of the associated sheaf.

```lean
noncomputable def tildeTensorPowerIso (R : CommRingCat.{u}) (M : ModuleCat.{u} R) :
    (n : ℕ) → (tilde (ModuleCat.of R (TensorPower R n M)) ≅ specTildeTensorPower R M n)
```

**`AlgebraicGeometry.tildeTensorPowerIso_hom_tprod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Modules/TildeTensorPower.lean, line 344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Modules/TildeTensorPower.lean#L344). The attribute's comment: “tensor_power”.

> **Stacks Project, Tag 01I8 (tensor-power part).** The canonical affine tensor-power
> comparison carries a pure tensor to the tensor product of its associated global sections.

```lean
theorem tildeTensorPowerIso_hom_tprod (R : CommRingCat.{u}) (M : ModuleCat.{u} R) (n : ℕ)
    (a : Fin n → M) :
    (tildeTensorPowerIso R M n).hom.val.app (specGlobalOpen R)
        ((tilde.toOpen (ModuleCat.of R (TensorPower R n M)) ⊤).hom
          (PiTensorProduct.tprod R a)) =
      tildeTensorPowerSection R M n a
```

**`AlgebraicGeometry.tildeTensorPowerIso_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Modules/TildeTensorPower.lean, line 554](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Modules/TildeTensorPower.lean#L554). The attribute's comment: “tensor_power”.

> **Stacks Project, Tag 01I8 (tensor-power part).** Naturality of the affine tensor-power
> comparison. The right-hand map is the degree-`n` component of a unital graded-algebra map
> extending `tilde.map f` on degree-one generators; the universal property of the tensor algebra
> makes such a map unique, so quantifying over it is a statement about the canonical one.

```lean
theorem tildeTensorPowerIso_natural
    (hg : (specTildeAlgebras R M).tensorGenerator ≫ g.app 1 =
      tilde.map f ≫ (specTildeAlgebras R N).tensorGenerator) (n : ℕ) :
    tilde.map (ModuleCat.ofHom (PiTensorProduct.map (fun _ : Fin n => f.hom))) ≫
        (tildeTensorPowerIso R N n).hom =
      (tildeTensorPowerIso R M n).hom ≫ ((specTildeAlgebras R M).tensorPieceIso n).inv ≫
        g.app (n : ℤ) ≫ ((specTildeAlgebras R N).tensorPieceIso n).hom
```

**`AlgebraicGeometry.tildeTensorPowerIso_natural_piTensorProductMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Modules/TildeTensorPower.lean, line 592](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Modules/TildeTensorPower.lean#L592). The attribute's comment: “tensor_power”.

> **Stacks Project, Tag 01I8 (tensor-power part).** Naturality of the affine tensor-power
> comparison against the canonical induced map, rather than against a hypothesised one: this is
> `tildeTensorPowerIso_natural` instantiated at `specTildeTensorAlgebraMap`, the unital
> graded-algebra map the universal property of the tensor algebra provides. The left-hand map is
> the associated sheaf of `PiTensorProduct.map`, the `n`-fold tensor power of `f`.

```lean
theorem tildeTensorPowerIso_natural_piTensorProductMap (n : ℕ) :
    tilde.map (ModuleCat.ofHom (PiTensorProduct.map (fun _ : Fin n => f.hom))) ≫
        (tildeTensorPowerIso R N n).hom =
      (tildeTensorPowerIso R M n).hom ≫ ((specTildeAlgebras R M).tensorPieceIso n).inv ≫
        (specTildeTensorAlgebraMap R f).app (n : ℤ) ≫
          ((specTildeAlgebras R N).tensorPieceIso n).hom
```

**`AlgebraicGeometry.tildeTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/AffineTensor.lean, line 407](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/AffineTensor.lean#L407). The attribute's comment: “tensor_product”. References: EGA I (1.3.12), “(i)”.

> For modules `M` and `N` over `R`, there is a canonical isomorphism
> `(M ⊗[R] N)~ ≅ M~ ⊗_{𝒪_(Spec R)} N~`.

```lean
noncomputable def tildeTensorIso (R : CommRingCat.{u})
    (M N : ModuleCat.{u} R) :
    tilde (M ⊗ N) ≅
      specTensorSheaf R (tilde M) (tilde N)
```

**`AlgebraicGeometry.tildeTensorIso_hom_tmul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/AffineTensor.lean, line 417](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/AffineTensor.lean#L417). The attribute's comment: “tensor_product”.

> The canonical isomorphism sends a pure tensor, under the
> tilde--global-sections adjunction, to the section obtained by tensoring the two
> canonical global sections and applying the sheafification unit.

```lean
theorem tildeTensorIso_hom_tmul (R : CommRingCat.{u})
    (M N : ModuleCat.{u} R) (m : M) (n : N) :
    (((tilde.adjunction (R := R)).homEquiv (M ⊗ N)
      (specTensorSheaf R (tilde M) (tilde N))) (tildeTensorIso R M N).hom).hom
        (TensorProduct.tmul R m n) =
      ((Stacks.SheafOfModules.TensorSheafification.toSheafify (Spec R).presheaf
        (isSheaf_specStructureRingPresheaf R)
        (specTensorPresheaf R (tilde M) (tilde N))).app (.op ⊤)).hom
        (TensorProduct.tmul ((Spec R).presheaf.obj (.op ⊤))
          ((tilde.toOpen M ⊤).hom m) ((tilde.toOpen N ⊤).hom n))
```

**`AlgebraicGeometry.tildeTensorIso_eq_of_hom_tmul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/AffineTensor.lean, line 433](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/AffineTensor.lean#L433). The attribute's comment: “tensor_product”.

> The comparison is canonical: it is the *only* isomorphism `(M ⊗ N)~ ≅ M~ ⊗ N~` satisfying
> the pure-tensor equation `tildeTensorIso_hom_tmul`, so `tildeTensorIso` does not depend on the
> choice `Classical.choose` makes to produce it.

```lean
theorem tildeTensorIso_eq_of_hom_tmul (R : CommRingCat.{u})
    (M N : ModuleCat.{u} R)
    (e : tilde (M ⊗ N) ≅ specTensorSheaf R (tilde M) (tilde N))
    (he : ∀ (m : M) (n : N),
      (((tilde.adjunction (R := R)).homEquiv (M ⊗ N)
        (specTensorSheaf R (tilde M) (tilde N))) e.hom).hom
          (TensorProduct.tmul R m n) =
        ((Stacks.SheafOfModules.TensorSheafification.toSheafify (Spec R).presheaf
          (isSheaf_specStructureRingPresheaf R)
          (specTensorPresheaf R (tilde M) (tilde N))).app (.op ⊤)).hom
          (TensorProduct.tmul ((Spec R).presheaf.obj (.op ⊤))
            ((tilde.toOpen M ⊤).hom m) ((tilde.toOpen N ⊤).hom n))) :
    e = tildeTensorIso R M N
```

**`AlgebraicGeometry.tildeTensorIso_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/AffineTensor.lean, line 455](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/AffineTensor.lean#L455). The attribute's comment: “tensor_product”.

> The canonical tensor comparison is natural in both modules.

```lean
theorem tildeTensorIso_natural (R : CommRingCat.{u})
    {M M' N N' : ModuleCat.{u} R} (f : M ⟶ M') (g : N ⟶ N') :
    tilde.map (f ⊗ₘ g) ≫ (tildeTensorIso R M' N').hom =
      (tildeTensorIso R M N).hom ≫ tildeTensorSheafMap R f g
```

**`Stacks.AssociatedSheaf.associatedSheafTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/AssociatedSheaf/Tensor.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/AssociatedSheaf/Tensor.lean#L141). The attribute's comment: “construction (3) commutes with the tensor product, on an arbitrary ringed space”.

> **Construction (3) carries the tensor product of `R`-modules to the tensor product of
> sheaves of modules:** `ℱ_{M ⊗_R N} ≅ ℱ_M ⊗_{𝒪_X} ℱ_N`, on an arbitrary ringed space.
>
> This is the clause of Tag 01I8 that the determinant argument of Tag 0FJN needs on the
> trivialising open of Tag 08BL rather than on an affine scheme.

```lean
def associatedSheafTensorIso (M N : ModuleCat.{u} R) :
    associatedSheaf X α (M ⊗ N) ≅
      ((Stacks.SheafOfModules.Tensor.sheafTensor
        ⟨X.presheaf, Presheaf.isSheaf_of_isSheaf_comp _ X.presheaf
          (forget₂ CommRingCat RingCat) (structureSheafRing X).property⟩).obj
        (associatedSheaf X α M)).obj (associatedSheaf X α N)
```

## Tag 01I9, a lemma

[Tag 01I9](https://stacks.math.columbia.edu/tag/01I9) in the Stacks Project.

**`Stacks.AlgebraicGeometry.AffineBaseChange.tilde_map_comp_pushforwardTildeIso_inv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineBaseChange/StructureSheaf.lean, line 327](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineBaseChange/StructureSheaf.lean#L327). The attribute's comment: “affine_pushforward_tilde at the ring itself: the comparison carries the structure map of φ to the structure morphism of Spec φ”.

> The associated sheaf of a map of `R`-modules `R ⟶ S` sending `1` to `1`, followed by the
> inverse of the comparison identifying the direct image along `Spec φ` of the associated sheaf of
> `S` with the associated sheaf of `S` restricted to an `R`-module, is the structure morphism
> `𝒪_{Spec R} ⟶ (Spec φ)_* 𝒪_{Spec S}`.

```lean
theorem tilde_map_comp_pushforwardTildeIso_inv
    (u : ModuleCat.of R R ⟶ (ModuleCat.restrictScalars φ.hom).obj (ModuleCat.of S S))
    (hu : u.hom (1 : R) = (1 : S)) :
    (tilde.functor R).map u ≫ ((pushforwardTildeIso R S φ).app (ModuleCat.of S S)).inv =
      structureUnitHom (Spec.map φ)
```

**`AlgebraicGeometry.pullbackTildeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/QuasiCoherent/AffineTilde.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/QuasiCoherent/AffineTilde.lean#L87). The attribute's comment: “affine_pullback_tilde”.

> Pullback along the map of affine schemes induced by `f : R ⟶ S` carries the associated sheaf
> of an `R`-module to the associated sheaf of its extension of scalars to `S`, naturally in the
> module.

```lean
public noncomputable def pullbackTildeIso (R S : CommRingCat.{u}) (f : R ⟶ S) :
    tilde.functor R ⋙ Scheme.Modules.pullback (Spec.map f) ≅
      ModuleCat.extendScalars f.hom ⋙ tilde.functor S
```

**`AlgebraicGeometry.pullbackTildeIso_hom_app_unit_toOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/QuasiCoherent/AffineTilde.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/QuasiCoherent/AffineTilde.lean#L99). The attribute's comment: “affine_pullback_tilde”.

> The canonical affine pullback comparison sends the pullback of the global
> section represented by `m` to the global section represented by `1 ⊗ m`.
> Here the first map is the pullback--pushforward adjunction unit.

```lean
public theorem pullbackTildeIso_hom_app_unit_toOpen
    (R S : CommRingCat.{u}) (f : R ⟶ S) (M : ModuleCat R) (m : M) :
    ((pullbackTildeIso R S f).hom.app M).val.app (.op ⊤)
      (((Scheme.Modules.pullbackPushforwardAdjunction (Spec.map f)).unit.app
        (tilde M)).val.app (.op ⊤) (tilde.toOpen M ⊤ m)) =
    tilde.toOpen ((ModuleCat.extendScalars f.hom).obj M) ⊤
      ((1 : S) ⊗ₜ[R, f.hom] m)
```

**`AlgebraicGeometry.pushforwardTildeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/QuasiCoherent/AffineTilde.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/QuasiCoherent/AffineTilde.lean#L155). The attribute's comment: “affine_pushforward_tilde”.

> Pushforward along the map of affine schemes induced by `φ : R ⟶ S` carries the associated
> sheaf of an `S`-module to the associated sheaf of its restriction of scalars along `φ`, naturally
> in the module.

```lean
public noncomputable def pushforwardTildeIso (R S : CommRingCat.{u}) (φ : R ⟶ S) :
    tilde.functor S ⋙ Scheme.Modules.pushforward (Spec.map φ) ≅
      ModuleCat.restrictScalars φ.hom ⋙ tilde.functor R
```

**`AlgebraicGeometry.pushforwardTildeIso_hom_app_toOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/QuasiCoherent/AffineTilde.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/QuasiCoherent/AffineTilde.lean#L193). The attribute's comment: “affine_pushforward_tilde”.

> The canonical affine pushforward comparison is normalized by the canonical identifications of
> a module with the global sections of its associated sheaf: its component at `N` sends the global
> section represented by `n` on `Spec S` to the global section represented by the same element of
> the restricted `R`-module on `Spec R`.

```lean
public theorem pushforwardTildeIso_hom_app_toOpen
    (R S : CommRingCat.{u}) (φ : R ⟶ S) (N : ModuleCat S) (n : N) :
    ((pushforwardTildeIso R S φ).hom.app N).val.app (Opposite.op (⊤ : (Spec R).Opens))
      (tilde.toOpen N (⊤ : (Spec S).Opens) n) =
    tilde.toOpen ((ModuleCat.restrictScalars φ.hom).obj N) (⊤ : (Spec R).Opens) n
```

**`Deformation.Artin.SectionsSheaf.tildePullbackIso_id_hom_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/SectionsFirstFactorIdentity.lean, line 447](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/SectionsFirstFactorIdentity.lean#L447). The attribute's comment: “the affine base-change comparison at the identity ring map: the pullback of the associated sheaf along Spec of the identity ring map is the identity law for pullback followed by the associated sheaf of m ↦ 1 ⊗ m”.

> **The affine base-change comparison of [Stacks, Tag 01I9] at the identity ring map.** The
> isomorphism `(Spec (𝟙 A))^* M̃ ≅ (A ⊗_A M)~` is the identity law for pullback followed by the
> associated sheaf of the unit `m ↦ 1 ⊗ m` of extension of scalars.
>
> Neither factor is an identity: `A ⊗_A M` is not `M` and `(Spec (𝟙 A))^*` is an abstract left
> adjoint. What the statement says is that the comparison, which is built by uniqueness of left
> adjoints and so has no formula, *is* the composite of the two canonical maps that are available.
>
> The proof is the uniqueness itself:
> `CategoryTheory.Adjunction.unit_leftAdjointUniq_hom_app` evaluates the comparison after the unit
> of `tildePullbackAdjunction (𝟙 A)`, and `eq_of_unit_comp` says that this determines a morphism
> out of `(tilde.functor A ⋙ (Spec (𝟙 A))^*).obj M`; the four lemmas above evaluate the
> right-hand side there.

```lean
theorem tildePullbackIso_id_hom_app (M : ModuleCat.{u} A) :
    (tildePullbackIso (𝟙 A)).hom.app M =
      ((Scheme.Modules.pullbackCongr (Spec.map_id A)).hom.app ((tilde.functor A).obj M) ≫
          (Scheme.Modules.pullbackId (Spec A)).hom.app ((tilde.functor A).obj M)) ≫
        (tilde.functor A).map (extendUnitId M)
```

## Tag 01IA, a lemma

[Tag 01IA](https://stacks.math.columbia.edu/tag/01IA) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.Modules.isIso_fromTildeΓ_of_isQuasicoherent`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Modules.isIso_fromTildeΓ_of_isQuasicoherent#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L151) (StacksFrontier). References: EGA I (1.4.1), “c ⇒ a for V = Spec A”; EGA I (1.4.3), “special case”; EGA I (4.1.1), “affine case”; EGA I (10.10.1), “Representation clause”; EGA III (6.4.1), “special case”; SGA 6 II (2.4.3), “c), special case”.

## Tag 01IB, a lemma

[Tag 01IB](https://stacks.math.columbia.edu/tag/01IB) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.tildeEquiv`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.tildeEquiv#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L157) (StacksFrontier). References: EGA I (1.4.3), “special case”; EGA II (1.4.3), “special case”.

## Tag 01IC, a lemma

[Tag 01IC](https://stacks.math.columbia.edu/tag/01IC) in the Stacks Project.

**`Stacks.DerivedQCoh.abelianQuasiCoherent`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/QuasiCoherentAbelian.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/QuasiCoherentAbelian.lean#L121). The attribute's comment: “abelian category”.

> **Stacks Project, Tag 01IC (abelian category).** The quasi-coherent modules on `Spec R` form
> an abelian category, kernels, cokernels and finite products being computed as in all
> `𝒪_{Spec R}`-modules.

```lean
instance abelianQuasiCoherent :
    Abelian (SheafOfModules.isQuasicoherent (Spec R).ringCatSheaf).FullSubcategory
```

**`AlgebraicGeometry.Scheme.Modules.isQuasicoherent_cokernel`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/QuasiCoherent/Affine.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/QuasiCoherent/Affine.lean#L85). The attribute's comment: “cokernel”. References: EGA I (4.1.1), “affine, cokernel”.

> **Stacks Project, Tag 01IC (cokernel).** The cokernel of a morphism between
> quasi-coherent modules on an affine scheme is quasi-coherent.

```lean
public instance isQuasicoherent_cokernel {X : Scheme.{u}} [IsAffine X]
    {M N : X.Modules} [M.IsQuasicoherent] [N.IsQuasicoherent] (f : M ⟶ N) :
    (cokernel f).IsQuasicoherent
```

**`Stacks.AffineTilde.isQuasicoherent_kernel`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherentRelative/TildeExact.lean, line 317](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherentRelative/TildeExact.lean#L317). The attribute's comment: “kernel”. References: EGA I (4.1.1), “affine, kernel”.

> **Stacks Project, Tag 01IC (kernel).** The kernel of a morphism of quasi-coherent modules
> on an affine scheme is quasi-coherent. The cokernel half is
> `AlgebraicGeometry.Scheme.Modules.isQuasicoherent_cokernel`.

```lean
instance isQuasicoherent_kernel {X : Scheme.{u}} [IsAffine X] {M N : X.Modules}
    [M.IsQuasicoherent] [N.IsQuasicoherent] (f : M ⟶ N) : (kernel f).IsQuasicoherent
```

Declarations registered for the tag:

- [`Stacks.AlgebraicGeometry.QcohLimits.isQuasicoherent_kernel`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QcohLimits/Basic.lean#L53), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/QuasiCoherent/General.lean, line 25](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/QuasiCoherent/General.lean#L25) (StacksFrontier): “kernel”.

## Tag 01ID, a lemma

[Tag 01ID](https://stacks.math.columbia.edu/tag/01ID) in the Stacks Project.

**`Stacks.AlgebraicGeometry.QuasicoherentColimits.isQuasicoherent_of_isColimit_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineQcohPushforward/Colimits.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineQcohPushforward/Colimits.lean#L71). The attribute's comment: “colimits”.

> On a spectrum, the point of a colimit cocone of quasi-coherent modules is
> quasi-coherent.

```lean
theorem isQuasicoherent_of_isColimit_spec (R : CommRingCat.{u})
    [HasColimitsOfShape K (ModuleCat.{u} R)] {D : K ⥤ (Spec R).Modules}
    (hD : ∀ k, (D.obj k).IsQuasicoherent) {c : Cocone D} (hc : IsColimit c) :
    c.pt.IsQuasicoherent
```

**`Stacks.AlgebraicGeometry.QuasicoherentColimits.isQuasicoherent_sigma`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineQcohPushforward/Colimits.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineQcohPushforward/Colimits.lean#L170). The attribute's comment: “direct sums”.

> A coproduct of quasi-coherent modules is quasi-coherent.

```lean
instance isQuasicoherent_sigma {X : Scheme.{u}} {I : Type u} (M : I → X.Modules)
    [∀ i, (M i).IsQuasicoherent] : (∐ M).IsQuasicoherent
```

## Tag 01IE, a lemma

[Tag 01IE](https://stacks.math.columbia.edu/tag/01IE) in the Stacks Project.

**`Stacks.AlgebraicGeometry.QcohExtension.isQuasicoherent_X₂_of_shortExact_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QcohShortExact/QcohExtension.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QcohShortExact/QcohExtension.lean#L146). References: EGA III (1.4.17), “affine case”.

> **[Stacks, Tag 01IE], the extension case.** If the two outer terms of a short exact sequence
> of `𝒪_{Spec R}`-modules are quasi-coherent then so is the middle one.

```lean
theorem isQuasicoherent_X₂_of_shortExact_spec (S : ShortComplex (Spec R).Modules)
    (hS : S.ShortExact) (h₁ : S.X₁.IsQuasicoherent) (h₃ : S.X₃.IsQuasicoherent) :
    S.X₂.IsQuasicoherent
```

**`Stacks.AlgebraicGeometry.QcohExtension.isQuasicoherent_X₁_of_shortExact_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QcohShortExact/QcohExtension.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QcohShortExact/QcohExtension.lean#L168).

> **[Stacks, Tag 01IE], the kernel case.** If the last two terms of a short exact sequence of
> `𝒪_{Spec R}`-modules are quasi-coherent then so is the first: it is the kernel of the last
> map.

```lean
theorem isQuasicoherent_X₁_of_shortExact_spec (S : ShortComplex (Spec R).Modules)
    (hS : S.ShortExact) (h₂ : S.X₂.IsQuasicoherent) (h₃ : S.X₃.IsQuasicoherent) :
    S.X₁.IsQuasicoherent
```

**`Stacks.AlgebraicGeometry.QcohExtension.isQuasicoherent_X₃_of_shortExact_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QcohShortExact/QcohExtension.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QcohShortExact/QcohExtension.lean#L181).

> **[Stacks, Tag 01IE], the cokernel case.** If the first two terms of a short exact sequence
> of `𝒪_{Spec R}`-modules are quasi-coherent then so is the last: it is the cokernel of the first
> map, and [Stacks, Tag 01IC] applies because `Spec R` is affine.

```lean
theorem isQuasicoherent_X₃_of_shortExact_spec (S : ShortComplex (Spec R).Modules)
    (hS : S.ShortExact) (h₁ : S.X₁.IsQuasicoherent) (h₂ : S.X₂.IsQuasicoherent) :
    S.X₃.IsQuasicoherent
```

**`Stacks.AlgebraicGeometry.QuasicoherentExtension.isQuasicoherent_left_of_shortExact`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasicoherentExtension/Basic.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasicoherentExtension/Basic.lean#L157). The attribute's comment: “left term”.

> In a short exact sequence of modules on an affine scheme, the left term is quasi-coherent if
> the middle and right terms are.

```lean
lemma isQuasicoherent_left_of_shortExact {X : Scheme.{u}} [IsAffine X]
    (S : ShortComplex X.Modules) (hS : S.ShortExact)
    [S.X₂.IsQuasicoherent] [S.X₃.IsQuasicoherent] :
    S.X₁.IsQuasicoherent
```

**`Stacks.AlgebraicGeometry.QuasicoherentExtension.isQuasicoherent_middle_of_shortExact`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasicoherentExtension/Basic.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasicoherentExtension/Basic.lean#L168). The attribute's comment: “middle term”.

> In a short exact sequence of modules on an affine scheme, the middle term is quasi-coherent if
> both outer terms are.

```lean
lemma isQuasicoherent_middle_of_shortExact {X : Scheme.{u}} [IsAffine X]
    (S : ShortComplex X.Modules) (hS : S.ShortExact)
    [S.X₁.IsQuasicoherent] [S.X₃.IsQuasicoherent] :
    S.X₂.IsQuasicoherent
```

**`Stacks.AlgebraicGeometry.QuasicoherentExtension.isQuasicoherent_right_of_shortExact`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasicoherentExtension/Basic.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasicoherentExtension/Basic.lean#L190). The attribute's comment: “right term”.

> In a short exact sequence of modules on an affine scheme, the right term is quasi-coherent if
> the left and middle terms are.

```lean
lemma isQuasicoherent_right_of_shortExact {X : Scheme.{u}} [IsAffine X]
    (S : ShortComplex X.Modules) (hS : S.ShortExact)
    [S.X₁.IsQuasicoherent] [S.X₂.IsQuasicoherent] :
    S.X₃.IsQuasicoherent
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 26.7, Tag 01I6](https://stacks.math.columbia.edu/tag/01I6)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
