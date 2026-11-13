---
declaration: section
origin: cited
lean: Crystalline.GlobalCrystallineSituation.SmallSite.crysDeRhamNatSheafComplex, Crystalline.GlobalCrystallineSituation.SmallSite.crysFormsSheaf
statement: formalized
proof: formalized
---

# 60.14 The de Rham complex

Section 60.14 of the Stacks Project, [Tag 07J4](https://stacks.math.columbia.edu/tag/07J4). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07J4, the section

[Tag 07J4](https://stacks.math.columbia.edu/tag/07J4) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.SmallSite.crysDeRhamNatSheafComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/DeRhamComplexSheaf.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/DeRhamComplexSheaf.lean#L86). The attribute's comment: “the de Rham complex 𝒪\_\{X/S} → Ω¹\_\{X/S} → Ω²\_\{X/S} → ⋯ of abelian sheaves on Cris(X/S); its terms are the sheaves Ω^i\_\{X/S} = crysFormsSheaf S i (crysDeRhamNatSheafComplexXIso), its degree-zero term is 𝒪\_\{X/S} (crysDeRhamNatSheafComplexXZeroIso), and its differential is the unique map of sheaves extending the de Rham differential of local sections (toCrysFormsSheafULift\_comp\_crysDeRhamNatSheafDifferential, crysDeRhamNatSheafDifferential\_unique)”.

> **The de Rham complex `𝒪_{X/S} → Ω¹_{X/S} → Ω²_{X/S} → ⋯` of abelian sheaves on the small
> crystalline site `Cris(X/S)`**, at the coefficient universe `u + 1`: the termwise sheafification
> of the de Rham complex of abelian presheaves `crysDeRhamCochainComplex`, whose differentials are
> the de Rham differentials of [Stacks, Tag 07HY] built from the universal `S`-derivation `d_{X/S}`.
> Its degree-`i` term is the sheaf `Ω^i_{X/S} = ∧^i_{𝒪_{X/S}} Ω_{X/S}` (`crysFormsSheaf`), by
> `crysDeRhamNatSheafComplexXIso`, and its degree-zero term is `𝒪_{X/S}`, by
> `crysDeRhamNatSheafComplexXZeroIso`.

```lean
def crysDeRhamNatSheafComplex :
    CochainComplex (Sheaf (smallTopology S) AddCommGrpCat.{u + 1}) ℕ
```

**`Crystalline.GlobalCrystallineSituation.SmallSite.crysFormsSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/DifferentialFormsSheaf.lean, line 173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/DifferentialFormsSheaf.lean#L173). The attribute's comment: “Ω^j\_\{X/S} = ∧^j\_\{𝒪\_\{X/S}} Ω\_\{X/S}, the sheaf of 𝒪\_\{X/S}-modules on Cris(X/S): the sheafification of the sectionwise exterior power (Tag 01CG); toCrysFormsSheaf is the canonical map from the presheaf of forms, locally injective and locally surjective”.

> **The sheaf of `𝒪_{X/S}`-modules `Ω^j_{X/S}` on the small crystalline site**, the sheaf
> associated with the presheaf `Ω^j_{X/S} = ⋀^j Ω_{X/S}` (`toCrysFormsSheaf`), with its sections in
> `Type u`.  It is the shrinking of the sheafification `crysFormsSheafULift` taken at the module
> universe `u + 1`, whose sections are `u`-small (`small_crysFormsSheafULift_obj`).
>
> This is the sheaf `Ω^j_{X/S} = ∧^j_{𝒪_{X/S}} Ω_{X/S}` of [Stacks, Tag 07J4]: by [Stacks, Tag 01CG]
> the exterior power of a sheaf of modules is the sheafification of the sectionwise exterior power,
> and the sheaf `Ω_{X/S}` is the sheafification of the presheaf of crystalline differentials, whose
> sectionwise exterior power has the same sheafification.  The de Rham complex of sheaves built on
> it is `crysDeRhamNatSheafComplex` of `SmallSite/DeRhamComplexSheaf.lean`.

```lean
def crysFormsSheaf (j : ℕ) : SheafOfModules.{u} (structureSheaf S)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 60.14, Tag 07J4](https://stacks.math.columbia.edu/tag/07J4)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
