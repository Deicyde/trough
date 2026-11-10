---
declaration: section
origin: cited
lean: Stacks.Algebraization.completion_hasProperSupport, Stacks.Algebraization.completionFunctorProperOver, Stacks.Algebraization.isEquivalence_completionFunctorProperOver_holds, AlgebraicGeometry.AdicCoherentModuleSystem, AlgebraicGeometry.adicThickeningCompletionFunctor, AlgebraicGeometry.hasProperSupport_of_isProper_adicBaseChange, AlgebraicGeometry.isEquivalence_adicThickeningCompletionFunctor, AlgebraicGeometry.isEquivalence_adicThickeningTransitionCompletionFunctor
statement: formalized
proof: formalized
---

# 30.27 Grothendieck's existence theorem, III

Section 30.27 of the Stacks Project, [Tag 0CYW](https://stacks.math.columbia.edu/tag/0CYW). 3 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 088D, an equation

[Tag 088D](https://stacks.math.columbia.edu/tag/088D) in the Stacks Project.

**`Stacks.Algebraization.completion_hasProperSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/Basic.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/Basic.lean#L111). The attribute's comment: “proper support of the completion”.

> **Stacks 088D.** The first term of the completion of a coherent sheaf whose support is
> proper over the base again has support proper over the base.
>
> That term is the quotient `F / I · F`, so its support is a closed subset of the support of `F`,
> and a closed subset of a closed subset proper over the base is proper over the base.

```lean
public theorem completion_hasProperSupport
    (A : Type u) [CommRing A] [IsNoetherianRing A] (I : Ideal A)
    {X : Scheme.{u}} (f : X ⟶ Spec (.of A)) [LocallyOfFiniteType f]
    (F : CoherentModulesProperOver f) :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian f
    HasProperSupport f
      (((completionFunctor X (baseIdealSheaf A I f)).obj F.obj).obj.obj (op 0))
```

**`Stacks.Algebraization.completionFunctorProperOver`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/Basic.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/Basic.lean#L144). The attribute's comment: “the functor”.

> **Stacks 088D.** The completion functor of Stacks 0880, restricted to the coherent sheaves
> and the coherent adic systems whose support is proper over the affine base.

```lean
public noncomputable def completionFunctorProperOver
    (A : Type u) [CommRing A] [IsNoetherianRing A] (I : Ideal A)
    {X : Scheme.{u}} (f : X ⟶ Spec (.of A)) [LocallyOfFiniteType f] :
    CoherentModulesProperOver f ⥤ CoherentAdicSystemsProperOver f (baseIdealSheaf A I f)
```

## Tag 088E, a theorem

[Tag 088E](https://stacks.math.columbia.edu/tag/088E) in the Stacks Project.

**`Stacks.Algebraization.isEquivalence_completionFunctorProperOver_holds`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/AdicUnitConditionDescent.lean, line 343](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/AdicUnitConditionDescent.lean#L343). The attribute's comment: “Grothendieck's existence theorem: A Noetherian and complete with respect to I, X separated and of finite type over A; the functor of 088D from coherent O\_X-modules with support proper over A to coherent I-adic systems with support proper over A is an equivalence”. References: EGA III (5.2.5), “more general”; EGA III (5.2.6), “more general”.

> **[Stacks, Tag 088E], Grothendieck's existence theorem.** Let `A` be a Noetherian ring
> complete with respect to an ideal `I` and let `f : Z ⟶ Spec A` be separated and of finite type
> (`IsSeparated`, `LocallyOfFiniteType` and `QuasiCompact`). Then the functor of [Stacks, Tag 088D]
>
>   `Coh_{support proper over A}(𝒪_Z) ⥤ Coh_{support proper over A}(Z, I 𝒪_Z)`
>
> is an equivalence.
>
> `Stacks.Algebraization.isEquivalence_completionFunctorProperOver_of_adicBaseChangeUnitCondition`
> at `Stacks.Algebraization.hasAdicBaseChangeUnitCondition`. Following the source, the proof reduces
> to Stacks 088C on the closed subschemes of `Z` proper over `A`, after showing that every coherent
> adic system with support proper over `A` is annihilated by the ideal sheaf of such a subscheme
> (Chow's lemma, the projective case 0885, and Stacks 088B through
> `Stacks.Algebraization.transport_of_isDirectImageComparison`).
>
> This is the carrier of Stacks 088E: it takes no input beyond the source's hypotheses, and
> supersedes the conditional forms
> `Stacks.Algebraization.isEquivalence_completionFunctorProperOver` and
> `Stacks.Algebraization.isEquivalence_completionFunctorProperOver_of_adicBaseChangeUnitCondition`,
> which take theirs as an argument.

```lean
public theorem isEquivalence_completionFunctorProperOver_holds
    (A : Type u) [CommRing A] [IsNoetherianRing A] (I : Ideal A) [IsAdicComplete I A]
    {Z : Scheme.{u}} (f : Z ⟶ Spec (.of A))
    [IsSeparated f] [LocallyOfFiniteType f] [QuasiCompact f] :
    (completionFunctorProperOver A I f).IsEquivalence
```

## Tag 088F, a remark

[Tag 088F](https://stacks.math.columbia.edu/tag/088F) in the Stacks Project.

**`AlgebraicGeometry.AdicCoherentModuleSystem`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AdicThickeningCoherentSystem.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AdicThickeningCoherentSystem.lean#L143). The attribute's comment: “the systems (F n, phi n) of clauses (1), (2) and (3)”.

> **The systems `(ℱₙ, φₙ)` of Stacks 088F.** For `f : X ⟶ Spec A` locally of finite type, a
> coherent `𝒪_{Xₙ}`-module for every `n`, together with an isomorphism `φₙ : iₙ^* ℱₙ₊₁ ≅ ℱₙ`
> along the transition `iₙ : Xₙ ⟶ Xₙ₊₁`, whose first term has support proper over `S₁`.
>
> The three fields other than `obj` are clauses (1), (2) and (3) of the remark. Clause (2) asks
> for an isomorphism as *data*, as in the source, not merely for the existence of one: the
> transition maps of the system are part of it.

```lean
public structure AdicCoherentModuleSystem (A : Type u) [CommRing A] (I : Ideal A)
    {X : Scheme.{u}} (f : X ⟶ Spec (.of A)) [LocallyOfFiniteType f]
```

**`AlgebraicGeometry.adicThickeningCompletionFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AdicThickeningCoherentSystem.lean, line 254](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AdicThickeningCoherentSystem.lean#L254). The attribute's comment: “the completion functor into those systems; not that it is an equivalence, for which Stacks 088E (itself conditional on 088C here) and an identification of the adic thickenings with the closed subschemes of the ideal powers are both missing”.

> **The completion functor of Stacks 088F.** It sends a coherent `𝒪_X`-module with support
> proper over `A` to the system `(ℱ|_{Xₙ})` of its restrictions to the adic thickenings, with the
> transition isomorphisms induced by `iₙ ≫ (Xₙ₊₁ ⟶ X) = (Xₙ ⟶ X)`, and a map of modules to the
> system of its restrictions.
>
> This is the arrow displayed in the remark. That it is an **equivalence** is Stacks 088E read
> through an identification of the coherent adic systems of `Stacks.Coherent.CoherentAdicSystems`
> with the systems of this file; neither input is available in this library, so no equivalence is
> claimed here.

```lean
public def adicThickeningCompletionFunctor (A : Type u) [CommRing A] [IsNoetherianRing A]
    (I : Ideal A) {X : Scheme.{u}} (f : X ⟶ Spec (.of A)) [LocallyOfFiniteType f] :
    Stacks.Algebraization.CoherentModulesProperOver f ⥤ AdicCoherentModuleSystem A I f
```

**`AlgebraicGeometry.hasProperSupport_of_isProper_adicBaseChange`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AdicThickeningCoherentSystem.lean, line 283](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AdicThickeningCoherentSystem.lean#L283). The attribute's comment: “for a proper f the support condition (3) on the systems is vacuous”.

> **Stacks 088F, final clause: over a proper base the support conditions may be omitted.**
> If `f : X ⟶ Spec A` is proper then the structure morphism `Xₙ ⟶ Sₙ` is proper too, being its
> base change, and so the support of any coherent `𝒪_{Xₙ}`-module is proper over `Sₙ`. Hence
> clause (3) is automatic.
>
> The companion statement on the other side of the arrow — that the support of any coherent
> `𝒪_X`-module is then proper over `A` — is `Stacks.Algebraization.hasProperSupport_of_isProper`.

```lean
public lemma hasProperSupport_of_isProper_adicBaseChange [IsProper f] (n : ℕ)
    (F : (adicBaseChange A I f n).Modules) (hF : _root_.SheafOfModules.IsCoherent.{u} F) :
    HasProperSupport (pullback.snd f (adicThickeningι A I n)) F
```

**`AlgebraicGeometry.isEquivalence_adicThickeningCompletionFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/AdicThickeningEssSurj.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/AdicThickeningEssSurj.lean#L245). The attribute's comment: “the completion functor from the coherent O\_X-modules with support proper over A to the systems (F n, phi n) of clauses (1), (2) and (3) is an equivalence of categories, for A Noetherian and I-adically complete and X -> Spec A separated and of finite type”.

> **The completion functor is an equivalence.** Let `A` be a Noetherian
> ring complete with respect to an ideal `I`, put `S = Spec A`, `Sₙ = Spec (A / Iⁿ)`, let
> `f : X ⟶ S` be separated and of finite type (locally of finite type and quasi-compact) and
> `Xₙ = X ×_S Sₙ`. Then the completion functor
> `AlgebraicGeometry.adicThickeningCompletionFunctor`, from the coherent `𝒪_X`-modules with support
> proper over `A` to the systems `(ℱₙ, φₙ)` — `ℱₙ` coherent on `Xₙ`, `φₙ : iₙ^*ℱₙ₊₁ ≅ ℱₙ`, and
> `Supp(ℱ₁)` proper over `S₁` — sending `ℱ` to its restrictions `ℱ|_{Xₙ}`, is an equivalence of
> categories.

```lean
public theorem isEquivalence_adicThickeningCompletionFunctor
    (A : Type u) [CommRing A] [IsNoetherianRing A] (I : Ideal A) [IsAdicComplete I A]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of A))
    [IsSeparated f] [LocallyOfFiniteType f] [QuasiCompact f] :
    (adicThickeningCompletionFunctor A I f).IsEquivalence
