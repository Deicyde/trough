---
declaration: section
origin: cited
lean: AlgebraicGeometry.isConstructibleSetSheaf_of_mono_of_epi_and_isSerreClass_abelian_and_module, AlgebraicGeometry.isConstructibleModuleSheaf_of_mono', AlgebraicGeometry.isConstructibleModuleSheaf_of_epi', AlgebraicGeometry.isConstructibleAbelianSheaf_of_mono, AlgebraicGeometry.isConstructibleAbelianSheaf_of_epi, AlgebraicGeometry.isSerreClass_isConstructibleAbelianSheaf, AlgebraicGeometry.isConstructibleModuleSheaf_of_mono, AlgebraicGeometry.isConstructibleModuleSheaf_of_epi
statement: formalized
proof: formalized
---

# 59.74 Constructible sheaves on Noetherian schemes

Section 59.74 of the Stacks Project, [Tag 03RY](https://stacks.math.columbia.edu/tag/03RY). 5 tags here are carried by 29 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09BH, a proposition

[Tag 09BH](https://stacks.math.columbia.edu/tag/09BH) in the Stacks Project.

**`AlgebraicGeometry.isConstructibleSetSheaf_of_mono_of_epi_and_isSerreClass_abelian_and_module`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/SerreSubcategory.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/SerreSubcategory.lean#L80).

> **Stacks 09BH.** Let `X` be a Noetherian scheme and let `Λ` be a Noetherian ring.
>
> 1. Any sub or quotient sheaf of a constructible sheaf of sets on the small étale site of `X` is
>    constructible.
> 2. The constructible abelian sheaves on that site form a (strong) Serre subcategory of all
>    abelian sheaves on it; in particular every subsheaf and quotient sheaf of a constructible
>    abelian sheaf is constructible.
> 3. The constructible sheaves of `Λ`-modules on that site form a (strong) Serre subcategory of all
>    sheaves of `Λ`-modules on it; in particular every submodule and quotient module of a
>    constructible sheaf of `Λ`-modules is constructible.
>
> `CategoryTheory.ObjectProperty.IsSerreClass` is containing zero and closure under subobjects,
> quotients and extensions, which is a Serre subcategory by Stacks 02MP.

```lean
public theorem isConstructibleSetSheaf_of_mono_of_epi_and_isSerreClass_abelian_and_module
    (B : BigEtaleSite.{u}) (X : B.Scheme) [IsNoetherian X.obj]
    (Λ : Type r) [CommRing Λ] [IsNoetherianRing Λ] [Small.{u + 1} Λ] :
    ((∀ (F G : Sheaf (SmallEtale.topology B X.obj X.property) (Type (u + 1))) (i : G ⟶ F),
        Mono i → IsConstructibleSetSheaf B X F → IsConstructibleSetSheaf B X G) ∧
      (∀ (F Q : Sheaf (SmallEtale.topology B X.obj X.property) (Type (u + 1))) (p : F ⟶ Q),
        Epi p → IsConstructibleSetSheaf B X F → IsConstructibleSetSheaf B X Q)) ∧
      ObjectProperty.IsSerreClass
        (fun F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{u + 1} =>
          IsConstructibleAbelianSheaf B X F) ∧
      ObjectProperty.IsSerreClass
        (fun F : Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{u + 1} Λ) =>
          IsConstructibleModuleSheaf B X Λ F)
```

**`AlgebraicGeometry.isConstructibleModuleSheaf_of_mono'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ShrinkCoefficients.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ShrinkCoefficients.lean#L237). The attribute's comment: “part (3), subsheaf, for a Noetherian coefficient ring in any universe”.

> **Stacks 09BH, part (3), subsheaves, for a coefficient ring in any universe.** A subsheaf of
> a constructible sheaf of `R`-modules on the small étale site of a Noetherian scheme is
> constructible.
>
> `AlgebraicGeometry.isConstructibleModuleSheaf_of_mono` proves this for a ring in `Type (u + 1)`.
> Here `R` need only be small in that universe: the statement is read at `Shrink.{u + 1} R`, a
> Noetherian ring in `Type (u + 1)`, and transported back. The equivalence of sheaf categories
> preserves monomorphisms, so the subsheaf upstairs is one.

```lean
public theorem isConstructibleModuleSheaf_of_mono' [IsNoetherian X.obj] [IsNoetherianRing R]
    {G F : Sheaf (SmallEtale.topology B X.1 X.property) (ModuleCat.{u + 1} R)}
    (i : G ⟶ F) [Mono i] (hF : IsConstructibleModuleSheaf B X R F) :
    IsConstructibleModuleSheaf B X R G
```

**`AlgebraicGeometry.isConstructibleModuleSheaf_of_epi'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ShrinkCoefficients.lean, line 251](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ShrinkCoefficients.lean#L251). The attribute's comment: “part (3), quotient sheaf, for a Noetherian coefficient ring in any universe”.

> **Stacks 09BH, part (3), quotient sheaves, for a coefficient ring in any universe.** A
> quotient of a constructible sheaf of `R`-modules on the small étale site of a Noetherian scheme
> is constructible. This is `AlgebraicGeometry.isConstructibleModuleSheaf_of_epi` transported along
> the same equivalence, which preserves epimorphisms.

```lean
public theorem isConstructibleModuleSheaf_of_epi' [IsNoetherian X.obj] [IsNoetherianRing R]
    {G Q : Sheaf (SmallEtale.topology B X.1 X.property) (ModuleCat.{u + 1} R)}
    (p : G ⟶ Q) [Epi p] (hG : IsConstructibleModuleSheaf B X R G) :
    IsConstructibleModuleSheaf B X R Q
```

**`AlgebraicGeometry.isConstructibleAbelianSheaf_of_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StrongSerreAbelian.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StrongSerreAbelian.lean#L168). The attribute's comment: “part (2), subsheaf, with Stacks 00YT as hunderlying, Stacks 03S8 as hrep and the surjection half of Stacks 09Y9 as hcover”.

> A subsheaf of a constructible sheaf of abelian groups on the small étale site of a Noetherian
> scheme is constructible. It assumes `hunderlying : SmallEtaleUnderlyingSetCommutes B X`,
> `hrep : RepresentableIsConstructibleSetSheaf B X` and `hcover : HasFiniteRepresentableCover B X`.

```lean
public theorem isConstructibleAbelianSheaf_of_mono [IsNoetherian X.obj]
    (hunderlying : SmallEtaleUnderlyingSetCommutes B X)
    (hrep : RepresentableIsConstructibleSetSheaf B X)
    (hcover : HasFiniteRepresentableCover B X)
    {F G : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{u + 1}}
    (i : G ⟶ F) [Mono i] (hF : IsConstructibleAbelianSheaf B X F) :
    IsConstructibleAbelianSheaf B X G
```

**`AlgebraicGeometry.isConstructibleAbelianSheaf_of_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StrongSerreAbelian.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StrongSerreAbelian.lean#L217). The attribute's comment: “part (2), quotient sheaf, with Stacks 00YT as hunderlying, Stacks 03S8 as hrep and the surjection half of Stacks 09Y9 as hcover”.

> A quotient of a constructible sheaf of abelian groups on the small étale site of a Noetherian
> scheme is constructible. It assumes `hunderlying : SmallEtaleUnderlyingSetCommutes B X`,
> `hrep : RepresentableIsConstructibleSetSheaf B X` and `hcover : HasFiniteRepresentableCover B X`.

```lean
public theorem isConstructibleAbelianSheaf_of_epi [IsNoetherian X.obj]
    (hunderlying : SmallEtaleUnderlyingSetCommutes B X)
    (hrep : RepresentableIsConstructibleSetSheaf B X)
    (hcover : HasFiniteRepresentableCover B X)
    {F Q : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{u + 1}}
    (p : F ⟶ Q) [Epi p] (hF : IsConstructibleAbelianSheaf B X F) :
    IsConstructibleAbelianSheaf B X Q
```

**`AlgebraicGeometry.isSerreClass_isConstructibleAbelianSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StrongSerreAbelian.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StrongSerreAbelian.lean#L235). The attribute's comment: “part (2), the strong Serre property, with Stacks 00YT as hunderlying, Stacks 03S8 as hrep and the surjection half of Stacks 09Y9 as hcover”.

> The constructible sheaves of abelian groups on the small étale site of a Noetherian scheme form
> a *strong* Serre subcategory of all abelian sheaves on that site: they contain zero and are closed
> under subobjects, quotients and extensions. It assumes
> `hunderlying : SmallEtaleUnderlyingSetCommutes B X`,
> `hrep : RepresentableIsConstructibleSetSheaf B X` and `hcover : HasFiniteRepresentableCover B X`.

```lean
public theorem isSerreClass_isConstructibleAbelianSheaf [IsNoetherian X.obj]
    (hunderlying : SmallEtaleUnderlyingSetCommutes B X)
    (hrep : RepresentableIsConstructibleSetSheaf B X)
    (hcover : HasFiniteRepresentableCover B X) :
    (isConstructibleAbelianSheafProperty B X :
      ObjectProperty (Sheaf (SmallEtale.topology B X.obj X.property)
        AddCommGrpCat.{u + 1})).IsSerreClass
```

**`AlgebraicGeometry.isConstructibleModuleSheaf_of_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StrongSerreModules.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StrongSerreModules.lean#L167). The attribute's comment: “part (3), subsheaf; Stacks 095E, Stacks 09YR, Stacks 03RZ (3) and the geometric step of the source's proof are all discharged from the library”.

> **Stacks 09BH, part (3), subsheaves.** A subsheaf of a constructible sheaf of `Λ`-modules on
> the small étale site of a Noetherian scheme is constructible.
>
> By Stacks 095E the ambient sheaf is locally constant of finite type on the strata of a single
> stratification of `X`. Inverse image to a stratum is left exact, so the subsheaf restricts to a
> subsheaf there, and the geometric step of the source's proof,
> `AlgebraicGeometry.finiteTypeLocallyConstantSubsheavesAreConstructible`, makes that restriction
> constructible on the stratum. The strata are immersed with constructible images and they cover
> `X`, so Stacks 09YR carries constructibility back to `X`.

```lean
public theorem isConstructibleModuleSheaf_of_mono [IsNoetherian X.obj]
    {G F : Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{u + 1} Λ)}
    (i : G ⟶ F) [Mono i] (hF : IsConstructibleModuleSheaf B X Λ F) :
    IsConstructibleModuleSheaf B X Λ G
```

**`AlgebraicGeometry.isConstructibleModuleSheaf_of_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StrongSerreModules.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StrongSerreModules.lean#L209). The attribute's comment: “part (3), quotient sheaf; Stacks 095E, Stacks 09YR, Stacks 03RZ (3) and the geometric step of the source's proof are all discharged from the library”.

> **Stacks 09BH, part (3), quotient sheaves.** A quotient of a constructible sheaf of
> `Λ`-modules on the small étale site of a Noetherian scheme is constructible.
>
> An epimorphism of sheaves of modules is the cokernel of its kernel; the kernel is a subobject, so
> it is constructible by `AlgebraicGeometry.isConstructibleModuleSheaf_of_mono`, and the weak Serre
> property of Stacks 03RZ (3) then puts the target in the class.

```lean
public theorem isConstructibleModuleSheaf_of_epi [IsNoetherian X.obj]
    {G Q : Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{u + 1} Λ)}
    (p : G ⟶ Q) [Epi p] (hG : IsConstructibleModuleSheaf B X Λ G) :
    IsConstructibleModuleSheaf B X Λ Q
```

**`AlgebraicGeometry.isSerreClass_isConstructibleModuleSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StrongSerreModules.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StrongSerreModules.lean#L246). The attribute's comment: “part (3), the strong Serre property; Stacks 095E, Stacks 09YR, Stacks 03RZ (3) and the geometric step of the source's proof are all discharged from the library”.

> **Stacks 09BH, part (3).** The constructible sheaves of `Λ`-modules on the small étale site
> of a Noetherian scheme form a *strong* Serre subcategory of all sheaves of `Λ`-modules on that
> site: `CategoryTheory.ObjectProperty.IsSerreClass` is closure under subobjects, quotients and
> extensions together with containing zero, which is the characterisation of a Serre subcategory in
> Stacks 02MP.
>
> Closure under extensions and the zero object are the weak Serre property of Stacks 03RZ (3),
> which is unconditional; closure under subobjects is
> `AlgebraicGeometry.isConstructibleModuleSheaf_of_mono`, and it implies closure under quotients
> because an epimorphism is the cokernel of its kernel.

```lean
public theorem isSerreClass_isConstructibleModuleSheaf [IsNoetherian X.obj] :
    ObjectProperty.IsSerreClass
      (fun F : Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{u + 1} Λ) =>
        IsConstructibleModuleSheaf B X Λ F)
```

**`AlgebraicGeometry.isConstructibleSetSheaf_of_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StrongSerreSets.lean, line 608](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StrongSerreSets.lean#L608). The attribute's comment: “part (1), subsheaf, with Stacks 03S8 as hrep and the surjection half of Stacks 09Y9 as hcover”.

> **Stacks 09BH, part (1), subsheaves.** A subsheaf of a constructible sheaf of sets on the
> small étale site of a Noetherian scheme is constructible.
>
> `hrep` is Stacks 03S8 and `hcover` is the surjection half of Stacks 09Y9; neither mentions
> subobjects. Given a surjection onto `F` from a finite coproduct of quasi-compact representables,
> sub-closure for the coproduct and for its square descends to `F`, and sub-closure for a
> quasi-compact representable is `isConstructibleSetSheaf_of_mono_representable`.

```lean
public theorem isConstructibleSetSheaf_of_mono (B : BigEtaleSite.{u})
    (X : B.Scheme) [IsNoetherian X.obj]
    (hrep : RepresentableIsConstructibleSetSheaf B X)
    (hcover : HasFiniteRepresentableCover B X)
    {F G : Sheaf (SmallEtale.topology B X.obj X.property) (Type (u + 1))}
    (i : G ⟶ F) [Mono i] (hF : IsConstructibleSetSheaf B X F) :
    IsConstructibleSetSheaf B X G
```

**`AlgebraicGeometry.isConstructibleSetSheaf_of_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StrongSerreSets.lean, line 641](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StrongSerreSets.lean#L641). The attribute's comment: “part (1), quotient sheaf, with Stacks 03S8 as hrep and the surjection half of Stacks 09Y9 as hcover”.

> **Stacks 09BH, part (1), quotient sheaves.** A quotient sheaf of a constructible sheaf of sets
> on the small étale site of a Noetherian scheme is constructible.
>
> This is the source's argument: the kernel pair `ℱ ×_𝒬 ℱ` is a subsheaf of `ℱ × ℱ`, hence
> constructible by the subsheaf case and Stacks 03RZ (1), and `𝒬` is the coequalizer of that kernel
> pair, hence constructible by Stacks 03RZ (1) again.

```lean
public theorem isConstructibleSetSheaf_of_epi (B : BigEtaleSite.{u})
    (X : B.Scheme) [IsNoetherian X.obj]
    (hrep : RepresentableIsConstructibleSetSheaf B X)
    (hcover : HasFiniteRepresentableCover B X)
    {F Q : Sheaf (SmallEtale.topology B X.obj X.property) (Type (u + 1))}
    (p : F ⟶ Q) [Epi p] (hF : IsConstructibleSetSheaf B X F) :
    IsConstructibleSetSheaf B X Q
```

**`Stacks.EtaleCohomology.FiniteLevelSheaf.isConstructible_of_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/LevelConstructibility.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/LevelConstructibility.lean#L63). The attribute's comment: “part (3), subsheaf, at the coefficients Z/l^\{n+1}Z of a finite level of an l-adic sheaf”.

> A subsheaf of a constructible finite-level sheaf is constructible.

```lean
public theorem isConstructible_of_mono (n : ℕ)
    {G F : FiniteLevelSheaf.{u, u + 1} B X ℓ n} (i : G ⟶ F) [Mono i]
    (hF : IsConstructibleModuleSheaf B X (ZMod (ℓ ^ (n + 1))) F) :
    IsConstructibleModuleSheaf B X (ZMod (ℓ ^ (n + 1))) G
```

**`Stacks.EtaleCohomology.FiniteLevelSheaf.isConstructible_of_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/LevelConstructibility.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/LevelConstructibility.lean#L74). The attribute's comment: “part (3), quotient sheaf, at the coefficients Z/l^\{n+1}Z of a finite level of an l-adic sheaf”.

> A quotient of a constructible finite-level sheaf is constructible.

```lean
public theorem isConstructible_of_epi (n : ℕ)
    {G Q : FiniteLevelSheaf.{u, u + 1} B X ℓ n} (p : G ⟶ Q) [Epi p]
    (hG : IsConstructibleModuleSheaf B X (ZMod (ℓ ^ (n + 1))) G) :
    IsConstructibleModuleSheaf B X (ZMod (ℓ ^ (n + 1))) Q
```

**`Stacks.EtaleCohomology.LAdicSheaf.isConstructible_stableKernelLevel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/StableKernel.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/StableKernel.lean#L225). The attribute's comment: “part (3), subsheaf, applied to the intersection of the images of the levelwise kernels inside a levelwise kernel”.

> Each level of the kernel of a morphism of ℓ-adic sheaves is a constructible sheaf.

```lean
public theorem isConstructible_stableKernelLevel {F G : LAdicSheaf.{u, u + 1} B X ℓ} (f : F ⟶ G)
    (n : ℕ) :
    IsConstructibleModuleSheaf B X (ZMod (ℓ ^ (n + 1))) (stableKernelLevel f n)
```

## Tag 09YV, a lemma

[Tag 09YV](https://stacks.math.columbia.edu/tag/09YV) in the Stacks Project.

**`AlgebraicGeometry.isNoetherianObject_of_isConstructibleSetSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ConstructibleAscendingChain.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ConstructibleAscendingChain.lean#L80). The attribute's comment: “sheaves of sets, carrying Stacks 09BH (a subsheaf of a constructible sheaf of sets is constructible) as the explicit hypothesis hsub and Stacks 095P (a filtered system of constructible sheaves of sets whose colimit is constructible is essentially constant) as the explicit hypothesis hess”.

> **Stacks Project, Tag 09YV** for sheaves of sets. On a Noetherian scheme every ascending
> chain of subsheaves of a constructible sheaf of sets stabilizes.

```lean
public theorem isNoetherianObject_of_isConstructibleSetSheaf
    (B : BigEtaleSite.{u}) (X : B.Scheme) [IsNoetherian X.obj]
    (hsub : ∀ {G H : Sheaf (SmallEtale.topology B X.obj X.property) (Type (u + 1))}
      (i : G ⟶ H), Mono i → IsConstructibleSetSheaf B X H → IsConstructibleSetSheaf B X G)
    (hess : ∀ (M : ℕ ⥤ Sheaf (SmallEtale.topology B X.obj X.property) (Type (u + 1)))
      (c : Cocone M), IsColimit c →
      (∀ n, IsConstructibleSetSheaf B X (M.obj n)) → IsConstructibleSetSheaf B X c.pt →
      ∃ (n : ℕ) (r : c.pt ⟶ M.obj n),
        EssentiallyConstantInd.IsEssentiallyConstantWith M c n r)
    (F : Sheaf (SmallEtale.topology B X.obj X.property) (Type (u + 1)))
    (hF : IsConstructibleSetSheaf B X F) :
    IsNoetherianObject F
```

**`AlgebraicGeometry.isNoetherianObject_of_isConstructibleAbelianSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ConstructibleAscendingChain.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ConstructibleAscendingChain.lean#L104). The attribute's comment: “sheaves of abelian groups, carrying Stacks 09BH (a subsheaf of a constructible sheaf of abelian groups is constructible) as the explicit hypothesis hsub and Stacks 095P (a filtered system of constructible sheaves of abelian groups whose colimit is constructible is essentially constant) as the explicit hypothesis hess”.

> **Stacks Project, Tag 09YV** for sheaves of abelian groups. On a Noetherian scheme every
> ascending chain of subsheaves of a constructible sheaf of abelian groups stabilizes.

```lean
public theorem isNoetherianObject_of_isConstructibleAbelianSheaf
    (B : BigEtaleSite.{u}) (X : B.Scheme) [IsNoetherian X.obj]
    [∀ (S T : B.Scheme) (f : T ⟶ S),
      ((smallEtaleBaseChange B f).sheafPushforwardContinuous AddCommGrpCat.{u + 1}
        (SmallEtale.topology B S.obj S.property)
        (SmallEtale.topology B T.obj T.property)).IsRightAdjoint]
    [∀ (T : B.Scheme) (V : SmallEtale B T.obj T.property),
      HasWeakSheafify ((SmallEtale.topology B T.obj T.property).over V) AddCommGrpCat.{u + 1}]
    (hsub : ∀ {G H : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{u + 1}}
      (i : G ⟶ H), Mono i →
      IsConstructibleAbelianSheaf B X H → IsConstructibleAbelianSheaf B X G)
    (hess : ∀ (M : ℕ ⥤ Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{u + 1})
      (c : Cocone M), IsColimit c →
      (∀ n, IsConstructibleAbelianSheaf B X (M.obj n)) →
      IsConstructibleAbelianSheaf B X c.pt →
      ∃ (n : ℕ) (r : c.pt ⟶ M.obj n),
        EssentiallyConstantInd.IsEssentiallyConstantWith M c n r)
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{u + 1})
    (hF : IsConstructibleAbelianSheaf B X F) :
    IsNoetherianObject F
