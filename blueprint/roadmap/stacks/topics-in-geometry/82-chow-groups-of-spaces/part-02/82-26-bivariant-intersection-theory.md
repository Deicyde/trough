---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.BivariantClass, AlgebraicGeometry.Space.BivariantClassCanonical, AlgebraicGeometry.Space.chowCohomologyComponent, AlgebraicGeometry.Space.chowCohomology, AlgebraicGeometry.Space.ChowCohomologyClass, AlgebraicGeometry.Space.ChowCohomologyClass.instGRing, AlgebraicGeometry.Space.ChowCohomologyAlgebra, AlgebraicGeometry.Space.chowCohomologyComponentCanonical
statement: formalized
proof: formalized
---

# 82.26 Bivariant intersection theory

Section 82.26 of the Stacks Project, [Tag 0ERI](https://stacks.math.columbia.edu/tag/0ERI). 9 tags here are carried by 25 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0ERJ, a definition

[Tag 0ERJ](https://stacks.math.columbia.edu/tag/0ERJ) in the Stacks Project.

**`AlgebraicGeometry.Space.BivariantClass`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/Bivariant.lean, line 258](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/Bivariant.lean#L258). The attribute's comment: “over the parameterized Chow groups of 82.15 and Gysin maps of 82.22”.

> **Stacks 0ERJ.** A bivariant class of degree `p` for a morphism `f : X ⟶ Y` of good
> algebraic spaces over the base: a rule assigning to every good `Y' ⟶ Y` over the base and every
> `k` an additive map `CH_k(Y') ⟶ CH_{k-p}(Y' ×_Y X)`, natural for proper pushforward, for flat
> pullback of fixed relative dimension, and for the refined Gysin maps of Stacks 0ER1. The group
> of all of them is denoted `A^p(X ⟶ Y)`.
>
> Stated against an `AlgebraicGeometry.Space.ChowGroupSystem`, which supplies the Chow groups of
> Stacks 82.15 and the three operations on them that the axioms quantify over, none of which this
> repository constructs; see the implementation notes of
> `StacksFrontier.AlgebraicGeometry.Spaces.Chow.Bivariant`.

```lean
structure BivariantClass (D : BaseSpaceDimensionSituation.{u}) (G : ChowGroupSystem D)
    {X Y : D.Ambient} (sX : X ⟶ D.space) (hX : D.IsGood sX) (sY : Y ⟶ D.space)
    (hY : D.IsGood sY) (f : X ⟶ Y) (hf : f ≫ sY = sX) (p : ℤ)
```

**`AlgebraicGeometry.Space.BivariantClassCanonical`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/BivariantCanonical.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/BivariantCanonical.lean#L213). The attribute's comment: “the group A^p(X → Y) of bivariant classes of degree p, over the constructed Chow groups of Stacks 0EQ6 and the constructed proper pushforward, flat pullback and refined Gysin maps of Stacks 0EP1, 0EP8 and 0ER1; the three naturality axioms are stated through cycle representatives, equivalently to the source's equations, because the descent of those three operations to Chow groups is Stacks 0EQC, 0EQB and 0ERA and is not proved here”.

> A bivariant class of degree `p` for a morphism `f : X ⟶ Y` of good algebraic spaces over the
> base: a rule assigning to every good `g : Y' ⟶ Y` over the base and every `k` an additive map
> `CH_k(Y') ⟶ CH_{k-p}(Y' ×_Y X)`, natural for proper pushforward, for flat pullback of fixed
> relative dimension, and for the refined Gysin maps of Stacks 0ER1. The group of all of them is
> denoted `A^p(X ⟶ Y)`.
>
> The Chow groups are `AlgebraicGeometry.Space.chowGroupCanonical` of Stacks 0EQ6, and the three
> operations are the operations on cycles of Stacks 0EP1, Stacks 0EP8 and Stacks 0ER1; each axiom
> asserts the source's equation through cycle representatives.

```lean
structure BivariantClassCanonical {X Y : D.Ambient} (sX : X ⟶ D.space) (hX : D.IsGood sX)
    (sY : Y ⟶ D.space) (hY : D.IsGood sY) (f : X ⟶ Y) (hf : f ≫ sY = sX) (p : ℤ)
```

## Tag 0ERK, a definition

[Tag 0ERK](https://stacks.math.columbia.edu/tag/0ERK) in the Stacks Project.

**`AlgebraicGeometry.Space.chowCohomologyComponent`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChowCohomology.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChowCohomology.lean#L89). The attribute's comment: “the degree p part”.

> **Stacks 0ERK.** The degree `p` part `A^p(X)` of the Chow cohomology of a good algebraic
> space `X/B`: the group `A^p(X ⟶ X)` of bivariant classes of degree `p` for the identity morphism
> of `X`.

```lean
abbrev chowCohomologyComponent (D : BaseSpaceDimensionSituation.{u}) (G : ChowGroupSystem D)
    {X : D.Ambient} (sX : X ⟶ D.space) (hX : D.IsGood sX) (p : ℤ) : Type (u + 1)
```

**`AlgebraicGeometry.Space.chowCohomology`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChowCohomology.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChowCohomology.lean#L97). The attribute's comment: “the graded group, not the ℤ-algebra: composition is absent”.

> **Stacks 0ERK.** The Chow cohomology `A^*(X)` of a good algebraic space `X/B`: the graded
> group whose degree `p` part is the group `A^p(X ⟶ X)` of bivariant classes of degree `p` for the
> identity morphism of `X`.

```lean
abbrev chowCohomology (D : BaseSpaceDimensionSituation.{u}) (G : ChowGroupSystem D)
    {X : D.Ambient} (sX : X ⟶ D.space) (hX : D.IsGood sX) : Type (u + 1)
```

**`AlgebraicGeometry.Space.ChowCohomologyClass`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChowCohomologyAlgebra.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChowCohomologyAlgebra.lean#L166). The attribute's comment: “the degree p component A^p(X) = A^p(X → X): bivariant classes of degree p for id_X over the constructed Chow groups of Stacks 0EQ6, with the fibre product Y' ×_X X taken to be Y'; flat pullback and Gysin maps are the descended ones of Stacks 0EQB and 0ERA, the proper axiom is stated through cycle representatives”.

> The group `A^p(X) = A^p(X ⟶ X)` of bivariant classes of degree `p` (Stacks 0ERJ) for the
> identity of a good algebraic space `X/B`: a rule assigning to every good test space `g : Y' ⟶ X`
> over the base and every `k` an additive map `c ∩ - : CH_k(Y') ⟶ CH_{k-p}(Y')` (the fibre product
> `Y' ×_X X` being `Y'`), such that
>
> 1. for `h : Y'' ⟶ Y'` proper, `c ∩ h_*α'' = h_*(c ∩ α'')` for all `α''` on `Y''`;
> 2. for `h : Y'' ⟶ Y'` flat of relative dimension `r`, `c ∩ h^*α' = h^*(c ∩ α')` for all `α'`;
> 3. for `(ℒ', s', i' : D' → Y')` as in Definition 0ER1, `c ∩ (i')^*α' = (i')^*(c ∩ α')` for all
>    `α'` on `Y'`.
>
> The Chow groups are the constructed `AlgebraicGeometry.Space.chowGroupCanonical` of Stacks 0EQ6;
> `h^*` is the flat pullback of Stacks 0EQB, `(i')^*` the Gysin map of Stacks 0ERA, and `h_*` the
> proper pushforward of cycles of Stacks 0EP1, axiom (1) being read through cycle representatives.
> The cap operation in degree `k` is indexed by its target degree `l`, with `l + p = k`. See the
> implementation notes of `StacksFrontier.AlgebraicGeometry.Spaces.Chow.ChowCohomologyAlgebra`.

```lean
structure ChowCohomologyClass (hX : D.IsGood sX) (p : ℤ)
```

**`AlgebraicGeometry.Space.ChowCohomologyClass.instGRing`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChowCohomologyAlgebra.lean, line 524](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChowCohomologyAlgebra.lean#L524). The attribute's comment: “the graded Z-algebra structure on A^*(X): the product of the degree p and q components is the composition A^p(X → X) × A^q(X → X) → A^{p+q}(X → X) of bivariant classes, associative and bilinear, with unit 1 ∈ A^0(X)”.

> The graded ring structure on `p ↦ A^p(X) = A^p(X ⟶ X)`: the product of the degree `p` and `q`
> components is the composition `A^p(X ⟶ X) × A^q(X ⟶ X) ⟶ A^{p+q}(X ⟶ X)` of bivariant classes,
> associative and bilinear, with unit `1 ∈ A^0(X)`; the integers act through the multiples of `1`.

```lean
instance instGRing : DirectSum.GRing (ChowCohomologyClass D sX hX)
```

**`AlgebraicGeometry.Space.ChowCohomologyAlgebra`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChowCohomologyAlgebra.lean, line 553](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChowCohomologyAlgebra.lean#L553). The attribute's comment: “the Chow cohomology A^*(X): the graded Z-algebra ⊕_p A^p(X → X), with multiplication the composition of bivariant classes”.

> The Chow cohomology `A^*(X)` of a good algebraic space `X/B`: the graded `ℤ`-algebra
> `⊕_p A^p(X)` whose degree `p` component is the group `A^p(X ⟶ X)` of bivariant classes of degree
> `p` for `id_X` over the constructed Chow groups of Stacks 0EQ6, with multiplication the composition
> of bivariant classes (`DirectSum.ring` of `AlgebraicGeometry.Space.ChowCohomologyClass.instGRing`)
> and its `ℤ`-algebra structure the one of any ring.

```lean
abbrev ChowCohomologyAlgebra : Type _
```

**`AlgebraicGeometry.Space.chowCohomologyComponentCanonical`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChowCohomologyCanonical.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChowCohomologyCanonical.lean#L82). The attribute's comment: “the degree p part A^p(X) = A^p(X → X), over the constructed Chow groups of Stacks 0EQ6”.

> The degree `p` part `A^p(X)` of the Chow cohomology of a good algebraic space `X/B`: the
> group `A^p(X ⟶ X)` of bivariant classes of degree `p` for the identity morphism of `X`, over the
> constructed Chow groups of Stacks 0EQ6.

```lean
abbrev chowCohomologyComponentCanonical (D : BaseSpaceDimensionSituation.{u}) {X : D.Ambient}
    (sX : X ⟶ D.space) (hX : D.IsGood sX) (p : ℤ)
```

**`AlgebraicGeometry.Space.chowCohomologyCanonical`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChowCohomologyCanonical.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChowCohomologyCanonical.lean#L95). The attribute's comment: “the graded group A^*(X) = ⊕_p A^p(X → X) over the constructed Chow groups of Stacks 0EQ6, not the ℤ-algebra: the product is composition of bivariant classes, which needs proper pushforward along an isomorphism to respect rational equivalence (Stacks 0EQC)”.

> The Chow cohomology `A^*(X)` of a good algebraic space `X/B`: the graded group whose degree
> `p` part is the group `A^p(X ⟶ X)` of bivariant classes of degree `p` for the identity morphism
> of `X`, over the constructed Chow groups of Stacks 0EQ6.
>
> This is the graded group and not the graded `ℤ`-algebra, whose product is composition of
> bivariant classes.

```lean
abbrev chowCohomologyCanonical (D : BaseSpaceDimensionSituation.{u}) {X : D.Ambient}
    (sX : X ⟶ D.space) (hX : D.IsGood sX)
```

## Tag 0ERL, a remark

[Tag 0ERL](https://stacks.math.columbia.edu/tag/0ERL) in the Stacks Project.

**`AlgebraicGeometry.Space.chowCohomologyRestrictionCap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChowCohomology.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChowCohomology.lean#L134). The attribute's comment: “the cap operations of the pullback f^*c”.

> **Stacks 0ERL.** The cap operations of the pullback `f^*c` of a Chow cohomology class
> `c ∈ A^p(Y)` along a morphism `f : X ⟶ Y` of good algebraic spaces over the base: on a good
> test space `g : X' ⟶ X` it is the cap operation of `c` on `X'` viewed over `Y`, carried to
> `X ×_X X'` along the comparison isomorphism.

```lean
def chowCohomologyRestrictionCap (c : chowCohomologyComponent D G sY hY p)
    (hg : D.IsGood (g ≫ sX)) (hpbY : D.IsGood (pullback.fst (𝟙 Y) (g ≫ f) ≫ sY))
    (hpbX : D.IsGood (pullback.fst (𝟙 X) g ≫ sX))
    (hκ : IsProper D.site D.base D.base_mem (restrictionComparisonIso D f g).hom) (k : ℤ) :
    G.chow (g ≫ sX) hg k →+ G.chow (pullback.fst (𝟙 X) g ≫ sX) hpbX (k - p)
```

**`AlgebraicGeometry.Space.chowCohomologyRestrictionCapHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChowCohomology.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChowCohomology.lean#L171). The attribute's comment: “the pullback of cap operations is additive in the class”.

> **Stacks 0ERL.** The pullback along `f : X ⟶ Y` of the cap operation of a Chow cohomology
> class on a fixed good test space over `X`, as an additive map in the class.

```lean
def chowCohomologyRestrictionCapHom (hg : D.IsGood (g ≫ sX))
    (hpbY : D.IsGood (pullback.fst (𝟙 Y) (g ≫ f) ≫ sY))
    (hpbX : D.IsGood (pullback.fst (𝟙 X) g ≫ sX))
    (hκ : IsProper D.site D.base D.base_mem (restrictionComparisonIso D f g).hom) (k : ℤ) :
    chowCohomologyComponent D G sY hY p →+
      (G.chow (g ≫ sX) hg k →+ G.chow (pullback.fst (𝟙 X) g ≫ sX) hpbX (k - p))
```

**`AlgebraicGeometry.Space.ChowCohomologyAlgebra.comap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChowCohomologyAlgebraPullback.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChowCohomologyAlgebraPullback.lean#L205).

> **Stacks 0ERL.** The canonical `ℤ`-algebra map `f^* : A^*(Y) ⟶ A^*(X)` attached to a
> morphism `f : X ⟶ Y` of good algebraic spaces over the base. On the degree `p` component it is
> the pullback `AlgebraicGeometry.Space.ChowCohomologyClass.comap`: given `c ∈ A^p(Y)` and a test
> space `X' ⟶ X`, the class `f^*c` caps on `CH_k(X') ⟶ CH_{k-p}(X')` as `c` does, `X'` being
> thought of as an algebraic space over `Y` through `X' ⟶ X ⟶ Y`.

```lean
def comap (f : X ⟶ Y) (hf : f ≫ sY = sX) :
    ChowCohomologyAlgebra D sY hY →ₐ[ℤ] ChowCohomologyAlgebra D sX hX
```

## Tag 0ERM, a lemma

[Tag 0ERM](https://stacks.math.columbia.edu/tag/0ERM) in the Stacks Project.

**`AlgebraicGeometry.Space.firstChernBivariantClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FirstChernBivariantClass.lean, line 685](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FirstChernBivariantClass.lean#L685). The attribute's comment: “the rule f : X' → X ↦ c_1(f^*L) ∩ - : CH_k(X') → CH_{k-1}(X'), for X/B good and L an invertible O_X-module, is a bivariant class of degree 1”.

> In Situation 0EDT let `X/B` be good and let `ℒ` be an invertible `𝒪_X`-module. Then the
> rule that to `f : X' ⟶ X` assigns `c₁(f^*ℒ) ∩ - : CH_k(X') ⟶ CH_{k-1}(X')` is a bivariant class
> of degree `1`, in the sense of Stacks 0ERJ (`AlgebraicGeometry.Space.BivariantClassCanonical` for
> `𝟙 X`, over the constructed Chow groups `AlgebraicGeometry.Space.chowGroupCanonical` of
> Stacks 0EQ6). The cap operation is `AlgebraicGeometry.Space.firstChernBivariantCap`.

```lean
def firstChernBivariantClass :
    BivariantClassCanonical.{u + 1} D sX hX sX hX (𝟙 X) (Category.id_comp sX) 1
```

## Tag 0ERN, a lemma

[Tag 0ERN](https://stacks.math.columbia.edu/tag/0ERN) in the Stacks Project.

**`AlgebraicGeometry.Space.flatPullbackBivariantClassCanonical`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullbackBivariantClass.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullbackBivariantClass.lean#L290). The attribute's comment: “the rule g : Y' → Y ↦ (f')^* : CH_k(Y') → CH_{k+r}(X'), X' = X ×_Y Y', for f flat of relative dimension r between good spaces over B, is a bivariant class of degree -r”.

> In Situation 0EDT let `f : X ⟶ Y` be a morphism of good algebraic spaces over `B` which is
> flat of relative dimension `r`. Then the rule that to `g : Y' ⟶ Y` assigns the flat pullback
> `(f')^* : CH_k(Y') ⟶ CH_{k+r}(X')` of Stacks 0EQB along the base change
> `f' : X' = X ×_Y Y' ⟶ Y'` is a bivariant class of degree `-r`, in the sense of Stacks 0ERJ
> (`AlgebraicGeometry.Space.BivariantClassCanonical`, over the constructed Chow groups
> `AlgebraicGeometry.Space.chowGroupCanonical` of Stacks 0EQ6).

```lean
def flatPullbackBivariantClassCanonical :
    BivariantClassCanonical.{u + 1} D sX hX sY hY f hf (-(r : ℤ))
```

## Tag 0ERP, a lemma

[Tag 0ERP](https://stacks.math.columbia.edu/tag/0ERP) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_bivariantClassCanonical_gysin`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/GysinBivariantClass/BivariantClass.lean, line 680](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/GysinBivariantClass/BivariantClass.lean#L680). The attribute's comment: “the rule g : X' → X ↦ (i')^* : CH_k(X') → CH_{k-1}(E'), E' = E ×_X X', for X/B good and (L, s, i : E → X) a triple as in 0ER1, is a bivariant class of degree 1 for i; the cap operation is pinned to the Gysin map of the pulled-back triple carried along Z(g^*s) ≅ E ×_X X'”.

> **Stacks 0ERP.**  In Situation 0EDT let `X/B` be good and `(ℒ, σ, i : E → X)` a triple as in
> Stacks 0ER1: `ℒ` an invertible `𝒪_X`-module, `σ` a global section and `E = Z(σ)` its vanishing
> locus.  Then the rule that to `g : X' ⟶ X` assigns the Gysin map
> `(i')^* : CH_k(X') ⟶ CH_{k-1}(E')`, `E' = E ×_X X'`, is a bivariant class of degree `1` for
> `i : E ⟶ X` (`AlgebraicGeometry.Space.BivariantClassCanonical`, Stacks 0ERJ).
>
> The cap operation of the class is pinned down on the class of every `k`-cycle `α` on every test
> space: it is the class of the Gysin cycle of Stacks 0ER1 of the pulled-back triple
> `(g^*ℒ, g^*σ, Z(g^*σ) → X')` (Stacks 0ER3) at its own rule, carried to `E ×_X X'` along the
> identification `e : Z(g^*σ) ≅ E ×_X X'` over `X'` (`chowGroupCanonicalPushforwardOfIso`).  The
> three axioms of Stacks 0ERJ are Stacks 0ER5, Stacks 0ER6 and Stacks 0ERC for the pulled-back
> triples, as in the source's proof.

```lean
theorem exists_bivariantClassCanonical_gysin :
    ∃ c : BivariantClassCanonical.{u + 1} D (𝔼.1.ι ≫ p) (isGood_vanishingLocus D p hp L σ) p hp
        𝔼.1.ι rfl 1,
      ∀ {X' : D.Ambient} (g : X' ⟶ X) (hX' : D.IsGood (g ≫ p))
        (hE' : D.IsGood (Limits.pullback.fst 𝔼.1.ι g ≫ 𝔼.1.ι ≫ p))
        (e : (vanishingLocus D (g ≫ p) hX'
            (pullbackSheaf D p hp (g ≫ p) hX' (ObjectProperty.homMk g) L)
            (pullbackGlobalSection D p hp (g ≫ p) hX' (ObjectProperty.homMk g) L σ)).1.toFunctor ≅
          Limits.pullback 𝔼.1.ι g)
        (_he : e.hom ≫ Limits.pullback.snd 𝔼.1.ι g =
          (vanishingLocus D (g ≫ p) hX'
            (pullbackSheaf D p hp (g ≫ p) hX' (ObjectProperty.homMk g) L)
            (pullbackGlobalSection D p hp (g ≫ p) hX' (ObjectProperty.homMk g) L σ)).1.ι)
        (hcomp : e.hom ≫ Limits.pullback.fst 𝔼.1.ι g ≫ 𝔼.1.ι ≫ p =
          (vanishingLocus D (g ≫ p) hX'
            (pullbackSheaf D p hp (g ≫ p) hX' (ObjectProperty.homMk g) L)
            (pullbackGlobalSection D p hp (g ≫ p) hX' (ObjectProperty.homMk g) L σ)).1.ι ≫
            g ≫ p)
        (k : ℤ) (α : CycleGroup D (g ≫ p) k),
        c.cap g hX' hE' k (chowClassCanonical.{u + 1} D (g ≫ p) hX' k α) =
          chowGroupCanonicalPushforwardOfIso.{u + 1} D _
            (isGood_vanishingLocus D (g ≫ p) hX' _ _) _ hE' e hcomp (k - 1)
            (chowClassCanonical.{u + 1} D _ (isGood_vanishingLocus D (g ≫ p) hX' _ _) (k - 1)
              (gysinCycleMap D (g ≫ p) (vanishingLocus D (g ≫ p) hX'
                  (pullbackSheaf D p hp (g ≫ p) hX' (ObjectProperty.homMk g) L)
                  (pullbackGlobalSection D p hp (g ≫ p) hX' (ObjectProperty.homMk g) L σ))
                (isGood_vanishingLocus D (g ≫ p) hX' _ _) (k - 1)
                (sectionGysinRule D (g ≫ p) hX' _
                  (pullbackGlobalSection D p hp (g ≫ p) hX' (ObjectProperty.homMk g) L σ)
                  (k - 1)
                  (isInvertibleSheaf_pullbackSheaf D p hp (g ≫ p) hX' (ObjectProperty.homMk g)
                    L hL))
                (cycleGroupDegreeCongr D (g ≫ p) (sub_add_cancel k 1).symm α)))
```

## Tag 0ERQ, a lemma

[Tag 0ERQ](https://stacks.math.columbia.edu/tag/0ERQ) in the Stacks Project.

**`AlgebraicGeometry.Space.isProper_bivariantPushforwardBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/BivariantProperPushforward.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/BivariantProperPushforward.lean#L205). The attribute's comment: “properness of the base change of the proper morphism, so that the rule is defined”.

> **Stacks 0ERQ.** The base change of a proper morphism along a test space is proper, so the
> rule of Stacks 0ERQ has a proper morphism to push forward along.

```lean
theorem isProper_bivariantPushforwardBaseChange (D : BaseSpaceDimensionSituation.{u})
    {X Y Z Z' : D.Ambient} (f : X ⟶ Y) (g : Y ⟶ Z) (q : Z' ⟶ Z)
    (hX : IsAlgebraicSpace D.site D.base D.base_mem X)
    (hY : IsAlgebraicSpace D.site D.base D.base_mem Y)
    (hPX : IsAlgebraicSpace D.site D.base D.base_mem (pullback (f ≫ g) q))
    (hPY : IsAlgebraicSpace D.site D.base D.base_mem (pullback g q))
    (hf : IsProper D.site D.base D.base_mem f) :
    IsProper D.site D.base D.base_mem (bivariantPushforwardBaseChange D f g q)
```

**`AlgebraicGeometry.Space.bivariantProperPushforwardCap_proper_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/BivariantProperPushforward.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/BivariantProperPushforward.lean#L337). The attribute's comment: “the proper-pushforward condition of Stacks 0ERJ for the rule, over functoriality of the parameterized proper pushforward”.

> **Stacks 0ERQ.** The proper-pushforward condition of Stacks 0ERJ for the rule of 0ERQ:
> the cap operation `α ↦ f'_*(c ∩ α)` commutes with proper pushforward along a morphism of good
> test spaces over `Z`. This is the part of the source proof carried by Stacks 0EP2, which enters
> as functoriality of the parameterized proper pushforward.

```lean
theorem bivariantProperPushforwardCap_proper_naturality
    (hfun : G.HasFunctorialProperPushforward) {Z' Z'' : D.Ambient} (q : Z' ⟶ Z)
    (hZ' : D.IsGood (q ≫ sZ)) (hY' : D.IsGood (pullback.fst g q ≫ sY)) (h : Z'' ⟶ Z')
    (hZ'' : D.IsGood ((h ≫ q) ≫ sZ)) (hY'' : D.IsGood (pullback.fst g (h ≫ q) ≫ sY))
    (hh : IsProper D.site D.base D.base_mem h) (h' : pullback g (h ≫ q) ⟶ pullback g q)
    (hsq : IsPullback (pullback.snd g (h ≫ q)) h' h (pullback.snd g q))
    (hfst : h' ≫ pullback.fst g q = pullback.fst g (h ≫ q))
    (hh' : IsProper D.site D.base D.base_mem h') (k : ℤ)
    (α : G.chow ((h ≫ q) ≫ sZ) hZ'' k) :
    bivariantProperPushforwardCap D G sX hX sY hY sZ hZ f g hf hfg hproper hgood p c q hZ'
        hY' k
        (G.properPushforward ((h ≫ q) ≫ sZ) hZ'' (q ≫ sZ) hZ' h (Category.assoc h q sZ).symm
          hh k α) =
      G.properPushforward (pullback.fst g (h ≫ q) ≫ sY) hY'' (pullback.fst g q ≫ sY) hY' h'
        (by rw [← Category.assoc, hfst]) hh' (k - p)
        (bivariantProperPushforwardCap D G sX hX sY hY sZ hZ f g hf hfg hproper hgood p c
          (h ≫ q) hZ'' hY'' k α)
```

**`AlgebraicGeometry.Space.eq_of_isBivariantProperPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/BivariantProperPushforward.lean, line 401](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/BivariantProperPushforward.lean#L401). The attribute's comment: “uniqueness of the class defined by the rule”.

> **Stacks 0ERQ.** The rule of Stacks 0ERQ determines the pushed-forward class: two bivariant
> classes of degree `p` for `g` that both push `c` forward along `f` are equal.

```lean
theorem eq_of_isBivariantProperPushforward (hg : g ≫ sZ = sY)
    {d d' : BivariantClass D G sY hY sZ hZ g hg p}
    (hd : IsBivariantProperPushforward D G sX hX sY hY sZ hZ f g hf hfg hproper hgood p c hg d)
    (hd' : IsBivariantProperPushforward D G sX hX sY hY sZ hZ f g hf hfg hproper hgood p c hg
      d') :
    d = d'
```

**`AlgebraicGeometry.Space.BivariantClassCanonical.properPushforward`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/BivariantProperPushforwardCanonical.lean, line 742](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/BivariantProperPushforwardCanonical.lean#L742). The attribute's comment: “the rule α ↦ f'_*(c ∩ α) is a bivariant class of degree p for g: the class f_* ∘ c ∈ A^p(Y → Z) over the constructed Chow groups and operations, with its three axioms proved from those of c, Stacks 0EP2, 0EPD and 0ER5”.

> **Stacks 0ERQ.** In Situation 0EDT let `f : X ⟶ Y` and `g : Y ⟶ Z` be morphisms of good
> algebraic spaces over the base, with `f` proper, and let `c ∈ A^p(X ⟶ Z)`.  The rule which to a
> test space `Z' ⟶ Z` assigns `α ↦ f'_*(c ∩ α)`, for `f' : Z' ×_Z X ⟶ Z' ×_Z Y` the base change of
> `f`, is a bivariant class of degree `p` for `g`; this is that class `f_* ∘ c ∈ A^p(Y ⟶ Z)`, and
> `AlgebraicGeometry.Space.BivariantClassCanonical.properPushforward_cap_apply` says that it caps by
> the rule.

```lean
def BivariantClassCanonical.properPushforward :
    BivariantClassCanonical.{max (u + 1) v} D sY hY sZ hZ g hg p
```

**`AlgebraicGeometry.Space.BivariantClassCanonical.properPushforward_cap_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/BivariantProperPushforwardCanonical.lean, line 754](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/BivariantProperPushforwardCanonical.lean#L754). The attribute's comment: “the class caps by the rule α ↦ f'_*(c ∩ α)”.

> **Stacks 0ERQ.** The class `f_* ∘ c` caps by the rule of the source: on a test space
> `z : Z' ⟶ Z`, `(f_* ∘ c) ∩ α = f'_*(c ∩ α)` in `CH_{k-p}(Z' ×_Z Y)`.

```lean
theorem BivariantClassCanonical.properPushforward_cap_apply {Z' : D.Ambient} (z : Z' ⟶ Z)
    (hZ' : D.IsGood (z ≫ sZ)) (hY' : D.IsGood (pullback.fst g z ≫ sY)) (k : ℤ)
    (α : chowGroupCanonical.{max (u + 1) v} D (z ≫ sZ) hZ' k) :
    (BivariantClassCanonical.properPushforward D hY hf hg hfP c).cap z hZ' hY' k α =
      chowGroupCanonicalProperPushforward.{max (u + 1) v} D (pullback.fst (f ≫ g) z ≫ sX)
        (isGood_pullback_fst D hX hZ (f ≫ g) z hZ') (pullback.fst g z ≫ sY) hY'
        (bivariantPushforwardBaseChange_comp_structure D hf g z)
        (isProper_bivariantPushforwardBaseChange D f g z hX.1 hY.1
          (isGood_pullback_fst D hX hZ (f ≫ g) z hZ').1 hY'.1 hfP) (k - p)
        (c.cap z hZ' (isGood_pullback_fst D hX hZ (f ≫ g) z hZ') k α)
```

## Tag 0ERR, a lemma

[Tag 0ERR](https://stacks.math.columbia.edu/tag/0ERR) in the Stacks Project.

**`AlgebraicGeometry.Space.firstChernBivariantClass_compCap_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FirstChernBivariantCentral.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FirstChernBivariantCentral.lean#L70). The attribute's comment: “c_1(L) ∈ A^1(X) commutes with every c ∈ A^p(X): the composites c_1(L) ∘ c and c ∘ c_1(L) have the same cap operation on every test space”.

> **Stacks 0ERR.** In Situation 0EDT let `X/B` be good and let `ℒ` be an invertible
> `𝒪_X`-module.  Then `c₁(ℒ) ∈ A^1(X)` (Stacks 0ERM,
> `AlgebraicGeometry.Space.firstChernBivariantClass`) commutes with every `c ∈ A^p(X)`: on every
> good test space `g : Y' ⟶ X` the composites `c₁(ℒ) ∘ c` and `c ∘ c₁(ℒ)` have the same cap
> operation, `c₁(ℒ) ∩ (c ∩ α) = c ∩ (c₁(ℒ) ∩ α)` for every `α ∈ CH_k(Y')`, the two degrees
> `k - p - 1` and `k - 1 - p` being identified.

```lean
theorem firstChernBivariantClass_compCap_comm {p : ℤ}
    (c : BivariantClassCanonical.{u + 1} D sX hX sX hX (𝟙 X) (Category.id_comp sX) p)
    {Y' : D.Ambient} (g : Y' ⟶ X) (hY' : D.IsGood (g ≫ sX)) (k : ℤ)
    (x : chowGroupCanonical.{u + 1} D (g ≫ sX) hY' k) :
    BivariantClassCanonical.compCap D (firstChernBivariantClass D sX hX L hL) c g hY' k x =
      chowGroupCanonicalDegreeCongr D _ _ (by omega)
        (BivariantClassCanonical.compCap D c (firstChernBivariantClass D sX hX L hL) g hY' k
          x)
```

## Tag 0ERS, a lemma

[Tag 0ERS](https://stacks.math.columbia.edu/tag/0ERS) in the Stacks Project.

**`AlgebraicGeometry.Space.zero_capsFundamentalClassesToZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/BivariantVanishing.lean, line 402](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/BivariantVanishing.lean#L402). The attribute's comment: “the forward implication”.

> **Stacks 0ERS, the forward implication.** The zero class of `A^p(X)` caps the fundamental
> class of every integral algebraic space locally of finite type over `X` to zero.

```lean
theorem zero_capsFundamentalClassesToZero :
    BivariantClass.CapsFundamentalClassesToZero D G sX hX p 0
```

**`AlgebraicGeometry.Space.cap_integralClosedSubspaceCycle_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/BivariantVanishing.lean, line 412](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/BivariantVanishing.lean#L412). The attribute's comment: “the converse on the cycle of an integral closed subspace”.

> **Stacks 0ERS, the content of the converse.** If `c ∈ A^p(X)` caps the fundamental class of
> every integral algebraic space locally of finite type over `X` to zero, then it caps the cycle
> of every integral closed subspace of every good test space over `X` to zero: push forward along
> the inclusion of the subspace, where the hypothesis applies.

```lean
theorem cap_integralClosedSubspaceCycle_eq_zero
    (hpp : G.IsInducedByClosedCyclePushforward) (hbc : D.HasGoodSubspaceBaseChanges sX)
    (c : chowCohomologyComponent D G sX hX p)
    (hc : BivariantClass.CapsFundamentalClassesToZero D G sX hX p c)
    {X' : D.Ambient} (g : X' ⟶ X) (hg : D.IsGood (g ≫ sX))
    (hpb : D.IsGood (pullback.fst (𝟙 X) g ≫ sX))
    (Z : IntegralClosedSubspace D.site D.base D.base_mem X') (k : ℤ)
    (hk : deltaDimension D (g ≫ sX) Z = k) :
    c.cap g hg hpb k
      (G.cycleClass (g ≫ sX) hg k (integralClosedSubspaceCycle D (g ≫ sX) Z k)) = 0
```

**`AlgebraicGeometry.Space.eq_zero_iff_capsFundamentalClassesToZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/BivariantVanishing.lean, line 458](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/BivariantVanishing.lean#L458). The attribute's comment: “for Chow classes of cycles of finite support, over a cycle-induced pushforward”.

> **Stacks 0ERS.** A class `c ∈ A^p(X)` is zero if and only if `c ∩ [Y] = 0` in `CH_*(Y)` for
> every integral algebraic space `Y` locally of finite type over `X`.

```lean
theorem eq_zero_iff_capsFundamentalClassesToZero
    (hpp : G.IsInducedByClosedCyclePushforward) (hbc : D.HasGoodSubspaceBaseChanges sX)
    (hfin : ∀ {X' : D.Ambient} (g : X' ⟶ X) (hg : D.IsGood (g ≫ sX)) (k : ℤ)
      (α : G.chow (g ≫ sX) hg k), ∃ β : CycleGroup D (g ≫ sX) k,
        (Function.support β.1).Finite ∧ G.cycleClass (g ≫ sX) hg k β = α)
    (c : chowCohomologyComponent D G sX hX p) :
    c = 0 ↔ BivariantClass.CapsFundamentalClassesToZero D G sX hX p c
```

**`AlgebraicGeometry.Space.ChowCohomologyClass.eq_zero_iff_capsFundamentalClassesToZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChowCohomologyVanishing.lean, line 505](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChowCohomologyVanishing.lean#L505).

> **Stacks 0ERS.** In Situation 0EDT let `X/B` be good and let `c ∈ A^p(X)`. Then `c` is zero if
> and only if `c ∩ [Y] = 0` in `CH_*(Y)` for every integral algebraic space `Y` locally of finite
> type over `X`.

```lean
theorem ChowCohomologyClass.eq_zero_iff_capsFundamentalClassesToZero
    (c : ChowCohomologyClass D sX hX p) : c = 0 ↔ c.CapsFundamentalClassesToZero D sX hX
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 82.26, Tag 0ERI](https://stacks.math.columbia.edu/tag/0ERI)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