```

**`AlgebraicGeometry.isEquivalence_adicThickeningTransitionCompletionFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/AdicThickeningProperEquivalence.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/AdicThickeningProperEquivalence.lean#L190). The attribute's comment: “the special case of X proper over A, with the conditions on the supports omitted: completion from all coherent O\_X-modules to the systems of coherent O\_\{X\_n}-modules F n with isomorphisms phi n is an equivalence of categories”.

> Let `A` be a Noetherian ring complete with respect to an ideal `I`, let `f : X ⟶ Spec A` be
> proper and `Xₙ = X ×_S Sₙ`. Then completion `ℱ ↦ (ℱ|_{Xₙ})` is an equivalence from the category
> of all coherent `𝒪_X`-modules to the category of systems `(ℱₙ, φₙ)` with `ℱₙ` a coherent
> `𝒪_{Xₙ}`-module and `φₙ : iₙ^*ℱₙ₊₁ ≅ ℱₙ` an isomorphism.

```lean
public theorem isEquivalence_adicThickeningTransitionCompletionFunctor [IsNoetherianRing A]
    [IsAdicComplete I A] [IsProper f] :
    (adicThickeningTransitionCompletionFunctor A I f).IsEquivalence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 30.27, Tag 0CYW](https://stacks.math.columbia.edu/tag/0CYW)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
