---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.FunctorialityQcoh.isQuasicoherent_iff_forall_isAffineOpen_exists_tilde, Stacks.AlgebraicGeometry.FunctorialityQcoh.isQuasicoherent_iff_forall_restrict, Stacks.AlgebraicGeometry.FunctorialityQcoh.isQuasicoherent_X₁_of_shortExact, Stacks.AlgebraicGeometry.FunctorialityQcoh.isQuasicoherent_X₃_of_shortExact, Stacks.AlgebraicGeometry.QuasicoherentColimits.isQuasicoherent_sigma, Stacks.AlgebraicGeometry.QuasicoherentColimits.isQuasicoherent_colimit, Stacks.AlgebraicGeometry.QcohLimits.isQuasicoherent_kernel, Stacks.AlgebraicGeometry.QuasicoherentColimits.isQuasicoherent_cokernel
statement: formalized
proof: formalized
---

# 26.24 Functoriality for quasi-coherent modules

Section 26.24 of the Stacks Project, [Tag 01LA](https://stacks.math.columbia.edu/tag/01LA). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier) and 16 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01LA, the section

[Tag 01LA](https://stacks.math.columbia.edu/tag/01LA) in the Stacks Project.

**`Stacks.AlgebraicGeometry.FunctorialityQcoh.isQuasicoherent_iff_forall_isAffineOpen_exists_tilde`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/FunctorialityQuasiCoherent/Enumeration.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/FunctorialityQuasiCoherent/Enumeration.lean#L117). The attribute's comment: “the section's item (1): a sheaf of modules is quasi-coherent exactly when its restriction to each affine open `U = Spec Γ(X, U)` is the sheaf associated to a `Γ(X, U)`-module”.

> **[Stacks, Tag 01LA], item (1).** A sheaf of `𝒪_X`-modules `F` is quasi-coherent if and
> only if the restriction of `F` to each affine open `U = Spec Γ(X, U)` is of the form `M^~` for
> some `Γ(X, U)`-module `M`.
>
> Forwards, the module is `Γ(F, U)` and the isomorphism is
> `Stacks.Modules.tildeIsoRestrictFromSpec`. Backwards, `M^~` is quasi-coherent, hence so is the
> restriction of `F` to `Spec Γ(X, U)`; transporting along `hU.isoSpec.hom ≫ hU.fromSpec = U.ι`
> makes the restriction of `F` to `U` quasi-coherent, and quasi-coherence is local on `X`.

```lean
theorem isQuasicoherent_iff_forall_isAffineOpen_exists_tilde (F : X.Modules) :
    F.IsQuasicoherent ↔
      ∀ (U : X.Opens) (hU : IsAffineOpen U),
        ∃ M : ModuleCat.{u} Γ(X, U),
          Nonempty (tilde (R := Γ(X, U)) M ≅ F.restrict hU.fromSpec)
```

**`Stacks.AlgebraicGeometry.FunctorialityQcoh.isQuasicoherent_iff_forall_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/FunctorialityQuasiCoherent/Enumeration.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/FunctorialityQuasiCoherent/Enumeration.lean#L145). The attribute's comment: “the section's item (2): a sheaf of modules is quasi-coherent exactly when its restriction to each member of an affine open covering is quasi-coherent”.

> **[Stacks, Tag 01LA], item (2).** A sheaf of `𝒪_X`-modules `F` is quasi-coherent if and
> only if the restriction of `F` to each of the members of an affine open covering of `X` is
> quasi-coherent.
>
> Forwards this is restriction along an open immersion, which preserves quasi-coherence;
> backwards it is `Stacks.Modules.isQuasicoherent_of_restrict`, the locality of
> quasi-coherence.

```lean
theorem isQuasicoherent_iff_forall_restrict {I : Type w} (F : X.Modules)
    (U : I → X.affineOpens) (hU : ⨆ i, (U i : X.Opens) = ⊤) :
    F.IsQuasicoherent ↔ ∀ i, (F.restrict (U i : X.Opens).ι).IsQuasicoherent
```

**`Stacks.AlgebraicGeometry.FunctorialityQcoh.isQuasicoherent_X₁_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/FunctorialityQuasiCoherent/Enumeration.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/FunctorialityQuasiCoherent/Enumeration.lean#L158). The attribute's comment: “the section's item (6), the kernel case on an arbitrary scheme: in a short exact sequence, if the last two terms are quasi-coherent then so is the first”.

> **[Stacks, Tag 01LA], item (6), the kernel case.** Let
> `0 ⟶ F₁ ⟶ F₂ ⟶ F₃ ⟶ 0` be a short exact sequence of `𝒪_X`-modules on an arbitrary scheme `X`.
> If `F₂` and `F₃` are quasi-coherent then so is `F₁`, being the kernel of `F₂ ⟶ F₃`.

```lean
theorem isQuasicoherent_X₁_of_shortExact (S : ShortComplex X.Modules)
    (hS : S.ShortExact) (h₂ : S.X₂.IsQuasicoherent) (h₃ : S.X₃.IsQuasicoherent) :
    S.X₁.IsQuasicoherent
```

**`Stacks.AlgebraicGeometry.FunctorialityQcoh.isQuasicoherent_X₃_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/FunctorialityQuasiCoherent/Enumeration.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/FunctorialityQuasiCoherent/Enumeration.lean#L170). The attribute's comment: “the section's item (6), the cokernel case on an arbitrary scheme: in a short exact sequence, if the first two terms are quasi-coherent then so is the last”.

> **[Stacks, Tag 01LA], item (6), the cokernel case.** Let
> `0 ⟶ F₁ ⟶ F₂ ⟶ F₃ ⟶ 0` be a short exact sequence of `𝒪_X`-modules on an arbitrary scheme `X`.
> If `F₁` and `F₂` are quasi-coherent then so is `F₃`, being the cokernel of `F₁ ⟶ F₂`.

```lean
theorem isQuasicoherent_X₃_of_shortExact (S : ShortComplex X.Modules)
    (hS : S.ShortExact) (h₁ : S.X₁.IsQuasicoherent) (h₂ : S.X₂.IsQuasicoherent) :
    S.X₃.IsQuasicoherent
```

Declarations registered for the tag:

- [`Stacks.AlgebraicGeometry.QuasicoherentColimits.isQuasicoherent_sigma`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineQcohPushforward/Colimits.lean#L170), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/FunctorialityQuasiCoherent/Enumeration.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/FunctorialityQuasiCoherent/Enumeration.lean#L184) (StacksFrontier): “the section's item (3): any direct sum of quasi-coherent modules is quasi-coherent”.
- [`Stacks.AlgebraicGeometry.QuasicoherentColimits.isQuasicoherent_colimit`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineQcohPushforward/Colimits.lean#L152), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/FunctorialityQuasiCoherent/Enumeration.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/FunctorialityQuasiCoherent/Enumeration.lean#L186) (StacksFrontier): “the section's item (4): any colimit of quasi-coherent modules is quasi-coherent”.
- [`Stacks.AlgebraicGeometry.QcohLimits.isQuasicoherent_kernel`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QcohLimits/Basic.lean#L53), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/FunctorialityQuasiCoherent/Enumeration.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/FunctorialityQuasiCoherent/Enumeration.lean#L188) (StacksFrontier): “the section's item (5) = Tag 01LB, the kernel half: the kernel of a morphism of quasi-coherent modules is quasi-coherent”.
- [`Stacks.AlgebraicGeometry.QuasicoherentColimits.isQuasicoherent_cokernel`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineQcohPushforward/Colimits.lean#L161), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/FunctorialityQuasiCoherent/Enumeration.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/FunctorialityQuasiCoherent/Enumeration.lean#L191) (StacksFrontier): “the section's item (5) = Tag 01LB, the cokernel half: the cokernel of a morphism of quasi-coherent modules is quasi-coherent”.
- [`Stacks.AlgebraicGeometry.QcohExtension.isQuasicoherent_X₂_of_shortExact`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QcohShortExact/QcohExtension.lean#L196), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/FunctorialityQuasiCoherent/Enumeration.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/FunctorialityQuasiCoherent/Enumeration.lean#L194) (StacksFrontier): “the section's item (6), the extension case on an arbitrary scheme: in a short exact sequence, if the two outer terms are quasi-coherent then so is the middle one”.
- [`Stacks.AlgebraicGeometry.AffineBaseChange.isQuasicoherent_pullback`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineBaseChange/Basic.lean#L160), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/FunctorialityQuasiCoherent/Enumeration.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/FunctorialityQuasiCoherent/Enumeration.lean#L197) (StacksFrontier): “the section's item (7): the pullback of a quasi-coherent module along a morphism of schemes is quasi-coherent”.
- [`AlgebraicGeometry.Scheme.Modules.isQuasicoherent_tensorObj`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Modules/TensorInvertible.lean#L55), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/FunctorialityQuasiCoherent/Enumeration.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/FunctorialityQuasiCoherent/Enumeration.lean#L200) (StacksFrontier): “the section's item (8): the tensor product of two quasi-coherent modules is quasi-coherent”.
- [`Stacks.SheafOfModules.isQuasicoherent_tensorAlgebraSheaf_of_isQuasicoherent`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorPowerPresentation.lean#L569), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/FunctorialityQuasiCoherent/Enumeration.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/FunctorialityQuasiCoherent/Enumeration.lean#L202) (StacksFrontier): “the section's item (9), the tensor algebra of a quasi-coherent module is quasi-coherent”.
- [`Stacks.SheafOfModules.isQuasicoherent_symmetricAlgebraSheaf_of_isQuasicoherent`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/QuasicoherentAlgebras.lean#L779), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/FunctorialityQuasiCoherent/Enumeration.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/FunctorialityQuasiCoherent/Enumeration.lean#L204) (StacksFrontier): “the section's item (9), the symmetric algebra of a quasi-coherent module is quasi-coherent”.
- [`Stacks.SheafOfModules.isQuasicoherent_exteriorAlgebraSheaf_of_isQuasicoherent`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/QuasicoherentAlgebras.lean#L788), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/FunctorialityQuasiCoherent/Enumeration.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/FunctorialityQuasiCoherent/Enumeration.lean#L207) (StacksFrontier): “the section's item (9), the exterior algebra of a quasi-coherent module is quasi-coherent”.
- [`Stacks.AlgebraicGeometry.InternalHomModules.isQuasicoherent_sheafHomModules`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Coherent/SheafHomQuasicoherent.lean#L231), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/FunctorialityQuasiCoherent/Enumeration.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/FunctorialityQuasiCoherent/Enumeration.lean#L210) (StacksFrontier): “the section's item (10): the internal hom from a module of finite presentation into a quasi-coherent module is quasi-coherent”.

## Tag 01LB, an item

[Tag 01LB](https://stacks.math.columbia.edu/tag/01LB) in the Stacks Project.

Declarations registered for the tag:

- [`Stacks.AlgebraicGeometry.QcohLimits.isQuasicoherent_kernel`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QcohLimits/Basic.lean#L53), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/QuasiCoherent/General.lean, line 22](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/QuasiCoherent/General.lean#L22) (StacksFrontier): “kernel”.
- [`Stacks.AlgebraicGeometry.QuasicoherentColimits.isQuasicoherent_cokernel`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineQcohPushforward/Colimits.lean#L161), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/QuasiCoherent/General.lean, line 23](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/QuasiCoherent/General.lean#L23) (StacksFrontier): “cokernel”.

## Tag 01LC, a lemma

[Tag 01LC](https://stacks.math.columbia.edu/tag/01LC) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RelativeMayerVietoris.pushforward_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeMayerVietoris/Qcoh.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeMayerVietoris/Qcoh.lean#L174).

> **[Stacks, Tag 01LC].** The direct image of a quasi-coherent module along a quasi-compact
> quasi-separated morphism of schemes is quasi-coherent.
>
> The statement is local on the target: over an affine open `V` of `S` the restriction of `f_* F` is
> the direct image along `f ∣_ V` of the restriction of `F` to `f ⁻¹ᵁ V`, and `f ∣_ V` is again
> quasi-compact and quasi-separated with affine target.

```lean
theorem pushforward_isQuasicoherent (f : X ⟶ S) [QuasiCompact f] [QuasiSeparated f]
    (F : X.Modules) [F.IsQuasicoherent] :
    ((Scheme.Modules.pushforward f).obj F).IsQuasicoherent
```

**`AlgebraicGeometry.pushforward_isQuasicoherent`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/FunctorialityQuasiCoherent/Basic/Pushforward.lean, line 899](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/FunctorialityQuasiCoherent/Basic/Pushforward.lean#L899). References: EGA III (1.4.10), “q = 0”.

> **Stacks Project, Tag 01LC.** Pushforward along a quasi-compact and
> quasi-separated morphism of schemes preserves quasi-coherence.

```lean
public instance pushforward_isQuasicoherent
    {X S : Scheme.{u}} (f : X ⟶ S) [QuasiCompact f] [QuasiSeparated f]
    (F : X.Modules) [F.IsQuasicoherent] :
    ((Scheme.Modules.pushforward f).obj F).IsQuasicoherent
```

## Tag 02V0, a lemma

[Tag 02V0](https://stacks.math.columbia.edu/tag/02V0) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.IsImmersion.comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsImmersion.comp#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L125) (StacksFrontier): “composition of immersions”. References: EGA I (4.1.6); EGA I (4.2.5); EGA I (4.5.5), “(i), special case”.
- [`AlgebraicGeometry.IsClosedImmersion.comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsClosedImmersion.comp#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L126) (StacksFrontier): “composition of closed immersions”. References: EGA I (10.14.5), “(i), ordinary schemes”; EGA I (4.1.6); EGA I (4.2.5); EGA I (4.5.5), “(i), special case”.
- [`AlgebraicGeometry.IsOpenImmersion.comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsOpenImmersion.comp#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L127) (StacksFrontier): “composition of open immersions”. References: EGA I (4.2.5); EGA I (4.5.5), “(i), special case”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 26.24, Tag 01LA](https://stacks.math.columbia.edu/tag/01LA)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
