---
declaration: section
origin: cited
lean: AlgebraicGeometry.SmallEtale.LAdicSheaf, AlgebraicGeometry.SmallEtale.LAdicSheaf.Hom, AlgebraicGeometry.SmallEtale.LAdicSheaf.IsLisse, AlgebraicGeometry.SmallEtale.exists_lAdicSheaf_of_eventuallyConstant_reductions, Stacks.EtaleCohomology.LAdicSheaf.normalEpiCategory, Stacks.EtaleCohomology.LAdicSheaf.hasKernels, Stacks.EtaleCohomology.LAdicSheaf.normalMonoCategory, Stacks.EtaleCohomology.LAdicSheaf.abelian
statement: formalized
proof: formalized
---

# 64.18 On l-adic sheaves

Section 64.18 of the Stacks Project, [Tag 03UL](https://stacks.math.columbia.edu/tag/03UL). 6 tags here are carried by 33 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03UM, a definition

[Tag 03UM](https://stacks.math.columbia.edu/tag/03UM) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.LAdicSheaf`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/LAdicSheaves.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/LAdicSheaves.lean#L134). The attribute's comment: “objects”. References: SGA 5 V (3.1), “ℓ-adic étale case”; SGA 4½ Rapport (2.1), “Z\_ℓ-sheaf definition”; SGA 5 V (3.1.1), “A=Z\_ℓ, J=(ℓ), étale site”; SGA 5 VI (1.1.1); SGA 5 VI (1.2), “Z\_ℓ-sheaf definition”.

> **Stacks 03UM.** An ℓ-adic sheaf is an inverse system of constructible `ℤ/ℓⁿℤ`-module
> sheaves whose successive scalar reductions are isomorphisms.

```lean
public structure LAdicSheaf [IsNoetherian X.obj] [Fact ℓ.Prime]
```

**`AlgebraicGeometry.SmallEtale.LAdicSheaf.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/LAdicSheaves.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/LAdicSheaves.lean#L152). The attribute's comment: “morphisms”. References: SGA 5 V (3.1), “morphisms, ℓ-adic case”; SGA 5 VI (1.1.1), “morphisms”; SGA 5 VI (1.2), “morphisms”; SGA 4½ Rapport (2.6), “hom(F,G)”.

> **Stacks 03UM.** A morphism of ℓ-adic sheaves is a compatible family of morphisms at the
> finite levels.

```lean
public structure LAdicSheaf.Hom [IsNoetherian X.obj] [Fact ℓ.Prime]
    (F G : LAdicSheaf.{u, m} B X ℓ)
```

**`AlgebraicGeometry.SmallEtale.LAdicSheaf.IsLisse`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/LAdicSheaves.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/LAdicSheaves.lean#L188). The attribute's comment: “lisse”.

> **Stacks 03UM.** A lisse ℓ-adic sheaf has locally constant sheaves at every finite
> level.

```lean
public abbrev LAdicSheaf.IsLisse [IsNoetherian X.obj] [Fact ℓ.Prime]
    (F : LAdicSheaf.{u, m} B X ℓ) : Prop
```

## Tag 03UN, a lemma

[Tag 03UN](https://stacks.math.columbia.edu/tag/03UN) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.exists_lAdicSheaf_of_eventuallyConstant_reductions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/LAdicEventuallyConstant.lean, line 1018](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/LAdicEventuallyConstant.lean#L1018). References: SGA 4½ Rapport (2.6), “ess.const ⇒ Zℓ-sheaf”.

> **Stacks 03UN.** Eventually constant reductions of a constructible inverse system give an
> ℓ-adic sheaf whose levels are the stable values of those reductions.

```lean
public theorem exists_lAdicSheaf_of_eventuallyConstant_reductions
    [IsNoetherian X.obj] [Fact ℓ.Prime]
    (G : ∀ n, FiniteLevelSheaf.{u, m} B X ℓ n)
    (t : ∀ n, G (n + 1) ⟶ (G n).restrictScalars B X ℓ n)
    (hG : ∀ n, IsConstructibleModuleSheaf B X (ZMod (ℓ ^ (n + 1))) (G n))
    (heventually : ∀ (k : ℕ), ∃ (N : ℕ), ∀ (n : ℕ), N ≤ n → (h : k ≤ n) →
      IsIso ((Sheaf.composeAndSheafify
        (SmallEtale.topology B X.obj X.property)
        (ModuleCat.extendScalars.{0, 0, m}
          (ZMod.castHom (pow_dvd_pow ℓ (by omega : k + 1 ≤ n + 2)) _ :
            ZMod (ℓ ^ (n + 2)) →+* ZMod (ℓ ^ (k + 1))))).map (t n))) :
    ∃ F : LAdicSheaf.{u, m} B X ℓ, ∃ N : ℕ → ℕ,
      ∃ e : ∀ (k n : ℕ), N k ≤ n → (h : k ≤ n) →
        F.level k ≅ FiniteLevelSheaf.reduceTo B X ℓ n k h (G n),
      (∀ (k n : ℕ) (hn : N k ≤ n) (h : k ≤ n),
        (e k (n + 1) (by omega) (by omega)).hom ≫
          ((Sheaf.composeAndSheafify
            (SmallEtale.topology B X.obj X.property)
            (ModuleCat.extendScalars.{0, 0, m}
              (ZMod.castHom (pow_dvd_pow ℓ (by omega : k + 1 ≤ n + 2)) _ :
                ZMod (ℓ ^ (n + 2)) →+* ZMod (ℓ ^ (k + 1))))).map (t n)) ≫
          (FiniteLevelSheaf.canonicalRestrictionComparison B X ℓ n k h (G n)) =
          (e k n hn h).hom) ∧
      (∀ (k n : ℕ) (hn₁ : N k ≤ n) (hn₂ : N (k + 1) ≤ n)
          (h : k + 1 ≤ n),
        F.transition k ≫
          (sheafCompose (SmallEtale.topology B X.obj X.property)
            (ModuleCat.restrictScalars.{m, 0, 0}
              (finiteLevelRingHom ℓ k))).map
            ((e k n hn₁ (by omega)).hom) =
        (e (k + 1) n hn₂ h).hom ≫
          (FiniteLevelSheaf.canonicalReductionTransition B X ℓ n k h (G n)))
```

## Tag 03UO, a lemma

[Tag 03UO](https://stacks.math.columbia.edu/tag/03UO) in the Stacks Project.

**`Stacks.EtaleCohomology.LAdicSheaf.normalEpiCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/Abelian.lean, line 214](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/Abelian.lean#L214). The attribute's comment: “every epimorphism is a cokernel”.

> **Stacks 03UO**, normality of epimorphisms: every epimorphism of ℓ-adic sheaves is a
> cokernel.

```lean
public instance normalEpiCategory : IsNormalEpiCategory (LAdicSheaf.{u, u + 1} B X ℓ)
```

**`Stacks.EtaleCohomology.LAdicSheaf.hasKernels`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/Abelian.lean, line 278](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/Abelian.lean#L278). The attribute's comment: “kernels”.

> **Stacks 03UO**, the kernel part: the category of ℓ-adic sheaves on a Noetherian scheme has
> kernels. The kernel of a morphism is the kernel of the epimorphism in its image
> factorisation.

```lean
public instance hasKernels : HasKernels (LAdicSheaf.{u, u + 1} B X ℓ)
```

**`Stacks.EtaleCohomology.LAdicSheaf.normalMonoCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/Abelian.lean, line 291](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/Abelian.lean#L291). The attribute's comment: “every monomorphism is a kernel”.

> **Stacks 03UO**, normality of monomorphisms: every monomorphism of ℓ-adic sheaves is a
> kernel. In the image factorisation of a monomorphism the epimorphic half is also a
> monomorphism, hence an isomorphism, so the monomorphism is the kernel the factorisation
> provides.

```lean
public instance normalMonoCategory : IsNormalMonoCategory (LAdicSheaf.{u, u + 1} B X ℓ)
```

**`Stacks.EtaleCohomology.LAdicSheaf.abelian`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/Abelian.lean, line 311](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/Abelian.lean#L311). References: SGA 5 V (3.2), “abelian”; SGA 4½ Rapport (2.6), “abelian”; SGA 5 VI (1.1.3), “special case”.

> **Stacks 03UO.** The category of `ℤ_ℓ`-sheaves on a Noetherian scheme is abelian: it is
> preadditive with finite biproducts, has kernels and cokernels, and every monomorphism is a
> kernel while every epimorphism is a cokernel.

```lean
public instance abelian : Abelian (LAdicSheaf.{u, u + 1} B X ℓ)
```

**`Stacks.EtaleCohomology.LAdicSheaf.hasZeroObject`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/Additive.lean, line 278](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/Additive.lean#L278). The attribute's comment: “zero object”.

> The category of ℓ-adic sheaves has a zero object.

```lean
public instance LAdicSheaf.hasZeroObject : HasZeroObject (LAdicSheaf B X ℓ)
```

**`Stacks.EtaleCohomology.LAdicSheaf.hasFiniteBiproducts`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/Additive.lean, line 399](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/Additive.lean#L399). The attribute's comment: “additive: finite biproducts, formed levelwise”.

> **Stacks 03UO**, the additive part: the category of ℓ-adic sheaves on a Noetherian scheme
> has finite biproducts, the biproduct being formed levelwise.

```lean
public instance hasFiniteBiproducts : HasFiniteBiproducts (LAdicSheaf B X ℓ)
```

**`Stacks.EtaleCohomology.LAdicSheaf.hasCokernels`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/Additive.lean, line 476](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/Additive.lean#L476). The attribute's comment: “cokernels, formed levelwise”.

> **Stacks 03UO**, the cokernel part: the category of ℓ-adic sheaves on a Noetherian scheme has
> cokernels, formed levelwise.

```lean
public instance hasCokernels : HasCokernels (LAdicSheaf B X ℓ)
```

**`Stacks.EtaleCohomology.LAdicSheaf.normalMono_of_app_mono`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/Normality.lean, line 154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/Normality.lean#L154). The attribute's comment: “monomorphisms with monomorphic components are kernels, of the levelwise cokernel”.

> A morphism of ℓ-adic sheaves whose components are monomorphisms is the kernel of its
> levelwise cokernel.

```lean
public def normalMono_of_app_mono {F G : LAdicSheaf.{u, u + 1} B X ℓ} (f : F ⟶ G)
    (hf : ∀ n, Mono (f.app n)) : NormalMono f
```

**`Stacks.EtaleCohomology.LAdicSheaf.normalEpi_of_epi_kernelLift`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/Normality.lean, line 198](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/Normality.lean#L198). The attribute's comment: “epimorphisms whose levelwise kernel comparisons are epimorphisms are cokernels, of the morphism those comparisons compare to”.

> An epimorphism of ℓ-adic sheaves is the cokernel of a morphism killed by it whose levelwise
> kernel comparisons are epimorphisms.

```lean
public def normalEpi_of_epi_kernelLift {K F G : LAdicSheaf.{u, u + 1} B X ℓ} (i : K ⟶ F)
    (f : F ⟶ G) [Epi f] (w : i ≫ f = 0)
    (hi : ∀ n, Epi (kernel.lift (f.app n) (i.app n) (comp_eq_zero_app i f w n))) :
    NormalEpi f
```

**`AlgebraicGeometry.SmallEtale.LAdicSheaf.preadditive`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/LAdicSheafPreadditive.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/LAdicSheafPreadditive.lean#L147). The attribute's comment: “preadditive”.

> **Stacks 03UO.** ℓ-adic sheaves form a preadditive category: morphisms add levelwise and
> composition is bilinear.

```lean
public instance LAdicSheaf.preadditive : Preadditive (LAdicSheaf.{u, m} B X ℓ)
```

## Tag 03UQ, a remark

[Tag 03UQ](https://stacks.math.columbia.edu/tag/03UQ) in the Stacks Project.

**`Stacks.EtaleCohomology.finite_finiteLevelStalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/FiniteLevelStalk.lean, line 384](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/FiniteLevelStalk.lean#L384). The attribute's comment: “finite\_level\_stalks”.

> Every finite-level stalk of an ℓ-adic sheaf at a geometric point is finite.

```lean
public theorem finite_finiteLevelStalk (F : LAdicSheaf B X ℓ) (s : GeometricPoint X.1) (n : ℕ) :
    Finite (finiteLevelStalk B X ℓ F s n)
```

**`Stacks.EtaleCohomology.finiteLevelStalkTransition_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/FiniteLevelStalk.lean, line 403](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/FiniteLevelStalk.lean#L403). The attribute's comment: “finite\_level\_stalks”.

> Each transition between consecutive finite-level stalks is surjective.

```lean
public theorem finiteLevelStalkTransition_surjective (F : LAdicSheaf B X ℓ)
    (s : GeometricPoint X.1) (n : ℕ) :
    Function.Surjective (finiteLevelStalkTransition B X ℓ F s n).hom
```

**`Stacks.EtaleCohomology.finiteLevelStalkTransition_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/FiniteLevelStalk.lean, line 426](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/FiniteLevelStalk.lean#L426). The attribute's comment: “finite\_level\_stalks”.

> The transition identifies the quotient of the level-`n+1` stalk by `ℓⁿ⁺¹` with the
> level-`n` stalk.

```lean
public theorem finiteLevelStalkTransition_quotient (F : LAdicSheaf B X ℓ)
    (s : GeometricPoint X.1) (n : ℕ) :
    ∃ e : (finiteLevelStalk B X ℓ F s (n + 1) ⧸
        (Ideal.span ({(ℓ ^ (n + 1) : ZMod (ℓ ^ (n + 2)))} : Set (ZMod (ℓ ^ (n + 2))))) •
          (⊤ : Submodule (ZMod (ℓ ^ (n + 2))) (finiteLevelStalk B X ℓ F s (n + 1))))
        ≃ₗ[ZMod (ℓ ^ (n + 2))]
          (ModuleCat.restrictScalars (finiteLevelRingHom ℓ n)).obj
            (finiteLevelStalk B X ℓ F s n),
      ∀ x, e (Submodule.Quotient.mk x) = (finiteLevelStalkTransition B X ℓ F s n).hom x
```

**`Stacks.EtaleCohomology.LAdicSheaf.stalk`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/Stalk.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/Stalk.lean#L87). The attribute's comment: “stalk\_of\_a\_sheaf”. References: SGA 4½ Rapport (2.2), “fiber definition”.

> The stalk of an ℓ-adic sheaf at a geometric point: the inverse limit of its finite-level
> stalks, as a `ℤ_[ℓ]`-module.

```lean
public abbrev LAdicSheaf.stalk (F : LAdicSheaf B X ℓ) (x : GeometricPoint X.1) :
    Type (u + 1)
```

**`Stacks.EtaleCohomology.LAdicSheaf.finite_stalk`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/StalkFiniteness.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/StalkFiniteness.lean#L163). The attribute's comment: “finite\_limit\_stalk”.

> The stalk of an ℓ-adic sheaf is finite over the ℓ-adic integers.

```lean
public instance LAdicSheaf.finite_stalk
    (F : LAdicSheaf B X ℓ) (x : GeometricPoint X.1) :
    Module.Finite (PadicInt ℓ)
      (LAdicSheaf.stalk B X ℓ F x)
```

**`Stacks.EtaleCohomology.LAdicSheaf.stalk_equiv_free_prod_torsion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/StalkFiniteness.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/StalkFiniteness.lean#L189). The attribute's comment: “stalk\_structure”.

> A stalk of an ℓ-adic sheaf is a sum of free and prime-power cyclic modules.

```lean
public theorem LAdicSheaf.stalk_equiv_free_prod_torsion
    (F : LAdicSheaf B X ℓ) (x : GeometricPoint X.1) :
    ∃ (r t : ℕ) (e : Fin t → ℕ),
      (∀ i, 1 ≤ e i) ∧
      Nonempty (LAdicSheaf.stalk B X ℓ F x ≃ₗ[PadicInt ℓ]
        (Fin r →₀ PadicInt ℓ) ×
          DirectSum (Fin t)
            (fun i => PadicInt ℓ ⧸ (PadicInt ℓ) ∙ ((ℓ : PadicInt ℓ) ^ e i)))
```

## Tag 03UR, a definition

[Tag 03UR](https://stacks.math.columbia.edu/tag/03UR) in the Stacks Project.

**`Stacks.EtaleCohomology.LAdicSheaf.IsTorsion`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/Basic.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/Basic.lean#L79). The attribute's comment: “torsion\_sheaf”.

> A torsion ℓ-adic sheaf is annihilated by a single power of ℓ, uniformly
> at all finite levels.

```lean
public abbrev LAdicSheaf.IsTorsion [IsNoetherian X.1] [Fact ℓ.Prime]
    (F : LAdicSheaf B X ℓ) : Prop
```

**`Stacks.EtaleCohomology.torsionSheaves`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/Rational.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/Rational.lean#L93). The attribute's comment: “the subcategory of torsion sheaves”.

> **Stacks 03UR.** The torsion `ℤ_ℓ`-sheaves, as a property of objects of the abelian category
> of `ℤ_ℓ`-sheaves.

```lean
public abbrev torsionSheaves : ObjectProperty (LAdicSheaf.{u, u + 1} B X ℓ)
```

**`Stacks.EtaleCohomology.RationalSheaf`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/Rational.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/Rational.lean#L107). The attribute's comment: “the category of Q\_ℓ-sheaves as the quotient by the torsion sheaves”. References: SGA 4½ Rapport (2.9).

> **Stacks 03UR.** The abelian category of `ℚ_ℓ`-sheaves on `X`: the quotient of the abelian
> category of `ℤ_ℓ`-sheaves by the Serre subcategory of torsion sheaves. Its objects are the
> `ℤ_ℓ`-sheaves on `X`.

```lean
public abbrev RationalSheaf
```

**`Stacks.EtaleCohomology.rationalization`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/Rational.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/Rational.lean#L111). The attribute's comment: “the quotient functor F ↦ F ⊗ Q\_ℓ”.

> **Stacks 03UR.** The quotient functor `F ↦ F ⊗ ℚ_ℓ` from `ℤ_ℓ`-sheaves to `ℚ_ℓ`-sheaves.

```lean
public abbrev rationalization : LAdicSheaf.{u, u + 1} B X ℓ ⥤ RationalSheaf B X ℓ
```

**`Stacks.EtaleCohomology.RationalSheaf.abelian`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/Rational.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/Rational.lean#L116). The attribute's comment: “Q\_ℓ-sheaves form an abelian category”.

> **Stacks 03UR.** The category of `ℚ_ℓ`-sheaves on `X` is abelian.

```lean
public instance RationalSheaf.abelian : Abelian (RationalSheaf B X ℓ)
```

**`Stacks.EtaleCohomology.LAdicSheaf.rationalStalk`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/Rational.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/Rational.lean#L123). The attribute's comment: “the stalk of F ⊗ Q\_l is the stalk of F tensored with Q\_l”.

> **Stacks 03UR.** The stalk at a geometric point `x` of the `ℚ_ℓ`-sheaf `F ⊗ ℚ_ℓ`, for `F` a
> `ℤ_ℓ`-sheaf: the `ℤ_ℓ`-module stalk of `F` (Tag 03UQ) tensored up to `ℚ_ℓ`. Every `ℚ_ℓ`-sheaf is
> of this shape, the objects of the quotient category being the `ℤ_ℓ`-sheaves themselves.

```lean
public abbrev LAdicSheaf.rationalStalk (F : LAdicSheaf.{u, u + 1} B X ℓ)
    (x : GeometricPoint X.1) : Type (u + 1)
```

**`Stacks.CategoryTheory.isTorsionObject_isSerreClass`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/SerreClass/BoundedTorsion.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Abelian/SerreClass/BoundedTorsion.lean#L140). The attribute's comment: “torsion sheaves are a Serre subcategory”. References: SGA 4½ Rapport (2.9), “more general”.

> The `ℓ`-power torsion objects of an abelian category form a Serre class: they contain the
> zero object and are closed under subobjects, quotients and extensions. For `ℤ_ℓ`-sheaves this is
> the Serre subcategory of torsion sheaves of Stacks 03UR.

```lean
public instance isTorsionObject_isSerreClass (ℓ : ℕ) :
    (isTorsionObject (C := C) ℓ).IsSerreClass
```

**`Stacks.CategoryTheory.isLocalizedModule_mapIntLinearMap`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/SerreClass/BoundedTorsion.lean, line 278](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Abelian/SerreClass/BoundedTorsion.lean#L278). The attribute's comment: “Hom\_\{Q\_l}(F,G) = Hom\_\{Z\_l}(F,G) localized at the powers of l”. References: SGA 4½ Rapport (2.9), “more general”.

> **The hom-groups of a Serre quotient at the `ℓ`-power torsion objects.** The localization
> functor exhibits `Hom (L.obj X) (L.obj Y)` as the localization of the abelian group `Hom X Y` at
> the powers of `ℓ`: multiplication by `ℓ` is invertible on the target, every element of the target
> is a power of `ℓ` away from the image, and two morphisms have the same image exactly when a power
> of `ℓ` equalizes them. For `ℤ_ℓ`-sheaves this is the formula
> `Hom_{ℚ_ℓ}(F, G) = Hom_{ℤ_ℓ}(F, G) ⊗_{ℤ_ℓ} ℚ_ℓ` of Stacks 03UR, since every integer prime to `ℓ`
> is already a unit of `ℤ_ℓ`.

```lean
public instance isLocalizedModule_mapIntLinearMap (X Y : C) :
    IsLocalizedModule (Submonoid.powers (ℓ : ℤ)) (mapIntLinearMap L X Y)
```

## Tag 03UT, a definition

[Tag 03UT](https://stacks.math.columbia.edu/tag/03UT) in the Stacks Project.

**`Stacks.EtaleCohomology.LAdicSheaf.cohomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/Cohomology.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/Cohomology.lean#L145). The attribute's comment: “ℓ-adic cohomology”. References: SGA 7 I (0.1), “b)”; SGA 5 VI (3.1), “def of H^i(X,F)”.

> **The ℓ-adic cohomology of an ℓ-adic sheaf.** For an ℓ-adic sheaf `F = {Fₙ}` on `X` and a
> degree `i`, this is `Hⁱ(X, F) = limₙ Hⁱ(X, Fₙ)`.

```lean
public def LAdicSheaf.cohomology (F : LAdicSheaf B X ℓ) (i : ℕ) : AddCommGrpCat.{u + 1}
```

**`Stacks.EtaleCohomology.LAdicSheaf.compactlySupportedCohomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/CompactlySupportedCohomology.lean, line 195](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/CompactlySupportedCohomology.lean#L195). The attribute's comment: “H^i\_c(X, F) = lim\_n H^i\_c(X, F\_n)”.

> **The compactly supported ℓ-adic cohomology of an ℓ-adic sheaf.** For an ℓ-adic sheaf
> `F = {Fₙ}` on `X` and a degree `i`, this is `Hⁱ_c(X, F) = limₙ Hⁱ_c(X, Fₙ)`.

```lean
public def LAdicSheaf.compactlySupportedCohomology (F : LAdicSheaf B X ℓ) (i : ℤ) :
    ModuleCat.{u + 1} ℤ_[ℓ]
```

**`Stacks.EtaleCohomology.LAdicSheaf.rationalCompactlySupportedCohomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/CompactlySupportedCohomology.lean, line 215](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/CompactlySupportedCohomology.lean#L215). The attribute's comment: “H^i\_c(X, F' ⊗ Q\_ell) = H^i\_c(X, F') ⊗\_\{Z\_ell} Q\_ell”. References: SGA 4½ Rapport (2.10); SGA 7 I (0.1), “more general”.

> **The compactly supported ℓ-adic cohomology with `ℚ_[ℓ]`-coefficients.** For the rational
> ℓ-adic sheaf `F ⊗ Q_ℓ` attached to an ℓ-adic sheaf `F`, this is the extension of scalars of
> `Hⁱ_c(X, F)` along `ℤ_[ℓ] → ℚ_[ℓ]`, that is `Hⁱ_c(X, F ⊗ Q_ℓ) = Hⁱ_c(X, F) ⊗_{ℤ_[ℓ]} ℚ_[ℓ]`.

```lean
public def LAdicSheaf.rationalCompactlySupportedCohomology (F : LAdicSheaf B X ℓ) (i : ℤ) :
    ModuleCat.{u + 1} ℚ_[ℓ]
```

**`Stacks.EtaleCohomology.LAdicSheaf.geometricCompactlySupportedCohomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GeometricLAdicCompactSupport.lean, line 209](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GeometricLAdicCompactSupport.lean#L209). The attribute's comment: “H^i\_c(X\_kbar, F) = lim\_n H^i\_c(X\_kbar, F\_n), on the geometric fibre”.

> **The compactly supported ℓ-adic cohomology of the geometric fibre**,
> `Hⁱ_c(X_k̄, F) = limₙ Hⁱ_c(X_k̄, Fₙ)`, as in [Tag 03UT](https://stacks.math.columbia.edu/tag/03UT)
> for the restriction of `F` to `X_k̄`.

```lean
public def LAdicSheaf.geometricCompactlySupportedCohomology (F : LAdicSheaf B X ℓ) (i : ℤ) :
    ModuleCat.{u + 1} ℤ_[ℓ]
```

**`Stacks.EtaleCohomology.LAdicSheaf.rationalGeometricCompactlySupportedCohomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GeometricLAdicCompactSupport.lean, line 225](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GeometricLAdicCompactSupport.lean#L225). The attribute's comment: “H^i\_c(X\_kbar, F' ⊗ Q\_ell) = H^i\_c(X\_kbar, F') ⊗\_\{Z\_ell} Q\_ell, on the geometric fibre”. References: SGA 4½ Rapport (2.10); SGA 7 XXI (2.0), “more general”.

> **`Hⁱ_c(X_k̄, F ⊗ Q_ℓ) = Hⁱ_c(X_k̄, F) ⊗_{ℤ_[ℓ]} ℚ_[ℓ]`**, the cohomology of the rational
> ℓ-adic sheaf `F ⊗ Q_ℓ` that [Tag 03V2](https://stacks.math.columbia.edu/tag/03V2) is about.

```lean
public def LAdicSheaf.rationalGeometricCompactlySupportedCohomology (F : LAdicSheaf B X ℓ)
    (i : ℤ) : ModuleCat.{u + 1} ℚ_[ℓ]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 64.18, Tag 03UL](https://stacks.math.columbia.edu/tag/03UL)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
