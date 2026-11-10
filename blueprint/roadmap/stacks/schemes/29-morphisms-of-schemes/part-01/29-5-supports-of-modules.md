---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.Modules.fromSpec_preimage_supp, AlgebraicGeometry.Scheme.Modules.mem_support_sections_iff_mem_supp, AlgebraicGeometry.Scheme.Modules.stableUnderSpecialization_supp, SheafOfModules.isClosed_supp, SheafOfModules.mem_supp_iff_nontrivial_stalk, AlgebraicGeometry.Scheme.Modules.nontrivial_stalk_iff_nontrivial_fibre, AlgebraicGeometry.SheafOfModules.pullback_isFiniteType, Stacks.Modules.supp_pullback
statement: formalized
proof: formalized
---

# 29.5 Supports of modules

Section 29.5 of the Stacks Project, [Tag 056H](https://stacks.math.columbia.edu/tag/056H). 6 tags here are carried by 16 declarations of the repository (all in StacksFrontier) and 16 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 056H, the section

[Tag 056H](https://stacks.math.columbia.edu/tag/056H) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.fromSpec_preimage_supp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Support/SupportsOfModules.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/SupportsOfModules.lean#L41). The attribute's comment: “the sheaf-theoretic and module-theoretic supports agree”.

> **The sheaf-theoretic and module-theoretic supports agree.** The inverse image of the
> support of a quasi-coherent module `F` under the inclusion `Spec Γ(X, U) → X` of an affine open
> `U` is the support of the `Γ(X, U)`-module `Γ(F, U)`.

```lean
public theorem fromSpec_preimage_supp {X : Scheme.{u}} (F : X.Modules) [F.IsQuasicoherent]
    (U : X.affineOpens) :
    ⇑U.2.fromSpec ⁻¹' SheafOfModules.supp F = Module.support Γ(X, U.1) Γ(F, U.1)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.Modules.mem_support_sections_iff_mem_supp`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/AffineOpen.lean#L52), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Support/SupportsOfModules.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/SupportsOfModules.lean#L62) (StacksFrontier): “Lemma 29.5.1: on an affine open the supports agree”.
- [`AlgebraicGeometry.Scheme.Modules.stableUnderSpecialization_supp`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/Specialization.lean#L41), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Support/SupportsOfModules.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/SupportsOfModules.lean#L65) (StacksFrontier): “Lemma 29.5.2: the support is stable under specialization”.
- [`SheafOfModules.isClosed_supp`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Support.lean#L151), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Support/SupportsOfModules.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/SupportsOfModules.lean#L68) (StacksFrontier): “Lemma 29.5.3 part (1): the support of a finite type module is closed”.
- [`SheafOfModules.mem_supp_iff_nontrivial_stalk`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/Defs.lean#L53), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Support/SupportsOfModules.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/SupportsOfModules.lean#L71) (StacksFrontier): “Lemma 29.5.3 part (2): the support is where the stalk is nonzero”.
- [`AlgebraicGeometry.Scheme.Modules.nontrivial_stalk_iff_nontrivial_fibre`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/FiniteType.lean#L218), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Support/SupportsOfModules.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/SupportsOfModules.lean#L74) (StacksFrontier): “Lemma 29.5.3 part (2): nonzero stalk is nonzero fibre”.
- [`AlgebraicGeometry.SheafOfModules.pullback_isFiniteType`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/FiniteType.lean#L304), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Support/SupportsOfModules.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/SupportsOfModules.lean#L77) (StacksFrontier): “Lemma 29.5.3 part (3): a pullback of a finite type module is of finite type”.
- [`Stacks.Modules.supp_pullback`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/PullbackSkyscraper.lean#L139), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Support/SupportsOfModules.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/SupportsOfModules.lean#L80) (StacksFrontier): “Lemma 29.5.3 part (3): the support of a pullback is the inverse image”.
- [`AlgebraicGeometry.Scheme.Modules.schemeTheoreticSupport`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/SchemeTheoretic.lean#L94), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Support/SupportsOfModules.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/SupportsOfModules.lean#L83) (StacksFrontier): “Lemma 29.5.4 and Definition 29.5.5: the scheme-theoretic support”.
- [`AlgebraicGeometry.Scheme.Modules.schemeTheoreticSupport_ideal`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/SchemeTheoretic.lean#L102), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Support/SupportsOfModules.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/SupportsOfModules.lean#L86) (StacksFrontier): “Lemma 29.5.4 part (1): the affine annihilator formula”.
- [`AlgebraicGeometry.Scheme.Modules.exists_module_on_schemeTheoreticSupport`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/SchemeTheoretic.lean#L177), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Support/SupportsOfModules.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/SupportsOfModules.lean#L89) (StacksFrontier): “Lemma 29.5.4: the module descends to its scheme-theoretic support”.
- [`AlgebraicGeometry.Scheme.Modules.schemeTheoreticSupport_isSmallest`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/SchemeTheoretic.lean#L189), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Support/SupportsOfModules.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/SupportsOfModules.lean#L92) (StacksFrontier): “Lemma 29.5.4: minimality of the scheme-theoretic support”.
- [`AlgebraicGeometry.Scheme.Modules.module_on_schemeTheoreticSupport_unique`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/SchemeTheoretic.lean#L203), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Support/SupportsOfModules.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/SupportsOfModules.lean#L95) (StacksFrontier): “Lemma 29.5.4 part (2): uniqueness of the descended module”.
- [`AlgebraicGeometry.Scheme.Modules.module_on_schemeTheoreticSupport_isFiniteType`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/SchemeTheoretic.lean#L219), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Support/SupportsOfModules.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/SupportsOfModules.lean#L98) (StacksFrontier): “Lemma 29.5.4 part (3): the descended module is of finite type”.
- [`AlgebraicGeometry.Scheme.Modules.supp_eq_support_schemeTheoreticSupport`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/SchemeTheoretic.lean#L256), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Support/SupportsOfModules.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/SupportsOfModules.lean#L101) (StacksFrontier): “Lemma 29.5.4 part (4): the support is the scheme-theoretic support”.
- [`AlgebraicGeometry.Scheme.Modules.module_on_schemeTheoreticSupport_support`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/SchemeTheoretic.lean#L269), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Support/SupportsOfModules.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/SupportsOfModules.lean#L104) (StacksFrontier): “Lemma 29.5.4 part (4): the descended module has support everything”.

## Tag 056I, a lemma

[Tag 056I](https://stacks.math.columbia.edu/tag/056I) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.mem_support_sections_iff_mem_supp`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Support/AffineOpen.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/AffineOpen.lean#L52).

> On an affine open, support of the sections module agrees with support of the
> quasi-coherent sheaf.

```lean
public lemma mem_support_sections_iff_mem_supp {X : Scheme.{u}} (F : X.Modules)
    [F.IsQuasicoherent] (U : X.affineOpens) (x : X) (hx : x ∈ U.1) :
    U.2.primeIdealOf ⟨x, hx⟩ ∈ Module.support Γ(X, U.1) Γ(F, U.1) ↔
      x ∈ SheafOfModules.supp F
```

## Tag 05AC, a lemma

[Tag 05AC](https://stacks.math.columbia.edu/tag/05AC) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.stableUnderSpecialization_supp`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Support/Specialization.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/Specialization.lean#L41).

> The support of a quasi-coherent sheaf of modules on a scheme is stable under
> specialization.

```lean
public lemma stableUnderSpecialization_supp (X : Scheme.{u}) (F : X.Modules)
    [F.IsQuasicoherent] : StableUnderSpecialization (SheafOfModules.supp F)
```

## Tag 056J, a lemma

[Tag 056J](https://stacks.math.columbia.edu/tag/056J) in the Stacks Project.

**`SheafOfModules.isClosed_supp`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Support.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Support.lean#L151). The attribute's comment: “closed_support”.

> The support of a sheaf of modules of finite type on a topological space is closed.

```lean
lemma isClosed_supp {X : TopCat.{u}} {R : TopCat.Sheaf RingCat.{u} X}
    (F : SheafOfModules.{u} R) [F.IsFiniteType] :
    IsClosed (supp F)
```

**`SheafOfModules.mem_supp_iff_nontrivial_stalk`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Support/Defs.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/Defs.lean#L53). The attribute's comment: “support_by_stalk”.

> A point is in the support of a sheaf of modules if and only if its stalk is nonzero.

```lean
lemma mem_supp_iff_nontrivial_stalk {X : TopCat.{u}}
    {R : TopCat.Sheaf RingCat.{u} X} (F : SheafOfModules.{u} R) (x : X) :
    x ∈ supp F ↔
      Nontrivial ((show TopCat.Presheaf Ab.{u} X from F.val.presheaf).stalk x)
```

**`AlgebraicGeometry.Scheme.Modules.nontrivial_stalk_iff_nontrivial_fibre`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Support/FiniteType.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/FiniteType.lean#L218). The attribute's comment: “support_by_fibre”.

> A finite type quasi-coherent module has nonzero stalk at `x` exactly when its fibre over
> the residue field at `x` is nonzero.

```lean
lemma nontrivial_stalk_iff_nontrivial_fibre
    {X : Scheme.{u}} (F : X.Modules) [F.IsFiniteType] [F.IsQuasicoherent] (x : X) :
    letI : Module (X.presheaf.stalk x) (F.presheaf.stalk x) :=
      PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
        F.val x
    letI : Algebra (X.presheaf.stalk x) (X.residueField x) :=
      (X.residue x).hom.toAlgebra
    Nontrivial (F.presheaf.stalk x) ↔
      Nontrivial (TensorProduct (X.presheaf.stalk x)
        (F.presheaf.stalk x) (X.residueField x))
```

**`SheafOfModules.supp_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportPullback/Basic.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportPullback/Basic.lean#L51). The attribute's comment: “pullback_support”.

> **Stacks Project, Tag 056J.** The support of the pullback of a module of finite type
> along a morphism of schemes is the inverse image of its support.

```lean
theorem supp_pullback {X Y : Scheme.{u}} (f : Y ⟶ X) (F : X.Modules) [F.IsFiniteType] :
    supp ((Scheme.Modules.pullback f).obj F) = f ⁻¹' supp F
```

Declarations registered for the tag:

- [`AlgebraicGeometry.SheafOfModules.pullback_isFiniteType`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/FiniteType.lean#L304), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Support/Pullback.lean, line 29](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/Pullback.lean#L29) (StacksFrontier): “pullback_finite_type”.

## Tag 05JU, a lemma

[Tag 05JU](https://stacks.math.columbia.edu/tag/05JU) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.schemeTheoreticSupport`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Support/SchemeTheoretic.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/SchemeTheoretic.lean#L94). The attribute's comment: “the closed subscheme”.

> **The scheme-theoretic support of a finite type quasi-coherent module**, as an ideal sheaf:
> its component at an affine open `U` is the annihilator of the `Γ(X, U)`-module `Γ(F, U)`. The
> closed subscheme it cuts out is the smallest one from which `F` is a direct image.

```lean
def schemeTheoreticSupport : X.IdealSheafData
```

**`AlgebraicGeometry.Scheme.Modules.schemeTheoreticSupport_ideal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Support/SchemeTheoretic.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/SchemeTheoretic.lean#L102). The attribute's comment: “part (1): affine annihilator formula”.

> On an affine open `U = Spec A` the scheme-theoretic support of `F` is cut out by the
> annihilator of the `A`-module `Γ(F, U)`; equivalently, if `F|_U` is `M~` then the
> scheme-theoretic support meets `U` in `Spec (A / Ann_A M)`.

```lean
theorem schemeTheoreticSupport_ideal (U : X.affineOpens) :
    (schemeTheoreticSupport F).ideal U = Module.annihilator Γ(X, U.1) Γ(F, U.1)
```

**`AlgebraicGeometry.Scheme.Modules.exists_module_on_schemeTheoreticSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Support/SchemeTheoretic.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/SchemeTheoretic.lean#L177). The attribute's comment: “existence of the descended module”.

> A quasi-coherent module of finite type is the direct image of a quasi-coherent module of
> finite type on its scheme-theoretic support.

```lean
theorem exists_module_on_schemeTheoreticSupport :
    ∃ G : (schemeTheoreticSupport F).subscheme.Modules,
      G.IsQuasicoherent ∧ G.IsFiniteType ∧
        Nonempty ((Scheme.Modules.pushforward
          (schemeTheoreticSupport F).subschemeι).obj G ≅ F)
```

**`AlgebraicGeometry.Scheme.Modules.schemeTheoreticSupport_isSmallest`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Support/SchemeTheoretic.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/SchemeTheoretic.lean#L189). The attribute's comment: “minimality”.

> Every closed subscheme of `X` from which `F` is a direct image contains the
> scheme-theoretic support of `F`; equivalently, its ideal sheaf is contained in the ideal sheaf
> of the scheme-theoretic support.

```lean
theorem schemeTheoreticSupport_isSmallest (J : X.IdealSheafData)
    (G : J.subscheme.Modules)
    (e : (Scheme.Modules.pushforward J.subschemeι).obj G ≅ F) :
    J ≤ schemeTheoreticSupport F
```

**`AlgebraicGeometry.Scheme.Modules.module_on_schemeTheoreticSupport_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Support/SchemeTheoretic.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/SchemeTheoretic.lean#L203). The attribute's comment: “part (2): uniqueness”.

> A descent of `F` to its scheme-theoretic support is unique up to a unique isomorphism
> compatible with the chosen identifications of the direct images with `F`.

```lean
theorem module_on_schemeTheoreticSupport_unique
    (G H : (schemeTheoreticSupport F).subscheme.Modules)
    (eG : (Scheme.Modules.pushforward (schemeTheoreticSupport F).subschemeι).obj G ≅ F)
    (eH : (Scheme.Modules.pushforward (schemeTheoreticSupport F).subschemeι).obj H ≅ F) :
    ∃! φ : G ≅ H,
      (Scheme.Modules.pushforward (schemeTheoreticSupport F).subschemeι).map φ.hom ≫
        eH.hom = eG.hom
```

**`AlgebraicGeometry.Scheme.Modules.module_on_schemeTheoreticSupport_isFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Support/SchemeTheoretic.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/SchemeTheoretic.lean#L219). The attribute's comment: “part (3): finite type”.

> Every descent of `F` to its scheme-theoretic support is of finite type.

```lean
theorem module_on_schemeTheoreticSupport_isFiniteType
    (G : (schemeTheoreticSupport F).subscheme.Modules)
    (e : (Scheme.Modules.pushforward (schemeTheoreticSupport F).subschemeι).obj G ≅ F) :
    G.IsFiniteType
```

**`AlgebraicGeometry.Scheme.Modules.supp_eq_support_schemeTheoreticSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Support/SchemeTheoretic.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/SchemeTheoretic.lean#L256). The attribute's comment: “part (4): support on the ambient scheme”.

> The support of `F` is the closed set underlying its scheme-theoretic support.

```lean
theorem supp_eq_support_schemeTheoreticSupport :
    SheafOfModules.supp F = ((schemeTheoreticSupport F).support : Set X)
```

**`AlgebraicGeometry.Scheme.Modules.module_on_schemeTheoreticSupport_support`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Support/SchemeTheoretic.lean, line 269](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/SchemeTheoretic.lean#L269). The attribute's comment: “part (4): support on the closed subscheme”.

> A descent of `F` to its scheme-theoretic support has support the whole closed subscheme.

```lean
theorem module_on_schemeTheoreticSupport_support
    (G : (schemeTheoreticSupport F).subscheme.Modules)
    (e : (Scheme.Modules.pushforward (schemeTheoreticSupport F).subschemeι).obj G ≅ F) :
    SheafOfModules.supp G = Set.univ
```

## Tag 05JV, a definition

[Tag 05JV](https://stacks.math.columbia.edu/tag/05JV) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.schemeTheoreticSupport`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Support/SchemeTheoretic.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Support/SchemeTheoretic.lean#L94). The attribute's comment: “the scheme-theoretic support”.

> **The scheme-theoretic support of a finite type quasi-coherent module**, as an ideal sheaf:
> its component at an affine open `U` is the annihilator of the `Γ(X, U)`-module `Γ(F, U)`. The
> closed subscheme it cuts out is the smallest one from which `F` is a direct image.

```lean
def schemeTheoreticSupport : X.IdealSheafData
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.5, Tag 056H](https://stacks.math.columbia.edu/tag/056H)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
