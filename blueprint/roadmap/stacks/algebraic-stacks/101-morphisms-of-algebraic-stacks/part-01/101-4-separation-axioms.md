---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.IsDM, AlgebraicGeometry.Stack.AlgebraicStacks.IsQuasiDM, AlgebraicGeometry.Stack.AlgebraicStacks.IsSeparated, AlgebraicGeometry.Stack.AlgebraicStacks.IsQuasiSeparated, AlgebraicGeometry.Stack.AlgebraicStacks.IsAbsolutelyDM, AlgebraicGeometry.Stack.AlgebraicStacks.IsAbsolutelyQuasiDM, AlgebraicGeometry.Stack.AlgebraicStacks.IsAbsolutelySeparated, AlgebraicGeometry.Stack.AlgebraicStacks.IsAbsolutelyQuasiSeparated
statement: formalized
proof: formalized
---

# 101.4 Separation axioms

Section 101.4 of the Stacks Project, [Tag 04YV](https://stacks.math.columbia.edu/tag/04YV). 16 tags here are carried by 102 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04YW, a definition

[Tag 04YW](https://stacks.math.columbia.edu/tag/04YW) in the Stacks Project.

**`AlgebraicGeometry.Stack.IsDM`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordMorphism.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordMorphism.lean#L68). The attribute's comment: “dm”.

> **Stacks 04YW, the DM condition.** A 1-morphism of algebraic stacks over `S` is
> *Deligne–Mumford* when its relative diagonal is representable by algebraic spaces and
> unramified, the latter in the relative sense of Stacks 03YK: every algebraic space representing
> a base change of the diagonal along a scheme-valued point of `𝒳 ×_{f, 𝒴, f} 𝒳` has unramified
> structural morphism.

```lean
abbrev IsDM {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) : Prop
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.IsQuasiDM`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationAxioms.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationAxioms.lean#L119). The attribute's comment: “quasi\_dm”.

> **Stacks 04YW, quasi-DM.** A 1-morphism of algebraic stacks over `S` is *quasi-DM* when its
> relative diagonal `Δ_f : 𝒳 ⟶ 𝒳 ×_{f, 𝒴, f} 𝒳` is locally quasi-finite in the sense of Stacks
> 04XB.

```lean
abbrev IsQuasiDM (f : 𝒳 ⟶ 𝒴) : Prop
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.IsSeparated`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationAxioms.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationAxioms.lean#L126). The attribute's comment: “separated”.

> **Stacks 04YW, separated.** A 1-morphism of algebraic stacks over `S` is *separated* when its
> relative diagonal `Δ_f : 𝒳 ⟶ 𝒳 ×_{f, 𝒴, f} 𝒳` is proper in the sense of Stacks 04XB.

```lean
abbrev IsSeparated (f : 𝒳 ⟶ 𝒴) : Prop
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.IsQuasiSeparated`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationAxioms.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationAxioms.lean#L133). The attribute's comment: “quasi\_separated”.

> **Stacks 04YW, quasi-separated.** A 1-morphism of algebraic stacks over `S` is
> *quasi-separated* when its relative diagonal `Δ_f : 𝒳 ⟶ 𝒳 ×_{f, 𝒴, f} 𝒳` is quasi-compact and
> quasi-separated, both in the sense of Stacks 04XB.

```lean
abbrev IsQuasiSeparated (f : 𝒳 ⟶ 𝒴) : Prop
```

## Tag 050D, a definition

[Tag 050D](https://stacks.math.columbia.edu/tag/050D) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.IsAbsolutelyDM`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationAbsolute.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationAbsolute.lean#L88). The attribute's comment: “part (5): absolute DM”.

> **Stacks 050D, part (5).** An algebraic stack is *DM* when it is DM over the terminal
> scheme `Spec ℤ`.

```lean
noncomputable abbrev IsAbsolutelyDM (𝒳 : Stack.AlgebraicStacks.{u, w} B S hS) : Prop
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.IsAbsolutelyQuasiDM`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationAbsolute.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationAbsolute.lean#L94). The attribute's comment: “part (6): absolute quasi-DM”.

> **Stacks 050D, part (6).** An algebraic stack is *quasi-DM* when it is quasi-DM over the
> terminal scheme `Spec ℤ`.

```lean
noncomputable abbrev IsAbsolutelyQuasiDM (𝒳 : Stack.AlgebraicStacks.{u, w} B S hS) : Prop
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.IsAbsolutelySeparated`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationAbsolute.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationAbsolute.lean#L100). The attribute's comment: “part (7): absolute separatedness”.

> **Stacks 050D, part (7).** An algebraic stack is *separated* when it is separated over the
> terminal scheme `Spec ℤ`.

```lean
noncomputable abbrev IsAbsolutelySeparated (𝒳 : Stack.AlgebraicStacks.{u, w} B S hS) : Prop
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.IsAbsolutelyQuasiSeparated`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationAbsolute.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationAbsolute.lean#L106). The attribute's comment: “part (8): absolute quasi-separatedness”.

> **Stacks 050D, part (8).** An algebraic stack is *quasi-separated* when it is quasi-separated
> over the terminal scheme `Spec ℤ`.

```lean
noncomputable abbrev IsAbsolutelyQuasiSeparated (𝒳 : Stack.AlgebraicStacks.{u, w} B S hS) :
    Prop
```

**`AlgebraicGeometry.Stack.IsDMAbs`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationAbsolute.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationAbsolute.lean#L141). The attribute's comment: “part (5): DM”.

> **Stacks 050D, part (5).** An algebraic stack is *DM* when it is DM over `Spec(ℤ)`, viewed as
> an algebraic stack over `Spec(ℤ)` by **Stacks 04X6**.

```lean
noncomputable abbrev IsDMAbs (𝒳 : AlgebraicStacks.{u, w} B S hS) : Prop
```

**`AlgebraicGeometry.Stack.IsQuasiDMAbs`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationAbsolute.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationAbsolute.lean#L147). The attribute's comment: “part (6): quasi-DM”.

> **Stacks 050D, part (6).** An algebraic stack is *quasi-DM* when it is quasi-DM over
> `Spec(ℤ)`, viewed as an algebraic stack over `Spec(ℤ)` by **Stacks 04X6**.

```lean
noncomputable abbrev IsQuasiDMAbs (𝒳 : AlgebraicStacks.{u, w} B S hS) : Prop
```

**`AlgebraicGeometry.Stack.IsSeparatedAbs`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationAbsolute.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationAbsolute.lean#L153). The attribute's comment: “part (7): separated”.

> **Stacks 050D, part (7).** An algebraic stack is *separated* when it is separated over
> `Spec(ℤ)`, viewed as an algebraic stack over `Spec(ℤ)` by **Stacks 04X6**.

```lean
noncomputable abbrev IsSeparatedAbs (𝒳 : AlgebraicStacks.{u, w} B S hS) : Prop
```

**`AlgebraicGeometry.Stack.IsQuasiSeparatedAbs`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationAbsolute.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationAbsolute.lean#L159). The attribute's comment: “part (8): quasi-separated”.

> **Stacks 050D, part (8).** An algebraic stack is *quasi-separated* when it is quasi-separated
> over `Spec(ℤ)`, viewed as an algebraic stack over `Spec(ℤ)` by **Stacks 04X6**.

```lean
noncomputable abbrev IsQuasiSeparatedAbs (𝒳 : AlgebraicStacks.{u, w} B S hS) : Prop
```

**`AlgebraicGeometry.Stack.IsDMOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationAxioms.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationAxioms.lean#L177). The attribute's comment: “part (1): DM over the base”.

> **Stacks 050D, part (1).** An algebraic stack over `S` is *DM over `S`* when its structure
> morphism to the algebraic stack represented by `S` is DM in the sense of Stacks 04YW.

```lean
noncomputable abbrev IsDMOver (𝒳 : AlgebraicStacks.{u, w} B S hS) : Prop
```

**`AlgebraicGeometry.Stack.IsQuasiDMOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationAxioms.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationAxioms.lean#L184). The attribute's comment: “part (2): quasi-DM over the base”.

> **Stacks 050D, part (2).** An algebraic stack over `S` is *quasi-DM over `S`* when its
> structure morphism to the algebraic stack represented by `S` is quasi-DM in the sense of Stacks
> 04YW.

```lean
noncomputable abbrev IsQuasiDMOver (𝒳 : AlgebraicStacks.{u, w} B S hS) : Prop
```

**`AlgebraicGeometry.Stack.IsSeparatedOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationAxioms.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationAxioms.lean#L191). The attribute's comment: “part (3): separated over the base”.

> **Stacks 050D, part (3).** An algebraic stack over `S` is *separated over `S`* when its
> structure morphism to the algebraic stack represented by `S` is separated in the sense of Stacks
> 04YW.

```lean
noncomputable abbrev IsSeparatedOver (𝒳 : AlgebraicStacks.{u, w} B S hS) : Prop
```

**`AlgebraicGeometry.Stack.IsQuasiSeparatedOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationAxioms.lean, line 198](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationAxioms.lean#L198). The attribute's comment: “part (4): quasi-separated over the base”.

> **Stacks 050D, part (4).** An algebraic stack over `S` is *quasi-separated over `S`* when its
> structure morphism to the algebraic stack represented by `S` is quasi-separated in the sense of
> Stacks 04YW.

```lean
noncomputable abbrev IsQuasiSeparatedOver (𝒳 : AlgebraicStacks.{u, w} B S hS) : Prop
```

## Tag 050E, a lemma

[Tag 050E](https://stacks.math.columbia.edu/tag/050E) in the Stacks Project.

**`AlgebraicGeometry.Stack.isUnramified_relativeDiagonal_of_isRepresentableByAlgebraicSpaces`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeDiagonalUnramified.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RelativeDiagonalUnramified.lean#L169). The attribute's comment: “representable\_implies\_dm”.

> **Stacks 050E, part (3).** A 1-morphism of algebraic stacks which is representable by
> algebraic spaces is Deligne–Mumford: its relative diagonal is representable by algebraic spaces
> (Stacks 04XS, part (1)), a monomorphism by part (3) of Stacks 04YQ and locally of finite type by
> part (2) of that tag, so Stacks 05W6 makes it unramified — which is the Deligne–Mumford
> condition of Stacks 04YW.
>
> **No part key of Stacks 04YQ is claimed**: that tag's five parts are representability, local
> finite type, monomorphy, separatedness and local quasi-finiteness, and unramifiedness is none of
> them.

```lean
theorem isUnramified_relativeDiagonal_of_isRepresentableByAlgebraicSpaces : IsDM B S hS f
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiDMWithRepresentableDiagonal_of_isDM`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationOverBase.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationOverBase.lean#L131). The attribute's comment: “dm\_implies\_quasi\_dm”.

> **Stacks 050E.** A DM 1-morphism of algebraic stacks over `S` is quasi-DM.
>
> Both conditions quantify over the same represented base changes of the relative diagonal and
> differ only in the property tested of the resulting morphism of algebraic spaces, so the
> implication is Stacks 05W0 — an unramified morphism of algebraic spaces is locally quasi-finite —
> applied at each of them.

```lean
theorem isQuasiDMWithRepresentableDiagonal_of_isDM
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hf : Stack.IsDM B S hS f) : IsQuasiDMWithRepresentableDiagonal B S hS f
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiSeparated_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationTrivialImplications.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationTrivialImplications.lean#L102). The attribute's comment: “part (1): separated implies quasi-separated”.

> **Stacks 050E, part (1).** A separated 1-morphism of algebraic stacks over `S` is
> quasi-separated: its relative diagonal is proper, hence separated and of finite type, hence
> quasi-separated and quasi-compact.

```lean
theorem isQuasiSeparated_of_isSeparated {f : 𝒳 ⟶ 𝒴} (hf : IsSeparated B S hS f) :
    IsQuasiSeparated B S hS f
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiDM_of_isDM`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationTrivialImplications.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationTrivialImplications.lean#L111). The attribute's comment: “part (2): DM implies quasi-DM”.

> **Stacks 050E, part (2).** A Deligne–Mumford 1-morphism of algebraic stacks over `S` is
> quasi-DM: its relative diagonal is unramified, hence locally quasi-finite.

```lean
theorem isQuasiDM_of_isDM {f : 𝒳 ⟶ 𝒴} (hf : Stack.IsDM B S hS f) :
    IsQuasiDM B S hS f
```

## Tag 050F, a lemma

[Tag 050F](https://stacks.math.columbia.edu/tag/050F) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isDM_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationBaseChange.lean, line 214](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationBaseChange.lean#L214). The attribute's comment: “dm”.

> **Stacks 050F, DM.** The base change `q : 𝒳 ×_𝒴 𝒵 ⟶ 𝒵` of a Deligne–Mumford 1-morphism of
> algebraic stacks over `S` is Deligne–Mumford: its relative diagonal is representable by algebraic
> spaces (**Stacks 04XS**, part (1)) and unramified in the sense of Stacks 04XB, the latter because
> `Δ_q` is a base change of `Δ_f`.

```lean
theorem isDM_baseChange (hf : Stack.IsDM B S hS f) :
    Stack.IsDM B S hS (twoFibreProductSquare B S hS f g).snd
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiDM_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationBaseChange.lean, line 225](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationBaseChange.lean#L225). The attribute's comment: “quasi\_dm”.

> **Stacks 050F, quasi-DM.** The base change `q : 𝒳 ×_𝒴 𝒵 ⟶ 𝒵` of a quasi-DM 1-morphism of
> algebraic stacks over `S` is quasi-DM: `Δ_q` is a base change of `Δ_f`, which is locally
> quasi-finite in the sense of Stacks 04XB.

```lean
theorem isQuasiDM_baseChange (hf : IsQuasiDM B S hS f) :
    IsQuasiDM B S hS (twoFibreProductSquare B S hS f g).snd
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isSeparated_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationBaseChange.lean, line 234](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationBaseChange.lean#L234). The attribute's comment: “separated”.

> **Stacks 050F, separated.** The base change `q : 𝒳 ×_𝒴 𝒵 ⟶ 𝒵` of a separated 1-morphism of
> algebraic stacks over `S` is separated: `Δ_q` is a base change of `Δ_f`, which is proper in the
> sense of Stacks 04XB.

```lean
theorem isSeparated_baseChange (hf : IsSeparated B S hS f) :
    IsSeparated B S hS (twoFibreProductSquare B S hS f g).snd
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiSeparated_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationBaseChange.lean, line 243](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationBaseChange.lean#L243). The attribute's comment: “quasi\_separated”.

> **Stacks 050F, quasi-separated.** The base change `q : 𝒳 ×_𝒴 𝒵 ⟶ 𝒵` of a quasi-separated
> 1-morphism of algebraic stacks over `S` is quasi-separated: `Δ_q` is a base change of `Δ_f`,
> which is quasi-compact and quasi-separated in the sense of Stacks 04XB.

```lean
theorem isQuasiSeparated_baseChange (hf : IsQuasiSeparated B S hS f) :
    IsQuasiSeparated B S hS (twoFibreProductSquare B S hS f g).snd
```

## Tag 06TZ, a lemma

[Tag 06TZ](https://stacks.math.columbia.edu/tag/06TZ) in the Stacks Project.

**`AlgebraicGeometry.Stack.isDM_of_isDM_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationFppfDescent.lean, line 303](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationFppfDescent.lean#L303). The attribute's comment: “dm\_descent”.

> **Stacks 06TZ, the Deligne–Mumford case.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic
> stacks over `S` and let `g : 𝒴' ⟶ 𝒴` be surjective, flat and locally of finite presentation with
> `𝒴'` representable by an algebraic space. If the base change
> `f' : 𝒳 ×_{f, 𝒴, g} 𝒴' ⟶ 𝒴'` of `f` by `g` is Deligne–Mumford, so is `f`.
>
> By Stacks 04YR the relative diagonal `Δ_{f'}` is a base change of `Δ_f` along `r × r`, and
> unramifiedness in the relative sense of Stacks 03YK descends along `r × r` by Stacks 045D, whose
> local essential surjectivity hypothesis is
> `AlgebraicGeometry.Stack.localEssSurj_diagonalMapDiag`. The representability witness is
> Stacks 04XS part (1), which holds for every 1-morphism of algebraic stacks and so is not
> descended.

```lean
theorem isDM_of_isDM_baseChange (f : 𝒳 ⟶ 𝒴) (g : 𝒴' ⟶ 𝒴)
    (h𝒴' : IsRepresentableByAlgebraicSpace B S hS 𝒴'.val)
    (hgSurj : IsSurjective B S hS g)
    (hgFlat : AlgebraicStacks.IsFlat B S hS g)
    (hgLfp : AlgebraicStacks.IsLocallyOfFinitePresentation B S hS g)
    (hf' : IsDM B S hS (twoFibreProductSquareAlgebraicStacks B S hS f g).snd) :
    IsDM B S hS f
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiDM_of_isQuasiDM_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationFppfDescent.lean, line 332](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationFppfDescent.lean#L332). The attribute's comment: “quasi\_dm\_descent”.

> **Stacks 06TZ, the quasi-DM case.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over
> `S` and let `g : 𝒴' ⟶ 𝒴` be surjective, flat and locally of finite presentation with `𝒴'`
> representable by an algebraic space. If the base change `f' : 𝒳 ×_{f, 𝒴, g} 𝒴' ⟶ 𝒴'` of `f` by
> `g` is quasi-DM, so is `f`.
>
> The relative diagonal of the base change is a base change of `Δ_f` by Stacks 04YR, and local
> quasi-finiteness of the represented base changes descends by Stacks 045D.

```lean
theorem isQuasiDM_of_isQuasiDM_baseChange (f : 𝒳 ⟶ 𝒴) (g : 𝒴' ⟶ 𝒴)
    (h𝒴' : IsRepresentableByAlgebraicSpace B S hS 𝒴'.val)
    (hgSurj : IsSurjective B S hS g)
    (hgFlat : AlgebraicStacks.IsFlat B S hS g)
    (hgLfp : AlgebraicStacks.IsLocallyOfFinitePresentation B S hS g)
    (hf' : IsQuasiDM B S hS (twoFibreProductSquareAlgebraicStacks B S hS f g).snd) :
    IsQuasiDM B S hS f
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isSeparated_of_isSeparated_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationFppfDescent.lean, line 354](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationFppfDescent.lean#L354). The attribute's comment: “separated\_descent”.

> **Stacks 06TZ, the separated case.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over
> `S` and let `g : 𝒴' ⟶ 𝒴` be surjective, flat and locally of finite presentation with `𝒴'`
> representable by an algebraic space. If the base change `f' : 𝒳 ×_{f, 𝒴, g} 𝒴' ⟶ 𝒴'` of `f` by
> `g` is separated, so is `f`.
>
> The relative diagonal of the base change is a base change of `Δ_f` by Stacks 04YR, and properness
> of the represented base changes descends by Stacks 045D, whose target-locality hypothesis is the
> fppf form of Stacks 0422.

```lean
theorem isSeparated_of_isSeparated_baseChange (f : 𝒳 ⟶ 𝒴) (g : 𝒴' ⟶ 𝒴)
    (h𝒴' : IsRepresentableByAlgebraicSpace B S hS 𝒴'.val)
    (hgSurj : IsSurjective B S hS g)
    (hgFlat : AlgebraicStacks.IsFlat B S hS g)
    (hgLfp : AlgebraicStacks.IsLocallyOfFinitePresentation B S hS g)
    (hf' : IsSeparated B S hS (twoFibreProductSquareAlgebraicStacks B S hS f g).snd) :
    IsSeparated B S hS f
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiSeparated_of_isQuasiSeparated_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationFppfDescent.lean, line 382](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationFppfDescent.lean#L382). The attribute's comment: “quasi\_separated\_descent”.

> **Stacks 06TZ, the quasi-separated case.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic
> stacks over `S` and let `g : 𝒴' ⟶ 𝒴` be surjective, flat and locally of finite presentation with
> `𝒴'` representable by an algebraic space. If the base change `f' : 𝒳 ×_{f, 𝒴, g} 𝒴' ⟶ 𝒴'` of `f`
> by `g` is quasi-separated, so is `f`.
>
> The relative diagonal of the base change is a base change of `Δ_f` by Stacks 04YR, and the
> conjunction of quasi-compactness and quasi-separatedness of the represented base changes descends
> by Stacks 045D — applied at the *conjunction*, read as a property of morphisms of algebraic
> spaces, exactly as the definition of quasi-separatedness is, with both of that conjunction's
> hypotheses formed as meets.

```lean
theorem isQuasiSeparated_of_isQuasiSeparated_baseChange (f : 𝒳 ⟶ 𝒴) (g : 𝒴' ⟶ 𝒴)
    (h𝒴' : IsRepresentableByAlgebraicSpace B S hS 𝒴'.val)
    (hgSurj : IsSurjective B S hS g)
    (hgFlat : AlgebraicStacks.IsFlat B S hS g)
    (hgLfp : AlgebraicStacks.IsLocallyOfFinitePresentation B S hS g)
    (hf' : IsQuasiSeparated B S hS (twoFibreProductSquareAlgebraicStacks B S hS f g).snd) :
    IsQuasiSeparated B S hS f
```

## Tag 050G, a lemma

[Tag 050G](https://stacks.math.columbia.edu/tag/050G) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiDMOver_changeOfBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationChangeOfBase.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationChangeOfBase.lean#L142). The attribute's comment: “quasi-DM over the base”.

> **Stacks 050G, the quasi-DM key.** Being quasi-DM over the base is stable under change of
> base scheme.

```lean
theorem isQuasiDMOver_changeOfBase (𝒳' : AlgebraicStacks.{u, w} B S' hS')
    (h𝒳' : Stack.IsQuasiDMOver B S' hS' 𝒳') :
    Stack.IsQuasiDMOver B S hS (Stack.changeOfBase B S S' hS hS' g 𝒳')
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiSeparatedOver_changeOfBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationChangeOfBase.lean, line 165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationChangeOfBase.lean#L165). The attribute's comment: “quasi-separated over the base”.

> **Stacks 050G, the quasi-separated key.** Being quasi-separated over the base is stable under
> change of base scheme.

```lean
theorem isQuasiSeparatedOver_changeOfBase (𝒳' : AlgebraicStacks.{u, w} B S' hS')
    (h𝒳' : Stack.IsQuasiSeparatedOver B S' hS' 𝒳') :
    Stack.IsQuasiSeparatedOver B S hS (Stack.changeOfBase B S S' hS hS' g 𝒳')
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isSeparatedOver_changeOfBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationChangeOfBase.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationChangeOfBase.lean#L192). The attribute's comment: “separated over the base”.

> **Stacks 050G, the separated key.** Being separated over the base is stable under change of
> base scheme.

```lean
theorem isSeparatedOver_changeOfBase (𝒳' : AlgebraicStacks.{u, w} B S' hS')
    (h𝒳' : Stack.IsSeparatedOver B S' hS' 𝒳') :
    Stack.IsSeparatedOver B S hS (Stack.changeOfBase B S S' hS hS' g 𝒳')
```

## Tag 050H, a lemma

[Tag 050H](https://stacks.math.columbia.edu/tag/050H) in the Stacks Project.

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FibreProductComparison.lean, line 215](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FibreProductComparison.lean#L215). The attribute's comment: “part (1): representable by algebraic spaces”.

> The comparison 1-morphism `i : 𝒳 ×_𝒵 𝒴 ⟶ 𝒳 ×_𝒯 𝒴` is representable by algebraic spaces.

```lean
theorem isRepresentableByAlgebraicSpaces_comparison
    (f : 𝒳 ⟶ 𝒵) (g : 𝒴 ⟶ 𝒵) (h : 𝒵 ⟶ 𝒯) :
    IsRepresentableByAlgebraicSpaces B S hS (comparison B S hS f g h).hom.hom
```

**`AlgebraicGeometry.Stack.isUnramified_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FibreProductComparison.lean, line 231](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FibreProductComparison.lean#L231). The attribute's comment: “dm\_unramified”.

> If `h : 𝒵 ⟶ 𝒯` is Deligne–Mumford then the comparison 1-morphism
> `i : 𝒳 ×_𝒵 𝒴 ⟶ 𝒳 ×_𝒯 𝒴` is unramified, in the sense of `HasRelativeProperty`. The statement
> supplies, as local instances, the stability of unramifiedness of morphisms of algebraic spaces
> under base change and its locality on the target for the fppf precoverage.

```lean
theorem isUnramified_comparison (f : 𝒳 ⟶ 𝒵) (g : 𝒴 ⟶ 𝒵) (h : 𝒵 ⟶ 𝒯)
    (hh : IsDM B S hS h) :
    letI : MorphismProperty.IsStableUnderBaseChange
      (fun ⦃X Y : AlgebraicSpaces B S hS⦄ (k : X ⟶ Y) =>
        Space.IsUnramified B S hS k.hom) :=
      Space.isUnramified_isStableUnderBaseChange B S hS
    letI : MorphismProperty.IsLocalAtTarget
      (fun ⦃X Y : AlgebraicSpaces B S hS⦄ (k : X ⟶ Y) =>
        Space.IsUnramified B S hS k.hom)
      (Space.Topology.fppf.precoverage.{u, u} B S hS) :=
      (Space.isUnramified_isLocalAtTarget_fpqc B S hS).of_le
        (Space.fppfPrecoverage_le_fpqcPrecoverage.{u, u} B S hS)
    HasRelativeProperty B S hS
      (fun _ _ k => Space.IsUnramified B S hS k.hom)
      (comparison B S hS f g h).hom
      (isRepresentableByAlgebraicSpaces_comparison B S hS f g h)
```

**`AlgebraicGeometry.Stack.isLocallyOfFiniteType_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FibreProductComparisonFiniteType.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FibreProductComparisonFiniteType.lean#L93). The attribute's comment: “part (1): locally of finite type”.

> **Stacks 050H, part (1), locally-of-finite-type half.** The comparison 1-morphism
> `i : 𝒳 ×_𝒵 𝒴 ⟶ 𝒳 ×_𝒯 𝒴` is locally of finite type, in the sense of Properties of Stacks,
> Section 04XB.
>
> By Stacks 04Z1 the comparison is the base change of the relative diagonal `Δ_{𝒵/𝒯}` along the
> right-hand leg of `AlgebraicGeometry.Stack.comparisonSquare`; that diagonal is locally of finite
> type by part (2) of Stacks 04XS, with no hypothesis on `h`, and Stacks 045C carries the property
> across. Together with `AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_comparison` this
> is the whole of part (1).

```lean
theorem isLocallyOfFiniteType_comparison (f : 𝒳 ⟶ 𝒵) (g : 𝒴 ⟶ 𝒵) (h : 𝒵 ⟶ 𝒯) :
    IsLocallyOfFiniteType B S hS (comparison B S hS f g h).hom
```

**`AlgebraicGeometry.Stack.isQuasiSeparated_comparison_of_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FibreProductComparisonSeparation.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FibreProductComparisonSeparation.lean#L100). The attribute's comment: “quasi\_separated\_diagonal”.

> If the relative diagonal `Δ_{𝒵/𝒯}` is quasi-separated, then so is the comparison 1-morphism
> `i : 𝒳 ×_𝒵 𝒴 ⟶ 𝒳 ×_𝒯 𝒴`, both in the sense of Properties of Stacks, Section 04XB.

```lean
theorem isQuasiSeparated_comparison_of_diagonal (f : 𝒳 ⟶ 𝒵) (g : 𝒴 ⟶ 𝒵) (h : 𝒵 ⟶ 𝒯)
    (hΔ : IsQuasiSeparated B S hS (relativeDiagonalAlgebraicStacks B S hS h).hom) :
    IsQuasiSeparated B S hS (comparison B S hS f g h).hom
```

**`AlgebraicGeometry.Stack.isSeparated_comparison_of_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FibreProductComparisonSeparation.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FibreProductComparisonSeparation.lean#L108). The attribute's comment: “separated\_diagonal”.

> If the relative diagonal `Δ_{𝒵/𝒯}` is separated, then so is the comparison 1-morphism
> `i : 𝒳 ×_𝒵 𝒴 ⟶ 𝒳 ×_𝒯 𝒴`, both in the sense of Properties of Stacks, Section 04XB.

```lean
theorem isSeparated_comparison_of_diagonal (f : 𝒳 ⟶ 𝒵) (g : 𝒴 ⟶ 𝒵) (h : 𝒵 ⟶ 𝒯)
    (hΔ : IsSeparated B S hS (relativeDiagonalAlgebraicStacks B S hS h).hom) :
    IsSeparated B S hS (comparison B S hS f g h).hom
```

**`AlgebraicGeometry.Stack.isLocallyQuasiFinite_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FibreProductComparisonSeparation.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FibreProductComparisonSeparation.lean#L116). The attribute's comment: “quasi\_dm\_lqf”.

> If `h : 𝒵 ⟶ 𝒯` is quasi-DM then the comparison 1-morphism `i : 𝒳 ×_𝒵 𝒴 ⟶ 𝒳 ×_𝒯 𝒴` is
> locally quasi-finite, in the sense of Properties of Stacks, Section 04XB.

```lean
theorem isLocallyQuasiFinite_comparison (f : 𝒳 ⟶ 𝒵) (g : 𝒴 ⟶ 𝒵) (h : 𝒵 ⟶ 𝒯)
    (hh : AlgebraicStacks.IsQuasiDM B S hS h) :
    IsLocallyQuasiFinite B S hS (comparison B S hS f g h).hom
```

**`AlgebraicGeometry.Stack.isProper_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FibreProductComparisonSeparation.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FibreProductComparisonSeparation.lean#L125). The attribute's comment: “separated\_proper”.

> If `h : 𝒵 ⟶ 𝒯` is separated then the comparison 1-morphism `i : 𝒳 ×_𝒵 𝒴 ⟶ 𝒳 ×_𝒯 𝒴` is
> proper, in the sense of Properties of Stacks, Section 04XB.

```lean
theorem isProper_comparison (f : 𝒳 ⟶ 𝒵) (g : 𝒴 ⟶ 𝒵) (h : 𝒵 ⟶ 𝒯)
    (hh : AlgebraicStacks.IsSeparated B S hS h) :
    IsProper B S hS (comparison B S hS f g h).hom
```

**`AlgebraicGeometry.Stack.isQuasiCompact_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FibreProductComparisonSeparation.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FibreProductComparisonSeparation.lean#L134). The attribute's comment: “part (7), the quasi-compactness half”.

> If `h : 𝒵 ⟶ 𝒯` is quasi-separated as a 1-morphism of algebraic stacks, then the comparison
> 1-morphism `i : 𝒳 ×_𝒵 𝒴 ⟶ 𝒳 ×_𝒯 𝒴` is quasi-compact, in the sense of Properties of Stacks,
> Section 04XB.

```lean
theorem isQuasiCompact_comparison (f : 𝒳 ⟶ 𝒵) (g : 𝒴 ⟶ 𝒵) (h : 𝒵 ⟶ 𝒯)
    (hh : AlgebraicStacks.IsQuasiSeparated B S hS h) :
    IsQuasiCompact B S hS (comparison B S hS f g h).hom
```

**`AlgebraicGeometry.Stack.isQuasiSeparated_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FibreProductComparisonSeparation.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FibreProductComparisonSeparation.lean#L146). The attribute's comment: “part (7), the quasi-separatedness half”.

> If `h : 𝒵 ⟶ 𝒯` is quasi-separated as a 1-morphism of algebraic stacks, then the comparison
> 1-morphism `i : 𝒳 ×_𝒵 𝒴 ⟶ 𝒳 ×_𝒯 𝒴` is quasi-separated, in the sense of Properties of Stacks,
> Section 04XB.

```lean
theorem isQuasiSeparated_comparison (f : 𝒳 ⟶ 𝒵) (g : 𝒴 ⟶ 𝒵) (h : 𝒵 ⟶ 𝒯)
    (hh : AlgebraicStacks.IsQuasiSeparated B S hS h) :
    IsQuasiSeparated B S hS (comparison B S hS f g h).hom
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiSeparated_mapBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationFibreProductProperties.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationFibreProductProperties.lean#L178). The attribute's comment: “part (2): quasi-separated”.

> **Stacks 050H, part (2).** If the relative diagonal `Δ_{𝒵/𝒯}` is quasi-separated in the sense
> of Stacks 04XB, then so is the comparison 1-morphism `i : 𝒳 ×_𝒵 𝒴 ⟶ 𝒳 ×_𝒯 𝒴`.

```lean
theorem isQuasiSeparated_mapBase
    (hΔ : Stack.IsQuasiSeparated.{u, u, u + 1} B S hS
      (relativeDiagonal.{u, u, u + 1} B S hS 𝒵.val 𝒯.val h.hom)) :
    Stack.IsQuasiSeparated.{u, u, u + 1} B S hS (mapBase B S hS f g h).hom
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isSeparated_mapBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationFibreProductProperties.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationFibreProductProperties.lean#L188). The attribute's comment: “part (3): separated”.

> **Stacks 050H, part (3).** If the relative diagonal `Δ_{𝒵/𝒯}` is separated in the sense of
> Stacks 04XB, then so is the comparison 1-morphism `i : 𝒳 ×_𝒵 𝒴 ⟶ 𝒳 ×_𝒯 𝒴`.

```lean
theorem isSeparated_mapBase
    (hΔ : Stack.IsSeparated.{u, u, u + 1} B S hS
      (relativeDiagonal.{u, u, u + 1} B S hS 𝒵.val 𝒯.val h.hom)) :
    Stack.IsSeparated.{u, u, u + 1} B S hS (mapBase B S hS f g h).hom
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isUnramified_mapBase_of_isDM`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationFibreProductProperties.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationFibreProductProperties.lean#L199). The attribute's comment: “part (4): unramified”.

> **Stacks 050H, part (4).** If `h : 𝒵 ⟶ 𝒯` is Deligne–Mumford, then the comparison 1-morphism
> `i : 𝒳 ×_𝒵 𝒴 ⟶ 𝒳 ×_𝒯 𝒴` is unramified in the sense of Stacks 04XB: `i` is a base change of
> `Δ_{𝒵/𝒯}`, which is unramified by the definition of Stacks 04YW.

```lean
theorem isUnramified_mapBase_of_isDM (hh : Stack.IsDM B S hS h) :
    ∀ (U : BigFppfOver B S hS)
      (z : BigFppfOver B U.left.1 U.left.2 ⥤
        (twoFibreProduct B S hS (f ≫ h) (g ≫ h)).val.val.obj)
      (_hz : z ⋙ (twoFibreProduct B S hS (f ≫ h) (g ≫ h)).val.val.p = Over.map U.hom)
      (F : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
      (hF : IsAlgebraicSpace B U.left.1 U.left.2 F),
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (TwoFibreProductOver.fst (Over.map U.hom)
            (twoFibreProduct B S hS f g).val.val.p
            (twoFibreProduct B S hS (f ≫ h) (g ≫ h)).val.val.p z
            (CatFiberedInGroupoids.homFunctor (mapBase B S hS f g h).hom))
          (presheafOfCategories (F ⋙ typeToCat)).p) →
        Space.IsUnramified B S hS
          (algebraicSpaceMap B S hS U
            ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨F, hF⟩)).hom
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyQuasiFinite_mapBase_of_isQuasiDM`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationFibreProductProperties.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationFibreProductProperties.lean#L221). The attribute's comment: “part (5): locally quasi-finite”.

> **Stacks 050H, part (5).** If `h : 𝒵 ⟶ 𝒯` is quasi-DM, then the comparison 1-morphism
> `i : 𝒳 ×_𝒵 𝒴 ⟶ 𝒳 ×_𝒯 𝒴` is locally quasi-finite in the sense of Stacks 04XB.

```lean
theorem isLocallyQuasiFinite_mapBase_of_isQuasiDM (hh : IsQuasiDM B S hS h) :
    Stack.IsLocallyQuasiFinite.{u, u, u + 1} B S hS (mapBase B S hS f g h).hom
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isProper_mapBase_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationFibreProductProperties.lean, line 229](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationFibreProductProperties.lean#L229). The attribute's comment: “part (6): proper”.

> **Stacks 050H, part (6).** If `h : 𝒵 ⟶ 𝒯` is separated, then the comparison 1-morphism
> `i : 𝒳 ×_𝒵 𝒴 ⟶ 𝒳 ×_𝒯 𝒴` is proper in the sense of Stacks 04XB.

```lean
theorem isProper_mapBase_of_isSeparated (hh : IsSeparated B S hS h) :
    Stack.IsProper.{u, u, u + 1} B S hS (mapBase B S hS f g h).hom
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiCompactAndQuasiSeparated_mapBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationFibreProductProperties.lean, line 237](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationFibreProductProperties.lean#L237). The attribute's comment: “part (7): quasi-compact and quasi-separated”.

> **Stacks 050H, part (7).** If `h : 𝒵 ⟶ 𝒯` is quasi-separated, then the comparison 1-morphism
> `i : 𝒳 ×_𝒵 𝒴 ⟶ 𝒳 ×_𝒯 𝒴` is quasi-compact and quasi-separated in the sense of Stacks 04XB.

```lean
theorem isQuasiCompactAndQuasiSeparated_mapBase
    (hh : IsQuasiSeparated B S hS h) :
    Stack.IsQuasiCompact.{u, u, u + 1} B S hS (mapBase B S hS f g h).hom ∧
      Stack.IsQuasiSeparated.{u, u, u + 1} B S hS (mapBase B S hS f g h).hom
```

## Tag 050I, a lemma

[Tag 050I](https://stacks.math.columbia.edu/tag/050I) in the Stacks Project.

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_graph`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GraphMorphism.lean, line 563](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/GraphMorphism.lean#L563). The attribute's comment: “part (1): representable by algebraic spaces”.

> **Stacks 050I, part (1), representability half.** The graph of a 1-morphism of algebraic
> stacks over a base algebraic stack is representable by algebraic spaces.
>
> The graph is 2-isomorphic to the comparison 1-morphism of Stacks 050H precomposed and
> postcomposed with equivalences, and representability by algebraic spaces is invariant under such
> a square by Stacks 0457.

```lean
theorem isRepresentableByAlgebraicSpaces_graph (g : 𝒳 ⟶ 𝒴) (p : 𝒳 ⟶ 𝒯) (q : 𝒴 ⟶ 𝒯)
    (η : p ≅ g ≫ q) :
    IsRepresentableByAlgebraicSpaces B S hS (graph B S hS g p q η).hom.hom
```

**`AlgebraicGeometry.Stack.isUnramified_graph`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GraphMorphism.lean, line 680](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/GraphMorphism.lean#L680). The attribute's comment: “part (2)”.

> **Stacks 050I, part (2).** If `q : 𝒴 ⟶ 𝒯` is Deligne–Mumford then the graph of `g : 𝒳 ⟶ 𝒴`
> over `𝒯` is unramified, in the relative sense of Stacks 03YK.
>
> By Stacks 050H part (4) the comparison 1-morphism `𝒳 ×_𝒴 𝒴 ⟶ 𝒳 ×_𝒯 𝒴` is unramified, and
> `AlgebraicGeometry.Stack.hasRelativeProperty_graph_of_comparison` carries that to the graph. The
> two instance arguments of Stacks 03YK are Stacks 03ZJ and Stacks 042A composed with the
> comparison of the fppf and fpqc precoverages.

```lean
theorem isUnramified_graph (g : 𝒳 ⟶ 𝒴) (p : 𝒳 ⟶ 𝒯) (q : 𝒴 ⟶ 𝒯) (η : p ≅ g ≫ q)
    (hq : IsDM B S hS q) :
    letI : MorphismProperty.IsStableUnderBaseChange
      (fun ⦃X Y : AlgebraicSpaces B S hS⦄ (k : X ⟶ Y) =>
        Space.IsUnramified B S hS k.hom) :=
      Space.isUnramified_isStableUnderBaseChange B S hS
    letI : MorphismProperty.IsLocalAtTarget
      (fun ⦃X Y : AlgebraicSpaces B S hS⦄ (k : X ⟶ Y) =>
        Space.IsUnramified B S hS k.hom)
      (Space.Topology.fppf.precoverage.{u, u} B S hS) :=
      (Space.isUnramified_isLocalAtTarget_fpqc B S hS).of_le
        (Space.fppfPrecoverage_le_fpqcPrecoverage.{u, u} B S hS)
    HasRelativeProperty B S hS
      (fun _ _ k => Space.IsUnramified B S hS k.hom)
      (graph B S hS g p q η).hom
      (isRepresentableByAlgebraicSpaces_graph B S hS g p q η)
```

**`AlgebraicGeometry.Stack.isLocallyOfFiniteType_graph`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GraphMorphism.lean, line 712](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/GraphMorphism.lean#L712). The attribute's comment: “part (1): locally of finite type”.

> **Stacks 050I, part (1), locally-of-finite-type half.** The graph of a 1-morphism of
> algebraic stacks over a base algebraic stack is locally of finite type, in the sense of
> Properties of Stacks, Section 04XB.
>
> By the locally-of-finite-type half of Stacks 050H part (1) the comparison 1-morphism
> `𝒳 ×_𝒴 𝒴 ⟶ 𝒳 ×_𝒯 𝒴` is locally of finite type, and
> `AlgebraicGeometry.Stack.relativeProperty_graph_of_comparison` carries that to the graph. No
> hypothesis on `q` is needed, exactly as in Stacks 050H. Together with
> `AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_graph` this is the whole of part (1).

```lean
theorem isLocallyOfFiniteType_graph (g : 𝒳 ⟶ 𝒴) (p : 𝒳 ⟶ 𝒯) (q : 𝒴 ⟶ 𝒯) (η : p ≅ g ≫ q) :
    IsLocallyOfFiniteType B S hS (graph B S hS g p q η).hom
```

**`AlgebraicGeometry.Stack.isLocallyQuasiFinite_graph`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GraphMorphism.lean, line 726](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/GraphMorphism.lean#L726). The attribute's comment: “part (3)”.

> **Stacks 050I, part (3).** If `q : 𝒴 ⟶ 𝒯` is quasi-DM then the graph of `g : 𝒳 ⟶ 𝒴` over `𝒯`
> is locally quasi-finite, in the sense of Properties of Stacks, Section 04XB.
>
> By Stacks 050H part (5) the comparison 1-morphism `𝒳 ×_𝒴 𝒴 ⟶ 𝒳 ×_𝒯 𝒴` is locally quasi-finite,
> and `AlgebraicGeometry.Stack.relativeProperty_graph_of_comparison` carries that to the graph.
> One statement suffices: Stacks 050H takes the quasi-DM condition of Stacks 04YW apart, so the
> input is local quasi-finiteness alone.

```lean
theorem isLocallyQuasiFinite_graph (g : 𝒳 ⟶ 𝒴) (p : 𝒳 ⟶ 𝒯) (q : 𝒴 ⟶ 𝒯) (η : p ≅ g ≫ q)
    (hq : AlgebraicStacks.IsQuasiDM B S hS q) :
    IsLocallyQuasiFinite B S hS (graph B S hS g p q η).hom
```

**`AlgebraicGeometry.Stack.isProper_graph`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GraphMorphism.lean, line 741](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/GraphMorphism.lean#L741). The attribute's comment: “part (4)”.

> **Stacks 050I, part (4).** If `q : 𝒴 ⟶ 𝒯` is separated then the graph of `g : 𝒳 ⟶ 𝒴` over
> `𝒯` is proper, in the sense of Properties of Stacks, Section 04XB.
>
> By Stacks 050H part (6) the comparison 1-morphism `𝒳 ×_𝒴 𝒴 ⟶ 𝒳 ×_𝒯 𝒴` is proper, and
> `AlgebraicGeometry.Stack.relativeProperty_graph_of_comparison` carries that to the graph. The
> separatedness condition of Stacks 04YW is a single property of the relative diagonal, so there
> is no conjunction to project here.

```lean
theorem isProper_graph (g : 𝒳 ⟶ 𝒴) (p : 𝒳 ⟶ 𝒯) (q : 𝒴 ⟶ 𝒯) (η : p ≅ g ≫ q)
    (hq : AlgebraicStacks.IsSeparated B S hS q) :
    IsProper B S hS (graph B S hS g p q η).hom
```

**`AlgebraicGeometry.Stack.isQuasiCompact_graph`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GraphMorphism.lean, line 759](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/GraphMorphism.lean#L759). The attribute's comment: “part (5): quasi-compact”.

> **Stacks 050I, part (5), the quasi-compactness half.** If `q : 𝒴 ⟶ 𝒯` is quasi-separated
> then the graph of `g : 𝒳 ⟶ 𝒴` over `𝒯` is quasi-compact, in the sense of Properties of Stacks,
> Section 04XB.
>
> By Stacks 050H part (7) the comparison 1-morphism `𝒳 ×_𝒴 𝒴 ⟶ 𝒳 ×_𝒯 𝒴` is quasi-compact, and
> `AlgebraicGeometry.Stack.relativeProperty_graph_of_comparison` carries that to the graph. A
> single statement suffices here, because Stacks 050H already projects the conjunction of
> Stacks 04YW quasi-separatedness: the input is quasi-compactness alone. The property is the
> longhand lambda rather than `AlgebraicGeometry.Space.quasiCompactProperty`, so neither
> Stacks 03HF nor Stacks 041L is needed even though both are available.

```lean
theorem isQuasiCompact_graph (g : 𝒳 ⟶ 𝒴) (p : 𝒳 ⟶ 𝒯) (q : 𝒴 ⟶ 𝒯) (η : p ≅ g ≫ q)
    (hq : AlgebraicStacks.IsQuasiSeparated B S hS q) :
    IsQuasiCompact B S hS (graph B S hS g p q η).hom
```

**`AlgebraicGeometry.Stack.isQuasiSeparated_graph`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GraphMorphism.lean, line 774](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/GraphMorphism.lean#L774). The attribute's comment: “part (5): quasi-separated”.

> **Stacks 050I, part (5), the quasi-separatedness half.** If `q : 𝒴 ⟶ 𝒯` is quasi-separated
> then the graph of `g : 𝒳 ⟶ 𝒴` over `𝒯` is quasi-separated, in the sense of Properties of Stacks,
> Section 04XB.
>
> As for the quasi-compactness half, over the second conjunct: Stacks 050H part (7) is stated
> twice, once for each conjunct of the quasi-separatedness condition of Stacks 04YW, so the input
> here is quasi-separatedness of the comparison 1-morphism alone.

```lean
theorem isQuasiSeparated_graph (g : 𝒳 ⟶ 𝒴) (p : 𝒳 ⟶ 𝒯) (q : 𝒴 ⟶ 𝒯) (η : p ≅ g ≫ q)
    (hq : AlgebraicStacks.IsQuasiSeparated B S hS q) :
    IsQuasiSeparated B S hS (graph B S hS g p q η).hom
```

## Tag 050J, a lemma

[Tag 050J](https://stacks.math.columbia.edu/tag/050J) in the Stacks Project.

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SectionMorphism.lean, line 231](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SectionMorphism.lean#L231). The attribute's comment: “part (1): representable by algebraic spaces”.

> **Stacks 050J, part (1), representability half.** A section of a 1-morphism of algebraic
> stacks is representable by algebraic spaces.
>
> The graph of `s` over `𝒯`, taken for the cospan `(𝟙 𝒯, f)`, is representable by algebraic spaces
> by Stacks 050I, and `s` is 2-isomorphic to its composite with the second projection, which is an
> equivalence by `AlgebraicGeometry.Stack.sectionSecondProjection_isEquivalence`. Stacks 0457
> carries representability across that square.

```lean
theorem isRepresentableByAlgebraicSpaces_section (f : 𝒳 ⟶ 𝒯) (s : 𝒯 ⟶ 𝒳)
    (hs : Nonempty (s ≫ f ≅ 𝟙 𝒯)) :
    IsRepresentableByAlgebraicSpaces B S hS s.hom.hom
```

**`AlgebraicGeometry.Stack.isLocallyOfFiniteType_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SectionMorphism.lean, line 360](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SectionMorphism.lean#L360). The attribute's comment: “part (1): locally of finite type”.

> **Stacks 050J, part (1), locally-of-finite-type half.** A section of a 1-morphism of
> algebraic stacks is locally of finite type, in the sense of Properties of Stacks, Section 04XB.
>
> By the locally-of-finite-type half of Stacks 050I part (1) the graph
> `Γ_s : 𝒯 ⟶ 𝒯 ×_{𝟙 𝒯, 𝒯, f} 𝒳` is locally of finite type, and
> `AlgebraicGeometry.Stack.relativeProperty_section_of_graph` carries that to `s`. No hypothesis on
> `f` is needed, exactly as in Stacks 050I and Stacks 050H. Together with
> `AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_section` this is the whole of
> part (1).

```lean
theorem isLocallyOfFiniteType_section (f : 𝒳 ⟶ 𝒯) (s : 𝒯 ⟶ 𝒳)
    (hs : Nonempty (s ≫ f ≅ 𝟙 𝒯)) :
    IsLocallyOfFiniteType B S hS s.hom
```

**`AlgebraicGeometry.Stack.isUnramified_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SectionMorphism.lean, line 376](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SectionMorphism.lean#L376). The attribute's comment: “part (2): unramified”.

> **Stacks 050J, part (2).** If `f : 𝒳 ⟶ 𝒯` is Deligne–Mumford then a section of `f` is
> unramified, in the relative sense of Stacks 03YK.
>
> By Stacks 050I part (2) the graph `Γ_s : 𝒯 ⟶ 𝒯 ×_{𝟙 𝒯, 𝒯, f} 𝒳` is unramified, and
> `AlgebraicGeometry.Stack.hasRelativeProperty_section_of_graph` carries that to `s`. The two
> instance arguments of Stacks 03YK are Stacks 03ZJ and Stacks 042A composed with the comparison
> of the fppf and fpqc precoverages.

```lean
theorem isUnramified_section (f : 𝒳 ⟶ 𝒯) (s : 𝒯 ⟶ 𝒳) (hs : Nonempty (s ≫ f ≅ 𝟙 𝒯))
    (hf : IsDM B S hS f) :
    letI : MorphismProperty.IsStableUnderBaseChange
      (fun ⦃X Y : AlgebraicSpaces B S hS⦄ (k : X ⟶ Y) =>
        Space.IsUnramified B S hS k.hom) :=
      Space.isUnramified_isStableUnderBaseChange B S hS
    letI : MorphismProperty.IsLocalAtTarget
      (fun ⦃X Y : AlgebraicSpaces B S hS⦄ (k : X ⟶ Y) =>
        Space.IsUnramified B S hS k.hom)
      (Space.Topology.fppf.precoverage.{u, u} B S hS) :=
      (Space.isUnramified_isLocalAtTarget_fpqc B S hS).of_le
        (Space.fppfPrecoverage_le_fpqcPrecoverage.{u, u} B S hS)
    HasRelativeProperty B S hS
      (fun _ _ k => Space.IsUnramified B S hS k.hom)
      s.hom (isRepresentableByAlgebraicSpaces_section B S hS f s hs)
```

**`AlgebraicGeometry.Stack.isLocallyQuasiFinite_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SectionMorphism.lean, line 407](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SectionMorphism.lean#L407). The attribute's comment: “part (3): locally quasi-finite”.

> **Stacks 050J, part (3).** If `f : 𝒳 ⟶ 𝒯` is quasi-DM then a section of `f` is locally
> quasi-finite, in the sense of Properties of Stacks, Section 04XB.
>
> By Stacks 050I part (3) the graph `Γ_s : 𝒯 ⟶ 𝒯 ×_{𝟙 𝒯, 𝒯, f} 𝒳` is locally quasi-finite, and
> `AlgebraicGeometry.Stack.relativeProperty_section_of_graph` carries that to `s`. One statement
> suffices: Stacks 050I already takes the quasi-DM condition of Stacks 04YW apart, so the input is
> local quasi-finiteness alone. The property is the longhand lambda rather than the packaged local
> quasi-finiteness of Stacks 06MF, so no instance of Stacks 03YK is needed.

```lean
theorem isLocallyQuasiFinite_section (f : 𝒳 ⟶ 𝒯) (s : 𝒯 ⟶ 𝒳) (hs : Nonempty (s ≫ f ≅ 𝟙 𝒯))
    (hf : AlgebraicStacks.IsQuasiDM B S hS f) :
    IsLocallyQuasiFinite B S hS s.hom
```

**`AlgebraicGeometry.Stack.isRelativelyProper_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SectionMorphism.lean, line 435](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SectionMorphism.lean#L435). The attribute's comment: “part (4): proper”.

> **Stacks 050J, part (4).** If `f : 𝒳 ⟶ 𝒯` is separated then a section of `f` is proper in
> the sense of Properties of Stacks, Section 04XB.
>
> By Stacks 050I part (4) the graph `Γ_s : 𝒯 ⟶ 𝒯 ×_{𝟙 𝒯, 𝒯, f} 𝒳` is proper, and
> `AlgebraicGeometry.Stack.relativeProperty_section_of_graph` carries that to `s`. The separatedness
> condition of Stacks 04YW is a single property of the relative diagonal, so there is no
> conjunction to project here. The property is the longhand lambda rather than
> `AlgebraicGeometry.Space.properProperty`, so the fppf
> `CategoryTheory.MorphismProperty.IsLocalAtTarget` instance of Stacks 0422 is not needed — which
> matters here, because this library does not have it.
>
> Properness is read in the sense of Section 04XB, as it is in Stacks 050I part (4)
> (`AlgebraicGeometry.Stack.isProper_graph`) and in Stacks 050H part (6)
> (`AlgebraicGeometry.Stack.isProper_comparison`). That is the reading the source's own proof
> forces: Stacks 050J is a special case of Stacks 050I, so its conclusions are the conclusions of
> Stacks 050I, and `s` carries the Section 04XB notions because part (1) makes it representable by
> algebraic spaces. Reading part (4) at Stacks 0CL5 instead would assert properness of `s` as a
> 1-morphism of algebraic stacks, which is a different statement from the one Stacks 050I
> supplies.

```lean
theorem isRelativelyProper_section (f : 𝒳 ⟶ 𝒯) (s : 𝒯 ⟶ 𝒳) (hs : Nonempty (s ≫ f ≅ 𝟙 𝒯))
    (hf : AlgebraicStacks.IsSeparated B S hS f) :
    IsProper B S hS s.hom
```

**`AlgebraicGeometry.Stack.isQuasiCompact_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SectionMorphism.lean, line 473](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SectionMorphism.lean#L473). The attribute's comment: “part (5): quasi-compact”.

> **Stacks 050J, part (5), quasi-compactness half.** If `f : 𝒳 ⟶ 𝒯` is quasi-separated then a
> section of `f` is quasi-compact in the sense of Stacks 050U: every base change of it by a
> quasi-compact algebraic stack is again a quasi-compact algebraic stack.
>
> The section is representable by algebraic spaces by part (1), and quasi-compact in the relative
> sense of Properties of Stacks, Section 04XB by
> `AlgebraicGeometry.Stack.isRelativelyQuasiCompact_section`. Stacks 050T identifies the two
> notions for a 1-morphism representable by algebraic spaces, and that is the whole step.

```lean
theorem isQuasiCompact_section (f : 𝒳 ⟶ 𝒯) (s : 𝒯 ⟶ 𝒳) (hs : Nonempty (s ≫ f ≅ 𝟙 𝒯))
    (hf : AlgebraicStacks.IsQuasiSeparated B S hS f) :
    IsQuasiCompactMorphism B S hS s
```

**`AlgebraicGeometry.Stack.isQuasiSeparated_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SectionMorphism.lean, line 491](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SectionMorphism.lean#L491). The attribute's comment: “part (5): quasi-separated”.

> **Stacks 050J, part (5), quasi-separatedness half.** If `f : 𝒳 ⟶ 𝒯` is quasi-separated then
> a section of `f` is quasi-separated, in the sense of Properties of Stacks, Section 04XB.
>
> By Stacks 050I part (5) the graph `Γ_s : 𝒯 ⟶ 𝒯 ×_{𝟙 𝒯, 𝒯, f} 𝒳` is quasi-separated, and
> `AlgebraicGeometry.Stack.relativeProperty_section_of_graph` carries that to `s`. A single
> statement suffices, because Stacks 050I already projects the conjunction of Stacks 04YW
> quasi-separatedness: the input is quasi-separatedness alone. The quasi-compactness half of
> part (5) is `AlgebraicGeometry.Stack.isQuasiCompact_section`, which reads the Section 04XB
> assertion `AlgebraicGeometry.Stack.isRelativelyQuasiCompact_section` across Stacks 050T into the
> notion of Stacks 050U.

```lean
theorem isQuasiSeparated_section (f : 𝒳 ⟶ 𝒯) (s : 𝒯 ⟶ 𝒳) (hs : Nonempty (s ≫ f ≅ 𝟙 𝒯))
    (hf : AlgebraicStacks.IsQuasiSeparated B S hS f) :
    IsQuasiSeparated B S hS s.hom
```

## Tag 050K, a lemma

[Tag 050K](https://stacks.math.columbia.edu/tag/050K) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isDM_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationComposition.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationComposition.lean#L149). The attribute's comment: “dm”.

> **Stacks 050K, DM.** The composite of two Deligne–Mumford 1-morphisms of algebraic stacks over
> `S` is Deligne–Mumford: its relative diagonal is `Δ_f` followed by the comparison 1-morphism `i`,
> `Δ_f` is unramified in the sense of Stacks 04XB because `f` is DM, `i` is unramified because `g`
> is DM (**Stacks 050H**, part (4)), and a condition of Stacks 04XB at a property stable under
> composition which descends along a surjective étale scheme chart of the target is stable under
> composition (**Stacks 045B**).

```lean
theorem isDM_comp (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵) (hf : Stack.IsDM B S hS f)
    (hg : Stack.IsDM B S hS g) : Stack.IsDM B S hS (f ≫ g)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiDM_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationComposition.lean, line 247](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationComposition.lean#L247). The attribute's comment: “quasi-DM”.

> **Stacks 050K, quasi-DM.** The composite of two quasi-DM 1-morphisms of algebraic stacks over
> `S` is quasi-DM: `Δ_{f ≫ g}` is `Δ_f` followed by the comparison 1-morphism `i`, `Δ_f` is locally
> quasi-finite in the sense of Stacks 04XB because `f` is quasi-DM, `i` is locally quasi-finite
> because `g` is quasi-DM (**Stacks 050H**, part (5)), and local quasi-finiteness of morphisms of
> algebraic spaces over `S` composes (**Stacks 03XK**) and is fpqc local on the base
> (**Stacks 0427**).

```lean
theorem isQuasiDM_comp (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵) (hf : IsQuasiDM B S hS f)
    (hg : IsQuasiDM B S hS g) : IsQuasiDM B S hS (f ≫ g)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isSeparated_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationComposition.lean, line 264](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationComposition.lean#L264). The attribute's comment: “separated”.

> **Stacks 050K, separated.** The composite of two separated 1-morphisms of algebraic stacks
> over `S` is separated: `Δ_{f ≫ g}` is `Δ_f` followed by the comparison 1-morphism `i`, `Δ_f` is
> proper in the sense of Stacks 04XB because `f` is separated, `i` is proper because `g` is
> separated (**Stacks 050H**, part (6)), and properness of morphisms of algebraic spaces over `S`
> composes (**Stacks 04XY**) and descends along a surjective étale scheme chart of the target
> (`AlgebraicGeometry.Space.properMorphismProperty_of_pullbackSnd_atlas`).

```lean
theorem isSeparated_comp (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵) (hf : IsSeparated B S hS f)
    (hg : IsSeparated B S hS g) : IsSeparated B S hS (f ≫ g)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiSeparated_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationComposition.lean, line 280](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationComposition.lean#L280). The attribute's comment: “quasi-separated”.

> **Stacks 050K, quasi-separated.** The composite of two quasi-separated 1-morphisms of
> algebraic stacks over `S` is quasi-separated. Quasi-separatedness of Stacks 04YW is the
> conjunction of two conditions of Stacks 04XB on `Δ_f` — quasi-compactness and
> quasi-separatedness — and each half is the same composition argument at its own property:
> `Δ_{f ≫ g} = Δ_f ≫ i`, the half for `Δ_f` is the axiom for `f`, the half for `i` comes from the
> axiom for `g` by **Stacks 050H**, part (7), and quasi-compactness and quasi-separatedness of
> morphisms of algebraic spaces over `S` compose (**Stacks 03HG**, **Stacks 03KQ**) and are fpqc
> local on the base (**Stacks 041L**, **Stacks 041N**).

```lean
theorem isQuasiSeparated_comp (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵) (hf : IsQuasiSeparated B S hS f)
    (hg : IsQuasiSeparated B S hS g) : IsQuasiSeparated B S hS (f ≫ g)
```

## Tag 050L, a lemma

[Tag 050L](https://stacks.math.columbia.edu/tag/050L) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isAbsolutelyQuasiSeparated_of_isQuasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationAbsoluteQuasiSeparated.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationAbsoluteQuasiSeparated.lean#L73). The attribute's comment: “quasi\_separated\_absolute”.

> **Stacks 050L, part (8).** If `f : 𝒳 ⟶ 𝒴` is quasi-separated and `𝒴` is quasi-separated, then
> `𝒳` is quasi-separated.
>
> Both absolute properties are quasi-separatedness over the terminal scheme of the views
> `AlgebraicGeometry.Stack.AlgebraicStacks.viewOverIntegers` of `𝒳` and `𝒴` there, and that view is
> `AlgebraicGeometry.Stack.changeBaseAlgebraicStack` along `terminal.from S` on the nose. So this is
> part (4) at the terminal scheme, applied to the 1-morphism of views that the hom-bijection of
> Stacks 04X5 assigns to `f`, which is quasi-separated by
> `AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiSeparated_changeBase`.

```lean
theorem isAbsolutelyQuasiSeparated_of_isQuasiSeparated (f : 𝒳 ⟶ 𝒴)
    (hY : IsAbsolutelyQuasiSeparated B S hS hZ 𝒴) (hf : IsQuasiSeparated B S hS f) :
    IsAbsolutelyQuasiSeparated B S hS hZ 𝒳
```

**`AlgebraicGeometry.Stack.isSeparatedOver_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationAbsoluteSource.lean, line 341](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationAbsoluteSource.lean#L341). The attribute's comment: “part (3): separated over the base”.

> **Stacks 050L, part (3).** If `𝒴` is separated over `S` and the 1-morphism `f : 𝒳 ⟶ 𝒴` is
> separated, then `𝒳` is separated over `S`.
>
> Being separated over `S` is being separated as a structure morphism (**Stacks 050D**, part (3)),
> the structure morphism of `𝒳` is `f` followed by that of `𝒴`
> (`AlgebraicGeometry.Stack.comp_structureMorphism`), and separated 1-morphisms compose
> (**Stacks 050K**).

```lean
theorem isSeparatedOver_of_isSeparated (f : 𝒳 ⟶ 𝒴) (h𝒴 : IsSeparatedOver B S hS 𝒴)
    (hf : AlgebraicStacks.IsSeparated B S hS f) : IsSeparatedOver B S hS 𝒳
```

**`AlgebraicGeometry.Stack.isDMAbs_of_isDM`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationAbsoluteSource.lean, line 372](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationAbsoluteSource.lean#L372). The attribute's comment: “part (5): DM”.

> **Stacks 050L, part (5).** If `𝒴` is DM and the 1-morphism `f : 𝒳 ⟶ 𝒴` is DM, then `𝒳` is
> DM — the two conditions on objects in the absolute sense of **Stacks 050D**, part (5).
>
> Being DM is being DM over `Spec(ℤ)` after viewing (**Stacks 050D**, part (5)); the structure
> morphism over `Spec(ℤ)` of `𝒳` viewed is `f` viewed followed by that of `𝒴` viewed
> (`AlgebraicGeometry.Stack.comp_structureMorphism` at the terminal base); the DM axiom for `f`
> survives the viewing (`AlgebraicGeometry.Stack.isDM_changeBaseHomAlgebraicStacks`); and DM
> 1-morphisms compose (**Stacks 050K**). So this is part (1) of Stacks 050L read at the base
> `Spec(ℤ)`.

```lean
theorem isDMAbs_of_isDM (f : 𝒳 ⟶ 𝒴) (h𝒴 : IsDMAbs.{u, w, w'} B S hS 𝒴)
    (hf : IsDM B S hS f) : IsDMAbs.{u, w, w'} B S hS 𝒳
```

**`AlgebraicGeometry.Stack.isQuasiDMAbs_of_isQuasiDM`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationAbsoluteSource.lean, line 389](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationAbsoluteSource.lean#L389). The attribute's comment: “part (6): quasi-DM”.

> **Stacks 050L, part (6).** If `𝒴` is quasi-DM and the 1-morphism `f : 𝒳 ⟶ 𝒴` is quasi-DM,
> then `𝒳` is quasi-DM — the two conditions on objects in the absolute sense of **Stacks 050D**,
> part (6).
>
> This is part (2) of Stacks 050L read at the base `Spec(ℤ)`, with
> `AlgebraicGeometry.Stack.isQuasiDM_changeBaseHomAlgebraicStacks` supplying the axiom for the
> viewed 1-morphism.

```lean
theorem isQuasiDMAbs_of_isQuasiDM (f : 𝒳 ⟶ 𝒴) (h𝒴 : IsQuasiDMAbs.{u, w, w'} B S hS 𝒴)
    (hf : AlgebraicStacks.IsQuasiDM B S hS f) : IsQuasiDMAbs.{u, w, w'} B S hS 𝒳
```

**`AlgebraicGeometry.Stack.isSeparatedAbs_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationAbsoluteSource.lean, line 409](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationAbsoluteSource.lean#L409). The attribute's comment: “part (7): separated, f's axiom read over Spec(Z) not over S”.

> **Stacks 050L, part (7).** If `𝒴` is separated and the 1-morphism `f : 𝒳 ⟶ 𝒴` is separated,
> then `𝒳` is separated — the two conditions on objects in the absolute sense of **Stacks 050D**,
> part (7).
>
> This is part (3) of Stacks 050L read at the base `Spec(ℤ)`. The hypothesis on `f` is the
> Stacks 04YW separatedness axiom for `f` **viewed over `Spec(ℤ)`**, which is the base the absolute
> statement lives at; it is not the axiom over `S`. Unlike the DM axiom of part (5), the
> separatedness axiom is not known in this library to survive the viewing: it is the Stacks 04XB
> condition at properness, which is not an every-étale-chart condition. See the implementation
> notes of this file.

```lean
theorem isSeparatedAbs_of_isSeparated (f : 𝒳 ⟶ 𝒴) (h𝒴 : IsSeparatedAbs.{u, w, w'} B S hS 𝒴)
    (hf : AlgebraicStacks.IsSeparated B _ (contains_specULiftZ B)
      (viewOverIntHom.{u, w, w'} B S hS f)) :
    IsSeparatedAbs.{u, w, w'} B S hS 𝒳
```

**`AlgebraicGeometry.Stack.isQuasiSeparatedAbs_of_isQuasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationAbsoluteSource.lean, line 427](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationAbsoluteSource.lean#L427). The attribute's comment: “part (8): quasi-separated, f's axiom read over Spec(Z) not over S”.

> **Stacks 050L, part (8).** If `𝒴` is quasi-separated and the 1-morphism `f : 𝒳 ⟶ 𝒴` is
> quasi-separated, then `𝒳` is quasi-separated — the two conditions on objects in the absolute
> sense of **Stacks 050D**, part (8), and so each the conjunction of quasi-compactness and
> quasi-separatedness of a relative diagonal. Both conjuncts of the conclusion are proved, through
> `AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiSeparated_comp`.
>
> This is part (4) of Stacks 050L read at the base `Spec(ℤ)`. As in part (7) the hypothesis on `f`
> is the Stacks 04YW axiom for `f` **viewed over `Spec(ℤ)`**: quasi-separatedness is the Stacks
> 04XB condition at quasi-compactness together with quasi-separatedness of morphisms of algebraic
> spaces, neither of which is an every-étale-chart condition.

```lean
theorem isQuasiSeparatedAbs_of_isQuasiSeparated (f : 𝒳 ⟶ 𝒴)
    (h𝒴 : IsQuasiSeparatedAbs.{u, w, w'} B S hS 𝒴)
    (hf : AlgebraicStacks.IsQuasiSeparated B _ (contains_specULiftZ B)
      (viewOverIntHom.{u, w, w'} B S hS f)) :
    IsQuasiSeparatedAbs.{u, w, w'} B S hS 𝒳
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isDMOver_of_isDM`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationOverBaseSource.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationOverBaseSource.lean#L95). The attribute's comment: “dm\_over\_s”.

> **Stacks 050L, part (1).** If `f : 𝒳 ⟶ 𝒴` is Deligne–Mumford and `𝒴` is Deligne–Mumford over
> the base scheme `S`, then `𝒳` is Deligne–Mumford over `S`.
>
> The structure morphism of `𝒳` is `f` followed by the structure morphism of `𝒴`
> (`AlgebraicGeometry.Stack.comp_structureMorphism`), so this is the Deligne–Mumford case of
> Stacks 050K.

```lean
theorem isDMOver_of_isDM (f : 𝒳 ⟶ 𝒴) (hY : Stack.IsDMOver B S hS 𝒴) (hf : Stack.IsDM B S hS f) :
    Stack.IsDMOver B S hS 𝒳
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiDMOver_of_isQuasiDM`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationOverBaseSource.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationOverBaseSource.lean#L108). The attribute's comment: “quasi\_dm\_over\_s”.

> **Stacks 050L, part (2).** If `f : 𝒳 ⟶ 𝒴` is quasi-DM and `𝒴` is quasi-DM over the base
> scheme `S`, then `𝒳` is quasi-DM over `S`.
>
> The structure morphism of `𝒳` is `f` followed by the structure morphism of `𝒴`
> (`AlgebraicGeometry.Stack.comp_structureMorphism`), so this is the quasi-DM case of
> Stacks 050K.

```lean
theorem isQuasiDMOver_of_isQuasiDM (f : 𝒳 ⟶ 𝒴) (hY : Stack.IsQuasiDMOver B S hS 𝒴)
    (hf : IsQuasiDM B S hS f) :
    Stack.IsQuasiDMOver B S hS 𝒳
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiSeparatedOver_of_isQuasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationOverBaseSource.lean, line 122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationOverBaseSource.lean#L122). The attribute's comment: “quasi\_separated\_over\_s”.

> **Stacks 050L, part (4).** If `f : 𝒳 ⟶ 𝒴` is quasi-separated and `𝒴` is quasi-separated over
> the base scheme `S`, then `𝒳` is quasi-separated over `S`.
>
> The structure morphism of `𝒳` is `f` followed by the structure morphism of `𝒴`
> (`AlgebraicGeometry.Stack.comp_structureMorphism`), so this is the quasi-separated case of
> Stacks 050K.

```lean
theorem isQuasiSeparatedOver_of_isQuasiSeparated (f : 𝒳 ⟶ 𝒴)
    (hY : Stack.IsQuasiSeparatedOver B S hS 𝒴) (hf : IsQuasiSeparated B S hS f) :
    Stack.IsQuasiSeparatedOver B S hS 𝒳
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isAbsolutelyDM_of_isDM`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationOverBaseSource.lean, line 151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationOverBaseSource.lean#L151). The attribute's comment: “dm\_absolute”.

> **Stacks 050L, part (5).** If `f : 𝒳 ⟶ 𝒴` is Deligne–Mumford and `𝒴` is Deligne–Mumford,
> then `𝒳` is Deligne–Mumford.
>
> Both absolute properties are the corresponding properties over the terminal scheme of the views
> `AlgebraicGeometry.Stack.AlgebraicStacks.viewOverIntegers` of `𝒳` and `𝒴` there, and that view is
> `AlgebraicGeometry.Stack.changeBaseAlgebraicStack` along `terminal.from S` on the nose. So this is
> part (1) at the terminal scheme, applied to the 1-morphism of views that the hom-bijection of
> Stacks 04X5 assigns to `f`, which is Deligne–Mumford by
> `AlgebraicGeometry.Stack.isDM_changeBase_iff`.

```lean
theorem isAbsolutelyDM_of_isDM (f : 𝒳 ⟶ 𝒴) (hY : IsAbsolutelyDM B S hS hZ 𝒴)
    (hf : Stack.IsDM B S hS f) :
    IsAbsolutelyDM B S hS hZ 𝒳
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isAbsolutelyQuasiDM_of_isQuasiDM`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationOverBaseSource.lean, line 171](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationOverBaseSource.lean#L171). The attribute's comment: “quasi\_dm\_absolute”.

> **Stacks 050L, part (6).** If `f : 𝒳 ⟶ 𝒴` is quasi-DM and `𝒴` is quasi-DM, then `𝒳` is
> quasi-DM.
>
> Part (2) at the terminal scheme, applied to the 1-morphism of views that the hom-bijection of
> Stacks 04X5 assigns to `f`, which is quasi-DM by
> `AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiDM_changeBase_iff`. That comparison is stated at
> `AlgebraicGeometry.Stack.AlgebraicStacks.IsQuasiDMWithRepresentableDiagonal`, the reading which
> carries the representability witness of the relative diagonal, so the hypothesis and the
> conclusion are passed across
> `AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiDMWithRepresentableDiagonal_iff_isQuasiDM`.

```lean
theorem isAbsolutelyQuasiDM_of_isQuasiDM (f : 𝒳 ⟶ 𝒴) (hY : IsAbsolutelyQuasiDM B S hS hZ 𝒴)
    (hf : IsQuasiDM B S hS f) :
    IsAbsolutelyQuasiDM B S hS hZ 𝒳
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isAbsolutelySeparated_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationOverBaseSource.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationOverBaseSource.lean#L192). The attribute's comment: “separated\_absolute”.

> **Stacks 050L, part (7).** If `f : 𝒳 ⟶ 𝒴` is separated and `𝒴` is separated, then `𝒳` is
> separated.
>
> Both absolute properties are separatedness over the terminal scheme of the views
> `AlgebraicGeometry.Stack.AlgebraicStacks.viewOverIntegers` of `𝒳` and `𝒴` there, and that view is
> `AlgebraicGeometry.Stack.changeBaseAlgebraicStack` along `terminal.from S` on the nose. So this is
> part (3) at the terminal scheme, applied to the 1-morphism of views that the hom-bijection of
> Stacks 04X5 assigns to `f`, which is separated by
> `AlgebraicGeometry.Stack.isProper_relativeDiagonal_changeBase`.

```lean
theorem isAbsolutelySeparated_of_isSeparated (f : 𝒳 ⟶ 𝒴)
    (hY : IsAbsolutelySeparated B S hS hZ 𝒴) (hf : IsSeparated B S hS f) :
    IsAbsolutelySeparated B S hS hZ 𝒳
```

## Tag 050M, a lemma

[Tag 050M](https://stacks.math.columbia.edu/tag/050M) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiSeparated_of_isQuasiSeparated_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiSeparatedCancellation.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/QuasiSeparatedCancellation.lean#L129). The attribute's comment: “quasi\_separated\_first”.

> **Stacks 050M, part (4).** If a composite `f ≫ g` of 1-morphisms of algebraic stacks over `S`
> is quasi-separated and the relative diagonal of `g` is quasi-separated, then `f` is
> quasi-separated.
>
> The comparison 1-morphism `i : 𝒴 ×_𝒴 𝒳 ⟶ 𝒴 ×_𝒵 𝒳` of Stacks 050H, taken at the identity of `𝒴`,
> composes with the second projection of `𝒴 ×_𝒵 𝒳` to give the second projection of `𝒴 ×_𝒴 𝒳` on
> the nose. The projection out of `𝒴 ×_𝒵 𝒳` is the base change of `f ≫ g` along `𝟙 𝒴 ≫ g` and is
> quasi-separated by Stacks 050F; `i` is quasi-separated by Stacks 050H part (2) from the
> hypothesis on `Δ_g`, upgraded from the Section 04XB predicate to the Definition 04YW condition by
> the two forms of Stacks 04YT condition (1); and Stacks 050K composes them. The projection out of
> `𝒴 ×_𝒴 𝒳` is the base change of `f` along an identity, which is `f` itself by
> `CategoryTheory.Bicategory.isTwoFibreProduct_trivialBaseChangeSquare`.

```lean
theorem isQuasiSeparated_of_isQuasiSeparated_comp
    {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hfg : IsQuasiSeparated B S hS (f ≫ g))
    (hΔg : Stack.IsQuasiSeparated B S hS
      (Stack.relativeDiagonalAlgebraicStacks B S hS g).hom) :
    IsQuasiSeparated B S hS f
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiDM_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationCancellation.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationCancellation.lean#L137). The attribute's comment: “quasi\_dm\_first”.

> **Stacks 050M, part (2).** If a composite `f ≫ g` of 1-morphisms of algebraic stacks over `S`
> is quasi-DM, then `f` is quasi-DM.
>
> `f` is 2-isomorphic to the graph of `f` over `𝒵` followed by the second projection of the
> canonical 2-fibre product of the cospan `(f ≫ g, g)`
> (`AlgebraicGeometry.Stack.graph_snd_iso`). That projection is the base change of `f ≫ g` along
> `g`, so it is quasi-DM by Stacks 050F; the graph is representable by algebraic spaces by
> Stacks 050I part (1), and the relative diagonal of such a 1-morphism is locally quasi-finite by
> Stacks 04YQ part (5), which is the quasi-DM condition on the nose. Stacks 050K composes them.

```lean
theorem isQuasiDM_of_comp {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵) (hfg : IsQuasiDM B S hS (f ≫ g)) :
    IsQuasiDM B S hS f
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isDM_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationCancellation.lean, line 170](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationCancellation.lean#L170). The attribute's comment: “dm\_first”.

> **Stacks 050M, part (1).** If a composite `f ≫ g` of 1-morphisms of algebraic stacks over `S`
> is Deligne–Mumford, then `f` is Deligne–Mumford.
>
> `f` is 2-isomorphic to the graph of `f` over `𝒵` followed by the second projection of the
> canonical 2-fibre product of the cospan `(f ≫ g, g)`
> (`AlgebraicGeometry.Stack.graph_snd_iso`). That projection is the base change of `f ≫ g` along
> `g`, so it is Deligne–Mumford by Stacks 050F; the graph is representable by algebraic spaces by
> Stacks 050I part (1), and a 1-morphism representable by algebraic spaces is Deligne–Mumford
> because its relative diagonal is a monomorphism which is locally of finite type, hence unramified
> by Stacks 05W6. Stacks 050K composes them.

```lean
theorem isDM_of_comp {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵) (hfg : Stack.IsDM B S hS (f ≫ g)) :
    Stack.IsDM B S hS f
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isSeparated_of_comp_of_isSeparated_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationCancellation.lean, line 290](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationCancellation.lean#L290). The attribute's comment: “part (3): a separated composite whose second factor has separated relative diagonal has separated first factor”.

> **Stacks 050M, part (3).** If a composite of 1-morphisms of algebraic stacks over `S` is
> separated and the relative diagonal `Δ_g` of its second factor is separated in the sense of
> Stacks 04XB, then its first factor is separated.
>
> The relative diagonal `Δ_{f ≫ g}` is `Δ_f` followed by the comparison 1-morphism `i`, it is
> proper in the sense of Stacks 04XB because `f ≫ g` is separated, `i` is separated because `Δ_g`
> is (**Stacks 050H**, part (3)), and properness of morphisms of algebraic spaces over `S` is
> inherited by the first factor of a composite that has it whose second factor is separated
> (**Stacks 04NX**, part (2)).

```lean
theorem isSeparated_of_comp_of_isSeparated_diagonal (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hfg : IsSeparated B S hS (f ≫ g))
    (hΔ : Stack.IsSeparated.{u, u, u + 1} B S hS
      (_root_.AlgebraicGeometry.Stack.relativeDiagonal.{u, u, u + 1} B S hS 𝒴.val 𝒵.val g.hom)) :
    IsSeparated B S hS f
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiSeparated_of_comp_of_isQuasiSeparated_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationCancellation.lean, line 317](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationCancellation.lean#L317). The attribute's comment: “part (4): a quasi-separated composite whose second factor has quasi-separated relative diagonal has quasi-separated first factor”.

> **Stacks 050M, part (4).** If a composite of 1-morphisms of algebraic stacks over `S` is
> quasi-separated and the relative diagonal `Δ_g` of its second factor is quasi-separated in the
> sense of Stacks 04XB, then its first factor is quasi-separated.
>
> Quasi-separatedness of Stacks 04YW is the conjunction of two conditions of Stacks 04XB on the
> relative diagonal — quasi-compactness and quasi-separatedness — and each half cancels the
> comparison 1-morphism `i` at its own property. The hypothesis on `i` comes from the one on `Δ_g`
> by **Stacks 050H**, part (2), and it is needed only by the quasi-compact half: quasi-compactness
> of morphisms of algebraic spaces over `S` cancels against a quasi-separated second factor
> (**Stacks 03KS**), while quasi-separatedness cancels outright (**Stacks 03KR**).

```lean
theorem isQuasiSeparated_of_comp_of_isQuasiSeparated_diagonal (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hfg : IsQuasiSeparated B S hS (f ≫ g))
    (hΔ : Stack.IsQuasiSeparated.{u, u, u + 1} B S hS
      (_root_.AlgebraicGeometry.Stack.relativeDiagonal.{u, u, u + 1} B S hS 𝒴.val 𝒵.val g.hom)) :
    IsQuasiSeparated B S hS f
```

## Tag 050N, a lemma

[Tag 050N](https://stacks.math.columbia.edu/tag/050N) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiSeparated_of_isQuasiSeparatedOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiSeparatedCancellation.lean, line 170](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/QuasiSeparatedCancellation.lean#L170). The attribute's comment: “quasi\_separated\_source”.

> **Stacks 050N, part (8).** A 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` whose source
> is quasi-separated over `S` and whose target has quasi-separated relative diagonal over `S` is
> quasi-separated.
>
> The structure morphism of `𝒳` is `f` followed by the structure morphism of `𝒴`
> (`AlgebraicGeometry.Stack.comp_structureMorphism`, an equality of 1-morphisms on the nose), so
> the hypothesis on `𝒳` says that that composite is quasi-separated, and Stacks 050M part (4)
> cancels the second factor. That is the source's own proof: *"Parts (5), (6), (7), and (8) follow
> immediately from Lemma 050M"*.

```lean
theorem isQuasiSeparated_of_isQuasiSeparatedOver
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (h𝒳 : Stack.IsQuasiSeparatedOver B S hS 𝒳)
    (hΔ : Stack.IsQuasiSeparated B S hS
      (Stack.relativeDiagonalAlgebraicStacks B S hS
        (Stack.structureMorphism B S hS 𝒴)).hom) :
    IsQuasiSeparated B S hS f
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isAbsolutelyDM_iff_isDMOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationAbsoluteDMEquivalence.lean, line 165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationAbsoluteDMEquivalence.lean#L165). The attribute's comment: “dm\_equiv”.

> **Stacks 050N, part (1).** An algebraic stack over `S` is Deligne–Mumford exactly when it is
> Deligne–Mumford over `S`.

```lean
theorem isAbsolutelyDM_iff_isDMOver (𝒳 : Stack.AlgebraicStacks.{u, w} B S hS) :
    IsAbsolutelyDM.{u, w} B S hS hZ 𝒳 ↔ Stack.IsDMOver B S hS 𝒳
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isAbsolutelyQuasiDM_iff_isQuasiDMOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationAbsoluteDMEquivalence.lean, line 173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationAbsoluteDMEquivalence.lean#L173). The attribute's comment: “quasi\_dm\_equiv”.

> **Stacks 050N, part (2).** An algebraic stack over `S` is quasi-DM exactly when it is
> quasi-DM over `S`.

```lean
theorem isAbsolutelyQuasiDM_iff_isQuasiDMOver (𝒳 : Stack.AlgebraicStacks.{u, w} B S hS) :
    IsAbsolutelyQuasiDM.{u, w} B S hS hZ 𝒳 ↔ Stack.IsQuasiDMOver B S hS 𝒳
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiSeparatedOver_of_isAbsolutelyQuasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationSmallerBase.lean, line 390](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationSmallerBase.lean#L390). The attribute's comment: “quasi\_separated\_base”.

> **Stacks 050N, part (4): a quasi-separated algebraic stack is quasi-separated over its
> base.** This is part (8) of Stacks 050D implying part (4): absolute quasi-separatedness is
> quasi-separatedness over the terminal scheme `Spec ℤ` after `𝒳` has been viewed over it by
> Construction A, so this is
> `AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiSeparatedOver_of_isQuasiSeparatedOver_changeBase`
> at `S' = Spec ℤ`.

```lean
theorem isQuasiSeparatedOver_of_isAbsolutelyQuasiSeparated
    (hZ : B.Contains (⊤_ Scheme.{u})) (𝒳 : Stack.AlgebraicStacks.{u, w} B S hS)
    (h𝒳 : IsAbsolutelyQuasiSeparated B S hS hZ 𝒳) :
    Stack.IsQuasiSeparatedOver B S hS 𝒳
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isSeparatedOver_of_isAbsolutelySeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationSmallerBaseDMAndSeparated.lean, line 211](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationSmallerBaseDMAndSeparated.lean#L211). The attribute's comment: “separated\_base”.

> **Stacks 050N, the separated assertion: a separated algebraic stack is separated over its
> base.** This is part (7) of Stacks 050D implying part (3): absolute separatedness is
> separatedness over the terminal scheme `Spec ℤ` after `𝒳` has been viewed over it by
> Construction A, so this is
> `AlgebraicGeometry.Stack.AlgebraicStacks.isSeparatedOver_of_isSeparatedOver_changeBase` at
> `S' = Spec ℤ`.

```lean
theorem isSeparatedOver_of_isAbsolutelySeparated
    (hZ : B.Contains (⊤_ Scheme.{u})) (𝒳 : Stack.AlgebraicStacks.{u, w} B S hS)
    (h𝒳 : IsAbsolutelySeparated B S hS hZ 𝒳) :
    Stack.IsSeparatedOver B S hS 𝒳
```

**`AlgebraicGeometry.Stack.isDMAbs_iff_isDMOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationSourceOverBase.lean, line 239](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationSourceOverBase.lean#L239). The attribute's comment: “part (1)”.

> **Stacks 050N, part (1).** An algebraic stack `𝒳` over `S` is DM **if and only if** it is DM
> over `S`.
>
> The implication from the absolute axiom is `AlgebraicGeometry.Stack.isDMOver_of_isDMAbs` above,
> which cancels the second factor of the factorisation `𝒳 ⟶ S ⟶ Spec(ℤ)` by part (1) of
> **Stacks 050M** and carries the resulting condition on the relative diagonal back from the base
> `Spec(ℤ)` to the base `S`. The converse is
> `AlgebraicGeometry.Stack.isDMAbs_of_isDMOver`, which composes along the same factorisation by
> part (5) of **Stacks 050L**, using that the second factor is DM
> (`AlgebraicGeometry.Stack.isDMOver_viewOverInt_schemeStack`, i.e. that `Δ_{S/ℤ}` is unramified).
> Neither direction carries a hypothesis the source does not have.

```lean
theorem isDMAbs_iff_isDMOver (𝒵 : AlgebraicStacks.{u, w} B S hS) :
    IsDMAbs.{u, w, w'} B S hS 𝒵 ↔ IsDMOver B S hS 𝒵
```

**`AlgebraicGeometry.Stack.isQuasiDMAbs_iff_isQuasiDMOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationSourceOverBase.lean, line 252](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationSourceOverBase.lean#L252). The attribute's comment: “part (2)”.

> **Stacks 050N, part (2).** An algebraic stack `𝒳` over `S` is quasi-DM **if and only if** it
> is quasi-DM over `S`.
>
> The same two halves as part (1), with local quasi-finiteness in place of unramifiedness:
> `AlgebraicGeometry.Stack.isQuasiDMOver_of_isQuasiDMAbs` above runs part (2) of **Stacks 050M**,
> and `AlgebraicGeometry.Stack.isQuasiDMAbs_of_isQuasiDMOver` runs part (6) of **Stacks 050L**
> against `AlgebraicGeometry.Stack.isQuasiDMOver_viewOverInt_schemeStack`. Neither direction
> carries a hypothesis the source does not have.

```lean
theorem isQuasiDMAbs_iff_isQuasiDMOver (𝒵 : AlgebraicStacks.{u, w} B S hS) :
    IsQuasiDMAbs.{u, w, w'} B S hS 𝒵 ↔ IsQuasiDMOver B S hS 𝒵
```

**`AlgebraicGeometry.Stack.isDM_of_isDMOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationSourceOverBase.lean, line 266](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationSourceOverBase.lean#L266). The attribute's comment: “part (5)”.

> **Stacks 050N, part (5).** If `𝒳` is DM over `S`, then every 1-morphism `f : 𝒳 ⟶ 𝒴` of
> algebraic stacks over `S` is DM.
>
> Being DM over `S` is DM-ness of the structure morphism of `𝒳` (**Stacks 050D**, part (1)), and
> that structure morphism is `f` followed by the structure morphism of `𝒴`
> (`AlgebraicGeometry.Stack.comp_structureMorphism`), so part (1) of **Stacks 050M**
> (`AlgebraicGeometry.Stack.AlgebraicStacks.isDM_of_comp`), which cancels the second factor of a
> DM composite with no hypothesis on it, gives the conclusion.

```lean
theorem isDM_of_isDMOver (f : 𝒳 ⟶ 𝒴) (h𝒳 : IsDMOver B S hS 𝒳) : IsDM B S hS f
```

**`AlgebraicGeometry.Stack.isQuasiDM_of_isQuasiDMOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationSourceOverBase.lean, line 277](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationSourceOverBase.lean#L277). The attribute's comment: “part (6)”.

> **Stacks 050N, part (6).** If `𝒳` is quasi-DM over `S`, then every 1-morphism `f : 𝒳 ⟶ 𝒴`
> of algebraic stacks over `S` is quasi-DM.
>
> The same argument as part (5), with part (2) of **Stacks 050M**
> (`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiDM_of_comp`) in place of part (1); it too needs
> no hypothesis on the second factor.

```lean
theorem isQuasiDM_of_isQuasiDMOver (f : 𝒳 ⟶ 𝒴) (h𝒳 : IsQuasiDMOver B S hS 𝒳) :
    AlgebraicStacks.IsQuasiDM B S hS f
```

**`AlgebraicGeometry.Stack.isSeparated_of_isSeparatedOver_of_isSeparated_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationSourceOverBase.lean, line 292](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationSourceOverBase.lean#L292). The attribute's comment: “part (7)”.

> **Stacks 050N, part (7).** If `𝒳` is separated over `S` and the relative diagonal `Δ_{𝒴/S}`
> is separated in the sense of Stacks 04XB, then every 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks
> over `S` is separated.
>
> The same argument as part (5), with part (3) of **Stacks 050M**
> (`AlgebraicGeometry.Stack.AlgebraicStacks.isSeparated_of_comp_of_isSeparated_diagonal`) in place
> of part (1). That part cancels the second factor of a separated composite provided the second
> factor has separated relative diagonal, and here the second factor is the structure morphism of
> `𝒴`, so the proviso is exactly the hypothesis `hΔ` that the source's part (7) carries too.

```lean
theorem isSeparated_of_isSeparatedOver_of_isSeparated_diagonal (f : 𝒳 ⟶ 𝒴)
    (h𝒳 : IsSeparatedOver B S hS 𝒳)
    (hΔ : IsSeparated.{u, u, u + 1} B S hS
      (relativeDiagonal.{u, u, u + 1} B S hS 𝒴.val
        (schemeStack.{u, w} B S hS (Over.mk (𝟙 (B.obj hS)))).val
        (structureMorphism B S hS 𝒴).hom)) :
    AlgebraicStacks.IsSeparated B S hS f
```

**`AlgebraicGeometry.Stack.isQuasiSeparated_of_isQuasiSeparatedOver_of_isQuasiSeparated_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationSourceOverBase.lean, line 311](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationSourceOverBase.lean#L311). The attribute's comment: “part (8)”.

> **Stacks 050N, part (8).** If `𝒳` is quasi-separated over `S` and the relative diagonal
> `Δ_{𝒴/S}` is quasi-separated in the sense of Stacks 04XB, then every 1-morphism `f : 𝒳 ⟶ 𝒴` of
> algebraic stacks over `S` is quasi-separated.
>
> The same argument as part (7), with part (4) of **Stacks 050M**
> (`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiSeparated_of_comp_of_isQuasiSeparated_diagonal`)
> in place of part (3); the hypothesis `hΔ` is again what that part needs of the second factor,
> which here is the structure morphism of `𝒴`.

```lean
theorem isQuasiSeparated_of_isQuasiSeparatedOver_of_isQuasiSeparated_diagonal (f : 𝒳 ⟶ 𝒴)
    (h𝒳 : IsQuasiSeparatedOver B S hS 𝒳)
    (hΔ : IsQuasiSeparated.{u, u, u + 1} B S hS
      (relativeDiagonal.{u, u, u + 1} B S hS 𝒴.val
        (schemeStack.{u, w} B S hS (Over.mk (𝟙 (B.obj hS)))).val
        (structureMorphism B S hS 𝒴).hom)) :
    AlgebraicStacks.IsQuasiSeparated B S hS f
```

## Tag 06MB, a lemma

[Tag 06MB](https://stacks.math.columbia.edu/tag/06MB) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isAbsolutelyDM_of_isUnramified_flatCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationFlatCoverDiagonal.lean, line 239](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationFlatCoverDiagonal.lean#L239). The attribute's comment: “part (1)”.

> **Stacks 06MB, part (1).** Let `𝒳` be an algebraic stack over `S` and let `f : 𝒲 ⟶ 𝒳` be
> surjective, flat and locally of finite presentation with `𝒲` representable by an algebraic space.
> If `f` is unramified in the relative sense of Stacks 03YK, then `𝒳` is Deligne–Mumford.
>
> Unramifiedness passes from `f` to the absolute diagonal of `𝒳` by
> `AlgebraicGeometry.Stack.hasRelativeProperty_diagonal_of_flatCover`, the cancellation of first
> factors being Stacks 06G6; the absolute diagonal and the relative diagonal of the structure
> 1-morphism have the same relative properties, and Stacks 050N part (1) turns DM over `S` into
> DM.

```lean
theorem isAbsolutelyDM_of_isUnramified_flatCover
    {𝒳 𝒲 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒲 ⟶ 𝒳)
    (h𝒲 : IsRepresentableByAlgebraicSpace B S hS 𝒲.val)
    (hSurj : IsSurjective B S hS f)
    (hFlat : IsFlat B S hS f)
    (hLfp : IsLocallyOfFinitePresentation B S hS f)
    (hUnr : haveI : (Space.unramifiedMorphismProperty B S hS).IsStableUnderBaseChange :=
        Space.isUnramified_isStableUnderBaseChange B S hS
      haveI : (Space.unramifiedMorphismProperty B S hS).IsLocalAtTarget
          (Space.Topology.fppf.precoverage.{u, u} B S hS) :=
        (Space.isUnramified_isLocalAtTarget_fpqc.{u, u} B S hS).of_le
          (Space.fppfPrecoverage_le_fpqcPrecoverage.{u, u} B S hS)
      HasRelativeProperty.{u, u, u + 1, u} B S hS (Space.unramifiedMorphismProperty B S hS)
        f.hom
        (isRepresentableByAlgebraicSpaces_of_isAlgebraicStack B S hS 𝒳.property h𝒲 f.hom)) :
    IsAbsolutelyDM.{u, w} B S hS hZ 𝒳
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isAbsolutelyQuasiDM_of_isLocallyQuasiFinite_flatCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationFlatCoverDiagonal.lean, line 278](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationFlatCoverDiagonal.lean#L278). The attribute's comment: “part (2)”.

> **Stacks 06MB, part (2).** Let `𝒳` be an algebraic stack over `S` and let `f : 𝒲 ⟶ 𝒳` be
> surjective, flat and locally of finite presentation with `𝒲` representable by an algebraic space.
> If `f` is locally quasi-finite in the relative sense of Stacks 03YK, then `𝒳` is quasi-DM.
>
> This is the argument of part (1) with the cancellation of first factors supplied by
> Stacks 03XN.

```lean
theorem isAbsolutelyQuasiDM_of_isLocallyQuasiFinite_flatCover
    {𝒳 𝒲 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒲 ⟶ 𝒳)
    (h𝒲 : IsRepresentableByAlgebraicSpace B S hS 𝒲.val)
    (hSurj : IsSurjective B S hS f)
    (hFlat : IsFlat B S hS f)
    (hLfp : IsLocallyOfFinitePresentation B S hS f)
    (hQf : haveI : (Space.locallyQuasiFiniteProperty B S hS).IsStableUnderBaseChange :=
        Space.isLocallyQuasiFinite_isStableUnderBaseChange B S hS
      HasRelativeProperty.{u, u, u + 1, u} B S hS
        (Space.locallyQuasiFiniteProperty B S hS) f.hom
        (isRepresentableByAlgebraicSpaces_of_isAlgebraicStack B S hS 𝒳.property h𝒲 f.hom)) :
    IsAbsolutelyQuasiDM.{u, w} B S hS hZ 𝒳
```

## Tag 06MY, a lemma

[Tag 06MY](https://stacks.math.columbia.edu/tag/06MY) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isDM_of_isMonomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/MonomorphismDeligneMumford.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/MonomorphismDeligneMumford.lean#L109). The attribute's comment: “monomorphisms are DM”.

> **Stacks 06MY, the Deligne–Mumford assertion for monomorphisms.** A monomorphism of
> algebraic stacks over `S` is Deligne–Mumford.
>
> A monomorphism is representable by algebraic spaces — the first conjunct of
> `AlgebraicGeometry.Stack.AlgebraicStacks.IsMonomorphism`, Stacks 04ZW — and a 1-morphism
> representable by algebraic spaces is Deligne–Mumford, so the monomorphism condition on the
> represented base changes is not needed. The source argues instead that the relative diagonal of a
> monomorphism is an isomorphism and that an isomorphism of algebraic spaces is unramified; the
> route taken here reaches the same conclusion from less.

```lean
theorem isDM_of_isMonomorphism (f : 𝒵 ⟶ 𝒳) (hf : IsMonomorphism B S hS f) :
    Stack.IsDM B S hS f
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isSeparated_of_isMonomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/MonomorphismDeligneMumford.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/MonomorphismDeligneMumford.lean#L131). The attribute's comment: “monomorphisms are separated”.

> **Stacks 06MY, the separatedness assertion for monomorphisms.** A monomorphism of algebraic
> stacks over `S` is separated.
>
> Every algebraic space representing a base change of a monomorphism has monomorphic structural
> morphism, so that morphism is a monomorphism of presheaves (Stacks 042M) and hence separated
> (Stacks 042N); so the monomorphism is separated in the relative sense of Stacks 04XB, and its
> relative diagonal is therefore proper by Stacks 04YS.
>
> The source argues instead that the relative diagonal of a monomorphism is an isomorphism and that
> an isomorphism of algebraic spaces is proper; the route taken here reaches the same conclusion
> without that comparison.

```lean
theorem isSeparated_of_isMonomorphism (f : 𝒵 ⟶ 𝒳) (hf : IsMonomorphism B S hS f) :
    IsSeparated B S hS f
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isSeparated_of_isImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/MonomorphismDeligneMumford.lean, line 151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/MonomorphismDeligneMumford.lean#L151). The attribute's comment: “immersions are separated”.

> **Stacks 06MY, the separatedness assertion for immersions.** An immersion of algebraic stacks
> over `S` is separated.
>
> An immersion is a monomorphism by Stacks 0504, so this is
> `AlgebraicGeometry.Stack.AlgebraicStacks.isSeparated_of_isMonomorphism`. This is the reduction the
> source makes when it says that the same is true for immersions.

```lean
theorem isSeparated_of_isImmersion (j : 𝒵 ⟶ 𝒳) (hj : IsImmersion B S hS j) :
    IsSeparated B S hS j
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isDM_of_isImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UnramifiedImmersionAlgebraicStack.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/UnramifiedImmersionAlgebraicStack.lean#L92). The attribute's comment: “immersions are DM”.

> **Stacks 06MY, the Deligne–Mumford assertion for immersions.** An immersion of algebraic
> stacks over `S` is Deligne–Mumford.
>
> An immersion is representable by algebraic spaces — the first conjunct of Stacks 04YL, part (3) —
> and a 1-morphism representable by algebraic spaces is Deligne–Mumford, so the immersion condition
> on the represented base changes is not needed. The source reduces the assertion to the
> monomorphism case, an immersion being a monomorphism by Stacks 0504; the route taken here reaches
> the same conclusion from less. The separatedness assertion of Stacks 06MY for immersions, which
> does use the immersion condition, is
> `AlgebraicGeometry.Stack.AlgebraicStacks.isSeparated_of_isImmersion`.

```lean
theorem isDM_of_isImmersion (j : 𝒵 ⟶ 𝒳) (hj : IsImmersion B S hS j) : Stack.IsDM B S hS j
```

## Tag 06MZ, a lemma

[Tag 06MZ](https://stacks.math.columbia.edu/tag/06MZ) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isAbsolutelyDM_of_isMonomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/MonomorphismDeligneMumford.lean, line 165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/MonomorphismDeligneMumford.lean#L165). The attribute's comment: “DM case”.

> **Stacks 06MZ, the Deligne–Mumford clause.** The source of a monomorphism into a
> Deligne–Mumford algebraic stack is Deligne–Mumford.
>
> The monomorphism is a Deligne–Mumford 1-morphism by Stacks 06MY, so part (5) of Stacks 050L
> applies to it. The statement is made at an arbitrary monomorphism, which is the form in which
> Stacks 06MZ's own proof uses it; see the implementation notes.

```lean
theorem isAbsolutelyDM_of_isMonomorphism (f : 𝒵 ⟶ 𝒳) (hf : IsMonomorphism B S hS f)
    (h𝒳 : IsAbsolutelyDM B S hS hZ 𝒳) :
    IsAbsolutelyDM B S hS hZ 𝒵
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isAbsolutelyQuasiDM_of_isMonomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/MonomorphismDeligneMumford.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/MonomorphismDeligneMumford.lean#L177). The attribute's comment: “quasi-DM case”.

> **Stacks 06MZ, the quasi-Deligne–Mumford clause.** The source of a monomorphism into a
> quasi-Deligne–Mumford algebraic stack is quasi-Deligne–Mumford.
>
> The quasi-Deligne–Mumford counterpart of
> `AlgebraicGeometry.Stack.AlgebraicStacks.isAbsolutelyDM_of_isMonomorphism`, through part (6) of
> Stacks 050L.

```lean
theorem isAbsolutelyQuasiDM_of_isMonomorphism (f : 𝒵 ⟶ 𝒳) (hf : IsMonomorphism B S hS f)
    (h𝒳 : IsAbsolutelyQuasiDM B S hS hZ 𝒳) :
    IsAbsolutelyQuasiDM B S hS hZ 𝒵
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isAbsolutelySeparated_of_isMonomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/MonomorphismDeligneMumford.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/MonomorphismDeligneMumford.lean#L189). The attribute's comment: “separated case”.

> **Stacks 06MZ, the separatedness clause.** The source of a monomorphism into a separated
> algebraic stack is separated.
>
> The monomorphism is a separated 1-morphism by Stacks 06MY, so part (7) of Stacks 050L applies to
> it.

```lean
theorem isAbsolutelySeparated_of_isMonomorphism (f : 𝒵 ⟶ 𝒳) (hf : IsMonomorphism B S hS f)
    (h𝒳 : IsAbsolutelySeparated B S hS hZ 𝒳) :
    IsAbsolutelySeparated B S hS hZ 𝒵
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isAbsolutelyQuasiSeparated_of_isMonomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/MonomorphismDeligneMumford.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/MonomorphismDeligneMumford.lean#L202). The attribute's comment: “quasi-separated case”.

> **Stacks 06MZ, the quasi-separatedness clause.** The source of a monomorphism into a
> quasi-separated algebraic stack is quasi-separated.
>
> The quasi-separated counterpart of
> `AlgebraicGeometry.Stack.AlgebraicStacks.isAbsolutelySeparated_of_isMonomorphism`, through part
> (8) of Stacks 050L.

```lean
theorem isAbsolutelyQuasiSeparated_of_isMonomorphism (f : 𝒵 ⟶ 𝒳)
    (hf : IsMonomorphism B S hS f) (h𝒳 : IsAbsolutelyQuasiSeparated B S hS hZ 𝒳) :
    IsAbsolutelyQuasiSeparated B S hS hZ 𝒵
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.4, Tag 04YV](https://stacks.math.columbia.edu/tag/04YV)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
