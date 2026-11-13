---
declaration: section
origin: cited
lean: AlgebraicGeometry.fppfH1_restriction_genericPoint_injective_of_dim_two, AlgebraicGeometry.bijective_torsorSectionsRestrictGenericPoint, AlgebraicGeometry.fppfH1_restriction_genericPoint_injective_of_isRegular, AlgebraicGeometry.Space.fppfH1_isAddTorsion, Stacks.Examples.NonAlgebraicHomStack.Situation.exists_not_restriction_homStackClassifyingStack, Stacks.Examples.NonAlgebraicHomStack.Situation.not_isAlgebraicStack_homStackClassifyingStack, Stacks.Examples.NonAlgebraicHomStack.not_forall_isAlgebraicStack_of_isAbsolutelySeparated_of_not_isEffective
statement: formalized
proof: formalized
---

# 110.74 An example of a non-algebraic Hom-stack

Section 110.74 of the Stacks Project, [Tag 0AF8](https://stacks.math.columbia.edu/tag/0AF8). 6 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AF9, a lemma

[Tag 0AF9](https://stacks.math.columbia.edu/tag/0AF9) in the Stacks Project.

**`AlgebraicGeometry.fppfH1_restriction_genericPoint_injective_of_dim_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/AbelianSchemeFirstCohomologyInjective.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/AbelianSchemeFirstCohomologyInjective.lean#L88).

> **Stacks 0AF9.** Let `W` be a two dimensional regular integral Noetherian scheme with
> function field `K` and let `G → W` be an abelian scheme. Then the restriction map
> `H¹_fppf(W, G) → H¹_fppf(Spec K, G)` along the generic point is injective.
>
> A class in the kernel is the class of a torsor with a section over `Spec K`, which is trivial by
> `AlgebraicGeometry.isTrivial_of_nonempty_sections_genericPoint`.

```lean
public theorem fppfH1_restriction_genericPoint_injective_of_dim_two
    [IsIntegral W] [AlgebraicGeometry.IsNoetherian W] (hreg : IsRegular W)
    (hdim : topologicalKrullDim (W : Type u) = (2 : WithBot ℕ∞))
    (hK : B.Contains (Spec W.functionField))
    (G : Over W) [GrpObj G] [IsAbelianScheme G] (hG : B.Contains G.left)
    [HasSheafify (BigFppfOver.topology B W hW) AddCommGrpCat.{u}]
    [HasExt.{w} (Sheaf (BigFppfOver.topology B W hW) AddCommGrpCat.{u})] :
    Function.Injective (((pointsSheaf B W hW G hG).cohomologyPresheaf 1).map
      (genericPointToBase B W hW hK).op)
```

## Tag 0H8E, a remark

[Tag 0H8E](https://stacks.math.columbia.edu/tag/0H8E) in the Stacks Project.

**`AlgebraicGeometry.bijective_torsorSectionsRestrictGenericPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/AbelianSchemeTorsorSectionsRegular.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/AbelianSchemeTorsorSectionsRegular.lean#L129). The attribute's comment: “part (1): P(W) → P(K) is bijective for every fppf G-torsor P, with W noetherian, regular and integral and G → W an abelian scheme, exactly as in the source; no bound on the dimension of W. The surjectivity, that a rational section of P → W extends to a section, is proved from the extension of rational sections of proper group schemes over regular bases, GroupScheme.exists\_section\_extending\_of\_regular, which is established by induction on the dimension of the local rings (the surface case of Stacks 0AF9, then Krull's height theorem and algebraic Hartogs) in place of the Picard-scheme argument the source sketches; part (2) is fppfH1\_restriction\_genericPoint\_injective\_of\_isRegular”.

> **Stacks 0H8E, part (1).** Let `W` be a regular integral Noetherian scheme with function
> field `K` and let `G → W` be an abelian scheme. For every fppf `G`-torsor `P` the restriction map
> `P(W) → P(K)` on sections is bijective. No bound on the dimension of `W` enters.
>
> Injectivity is `AlgebraicGeometry.injective_torsorSectionsRestrictGenericPoint`. For
> surjectivity, a torsor with a section over `Spec K` is trivial
> (`AlgebraicGeometry.isTrivial_of_nonempty_sections_genericPoint_of_isRegular`), and by naturality
> of the trivialising isomorphism its restriction map is conjugate to the map `G(W) → G(K)`, which is
> surjective (`AlgebraicGeometry.surjective_torsorSectionsRestrictGenericPoint_trivialTorsor`).
>
> The hypotheses `hW`, `hK` and `hG` only say that `W`, `Spec K` and `G` lie in the big fppf site
> `B`; they fix the size of the site and assume nothing about torsors or sections.

```lean
public theorem bijective_torsorSectionsRestrictGenericPoint
    [IsIntegral W] [AlgebraicGeometry.IsNoetherian W] (hreg : IsRegular W)
    (hK : B.Contains (Spec W.functionField))
    (G : Over W) [GrpObj G] [IsAbelianScheme G] (hG : B.Contains G.left)
    (F : Stacks.Cohomology.Torsors.AbelianTorsor (pointsSheaf B W hW G hG)) :
    Function.Bijective (torsorSectionsRestrictGenericPoint B W hW hK G hG F)
```

**`AlgebraicGeometry.fppfH1_restriction_genericPoint_injective_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/AbelianSchemeTorsorSectionsRegular.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/AbelianSchemeTorsorSectionsRegular.lean#L169). The attribute's comment: “part (2): H¹\_fppf(W, G) → H¹\_fppf(Spec K, G) is injective, with W noetherian, regular and integral and G → W an abelian scheme, exactly as in the source; this is the conclusion of Stacks 0AF9 with its two-dimensionality assumption removed. It is derived from part (1), bijective\_torsorSectionsRestrictGenericPoint, as in the source. The source's further remarks, that regularity may be weakened to local factoriality of smooth W-schemes and the attribution of the argument, carry no assertion”.

> **Stacks 0H8E, part (2).** Let `W` be a regular integral Noetherian scheme with function
> field `K` and let `G → W` be an abelian scheme. Then the restriction map
> `H¹_fppf(W, G) → H¹_fppf(Spec K, G)` on first cohomology is injective. No bound on the dimension
> of `W` enters.
>
> As in the source, part (2) follows from part (1),
> `AlgebraicGeometry.bijective_torsorSectionsRestrictGenericPoint`: a class in the kernel is the
> class of a torsor with a section over `Spec K`, which by surjectivity on sections has a section
> over `W`, so is trivial. The hypotheses `hW`, `hK` and `hG` only place `W`, `Spec K` and `G` in
> the big fppf site `B`, and the instances on sheafification and `Ext` make the first cohomology
> `H¹_fppf` defined.

```lean
public theorem fppfH1_restriction_genericPoint_injective_of_isRegular
    [IsIntegral W] [AlgebraicGeometry.IsNoetherian W] (hreg : IsRegular W)
    (hK : B.Contains (Spec W.functionField))
    (G : Over W) [GrpObj G] [IsAbelianScheme G] (hG : B.Contains G.left)
    [HasSheafify (BigFppfOver.topology B W hW) AddCommGrpCat.{u}]
    [HasExt.{w} (Sheaf (BigFppfOver.topology B W hW) AddCommGrpCat.{u})] :
    Function.Injective (((pointsSheaf B W hW G hG).cohomologyPresheaf 1).map
      (genericPointToBase B W hW hK).op)
```

## Tag 0AFA, a lemma

[Tag 0AFA](https://stacks.math.columbia.edu/tag/0AFA) in the Stacks Project.

**`AlgebraicGeometry.Space.fppfH1_isAddTorsion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmoothGroupFirstCohomologyTorsion.lean, line 1103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmoothGroupFirstCohomologyTorsion.lean#L1103).

> **Stacks 0AFA.** The first fppf cohomology group of a smooth commutative group algebraic
> space over a field is torsion.

```lean
public theorem Space.fppfH1_isAddTorsion
    (k : Type u) [Field k]
    (B : AlgebraicGeometry.BigFppfSite.{u})
    (hk : B.Contains (Spec (.of k)))
    [HasSheafify (AlgebraicGeometry.BigFppfOver.topology B (Spec (.of k)) hk) AddCommGrpCat.{u}]
    [HasExt.{w} (Sheaf (AlgebraicGeometry.BigFppfOver.topology B (Spec (.of k)) hk)
      AddCommGrpCat.{u})]
    (G : Sheaf (AlgebraicGeometry.BigFppfOver.topology B (Spec (.of k)) hk)
      AddCommGrpCat.{u})
    (hG : AlgebraicGeometry.IsAlgebraicSpace B (Spec (.of k)) hk
      (G.obj ⋙ forget AddCommGrpCat))
    (hSmooth : AlgebraicGeometry.Space.IsSmooth B (Spec (.of k)) hk
      (terminal.from (G.obj ⋙ forget AddCommGrpCat))) :
    IsAddTorsion (Sheaf.H G 1)
```

## Tag 0AFB, a lemma

[Tag 0AFB](https://stacks.math.columbia.edu/tag/0AFB) in the Stacks Project.

**`Stacks.Examples.NonAlgebraicHomStack.Situation.exists_not_restriction_homStackClassifyingStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Stacks/NonAlgebraicHomStack/Main.lean, line 223](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Stacks/NonAlgebraicHomStack/Main.lean#L223). The attribute's comment: “for the Hom-stack Mor\_S(X, [S/A]) of the situation of Section 0AF8: k algebraically closed and not the algebraic closure of a finite field, S = Spec k⟦t⟧, X ⟶ S projective and flat with geometrically connected curves as fibres, X regular, the special fibre a nodal curve with smooth components whose dual graph has a loop of rational curves, A = A₀ ×\_k S for a non-zero abelian variety A₀, and [S/A] the quotient stack of the trivial action of A on S. The torsion of H¹(X, A), part (a) and part (b) are proved from these data. Not essentially surjective is stated as: some formal object over k⟦t⟧ admits no morphisms, over the closed immersions Sₙ ⟶ S, to an object over S. The index of the thickenings is shifted by one against the source: level n lies over Spec k⟦t⟧/(t^(n+1))”.

> **Stacks 0AFB.** In the situation of Section 0AF8, let `𝒳 = Mor_S(X, [S/A])`, with `[S/A]` the
> quotient stack of the trivial action of `A` on `S`. The functor `𝒳(S) ⟶ lim 𝒳(Sₙ)` is not
> essentially surjective: there is a formal object `ξ` of `𝒳` over the complete local ring `k⟦t⟧`,
> with `ξₙ` lying over `Sₙ = Spec (k⟦t⟧/(tⁿ⁺¹))`, such that no object `x` of `𝒳` admits morphisms
> `ξₙ ⟶ x` lying over the closed immersions `Sₙ ⟶ S`; in a category fibred in groupoids such
> morphisms are exactly the identifications of `ξₙ` with the restrictions `x|_{Sₙ}`.
>
> The fibre categories of `𝒳` are classified by `H¹(X ×_S -, A)`: the class in `H¹` of the torsor
> attached to an object of `[S/A]` (Stacks 04WM, 03AJ) is transported from the small model of
> `[S/A]` along its equivalence over the site with `[S/A]`.

```lean
theorem exists_not_restriction_homStackClassifyingStack :
    ∃ ξ : FormalObject B (base k) hS (sit.homStackClassifyingStack B hS).p,
      ξ.base = powerSeriesFormalBase k ∧
      (∀ n, (sit.homStackClassifyingStack B hS).p.obj (ξ.level n) = truncationObj B hS n) ∧
      ∀ (x : (sit.homStackClassifyingStack B hS).obj) (r : ∀ n, ξ.level n ⟶ x),
        ¬ ∀ n, (sit.homStackClassifyingStack B hS).p.IsHomLift
          (restrictionToBase B (base k) hS (powerSeriesFormalBase k) hS
            (powerSeriesFormalBase_contains B hS) n) (r n)
```

## Tag 0AFC, a proposition

[Tag 0AFC](https://stacks.math.columbia.edu/tag/0AFC) in the Stacks Project.

**`Stacks.Examples.NonAlgebraicHomStack.Situation.not_isAlgebraicStack_homStackClassifyingStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Stacks/NonAlgebraicHomStack/Main.lean, line 262](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Stacks/NonAlgebraicHomStack/Main.lean#L262). The attribute's comment: “for the Hom-stack Mor\_S(X, [S/A]) of the situation of Section 0AF8: k algebraically closed and not the algebraic closure of a finite field, S = Spec k⟦t⟧, X ⟶ S projective and flat with geometrically connected curves as fibres, X regular, the special fibre a nodal curve with smooth components whose dual graph has a loop of rational curves, A = A₀ ×\_k S for a non-zero abelian variety A₀, and [S/A] the quotient stack of the trivial action of A on S. Derived from the proof of 0AFB and from Stacks 07X8 as proved in this library (Deformation.Artin.isEquivalence\_approximationFunctor\_algebraicStacks)”.

> **Stacks 0AFC.** In the situation of Section 0AF8, the Hom-stack `𝒳 = Mor_S(X, [S/A])`, with
> `[S/A]` the quotient stack of the trivial action of `A` on `S`, is not an algebraic stack. It is
> equivalent over the site to the Hom-stack into the small model of `[S/A]`
> (`CategoryTheory.BasedCategory.basePullbackEquivalenceOver`), which is not algebraic by
> `Stacks.Examples.NonAlgebraicHomStack.Situation.not_isAlgebraicStack_homStack`, and algebraicity
> is invariant under equivalence over the site (Stacks 03YQ).

```lean
theorem not_isAlgebraicStack_homStackClassifyingStack :
    ¬ Stack.IsAlgebraicStack.{u, w} B (base k) hS (sit.homStackClassifyingStack B hS)
```

## Tag 0AFD, a remark

[Tag 0AFD](https://stacks.math.columbia.edu/tag/0AFD) in the Stacks Project.

**`Stacks.Examples.NonAlgebraicHomStack.not_forall_isAlgebraicStack_of_isAbsolutelySeparated_of_not_isEffective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Stacks/HomStackSeparatedTargetCriterionUnconditional.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Stacks/HomStackSeparatedTargetCriterionUnconditional.lean#L144). The attribute's comment: “the mathematical assertion of the remark and not its bibliography: the criterion the Erratum asserts -- that a Hom-stack is algebraic as soon as its target is separated -- is false, because the target [S/A] of a Hom-stack with a non-effective formal object is separated. Separatedness of [S/A] is derived from Stacks 0DTY part (6) read at the groupoid of the trivial action and from separatedness of the stack of the affine base Spec k[[t]]; A is any group algebraic space over S that is proper, flat and locally of finite presentation, the clauses of the source's abelian scheme that the remark uses. Non-algebraicity is derived from Stacks 07X8 of this library. The Hom-stack Mor\_S(X, [S/A]) is not defined in this library, so Mor is an arbitrary assignment and the source's Lemma 0AFB for it -- a formal object of Mor Y Z that is not effective -- is the input hξ (0AFB and 0AFC: item C6003). The bibliographic claims about AokiHomStacks and its Erratum are cited in the docstring only”.

> **Stacks 0AFD**, the mathematical assertion of the remark: the criterion that a Hom-stack is
> algebraic whenever its target is separated is false.
>
> Let `S = Spec k⟦t⟧`, let `A` be a group algebraic space over `S` which is proper, flat and locally
> of finite presentation, and let `𝒵` be an algebraic stack equivalent over the site to the quotient
> stack `[S/A]` of the trivial action of `A`. Let `Mor` assign a category over the site to a pair of
> algebraic stacks, let `𝒴` be an algebraic stack and suppose `Mor 𝒴 𝒵` has a formal object that is
> not effective. Then it is not the case that `Mor 𝒴' 𝒵'` is an algebraic stack for every `𝒴'` and
> every separated `𝒵'`.
>
> * `[S/A]` is separated by Stacks 0DTY part (6) at the trivial-action groupoid
>   (`AlgebraicGeometry.Stack.isAbsolutelySeparated_quotientStack_trivialAction`), the algebraic
>   stack of the affine scheme `S` being separated by
>   `AlgebraicGeometry.Stack.isAbsolutelySeparated_schemeStack_of_isAffine`.
> * An algebraic `Mor 𝒴 𝒵` would have every formal object effective by Stacks 07X8,
>   `Deformation.Artin.FormalObject.isEffective_of_isAlgebraicStack_of_isFiberedInGroupoids`.
>
> **The group `A`.** The source's `A = A₀ × S` is an abelian scheme over `S`, and properness, flatness
> and local finite presentation of `A ⟶ S` are among the defining conditions of an abelian scheme
> (`AlgebraicGeometry.IsAbelianScheme` extends `IsProper`, `Flat` and
> `LocallyOfFinitePresentation`). They are the only part of that assumption the remark uses, so they
> are stated, on the algebraic-space side, as `hproper`, `hflat` and `hlfp`; the statement therefore
> covers every such group algebraic space, the source's abelian scheme among them.
>
> **The universes of `Mor`.** The fibre of the source's Hom-stack `Mor_S(𝒴, 𝒵)` over an `S`-scheme
> `T` consists of 1-morphisms `(Sch/T)_{fppf} ×_S 𝒴 ⟶ 𝒵` between categories whose objects lie in the
> universe `u + 1` of the site's schemes; so its total category has objects in `u + 1`, and its
> morphisms (natural transformations) in `u + 1` as well. `Mor` is accordingly a based category with
> objects in `u + 1` and morphisms in an arbitrary universe `v`, which contains the source's case.
>
> **The input `hξ`.** This library defines no Hom-stack of two algebraic stacks, so `Mor` is an
> arbitrary assignment and the non-effectivity of a formal object of `Mor 𝒴 [S/A]` — the source's
> Lemma 0AFB, read through its identification of the fibres of `Mor_S(X, [S/A])` with groupoids of
> `A₀`-torsors — is the input `hξ`. Lemma 0AFB and Proposition 0AFC belong to item C6003 of
> lane rb-201 (`StacksFrontier.Examples.Stacks.NonAlgebraicHomStack`).

```lean
public theorem not_forall_isAlgebraicStack_of_isAbsolutelySeparated_of_not_isEffective
    {k : Type u} [Field k] (B : BigFppfSite.{u}) (hS : B.Contains (base k))
    (hZ : B.Contains (⊤_ Scheme.{u}))
    (A : Over (Space.terminalSpace B (base k) hS).obj) [GrpObj A]
    (hA : IsAlgebraicSpace B (base k) hS A.left)
    (Agpd : Space.ActionGroupoidConstruction (Space.terminalSpace B (base k) hS) A
      (𝟙_ (Over (Space.terminalSpace B (base k) hS).obj)) hA
      (Space.terminalSpace B (base k) hS).property)
    (𝒵 : Stack.AlgebraicStacks.{u, w} B (base k) hS)
    (hequiv : Nonempty (StacksRepresentableCFG.EquivalenceOver
      (Stack.quotientStack Agpd.groupoid).p 𝒵.val.val.p))
    (hproper : Space.IsProper B (base k) hS A.hom)
    (hflat : Space.IsFlat B (base k) hS A.hom)
    (hlfp : Space.IsLocallyOfFinitePresentation B (base k) hS A.hom)
    (Mor : Stack.AlgebraicStacks.{u, w} B (base k) hS →
      Stack.AlgebraicStacks.{u, w} B (base k) hS →
      BasedCategory.{v, u + 1} (BigFppfOver B (base k) hS))
    (𝒴 : Stack.AlgebraicStacks.{u, w} B (base k) hS)
    (hp : (Mor 𝒴 𝒵).p.IsFiberedInGroupoids)
    (hξ : ∃ ξ : Deformation.Artin.FormalObject B (base k) hS (Mor 𝒴 𝒵).p,
      ¬ Deformation.Artin.FormalObject.IsEffective B (base k) hS (Mor 𝒴 𝒵).p hp ξ) :
    ¬ ∀ 𝒴' 𝒵' : Stack.AlgebraicStacks.{u, w} B (base k) hS,
        Stack.AlgebraicStacks.IsAbsolutelySeparated.{u, w} B (base k) hS hZ 𝒵' →
          Stack.IsAlgebraicStack.{u, w} B (base k) hS (Mor 𝒴' 𝒵')
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.74, Tag 0AF8](https://stacks.math.columbia.edu/tag/0AF8)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
