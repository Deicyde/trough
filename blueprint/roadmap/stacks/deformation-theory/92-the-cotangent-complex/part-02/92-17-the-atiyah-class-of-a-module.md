---
declaration: section
origin: cited
lean: CommAlgCat.polynomialAtiyahTriangle, CommAlgCat.polynomialAtiyahTriangle_distinguished, CommAlgCat.polynomialAtiyahClass, CommAlgCat.polynomialAtiyahTriangle_distinguished_of_iso, CommAlgCat.atiyahDisplayedTriangle_distinguished, CommAlgCat.exists_atiyahDisplayedTriangle_distinguished, CommAlgCat.atiyahClass
statement: formalized
proof: formalized
---

# 92.17 The Atiyah class of a module

Section 92.17 of the Stacks Project, [Tag 09DC](https://stacks.math.columbia.edu/tag/09DC). 2 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09DD, an equation

[Tag 09DD](https://stacks.math.columbia.edu/tag/09DD) in the Stacks Project.

**`CommAlgCat.polynomialAtiyahTriangle`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/AtiyahClass.lean, line 279](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/AtiyahClass.lean#L279). The attribute's comment: “the triangle”.

> **Stacks 09DD.** The Atiyah triangle of a `B`-module `M`: the image under
> `Lπ_! : D(𝒪) ⟶ D(B)` of the sequence of first principal parts of `M` on `C_{B/A}`.

```lean
def polynomialAtiyahTriangle :
    Triangle (DerivedCategory (ModuleCat.{u + 1} (ULift.{u + 1} (B : Type u))))
```

**`CommAlgCat.polynomialAtiyahTriangle_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/AtiyahClass.lean, line 286](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/AtiyahClass.lean#L286). The attribute's comment: “the triangle is distinguished”.

> **Stacks 09DD.** The Atiyah triangle is distinguished.

```lean
theorem polynomialAtiyahTriangle_distinguished :
    polynomialAtiyahTriangle A B M ∈ distinguishedTriangles
```

**`CommAlgCat.polynomialAtiyahClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/AtiyahClass.lean, line 300](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/AtiyahClass.lean#L300). The attribute's comment: “the Atiyah class, the last arrow of the triangle”.

> **Stacks 09DD.** The Atiyah class of `M`: the last arrow of the Atiyah triangle.

```lean
def polynomialAtiyahClass :
    (polynomialAtiyahTriangle A B M).obj₃ ⟶ (polynomialAtiyahTriangle A B M).obj₁⟦(1 : ℤ)⟧
```

**`CommAlgCat.polynomialAtiyahTriangle_distinguished_of_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/AtiyahClass.lean, line 309](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/AtiyahClass.lean#L309). The attribute's comment: “the displayed triangle”.

> **Stacks 09DD.** The Atiyah triangle written with its first and third terms replaced by
> objects identified with them: for `L` identified with `Lπ_!(Ω_{𝒪/A} ⊗_𝒪 M)` and `N` identified
> with `Lπ_!(M)`, the sequence `L ⟶ Lπ_!(P¹_{𝒪/A}(M)) ⟶ N ⟶ L[1]` is a distinguished triangle,
> whose last arrow is the Atiyah class of `M`.

```lean
theorem polynomialAtiyahTriangle_distinguished_of_iso
    (L N : DerivedCategory (ModuleCat.{u + 1} (ULift.{u + 1} (B : Type u))))
    (e₁ : (polynomialAtiyahTriangle A B M).obj₁ ≅ L)
    (e₃ : (polynomialAtiyahTriangle A B M).obj₃ ≅ N) :
    Triangle.mk (e₁.inv ≫ (polynomialAtiyahTriangle A B M).mor₁)
        ((polynomialAtiyahTriangle A B M).mor₂ ≫ e₃.hom)
        (e₃.inv ≫ (polynomialAtiyahTriangle A B M).mor₃ ≫
          (shiftFunctor (DerivedCategory (ModuleCat.{u + 1} (ULift.{u + 1} (B : Type u))))
            (1 : ℤ)).map e₁.hom) ∈
      distinguishedTriangles
```

**`CommAlgCat.atiyahDisplayedTriangle_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/AtiyahClassBigSiteCanonical.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/AtiyahClassBigSiteCanonical.lean#L134). The attribute's comment: “the displayed triangle in D(B), its endpoints identified canonically and its last arrow the Atiyah class”.

> **Stacks 09DD/09DE.** The displayed triangle
>
> `L_{B/A} ⊗^𝐋_B M ⟶ Lπ_!(P¹_{𝒪/A}(M)) ⟶ M ⟶ (L_{B/A} ⊗^𝐋_B M)[1]`
>
> of (92.17.0.1), whose last arrow is the Atiyah class `CommAlgCat.atiyahClass`, is
> distinguished in `D(B)`.

```lean
theorem atiyahDisplayedTriangle_distinguished :
    Triangle.mk ((atiyahFirstVertexDisplayedIso A B M).inv ≫ (polynomialAtiyahTriangle A B M).mor₁)
        ((polynomialAtiyahTriangle A B M).mor₂ ≫ (polynomialAtiyahTriangleObj₃Iso A B M).hom)
        (atiyahClass A B M) ∈ distinguishedTriangles
```

**`CommAlgCat.exists_atiyahDisplayedTriangle_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/AtiyahClassBigSiteDisplayed.lean, line 239](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/AtiyahClassBigSiteDisplayed.lean#L239). The attribute's comment: “the displayed triangle `L_{B/A} ⊗^L_B M → Lπ_!(P¹(M)) → M → [1]` at the site C\_\{B/A} itself, with both endpoint identifications proved rather than assumed”.

> **Stacks 09DD, the displayed triangle.** For a ring map `A → B` and a `B`-module `M` there is
> an identification `e₁` of the first term of the Atiyah triangle on the site `C_{B/A}` with
> `L_{B/A} ⊗^𝐋_B M` for which
>
> `L_{B/A} ⊗^𝐋_B M ⟶ Lπ_!(P¹_{𝒪/A}(M)) ⟶ M ⟶ (L_{B/A} ⊗^𝐋_B M)[1]`
>
> is a distinguished triangle, the third term being identified with `M` by the canonical
> `CommAlgCat.polynomialAtiyahTriangleObj₃Iso`.
>
> Nothing is assumed: the first identification is
> `CommAlgCat.nonempty_atiyahFirstVertexDerivedTensorIso`, the chain of [Stacks, Tag 08PT] and
> [Tag 08PU] together with the universe-lift comparison of the sections of `B̲ ⊗_𝒪 Ω_{𝒪/A}`, and
> the third is [Tag 08QE] through
> `Stacks.ChaoticSite.derivedColimitWithCoefficientsRestrictScalarsIso`. It is `e₁` that is
> existentially quantified rather than named, because the K-flat resolution computing the derived
> tensor product is chosen and not canonical.

```lean
theorem exists_atiyahDisplayedTriangle_distinguished :
    ∃ e₁ : (polynomialAtiyahTriangle A B M).obj₁ ≅ atiyahDisplayedObj₁ A B M,
      Triangle.mk (e₁.inv ≫ (polynomialAtiyahTriangle A B M).mor₁)
          ((polynomialAtiyahTriangle A B M).mor₂ ≫
            (polynomialAtiyahTriangleObj₃Iso A B M).hom)
          ((polynomialAtiyahTriangleObj₃Iso A B M).inv ≫
            (polynomialAtiyahTriangle A B M).mor₃ ≫
              (shiftFunctor
                (DerivedCategory (ModuleCat.{u + 1} (ULift.{u + 1} (B : Type u))))
                (1 : ℤ)).map e₁.hom) ∈
        distinguishedTriangles
```

## Tag 09DE, a definition

[Tag 09DE](https://stacks.math.columbia.edu/tag/09DE) in the Stacks Project.

**`CommAlgCat.atiyahClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/AtiyahClassBigSiteCanonical.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/AtiyahClassBigSiteCanonical.lean#L119). The attribute's comment: “the Atiyah class M → (L\_\{B/A} ⊗^L\_B M)[1] in D(B): the last arrow of the triangle of 09DD, its endpoints identified canonically by 08PT and 08QE”.

> **Stacks 09DE, the Atiyah class of a module.** For a ring map `A → B` and a `B`-module `M`,
> the Atiyah class of `M` is the morphism
>
> `M ⟶ (L_{B/A} ⊗^𝐋_B M)[1]`
>
> of the derived category of `B`-modules that is the last arrow of the distinguished triangle
> (92.17.0.1) of [Stacks, Tag 09DD], obtained by applying `Lπ_!` of [Stacks, Tag 09CZ] to the
> sequence of first principal parts `0 ⟶ Ω_{𝒪/A} ⊗_𝒪 M̲ ⟶ P¹_{𝒪/A}(M) ⟶ M̲ ⟶ 0` on `C_{B/A}`, with
> its endpoints identified by `Lπ_!(M̲) = M` ([Stacks, Tag 08QE],
> `CommAlgCat.polynomialAtiyahTriangleObj₃Iso`) and
> `Lπ_!(Ω_{𝒪/A} ⊗_𝒪 M̲) = L_{B/A} ⊗^𝐋_B M` ([Stacks, Tag 08PT] and the flatness of the terms of
> `L_{B/A}`, `CommAlgCat.atiyahFirstVertexDisplayedIso`). That it is the last arrow of the
> displayed distinguished triangle is `CommAlgCat.atiyahDisplayedTriangle_distinguished`.

```lean
def atiyahClass :
    (DerivedCategory.singleFunctor (ModuleCat.{u + 1} (ULift.{u + 1} (B : Type u))) 0).obj M ⟶
      (atiyahDisplayedObj₁ A B M)⟦(1 : ℤ)⟧
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 92.17, Tag 09DC](https://stacks.math.columbia.edu/tag/09DC)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
