---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.CoherenceCriteria.coherent_tfae, Stacks.AlgebraicGeometry.CoherenceCriteria.structureSheaf_isCoherent, Stacks.AlgebraicGeometry.CoherenceCriteria.isCoherent_of_isFiniteLocallyFree, Stacks.AlgebraicGeometry.CoherenceCriteria.isCoherent_of_isInvertible, Stacks.AlgebraicGeometry.CoherentKernel.coherent_tfae, Stacks.AlgebraicGeometry.CoherentKernel.structureSheaf_isCoherent, Stacks.AlgebraicGeometry.CoherentKernel.isCoherent_of_isFiniteLocallyFree, Stacks.AlgebraicGeometry.CoherentKernel.isCoherent_of_isInvertible
statement: formalized
proof: formalized
---

# 30.9 Coherent sheaves on locally Noetherian schemes

Section 30.9 of the Stacks Project, [Tag 01XY](https://stacks.math.columbia.edu/tag/01XY). 11 tags here are carried by 43 declarations of the repository (all in StacksFrontier) and 7 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01XZ, a lemma

[Tag 01XZ](https://stacks.math.columbia.edu/tag/01XZ) in the Stacks Project.

**`Stacks.AlgebraicGeometry.CoherenceCriteria.coherent_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CoherenceCriteria/Basic.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CoherenceCriteria/Basic.lean#L168). The attribute's comment: “five equivalent conditions”. References: EGA I (1.5.1), “(a) <=> (b)”.

> **[Stacks, Tag 01XZ].** On a locally Noetherian scheme the following are equivalent for a
> module `F`: it is coherent; it is quasi-coherent and of finite type; it is of finite
> presentation; on every affine open it is the sheaf associated with a finite module; on the
> members of some affine open covering it is the sheaf associated with a finite module.

```lean
theorem coherent_tfae (X : Scheme.{u}) [IsLocallyNoetherian X] (F : X.Modules) :
    List.TFAE [
      F.IsCoherent,
      F.IsQuasicoherent ∧ F.IsFiniteType,
      F.IsFinitePresentation,
      ∀ (U : X.Opens) (hU : IsAffineOpen U), IsFiniteTildeOn F U hU,
      ∃ (ι : Type u) (U : ι → X.Opens),
        IsOpenCover U ∧ ∀ i, ∃ hU : IsAffineOpen (U i), IsFiniteTildeOn F (U i) hU]
```

**`Stacks.AlgebraicGeometry.CoherenceCriteria.structureSheaf_isCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CoherenceCriteria/Basic.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CoherenceCriteria/Basic.lean#L229). The attribute's comment: “the structure sheaf is coherent”.

> **[Stacks, Tag 01XZ].** The structure sheaf of a locally Noetherian scheme is coherent.

```lean
theorem structureSheaf_isCoherent (X : Scheme.{u}) [IsLocallyNoetherian X] :
    (SheafOfModules.unit X.ringCatSheaf).IsCoherent
```

**`Stacks.AlgebraicGeometry.CoherenceCriteria.isCoherent_of_isFiniteLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CoherenceCriteria/Basic.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CoherenceCriteria/Basic.lean#L259). The attribute's comment: “finite locally free modules are coherent”.

> **[Stacks, Tag 01XZ].** A finite locally free module on a locally Noetherian scheme is
> coherent.

```lean
theorem isCoherent_of_isFiniteLocallyFree (X : Scheme.{u}) [IsLocallyNoetherian X]
    (F : X.Modules) [_root_.AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree
      (C := Opens ↥X) (J := Opens.grothendieckTopology ↥X) F] : F.IsCoherent
```

**`Stacks.AlgebraicGeometry.CoherenceCriteria.isCoherent_of_isInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CoherenceCriteria/Basic.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CoherenceCriteria/Basic.lean#L325). The attribute's comment: “invertible modules are coherent”.

> **[Stacks, Tag 01XZ].** An invertible module on a locally Noetherian scheme is coherent.
>
> By [Stacks, Tag 0B8N] (b) an invertible module is, on a covering of the whole scheme, a direct
> summand of a finite free module, hence the kernel of `1 - e` for the associated split idempotent;
> and the structure sheaf is coherent, so
> `Stacks.SheafOfModules.isCoherent_of_locallyKernelFiniteCoproduct` applies.

```lean
theorem isCoherent_of_isInvertible (X : Scheme.{u}) [IsLocallyNoetherian X] (F : X.Modules)
    [Stacks.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property F] :
    F.IsCoherent
```

**`Stacks.AlgebraicGeometry.CoherentKernel.coherent_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CoherentKernel/Basic.lean, line 617](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CoherentKernel/Basic.lean#L617). The attribute's comment: “five equivalent conditions”.

> **The five equivalent conditions of [Stacks, Tag 01XZ]** for a module on a locally Noetherian
> scheme: coherence, quasi-coherence together with finite type, finite presentation, and the two
> forms — at every affine open and on some affine open covering — of being the sheaf associated to
> a finite module.
>
> Every implication but the two into (1) was available beforehand; the new one is
> `isCoherent_of_isQuasicoherent_isFiniteType`.

```lean
theorem coherent_tfae (F : X.Modules) :
    List.TFAE [
      F.IsCoherent,
      F.IsQuasicoherent ∧ F.IsFiniteType,
      F.IsFinitePresentation,
      ∀ (U : X.Opens) (hU : IsAffineOpen U), IsFiniteTildeOn F U hU,
      ∃ (ι : Type u) (U : ι → X.Opens),
        IsOpenCover U ∧ ∀ i, ∃ hU : IsAffineOpen (U i), IsFiniteTildeOn F (U i) hU
    ]
```

**`Stacks.AlgebraicGeometry.CoherentKernel.structureSheaf_isCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CoherentKernel/Basic.lean, line 639](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CoherentKernel/Basic.lean#L639). The attribute's comment: “the structure sheaf is coherent”.

> **On a locally Noetherian scheme the structure sheaf is coherent.**

```lean
theorem structureSheaf_isCoherent : (SheafOfModules.unit X.ringCatSheaf).IsCoherent
```

**`Stacks.AlgebraicGeometry.CoherentKernel.isCoherent_of_isFiniteLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CoherentKernel/Basic.lean, line 652](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CoherentKernel/Basic.lean#L652). The attribute's comment: “finite locally free modules are coherent”.

> **A finite locally free module on a locally Noetherian scheme is coherent.**

```lean
theorem isCoherent_of_isFiniteLocallyFree (F : X.Modules)
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree (R := X.ringCatSheaf) F] :
    F.IsCoherent
```

**`Stacks.AlgebraicGeometry.CoherentKernel.isCoherent_of_isInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CoherentKernel/Basic.lean, line 662](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CoherentKernel/Basic.lean#L662). The attribute's comment: “invertible modules are coherent”.

> **An invertible module on a locally Noetherian scheme is coherent.** An invertible module on
> a scheme is finite locally free of rank one, by
> `Stacks.SheafRankOne.isFiniteLocallyFreeOfRank_one_of_isInvertible_scheme`.

```lean
theorem isCoherent_of_isInvertible (F : X.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 F] :
    F.IsCoherent
```

**`Stacks.AlgebraicGeometry.CoherentTFAE.tfae_isCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/NoetherianCoherent.lean, line 373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/NoetherianCoherent.lean#L373).

> **[Stacks, Tag 01XZ].** For a module on a locally Noetherian scheme the following are
> equivalent:
>
> 1. it is coherent;
> 2. it is quasi-coherent and of finite type;
> 3. it is of finite presentation;
> 4. on every affine open `U` it is the `tilde` of a finite `Γ(X, U)`-module;
> 5. the same on the members of some affine open covering.
>
> The implications not using the Noetherian hypothesis are the ones already proved in
> `StacksFrontier/AlgebraicGeometry/CoherentTFAE/` and
> `StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/FiniteTilde.lean`; the one that uses it is
> (2) ⇒ (1).

```lean
theorem tfae_isCoherent (F : X.Modules) :
    List.TFAE
      [_root_.SheafOfModules.IsCoherent F,
        F.IsQuasicoherent ∧ SheafOfModules.IsFiniteType.{u, u, u} F,
        F.IsFinitePresentation,
        ∀ (U : X.Opens) (hU : IsAffineOpen U), IsFiniteTildeOn F U hU,
        ∃ (ι : Type u) (U : ι → X.Opens),
          IsOpenCover U ∧ ∀ i, ∃ hU : IsAffineOpen (U i), IsFiniteTildeOn F (U i) hU]
```

**`Stacks.AlgebraicGeometry.CoherentTFAE.coherent_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/LocallyNoetherian/Coherent.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/LocallyNoetherian/Coherent.lean#L57). The attribute's comment: “five equivalent conditions”.

> **Stacks Project, Tag 01XZ.** The five characterizations of a coherent module on a locally
> Noetherian scheme.

```lean
theorem coherent_tfae (X : Scheme.{u}) [IsLocallyNoetherian X]
    (F : X.Modules) :
    List.TFAE [
      F.IsCoherent,
      F.IsQuasicoherent ∧ F.IsFiniteType,
      F.IsFinitePresentation,
      ∀ (U : X.Opens) (hU : IsAffineOpen U), IsFiniteTildeOn F U hU,
      ∃ (ι : Type u) (U : ι → X.Opens),
        IsOpenCover U ∧ ∀ i, ∃ hU : IsAffineOpen (U i), IsFiniteTildeOn F (U i) hU
    ]
```

**`Stacks.AlgebraicGeometry.CoherentTFAE.structureSheaf_isCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/LocallyNoetherian/Coherent.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/LocallyNoetherian/Coherent.lean#L83). The attribute's comment: “the structure sheaf is coherent”.

> **Stacks Project, Tag 01XZ.** On a locally Noetherian scheme the structure sheaf is
> coherent.

```lean
theorem structureSheaf_isCoherent (X : Scheme.{u}) [IsLocallyNoetherian X] :
    (SheafOfModules.unit X.ringCatSheaf).IsCoherent
```

**`Stacks.AlgebraicGeometry.CoherentTFAE.isCoherent_of_isFiniteLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/LocallyNoetherian/Coherent.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/LocallyNoetherian/Coherent.lean#L89). The attribute's comment: “finite locally free modules are coherent”.

> **Stacks Project, Tag 01XZ.** A finite locally free module on a locally Noetherian scheme is
> coherent.

```lean
theorem isCoherent_of_isFiniteLocallyFree (X : Scheme.{u}) [IsLocallyNoetherian X]
    (F : X.Modules) [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree
      (C := Opens X) (J := Opens.grothendieckTopology X) F] :
    F.IsCoherent
```

## Tag 01Y0, a lemma

[Tag 01Y0](https://stacks.math.columbia.edu/tag/01Y0) in the Stacks Project.

**`AlgebraicGeometry.isCoherent_kernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CoherentSubquotients/Abelian.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CoherentSubquotients/Abelian.lean#L71). The attribute's comment: “kernel”.

> **[Stacks, Tag 01Y0].** The kernel of a map of coherent modules on a locally Noetherian
> scheme is coherent.

```lean
theorem isCoherent_kernel {X : Scheme.{u}} [IsLocallyNoetherian X] {F G : X.Modules}
    [F.IsCoherent] [G.IsCoherent] (φ : F ⟶ G) : (kernel φ).IsCoherent
```

**`AlgebraicGeometry.isCoherent_cokernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CoherentSubquotients/Abelian.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CoherentSubquotients/Abelian.lean#L78). The attribute's comment: “cokernel”.

> **[Stacks, Tag 01Y0].** The cokernel of a map of coherent modules on a locally Noetherian
> scheme is coherent.

```lean
theorem isCoherent_cokernel {X : Scheme.{u}} [IsLocallyNoetherian X] {F G : X.Modules}
    [F.IsCoherent] [G.IsCoherent] (φ : F ⟶ G) : (cokernel φ).IsCoherent
```

**`AlgebraicGeometry.isCoherent_X₂_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CoherentSubquotients/Abelian.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CoherentSubquotients/Abelian.lean#L86). The attribute's comment: “extensions”.

> **[Stacks, Tag 01Y0].** An extension of coherent modules on a locally Noetherian scheme is
> coherent: the middle term of a short exact sequence of `𝒪_X`-modules whose outer terms are
> coherent is coherent.

```lean
theorem isCoherent_X₂_of_shortExact {X : Scheme.{u}} [IsLocallyNoetherian X]
    {S : ShortComplex X.Modules} (hS : S.ShortExact)
    (h₁ : S.X₁.IsCoherent) (h₃ : S.X₃.IsCoherent) : S.X₂.IsCoherent
```

**`AlgebraicGeometry.nonempty_abelian_coherentModules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CoherentSubquotients/Abelian.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CoherentSubquotients/Abelian.lean#L96). The attribute's comment: “abelian category”.

> **[Stacks, Tag 01Y0].** The category of coherent `𝒪_X`-modules on a locally Noetherian
> scheme is abelian. The abelian structure is the one a weak Serre subcategory of an abelian
> category carries, by [Stacks, Tag 0754].

```lean
theorem nonempty_abelian_coherentModules (X : Scheme.{u}) [IsLocallyNoetherian X] :
    Nonempty (Abelian (ObjectProperty.FullSubcategory (fun F : X.Modules => F.IsCoherent)))
```

Declarations registered for the tag:

- [`Stacks.SheafOfModules.coherentModulesAbelian`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/AbelianCategory.lean#L39), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/AbelianCategory.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/AbelianCategory.lean#L43) (StacksFrontier): “abelian category”.
- [`Stacks.SheafOfModules.isCoherent_kernel`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/CoherentWeakSerre.lean#L583), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/AbelianCategory.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/AbelianCategory.lean#L44) (StacksFrontier): “kernel”.
- [`Stacks.SheafOfModules.coherentModules_isClosedUnderCokernels`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/CoherentWeakSerre.lean#L647), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/AbelianCategory.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/AbelianCategory.lean#L45) (StacksFrontier): “cokernel”.
- [`Stacks.SheafOfModules.isCoherent_X₂_of_shortExact`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/CoherentWeakSerre.lean#L591), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/AbelianCategory.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/AbelianCategory.lean#L46) (StacksFrontier): “extensions”.

## Tag 01Y1, a lemma

[Tag 01Y1](https://stacks.math.columbia.edu/tag/01Y1) in the Stacks Project.

**`Stacks.AlgebraicGeometry.CoherentOfFiniteType.isCoherent_of_mono_of_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CoherentOfFiniteType.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CoherentOfFiniteType.lean#L195). The attribute's comment: “quasi_coherent_submodule”. References: EGA I (9.6.4), “submodule, B = O_X”.

> **Stacks 01Y1, submodules.** A quasi-coherent submodule of a coherent module on a locally
> Noetherian scheme is coherent.
>
> This carries the tag, and with the quotient statement below 01Y1's covering set is complete. The
> source (coherent.tex:2364) states exactly two assertions — "Any quasi-coherent submodule of `F`
> is coherent. Any quasi-coherent quotient module of `F` is coherent." — and one declaration is
> tagged for each. Both are proved here, so the attribute is not an over-claim.

```lean
theorem isCoherent_of_mono_of_isQuasicoherent {G F : X.Modules} [G.IsQuasicoherent]
    (hF : _root_.SheafOfModules.IsCoherent F) (ι : G ⟶ F) [Mono ι] :
    _root_.SheafOfModules.IsCoherent G
```

**`Stacks.AlgebraicGeometry.CoherentOfFiniteType.isCoherent_of_epi_of_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CoherentOfFiniteType.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CoherentOfFiniteType.lean#L206). The attribute's comment: “quasi_coherent_quotient”. References: EGA I (9.6.4), “quotient, B = O_X”.

> **Stacks 01Y1, quotients.** A quasi-coherent quotient of a coherent module on a locally
> Noetherian scheme is coherent. This is the second of 01Y1's two assertions; see the submodule
> statement above for why the tag is complete here.

```lean
theorem isCoherent_of_epi_of_isQuasicoherent {F Q : X.Modules} [Q.IsQuasicoherent]
    (hF : _root_.SheafOfModules.IsCoherent F) (p : F ⟶ Q) [Epi p] :
    _root_.SheafOfModules.IsCoherent Q
```

**`Stacks.AlgebraicGeometry.CoherentSubquotients.isCoherent_of_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CoherentSubquotients/Basic.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CoherentSubquotients/Basic.lean#L66). The attribute's comment: “quasi_coherent_quotient”. References: EGA I (9.6.4), “quotient, B = O_X”.

> **[Stacks, Tag 01Y1].** A quasi-coherent quotient of a coherent sheaf of modules on a
> locally Noetherian scheme is coherent.

```lean
theorem isCoherent_of_epi {X : Scheme.{u}} [IsLocallyNoetherian X]
    {F G : X.Modules} [hF : F.IsCoherent] [G.IsQuasicoherent]
    (f : F ⟶ G) [Epi f] : G.IsCoherent
```

**`Stacks.AlgebraicGeometry.CoherentSubquotients.isCoherent_of_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CoherentSubquotients/Basic.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CoherentSubquotients/Basic.lean#L191). The attribute's comment: “quasi_coherent_submodule”.

> **[Stacks, Tag 01Y1].** A quasi-coherent submodule of a coherent sheaf of modules on a
> locally Noetherian scheme is coherent.

```lean
theorem isCoherent_of_mono {X : Scheme.{u}} [IsLocallyNoetherian X]
    {F G : X.Modules} [F.IsCoherent] [G.IsQuasicoherent]
    (f : G ⟶ F) [Mono f] : G.IsCoherent
```

**`Stacks.AlgebraicGeometry.CoherentTFAE.isCoherent_of_epi_of_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/LocallyNoetherian/SubQuotient.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/LocallyNoetherian/SubQuotient.lean#L56). The attribute's comment: “quasi_coherent_quotient”.

> **Stacks Project, Tag 01Y1.** A quasi-coherent quotient of a coherent module on a locally
> Noetherian scheme is coherent.

```lean
theorem isCoherent_of_epi_of_isQuasicoherent [IsLocallyNoetherian X]
    {F G : X.Modules} [F.IsCoherent] [G.IsQuasicoherent]
    (f : F ⟶ G) [Epi f] : G.IsCoherent
```

**`Stacks.AlgebraicGeometry.CoherentTFAE.isCoherent_of_mono_of_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/LocallyNoetherian/SubQuotient.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/LocallyNoetherian/SubQuotient.lean#L75). The attribute's comment: “quasi_coherent_submodule”.

> **Stacks Project, Tag 01Y1.** A quasi-coherent submodule of a coherent module on a locally
> Noetherian scheme is coherent.

```lean
theorem isCoherent_of_mono_of_isQuasicoherent [IsLocallyNoetherian X]
    {F G : X.Modules} [F.IsCoherent] [G.IsQuasicoherent]
    (f : G ⟶ F) [Mono f] : G.IsCoherent
```

## Tag 01Y2, a lemma

[Tag 01Y2](https://stacks.math.columbia.edu/tag/01Y2) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.tensorSheaf_isCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TensorCoherence/Basic.lean, line 556](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TensorCoherence/Basic.lean#L556). The attribute's comment: “tensor product”. References: EGA 0 (5.3.5), “tensor product”; EGA I (9.1.1), “coherent tensor”.

> The tensor product of two coherent sheaves of modules is coherent.

```lean
theorem tensorSheaf_isCoherent (X : AlgebraicGeometry.RingedSpace.{u, u})
    (F G : _root_.SheafOfModules.{u}
      (structureSheafRing X))
    [_root_.SheafOfModules.IsCoherent F] [_root_.SheafOfModules.IsCoherent G] :
    _root_.SheafOfModules.IsCoherent ((((Stacks.SheafOfModules.Tensor.sheafTensor ⟨((X)).presheaf,
        ((X)).IsSheaf⟩).obj (F)).obj (G)))
```

**`Stacks.AlgebraicGeometry.TensorHomCoherent.isCoherent_sheafInternalHom_of_isCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TensorHomCoherent/Basic.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TensorHomCoherent/Basic.lean#L104). The attribute's comment: “sheaf-hom”. References: EGA I (9.1.1), “more general”.

> **The sheaf-hom clause of [Stacks, Tag 01Y2].** On a ringed space, the sheaf-hom
> `SheafHom(ℱ, 𝒢)` between two coherent modules is coherent.
>
> A coherent module is of finite presentation ([Stacks, Tag 01BW] (1)), and the sheaf-hom from a
> module of finite presentation into a coherent module is coherent ([Stacks, Tag 01CQ] (2)). The
> source states this for a locally Noetherian scheme; see `isCoherent_sheafHom` below for that
> statement.

```lean
theorem isCoherent_sheafInternalHom_of_isCoherent {Y : Type u} [TopologicalSpace Y]
    (O : Sheaf (Opens.grothendieckTopology Y) CommRingCat.{u})
    (F G : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf (spaceRingedSite O).O))
    [_root_.SheafOfModules.IsCoherent F] [_root_.SheafOfModules.IsCoherent G] :
    _root_.SheafOfModules.IsCoherent (sheafInternalHom (spaceRingedSite O) F G)
```

**`Stacks.AlgebraicGeometry.TensorHomCoherent.isCoherent_sheafHom`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TensorHomCoherent/Basic.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TensorHomCoherent/Basic.lean#L137). The attribute's comment: “sheaf-hom, as the source states it: locally Noetherian scheme”.

> **[Stacks, Tag 01Y2], the sheaf-hom clause.** Let `X` be a locally Noetherian scheme and let
> `ℱ`, `𝒢` be coherent `𝒪_X`-modules. Then `SheafHom_{𝒪_X}(ℱ, 𝒢)` is coherent.
>
> This is `isCoherent_sheafInternalHom_of_isCoherent` at the site of opens of `X` with its
> structure sheaf; the Noetherian condition is the source's and is not used.

```lean
instance isCoherent_sheafHom (X : Scheme.{u}) [IsLocallyNoetherian X] (F G : X.Modules)
    [hF : _root_.SheafOfModules.IsCoherent F] [hG : _root_.SheafOfModules.IsCoherent G] :
    _root_.SheafOfModules.IsCoherent (sheafInternalHom (spaceRingedSite X.sheaf) F G)
```

**`Stacks.AlgebraicGeometry.TensorHomCoherent.isCoherent_tensorObj`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TensorHomCoherent/Basic.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TensorHomCoherent/Basic.lean#L149). The attribute's comment: “tensor product, as the source states it: locally Noetherian scheme”.

> **[Stacks, Tag 01Y2], the tensor-product clause.** Let `X` be a locally Noetherian scheme and
> let `ℱ`, `𝒢` be coherent `𝒪_X`-modules. Then `ℱ ⊗_{𝒪_X} 𝒢` is coherent.
>
> This is `AlgebraicGeometry.SheafOfModules.tensorSheaf_isCoherent`, which carries the tag, read at
> the `AlgebraicGeometry.Scheme.Modules.tensorObj` spelling of the tensor product; the Noetherian
> condition is the source's and is not used.

```lean
instance isCoherent_tensorObj (X : Scheme.{u}) [IsLocallyNoetherian X] (F G : X.Modules)
    [hF : _root_.SheafOfModules.IsCoherent F] [hG : _root_.SheafOfModules.IsCoherent G] :
    _root_.SheafOfModules.IsCoherent (Scheme.Modules.tensorObj F G)
```

## Tag 01Y3, a lemma

[Tag 01Y3](https://stacks.math.columbia.edu/tag/01Y3) in the Stacks Project.

**`AlgebraicGeometry.exists_epi_over_of_stalk_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/LocalSurjectivity.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/LocalSurjectivity.lean#L114). The attribute's comment: “part (3)”.

> **Stacks Project, Tag 01Y3.** A morphism with finite-type target which is surjective on one
> stalk is an epimorphism after restriction to a neighbourhood of that point.

```lean
public theorem exists_epi_over_of_stalk_surjective {F G : SheafOfModules.{u} R}
    [F.IsFiniteType] (φ : G ⟶ F) (x : X)
    (hx : Function.Surjective
      (ConcreteCategory.hom ((TopCat.Presheaf.stalkFunctor AddCommGrpCat.{u} x).map
        ((PresheafOfModules.toPresheaf R.obj).map φ.val)))) :
    ∃ U : Opens X, x ∈ U ∧ Epi (φ.over U)
```

**`AlgebraicGeometry.exists_isZero_over_of_stalk_isZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/LocalSurjectivity.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/LocalSurjectivity.lean#L126). The attribute's comment: “part (1)”. References: EGA 0 (5.2.2), “support closed”.

> **Stacks Project, Tag 01Y3.** A finite-type sheaf whose stalk vanishes at a point vanishes
> on a neighbourhood of that point.

```lean
public theorem exists_isZero_over_of_stalk_isZero (F : SheafOfModules.{u} R)
    [F.IsFiniteType] (x : X)
    (hx : IsZero (TopCat.Presheaf.stalk (C := Ab.{u}) F.val.presheaf x)) :
    ∃ U : Opens X, x ∈ U ∧ IsZero (F.over U)
```

**`AlgebraicGeometry.exists_isIso_over_of_stalk_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/LocalSurjectivity.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/LocalSurjectivity.lean#L159). The attribute's comment: “part (4)”.

> **Stacks Project, Tag 01Y3.** A morphism from a module of finite type to a coherent module
> which is bijective on the stalk at a point is an isomorphism after restriction to a
> neighbourhood of that point.

```lean
public theorem exists_isIso_over_of_stalk_isIso {F G : SheafOfModules.{u} R}
    [F.IsCoherent] [G.IsFiniteType] (φ : G ⟶ F) (x : X)
    (hx : IsIso ((TopCat.Presheaf.stalkFunctor AddCommGrpCat.{u} x).map
      ((PresheafOfModules.toPresheaf R.obj).map φ.val))) :
    ∃ U : Opens X, x ∈ U ∧ IsIso (φ.over U)
```

**`Stacks.AlgebraicGeometry.Tag01Y3LocalIso.exists_isIso_over_of_stalk_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalIso/Basic.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalIso/Basic.lean#L293). The attribute's comment: “part (4)”.

> **Part (4) of [Stacks, Tag 01Y3].** A map from a finite-type module sheaf to a coherent
> module sheaf which is an isomorphism on one stalk is an isomorphism after restriction to a
> neighbourhood of that point.

```lean
theorem exists_isIso_over_of_stalk_isIso {F G : SheafOfModules.{u} R}
    [F.IsCoherent] [G.IsFiniteType] (φ : G ⟶ F) (x : X)
    (hx : IsIso ((TopCat.Presheaf.stalkFunctor AddCommGrpCat.{u} x).map
      ((PresheafOfModules.toPresheaf R.obj).map φ.val))) :
    ∃ U : Opens X, x ∈ U ∧ IsIso (φ.over U)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.exists_isMono_over_of_stalk_injective`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/LocalIsomorphism.lean#L136), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/LocalIsomorphism.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/LocalIsomorphism.lean#L156) (StacksFrontier): “part (2)”.
- [`Stacks.AlgebraicGeometry.Tag01Y3LocalIso.exists_isMono_over_of_stalk_injective`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalIso/Basic.lean#L277), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/LocalIso/Basic.lean, line 286](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalIso/Basic.lean#L286) (StacksFrontier): “part (2)”.

## Tag 01Y4, a lemma

[Tag 01Y4](https://stacks.math.columbia.edu/tag/01Y4) in the Stacks Project.

**`Stacks.SheafOfModules.SheafHomStalk.exists_localHom_of_stalkLinearMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/LocalHom.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/LocalHom.lean#L86).

> **Stacks Project, Tag 01Y4.** A linear map out of the stalk of a finitely presented sheaf of
> modules on a ringed space is represented by a homomorphism on some open neighbourhood.

```lean
theorem exists_localHom_of_stalkLinearMap (X : TopCat.{u})
    (Rc : TopCat.Sheaf CommRingCat.{u} X)
    (G F : SheafOfModules.{u} (structureSheaf Rc))
    [G.IsFinitePresentation] (x : X)
    (ψ : TopCat.Presheaf.stalk (C := Ab.{u})
        (commVal G).presheaf x →ₗ[TopCat.Presheaf.stalk
          (C := CommRingCat.{u}) Rc.obj x]
      TopCat.Presheaf.stalk (C := Ab.{u}) (commVal F).presheaf x) :
    ∃ (U : Opens X) (_hxU : x ∈ U) (φ : G.over U ⟶ F.over U),
      ∀ (V : Opens X) (hVU : V ≤ U) (hxV : x ∈ V) (m : G.val.obj (op V)),
        TopCat.Presheaf.germ (C := Ab.{u}) F.val.presheaf V x hxV
            ((φ.val.app (op (Over.mk (homOfLE hVU)))) m) =
          ψ (TopCat.Presheaf.germ (C := Ab.{u}) G.val.presheaf V x hxV m)
```

## Tag 01Y5, a lemma

[Tag 01Y5](https://stacks.math.columbia.edu/tag/01Y5) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.exists_coherent_module_on_schemeTheoreticSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Support/SchemeTheoreticCoherent.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/SchemeTheoreticCoherent.lean#L72). The attribute's comment: “descent to a coherent module on the scheme-theoretic support”.

> **[Stacks, Tag 01Y5].** A coherent module on a locally Noetherian scheme is the direct
> image of a coherent module on its scheme-theoretic support.

```lean
theorem exists_coherent_module_on_schemeTheoreticSupport :
    ∃ G : (schemeTheoreticSupport F).subscheme.Modules,
      G.IsCoherent ∧
        Nonempty ((Scheme.Modules.pushforward
          (schemeTheoreticSupport F).subschemeι).obj G ≅ F)
```

Declarations registered for the tag:

- [`SheafOfModules.isClosed_supp`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Support.lean#L151), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Support/SchemeTheoreticCoherent.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/SchemeTheoreticCoherent.lean#L50) (StacksFrontier): “closedness of the support”.

## Tag 087T, a lemma

[Tag 087T](https://stacks.math.columbia.edu/tag/087T) in the Stacks Project.

**`Stacks.ClosedImmersion.pushforwardCoh`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ClosedPushforward/Coherent.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ClosedPushforward/Coherent.lean#L170). The attribute's comment: “the induced functor”.

> **[Stacks, Tag 087T], the induced functor.** Direct image along a closed immersion of
> locally Noetherian schemes carries a coherent `𝒪_Z`-module to a coherent `𝒪_X`-module
> annihilated by the ideal sheaf cutting out `Z`, hence induces a functor
> `Coh(𝒪_Z) ⥤ {ℱ ∈ Coh(𝒪_X) | ℐℱ = 0}`.

```lean
def pushforwardCoh :
    _root_.AlgebraicGeometry.SheafOfModules.CoherentModules Z.ringCatSheaf ⥤
      (coherentAnnihilatedByKer i).FullSubcategory
```

**`Stacks.ClosedImmersion.pushforwardCohEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ClosedPushforward/Coherent.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ClosedPushforward/Coherent.lean#L230). The attribute's comment: “the equivalence”.

> **[Stacks, Tag 087T].** Let `i : Z ⟶ X` be a closed immersion of locally Noetherian schemes
> and let `ℐ ⊆ 𝒪_X` be the quasi-coherent sheaf of ideals cutting out `Z`. Direct image along `i`
> is an equivalence from the category of coherent `𝒪_Z`-modules to the category of coherent
> `𝒪_X`-modules annihilated by `ℐ`.
>
> The functor of this equivalence is `Stacks.ClosedImmersion.pushforwardCoh`, which composed with
> the inclusion of the full subcategory *is* `AlgebraicGeometry.Scheme.Modules.pushforward i`, by
> `pushforwardCoh_comp_ι`.

```lean
def pushforwardCohEquivalence :
    _root_.AlgebraicGeometry.SheafOfModules.CoherentModules Z.ringCatSheaf ≌
      (coherentAnnihilatedByKer i).FullSubcategory
```

**`AlgebraicGeometry.isCoherent_pushforward_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ClosedPushforward/Coherent.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ClosedPushforward/Coherent.lean#L268). The attribute's comment: “coherence of the direct image”.

> **[Stacks, Tag 087T], coherence of the direct image.** The direct image of a coherent
> module along a closed immersion into a locally Noetherian scheme is coherent.
>
> Local Noetherianity of the source is not assumed: it follows from that of the target by
> `isLocallyNoetherian_of_isClosedImmersion`.

```lean
theorem isCoherent_pushforward_of_isClosedImmersion
    [IsClosedImmersion i] [IsLocallyNoetherian X] (G : Z.Modules) [G.IsCoherent] :
    ((Scheme.Modules.pushforward i).obj G).IsCoherent
```

**`AlgebraicGeometry.exists_isCoherent_pushforward_iso_of_smul_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ClosedPushforward/Coherent.lean, line 283](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ClosedPushforward/Coherent.lean#L283). The attribute's comment: “essential surjectivity onto coherent modules”.

> **[Stacks, Tag 087T], essential surjectivity.** A coherent module on `X` annihilated,
> section by section, by the kernel of the comorphism of a closed immersion `i : Z ⟶ X` is the
> direct image along `i` of a coherent module on `Z`.
>
> The module on `Z` is `i^* M`: it is coherent because `Z` is locally Noetherian and the pullback
> of a coherent module is coherent, and the unit `M ⟶ i_* i^* M` is an isomorphism by
> `Stacks.ClosedImmersion.isIso_unit_app_of_smul_eq_zero`.

```lean
theorem exists_isCoherent_pushforward_iso_of_smul_eq_zero
    [IsClosedImmersion i] [IsLocallyNoetherian X] (M : X.Modules) [M.IsCoherent]
    (h : ∀ (U : X.Opens) (a : Γ(X, U)), (i.app U).hom a = 0 → ∀ m : Γ(M, U), a • m = 0) :
    ∃ G : Z.Modules, G.IsCoherent ∧
      Nonempty ((Scheme.Modules.pushforward i).obj G ≅ M)
```

**`AlgebraicGeometry.exists_isCoherent_pushforward_iso_iff_smul_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ClosedPushforward/Coherent.lean, line 303](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ClosedPushforward/Coherent.lean#L303). The attribute's comment: “the essential image on coherent modules”.

> **[Stacks, Tag 087T], the essential image on coherent modules.** A coherent module on `X`
> is the direct image of a coherent module on `Z` exactly when the kernel of the comorphism of
> the closed immersion annihilates it section by section.
>
> This is the characterisation of the essential image of `i_*` restricted to coherent modules:
> the forward implication is the general essential-image criterion
> `Stacks.ClosedImmersion.pushforward_essImage_iff`, which needs no coherence at all, and the
> reverse one is `exists_isCoherent_pushforward_iso_of_smul_eq_zero`.

```lean
theorem exists_isCoherent_pushforward_iso_iff_smul_eq_zero
    [IsClosedImmersion i] [IsLocallyNoetherian X] (M : X.Modules) [M.IsCoherent] :
    (∃ G : Z.Modules, G.IsCoherent ∧
        Nonempty ((Scheme.Modules.pushforward i).obj G ≅ M)) ↔
      ∀ (U : X.Opens) (a : Γ(X, U)), (i.app U).hom a = 0 → ∀ m : Γ(M, U), a • m = 0
```

**`Stacks.AlgebraicGeometry.Tag087TCoherentImage.coherentPushforwardEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CoherentImage/Basic.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CoherentImage/Basic.lean#L236).

> **[Stacks, Tag 087T].** Direct image along a closed immersion of locally Noetherian schemes
> is an equivalence from the coherent modules on the source onto the coherent modules on the
> target annihilated by the defining ideal, and the equivalence is the one induced by direct
> image.
>
> The second component of the pair is `ObjectProperty.liftCompιIso`, which is `Iso.refl`: the
> functor was built as the lift of `ι ⋙ i_*`, so no identification is needed.

```lean
def coherentPushforwardEquivalence :
    Σ e : CoherentModulesOn Z ≌ CoherentAnnihilatedModules i,
      e.functor ⋙ ObjectProperty.ι
          (fun M : X.Modules => M.IsCoherent ∧ AnnihilatedByKer i M) ≅
        ObjectProperty.ι (fun M : Z.Modules => M.IsCoherent) ⋙ Scheme.Modules.pushforward i
```

## Tag 01Y6, a lemma

[Tag 01Y6](https://stacks.math.columbia.edu/tag/01Y6) in the Stacks Project.

**`Stacks.AlgebraicGeometry.FiniteDirectImageCoherent.isCoherent_pushforward_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FiniteDirectImageCoherent/Basic.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FiniteDirectImageCoherent/Basic.lean#L166). The attribute's comment: “the direct image is coherent”. References: EGA III (3.2.2), “finite case”; EGA III (4.8.6), “scheme case”.

> The direct image of a coherent module along a finite morphism to a locally Noetherian scheme is
> coherent.
>
> It is quasi-coherent because a finite morphism is affine, and on every affine open of the target
> its sections form a finite module, which is condition (5) of [Stacks, Tag 01XZ].

```lean
theorem isCoherent_pushforward_of_isFinite {X S : Scheme.{u}} (f : X ⟶ S) [IsFinite f]
    [IsLocallyNoetherian S] (F : X.Modules) [F.IsCoherent] :
    ((Scheme.Modules.pushforward f).obj F).IsCoherent
```

**`Stacks.AlgebraicGeometry.FiniteDirectImageCoherent.isZero_higherDirectImage_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FiniteDirectImageCoherent/Basic.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FiniteDirectImageCoherent/Basic.lean#L178). The attribute's comment: “the higher direct images vanish”.

> The higher direct images of a quasi-coherent module along a finite morphism vanish in positive
> degrees, a finite morphism being affine; this is [Stacks, Tag 01XC]. No hypothesis on the target is
> used.

```lean
theorem isZero_higherDirectImage_of_isFinite {X S : Scheme.{u}} (f : X ⟶ S) [IsFinite f]
    (F : X.Modules) [F.IsQuasicoherent] (p : ℤ) (hp : 0 < p) :
    IsZero (((Scheme.Modules.pushforward f).rightDerivedPlus p).obj F)
```

## Tag 0B3J, a lemma

[Tag 0B3J](https://stacks.math.columbia.edu/tag/0B3J) in the Stacks Project.

**`AlgebraicGeometry.nonempty_generatingSections_of_support_dim_le_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/GlobalGeneration/ZeroDimensionalSupport.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/GlobalGeneration/ZeroDimensionalSupport.lean#L270). The attribute's comment: “global_generation”.

> A coherent sheaf with support of dimension at most zero on a locally Noetherian
> scheme is generated by global sections.
>
> This is also clause (1) of Stacks 0AYT, in a form more general than that clause states it: Stacks
> 0AYT takes `X` proper over a field `k`, which gives `IsLocallyNoetherian X` through
> `LocallyOfFiniteType.isLocallyNoetherian`, so the condition here is strictly weaker than the
> clause's and the clause follows by instantiation.

```lean
public theorem nonempty_generatingSections_of_support_dim_le_zero
    {X : Scheme.{u}} [IsLocallyNoetherian X] (F : X.Modules) [F.IsCoherent]
    (hF : topologicalKrullDim (SheafOfModules.supp F) ≤ 0) :
    Nonempty F.GeneratingSections
```

**`AlgebraicGeometry.isZero_hgroup_top_of_support_dim_le_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/ZeroDimensionalSupport/HigherVanishing.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/ZeroDimensionalSupport/HigherVanishing.lean#L80). The attribute's comment: “vanishing”.

> **[Stacks, Tag 0B3J], the vanishing clause.** For `X` a locally Noetherian scheme and `ℱ` a
> coherent `𝒪_X`-module whose support has dimension at most zero, `Hⁱ(X, ℱ) = 0` for every
> `i > 0`.
>
> The global generation clause of the same tag is
> `AlgebraicGeometry.nonempty_generatingSections_of_support_dim_le_zero`.

```lean
theorem isZero_hgroup_top_of_support_dim_le_zero
    {X : Scheme.{u}} [IsLocallyNoetherian X] (F : X.Modules) [F.IsCoherent]
    (hF : topologicalKrullDim (SheafOfModules.supp F) ≤ 0)
    (i : ℕ) (hi : 0 < i) :
    IsZero (Hgroup X.ringCatSheaf ⊤ i F)
```

## Tag 0CYJ, a lemma

[Tag 0CYJ](https://stacks.math.columbia.edu/tag/0CYJ) in the Stacks Project.

**`Stacks.AlgebraicGeometry.CoherentPushforward.isCoherent_pushforward_of_supp_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/LocallyNoetherian/PushforwardSupport.lean, line 350](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/LocallyNoetherian/PushforwardSupport.lean#L350).

> A coherent sheaf on an open subscheme, supported on a closed subset contained in
> that open, has coherent direct image.

```lean
theorem isCoherent_pushforward_of_supp_subset {X : Scheme.{u}} (U : X.Opens) (T : Set X)
    (hT : IsClosed T) (hTU : T ⊆ U)
    (F : (U : Scheme.{u}).Modules) [F.IsCoherent]
    (hF : U.ι.base '' SheafOfModules.supp F ⊆ T) :
    ((Scheme.Modules.pushforward U.ι).obj F).IsCoherent
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 30.9, Tag 01XY](https://stacks.math.columbia.edu/tag/01XY)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
