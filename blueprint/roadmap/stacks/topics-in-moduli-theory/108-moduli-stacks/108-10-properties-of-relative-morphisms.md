---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.diagonal_relativeHomProjection, AlgebraicGeometry.Space.isSeparated_and_isLocallyOfFinitePresentation_relativeHomProjection_unconditional, AlgebraicGeometry.Space.isomSubfunctor, AlgebraicGeometry.Space.isOpenSubspace_isomSubfunctor, AlgebraicGeometry.Space.isOpenSubspace_isomSubfunctor_of_isFinitePresentation, AlgebraicGeometry.Space.numericalRelativeHom, AlgebraicGeometry.Space.numericalSituationRelativeHom, AlgebraicGeometry.Space.isFlat_and_isClosedImmersion_numericalSituationRelativeHom_ι
statement: formalized
proof: formalized
---

# 108.10 Properties of relative morphisms

Section 108.10 of the Stacks Project, [Tag 0DPL](https://stacks.math.columbia.edu/tag/0DPL). 5 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DPM, a lemma

[Tag 0DPM](https://stacks.math.columbia.edu/tag/0DPM) in the Stacks Project.

**`AlgebraicGeometry.Space.diagonal_relativeHomProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/RelativeMorphismDiagonal.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/RelativeMorphismDiagonal.lean#L94).

> **Stacks 0DPM.** The diagonal of `Mor_B(Y, X) ⟶ B` is a closed immersion of finite
> presentation, for `Y ⟶ B` flat, proper and of finite presentation and `X ⟶ B` separated and of
> finite presentation: it is representable by closed immersions of schemes locally of finite
> presentation.

```lean
theorem diagonal_relativeHomProjection (hsep : IsSeparated B S hS x)
    (hxfp : IsFinitePresentation B S hS x) (hfp : IsFinitePresentation B S hS z)
    (hflat : IsFlat B S hS z) (hproper : IsProper B S hS z) :
    (closedImmersionFinitePresentation (B := B) (S := S) (hS := hS)).presheaf
      (pullback.diagonal (relativeHomProjection B S hS Z X Q z x hZ hX hQ))
```

## Tag 0DPN, a lemma

[Tag 0DPN](https://stacks.math.columbia.edu/tag/0DPN) in the Stacks Project.

**`AlgebraicGeometry.Space.isSeparated_and_isLocallyOfFinitePresentation_relativeHomProjection_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/RelativeMorphismSeparatedFinitePresentationUnconditional.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/RelativeMorphismSeparatedFinitePresentationUnconditional.lean#L56).

> **Stacks 0DPN.** Let `Q` be an algebraic space, `z : Z ⟶ Q` flat, proper and of finite
> presentation and `x : X ⟶ Q` separated and of finite presentation, all algebraic spaces over `S`.
> Then the projection `Mor_Q(Z, X) ⟶ Q` of the relative morphism functor is separated (its diagonal
> is a closed immersion, Stacks 0DPM) and locally of finite presentation.

```lean
theorem isSeparated_and_isLocallyOfFinitePresentation_relativeHomProjection_unconditional
    (hsep : IsSeparated B S hS x) (hxfp : IsFinitePresentation B S hS x)
    (hfp : IsFinitePresentation B S hS z) (hflat : IsFlat B S hS z)
    (hproper : IsProper B S hS z) :
    IsSeparated B S hS (relativeHomProjection B S hS Z X Q z x hZ hX hQ) ∧
      IsLocallyOfFinitePresentation B S hS (relativeHomProjection B S hS Z X Q z x hZ hX hQ)
```

## Tag 0DPP, a lemma

[Tag 0DPP](https://stacks.math.columbia.edu/tag/0DPP) in the Stacks Project.

**`AlgebraicGeometry.Space.isomSubfunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/IsomorphismLocusInRelativeMorphisms.lean, line 290](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/IsomorphismLocusInRelativeMorphisms.lean#L290). The attribute's comment: “the subfunctor Isom\_B(Y, X) of Mor\_B(Y, X) of isomorphisms”.

> **Stacks 0DPP,** the subfunctor `Isom_Q(Z, X) ⊆ Mor_Q(Z, X)` of relative isomorphisms: its
> sections over a scheme `T` are the pairs `(a, b)` of Stacks 05Y1 at `T` whose morphism of base
> changes `Z_T ⟶ X_T` is an isomorphism.
>
> This is a subfunctor because the restriction maps of `Mor_Q(Z, X)` are restriction of pairs
> (`AlgebraicGeometry.Space.relativeHomSections_map`) and a restriction of a relative isomorphism
> is a relative isomorphism.

```lean
def isomSubfunctor : Subfunctor (relativeHom B S hS Z X Q z x hZ hX hQ)
```

**`AlgebraicGeometry.Space.isOpenSubspace_isomSubfunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/IsomorphismLocusInRelativeMorphisms.lean, line 322](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/IsomorphismLocusInRelativeMorphisms.lean#L322). The attribute's comment: “openness of the subfunctor of isomorphisms”.

> **Stacks 0DPP.** With `Z ⟶ Q` flat, proper and of finite presentation and `X ⟶ Q` proper,
> the subfunctor `Isom_Q(Z, X) ⊆ Mor_Q(Z, X)` of relative isomorphisms is an open subspace.
>
> This is the isomorphism locus of Stacks 05XD applied to the universal relative morphism, the
> pair corresponding to the identity of `Mor_Q(Z, X)` under the bijection of Stacks 05Y3: the
> source of that morphism is flat, locally of finite presentation and universally closed over
> `Mor_Q(Z, X)` and its target is separated, locally of finite type and closed over
> `Mor_Q(Z, X)`, both being base changes. A morphism from a scheme `T` factors through the locus
> exactly when the base change of the universal morphism along it is an isomorphism, which is the
> condition cutting out `Isom_Q(Z, X)`, so the locus *is* `Isom_Q(Z, X)`.
>
> The algebraicity `hM` of `Mor_Q(Z, X)` is an explicit hypothesis: it is Stacks 0D1C, the standing
> fact of the source's section, and the conclusion cannot do without it, because an open subspace
> is in particular an algebraic space and the finite presentation and separatedness hypotheses on
> `x` of the source's section enter the statement only through it.

```lean
theorem isOpenSubspace_isomSubfunctor (hzfp : IsFinitePresentation B S hS z)
    (hzflat : IsFlat B S hS z) (hzproper : IsProper B S hS z) (hxproper : IsProper B S hS x)
    (hM : IsAlgebraicSpace B S hS (relativeHom B S hS Z X Q z x hZ hX hQ)) :
    IsOpenSubspace B S hS (isomSubfunctor B S hS Z X Q z x hZ hX hQ)
```

**`AlgebraicGeometry.Space.isOpenSubspace_isomSubfunctor_of_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/IsomorphismLocusUnconditional.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/IsomorphismLocusUnconditional.lean#L59). The attribute's comment: “the subfunctor Isom\_B(Y, X) of Mor\_B(Y, X) of isomorphisms is an open subspace, for Y ⟶ B flat, proper and of finite presentation and X ⟶ B proper and of finite presentation”.

> Let `Q` be an algebraic space and `z : Z ⟶ Q`, `x : X ⟶ Q` morphisms of algebraic spaces over
> `S` with `z` flat, proper and of finite presentation and `x` proper and of finite presentation (in
> particular separated, as in the standing data of Stacks 0DPL). Then the subfunctor
> `Isom_Q(Z, X) ⊆ Mor_Q(Z, X)` of isomorphisms is an open subspace.

```lean
theorem isOpenSubspace_isomSubfunctor_of_isFinitePresentation
    (hx_fp : IsFinitePresentation B S hS x) (hx_proper : IsProper B S hS x)
    (hz_fp : IsFinitePresentation B S hS z) (hz_flat : IsFlat B S hS z)
    (hz_proper : IsProper B S hS z) :
    IsOpenSubspace B S hS (isomSubfunctor B S hS Z X Q z x hZ hX hQ)
```

## Tag 0DPQ, a remark

[Tag 0DPQ](https://stacks.math.columbia.edu/tag/0DPQ) in the Stacks Project.

**`AlgebraicGeometry.Space.numericalRelativeHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/NumericalRelativeMorphisms.lean, line 320](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/NumericalRelativeMorphisms.lean#L320). The attribute's comment: “the definition of `Mor^P_B(Y, X)` as the subfunctor of `Mor_B(Y, X)` of relative morphisms whose graph has the prescribed invariants, with the open subspace of a test scheme that tests the source's open immersion for a finite index set; that `Mor^P_B(Y, X) ⟶ Mor_B(Y, X)` is a flat closed immersion rests on Lemmas 0DND and 0DNE, which are assertions about a morphism of algebraic stacks and are unavailable in this development, and is not stated”.

> **Stacks 0DPQ,** the subfunctor `Mor^P_Q(Z, X) ⊆ Mor_Q(Z, X)`: its sections over a scheme `T`
> are the pairs `(a, b)` of Stacks 05Y1 at `T` whose graph, a point of `Hilb_{Z ×_Q X / Q}` over
> `T` by Stacks 0D1A, has the prescribed invariants.  Since the graph transformation is the
> inclusion `Mor_Q(Z, X) ⊆ Hilb_{Z ×_Q X / Q}` of Stacks 0D1B, this is the intersection
> `Mor_Q(Z, X) ∩ Hilb^P_{Z ×_Q X / Q}` of the source, formed as an inverse image.
>
> This is a subfunctor because the restriction maps of `Mor_Q(Z, X)` go to base change of graphs
> and the condition on the invariants is stable under base change.

```lean
def numericalRelativeHom : Subfunctor (relativeHom B S hS Z X Q z x hZ hX hQ)
```

**`AlgebraicGeometry.Space.numericalSituationRelativeHom`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/NumericalRelativeMorphismsClopen.lean, line 173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/NumericalRelativeMorphismsClopen.lean#L173). The attribute's comment: “the definition `Mor^P_B(Y, X) = Mor_B(Y, X) ∩ Hilb^P_{Y ×_B X/B}`, for the numerical invariants `χ(K_i ⊗^𝐋 κ(t))` of Situation 0DNC on `Y ×_B X ⟶ B`”.

> The subfunctor `Mor^P_Q(Z, X) = Mor_Q(Z, X) ∩ Hilb^P_{Z ×_Q X / Q}`. For the standing data `N`
> of Situation 0DNC on `Z ×_Q X ⟶ Q` (a set `I`, perfect objects `E_i` of `D(𝒪_{Z ×_Q X})` and
> `P : I → ℤ`), the subfunctor of `Mor_Q(Z, X)` of the relative morphisms over `T` whose graph `W`, a
> point of `Hilb_{Z ×_Q X / Q}` by Stacks 0D1A and 0D1B, lies in `Hilb^P_{Z ×_Q X / Q}` of Stacks
> 0DPG: `χ(K_i ⊗^𝐋 κ(t)) = P(i)` for `K_i = Rf_{T,*}(E_{i,T} ⊗^𝐋 𝒪_W)`, every `i ∈ I` and every point
> `t` of `T`.

```lean
abbrev numericalSituationRelativeHom : Subfunctor (relativeHom B S hS Z X Q z x hZ hX hQ)
```

**`AlgebraicGeometry.Space.isFlat_and_isClosedImmersion_numericalSituationRelativeHom_ι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/NumericalRelativeMorphismsClopen.lean, line 222](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/NumericalRelativeMorphismsClopen.lean#L222). The attribute's comment: “`Mor^P_B(Y, X) ⟶ Mor_B(Y, X)` is a flat closed immersion”.

> The morphism `Mor^P_Q(Z, X) ⟶ Mor_Q(Z, X)` is a flat closed immersion.

```lean
theorem isFlat_and_isClosedImmersion_numericalSituationRelativeHom_ι :
    IsFlat B S hS (numericalSituationRelativeHom B S hS hsep hx_fp hfp hflat hproper N).ι ∧
      IsClosedImmersion B S hS
        (numericalSituationRelativeHom B S hS hsep hx_fp hfp hflat hproper N).ι
```

**`AlgebraicGeometry.Space.isOpenImmersion_and_isClosedImmersion_numericalSituationRelativeHom_ι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/NumericalRelativeMorphismsClopen.lean, line 232](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/NumericalRelativeMorphismsClopen.lean#L232). The attribute's comment: “for `I` finite, `Mor^P_B(Y, X) ⟶ Mor_B(Y, X)` is an open and closed immersion”.

> For `I` finite the morphism `Mor^P_Q(Z, X) ⟶ Mor_Q(Z, X)` is an open and closed immersion.

```lean
theorem isOpenImmersion_and_isClosedImmersion_numericalSituationRelativeHom_ι [Finite N.I] :
    IsOpenImmersion B S hS (numericalSituationRelativeHom B S hS hsep hx_fp hfp hflat hproper N).ι ∧
      IsClosedImmersion B S hS
        (numericalSituationRelativeHom B S hS hsep hx_fp hfp hflat hproper N).ι
```

**`AlgebraicGeometry.Space.isOpenImmersion_and_isClosedImmersion_numericalSituationRelativeHom_ι_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/NumericalRelativeMorphismsClopen.lean, line 244](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/NumericalRelativeMorphismsClopen.lean#L244). The attribute's comment: “for `B` locally Noetherian, `Mor^P_B(Y, X) ⟶ Mor_B(Y, X)` is an open and closed immersion, for an arbitrary index set `I`”.

> If `Q` is locally Noetherian, then for any index set `I` the morphism
> `Mor^P_Q(Z, X) ⟶ Mor_Q(Z, X)` is an open and closed immersion.

```lean
theorem isOpenImmersion_and_isClosedImmersion_numericalSituationRelativeHom_ι_of_isLocallyNoetherian
    (hQN : IsLocallyNoetherian B S hS Q) :
    IsOpenImmersion B S hS (numericalSituationRelativeHom B S hS hsep hx_fp hfp hflat hproper N).ι ∧
      IsClosedImmersion B S hS
        (numericalSituationRelativeHom B S hS hsep hx_fp hfp hflat hproper N).ι
```

**`AlgebraicGeometry.Space.hilbertPolynomialSituationRelativeHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/NumericalRelativeMorphismsClopen.lean, line 301](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/NumericalRelativeMorphismsClopen.lean#L301). The attribute's comment: “the notation `Mor^{P, L}_B(Y, X)`: `Mor^P_B(Y, X)` for `I = ℤ` and `E_i = L^{⊗ i}`, the relative morphisms whose graph `W` has `χ((Y ×_B X)_t, 𝒪_{W_t} ⊗ L_t^{⊗ i}) = P(i)` for all `i` and `t`”.

> The subfunctor `Mor^{P, L}_Q(Z, X)`: `Mor^P_Q(Z, X)` for `I = ℤ` and `E_n = L^{⊗ n}`, an
> invertible `𝒪_{Z ×_Q X}`-module `L`. Its sections over `T` are the relative morphisms whose graph
> `W ⊆ (Z ×_Q X)_T` has `χ((Z ×_Q X)_t, 𝒪_{W_t} ⊗ L_t^{⊗ n}) = P(n)` for every `n ∈ ℤ` and every
> point `t` of `T`, the invariants `χ(X_t, E_{n,t} ⊗^𝐋 𝒪_{W_t})` of Situation 0DNC for
> `E_n = L^{⊗ n}`: the pull-back along the graph transformation of the subfunctor of
> `Hilb_{Z ×_Q X / Q}` corresponding to `Coh^{P, L}_{Z ×_Q X / Q}` (Stacks 0DNF).

```lean
def hilbertPolynomialSituationRelativeHom : Subfunctor (relativeHom B S hS Z X Q z x hZ hX hQ)
```

**`AlgebraicGeometry.Space.isOpenImmersion_and_isClosedImmersion_hilbertPolynomialSituationRelativeHom_ι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/NumericalRelativeMorphismsClopen.lean, line 323](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/NumericalRelativeMorphismsClopen.lean#L323). The attribute's comment: “for `I = ℤ` and `E_i = L^{⊗ i}` with `L` an invertible module on `Y ×_B X`, `Mor^{P, L}_B(Y, X) ⟶ Mor_B(Y, X)` is an open and closed immersion”.

> For an invertible `𝒪_{Z ×_Q X}`-module `L` and any `P : ℤ → ℤ`, the morphism
> `Mor^{P, L}_Q(Z, X) ⟶ Mor_Q(Z, X)` is an open and closed immersion.

```lean
theorem isOpenImmersion_and_isClosedImmersion_hilbertPolynomialSituationRelativeHom_ι :
    IsOpenImmersion B S hS
        (hilbertPolynomialSituationRelativeHom B S hS hsep hx_fp hfp hflat hproper L P).ι ∧
      IsClosedImmersion B S hS
        (hilbertPolynomialSituationRelativeHom B S hS hsep hx_fp hfp hflat hproper L P).ι
```

**`AlgebraicGeometry.Space.isFlat_and_isClosedImmersion_numericalRelativeHomInclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/NumericalRelativeMorphismsImmersion.lean, line 244](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/NumericalRelativeMorphismsImmersion.lean#L244). The attribute's comment: “`Mor^P_B(Y, X) ⟶ Mor_B(Y, X)` is a flat closed immersion”.

> **Stacks 0DPQ.**  The morphism `Mor^P_Q(Z, X) ⟶ Mor_Q(Z, X)` is a flat closed immersion.

```lean
theorem isFlat_and_isClosedImmersion_numericalRelativeHomInclusion :
    IsFlat B S hS
        (numericalRelativeHomInclusion B S hS Z X Q z x hZ hX hQ χd P hsep hfp hflat hproper) ∧
      IsClosedImmersion B S hS
        (numericalRelativeHomInclusion B S hS Z X Q z x hZ hX hQ χd P hsep hfp hflat hproper)
```

**`AlgebraicGeometry.Space.isOpenImmersion_and_isClosedImmersion_numericalRelativeHomInclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/NumericalRelativeMorphismsImmersion.lean, line 256](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/NumericalRelativeMorphismsImmersion.lean#L256). The attribute's comment: “for `I` finite, `Mor^P_B(Y, X) ⟶ Mor_B(Y, X)` is an open and closed immersion”.

> **Stacks 0DPQ, the case of a finite index set.**  For `I` finite the morphism
> `Mor^P_Q(Z, X) ⟶ Mor_Q(Z, X)` is an open and closed immersion.

```lean
theorem isOpenImmersion_and_isClosedImmersion_numericalRelativeHomInclusion [Finite I] :
    IsOpenImmersion B S hS
        (numericalRelativeHomInclusion B S hS Z X Q z x hZ hX hQ χd P hsep hfp hflat hproper) ∧
      IsClosedImmersion B S hS
        (numericalRelativeHomInclusion B S hS Z X Q z x hZ hX hQ χd P hsep hfp hflat hproper)
```

## Tag 0DPR, a lemma

[Tag 0DPR](https://stacks.math.columbia.edu/tag/0DPR) in the Stacks Project.

**`AlgebraicGeometry.Space.isSeparated_and_isFinitePresentation_relativeHomHilbertPolynomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/RelativeMorphismsHilbertPolynomialFinitePresentation.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/RelativeMorphismsHilbertPolynomialFinitePresentation.lean#L59).

> Let `Q` be an algebraic space over `Spec ℤ`, `z : Z ⟶ Q` flat, proper and of finite
> presentation, `x : X ⟶ Q` separated and of finite presentation, `N` an invertible module ample on
> `Z/Q` and `L` an invertible module ample on `X/Q` (Stacks 0D31), and `P` a numerical polynomial.
> Then for `ℳ = pr₁^*N ⊗ pr₂^*L` on `Z ×_Q X` (`AlgebraicGeometry.Space.graphAmbientTensor`),
> `Mor^{P, ℳ}_Q(Z, X)` (`AlgebraicGeometry.Space.relativeHomHilbertPolynomial`) is an algebraic
> space and its morphism to `Q` is separated and of finite presentation.

```lean
theorem isSeparated_and_isFinitePresentation_relativeHomHilbertPolynomial
    {Z X Q : (BigFppfOver B integerBase ℤS)ᵒᵖ ⥤ Type u} {z : Z ⟶ Q} {x : X ⟶ Q}
    (hZ : IsAlgebraicSpace B integerBase ℤS Z) (hX : IsAlgebraicSpace B integerBase ℤS X)
    (hQ : IsAlgebraicSpace B integerBase ℤS Q)
    (hsep : IsSeparated B integerBase ℤS x) (hxfp : IsFinitePresentation B integerBase ℤS x)
    (hfp : IsFinitePresentation B integerBase ℤS z) (hflat : IsFlat B integerBase ℤS z)
    (hproper : IsProper B integerBase ℤS z)
    (N : Modules.{u, u} B integerBase ℤS Z hZ)
    [hNi : Stacks.SheafOfModules.IsInvertible (structurePresheaf B integerBase ℤS Z)
      ((Stacks.SheafOfModules.Tensor.ringSheaf
        (smallEtaleRingedSite B integerBase ℤS Z hZ).O)).property N]
    (L : Modules.{u, u} B integerBase ℤS X hX)
    [hLi : Stacks.SheafOfModules.IsInvertible (structurePresheaf B integerBase ℤS X)
      ((Stacks.SheafOfModules.Tensor.ringSheaf
        (smallEtaleRingedSite B integerBase ℤS X hX).O)).property L]
    (hN : IsRelativelyAmple B integerBase ℤS
      (ObjectProperty.homMk z : (⟨Z, hZ⟩ : AlgebraicSpaces B integerBase ℤS) ⟶ ⟨Q, hQ⟩) N)
    (hL : IsRelativelyAmple B integerBase ℤS
      (ObjectProperty.homMk x : (⟨X, hX⟩ : AlgebraicSpaces B integerBase ℤS) ⟶ ⟨Q, hQ⟩) L)
    {P : ℤ → ℤ} {p : Polynomial ℚ} (hP : ∀ m : ℤ, p.eval (m : ℚ) = (P m : ℚ)) :
    IsAlgebraicSpace B integerBase ℤS (relativeHomHilbertPolynomial hZ hX hQ hsep hxfp hfp hflat
        hproper (graphAmbientTensor z x hZ hX hQ N L) P).toFunctor ∧
      IsSeparated B integerBase ℤS ((relativeHomHilbertPolynomial hZ hX hQ hsep hxfp hfp hflat
        hproper (graphAmbientTensor z x hZ hX hQ N L) P).ι ≫
          relativeHomProjection B integerBase ℤS Z X Q z x hZ hX hQ) ∧
      IsFinitePresentation B integerBase ℤS ((relativeHomHilbertPolynomial hZ hX hQ hsep hxfp hfp
        hflat hproper (graphAmbientTensor z x hZ hX hQ N L) P).ι ≫
          relativeHomProjection B integerBase ℤS Z X Q z x hZ hX hQ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 108.10, Tag 0DPL](https://stacks.math.columbia.edu/tag/0DPL)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
