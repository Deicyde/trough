---
declaration: section
origin: cited
lean: AlgebraicGeometry.fppfH1_restriction_genericPoint_injective, AlgebraicGeometry.injective_torsorSectionsRestrictGenericPoint, AlgebraicGeometry.fppfH1_restriction_genericPoint_injective_of_isTrivial, AlgebraicGeometry.Space.fppfH1_isAddTorsion, Stacks.Examples.NonAlgebraicHomStack.exists_compatible_ne_restrictTotal, Stacks.Examples.NonAlgebraicHomStack.not_surjective_toCompatibleSystems, Stacks.Examples.NonAlgebraicHomStack.not_isAlgebraicStack_of_not_essSurj_approximationFunctor, Stacks.Examples.NonAlgebraicHomStack.not_isAlgebraicStack_of_exists_not_isEffective
statement: formalized
proof: formalized
---

# 110.74 An example of a non-algebraic Hom-stack

Section 110.74 of the Stacks Project, [Tag 0AF8](https://stacks.math.columbia.edu/tag/0AF8). 6 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AF9, a lemma

[Tag 0AF9](https://stacks.math.columbia.edu/tag/0AF9) in the Stacks Project.

**`AlgebraicGeometry.fppfH1_restriction_genericPoint_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/AbelianSchemeFirstCohomologyGenericPoint.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/AbelianSchemeFirstCohomologyGenericPoint.lean#L183). The attribute's comment: “with the sketch's conclusion that a G-torsor with a K-point is trivial as htrivial”.

> **Stacks 0AF9.** Let `W` be a two dimensional regular integral Noetherian scheme with
> function field `K` and let `G → W` be an abelian scheme. Then the restriction map
> `H¹_fppf(W, G) → H¹_fppf(Spec K, G)` along the generic point is injective.
>
> The geometric conclusion of the source's sketch of proof — an fppf `G`-torsor with a section
> over `Spec K` is trivial — is the hypothesis `htrivial`; the sketch obtains it from a step the
> source itself leaves to an unwritten reference on resolving indeterminacies of morphisms for
> surfaces. See the implementation notes of this file.

```lean
public theorem fppfH1_restriction_genericPoint_injective
    [IsIntegral W] [AlgebraicGeometry.IsNoetherian W] (_hreg : IsRegular W)
    (_hdim : topologicalKrullDim (W : Type u) = (2 : WithBot ℕ∞))
    (hK : B.Contains (Spec W.functionField))
    (G : Over W) [GrpObj G] [IsAbelianScheme G] (hG : B.Contains G.left)
    [HasSheafify (BigFppfOver.topology B W hW) AddCommGrpCat.{u}]
    [HasExt.{w} (Sheaf (BigFppfOver.topology B W hW) AddCommGrpCat.{u})]
    (htrivial : ∀ F : Stacks.Cohomology.Torsors.AbelianTorsor (pointsSheaf B W hW G hG),
      Nonempty (F.1.presheaf.obj (op (genericPointObj B W hW hK))) → F.1.IsTrivial) :
    Function.Injective (((pointsSheaf B W hW G hG).cohomologyPresheaf 1).map
      (genericPointToBase B W hW hK).op)
```

## Tag 0H8E, a remark

[Tag 0H8E](https://stacks.math.columbia.edu/tag/0H8E) in the Stacks Project.

**`AlgebraicGeometry.injective_torsorSectionsRestrictGenericPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/AbelianSchemeTorsorSectionsGenericPoint.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/AbelianSchemeTorsorSectionsGenericPoint.lean#L170). The attribute's comment: “part (1), the injectivity half, for every G-torsor and with the two-dimensionality hypothesis of Stacks 0AF9 absent: the hypotheses on W are exactly noetherian, regular and integral. The surjectivity half of part (1) is the statement that the schematic closure of a rational section of P → W is a section; it is not proved, and is the hypothesis hsurj of bijective_torsorSectionsRestrictGenericPoint_of_surjective, which states part (1) in full. The tag obtains surjectivity by identifying G with the identity component of the Picard scheme of the dual abelian scheme and extending a generically defined invertible sheaf over the regular base, and neither the dual abelian scheme nor that identity component is available in this library”.

> **Stacks 0H8E, the injectivity half of part (1).** Let `W` be a regular integral Noetherian
> scheme with function field `K` and let `G → W` be an abelian scheme. For every fppf `G`-torsor
> `P` the restriction map `P(W) → P(K)` on sections is injective. No hypothesis on the dimension of
> `W` enters.
>
> A torsor with no section over `W` has nothing to separate. A torsor with one is trivial, and by
> naturality of the trivialising isomorphism its restriction map is then conjugate to the
> restriction map `G(W) → G(K)` on the points of `G`, which is injective.

```lean
public theorem injective_torsorSectionsRestrictGenericPoint
    [IsIntegral W] [AlgebraicGeometry.IsNoetherian W] (_hreg : IsRegular W)
    (hK : B.Contains (Spec W.functionField))
    (G : Over W) [GrpObj G] [IsAbelianScheme G] (hG : B.Contains G.left)
    (F : Stacks.Cohomology.Torsors.AbelianTorsor (pointsSheaf B W hW G hG)) :
    Function.Injective (torsorSectionsRestrictGenericPoint B W hW hK G hG F)
```

**`AlgebraicGeometry.fppfH1_restriction_genericPoint_injective_of_isTrivial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/AbelianSchemeTorsorSectionsGenericPoint.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/AbelianSchemeTorsorSectionsGenericPoint.lean#L232). The attribute's comment: “part (2): the conclusion of Stacks 0AF9 with its two-dimensionality hypothesis dropped, which is what the tag asserts; the hypotheses on W are exactly noetherian, regular and integral. As in Stacks 0AF9 the geometric content is the hypothesis htrivial, that a G-torsor with a section over Spec K is trivial. The tag derives part (2) from its part (1), the bijectivity of P(W) → P(K): the injectivity half of part (1) is proved here, in injective_torsorSectionsRestrictGenericPoint, and its surjectivity half -- the statement that the schematic closure of a rational section of P → W is a section, which supplies htrivial by fppfH1_restriction_genericPoint_injective_of_surjective_sections -- is not, the tag obtaining it by identifying G with the identity component of the Picard scheme of the dual abelian scheme and extending a generically defined invertible sheaf over the regular base, and neither the dual abelian scheme nor that identity component is available in this library. The tag's further remarks, that regularity may be weakened to local factoriality of smooth W-schemes and the attribution of the argument, carry no assertion”.

> **Stacks 0H8E, part (2).** Let `W` be a regular integral Noetherian scheme with function
> field `K` and let `G → W` be an abelian scheme. Then the restriction map
> `H¹_fppf(W, G) → H¹_fppf(Spec K, G)` on first cohomology is injective. No hypothesis on the
> dimension of `W` enters.
>
> A class in the kernel of the restriction map is the class of a torsor having a section over
> `Spec K`, and such a torsor is trivial by the hypothesis `htrivial`, so the class is zero.

```lean
public theorem fppfH1_restriction_genericPoint_injective_of_isTrivial
    [IsIntegral W] [AlgebraicGeometry.IsNoetherian W] (_hreg : IsRegular W)
    (hK : B.Contains (Spec W.functionField))
    (G : Over W) [GrpObj G] [IsAbelianScheme G] (hG : B.Contains G.left)
    [HasSheafify (BigFppfOver.topology B W hW) AddCommGrpCat.{u}]
    [HasExt.{w} (Sheaf (BigFppfOver.topology B W hW) AddCommGrpCat.{u})]
    (htrivial : ∀ F : Stacks.Cohomology.Torsors.AbelianTorsor (pointsSheaf B W hW G hG),
      Nonempty (F.1.presheaf.obj (op (genericPointObj B W hW hK))) → F.1.IsTrivial) :
    Function.Injective (((pointsSheaf B W hW G hG).cohomologyPresheaf 1).map
      (genericPointToBase B W hW hK).op)
```

## Tag 0AFA, a lemma

[Tag 0AFA](https://stacks.math.columbia.edu/tag/0AFA) in the Stacks Project.

**`AlgebraicGeometry.Space.fppfH1_isAddTorsion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmoothGroupFirstCohomologyTorsion.lean, line 1103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmoothGroupFirstCohomologyTorsion.lean#L1103).

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

**`Stacks.Examples.NonAlgebraicHomStack.exists_compatible_ne_restrictTotal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Stacks/NonAlgebraicHomStack.lean, line 319](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Stacks/NonAlgebraicHomStack.lean#L319). The attribute's comment: “the source's own reduction of the tag to the non-surjectivity of H¹(X, A) → lim H¹(Xₙ, A), with the three inputs of its proof as the hypotheses htorsion (0AF9 and 0AFA), hsurjective (part (b)) and hnotTorsion (part (a)); the identification of the Hom-stack's fibre categories with groupoids of torsors, by which the tag's essential surjectivity is this surjectivity, is not formalized”.

> **Stacks 0AFB**, in the shape to which the source reduces it. For the example of a
> non-algebraic Hom-stack over `S = Spec k⟦t⟧`, with `Xₙ = X ×_S Sₙ` the thickenings of the
> special fibre and `A` the constant abelian scheme, there is a compatible system of classes
> in `H¹_fppf(Xₙ, A)` which is the restriction of no class in `H¹_fppf(X, A)`.
>
> The system is constructed: its level `0` is a class of infinite order, supplied by
> `hnotTorsion`, and each next level is a preimage of the level below under the surjection of
> `hsurjective`. No class on `X` restricts to it, because a class on `X` has finite order by
> `htorsion` and hence so does its restriction to `X₀`.

```lean
public theorem exists_compatible_ne_restrictTotal
    (htorsion : IsAddTorsion (Sheaf.H' 𝒜 1 (totalObj B hS fX hX)))
    (hsurjective : ∀ n, Function.Surjective (restrictSucc B hS fX hXn 𝒜 n))
    (hnotTorsion :
      ¬ IsAddTorsion (Sheaf.H' 𝒜 1 (thickeningObj B hS fX hXn 0))) :
    ∃ s : ∀ n, Sheaf.H' 𝒜 1 (thickeningObj B hS fX hXn n),
      (¬ IsOfFinAddOrder (s 0)) ∧
      (∀ n, restrictSucc B hS fX hXn 𝒜 n (s (n + 1)) = s n) ∧
      ∀ ξ : Sheaf.H' 𝒜 1 (totalObj B hS fX hX),
        ∃ n, restrictTotal B hS fX hX hXn 𝒜 n ξ ≠ s n
```

**`Stacks.Examples.NonAlgebraicHomStack.not_surjective_toCompatibleSystems`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Stacks/NonAlgebraicHomStack.lean, line 342](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Stacks/NonAlgebraicHomStack.lean#L342). The attribute's comment: “the source's own reduction of the tag to the non-surjectivity of H¹(X, A) → lim H¹(Xₙ, A), with the three inputs of its proof as the hypotheses htorsion (0AF9 and 0AFA), hsurjective (part (b)) and hnotTorsion (part (a)); the identification of the Hom-stack's fibre categories with groupoids of torsors, by which the tag's essential surjectivity is this surjectivity, is not formalized”.

> **Stacks 0AFB**, in the shape to which the source reduces it: the comparison map
> `H¹_fppf(X, A) ⟶ lim H¹_fppf(Xₙ, A)` is not surjective.

```lean
public theorem not_surjective_toCompatibleSystems
    (htorsion : IsAddTorsion (Sheaf.H' 𝒜 1 (totalObj B hS fX hX)))
    (hsurjective : ∀ n, Function.Surjective (restrictSucc B hS fX hXn 𝒜 n))
    (hnotTorsion :
      ¬ IsAddTorsion (Sheaf.H' 𝒜 1 (thickeningObj B hS fX hXn 0))) :
    ¬ Function.Surjective (toCompatibleSystems B hS fX hX hXn 𝒜)
```

## Tag 0AFC, a proposition

[Tag 0AFC](https://stacks.math.columbia.edu/tag/0AFC) in the Stacks Project.

**`Stacks.Examples.NonAlgebraicHomStack.not_isAlgebraicStack_of_not_essSurj_approximationFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Stacks/NonAlgebraicHomStack.lean, line 382](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Stacks/NonAlgebraicHomStack.lean#L382). The attribute's comment: “the deduction of the tag from Stacks 07X8 and Stacks 0AFB only, and not about the tag's subject: for a category fibred in groupoids over the big fppf site of a locally Noetherian base, 07X8 as the named hypothesis h07X8 together with the failure of essential surjectivity of the comparison functor of Stacks 07X6 for that category give non-algebraicity. The tag's subject, the Hom-stack Mor_S(X, [S/A]), cannot be named — this library defines no Hom-stack of two algebraic stacks — so 0AFC is not asserted of it, and the implication is not instantiated at the example: the 0AFB available in this file is the non-surjectivity of H¹(X, A) → lim H¹(Xₙ, A), and its identification with the failure of essential surjectivity hypothesised here is the source's unformalized computation of the Hom-stack's fibre categories. 07X8 is a hypothesis, not a result of this library”.

> **Stacks 0AFC**, as the deduction the source makes, for a hypothesised subject. Let `B` be a
> big fppf site, `S` a locally Noetherian scheme in it and `𝒳` a category over the big fppf site
> over `S` which is fibred in groupoids. Assume Stacks 07X8, as the hypothesis `h07X8`: every
> algebraic stack over `S` has an equivalence for its comparison functor of Stacks 07X6, from
> objects over a Noetherian complete local base to compatible systems over the infinitesimal
> thickenings of its closed point. If that comparison functor is *not* essentially surjective for
> `𝒳` — which is Stacks 0AFB for the source's `𝒳 = Mor_S(X, [S/A])` — then `𝒳` is not an
> algebraic stack.
>
> The source's `𝒳` cannot be named here: this library has no Hom-stack of two algebraic stacks.
> See the module documentation.

```lean
public theorem not_isAlgebraicStack_of_not_essSurj_approximationFunctor
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    [IsLocallyNoetherian S]
    (𝒳 : CategoryTheory.BasedCategory.{v, t} (AlgebraicGeometry.BigFppfOver B S hS))
    (hp : 𝒳.p.IsFiberedInGroupoids)
    (h07X8 : ∀ 𝒴 : CategoryTheory.BasedCategory.{v, t}
        (AlgebraicGeometry.BigFppfOver B S hS),
        AlgebraicGeometry.Stack.IsAlgebraicStack.{u, w} B S hS 𝒴 →
          ∀ hq : 𝒴.p.IsFiberedInGroupoids,
            (Deformation.Artin.approximationFunctor B S hS 𝒴.p hq).IsEquivalence)
    (h0AFB : ¬ (Deformation.Artin.approximationFunctor B S hS 𝒳.p hp).EssSurj) :
    ¬ AlgebraicGeometry.Stack.IsAlgebraicStack.{u, w} B S hS 𝒳
```

**`Stacks.Examples.NonAlgebraicHomStack.not_isAlgebraicStack_of_exists_not_isEffective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Stacks/NonAlgebraicHomStack.lean, line 414](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Stacks/NonAlgebraicHomStack.lean#L414). The attribute's comment: “the deduction of the tag from Stacks 07X8 and Stacks 0AFB only, and not about the tag's subject: for a category fibred in groupoids over the big fppf site of a locally Noetherian base, 07X8 as the named hypothesis h07X8 together with a formal object of that category that is not effective give non-algebraicity. The tag's subject, the Hom-stack Mor_S(X, [S/A]), cannot be named — this library defines no Hom-stack of two algebraic stacks — so 0AFC is not asserted of it, and the implication is not instantiated at the example: the 0AFB available in this file is the non-surjectivity of H¹(X, A) → lim H¹(Xₙ, A), and its identification with the non-effective formal object hypothesised here is the source's unformalized computation of the Hom-stack's fibre categories. 07X8 is a hypothesis, not a result of this library”.

> **Stacks 0AFC**, in the vocabulary of effective formal objects. Under Stacks 07X8 as the
> hypothesis `h07X8`, a category fibred in groupoids over the big fppf site of a locally
> Noetherian base which has a formal object that is not effective, in the sense of Stacks 07X7,
> is not an algebraic stack. This is the form in which the source's Remark 0AFD diagnoses the
> example: "the problem is the non-effectivity of formal objects for `Mor_S(X, [S/A])`".
>
> The source's `𝒳` cannot be named here: this library has no Hom-stack of two algebraic stacks.
> See the module documentation.

```lean
public theorem not_isAlgebraicStack_of_exists_not_isEffective
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    [IsLocallyNoetherian S]
    (𝒳 : CategoryTheory.BasedCategory.{v, t} (AlgebraicGeometry.BigFppfOver B S hS))
    (hp : 𝒳.p.IsFiberedInGroupoids)
    (h07X8 : ∀ 𝒴 : CategoryTheory.BasedCategory.{v, t}
        (AlgebraicGeometry.BigFppfOver B S hS),
        AlgebraicGeometry.Stack.IsAlgebraicStack.{u, w} B S hS 𝒴 →
          ∀ hq : 𝒴.p.IsFiberedInGroupoids,
            (Deformation.Artin.approximationFunctor B S hS 𝒴.p hq).IsEquivalence)
    (h0AFB : ∃ ξ : Deformation.Artin.FormalObject B S hS 𝒳.p,
      ¬ Deformation.Artin.FormalObject.IsEffective B S hS 𝒳.p hp ξ) :
    ¬ AlgebraicGeometry.Stack.IsAlgebraicStack.{u, w} B S hS 𝒳
```

**`Stacks.Examples.NonAlgebraicHomStack.not_isAlgebraicStack_powerSeriesBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Stacks/NonAlgebraicHomStack.lean, line 446](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Stacks/NonAlgebraicHomStack.lean#L446). The attribute's comment: “the deduction of the tag from Stacks 07X8 and Stacks 0AFB only, over the section's base S = Spec k⟦t⟧ but not about the tag's subject: 07X8 as the named hypothesis h07X8 together with a formal object that is not effective give non-algebraicity. The tag's subject, the Hom-stack Mor_S(X, [S/A]), cannot be named — this library defines no Hom-stack of two algebraic stacks — so 0AFC is not asserted of it, and the implication is not instantiated at the example: the 0AFB available in this file is the non-surjectivity of H¹(X, A) → lim H¹(Xₙ, A), and its identification with the non-effective formal object hypothesised here is the source's unformalized computation of the Hom-stack's fibre categories. 07X8 is a hypothesis, not a result of this library”.

> **Stacks 0AFC** over the section's own base `S = Spec k⟦t⟧`. Under Stacks 07X8 as the
> hypothesis `h07X8`, a category fibred in groupoids over the big fppf site over `S` which has a
> formal object that is not effective is not an algebraic stack. Only the base of the source's
> example is pinned down here; its `𝒳 = Mor_S(X, [S/A])` still cannot be named, so `𝒳` remains a
> hypothesis. See the module documentation.

```lean
public theorem not_isAlgebraicStack_powerSeriesBase
    {k : Type u} [Field k] (B : AlgebraicGeometry.BigFppfSite.{u})
    (hS : B.Contains (base k))
    (𝒳 : CategoryTheory.BasedCategory.{v, t} (AlgebraicGeometry.BigFppfOver B (base k) hS))
    (hp : 𝒳.p.IsFiberedInGroupoids)
    (h07X8 : ∀ 𝒴 : CategoryTheory.BasedCategory.{v, t}
        (AlgebraicGeometry.BigFppfOver B (base k) hS),
        AlgebraicGeometry.Stack.IsAlgebraicStack.{u, w} B (base k) hS 𝒴 →
          ∀ hq : 𝒴.p.IsFiberedInGroupoids,
            (Deformation.Artin.approximationFunctor B (base k) hS 𝒴.p hq).IsEquivalence)
    (h0AFB : ∃ ξ : Deformation.Artin.FormalObject B (base k) hS 𝒳.p,
      ¬ Deformation.Artin.FormalObject.IsEffective B (base k) hS 𝒳.p hp ξ) :
    ¬ AlgebraicGeometry.Stack.IsAlgebraicStack.{u, w} B (base k) hS 𝒳
```

## Tag 0AFD, a remark

[Tag 0AFD](https://stacks.math.columbia.edu/tag/0AFD) in the Stacks Project.

**`Stacks.Examples.NonAlgebraicHomStack.not_forall_isAlgebraicStack_of_isAbsolutelySeparated_target`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Stacks/HomStackSeparatedTargetCriterion.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Stacks/HomStackSeparatedTargetCriterion.lean#L124). The attribute's comment: “the mathematical assertion of the remark and not its bibliography: the criterion the Erratum asserts -- that a Hom-stack is algebraic as soon as its target is separated -- is false, because the target [S/A] of the non-algebraic Hom-stack of Stacks 0AFC is separated. Both legs are derived, not hypothesised: separatedness of [S/A] from Stacks 0DTY part (6) read at the groupoid of the trivial action, and non-algebraicity from Stacks 0AFC of StacksFrontier.Examples.Stacks.NonAlgebraicHomStack. NOT carried: the bibliographic claims (that Stacks 0AFC contradicts Theorem 1.1 of AokiHomStacks, and that the criterion is the Erratum's), which are cited in the docstring only. The tag's subject, the Hom-stack Mor_S(Y, Z), cannot be named -- this library defines no Hom-stack of two algebraic stacks -- so the criterion is stated for an arbitrary assignment Mor of a based category to a pair of algebraic stacks, and the source's unformalized identification of the Hom-stack's fibre categories with groupoids of torsors is the hypothesis h0AFB, a non-effective formal object of Mor Y Z. Stacks 07X8 is the hypothesis h07X8 and is not a result of this library; separatedness inherits from Stacks 0DTY, for the source's unqualified (absolute) separatedness, the hypothesis hBase on the algebraic stack of the base scheme”.

> **Stacks 0AFD**, the mathematical assertion the remark makes: the criterion that a Hom-stack
> is algebraic whenever its target is separated is false.
>
> Let `S = Spec k⟦t⟧`, let `A` be a group algebraic space over the terminal algebraic space over
> `S` which is proper, flat and locally of finite presentation — the source's abelian scheme — and
> let `𝒵` be an algebraic stack equivalent over the site to the quotient stack of the trivial
> action of `A`, that is to `[S/A]`. Let `Mor` be any assignment of a based category over the site
> to a pair of algebraic stacks over `S`, let `𝒴` be an algebraic stack and suppose, as the source
> computes, that `Mor 𝒴 𝒵` has a formal object which is not effective. Then, assuming Stacks 07X8,
> it is *not* the case that `Mor 𝒴' 𝒵'` is an algebraic stack for every `𝒴'` and every separated
> `𝒵'`.
>
> The two legs are derived: `[S/A]` is separated by Stacks 0DTY part (6) at the trivial-action
> groupoid, and `Mor 𝒴 𝒵` is not algebraic by Stacks 0AFC of the neighbouring module.
> See the module documentation.

```lean
public theorem not_forall_isAlgebraicStack_of_isAbsolutelySeparated_target
    {k : Type u} [Field k] (B : BigFppfSite.{u}) (hS : B.Contains (base k))
    (hZ : B.Contains (⊤_ Scheme.{u}))
    (hBase : Stack.AlgebraicStacks.IsAbsolutelySeparated.{u, w} B (base k) hS hZ
      (Stack.schemeStack.{u, w} B (base k) hS (Over.mk (𝟙 (B.obj hS)))))
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
      BasedCategory.{v, t} (BigFppfOver B (base k) hS))
    (𝒴 : Stack.AlgebraicStacks.{u, w} B (base k) hS)
    (hp : (Mor 𝒴 𝒵).p.IsFiberedInGroupoids)
    (h07X8 : ∀ 𝒲 : BasedCategory.{v, t} (BigFppfOver B (base k) hS),
        Stack.IsAlgebraicStack.{u, w} B (base k) hS 𝒲 →
          ∀ hq : 𝒲.p.IsFiberedInGroupoids,
            (Deformation.Artin.approximationFunctor B (base k) hS 𝒲.p hq).IsEquivalence)
    (h0AFB : ∃ ξ : Deformation.Artin.FormalObject B (base k) hS (Mor 𝒴 𝒵).p,
      ¬ Deformation.Artin.FormalObject.IsEffective B (base k) hS (Mor 𝒴 𝒵).p hp ξ) :
    ¬ ∀ 𝒴' 𝒵' : Stack.AlgebraicStacks.{u, w} B (base k) hS,
        Stack.AlgebraicStacks.IsAbsolutelySeparated.{u, w} B (base k) hS hZ 𝒵' →
          Stack.IsAlgebraicStack.{u, w} B (base k) hS (Mor 𝒴' 𝒵')
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.74, Tag 0AF8](https://stacks.math.columbia.edu/tag/0AF8)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
