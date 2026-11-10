---
declaration: section
origin: cited
lean: Stacks.WeilCohomology.correspondenceToPointEquiv, Stacks.WeilCohomology.correspondenceFromPointEquiv, Stacks.WeilCohomology.corrToPointEquiv_pullback_canonicalDiagonalClassFamily, Stacks.WeilCohomology.corrFromPointEquiv_pushforward_canonicalDiagonalClassFamily, Stacks.WeilCohomology.comp_bilinear_assoc_canonicalDiagonalClassFamily, Stacks.WeilCohomology.comp_pullback_pushforward_canonicalDiagonalClassFamily, Stacks.WeilCohomology.corrToPointEquiv, Stacks.WeilCohomology.corrFromPointEquiv
statement: formalized
proof: formalized
---

# 45.3 Correspondences

Section 45.3 of the Stacks Project, [Tag 0FFZ](https://stacks.math.columbia.edu/tag/0FFZ). 9 tags here are carried by 51 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FG0, a lemma

[Tag 0FG0](https://stacks.math.columbia.edu/tag/0FG0) in the Stacks Project.

**`Stacks.WeilCohomology.correspondenceToPointEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/BasePoint.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/BasePoint.lean#L137). The attribute's comment: “CH\_\{-r}(X) ⊗ Q = Corr^r(X, Spec k)”.

> **Stacks Project, Tag 0FG0 (2).** The canonical `ℚ`-linear isomorphism
>
>   `CH_{-r}(X) ⊗ ℚ = Corrʳ(X, Spec k)`,
>
> pushforward along the collapsing projection `X ×_{Spec k} Spec k ≅ X`. The target of the
> correspondence is the base, which contributes dimension `0`, so a correspondence of degree `r`
> from `X` to `Spec k` is a rational Chow class of dimension `-r`.

```lean
def correspondenceToPointEquiv (r : ℤ) :
    TensorProduct ℤ ℚ (chowGroup C sX (-r)) ≃ₗ[ℚ] Correspondence C sX (𝟙 C.S) 0 r
```

**`Stacks.WeilCohomology.correspondenceFromPointEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/BasePoint.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/BasePoint.lean#L163). The attribute's comment: “CH^r(X) ⊗ Q = Corr^r(Spec k, X)”.

> **Stacks Project, Tag 0FG0 (3).** The canonical `ℚ`-linear isomorphism
>
>   `CH^r(X) ⊗ ℚ = Corrʳ(Spec k, X)`,
>
> pushforward along the collapsing projection `Spec k ×_{Spec k} X ≅ X`. The source of the
> correspondence is the base, which contributes dimension `0`, so a correspondence of degree `r`
> from `Spec k` to a target of dimension `d` is a rational Chow class of dimension `d - r`, which
> is codimension `r`.

```lean
def correspondenceFromPointEquiv (d r : ℤ) :
    TensorProduct ℤ ℚ (chowGroup C sX (d - r)) ≃ₗ[ℚ] Correspondence C (𝟙 C.S) sX d r
```

**`Stacks.WeilCohomology.corrToPointEquiv_pullback_canonicalDiagonalClassFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/CanonicalDiagonal.lean, line 997](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/CanonicalDiagonal.lean#L997). The attribute's comment: “(2): CH\_\{-r}(X) ⊗ Q = Corr^r(X, Spec k), under which pullback by correspondences corresponds to composition”.

> **Stacks Project, Tag 0FG0 (2).** For schemes `X'`, `X` smooth and proper over `k`, of
> arbitrary, not necessarily constant, dimension, the canonical isomorphism
> `CH_{-r}(X) ⊗ ℚ = Corrʳ(X, Spec k)` of `Stacks.WeilCohomology.corrToPointEquiv` turns pullback by
> correspondences into composition: for `c ∈ Corrˢ(X', X)` and `β ∈ CH_{-r}(X) ⊗ ℚ`, the class
> `c^*(β) ∈ CH_{-(s+r)}(X') ⊗ ℚ` corresponds to `β ∘ c ∈ Corr^{s+r}(X', Spec k)`, the
> intersection products being formed with the Gysin classes of the diagonals of Stacks 0FBR.

```lean
theorem corrToPointEquiv_pullback_canonicalDiagonalClassFamily [IsProper sX'] [IsProper sX]
    (s r : ℤ) (c : Corr k sX' sX s)
    (β : TensorProduct ℤ ℚ (chowGroup (fieldChowSituation k) sX (-r))) :
    corrToPointEquiv k sX' (s + r)
        ((chowGroupDegreeEquiv _ sX' (show -r - s = -(s + r) by ring)).toIntLinearEquiv.baseChange
          ℤ ℚ _ _ (pullback k sX' sX (canonicalDiagonalClassFamily k) s (-r) c β)) =
      comp k sX' sX (𝟙 _) (canonicalDiagonalClassFamily k) s r c (corrToPointEquiv k sX r β)
```

**`Stacks.WeilCohomology.corrFromPointEquiv_pushforward_canonicalDiagonalClassFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/CanonicalDiagonal.lean, line 1018](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/CanonicalDiagonal.lean#L1018). The attribute's comment: “(3): CH^r(X) ⊗ Q = Corr^r(Spec k, X), under which pushforward by correspondences corresponds to composition”.

> **Stacks Project, Tag 0FG0 (3).** For schemes `X`, `Y` smooth over `k`, of arbitrary, not
> necessarily constant, dimension, with `X` proper, the canonical isomorphism
> `CH^r(X) ⊗ ℚ = Corrʳ(Spec k, X)` of `Stacks.WeilCohomology.corrFromPointEquiv` turns pushforward
> by correspondences into composition: for `c ∈ Corrˢ(X, Y)` and `α ∈ CH^i(X) ⊗ ℚ`, the class
> `c_*(α) ∈ CH^{i+s}(Y) ⊗ ℚ` corresponds to `c ∘ α ∈ Corr^{i+s}(Spec k, Y)`, the intersection
> products being formed with the Gysin classes of the diagonals of Stacks 0FBR.

```lean
theorem corrFromPointEquiv_pushforward_canonicalDiagonalClassFamily [IsProper sX] (i s : ℤ)
    (c : Corr k sX sY s) (α : CodimChow k sX i) :
    corrFromPointEquiv k sY (i + s) (pushforward k sX sY (canonicalDiagonalClassFamily k) s i c α) =
      comp k (𝟙 _) sX sY (canonicalDiagonalClassFamily k) i s (corrFromPointEquiv k sX i α) c
```

**`Stacks.WeilCohomology.comp_bilinear_assoc_canonicalDiagonalClassFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/CanonicalDiagonalFlat.lean, line 378](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/CanonicalDiagonalFlat.lean#L378). The attribute's comment: “(1): composition of correspondences is Q-bilinear and associative”.

> **Stacks Project, Tag 0FG0 (1).** For schemes `X`, `Y`, `Z`, `W` smooth over `k`, of arbitrary,
> not necessarily constant, dimension, with `Y` and `Z` proper, composition of correspondences
> `Corrʳ(X, Y) × Corrˢ(Y, Z) ⟶ Corr^{r+s}(X, Z)` is `ℚ`-bilinear and associative,
> `c'' ∘ (c' ∘ c) = (c'' ∘ c') ∘ c`, the two sides compared through `(r + s) + t = r + (s + t)`; the
> intersection products are formed with the Gysin classes of the diagonals of Stacks 0FBR.

```lean
theorem comp_bilinear_assoc_canonicalDiagonalClassFamily [IsProper sY] [IsProper sZ]
    (r s t : ℤ) :
    (∀ (a b : ℚ) (c₁ c₂ : Corr k sX sY r) (c' : Corr k sY sZ s),
      comp k sX sY sZ (canonicalDiagonalClassFamily k) r s (a • c₁ + b • c₂) c' =
        a • comp k sX sY sZ (canonicalDiagonalClassFamily k) r s c₁ c' +
          b • comp k sX sY sZ (canonicalDiagonalClassFamily k) r s c₂ c') ∧
    (∀ (a b : ℚ) (c : Corr k sX sY r) (c'₁ c'₂ : Corr k sY sZ s),
      comp k sX sY sZ (canonicalDiagonalClassFamily k) r s c (a • c'₁ + b • c'₂) =
        a • comp k sX sY sZ (canonicalDiagonalClassFamily k) r s c c'₁ +
          b • comp k sX sY sZ (canonicalDiagonalClassFamily k) r s c c'₂) ∧
    ∀ (c : Corr k sX sY r) (c' : Corr k sY sZ s) (c'' : Corr k sZ sW t),
      corrCongr k sX sW (add_assoc r s t)
          (comp k sX sZ sW (canonicalDiagonalClassFamily k) (r + s) t
            (comp k sX sY sZ (canonicalDiagonalClassFamily k) r s c c') c'') =
        comp k sX sY sW (canonicalDiagonalClassFamily k) r (s + t) c
          (comp k sY sZ sW (canonicalDiagonalClassFamily k) s t c' c'')
```

**`Stacks.WeilCohomology.comp_pullback_pushforward_canonicalDiagonalClassFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/CanonicalDiagonalFlat.lean, line 408](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/CanonicalDiagonalFlat.lean#L408). The attribute's comment: “(4): composition of correspondences is compatible with pushforward and pullback of cycles”.

> **Stacks Project, Tag 0FG0 (4).** For schemes `X`, `Y`, `Z` smooth and proper over `k`, of
> arbitrary, not necessarily constant, dimension, composition of correspondences is compatible with
> pullback and pushforward of cycles: for `c ∈ Corrʳ(X, Y)` and `c' ∈ Corrˢ(Y, Z)`,
>
>   `(c' ∘ c)^*(α) = c^*((c')^*(α))`  for `α ∈ CH_m(Z) ⊗ ℚ`, and
>   `(c' ∘ c)_*(α) = (c')_*(c_*(α))`  for `α ∈ CH^i(X) ⊗ ℚ`,
>
> the degrees `m - (r + s) = (m - s) - r` and `i + (r + s) = (i + r) + s` being identified, the
> intersection products being formed with the Gysin classes of the diagonals of Stacks 0FBR.

```lean
theorem comp_pullback_pushforward_canonicalDiagonalClassFamily [IsProper sX] [IsProper sY]
    [IsProper sZ] (r s : ℤ) (c : Corr k sX sY r) (c' : Corr k sY sZ s) :
    (∀ (m : ℤ) (α : TensorProduct ℤ ℚ (chowGroup (fieldChowSituation k) sZ m)),
      Stacks.WeilCohomology.pullback k sX sZ (canonicalDiagonalClassFamily k) (r + s) m
          (comp k sX sY sZ (canonicalDiagonalClassFamily k) r s c c') α =
        (chowGroupDegreeEquiv _ sX
            (show m - s - r = m - (r + s) by ring)).toIntLinearEquiv.baseChange
          ℤ ℚ _ _ (Stacks.WeilCohomology.pullback k sX sY (canonicalDiagonalClassFamily k) r (m - s)
            c (Stacks.WeilCohomology.pullback k sY sZ (canonicalDiagonalClassFamily k) s m c' α))) ∧
    ∀ (i : ℤ) (α : CodimChow k sX i),
      pushforward k sX sZ (canonicalDiagonalClassFamily k) (r + s) i
          (comp k sX sY sZ (canonicalDiagonalClassFamily k) r s c c') α =
        codimChowCongr k sZ (add_assoc i r s)
          (pushforward k sY sZ (canonicalDiagonalClassFamily k) s (i + r) c'
            (pushforward k sX sY (canonicalDiagonalClassFamily k) r i c α))
```

Declarations registered for the tag:

- [`Stacks.WeilCohomology.corrToPointEquiv`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/DimensionDecompositionBasePoint.lean#L807), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/CanonicalDiagonal.lean, line 1007](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/CanonicalDiagonal.lean#L1007) (StacksFrontier): “(2): CH\_\{-r}(X) ⊗ Q = Corr^r(X, Spec k), under which pullback by correspondences corresponds to composition”.
- [`Stacks.WeilCohomology.corrFromPointEquiv`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/DimensionDecompositionBasePoint.lean#L853), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/CanonicalDiagonal.lean, line 1026](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/CanonicalDiagonal.lean#L1026) (StacksFrontier): “(3): CH^r(X) ⊗ Q = Corr^r(Spec k, X), under which pushforward by correspondences corresponds to composition”.

## Tag 0FG1, an example

[Tag 0FG1](https://stacks.math.columbia.edu/tag/0FG1) in the Stacks Project.

**`Stacks.WeilCohomology.graph`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/Graph.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/Graph.lean#L71). The attribute's comment: “graph\_of\_morphism”.

> **Stacks Project, Tag 0FG1.** The graph `Γ_f ⊆ X ×_S Y` of a morphism `f : Y ⟶ X` over `S`:
> the scheme-theoretic image of `(f, 𝟙 Y) : Y ⟶ X ×_S Y`.

```lean
abbrev graph (pX : X ⟶ S) (pY : Y ⟶ S) (f : Y ⟶ X) (hf : f ≫ pX = pY) : Scheme.{u}
```

**`Stacks.WeilCohomology.isClosedImmersion_graphMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/Graph.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/Graph.lean#L80). The attribute's comment: “graph\_closed\_immersion”. References: EGA I (5.4.3); EGA I (10.15.4), “ordinary schemes”; EGA I (5.3.11), “separated case”; EGA I (5.4.2), “special case”.

> **Stacks Project, Tag 0FG1.** The graph morphism of an `S`-morphism `f : Y ⟶ X` is a closed
> immersion whenever `X` is separated over `S`.

```lean
theorem isClosedImmersion_graphMorphism (pX : X ⟶ S) (pY : Y ⟶ S) (f : Y ⟶ X)
    (hf : f ≫ pX = pY) [IsSeparated pX] :
    IsClosedImmersion (graphMorphism pX pY f hf)
```

**`Stacks.WeilCohomology.codimension_graphPartMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/GraphCodimension.lean, line 381](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/GraphCodimension.lean#L381). The attribute's comment: “graph\_pure\_codimension”.

> **Stacks 0FG1: the intersection `Γ_f ∩ (X_d × Y)` has pure codimension `d`.**
>
> Let `U ⊆ X` be an open and closed part of `X` which is equidimensional of dimension `d`, in the
> sense that every irreducible component of `U` has dimension `d`. Then every irreducible component
> of `Γ_f ∩ (U × Y)` has codimension `d` in `U × Y`; the components are indexed by the generic
> points of `f⁻¹U`, because the graph morphism is a closed immersion with source `f⁻¹U`.
>
> The proof is the dimension formula of Stacks 0A21 at the point: the local dimension of `U × Y`
> there is the dimension of the point closure plus the codimension. The point closure has the
> delta-dimension of the corresponding point of `Y`, since the graph is a closed immersion over
> `k`; and the local dimension is the delta-dimension of an irreducible component of `U × Y`
> through the point, which by Stacks 02R8 exceeds the delta-dimension of the component of `Y`
> beneath it by `d`, the relative dimension of the flat projection `U × Y ⟶ Y`. The component of
> `Y` beneath is the one through the point of `Y`, which is a generic point because `f⁻¹U` is open
> and closed in `Y`.

```lean
theorem codimension_graphPartMorphism (hU : IsClopen (U : Set X)) (d : ℕ)
    (hrel : AlgebraicGeometry.RelativeDimension (U.ι ≫ sX) d) (ξ : (f ⁻¹ᵁ U).toScheme)
    (hξ : closure ({ξ} : Set (f ⁻¹ᵁ U).toScheme) ∈ irreducibleComponents (f ⁻¹ᵁ U).toScheme) :
    codimension (closureSingleton ((graphPartMorphism sX sY f hf U).base ξ)) = (d : ℕ∞)
```

**`Stacks.WeilCohomology.cycleAssociatedToClosedSubscheme_graphMorphism_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/GraphCodimension.lean, line 465](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/GraphCodimension.lean#L465). The attribute's comment: “graph\_degree\_zero\_correspondence”.

> **Stacks 0FG1: `[Γ_f]` is a correspondence of degree zero.** If every generic point of `Y`
> has delta-dimension `e` — which is what it means for `Y` to be equidimensional of dimension `e` —
> then the cycle of the graph `Γ_f` on `X ×_k Y` vanishes in every delta-dimension other than `e`.
> Since `Corrʳ(X, Y)` is the degree-`(e - r)` Chow group of `X ×_k Y` with rational coefficients,
> this says that `[Γ_f]` lies in `Corr⁰(X, Y)` and in no other degree.

```lean
theorem cycleAssociatedToClosedSubscheme_graphMorphism_eq_zero (e : ℤ)
    (hY : ∀ y : Y, closure ({y} : Set Y) ∈ irreducibleComponents Y →
      relativeDimension (fieldChowSituation k).dimensionFunction sY y = e)
    (m : ℤ) (hm : m ≠ e) :
    cycleAssociatedToClosedSubscheme (fieldChowSituation k) (pullback.fst sX sY ≫ sX)
      (graphMorphism sX sY f hf) m = 0
```

**`Stacks.WeilCohomology.graphCorrespondence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/GraphCodimension.lean, line 483](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/GraphCodimension.lean#L483). The attribute's comment: “graph\_degree\_zero\_correspondence”. References: SGA 7 XX (4.4), “partial”.

> **Stacks 0FG1.** The graph of `f` as a correspondence of degree zero from `X` to a target
> equidimensional of dimension `e`: the class of the cycle `[Γ_f]` of the graph on `X ×_k Y`, with
> rational coefficients.

```lean
def graphCorrespondence (e : ℤ) : Correspondence (fieldChowSituation k) sX sY e 0
```

**`Stacks.WeilCohomology.exists_decomposition_graph_pure_codimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/GraphCodimension.lean, line 521](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/GraphCodimension.lean#L521). The attribute's comment: “graph\_pure\_codimension\_degree\_zero\_correspondence”.

> **Stacks Project, Tag 0FG1.** Let `f : Y ⟶ X` be a morphism of smooth projective schemes
> over a field `k` and let `Γ_f ⊆ X ×_k Y` be the graph of `f`, the image of the closed immersion
> `(f, id_Y) : Y ⟶ X ×_k Y`. Let `X = ∐_d X_d` be the decomposition of `X` into its open and closed
> parts which are equidimensional of dimension `d`, and likewise `Y = ∐_e Y_e`. Then:
>
> * `Γ_f ∩ (X_d × Y)` has pure codimension `d` in `X_d × Y`; and
> * consequently `[Γ_f]` lies in `Corr⁰(X, Y)`, i.e. it is a correspondence of degree `0` from `X`
>   to `Y`.
>
> The decomposition is the relative-dimension decomposition of Stacks 02NM: a smooth morphism is
> flat and locally of finite presentation with Cohen-Macaulay fibres, so its relative dimension is
> locally constant and the locus where it equals `d` is open and closed; over a field that locus is
> the part of `X` which is equidimensional of dimension `d`, which is the fourth clause below.
>
> `Γ_f ∩ (X_d × Y)` is the closed subscheme `Stacks.WeilCohomology.graphPartMorphism` of
> `X_d ×_k Y`, namely the graph of `f` restricted over `X_d`; its irreducible components are
> indexed by the generic points of the open and closed subscheme `f⁻¹(X_d)` of `Y`, which is the
> source of that closed immersion. The fifth clause says that each of them has codimension `d`.
>
> The last clause is the membership `[Γ_f] ∈ Corr⁰(X, Y)`. The group `Corrʳ(X, Y)` is
> `⊕_d CH^{d+r}(X_d × Y) ⊗ ℚ`; in the dimension grading used by this repository's Chow groups
> `CH^{d}(X_d × Y_e) = A_e(X_d × Y_e)`, so saying that `[Γ_f]` is a correspondence of degree `0` is
> saying that over the part `Y_e` of `Y` the cycle `[Γ_f]` is concentrated in delta-dimension `e`
> and vanishes in every other delta-dimension — which is the codimension-`d` purity of the previous
> clause read in the dimension grading.

```lean
theorem exists_decomposition_graph_pure_codimension (k : Type u) [Field k] {X Y : Scheme.{u}}
    (sX : X ⟶ Spec (.of k)) (sY : Y ⟶ Spec (.of k)) [Smooth sX] [Smooth sY]
    (hXproj : IsProjectiveMorphism sX) (f : Y ⟶ X) (hf : f ≫ sX = sY) :
    haveI : IsSeparated sX := isSeparated_of_isProjectiveMorphism sX hXproj
    ∃ U : ℕ → X.Opens, ∃ V : ℕ → Y.Opens,
      ((∀ d, IsClopen (U d : Set X)) ∧ (⨆ d, U d) = ⊤ ∧
        ∀ d d', d ≠ d' → Disjoint (U d) (U d')) ∧
      ((∀ e, IsClopen (V e : Set Y)) ∧ (⨆ e, V e) = ⊤ ∧
        ∀ e e', e ≠ e' → Disjoint (V e) (V e')) ∧
      (∀ d : ℕ, Nonempty (U d).toScheme →
        TopologicalSpace.Equidimensional (U d).toScheme ∧
          topologicalKrullDim (U d).toScheme = (d : WithBot ℕ∞)) ∧
      (∀ e : ℕ, Nonempty (V e).toScheme →
        TopologicalSpace.Equidimensional (V e).toScheme ∧
          topologicalKrullDim (V e).toScheme = (e : WithBot ℕ∞)) ∧
      (∀ d : ℕ, Set.range (graphPartMorphism sX sY f hf (U d) ≫
            partProductι sX sY (U d)).base =
          Set.range (graphMorphism sX sY f hf).base ∩
            Set.range (partProductι sX sY (U d)).base) ∧
      (∀ (d : ℕ) (ξ : (f ⁻¹ᵁ U d).toScheme),
        closure ({ξ} : Set (f ⁻¹ᵁ U d).toScheme) ∈ irreducibleComponents (f ⁻¹ᵁ U d).toScheme →
          codimension (closureSingleton ((graphPartMorphism sX sY f hf (U d)).base ξ)) =
            (d : ℕ∞)) ∧
      (∀ (e : ℕ) (m : ℤ), m ≠ (e : ℤ) →
        cycleAssociatedToClosedSubscheme (fieldChowSituation k)
          (pullback.fst sX ((V e).ι ≫ sY) ≫ sX)
          (graphMorphism sX ((V e).ι ≫ sY) ((V e).ι ≫ f)
            (by rw [Category.assoc, hf])) m = 0)
```

## Tag 0FG2, a lemma

[Tag 0FG2](https://stacks.math.columbia.edu/tag/0FG2) in the Stacks Project.

**`Stacks.WeilCohomology.canonicalCorrespondences_gradedCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/CanonicalGradedCategory.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/CanonicalGradedCategory.lean#L53).

> Correspondences between smooth projective schemes over `k` form a graded category over `ℚ`:
> the morphisms from `X` to `Y` are `⨁ᵣ Corrʳ(X, Y)`, the identity is the class of the diagonal, of
> degree zero, and the composite of correspondences of degrees `r` and `s`, formed with the
> canonical diagonal classes, has degree `r + s`.

```lean
instance canonicalCorrespondences_gradedCategory :
    GradedCategory ℚ (canonicalCorrespondenceCompositionData k).Obj
```

**`Stacks.WeilCohomology.GradedCompositionData.gradedCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/GradedStructure.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/GradedStructure.lean#L241). The attribute's comment: “correspondences form a graded category over Q”.

> Correspondences form a graded category over `ℚ` in the sense of Definition 09L2: the morphism
> module `⨁ᵣ Corrʳ(X, Y)` is the direct sum of its homogeneous pieces `Corrʳ(X, Y)`, the
> identity — the diagonal class — is homogeneous of degree zero, and composing correspondences of
> degrees `r` and `s` gives one of degree `r + s`.

```lean
instance gradedCategory : GradedCategory ℚ D.Obj
```

## Tag 0FG3, a lemma

[Tag 0FG3](https://stacks.math.columbia.edu/tag/0FG3) in the Stacks Project.

**`Stacks.WeilCohomology.canonicalGraphFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/CanonicalGradedCategory.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/CanonicalGradedCategory.lean#L61).

> The contravariant functor from smooth projective schemes over `k` to the category of
> correspondences which is the identity on objects and sends `f : X ⟶ Y` to the class
> `[Γ_f] ∈ Corr⁰(Y, X)` of its graph.

```lean
noncomputable def canonicalGraphFunctor :
    ((SmoothProjectiveScheme k).FullSubcategory)ᵒᵖ ⥤
      (canonicalCorrespondenceCompositionData k).Obj
```

**`Stacks.WeilCohomology.GradedCompositionData.PushforwardData.graphFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/GraphFunctor.lean, line 326](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/GraphFunctor.lean#L326). The attribute's comment: “the contravariant functor f ↦ [graph f] to correspondences, identity on objects”.

> **Stacks Project, Tag 0FG3.** The contravariant functor from the ambient category — in the
> source the smooth projective schemes over `k` — to the category of correspondences which is the
> identity on objects and sends `f : Y ⟶ X` to the class `[Γ_f] ∈ Corr⁰(X, Y)` of its graph.
>
> Keyed: the functor, its two laws and the identity on objects are all proved. The carried input
> is the composition of correspondences of `Stacks.WeilCohomology.GradedCompositionData`, as for
> Stacks 0FG2, together with proper pushforward of correspondences along `u ×ₛ 𝟙` and its
> compatibilities in `Stacks.WeilCohomology.GradedCompositionData.PushforwardData` — Stacks 02RW,
> 02S2, the three-projection formula of Stacks 0FG0 and the projection formula of Stacks 0FFC.
> No carried field refers to graphs. See the implementation notes of the file.

```lean
def graphFunctor : Cᵒᵖ ⥤ D.Obj
```

## Tag 0FG4, a remark

[Tag 0FG4](https://stacks.math.columbia.edu/tag/0FG4) in the Stacks Project.

**`Stacks.WeilCohomology.cycleTranspose`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/Transpose.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/Transpose.lean#L95). The attribute's comment: “transpose”.

> **Stacks Project, Tag 0FG4.** Transposition of cycles on a fibre product: proper pushforward
> along the factor switch `X ×_S Y ≅ Y ×_S X`.

```lean
def cycleTranspose (n : ℤ) :
    CycleGroup C (pullback.fst sX sY ≫ sX) n →+ CycleGroup C (pullback.fst sY sX ≫ sY) n
```

**`Stacks.WeilCohomology.chowTranspose`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/Transpose.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/Transpose.lean#L104). The attribute's comment: “transpose”.

> **Stacks Project, Tag 0FG4.** Transposition of Chow classes on a fibre product, induced by
> transposition of cycles. The factor switch is an isomorphism, so this needs no instance of
> Stacks 02S2.

```lean
def chowTranspose (n : ℤ) :
    chowGroup C (pullback.fst sX sY ≫ sX) n →+ chowGroup C (pullback.fst sY sX ≫ sY) n
```

**`Stacks.WeilCohomology.cycleTransposeEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/Transpose.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/Transpose.lean#L126). The attribute's comment: “the transpose is an isomorphism, on cycles”.

> **Stacks Project, Tag 0FG4.** Transposition of cycles on a fibre product is an isomorphism
> of groups of `n`-cycles, with inverse the transposition in the other direction.

```lean
def cycleTransposeEquiv (n : ℤ) :
    CycleGroup C (pullback.fst sX sY ≫ sX) n ≃+ CycleGroup C (pullback.fst sY sX ≫ sY) n
```

**`Stacks.WeilCohomology.chowTransposeEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/Transpose.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/Transpose.lean#L169). The attribute's comment: “the transpose is an isomorphism, on cycle classes”.

> **Stacks Project, Tag 0FG4.** Transposition of Chow classes on a fibre product is an
> isomorphism of Chow groups, with inverse the transposition in the other direction.

```lean
def chowTransposeEquiv (n : ℤ) :
    chowGroup C (pullback.fst sX sY ≫ sX) n ≃+ chowGroup C (pullback.fst sY sX ≫ sY) n
```

**`Stacks.WeilCohomology.transpose`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/Transpose.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/Transpose.lean#L199). The attribute's comment: “transpose”.

> **Stacks Project, Tag 0FG4.** The transpose `c ↦ cᵗ` of a rational correspondence. For `X`
> equidimensional of dimension `d` and `Y` equidimensional of dimension `e` it maps
> `Corrʳ(X, Y)` to `Corr^{d - e + r}(Y, X)`.

```lean
def transpose (d e r : ℤ) :
    Correspondence C sX sY e r →ₗ[ℤ] Correspondence C sY sX d (d - e + r)
```

**`Stacks.WeilCohomology.transposeEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/Transpose.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/Transpose.lean#L224). The attribute's comment: “the transpose is an isomorphism Corr^r(X, Y) = Corr^\{d - e + r}(Y, X)”.

> **Stacks Project, Tag 0FG4.** For `X` equidimensional of dimension `d` and `Y`
> equidimensional of dimension `e`, the factor switch `X ×_S Y ≅ Y ×_S X` determines an
> *isomorphism*
>
>   `Corrʳ(X, Y) ≃ Corr^{d - e + r}(Y, X)`, `c ↦ cᵗ`,
>
> the transpose, with inverse the transpose in the other direction.

```lean
def transposeEquiv (d e r : ℤ) :
    Correspondence C sX sY e r ≃ₗ[ℚ] Correspondence C sY sX d (d - e + r)
```

**`Stacks.WeilCohomology.cycleTranspose_graph`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/TransposeGraph.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/TransposeGraph.lean#L155). The attribute's comment: “transpose\_graph”.

> **Stacks Project, Tag 0FG4.** Transposing the cycle of the graph of `f : Y ⟶ X` gives the
> cycle of the transposed graph.

```lean
theorem cycleTranspose_graph (f : Y ⟶ X) (hf : f ≫ sX = sY) (k : ℤ) :
    cycleTranspose C sX sY k
        (cycleAssociatedToClosedSubscheme C (pullback.fst sX sY ≫ sX)
          (graphMorphism sX sY f hf).imageι k) =
      cycleAssociatedToClosedSubscheme C (pullback.fst sY sX ≫ sY)
        (graphMorphism sX sY f hf ≫ (pullbackSymmetry sX sY).hom).imageι k
```

**`Stacks.WeilCohomology.transpose_graph`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/TransposeGraph.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/TransposeGraph.lean#L171). The attribute's comment: “transpose\_graph”.

> **Stacks Project, Tag 0FG4.** The transpose of the rational correspondence of the graph of
> `f : Y ⟶ X` is the rational correspondence of the transposed graph: `[Γ_f]ᵗ = [Γ_fᵗ]`.

```lean
theorem transpose_graph (f : Y ⟶ X) (hf : f ≫ sX = sY) (d e r : ℤ) (q : ℚ) :
    transpose C sX sY d e r (q ⊗ₜ[ℤ] QuotientAddGroup.mk
        (cycleAssociatedToClosedSubscheme C (pullback.fst sX sY ≫ sX)
          (graphMorphism sX sY f hf).imageι (e - r))) =
      q ⊗ₜ[ℤ] chowGroupDegreeEquiv C (pullback.fst sY sX ≫ sY)
        (show e - r = d - (d - e + r) by omega)
        (QuotientAddGroup.mk (cycleAssociatedToClosedSubscheme C (pullback.fst sY sX ≫ sY)
          (graphMorphism sX sY f hf ≫ (pullbackSymmetry sX sY).hom).imageι (e - r)))
```

## Tag 0FG5, a lemma

[Tag 0FG5](https://stacks.math.columbia.edu/tag/0FG5) in the Stacks Project.

**`Stacks.WeilCohomology.pullback_graphCorrespondenceSP`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/GraphAction.lean, line 1075](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/GraphAction.lean#L1075). The attribute's comment: “(2): pullback of cycles by the correspondence [Γ\_f] agrees with the pushforward f\_* : CH\_*(Y) → CH\_*(X), in every dimension, with rational coefficients”.

> **Stacks Project, Tag 0FG5 (2).** Let `f : Y ⟶ X` be a morphism of smooth projective
> schemes over `k` and `[Γ_f] ∈ Corr⁰(X, Y)` its graph (Example 0FG1). Pullback of cycles by the
> correspondence `[Γ_f]`, `β ↦ pr₁,*([Γ_f] · pr₂^*β)`, agrees with proper pushforward
> `f_* : CH_m(Y) ⊗ ℚ ⟶ CH_m(X) ⊗ ℚ`, in every dimension `m`.

```lean
theorem pullback_graphCorrespondenceSP (m : ℤ) :
    haveI := isProper_of_comp_eq X.obj.hom Y.obj.hom (Over.w f.hom)
    pullback k X.obj.hom Y.obj.hom (canonicalDiagonalClassFamily k) 0 m
        (SmoothProjectiveCorr.toCorr X Y 0 (graphCorrespondenceSP f)) =
      ((chowGroupDegreeEquiv (fieldChowSituation k) X.obj.hom (sub_zero m).symm).toAddMonoidHom.comp
        (properChowPushforward (fieldChowSituation k) Y.obj.hom X.obj.hom f.hom.left
          (Over.w f.hom) m
          (properPushforwardDescends _ _ _ _ _ _))).toIntLinearMap.baseChange ℚ
```

**`Stacks.WeilCohomology.pullback_transposeGraphCorrespondenceSP`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/GraphAction.lean, line 1099](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/GraphAction.lean#L1099). The attribute's comment: “(3)(b): for X and Y equidimensional of dimensions d and e, pullback of cycles by the transposed graph [Γ\_f]ᵗ ∈ Corr^\{d-e}(Y, X) of Remark 0FG4 agrees with the Gysin map f^!, in every dimension, with rational coefficients”.

> **Stacks Project, Tag 0FG5 (3)(b).** Let `f : Y ⟶ X` be a morphism of smooth projective
> schemes over `k`, with `X` and `Y` equidimensional of dimensions `d` and `e`. Pullback of cycles
> by the transposed graph `[Γ_f]ᵗ ∈ Corr^{d-e}(Y, X)` of Remark 0FG4,
> `β ↦ pr₁,*([Γ_f]ᵗ · pr₂^*β)`, agrees with the Gysin map
> `f^! : CH_m(X) ⊗ ℚ ⟶ CH_{m-(d-e)}(Y) ⊗ ℚ` of Stacks 0FF3, in every dimension `m`.

```lean
theorem pullback_transposeGraphCorrespondenceSP {d e : ℕ} (hX : RelativeDimension X.obj.hom d)
    (hY : RelativeDimension Y.obj.hom e) (m : ℤ) :
    haveI := locallyOfFiniteType_of_comp_eq (Over.w f.hom)
    pullback k Y.obj.hom X.obj.hom (canonicalDiagonalClassFamily k) ((d : ℤ) - e) m
        (SmoothProjectiveCorr.toCorr Y X _ (transposeGraphCorrespondenceSP f d e)) =
      (smoothGysinChow (fieldChowSituation k) Y.obj.hom X.obj.hom (Over.w f.hom) ((d : ℤ) - e)
        m).toIntLinearMap.baseChange ℚ
```

**`Stacks.WeilCohomology.pushforward_transposeGraphCorrespondenceSP`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/GraphAction.lean, line 1152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/GraphAction.lean#L1152). The attribute's comment: “(3)(a): for X and Y equidimensional of dimensions d and e, pushforward of cycles by the transposed graph [Γ\_f]ᵗ ∈ Corr^\{d-e}(Y, X) of Remark 0FG4 corresponds to pushforward of cycles by f, on CH^i(Y) ⊗ Q for every i”.

> **Stacks Project, Tag 0FG5 (3)(a).** Let `f : Y ⟶ X` be a morphism of smooth projective
> schemes over `k`, with `X` and `Y` equidimensional of dimensions `d` and `e`. Pushforward of
> cycles by the transposed graph `[Γ_f]ᵗ ∈ Corr^{d-e}(Y, X)` of Remark 0FG4,
> `α ↦ pr₂,*([Γ_f]ᵗ · pr₁^*α)`, corresponds to pushforward of cycles by `f`,
> `f_* : CH^i(Y) = CH_{e-i}(Y) ⟶ CH_{e-i}(X) = CH^{i+d-e}(X)`, on `CH^i(Y) ⊗ ℚ`.

```lean
theorem pushforward_transposeGraphCorrespondenceSP {d e : ℕ}
    (hX : RelativeDimension X.obj.hom d) (hY : RelativeDimension Y.obj.hom e) (i : ℤ) :
    haveI : CompactSpace X.obj.left := QuasiCompact.compactSpace_of_compactSpace X.obj.hom
    haveI : CompactSpace Y.obj.left := QuasiCompact.compactSpace_of_compactSpace Y.obj.hom
    pushforward k Y.obj.hom X.obj.hom (canonicalDiagonalClassFamily k) ((d : ℤ) - e) i
        (SmoothProjectiveCorr.toCorr Y X _ (transposeGraphCorrespondenceSP f d e)) ∘ₗ
        rationalCodimensionToCodimChow k Y.obj.hom i =
      rationalCodimensionToCodimChow k X.obj.hom (i + ((d : ℤ) - e)) ∘ₗ
        (equidimensionalPushforward f e d i (i + ((d : ℤ) - e)) (by ring)).toIntLinearMap.baseChange
          ℚ
```

**`Stacks.WeilCohomology.pushforward_graphCorrespondenceSP`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/GraphAction.lean, line 1177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/GraphAction.lean#L1177). The attribute's comment: “(1): pushforward of cycles by the correspondence [Γ\_f] agrees with the Gysin map f^! : CH^*(X) → CH^*(Y), on CH^i(X) ⊗ Q for every i, X and Y not necessarily equidimensional”.

> **Stacks Project, Tag 0FG5 (1).** Let `f : Y ⟶ X` be a morphism of smooth projective
> schemes over `k` and `[Γ_f] ∈ Corr⁰(X, Y)` its graph (Example 0FG1). Pushforward of cycles by
> the correspondence `[Γ_f]`, `α ↦ pr₂,*([Γ_f] · pr₁^*α)`, agrees with the Gysin map
> `f^! : CH^i(X) ⟶ CH^i(Y)` of Stacks 0FF3, on `CH^i(X) ⊗ ℚ` for every `i`. The schemes need not be
> equidimensional: `CH^i(X) = ∏_d CH_{d-i}(X_d)` is graded by codimension on the parts `X_d` of
> constant dimension.

```lean
theorem pushforward_graphCorrespondenceSP (i : ℤ) :
    haveI : CompactSpace X.obj.left := QuasiCompact.compactSpace_of_compactSpace X.obj.hom
    haveI : CompactSpace Y.obj.left := QuasiCompact.compactSpace_of_compactSpace Y.obj.hom
    haveI := locallyOfFiniteType_of_comp_eq (Over.w f.hom)
    pushforward k X.obj.hom Y.obj.hom (canonicalDiagonalClassFamily k) 0 i
        (SmoothProjectiveCorr.toCorr X Y 0 (graphCorrespondenceSP f)) ∘ₗ
        rationalCodimensionToCodimChow k X.obj.hom i =
      (codimChowCongr k Y.obj.hom (add_zero i).symm).toLinearMap ∘ₗ
        rationalCodimensionToCodimChow k Y.obj.hom i ∘ₗ
          (codimensionGysin Y.obj.hom X.obj.hom (Over.w f.hom) i).toIntLinearMap.baseChange ℚ
```

## Tag 0FG6, an example

[Tag 0FG6](https://stacks.math.columbia.edu/tag/0FG6) in the Stacks Project.

**`Stacks.WeilCohomology.projectiveLineCorrEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectiveLineCorrespondenceAlgebra.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectiveLineCorrespondenceAlgebra.lean#L111). The attribute's comment: “Corr⁰(X, X) = CH¹(X × X) ⊗ ℚ = CH₁(X × X) ⊗ ℚ”.

> `Corr⁰(P¹_k, P¹_k) = CH¹(P¹ × P¹) ⊗ ℚ = CH₁(P¹ × P¹) ⊗ ℚ`: a correspondence of degree zero
> on the projective line is a rational cycle class of dimension one on `P¹_k ×_k P¹_k`.

```lean
def projectiveLineCorrEquiv :
    SmoothProjectiveCorr (projectiveLineObj k) (projectiveLineObj k) 0 ≃ₗ[ℚ]
      Correspondence (fieldChowSituation k) σ σ 1 0
```

**`Stacks.WeilCohomology.projectiveLineCorrBasis`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectiveLineCorrespondenceAlgebra.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectiveLineCorrespondenceAlgebra.lean#L120). The attribute's comment: “c₀ and c₂ are a basis of Corr⁰(X, X)”.

> A basis of `Corr⁰(P¹_k, P¹_k)` over `ℚ`, formed by `c₀ = [x × P¹]` and `c₂ = [P¹ × x]`.

```lean
def projectiveLineCorrBasis :
    Module.Basis (Fin 2) ℚ (SmoothProjectiveCorr (projectiveLineObj k) (projectiveLineObj k) 0)
```

**`Stacks.WeilCohomology.projectiveLinePointFibreCorr`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectiveLineCorrespondenceAlgebra.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectiveLineCorrespondenceAlgebra.lean#L163). The attribute's comment: “c₀ = [x × X]”.

> The correspondence `c₀ = [x × P¹] ∈ Corr⁰(P¹_k, P¹_k)` of a rational point `x`.

```lean
def projectiveLinePointFibreCorr :
    SmoothProjectiveCorr (projectiveLineObj k) (projectiveLineObj k) 0
```

**`Stacks.WeilCohomology.projectiveLineFibrePointCorr`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectiveLineCorrespondenceAlgebra.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectiveLineCorrespondenceAlgebra.lean#L169). The attribute's comment: “c₂ = [X × x]”.

> The correspondence `c₂ = [P¹ × x] ∈ Corr⁰(P¹_k, P¹_k)` of a rational point `x`.

```lean
def projectiveLineFibrePointCorr :
    SmoothProjectiveCorr (projectiveLineObj k) (projectiveLineObj k) 0
```

**`Stacks.WeilCohomology.projectiveLine_diagonal_eq_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectiveLineCorrespondenceAlgebra.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectiveLineCorrespondenceAlgebra.lean#L225). The attribute's comment: “1 = [Δ] = c₀ + c₂”.

> `1 = [Δ] = c₀ + c₂` in `Corr⁰(P¹_k, P¹_k)`.

```lean
theorem projectiveLine_diagonal_eq_add :
    (canonicalCorrespondenceCompositionData k).diagonal (projectiveLineObj k) =
      projectiveLinePointFibreCorr x hx + projectiveLineFibrePointCorr x hx
```

**`Stacks.WeilCohomology.projectiveLine_pointFibre_comp_pointFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectiveLineCorrespondenceAlgebra.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectiveLineCorrespondenceAlgebra.lean#L252). The attribute's comment: “c₀ ∘ c₀ = c₀”.

> `c₀ ∘ c₀ = c₀` in the category of correspondences.

```lean
theorem projectiveLine_pointFibre_comp_pointFibre :
    projectiveLinePointFibreHom x hx ≫ projectiveLinePointFibreHom x hx =
      projectiveLinePointFibreHom x hx
```

**`Stacks.WeilCohomology.projectiveLine_fibrePoint_comp_pointFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectiveLineCorrespondenceAlgebra.lean, line 278](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectiveLineCorrespondenceAlgebra.lean#L278). The attribute's comment: “c₀ ∘ c₂ = 0”.

> `c₀ ∘ c₂ = 0` in the category of correspondences.

```lean
theorem projectiveLine_fibrePoint_comp_pointFibre :
    projectiveLineFibrePointHom x hx ≫ projectiveLinePointFibreHom x hx = 0
```

**`Stacks.WeilCohomology.projectiveLine_pointFibre_comp_fibrePoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectiveLineCorrespondenceAlgebra.lean, line 285](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectiveLineCorrespondenceAlgebra.lean#L285). The attribute's comment: “c₂ ∘ c₀ = 0”.

> `c₂ ∘ c₀ = 0` in the category of correspondences.

```lean
theorem projectiveLine_pointFibre_comp_fibrePoint :
    projectiveLinePointFibreHom x hx ≫ projectiveLineFibrePointHom x hx = 0
```

**`Stacks.WeilCohomology.projectiveLine_fibrePoint_comp_fibrePoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectiveLineCorrespondenceAlgebra.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectiveLineCorrespondenceAlgebra.lean#L292). The attribute's comment: “c₂ ∘ c₂ = c₂”.

> `c₂ ∘ c₂ = c₂` in the category of correspondences.

```lean
theorem projectiveLine_fibrePoint_comp_fibrePoint :
    projectiveLineFibrePointHom x hx ≫ projectiveLineFibrePointHom x hx =
      projectiveLineFibrePointHom x hx
```

**`Stacks.WeilCohomology.projectiveLineCorrAlgEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectiveLineCorrespondenceAlgebra.lean, line 351](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectiveLineCorrespondenceAlgebra.lean#L351). The attribute's comment: “Corr⁰(X, X) = ℚ × ℚ as a ℚ-algebra”.

> `Corr⁰(P¹_k, P¹_k) = ℚ × ℚ` as a `ℚ`-algebra: the degree-zero endomorphisms of `P¹_k` in the
> category of correspondences, with composition as multiplication, are the product algebra, via
> `(a, b) ↦ a c₀ + b c₂`.

```lean
def projectiveLineCorrAlgEquiv : (ℚ × ℚ) ≃ₐ[ℚ] degreeZeroSubalgebra (R := ℚ) 𝐗
```

**`Stacks.WeilCohomology.mul_self_of_add_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/ProjectiveLineAlgebra.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/ProjectiveLineAlgebra.lean#L78). The attribute's comment: “c₂ ∘ c₂ = c₂”.

> The complement of an idempotent is idempotent: from `[Δ] = c₀ + c₂` and `c₀ ∘ c₀ = c₀`
> follows `c₂ ∘ c₂ = c₂`.

```lean
theorem mul_self_of_add_eq_one (hsum : c₀ + c₂ = 1) (h₀ : c₀ * c₀ = c₀) : c₂ * c₂ = c₂
```

**`Stacks.WeilCohomology.mul_eq_zero_of_add_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/ProjectiveLineAlgebra.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/ProjectiveLineAlgebra.lean#L85). The attribute's comment: “c₀ ∘ c₂ = 0”.

> An idempotent and its complement are orthogonal: from `[Δ] = c₀ + c₂` and `c₀ ∘ c₀ = c₀`
> follows `c₀ ∘ c₂ = 0`.

```lean
theorem mul_eq_zero_of_add_eq_one (hsum : c₀ + c₂ = 1) (h₀ : c₀ * c₀ = c₀) : c₀ * c₂ = 0
```

**`Stacks.WeilCohomology.mul_eq_zero_of_add_eq_one'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/ProjectiveLineAlgebra.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/ProjectiveLineAlgebra.lean#L92). The attribute's comment: “c₂ ∘ c₀ = 0”.

> An idempotent and its complement are orthogonal in the other order too: from
> `[Δ] = c₀ + c₂` and `c₀ ∘ c₀ = c₀` follows `c₂ ∘ c₀ = 0`.

```lean
theorem mul_eq_zero_of_add_eq_one' (hsum : c₀ + c₂ = 1) (h₀ : c₀ * c₀ = c₀) : c₂ * c₀ = 0
```

**`Stacks.WeilCohomology.algEquivProdOfBasisOfAddEqOne`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/ProjectiveLineAlgebra.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/ProjectiveLineAlgebra.lean#L111). The attribute's comment: “Corr⁰(X, X) = ℚ × ℚ as a ℚ-algebra”.

> An algebra with a two-element basis `c₀`, `c₂` whose sum is the identity and whose first
> member is idempotent is the product algebra `R × R`: the two basis elements are orthogonal
> idempotents, so multiplication is coordinatewise. For the projective line this is
> `Corr⁰(P¹, P¹) = ℚ × ℚ`, with `c₀ = [x × P¹]` and `c₂ = [P¹ × x]`.

```lean
def algEquivProdOfBasisOfAddEqOne (b : Module.Basis (Fin 2) R A) (hsum : b 0 + b 1 = 1)
    (h₀ : b 0 * b 0 = b 0) : (R × R) ≃ₐ[R] A
```

**`Stacks.WeilCohomology.pointFibreCorrespondence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/ProjectiveLineAlgebra.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/ProjectiveLineAlgebra.lean#L147). The attribute's comment: “c₀ = [x × X]”.

> The degree-zero correspondence `c₀ = [x × X]` attached to a section `x` of `sX`, for a source
> equidimensional of dimension `d`: the rational class of the fibre `x × X ⊆ X ×_S X`, which is the
> graph of the constant morphism of `X` through `x`.

```lean
def pointFibreCorrespondence (d : ℤ) : Correspondence C sX sX d 0
```

**`Stacks.WeilCohomology.fibrePointCorrespondence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/ProjectiveLineAlgebra.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/ProjectiveLineAlgebra.lean#L155). The attribute's comment: “c₂ = [X × x]”.

> The degree-zero correspondence `c₂ = [X × x]` attached to a section `x` of `sX`: the rational
> class of the fibre `X × x ⊆ X ×_S X`, the factor switch of `x × X`.

```lean
def fibrePointCorrespondence (d : ℤ) : Correspondence C sX sX d 0
```

**`Stacks.WeilCohomology.cycleTranspose_pointFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/ProjectiveLineAlgebra.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/ProjectiveLineAlgebra.lean#L164). The attribute's comment: “[X × x] is the transpose of [x × X]”.

> The fibre `X × x` is the transpose of the fibre `x × X`: transposing the cycle of the one gives
> the cycle of the other.

```lean
theorem cycleTranspose_pointFibre (k : ℤ) :
    cycleTranspose C sX sX k
        (cycleAssociatedToClosedSubscheme C (pullback.fst sX sX ≫ sX)
          (graphMorphism sX sX (sX ≫ x) (constantMorphism_comp_base sX x hx)).imageι k) =
      cycleAssociatedToClosedSubscheme C (pullback.fst sX sX ≫ sX)
        (graphMorphism sX sX (sX ≫ x) (constantMorphism_comp_base sX x hx) ≫
          (pullbackSymmetry sX sX).hom).imageι k
```

**`Stacks.WeilCohomology.correspondence_zero_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/ProjectiveLineAlgebra.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/ProjectiveLineAlgebra.lean#L177). The attribute's comment: “Corr⁰(X, X) = CH₁(X × X) ⊗ ℚ”.

> For a source equidimensional of dimension one, such as the projective line, the degree-zero
> correspondences are the rational dimension-one Chow classes of the square,
> `Corr⁰(X, X) = CH₁(X × X) ⊗ ℚ`.

```lean
theorem correspondence_zero_eq :
    Correspondence C sX sX 1 0 =
      TensorProduct ℤ ℚ (chowGroup C (pullback.fst sX sX ≫ sX) 1)
```

## Tag 0FG7, a lemma

[Tag 0FG7](https://stacks.math.columbia.edu/tag/0FG7) in the Stacks Project.

**`Stacks.WeilCohomology.CorrespondenceCategory.monoidalCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CorrespondenceMonoidal.lean, line 1045](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CorrespondenceMonoidal.lean#L1045).

> **Stacks Project, Tag 0FG7** (monoidal structure). The tensor product of correspondences
> `c ⊗ c' = pr₁₃^* c · pr₂₄^* c'` turns the category of correspondences between smooth projective
> schemes over `k` (Stacks 0FG2) into a monoidal category, with `X ⊗ Y = X × Y`, unit `Spec k`, and
> as associativity constraint the usual associativity constraint of products of schemes (taken
> through the graph functor of Stacks 0FG3).

```lean
instance monoidalCategory : MonoidalCategory (CorrespondenceCategory k)
```

**`Stacks.WeilCohomology.CorrespondenceCategory.symmetricCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CorrespondenceMonoidal.lean, line 1105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CorrespondenceMonoidal.lean#L1105).

> **Stacks Project, Tag 0FG7.** The tensor product of correspondences
> `c ⊗ c' = pr₁₃^* c · pr₂₄^* c'` turns the category of correspondences between smooth projective
> schemes over `k` (Stacks 0FG2) into a symmetric monoidal category with unit `Spec k`: the
> associativity constraint is the usual associativity constraint on products of schemes and the
> commutativity constraint is the isomorphism `X × Y ⟶ Y × X` switching the factors, both taken
> through the graph functor of Stacks 0FG3.

```lean
instance symmetricCategory : SymmetricCategory (CorrespondenceCategory k)
```

**`Stacks.WeilCohomology.CorrespondenceStructure.monoidalCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/MonoidalStructure.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/MonoidalStructure.lean#L243). The attribute's comment: “the category of correspondences is monoidal for the exterior product”.

> **Stacks Project, Tag 0FG7.** The exterior product of correspondences makes the category of
> correspondences monoidal. The pentagon and the triangle hold because every morphism they
> involve is a graph, so both sides are the graph of the corresponding composite in `C`.

```lean
instance monoidalCategory : MonoidalCategory S.Obj
```

**`Stacks.WeilCohomology.CorrespondenceStructure.symmetricCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/MonoidalStructure.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/MonoidalStructure.lean#L295). The attribute's comment: “the category of correspondences is symmetric monoidal with unit Spec(k)”.

> **Stacks Project, Tag 0FG7.** The exterior product of correspondences makes the category of
> correspondences symmetric monoidal with unit `Spec(k)`: the commutativity constraint is the
> graph of the factor switch, which is an involution.

```lean
instance symmetricCategory : SymmetricCategory S.Obj
```

## Tag 0FG8, a lemma

[Tag 0FG8](https://stacks.math.columbia.edu/tag/0FG8) in the Stacks Project.

**`Stacks.WeilCohomology.graph_tensor_diagonal_fundamental_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/GraphFundamentalPairing.lean, line 783](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/GraphFundamentalPairing.lean#L783).

> **Stacks Project, Tag 0FG8.** Let `f : Y ⟶ X` be a morphism of smooth projective schemes over
> `k`, with `X` and `Y` equidimensional of dimensions `d` and `e`. Let `a = [Γ_f] ∈ Corr⁰(X, Y)`,
> `aᵗ = [Γ_fᵗ] ∈ Corr^{d-e}(Y, X)`, `η_X = [Γ_{X → X × X}] ∈ Corr⁰(X × X, X)`,
> `η_Y = [Γ_{Y → Y × Y}] ∈ Corr⁰(Y × Y, Y)`, and let `[X] ∈ Corr^{-d}(X, Spec k)` and
> `[Y] ∈ Corr^{-e}(Y, Spec k)` be the fundamental classes. Then the diagram
>
>   `X ⊗ Y --(a ⊗ 1)--> Y ⊗ Y --η_Y--> Y --[Y]--> Spec k`,
>   `X ⊗ Y --(1 ⊗ aᵗ)--> X ⊗ X --η_X--> X --[X]--> Spec k`
>
> commutes in the category of correspondences. Here `⊗` on morphisms is the tensor product of
> correspondences `c ⊗ c' = pr₁₃^* c · pr₂₄^* c'`,
> `Stacks.WeilCohomology.CorrespondenceCategory.tensorHom`, which is the tensor product of morphisms
> of the symmetric monoidal structure of Stacks 0FG7 (`CorrespondenceCategory.tensorHom_eq` in
> `StacksFrontier.AlgebraicGeometry.WeilCohomology.Concrete.CorrespondenceMonoidal`).

```lean
theorem graph_tensor_diagonal_fundamental_comm (f : Y ⟶ X) :
    CorrespondenceCategory.tensorHom (graphHom f : (GradedCompositionData.Obj.mk X :
        CorrespondenceCategory k) ⟶ GradedCompositionData.Obj.mk Y)
        (𝟙 (GradedCompositionData.Obj.mk Y : CorrespondenceCategory k)) ≫
        diagonalGraphHom Y ≫ fundamentalClassHom hY =
      CorrespondenceCategory.tensorHom (𝟙 (GradedCompositionData.Obj.mk X :
          CorrespondenceCategory k)) (transposeGraphHom f d e) ≫
        diagonalGraphHom X ≫ fundamentalClassHom hX
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 45.3, Tag 0FFZ](https://stacks.math.columbia.edu/tag/0FFZ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
