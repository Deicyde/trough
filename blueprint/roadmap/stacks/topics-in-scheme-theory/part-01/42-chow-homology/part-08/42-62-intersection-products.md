---
declaration: section
origin: cited
lean: Stacks.Chow.diagonalGysinProduct, Stacks.Chow.intersectionProduct, Stacks.Chow.intersectionProduct_apply, Stacks.Chow.intersectionProductBilin, Stacks.Chow.intersectionProductBilin_apply, Stacks.Chow.intersectionProductOfVirtualNormalBundle, Stacks.Chow.intersectionProductOfVirtualNormalBundleClass, Stacks.Chow.isAssociativeIntersectionProduct
statement: formalized
proof: formalized
---

# 42.62 Intersection products

Section 42.62 of the Stacks Project, [Tag 0FC0](https://stacks.math.columbia.edu/tag/0FC0). 8 tags here are carried by 25 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FC0, the section

[Tag 0FC0](https://stacks.math.columbia.edu/tag/0FC0) in the Stacks Project.

**`Stacks.Chow.diagonalGysinProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/IntersectionProduct.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/IntersectionProduct.lean#L226). The attribute's comment: “the product Δ^!(α × β), on the pullback of the diagonal rather than on Y ×\_X Z, with the Gysin class Δ^! of the diagonal carried as c (Stacks 0FBR and 0FBK supply it; no product is assumed); the exterior product's instances of Stacks 02S1 are supplied by the general case of Stacks 02S1, Stacks.Chow.flatPullbackFactorsThroughRationalEquivalence\_general, and are not carried; no property of the product is proved”.

> **Stacks Project, Tag 0FC0.** The Gysin pullback `Δ^!(α × β)` of the exterior product along
> the diagonal of `X`, read on the pullback `(Y ×_k Z) ×_{X ×_k X} X` of the diagonal. This is the
> intersection product of Stacks 0FC0 before the identification of that pullback with `Y ×_X Z`;
> `Stacks.Chow.intersectionProduct` performs the identification.
>
> It is an additive map out of `CH_n(Y) ⊗_ℤ CH_m(Z)`, so the product it defines is `ℤ`-bilinear by
> construction; `Stacks.Chow.intersectionProductBilin` is that bilinear form.
>
> The Gysin class `c` of the diagonal is a hypothesis: it is a single element of
> `A^d(X ⟶ X ×_k X)` depending on `X` alone, and it is produced from smoothness of `X` by
> `Stacks.Chow.isRegularImmersion_diagonal_of_smooth` together with the construction of Stacks
> 0FBK, which `Stacks.Chow.diagonalVirtualNormalGysinClass` carries out. The instances of Stacks
> 02S1 that the exterior product needs are not hypotheses: they are supplied by
> `Stacks.Chow.flatPullbackFactorsThroughRationalEquivalenceOnPointClosureFibres_holds`, hence
> ultimately by the general case of Stacks 02S1.

```lean
def diagonalGysinProduct :
    TensorProduct ℤ (chowGroup C (a ≫ sX) n) (chowGroup C (b ≫ sX) m) →+
      chowGroup C (pullback.fst (pullback.diagonal sX) (exteriorToSelfProduct C sX a b) ≫ sX)
        (n + m - d)
```

**`Stacks.Chow.intersectionProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/IntersectionProduct.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/IntersectionProduct.lean#L257). The attribute's comment: “the intersection product α · β = Δ^!(α × β) in CH\_\{n+m-d}(Y ×\_X Z), with Δ^! carried as c (Stacks 0FBR and 0FBK supply it; no product is assumed); the exterior product's instances of Stacks 02S1 are supplied by Stacks.Chow.flatPullbackFactorsThroughRationalEquivalence\_general and the Stacks 02S2 instance for the pushforward along Y ×\_X Z = (Y ×\_k Z) ×\_\{X ×\_k X} X by Stacks.Chow.properPushforwardDescends, so neither is carried; no property of the product is proved”.

> **Stacks Project, Tag 0FC0.** The intersection product
>
> `· : CH_n(Y) ⊗_ℤ CH_m(Z) ⟶ CH_{n+m-d}(Y ×_X Z)`
>
> of Stacks 0FC0, for `Y` and `Z` locally of finite type over a scheme `X` whose diagonal has a
> Gysin class of degree `d`. It is the Gysin pullback of the exterior product along the diagonal,
> `Stacks.Chow.diagonalGysinProduct`, pushed forward along the identification
> `(Y ×_k Z) ×_{X ×_k X} X ≅ Y ×_X Z` the source uses.
>
> The pushforward is along an isomorphism, so the only instance of Stacks 02S2 it needs is the one
> that lets proper pushforward descend to Chow groups, and that is supplied here by
> `Stacks.Chow.properPushforwardDescends` rather than assumed. The instances of Stacks 02S1 the
> exterior product needs are likewise supplied, by
> `Stacks.Chow.flatPullbackFactorsThroughRationalEquivalenceOnPointClosureFibres_holds`. The only
> hypothesis of the product is therefore the Gysin class `c` of the diagonal.

```lean
def intersectionProduct :
    TensorProduct ℤ (chowGroup C (a ≫ sX) n) (chowGroup C (b ≫ sX) m) →+
      chowGroup C (pullback.fst a b ≫ (a ≫ sX)) (n + m - d)
```

**`Stacks.Chow.intersectionProduct_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/IntersectionProduct.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/IntersectionProduct.lean#L270). The attribute's comment: “the defining formula α · β = Δ^!(α × β) of the product, unfolded”.

> **Stacks Project, Tag 0FC0.** The defining formula of the intersection product: it is the
> Gysin pullback of the exterior product along the diagonal, carried to `Y ×_X Z`.

```lean
theorem intersectionProduct_apply
    (t : TensorProduct ℤ (chowGroup C (a ≫ sX) n) (chowGroup C (b ≫ sX) m)) :
    intersectionProduct C hδ G sX a b d c n m t =
      properChowPushforward C
        (pullback.fst (pullback.diagonal sX) (exteriorToSelfProduct C sX a b) ≫ sX)
        (pullback.fst a b ≫ (a ≫ sX)) (pullbackDiagonalMapIdIso a b sX).hom
        (pullbackDiagonalMapIdIso_hom_comp_structure C sX a b) (n + m - d)
        (properPushforwardDescends C _ _ _ _ _)
        (c.cap (exteriorToSelfProduct C sX a b) (n + m)
          (chowGroupCongr C (exteriorToSelfProduct_comp_selfProductStructure C sX a b).symm
            (n + m) (chowExteriorProduct C hδ (a ≫ sX) (b ≫ sX) n m t)))
```

**`Stacks.Chow.intersectionProductBilin`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/IntersectionProduct.lean, line 291](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/IntersectionProduct.lean#L291). The attribute's comment: “the product as the bilinear map α ↦ β ↦ α · β, bilinear by construction, with the same carried hypotheses as Stacks.Chow.intersectionProduct”.

> **Stacks Project, Tag 0FC0.** The intersection product as a `ℤ`-bilinear map
>
> `CH_n(Y) → CH_m(Z) → CH_{n+m-d}(Y ×_X Z)`,
>
> which is the shape `α · β` is used in. Bilinearity is free: the product is an additive map out
> of the tensor product by construction.

```lean
def intersectionProductBilin :
    chowGroup C (a ≫ sX) n →ₗ[ℤ] chowGroup C (b ≫ sX) m →ₗ[ℤ]
      chowGroup C (pullback.fst a b ≫ (a ≫ sX)) (n + m - d)
```

**`Stacks.Chow.intersectionProductBilin_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/IntersectionProduct.lean, line 299](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/IntersectionProduct.lean#L299). The attribute's comment: “the bilinear form evaluates to the product on a pure tensor”.

> **Stacks Project, Tag 0FC0.** The bilinear form of the product agrees with the product.

```lean
theorem intersectionProductBilin_apply
    (α : chowGroup C (a ≫ sX) n) (β : chowGroup C (b ≫ sX) m) :
    intersectionProductBilin C hδ G sX a b d c n m α β =
      intersectionProduct C hδ G sX a b d c n m (TensorProduct.tmul ℤ α β)
```

**`Stacks.Chow.intersectionProductOfVirtualNormalBundle`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/IntersectionProduct.lean, line 362](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/IntersectionProduct.lean#L362). The attribute's comment: “the product α · β = Δ^!(α × β) with Δ^! the class of the diagonal built by the Stacks 0FBK construction, so no bivariant class is carried; that construction's inputs (the Stacks 0FBQ datum, Stacks 02TY bijectivity, the flat and Gysin transport laws) remain carried, while Stacks 02S1 is supplied by Stacks.Chow.flatPullbackFactorsThroughRationalEquivalence\_general and Stacks 02S2 by Stacks.Chow.properPushforwardDescends, neither being carried, and no property of the product is proved”.

> **Stacks Project, Tag 0FC0.** The intersection product of Stacks 0FC0 formed with the Gysin
> class of the diagonal that the construction of Stacks 0FBK produces, so that no bivariant class
> is assumed: the degree of the product is the rank `r` of the virtual normal bundle of the
> diagonal, which for `X` smooth is its relative dimension.

```lean
def intersectionProductOfVirtualNormalBundle
    (P : VirtualNormalBundleProjection (pullback.diagonal sX) q r)
    (hπ : ∀ {T : Scheme.{u}} (g : T ⟶ (pullback sX sX : Scheme.{u})) [LocallyOfFiniteType g]
      (k : ℤ), Function.Bijective (π g k))
    (hproper : PiProperNaturality C sX sN (pullback.diagonal sX) q r e π)
    (hflat : TransportFlatNaturality C G sX (selfProductStructure C sX) sN
      (pullback.diagonal sX) (diagonal_comp_selfProductStructure C sX) q hq r e E π hπ)
    (hgysin : TransportGysinNaturality C G sX (selfProductStructure C sX) sN
      (pullback.diagonal sX) (diagonal_comp_selfProductStructure C sX) q hq r e E π hπ)
    (n m : ℤ) :
    TensorProduct ℤ (chowGroup C (a ≫ sX) n) (chowGroup C (b ≫ sX) m) →+
      chowGroup C (pullback.fst a b ≫ (a ≫ sX)) (n + m - (r : ℤ))
```

**`Stacks.Chow.intersectionProductOfVirtualNormalBundleClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/IntersectionProductVirtualNormalBundle.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/IntersectionProductVirtualNormalBundle.lean#L63). The attribute's comment: “the product α · β = Δ^!(α × β) with Δ^! the class c(X → X ×\_k X, 𝒩) of Stacks 0FBK for a virtual normal bundle 𝒩 of the diagonal; no property of the product is proved here”.

> The intersection product `α · β = Δ^!(α × β)` formed with the Gysin class
> `Δ^! = c(X ⟶ X ×_k X, 𝒩)` of the diagonal; its degree is the rank `r` of the virtual normal
> bundle `𝒩`.

```lean
def intersectionProductOfVirtualNormalBundleClass (n m : ℤ) :
    TensorProduct ℤ (chowGroup C (a ≫ sX) n) (chowGroup C (b ≫ sX) m) →+
      chowGroup C (pullback.fst a b ≫ (a ≫ sX)) (n + m - (r : ℤ))
```

## Tag 0FC1, a lemma

[Tag 0FC1](https://stacks.math.columbia.edu/tag/0FC1) in the Stacks Project.

**`Stacks.Chow.isAssociativeIntersectionProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TripleIntersectionProduct.lean, line 656](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TripleIntersectionProduct.lean#L656). The attribute's comment: “associativity (α·β)·γ = α·(β·γ) of the Stacks 0FC0 product over a field, via the source's five-step chain; 0FBZ comes from this repository and the chain's fibre-product identification is proved here; carried are 0FBY in both variables (only its fundamental-class case is carried here) and 0FBP (needs the class half of 0FBJ), plus 02S1 and 02S2”.

> **Stacks Project, Tag 0FC1.** Associativity of the intersection product of Stacks 0FC0: for
> `X` a scheme over a field `k` whose diagonal carries a Gysin class `Δ^!` of degree `d`, and `Y`,
> `Z`, `W` locally of finite type over `X`,
>
> `(α · β) · γ = α · (β · γ)`   in   `CH_*(Y ×_X Z ×_X W)`,
>
> read through the associator of the triple fibre product over `X` and the matching of the two
> degrees, which is `Stacks.Chow.IsAssociativeIntersectionProduct`.
>
> This is the source's chain of five equalities. The two instances of Stacks 0FBY are carried, as
> `Stacks.Chow.CommutesDiagonalCapExteriorFirst` and
> `Stacks.Chow.CommutesDiagonalCapExteriorSecond` — the repository's one carrier of that tag is the
> fundamental-class case and does not cover either of them — and Stacks 0FBP is carried as
> `Stacks.Chow.DiagonalGysinCommuteOnTripleProduct`, whose carriers here would apply but for the
> class half of Stacks 0FBJ. The docstrings of those three say exactly what they assume and why
> none of them is this conclusion. Stacks 0FBZ, associativity of the exterior
> product, is **proved** in this repository and is consumed here as
> `Stacks.Chow.chowExteriorProduct_assoc`; Stacks 0F9Z is free, the cap operation of
> `Stacks.Chow.BivariantClass` being indexed by an arbitrary test morphism, so that `Δ₁₂^!` and
> `Δ₂₃^!` are cap operations of `Δ^!` itself and no triple self-product of `X` is needed; and the
> fibre-product identification the chain runs on is **proved** above, as
> `Stacks.Chow.pullbackDiagonalExteriorTestIso` with its two instances
> `Stacks.Chow.firstPartialDiagonalPullbackIso` and
> `Stacks.Chow.secondPartialDiagonalPullbackIso`.

```lean
theorem isAssociativeIntersectionProduct
    (hfirst : CommutesDiagonalCapExteriorFirst k G hpp sX a b g d Dc n m l)
    (hsecond : CommutesDiagonalCapExteriorSecond k G hpp sX a b g d Dc n m l)
    (hcommute : DiagonalGysinCommuteOnTripleProduct k G hpp sX a b g d Dc n m l) :
    IsAssociativeIntersectionProduct (fieldChowSituation k) (fun _ _ ↦ rfl) G sX a b g d Dc
      n m l hpp
```

**`Stacks.Chow.isAssociativeIntersectionProduct_canonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TripleIntersectionProductExterior.lean, line 1216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TripleIntersectionProductExterior.lean#L1216). The attribute's comment: “the whole statement: associativity (α·β)·γ = α·(β·γ) in CH\_*(Y ×\_X Z ×\_X W) of the Stacks 0FC0 product for X smooth over a field of arbitrary dimension, Y, Z, W locally of finite type over X and arbitrary α, β, γ, the product Δ^!(α × β) formed with the Gysin class of the diagonal on the open and closed parts of X of constant dimension, as in Section 0FC0”.

> **Stacks 0FC1.** Let `k` be a field, `X` smooth over `k` of arbitrary, not necessarily
> constant, dimension, and `Y`, `Z`, `W` locally of finite type over `X`. The intersection product
> `α · β = Δ^!(α × β)` of Stacks 0FC0 is formed with the Gysin class of the diagonal of Stacks 0FBR
> part by part, over the open and closed parts `X_d` of `X` of dimension `d`
> (`Stacks.Chow.dimPartOverIntersectionProduct`): for `α ∈ CH_n(Y)` and `β ∈ CH_m(Z)`, `α · β` has
> component `α|_{Y_d} · β|_{Z_d} ∈ CH_{n+m-d}(Y_d ×_{X_d} Z_d)` over `X_d`, where
> `Y_d = a⁻¹(X_d)`, `Z_d = b⁻¹(X_d)` are the parts of `Y` and `Z` over `X_d`. Then for
> `γ ∈ CH_l(W)`
>
> `(α · β) · γ = α · (β · γ)`   in   `CH_*(Y ×_X Z ×_X W)`,
>
> component by component, read through the associator of the triple fibre product over `X_d` and
> the matching of the degrees `(n + m - d) + l - d = n + (m + l - d) - d`.

```lean
theorem isAssociativeIntersectionProduct_canonical
    (α : chowGroup (fieldChowSituation k) (a ≫ sX) n)
    (β : chowGroup (fieldChowSituation k) (b ≫ sX) m)
    (γ : chowGroup (fieldChowSituation k) (g ≫ sX) l) :
    (fun d : ℕ ↦ chowGroupDegreeEquiv (fieldChowSituation k)
        (pullback.fst (dimPartOverHom sX a d)
            (pullback.fst (dimPartOverHom sX b d) (dimPartOverHom sX g d) ≫
              dimPartOverHom sX b d) ≫
          (dimPartOverHom sX a d ≫ partBase sX d))
        (intersectionProductAssocDegree n m l d)
        (properChowPushforward (fieldChowSituation k)
          (pullback.fst (pullback.fst (dimPartOverHom sX a d) (dimPartOverHom sX b d) ≫
              dimPartOverHom sX a d) (dimPartOverHom sX g d) ≫
            ((pullback.fst (dimPartOverHom sX a d) (dimPartOverHom sX b d) ≫
              dimPartOverHom sX a d) ≫ partBase sX d))
          (pullback.fst (dimPartOverHom sX a d)
              (pullback.fst (dimPartOverHom sX b d) (dimPartOverHom sX g d) ≫
                dimPartOverHom sX b d) ≫
            (dimPartOverHom sX a d ≫ partBase sX d))
          (tripleProductAssoc (dimPartOverHom sX a d) (dimPartOverHom sX b d)
            (dimPartOverHom sX g d)).hom
          (tripleProductAssoc_hom_comp_structureMorphism (fieldChowSituation k) (partBase sX d)
            (dimPartOverHom sX a d) (dimPartOverHom sX b d) (dimPartOverHom sX g d))
          ((n + m - d) + l - d) (properPushforwardDescends (fieldChowSituation k) _ _ _ _ _)
          (μ (fun d ↦ pullback.fst (dimPartOverHom sX a d) (dimPartOverHom sX b d) ≫
              dimPartOverHom sX a d) (fun d ↦ dimPartOverHom sX g d)
            (fun d : ℕ ↦ n + m - d) (fun _ ↦ l)
            (fun d ↦ chowGroupCongr (fieldChowSituation k)
              (Category.assoc (pullback.fst (dimPartOverHom sX a d) (dimPartOverHom sX b d))
                (dimPartOverHom sX a d) (partBase sX d)).symm (n + m - d)
              (μ (fun d ↦ dimPartOverHom sX a d) (fun d ↦ dimPartOverHom sX b d) (fun _ ↦ n)
                (fun _ ↦ m) res[a, n, α] res[b, m, β] d))
            res[g, l, γ] d))) =
      μ (fun d ↦ dimPartOverHom sX a d)
        (fun d ↦ pullback.fst (dimPartOverHom sX b d) (dimPartOverHom sX g d) ≫
          dimPartOverHom sX b d) (fun _ ↦ n) (fun d : ℕ ↦ m + l - d) res[a, n, α]
        (fun d ↦ chowGroupCongr (fieldChowSituation k)
          (Category.assoc (pullback.fst (dimPartOverHom sX b d) (dimPartOverHom sX g d))
            (dimPartOverHom sX b d) (partBase sX d)).symm (m + l - d)
          (μ (fun d ↦ dimPartOverHom sX b d) (fun d ↦ dimPartOverHom sX g d) (fun _ ↦ m)
            (fun _ ↦ l) res[b, m, β] res[g, l, γ] d))
```

## Tag 0FC2, a lemma

[Tag 0FC2](https://stacks.math.columbia.edu/tag/0FC2) in the Stacks Project.

**`Stacks.Chow.chowCohomologyCapFundamentalClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/SmoothCapFundamentalIso.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/SmoothCapFundamentalIso.lean#L178). The attribute's comment: “the map A^p(X) → CH\_\{d-p}(X), c ↦ c ∩ [X]\_d, for an arbitrary degree d over a general Chow situation; neither its bijectivity nor the compatibility of composition with the intersection product is covered”.

> **Stacks 0FC2.** The map `A^p(X) ⟶ CH_{d-p}(X)` of Stacks 0FC2: cap product of a bivariant
> class for the identity of `X` with the fundamental class `[X]_d`, read through the collapse of
> `X ×_X X` onto `X` along its first projection.
>
> For `X` smooth over a field and equidimensional of dimension `d` the source asserts that this map
> is an isomorphism. Neither that assertion nor the compatibility of composition with the
> intersection product is proved here; what is proved is the reduction of injectivity in
> `Stacks.Chow.chowCohomologyCapFundamentalClass_injective_iff`. See the implementation notes of
> this module.

```lean
def chowCohomologyCapFundamentalClass :
    chowCohomologyComponent C G sX p →+ chowGroup C sX (d - p)
```

**`Stacks.Chow.chowCohomologyCapFundamentalClass_injective_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/SmoothCapFundamentalIso.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/SmoothCapFundamentalIso.lean#L224). The attribute's comment: “injectivity of the map c ↦ c ∩ [X]\_d, reduced by Stacks 02UC to the statement that a class killing [X]\_d kills the fundamental class of every integral scheme locally of finite type over X; the surjectivity of the map and the compatibility of composition with the intersection product are not covered”.

> **Stacks 0FC2, injectivity reduced to Stacks 02UC.** The map `A^p(X) ⟶ CH_{d-p}(X)` of
> Stacks 0FC2 is injective exactly when every bivariant class killing the fundamental class `[X]_d`
> kills the fundamental class of every integral scheme locally of finite type over `X`.
>
> This is the whole of what Stacks 02UC contributes to the injectivity half of Stacks 0FC2, and the
> right-hand side is the statement that remains: in the source it is obtained by factoring the map
> through `A^{p-d}(X ⟶ Spec k)` using Stacks 0FBT, which is not available here. The equivalence is
> not vacuous in either direction — the forward implication uses that the zero class kills every
> fundamental class, the backward one uses Stacks 02UC proper.

```lean
theorem chowCohomologyCapFundamentalClass_injective_iff :
    Function.Injective (chowCohomologyCapFundamentalClass C G sX d p) ↔
      ∀ c : chowCohomologyComponent C G sX p,
        c.cap (𝟙 X) d (selfFundamentalClass C sX d) = 0 →
          c.CapsIntegralFundamentalClassesToZero C G sX sX (𝟙 X) (Category.id_comp sX) p
```

**`Stacks.Chow.chowCohomologyCapFundamentalClass_injective_iff_hasBirationalModification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/SmoothCapFundamentalIso.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/SmoothCapFundamentalIso.lean#L245). The attribute's comment: “injectivity of the map c ↦ c ∩ [X]\_d, reduced by clause (3) of Stacks 02UC to the existence of proper birational modifications capping to zero; the surjectivity of the map and the compatibility of composition with the intersection product are not covered”.

> **Stacks 0FC2, injectivity reduced to clause (3) of Stacks 02UC.** The same reduction as
> `Stacks.Chow.chowCohomologyCapFundamentalClass_injective_iff`, with the criterion read through
> the birational form of Stacks 02UC: it is enough that every integral scheme locally of finite
> type over `X` admit a proper birational modification whose fundamental class the class kills.

```lean
theorem chowCohomologyCapFundamentalClass_injective_iff_hasBirationalModification :
    Function.Injective (chowCohomologyCapFundamentalClass C G sX d p) ↔
      ∀ c : chowCohomologyComponent C G sX p,
        c.cap (𝟙 X) d (selfFundamentalClass C sX d) = 0 →
          c.HasBirationalModificationCappingToZero C G sX sX (𝟙 X) (Category.id_comp sX) p
```

**`Stacks.Chow.chowCohomologyCapFundamentalClass_bijective_of_smooth_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SmoothChowCohomology.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/SmoothChowCohomology.lean#L150). The attribute's comment: “first clause; equidimensional of dimension d read as of constant relative dimension d over k; bivariant classes are those of the Gysin system of invertible modules”.

> **Stacks 0FC2, first clause.** Let `X` be smooth over a field `k`, of constant relative
> dimension `d`, that is equidimensional of dimension `d`. Then
>
>   `A^p(X) ⟶ CH_{d-p}(X)`,  `c ↦ c ∩ [X]_d`
>
> is bijective.

```lean
theorem chowCohomologyCapFundamentalClass_bijective_of_smooth_field (p : ℤ) :
    Function.Bijective (chowCohomologyCapFundamentalClass (fieldChowSituation k)
      (gysinSystemOfInvertible (fieldChowSituation k)) sX d p)
```

**`Stacks.Chow.chowCohomologyCapFundamentalClass_mulId_of_smooth_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SmoothChowCohomology.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/SmoothChowCohomology.lean#L167). The attribute's comment: “second clause, with the intersection product of Stacks 0FC0 formed with the Gysin class Δ^! of the diagonal; equidimensional of dimension d read as of constant relative dimension d over k”.

> **Stacks 0FC2, second clause.** Let `X` be smooth over a field `k`, of constant relative
> dimension `d`. Via `Θ : A^p(X) ⟶ CH_{d-p}(X)`, `c ↦ c ∩ [X]_d`, composition of bivariant classes
> becomes the intersection product of Stacks 0FC0 formed with the Gysin class `Δ^!` of the
> diagonal (Stacks 0FBR):
>
>   `Θ(a · b) = Θ(a) · Θ(b)`.

```lean
theorem chowCohomologyCapFundamentalClass_mulId_of_smooth_field (p q : ℤ)
    (a : chowCohomologyComponent (fieldChowSituation k)
      (gysinSystemOfInvertible (fieldChowSituation k)) sX p)
    (b : chowCohomologyComponent (fieldChowSituation k)
      (gysinSystemOfInvertible (fieldChowSituation k)) sX q) :
    chowCohomologyCapFundamentalClass (fieldChowSituation k)
        (gysinSystemOfInvertible (fieldChowSituation k)) sX d (p + q)
        (a.mulId (fieldChowSituation k) sX b) =
      chowGroupDegreeEquiv (fieldChowSituation k) sX
        (by ring : ((d : ℤ) - p) + (d - q) - d = d - (p + q))
        (chowGroupSelfProductUnitCollapse (fieldChowSituation k) sX
          (((d : ℤ) - p) + (d - q) - d)
          (intersectionProduct (fieldChowSituation k) (fun _ _ ↦ rfl)
            (gysinSystemOfInvertible (fieldChowSituation k)) sX (𝟙 X) (𝟙 X) d
            (bivariantClassCongrBase (fieldChowSituation k)
              (gysinSystemOfInvertible (fieldChowSituation k)) (pullback.diagonal sX)
              (diagonal_comp_selfProductStructure (fieldChowSituation k) sX) rfl d
              (diagonalGysinClass (fieldChowSituation k) sX sX hd))
            ((d : ℤ) - p) ((d : ℤ) - q)
            (chowGroupCongr (fieldChowSituation k) (Category.id_comp sX).symm ((d : ℤ) - p)
              (chowCohomologyCapFundamentalClass (fieldChowSituation k)
                (gysinSystemOfInvertible (fieldChowSituation k)) sX d p a) ⊗ₜ[ℤ]
              chowGroupCongr (fieldChowSituation k) (Category.id_comp sX).symm ((d : ℤ) - q)
                (chowCohomologyCapFundamentalClass (fieldChowSituation k)
                  (gysinSystemOfInvertible (fieldChowSituation k)) sX d q b))))
```

## Tag 0FFB, a lemma

[Tag 0FFB](https://stacks.math.columbia.edu/tag/0FFB) in the Stacks Project.

**`Stacks.Chow.GysinMapExists.of_smooth_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/Factorization.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/Factorization.lean#L98). The attribute's comment: “the Gysin map exists for a morphism of schemes smooth over the base”.

> **Stacks 0FFB and Stacks 0FFC, first assertion.** The Gysin map exists for a morphism
> `f : X ⟶ Y` over a base `S` whose source is smooth over `S`.
>
> Indeed `f ≫ sY` is the structure morphism `sX : X ⟶ S`, for which the Gysin map exists because a
> smooth morphism is its own factorization through the identity of its source. Over a field this is
> the assertion of Stacks 0FFB and of Stacks 0FFC that the Gysin map exists for a morphism of
> schemes smooth over the field; smoothness of the target is not needed.

```lean
theorem GysinMapExists.of_smooth_source {X Y S : Scheme.{u}} (f : X ⟶ Y) (sY : Y ⟶ S)
    (sX : X ⟶ S) [Smooth sX] (hbase : f ≫ sY = sX) : GysinMapExists f
```

**`Stacks.Chow.codimensionGysin_codimensionIntersectionProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/SmoothIntersectionProductMixed.lean, line 975](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/SmoothIntersectionProductMixed.lean#L975). The attribute's comment: “the whole statement for a morphism `f` of schemes smooth over a field, of arbitrary dimension: its Gysin map `f^!` exists and `f^!(α · β) = f^!α · f^!β`, for `f^!` the Gysin map of `f` itself acting part by part and products formed part by part on the open and closed parts of constant dimension”.

> **Stacks 0FFB: `f^!(α · β) = f^!α · f^!β`.** Let `f : X ⟶ Y` be a morphism of schemes
> smooth over a field `k`, of arbitrary and not necessarily constant dimension. Then
> `f` is a local complete intersection morphism for which the Gysin map `f^!` of Stacks 0FF3 exists
> (`AlgebraicGeometry.isLocalCompleteIntersectionMorphism_of_smooth_of_smooth`,
> `Stacks.Chow.GysinMapExists.of_smooth_source`), and for `α ∈ CH^i(Y)` and `β ∈ CH^j(Y)`
>
>   `f^!(α · β) = f^!α · f^!β`   in   `CH^{i+j}(X)`,
>
> for `f^!` the Gysin map of `f` acting on classes graded by codimension
> (`Stacks.Chow.codimensionGysin`) and the intersection product
> `Stacks.Chow.codimensionIntersectionProduct` of Stacks 0FC0, formed part by part on the open
> and closed parts of `X` and `Y` of constant dimension.
>
> Both sides are compared on each piece `X_{d,e}`, where `f^!` is the Gysin map of `f` restricted to
> `X_{d,e}` and `Y_e` (`Stacks.Chow.dimPartPieceGysinClass`): the left is `f^!(α_e · β_e)`; the
> right is the restriction of a product on `X_d`, which is the product of the restrictions
> (`Stacks.Chow.chowGroupRestrict_selfIntersectionProduct_canonical`); and the two agree by the
> source's argument (`Stacks.Chow.BivariantClass.capTargetHom_selfIntersectionProduct`), whose
> inputs Stacks 0FF7 and Stacks 0FF6 for `f^!` on the piece are
> `Stacks.Chow.dimPartPieceGysinClass_capTargetHom_fundamentalChowClass` and
> `Stacks.Chow.dimPartPieceGysinClass_bivariantCommute`.

```lean
theorem codimensionGysin_codimensionIntersectionProduct
    (i j : ℤ) (α : codimensionChowGroup k sY i) (β : codimensionChowGroup k sY j) :
    codimensionGysin sX sY hf (i + j) (codimensionIntersectionProduct k sY i j α β) =
      codimensionIntersectionProduct k sX i j (codimensionGysin sX sY hf i α)
        (codimensionGysin sX sY hf j β)
```

## Tag 0FFC, a lemma

[Tag 0FFC](https://stacks.math.columbia.edu/tag/0FFC) in the Stacks Project.

**`Stacks.Chow.GysinMapExists.of_smooth_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/Factorization.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/Factorization.lean#L98). The attribute's comment: “the Gysin map exists for a morphism of schemes smooth over the base”.

> **Stacks 0FFB and Stacks 0FFC, first assertion.** The Gysin map exists for a morphism
> `f : X ⟶ Y` over a base `S` whose source is smooth over `S`.
>
> Indeed `f ≫ sY` is the structure morphism `sX : X ⟶ S`, for which the Gysin map exists because a
> smooth morphism is its own factorization through the identity of its source. Over a field this is
> the assertion of Stacks 0FFB and of Stacks 0FFC that the Gysin map exists for a morphism of
> schemes smooth over the field; smoothness of the target is not needed.

```lean
theorem GysinMapExists.of_smooth_source {X Y S : Scheme.{u}} (f : X ⟶ Y) (sY : Y ⟶ S)
    (sX : X ⟶ S) [Smooth sX] (hbase : f ≫ sY = sX) : GysinMapExists f
```

**`Stacks.Chow.properChowPushforward_dimensionCodimensionIntersectionProduct_codimensionGysin`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/SmoothIntersectionProductMixed.lean, line 1053](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/SmoothIntersectionProductMixed.lean#L1053). The attribute's comment: “the whole statement for a proper morphism `f` of schemes smooth over a field, of arbitrary dimension: its Gysin map `f^!` exists and `f_*(α · f^!β) = f_*α · β`, for `f^!` the Gysin map of `f` itself acting part by part and products formed part by part on the open and closed parts of constant dimension”.

> **Stacks 0FFC: the projection formula `f_*(α · f^!β) = f_*α · β`.** Let `f : X ⟶ Y` be a
> proper morphism of schemes smooth over a field `k`, of arbitrary and not
> necessarily constant dimension. Then the Gysin map `f^!` of Stacks 0FF3 exists
> (`Stacks.Chow.GysinMapExists.of_smooth_source`), and for `α ∈ CH_n(X)` and `β ∈ CH^j(Y)`
>
>   `f_*(α · f^!β) = f_*α · β`   in   `CH_{n-j}(Y)`,
>
> for `f^!` the Gysin map of `f` acting on classes graded by codimension
> (`Stacks.Chow.codimensionGysin`) and the intersection product
> `Stacks.Chow.dimensionCodimensionIntersectionProduct` of Stacks 0FC0, formed part by part on the
> open and closed parts of `X` and `Y` of constant dimension.
>
> Both sides are compared on each part `Y_e` of `Y`, where `f_*` becomes the pushforward from
> `f⁻¹(Y_e)`. Writing `β_e = c ∩ [Y_e]_e` (Stacks 0FC2), one has `γ · β_e = c ∩ γ` and
> `c ∩ f_*α = f_*(res(c) ∩ α)` (`Stacks.Chow.chowCohomologyCap_properChowPushforward_restriction`),
> and `α · f^!β = res(c) ∩ α` on `f⁻¹(Y_e)`, checked on each piece `X_{d,e}`: there
> `f^!β_e = res(c) ∩ [X_{d,e}]_d` by Stacks 0FF6 and Stacks 0FF7 for the Gysin map of `f`
> restricted to the piece
> (`Stacks.Chow.BivariantClass.capTargetHom_chowCohomologyCapFundamentalClass_heq`,
> `Stacks.Chow.dimPartPieceGysinClass_bivariantCommute`,
> `Stacks.Chow.dimPartPieceGysinClass_capTargetHom_fundamentalChowClass`), and
> `α · (res(c) ∩ [X_{d,e}]_d) = res(c) ∩ α` by Stacks 0FC2 and the symmetry of the product.

```lean
theorem properChowPushforward_dimensionCodimensionIntersectionProduct_codimensionGysin
    (n j : ℤ) (α : chowGroup (fieldChowSituation k) sX n) (β : codimensionChowGroup k sY j) :
    properChowPushforward (fieldChowSituation k) sX sY f hf (n - j)
        (properPushforwardDescends _ _ _ _ _ _)
        (dimensionCodimensionIntersectionProduct k sX n j α (codimensionGysin sX sY hf j β)) =
      dimensionCodimensionIntersectionProduct k sY n j
        (properChowPushforward (fieldChowSituation k) sX sY f hf n
          (properPushforwardDescends _ _ _ _ _ _) α) β
```

## Tag 0FFD, a lemma

[Tag 0FFD](https://stacks.math.columbia.edu/tag/0FFD) in the Stacks Project.

**`Stacks.Chow.Intersection.selfIntersectionProduct_diagonalGysinClass_mk_of_cohenMacaulayAtIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Intersection/CohenMacaulayIntersectionProduct.lean, line 1036](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Intersection/CohenMacaulayIntersectionProduct.lean#L1036).

> **Stacks Project, Tag 0FFD.** Let `k` be a field, let `X` be an integral scheme smooth over
> `k` of dimension `dX`, and let `Y, Z ⊆ X` be integral closed subschemes of dimensions `dY` and
> `dZ`. Put `d = dY + dZ - dX`, and assume
>
> 1. `dim(Y ∩ Z) ≤ d`, and
> 2. `𝒪_{Y,ξ}` and `𝒪_{Z,ξ}` are Cohen–Macaulay for every `ξ ∈ Y ∩ Z` with `δ(ξ) = d`.
>
> Then `[Y] · [Z] = [Y ∩ Z]_d` in `CH_d(X)`, where the intersection product
> `Stacks.Chow.selfIntersectionProduct` is formed with the Gysin class `Δ^!` of the diagonal of
> `X ⟶ Spec k` (Stacks 0FBR), and `Y ∩ Z = Y ×_X Z` is the scheme-theoretic intersection.
>
> This is the source's proof: `Y ×_k Z` is pure of dimension `dY + dZ`, its local rings at the
> points of `Y ∩ Z` of `δ`-dimension `d` are Cohen–Macaulay by Stacks 045J, and Stacks 0FEA for
> `Δ^!` (`Stacks.Chow.diagonalGysinClass_capCohenMacaulayFormula`, from Stacks 0FBM at vanishing
> excess for its closed factor) gives `Δ^! ∩ [Y ×_k Z] = [Y ∩ Z]_d`. Hypothesis (1) is stated as
> `dim(Y ∩ Z) + dX ≤ dY + dZ`, which is `dim(Y ∩ Z) ≤ d` without the subtraction.

```lean
theorem selfIntersectionProduct_diagonalGysinClass_mk_of_cohenMacaulayAtIntersection
    {X Y Z : Scheme.{u}} (p : X ⟶ (fieldChowSituation k).S) [LocallyOfFiniteType p] [Smooth p]
    [IsIntegral X] (i : Y ⟶ X) [IsClosedImmersion i] [IsIntegral Y] (j : Z ⟶ X)
    [IsClosedImmersion j] [IsIntegral Z] (dX dY dZ : ℕ) (d : ℤ)
    (hXdim : topologicalKrullDim X = (dX : WithBot ℕ∞))
    (hYdim : topologicalKrullDim Y = (dY : WithBot ℕ∞))
    (hZdim : topologicalKrullDim Z = (dZ : WithBot ℕ∞)) (hd : (dY : ℤ) + dZ - dX = d)
    (hIntDim : topologicalKrullDim ↑(pullback i j) + (dX : WithBot ℕ∞) ≤
      (dY : WithBot ℕ∞) + (dZ : WithBot ℕ∞))
    (hCM : CohenMacaulayAtIntersection k p i j d) :
    chowGroupDegreeEquiv (fieldChowSituation k) p hd
        (selfIntersectionProduct (fieldChowSituation k)
          (Stacks.Chow.fieldChowSituation_dimensionFunction_of_isClosed k)
          (Stacks.WeilCohomology.fieldGysinSystem k) p dX
          (diagonalGysinClassOverField k p
            (relativeDimension_of_isIntegral_of_topologicalKrullDim_eq k p hXdim)) dY dZ
          (QuotientAddGroup.mk (cycleAssociatedToClosedSubscheme (fieldChowSituation k) p i dY))
          (QuotientAddGroup.mk
            (cycleAssociatedToClosedSubscheme (fieldChowSituation k) p j dZ))) =
      QuotientAddGroup.mk (cycleAssociatedToClosedSubscheme (fieldChowSituation k) p
        (pullback.fst i j ≫ i) d)
```

**`Stacks.Chow.Intersection.diagonalPullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Intersection/CohenMacaulayProperIntersection.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Intersection/CohenMacaulayProperIntersection.lean#L198). The attribute's comment: “the scheme-theoretic identification `Y ∩ Z = X ×_{Δ, X ×_k X} (Y ×_k Z)`”.

> **Stacks Project, Tag 0FFD.** The scheme-theoretic identification
> `Y ∩ Z = X ×_{Δ, X ×_k X} (Y ×_k Z)` used by the source to recognise the source of the Gysin
> class as the intersection. It is the pullback square of Stacks 01KR expressing that
> `Y ×_X Z ⟶ Y ×_k Z` is the base change of the diagonal along `Y ×_k Z ⟶ X ×_k X`.

```lean
def diagonalPullbackIso (p : X ⟶ Spec (.of k)) (i : Y ⟶ X) (j : Z ⟶ X) :
    (diagonalPullback p i j) ≅ (pullback i j : Scheme.{u})
```

**`Stacks.Chow.Intersection.gysinFormulaHypotheses_of_cohenMacaulayAtIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Intersection/CohenMacaulayProperIntersection.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Intersection/CohenMacaulayProperIntersection.lean#L287). The attribute's comment: “the reduction of the lemma to Stacks 0FEA: the identification of the intersection with the diagonal pullback, and hypotheses (2), (3) and (4) of 0FEA at the diagonal of X → Spec k. Neither the conclusion [Y]·[Z] = [Y ∩ Z]\_d nor 0FEA itself is stated; carries ProductStalkCohenMacaulay for Stacks 045J. The docstring says what is covered in full”.

> **Stacks Project, Tag 0FFD.** Let `k` be a field, let `X` be an integral scheme smooth over
> `k` of dimension `dX`, and let `Y, Z ⊆ X` be integral closed subschemes of dimensions `dY` and
> `dZ`. Put `d = dY + dZ - dX`. Assume
>
> 1. `dim (Y ∩ Z) ≤ d`, and
> 2. `𝒪_{Y,ξ}` and `𝒪_{Z,ξ}` are Cohen–Macaulay for every `ξ ∈ Y ∩ Z` with `δ(ξ) = d`.
>
> Then the hypotheses of the higher-codimension Gysin formula of Stacks 0FEA hold for the diagonal
> `Δ : X ⟶ X ×_k X` and the morphism `Y ×_k Z ⟶ X ×_k X`, which is what the source's proof
> establishes before quoting that formula to conclude `[Y] · [Z] = [Y ∩ Z]_d`.
>
> What this theorem covers of Stacks 0FFD, and what it does not: it is the reduction of the lemma
> to Stacks 0FEA, namely the identification `Y ∩ Z = X ×_{Δ, X ×_k X} (Y ×_k Z)` together with the
> verification of hypotheses (2), (3) and (4) of 0FEA at the diagonal of `X ⟶ Spec k`. The
> conclusion `[Y] · [Z] = [Y ∩ Z]_d` is **not** stated, and neither is Stacks 0FEA itself, for the
> reason recorded in the implementation notes of
> `StacksFrontier.AlgebraicGeometry.Chow.DiagonalGysin`. Hypothesis (1) of 0FEA concerns the virtual
> normal sheaf `𝒯_{X/k}` of Stacks 0FBQ rather than the situation `(X, Y, Z)`, so it is not among
> the clauses verified here. The scheme-level form of Stacks 045J that the source uses at exactly
> this point is taken as the hypothesis `ProductStalkCohenMacaulay`; it is proved in
> `productStalkCohenMacaulay`, and
> `gysinFormulaHypotheses_of_cohenMacaulayAtIntersection'` is this statement with that hypothesis
> discharged.

```lean
theorem gysinFormulaHypotheses_of_cohenMacaulayAtIntersection (k : Type u) [Field k]
    {X Y Z : Scheme.{u}} (p : X ⟶ Spec (.of k)) [Smooth p] [IsIntegral X]
    (i : Y ⟶ X) [IsClosedImmersion i] [IsIntegral Y]
    (j : Z ⟶ X) [IsClosedImmersion j] [IsIntegral Z]
    (dX dY dZ d : ℕ)
    (_hXdim : topologicalKrullDim X = (dX : WithBot ℕ∞))
    (hYdim : topologicalKrullDim Y = (dY : WithBot ℕ∞))
    (hZdim : topologicalKrullDim Z = (dZ : WithBot ℕ∞))
    (_hd : dY + dZ = dX + d)
    (hIntDim : topologicalKrullDim ↑(pullback i j) ≤ (d : WithBot ℕ∞))
    (hCM : CohenMacaulayAtIntersection k p i j (d : ℤ))
    (hAscent : ProductStalkCohenMacaulay k p i j) :
    GysinFormulaHypotheses k p i j dY dZ d
```

**`Stacks.Chow.Intersection.gysinFormulaHypotheses_of_cohenMacaulayAtIntersection'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Intersection/CohenMacaulayProperIntersection.lean, line 425](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Intersection/CohenMacaulayProperIntersection.lean#L425). The attribute's comment: “the reduction of the lemma to Stacks 0FEA from hypotheses (1) and (2) alone: the identification of the intersection with the diagonal pullback, and hypotheses (2), (3) and (4) of 0FEA at the diagonal of X → Spec k. Nothing is carried. Neither the conclusion [Y]·[Z] = [Y ∩ Z]\_d nor 0FEA itself is stated, and hypothesis (1) of 0FEA, about the virtual normal sheaf, is not among the clauses. The docstring says what is covered in full”.

> **Stacks Project, Tag 0FFD.** Let `k` be a field, let `X` be an integral scheme smooth over
> `k` of dimension `dX`, and let `Y, Z ⊆ X` be integral closed subschemes of dimensions `dY` and
> `dZ`. Put `d = dY + dZ - dX`. Assume
>
> 1. `dim (Y ∩ Z) ≤ d`, and
> 2. `𝒪_{Y,ξ}` and `𝒪_{Z,ξ}` are Cohen–Macaulay for every `ξ ∈ Y ∩ Z` with `δ(ξ) = d`.
>
> Then the hypotheses of the higher-codimension Gysin formula of Stacks 0FEA hold for the diagonal
> `Δ : X ⟶ X ×_k X` and the morphism `Y ×_k Z ⟶ X ×_k X`, which is what the source's proof
> establishes before quoting that formula to conclude `[Y] · [Z] = [Y ∩ Z]_d`.
>
> This is `Stacks.Chow.Intersection.gysinFormulaHypotheses_of_cohenMacaulayAtIntersection` with
> its carried hypothesis `ProductStalkCohenMacaulay` discharged by
> `Stacks.Chow.Intersection.productStalkCohenMacaulay`, so hypotheses (1) and (2) of the source
> are the only ones it takes. It states no more than that theorem does: the conclusion
> `[Y] · [Z] = [Y ∩ Z]_d` is **not** stated, and neither is Stacks 0FEA itself, for the reason
> recorded in the implementation notes of
> `StacksFrontier.AlgebraicGeometry.Chow.DiagonalGysin`; and hypothesis (1) of 0FEA, which concerns
> the virtual normal sheaf `𝒯_{X/k}` of Stacks 0FBQ rather than the situation `(X, Y, Z)`, is not
> among the clauses verified here.

```lean
public theorem gysinFormulaHypotheses_of_cohenMacaulayAtIntersection' (k : Type u) [Field k]
    {X Y Z : Scheme.{u}} (p : X ⟶ Spec (.of k)) [Smooth p] [IsIntegral X]
    (i : Y ⟶ X) [IsClosedImmersion i] [IsIntegral Y]
    (j : Z ⟶ X) [IsClosedImmersion j] [IsIntegral Z]
    (dX dY dZ d : ℕ)
    (hXdim : topologicalKrullDim X = (dX : WithBot ℕ∞))
    (hYdim : topologicalKrullDim Y = (dY : WithBot ℕ∞))
    (hZdim : topologicalKrullDim Z = (dZ : WithBot ℕ∞))
    (hd : dY + dZ = dX + d)
    (hIntDim : topologicalKrullDim ↑(pullback i j) ≤ (d : WithBot ℕ∞))
    (hCM : CohenMacaulayAtIntersection k p i j (d : ℤ)) :
    GysinFormulaHypotheses k p i j dY dZ d
```

## Tag 0FFE, a lemma

[Tag 0FFE](https://stacks.math.columbia.edu/tag/0FFE) in the Stacks Project.

**`Stacks.Chow.intersectionProduct_fundamentalChowClass_eq_pushforward_regularImmersionGysin`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/RegularImmersionIntersectionProduct.lean, line 363](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinLocalCompleteIntersection/RegularImmersionIntersectionProduct.lean#L363). The attribute's comment: “the whole statement for a regular closed immersion i : Y → X with X smooth over a field, of arbitrary dimension, and Y equidimensional of dimension e: α · [Y]\_e = i\_*(i^!(α)) for every j and every α ∈ CH^j(X), the classes graded by codimension on the open and closed parts X\_d of X of constant dimension, both sides in CH\_\{e-j}(X); i^! is the Gysin map of i itself acting part by part, and the product is formed part by part on the X\_d”.

> **Stacks 0FFE: `α · [Y]_e = i_*(i^!α)`.** Let `k` be a field, let `X` be a scheme smooth over
> `k`, of arbitrary and not necessarily constant dimension, and let `i : Y ⟶ X` be a regular closed
> immersion with `Y` equidimensional of dimension `e`. Then for every `α ∈ CH^j(X)`
>
>   `α · i_*[Y]_e = i_*(i^!α)`   in   `CH_{e-j}(X)`,
>
> for `·` the intersection product of Section 0FC0, formed part by part on the open and closed parts
> `X_d` of `X` of constant dimension (`Stacks.Chow.codimensionDimensionIntersectionProduct`),
> `[Y]_e` the fundamental class of Stacks 0FE4, `i_*` proper pushforward, and `i^!` the Gysin map of
> Stacks 0FF3 of `i` acting part by part (`Stacks.Chow.regularImmersionGysin`).
>
> Both sides are compared on each part `X_d`. Writing `α_d = c ∩ [X_d]_d` (Stacks 0FC2), the
> source's chain `i\_*(i^!(c ∩ [X\_d]\_d)) = i\_*(c ∩ i^![X\_d]\_d) = i\_*(c ∩ [Y\_d]\_e) = c ∩ i\_*[Y\_d]\_e =
> α\_d · [Y\_d]\_e` is Stacks 0FF6
> (`Stacks.Chow.regularImmersionPartGysinClass_commutesWithEveryClass`), Stacks 0FF7
> (`Stacks.Chow.regularImmersionPartGysinClass_capTargetHom_fundamentalChowClass`), the projection
> formula of a bivariant class (`Stacks.Chow.chowCohomologyCap_properChowPushforward_restriction`)
> and Stacks 0FC2 (`Stacks.WeilCohomology.canonicalDiagonalClassFamily_capEqProduct`). See the
> module documentation for the grading.

```lean
theorem intersectionProduct_fundamentalChowClass_eq_pushforward_regularImmersionGysin
    (hreg : Stacks.AlgebraicGeometry.RegularIdealSheaf.IsRegularImmersion i) (e : ℕ)
    (hY : RelativeDimension (i ≫ sX) e) (j : ℤ) (α : codimensionChowGroup k sX j) :
    codimensionDimensionIntersectionProduct k sX j e α
        (properChowPushforward (fieldChowSituation k) (i ≫ sX) sX i rfl e
          (properPushforwardDescends _ _ _ _ _ _)
          (fundamentalChowClass (fieldChowSituation k) (i ≫ sX) e)) =
      properChowPushforward (fieldChowSituation k) (i ≫ sX) sX i rfl (e - j)
        (properPushforwardDescends _ _ _ _ _ _) (regularImmersionGysin sX i hreg e j α)
```

**`Stacks.Chow.intersectionProduct_fundamentalChowClass_eq_pushforward_gysin`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/IntersectionProductRegularImmersion.lean, line 426](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/IntersectionProductRegularImmersion.lean#L426). The attribute's comment: “alpha . i\_*[Y]\_e = i\_*(i^!(alpha)), with the product of Tag 0FC0 at a = b = identity and i^! the Gysin class CHARACTERIZED by Tag 0FBK for a virtual normal bundle of rank r, the lci Gysin map not being constructed in this repository. e = d - r is FORCED by the degrees of the two sides, so nothing is lost by not binding e separately; equidimensionality of Y is the delta-dimension bound dim\_delta(Y) <= e, which is WEAKER than a generic-point equality, and equidimensionality of X is not assumed, entering only through the degree of the carried diagonal class. CARRIED: the i^! half of Tag 0FF6, which is Tag 0FBP, as h0FBP; and clauses (1) and (2) of Tag 0FC2 as hA and h0FC2, neither being formalized -- 0FC2 is formalized only as the map c |-> c cap [X]\_d plus injectivity reductions. PROVED here: i^![X]\_d = [Y]\_e (Tag 0FBM at vanishing excess, g = identity) and c cap i\_*beta = i\_*(c cap beta) (Tag 0B76 clause (1) at the test scheme identity), and the chain combining them with the three carried clauses. Also carried: 0FBM's hinj (Tag 02TY) and hcone, Tags 02S1 and 02S2, and the side conditions Tag 0FBV and 0FC0 already carry. THE TAG'S REGULARITY HYPOTHESIS IS PRESENT AS `_hreg` BUT UNUSED, being encoded in the virtual normal projection together with vanishing excess. The source's reduction of a non-equidimensional smooth X to its clopen constant-dimension pieces is NOT carried out, that sum being a statement about graded CH\_*(X); the same limitation the tree records for 0FF7”.

> **Stacks 0FFE.** Let `i : Y ⟶ X` be a closed immersion of schemes locally of finite type over
> the base, carrying a virtual normal bundle of constant rank `r`, let `cd` be a Gysin class of the
> diagonal of `X` of degree `d` — the class `Δ^!` through which Stacks 0FC0 defines the
> intersection product, of degree `d` for `X` smooth and equidimensional of dimension `d` — and let
> `ci` be the Gysin class `i^!` of Stacks 0FBK for `i`. Let `α = c ∩ [X]_d` for a bivariant class
> `c ∈ A^p(X)`, and let `Y` have delta-dimension at most `e = d - r`. Then
>
>   `α · i_*[Y]_e = i_*(i^!(α))`   in   `CH_{e-p}(X)`,
>
> the two sides being read on `X` through the collapse of `X ×_X X` and through the transport
> between the two ways of writing their common degree.
>
> The proof is the source's: `h0FC2` replaces the product by `c ∩ -`,
> `Stacks.Chow.chowCohomologyCap_properChowPushforward` moves `i_*` across `c ∩ -`,
> `Stacks.Chow.closedImmersionBivariantCap_fundamentalChowClass` identifies `i^![X]_d` with
> `[Y]_e`, and `h0FBP` moves `i^!` across `c ∩ -`. See the implementation notes for what each
> hypothesis is, and why neither carried hypothesis is the conclusion.

```lean
theorem intersectionProduct_fundamentalChowClass_eq_pushforward_gysin
    (c : chowCohomologyComponent C G sX p)
    (hinj : ∀ {T : Scheme.{u}} (g : T ⟶ X) [LocallyOfFiniteType g] (k : ℤ),
      Function.Injective
        (bundleFlatPullback C (i ≫ sX) sN i q hq r NP.flat NP.relativeDimension hdesc g k))
    {ci : BivariantClass C G (i ≫ sX) sX i rfl (r : ℤ)}
    (hci : IsVirtualNormalGysinClass C G (i ≫ sX) sX sN i rfl q hq r 0 E
      (bundleFlatPullback C (i ≫ sX) sN i q hq r NP.flat NP.relativeDimension hdesc) NP ci)
    (hY : schemeDeltaDimension C (i ≫ sX) ≤ ((d - (r : ℤ) : ℤ) : EInt))
    (_hreg : Stacks.AlgebraicGeometry.RegularIdealSheaf.IsRegularImmersion i)
    (hcone : chowGroupDegreeEquiv C (pullback.fst (q ≫ i) (𝟙 X) ≫ sN)
        (by omega : d - (0 : ℤ) = (d - (r : ℤ)) + (r : ℤ))
        (E.cap (𝟙 X) d (fundamentalChowClass C (𝟙 X ≫ sX) d)) =
      fundamentalChowClass C (pullback.fst (q ≫ i) (𝟙 X) ≫ sN) ((d - (r : ℤ)) + (r : ℤ)))
    (α : chowGroup C sX (d - p))
    (hα : chowCohomologyCap C G sX p c d (fundamentalChowClass C sX d) = α)
    (h0FBP : ∀ (k : ℤ) (x : chowGroup C sX k),
      closedImmersionBivariantCap C G sX i (r : ℤ) ci (k - p)
          (chowCohomologyCap C G sX p c k x) =
        chowGroupDegreeEquiv C (i ≫ sX) (by ring : k - (r : ℤ) - p = k - p - (r : ℤ))
          (chowCohomologyCapOnSubscheme C G sX i p c (k - (r : ℤ))
            (closedImmersionBivariantCap C G sX i (r : ℤ) ci k x)))
    (h0FC2 : ∀ β : chowGroup C sX (d - (r : ℤ)),
      chowGroupSelfProductUnitCollapse C sX ((d - p) + (d - (r : ℤ)) - d)
          (intersectionProduct C hδ G sX (𝟙 X) (𝟙 X) d cd (d - p) (d - (r : ℤ))
            (TensorProduct.tmul ℤ (chowGroupCongr C (Category.id_comp sX).symm (d - p) α)
              (chowGroupCongr C (Category.id_comp sX).symm (d - (r : ℤ)) β))) =
        chowGroupDegreeEquiv C sX
          (by ring : (d - (r : ℤ)) - p = (d - p) + (d - (r : ℤ)) - d)
          (chowCohomologyCap C G sX p c (d - (r : ℤ)) β)) :
    chowGroupSelfProductUnitCollapse C sX ((d - p) + (d - (r : ℤ)) - d)
        (intersectionProduct C hδ G sX (𝟙 X) (𝟙 X) d cd (d - p) (d - (r : ℤ))
          (TensorProduct.tmul ℤ (chowGroupCongr C (Category.id_comp sX).symm (d - p) α)
            (chowGroupCongr C (Category.id_comp sX).symm (d - (r : ℤ))
              (properChowPushforward C (i ≫ sX) sX i rfl (d - (r : ℤ)) (hpp _ _ _ _ _)
                (fundamentalChowClass C (i ≫ sX) (d - (r : ℤ))))))) =
      chowGroupDegreeEquiv C sX (by ring : (d - p) - (r : ℤ) = (d - p) + (d - (r : ℤ)) - d)
        (properChowPushforward C (i ≫ sX) sX i rfl ((d - p) - (r : ℤ)) (hpp _ _ _ _ _)
          (closedImmersionBivariantCap C G sX i (r : ℤ) ci (d - p) α))
```

## Tag 0FFF, a lemma

[Tag 0FFF](https://stacks.math.columbia.edu/tag/0FFF) in the Stacks Project.

**`Stacks.Chow.codimensionRationalChowEquiv_codimensionIntersectionProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalIntersection/RationalIntersectionProduct.lean, line 918](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalIntersection/RationalIntersectionProduct.lean#L918). The attribute's comment: “the whole lemma: for X smooth over k, quasi-compact, with affine diagonal, the identification CH^*(X) ⊗ Q ≅ CH\_*(X) ⊗ Q carries the product of 0FC0 tensored with Q, (q ⊗ α)(q' ⊗ β) = qq' ⊗ α · β, to the product of 0FEX”.

> **Stacks Project, Tag 0FFF.** Let `k` be a field and let `X` be a smooth scheme over `k`
> which is quasi-compact and has affine diagonal. Then the intersection product of Section 0FC0 on
> `CH^*(X)` agrees after tensoring with `𝐐` with the intersection product of Section 0FEX: the
> identification `CH^*(X) ⊗ 𝐐 = (⨁_i CH^i(X)) ⊗ 𝐐 ≅ CH_*(X) ⊗ 𝐐`
> (`Stacks.Chow.codimensionRationalChowEquiv`) carries the product
> `(q ⊗ α) · (q' ⊗ β) = qq' ⊗ α · β` of `CH^*(X) ⊗ 𝐐`, with `α · β ∈ CH^{i+j}(X)` the product of
> Section 0FC0 (`Stacks.Chow.codimensionIntersectionProduct`) for `α ∈ CH^i(X)` and `β ∈ CH^j(X)`,
> to the product of Section 0FEX.

```lean
theorem codimensionRationalChowEquiv_codimensionIntersectionProduct [CompactSpace X]
    [IsAffineHom (pullback.diagonal (terminal.from X))] (i j : ℤ) (q q' : ℚ)
    (a : codimensionChowGroup k sX i) (b : codimensionChowGroup k sX j) :
    haveI := isNoetherian_of_compactSpace sX
    codimensionRationalChowEquiv k sX ((q * q') ⊗ₜ[ℤ]
        DirectSum.of (codimensionChowGroup k sX) (i + j)
          (codimensionIntersectionProduct k sX i j a b)) =
      rationalIntersectionProduct (isRegular_of_smooth_over_field sX)
        (exists_bounds_relativeDimension_fieldChowSituation k sX)
        (codimensionRationalChowEquiv k sX (q ⊗ₜ[ℤ] DirectSum.of (codimensionChowGroup k sX) i a))
        (codimensionRationalChowEquiv k sX
          (q' ⊗ₜ[ℤ] DirectSum.of (codimensionChowGroup k sX) j b))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.62, Tag 0FC0](https://stacks.math.columbia.edu/tag/0FC0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