```

**`AlgebraicGeometry.isNoetherianObject_of_isConstructibleModuleSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ConstructibleAscendingChain.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ConstructibleAscendingChain.lean#L136). The attribute's comment: “sheaves of modules over a Noetherian ring, carrying Stacks 09BH (a subsheaf of a constructible sheaf of modules is constructible) as the explicit hypothesis hsub and Stacks 095P (a filtered system of constructible sheaves of modules whose colimit is constructible is essentially constant) as the explicit hypothesis hess”.

> **Stacks Project, Tag 09YV** for sheaves of modules. On a Noetherian scheme, and over a
> Noetherian coefficient ring, every ascending chain of subsheaves of a constructible sheaf of
> modules stabilizes.

```lean
public theorem isNoetherianObject_of_isConstructibleModuleSheaf
    (B : BigEtaleSite.{u}) (X : B.Scheme) [IsNoetherian X.obj]
    (R : Type r) [CommRing R] [IsNoetherianRing R]
    [∀ (S T : B.Scheme) (f : T ⟶ S),
      ((smallEtaleBaseChange B f).sheafPushforwardContinuous (ModuleCat.{w} R)
        (SmallEtale.topology B S.obj S.property)
        (SmallEtale.topology B T.obj T.property)).IsRightAdjoint]
    [∀ (T : B.Scheme) (V : SmallEtale B T.obj T.property),
      HasWeakSheafify ((SmallEtale.topology B T.obj T.property).over V) (ModuleCat.{w} R)]
    [HasSheafify (SmallEtale.topology B X.obj X.property) (ModuleCat.{w} R)]
    (hsub : ∀ {G H : Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{w} R)}
      (i : G ⟶ H), Mono i →
      IsConstructibleModuleSheaf B X R H → IsConstructibleModuleSheaf B X R G)
    (hess : ∀ (M : ℕ ⥤ Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{w} R))
      (c : Cocone M), IsColimit c →
      (∀ n, IsConstructibleModuleSheaf B X R (M.obj n)) →
      IsConstructibleModuleSheaf B X R c.pt →
      ∃ (n : ℕ) (r : c.pt ⟶ M.obj n),
        EssentiallyConstantInd.IsEssentiallyConstantWith M c n r)
    (F : Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{w} R))
    (hF : IsConstructibleModuleSheaf B X R F) :
    IsNoetherianObject F
```

