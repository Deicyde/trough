---
declaration: section
origin: cited
lean: Crystalline.GlobalCrystallineSituation.crysDifferentialForms, Crystalline.GlobalCrystallineSituation.crysDeRhamComplex, Crystalline.GlobalCrystallineSituation.SmallSite.crysDifferentialForms, Crystalline.GlobalCrystallineSituation.SmallSite.crysDeRhamDifferential
statement: formalized
proof: formalized
---

# 60.14 The de Rham complex

Section 60.14 of the Stacks Project, [Tag 07J4](https://stacks.math.columbia.edu/tag/07J4). 1 tag here is carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07J4, the section

[Tag 07J4](https://stacks.math.columbia.edu/tag/07J4) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.crysDifferentialForms`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/DeRhamComplex.lean, line 406](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/DeRhamComplex.lean#L406). The attribute's comment: “Ω^i\_\{X/S} = ∧^i Ω\_\{X/S}, on the big crystalline category CRIS(X/S)”.

> **The presheaf `Ω^i_{X/S}` of crystalline differential forms of degree `i` on the big
> crystalline category.**  Its sections over an object `(U, T, δ)` are the `i`-th exterior power
> over `Γ(T, 𝒪_T)` of the sections of `Ω_{X/S}` there, and its transition maps are the exterior
> powers of those of `Ω_{X/S}`.

```lean
abbrev crysDifferentialForms (i : ℕ) : PresheafOfModules.{u} (structureRingCatPresheaf S)
```

**`Crystalline.GlobalCrystallineSituation.crysDeRhamComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/DeRhamComplex.lean, line 739](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/DeRhamComplex.lean#L739). The attribute's comment: “the de Rham complex 𝒪\_\{X/S} → Ω¹ → Ω² → ⋯, on CRIS(X/S)”.

> **The canonical de Rham complex on the crystalline site**, the complex
> `𝒪_{X/S} → Ω¹_{X/S} → Ω²_{X/S} → ⋯` that the universal `S`-derivation `d_{X/S}` gives rise to.

```lean
def crysDeRhamComplex : CrysDeRhamComplex S
```

**`Crystalline.GlobalCrystallineSituation.SmallSite.crysDifferentialForms`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/DeRhamComplex.lean, line 785](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/DeRhamComplex.lean#L785). The attribute's comment: “Ω^i\_\{X/S} = ∧^i\_\{𝒪\_\{X/S}} Ω\_\{X/S} on the small crystalline site Cris(X/S)”.

> **The presheaf `Ω^i_{X/S}` of crystalline differential forms of degree `i` on the small
> crystalline site `Cris(X/S)`**, the `i`-th exterior power of `Ω_{X/S}` over `𝒪_{X/S}`.

```lean
abbrev crysDifferentialForms (i : ℕ) :
    PresheafOfModules.{u} (structurePresheaf S ⋙ forget₂ CommRingCat RingCat)
```

**`Crystalline.GlobalCrystallineSituation.SmallSite.crysDeRhamDifferential`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/DeRhamComplex.lean, line 876](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/DeRhamComplex.lean#L876). The attribute's comment: “the de Rham complex 𝒪\_\{X/S} → Ω¹ → Ω² → ⋯ on Cris(X/S)”.

> **The de Rham complex `𝒪_{X/S} → Ω¹_{X/S} → Ω²_{X/S} → ⋯` on the small crystalline site
> `Cris(X/S)`**: the differential of the canonical complex on `CRIS(X/S)` at an object of the full
> subcategory `Cris(X/S)`.

```lean
def crysDeRhamDifferential (i : ℕ) (A : CrystallineThickening S) :
    ⋀[crysFormRing S A]^i ((crysDifferentials S).obj (op A)) →+
      ⋀[crysFormRing S A]^(i + 1) ((crysDifferentials S).obj (op A))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 60.14, Tag 07J4](https://stacks.math.columbia.edu/tag/07J4)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
