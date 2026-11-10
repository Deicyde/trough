---
declaration: section
origin: cited
lean: Stacks.Chow.chowCohomologyGRingOfInvertible, Stacks.Chow.chowCohomologyRingOfInvertible, Stacks.Chow.chowCohomologyAlgebraOfInvertible, Stacks.Chow.ChowCohomologyGroup, Stacks.Chow.ChowCohomologyGroup.instGRing, Stacks.Chow.ChowCohomology, Stacks.Chow.chowCohomologyComponent, Stacks.Chow.chowCohomology
statement: formalized
proof: formalized
---

# 42.34 Chow cohomology and the first Chern class

Section 42.34 of the Stacks Project, [Tag 0FDV](https://stacks.math.columbia.edu/tag/0FDV). 8 tags here are carried by 72 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0B7E, a definition

[Tag 0B7E](https://stacks.math.columbia.edu/tag/0B7E) in the Stacks Project.

**`Stacks.Chow.chowCohomologyGRingOfInvertible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyCompositionRing.lean, line 761](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyCompositionRing.lean#L761). The attribute's comment: “the graded Z-algebra structure on A^*(X): composition of bivariant classes as the multiplication, with associativity, the unit 1 in A^0(X) and the two distributive laws, for the Gysin system of the genuine first Chern class rule and with no hypothesis on that system”.

> The Chow cohomology of `X` as a graded ring, for the Gysin system
> `Stacks.Chow.gysinSystemOfInvertible`: the degree `p` component is `A^p(X ⟶ X)`, the multiplication
> is `Stacks.Chow.chowCohomologyGradedMul` (composition of bivariant classes), the unit is
> `Stacks.Chow.chowCohomologyGradedOne` (the identity class `1 ∈ A^0(X)`), and `ℤ` maps to the
> multiples of `1`.

```lean
def chowCohomologyGRingOfInvertible :
    DirectSum.GRing fun p : ℤ ↦ chowCohomologyComponent C (gysinSystemOfInvertible C) sX p
```

**`Stacks.Chow.chowCohomologyRingOfInvertible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyCompositionRing.lean, line 788](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyCompositionRing.lean#L788). The attribute's comment: “the ring structure on the graded group A^*(X), with no hypothesis on the Gysin system”.

> The Chow cohomology `A^*(X)` as a ring, for the Gysin system
> `Stacks.Chow.gysinSystemOfInvertible`.

```lean
def chowCohomologyRingOfInvertible :
    Ring (chowCohomology C (gysinSystemOfInvertible C) sX)
```

**`Stacks.Chow.chowCohomologyAlgebraOfInvertible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyCompositionRing.lean, line 798](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyCompositionRing.lean#L798). The attribute's comment: “the graded Z-algebra A^*(X), the Chow cohomology of X, with no hypothesis on the Gysin system”.

> The *Chow cohomology* of `X`: the graded `ℤ`-algebra `A^*(X)` whose degree `p` component is
> `A^p(X ⟶ X)`, for the Gysin system `Stacks.Chow.gysinSystemOfInvertible`.

```lean
def chowCohomologyAlgebraOfInvertible :
    @Algebra ℤ (chowCohomology C (gysinSystemOfInvertible C) sX) _
      (chowCohomologyRingOfInvertible C sX).toSemiring
```

**`Stacks.Chow.ChowCohomologyGroup`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyRing.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyRing.lean#L72). The attribute's comment: “the degree p component A^p(X) = A^p(X → X) of the Chow cohomology: the bivariant classes of degree p of Stacks 0B76 for id\_X”.

> The group `A^p(X) = A^p(X ⟶ X)` of bivariant classes of degree `p` (Stacks 0B76) for the
> identity morphism of `X`.

```lean
abbrev ChowCohomologyGroup (p : ℤ) : Type (u + 1)
```

**`Stacks.Chow.ChowCohomologyGroup.instGRing`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyRing.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyRing.lean#L225). The attribute's comment: “the graded Z-algebra structure on A^*(X): the product of the degree p and q components is the composition A^p(X → X) × A^q(X → X) → A^\{p+q}(X → X) of Stacks 0B75, associative and bilinear, with unit 1 ∈ A^0(X)”.

> The family `p ↦ A^p(X)` is a graded ring: the product `A^p(X) × A^q(X) ⟶ A^{p+q}(X)` is the
> composition of bivariant classes of Stacks 0B75, which is associative and bilinear, with unit the
> class `1 ∈ A^0(X)`.

```lean
instance instGRing : DirectSum.GRing (ChowCohomologyGroup C sX)
```

**`Stacks.Chow.ChowCohomology`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyRing.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyRing.lean#L279). The attribute's comment: “the Chow cohomology A^*(X): the graded Z-algebra ⊕\_p A^p(X → X), with multiplication the composition of bivariant classes”.

> The *Chow cohomology* `A^*(X)` of `X`: the graded `ℤ`-algebra `⊕_{p ∈ ℤ} A^p(X)` whose degree
> `p` component is `A^p(X ⟶ X)`, with the multiplication of
> `Stacks.Chow.ChowCohomologyGroup.instGRing`, composition of bivariant classes.

```lean
abbrev ChowCohomology : Type (u + 1)
```

**`Stacks.Chow.chowCohomologyComponent`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/ChowCohomology.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/ChowCohomology.lean#L73). The attribute's comment: “the degree p part”.

> **Stacks 0B7E.** The degree `p` part `A^p(X)` of the Chow cohomology of a scheme `X` locally
> of finite type over the base: the group `A^p(X ⟶ X)` of bivariant classes of degree `p` for the
> identity morphism of `X`.

```lean
abbrev chowCohomologyComponent (C : ChowSituation.{u}) (G : GysinSystem C) {X : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (p : ℤ) : Type (u + 1)
```

**`Stacks.Chow.chowCohomology`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/ChowCohomology.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/ChowCohomology.lean#L81). The attribute's comment: “the graded group”.

> **Stacks 0B7E.** The Chow cohomology `A^*(X)` of a scheme `X` locally of finite type over the
> base: the graded group whose degree `p` part is the group `A^p(X ⟶ X)` of bivariant classes of
> degree `p` for the identity morphism of `X`.

```lean
abbrev chowCohomology (C : ChowSituation.{u}) (G : GysinSystem C) {X : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] : Type (u + 1)
```

## Tag 0B7F, a remark

[Tag 0B7F](https://stacks.math.columbia.edu/tag/0B7F) in the Stacks Project.

**`Stacks.Chow.chowCohomologyRestriction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomology.lean, line 484](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomology.lean#L484). The attribute's comment: “the canonical map”.

> **Stacks 0B7F.** The restriction map `res : A^p(Y) ⟶ A^p(Y')` along a morphism `f : Y' ⟶ Y`
> of schemes locally of finite type over the base, a homomorphism of groups: the special case
> `X = Y`, `f = 𝟙 Y` of the restriction map of Stacks 0F9Z, followed by the transport of a
> bivariant class along the canonical isomorphism `Y ×_Y Y' ≅ Y'`. It is often written `f^*`.
>
> The tag asserts more, namely that the induced map `A^*(Y) ⟶ A^*(Y')` of the graded groups is a
> map of `ℤ`-algebras. The multiplication is composition of bivariant classes, and the graded ring
> it makes of `A^*(Y)` is `Stacks.Chow.chowCohomologyGRing` of
> `StacksFrontier.AlgebraicGeometry.Chow.Bivariant.ChowCohomologyCompositionRing`, hypothesis-free for
> the Gysin system this repository constructs as `Stacks.Chow.chowCohomologyGRingOfInvertible`. Only
> the additive map is given here; that it respects that multiplication is
> `Stacks.Chow.chowCohomologyRestriction_chowCohomologyRingMul` of
> `StacksFrontier.AlgebraicGeometry.Chow.Bivariant.ChowCohomologyMultiplicative`, which assembles the
> `ℤ`-algebra map of the tag as
> `Stacks.Chow.chowCohomologyTotalRestrictionAlgHomOfInvertible`.

```lean
def chowCohomologyRestriction (hgys : G.IsNaturalUnderBaseChangeIso) :
    chowCohomologyComponent C G sY p →+ chowCohomologyComponent C G (f ≫ sY) p
```

**`Stacks.Chow.chowCohomologyRestriction_cap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomology.lean, line 497](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomology.lean#L497). The attribute's comment: “the cap formula for the canonical map”.

> **Stacks 0B7F.** The restriction map on Chow cohomology satisfies the cap formula of Stacks
> 0F9Z: `res(c) ∩ α = c ∩ α` for every `α ∈ CH_k(T)` and every test scheme `g : T ⟶ Y'`, both
> sides read in `CH_{k-p}(T)` through the canonical identifications `Y' ×_{Y'} T ≅ T` and
> `Y ×_Y T ≅ T`.

```lean
theorem chowCohomologyRestriction_cap (hgys : G.IsNaturalUnderBaseChangeIso)
    (c : chowCohomologyComponent C G sY p) {T : Scheme.{u}} (g : T ⟶ Y') [LocallyOfFiniteType g]
    (k : ℤ)
    (α : chowGroup C (g ≫ (f ≫ sY)) k) :
    chowPushforwardOfIso C (pullback.fst (𝟙 Y') g ≫ (f ≫ sY)) (g ≫ (f ≫ sY))
        (identityBaseChangeIso g).hom (identityBaseChangeIso_hom_comp_base C (f ≫ sY) g) (k - p)
        ((chowCohomologyRestriction C G sY f p hgys c).cap g k α) =
      chowPushforwardOfIso C (pullback.fst (𝟙 Y) (g ≫ f) ≫ sY) (g ≫ (f ≫ sY))
        (identityBaseChangeIso (g ≫ f)).hom
        (by rw [← Category.assoc]; exact identityBaseChangeIso_hom_comp_base C sY (g ≫ f))
        (k - p) (c.cap (g ≫ f) k (chowGroupCongr C (Category.assoc g f sY).symm k α))
```

**`Stacks.Chow.chowCohomologyTotalRestriction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomology.lean, line 539](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomology.lean#L539). The attribute's comment: “the canonical map of graded groups”.

> **Stacks 0B7F.** The restriction map `res : A^*(Y) ⟶ A^*(Y')` of the graded Chow cohomology
> groups along `f : Y' ⟶ Y`, a homomorphism of graded groups: the degreewise restriction map.
>
> The tag asserts that this is a map of `ℤ`-algebras. The multiplication on `A^*` is composition of
> bivariant classes and the graded ring it produces is `Stacks.Chow.chowCohomologyGRing` of
> `StacksFrontier.AlgebraicGeometry.Chow.Bivariant.ChowCohomologyCompositionRing`. Only additivity is
> proved here; that this map respects that multiplication is
> `Stacks.Chow.chowCohomologyTotalRestriction_mul` of
> `StacksFrontier.AlgebraicGeometry.Chow.Bivariant.ChowCohomologyMultiplicative`, and the `ℤ`-algebra
> map of the tag is `Stacks.Chow.chowCohomologyTotalRestrictionAlgHomOfInvertible` there.

```lean
def chowCohomologyTotalRestriction (hgys : G.IsNaturalUnderBaseChangeIso) :
    chowCohomology C G sY →+ chowCohomology C G (f ≫ sY)
```

**`Stacks.Chow.chowCohomologyRestrictionOfInvertible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/ChowCohomologyRestriction.lean, line 493](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/ChowCohomologyRestriction.lean#L493). The attribute's comment: “the canonical map, at the Gysin system of the first Chern class rule, with nothing assumed beyond the tag's own hypotheses”.

> **Stacks 0B7F.** The restriction map `res : A^p(Y) ⟶ A^p(Y')` along a morphism `f : Y' ⟶ Y`
> of schemes locally of finite type over the base, a homomorphism of groups, at the Gysin system of
> the first Chern class rule of an invertible module. It is often written `f^*`.
>
> This is `Stacks.Chow.chowCohomologyRestriction` with its case of Stacks 02TA discharged, by
> `Stacks.Chow.gysinSystemOfInvertible_isNaturalUnderBaseChangeIso`. Nothing is assumed: the Gysin
> system itself carries no hypothesis either, so the only hypotheses are those of the tag.

```lean
def chowCohomologyRestrictionOfInvertible :
    chowCohomologyComponent C (gysinSystemOfInvertible C) sY p →+
      chowCohomologyComponent C (gysinSystemOfInvertible C) (f ≫ sY) p
```

**`Stacks.Chow.chowCohomologyRestrictionOfInvertible_cap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/ChowCohomologyRestriction.lean, line 505](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/ChowCohomologyRestriction.lean#L505). The attribute's comment: “the cap formula for the canonical map, at the Gysin system of the first Chern class rule, with nothing assumed beyond the tag's own hypotheses”.

> **Stacks 0B7F.** The restriction map on Chow cohomology satisfies the cap formula of Stacks
> 0F9Z: `res(c) ∩ α = c ∩ α` for every `α ∈ CH_k(T)` and every test scheme `g : T ⟶ Y'`, both
> sides read in `CH_{k-p}(T)` through the canonical identifications `Y' ×_{Y'} T ≅ T` and
> `Y ×_Y T ≅ T`. Nothing is assumed.

```lean
theorem chowCohomologyRestrictionOfInvertible_cap
    (c : chowCohomologyComponent C (gysinSystemOfInvertible C) sY p) {T : Scheme.{u}}
    (g : T ⟶ Y') [LocallyOfFiniteType g] (k : ℤ)
    (α : chowGroup C (g ≫ (f ≫ sY)) k) :
    chowPushforwardOfIso C (pullback.fst (𝟙 Y') g ≫ (f ≫ sY)) (g ≫ (f ≫ sY))
        (identityBaseChangeIso g).hom (identityBaseChangeIso_hom_comp_base C (f ≫ sY) g) (k - p)
        ((chowCohomologyRestrictionOfInvertible C sY f p c).cap g k α) =
      chowPushforwardOfIso C (pullback.fst (𝟙 Y) (g ≫ f) ≫ sY) (g ≫ (f ≫ sY))
        (identityBaseChangeIso (g ≫ f)).hom
        (by rw [← Category.assoc]; exact identityBaseChangeIso_hom_comp_base C sY (g ≫ f))
        (k - p) (c.cap (g ≫ f) k (chowGroupCongr C (Category.assoc g f sY).symm k α))
```

**`Stacks.Chow.chowCohomologyTotalRestrictionOfInvertible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/ChowCohomologyRestriction.lean, line 528](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/ChowCohomologyRestriction.lean#L528). The attribute's comment: “the canonical map of graded groups, at the Gysin system of the first Chern class rule, with nothing assumed beyond the tag's own hypotheses”.

> **Stacks 0B7F.** The restriction map `res : A^*(Y) ⟶ A^*(Y')` of the graded Chow cohomology
> groups along `f : Y' ⟶ Y`, a homomorphism of graded groups, at the Gysin system of the first
> Chern class rule: the degreewise restriction map. Nothing is assumed.
>
> That this graded map is a map of `ℤ`-algebras is the `AddMonoidHom` structure here and in each
> degree, together with `Stacks.Chow.chowCohomologyRestrictionOfInvertible_mul` and
> `Stacks.Chow.chowCohomologyRestrictionOfInvertible_bivariantIdentityClass`.

```lean
def chowCohomologyTotalRestrictionOfInvertible :
    chowCohomology C (gysinSystemOfInvertible C) sY →+
      chowCohomology C (gysinSystemOfInvertible C) (f ≫ sY)
```

**`Stacks.Chow.chowCohomologyRestrictionOfInvertible_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/ChowCohomologyRestriction.lean, line 558](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/ChowCohomologyRestriction.lean#L558). The attribute's comment: “the canonical map is multiplicative: res(a ⬝ b) = res(a) ⬝ res(b), the multiplication on Chow cohomology being composition of bivariant classes -- at the Gysin system of the first Chern class rule, with nothing assumed beyond the tag's own hypotheses”.

> **Stacks 0B7F.** The restriction map `res : A^*(Y) ⟶ A^*(Y')` along `f : Y' ⟶ Y` is
> multiplicative: `res(a ⬝ b) = res(a) ⬝ res(b)` for `a ∈ A^p(Y)` and `b ∈ A^q(Y)`, the
> multiplication being composition of bivariant classes, Stacks 0B75. Nothing is assumed.
>
> This is `Stacks.Chow.chowCohomologyRestriction_mul` with both of its cases of Stacks 02TA
> discharged, by `Stacks.Chow.gysinSystemOfInvertible_isNaturalUnderBaseChangeIso` and
> `Stacks.Chow.gysinSystemOfInvertible_isNaturalUnderPullbackCompPushforward`.

```lean
theorem chowCohomologyRestrictionOfInvertible_mul
    (a : chowCohomologyComponent C (gysinSystemOfInvertible C) sY p)
    (b : chowCohomologyComponent C (gysinSystemOfInvertible C) sY q) :
    chowCohomologyRestrictionOfInvertible C sY f (p + q)
        (chowCohomologyMulOfInvertible C sY p q a b) =
      chowCohomologyMulOfInvertible C (f ≫ sY) p q
        (chowCohomologyRestrictionOfInvertible C sY f p a)
        (chowCohomologyRestrictionOfInvertible C sY f q b)
```

**`Stacks.Chow.chowCohomologyRestrictionOfInvertible_bivariantIdentityClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/ChowCohomologyRestriction.lean, line 583](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/ChowCohomologyRestriction.lean#L583). The attribute's comment: “the canonical map is unital: it carries the identity class 1 of A^0(Y) to the identity class of A^0(Y') -- at the Gysin system of the first Chern class rule, with nothing assumed beyond the tag's own hypotheses”.

> **Stacks 0B7F.** The restriction map `res : A^*(Y) ⟶ A^*(Y')` along `f : Y' ⟶ Y` is unital:
> it carries the identity class `1 ∈ A^0(Y)` of Stacks 0FBS to the identity class `1 ∈ A^0(Y')`.
> Nothing is assumed.
>
> This is `Stacks.Chow.chowCohomologyRestriction_bivariantIdentityClass` with its case of Stacks
> 02TA discharged by `Stacks.Chow.gysinSystemOfInvertible_isNaturalUnderBaseChangeIso` and its two
> Gysin axioms for the transported identity cap rule discharged by
> `Stacks.Chow.IdentityCapRule.transportGysinNaturality` — exactly the proofs
> `Stacks.Chow.bivariantIdentityClassOfInvertible` is built from, so the two identity classes in
> the statement are the unconditional ones.

```lean
theorem chowCohomologyRestrictionOfInvertible_bivariantIdentityClass :
    chowCohomologyRestrictionOfInvertible C sY f 0 (bivariantIdentityClassOfInvertible C sY) =
      bivariantIdentityClassOfInvertible C (f ≫ sY)
```

**`Stacks.Chow.chowCohomologyTotalRestrictionRingOfInvertible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/ChowCohomologyRestriction.lean, line 686](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/ChowCohomologyRestriction.lean#L686). The attribute's comment: “the canonical map res : A^*(Y) → A^*(Y') on the graded groups is a homomorphism for addition and for the multiplication of Stacks 0B75 -- at the Gysin system of the first Chern class rule, with nothing assumed beyond the tag's own hypotheses”.

> **Stacks 0B7F.** The restriction map `res : A^*(Y) ⟶ A^*(Y')` along `f : Y' ⟶ Y` as a map of
> the ring structures of the graded Chow cohomology: a homomorphism for addition and for the
> multiplication of Stacks 0B75, at the Gysin system of the first Chern class rule. It is often
> written `f^*`.
>
> Its underlying additive map is `Stacks.Chow.chowCohomologyTotalRestrictionOfInvertible`, and that
> it also carries `1` to `1` is `Stacks.Chow.chowCohomologyTotalRestrictionRingOfInvertible_map_one`
> just below; since an additive map between abelian groups is `ℤ`-linear, the two together are the
> whole of the tag's "map of `ℤ`-algebras". Nothing is assumed.
>
> The proof reduces to the degreewise statement
> `Stacks.Chow.chowCohomologyRestrictionOfInvertible_mul`: multiplication on a `DirectSum` is
> bilinear, so both sides of `res(x ⬝ y) = res(x) ⬝ res(y)` are additive in `x` and in `y` and it
> is enough to check them on the summands.

```lean
def chowCohomologyTotalRestrictionRingOfInvertible :
    chowCohomology C (gysinSystemOfInvertible C) sY →ₙ+*
      chowCohomology C (gysinSystemOfInvertible C) (f ≫ sY)
```

**`Stacks.Chow.chowCohomologyTotalRestrictionRingOfInvertible_map_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/ChowCohomologyRestriction.lean, line 717](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/ChowCohomologyRestriction.lean#L717). The attribute's comment: “the canonical map res : A^*(Y) → A^*(Y') on the graded groups carries the unit 1 of A^*(Y) to the unit of A^*(Y') -- at the Gysin system of the first Chern class rule, with nothing assumed beyond the tag's own hypotheses”.

> **Stacks 0B7F.** The restriction map `res : A^*(Y) ⟶ A^*(Y')` carries the unit `1` of
> `A^*(Y)` to the unit of `A^*(Y')`: the unit of the graded ring is the identity class of Stacks
> 0FBS sitting in degree `0`, and `res` carries it to the identity class of `A^0(Y')` by
> `Stacks.Chow.chowCohomologyRestrictionOfInvertible_bivariantIdentityClass`. Nothing is
> assumed.

```lean
theorem chowCohomologyTotalRestrictionRingOfInvertible_map_one :
    chowCohomologyTotalRestrictionRingOfInvertible C sY f 1 = 1
```

**`Stacks.Chow.chowCohomologyRestriction_chowCohomologyComposite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingProjectionFormula/RestrictionMultiplicative.lean, line 475](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingProjectionFormula/RestrictionMultiplicative.lean#L475). The attribute's comment: “the multiplicativity of the canonical map: res(c ∘ c') = res(c) ∘ res(c') for the multiplication of A^* that is composition of bivariant classes, which is the clause that the map of graded groups is a map of algebras”.

> **The restriction map of Stacks 0B7F is multiplicative:** `res(c ∘ c') = res(c) ∘ res(c')` for
> the multiplication `Stacks.Chow.chowCohomologyComposite` of `A^*`, and so for the restriction
> `Aⁱ(X) ⟶ Aⁱ(Z)` of Stacks 0F9Z that the second pairing of Stacks 0FA0 is built from.
>
> This is the clause of Stacks 0B7F asserting that `res : A^*(Y) ⟶ A^*(Y')` is a map of
> `ℤ`-algebras, for the multiplication of `A^*` that this repository has. It is also the first of
> the two inputs an associativity proof for the multiplication of Stacks 0FA0 needs: the degree `n`
> terms `res(res(c) ∘ c') ∘ c''` and `res(c) ∘ (res(c') ∘ c'')` of the two groupings cannot be
> compared without it, however associative the composition of Stacks 0B75 is.
>
> Both sides cap, on a test scheme `g : T ⟶ Y'`, by capping with `c'` and then with `c`, both at
> test morphisms over `Y` obtained from `g ≫ f`; the two differ by an isomorphism of test schemes,
> which the proper-pushforward axiom of Stacks 0B76 for `c` absorbs.

```lean
theorem chowCohomologyRestriction_chowCohomologyComposite (i j : ℤ)
    (c : chowCohomologyComponent C G sY i) (c' : chowCohomologyComponent C G sY j) :
    chowCohomologyRestriction C G sY f (i + j) hgys
        (chowCohomologyComposite C G sY hgys hgysc i j c c') =
      chowCohomologyComposite C G (f ≫ sY) hgys hgysc i j
        (chowCohomologyRestriction C G sY f i hgys c)
        (chowCohomologyRestriction C G sY f j hgys c')
```

## Tag 0B77, a lemma

[Tag 0B77](https://stacks.math.columbia.edu/tag/0B77) in the Stacks Project.

**`Stacks.Chow.isFirstChernClassBivariant_firstChernClassBivariantCanonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/FirstChernClassCanonical.lean, line 399](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/FirstChernClassCanonical.lean#L399).

> The bivariant class `Stacks.Chow.firstChernClassBivariantCanonical` caps by `c₁(g^*ℒ) ∩ -` on
> every test scheme.

```lean
theorem isFirstChernClassBivariant_firstChernClassBivariantCanonical :
    IsFirstChernClassBivariant C sX (canonicalFirstChernCapRule C) L (canonicalGysinSystem C)
      (firstChernClassBivariantCanonical C sX L)
```

**`Stacks.Chow.GenuineChern.firstChernClassBivariantClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/FirstChernClassBivariant.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/FirstChernClassBivariant.lean#L69).

> For an invertible module `ℒ` on `X`, the rule assigning to `f : X' ⟶ X` the operation
> `c₁(f^*ℒ) ∩ - : A_k(X') ⟶ A_{k-1}(X')` is a bivariant class of degree `1`: the class
> `c₁(ℒ) ∈ A^1(X)` together with the statement that it caps by `c₁(f^*ℒ) ∩ -` on every test
> scheme.

```lean
def firstChernClassBivariantClass :
    {c : BivariantClass C (gysinSystemOfInvertible C) sX sX (𝟙 X) (Category.id_comp sX) 1 //
      ∀ {T : Scheme.{u}} (g : T ⟶ X) [LocallyOfFiniteType g] (k : ℤ)
        (α : chowGroup C (g ≫ sX) k),
        c.idRule C sX (gysinSystemOfInvertible C) g k α =
          (invCap C (g ≫ sX) ((Scheme.Modules.pullback g).obj L)).capOnChow C (g ≫ sX) (k - 1)
            (chowGroupCast C (g ≫ sX) (by omega) α)}
```

## Tag 0FDW, a definition

[Tag 0FDW](https://stacks.math.columbia.edu/tag/0FDW) in the Stacks Project.

**`Stacks.Chow.firstChernClassBivariantCanonical`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/FirstChernClassCanonical.lean, line 388](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/FirstChernClassCanonical.lean#L388).

> The first Chern class `c₁(ℒ) ∈ A^1(X)` of an invertible module `ℒ` on a scheme `X` locally of
> finite type over the base, as a bivariant class of degree `1` for `𝟙 X` at the canonical Gysin
> system.

```lean
def firstChernClassBivariantCanonical :
    BivariantClass C (canonicalGysinSystem C) sX sX (𝟙 X) (Category.id_comp sX) 1
```

## Tag 0B7B, a lemma

[Tag 0B7B](https://stacks.math.columbia.edu/tag/0B7B) in the Stacks Project.

**`Stacks.Chow.GenuineChern.comp_firstChernClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/BivariantFirstChernCentral.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/BivariantFirstChernCentral.lean#L75). The attribute's comment: “(2): c ∘ c\_1(L) = c\_1(f^*L) ∘ c in A^\{p+1}(X' → X) for every f : X' → X locally of finite type and every bivariant class c in A^p(X' → X) of Stacks 0B76”.

> **Stacks 0B7B (2).** Let `ℒ` be an invertible `𝒪_X`-module, let `f : X' ⟶ X` be locally of
> finite type and let `c ∈ A^p(X' ⟶ X)` be a bivariant class. Then
>
>   `c ∘ c₁(ℒ) = c₁(f^*ℒ) ∘ c`   in   `A^{p+1}(X' ⟶ X)`,
>
> with `c₁(ℒ) ∈ A^1(X)` and `c₁(f^*ℒ) ∈ A^1(X')` the bivariant first Chern classes of Stacks 0B77.
> The left side is a class for `f ≫ 𝟙 X` of degree `p + 1`; the right side, a class for `𝟙 X' ≫ f` of
> degree `1 + p`, is read as one for `f ≫ 𝟙 X` of degree `p + 1` along the identity of `X'`.

```lean
theorem comp_firstChernClass {X' : Scheme.{u}} {sX' : X' ⟶ C.S} [LocallyOfFiniteType sX']
    (L : X.Modules) [SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L]
    (f : X' ⟶ X) (hf : f ≫ sX = sX') {p : ℤ} (c : BivariantChowClass C sX' sX f hf p) :
    haveI := isInvertible_pullback f L
    c.comp (BivariantChowClass.equivBivariantClass.symm (firstChernClass C sX L)) =
      (((BivariantChowClass.equivBivariantClass.symm
          (firstChernClass C sX' ((Scheme.Modules.pullback f).obj L))).comp c).degreeCongr
        (add_comm 1 p)).transport (comp_comp_structureMorphism_eq hf (Category.id_comp sX))
        (Iso.refl X') (by simp)
```

**`Stacks.Chow.GenuineChern.firstChernClass_mem_center`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/BivariantFirstChernCentral.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/BivariantFirstChernCentral.lean#L92). The attribute's comment: “(1): c\_1(L) in A^1(X) is in the center of the Chow cohomology ring A^*(X) of Stacks 0B7E, for the bivariant first Chern class of Stacks 0B77”.

> **Stacks 0B7B (1).** The first Chern class `c₁(ℒ) ∈ A^1(X)` of an invertible `𝒪_X`-module lies
> in the center of the Chow cohomology ring `A^*(X)` of Stacks 0B7E. The ring structure is an
> `@[instance_reducible] def` and not an `instance`, which is why it is supplied by hand.

```lean
theorem firstChernClass_mem_center (L : X.Modules)
    [SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L] :
    letI : Ring (chowCohomology C (gysinSystemOfInvertible C) sX) :=
      chowCohomologyRingOfInvertible C sX
    DirectSum.of (fun q : ℤ ↦ chowCohomologyComponent C (gysinSystemOfInvertible C) sX q) 1
        (firstChernClass C sX L) ∈
      Subring.center (chowCohomology C (gysinSystemOfInvertible C) sX)
```

**`Stacks.Chow.BivariantClass.heq_bivariantCompositeOfInvertible_firstChernClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/FirstChernClassCommute.lean, line 387](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/FirstChernClassCommute.lean#L387). The attribute's comment: “(2), for a homogeneous c in A^q(X' -> X) and the composition of Stacks 0B75 at the Gysin system of the first Chern class of an invertible module; the two composites are classes for g ≫ 𝟙 X and 𝟙 X' ≫ g of degrees q + 1 and 1 + q, whence the heterogeneous equality”.

> **Stacks 0B7B (2).** Let `g : X' ⟶ X` be locally of finite type, let `c ∈ A^q(X' ⟶ X)` and
> let `ℒ` be an invertible `𝒪_X`-module. Then
>
>   `c ∘ c₁(ℒ) = c₁(g^*ℒ) ∘ c`   in   `A^{q+1}(X' ⟶ X)`,
>
> the composites being those of Stacks 0B75, classes for the equal morphisms `g ≫ 𝟙 X` and
> `𝟙 X' ≫ g` of the equal degrees `q + 1` and `1 + q`.

```lean
theorem BivariantClass.heq_bivariantCompositeOfInvertible_firstChernClass
    (c : BivariantClass C (gysinSystemOfInvertible C) sX' sX g hg q) (L : X.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L] :
    haveI := GenuineChern.isInvertible_pullback g L
    bivariantCompositeOfInvertible C sX' sX sX g (𝟙 X) hg (Category.id_comp sX) q 1 c
        (GenuineChern.firstChernClass C sX L) ≍
      bivariantCompositeOfInvertible C sX' sX' sX (𝟙 X') g (Category.id_comp sX') hg 1 q
        (GenuineChern.firstChernClass C sX' ((Scheme.Modules.pullback g).obj L)) c
```

**`Stacks.Chow.BivariantClass.heq_mulId_firstChernClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/FirstChernClassCommute.lean, line 415](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/FirstChernClassCommute.lean#L415). The attribute's comment: “(1), for the product of A^*(X) given by the composition of Stacks 0B75 at the Gysin system of the first Chern class of an invertible module, against every homogeneous c in A^q(X); the two products have degrees q + 1 and 1 + q, whence the heterogeneous equality”.

> **Stacks 0B7B (1).** The first Chern class `c₁(ℒ) ∈ A^1(X)` of an invertible module is in the
> center of `A^*(X)`: for every `c ∈ A^q(X)`,
>
>   `c · c₁(ℒ) = c₁(ℒ) · c`,
>
> the two products lying in `A^{q+1}(X)` and `A^{1+q}(X)`.

```lean
theorem BivariantClass.heq_mulId_firstChernClass
    (c : BivariantClass C (gysinSystemOfInvertible C) sX sX (𝟙 X) (Category.id_comp sX) q)
    (L : X.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L] :
    c.mulId C sX (GenuineChern.firstChernClass C sX L) ≍
      (GenuineChern.firstChernClass C sX L).mulId C sX c
```

## Tag 0FDX, a lemma

[Tag 0FDX](https://stacks.math.columbia.edu/tag/0FDX) in the Stacks Project.

**`Stacks.Chow.iteratedChernCapOnChow_ofFn_eq_zero_of_topologicalKrullDim_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernCapDimensionInduction.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernCapDimensionInduction.lean#L287). The attribute's comment: “the conclusion read on EVERY test scheme locally of finite type, with no bound on its dimension: the cap operation of the product of the d+1 first Chern classes annihilates every Chow class of every such test scheme. This is the clause the source's induction on d proves, and the one the dimension-counting proofs of ChernCapDimensionVanishing do not reach”.

> **Stacks 0FDX, on every test scheme locally of finite type.**
>
> Let `X` be locally of finite type over the base scheme of chapter 42, Noetherian, and carrying an
> ample invertible module `A`, and let `dim X ≤ d`. For invertible `𝒪_X`-modules `ℒ_1, …, ℒ_{d+1}`
> and every test scheme `u : T ⟶ X` locally of finite type,
>
>   `c₁(u^*ℒ_1) ∩ ⋯ ∩ c₁(u^*ℒ_{d+1}) ∩ α = 0`   for every Chow class `α` of `T`.
>
> No bound is placed on the dimension of `T`: this is the cap-level content of the vanishing of
> `c₁(ℒ_1) ∘ ⋯ ∘ c₁(ℒ_{d+1})` in `A^{d+1}(X)`, which by Stacks 02UC is exactly the vanishing of
> the cap operation on every such `T`, and it is what the source's induction on `d` establishes.
>
> The proof is that induction. The base case `d = 0` is
> `Stacks.Chow.invCap_capOnChow_pullback_eq_zero_of_topologicalKrullDim_le_zero`; the step is
> `Stacks.Chow.iteratedChernCapOnChow_ofFn_succ_eq_zero_of_effectiveCartierDivisors` applied to the
> two effective Cartier divisors Stacks 0AYM produces from `ℒ_{d+2}` and the ample module, with the
> inductive hypothesis transported to each of them along the closed immersion.
>
> The ample invertible module is used only through Stacks 0AYM, and Noetherianness only through
> Stacks 0AYM and the dimension drop; both follow from the source's hypothesis that `X` be of
> finite type over the base, the base being locally Noetherian.

```lean
theorem iteratedChernCapOnChow_ofFn_eq_zero_of_topologicalKrullDim_le (d : ℕ) {X : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] [IsNoetherian X] (A : X.Modules)
    [Stacks.Ample.IsInvertibleModule X A] (hA : Stacks.Ample.IsAmple X A)
    (hdim : topologicalKrullDim X ≤ (d : WithBot ℕ∞)) (N : Fin (d + 1) → X.Modules)
    [∀ i, AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property (N i)]
    {T : Scheme.{u}} (u : T ⟶ X) [LocallyOfFiniteType u] (q : T ⟶ C.S) [LocallyOfFiniteType q]
    (hq : u ≫ sX = q) (k : ℤ)
    (α : chowGroup C q
      (k + ((List.ofFn fun i => invCap C q ((Scheme.Modules.pullback u).obj (N i))).length : ℤ))) :
    iteratedChernCapOnChow C q
      (List.ofFn fun i => invCap C q ((Scheme.Modules.pullback u).obj (N i))) k α = 0
```

**`Stacks.Chow.iteratedChernCapOnChow_eq_zero_of_topologicalKrullDim_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernCapDimensionVanishing.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernCapDimensionVanishing.lean#L232). The attribute's comment: “the cap-product form on the test scheme X itself: a product of d+1 or more first Chern class cap operators annihilates every Chow class of X, for X locally of finite type over a Jacobson base whose dimension function vanishes at closed points and of topological dimension at most d. The product of first Chern classes is the iterated cap operation Stacks.Chow.iteratedChernCapOnChow on an arbitrary list of Stacks.Chow.ChernCapOperator, not a composite of bivariant classes: no such composite is constructed in this library, so the equality in A^\{d+1}(X) that the source states has no term here. The ample invertible module of the source is not assumed, being used there only to reach Stacks 0AYM. Proved by a delta-dimension count — CH\_k(X) is zero outside 0 ≤ k ≤ d — rather than by the induction on d of the source, so the same vanishing holds for every additive map of that bidegree”.

> **Stacks 0FDX, the cap-product form on `X` itself.** Let `X` be locally of finite type over
> a Jacobson base whose dimension function vanishes at closed points, and let the topological
> dimension of `X` be at most `d`. Then any `d + 1` (or more) first Chern class cap operators on
> `X` annihilate every Chow class of `X`:
>
>   `c₁(L_1) ∩ ⋯ ∩ c₁(L_{d+1}) ∩ α = 0`   in `CH_k(X)`,  for every `α ∈ CH_{k + d + 1}(X)`.
>
> The operation goes `CH_{k + r}(X) ⟶ CH_k(X)` with `r = Os.length ≥ d + 1`. For `k < 0` the
> target vanishes, and for `k ≥ 0` the source has degree `k + r ≥ d + 1 > d` and vanishes. So the
> proof is a delta-dimension count, not the induction on `d` of the source, and it establishes the
> same vanishing for every additive map of that bidegree.

```lean
theorem iteratedChernCapOnChow_eq_zero_of_topologicalKrullDim_le {X : Scheme.{u}} (p : X ⟶ C.S)
    [LocallyOfFiniteType p] {d : ℕ} (hd : topologicalKrullDim X ≤ (d : WithBot ℕ∞))
    (Os : List (ChernCapOperator C p)) (hlen : d + 1 ≤ Os.length) (k : ℤ)
    (α : chowGroup C p (k + (Os.length : ℤ))) :
    iteratedChernCapOnChow C p Os k α = 0
```

**`Stacks.Chow.firstChernCapTower_eq_zero_of_topologicalKrullDim_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernCapDimensionVanishing.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernCapDimensionVanishing.lean#L289). The attribute's comment: “the conclusion for the product of the first Chern classes of the GIVEN invertible modules L\_1, …, L\_\{d+1} on X: that product annihilates every Chow class of X, for X locally of finite type over a Jacobson base whose dimension function vanishes at closed points and of topological dimension at most d. The product is read as the composite of the Chow-group cap products Stacks.Chow.firstChernCapStep of the modules themselves — Stacks.Chow.firstChernCapTower — and NOT as an equality in A^\{d+1}(X): no composite of bivariant classes is constructed in this library, so the source's conclusion has no term here. Carried: Stacks 02TI for each module, as the hypotheses InvertibleChernCapDescends, which by Stacks.Chow.firstChernClassCapFactorsThroughRationalEquivalence\_iff are implied by the mere existence of the descended cap products and so are not a weakening. The ample invertible module of the source is not assumed, being used there only to reach Stacks 0AYM. Proved by a delta-dimension count — CH\_k(X) is zero outside 0 ≤ k ≤ d — rather than by the induction on d of the source”.

> **Stacks 0FDX for the first Chern classes of given invertible modules.** Let `X` be locally
> of finite type over a Jacobson base whose dimension function vanishes at closed points, and let
> the topological dimension of `X` be at most `d`. Then for every sequence `L_1, L_2, …` of
> invertible `𝒪_X`-modules on `X` and every `r ≥ d + 1`,
>
>   `c₁(L_1) ∩ ⋯ ∩ c₁(L_r) ∩ α = 0`   in `A_{n-r}(X)`,  for every `α ∈ A_n(X)`,
>
> the product being the tower `Stacks.Chow.firstChernCapTower` of the cap products
> `Stacks.Chow.firstChernCapStep` of the `L_i` themselves.
>
> The degree count: if `n - r < 0` the target `A_{n-r}(X)` vanishes, and otherwise
> `n ≥ r ≥ d + 1 > d`, so the source `A_n(X)` vanishes.

```lean
theorem firstChernCapTower_eq_zero_of_topologicalKrullDim_le {X : Scheme.{u}} (p : X ⟶ C.S)
    [LocallyOfFiniteType p] {d : ℕ} (hd : topologicalKrullDim X ≤ (d : WithBot ℕ∞)) (n : ℤ)
    (L : ℕ → X.Modules)
    [∀ i, AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property (L i)]
    (hfac : ∀ i, InvertibleChernCapDescends C p (L i)) (r : ℕ) (hr : d + 1 ≤ r)
    (α : chowGroup C p (n - ((0 : ℕ) : ℤ))) :
    firstChernCapTower C p n L hfac r α = 0
```

**`Stacks.Chow.BivariantClass.cap_eq_zero_of_topologicalKrullDim_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernCapDimensionVanishing.lean, line 316](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernCapDimensionVanishing.lean#L316). The attribute's comment: “the conclusion read on the test schemes of dimension at most d: every bivariant class of degree at least d+1 caps every Chow class of such a test scheme to zero, for a Jacobson base whose dimension function vanishes at closed points. This covers the test scheme X itself but not the test schemes of dimension larger than d, so it does not give the equality c = 0 in A^\{d+1}(X) that the source states; and the class c is arbitrary of that degree rather than a composite of first Chern classes, no composite of bivariant classes being constructed in this library”.

> **Stacks 0FDX on the test schemes of dimension at most `d`.** A bivariant class of degree at
> least `d + 1` caps every Chow class of every test scheme of topological dimension at most `d` to
> zero. Applied to a product of `d + 1` first Chern classes on a scheme `X` of dimension `d`, and
> to the test scheme `X` itself, this is the conclusion of Stacks 0FDX read on that test scheme.
>
> For a test scheme `T` of dimension at most `d` the source group `CH_k(T)` vanishes unless
> `0 ≤ k ≤ d`, and in that range the target group has degree `k - p ≤ d - (d + 1) < 0`, so it
> vanishes by nonnegativity of the delta-dimension.

```lean
theorem BivariantClass.cap_eq_zero_of_topologicalKrullDim_le (G : GysinSystem C)
    {X Y : Scheme.{u}} (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S)
    [LocallyOfFiniteType sY] (f : X ⟶ Y) [LocallyOfFiniteType f] (hf : f ≫ sY = sX) {p : ℤ}
    (c : BivariantClass C G sX sY f hf p) {d : ℕ} (hp : (d : ℤ) + 1 ≤ p) {T : Scheme.{u}}
    (g : T ⟶ Y) [LocallyOfFiniteType g] (hT : topologicalKrullDim T ≤ (d : WithBot ℕ∞))
    (k : ℤ) (α : chowGroup C (g ≫ sY) k) :
    c.cap g k α = 0
```

**`Stacks.Chow.firstChernClassProduct_eq_zero_of_topologicalKrullDim_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FirstChernClassProductVanishing.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FirstChernClassProductVanishing.lean#L168).

> **Stacks 0FDX.** Let `X` be a scheme of finite type over the base scheme `S` of chapter 42
> which has an ample invertible module `A`, and let `dim X ≤ d`. Then for invertible
> `𝒪_X`-modules `ℒ_1, …, ℒ_{d+1}` on `X`
>
>   `c₁(ℒ_1) ∘ ⋯ ∘ c₁(ℒ_{d+1}) = 0`   in `A^{d+1}(X)`,
>
> the product being the composition of Stacks 0B75 of the bivariant first Chern classes of
> Stacks 0B77, at the Gysin system of the first Chern class rule.

```lean
theorem firstChernClassProduct_eq_zero_of_topologicalKrullDim_le [QuasiCompact sX]
    (A : X.Modules) [Stacks.Ample.IsInvertibleModule X A] (hA : Stacks.Ample.IsAmple X A)
    (d : ℕ) (hdim : topologicalKrullDim X ≤ (d : WithBot ℕ∞)) (L : Fin (d + 1) → X.Modules)
    [∀ i, AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property (L i)] :
    firstChernClassProduct C sX d L = 0
```

## Tag 0FA0, a remark

[Tag 0FA0](https://stacks.math.columbia.edu/tag/0FA0) in the Stacks Project.

**`Stacks.Chow.localizedBivariantGrading`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGrading.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGrading.lean#L53). The attribute's comment: “localized\_bivariant\_grading”.

> **Stacks 0FA0.** The group `A⁽ᵖ⁾(Z ⟶ X)` attached to a closed immersion `f : Z ⟶ X` of
> schemes locally of finite type over the base: operational Chow classes on `X` in the degrees
> below `p`, and bivariant classes for `f` in the degrees from `p` onward.

```lean
abbrev localizedBivariantGrading (C : ChowSituation.{u}) (G : GysinSystem C) {Z X : Scheme.{u}}
    (sZ : Z ⟶ C.S) [LocallyOfFiniteType sZ] (sX : X ⟶ C.S) [LocallyOfFiniteType sX]
    (f : Z ⟶ X) [IsClosedImmersion f] (hf : f ≫ sX = sZ) (p : ℕ) : Type (u + 1)
```

**`Stacks.Chow.localizedBivariantGradingMulHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingAlgebra.lean, line 620](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingAlgebra.lean#L620). The attribute's comment: “the multiplication of the remark's graded algebra as a biadditive map A^(p)(Z ⟶ X) ⟶ A^(q)(Z ⟶ X) ⟶ A^(r)(Z ⟶ X), which is its distributive law, at every p, q and every target r”.

> **Stacks 0FA0.** The multiplication
> `A⁽ᵖ⁾(Z ⟶ X) × A⁽ᑫ⁾(Z ⟶ X) ⟶ A⁽ʳ⁾(Z ⟶ X)` of the remark as a **biadditive map**, at every `p`, `q`
> and every target `r`. This is the distributive law of the source's graded algebra, bundled: the
> underlying function is `Stacks.Chow.localizedBivariantGradingMul` and the additivity in each
> argument is `Stacks.Chow.localizedBivariantGradingMul_add_left` and `_add_right`.

```lean
def localizedBivariantGradingMulHom (p q r : ℕ) :
    localizedBivariantGrading C G (f ≫ sX) sX f rfl p →+
      localizedBivariantGrading C G (f ≫ sX) sX f rfl q →+
        localizedBivariantGrading C G (f ≫ sX) sX f rfl r
```

**`Stacks.Chow.localizedBivariantGradingMulMaxHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingAlgebra.lean, line 635](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingAlgebra.lean#L635). The attribute's comment: “the multiplication A^(p)(Z ⟶ X) × A^(q)(Z ⟶ X) ⟶ A^(max(p,q))(Z ⟶ X) displayed in the remark as a biadditive map, for every p and q”.

> **Stacks 0FA0.** The multiplication with the target `A⁽ᵐᵃˣ⁽ᵖ⁼ᑫ⁾⁾(Z ⟶ X)` the source displays,
> as a biadditive map.

```lean
def localizedBivariantGradingMulMaxHom (p q : ℕ) :
    localizedBivariantGrading C G (f ≫ sX) sX f rfl p →+
      localizedBivariantGrading C G (f ≫ sX) sX f rfl q →+
        localizedBivariantGrading C G (f ≫ sX) sX f rfl (max p q)
```

**`Stacks.Chow.localizedBivariantGradingInternalMulHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingAlgebra.lean, line 645](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingAlgebra.lean#L645). The attribute's comment: “the multiplication internal to A^(p)(Z ⟶ X) of the remark's graded algebra as a biadditive map A^(p) ⟶ A^(p) ⟶ A^(p), which is its distributive law, for every p ≥ 0”.

> **Stacks 0FA0.** The multiplication internal to `A⁽ᵖ⁾(Z ⟶ X)` — the product of the source's
> graded algebra — as a biadditive map, for every `p ≥ 0`.

```lean
def localizedBivariantGradingInternalMulHom (p : ℕ) :
    localizedBivariantGrading C G (f ≫ sX) sX f rfl p →+
      localizedBivariantGrading C G (f ≫ sX) sX f rfl p →+
        localizedBivariantGrading C G (f ≫ sX) sX f rfl p
```

**`Stacks.Chow.eq_localizedBivariantGradingMulHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingAlgebra.lean, line 668](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingAlgebra.lean#L668). The attribute's comment: “uniqueness of the canonical multiplication as a biadditive map: a biadditive map satisfying the two finite-convolution formulas of the remark is the multiplication”.

> **Stacks 0FA0, uniqueness of the canonical multiplication as a biadditive map.** A biadditive
> map whose components are the two finite convolutions of the source — the property
> `Stacks.Chow.LocalizedGrading.IsMul` — is `Stacks.Chow.localizedBivariantGradingMulHom`. This is
> `Stacks.Chow.LocalizedGrading.IsMul.eq_localizedBivariantGradingMul` read through
> `Stacks.Chow.localizedBivariantGradingMulHom_apply`; additivity is not used in the uniqueness, the
> component formulas already prescribing every value.

```lean
theorem eq_localizedBivariantGradingMulHom (p q r : ℕ)
    (M : localizedBivariantGrading C G (f ≫ sX) sX f rfl p →+
      localizedBivariantGrading C G (f ≫ sX) sX f rfl q →+
        localizedBivariantGrading C G (f ≫ sX) sX f rfl r)
    (hM : LocalizedGrading.IsMul C G sX f hRG hgysP hgys hgysc p q r fun a b ↦ M a b) :
    M = localizedBivariantGradingMulHom C G sX f hRG hgysP hgys hgysc p q r
```

**`Stacks.Chow.localizedBivariantGradingOne`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingAlgebra.lean, line 822](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingAlgebra.lean#L822). The attribute's comment: “the unit of the remark's graded algebra on A^(p)(Z ⟶ X): the class 1 of A^0(X) in the degree 0 slot, which is a slot of A^(p)(Z ⟶ X) exactly for p ≥ 1”.

> **Stacks 0FA0, the unit of the graded algebra on `A⁽ᵖ⁾(Z ⟶ X)`:** the element whose degree `0`
> component is the class `1 ∈ A⁰(X)` of Stacks 0FBS and whose components in the other degrees
> vanish.
>
> For `p ≥ 1` the degree `0` slot of `A⁽ᵖ⁾(Z ⟶ X)` is `A⁰(X)` and this is the unit; for `p = 0` that
> slot is `A⁰(Z ⟶ X)`, which holds no canonical class, and this element is zero there. Together with
> `Stacks.Chow.localizedGrading_self_admissible_iff` that makes `p = 1` the one `p` at which the
> source's graded algebra on `A⁽ᵖ⁾(Z ⟶ X)` is unital.

```lean
def localizedBivariantGradingOne (p : ℕ) :
    localizedBivariantGrading C G (f ≫ sX) sX f rfl p
```

**`Stacks.Chow.localizedBivariantGradingInternalMul_one_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingAlgebra.lean, line 1033](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingAlgebra.lean#L1033). The attribute's comment: “the unit law of the remark's graded algebra on A^(p)(Z ⟶ X) for every p ≥ 1: the class 1 of A^0(X) placed in degree 0 is a left unit for the multiplication internal to A^(p)(Z ⟶ X), on all of A^(p)(Z ⟶ X)”.

> **Stacks 0FA0, the unit law of the graded algebra on `A⁽ᵖ⁾(Z ⟶ X)`, for every `p ≥ 1`:**
> multiplying by `Stacks.Chow.localizedBivariantGradingOne` on the left returns the element. The
> bound `1 ≤ p` is what puts the degree `0` slot, where the unit sits, in `A⁰(X)`; for `p = 0` that
> slot is `A⁰(Z ⟶ X)` and holds no canonical class.
>
> Degree by degree the product has a single surviving term, the one at `i = 0`: below the cutoff it
> is `1 · bₙ` in `A^*(X)` (`Stacks.Chow.chowCohomologyComposite_identityClass_left`), and from the
> cutoff on it is the source's second pairing at the unit
> (`Stacks.Chow.localizedMulChowBivariant_identityClass_left`), which is `res(1) ∘ bₙ = bₙ`.
>
> No hypothesis is imposed on `b`: the index range of the sums,
> `Finset.Icc (min 0 n) (max 0 n)`, contains the one surviving index `i = 0` in every degree
> (`Stacks.Chow.zero_mem_Icc_min_max`), so the law holds on all of `A⁽ᵖ⁾(Z ⟶ X)` — which is the group
> the source asserts the graded algebra on, negative-degree factors included. See the implementation
> notes of this module.

```lean
theorem localizedBivariantGradingInternalMul_one_left (p : ℕ) (hp : 1 ≤ p)
    (b : localizedBivariantGrading C G (f ≫ sX) sX f rfl p) :
    localizedBivariantGradingInternalMul C G sX f hRG hgysP hgys hgysc p
        (localizedBivariantGradingOne C G sX f hgysinX p) b = b
```

**`Stacks.Chow.localizedBivariantGradingInternalMul_one_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingAlgebra.lean, line 1087](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingAlgebra.lean#L1087). The attribute's comment: “the unit law of the remark's graded algebra on A^(p)(Z ⟶ X) on the right for every p ≥ 1: the class 1 of A^0(X) placed in degree 0 is a right unit for the multiplication internal to A^(p)(Z ⟶ X), on all of A^(p)(Z ⟶ X)”.

> **Stacks 0FA0, the unit law of the graded algebra on `A⁽ᵖ⁾(Z ⟶ X)` on the right, for every
> `p ≥ 1`:** multiplying by `Stacks.Chow.localizedBivariantGradingOne` on the right returns the
> element. Together with `Stacks.Chow.localizedBivariantGradingInternalMul_one_left` this makes
> `Stacks.Chow.localizedBivariantGradingOne` a two-sided unit, and with the associativity of
> `Stacks.Chow.localizedBivariantGradingInternalMul_assoc` it is what
> `Stacks.Chow.localizedBivariantGradingMonoid` is assembled from.
>
> Here the surviving term of the degree `n` component is the one at `i = n`, and the pairing that
> applies is the source's *first* one, `Stacks.Chow.localizedMulBivariantChow_identityClass_right`:
> `bₙ ∘ 1 = bₙ`.
>
> This law is the sharp test of the index range of the sums: the component of `b` it has to return
> in degree `n` is carried by the term at `i = n` alone. The range
> `Finset.Icc (min 0 n) (max 0 n)` contains `i = n` in every degree
> (`Stacks.Chow.self_mem_Icc_min_max`), so the law needs no hypothesis on `b` and holds on all of
> `A⁽ᵖ⁾(Z ⟶ X)`; under the narrower range `0 ≤ i ≤ n` it would fail in every negative degree in which
> `b` has a nonzero component. See the implementation notes of this module.

```lean
theorem localizedBivariantGradingInternalMul_one_right (p : ℕ) (hp : 1 ≤ p)
    (b : localizedBivariantGrading C G (f ≫ sX) sX f rfl p) :
    localizedBivariantGradingInternalMul C G sX f hRG hgysP hgys hgysc p b
        (localizedBivariantGradingOne C G sX f hgysinX p) = b
```

**`Stacks.Chow.localizedBivariantGradingInternalMulHomOfInvertible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingAlgebra.lean, line 1163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingAlgebra.lean#L1163). The attribute's comment: “the multiplication internal to A^(p)(Z ⟶ X) of the remark's graded algebra as a biadditive map, which is its distributive law, at the Gysin system of the first Chern class rule with nothing assumed”.

> **Stacks 0FA0.** The multiplication internal to `A⁽ᵖ⁾(Z ⟶ X)` of the remark's graded algebra
> as a biadditive map, at the Gysin system of the first Chern class rule, where nothing is
> assumed.

```lean
def localizedBivariantGradingInternalMulHomOfInvertible (p : ℕ) :
    localizedBivariantGrading C (gysinSystemOfInvertible C) (f ≫ sX) sX f rfl p →+
      localizedBivariantGrading C (gysinSystemOfInvertible C) (f ≫ sX) sX f rfl p →+
        localizedBivariantGrading C (gysinSystemOfInvertible C) (f ≫ sX) sX f rfl p
```

**`Stacks.Chow.localizedBivariantGradingOneOfInvertible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingAlgebra.lean, line 1178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingAlgebra.lean#L1178). The attribute's comment: “the unit of the remark's graded algebra on A^(p)(Z ⟶ X), at the Gysin system of the first Chern class rule with nothing assumed”.

> **Stacks 0FA0, the unit of the graded algebra** at the Gysin system of the first Chern class
> rule, where nothing is assumed: its degree `0` component is
> `Stacks.Chow.bivariantIdentityClassOfInvertible`.

```lean
def localizedBivariantGradingOneOfInvertible (p : ℕ) :
    localizedBivariantGrading C (gysinSystemOfInvertible C) (f ≫ sX) sX f rfl p
```

**`Stacks.Chow.localizedBivariantGradingInternalMul_one_left_ofInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingAlgebra.lean, line 1188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingAlgebra.lean#L1188). The attribute's comment: “the unit law of the remark's graded algebra on A^(p)(Z ⟶ X) for every p ≥ 1, on all of A^(p)(Z ⟶ X), at the Gysin system of the first Chern class rule with NOTHING ASSUMED”.

> **Stacks 0FA0, the unit law of the graded algebra on `A⁽ᵖ⁾(Z ⟶ X)` for every `p ≥ 1`** at the
> Gysin system of the first Chern class rule, where nothing at all is assumed: the law holds on all
> of `A⁽ᵖ⁾(Z ⟶ X)`.

```lean
theorem localizedBivariantGradingInternalMul_one_left_ofInvertible (p : ℕ) (hp : 1 ≤ p)
    (b : localizedBivariantGrading C (gysinSystemOfInvertible C) (f ≫ sX) sX f rfl p) :
    localizedBivariantGradingInternalMulHomOfInvertible C sX f p
        (localizedBivariantGradingOneOfInvertible C sX f p) b = b
```

**`Stacks.Chow.localizedBivariantGradingInternalMul_one_right_ofInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingAlgebra.lean, line 1207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingAlgebra.lean#L1207). The attribute's comment: “the unit law of the remark's graded algebra on A^(p)(Z ⟶ X) on the right for every p ≥ 1: the class 1 of A^0(X) placed in degree 0 is a right unit for the multiplication internal to A^(p)(Z ⟶ X), on all of A^(p)(Z ⟶ X), at the Gysin system of the first Chern class rule with NOTHING ASSUMED”.

> **Stacks 0FA0, the unit law of the graded algebra on `A⁽ᵖ⁾(Z ⟶ X)` on the right, for every
> `p ≥ 1`** at the Gysin system of the first Chern class rule, where nothing at all is assumed: the
> law holds on all of `A⁽ᵖ⁾(Z ⟶ X)`.

```lean
theorem localizedBivariantGradingInternalMul_one_right_ofInvertible (p : ℕ) (hp : 1 ≤ p)
    (b : localizedBivariantGrading C (gysinSystemOfInvertible C) (f ≫ sX) sX f rfl p) :
    localizedBivariantGradingInternalMulHomOfInvertible C sX f p b
        (localizedBivariantGradingOneOfInvertible C sX f p) = b
```

**`Stacks.Chow.localizedMulBivariantChow`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingMultiplication.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingMultiplication.lean#L246). The attribute's comment: “the pairing A^i(Z ⟶ X) × A^j(X) ⟶ A^\{i+j}(Z ⟶ X) of the remark, composition of bivariant classes”.

> The first of the three pairings: `A^i(Z ⟶ X) × A^j(X) ⟶ A^{i+j}(Z ⟶ X)`, composition of
> bivariant classes, read through the equality `f ≫ 𝟙 X = f`.

```lean
def localizedMulBivariantChow (i j : ℤ) (c : BivariantClass C G (f ≫ sX) sX f rfl i)
    (b : chowCohomologyComponent C G sX j) : BivariantClass C G (f ≫ sX) sX f rfl (i + j)
```

**`Stacks.Chow.localizedMulChowBivariant`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingMultiplication.lean, line 322](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingMultiplication.lean#L322). The attribute's comment: “the pairing A^i(X) × A^j(Z ⟶ X) ⟶ A^\{i+j}(Z ⟶ X) of the remark, the restriction A^i(X) ⟶ A^i(Z) of Stacks 0F9Z followed by composition”.

> The second of the three pairings: `A^i(X) × A^j(Z ⟶ X) ⟶ A^{i+j}(Z ⟶ X)`, the restriction
> `Stacks.Chow.chowCohomologyRestriction : A^i(X) ⟶ A^i(Z)` followed by the composition
> `A^i(Z) × A^j(Z ⟶ X) ⟶ A^{i+j}(Z ⟶ X)`.

```lean
def localizedMulChowBivariant (i j : ℤ) (a : chowCohomologyComponent C G sX i)
    (c : BivariantClass C G (f ≫ sX) sX f rfl j) :
    BivariantClass C G (f ≫ sX) sX f rfl (i + j)
```

**`Stacks.Chow.localizedMulBivariant`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingMultiplication.lean, line 359](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingMultiplication.lean#L359). The attribute's comment: “the pairing A^i(Z ⟶ X) × A^j(Z ⟶ X) ⟶ A^\{i+j}(Z ⟶ X) of the remark, (c, c') ↦ res(c) ∘ c' for the restriction res of Stacks 0F9Z”.

> The third of the three pairings: `A^i(Z ⟶ X) × A^j(Z ⟶ X) ⟶ A^{i+j}(Z ⟶ X)`, sending
> `(c, c')` to `res(c) ∘ c'` for the restriction
> `res = Stacks.Chow.closedImmersionChowCohomologyRestriction : A^i(Z ⟶ X) ⟶ A^i(Z)`.

```lean
def localizedMulBivariant (i j : ℤ) (c : BivariantClass C G (f ≫ sX) sX f rfl i)
    (c' : BivariantClass C G (f ≫ sX) sX f rfl j) :
    BivariantClass C G (f ≫ sX) sX f rfl (i + j)
```

**`Stacks.Chow.localizedBivariantGradingMul`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingMultiplication.lean, line 469](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingMultiplication.lean#L469). The attribute's comment: “the canonical multiplication A^(p)(Z ⟶ X) × A^(q)(Z ⟶ X) ⟶ A^(r)(Z ⟶ X) of the remark at every p, q and every target r, assembled degreewise from the three pairings and the pushforward of Stacks 0EPK; its associativity, which the source omits, is localizedBivariantGradingMul\_assoc”.

> The multiplication `A⁽ᵖ⁾(Z ⟶ X) × A⁽ᑫ⁾(Z ⟶ X) ⟶ A⁽ʳ⁾(Z ⟶ X)` attached to a closed immersion
> `f : Z ⟶ X` of schemes locally of finite type over the base, at every `p`, `q` and every target
> `r`. Its degree `n` component is the sum over `i ∈ Finset.Icc (min 0 n) (max 0 n)` of the
> products of the degree `i` component of the first factor with the degree `n - i` component of the
> second: for `n < r` the localized factors are pushed forward to `A^*(X)` and the product is taken
> in `A^*(X)` (`Stacks.Chow.localizedGradingMulAmbientTerm`), and for `n ≥ r` the term is the one of
> the three pairings `Stacks.Chow.localizedMulBivariantChow`,
> `Stacks.Chow.localizedMulChowBivariant`, `Stacks.Chow.localizedMulBivariant` that applies, and
> `0` on the pairs `i < p`, `n - i < q` (`Stacks.Chow.localizedGradingMulLocalizedTerm`).

```lean
def localizedBivariantGradingMul (p q r : ℕ)
    (a : localizedBivariantGrading C G (f ≫ sX) sX f rfl p)
    (b : localizedBivariantGrading C G (f ≫ sX) sX f rfl q) :
    localizedBivariantGrading C G (f ≫ sX) sX f rfl r
```

**`Stacks.Chow.localizedBivariantGradingMulMax`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingMultiplication.lean, line 482](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingMultiplication.lean#L482). The attribute's comment: “the multiplication A^(p)(Z ⟶ X) × A^(q)(Z ⟶ X) ⟶ A^(max(p,q))(Z ⟶ X) displayed in the remark, for every p and q”.

> The multiplication `A⁽ᵖ⁾(Z ⟶ X) × A⁽ᑫ⁾(Z ⟶ X) ⟶ A⁽ᵐᵃˣ⁽ᵖ⁼ᑫ⁾⁾(Z ⟶ X)`, for every `p` and `q`:
> `Stacks.Chow.localizedBivariantGradingMul` at `r = max(p, q)`.

```lean
def localizedBivariantGradingMulMax (p q : ℕ)
    (a : localizedBivariantGrading C G (f ≫ sX) sX f rfl p)
    (b : localizedBivariantGrading C G (f ≫ sX) sX f rfl q) :
    localizedBivariantGrading C G (f ≫ sX) sX f rfl (max p q)
```

**`Stacks.Chow.localizedBivariantGradingInternalMul`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingMultiplication.lean, line 493](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingMultiplication.lean#L493). The attribute's comment: “the multiplication internal to A^(p)(Z ⟶ X) of the remark's graded algebra, for every p ≥ 0; it is graded, and additive in each argument by localizedBivariantGradingMul\_add\_left and \_add\_right”.

> The multiplication internal to `A⁽ᵖ⁾(Z ⟶ X)`, for every `p ≥ 0`:
> `Stacks.Chow.localizedBivariantGradingMul` at `r = p = q`.

```lean
def localizedBivariantGradingInternalMul (p : ℕ)
    (a b : localizedBivariantGrading C G (f ≫ sX) sX f rfl p) :
    localizedBivariantGrading C G (f ≫ sX) sX f rfl p
```

**`Stacks.Chow.localizedBivariantGradingMul_fst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingMultiplication.lean, line 507](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingMultiplication.lean#L507). The attribute's comment: “the finite-convolution formula for the degree n part of a product in a degree n below the cutoff of the target: the sum over i + j = n of the products of the degree i and degree j parts of the factors, pushed into A^*(X) by Stacks 0EPK and multiplied there”.

> **The component formula below the cutoff of the target.** For `n < r`, the degree `n`
> component of a product is the finite convolution `∑ aᵢ · bₙ₋ᵢ` over
> `i ∈ Finset.Icc (min 0 n) (max 0 n)`, taken in `A^*(X)`
> (`Stacks.Chow.localizedGradingMulAmbientTerm`).

```lean
theorem localizedBivariantGradingMul_fst (p q r : ℕ)
    (a : localizedBivariantGrading C G (f ≫ sX) sX f rfl p)
    (b : localizedBivariantGrading C G (f ≫ sX) sX f rfl q) (n : {n : ℤ // n < (r : ℤ)}) :
    (localizedBivariantGradingMul C G sX f hRG hgysP hgys hgysc p q r a b).1 n =
      ∑ i ∈ Finset.Icc (min 0 n.1) (max 0 n.1),
        localizedGradingMulAmbientTerm C G sX f hRG hgysP hgys hgysc p q a b n.1 i
```

**`Stacks.Chow.localizedBivariantGradingMul_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingMultiplication.lean, line 522](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingMultiplication.lean#L522). The attribute's comment: “the finite-convolution formula for the degree n part of a product in a degree n at or above the cutoff of the target: the sum over i + j = n of the products of the degree i and degree j parts of the factors under the three pairings of the remark”.

> **The component formula from the cutoff of the target on.** For `n ≥ r`, the degree `n`
> component of a product is the finite convolution `∑ aᵢ · bₙ₋ᵢ` over
> `i ∈ Finset.Icc (min 0 n) (max 0 n)`, taken in `A^*(Z ⟶ X)`
> (`Stacks.Chow.localizedGradingMulLocalizedTerm`).

```lean
theorem localizedBivariantGradingMul_snd (p q r : ℕ)
    (a : localizedBivariantGrading C G (f ≫ sX) sX f rfl p)
    (b : localizedBivariantGrading C G (f ≫ sX) sX f rfl q) (n : {n : ℤ // (r : ℤ) ≤ n}) :
    (localizedBivariantGradingMul C G sX f hRG hgysP hgys hgysc p q r a b).2 n =
      ∑ i ∈ Finset.Icc (min 0 n.1) (max 0 n.1),
        localizedGradingMulLocalizedTerm C G sX f hgys hgysc p q a b n.1 i
```

**`Stacks.Chow.LocalizedGrading.IsMul.eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingMultiplication.lean, line 556](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingMultiplication.lean#L556). The attribute's comment: “uniqueness of the canonical multiplication: the two finite-convolution formulas determine it degreewise, so any two maps satisfying them are equal”.

> **Uniqueness of the multiplication.** Any two maps satisfying the two component formulas
> `Stacks.Chow.LocalizedGrading.IsMul` are equal; nothing else, not even additivity, is assumed of
> them.

```lean
theorem LocalizedGrading.IsMul.eq {p q r : ℕ}
    {M N : localizedBivariantGrading C G (f ≫ sX) sX f rfl p →
      localizedBivariantGrading C G (f ≫ sX) sX f rfl q →
      localizedBivariantGrading C G (f ≫ sX) sX f rfl r}
    (hM : LocalizedGrading.IsMul C G sX f hRG hgysP hgys hgysc p q r M)
    (hN : LocalizedGrading.IsMul C G sX f hRG hgysP hgys hgysc p q r N) : M = N
```

**`Stacks.Chow.localizedMulBivariantChowOfInvertible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingMultiplication.lean, line 943](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingMultiplication.lean#L943). The attribute's comment: “the pairing A^i(Z ⟶ X) × A^j(X) ⟶ A^\{i+j}(Z ⟶ X) of the remark, at the Gysin system of the first Chern class rule, with nothing assumed”.

> The first pairing `A^i(Z ⟶ X) × A^j(X) ⟶ A^{i+j}(Z ⟶ X)` at the Gysin system
> `Stacks.Chow.gysinSystemOfInvertible`, with no hypotheses.

```lean
def localizedMulBivariantChowOfInvertible (i j : ℤ)
    (c : BivariantClass C (gysinSystemOfInvertible C) (f ≫ sX) sX f rfl i)
    (b : chowCohomologyComponent C (gysinSystemOfInvertible C) sX j) :
    BivariantClass C (gysinSystemOfInvertible C) (f ≫ sX) sX f rfl (i + j)
```

**`Stacks.Chow.localizedMulChowBivariantOfInvertible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingMultiplication.lean, line 955](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingMultiplication.lean#L955). The attribute's comment: “the pairing A^i(X) × A^j(Z ⟶ X) ⟶ A^\{i+j}(Z ⟶ X) of the remark, at the Gysin system of the first Chern class rule, with nothing assumed”.

> The second pairing `A^i(X) × A^j(Z ⟶ X) ⟶ A^{i+j}(Z ⟶ X)` at the Gysin system
> `Stacks.Chow.gysinSystemOfInvertible`, with no hypotheses.

```lean
def localizedMulChowBivariantOfInvertible (i j : ℤ)
    (a : chowCohomologyComponent C (gysinSystemOfInvertible C) sX i)
    (c : BivariantClass C (gysinSystemOfInvertible C) (f ≫ sX) sX f rfl j) :
    BivariantClass C (gysinSystemOfInvertible C) (f ≫ sX) sX f rfl (i + j)
```

**`Stacks.Chow.localizedMulBivariantOfInvertible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingMultiplication.lean, line 967](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingMultiplication.lean#L967). The attribute's comment: “the pairing A^i(Z ⟶ X) × A^j(Z ⟶ X) ⟶ A^\{i+j}(Z ⟶ X) of the remark, at the Gysin system of the first Chern class rule, with nothing assumed”.

> The third pairing `A^i(Z ⟶ X) × A^j(Z ⟶ X) ⟶ A^{i+j}(Z ⟶ X)`, `(c, c') ↦ res(c) ∘ c'`, at the
> Gysin system `Stacks.Chow.gysinSystemOfInvertible`, with no hypotheses.

```lean
def localizedMulBivariantOfInvertible (i j : ℤ)
    (c : BivariantClass C (gysinSystemOfInvertible C) (f ≫ sX) sX f rfl i)
    (c' : BivariantClass C (gysinSystemOfInvertible C) (f ≫ sX) sX f rfl j) :
    BivariantClass C (gysinSystemOfInvertible C) (f ≫ sX) sX f rfl (i + j)
```

**`Stacks.Chow.localizedBivariantGradingMulOfInvertible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingMultiplication.lean, line 982](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingMultiplication.lean#L982). The attribute's comment: “the canonical multiplication A^(p)(Z ⟶ X) × A^(q)(Z ⟶ X) ⟶ A^(r)(Z ⟶ X) of the remark at every p, q and every target r, at the Gysin system of the first Chern class rule, with NOTHING ASSUMED: every Gysin compatibility is discharged there and Stacks 02RG on Chow groups, which the pushforward of Stacks 0EPK costs, is a theorem of this repository; its associativity, which the source omits, is localizedBivariantGradingMulOfInvertible\_assoc”.

> The multiplication `A⁽ᵖ⁾(Z ⟶ X) × A⁽ᑫ⁾(Z ⟶ X) ⟶ A⁽ʳ⁾(Z ⟶ X)`, at every `p`, `q` and every
> target `r`, at the Gysin system `Stacks.Chow.gysinSystemOfInvertible`, with no hypotheses.

```lean
def localizedBivariantGradingMulOfInvertible (p q r : ℕ)
    (a : localizedBivariantGrading C (gysinSystemOfInvertible C) (f ≫ sX) sX f rfl p)
    (b : localizedBivariantGrading C (gysinSystemOfInvertible C) (f ≫ sX) sX f rfl q) :
    localizedBivariantGrading C (gysinSystemOfInvertible C) (f ≫ sX) sX f rfl r
```

**`Stacks.Chow.localizedBivariantGradingMulMaxOfInvertible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingMultiplication.lean, line 997](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingMultiplication.lean#L997). The attribute's comment: “the multiplication A^(p)(Z ⟶ X) × A^(q)(Z ⟶ X) ⟶ A^(max(p,q))(Z ⟶ X) displayed in the remark, for every p and q, at the Gysin system of the first Chern class rule with nothing assumed”.

> The multiplication `A⁽ᵖ⁾(Z ⟶ X) × A⁽ᑫ⁾(Z ⟶ X) ⟶ A⁽ᵐᵃˣ⁽ᵖ⁼ᑫ⁾⁾(Z ⟶ X)`, for every `p` and `q`,
> at the Gysin system `Stacks.Chow.gysinSystemOfInvertible`, with no hypotheses.

```lean
def localizedBivariantGradingMulMaxOfInvertible (p q : ℕ)
    (a : localizedBivariantGrading C (gysinSystemOfInvertible C) (f ≫ sX) sX f rfl p)
    (b : localizedBivariantGrading C (gysinSystemOfInvertible C) (f ≫ sX) sX f rfl q) :
    localizedBivariantGrading C (gysinSystemOfInvertible C) (f ≫ sX) sX f rfl (max p q)
```

**`Stacks.Chow.localizedBivariantGradingInternalMulOfInvertible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingMultiplication.lean, line 1007](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingMultiplication.lean#L1007). The attribute's comment: “the multiplication internal to A^(p)(Z ⟶ X) of the remark's graded algebra for every p ≥ 0, at the Gysin system of the first Chern class rule with nothing assumed”.

> The multiplication internal to `A⁽ᵖ⁾(Z ⟶ X)`, for every `p ≥ 0`, at the Gysin system
> `Stacks.Chow.gysinSystemOfInvertible`, with no hypotheses.

```lean
def localizedBivariantGradingInternalMulOfInvertible (p : ℕ)
    (a b : localizedBivariantGrading C (gysinSystemOfInvertible C) (f ≫ sX) sX f rfl p) :
    localizedBivariantGrading C (gysinSystemOfInvertible C) (f ≫ sX) sX f rfl p
```

**`Stacks.Chow.localizedBivariantGradingMul_assoc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingProjectionFormula/Associativity.lean, line 479](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingProjectionFormula/Associativity.lean#L479). The attribute's comment: “associativity of the canonical multiplication A^(p)(Z ⟶ X) × A^(q)(Z ⟶ X) ⟶ A^(r)(Z ⟶ X) of the remark -- the verification the source omits -- for every triple of factors and every choice of intermediate targets r₁, r₂ and common target r with p + q + s ≤ r + 2, where every term of a triple product is one of the remark's three pairings; this covers the displayed target max(p,q) and the product internal to A^(p)(Z ⟶ X) of the graded algebra”.

> **Stacks 0FA0, associativity of the canonical multiplication**
> `A⁽ᵖ⁾(Z ⟶ X) × A⁽ᑫ⁾(Z ⟶ X) ⟶ A⁽ʳ⁾(Z ⟶ X)`: for `a ∈ A⁽ᵖ⁾(Z ⟶ X)`, `b ∈ A⁽ᑫ⁾(Z ⟶ X)`,
> `c ∈ A⁽ˢ⁾(Z ⟶ X)` the two groupings `(a · b) · c` and `a · (b · c)` of a triple product agree, at
> every pair of intermediate targets `A⁽ʳ¹⁾(Z ⟶ X)`, `A⁽ʳ²⁾(Z ⟶ X)` and every common target
> `A⁽ʳ⁾(Z ⟶ X)` whose cutoffs satisfy the four inequalities below, which together come to
> `p + q + s ≤ r + 2`. This is "the verification that these multiplications are associative in a
> suitable sense" that the source omits, carried out in the range where every term of every grouping
> is one of the source's own three pairings — no pair of degrees the remark leaves unprescribed
> occurs. That covers every product the chapter forms: `r₁ = max(p, q)`, the target the source
> displays (`Stacks.Chow.localizedBivariantGradingMulMax`), qualifies for `min(p, q) ≤ 1`, and so
> does `r₁ = p + q`, the target at which Stacks 0FAL and Stacks 0FAY state their products. The
> product internal to `A⁽ᵖ⁾(Z ⟶ X)` of the source's graded algebra, where all six targets are
> `p ≤ 1`, is the corollary `Stacks.Chow.localizedBivariantGradingInternalMul_assoc`; what
> associativity of that product would come to for `p ≥ 2` is
> `Stacks.Chow.localizedBivariantGradingInternalMul_singleLow_eq_zero_of_assoc`.
>
> It is an equality and not a heterogeneous equality because the common target `r` is a parameter;
> the degrees of the intermediate products are the arguments `r₁`, `r₂`, which the two groupings
> bracket differently. Degreewise the two sides are the same double convolution of the three
> factors' components written in the two decompositions `(m, i - m, n - i)` and `(m, j, n - m - j)`
> of the total degree `n`, and the proof is exactly the two pieces the implementation notes name:
> the reindexing `Stacks.Chow.sum_Icc_diag_flip` of that double convolution, and — term by term —
> the three instances of the associativity of Stacks 0B75 for the pairings, read through the
> transports the pairings carry by `Stacks.Chow.bivariantClassDegreeCongr_eq_of_heq`. Below the
> cutoff of the target both sides are the double convolution in `A^*(X)`
> (`Stacks.Chow.localizedBivariantGradingMul_isAmbientConvolution`) and the input is the
> associativity of the multiplication of `A^*(X)`,
> `Stacks.Chow.chowCohomologyComposite_assoc`; at or above it one of the three pairings applies to
> each term, and where an intermediate product was read in `A^*(X)` the comparison also needs
> `Stacks.Chow.localizedMulChowBivariant_localizedGradingPushforward_eq`, that a localized factor
> may be pushed forward by Stacks 0EPK before it is multiplied on the left.

```lean
theorem localizedBivariantGradingMul_assoc (p q s r₁ r₂ r : ℕ) (h₁ : p + q ≤ r₁ + 1)
    (h₂ : r₁ + s ≤ r + 1) (h₃ : q + s ≤ r₂ + 1) (h₄ : p + r₂ ≤ r + 1)
    (a : localizedBivariantGrading C G (f ≫ sX) sX f rfl p)
    (b : localizedBivariantGrading C G (f ≫ sX) sX f rfl q)
    (c : localizedBivariantGrading C G (f ≫ sX) sX f rfl s) :
    localizedBivariantGradingMul C G sX f hRG hgysP hgys hgysc r₁ s r
        (localizedBivariantGradingMul C G sX f hRG hgysP hgys hgysc p q r₁ a b) c =
      localizedBivariantGradingMul C G sX f hRG hgysP hgys hgysc p r₂ r a
        (localizedBivariantGradingMul C G sX f hRG hgysP hgys hgysc q s r₂ b c)
```

**`Stacks.Chow.localizedBivariantGradingInternalMul_assoc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingProjectionFormula/Associativity.lean, line 522](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingProjectionFormula/Associativity.lean#L522). The attribute's comment: “associativity of the multiplication internal to A^(p)(Z ⟶ X) of the remark's graded algebra, for p ≤ 1, where no pair of degrees the remark leaves unprescribed occurs in a triple product”.

> **Stacks 0FA0, associativity of the multiplication internal to `A⁽ᵖ⁾(Z ⟶ X)`**, which is the
> associativity the source's "`A⁽ᵖ⁾(Z ⟶ X)` canonically comes equipped with the structure of a
> graded algebra" asks for, for `p ≤ 1` — the `p` at which a triple product of the internal
> multiplication (`Stacks.Chow.localizedBivariantGradingInternalMul`, defined for every `p ≥ 0`)
> meets no pair of degrees the remark leaves unprescribed,
> `Stacks.Chow.localizedGrading_self_admissible_iff`. With
> `Stacks.Chow.localizedBivariantGradingMul_add_left`,
> `Stacks.Chow.localizedBivariantGradingMul_add_right` and the two unit laws
> `Stacks.Chow.localizedBivariantGradingInternalMul_one_left` and `_one_right` this completes the
> graded-algebra axioms for that product. For `p ≥ 2` the content of associativity is
> `Stacks.Chow.localizedBivariantGradingInternalMul_singleLow_eq_zero_of_assoc`.

```lean
theorem localizedBivariantGradingInternalMul_assoc (p : ℕ) (hp : p ≤ 1)
    (a b c : localizedBivariantGrading C G (f ≫ sX) sX f rfl p) :
    localizedBivariantGradingInternalMul C G sX f hRG hgysP hgys hgysc p
        (localizedBivariantGradingInternalMul C G sX f hRG hgysP hgys hgysc p a b) c =
      localizedBivariantGradingInternalMul C G sX f hRG hgysP hgys hgysc p a
        (localizedBivariantGradingInternalMul C G sX f hRG hgysP hgys hgysc p b c)
```

**`Stacks.Chow.localizedBivariantGradingSemigroup`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingProjectionFormula/Associativity.lean, line 560](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingProjectionFormula/Associativity.lean#L560). The attribute's comment: “the multiplicative structure of the remark's graded algebra on A^(p)(Z ⟶ X) as a bundled Semigroup, on all of A^(p)(Z ⟶ X) for p ≤ 1, where associativity of the internal product is proved: the multiplication of the remark together with its associativity, with no hypothesis beyond the Gysin compatibilities the product itself carries”.

> **Stacks 0FA0, the multiplicative structure of the remark's graded algebra on `A⁽ᵖ⁾(Z ⟶ X)`
> as a bundled `Semigroup`**, on all of `A⁽ᵖ⁾(Z ⟶ X)` for `p ≤ 1`, which is where associativity of
> the internal product is proved. Nothing beyond the Gysin compatibilities of the product itself is
> assumed: the multiplication is `Stacks.Chow.localizedBivariantGradingInternalMul`, which is defined
> for every `p ≥ 0`, and the associativity is
> `Stacks.Chow.localizedBivariantGradingInternalMul_assoc`.
>
> The unit of the algebra needs `p ≥ 1`, so the bundled `Monoid` is at `p = 1`:
> `Stacks.Chow.localizedBivariantGradingMonoid`.

```lean
def localizedBivariantGradingSemigroup (p : ℕ) (hp : p ≤ 1) :
    Semigroup (localizedBivariantGrading C G (f ≫ sX) sX f rfl p)
```

**`Stacks.Chow.localizedBivariantGradingMonoid`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingProjectionFormula/Associativity.lean, line 599](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingProjectionFormula/Associativity.lean#L599). The attribute's comment: “the remark's graded algebra on A^(1)(Z ⟶ X) as a bundled Monoid -- the multiplication internal to A^(1)(Z ⟶ X), the class 1 of A^0(X) in degree 0 as its unit, associativity and the two unit laws -- at p = 1, where the unit's degree 0 slot is A^0(X) and associativity is proved, on all of A^(1)(Z ⟶ X)”.

> **Stacks 0FA0, the remark's graded algebra on `A⁽¹⁾(Z ⟶ X)` as a bundled `Monoid`:** the
> multiplication internal to `A⁽¹⁾(Z ⟶ X)`, its unit, and the three laws. This is the structure the
> source's "`A⁽ᵖ⁾(Z ⟶ X)` canonically comes equipped with the structure of a graded algebra" asserts
> on the multiplicative side. Its fields are
> `Stacks.Chow.localizedBivariantGradingInternalMul`,
> `Stacks.Chow.localizedBivariantGradingOne`,
> `Stacks.Chow.localizedBivariantGradingInternalMul_assoc`,
> `Stacks.Chow.localizedBivariantGradingInternalMul_one_left` and
> `Stacks.Chow.localizedBivariantGradingInternalMul_one_right`; the additive side of the algebra is
> the `AddCommGroup` the grading carries, with the distributive law
> `Stacks.Chow.localizedBivariantGradingInternalMulHom`.
>
> `p = 1` is where the three laws meet. The multiplication internal to `A⁽ᵖ⁾(Z ⟶ X)` is defined for
> every `p ≥ 0` and the two unit laws hold for every `p ≥ 1`, the degree `0` slot where the unit sits
> being `A⁰(X)` exactly then; associativity is proved for `p ≤ 1`
> (`Stacks.Chow.localizedGrading_self_admissible_iff`), and what it would come to for `p ≥ 2` is
> `Stacks.Chow.localizedBivariantGradingInternalMul_singleLow_eq_zero_of_assoc`.
>
> The carrier is **all** of `A⁽¹⁾(Z ⟶ X)`, the group the source asserts the algebra on. That rests
> on the index range of the sums the product is formed from: a degree `n` component is the sum over
> `Finset.Icc (min 0 n) (max 0 n)`, the pairs `i + j = n` whose two degrees both have the sign of
> `n`, and that range contains `i = 0` and `i = n` in every degree
> (`Stacks.Chow.zero_mem_Icc_min_max`, `Stacks.Chow.self_mem_Icc_min_max`) — the two indices
> carrying the surviving term of a product with the unit on the left and on the right. The range is a
> reading of the source's `∑_{i + j = n}`, which runs over an infinite index set; the reading and the
> witness that the index set is infinite with independent summands are in the implementation notes of
> `StacksFrontier.AlgebraicGeometry.Chow.BivariantLemmas.LocalizedGradingMultiplication`.

```lean
def localizedBivariantGradingMonoid :
    Monoid (localizedBivariantGrading C G (f ≫ sX) sX f rfl 1)
```

**`Stacks.Chow.localizedBivariantGradingMulOfInvertible_assoc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingProjectionFormula/Associativity.lean, line 629](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingProjectionFormula/Associativity.lean#L629). The attribute's comment: “associativity of the canonical multiplication of the remark -- the verification the source omits -- at every choice of intermediate and common targets with p + q + s ≤ r + 2, at the Gysin system of the first Chern class rule, with NOTHING ASSUMED”.

> **Stacks 0FA0, associativity of the canonical multiplication at the Gysin system of the first
> Chern class rule, with nothing assumed:** there every Gysin compatibility that Stacks 0F9Z,
> Stacks 0B75 and Stacks 0EPK carry for an arbitrary Gysin system is a theorem, and so is Stacks
> 02RG on Chow groups, which the pushforward of Stacks 0EPK costs. See
> `Stacks.Chow.localizedBivariantGradingMul_assoc`.

```lean
theorem localizedBivariantGradingMulOfInvertible_assoc (p q s r₁ r₂ r : ℕ) (h₁ : p + q ≤ r₁ + 1)
    (h₂ : r₁ + s ≤ r + 1) (h₃ : q + s ≤ r₂ + 1) (h₄ : p + r₂ ≤ r + 1)
    (a : localizedBivariantGrading C (gysinSystemOfInvertible C) (f ≫ sX) sX f rfl p)
    (b : localizedBivariantGrading C (gysinSystemOfInvertible C) (f ≫ sX) sX f rfl q)
    (c : localizedBivariantGrading C (gysinSystemOfInvertible C) (f ≫ sX) sX f rfl s) :
    localizedBivariantGradingMulOfInvertible C sX f r₁ s r
        (localizedBivariantGradingMulOfInvertible C sX f p q r₁ a b) c =
      localizedBivariantGradingMulOfInvertible C sX f p r₂ r a
        (localizedBivariantGradingMulOfInvertible C sX f q s r₂ b c)
```

**`Stacks.Chow.localizedBivariantGradingInternalMulOfInvertible_assoc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingProjectionFormula/Associativity.lean, line 651](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedGradingProjectionFormula/Associativity.lean#L651). The attribute's comment: “associativity of the multiplication internal to A^(p)(Z ⟶ X) of the remark's graded algebra, for p ≤ 1, at the Gysin system of the first Chern class rule with NOTHING ASSUMED”.

> **Stacks 0FA0, associativity of the multiplication internal to `A⁽ᵖ⁾(Z ⟶ X)` at the Gysin
> system of the first Chern class rule, with nothing assumed.** This is the associativity of the
> source's graded algebra on `A⁽ᵖ⁾(Z ⟶ X)` for `p ≤ 1`, with no hypothesis of any kind beyond that
> bound.

```lean
theorem localizedBivariantGradingInternalMulOfInvertible_assoc (p : ℕ) (hp : p ≤ 1)
    (a b c : localizedBivariantGrading C (gysinSystemOfInvertible C) (f ≫ sX) sX f rfl p) :
    localizedBivariantGradingInternalMulOfInvertible C sX f p
        (localizedBivariantGradingInternalMulOfInvertible C sX f p a b) c =
      localizedBivariantGradingInternalMulOfInvertible C sX f p a
        (localizedBivariantGradingInternalMulOfInvertible C sX f p b c)
```

## Tag 0FA1, a remark

[Tag 0FA1](https://stacks.math.columbia.edu/tag/0FA1) in the Stacks Project.

**`Stacks.Chow.bivariantRestrictionCap_id_eq_cap_properChowPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomology.lean, line 305](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomology.lean#L305).

> **Stacks 0FA1.** For a closed immersion `i : Z ⟶ X` of schemes locally of finite type over
> the base and a bivariant class `c` of degree `p` for `i`, the restriction `res(c)` of `c` along
> `i` — a class of degree `p` for `Z ×_X Z ⟶ Z`, whose cap operation at the test scheme `𝟙 Z` is
> read on `Z` through the canonical identification `(Z ×_X Z) ×_Z Z ≅ Z` — satisfies
>
>   `res(c) ∩ α = c ∩ i_*α`
>
> in `CH_{k-p}(Z)` for every `α ∈ CH_k(Z)`, the right-hand side being read on `Z` through the
> canonical identification `X ×_X Z ≅ Z`.

```lean
theorem bivariantRestrictionCap_id_eq_cap_properChowPushforward
    (c : BivariantClass C G sZ sX i hi p) (k : ℤ)
    (hfac : ProperPushforwardFactorsThroughRationalEquivalence C sZ sX i hi k)
    (α : chowGroup C sZ k) :
    chowPushforwardOfIso C (pullback.fst (pullback.snd i i) (𝟙 Z) ≫ (pullback.fst i i ≫ sZ)) sZ
        (selfPullbackIdIso i).inv (selfPullbackIdIso_inv_comp i sZ) (k - p)
        (bivariantRestrictionCap C G sZ sX i hi i p c (𝟙 Z) k
          (chowGroupCongr C (id_comp_comp_structureMorphism_eq C sZ sX i hi) k α)) =
      chowPushforwardOfIso C (pullback.fst i (𝟙 X) ≫ sZ) sZ (pullbackIdIso i).inv
        (pullbackIdIso_inv_comp i sZ) (k - p)
        (c.cap (𝟙 X) k (chowGroupCongr C (Category.id_comp sX).symm k
          (properChowPushforward C sZ sX i hi k hfac α)))
```

**`Stacks.Chow.bivariantRestriction_cap_id_eq_cap_properChowPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomology.lean, line 386](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomology.lean#L386). The attribute's comment: “for the restricted bivariant class”.

> **Stacks 0FA1** for the restricted class itself: the bivariant class
> `Stacks.Chow.bivariantRestriction` of `c` along the closed immersion `i`, read at the test scheme
> `𝟙 Z`, satisfies `res(c) ∩ α = c ∩ i_*α` in `CH_{k-p}(Z)`.

```lean
theorem bivariantRestriction_cap_id_eq_cap_properChowPushforward
    (hgys : G.IsNaturalUnderBaseChangeIso) (c : BivariantClass C G sZ sX i hi p) (k : ℤ)
    (hfac : ProperPushforwardFactorsThroughRationalEquivalence C sZ sX i hi k)
    (α : chowGroup C sZ k) :
    chowPushforwardOfIso C (pullback.fst (pullback.snd i i) (𝟙 Z) ≫ (pullback.fst i i ≫ sZ)) sZ
        (selfPullbackIdIso i).inv (selfPullbackIdIso_inv_comp i sZ) (k - p)
        ((bivariantRestriction C G sZ sX i hi i p hgys c).cap (𝟙 Z) k
          (chowGroupCongr C (id_comp_comp_structureMorphism_eq C sZ sX i hi) k α)) =
      chowPushforwardOfIso C (pullback.fst i (𝟙 X) ≫ sZ) sZ (pullbackIdIso i).inv
        (pullbackIdIso_inv_comp i sZ) (k - p)
        (c.cap (𝟙 X) k (chowGroupCongr C (Category.id_comp sX).symm k
          (properChowPushforward C sZ sX i hi k hfac α)))
```

**`Stacks.Chow.closedImmersionChowCohomologyRestriction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomology.lean, line 404](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomology.lean#L404). The attribute's comment: “the restriction map to A^p(Z)”.

> **Stacks 0FA1.** The restriction map `res : A^p(Z ⟶ X) ⟶ A^p(Z)` along a closed immersion
> `i : Z ⟶ X`, a homomorphism of groups: the restriction map of Stacks 0F9Z along `i`, followed by
> the transport of a bivariant class along the canonical isomorphism `Z ×_X Z ≅ Z`.

```lean
def closedImmersionChowCohomologyRestriction (hgys : G.IsNaturalUnderBaseChangeIso) :
    BivariantClass C G sZ sX i hi p →+ chowCohomologyComponent C G (i ≫ sX) p
```

**`Stacks.Chow.closedImmersionChowCohomologyRestriction_cap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomology.lean, line 424](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomology.lean#L424). The attribute's comment: “the cap formula for the restriction map to A^p(Z)”.

> **Stacks 0FA1.** The restriction map `res : A^p(Z ⟶ X) ⟶ A^p(Z)` of a closed immersion
> satisfies `res(c) ∩ α = c ∩ i_*α` in `CH_{k-p}(Z)` for every `α ∈ CH_k(Z)`, both sides being read
> on `Z` through the canonical identifications `Z ×_Z Z ≅ Z` and `X ×_X Z ≅ Z`.

```lean
theorem closedImmersionChowCohomologyRestriction_cap (hgys : G.IsNaturalUnderBaseChangeIso)
    (c : BivariantClass C G sZ sX i hi p) (k : ℤ)
    (hfac : ProperPushforwardFactorsThroughRationalEquivalence C sZ sX i hi k)
    (α : chowGroup C sZ k) :
    chowPushforwardOfIso C (pullback.fst (𝟙 Z) (𝟙 Z) ≫ (i ≫ sX)) sZ
        (identityBaseChangeIso (𝟙 Z)).hom
        (identityBaseChangeIso_id_comp_base C sZ sX i hi) (k - p)
        ((closedImmersionChowCohomologyRestriction C G sZ sX i hi p hgys c).cap (𝟙 Z) k
          (chowGroupCongr C (id_comp_comp_structureMorphism_eq C sZ sX i hi) k α)) =
      chowPushforwardOfIso C (pullback.fst i (𝟙 X) ≫ sZ) sZ (pullbackIdIso i).inv
        (pullbackIdIso_inv_comp i sZ) (k - p)
        (c.cap (𝟙 X) k (chowGroupCongr C (Category.id_comp sX).symm k
          (properChowPushforward C sZ sX i hi k hfac α)))
```

**`Stacks.Chow.bivariantRestrictionCap_id_eq_cap_properChowPushforward_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyOfInvertible.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyOfInvertible.lean#L68).

> For a Gysin system `G`, a closed immersion `i : Z ⟶ X` of schemes locally of finite type over
> the base and a bivariant class `c` of degree `p` for `i`, the restriction `res(c)` of `c` along
> `i`, read at the test scheme `𝟙 Z`, satisfies
>
>   `res(c) ∩ α = c ∩ i_*α`
>
> in `CH_{k-p}(Z)` for every `α ∈ CH_k(Z)`.

```lean
theorem bivariantRestrictionCap_id_eq_cap_properChowPushforward_unconditional
    (c : BivariantClass C G sZ sX i hi p) (k : ℤ) (α : chowGroup C sZ k) :
    chowPushforwardOfIso C (pullback.fst (pullback.snd i i) (𝟙 Z) ≫ (pullback.fst i i ≫ sZ)) sZ
        (selfPullbackIdIso i).inv (selfPullbackIdIso_inv_comp i sZ) (k - p)
        (bivariantRestrictionCap C G sZ sX i hi i p c (𝟙 Z) k
          (chowGroupCongr C (id_comp_comp_structureMorphism_eq C sZ sX i hi) k α)) =
      chowPushforwardOfIso C (pullback.fst i (𝟙 X) ≫ sZ) sZ (pullbackIdIso i).inv
        (pullbackIdIso_inv_comp i sZ) (k - p)
        (c.cap (𝟙 X) k (chowGroupCongr C (Category.id_comp sX).symm k
          (properChowPushforward C sZ sX i hi k
            (properPushforwardFactorsThroughRationalEquivalence C sZ sX i hi k) α)))
```

**`Stacks.Chow.bivariantRestrictionOfInvertible_cap_id_eq_cap_properChowPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyOfInvertible.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyOfInvertible.lean#L97). The attribute's comment: “for the restricted bivariant class, at the Gysin system of the first Chern class rule, with the isomorphism case of Stacks 02TA discharged”.

> At the Gysin system of the first Chern class rule of an invertible module, the restriction
> `res(c)` of Stacks 0F9Z of a bivariant class `c` of degree `p` for the closed immersion `i : Z ⟶ X`
> — a class for `Z ×_X Z ⟶ Z`, read at the test scheme `𝟙 Z` — satisfies
>
>   `res(c) ∩ α = c ∩ i_*α`
>
> in `CH_{k-p}(Z)` for every `α ∈ CH_k(Z)`.

```lean
theorem bivariantRestrictionOfInvertible_cap_id_eq_cap_properChowPushforward
    (c : BivariantClass C (gysinSystemOfInvertible C) sZ sX i hi p) (k : ℤ)
    (α : chowGroup C sZ k) :
    chowPushforwardOfIso C (pullback.fst (pullback.snd i i) (𝟙 Z) ≫ (pullback.fst i i ≫ sZ)) sZ
        (selfPullbackIdIso i).inv (selfPullbackIdIso_inv_comp i sZ) (k - p)
        ((bivariantRestriction C (gysinSystemOfInvertible C) sZ sX i hi i p
            (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso C) c).cap (𝟙 Z) k
          (chowGroupCongr C (id_comp_comp_structureMorphism_eq C sZ sX i hi) k α)) =
      chowPushforwardOfIso C (pullback.fst i (𝟙 X) ≫ sZ) sZ (pullbackIdIso i).inv
        (pullbackIdIso_inv_comp i sZ) (k - p)
        (c.cap (𝟙 X) k (chowGroupCongr C (Category.id_comp sX).symm k
          (properChowPushforward C sZ sX i hi k
            (properPushforwardFactorsThroughRationalEquivalence C sZ sX i hi k) α)))
```

**`Stacks.Chow.closedImmersionChowCohomologyRestrictionOfInvertible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyOfInvertible.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyOfInvertible.lean#L118). The attribute's comment: “the restriction map to A^p(Z), at the Gysin system of the first Chern class rule, with the isomorphism case of Stacks 02TA discharged”.

> The restriction map `res : A^p(Z ⟶ X) ⟶ A^p(Z)` along a closed immersion `i : Z ⟶ X`, as a
> group homomorphism, at the Gysin system of the first Chern class rule of an invertible module.

```lean
def closedImmersionChowCohomologyRestrictionOfInvertible :
    BivariantClass C (gysinSystemOfInvertible C) sZ sX i hi p →+
      chowCohomologyComponent C (gysinSystemOfInvertible C) (i ≫ sX) p
```

**`Stacks.Chow.closedImmersionChowCohomologyRestrictionOfInvertible_cap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyOfInvertible.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyOfInvertible.lean#L133). The attribute's comment: “the cap formula for the restriction map to A^p(Z), at the Gysin system of the first Chern class rule, with the isomorphism case of Stacks 02TA discharged”.

> At the Gysin system of the first Chern class rule of an invertible module, the restriction map
> `res : A^p(Z ⟶ X) ⟶ A^p(Z)` of a closed immersion `i : Z ⟶ X` satisfies
>
>   `res(c) ∩ α = c ∩ i_*α`
>
> in `CH_{k-p}(Z)` for every `α ∈ CH_k(Z)`, both sides being read on `Z` through the canonical
> identifications `Z ×_Z Z ≅ Z` and `X ×_X Z ≅ Z`.

```lean
theorem closedImmersionChowCohomologyRestrictionOfInvertible_cap
    (c : BivariantClass C (gysinSystemOfInvertible C) sZ sX i hi p) (k : ℤ)
    (α : chowGroup C sZ k) :
    chowPushforwardOfIso C (pullback.fst (𝟙 Z) (𝟙 Z) ≫ (i ≫ sX)) sZ
        (identityBaseChangeIso (𝟙 Z)).hom
        (identityBaseChangeIso_id_comp_base C sZ sX i hi) (k - p)
        ((closedImmersionChowCohomologyRestrictionOfInvertible C sZ sX i hi p c).cap (𝟙 Z) k
          (chowGroupCongr C (id_comp_comp_structureMorphism_eq C sZ sX i hi) k α)) =
      chowPushforwardOfIso C (pullback.fst i (𝟙 X) ≫ sZ) sZ (pullbackIdIso i).inv
        (pullbackIdIso_inv_comp i sZ) (k - p)
        (c.cap (𝟙 X) k (chowGroupCongr C (Category.id_comp sX).symm k
          (properChowPushforward C sZ sX i hi k
            (properPushforwardFactorsThroughRationalEquivalence C sZ sX i hi k) α)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.34, Tag 0FDV](https://stacks.math.columbia.edu/tag/0FDV)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