**`AlgebraicGeometry.isNoetherianObject_of_isConstructibleSetSheaf'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ConstructibleAscendingChainSetsAbelian.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ConstructibleAscendingChainSetsAbelian.lean#L79). The attribute's comment: “sheaves of sets: on a Noetherian scheme a constructible sheaf of sets on the small etale site is a Noetherian object, so every ascending chain of subsheaves stabilizes”. References: SGA 4 IX (2.9), “(ii)”.

> **Stacks 09YV for sheaves of sets.** On a Noetherian scheme every ascending chain of
> subsheaves of a constructible sheaf of sets on the small étale site stabilizes: the sheaf is a
> Noetherian object of the category of sheaves of sets.
>
> Stacks 09BH (1) and Stacks 095P (1) are supplied to
> `AlgebraicGeometry.isNoetherianObject_of_isConstructibleSetSheaf` by
> `AlgebraicGeometry.isConstructibleSetSheaf_of_mono` and
> `AlgebraicGeometry.exists_isEssentiallyConstantWith_of_isConstructibleSetSheaf_colimit`.

```lean
public theorem isNoetherianObject_of_isConstructibleSetSheaf'
    (B : BigEtaleSite.{u}) (X : B.Scheme) [IsNoetherian X.obj]
    (F : Sheaf (SmallEtale.topology B X.obj X.property) (Type (u + 1)))
    (hF : IsConstructibleSetSheaf B X F) :
    IsNoetherianObject F
