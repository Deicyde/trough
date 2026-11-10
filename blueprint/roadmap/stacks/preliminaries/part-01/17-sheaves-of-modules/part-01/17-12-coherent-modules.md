---
declaration: section
origin: cited
lean: Stacks.SheafOfModules.IsCoherent, Stacks.SheafOfModules.CoherentModules, AlgebraicGeometry.SheafOfModules.CoherentModules, SheafOfModules.IsCoherent, isFinitePresentation_of_isCoherent, isQuasicoherent_of_isFinitePresentation, Stacks.SheafOfModules.isCoherent_of_mono, Stacks.SheafOfModules.isFiniteType_kernel_of_isCoherent
statement: formalized
proof: formalized
---

# 17.12 Coherent modules

Section 17.12 of the Stacks Project, [Tag 01BU](https://stacks.math.columbia.edu/tag/01BU). 5 tags here are carried by 19 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01BV, a definition

[Tag 01BV](https://stacks.math.columbia.edu/tag/01BV) in the Stacks Project.

**`Stacks.SheafOfModules.IsCoherent`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/Coherent.lean, line 296](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/Coherent.lean#L296). The attribute's comment: “the coherence predicate”. References: EGA 0 (5.3.7).

> A sheaf of modules `M` over a ringed space is *coherent* if
>
> 1. `M` is of finite type, and
> 2. for every open `U` and every finite index type `I`, the kernel of every `O_U`-module map
>    `free I ⟶ M|_U` — equivalently, of the associated map of every finite family of sections of
>    `M` over `U` — is of finite type.

```lean
class IsCoherent (M : SheafOfModules.{u} R) : Prop
```

**`Stacks.SheafOfModules.CoherentModules`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/Coherent.lean, line 313](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/Coherent.lean#L313). The attribute's comment: “the category Coh”.

> The full subcategory `Coh(O_X)` of coherent sheaves of modules over a ringed space.

```lean
abbrev CoherentModules (R : Sheaf (Opens.grothendieckTopology X) RingCat.{u})
```

**`AlgebraicGeometry.SheafOfModules.CoherentModules`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/Coherent.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/Coherent.lean#L45). The attribute's comment: “the category Coh”.

> The full category of coherent sheaves of modules over a ringed space.

```lean
abbrev CoherentModules {X : Type u} [TopologicalSpace X]
    (R : Sheaf (Opens.grothendieckTopology X) RingCat.{u})
```

Declarations registered for the tag:

- [`SheafOfModules.IsCoherent`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/CoherentFinitePresentation.lean#L399), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Modules/Coherent.lean, line 39](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/Coherent.lean#L39) (StacksFrontier): “the coherence predicate”.

## Tag 01BW, a lemma

[Tag 01BW](https://stacks.math.columbia.edu/tag/01BW) in the Stacks Project.

**`isFinitePresentation_of_isCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/CoherentFinitePresentation.lean, line 418](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/CoherentFinitePresentation.lean#L418). The attribute's comment: “(1)”. References: EGA 0 (5.3.2), “first assertion”; SGA 6 I (3.5), “a) (ii)⇒(i)”.

> **Stacks Tag 01BW, implication (1): coherent ⟹ finite presentation.**
> A coherent sheaf of modules over a ringed space is of finite presentation.
>
> The decomposition into `bind_isFinitePresentation` (Lemma A) and
> `over_quasicoherentData_isFP_of_finiteGenerators_finiteKernel` (Lemma B) makes
> this body fully proved (no open goals): take a finite-type local-generators datum,
> apply coherence condition (2) to the finite generators over each cover open to
> learn the kernel is finite type, feed that to Lemma B, and glue with Lemma A.

```lean
theorem isFinitePresentation_of_isCoherent (M : SheafOfModules.{u} R)
    [M.IsCoherent] : M.IsFinitePresentation
```

**`isQuasicoherent_of_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/CoherentFinitePresentation.lean, line 445](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/CoherentFinitePresentation.lean#L445). The attribute's comment: “(2)”. References: EGA 0 (5.2.5), “fin. pres. ⇒ quasi-coh.”.

> **Stacks Tag 01BW, implication (2): finite presentation ⟹ quasi-coherent.**
> A sheaf of modules of finite presentation is quasi-coherent. (This is immediate
> from the definitions, since finite free modules are free modules; in Mathlib it
> is recorded as an instance.)

```lean
theorem isQuasicoherent_of_isFinitePresentation (M : SheafOfModules.{u} R)
    [M.IsFinitePresentation] : M.IsQuasicoherent
```

## Tag 01BY, a lemma

[Tag 01BY](https://stacks.math.columbia.edu/tag/01BY) in the Stacks Project.

**`Stacks.SheafOfModules.isCoherent_of_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/Coherent.lean, line 332](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/Coherent.lean#L332). The attribute's comment: “(1)”.

> A finite type subsheaf of a coherent sheaf of modules is coherent: the second condition of
> coherence passes to subsheaves, because a map out of a free module into the subsheaf has the
> same kernel as its composite into the ambient sheaf.

```lean
theorem isCoherent_of_mono {M N : SheafOfModules.{u} R} (ι : N ⟶ M) [Mono ι]
    [IsCoherent M] [N.IsFiniteType] : IsCoherent N
```

**`Stacks.SheafOfModules.isFiniteType_kernel_of_isCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/CoherentWeakSerre.lean, line 522](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/CoherentWeakSerre.lean#L522). The attribute's comment: “(2)”.

> The kernel of a morphism from a sheaf of modules of finite type to a coherent sheaf of modules
> is of finite type.

```lean
theorem isFiniteType_kernel_of_isCoherent {M N : SheafOfModules.{u} R} [M.IsFiniteType]
    [IsCoherent N] (φ : M ⟶ N) : (kernel φ).IsFiniteType
```

**`Stacks.SheafOfModules.isCoherent_kernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/CoherentWeakSerre.lean, line 583](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/CoherentWeakSerre.lean#L583). The attribute's comment: “(3), kernels”.

> The kernel of a morphism of coherent sheaves of modules is coherent.

```lean
theorem isCoherent_kernel {M N : SheafOfModules.{u} R} [IsCoherent M] [IsCoherent N]
    (φ : M ⟶ N) : IsCoherent (kernel φ)
```

**`Stacks.SheafOfModules.isCoherent_X₂_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/CoherentWeakSerre.lean, line 591](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/CoherentWeakSerre.lean#L591). The attribute's comment: “(4)”. References: EGA 0 (5.3.3), “Extension clause”.

> The middle term of a short exact sequence of sheaves of modules whose outer terms are coherent
> is coherent.

```lean
theorem isCoherent_X₂_of_shortExact {S : ShortComplex (SheafOfModules.{u} R)} (hS : S.ShortExact)
    (h₁ : IsCoherent S.X₁) (h₃ : IsCoherent S.X₃) : IsCoherent S.X₂
```

**`Stacks.SheafOfModules.isCoherent_X₃_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/CoherentWeakSerre.lean, line 623](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/CoherentWeakSerre.lean#L623). The attribute's comment: “(3), cokernels”. References: EGA 0 (5.3.3), “Quotient clause”.

> The third term of a short exact sequence of sheaves of modules whose first two terms are
> coherent is coherent.

```lean
theorem isCoherent_X₃_of_shortExact {S : ShortComplex (SheafOfModules.{u} R)} (hS : S.ShortExact)
    (h₁ : IsCoherent S.X₁) (h₂ : IsCoherent S.X₂) : IsCoherent S.X₃
```

**`Stacks.SheafOfModules.coherentModules_isWeakSerreClass`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/CoherentWeakSerre.lean, line 684](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/CoherentWeakSerre.lean#L684). The attribute's comment: “coherent\_weak\_serre”.

> On a ringed space, the coherent sheaves of modules form a weak Serre subcategory of the
> category of all sheaves of modules: they contain the zero object, are closed under isomorphisms,
> and are closed under kernels, cokernels and extensions.

```lean
instance coherentModules_isWeakSerreClass :
    ObjectProperty.IsWeakSerreClass (fun M : SheafOfModules.{u} R => IsCoherent M)
```

**`Stacks.SheafOfModules.coherentModules_inclusion_preservesFiniteLimits`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/CoherentInclusionExact.lean, line 40](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/CoherentInclusionExact.lean#L40). The attribute's comment: “coherent\_inclusion\_exact”.

> The inclusion of coherent modules preserves finite limits.

```lean
instance coherentModules_inclusion_preservesFiniteLimits
    {X : Type u} [TopologicalSpace X]
    (R : Sheaf (Opens.grothendieckTopology X) RingCat.{u}) :
    PreservesFiniteLimits (ObjectProperty.ι (coherentModules R))
```

**`Stacks.SheafOfModules.coherentModules_inclusion_preservesFiniteColimits`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/CoherentInclusionExact.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/CoherentInclusionExact.lean#L48). The attribute's comment: “coherent\_inclusion\_exact”.

> The inclusion of coherent modules preserves finite colimits.

```lean
instance coherentModules_inclusion_preservesFiniteColimits
    {X : Type u} [TopologicalSpace X]
    (R : Sheaf (Opens.grothendieckTopology X) RingCat.{u}) :
    PreservesFiniteColimits (ObjectProperty.ι (coherentModules R))
```

**`SheafOfModules.kernel_isCoherent`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/KernelCokernel.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/KernelCokernel.lean#L57). The attribute's comment: “kernel\_coherent”. References: EGA 0 (5.3.4), “Ker(u) coherent”.

> A kernel of a morphism of coherent sheaves of modules is coherent.

```lean
instance kernel_isCoherent {F G : SheafOfModules.{u} R} [F.IsCoherent] [G.IsCoherent]
    (f : F ⟶ G) : (kernel f).IsCoherent
```

**`SheafOfModules.cokernel_isCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/KernelCokernel.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/KernelCokernel.lean#L65). The attribute's comment: “cokernel\_coherent”. References: EGA 0 (5.3.4), “Coker(u) coherent”.

> The cokernel of a morphism of coherent sheaves of modules is coherent.

```lean
theorem cokernel_isCoherent {F G : SheafOfModules.{u} R} [F.IsCoherent] [G.IsCoherent]
    (f : F ⟶ G) : (cokernel f).IsCoherent
```

## Tag 01BZ, a lemma

[Tag 01BZ](https://stacks.math.columbia.edu/tag/01BZ) in the Stacks Project.

**`Stacks.SheafOfModules.isCoherent_iff_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/CoherentIffFinitePresentation.lean, line 291](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/CoherentIffFinitePresentation.lean#L291).

> **Stacks 01BZ.** Over a ringed space whose structure sheaf is coherent as a module over
> itself, a sheaf of modules is coherent if and only if it is of finite presentation.

```lean
theorem isCoherent_iff_isFinitePresentation
    (R : Sheaf (Opens.grothendieckTopology X) RingCat.{u}) (M : SheafOfModules.{u} R)
    [IsCoherent (unit R)] : IsCoherent M ↔ M.IsFinitePresentation
```

## Tag 01C0, a lemma

[Tag 01C0](https://stacks.math.columbia.edu/tag/01C0) in the Stacks Project.

**`AlgebraicGeometry.exists_isMono_over_of_stalk_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/LocalIsomorphism.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/LocalIsomorphism.lean#L136).

> **Stacks Project, Tag 01Y3.** A morphism from a module of finite type to a coherent module
> which is injective on one stalk is a monomorphism after restriction to a neighbourhood of that
> point.

```lean
public theorem exists_isMono_over_of_stalk_injective {G F : SheafOfModules.{u} R}
    (φ : G ⟶ F) [G.IsFiniteType] [_root_.SheafOfModules.IsCoherent F] (x : X)
    (hx : Function.Injective
      (ConcreteCategory.hom ((TopCat.Presheaf.stalkFunctor AddCommGrpCat.{u} x).map
        ((PresheafOfModules.toPresheaf R.obj).map φ.val)))) :
    ∃ U : Opens X, x ∈ U ∧ Mono (φ.over U)
```

**`Stacks.AlgebraicGeometry.Tag01Y3LocalIso.exists_isMono_over_of_stalk_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalIso/Basic.lean, line 277](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalIso/Basic.lean#L277).

> **[Stacks, Tag 01C0]**, which is also part (2) of [Stacks, Tag 01Y3]. A morphism from a
> finite-type module sheaf to a coherent module sheaf which is injective on one stalk is injective
> after restriction to a neighbourhood of that point.

```lean
theorem exists_isMono_over_of_stalk_injective {F G : SheafOfModules.{u} R}
    [G.IsFiniteType] [F.IsCoherent] (φ : G ⟶ F) (x : X)
    (hx : Function.Injective
      (ConcreteCategory.hom ((TopCat.Presheaf.stalkFunctor AddCommGrpCat.{u} x).map
        ((PresheafOfModules.toPresheaf R.obj).map φ.val)))) :
    ∃ U : Opens X, x ∈ U ∧ Mono (φ.over U)
```

**`Stacks.SheafOfModules.exists_isMono_over_of_stalk_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/Generators/CoherentMonoNeighbourhood.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/Generators/CoherentMonoNeighbourhood.lean#L187).

> **Stacks Project, Tag 01C0.** A morphism from a finite-type sheaf of modules to a coherent
> sheaf of modules which is injective on one stalk is injective after restriction to a
> neighbourhood of that point.

```lean
theorem exists_isMono_over_of_stalk_injective
    (φ : G ⟶ F) [G.IsFiniteType] [F.IsCoherent] (x : X)
    (hx : Function.Injective
      (ConcreteCategory.hom ((TopCat.Presheaf.stalkFunctor AddCommGrpCat.{u} x).map
        ((PresheafOfModules.toPresheaf R.obj).map φ.val)))) :
    ∃ U : Opens X, x ∈ U ∧ Mono (φ.over U)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 17.12, Tag 01BU](https://stacks.math.columbia.edu/tag/01BU)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
