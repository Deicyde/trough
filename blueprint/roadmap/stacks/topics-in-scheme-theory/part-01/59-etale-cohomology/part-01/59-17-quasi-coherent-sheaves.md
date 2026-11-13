---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.fpqcAssociatedPresheafOfModules, Stacks.EtaleCohomology.isSheaf_fpqcAssociatedPresheafOfModules, SheafOfModules.IsQuasicoherentOnSite, Stacks.SheafOfModules.isQuasicoherentOnSite_iff_of_isTerminal, Stacks.Sites.isSheaf_structurePresheaf_and_exists_iso_siteAssociatedModule
statement: formalized
proof: formalized
---

# 59.17 Quasi-coherent sheaves

Section 59.17 of the Stacks Project, [Tag 03OF](https://stacks.math.columbia.edu/tag/03OF). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03OG, a proposition

[Tag 03OG](https://stacks.math.columbia.edu/tag/03OG) in the Stacks Project.

**`Stacks.EtaleCohomology.fpqcAssociatedPresheafOfModules`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FpqcTopology/QuasicoherentFpqcSheaf.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FpqcTopology/QuasicoherentFpqcSheaf.lean#L111). The attribute's comment: “F^a is an O-module”.

> **Stacks Project, Tag 03OG**, first assertion.  The presheaf
> `Fᵃ : (f : T ⟶ S) ↦ Γ(T, f⁺ F)` attached to a quasi-coherent module `F` on `S` is a module over
> the structure presheaf `𝒪` of the big fpqc site of `S`: the sections of `f⁺ F` over `T` form a
> module over `Γ(T, 𝒪_T)`, and the restriction maps of `Fᵃ` are semilinear over those of `𝒪`.

```lean
public noncomputable def fpqcAssociatedPresheafOfModules :
    PresheafOfModules.{u} (fpqcStructurePresheaf S)
```

**`Stacks.EtaleCohomology.isSheaf_fpqcAssociatedPresheafOfModules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FpqcTopology/QuasicoherentFpqcSheaf.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FpqcTopology/QuasicoherentFpqcSheaf.lean#L140). The attribute's comment: “the sheaf condition for the fpqc topology”.

> **Stacks Project, Tag 03OG**, second assertion.  The presheaf
> `Fᵃ : (f : T ⟶ S) ↦ Γ(T, f⁺ F)` attached to a quasi-coherent module `F` on `S` satisfies the
> sheaf condition for the fpqc topology on the schemes over `S`.

```lean
public theorem isSheaf_fpqcAssociatedPresheafOfModules :
    Presheaf.IsSheaf (Scheme.fpqcTopology.{u}.over S)
      (fpqcAssociatedPresheafOfModules S F).presheaf
```

## Tag 03OH, a definition

[Tag 03OH](https://stacks.math.columbia.edu/tag/03OH) in the Stacks Project.

Declarations registered for the tag:

- [`SheafOfModules.IsQuasicoherentOnSite`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/QuasicoherentOnSite.lean#L99), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/QuasiCoherentSheaves/Basic.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/QuasiCoherentSheaves/Basic.lean#L53) (StacksFrontier).

## Tag 03OI, a remark

[Tag 03OI](https://stacks.math.columbia.edu/tag/03OI) in the Stacks Project.

**`Stacks.SheafOfModules.isQuasicoherentOnSite_iff_of_isTerminal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/QuasiCoherentSheaves/Basic.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/QuasiCoherentSheaves/Basic.lean#L64). The attribute's comment: “quasi\_coherent”.

> **Stacks 03OI.** On a site with a final object `S`, the defining condition of Stacks 03OH
> for quasi-coherence of a sheaf of modules need only be checked at `U = S`: the module is
> quasi-coherent if and only if some covering of `S` admits a global presentation of the module
> on each of its members.

```lean
theorem isQuasicoherentOnSite_iff_of_isTerminal (M : SheafOfModules.{m} R)
    {S : C} (hS : IsTerminal S) :
    M.IsQuasicoherentOnSite ↔
      ∃ (I : Type (max u v)) (V : I → C) (f : ∀ i, V i ⟶ S),
        Sieve.ofArrows V f ∈ J S ∧ ∀ i, (M.over (V i)).HasGlobalPresentation
```

## Tag 03OJ, a theorem

[Tag 03OJ](https://stacks.math.columbia.edu/tag/03OJ) in the Stacks Project.

**`Stacks.Sites.isSheaf_structurePresheaf_and_exists_iso_siteAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/AssociatedModuleQuasicoherentEssSurj.lean, line 615](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/AssociatedModuleQuasicoherentEssSurj.lean#L615). The attribute's comment: “both assertions: O is a sheaf and every quasi-coherent O-module is F^a for a quasi-coherent F on S. Corrected form, recorded in errata.md: the printed statement is false when the fibre products of the site along coverings are not fibre products of schemes (not\_isSheaf\_structurePresheaf\_counterexample); PreservesCoveringFibreProducts says they are, as on every site of schemes Stacks uses, all of which form fibre products in Sch/S. Condition (1) is fullness, faithfulness and essential smallness; the site axioms are Stacks 00VH”.

> Let a site of schemes over `S` be presented by a precoverage `K` on a category
> `C` and a functor `toOver : C ⥤ Over S`, satisfying the site axioms of Stacks 00VH (isomorphisms,
> composites and base changes of coverings are coverings, the base changes being fibre products in
> `C` along covering arrows) and the four conditions of the tag: (1) `toOver` is fully faithful and
> `C` is essentially small; (2) every Zariski covering of the underlying scheme of an object is
> refined by a covering of the site; (3) `S/S` is an object of the site; (4) every covering of the
> site is an fpqc covering of schemes.  Assume that the fibre products of the site along covering
> arrows are fibre products of schemes.  Then the presheaf `𝒪` is a sheaf, and every quasi-coherent
> `𝒪`-module `M` is isomorphic to `Fᵃ` for a quasi-coherent `𝒪_S`-module `F`.

```lean
public theorem isSheaf_structurePresheaf_and_exists_iso_siteAssociatedModule
    (hTerminal : ∃ T : C, Nonempty (toOver.obj T ≅ Over.mk (𝟙 S))) :
    ∃ hR : Presheaf.IsSheaf K.toGrothendieck (structurePresheaf S toOver),
      ∀ (M : SheafOfModules.{u} (siteStructureSheaf S toOver K.toGrothendieck hR)),
        M.IsQuasicoherentOnSite →
        ∃ (F : S.Modules) (_ : F.IsQuasicoherent),
          Nonempty (M ≅ siteAssociatedModule S F toOver K.toGrothendieck hR
            (isSheaf_associatedPresheaf_of_preservesCoveringFibreProducts K toOver hfpqc hpres
              F))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.17, Tag 03OF](https://stacks.math.columbia.edu/tag/03OF)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