```

**`AlgebraicGeometry.isNoetherianObject_of_isConstructibleAbelianSheaf'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ConstructibleAscendingChainSetsAbelian.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ConstructibleAscendingChainSetsAbelian.lean#L103). The attribute's comment: “sheaves of abelian groups: on a Noetherian scheme a constructible abelian sheaf on the small etale site is a Noetherian object, so every ascending chain of subsheaves stabilizes”. References: SGA 4 IX (2.9), “(ii), special case”.

> **Stacks 09YV for sheaves of abelian groups.** On a Noetherian scheme every ascending chain
> of subsheaves of a constructible sheaf of abelian groups on the small étale site stabilizes: the
> sheaf is a Noetherian object of the category of abelian sheaves.
>
> Stacks 09BH (2) and Stacks 095P (2) are supplied to
> `AlgebraicGeometry.isNoetherianObject_of_isConstructibleAbelianSheaf` by
> `AlgebraicGeometry.isConstructibleAbelianSheaf_of_mono` and
> `AlgebraicGeometry.exists_isEssentiallyConstantWith_of_isConstructibleAbelianSheaf_colimit`.

```lean
public theorem isNoetherianObject_of_isConstructibleAbelianSheaf'
    (B : BigEtaleSite.{u}) (X : B.Scheme) [IsNoetherian X.obj]
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{u + 1})
    (hF : IsConstructibleAbelianSheaf B X F) :
    IsNoetherianObject F
```

