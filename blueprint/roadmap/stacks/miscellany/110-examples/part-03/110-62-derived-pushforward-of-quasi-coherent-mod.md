---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.exists_isDerivedLimit_truncGETower_of_lqcFbc', AlgebraicGeometry.Stack.isIso_coproductToProduct_shiftedLqcFbc, Stacks.Examples.UnboundedDerivedPushforward.not_isQuasicoherent_of_iso_piStructureSheaf
statement: formalized
proof: formalized
---

# 110.62 Derived pushforward of quasi-coherent modules

Section 110.62 of the Stacks Project, [Tag 07DC](https://stacks.math.columbia.edu/tag/07DC). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08IY, a lemma

[Tag 08IY](https://stacks.math.columbia.edu/tag/08IY) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_isDerivedLimit_truncGETower_of_lqcFbc'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedLimitOfTruncations.lean, line 285](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedLimitOfTruncations.lean#L285). The attribute's comment: “K is the derived limit of its canonical truncations from below, for a complex of fppf modules with cohomology sheaves in LQCoh^fbc; the affine-object vanishing the source cites is carried as the hypothesis `hvan`”.

> **Stacks 08IY.** Let `𝒳` be an algebraic stack and let `K` be an object of `D(𝒪_𝒳)` whose
> cohomology sheaves are locally quasi-coherent (**Stacks 06WJ**) and have the flat base change
> property (**Stacks 0762**).  Then there is a distinguished triangle
>
> `K ⟶ ∏_{n ≥ 0} τ_{≥ -n}K ⟶ ∏_{n ≥ 0} τ_{≥ -n}K ⟶ K[1]`
>
> in `D(𝒪_𝒳)`: `K` is the derived limit of its canonical truncations from below.
>
> This is `AlgebraicGeometry.Stack.exists_isDerivedLimit_truncGETower_of_lqcFbc` with the covering
> class of the source's proof discharged by
> `AlgebraicGeometry.Stack.hasEnoughObjects_isAffineOver`, at the hom universe `u + 1` of the fppf
> site of an algebraic stack.  The hypothesis `hvan` is the source's first sentence, carried; see
> this file's module documentation for the four cited lemmas it stands for and for why none of them
> is available.

```lean
theorem exists_isDerivedLimit_truncGETower_of_lqcFbc' {𝒳 : Type v} [Category.{u + 1} 𝒳]
    (p : 𝒳 ⥤ BigFppfOver B S hS) (hp : p.IsFiberedInGroupoids)
    [HasSheafify (BigFppfOver.associatedTopology B S hS p .fppf) AddCommGrpCat.{u}]
    [(BigFppfOver.associatedTopology B S hS p .fppf).WEqualsLocallyBijective AddCommGrpCat.{u}]
    [EnoughInjectives (fppfSiteModules B S hS p hp)]
    (K : DerivedCategory (fppfSiteModules B S hS p hp))
    (hK : ∀ i : ℤ, IsLocallyQuasicoherentWithFlatBaseChange B E h S hS p hp
      ((DerivedCategory.homologyFunctor (fppfSiteModules B S hS p hp) i).obj K).val)
    (hvan : HasAffineAcyclicLqcFbcModules B E h S hS p hp) :
    ∃ _ : HasProduct fun n : ℕ ↦ (fppfTruncGETower B S hS p hp K).obj ⟨n⟩,
      IsDerivedLimit (fppfTruncGETower B S hS p hp K) K
```

## Tag 08IZ, a lemma

[Tag 08IZ](https://stacks.math.columbia.edu/tag/08IZ) in the Stacks Project.

**`AlgebraicGeometry.Stack.isIso_coproductToProduct_shiftedLqcFbc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ShiftedSumOfModules.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ShiftedSumOfModules.lean#L117). The attribute's comment: “the sum of a family of shifted LQCoh^fbc modules, indexed by n ≥ 0 as the source's proof supports, maps isomorphically to their product in D(𝒪_𝒳); the affine acyclicity the library's Stacks 08IY carries is carried here as that same predicate”.

> **Stacks 08IZ.** Let `𝒳` be an algebraic stack and let `ℱ_n`, `n ≥ 0`, be sheaves of
> `𝒪_𝒳`-modules on its big fppf site which are locally quasi-coherent (**Stacks 06WJ**) and have
> the flat base change property (**Stacks 0762**).  Then the canonical map
>
> `⊕_n ℱ_n[n] ⟶ ∏_n ℱ_n[n]`
>
> is an isomorphism in `D(𝒪_𝒳)`.
>
> The vanishing `hvan` is the hypothesis the library's **Stacks 08IY** carries, and it is carried in
> exactly that form; see this file's module documentation.

```lean
theorem isIso_coproductToProduct_shiftedLqcFbc (F : ℕ → fppfSiteModules B S hS p hp)
    (hF : ∀ n : ℕ, IsLocallyQuasicoherentWithFlatBaseChange B E h S hS p hp (F n).val)
    (hvan : HasAffineAcyclicLqcFbcModules B E h S hS p hp) :
    IsIso (Pi.lift (Sigma.π (shiftedSingleFamily B S hS p hp F)))
```

## Tag 07DD, a lemma

[Tag 07DD](https://stacks.math.columbia.edu/tag/07DD) in the Stacks Project.

**`Stacks.Examples.UnboundedDerivedPushforward.not_isQuasicoherent_of_iso_piStructureSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Examples/UnboundedDerivedPushforward.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Examples/UnboundedDerivedPushforward.lean#L193). The attribute's comment: “the last step of the discussion of Tag 07DC, over its own base S = Spec k[x]: a module identified with the countable product of copies of O_S, which is what that discussion produces as the degree-zero cohomology sheaf of Rf_*E, is not quasi-coherent, so Rf_*E does not lie in D_QCoh(O_S). Carried as the hypothesis hH is exactly that identification, and with it the quotient stack [Spec k[x]/(Z/pZ)], the quasi-compactness and quasi-separatedness of its structure morphism, the computation Rf_*O_X = sum of O_S[-n] and the identification of E with a product; none of those is established here. Quasi-coherence is that of a module on the scheme S, the sense of the source's `not even locally quasi-coherent`, and not the local quasi-coherence of Tag 06WJ on the big fppf site”.

> **Stacks 07DD**, in the form this development reaches.  The discussion of **Stacks 07DC**
> exhibits a quasi-compact and quasi-separated `f : 𝒳 = [Spec k[x] / (ℤ/pℤ)] ⟶ S = Spec k[x]` and
> an object `E = ⊕_{m ≥ 0} 𝒪_𝒳[m]` of `D_QCoh(𝒪_𝒳)` whose derived pushforward
> `Rf_*E = ∏_{m ≥ 0} ⊕_{n ≥ 0} 𝒪_S[m - n]` has, in degree zero, a countable product of copies of
> `𝒪_S`.  Here that identification is the hypothesis `hH`, and the conclusion is the source's:
> the sheaf so obtained is not quasi-coherent, hence `Rf_*E` is not an object of `D_QCoh(𝒪_S)` and
> `Rf_*` does not restrict to a functor `D_QCoh(𝒪_𝒳) ⟶ D_QCoh(𝒪_S)`.
>
> The hypothesis is satisfiable: the product exists, so `H` may be taken to be it with `hH` the
> identity.  Its content — the quotient stack, the morphism, and the computation of the
> pushforward — is what this repository does not have; see this file's module documentation for
> the step-by-step comparison.

```lean
public theorem not_isQuasicoherent_of_iso_piStructureSheaf {k : Type u} [CommRing k]
    [Nontrivial k] (H : (Spec (CommRingCat.of (Polynomial k))).Modules)
    (hH : H ≅ ∏ᶜ (fun _ : ℕ => SheafOfModules.unit
      (Spec (CommRingCat.of (Polynomial k))).ringCatSheaf)) :
    ¬ H.IsQuasicoherent
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.62, Tag 07DC](https://stacks.math.columbia.edu/tag/07DC)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
