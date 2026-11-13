---
declaration: section
origin: cited
lean: Stacks.SheafOfModules.annihilatorSheaf, Stacks.SheafOfModules.stalk_annihilatorSheaf_le_annihilator_stalk, Stacks.SheafOfModules.annihilatorSheaf_stalk, Stacks.SheafOfModules.quotientRingSheafModule, Stacks.SheafOfModules.quotientRingSheafModule_restrictScalars, Stacks.SheafOfModules.quotientRingSheafModule_unique, Stacks.SheafOfModules.quotientRingSheafModule_stalk_smul, Stacks.SheafOfModules.isCoherent_annihilatorSheaf
statement: formalized
proof: formalized
---

# 17.23 The annihilator of a sheaf of modules

Section 17.23 of the Stacks Project, [Tag 0H2G](https://stacks.math.columbia.edu/tag/0H2G). 5 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0H2H, a definition

[Tag 0H2H](https://stacks.math.columbia.edu/tag/0H2H) in the Stacks Project.

**`Stacks.SheafOfModules.annihilatorSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/InvertibleAndOperators/Annihilator.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/InvertibleAndOperators/Annihilator.lean#L125). References: EGA 0 (5.3.7), “annihilator def”.

> **Stacks Project, Tag 0H2H.** The annihilator of an `𝒪_X`-module `F` is the
> subsheaf of `𝒪_X` consisting of the local functions that act as zero on `F`.  Equivalently,
> it is the kernel of the canonical map from `𝒪_X` to the internal endomorphism sheaf of
> `F`.

```lean
noncomputable def annihilatorSheaf :
    (SheafOfModules.unit (structureSheafRing X)).Submodule
```

## Tag 0H2I, an equation

[Tag 0H2I](https://stacks.math.columbia.edu/tag/0H2I) in the Stacks Project.

**`Stacks.SheafOfModules.stalk_annihilatorSheaf_le_annihilator_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/InvertibleAndOperators/Annihilator.lean, line 257](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/InvertibleAndOperators/Annihilator.lean#L257).

> **Stacks Project, Tag 0H2I.** The germs of local sections of the annihilator
> sheaf at `x` annihilate the stalk `Fₓ`.

```lean
theorem stalk_annihilatorSheaf_le_annihilator_stalk (x : X) :
    { a : (show X.carrier.Presheaf RingCat from (structureSheafRing X).obj).stalk x |
      ∃ (U : Opens X.carrier) (hx : x ∈ U) (r : (structureSheafRing X).obj.obj (op U)),
        r ∈ (annihilatorSheaf X F).toSubmodule.obj (op U) ∧
          (show X.carrier.Presheaf RingCat from (structureSheafRing X).obj).germ U x hx r = a } ⊆
      Module.annihilator
        ((show X.carrier.Presheaf RingCat from (structureSheafRing X).obj).stalk x)
        ((show X.carrier.Presheaf Ab.{u} from F.val.presheaf).stalk x)
```

## Tag 0H2J, a lemma

[Tag 0H2J](https://stacks.math.columbia.edu/tag/0H2J) in the Stacks Project.

**`Stacks.SheafOfModules.annihilatorSheaf_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/InvertibleAndOperators/AnnihilatorStalk.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/InvertibleAndOperators/AnnihilatorStalk.lean#L189).

> **Stacks Project, Tag 0H2J.** For `F` of finite type, the germs at `x` of the local sections
> of the annihilator sheaf of `F` are exactly the elements of the local ring `O_{X,x}` that
> annihilate the stalk `F_x`.

```lean
theorem annihilatorSheaf_stalk [F.IsFiniteType] (x : X) :
    {r : TopCat.Presheaf.stalk (C := CommRingCat.{u}) X.sheaf.obj x |
      ∃ (U : Opens X) (hx : x ∈ U) (s : (structureSheafRing X).obj.obj (op U)),
        s ∈ (annihilatorSheaf X F).toSubmodule.obj (op U) ∧
          TopCat.Presheaf.germ (C := CommRingCat.{u}) X.sheaf.obj U x hx s = r} =
      (Module.annihilator
        (TopCat.Presheaf.stalk (C := CommRingCat.{u}) X.sheaf.obj x)
        (TopCat.Presheaf.stalk (C := Ab.{u})
          (show PresheafOfModules.{u}
              (X.sheaf.obj ⋙ forget₂ CommRingCat RingCat) from F.val).presheaf x) :
          Set (TopCat.Presheaf.stalk (C := CommRingCat.{u}) X.sheaf.obj x))
```

## Tag 0H2K, a lemma

[Tag 0H2K](https://stacks.math.columbia.edu/tag/0H2K) in the Stacks Project.

**`Stacks.SheafOfModules.quotientRingSheafModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/InvertibleAndOperators/AnnihilatorQuotient.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/InvertibleAndOperators/AnnihilatorQuotient.lean#L184). The attribute's comment: “the descended module structure”.

> **Stacks Project, Tag 0H2K.** The canonical `𝒪_X/I`-module structure on a sheaf of modules
> annihilated by the ideal subsheaf `I`: its underlying presheaf of abelian groups is that of `F`,
> and a local section of `𝒪_X/I` acts through any local lift of it to `𝒪_X`.

```lean
noncomputable def quotientRingSheafModule (hI : I ≤ annihilatorSheaf X F) :
    SheafOfModules.{v} (quotientRingSheaf X I).sheaf
```

**`Stacks.SheafOfModules.quotientRingSheafModule_restrictScalars`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/InvertibleAndOperators/AnnihilatorQuotient.lean, line 236](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/InvertibleAndOperators/AnnihilatorQuotient.lean#L236). The attribute's comment: “compatibility with the given action”.

> **Stacks Project, Tag 0H2K.** The descended action is compatible with the given one:
> restricting scalars along the quotient map returns `F`.

```lean
theorem quotientRingSheafModule_restrictScalars (hI : I ≤ annihilatorSheaf X F) :
    (SheafOfModules.restrictScalars (quotientRingSheaf X I).quotientMap).obj
      (quotientRingSheafModule X I F hI) = F
```

**`Stacks.SheafOfModules.quotientRingSheafModule_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/InvertibleAndOperators/AnnihilatorQuotient.lean, line 251](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/InvertibleAndOperators/AnnihilatorQuotient.lean#L251). The attribute's comment: “uniqueness of the descended action”.

> **Stacks Project, Tag 0H2K.** The descended action is the only `𝒪_X/I`-action whose
> restriction of scalars along the quotient map is the given `𝒪_X`-action.

```lean
theorem quotientRingSheafModule_unique (hI : I ≤ annihilatorSheaf X F)
    (G : SheafOfModules.{v} (quotientRingSheaf X I).sheaf)
    (hG : (SheafOfModules.restrictScalars (quotientRingSheaf X I).quotientMap).obj G = F) :
    G = quotientRingSheafModule X I F hI
```

**`Stacks.SheafOfModules.quotientRingSheafModule_stalk_smul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/InvertibleAndOperators/AnnihilatorQuotient.lean, line 393](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/InvertibleAndOperators/AnnihilatorQuotient.lean#L393). The attribute's comment: “the action on stalks”.

> **Stacks Project, Tag 0H2K.** On stalks the descended action is the ordinary action of the
> quotient ring `𝒪_{X,x}/I_x` on the stalk `F_x`, which the stalk of `I` annihilates: the class of a
> germ `r` acts on `F_x` exactly as `r` itself.

```lean
theorem quotientRingSheafModule_stalk_smul (F : SheafOfModules.{u} (structureSheafRing X))
    (hI : I ≤ annihilatorSheaf X F) (x : X.carrier)
    (r : TopCat.Presheaf.stalk (C := RingCat) (structureSheafRing X).obj x)
    (m : TopCat.Presheaf.stalk (C := Ab.{u}) F.val.presheaf x) :
    quotientStalkSMul X I F hI x
        (quotientRingSheafStalkIdealEquiv X I x
          (Ideal.Quotient.mk (idealSheafStalk X I x) r)) m = r • m
```

## Tag 0H2L, a lemma

[Tag 0H2L](https://stacks.math.columbia.edu/tag/0H2L) in the Stacks Project.

**`Stacks.SheafOfModules.isCoherent_annihilatorSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/InvertibleAndOperators/AnnihilatorCoherent.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/InvertibleAndOperators/AnnihilatorCoherent.lean#L75).

> **Stacks Project, Tag 0H2L.** If the structure sheaf of a ringed space and an `𝒪_X`-module
> `F` are coherent, then the annihilator of `F` is coherent.

```lean
theorem isCoherent_annihilatorSheaf (F : SheafOfModules.{u} (structureSheafRing X))
    [IsCoherent (SheafOfModules.unit (structureSheafRing X))] [IsCoherent F] :
    IsCoherent (annihilatorSheaf X F).toSheafOfModules
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 17.23, Tag 0H2G](https://stacks.math.columbia.edu/tag/0H2G)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