**`AlgebraicGeometry.isNoetherianObject_of_isConstructibleModuleSheaf'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ShrinkCoefficients.lean, line 328](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ShrinkCoefficients.lean#L328). The attribute's comment: “sheaves of modules over a Noetherian ring in any universe, with Stacks 09BH and Stacks 095P discharged”. References: SGA 4 IX (2.10).

> **Stacks 09YV for sheaves of modules, with nothing granted and the coefficient ring in any
> universe.** On a Noetherian scheme, over a Noetherian ring, every ascending chain of subsheaves
> of a constructible sheaf of `R`-modules stabilizes.
>
> `AlgebraicGeometry.isNoetherianObject_of_isConstructibleModuleSheaf` carries Stacks 09BH and
> Stacks 095P as the explicit hypotheses `hsub` and `hess`. Both are available above at a
> coefficient ring in any universe, so they are supplied here and nothing is granted. The
> quasi-compactness and quasi-separatedness that Stacks 095P asks of `X` follow from its being
> Noetherian.

```lean
public theorem isNoetherianObject_of_isConstructibleModuleSheaf' [IsNoetherian X.obj]
    [IsNoetherianRing R]
    [HasSheafify (SmallEtale.topology B X.1 X.property) (ModuleCat.{u + 1} R)]
    (F : Sheaf (SmallEtale.topology B X.1 X.property) (ModuleCat.{u + 1} R))
    (hF : IsConstructibleModuleSheaf B X R F) :
    IsNoetherianObject F
```

**`Stacks.EtaleCohomology.FiniteLevelSheaf.isNoetherianObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/LevelConstructibility.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LAdicSheaves/LevelConstructibility.lean#L95). The attribute's comment: “sheaves of modules, at the coefficients Z/l^\{n+1}Z of a finite level of an l-adic sheaf”.

> A constructible finite-level sheaf is a Noetherian object: every ascending chain of subsheaves
> of it stabilises.

```lean
public theorem isNoetherianObject (n : ℕ) (F : FiniteLevelSheaf.{u, u + 1} B X ℓ n)
    (hF : IsConstructibleModuleSheaf B X (ZMod (ℓ ^ (n + 1))) F) :
    IsNoetherianObject F
```

## Tag 09Z6, a lemma

