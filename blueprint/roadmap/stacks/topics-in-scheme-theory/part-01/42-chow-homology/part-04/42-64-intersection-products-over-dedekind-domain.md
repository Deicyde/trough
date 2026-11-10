---
declaration: section
origin: cited
lean: Stacks.Chow.IsDedekindChowBase.intersectionProduct_assoc, Stacks.Chow.IsDedekindChowBase.chowCohomologyCapFundamentalClass_bijective_of_smooth_of_equidimensional, Stacks.Chow.IsDedekindChowBase.chowGroupRestrict_chowCohomologyCapFundamentalClass_mulId
statement: formalized
proof: formalized
---

# 42.64 Intersection products over Dedekind domains

Section 42.64 of the Stacks Project, [Tag 0FC9](https://stacks.math.columbia.edu/tag/0FC9). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FCA, a lemma

[Tag 0FCA](https://stacks.math.columbia.edu/tag/0FCA) in the Stacks Project.

**`Stacks.Chow.IsDedekindChowBase.intersectionProduct_assoc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/IntersectionProductDedekindAssociativity.lean, line 635](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/IntersectionProductDedekindAssociativity.lean#L635). The attribute's comment: “the whole statement (α·β)·γ = α·(β·γ) in CH\_*(Y ×\_X Z ×\_X W) for X smooth over a base as in section 42.63 (zero-dimensional components allowed), of arbitrary relative dimension, Y, Z, W locally of finite type over X and arbitrary α, β, γ; the product is Δ^!(α × β) with Δ^! the Gysin class of the diagonal of Stacks 0FBR and × the exterior product of Stacks 0FC4, formed on the open and closed parts of X of constant relative dimension as in section 42.64, bivariant classes those of `Stacks.Chow.gysinSystemOfInvertible`”.

> **Stacks 0FCA.** Let `(S, δ)` be as in section 42.63: `S` locally Noetherian with an open
> covering by spectra of Dedekind domains, `δ = 0` at closed points and `δ = 1` elsewhere. Let `X`
> be smooth over `S`, of arbitrary and not necessarily constant relative dimension, and let `Y`,
> `Z`, `W` be locally of finite type over `X`. As section 42.64 prescribes, the intersection product
> `α · β = Δ^!(α × β)` is formed over the open and closed parts `X_e` of `X` where `X ⟶ S` has
> relative dimension `e` (`Stacks.WeilCohomology.dimPart`), with the Gysin class
> `Δ^! ∈ A^e(X_e ⟶ X_e ×_S X_e)` of the diagonal of Stacks 0FBR: for `α ∈ CH_n(Y)` and
> `β ∈ CH_m(Z)` its component over `X_e` is `α|_{Y_e} · β|_{Z_e} ∈ CH_{n+m-1-e}(Y_e ×_{X_e} Z_e)`,
> where `Y_e = a⁻¹(X_e)` and `Z_e = b⁻¹(X_e)` are the parts of `Y` and `Z` over `X_e`
> (`Stacks.Chow.chowGroupDimPartOver`). Then for `γ ∈ CH_l(W)`
>
>   `(α · β) · γ = α · (β · γ)`   in   `CH_*(Y ×_X Z ×_X W)`,
>
> component by component, read through the associator of the triple fibre product over `X_e` and
> the matching of the degrees `(n + m - 1 - e) + l - 1 - e` and `n + (m + l - 1 - e) - 1 - e`.

```lean
theorem IsDedekindChowBase.intersectionProduct_assoc [Smooth sX] (n m l : ℤ)
    (α : chowGroup C (a ≫ sX) n) (β : chowGroup C (b ≫ sX) m) (γ : chowGroup C (g ≫ sX) l)
    (e : ℕ) :
    chowGroupDegreeEquiv C
        (pullback.fst π[a, e] (pullback.fst π[b, e] π[g, e] ≫ π[b, e]) ≫ (π[a, e] ≫ X[e]))
        (by ring : n + m - 1 - e + l - 1 - e = n + (m + l - 1 - e) - 1 - e)
        (properChowPushforward C
          (pullback.fst (pullback.fst π[a, e] π[b, e] ≫ π[a, e]) π[g, e] ≫
            ((pullback.fst π[a, e] π[b, e] ≫ π[a, e]) ≫ X[e]))
          (pullback.fst π[a, e] (pullback.fst π[b, e] π[g, e] ≫ π[b, e]) ≫ (π[a, e] ≫ X[e]))
          (tripleProductAssoc π[a, e] π[b, e] π[g, e]).hom
          (tripleProductAssoc_hom_comp_structureMorphism C X[e] π[a, e] π[b, e] π[g, e])
          (n + m - 1 - e + l - 1 - e) (properPushforwardDescends C _ _ _ _ _)
          (hS.intersectionProduct (gysinSystemOfInvertible C) X[e]
            (pullback.fst π[a, e] π[b, e] ≫ π[a, e]) π[g, e] e Δ[e] (n + m - 1 - e) l
            (chowGroupCongr C (Category.assoc (pullback.fst π[a, e] π[b, e]) π[a, e] X[e]).symm
              (n + m - 1 - e)
              (hS.intersectionProduct (gysinSystemOfInvertible C) X[e] π[a, e] π[b, e] e Δ[e] n m
                (res[a, e, n, α] ⊗ₜ[ℤ] res[b, e, m, β])) ⊗ₜ[ℤ] res[g, e, l, γ]))) =
      hS.intersectionProduct (gysinSystemOfInvertible C) X[e] π[a, e]
        (pullback.fst π[b, e] π[g, e] ≫ π[b, e]) e Δ[e] n (m + l - 1 - e)
        (res[a, e, n, α] ⊗ₜ[ℤ]
          chowGroupCongr C (Category.assoc (pullback.fst π[b, e] π[g, e]) π[b, e] X[e]).symm
            (m + l - 1 - e)
            (hS.intersectionProduct (gysinSystemOfInvertible C) X[e] π[b, e] π[g, e] e Δ[e] m l
              (res[b, e, m, β] ⊗ₜ[ℤ] res[g, e, l, γ])))
```

## Tag 0FCB, a lemma

[Tag 0FCB](https://stacks.math.columbia.edu/tag/0FCB) in the Stacks Project.

**`Stacks.Chow.IsDedekindChowBase.chowCohomologyCapFundamentalClass_bijective_of_smooth_of_equidimensional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SmoothChowCohomologyDedekind.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/SmoothChowCohomologyDedekind.lean#L160). The attribute's comment: “first clause, in full: S as in section 42.63 with field components allowed, X smooth over S and equidimensional of dimension d (every irreducible component of δ-dimension d); bivariant classes are those of the Gysin system of invertible modules, `Stacks.Chow.gysinSystemOfInvertible`”.

> **Stacks 0FCB, first clause.** Let `(S, δ)` be a base as in section 42.63 of the Stacks Project
> (locally the spectrum of a Dedekind domain, fields allowed; `δ = 0` at closed points and `1`
> elsewhere), and let `X` be smooth over `S`, equidimensional of dimension `d`: every irreducible
> component of `X` has δ-dimension `d`. Then
>
>   `A^p(X) ⟶ CH_{d-p}(X)`,   `c ↦ c ∩ [X]_d`,
>
> is an isomorphism for every `p ∈ ℤ`.

```lean
theorem chowCohomologyCapFundamentalClass_bijective_of_smooth_of_equidimensional (d : ℕ)
    (hd : ∀ V : irreducibleComponents X,
      deltaDimension C sX ⟨V, V.2.1, isClosed_of_mem_irreducibleComponents _ V.2⟩ = d)
    (p : ℤ) :
    Function.Bijective
      (chowCohomologyCapFundamentalClass C (gysinSystemOfInvertible C) sX d p)
```

**`Stacks.Chow.IsDedekindChowBase.chowGroupRestrict_chowCohomologyCapFundamentalClass_mulId`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SmoothChowCohomologyDedekind.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/SmoothChowCohomologyDedekind.lean#L237). The attribute's comment: “second clause, corrected form: Θ(a · b) = Θ(a) · Θ(b) on the part X₁ of X over the one-dimensional part of S (all of X when S has no zero-dimensional component), with the intersection product of section 42.64 formed with the Gysin class Δ^! of the diagonal; over a zero-dimensional component the clause is false as stated, see `Stacks.Chow.not_chowCohomologyCapFundamentalClass_mulId_fieldChowSituation`; S as in section 42.63 with field components allowed, X smooth and equidimensional of dimension e + 1”.

> **Stacks 0FCB, second clause**, corrected form: over the one-dimensional part of the base. Let
> `(S, δ)` be a base as in section 42.63 (field components allowed), and let `X` be smooth over `S`
> and equidimensional of dimension `e + 1`. Write `X₁ ⊆ X` for the open and closed part over the
> one-dimensional part `S₁` of `S`; it is smooth of relative dimension `e` over `S`. Then via
> `Θ : c ↦ c ∩ [X]_{e+1}` composition of bivariant classes turns into the intersection product of
> section 42.64 on `X₁`, formed with the Gysin class `Δ^!` of the diagonal of `X₁` (Stacks 0FBR):
>
>   `Θ(a · b)|_{X₁} = Θ(a)|_{X₁} · Θ(b)|_{X₁}`.
>
> When `S` has no zero-dimensional component, `X₁ = X`. Over the zero-dimensional part the clause is
> false as stated, the exterior product of section 42.63 vanishing there identically
> (`Stacks.Chow.not_chowCohomologyCapFundamentalClass_mulId_fieldChowSituation`); for `X`
> equidimensional of dimension `0` the part `X₁` is empty.

```lean
theorem chowGroupRestrict_chowCohomologyCapFundamentalClass_mulId (e : ℕ)
    (hd : ∀ V : irreducibleComponents X,
      deltaDimension C sX ⟨V, V.2.1, isClosed_of_mem_irreducibleComponents _ V.2⟩ = e + 1)
    (p q : ℤ) (a : chowCohomologyComponent C (gysinSystemOfInvertible C) sX p)
    (b : chowCohomologyComponent C (gysinSystemOfInvertible C) sX q) :
    chowGroupRestrict C sX ((hS.oneDimensionalPartPreimage sX).ι ≫ sX)
        (hS.oneDimensionalPartPreimage sX).ι rfl ((e : ℤ) + 1 - (p + q))
        (chowCohomologyCapFundamentalClass C (gysinSystemOfInvertible C) sX (e + 1) (p + q)
          (a.mulId C sX b)) =
      chowGroupDegreeEquiv C ((hS.oneDimensionalPartPreimage sX).ι ≫ sX)
        (by ring : ((e : ℤ) + 1 - p) + ((e : ℤ) + 1 - q) - 1 - e = (e + 1) - (p + q))
        (chowGroupSelfProductUnitCollapse C ((hS.oneDimensionalPartPreimage sX).ι ≫ sX)
          (((e : ℤ) + 1 - p) + ((e : ℤ) + 1 - q) - 1 - e)
          (hS.intersectionProduct (gysinSystemOfInvertible C)
            ((hS.oneDimensionalPartPreimage sX).ι ≫ sX) (𝟙 _) (𝟙 _) e
            (bivariantClassCongrBase C (gysinSystemOfInvertible C)
              (pullback.diagonal ((hS.oneDimensionalPartPreimage sX).ι ≫ sX))
              (diagonal_comp_selfProductStructure C ((hS.oneDimensionalPartPreimage sX).ι ≫ sX))
              rfl e (diagonalGysinClass C ((hS.oneDimensionalPartPreimage sX).ι ≫ sX)
                ((hS.oneDimensionalPartPreimage sX).ι ≫ sX)
                (hS.relativeDimension_oneDimensionalPartPreimage sX e hd)))
            ((e : ℤ) + 1 - p) ((e : ℤ) + 1 - q)
            (chowGroupCongr C (Category.id_comp _).symm ((e : ℤ) + 1 - p)
              (chowGroupRestrict C sX ((hS.oneDimensionalPartPreimage sX).ι ≫ sX)
                (hS.oneDimensionalPartPreimage sX).ι rfl ((e : ℤ) + 1 - p)
                (chowCohomologyCapFundamentalClass C (gysinSystemOfInvertible C) sX (e + 1) p a))
              ⊗ₜ[ℤ] chowGroupCongr C (Category.id_comp _).symm ((e : ℤ) + 1 - q)
                (chowGroupRestrict C sX ((hS.oneDimensionalPartPreimage sX).ι ≫ sX)
                  (hS.oneDimensionalPartPreimage sX).ι rfl ((e : ℤ) + 1 - q)
                  (chowCohomologyCapFundamentalClass C (gysinSystemOfInvertible C) sX (e + 1) q
                    b)))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.64, Tag 0FC9](https://stacks.math.columbia.edu/tag/0FC9)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
