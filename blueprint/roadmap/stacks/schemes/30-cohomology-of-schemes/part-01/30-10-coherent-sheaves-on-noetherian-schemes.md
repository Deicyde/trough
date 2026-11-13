---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_eventually_constant_quasicoherentSubobjects, AlgebraicGeometry.exists_idealPowerMultiple_eq_bot_iff_supp_subset, Stacks.IdealPowerSupport.exists_idealPowerMultiple_eq_bot_iff_supp_subset, AlgebraicGeometry.exists_ideal_pow_smul_inf_eq, AlgebraicGeometry.coherentSubobject_isFiltered, AlgebraicGeometry.isColimit_coherentSubobjectCocone, Stacks.AlgebraicGeometry.IdealPowerColimit.canonicalMapToHomRestrict_bijective, Stacks.AlgebraicGeometry.IdealPowerColimit.canonicalMapToSections_bijective_of_isQuasicoherent
statement: formalized
proof: formalized
---

# 30.10 Coherent sheaves on Noetherian schemes

Section 30.10 of the Stacks Project, [Tag 01Y7](https://stacks.math.columbia.edu/tag/01Y7). 6 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01Y8, a lemma

[Tag 01Y8](https://stacks.math.columbia.edu/tag/01Y8) in the Stacks Project.

**`AlgebraicGeometry.exists_eventually_constant_quasicoherentSubobjects`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/AscendingChain.lean, line 270](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/AscendingChain.lean#L270).

> **Stacks Project, Tag 01Y8.** An ascending chain of quasi-coherent submodules of a coherent
> sheaf on a Noetherian scheme eventually stabilizes.

```lean
public theorem exists_eventually_constant_quasicoherentSubobjects
    (X : Scheme.{u}) [IsNoetherian X] (F : X.Modules) [F.IsCoherent]
    (G : ℕ → Subobject F) (hG : ∀ n, (G n : X.Modules).IsQuasicoherent)
    (hmono : Monotone G) :
    ∃ n, ∀ m, n ≤ m → G m = G n
```

## Tag 01Y9, a lemma

[Tag 01Y9](https://stacks.math.columbia.edu/tag/01Y9) in the Stacks Project.

**`AlgebraicGeometry.exists_idealPowerMultiple_eq_bot_iff_supp_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/IdealPowerAnnihilation.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/IdealPowerAnnihilation.lean#L159). References: EGA I (9.3.4).

> **Stacks Project, Tag 01Y9.** Let `ℱ` be a coherent module on a Noetherian scheme `X` and
> let `ℐ ⊆ 𝒪_X` be a quasi-coherent sheaf of ideals, cutting out the closed subscheme
> `Z ⊆ X`. Then some power of `ℐ` annihilates `ℱ` if and only if the support of `ℱ` is contained
> in `Z`.

```lean
theorem exists_idealPowerMultiple_eq_bot_iff_supp_subset {X : Scheme.{u}} [IsNoetherian X]
    (F : X.Modules) [F.IsCoherent] (I : X.IdealSheafData) :
    (∃ n : ℕ, idealPowerMultiple I n F = ⊥) ↔
      SheafOfModules.supp F ⊆ (I.support : Set X)
```

**`Stacks.IdealPowerSupport.exists_idealPowerMultiple_eq_bot_iff_supp_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/IdealPowerSupport.lean, line 230](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/IdealPowerSupport.lean#L230). References: EGA I (9.3.4).

> **Stacks Project, Tag 01Y9.** Let `X` be a Noetherian scheme, `I` a quasi-coherent sheaf of
> ideals and `F` a coherent `𝒪_X`-module — here a quasi-coherent module of finite type, which on a
> locally Noetherian scheme is the same thing by Tag 01XZ. Then some power of `I` annihilates `F`
> if and only if the support of `F` is contained in the closed set cut out by `I`.
>
> Both directions are affine-local, with the algebraic content supplied by Tag 00L6 over the
> Noetherian ring of sections on an affine open: a power of an ideal kills a finite module exactly
> when the support of the module lies in the zero locus of the ideal. For the forward direction one
> affine open containing the point suffices. For the converse the exponent must be chosen uniformly,
> and that is where quasi-compactness enters: finitely many affine opens cover `X`, the largest of
> their exponents works on each of them, and `smul_pow_eq_bot_of_le` carries the vanishing from a
> member of the cover to any affine open inside it, which is enough to conclude by sheaf
> separation.

```lean
public theorem exists_idealPowerMultiple_eq_bot_iff_supp_subset {X : Scheme.{u}}
    [IsNoetherian X] (F : X.Modules) [_root_.SheafOfModules.IsCoherent F]
    (I : X.IdealSheafData) :
    (∃ n : ℕ, idealPowerMultiple I n F = ⊥) ↔
      SheafOfModules.supp F ⊆ (I.support : Set X)
```

## Tag 01YA, a lemma

[Tag 01YA](https://stacks.math.columbia.edu/tag/01YA) in the Stacks Project.

**`AlgebraicGeometry.exists_ideal_pow_smul_inf_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/ArtinRees.lean, line 301](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/ArtinRees.lean#L301). References: EGA 0 (7.3.2.1).

> **Stacks Project, Tag 01YA.** Artin-Rees for a coherent sheaf and a quasi-coherent subsheaf
> on a Noetherian scheme: the equality holds on every affine open with a single constant.

```lean
theorem exists_ideal_pow_smul_inf_eq {X : Scheme.{u}} [IsNoetherian X]
    (F : X.Modules) [F.IsCoherent]
    (G : F.Submodule) [G.toSheafOfModules.IsQuasicoherent]
    (I : (SheafOfModules.unit X.ringCatSheaf).Submodule)
    [I.toSheafOfModules.IsQuasicoherent] :
    ∃ c : ℕ, ∀ n : ℕ, c ≤ n → ∀ U : X.affineOpens,
      (show Ideal Γ(X, U.1) from I.toSubmodule.obj (op U.1)) ^ (n - c) •
          (((show Ideal Γ(X, U.1) from I.toSubmodule.obj (op U.1)) ^ c •
            (⊤ : Submodule Γ(X, U.1) Γ(F, U.1))) ⊓
            G.toSubmodule.obj (op U.1)) =
        ((show Ideal Γ(X, U.1) from I.toSubmodule.obj (op U.1)) ^ n •
          (⊤ : Submodule Γ(X, U.1) Γ(F, U.1))) ⊓
          G.toSubmodule.obj (op U.1)
```

## Tag 0GN6, a lemma

[Tag 0GN6](https://stacks.math.columbia.edu/tag/0GN6) in the Stacks Project.

**`AlgebraicGeometry.coherentSubobject_isFiltered`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/FilteredColimit.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/FilteredColimit.lean#L121). The attribute's comment: “directedness”. References: EGA I (1.5.4), “filtered system”.

> **Stacks Project, Tag 0GN6 (directedness).** The coherent submodules of a quasi-coherent
> module on a Noetherian scheme form a filtered category.

```lean
instance coherentSubobject_isFiltered {X : Scheme.{u}} (F : X.Modules)
    [IsNoetherian X] [F.IsQuasicoherent] : IsFiltered (CoherentSubobject F)
```

**`AlgebraicGeometry.isColimit_coherentSubobjectCocone`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/FilteredColimit.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/FilteredColimit.lean#L128). The attribute's comment: “colimit”. References: EGA I (1.5.4), “colimit”; EGA I (9.4.9), “Noetherian scheme”.

> **Stacks Project, Tag 0GN6 (colimit).** A quasi-coherent module on a Noetherian scheme is
> the filtered colimit of its coherent submodules.

```lean
noncomputable def isColimit_coherentSubobjectCocone {X : Scheme.{u}} (F : X.Modules)
    [IsNoetherian X] [F.IsQuasicoherent] :
    IsColimit (coherentSubobjectCocone F)
```

## Tag 01YB, a lemma

[Tag 01YB](https://stacks.math.columbia.edu/tag/01YB) in the Stacks Project.

**`Stacks.AlgebraicGeometry.IdealPowerColimit.canonicalMapToHomRestrict_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Coherent/HomColimit/FirstDisplaySurjectivity.lean, line 295](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Coherent/HomColimit/FirstDisplaySurjectivity.lean#L295). The attribute's comment: “first display”. References: SGA 2 II (Theorem6), “b)”.

> For a Noetherian scheme `X`, a quasi-coherent sheaf of ideals `I` with complement
> `U = X \ V(I)`, a coherent `𝒪_X`-module `G` and a quasi-coherent `𝒪_X`-module `F`, the canonical
> map
>
> `colim_n Hom_{𝒪_X}(Iⁿ G, F) ⟶ Hom_{𝒪_U}(G|_U, F|_U)`
>
> is bijective.

```lean
public theorem canonicalMapToHomRestrict_bijective [AlgebraicGeometry.IsNoetherian X]
    (I : X.IdealSheafData) (G F : X.Modules) [G.IsCoherent] [F.IsQuasicoherent] :
    Function.Bijective (canonicalMapToHomRestrict I G F)
```

**`Stacks.AlgebraicGeometry.IdealPowerColimit.canonicalMapToSections_bijective_of_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Coherent/HomColimit/GlobalSections.lean, line 496](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Coherent/HomColimit/GlobalSections.lean#L496). The attribute's comment: “global sections”. References: SGA 2 II (Theorem6), “b)”.

> **The global-sections clause of [Stacks, Tag 01YB].** For a Noetherian scheme `X`, a
> quasi-coherent sheaf of ideals `I` and a quasi-coherent `𝒪_X`-module `F`, the canonical map
>
> `colim_n Hom_{𝒪_X}(Iⁿ, F) ⟶ Γ(X \\ V(I), F)`
>
> is a bijection. Injectivity is `canonicalMapToSections_injective`, the first assertion of
> [Stacks, Tag 01PQ]; surjectivity is
> `exists_hom_idealPow_app_oneSection_eq_of_isQuasicoherent`.
>
> **This is the second of the two displays of Tag 01YB.** The tag's *first* display,
> `colim_n Hom(Iⁿ G, F) ≅ Hom(G|_U, F|_U)` for a coherent `G`, is not proved here; its `G = 𝒪_X`
> case is, so the clause label records the global-sections half only. The first display is what
> [Stacks, Tag 0BJZ] consumes: there `G` is the coherent module itself, never `𝒪_X`. Its arrow
> is `canonicalMapToHomRestrict` and its bijectivity is
> `canonicalMapToHomRestrict_bijective`, whose surjectivity half applies this clause to
> `SheafHom(G, F)` and then transports the resulting morphism `Iⁿ ⟶ SheafHom(G, F)` across the
> surjection `Iⁿ ⊗ G ⟶ Iⁿ G`, using the vanishing `Iⁿ ker(Iⁿ ⊗ G ⟶ Iⁿ G) = 0` and a second
> Artin-Rees step.

```lean
theorem canonicalMapToSections_bijective_of_isQuasicoherent
    [AlgebraicGeometry.IsNoetherian X] (I : X.IdealSheafData) (F : X.Modules)
    [F.IsQuasicoherent] :
    Function.Bijective (canonicalMapToSections I F)
```

## Tag 0FD0, a lemma

[Tag 0FD0](https://stacks.math.columbia.edu/tag/0FD0) in the Stacks Project.

**`AlgebraicGeometry.exists_coherent_submodule_extension_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/CoherentExtension/LocallyNoetherian.lean, line 350](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/CoherentExtension/LocallyNoetherian.lean#L350).

> **Stacks Project, Tag 0FD0.** Let `F` and `G` be coherent modules on a locally Noetherian
> scheme `X`, and let `φ : F|_U ⟶ G|_U` be a morphism over an open subscheme `U`. Then there is a
> coherent submodule `F' ⟶ F` agreeing with `F` over `U` and a morphism `φ' : F' ⟶ G` whose
> restriction to `U` is `φ` under that agreement.
>
> The submodule is presented as a monomorphism `i : F' ⟶ F` whose restriction to `U` is an
> isomorphism `e`; the two equations say that `e` is that restriction and that `φ` is the
> restriction of `φ'` read through `e`.

```lean
theorem exists_coherent_submodule_extension_of_isLocallyNoetherian [IsLocallyNoetherian X]
    (F G : X.Modules) [F.IsCoherent] [G.IsCoherent] (U : X.Opens)
    (φ : F.restrict U.ι ⟶ G.restrict U.ι) :
    ∃ (F' : X.Modules) (_ : F'.IsCoherent) (i : F' ⟶ F) (_ : Mono i)
      (φ' : F' ⟶ G) (e : F'.restrict U.ι ≅ F.restrict U.ι),
      (Scheme.Modules.restrictFunctor U.ι).map i = e.hom ∧
        e.hom ≫ φ = (Scheme.Modules.restrictFunctor U.ι).map φ'
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 30.10, Tag 01Y7](https://stacks.math.columbia.edu/tag/01Y7)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