[Tag 09Z6](https://stacks.math.columbia.edu/tag/09Z6) in the Stacks Project.

**`Stacks.EtaleCohomology.exists_mono_biproduct_etaleModuleDirectImage_constantSheaf_and_nsmul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleEmbedding/Main.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleEmbedding/Main.lean#L74). The attribute's comment: “(3)”.

> **Stacks 09Z6 (3), with the refinement of its last sentence.** Let `X` be a Noetherian scheme,
> `Λ` a Noetherian ring and `ℱ` a constructible sheaf of `Λ`-modules on `X_étale`. There is an
> injective map of sheaves of modules `ℱ ⟶ ⨁ᵢ fᵢ_* M̲ᵢ` into a finite direct sum, with
> `fᵢ : Yᵢ ⟶ X` finite (and of finite presentation) and `Mᵢ` a finite `Λ`-module. Moreover each
> `Yᵢ` is irreducible and reduced and maps onto an irreducible and reduced closed subscheme `Zᵢ` of
> `X` such that `Yᵢ ⟶ Zᵢ` is finite étale over a nonempty open of `Zᵢ`
> (`AlgebraicGeometry.IsGenericallyFiniteEtaleOntoImage`). In addition, every integer killing `ℱ`
> kills the `Mᵢ`.
>
> The ring `Λ` lives in `Type (u + 1)`, the universe of the library's constructibility theory.

```lean
theorem exists_mono_biproduct_etaleModuleDirectImage_constantSheaf_and_nsmul
    {X : Scheme.{u}} [IsNoetherian X] (F : EtaleModules.{u, u + 1} Λ X)
    (hF : IsConstructibleEtaleModule Λ F) :
    ∃ (n : ℕ) (Y : Fin n → Scheme.{u}) (f : ∀ k, Y k ⟶ X) (_ : ∀ k, IsFinite (f k))
      (_ : ∀ k, FinitePresentation (f k)) (M : Fin n → ModuleCat.{u + 1} Λ)
      (_ : ∀ k, Module.Finite Λ (M k))
      (φ : F ⟶ ⨁ fun k => (etaleModuleDirectImage.{u, u + 1} Λ (f k)).obj
        ((constantSheaf (Y k).smallEtaleTopology (ModuleCat.{u + 1} Λ)).obj (M k))),
      Mono φ ∧ (∀ N : ℕ, N • 𝟙 F = 0 → ∀ k (m : M k), N • m = 0) ∧
        ∀ k, IsGenericallyFiniteEtaleOntoImage (f k)
```

**`Stacks.EtaleCohomology.exists_mono_biproduct_etaleAbelianDirectImage_constantSheaf_isGenericallyFiniteEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleEmbedding/Main.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleEmbedding/Main.lean#L122). The attribute's comment: “(2)”. References: SGA 4 XIV (1.11), “special case”; SGA 4½ Arcata (4.3.2), “(i) ⇒ (ii)”.

> **Stacks 09Z6 (2), with the refinement of its last sentence.** Let `X` be a Noetherian
> scheme and `ℱ` a constructible abelian sheaf on `X_étale`. There is an injective map of abelian
> sheaves `ℱ ⟶ ⨁ᵢ fᵢ_* M̲ᵢ` into a finite direct sum, with `fᵢ : Yᵢ ⟶ X` finite (and of finite
> presentation) and `Mᵢ` a finite abelian group. Moreover each `Yᵢ` is irreducible and reduced and
> maps onto an irreducible and reduced closed subscheme `Zᵢ` of `X` such that `Yᵢ ⟶ Zᵢ` is finite
> étale over a nonempty open of `Zᵢ` (`AlgebraicGeometry.IsGenericallyFiniteEtaleOntoImage`).
>
> The abelian sheaves take values in `AddCommGrpCat.{u + 1}` (constructibility in the universe
> `v = 0` of `_root_.Stacks.EtaleCohomology.IsConstructibleSmallEtaleAbelianSheaf`), the universe of
> the library's constructibility theory; the proof views them as sheaves of `ULift ℤ`-modules.

```lean
theorem exists_mono_biproduct_etaleAbelianDirectImage_constantSheaf_isGenericallyFiniteEtale
    {X : Scheme.{u}}
    [IsNoetherian X] (F : Sheaf X.smallEtaleTopology AddCommGrpCat.{u + 1})
    (hF : _root_.Stacks.EtaleCohomology.IsConstructibleSmallEtaleAbelianSheaf.{u, 0} F) :
    ∃ (J : Type) (_ : Finite J) (Y : J → Scheme.{u}) (f : ∀ j, Y j ⟶ X)
      (_ : ∀ j, IsFinite (f j)) (_ : ∀ j, FinitePresentation (f j))
      (M : J → AddCommGrpCat.{u + 1}) (_ : ∀ j, Finite (M j))
      (m : F ⟶ ⨁ fun j => (etaleAbelianDirectImage.{u, 0} (f j)).obj
        ((constantSheaf (Y j).smallEtaleTopology AddCommGrpCat.{u + 1}).obj (M j))),
      Mono m ∧ ∀ j, IsGenericallyFiniteEtaleOntoImage (f j)
```

**`Stacks.EtaleCohomology.exists_mono_pi_smallEtalePushforward_constantSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleEmbedding/Sets.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleEmbedding/Sets.lean#L176). The attribute's comment: “(1)”. References: SGA 4 IX (2.14), “(ii), special case”.

> **Stacks 09Z6 (1), with the refinement of its last sentence.** Let `X` be a Noetherian scheme
> and `ℱ` a constructible sheaf of sets on `X_étale`. There is an injective map of sheaves
> `ℱ ⟶ ∏ᵢ fᵢ_* E̲ᵢ` into a finite product, with `fᵢ : Yᵢ ⟶ X` finite (and of finite presentation)
> and `Eᵢ` a finite set. Moreover each `Yᵢ` is irreducible and reduced and maps onto an irreducible
> and reduced closed subscheme `Zᵢ` of `X` such that `Yᵢ ⟶ Zᵢ` is finite étale over a nonempty open
> of `Zᵢ` (`AlgebraicGeometry.IsGenericallyFiniteEtaleOntoImage`).
>
> The sheaves of sets take values in `Type (u + 1)`, the universe of
> `AlgebraicGeometry.IsConstructibleSetSheaf`.

```lean
theorem exists_mono_pi_smallEtalePushforward_constantSheaf {X : Scheme.{u}} [IsNoetherian X]
    (F : Sheaf X.smallEtaleTopology (Type (u + 1))) (hF : IsConstructibleEtaleSetSheaf F) :
    ∃ (n : ℕ) (Y : Fin n → Scheme.{u}) (f : ∀ k, Y k ⟶ X) (_ : ∀ k, IsFinite (f k))
      (_ : ∀ k, FinitePresentation (f k)) (E : Fin n → Type (u + 1)) (_ : ∀ k, Finite (E k))
      (φ : F ⟶ ∏ᶜ fun k => (smallEtalePushforward (f k) (Type (u + 1))).obj
        ((constantSheaf (Y k).smallEtaleTopology (Type (u + 1))).obj (E k))),
      Mono φ ∧ ∀ k, IsGenericallyFiniteEtaleOntoImage (f k)
```

## Tag 09Z7, a lemma

[Tag 09Z7](https://stacks.math.columbia.edu/tag/09Z7) in the Stacks Project.

**`Stacks.EtaleCohomology.exists_mono_biproduct_etaleAbelianDirectImage_constantSheaf_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/FinitePushforwardEmbedding.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/FinitePushforwardEmbedding.lean#L117). The attribute's comment: “(2)”. References: SGA 4 IX (2.14), “(ii), special case”; SGA 4 XIV (1.11), “special case”; SGA 4½ Arcata (4.3.2), “(i) ⇒ (ii)”.

> **Stacks Project, Tag 09Z7, part (2).** Let `X` be a quasi-compact and quasi-separated scheme
> and `F` a constructible abelian sheaf on `X_étale`. There is an injective map of abelian sheaves
> `F ⟶ ⨁ⱼ fⱼ_* Mⱼ` into a finite direct sum, where each `fⱼ : Yⱼ ⟶ X` is finite and of finite
> presentation and each `Mⱼ` is a finite abelian group.
>
> The proof descends `F` to a Noetherian stage of an absolute Noetherian approximation of `X`
> (Stacks 01ZA, the essential-surjectivity assertion of Stacks 09YU), embeds it there (Stacks 09Z6
> (2)), and pulls the embedding back, the inverse image of each finite pushforward being the finite
> pushforward along the base change (Stacks 0959).

```lean
theorem exists_mono_biproduct_etaleAbelianDirectImage_constantSheaf_of_qcqs (X : Scheme.{u})
    [CompactSpace X] [QuasiSeparatedSpace X]
    (F : Sheaf X.smallEtaleTopology AddCommGrpCat.{u + 1})
    (hF : IsConstructibleSmallEtaleAbelianSheaf.{u, 0} F) :
    ∃ (J : Type) (_ : Finite J) (Y : J → Scheme.{u}) (f : ∀ j, Y j ⟶ X)
      (_ : ∀ j, IsFinite (f j)) (_ : ∀ j, FinitePresentation (f j))
      (M : J → AddCommGrpCat.{u + 1}) (_ : ∀ j, Finite (M j))
      (m : F ⟶ ⨁ fun j => (etaleAbelianDirectImage.{u, 0} (f j)).obj
        ((constantSheaf (Y j).smallEtaleTopology AddCommGrpCat.{u + 1}).obj (M j))),
      Mono m
```

**`Stacks.EtaleCohomology.exists_mono_biproduct_etaleModuleDirectImage_constantSheaf_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/FinitePushforwardEmbedding.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/FinitePushforwardEmbedding.lean#L170). The attribute's comment: “(3)”. References: SGA 4 IX (2.14), “(ii), A-modules”.

> **Stacks Project, Tag 09Z7, part (3).** Let `X` be a quasi-compact and quasi-separated scheme,
> `Λ` a Noetherian ring and `F` a constructible sheaf of `Λ`-modules on `X_étale`. There is an
> injective map of sheaves of modules `F ⟶ ⨁ᵢ fᵢ_* M̲ᵢ` into a finite direct sum, where each
> `fᵢ : Yᵢ ⟶ X` is finite and of finite presentation and each `Mᵢ` is a finite `Λ`-module.
>
> The proof descends `F` to a Noetherian stage of an absolute Noetherian approximation of `X`
> (Stacks 01ZA, the essential-surjectivity assertion of Stacks 09YU), embeds it there (Stacks 09Z6
> (3)), and pulls the embedding back, the inverse image of each finite pushforward being the finite
> pushforward along the base change (Stacks 0959). The ring `Λ` lives in `Type (u + 1)`, the
> universe of Stacks 09Z6 (3).

```lean
theorem exists_mono_biproduct_etaleModuleDirectImage_constantSheaf_of_qcqs
    (Λ : Type (u + 1)) [CommRing Λ] [IsNoetherianRing Λ] (X : Scheme.{u})
    [CompactSpace X] [QuasiSeparatedSpace X] (F : EtaleModules.{u, u + 1} Λ X)
    (hF : IsConstructibleEtaleModule Λ F) :
    ∃ (n : ℕ) (Y : Fin n → Scheme.{u}) (f : ∀ k, Y k ⟶ X) (_ : ∀ k, IsFinite (f k))
      (_ : ∀ k, FinitePresentation (f k)) (M : Fin n → ModuleCat.{u + 1} Λ)
      (_ : ∀ k, Module.Finite Λ (M k))
      (φ : F ⟶ ⨁ fun k => (etaleModuleDirectImage.{u, u + 1} Λ (f k)).obj
        ((constantSheaf (Y k).smallEtaleTopology (ModuleCat.{u + 1} Λ)).obj (M k))),
      Mono φ
```

**`Stacks.EtaleCohomology.exists_mono_pi_smallEtalePushforward_constantSheaf_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/FinitePushforwardEmbedding.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/FinitePushforwardEmbedding.lean#L230). The attribute's comment: “(1)”. References: SGA 4 IX (2.14), “(ii), sheaves of sets”.

> **Stacks Project, Tag 09Z7, part (1).** Let `X` be a quasi-compact and quasi-separated scheme
> and `F` a constructible sheaf of sets on `X_étale`. There is an injective map of sheaves
> `F ⟶ ∏ᵢ fᵢ_* E̲ᵢ` into a finite product, where each `fᵢ : Yᵢ ⟶ X` is finite and of finite
> presentation and each `Eᵢ` is a finite set.
>
> As for Stacks 09Z6 (1), the proof goes through part (3) over the finite ring
> `Λ = ULift (ZMod 2)`: `F` embeds in the free sheaf of `Λ`-modules `Λ[F]`
> (`CategoryTheory.Sheaf.mono_adjunction_free_unit`), which is constructible
> (`Stacks.EtaleCohomology.isConstructibleEtaleModule_composeAndSheafify_free`); part (3) embeds
> `Λ[F]` in `⨁ᵢ fᵢ_* M̲ᵢ`, and forgetting the module structure carries this to `∏ᵢ fᵢ_* M̲ᵢ` with
> the `Mᵢ` finite sets. The sheaves of sets take values in `Type (u + 1)`, the universe of
> `AlgebraicGeometry.IsConstructibleSetSheaf`.

```lean
theorem exists_mono_pi_smallEtalePushforward_constantSheaf_of_qcqs (X : Scheme.{u})
    [CompactSpace X] [QuasiSeparatedSpace X]
    (F : Sheaf X.smallEtaleTopology (Type (u + 1))) (hF : IsConstructibleEtaleSetSheaf F) :
    ∃ (n : ℕ) (Y : Fin n → Scheme.{u}) (f : ∀ k, Y k ⟶ X) (_ : ∀ k, IsFinite (f k))
      (_ : ∀ k, FinitePresentation (f k)) (E : Fin n → Type (u + 1)) (_ : ∀ k, Finite (E k))
      (φ : F ⟶ ∏ᶜ fun k => (smallEtalePushforward (f k) (Type (u + 1))).obj
        ((constantSheaf (Y k).smallEtaleTopology (Type (u + 1))).obj (E k))),
      Mono φ
```

## Tag 0F0N, a lemma

[Tag 0F0N](https://stacks.math.columbia.edu/tag/0F0N) in the Stacks Project.

**`AlgebraicGeometry.exists_isFilteredColimit_isConstructibleModuleSheaf_isClosed_support`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/SpecializationClosedSupportColimit.lean, line 461](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/SpecializationClosedSupportColimit.lean#L461). The attribute's comment: “part (2); Stacks 03SA (3), Stacks 093C, Stacks 03S8 for sheaves of modules, Stacks 09BH (3), Stacks 09YS (3), Stacks 0903, Stacks 095E, Stacks 09YR and Stacks 03RZ (3) are all discharged from the library”.

> **Stacks 0F0N, part (2).** Let `X` be a Noetherian scheme, let `Λ` be a Noetherian ring and
> let `E ⊆ X` be stable under specialization. A sheaf of `Λ`-modules `F` on the small étale site of
> `X` whose support is contained in `E` is a filtered colimit of constructible sheaves of
> `Λ`-modules, each of whose supports is contained in a closed subset of `E`.
>
> The source says of this part only that it is "exactly the same" as part (1), and so it is: write
> `F` as a filtered colimit of constructible sheaves of `Λ`-modules by Stacks 03SA (3) — which is
> in the library — replace each term by the image of its map to `F`, and run the same three steps,
> with Stacks 09BH (3) in place of Stacks 09BH (2) and Stacks 09YS (3) in place of
> Stacks 09YS (2).
>
> Stacks 03SA (3) enters as the unconditional
> `AlgebraicGeometry.exists_isFilteredColimit_isConstructibleModuleSheaf_of_qcqs`, so neither
> Stacks 093C in the shriek spelling nor the sheaves-of-modules case of Stacks 03S8 has to be
> supplied here. Stacks 09BH (3) enters through
> `AlgebraicGeometry.isConstructibleModuleSheaf_forall_epi`, whose own geometric step is
> `AlgebraicGeometry.finiteTypeLocallyConstantSubsheavesAreConstructible`. So this statement
> assumes nothing.

```lean
public theorem exists_isFilteredColimit_isConstructibleModuleSheaf_isClosed_support
    [IsNoetherian X.obj]
    (E : Set X.obj) (hE : StableUnderSpecialization E)
    (F : Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{u + 1} Λ))
    (hsupp : supportModuleSheaf B X Λ F ⊆ E) :
    ∃ (I : Type (u + 1)) (_ : SmallCategory I) (_ : IsFiltered I)
      (D : I ⥤ Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{u + 1} Λ))
      (ι : D ⟶ (Functor.const I).obj F), Nonempty (IsColimit (Cocone.mk F ι)) ∧
        ∀ i, IsConstructibleModuleSheaf B X Λ (D.obj i) ∧
          ∃ Z : Set X.obj, IsClosed Z ∧ Z ⊆ E ∧ supportModuleSheaf B X Λ (D.obj i) ⊆ Z
```

**`AlgebraicGeometry.exists_isFilteredColimit_isConstructibleAbelianSheaf_isClosed_support_of_torsion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/SpecializationClosedSupportTorsionColimit.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/SpecializationClosedSupportTorsionColimit.lean#L48). The attribute's comment: “part (1), torsion abelian sheaves, torsion in the local sense of Stacks 0DD7”. References: SGA 4½ Arcata (4.3.3), “more general”.

> Let `X` be a Noetherian scheme and let `E ⊆ X` be stable under specialization. A torsion
> abelian sheaf `F` on the small étale site of `X` whose support is contained in `E` is a filtered
> colimit of constructible abelian sheaves, each of whose supports is contained in a closed subset
> of `E`. Here torsion is the local condition `Stacks.Torsion.torsionSheafProperty`.

```lean
public theorem exists_isFilteredColimit_isConstructibleAbelianSheaf_isClosed_support_of_torsion
    (B : BigEtaleSite.{u}) (X : B.Scheme) [IsNoetherian X.obj]
    (E : Set X.obj) (hE : StableUnderSpecialization E)
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{u + 1})
    (hF : Stacks.Torsion.torsionSheafProperty (SmallEtale.topology B X.obj X.property) F)
    (hsupp : supportSheaf B X.obj X.property F ⊆ E) :
    ∃ (I : Type (u + 1)) (_ : SmallCategory I) (_ : IsFiltered I)
      (D : I ⥤ Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{u + 1})
      (ι : D ⟶ (Functor.const I).obj F), Nonempty (IsColimit (Cocone.mk F ι)) ∧
        ∀ i, IsConstructibleAbelianSheaf B X (D.obj i) ∧
          ∃ Z : Set X.obj, IsClosed Z ∧ Z ⊆ E ∧
            supportSheaf B X.obj X.property (D.obj i) ⊆ Z
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.74, Tag 03RY](https://stacks.math.columbia.edu/tag/03RY)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
