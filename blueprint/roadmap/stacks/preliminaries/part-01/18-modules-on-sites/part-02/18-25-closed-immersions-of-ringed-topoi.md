---
declaration: section
origin: cited
lean: AlgebraicGeometry.ClosedRingedImmersion.pushforwardModules_exact, Stacks.Sheaves.PushforwardEssentialImage.essImage_pushforwardModules_iff_of_isClosedImmersion, AlgebraicGeometry.ClosedRingedImmersion.pushforwardModules_fullyFaithful, Stacks.ToposBridge.essImage_schemeModulesPushforward_iff
statement: formalized
proof: formalized
---

# 18.25 Closed immersions of ringed topoi

Section 18.25 of the Stacks Project, [Tag 08M2](https://stacks.math.columbia.edu/tag/08M2). 1 tag here is carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08M3, a lemma

[Tag 08M3](https://stacks.math.columbia.edu/tag/08M3) in the Stacks Project.

**`AlgebraicGeometry.ClosedRingedImmersion.pushforwardModules_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PushforwardEssentialImageDirect/Exactness.lean, line 263](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PushforwardEssentialImageDirect/Exactness.lean#L263). The attribute's comment: “exactness”. References: SGA 4 IV (13.6), “special case”.

> **Stacks Project, Tag 08M3.** The direct image of sheaves of modules along a closed immersion
> of ringed topoi with locally surjective structure map is exact.
>
> Left exactness: the underlying sheaf of sets of the direct image is the direct image of the
> underlying sheaf of sets, the latter preserves finite limits because it is a right adjoint, and
> the underlying-sheaf functor on sheaves of modules preserves and reflects them. Right exactness:
> the direct image is fully faithful with essential image the modules annihilated by the kernel
> ideal, hence a left adjoint, hence preserves all colimits.

```lean
theorem ClosedRingedImmersion.pushforwardModules_exact
    (S : ClosedRingedImmersion.{v, u, v', u', w}) :
    exactFunctor (_root_.SheafOfModules.{w} S.sourceRingSheaf)
      (_root_.SheafOfModules.{w} S.targetRingSheaf) S.hom.pushforwardModules
```

**`Stacks.Sheaves.PushforwardEssentialImage.essImage_pushforwardModules_iff_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PushforwardEssentialSurjectivity.lean, line 408](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PushforwardEssentialSurjectivity.lean#L408). The attribute's comment: “essential\_image”.

> **Stacks 08M3, the essential-image statement.** Let `i : (Sh(C), O) → (Sh(D), O')` be a
> morphism of ringed topoi whose underlying morphism of topoi is a closed immersion and whose
> structure map `i^# : O' ⟶ i_*O` is locally surjective, and let `I ⊆ O'` be the sectionwise kernel
> of `i^#`. Then a sheaf of `O'`-modules is in the essential image of the direct image
> `i_* : Mod(O) ⥤ Mod(O')` exactly when `I` annihilates it.
>
> The forward implication needs neither hypothesis on `i`
> (`smul_eq_zero_of_essImage_pushforwardModules`); the reverse one spends local surjectivity in
> `Stacks.SheafOfModules.ChangeOfRings.essImage_restrictScalars_of_smul_eq_zero` and the
> closed-immersion hypothesis in `essSurj_pushforwardModuleFunctor`.

```lean
theorem essImage_pushforwardModules_iff_of_isClosedImmersion
    (hfc : MorphismOfTopoi.IsClosedImmersion f) {O' : Sheaf K RingCat.{w}}
    (fSharp : O' ⟶ pushforwardRingSheaf f O) [Sheaf.IsLocallySurjective fSharp]
    (G : SheafOfModules.{w} O') :
    (pushforwardModules f O fSharp).essImage G ↔
      ∀ (X : Dᵒᵖ) (a : O'.obj.obj X), a ∈ RingHom.ker (fSharp.hom.app X).hom →
        ∀ m : G.val.obj X, a • m = 0
```

**`AlgebraicGeometry.ClosedRingedImmersion.pushforwardModules_fullyFaithful`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PushforwardFullyFaithful/Basic.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PushforwardFullyFaithful/Basic.lean#L152). The attribute's comment: “full\_faithfulness”.

> **Stacks 08M3.** The direct image of sheaves of modules along a closed immersion of ringed
> topoi with locally surjective structure map is fully faithful.
>
> The direct image is the Stacks 03D1 direct image followed by restriction of scalars along the
> structure map. The first factor is fully faithful because the direct image of sheaves of sets
> is, the underlying morphism of topoi being an embedding; the second is fully faithful by
> Stacks 0930, the structure map being locally surjective.

```lean
theorem pushforwardModules_fullyFaithful :
    Nonempty S.hom.pushforwardModules.FullyFaithful
```

**`Stacks.ToposBridge.essImage_schemeModulesPushforward_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ClosedImmersion/TopoiBridge/EssentialImage.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ClosedImmersion/TopoiBridge/EssentialImage.lean#L106). The attribute's comment: “essential\_image, for a closed immersion of schemes”.

> **The essential-image half of Stacks 08M3 for a closed immersion of schemes.** A sheaf of
> `𝒪_X`-modules lies in the essential image of pushforward along a closed immersion `i : Z ⟶ X`
> exactly when the sectionwise kernel of the structure map of `i` annihilates it.
>
> This is `Stacks.ToposBridge.essImage_pushforwardModules_iff_of_iso` at the morphism of topoi
> presented by `i`, whose closed-immersion and local-surjectivity hypotheses hold for a closed
> immersion of schemes, transported along `Stacks.ToposBridge.schemePushforwardModulesIso`.

```lean
theorem essImage_schemeModulesPushforward_iff {Z X : Scheme.{u}} (i : Z ⟶ X)
    [AlgebraicGeometry.IsClosedImmersion i] (G : X.Modules) :
    (Scheme.Modules.pushforward i).essImage G ↔
      ∀ (U : (Opens X.carrier)ᵒᵖ) (a : X.ringCatSheaf.obj.obj U),
        a ∈ RingHom.ker ((toposStructureRingMap i.toLRSHom.toShHom).hom.app U).hom →
          ∀ m : G.val.obj U, a • m = 0
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.25, Tag 08M2](https://stacks.math.columbia.edu/tag/08M2)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
