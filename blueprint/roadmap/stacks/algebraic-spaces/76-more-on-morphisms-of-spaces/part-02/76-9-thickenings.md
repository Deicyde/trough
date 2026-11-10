---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_sieve_isNilpotent_of_mem_definingIdealAt, AlgebraicGeometry.Space.thickeningHom_structureSharp_compatible, AlgebraicGeometry.Space.exists_idealPow_firstOrderThickening_filtration, AlgebraicGeometry.Space.isLocallySurjective_structureSharpInverseImage, AlgebraicGeometry.Space.isIntegralHom_universallyInjective_isSurjective_ι_of_isThickening, AlgebraicGeometry.Space.IsThickening, AlgebraicGeometry.Space.IsMorphismOfThickenings, AlgebraicGeometry.Space.IsThickeningOver
statement: formalized
proof: formalized
---

# 76.9 Thickenings

Section 76.9 of the Stacks Project, [Tag 05ZJ](https://stacks.math.columbia.edu/tag/05ZJ). 13 tags here are carried by 60 declarations of the repository (all in StacksFrontier) and 8 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05ZJ, the section

[Tag 05ZJ](https://stacks.math.columbia.edu/tag/05ZJ) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_sieve_isNilpotent_of_mem_definingIdealAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/LocallyNilpotentIdeal.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/LocallyNilpotentIdeal.lean#L72). The attribute's comment: “any local section of the kernel I = Ker(i\_X^#) of a thickening i\_X : X -> X' is locally nilpotent (the paragraph after Lemma 05ZP), on the small etale site of X'”.

> **Section 05ZJ: the ideal of a thickening is locally nilpotent.** Let `G ⊂ X` be a
> thickening of algebraic spaces over `S`, with ideal sheaf `𝓘 = Ker(i^♯) ⊆ 𝒪_X` on the small
> étale site of `X`.  Every local section `s` of `𝓘`, over an arbitrary étale chart `U` of `X`, is
> locally nilpotent: there is a covering sieve of `U` along each of whose arrows the restriction of
> `s` is nilpotent.
>
> The covering sieve is that of the arrows factoring through an affine étale chart, which covers
> by Stacks 04JS; on an affine chart the section is nilpotent by
> `AlgebraicGeometry.Space.isNilpotent_of_mem_definingIdealAt_of_isThickening`.

```lean
theorem exists_sieve_isNilpotent_of_mem_definingIdealAt (hG : IsThickening B S hS X G)
    (U : SmallEtale B S hS X.1)
    (s : ToType ((structureRingSheaf B S hS X).obj.obj (op U)))
    (hs : s ∈ definingIdealAt B S hS X ⟨G, hG.1⟩ (op U)) :
    ∃ T : Sieve U, T ∈ SmallEtale.topology B S hS X.1 U ∧
      ∀ (V : SmallEtale B S hS X.1) (m : V ⟶ U), T m →
        IsNilpotent (((structureRingSheaf B S hS X).obj.map m.op).hom s)
```

**`AlgebraicGeometry.Space.thickeningHom_structureSharp_compatible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/MorphismStructureSquare.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/MorphismStructureSquare.lean#L95). The attribute's comment: “the paragraph on a morphism (f, f') : (X ⊂ X') -> (Y ⊂ Y') of thickenings over B: the vertical arrows of the square of etale topoi are equivalences, and (f')^# : f^\{-1}O\_\{Y'} -> O\_\{X'} is a map of O\_B-algebras fitting into the commutative square with f^#, i\_X^# and i\_Y^#, read as 2-isomorphisms of morphisms of small etale ringed topoi (the form of the hypotheses of Lemma 05ZN); (f')\_small is moreover locally ringed”.

> **Section 05ZJ: the structure map of a morphism of thickenings over a base.** Let
> `G ⊂ X'` and `H ⊂ Y'` be thickenings of algebraic spaces over `T` (structure morphisms `pX'`,
> `pY'`), and let `(f, f')` be a morphism of thickenings over `T`: `f : G ⟶ H`, `f' : X' ⟶ Y'`,
> `f' ∘ i_X = i_Y ∘ f` and `pY' ∘ f' = pX'`.  Then
>
> 1. the direct images along `i_X` and `i_Y` of the small étale topoi are equivalences (the
>    vertical arrows of the source's square of topoi);
> 2. `(f')_small` is a morphism of locally ringed topoi;
> 3. `(f')^♯` fits into the source's commuting square with `f^♯`, `i_X^♯` and `i_Y^♯`:
>    `(f')_small ∘ (i_X)_small` is 2-isomorphic to `(i_Y ∘ f)_small`;
> 4. `(f')^♯` is a map of `𝒪_T`-algebras: `(p_{Y'})_small ∘ (f')_small` is 2-isomorphic to
>    `(p_{X'})_small`.
>
> Clauses 3 and 4 are the hypotheses `hsquare` and `halgebra`, and clause 2 the hypothesis
> `hlocal`, of `AlgebraicGeometry.Space.existsUnique_thickeningHom_of_isLocallyRinged` at
> `Φ = (f')_small`.

```lean
theorem thickeningHom_structureSharp_compatible (hG : IsThickening B S hS X' G)
    (hH : IsThickening B S hS Y' H) (pX' : X' ⟶ T) (pY' : Y' ⟶ T)
    (f : IsThickening.space B S hS hG ⟶ IsThickening.space B S hS hH) (f' : X' ⟶ Y')
    (hsq : IsThickening.inclusion B S hS hG ≫ f' = f ≫ IsThickening.inclusion B S hS hH)
    (hT : f' ≫ pY' = pX') :
    (smallToposMorphismTypeU B S hS
        (IsThickening.inclusion B S hS hG)).pushforward.IsEquivalence ∧
      (smallToposMorphismTypeU B S hS
        (IsThickening.inclusion B S hS hH)).pushforward.IsEquivalence ∧
      (smallEtaleRingedToposHom B S hS f').IsLocallyRinged ∧
      Nonempty (SmallEtaleTwoIso B S hS
        (smallEtaleComp B S hS (smallEtaleRingedToposHom B S hS f')
          (smallEtaleRingedToposHom B S hS (IsThickening.inclusion B S hS hG)))
        (smallEtaleRingedToposHom B S hS (f ≫ IsThickening.inclusion B S hS hH))) ∧
      Nonempty (SmallEtaleTwoIso B S hS
        (smallEtaleComp B S hS (smallEtaleRingedToposHom B S hS pY')
          (smallEtaleRingedToposHom B S hS f'))
        (smallEtaleRingedToposHom B S hS pX'))
```

**`AlgebraicGeometry.Space.exists_idealPow_firstOrderThickening_filtration`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/OrderFiltration.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/OrderFiltration.lean#L201). The attribute's comment: “the paragraph after Lemma 05ZP: for an nth order thickening X ⊂ X' with ideal I, the filtration 0 = I^\{n+1} ⊂ I^n ⊂ ... ⊂ I ⊂ O\_\{X'} gives closed subspaces X = X\_0 ⊂ X\_1 ⊂ ... ⊂ X\_n = X', X\_k cut out by I^\{k+1}, with each X\_k ⊂ X\_\{k+1} a first order thickening (the source's X\_\{n+1} = X' is a misprint for X\_n = X')”.

> **Section 05ZJ: an `n`th order thickening is filtered by first order thickenings.** Let
> `X ⊂ X'` be an `n`th order thickening of algebraic spaces over `S`, with quasi-coherent ideal
> sheaf `𝓘 ⊆ 𝒪_{X'}`.  There are closed subspaces `X_0, X_1, …` of `X'`, the `k`th one cut out by
> `𝓘^{k+1}` (so the filtration `0 = 𝓘^{n+1} ⊂ 𝓘^n ⊂ ⋯ ⊂ 𝓘 ⊂ 𝒪_{X'}` is that of their ideal
> sheaves), with `X = X_0 ⊂ X_1 ⊂ ⋯ ⊂ X_n = X'`, such that every `X_k ⊂ X_{k+1}` is a first order
> thickening.

```lean
theorem exists_idealPow_firstOrderThickening_filtration {n : ℕ} {G : Subfunctor X.1}
    (hG : IsNthOrderThickening B S hS n X G) :
    ∃ Xs : ℕ → ClosedSubspaces B S hS X.1,
      (Xs 0).1 = G ∧ (Xs n).1 = ⊤ ∧ Monotone (fun k => (Xs k).1) ∧
      (∀ k, definingIdealSheaf B S hS X (Xs k) =
        idealPowSubmodule (definingIdealSheaf B S hS X ⟨G, hG.1.1⟩) (k + 1)
          (SheafOfModules.unit (structureRingSheaf B S hS X))) ∧
      ∀ k, IsFirstOrderThickening B S hS ⟨(Xs (k + 1)).1.toFunctor, (Xs (k + 1)).2.1⟩
        ((Xs k).1.preimage (Xs (k + 1)).1.ι)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.isLocallySurjective_structureSharpInverseImage`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionStructureSharpInverseImage.lean#L145), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/LocallyNilpotentIdeal.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/LocallyNilpotentIdeal.lean#L96) (StacksFrontier): “the sentence after Equation 05ZM: the closed immersion i\_X : X -> X' corresponds to the surjective map i\_X^# : O\_\{X'} -> O\_X, read on the small etale site of X as i\_X^\{-1}O\_\{X'} -> O\_X (stated for every closed immersion)”.
- [`AlgebraicGeometry.Space.isIntegralHom_universallyInjective_isSurjective_ι_of_isThickening`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/EtaleSite.lean#L127), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/MorphismStructureSquare.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/MorphismStructureSquare.lean#L121) (StacksFrontier): “the sentence opening 'The fundamental equivalence': if X ⊂ X' is a thickening, then X -> X' is integral and universally bijective (universally injective and surjective)”.

## Tag 05ZK, a definition

[Tag 05ZK](https://stacks.math.columbia.edu/tag/05ZK) in the Stacks Project.

**`AlgebraicGeometry.Space.IsThickening`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings.lean#L95). The attribute's comment: “part (1): thickening”.

> **Stacks 05ZK, part (1).** A closed subspace `G` of an algebraic space `X` over `S` is a
> *thickening* of `X` when the two have the same associated topological space, i.e. when the
> map on points induced by the closed immersion `G.ι` is surjective.

```lean
abbrev IsThickening (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (X : AlgebraicSpaces B S hS) (G : Subfunctor X.1) : Prop
```

**`AlgebraicGeometry.Space.IsMorphismOfThickenings`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings.lean#L126). The attribute's comment: “part (5): morphism of thickenings”.

> **Stacks 05ZK, part (5).** Given two thickenings `G ⊂ X'` and `H ⊂ Y'` of algebraic spaces
> over `S`, a *morphism of thickenings* is a morphism `f' : X' ⟶ Y'` with `f'(G) ⊂ H`, i.e. one
> whose restriction to `G` factors through the closed subspace `H`.
>
> The restriction `f = f'|_G : G ⟶ H` is
> `AlgebraicGeometry.Space.IsMorphismOfThickenings.restrict`, and the pair `(f, f')` is what the
> source calls the morphism of thickenings `(G ⊂ X') → (H ⊂ Y')`.

```lean
abbrev IsMorphismOfThickenings {X' Y' : AlgebraicSpaces B S hS} (G : Subfunctor X'.1)
    (H : Subfunctor Y'.1) (f' : X' ⟶ Y') : Prop
```

**`AlgebraicGeometry.Space.IsThickeningOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings.lean#L190). The attribute's comment: “part (6): thickening over a base”.

> **Stacks 05ZK, part (6).** A *thickening over* an algebraic space `Z`: a thickening
> `G ⊂ X'` of algebraic spaces over `S` together with structure morphisms `a' : X' ⟶ Z` of the
> ambient space and `a : G ⟶ Z` of the subspace, such that the closed immersion `G ⟶ X'` is a
> morphism over `Z`.

```lean
abbrev IsThickeningOver (Z : AlgebraicSpaces B S hS) {X' : AlgebraicSpaces B S hS}
    (G : Subfunctor X'.1) (a : G.toFunctor ⟶ Z.1) (a' : X' ⟶ Z) : Prop
```

**`AlgebraicGeometry.Space.IsMorphismOfThickeningsOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings.lean#L198). The attribute's comment: “part (6): morphism of thickenings over a base”.

> **Stacks 05ZK, part (6).** A *morphism of thickenings over* an algebraic space `Z`: two
> thickenings over `Z` and a morphism of thickenings between them which is a morphism over
> `Z`.

```lean
abbrev IsMorphismOfThickeningsOver (Z : AlgebraicSpaces B S hS)
    {X' Y' : AlgebraicSpaces B S hS} (G : Subfunctor X'.1) (H : Subfunctor Y'.1)
    (a : G.toFunctor ⟶ Z.1) (a' : X' ⟶ Z) (b : H.toFunctor ⟶ Z.1) (b' : Y' ⟶ Z)
    (f' : X' ⟶ Y') : Prop
```

**`AlgebraicGeometry.Space.isThickening_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/LiftDifferenceUndeformedTarget.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/LiftDifferenceUndeformedTarget.lean#L71). The attribute's comment: “part (1): an algebraic space is a thickening of itself”.

> An algebraic space is a thickening of itself: its top closed subspace.

```lean
theorem isThickening_top (Y : AlgebraicSpaces B S hS) : IsThickening B S hS Y ⊤
```

**`AlgebraicGeometry.Space.IsNthOrderThickening`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/Order.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/Order.lean#L127). The attribute's comment: “part (4): nth-order thickening”.

> **Stacks 05ZK, part (4).** A closed subspace `G` of an algebraic space `X` over `S` is an
> *`n`th-order thickening* when the `(n+1)`st power of its defining ideal vanishes on every
> object of the small étale site of `X`.

```lean
abbrev IsNthOrderThickening (n : ℕ) (X : AlgebraicSpaces B S hS) (G : Subfunctor X.1) : Prop
```

**`AlgebraicGeometry.Space.IsFirstOrderThickening`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/Order.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/Order.lean#L135). The attribute's comment: “part (2): first-order thickening”.

> **Stacks 05ZK, part (2).** A closed subspace `G` of an algebraic space `X` over `S` is a
> *first-order thickening* when its defining ideal has square zero on every object of the small
> étale site of `X`.

```lean
abbrev IsFirstOrderThickening (X : AlgebraicSpaces B S hS) (G : Subfunctor X.1) : Prop
```

**`AlgebraicGeometry.Space.IsFiniteOrderThickening`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/Order.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/Order.lean#L142). The attribute's comment: “part (3): finite-order thickening”.

> **Stacks 05ZK, part (3).** A closed subspace `G` of an algebraic space `X` over `S` is a
> *finite-order thickening* when its defining ideal is nilpotent, with one exponent valid on
> every object of the small étale site of `X`.

```lean
abbrev IsFiniteOrderThickening (X : AlgebraicSpaces B S hS) (G : Subfunctor X.1) : Prop
```

Declarations registered for the tag:

- [`CategoryTheory.Arrow.Hom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Arrow.Hom#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings.lean#L100) (StacksFrontier): “parts (5) and (6): morphisms of thickenings, also over a base”.

## Tag 05ZL, an equation

[Tag 05ZL](https://stacks.math.columbia.edu/tag/05ZL) in the Stacks Project.

**`AlgebraicGeometry.Space.isIntegralHom_universallyInjective_isSurjective_ι_of_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/EtaleSite.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/EtaleSite.lean#L127). The attribute's comment: “the inclusion of a thickening is integral, universally injective and surjective”.

> **Stacks 05ZL.** The inclusion of a thickening of an algebraic space over `S` is integral,
> universally injective and surjective.

```lean
theorem isIntegralHom_universallyInjective_isSurjective_ι_of_isThickening
    (hG : IsThickening B S hS X G) :
    IsIntegralHom B S hS G.ι ∧ UniversallyInjective B S hS G.ι ∧ IsSurjective B S hS G.ι
```

**`AlgebraicGeometry.Space.spacesEtaleAbelianSheafEquiv_of_isThickening`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/EtaleToposAbelian.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/EtaleToposAbelian.lean#L101). The attribute's comment: “the identification of the two spaces-etale topoi, at sheaves of abelian groups”.

> **Equation [Stacks Project, Tag 05ZL] for sheaves of abelian groups.**  For a thickening
> `G ⊂ X` of algebraic spaces over `S`, the sheaves of abelian groups on the spaces-étale site of
> `X` and those on the spaces-étale site of `G` are canonically equivalent.
>
> The equivalence is the chart form
> `AlgebraicGeometry.Space.smallEtaleAbelianSheafEquiv_of_isThickening` conjugated by the two
> comparison equivalences of [Stacks Project, Tag 03G1], exactly as the set-valued
> `AlgebraicGeometry.Space.spacesEtaleSheafEquiv_of_isThickening` is.

```lean
noncomputable def spacesEtaleAbelianSheafEquiv_of_isThickening (hG : IsThickening B S hS X G) :
    Sheaf (SpacesEtale.topology B S hS X) AddCommGrpCat.{u + 1} ≌
      Sheaf (SpacesEtale.topology B S hS (IsThickening.space B S hS hG))
        AddCommGrpCat.{u + 1}
```

**`AlgebraicGeometry.Space.mem_spacesEtaleTopology_iff_functorPushforward_of_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleCovering.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleCovering.lean#L121). The attribute's comment: “identification of the covering sieves of the two spaces-étale sites”.

> **Stacks 05ZL.** Base change along the inclusion of a thickening `G ⊂ X` identifies the
> covering sieves of the spaces-étale site of `X` with those of the spaces-étale site of `G`: a
> sieve of an object `U` is covering exactly when the sieve it generates on the base change of
> `U` is covering.

```lean
theorem mem_spacesEtaleTopology_iff_functorPushforward_of_isThickening
    {X : AlgebraicSpaces B S hS} {G : Subfunctor X.1} (hG : IsThickening B S hS X G)
    (U : SpacesEtale B S hS X) (R : Sieve U) :
    R ∈ SpacesEtale.topology B S hS X U ↔
      R.functorPushforward
          (spacesBaseChange B S hS (IsThickening.inclusion B S hS hG)).functor ∈
        SpacesEtale.topology B S hS (IsThickening.space B S hS hG)
          ((spacesBaseChange B S hS (IsThickening.inclusion B S hS hG)).functor.obj U)
```

**`AlgebraicGeometry.Space.spacesEtaleEquivalenceOfIsThickening`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleEquivalence.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleEquivalence.lean#L152). The attribute's comment: “the identification of the two spaces-étale sites of Stacks 03G0, as an equivalence of categories, for a thickening of arbitrary order”.

> Let `G ⊂ X` be a thickening of algebraic spaces over `S`, of arbitrary order. Base change
> along the inclusion, `V ↦ G ×_X V`, is an equivalence of categories from the spaces-étale site of
> the ambient space `X` to the spaces-étale site of the closed subspace `G`.

```lean
noncomputable def spacesEtaleEquivalenceOfIsThickening (hG : IsThickening B S hS X G) :
    SpacesEtale B S hS X ≌ SpacesEtale B S hS (IsThickening.space B S hS hG)
```

**`AlgebraicGeometry.Space.isEquivalence_spacesBaseChange_of_isClosedImmersion_of_isSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleEssSurj/LiftedEtalePresentation.lean, line 576](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleEssSurj/LiftedEtalePresentation.lean#L576). The attribute's comment: “the identification of the two spaces-étale sites: base change along the inclusion of a thickening of arbitrary order is an equivalence of categories”.

> Base change `V ↦ X ×_Y V` is an equivalence from the spaces-étale site of `Y` to that of `X`,
> for a surjective closed immersion `f`.

```lean
theorem isEquivalence_spacesBaseChange_of_isClosedImmersion_of_isSurjective (f : X ⟶ Y)
    (hci : IsClosedImmersion B S hS f.hom) (hsurj : IsSurjective B S hS f.hom) :
    (spacesBaseChange B S hS f).functor.IsEquivalence
```

## Tag 05ZM, an equation

[Tag 05ZM](https://stacks.math.columbia.edu/tag/05ZM) in the Stacks Project.

**`AlgebraicGeometry.Space.spacesEtaleRingSheafEquiv_of_isThickening`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/EtaleRingedTopos.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/EtaleRingedTopos.lean#L227). The attribute's comment: “the equivalence of the two spaces-étale topoi at sheaves of commutative rings, which is what carries the structure sheaf of the ambient space to the right hand side of the equation; neither pair is claimed to be a locally ringed topos”.

> **The fundamental equivalence of a thickening, at sheaves of rings.**  For a thickening
> `G ⊂ X` of algebraic spaces the sheaves of commutative rings on the spaces-étale site of `X`
> and those on the spaces-étale site of `G` are canonically equivalent.

```lean
def spacesEtaleRingSheafEquiv_of_isThickening (hG : IsThickening B S hS X G) :
    Sheaf (SpacesEtale.topology B S hS X) CommRingCat.{u + 1} ≌
      Sheaf (SpacesEtale.topology B S hS (IsThickening.space B S hS hG))
        CommRingCat.{u + 1}
```

**`AlgebraicGeometry.Space.thickeningStructureSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/EtaleRingedTopos.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/EtaleRingedTopos.lean#L246). The attribute's comment: “the sheaf of rings O\_\{X'} of the right hand side of the equation, the structure sheaf of the ambient space read on the spaces-étale site of the thickening”.

> **The structure sheaf of the ambient space, on the site of the thickening.**  For a
> thickening `G ⊂ X` this is `𝒪_X` carried through the equivalence of the two spaces-étale
> topoi, the sheaf of rings of the right hand side of the fundamental equivalence.

```lean
def thickeningStructureSheaf (hG : IsThickening B S hS X G) :
    Sheaf (SpacesEtale.topology B S hS (IsThickening.space B S hS hG)) CommRingCat.{u + 1}
```

**`AlgebraicGeometry.Space.thickeningInverseImageRingedTopos`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/EtaleRingedTopos.lean, line 323](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/EtaleRingedTopos.lean#L323). The attribute's comment: “the right hand pair of the equation, in the presentation of scheme charts and with the structure sheaf of the ambient space read on the smaller site as its inverse image”.

> **The right hand side `(Sh(G_étale), 𝒪_X)` of the fundamental equivalence of a thickening.**
> The small étale site of scheme charts of the closed subspace `G` of a thickening `G ⊂ X`,
> equipped with the structure sheaf of the *ambient* space `X` read on it as the inverse image
> `i^{-1}𝒪_X` along the inclusion.
>
> This is the inverse-image ringed topos of Stacks 04KR at the morphism of small étale topoi of the
> inclusion.  Its structure sheaf is not `𝒪_G`: the two are related by the surjection
> `i^♯ : i^{-1}𝒪_X ⟶ 𝒪_G`, whose kernel is the conormal module of the thickening when the
> thickening is of first order.

```lean
abbrev thickeningInverseImageRingedTopos (hG : IsThickening B S hS X G) :
    RingedTopos.{u, u + 1, u}
```

**`AlgebraicGeometry.Space.thickeningFundamentalHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/EtaleRingedTopos.lean, line 345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/EtaleRingedTopos.lean#L345). The attribute's comment: “the canonical morphism between the two pairs of the equation, in the presentation of scheme charts: its geometric morphism is the direct image along the inclusion, and its structure map is the unit of the adjunction at the ambient structure sheaf”.

> **The canonical morphism of the fundamental equivalence of a thickening.**  Its underlying
> geometric morphism is the direct image along the inclusion `i : G ⟶ X`, and its structure map is
> the unit `𝒪_X ⟶ i_*i^{-1}𝒪_X` of the adjunction `i^{-1} ⊣ i_*` on sheaves of commutative rings.
>
> Both of the equation's claims about it are below:
> `AlgebraicGeometry.Space.isIso_thickeningFundamentalHom_fSharp` is that the structure map is an
> isomorphism, and `AlgebraicGeometry.Space.isEquivalence_smallEtalePushforward_of_isThickening` is
> that the geometric morphism is an equivalence — the latter is stated at the geometric morphism
> itself, which is this morphism's `toToposHom` by
> `AlgebraicGeometry.inverseImageRingedToposHom_toToposHom`, so it supplies that instance after an
> ascription at this spelling, as in
> `AlgebraicGeometry.Space.thickeningFundamentalHomInverse` below.

```lean
def thickeningFundamentalHom (hG : IsThickening B S hS X G) :
    RingedToposHom (thickeningInverseImageRingedTopos B S hS hG)
      (smallEtaleRingedTopos B S hS X)
```

**`AlgebraicGeometry.Space.isIso_thickeningFundamentalHom_fSharp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/EtaleRingedTopos.lean, line 365](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/EtaleRingedTopos.lean#L365). The attribute's comment: “the structure-sheaf half: the structure map of the canonical morphism between the two pairs is an isomorphism, so both pairs carry the structure sheaf of the ambient space”.

> **The structure-sheaf half of Stacks 05ZM.**  The structure map of the canonical morphism —
> the unit `𝒪_X ⟶ i_*i^{-1}𝒪_X` at the structure sheaf of the ambient space of a thickening — is an
> isomorphism of sheaves of commutative rings.  So the two pairs of the equation carry one and the
> same structure sheaf, and not merely equivalent topoi.
>
> The direct image of sheaves of sets along the inclusion is fully faithful and essentially
> surjective, so the set-level unit is invertible at every sheaf; forgetting the ring operations
> carries the unit of the adjunction on sheaves of commutative rings to the set-level unit, and
> reflects isomorphisms.  The same statement for sheaves of not necessarily commutative rings is
> `AlgebraicGeometry.Space.isIso_ringUnit_of_isThickening`.

```lean
theorem isIso_thickeningFundamentalHom_fSharp (hG : IsThickening B S hS X G) :
    IsIso (thickeningFundamentalHom B S hS hG).fSharp
```

**`AlgebraicGeometry.Space.thickeningFundamentalHom_isLocallyRinged`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/EtaleRingedTopos.lean, line 404](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/EtaleRingedTopos.lean#L404). The attribute's comment: “that the canonical morphism between the two pairs is a morphism of LOCALLY ringed topoi, which is the clause the equation adds to the equivalence of the two topoi; that either pair is a locally ringed SITE is not claimed”.

> **The canonical morphism of the fundamental equivalence is a morphism of locally ringed
> topoi.**  This is the clause that makes the equation of Stacks 05ZM an equivalence of *locally*
> ringed topoi and not only of ringed topoi.
>
> It needs no hypothesis on the thickening: the inverse-image form of the structure map of the
> canonical morphism out of an inverse-image ringed topos is the identity, and a morphism of ringed
> topoi whose inverse-image structure map is invertible is locally ringed, which is the step
> Stacks 04H9 settles with the words "as it is an isomorphism this is clear".  The thickening
> hypothesis is what makes the morphism *invertible*, through
> `AlgebraicGeometry.Space.isIso_thickeningFundamentalHom_fSharp` and
> `AlgebraicGeometry.Space.isEquivalence_smallEtalePushforward_of_isThickening`.
>
> That the two ringed topoi are locally ringed *sites* is a different assertion, and is not
> claimed; see the implementation notes.

```lean
theorem thickeningFundamentalHom_isLocallyRinged (hG : IsThickening B S hS X G) :
    (thickeningFundamentalHom B S hS hG).IsLocallyRinged
```

**`AlgebraicGeometry.Space.thickeningFundamentalHomInverse`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/EtaleRingedTopos.lean, line 420](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/EtaleRingedTopos.lean#L420). The attribute's comment: “that the canonical morphism between the two pairs is invertible as a morphism of ringed topoi, which is the word equivalence in the equation”.

> **The inverse of the canonical morphism of the fundamental equivalence of a thickening.**  The
> geometric morphism is `i^{-1}` read as a direct image, and the structure map is the inverse of the
> inverse-image form `i^{-1}𝒪_X ⟶ i^{-1}𝒪_X` of the structure map of
> `AlgebraicGeometry.Space.thickeningFundamentalHom`.
>
> Its existence is the content of the word *equivalence* in the equation of Stacks 05ZM: the
> canonical morphism is invertible because its geometric morphism is an equivalence of topoi and its
> structure map is an isomorphism of sheaves of rings.

```lean
def thickeningFundamentalHomInverse (hG : IsThickening B S hS X G) :
    RingedToposHom (smallEtaleRingedTopos B S hS X)
      (thickeningInverseImageRingedTopos B S hS hG)
```

**`AlgebraicGeometry.Space.thickeningFundamentalHomInverse_isLocallyRinged`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/EtaleRingedTopos.lean, line 439](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/EtaleRingedTopos.lean#L439). The attribute's comment: “that the inverse of the canonical morphism is again a morphism of LOCALLY ringed topoi, so that the equation is an equivalence of locally ringed topoi in both directions”.

> **The inverse of the canonical morphism is again a morphism of locally ringed topoi.**
> Together with `AlgebraicGeometry.Space.thickeningFundamentalHom_isLocallyRinged` this is the
> equation of Stacks 05ZM in full: an invertible morphism of locally ringed topoi between the two
> pairs, in both directions.
>
> The inverse is an isomorphism of ringed topoi — its geometric morphism is the inverse image of an
> equivalence and its structure map is the inverse of an isomorphism — and an isomorphism of ringed
> topoi is locally ringed by Stacks 04H9.

```lean
theorem thickeningFundamentalHomInverse_isLocallyRinged (hG : IsThickening B S hS X G) :
    (thickeningFundamentalHomInverse B S hS hG).IsLocallyRinged
```

**`AlgebraicGeometry.Space.spacesEtaleSheafEquiv_of_isThickening`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/EtaleTopos.lean, line 303](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/EtaleTopos.lean#L303). The attribute's comment: “equivalence of the spaces-étale sheaf topoi”.

> **The equivalence of the spaces-étale sheaf topoi of a thickening.** For a thickening
> `G ⊂ X` of algebraic spaces over `S`, the sheaves of sets on the spaces-étale site of `X` and
> the sheaves of sets on the spaces-étale site of `G` are canonically equivalent.
>
> The equivalence is the chart form
> `AlgebraicGeometry.Space.smallEtaleSheafEquiv_of_isThickening` conjugated by the two comparison
> equivalences of Stacks 03G1, `AlgebraicGeometry.Space.comparisonFunctor_sheafEquivalence`, which
> identify the sheaves on the spaces-étale site of an algebraic space with the sheaves on its
> small étale site of scheme charts.

```lean
noncomputable def spacesEtaleSheafEquiv_of_isThickening (hG : IsThickening B S hS X G) :
    Sheaf (SpacesEtale.topology B S hS X) (Type (u + 1)) ≌
      Sheaf (SpacesEtale.topology B S hS (IsThickening.space B S hS hG)) (Type (u + 1))
```

**`AlgebraicGeometry.Space.fundamentalEquivalence_of_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/FundamentalEquivalence.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/FundamentalEquivalence.lean#L221).

> **Stacks 05ZM, equation 76.9.1.2.** Let `G ⊂ X` be a thickening of algebraic spaces over a
> scheme `S`; in the notation of the source `G` is `X` and `X` is `X'`. Then
>
> `(Sh(X'_{spaces,étale}), 𝒪_{X'}) ≅ (Sh(X_{spaces,étale}), 𝒪_{X'})`
>
> as locally ringed topoi, the right-hand structure sheaf being `𝒪_{X'}` transported along the
> equivalence of spaces-étale topoi. The isomorphism is the canonical morphism
> `AlgebraicGeometry.Space.spacesEtaleRingedToposHom_of_isThickening`, and the four conjuncts
> below are what make it one: its geometric morphism is an equivalence in both directions, its
> structure map is invertible, and it is a morphism of locally ringed topoi.

```lean
theorem fundamentalEquivalence_of_isThickening (hG : IsThickening B S hS X G) :
    Functor.IsEquivalence
        (spacesEtaleRingedToposHom_of_isThickening B S hS hG).toToposHom.pushforward ∧
      Functor.IsEquivalence
        (spacesEtaleRingedToposHom_of_isThickening B S hS hG).toToposHom.inverseImage ∧
      IsIso (spacesEtaleRingedToposHom_of_isThickening B S hS hG).fSharp ∧
      RingedToposHom.IsLocallyRinged
        (spacesEtaleRingedToposHom_of_isThickening B S hS hG)
```

**`AlgebraicGeometry.Space.structureRingSheafDirectImageIsoOfRestrictEq`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/StructureSheafEquivalence.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/StructureSheafEquivalence.lean#L325). The attribute's comment: “the structure sheaf transported across the equivalence of étale topoi of a thickening: the direct image of the structure sheaf of the ambient space depends only on the restriction of the morphism to the closed subspace”.

> **The structure-sheaf half of [Stacks Project, Tag 05ZM].**  Let `G ⊂ X'` be a thickening of
> algebraic spaces over `S`, with inclusion `i : X ⟶ X'`, and let `a', b' : X' ⟶ Y'` be two
> morphisms which agree on `X`.  Then the two direct images `(a')_*𝒪_{X'}` and `(b')_*𝒪_{X'}` of
> the structure sheaf of `X'` are canonically isomorphic as sheaves of rings on the small étale
> site of `Y'`.
>
> This is the sense in which the structure sheaf of `X'` is carried across the equivalence of
> étale topoi of the thickening: the direct image of `𝒪_{X'}` depends only on the restriction of
> the morphism to the closed subspace, because the direct image of sheaves of sets does and the
> ring operations are transported along it.
>
> It is what lets the structure maps `(a')^♯` and `(b')^♯` be compared, and so what
> [Stacks Project, Tag 0618] needs in order to speak of the difference of two lifts; see
> `AlgebraicGeometry.Space.structureSharpOfRestrictEq`.

```lean
noncomputable def structureRingSheafDirectImageIsoOfRestrictEq :
    structureRingSheafDirectImage B S hS a' ≅ structureRingSheafDirectImage B S hS b'
```

**`AlgebraicGeometry.Space.pushforwardCommRingFunctorIsoOfRestrictEq`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/StructureSheafEquivalence.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/StructureSheafEquivalence.lean#L337). The attribute's comment: “the structure sheaf transported across the equivalence of étale topoi of a thickening, for sheaves of commutative rings: the direct image functor of sheaves of commutative rings depends only on the restriction of the morphism to the closed subspace”.

> **The structure-sheaf half of [Stacks Project, Tag 05ZM] for sheaves of commutative
> rings.**  This is the spelling in which the structure map `fSharp` of
> `AlgebraicGeometry.Space.smallEtaleRingedToposHom` takes its values.

```lean
noncomputable def pushforwardCommRingFunctorIsoOfRestrictEq :
    pushforwardCommRingFunctor.{u, u, u, u + 1, u, u + 1}
        (smallToposMorphismTypeU B S hS a') ≅
      pushforwardCommRingFunctor.{u, u, u, u + 1, u, u + 1}
        (smallToposMorphismTypeU B S hS b')
```

**`AlgebraicGeometry.Space.isIso_ringUnit_of_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/StructureSheafRingUnit.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/StructureSheafRingUnit.lean#L187). The attribute's comment: “the structure-sheaf half, at the small étale sites: every sheaf of rings on the site of the ambient space — its structure sheaf in particular — is canonically the direct image along the inclusion of a sheaf of rings on the site of the thickening, which is the identification under which the two topoi carry one and the same structure sheaf”.

> **The unit `O ⟶ i_*i^{-1}O` of `i^{-1} ⊣ i_*` at a sheaf of rings is an isomorphism for the
> inclusion `i : Z ⟶ X` of a thickening.**  The direct image of sheaves of sets along `i` is fully
> faithful because `i` is a closed immersion and essentially surjective because `Z ⊂ X` is a
> thickening, so the set-level unit is invertible at every sheaf; and
> `CategoryTheory.sheafCompose _ (CategoryTheory.forget RingCat)` reflects isomorphisms.
>
> So every sheaf of rings on the small étale site of `X` is canonically the direct image of one
> on the small étale site of `Z`.  This is what lets the comorphisms of two morphisms agreeing on
> a thickening be read in one and the same sheaf of rings; see the module documentation.

```lean
theorem isIso_ringUnit_of_isThickening (hZ : IsThickening B S hS X Z.1)
    (O : Sheaf (SmallEtale.topology B S hS X.1) RingCat.{u}) :
    IsIso (ringUnit (smallToposMorphismTypeU B S hS (subspaceInclusion B S hS X Z)) O)
```

**`AlgebraicGeometry.Space.isIso_commRingUnit_of_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/StructureSheafRingUnit.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/StructureSheafRingUnit.lean#L226). The attribute's comment: “the structure-sheaf half at the coefficient category of a morphism of ringed topoi: the direct image along the inclusion identifies the sheaves of commutative rings on the site of the thickening with those on the site of the ambient space, carrying the inverse image of the structure sheaf of the ambient space to that structure sheaf”.

> **The unit of the adjunction of [Stacks Project, Tag 00YV] at a sheaf of *commutative* rings
> is an isomorphism for the inclusion `i : Z ⟶ X` of a thickening.**
>
> This is `AlgebraicGeometry.Space.isIso_ringUnit_of_isThickening` at the coefficient category in
> which `AlgebraicGeometry.RingedToposHom.fSharp` takes its values, and the proof is the same: the
> direct image of sheaves of sets along a thickening is fully faithful and essentially surjective,
> `Stacks.Sheaves.ToposPushforward.pushforwardCommRingFunctor_isEquivalence` carries that to the
> direct image of sheaves of commutative rings, and the unit of an adjunction whose right adjoint
> is an equivalence is an isomorphism.
>
> Stated at `CommRingCat` the identification applies to a morphism of ringed topoi: the
> invertibility of a structure map is the hypothesis `[IsIso f.fSharp]` of
> `AlgebraicGeometry.RingedToposHom.inverse`, and
> `AlgebraicGeometry.RingedToposHom.ofInverseImageIso` builds a morphism of ringed topoi out of a
> morphism of topoi together with an isomorphism of inverse-image structure sheaves.

```lean
theorem isIso_commRingUnit_of_isThickening (hZ : IsThickening B S hS X Z.1)
    (O : Sheaf (SmallEtale.topology B S hS X.1) CommRingCat.{u}) :
    IsIso ((commRingImageAdjunction
      (smallToposMorphismTypeU B S hS (subspaceInclusion B S hS X Z))).unit.app O)
```

**`AlgebraicGeometry.Space.smallEtaleCommRingSheafEquiv_of_isThickening`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/StructureSheafTransport.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/StructureSheafTransport.lean#L106). The attribute's comment: “equivalence of the small étale sheaves of commutative rings”.

> **Stacks 05ZM for sheaves of commutative rings.** For a thickening `G ⊂ X` of algebraic
> spaces over `S`, the sheaves of commutative rings on the small étale site of `X` and on the small
> étale site of `G` are equivalent, by restriction along base change of étale scheme charts.
>
> This is the comparison lemma for the dense subsite inclusion
> `AlgebraicGeometry.Space.thickeningChartBaseChange_isDenseSubsite`, instantiated at
> `CommRingCat.{u}` rather than at sheaves of sets; see the implementation notes for why that
> instantiation needs the essential smallness of the site.

```lean
noncomputable def smallEtaleCommRingSheafEquiv_of_isThickening (hG : IsThickening B S hS X G) :
    Sheaf (SmallEtale.topology B S hS X.1) CommRingCat.{u} ≌
      Sheaf (SmallEtale.topology B S hS (IsThickening.space B S hS hG).1) CommRingCat.{u}
```

## Tag 05ZN, a lemma

[Tag 05ZN](https://stacks.math.columbia.edu/tag/05ZN) in the Stacks Project.

**`AlgebraicGeometry.Space.eq_of_inducesCommonSmallEtaleRingedToposHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/MorphismFromStructureMap/RecoveryAndThickeningHom.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/MorphismFromStructureMap/RecoveryAndThickeningHom.lean#L270). The attribute's comment: “the uniqueness clause of the tag, unconditionally and in the generality in which it is true: at most one morphism `X' ⟶ Y'` of the ambient algebraic spaces over the base is 2-isomorphic to a given morphism of their small étale ringed topoi, so there is at most one morphism of thickenings `(f, f')` with `alpha = (f')^sharp`. This is the faithfulness half of 04KL over a base and it is PROVED, by 04M6; no thickening hypothesis and no 2-compatibility with the base is used”.

> **A morphism of algebraic spaces is determined by the morphism of small étale ringed topoi
> it induces.**  At most one morphism `P ⟶ Q` over `S` is 2-isomorphic to a given morphism `ψ` of
> the small étale ringed topoi.
>
> This is the faithfulness half of Stacks 04KL over a base, and it is **not** carried: it holds
> unconditionally, by Stacks 04M6,
> `AlgebraicGeometry.Space.eq_of_smallEtaleRingedToposHom_twoIso`, which says exactly that two
> morphisms of algebraic spaces over `S` with 2-isomorphic morphisms of small étale ringed topoi
> are equal.  The *existence* half of Stacks 04KL over a base is
> `AlgebraicGeometry.Space.IsRecoveredFromSmallEtale`, which is proved for every base scheme by
> `AlgebraicGeometry.Space.isRecoveredFromSmallEtale_holds`.
>
> Note that the 2-compatibility with structure morphisms to a base, which
> `AlgebraicGeometry.Space.IsRecoveredFromSmallEtale` cannot do without, and the hypothesis on the
> base scheme, which its proof cannot do without, are not needed here: the
> counterexample recorded in that definition's docstring is a `ψ` induced by *no* morphism over
> `S`, not by two.

```lean
theorem eq_of_inducesCommonSmallEtaleRingedToposHom {P Q : AlgebraicSpaces B S hS}
    {ψ : RingedToposHom (smallEtaleRingedTopos B S hS P) (smallEtaleRingedTopos B S hS Q)}
    (k₁ k₂ : P ⟶ Q) (h₁ : InducesSmallEtaleRingedToposHom B S hS k₁ ψ)
    (h₂ : InducesSmallEtaleRingedToposHom B S hS k₂ ψ) :
    k₁ = k₂
```

**`AlgebraicGeometry.Space.existsUnique_thickeningHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/MorphismFromStructureMap/RecoveryAndThickeningHom.lean, line 538](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/MorphismFromStructureMap/RecoveryAndThickeningHom.lean#L538). The attribute's comment: “over a base SCHEME whose canonical morphism to the spectrum of its global functions is a monomorphism -- an affine base, a quasi-affine base, any base which embeds in an affine scheme: that the recovered morphism is a morphism of thickenings over the base and that the pair is unique. The source states the tag over an arbitrary base and ends `we omit the verification that f-prime is a morphism over B`; the existence of the morphism recovering a locally ringed morphism of the small etale ringed topoi over the base -- 04KL over a base -- is what that verification amounts to, and it is PROVED here for such a base scheme, by `isRecoveredFromSmallEtale_of_mono_toSpecGamma`. That hypothesis is the exact reach of the route, being equivalent to the assertion that a morphism of schemes into the base is determined by its ring map on global functions, which is all the chart construction of 04KL produces. So this clause is unconditional for those base schemes only, and is NOT the tag in the generality the source states it in. The locally ringed condition on (f\_spaces,etale, alpha) is derived from the commuting square, not assumed, and the uniqueness of the pair and the two equations are derived from the faithfulness half of 04KL over a base, which is PROVED for every base -- see `eq_of_inducesCommonSmallEtaleRingedToposHom`, from 04M6”.

> **Stacks 05ZN over a base scheme determined by its global functions.**  Let
> `G ⊂ X'` and `H ⊂ Y'` be thickenings of algebraic spaces over `T`, let `f : X ⟶ Y` be a
> morphism of the two closed subspaces, and let `Φ = (f_{spaces,étale}, α)` be a morphism of the
> small étale ringed topoi of `X'` and `Y'` which is compatible with the two inclusions and with
> the two structure morphisms to `T`.  Then there is exactly one morphism `f' : X' ⟶ Y'` inducing
> `Φ`, and it makes `(f, f')` a morphism of thickenings over `T`.
>
> The two compatibilities are the source's commuting square for `α`, `f^♯`, `i_X^♯` and `i_Y^♯`,
> and the hypothesis that `α` is a map of `𝒪_T`-algebras.  That `Φ` is locally ringed is *not*
> assumed: it is derived from the square by
> `AlgebraicGeometry.Space.isLocallyRinged_of_thickeningSquare`, as in the source.  Neither is the
> recovery of morphisms from their small étale ringed topoi assumed: it is
> `AlgebraicGeometry.Space.isRecoveredFromSmallEtale_of_mono_toSpecΓ`, which is where the
> hypothesis on the base scheme is used and the only place it is used.  That hypothesis holds for
> an affine base scheme and for a quasi-affine one.

```lean
theorem existsUnique_thickeningHom (hSmono : Mono S.toSpecΓ)
    (hG : IsThickening B S hS X' G) (hH : IsThickening B S hS Y' H)
    (pX' : X' ⟶ T) (pY' : Y' ⟶ T)
    (f : IsThickening.space B S hS hG ⟶ IsThickening.space B S hS hH)
    (Φ : RingedToposHom (smallEtaleRingedTopos B S hS X') (smallEtaleRingedTopos B S hS Y'))
    (hsquare : Nonempty (SmallEtaleTwoIso B S hS
      (smallEtaleComp B S hS Φ
        (smallEtaleRingedToposHom B S hS (IsThickening.inclusion B S hS hG)))
      (smallEtaleRingedToposHom B S hS (f ≫ IsThickening.inclusion B S hS hH))))
    (halgebra : Nonempty (SmallEtaleTwoIso B S hS
      (smallEtaleComp B S hS (smallEtaleRingedToposHom B S hS pY') Φ)
      (smallEtaleRingedToposHom B S hS pX'))) :
    ∃! f' : X' ⟶ Y', InducesSmallEtaleRingedToposHom B S hS f' Φ ∧
      IsThickening.inclusion B S hS hG ≫ f' = f ≫ IsThickening.inclusion B S hS hH ∧
      f' ≫ pY' = pX'
```

**`AlgebraicGeometry.Space.existsUnique_thickeningHom_of_isLocallyRinged`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/MorphismFromStructureMap/RecoveryAndThickeningHom.lean, line 574](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/MorphismFromStructureMap/RecoveryAndThickeningHom.lean#L574). The attribute's comment: “that the recovered morphism is a morphism of thickenings over the base and that the pair is unique, with the recovery of morphisms over the base taken as an argument (`IsRecoveredFromSmallEtale`, which is Stacks 04KL over a base) and with the locally ringed condition on (f\_spaces,etale, alpha) taken as an argument, since the latter needs the structure-sheaf half of 05ZM”.

> **Stacks 05ZN with the recovery of morphisms over the base and the local ringedness of
> `Φ` taken as arguments.**
>
> This is the shape in which the statement was first written.  Both arguments are now available
> without being assumed — `hlocal` from the commuting square by
> `AlgebraicGeometry.Space.isLocallyRinged_of_thickeningSquare`, and `hKL` for a base scheme whose
> canonical morphism to the spectrum of its global functions is a monomorphism by
> `AlgebraicGeometry.Space.isRecoveredFromSmallEtale_of_mono_toSpecΓ` — so the tag is registered on
> `AlgebraicGeometry.Space.existsUnique_thickeningHom` above rather than here.  This form is kept
> because the declarations below are stated in terms of it.

```lean
theorem existsUnique_thickeningHom_of_isLocallyRinged (hKL : IsRecoveredFromSmallEtale B S hS)
    (hG : IsThickening B S hS X' G) (hH : IsThickening B S hS Y' H)
    (pX' : X' ⟶ T) (pY' : Y' ⟶ T)
    (f : IsThickening.space B S hS hG ⟶ IsThickening.space B S hS hH)
    (Φ : RingedToposHom (smallEtaleRingedTopos B S hS X') (smallEtaleRingedTopos B S hS Y'))
    (hlocal : Φ.IsLocallyRinged)
    (hsquare : Nonempty (SmallEtaleTwoIso B S hS
      (smallEtaleComp B S hS Φ
        (smallEtaleRingedToposHom B S hS (IsThickening.inclusion B S hS hG)))
      (smallEtaleRingedToposHom B S hS (f ≫ IsThickening.inclusion B S hS hH))))
    (halgebra : Nonempty (SmallEtaleTwoIso B S hS
      (smallEtaleComp B S hS (smallEtaleRingedToposHom B S hS pY') Φ)
      (smallEtaleRingedToposHom B S hS pX'))) :
    ∃! f' : X' ⟶ Y', InducesSmallEtaleRingedToposHom B S hS f' Φ ∧
      IsThickening.inclusion B S hS hG ≫ f' = f ≫ IsThickening.inclusion B S hS hH ∧
      f' ≫ pY' = pX'
```

**`AlgebraicGeometry.Space.existsUnique_thickeningHom_of_ringedToposHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/MorphismFromStructureMap/RecoveryAndThickeningHom.lean, line 616](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/MorphismFromStructureMap/RecoveryAndThickeningHom.lean#L616). The attribute's comment: “the whole lemma, over an arbitrary base scheme: the morphism (f\_spaces,etale, alpha) of the small etale ringed topoi of the ambient spaces, compatible with the inclusions and with the structure morphisms to the base space, is induced by exactly one f', and (f, f') is a morphism of thickenings over the base space”.

> **Stacks 05ZN.**  Let `B` be a big fppf site, `S` a scheme in it and `T` an algebraic space
> over `S`.  Let `G ⊂ X'` and `H ⊂ Y'` be thickenings of algebraic spaces over `T`, with structure
> morphisms `p_{X'} : X' ⟶ T` and `p_{Y'} : Y' ⟶ T`, and let `f : X ⟶ Y` be a morphism of the two
> closed subspaces.  Let `Φ = (f_{spaces,étale}, α)` be a morphism of the small étale ringed topoi of
> `X'` and `Y'` which is compatible with the two inclusions (the source's commuting square for
> `α`, `f^♯`, `i_X^♯` and `i_Y^♯`) and with the two structure morphisms to `T` (the source's
> hypothesis that `α` is a map of `𝒪_T`-algebras).  Then there is exactly one morphism
> `f' : X' ⟶ Y'` inducing `Φ`, that is with `α = (f')^♯`, and `(f, f')` is a morphism of
> thickenings over `T`: `f' ∘ i_X = i_Y ∘ f` and `p_{Y'} ∘ f' = p_{X'}`.
>
> Nothing is assumed of the base scheme: the recovery of morphisms over the base is
> `AlgebraicGeometry.Space.isRecoveredFromSmallEtale_holds`, Stacks 04KL over an arbitrary base, the
> locality of `Φ` is derived from the square by
> `AlgebraicGeometry.Space.isLocallyRinged_of_thickeningSquare`, and the two equations and the
> uniqueness come from the faithfulness half of Tag 04KL,
> `AlgebraicGeometry.Space.eq_of_inducesCommonSmallEtaleRingedToposHom`.  This supersedes
> `AlgebraicGeometry.Space.existsUnique_thickeningHom`, which carries a hypothesis on the base.

```lean
theorem existsUnique_thickeningHom_of_ringedToposHom
    (hG : IsThickening B S hS X' G) (hH : IsThickening B S hS Y' H)
    (pX' : X' ⟶ T) (pY' : Y' ⟶ T)
    (f : IsThickening.space B S hS hG ⟶ IsThickening.space B S hS hH)
    (Φ : RingedToposHom (smallEtaleRingedTopos B S hS X') (smallEtaleRingedTopos B S hS Y'))
    (hsquare : Nonempty (SmallEtaleTwoIso B S hS
      (smallEtaleComp B S hS Φ
        (smallEtaleRingedToposHom B S hS (IsThickening.inclusion B S hS hG)))
      (smallEtaleRingedToposHom B S hS (f ≫ IsThickening.inclusion B S hS hH))))
    (halgebra : Nonempty (SmallEtaleTwoIso B S hS
      (smallEtaleComp B S hS (smallEtaleRingedToposHom B S hS pY') Φ)
      (smallEtaleRingedToposHom B S hS pX'))) :
    ∃! f' : X' ⟶ Y', InducesSmallEtaleRingedToposHom B S hS f' Φ ∧
      IsThickening.inclusion B S hS hG ≫ f' = f ≫ IsThickening.inclusion B S hS hH ∧
      f' ≫ pY' = pX'
```

## Tag 05ZP, a lemma

[Tag 05ZP](https://stacks.math.columbia.edu/tag/05ZP) in the Stacks Project.

**`AlgebraicGeometry.Space.existsUnique_isOpenSubspace_preimage_eq_of_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/OpenSubspaces.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/OpenSubspaces.lean#L117).

> **Stacks 05ZP.** Let `G ⊂ X` be a thickening of algebraic spaces over `S`. Every open
> subspace `U ⊂ G` is the inverse image of a unique open subspace `U' ⊂ X`, in other words
> `U = G ×_X U'`; the inverse image is `CategoryTheory.Subfunctor.preimage`, identified with the
> fibre product by Stacks 083Q.
>
> In the notation of the source, `G` is `X` and `X` is `X'`.
>
> The open subspace is the one cut out by the image of the point set of `U` under the inclusion
> of the thickening, which is a homeomorphism on point spaces.

```lean
theorem existsUnique_isOpenSubspace_preimage_eq_of_isThickening
    (hG : IsThickening B S hS X G) (U : Subfunctor G.toFunctor)
    (hU : IsOpenSubspace B S hS U) :
    ∃! U' : Subfunctor X.1, IsOpenSubspace B S hS U' ∧ U'.preimage G.ι = U
```

## Tag 05ZQ, a lemma

[Tag 05ZQ](https://stacks.math.columbia.edu/tag/05ZQ) in the Stacks Project.

**`AlgebraicGeometry.Space.surjective_globalFunctionsMap_projection_of_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/AffineSections.lean, line 314](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/AffineSections.lean#L314). The attribute's comment: “surjectivity of the restriction of regular functions, stated at the level of the spaces-étale sites: the affine object of the thickening's site is the base change `G ×_X U` of an object `U` of the ambient space's site, and the map is pullback along the cartesian projection `G ×_X U ⟶ U`, which is the closed immersion the source proof uses. The transport of the ambient structure sheaf through Stacks 05ZM is not used and no part of Stacks 05ZM is claimed: in this library 05ZM is formalized as an equivalence of topoi only, so the sheaf `𝒪_{X'}` on the thickening's site does not exist and `Γ(U, 𝒪_{X'})` is `Γ(U, 𝒪_U)` by construction. Granted `h07VR`, `h07SQ` and `hFinitePresentation`, which are passed unchanged to Stacks 07VS, `AlgebraicGeometry.Space.isAffineSpace_of_isSurjective_of_isFinite`, and are the conclusions of Stacks 07VR and Stacks 07SQ about inverse systems together with the finite-presentation special case of Stacks 07VS; none is the universally quantified form of this conclusion”.

> **Stacks 05ZQ.** Let `G ⊂ X` be a thickening of algebraic spaces over `S` and let `U` be an
> object of the spaces-étale site of `X` whose base change `G ×_X U` along the inclusion is
> affine. Then restriction of global regular functions along the cartesian projection
> `G ×_X U ⟶ U`, that is `Γ(U, 𝒪_U) → Γ(G ×_X U, 𝒪_{G ×_X U})`, is surjective.
>
> The ambient object `U` is affine by
> `AlgebraicGeometry.Space.isAffineSpace_of_isThickening_of_isAffineSpace_baseChange`, which is
> Stacks 07VS, and the projection is a closed immersion, so
> `AlgebraicGeometry.Space.surjective_globalFunctionsMap_of_isClosedImmersion` applies.

```lean
theorem surjective_globalFunctionsMap_projection_of_isThickening
    (hG : IsThickening B S hS X G) (U : SpacesEtale B S hS X)
    (hU : IsAffineSpace B S hS
      ((SpacesEtale.toSpaces B S hS (IsThickening.space B S hS hG)).obj
        ((spacesBaseChange B S hS (IsThickening.inclusion B S hS hG)).functor.obj U)).obj)
    (h07VR : ∀ {X' Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (g : X' ⟶ Y'),
      IsAlgebraicSpace B S hS X' → IsAlgebraicSpace B S hS Y' → IsFinite B S hS g →
      IsQuasiCompactSpace B S hS Y' →
      IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y' →
      IntegralFiniteSystem B S hS g)
    (h07SQ : ∀ {I : Type u} [Preorder I] [IsDirected I (· ≤ ·)]
      (D : DescentSituation B S hS B.contains_terminal I),
      IsAffineSpace B S hS D.limitCone.pt →
      ∃ i : I, D.base ≤ i ∧ IsAffineSpace B S hS (D.system.obj (Opposite.op i)))
    (hFinitePresentation : ∀ {X' Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (g : X' ⟶ Y'),
      IsAlgebraicSpace B S hS X' → IsAlgebraicSpace B S hS Y' → IsFinite B S hS g →
      IsFinitePresentation B S hS g → IsSurjective B S hS g → IsAffineSpace B S hS X' →
      IsAffineSpace B S hS Y') :
    Function.Surjective (globalFunctionsMap B S hS
      ((spacesBaseChange B S hS (IsThickening.inclusion B S hS hG)).projection.app U))
```

**`AlgebraicGeometry.Space.surjective_globalFunctionsMap_of_isFirstOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/AffineSections.lean, line 381](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/AffineSections.lean#L381). The attribute's comment: “the FIRST-ORDER thickening case only, with the source's own quantifier: `V` is an arbitrary object of the spaces-étale site of the closed subspace `G` whose underlying algebraic space is affine, and the map is pullback of global regular functions along the composite `V ≅ G ×_X U ⟶ U` of the isomorphism supplied by essential surjectivity of base change with the cartesian projection, `U` being the object of the ambient space's site that essential surjectivity produces. The source states 05ZQ for a thickening of arbitrary order; essential surjectivity, `AlgebraicGeometry.Space.essSurj_spacesBaseChange_of_isFirstOrderThickening`, is proved only at a first-order thickening, so the general case stays with the weaker parametrisation of `AlgebraicGeometry.Space.surjective_globalFunctionsMap_projection_of_isThickening`. The source's own second proof, for finite order thickenings, likewise reduces to the first-order case. As for the general statement, the transport of the ambient structure sheaf through Stacks 05ZM is not used and no part of Stacks 05ZM is claimed: `Γ(V, 𝒪_{X'})` is `Γ(U, 𝒪_U)` by construction. Granted `h07VR`, `h07SQ` and `hFinitePresentation`, passed unchanged to the theorem of Stacks 07VS, `AlgebraicGeometry.Space.isAffineSpace_of_isSurjective_of_isFinite`, and are the conclusions of Stacks 07VR and Stacks 07SQ about inverse systems together with the finite-presentation special case of Stacks 07VS; none is the universally quantified form of this conclusion”.

> **Stacks 05ZQ at a first-order thickening, with the source's own quantifier.** Let
> `G ⊂ X` be a *first-order* thickening of algebraic spaces over `S` and let `V` be an
> *arbitrary* object of the spaces-étale site of `G` whose underlying algebraic space is affine.
> Then restriction of global regular functions `Γ(U, 𝒪_U) → Γ(V, 𝒪_V)` is surjective, where `U`
> is the object of the spaces-étale site of `X` whose base change along the inclusion is
> isomorphic to `V`, and the map is pullback along the composite `V ≅ G ×_X U ⟶ U` of that
> isomorphism with the cartesian projection.
>
> Base change along the inclusion of a first-order thickening is essentially surjective by
> `AlgebraicGeometry.Space.essSurj_spacesBaseChange_of_isFirstOrderThickening`, which is
> Stacks 05ZH in the only generality the library has it; the instance is discharged in the
> statement, so no part of Stacks 05ZH is granted. The object `U` and the isomorphism are the
> `CategoryTheory.Functor.objPreimage` and `CategoryTheory.Functor.objObjPreimageIso` of that
> essential surjectivity. Transporting affineness of `V` across the isomorphism makes
> `AlgebraicGeometry.Space.surjective_globalFunctionsMap_projection_of_isThickening` apply at
> `U`, and pullback along an isomorphism is bijective on global regular functions, so the
> composite is surjective.
>
> Only the first-order case: Stacks 05ZQ is stated in the source for a thickening of arbitrary
> order, and for such a thickening the weaker parametrisation of
> `AlgebraicGeometry.Space.surjective_globalFunctionsMap_projection_of_isThickening` remains all
> that is available. The three hypotheses are threaded unchanged into that theorem.

```lean
theorem surjective_globalFunctionsMap_of_isFirstOrderThickening
    (hG : IsFirstOrderThickening B S hS X G)
    (V : SpacesEtale B S hS (IsThickening.space B S hS (hG.isThickening B S hS)))
    (hV : IsAffineSpace B S hS
      ((SpacesEtale.toSpaces B S hS
        (IsThickening.space B S hS (hG.isThickening B S hS))).obj V).obj)
    (h07VR : ∀ {X' Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (g : X' ⟶ Y'),
      IsAlgebraicSpace B S hS X' → IsAlgebraicSpace B S hS Y' → IsFinite B S hS g →
      IsQuasiCompactSpace B S hS Y' →
      IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y' →
      IntegralFiniteSystem B S hS g)
    (h07SQ : ∀ {I : Type u} [Preorder I] [IsDirected I (· ≤ ·)]
      (D : DescentSituation B S hS B.contains_terminal I),
      IsAffineSpace B S hS D.limitCone.pt →
      ∃ i : I, D.base ≤ i ∧ IsAffineSpace B S hS (D.system.obj (Opposite.op i)))
    (hFinitePresentation : ∀ {X' Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (g : X' ⟶ Y'),
      IsAlgebraicSpace B S hS X' → IsAlgebraicSpace B S hS Y' → IsFinite B S hS g →
      IsFinitePresentation B S hS g → IsSurjective B S hS g → IsAffineSpace B S hS X' →
      IsAffineSpace B S hS Y') :
    letI : (spacesBaseChange B S hS
        (IsThickening.inclusion B S hS (hG.isThickening B S hS))).functor.EssSurj :=
      @essSurj_spacesBaseChange_of_isFirstOrderThickening B S hS _ X
        (IsThickening.inclusion B S hS (hG.isThickening B S hS)) (inferInstanceAs (Mono G.ι))
        (Eq.mpr (congrArg (IsFirstOrderThickening B S hS X) (Subfunctor.range_ι G)) hG)
    Function.Surjective (globalFunctionsMap B S hS
      ((SpacesEtale.toSpaces B S hS
            (IsThickening.space B S hS (hG.isThickening B S hS))).map
          ((spacesBaseChange B S hS (IsThickening.inclusion B S hS
            (hG.isThickening B S hS))).functor.objObjPreimageIso V).inv ≫
        (spacesBaseChange B S hS (IsThickening.inclusion B S hS
            (hG.isThickening B S hS))).projection.app
          ((spacesBaseChange B S hS (IsThickening.inclusion B S hS
            (hG.isThickening B S hS))).functor.objPreimage V)))
```

**`AlgebraicGeometry.Space.surjective_globalFunctionsMap_of_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/AffineSectionsSpacesEtale.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/AffineSectionsSpacesEtale.lean#L122). The attribute's comment: “for a thickening of arbitrary order and an arbitrary affine object `V` of the spaces-étale site of the closed subspace. The source's `Γ(U, 𝒪_{X'})`, the sections of `𝒪_{X'}` read on the site of the closed subspace through Stacks 05ZM, is stated as `Γ(U', 𝒪_{U'})` for the object `U'` of the ambient space's site with `V ≅ X ×_{X'} U'` given by essential surjectivity of base change, and the map is pullback along `V ≅ X ×_{X'} U' ⟶ U'`”.

> **Stacks 05ZQ.** Let `S` be a scheme and let `G ⊂ X` be a thickening of algebraic spaces
> over `S`, of arbitrary order. Let `V` be an object of the spaces-étale site of `G` whose
> underlying algebraic space is affine. Then restriction of global regular functions
> `Γ(U, 𝒪_U) → Γ(V, 𝒪_V)` is surjective, where `U` is the object of the spaces-étale site of `X`
> whose base change along the inclusion is isomorphic to `V`, and the map is pullback along the
> composite `V ≅ G ×_X U ⟶ U` of that isomorphism with the cartesian projection.
>
> In the notation of the source, `G` is `X`, `X` is `X'`, and `V` is the source's `U`: the object
> `U` here is the source's `U'` with `U = X ×_{X'} U'`, and `Γ(U, 𝒪_U)` is the source's
> `Γ(U, 𝒪_{X'})`, the sections of `𝒪_{X'}` read on `X_{spaces,étale}` through Stacks 05ZM.
>
> Base change along the inclusion is essentially surjective at a thickening of arbitrary order,
> `AlgebraicGeometry.Space.essSurj_spacesBaseChange_of_isThickening`; the instance is discharged
> in the statement, so no part of Stacks 05ZH is granted. The object `U` and the isomorphism are
> the `CategoryTheory.Functor.objPreimage` and `CategoryTheory.Functor.objObjPreimageIso` of that
> essential surjectivity. Affineness of `V` transported across the isomorphism makes
> `AlgebraicGeometry.Space.surjective_globalFunctionsMap_spacesBaseChange_projection_of_isThickening`
> apply at `U`, and pullback along an isomorphism is bijective on global regular functions.

```lean
theorem surjective_globalFunctionsMap_of_isThickening
    (hG : IsThickening B S hS X G)
    (V : SpacesEtale B S hS (IsThickening.space B S hS hG))
    (hV : IsAffineSpace B S hS
      ((SpacesEtale.toSpaces B S hS (IsThickening.space B S hS hG)).obj V).obj) :
    letI : (spacesBaseChange B S hS (IsThickening.inclusion B S hS hG)).functor.EssSurj :=
      essSurj_spacesBaseChange_of_isThickening B S hS hG
    Function.Surjective (globalFunctionsMap B S hS
      ((SpacesEtale.toSpaces B S hS (IsThickening.space B S hS hG)).map
          ((spacesBaseChange B S hS (IsThickening.inclusion B S hS hG)).functor.objObjPreimageIso
            V).inv ≫
        (spacesBaseChange B S hS (IsThickening.inclusion B S hS hG)).projection.app
          ((spacesBaseChange B S hS (IsThickening.inclusion B S hS hG)).functor.objPreimage
            V)))
```

## Tag 05ZR, a lemma

[Tag 05ZR](https://stacks.math.columbia.edu/tag/05ZR) in the Stacks Project.

**`AlgebraicGeometry.Space.isRepresentable_of_isRepresentable_thickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ThickeningSchemeRepresentable.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ThickeningSchemeRepresentable.lean#L96). The attribute's comment: “granted the three hypotheses of Stacks 07VT, carried verbatim from Stacks 07VV and used for nothing else: `h09YA`, the conclusion of Stacks 09YA that an integral morphism over a quasi-compact quasi-separated algebraic space is a directed limit of finite morphisms of finite presentation; `h07SQ`, the conclusion of Stacks 07SQ that a directed system with affine transition morphisms whose limit is affine has an affine stage; and `hFinitePresentation`, the case of Stacks 07VT in which the morphism is finite and of finite presentation. None is the universally quantified form of this conclusion: the first two conclude about inverse systems and the third about affineness of a target, while this concludes representability of a presheaf”.

> **Stacks 05ZR.** Let `S` be a scheme and let `G ⊂ X'` be a thickening of algebraic spaces
> over `S`, in the subspace form of Stacks 05ZK, part (1). If `G` is (representable by) a
> scheme, then so is `X'`.
>
> The inclusion `G.ι` is integral by Stacks 081Y, injective on points because it is a
> monomorphism, and surjective on points by the definition of a thickening, so Stacks 07VV
> applies in the direction that goes from the source.

```lean
theorem isRepresentable_of_isRepresentable_thickening {X' : AlgebraicSpaces B S hS}
    {G : Subfunctor X'.1} (hG : IsThickening B S hS X' G)
    (hGrep : G.toFunctor.IsRepresentable)
    (h09YA : ∀ {Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (g : Y ⟶ Z),
      IsAlgebraicSpace B S hS Y → IsAlgebraicSpace B S hS Z → IsIntegralHom B S hS g →
      IsQuasiCompactSpace B S hS Z →
      IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Z →
      IntegralFiniteSystem B S hS g)
    (h07SQ : ∀ {I : Type u} [Preorder I] [IsDirected I (· ≤ ·)]
      (D : DescentSituation B S hS B.contains_terminal I),
      IsAffineSpace B S hS D.limitCone.pt →
      ∃ i : I, D.base ≤ i ∧ IsAffineSpace B S hS (D.system.obj (Opposite.op i)))
    (hFinitePresentation : ∀ {Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (g : Y ⟶ Z),
      IsAlgebraicSpace B S hS Y → IsAlgebraicSpace B S hS Z → IsFinite B S hS g →
      IsFinitePresentation B S hS g → IsSurjective B S hS g → IsAffineSpace B S hS Y →
      IsAffineSpace B S hS Z) :
    X'.1.IsRepresentable
```

**`AlgebraicGeometry.Space.isRepresentable_of_isThickeningHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ThickeningSchemeRepresentable.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ThickeningSchemeRepresentable.lean#L134). The attribute's comment: “the morphism form, granted the three hypotheses of Stacks 07VT, carried verbatim from Stacks 07VV and used for nothing else: `h09YA`, the conclusion of Stacks 09YA that an integral morphism over a quasi-compact quasi-separated algebraic space is a directed limit of finite morphisms of finite presentation; `h07SQ`, the conclusion of Stacks 07SQ that a directed system with affine transition morphisms whose limit is affine has an affine stage; and `hFinitePresentation`, the case of Stacks 07VT in which the morphism is finite and of finite presentation. None is the universally quantified form of this conclusion: the first two conclude about inverse systems and the third about affineness of a target, while this concludes representability of a presheaf”.

> **Stacks 05ZR, morphism form.** Let `S` be a scheme and let `i : X ⟶ X'` be a thickening
> of algebraic spaces over `S`, in the morphism form of
> `AlgebraicGeometry.Space.IsThickeningHom`. If `X` is (representable by) a scheme, then so is
> `X'`.
>
> A thickening is a closed immersion, hence integral by Stacks 081Y, it is a monomorphism and
> therefore injective on points, and it is surjective on points, so Stacks 07VV applies in the
> direction that goes from the source.

```lean
theorem isRepresentable_of_isThickeningHom {X X' : AlgebraicSpaces B S hS} (i : X ⟶ X')
    (hi : IsThickeningHom B S hS i) (hXrep : X.1.IsRepresentable)
    (h09YA : ∀ {Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (g : Y ⟶ Z),
      IsAlgebraicSpace B S hS Y → IsAlgebraicSpace B S hS Z → IsIntegralHom B S hS g →
      IsQuasiCompactSpace B S hS Z →
      IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Z →
      IntegralFiniteSystem B S hS g)
    (h07SQ : ∀ {I : Type u} [Preorder I] [IsDirected I (· ≤ ·)]
      (D : DescentSituation B S hS B.contains_terminal I),
      IsAffineSpace B S hS D.limitCone.pt →
      ∃ j : I, D.base ≤ j ∧ IsAffineSpace B S hS (D.system.obj (Opposite.op j)))
    (hFinitePresentation : ∀ {Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (g : Y ⟶ Z),
      IsAlgebraicSpace B S hS Y → IsAlgebraicSpace B S hS Z → IsFinite B S hS g →
      IsFinitePresentation B S hS g → IsSurjective B S hS g → IsAffineSpace B S hS Y →
      IsAffineSpace B S hS Z) :
    X'.1.IsRepresentable
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.isRepresentable_of_isThickening_of_isRepresentable`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ThickeningSchemeRepresentableClosedImmersion.lean#L82), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SchemeOfThickening.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SchemeOfThickening.lean#L71) (StacksFrontier).
- [`AlgebraicGeometry.Space.isRepresentable_of_isThickeningHom_of_isRepresentable`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ThickeningSchemeRepresentableClosedImmersion.lean#L98), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SchemeOfThickening.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SchemeOfThickening.lean#L78) (StacksFrontier): “the morphism form”.
- [`AlgebraicGeometry.Space.isRepresentable_of_isThickening_of_isRepresentable`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ThickeningSchemeRepresentableClosedImmersion.lean#L82), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/ThickeningSchemeRepresentableTag.lean, line 21](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ThickeningSchemeRepresentableTag.lean#L21) (StacksFrontier).
- [`AlgebraicGeometry.Space.isRepresentable_of_isThickeningHom_of_isRepresentable`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ThickeningSchemeRepresentableClosedImmersion.lean#L98), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/ThickeningSchemeRepresentableTag.lean, line 23](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ThickeningSchemeRepresentableTag.lean#L23) (StacksFrontier): “the morphism form”.

## Tag 05ZS, a lemma

[Tag 05ZS](https://stacks.math.columbia.edu/tag/05ZS) in the Stacks Project.

**`AlgebraicGeometry.Space.isEquivalence_smallBaseChange_of_isThickeningHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SmallEtaleThickeningEquivalence.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SmallEtaleThickeningEquivalence.lean#L58).

> **Stacks 05ZS.** Let `i : X ⟶ X'` be a thickening of algebraic spaces over `S`. Base change
> `V' ↦ X ×_{X'} V'` is an equivalence from the small étale site of `X'` to that of `X`.

```lean
theorem isEquivalence_smallBaseChange_of_isThickeningHom {X X' : AlgebraicSpaces B S hS}
    (i : X ⟶ X') (hi : IsThickeningHom B S hS i) :
    (smallBaseChange B S hS i hi.isClosedImmersion.rep).IsEquivalence
```

**`AlgebraicGeometry.Space.spacesEtaleEquivalenceOfIsFirstOrderThickening`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleEquivalence.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleEquivalence.lean#L180). The attribute's comment: “the FIRST-ORDER thickening case, on the spaces-étale site of Stacks 03G0. The source states the tag for a thickening of arbitrary order and as an equivalence of the small étale sites of scheme charts; on the spaces-étale site the arbitrary-order equivalence is `AlgebraicGeometry.Space.spacesEtaleEquivalenceOfIsThickening`, and on the small étale sites of scheme charts this module covers the full faithfulness of the functor, by `AlgebraicGeometry.Space.fullyFaithfulThickeningChartBaseChangeOfIsFirstOrderThickening`. The module's `What is not covered` section sets out the differences from the source”.

> **Stacks 05ZS at a first-order thickening, on the spaces-étale site.** Let `G ⊂ X` be a
> first-order thickening of algebraic spaces over `S`. Base change along the inclusion,
> `V ↦ G ×_X V`, is an equivalence of categories from the spaces-étale site of `X` to the
> spaces-étale site of `G`.
>
> In the notation of the source, `G` is `X` and `X` is `X'`: the functor is `V' ↦ X ×_{X'} V'`
> and the equivalence runs `X'_étale → X_étale`.
>
> The functor is the one of the Stacks 03G2 base-change datum
> `AlgebraicGeometry.Space.spacesBaseChange`, and it is an equivalence because a first-order
> thickening is in particular a thickening: this is
> `AlgebraicGeometry.Space.spacesEtaleEquivalenceOfIsThickening`, the arbitrary-order
> equivalence of Stacks 05ZL, read at first order.

```lean
noncomputable def spacesEtaleEquivalenceOfIsFirstOrderThickening
    (hG : IsFirstOrderThickening B S hS X G) :
    SpacesEtale B S hS X ≌
      SpacesEtale B S hS (IsThickening.space B S hS (hG.isThickening B S hS))
```

**`AlgebraicGeometry.Space.fullyFaithfulThickeningChartBaseChangeOfIsFirstOrderThickening`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleEquivalence.lean, line 244](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleEquivalence.lean#L244). The attribute's comment: “FULL FAITHFULNESS ONLY, at a FIRST-ORDER thickening, of the source's own functor `X'_étale → X_étale` on the small étale sites of SCHEME charts, Stacks 03ED. The source asserts an equivalence, so essential surjectivity on those sites is a separate statement, Stacks 07VW. The restriction to first order is inherited from the library's Stacks 05ZH, `AlgebraicGeometry.Space.full_spacesBaseChange_of_isFirstOrderThickening` and `AlgebraicGeometry.Space.faithful_spacesBaseChange_of_isFirstOrderThickening`. The companion statement on the spaces-étale site of Stacks 03G0, where the full equivalence IS available at first order, is `AlgebraicGeometry.Space.spacesEtaleEquivalenceOfIsFirstOrderThickening`; the module's `What is not covered` section sets out the differences from the source”.

> **Stacks 05ZS, full faithfulness of the functor `X'_étale → X_étale`, at a first-order
> thickening.** Let `G ⊂ X` be a first-order thickening of algebraic spaces over `S`. Base
> change of étale *scheme* charts along the inclusion,
> `AlgebraicGeometry.Space.thickeningChartBaseChange`, is fully faithful.
>
> This is on the source's own site: the objects are the schemes étale over the two spaces. Only
> full faithfulness is reached. Essential surjectivity is Stacks 07VW, which rests on
> Stacks 05ZR; these are `AlgebraicGeometry.Space.smallEtalePullback_isEquivalence` and
> `AlgebraicGeometry.Space.isRepresentable_of_isRepresentable_thickening`, and they do not apply
> here, for two separate reasons, as the module's `What is not covered` section sets out: each
> carries three inputs of Stacks 07VT that this library does not prove, and the 07VW equivalence
> is for `AlgebraicGeometry.Space.smallEtalePullback`, which nothing in this library relates as a
> functor to `AlgebraicGeometry.Space.thickeningChartBaseChange`.
>
> Chart base change becomes spaces-étale base change after the Stacks 03G1 comparison, by
> `AlgebraicGeometry.Space.smallBaseChange_comparison`. The comparison is fully faithful and
> spaces-étale base change at a first-order thickening is fully faithful, so the composite of
> chart base change with the comparison at `G` is isomorphic to a fully faithful functor, hence
> fully faithful; cancelling the faithful comparison at `G` leaves chart base change fully
> faithful.

```lean
noncomputable def fullyFaithfulThickeningChartBaseChangeOfIsFirstOrderThickening
    (hG : IsFirstOrderThickening B S hS X G) :
    (thickeningChartBaseChange B S hS (hG.isThickening B S hS)).FullyFaithful
```

**`AlgebraicGeometry.Space.isEquivalence_thickeningChartBaseChange_of_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleEquivalenceArbitraryOrder.lean, line 335](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleEquivalenceArbitraryOrder.lean#L335). The attribute's comment: “the functor is `AlgebraicGeometry.Space.thickeningChartBaseChange`, base change `V' ↦ X ×_{X'} V'` of schemes étale over `X'` along the inclusion of the thickening, between the small étale sites of Stacks 03ED; the packaged `CategoryTheory.Equivalence` is `AlgebraicGeometry.Space.smallEtaleEquivalenceOfIsThickening`”.

> **Stacks 05ZS.** Let `S` be a scheme and let `G ⊂ X` be a thickening of algebraic spaces
> over `S`, of arbitrary order. Base change of étale *scheme* charts along the inclusion,
> `V' ↦ G ×_X V'`, is an equivalence of categories from the small étale site of `X` to the small
> étale site of `G`.
>
> In the notation of the source, `G` is `X` and `X` is `X'`: the functor is `V' ↦ V = X ×_{X'} V'`
> and the equivalence runs `X'_étale → X_étale`, on the sites of Stacks 03ED whose objects are the
> schemes étale over the two spaces, which are the sites the source's statement is about. The
> cartesian square identifying the value of the functor at a chart with the fibre product is
> `AlgebraicGeometry.Space.smallBaseChange_isPullback`.
>
> Full faithfulness is `AlgebraicGeometry.Space.thickeningChartBaseChange_full` and
> `AlgebraicGeometry.Space.thickeningChartBaseChange_faithful`; essential surjectivity is
> `AlgebraicGeometry.Space.essSurj_thickeningChartBaseChange_of_isThickening`, which uses the
> source's Lemma 05ZR in its closed-immersion form. Nothing is granted and neither half bounds the
> order of the thickening.

```lean
theorem isEquivalence_thickeningChartBaseChange_of_isThickening
    (hG : IsThickening B S hS X G) :
    (thickeningChartBaseChange B S hS hG).IsEquivalence
```

## Tag 05ZT, a lemma

[Tag 05ZT](https://stacks.math.columbia.edu/tag/05ZT) in the Stacks Project.

**`AlgebraicGeometry.Space.SquareZeroExtension.nonempty_enlargedRealization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SquareZeroExtensionEnlargedRealization.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SquareZeroExtensionEnlargedRealization.lean#L98). The attribute's comment: “corrected: realized after enlarging the big fppf site, since on a fixed cutoff site a free kernel of rank the cutoff cannot be realized”.

> **Stacks 05ZT, corrected: a square-zero extension of the étale structure sheaf by a
> quasi-coherent module is realized by a first-order thickening after enlarging the big fppf
> site.**
>
> *Why the enlargement.* On a big fppf site `B` of a fixed cutoff `κ` the statement is false. Take
> `X = Y = S = Spec k` for a field `k` of size below `κ` and `𝒜 = 𝒪_X ⊕ ℐ` the trivial square-zero
> extension by the free module `ℐ = 𝒪_X^{(κ)}` of rank `κ`, which is quasi-coherent. A first-order
> thickening `X ⊂ X'` realizing it is a thickening of an affine scheme, hence an affine scheme
> (Stacks 07VT), `X' = Spec R` with `R ⟶ k` surjective with kernel `ℐ(X) = k^{(κ)}`, so `#R ≥ κ`.
> But `X'` is an algebraic space for `B`, so it has an étale chart from an object of `B`; a nonempty
> affine open `U` of it is an object of `B`, of size below `κ`, and it maps onto the one-point space
> `X'`. So `R ⟶ Γ(U, 𝒪_U)` is faithfully flat, hence injective, and `#R ≤ #Γ(U, 𝒪_U) < κ`: a
> contradiction.
>
> *What is proved.* There is a big fppf site `B'` containing `B` (the realization uses a site
> containing the thickenings of the two presenting charts of a charted presentation of `f`), with
> the transport of `X`, `Y`, `f` and `E` to `B'` (`AlgebraicGeometry.Space.siteTransport`), and a
> realization of the transported extension on `B'`. This is the Stacks statement read with the
> universe of schemes allowed to grow, which is how the Stacks project uses it.

```lean
theorem nonempty_enlargedRealization (E : SquareZeroExtension B S hS f) :
    Nonempty (EnlargedRealization B S hS E)
```

## Tag 09ZX, a lemma

[Tag 09ZX](https://stacks.math.columbia.edu/tag/09ZX) in the Stacks Project.

**`AlgebraicGeometry.Space.thickeningBaseChangeHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/BaseChange.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/BaseChange.lean#L144). The attribute's comment: “morphism of thickenings”.

> **Stacks 09ZX.** The commutative square expressing that the inclusion of the inverse image
> of a subfunctor `Y` of `Y'` along `f : X' ⟶ Y'` lies over the inclusion of `Y`: a morphism in
> the arrow category from `(Y ×_{Y'} X' ⟶ X')` to `(Y ⟶ Y')`.

```lean
def thickeningBaseChangeHom {Y' X' : AlgebraicSpaces B S hS} (Y : Subfunctor Y'.1)
    (f : X' ⟶ Y') :
    Arrow.mk (Y.preimage f.hom).ι ⟶ Arrow.mk Y.ι
```

**`AlgebraicGeometry.Space.isThickening_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/BaseChange.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/BaseChange.lean#L152). The attribute's comment: “base change of a thickening”.

> **Stacks 09ZX.** The inverse image of a thickening `Y ⊂ Y'` along a morphism of algebraic
> spaces `f : X' ⟶ Y'` is a thickening of `X'`.

```lean
theorem isThickening_preimage {Y' X' : AlgebraicSpaces B S hS} (Y : Subfunctor Y'.1)
    (f : X' ⟶ Y') (hY : IsThickening B S hS Y' Y) :
    IsThickening B S hS X' (Y.preimage f.hom)
```

**`AlgebraicGeometry.Space.isThickening_range_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/BaseChangeFibreProduct.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/BaseChangeFibreProduct.lean#L79). The attribute's comment: “base change of a thickening, at a chosen fibre product”.

> **Stacks 09ZX, at a chosen fibre product.** Let `G ⊂ X` be a thickening of algebraic
> spaces over `S` with inclusion `i : G ⟶ X`, let `φ : U ⟶ X` be any morphism, and let
>
>     P --q--> U
>     |        |
>     p        φ
>     v        v
>     G --i--> X
>
> be a cartesian square. Then the range of `q` is a thickening of `U`.
>
> This is the reading of the base change of a thickening that a chosen fibre product supplies,
> and in particular the one that the `isPullback` field of
> `AlgebraicGeometry.Space.spacesBaseChange` supplies for an object of the spaces-étale site of
> `X`. The range of `q` is the inverse image of `G` along `φ`, so this is
> `AlgebraicGeometry.Space.isThickening_preimage` read through that identification; see the
> implementation notes.

```lean
theorem isThickening_range_of_isPullback {X U P : AlgebraicSpaces B S hS}
    {G : Subfunctor X.1} (hG : IsThickening B S hS X G) {φ : U ⟶ X} {q : P ⟶ U}
    {p : P ⟶ IsThickening.space B S hS hG}
    (sq : IsPullback q p φ (IsThickening.inclusion B S hS hG)) :
    IsThickening B S hS U (Subfunctor.range q.hom)
```

**`AlgebraicGeometry.Space.isNthOrderThickening_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/BaseChangeOrder.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/BaseChangeOrder.lean#L130). The attribute's comment: “base change of an nth-order thickening”.

> **Stacks 09ZX.** The inverse image of an `n`th-order thickening `Y ⊂ Y'` along an arbitrary
> morphism `f : X' ⟶ Y'` of algebraic spaces is an `n`th-order thickening of `X'`.
>
> It is a thickening by the order-free part of the tag.  Its defining ideal on an affine chart of
> `X'` lying over an affine chart of `Y'` is the extension of the defining ideal of `Y` there, so
> its `(n+1)`st power is the extension of the `(n+1)`st power and vanishes; the affine chart
> diagrams are cofinal by Stacks 03G2, and the vanishing descends from a covering family.

```lean
theorem isNthOrderThickening_preimage {n : ℕ} {Y' X' : AlgebraicSpaces B S hS}
    (Y : Subfunctor Y'.1) (f : X' ⟶ Y') (hY : IsNthOrderThickening B S hS n Y' Y) :
    IsNthOrderThickening B S hS n X' (Y.preimage f.hom)
```

**`AlgebraicGeometry.Space.isFirstOrderThickening_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/BaseChangeOrder.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/BaseChangeOrder.lean#L152). The attribute's comment: “base change of a first-order thickening”.

> **Stacks 09ZX.** The inverse image of a first-order thickening along an arbitrary morphism
> of algebraic spaces is a first-order thickening: the case `n = 1` of
> `AlgebraicGeometry.Space.isNthOrderThickening_preimage`.

```lean
theorem isFirstOrderThickening_preimage {Y' X' : AlgebraicSpaces B S hS}
    (Y : Subfunctor Y'.1) (f : X' ⟶ Y') (hY : IsFirstOrderThickening B S hS Y' Y) :
    IsFirstOrderThickening B S hS X' (Y.preimage f.hom)
```

**`AlgebraicGeometry.Space.isFiniteOrderThickening_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/BaseChangeOrder.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/BaseChangeOrder.lean#L160). The attribute's comment: “base change of a finite-order thickening”.

> **Stacks 09ZX.** The inverse image of a finite-order thickening along an arbitrary morphism
> of algebraic spaces is a finite-order thickening, with the same bound on the order.

```lean
theorem isFiniteOrderThickening_preimage {Y' X' : AlgebraicSpaces B S hS}
    (Y : Subfunctor Y'.1) (f : X' ⟶ Y') (hY : IsFiniteOrderThickening B S hS Y' Y) :
    IsFiniteOrderThickening B S hS X' (Y.preimage f.hom)
```

Declarations registered for the tag:

- [`CategoryTheory.Subfunctor.isPullback_preimage`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SubspacePreimage.lean#L67), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/BaseChange.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/BaseChange.lean#L168) (StacksFrontier): “cartesian square”.

## Tag 0BPH, a lemma

[Tag 0BPH](https://stacks.math.columbia.edu/tag/0BPH) in the Stacks Project.

**`AlgebraicGeometry.Space.isThickening_image`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/Comp.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/Comp.lean#L50).

> **Stacks 0BPH.** A thickening `X ⊂ X'` of a closed subspace `X' ⊂ X''` of an algebraic
> space `X''` which is itself a thickening of `X''` presents `X` as a thickening of `X''`, the
> composite closed subspace being the image of `X` under the inclusion of `X'`.

```lean
theorem isThickening_image (X'' : AlgebraicSpaces B S hS) (X' : Subfunctor X''.1)
    (hX' : IsThickening B S hS X'' X') (X : Subfunctor X'.toFunctor)
    (hX : IsThickening B S hS ⟨X'.toFunctor, hX'.1.1⟩ X) :
    IsThickening B S hS X'' (X.image X'.ι)
```

## Tag 0BPI, a lemma

[Tag 0BPI](https://stacks.math.columbia.edu/tag/0BPI) in the Stacks Project.

**`AlgebraicGeometry.Space.thickening_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/FpqcLocal.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/FpqcLocal.lean#L111). The attribute's comment: “thickenings”.

> Being a thickening is fpqc local on the base for morphisms of algebraic spaces over `S`: a
> morphism whose base change to every member of some fpqc covering of its target is a thickening is
> itself a thickening.

```lean
instance thickening_isLocalAtTarget_fpqc :
    (thickeningMorphismProperty B S hS).IsLocalAtTarget
      (Topology.precoverage.{u, v} .fpqc B S hS)
```

**`AlgebraicGeometry.Space.isFirstOrderThickeningHom_of_isFpqcCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/FpqcLocalFirstOrder.lean, line 353](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/FpqcLocalFirstOrder.lean#L353). The attribute's comment: “first-order clause, for an arbitrary fpqc covering”.

> Let `f : X ⟶ X'` be a morphism of algebraic spaces over `S` and let `{gᵢ : X'ᵢ ⟶ X'}` be an
> fpqc covering of `X'` by algebraic spaces. If every base change `fᵢ : Xᵢ ⟶ X'ᵢ` of `f` is a
> first-order thickening then `f` is a first-order thickening.

```lean
theorem isFirstOrderThickeningHom_of_isFpqcCovering {I : Type v}
    {X X' : AlgebraicSpaces B S hS} (f : X ⟶ X')
    {Xi X'i : I → AlgebraicSpaces B S hS} (g : ∀ i, X'i i ⟶ X')
    (fi : ∀ i, Xi i ⟶ X'i i) (p : ∀ i, Xi i ⟶ X)
    (hsq : ∀ i, IsPullback (p i).hom (fi i).hom f.hom (g i).hom)
    (hg : IsFpqcCovering B S hS fun i ↦ (g i).hom)
    (h : ∀ i, IsFirstOrderThickeningHom B S hS (fi i)) :
    IsFirstOrderThickeningHom B S hS f
```

**`AlgebraicGeometry.Space.firstOrderThickening_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/FpqcLocalFirstOrder.lean, line 393](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/FpqcLocalFirstOrder.lean#L393). The attribute's comment: “first order thickenings”.

> Being a first-order thickening is fpqc local on the base for morphisms of algebraic spaces
> over `S`: a morphism whose base change to every member of some fpqc covering of its target is a
> first-order thickening is itself one, and conversely.

```lean
instance firstOrderThickening_isLocalAtTarget_fpqc :
    (firstOrderThickeningMorphismProperty B S hS).IsLocalAtTarget
      (Topology.precoverage.{u, v} .fpqc B S hS)
```

**`AlgebraicGeometry.Space.isThickeningHom_and_isFirstOrderThickeningHom_of_isFpqcCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/FpqcLocalFirstOrder.lean, line 415](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/FpqcLocalFirstOrder.lean#L415).

> Being a thickening is fpqc local, and similarly for first order thickenings. Let
> `f : X ⟶ X'` be a morphism of algebraic spaces over `S` and let `{gᵢ : X'ᵢ ⟶ X'}` be an fpqc
> covering of `X'` by algebraic spaces, with `fᵢ : Xᵢ ⟶ X'ᵢ` the base change of `f` along `gᵢ`.
> Then: if every `fᵢ` is a thickening so is `f`, and if every `fᵢ` is a first-order thickening so
> is `f`.

```lean
theorem isThickeningHom_and_isFirstOrderThickeningHom_of_isFpqcCovering {I : Type v}
    {X X' : AlgebraicSpaces B S hS} (f : X ⟶ X')
    {Xi X'i : I → AlgebraicSpaces B S hS} (g : ∀ i, X'i i ⟶ X')
    (fi : ∀ i, Xi i ⟶ X'i i) (p : ∀ i, Xi i ⟶ X)
    (hsq : ∀ i, IsPullback (p i).hom (fi i).hom f.hom (g i).hom)
    (hg : IsFpqcCovering B S hS fun i ↦ (g i).hom) :
    ((∀ i, IsThickeningHom B S hS (fi i)) → IsThickeningHom B S hS f) ∧
      ((∀ i, IsFirstOrderThickeningHom B S hS (fi i)) →
        IsFirstOrderThickeningHom B S hS f)
```

**`AlgebraicGeometry.Space.isThickeningHom_iff_forall_of_isFpqcCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/FpqcLocalFirstOrder.lean, line 431](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/FpqcLocalFirstOrder.lean#L431). The attribute's comment: “thickenings, as an equivalence along an fpqc covering”.

> A morphism `f : X ⟶ X'` of
> algebraic spaces over `S` is a thickening if and only if its base change along every member of
> an fpqc covering `{gᵢ : X'ᵢ ⟶ X'}` is a thickening.

```lean
theorem isThickeningHom_iff_forall_of_isFpqcCovering {I : Type v}
    {X X' : AlgebraicSpaces B S hS} (f : X ⟶ X')
    {Xi X'i : I → AlgebraicSpaces B S hS} (g : ∀ i, X'i i ⟶ X')
    (fi : ∀ i, Xi i ⟶ X'i i) (p : ∀ i, Xi i ⟶ X)
    (hsq : ∀ i, IsPullback (p i).hom (fi i).hom f.hom (g i).hom)
    (hg : IsFpqcCovering B S hS fun i ↦ (g i).hom) :
    IsThickeningHom B S hS f ↔ ∀ i, IsThickeningHom B S hS (fi i)
```

**`AlgebraicGeometry.Space.isFirstOrderThickeningHom_iff_forall_of_isFpqcCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/FpqcLocalFirstOrder.lean, line 445](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/FpqcLocalFirstOrder.lean#L445). The attribute's comment: “first-order clause, as an equivalence along an fpqc covering”.

> A morphism `f : X ⟶ X'` of
> algebraic spaces over `S` is a first-order thickening if and only if its base change along
> every member of an fpqc covering `{gᵢ : X'ᵢ ⟶ X'}` is a first-order thickening.

```lean
theorem isFirstOrderThickeningHom_iff_forall_of_isFpqcCovering {I : Type v}
    {X X' : AlgebraicSpaces B S hS} (f : X ⟶ X')
    {Xi X'i : I → AlgebraicSpaces B S hS} (g : ∀ i, X'i i ⟶ X')
    (fi : ∀ i, Xi i ⟶ X'i i) (p : ∀ i, Xi i ⟶ X)
    (hsq : ∀ i, IsPullback (p i).hom (fi i).hom f.hom (g i).hom)
    (hg : IsFpqcCovering B S hS fun i ↦ (g i).hom) :
    IsFirstOrderThickeningHom B S hS f ↔
      ∀ i, IsFirstOrderThickeningHom B S hS (fi i)
```

**`Stacks.Spaces.UniversalThickening.isClosedSubspace_and_isFirstOrderThickening_of_surjectiveEtaleChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/UniversalExistence/FirstOrderClauseAndAffineSize.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/UniversalExistence/FirstOrderClauseAndAffineSize.lean#L279). The attribute's comment: “first-order clause, along a surjective etale chart”.

> **Stacks 0BPI, the first-order clause, along a surjective étale chart.** Let `Y` be a
> subfunctor of an algebraic space `Q` over `S` which is a sheaf for the big fppf topology, and
> let `q : V ⟶ Q` be a surjective étale chart of `Q` by an object of the site. If the base change
> of the inclusion of `Y` along `q` is a closed immersion whose range is a first-order thickening
> of `V`, then `Y` is a closed subspace of `Q` and a first-order thickening of it.
>
> The source states the clause for an arbitrary fpqc covering of the target; this is the case of
> a one-member covering by a surjective étale scheme chart, which is the case the construction
> below consumes, together with the sheaf condition on `Y` that the fpqc statement does not ask
> for. Algebraicity of `Y` and closedness of its inclusion are Stacks 03I2 at the closed
> immersions, whose effective-descent input is discharged outright by
> `AlgebraicGeometry.Space.isEffectiveDescentAlongSurjectiveEtale_isClosedImmersion`;
> surjectivity on points follows from surjectivity of `q` and of the base change; and the order
> clause is `Stacks.Spaces.UniversalThickening.definingIdealAt_pow_eq_bot_of_surjectiveEtaleChart`,
> which descends the vanishing of the square of the defining ideal from the charts of `V` to the
> charts of `Q`.

```lean
theorem isClosedSubspace_and_isFirstOrderThickening_of_surjectiveEtaleChart
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {Q : AlgebraicGeometry.AlgebraicSpaces B S hS} (Y : Subfunctor Q.1)
    (hYsheaf : Presheaf.IsSheaf (AlgebraicGeometry.BigFppfOver.topology B S hS) Y.toFunctor)
    {V : AlgebraicGeometry.BigFppfOver B S hS} (q : yoneda.obj V ⟶ Q.1)
    (hqsurj : (MorphismProperty.inverseImage
      (@AlgebraicGeometry.Surjective.{u} : MorphismProperty Scheme.{u})
      (AlgebraicGeometry.BigFppfOver.toScheme B S hS)).presheaf q)
    (hqetale : (MorphismProperty.inverseImage
      (@AlgebraicGeometry.Etale.{u} : MorphismProperty Scheme.{u})
      (AlgebraicGeometry.BigFppfOver.toScheme B S hS)).presheaf q)
    (hclosed : AlgebraicGeometry.Space.IsClosedImmersion B S hS
      (Limits.pullback.snd Y.ι q))
    (hfirst : AlgebraicGeometry.Space.IsFirstOrderThickening B S hS
      (AlgebraicGeometry.schemeSpace V)
      (Subfunctor.range (Limits.pullback.snd Y.ι q))) :
    AlgebraicGeometry.Space.IsClosedSubspace B S hS Y ∧
      AlgebraicGeometry.Space.IsFirstOrderThickening B S hS Q Y
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.9, Tag 05ZJ](https://stacks.math.columbia.edu/tag/05ZJ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
