---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.MayerVietoris.cohomologySequence_exact, Stacks.EtaleCohomology.MayerVietoris.initialSequence_exact, Stacks.EtaleCohomology.MayerVietoris.mayerVietoris_longExactSequence_etaleCohomology, Stacks.EtaleCohomology.MayerVietoris.mayerVietoris_longExactSequence_cover, Stacks.EtaleCohomology.RelativeMayerVietoris.toCover, Stacks.EtaleCohomology.RelativeMayerVietoris.toIntersection, Stacks.EtaleCohomology.RelativeMayerVietoris.boundary, Stacks.EtaleCohomology.RelativeMayerVietoris.cohomologySequence_exact
statement: formalized
proof: formalized
---

# 59.50 Étale cohomology

Section 59.50 of the Stacks Project, [Tag 03Q3](https://stacks.math.columbia.edu/tag/03Q3). 2 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0A50, a lemma

[Tag 0A50](https://stacks.math.columbia.edu/tag/0A50) in the Stacks Project.

**`Stacks.EtaleCohomology.MayerVietoris.cohomologySequence_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/MayerVietoris.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/MayerVietoris.lean#L325). The attribute's comment: “exactness of each six-term window”.

> **Stacks 0A50.** The Mayer--Vietoris sequence in étale cohomology is exact: for open
> subschemes `U`, `V` of a scheme `X` and an abelian sheaf `F` on the small étale site of `X`,
> every six-term window of
>
> `⋯ ⟶ Hⁿ(U ⊔ V, F) ⟶ Hⁿ(U, F) ⊞ Hⁿ(V, F) ⟶ Hⁿ(U ⊓ V, F) ⟶ Hⁿ⁺¹(U ⊔ V, F) ⟶ ⋯`
>
> is exact.

```lean
theorem cohomologySequence_exact (n₀ n₁ : ℕ) (h : n₀ + 1 = n₁) :
    (cohomologySequence F U V n₀ n₁ h).Exact
```

**`Stacks.EtaleCohomology.MayerVietoris.initialSequence_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/MayerVietoris.lean, line 343](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/MayerVietoris.lean#L343). The attribute's comment: “the long exact sequence, with its leading zero”.

> **Stacks 0A50.** The Mayer--Vietoris sequence in étale cohomology is exact at its initial
> segment, leading zero included: the sum of the two restriction maps
> `H⁰(U ⊔ V, F) ⟶ H⁰(U, F) ⊞ H⁰(V, F)` is injective.

```lean
theorem initialSequence_exact : (initialSequence F U V).Exact
```

**`Stacks.EtaleCohomology.MayerVietoris.mayerVietoris_longExactSequence_etaleCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/MayerVietorisAbsolute.lean, line 582](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/MayerVietorisAbsolute.lean#L582).

> **Stacks 0A50: Mayer--Vietoris for étale cohomology.** For open subschemes `U`, `V` of a
> scheme `X` and an abelian sheaf `F` on the small étale site of `X`, the sequence
>
> `0 ⟶ H⁰(U ∪ V, F) ⟶ H⁰(U, F) ⊞ H⁰(V, F) ⟶ H⁰(U ∩ V, F)
>   ⟶ H¹(U ∪ V, F) ⟶ H¹(U, F) ⊞ H¹(V, F) ⟶ H¹(U ∩ V, F) ⟶ ⋯`
>
> of absolute étale cohomology groups of the open subschemes `U ∪ V`, `U`, `V`, `U ∩ V` is a long
> exact sequence, functorial in `F`. That is the conjunction of the clauses stated here:
>
> * its initial segment is exact, leading zero included, which is exactness at `H⁰(U ∪ V, F)`, the
>   one place no six-term window reaches;
> * every six-term window of it is exact, which is exactness at `Hⁿ(U, F) ⊞ Hⁿ(V, F)` and at
>   `Hⁿ(U ∩ V, F)` for every `n`, and at `Hⁿ(U ∪ V, F)` for every `n ≥ 1`;
> * each of the three families of maps of the sequence — the connecting morphisms, the sum of the
>   two restriction maps and their difference — is natural in `F`, so that a morphism of abelian
>   sheaves induces a morphism of long exact sequences: this is the functoriality the source
>   asserts.
>
> The first two clauses together are exactness at every term of the sequence.
>
> The terms are the étale cohomology of the *schemes* `U ∪ V`, `U`, `V`, `U ∩ V` with coefficients
> in the restriction of `F` to their small étale sites. The comparison with the cohomology over
> those opens read as objects of the small étale site of `X`, which is where the exactness is
> proved, is `Stacks.EtaleCohomology.MayerVietoris.h'OpensIsoH`, and the arrows of the sequence are
> the arrows of `Stacks.EtaleCohomology.MayerVietoris.mayerVietoris_longExactSequence` read through
> it.
>
> The statement is made for arbitrary open subschemes `U`, `V`, so it is more general than the
> source, whose hypothesis is `X = U ∪ V`: in that case the open subscheme `U ⊔ V` is `X` itself,
> and the same ambient terms are identified with the global étale cohomology groups `Hⁿ(F)` on the
> small étale site of `X` directly by
> `Stacks.EtaleCohomology.MayerVietoris.cohomologySupIsoH`.

```lean
theorem mayerVietoris_longExactSequence_etaleCohomology :
    (absoluteInitialSequence F U V).Exact ∧
      (∀ (n₀ n₁ : ℕ) (h : n₀ + 1 = n₁), (absoluteSequence F U V n₀ n₁ h).Exact) ∧
      (∀ (G' : Sheaf (topology X) AddCommGrpCat.{u + 1}) (f : F ⟶ G') (n₀ n₁ : ℕ)
          (h : n₀ + 1 = n₁),
        opensCohomologyMap X (U ⊓ V) n₀ f ≫ absoluteDelta G' U V n₀ n₁ h =
          absoluteDelta F U V n₀ n₁ h ≫ opensCohomologyMap X (U ⊔ V) n₁ f) ∧
      (∀ (G' : Sheaf (topology X) AddCommGrpCat.{u + 1}) (f : F ⟶ G') (n : ℕ),
        opensCohomologyMap X (U ⊔ V) n f ≫ absoluteToBiprod G' U V n =
          absoluteToBiprod F U V n ≫
            biprod.map (opensCohomologyMap X U n f) (opensCohomologyMap X V n f)) ∧
      ∀ (G' : Sheaf (topology X) AddCommGrpCat.{u + 1}) (f : F ⟶ G') (n : ℕ),
        biprod.map (opensCohomologyMap X U n f) (opensCohomologyMap X V n f) ≫
            absoluteFromBiprod G' U V n =
          absoluteFromBiprod F U V n ≫ opensCohomologyMap X (U ⊓ V) n f
```

**`Stacks.EtaleCohomology.MayerVietoris.mayerVietoris_longExactSequence_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/MayerVietorisAbsolute.lean, line 829](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/MayerVietorisAbsolute.lean#L829). The attribute's comment: “the source's own statement: the hypothesis `X = U ∪ V`, with the ambient terms of the sequence the global étale cohomology groups of `X` itself”.

> **Stacks 0A50: Mayer--Vietoris for étale cohomology, as the source states it.** Let `X` be a
> scheme which is the union `X = U ∪ V` of two open subschemes and let `F` be an abelian sheaf on
> the small étale site of `X`. Then
>
> `0 ⟶ H⁰(X, F) ⟶ H⁰(U, F) ⊞ H⁰(V, F) ⟶ H⁰(U ∩ V, F)
>   ⟶ H¹(X, F) ⟶ H¹(U, F) ⊞ H¹(V, F) ⟶ H¹(U ∩ V, F) ⟶ ⋯`
>
> is a long exact sequence, functorial in `F`. That is the conjunction of the clauses stated here:
>
> * its initial segment is exact, leading zero included, which is exactness at `H⁰(X, F)`, the one
>   place no six-term window reaches;
> * every six-term window of it is exact, which is exactness at `Hⁿ(U, F) ⊞ Hⁿ(V, F)` and at
>   `Hⁿ(U ∩ V, F)` for every `n`, and at `Hⁿ(X, F)` for every `n ≥ 1`;
> * each of the three families of maps of the sequence — the connecting morphisms, the sum of the
>   two restriction maps and their difference — is natural in `F`, so that a morphism of abelian
>   sheaves induces a morphism of long exact sequences: this is the functoriality the source
>   asserts.
>
> The first two clauses together are exactness at every term of the sequence.
>
> The ambient terms are the global étale cohomology groups of `X` itself, which is the hypothesis
> `U ⊔ V = ⊤` being used: the other terms are the étale cohomology of the schemes `U`, `V`,
> `U ∩ V` with coefficients in the restriction of `F` to their small étale sites.
>
> This is the statement of
> `Stacks.EtaleCohomology.MayerVietoris.mayerVietoris_longExactSequence_etaleCohomology`, which
> makes no hypothesis on `U` and `V` and whose ambient terms are therefore the étale cohomology of
> the open subscheme `U ∪ V`, transported along the comparison `supIsoGlobalH` of those terms with
> the global étale cohomology of `X`. Nothing of the Mayer--Vietoris sequence is reproved.

```lean
theorem mayerVietoris_longExactSequence_cover (hUV : U ⊔ V = ⊤) :
    (coverInitialSequence F U V hUV).Exact ∧
      (∀ (n₀ n₁ : ℕ) (h : n₀ + 1 = n₁), (coverSequence F U V hUV n₀ n₁ h).Exact) ∧
      (∀ (G' : Sheaf (topology X) AddCommGrpCat.{u + 1}) (f : F ⟶ G') (n₀ n₁ : ℕ)
          (h : n₀ + 1 = n₁),
        opensCohomologyMap X (U ⊓ V) n₀ f ≫ coverDelta G' U V hUV n₀ n₁ h =
          coverDelta F U V hUV n₀ n₁ h ≫ globalCohomologyMap X n₁ f) ∧
      (∀ (G' : Sheaf (topology X) AddCommGrpCat.{u + 1}) (f : F ⟶ G') (n : ℕ),
        globalCohomologyMap X n f ≫ coverToBiprod G' U V hUV n =
          coverToBiprod F U V hUV n ≫
            biprod.map (opensCohomologyMap X U n f) (opensCohomologyMap X V n f)) ∧
      ∀ (G' : Sheaf (topology X) AddCommGrpCat.{u + 1}) (f : F ⟶ G') (n : ℕ),
        biprod.map (opensCohomologyMap X U n f) (opensCohomologyMap X V n f) ≫
            absoluteFromBiprod G' U V n =
          absoluteFromBiprod F U V n ≫ opensCohomologyMap X (U ⊓ V) n f
```

## Tag 0EYK, a lemma

[Tag 0EYK](https://stacks.math.columbia.edu/tag/0EYK) in the Stacks Project.

**`Stacks.EtaleCohomology.RelativeMayerVietoris.toCover`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/RelativeMayerVietoris.lean, line 659](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/RelativeMayerVietoris.lean#L659). The attribute's comment: “the map Rⁿf\_*F → Rⁿa\_*(F|\_U) ⊕ Rⁿb\_*(F|\_V)”.

> **The first map of the Mayer--Vietoris sequence in degree `n`**,
> `Rⁿf_*F ⟶ Rⁿa_*(F|_U) ⊕ Rⁿb_*(F|_V)`, as a natural transformation of functors in `F`: that
> naturality is the functoriality asserted by the statement.

```lean
def toCover (n : ℕ) :
    higherDirectImage.{u, v} f n ⟶
      restrictedHigherDirectImage.{u, v} f U n ⊞
        restrictedHigherDirectImage.{u, v} f V n
```

**`Stacks.EtaleCohomology.RelativeMayerVietoris.toIntersection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/RelativeMayerVietoris.lean, line 670](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/RelativeMayerVietoris.lean#L670). The attribute's comment: “the map Rⁿa\_*(F|\_U) ⊕ Rⁿb\_*(F|\_V) → Rⁿc\_*(F|\_\{U ∩ V})”.

> **The second map of the Mayer--Vietoris sequence in degree `n`**,
> `Rⁿa_*(F|_U) ⊕ Rⁿb_*(F|_V) ⟶ Rⁿc_*(F|_{U ∩ V})`, as a natural transformation of functors
> in `F`.

```lean
def toIntersection (n : ℕ) :
    restrictedHigherDirectImage.{u, v} f U n ⊞
        restrictedHigherDirectImage.{u, v} f V n ⟶
      restrictedHigherDirectImage.{u, v} f (U ⊓ V) n
```

**`Stacks.EtaleCohomology.RelativeMayerVietoris.boundary`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/RelativeMayerVietoris.lean, line 681](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/RelativeMayerVietoris.lean#L681). The attribute's comment: “the connecting map Rⁿc\_*(F|\_\{U ∩ V}) → Rⁿ⁺¹f\_*F”.

> **The connecting map of the Mayer--Vietoris sequence**,
> `Rⁿc_*(F|_{U ∩ V}) ⟶ Rⁿ⁺¹f_*F`, as a natural transformation of functors in `F`.

```lean
def boundary (hUV : U ⊔ V = ⊤) (n : ℕ) :
    restrictedHigherDirectImage.{u, v} f (U ⊓ V) n ⟶
      higherDirectImage.{u, v} f (n + 1)
```

**`Stacks.EtaleCohomology.RelativeMayerVietoris.cohomologySequence_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/RelativeMayerVietoris.lean, line 698](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/RelativeMayerVietoris.lean#L698). The attribute's comment: “exactness of the long sequence”.

> **Stacks Project, Tag 0EYK (relative Mayer--Vietoris), exactness.** For a morphism
> `f : X ⟶ Y` of schemes, two open subschemes `U` and `V` covering `X`, and every abelian sheaf
> `F` on the small étale site of `X`, the six-term window
>
> `Rⁿf_*F ⟶ Rⁿa_*(F|_U) ⊕ Rⁿb_*(F|_V) ⟶ Rⁿc_*(F|_{U ∩ V}) ⟶ Rⁿ⁺¹f_*F ⟶ ⋯`
>
> of the Mayer--Vietoris sequence is exact, for every `n`. Since the three maps are natural
> transformations of functors of `F`, the sequence is functorial in `F`.

```lean
theorem cohomologySequence_exact (hUV : U ⊔ V = ⊤) (n : ℕ)
    (F : Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}) :
    (ComposableArrows.mk₅ ((toCover.{u, v} f U V n).app F)
      ((toIntersection.{u, v} f U V n).app F) ((boundary.{u, v} f U V hUV n).app F)
      ((toCover.{u, v} f U V (n + 1)).app F)
      ((toIntersection.{u, v} f U V (n + 1)).app F)).Exact
```

**`Stacks.EtaleCohomology.RelativeMayerVietoris.mono_toCover_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/RelativeMayerVietoris.lean, line 736](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/RelativeMayerVietoris.lean#L736). The attribute's comment: “the sequence begins with 0 ⟶ f\_*F”.

> **Stacks Project, Tag 0EYK (relative Mayer--Vietoris), the left end.** The Mayer--Vietoris
> sequence starts with `0 ⟶ f_*F`: the degree-zero map `f_*F ⟶ a_*(F|_U) ⊕ b_*(F|_V)` is a
> monomorphism.

```lean
theorem mono_toCover_zero (hUV : U ⊔ V = ⊤)
    (F : Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}) :
    Mono ((toCover.{u, v} f U V 0).app F)
```

**`Stacks.EtaleCohomology.RelativeMayerVietoris.higherDirectImageZeroIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/RelativeMayerVietoris.lean, line 753](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/RelativeMayerVietoris.lean#L753). The attribute's comment: “the degree-zero term is f\_*F”.

> **The degree-zero term of the sequence is the direct image itself.** The direct image along
> `f` is left exact, being a right adjoint, so `R⁰f_* ≅ f_*`; this is what makes the sequence of
> the statement begin with `0 ⟶ f_*F`.

```lean
def higherDirectImageZeroIso :
    higherDirectImage.{u, v} f 0 ≅ etaleAbelianDirectImage.{u, v} f
```

**`Stacks.EtaleCohomology.RelativeMayerVietoris.restrictedHigherDirectImageZeroIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/RelativeMayerVietoris.lean, line 761](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/RelativeMayerVietoris.lean#L761). The attribute's comment: “the degree-zero restricted term is a\_*(F|\_U)”.

> **The degree-zero restricted term of the sequence is the pushed-forward restriction
> itself**, `R⁰(F ↦ a_*(F|_U)) ≅ (F ↦ a_*(F|_U))`: restriction to `U` is exact and the direct
> image along `a = f|_U` is left exact.

```lean
def restrictedHigherDirectImageZeroIso :
    restrictedHigherDirectImage.{u, v} f U 0 ≅ restrictedPushforward.{u, v} f U
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.50, Tag 03Q3](https://stacks.math.columbia.edu/tag/03Q3)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
