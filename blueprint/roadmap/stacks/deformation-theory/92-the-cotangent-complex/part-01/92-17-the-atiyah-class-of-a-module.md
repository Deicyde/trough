---
declaration: section
origin: cited
lean: CommAlgCat.polynomialAtiyahTriangle, CommAlgCat.polynomialAtiyahTriangle_distinguished, CommAlgCat.polynomialAtiyahClass, CommAlgCat.polynomialAtiyahTriangle_distinguished_of_iso, CommAlgCat.exists_atiyahDisplayedTriangle_distinguished, CommAlgCat.polynomialAtiyahClassOfIso, CommAlgCat.exists_atiyahDisplayedClass_mem_distinguished
statement: formalized
proof: formalized
---

# 92.17 The Atiyah class of a module

Section 92.17 of the Stacks Project, [Tag 09DC](https://stacks.math.columbia.edu/tag/09DC). 2 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09DD, an equation

[Tag 09DD](https://stacks.math.columbia.edu/tag/09DD) in the Stacks Project.

**`CommAlgCat.polynomialAtiyahTriangle`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/AtiyahClass.lean, line 282](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/AtiyahClass.lean#L282). The attribute's comment: “the triangle”.

> **Stacks 09DD.** The Atiyah triangle of a `B`-module `M`: the image under
> `Lπ_! : D(𝒪) ⟶ D(B)` of the sequence of first principal parts of `M` on `C_{B/A}`.

```lean
def polynomialAtiyahTriangle :
    Triangle (DerivedCategory (ModuleCat.{u + 1} (ULift.{u + 1} (B : Type u))))
```

**`CommAlgCat.polynomialAtiyahTriangle_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/AtiyahClass.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/AtiyahClass.lean#L289). The attribute's comment: “the triangle is distinguished”.

> **Stacks 09DD.** The Atiyah triangle is distinguished.

```lean
theorem polynomialAtiyahTriangle_distinguished :
    polynomialAtiyahTriangle A B M ∈ distinguishedTriangles
```

**`CommAlgCat.polynomialAtiyahClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/AtiyahClass.lean, line 303](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/AtiyahClass.lean#L303). The attribute's comment: “the Atiyah class, the last arrow of the triangle”.

> **Stacks 09DD.** The Atiyah class of `M`: the last arrow of the Atiyah triangle.

```lean
def polynomialAtiyahClass :
    (polynomialAtiyahTriangle A B M).obj₃ ⟶ (polynomialAtiyahTriangle A B M).obj₁⟦(1 : ℤ)⟧
```

**`CommAlgCat.polynomialAtiyahTriangle_distinguished_of_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/AtiyahClass.lean, line 312](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/AtiyahClass.lean#L312). The attribute's comment: “the displayed triangle”.

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

**`CommAlgCat.exists_atiyahDisplayedTriangle_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/AtiyahClassBigSiteDisplayed.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/AtiyahClassBigSiteDisplayed.lean#L247). The attribute's comment: “the displayed triangle `L_{B/A} ⊗^L_B M → Lπ_!(P¹(M)) → M → [1]` at the site C\_\{B/A} itself, with both endpoint identifications proved rather than assumed”.

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

**`CommAlgCat.polynomialAtiyahClassOfIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/AtiyahClass.lean, line 333](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/AtiyahClass.lean#L333). The attribute's comment: “the Atiyah class; the source's identifications Lπ\_!(Ω\_\{𝒪/A} ⊗\_𝒪 M) = L\_\{B/A} ⊗\_B^L M (Tag 08PT) and Lπ\_!(M) = M (Tag 08QE) are not available here, so they are carried as the extra hypotheses `e₁` and `e₃`, which the source does not have”.

> **Stacks 09DE.** The *Atiyah class* of `M`, in the form displayed by the source. For `L`
> identified with `Lπ_!(Ω_{𝒪/A} ⊗_𝒪 M)` and `N` identified with `Lπ_!(M)` this is the last arrow
> `N ⟶ L[1]` of the distinguished triangle of Tag 09DD. Under the source's identifications
> `L = L_{B/A} ⊗_B^𝐋 M` and `N = M` it is the Atiyah class `M ⟶ L_{B/A} ⊗_B^𝐋 M[1]`. That it is
> the last arrow of the displayed triangle is
> `CommAlgCat.polynomialAtiyahClassOfIso_mem_distinguished`.

```lean
def polynomialAtiyahClassOfIso
    (L N : DerivedCategory (ModuleCat.{u + 1} (ULift.{u + 1} (B : Type u))))
    (e₁ : (polynomialAtiyahTriangle A B M).obj₁ ≅ L)
    (e₃ : (polynomialAtiyahTriangle A B M).obj₃ ≅ N) : N ⟶ L⟦(1 : ℤ)⟧
```

**`CommAlgCat.exists_atiyahDisplayedClass_mem_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/AtiyahClassBigSiteDisplayed.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/AtiyahClassBigSiteDisplayed.lean#L292). The attribute's comment: “the Atiyah class M → (L\_\{B/A} ⊗^L\_B M)[1] at the site C\_\{B/A} itself, as the last arrow of the displayed distinguished triangle of (92.17.0.1); both endpoint identifications are proved rather than assumed”.

> **Stacks 09DE, the Atiyah class of a module.** For a ring map `A → B` and a `B`-module `M`
> there is an identification `e₁` of the first term of the Atiyah triangle on the site `C_{B/A}`
> with `L_{B/A} ⊗^𝐋_B M` for which the *Atiyah class* of `M`,
>
> `M ⟶ (L_{B/A} ⊗^𝐋_B M)[1]`,
>
> is the last arrow of the distinguished triangle displayed by [Stacks, Tag 09DD]:
>
> `L_{B/A} ⊗^𝐋_B M ⟶ Lπ_!(P¹_{𝒪/A}(M)) ⟶ M ⟶ (L_{B/A} ⊗^𝐋_B M)[1]`.
>
> The class itself is `CommAlgCat.polynomialAtiyahClassOfIso`, the last arrow
> `Lπ_!(M̲) ⟶ Lπ_!(Ω_{𝒪/A} ⊗_𝒪 M̲)[1]` of the Atiyah triangle read through identifications of the
> endpoints, instantiated at the displayed endpoints: the third by the canonical
> `CommAlgCat.polynomialAtiyahTriangleObj₃Iso`, [Stacks, Tag 08QE] at this site, and the first by
> `e₁`. Nothing is assumed — `e₁` is produced inside the proof from
> `CommAlgCat.nonempty_atiyahFirstVertexDerivedTensorIso`, the chain of [Tag 08PT] and [Tag 08PU]
> at this site — and this is the whole of the definition: the arrow, its source `M`, its target
> `(L_{B/A} ⊗^𝐋_B M)[1]`, and its being the last arrow of the triangle of (92.17.0.1).
>
> `e₁` is existentially quantified rather than named because the K-flat resolution computing the
> derived tensor product is chosen and not canonical, so there is no canonical identification of
> the first term to name. That costs nothing: by
> `CommAlgCat.polynomialAtiyahClassOfIso_mem_distinguished` the conclusion holds for *every* such
> identification, so the existential asserts only that one exists. The module documentation records
> why naming one by `Classical.choice` instead would fix a non-canonical choice.

```lean
theorem exists_atiyahDisplayedClass_mem_distinguished :
    ∃ e₁ : (polynomialAtiyahTriangle A B M).obj₁ ≅ atiyahDisplayedObj₁ A B M,
      Triangle.mk (e₁.inv ≫ (polynomialAtiyahTriangle A B M).mor₁)
          ((polynomialAtiyahTriangle A B M).mor₂ ≫
            (polynomialAtiyahTriangleObj₃Iso A B M).hom)
          (polynomialAtiyahClassOfIso A B M (atiyahDisplayedObj₁ A B M)
            ((DerivedCategory.singleFunctor
              (ModuleCat.{u + 1} (ULift.{u + 1} (B : Type u))) 0).obj M) e₁
            (polynomialAtiyahTriangleObj₃Iso A B M)) ∈
        distinguishedTriangles
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 92.17, Tag 09DC](https://stacks.math.columbia.edu/tag/09DC)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
