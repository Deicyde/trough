---
declaration: section
origin: cited
lean: Stacks.Chow.bivariantComposite_assoc, Stacks.Chow.bivariantCompositeBilinear_assoc, Stacks.Chow.bivariantComposite_add_left', Stacks.Chow.bivariantComposite_add_right', Stacks.Chow.bivariantComposite_neg_left, Stacks.Chow.bivariantComposite_neg_right, Stacks.Chow.bivariantComposite_zero_left, Stacks.Chow.bivariantComposite_zero_right
statement: formalized
proof: formalized
---

# 42.33 Bivariant intersection theory

Section 42.33 of the Stacks Project, [Tag 0B75](https://stacks.math.columbia.edu/tag/0B75). 9 tags here are carried by 82 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0B75, the section

[Tag 0B75](https://stacks.math.columbia.edu/tag/0B75) in the Stacks Project.

**`Stacks.Chow.bivariantComposite_assoc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/Associativity.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/Associativity.lean#L188). The attribute's comment: “the composition of bivariant classes is associative: for a ∈ A^p(X ⟶ Y), b ∈ A^q(Y ⟶ Z) and c ∈ A^r(Z ⟶ W) the triple composites (a ∘ b) ∘ c and a ∘ (b ∘ c) agree in A^\{p+q+r}(X ⟶ W), the degrees (p + q) + r and p + (q + r) being the same integer written two ways”.

> The composition of bivariant classes is associative: for `a ∈ A^p(X ⟶ Y)`, `b ∈ A^q(Y ⟶ Z)`
> and `c ∈ A^r(Z ⟶ W)` the two triple composites `(a ∘ b) ∘ c` and `a ∘ (b ∘ c)` agree in
> `A^{p+q+r}(X ⟶ W)`, the equality being heterogeneous because the two sides are indexed by
> `(p + q) + r` and `p + (q + r)` [Stacks, Tag 0B75].

```lean
theorem bivariantComposite_assoc (hgys : G.IsNaturalUnderBaseChangeIso)
    (hgysc : G.IsNaturalUnderPullbackCompPushforward) :
    bivariantComposite C G sX sZ sW (f ≫ g) h (comp_comp_structureMorphism_eq hf hg) hh (p + q) r
        (bivariantComposite C G sX sY sZ f g hf hg p q a b hgys hgysc) c hgys hgysc ≍
      bivariantComposite C G sX sY sW f (g ≫ h) hf (comp_comp_structureMorphism_eq hg hh) p
        (q + r) a (bivariantComposite C G sY sZ sW g h hg hh q r b c hgys hgysc) hgys hgysc
```

**`Stacks.Chow.bivariantCompositeBilinear_assoc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/Associativity.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/Associativity.lean#L203). The attribute's comment: “the bilinear composition A^p(X ⟶ Y) × A^q(Y ⟶ Z) ⟶ A^\{p+q}(X ⟶ Z) is associative”.

> Associativity of the composition, read on the bilinear map
> `Stacks.Chow.bivariantCompositeBilinear` that bundles it [Stacks, Tag 0B75].

```lean
theorem bivariantCompositeBilinear_assoc (hgys : G.IsNaturalUnderBaseChangeIso)
    (hgysc : G.IsNaturalUnderPullbackCompPushforward) :
    bivariantCompositeBilinear C G sX sZ sW (f ≫ g) h (comp_comp_structureMorphism_eq hf hg) hh
          (p + q) r hgys hgysc
        (bivariantCompositeBilinear C G sX sY sZ f g hf hg p q hgys hgysc a b) c ≍
      bivariantCompositeBilinear C G sX sY sW f (g ≫ h) hf
        (comp_comp_structureMorphism_eq hg hh) p (q + r) hgys hgysc a
        (bivariantCompositeBilinear C G sY sZ sW g h hg hh q r hgys hgysc b c)
```

**`Stacks.Chow.bivariantComposite_add_left'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/Bilinearity.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/Bilinearity.lean#L56). The attribute's comment: “the bilinearity of the composition, additivity in the first argument”.

> Additivity of the composition in the first argument: `(a + a') ∘ b = a ∘ b + a' ∘ b`.

```lean
theorem bivariantComposite_add_left' (a a' : BivariantClass C G sX sY f hf p)
    (b : BivariantClass C G sY sZ g hg q) :
    bivariantComposite C G sX sY sZ f g hf hg p q (a + a') b hgys hgysc =
      bivariantComposite C G sX sY sZ f g hf hg p q a b hgys hgysc +
        bivariantComposite C G sX sY sZ f g hf hg p q a' b hgys hgysc
```

**`Stacks.Chow.bivariantComposite_add_right'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/Bilinearity.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/Bilinearity.lean#L70). The attribute's comment: “the bilinearity of the composition, additivity in the second argument”.

> Additivity of the composition in the second argument: `a ∘ (b + b') = a ∘ b + a ∘ b'`.

```lean
theorem bivariantComposite_add_right' (a : BivariantClass C G sX sY f hf p)
    (b b' : BivariantClass C G sY sZ g hg q) :
    bivariantComposite C G sX sY sZ f g hf hg p q a (b + b') hgys hgysc =
      bivariantComposite C G sX sY sZ f g hf hg p q a b hgys hgysc +
        bivariantComposite C G sX sY sZ f g hf hg p q a b' hgys hgysc
```

**`Stacks.Chow.bivariantComposite_neg_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/Bilinearity.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/Bilinearity.lean#L84). The attribute's comment: “the bilinearity of the composition, negation in the first argument”.

> The composition negates in its first argument: `(-a) ∘ b = -(a ∘ b)`.

```lean
theorem bivariantComposite_neg_left (a : BivariantClass C G sX sY f hf p)
    (b : BivariantClass C G sY sZ g hg q) :
    bivariantComposite C G sX sY sZ f g hf hg p q (-a) b hgys hgysc =
      -bivariantComposite C G sX sY sZ f g hf hg p q a b hgys hgysc
```

**`Stacks.Chow.bivariantComposite_neg_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/Bilinearity.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/Bilinearity.lean#L95). The attribute's comment: “the bilinearity of the composition, negation in the second argument”.

> The composition negates in its second argument: `a ∘ (-b) = -(a ∘ b)`.

```lean
theorem bivariantComposite_neg_right (a : BivariantClass C G sX sY f hf p)
    (b : BivariantClass C G sY sZ g hg q) :
    bivariantComposite C G sX sY sZ f g hf hg p q a (-b) hgys hgysc =
      -bivariantComposite C G sX sY sZ f g hf hg p q a b hgys hgysc
```

**`Stacks.Chow.bivariantComposite_zero_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/Bilinearity.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/Bilinearity.lean#L106). The attribute's comment: “the bilinearity of the composition, the zero class on the left”.

> The composite of the zero class with any class is zero.

```lean
theorem bivariantComposite_zero_left (b : BivariantClass C G sY sZ g hg q) :
    bivariantComposite C G sX sY sZ f g hf hg p q 0 b hgys hgysc = 0
```

**`Stacks.Chow.bivariantComposite_zero_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/Bilinearity.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/Bilinearity.lean#L114). The attribute's comment: “the bilinearity of the composition, the zero class on the right”.

> The composite of any class with the zero class is zero.

```lean
theorem bivariantComposite_zero_right (a : BivariantClass C G sX sY f hf p) :
    bivariantComposite C G sX sY sZ f g hf hg p q a 0 hgys hgysc = 0
```

**`Stacks.Chow.bivariantCompositeAddHomLeft`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/Bilinearity.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/Bilinearity.lean#L124). The attribute's comment: “the bilinearity of the composition: the partial map in the first argument as a homomorphism of groups”.

> Composition with a fixed class `b ∈ A^q(Y ⟶ Z)` on the right, as a homomorphism
> `A^p(X ⟶ Y) ⟶ A^{p+q}(X ⟶ Z)` of groups.

```lean
def bivariantCompositeAddHomLeft (b : BivariantClass C G sY sZ g hg q) :
    BivariantClass C G sX sY f hf p →+
      BivariantClass C G sX sZ (f ≫ g) (comp_comp_structureMorphism_eq hf hg) (p + q)
```

**`Stacks.Chow.bivariantCompositeAddHomRight`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/Bilinearity.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/Bilinearity.lean#L135). The attribute's comment: “the bilinearity of the composition: the partial map in the second argument as a homomorphism of groups”.

> Composition with a fixed class `a ∈ A^p(X ⟶ Y)` on the left, as a homomorphism
> `A^q(Y ⟶ Z) ⟶ A^{p+q}(X ⟶ Z)` of groups.

```lean
def bivariantCompositeAddHomRight (a : BivariantClass C G sX sY f hf p) :
    BivariantClass C G sY sZ g hg q →+
      BivariantClass C G sX sZ (f ≫ g) (comp_comp_structureMorphism_eq hf hg) (p + q)
```

**`Stacks.Chow.bivariantComposite`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/Class.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/Class.lean#L134). The attribute's comment: “the composite bivariant class, assembled from its cap operation and the three naturality conditions of Stacks 0B76”.

> The composite `a ∘ b ∈ A^{p+q}(X ⟶ Z)` of bivariant classes `a ∈ A^p(X ⟶ Y)` and
> `b ∈ A^q(Y ⟶ Z)`: the bivariant class of degree `p + q` for `f ≫ g` whose cap operation is
> `α ↦ a ∩ (b ∩ α)`, that is, `Stacks.Chow.bivariantCompositeCap` read through the transport of Chow
> groups along `k - q - p = k - (p + q)` [Stacks, Tag 0B75].

```lean
def bivariantComposite (hgys : G.IsNaturalUnderBaseChangeIso)
    (hgysc : G.IsNaturalUnderPullbackCompPushforward) :
    BivariantClass C G sX sZ (f ≫ g) (comp_comp_structureMorphism_eq hf hg) (p + q)
```

**`Stacks.Chow.bivariantCompositeBilinear`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/Class.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/Class.lean#L260). The attribute's comment: “the composition of bivariant classes is bilinear”.

> The composition `A^p(X ⟶ Y) × A^q(Y ⟶ Z) ⟶ A^{p+q}(X ⟶ Z)` as a bilinear map, that is,
> `Stacks.Chow.bivariantComposite` bundled through its additivity in each argument
> [Stacks, Tag 0B75].

```lean
def bivariantCompositeBilinear (hgys : G.IsNaturalUnderBaseChangeIso)
    (hgysc : G.IsNaturalUnderPullbackCompPushforward) :
    BivariantClass C G sX sY f hf p →+
      BivariantClass C G sY sZ g hg q →+
        BivariantClass C G sX sZ (f ≫ g) (comp_comp_structureMorphism_eq hf hg) (p + q)
```

**`Stacks.Chow.bivariantCompositeOfInvertible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/GysinSystemOfInvertible.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/GysinSystemOfInvertible.lean#L157). The attribute's comment: “the composite bivariant class at the Gysin system of the first Chern class rule, with both cases of Stacks 02TA discharged”.

> The composite `a ∘ b ∈ A^{p+q}(X ⟶ Z)` of bivariant classes at the Gysin system of the first
> Chern class rule of an invertible module.

```lean
def bivariantCompositeOfInvertible
    (a : BivariantClass C (gysinSystemOfInvertible C) sX sY f hf p)
    (b : BivariantClass C (gysinSystemOfInvertible C) sY sZ g hg q) :
    BivariantClass C (gysinSystemOfInvertible C) sX sZ (f ≫ g)
      (comp_comp_structureMorphism_eq hf hg) (p + q)
```

**`Stacks.Chow.bivariantCompositeBilinearOfInvertible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/GysinSystemOfInvertible.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/GysinSystemOfInvertible.lean#L170). The attribute's comment: “the composition as a bilinear map, at the Gysin system of the first Chern class rule, with both cases of Stacks 02TA discharged”.

> The composition `A^p(X ⟶ Y) × A^q(Y ⟶ Z) ⟶ A^{p+q}(X ⟶ Z)` of bivariant classes as a bilinear
> map, at the Gysin system of the first Chern class rule.

```lean
def bivariantCompositeBilinearOfInvertible :
    BivariantClass C (gysinSystemOfInvertible C) sX sY f hf p →+
      BivariantClass C (gysinSystemOfInvertible C) sY sZ g hg q →+
        BivariantClass C (gysinSystemOfInvertible C) sX sZ (f ≫ g)
          (comp_comp_structureMorphism_eq hf hg) (p + q)
```

**`Stacks.Chow.bivariantCompositeCap_proper_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/Naturality.lean, line 597](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/Naturality.lean#L597). The attribute's comment: “the proper-pushforward condition of the composite”.

> The proper-pushforward condition of Stacks 0B76 for the composite of two bivariant classes:
> the cap operation `α ↦ a ∩ (b ∩ α)` commutes with proper pushforward along a morphism of test
> schemes. The condition for `b` moves the pushforward past the inner cap and onto the middle base
> change `T' ×_Z Y ⟶ T ×_Z Y`, and the outer cap operation's condition moves it past the outer
> cap.

```lean
theorem bivariantCompositeCap_proper_naturality {T T' : Scheme.{u}} (t : T ⟶ Z)
    [LocallyOfFiniteType t] (h : T' ⟶ T) [IsProper h]
    (h' : pullback (f ≫ g) (h ≫ t) ⟶ pullback (f ≫ g) t)
    (sq : IsPullback (pullback.snd (f ≫ g) (h ≫ t)) h' h (pullback.snd (f ≫ g) t))
    (hfst : h' ≫ pullback.fst (f ≫ g) t = pullback.fst (f ≫ g) (h ≫ t)) (k : ℤ)
    (α : chowGroup C ((h ≫ t) ≫ sZ) k) :
    letI : IsProper h' := MorphismProperty.of_isPullback sq (P := @IsProper) inferInstance
    bivariantCompositeCap C G sX sY sZ f g hf hg hpp p q a b t k
        (properChowPushforward C ((h ≫ t) ≫ sZ) (t ≫ sZ) h (by simp [Category.assoc]) k
          (hpp _ _ _ _ _) α) =
      properChowPushforward C (pullback.fst (f ≫ g) (h ≫ t) ≫ sX)
        (pullback.fst (f ≫ g) t ≫ sX) h' (by rw [← Category.assoc, hfst]) (k - q - p)
        (hpp _ _ _ _ _)
        (bivariantCompositeCap C G sX sY sZ f g hf hg hpp p q a b (h ≫ t) k α)
```

Declarations registered for the tag:

- [`Stacks.Chow.instAddCommGroupBivariantClass`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Stacks.Chow.instAddCommGroupBivariantClass#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/Naturality.lean, line 773](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/Naturality.lean#L773) (StacksFrontier): “the abelian group of bivariant classes”.

## Tag 0B76, a definition

[Tag 0B76](https://stacks.math.columbia.edu/tag/0B76) in the Stacks Project.

**`Stacks.Chow.BivariantClass`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Basic.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Basic.lean#L250). The attribute's comment: “the group A^p(X ⟶ Y) of bivariant classes of degree p for f, stated against a GysinSystem supplying the first Chern class rule of Stacks 02SO and the vanishing of Stacks 02TO”.

> **Stacks 0B76.** A bivariant class of degree `p` for `f : X ⟶ Y`: a rule assigning to every
> morphism `g : T ⟶ Y` locally of finite type and every `k` an additive map
> `A_k(T) ⟶ A_{k-p}(T ×_Y X)`, natural for proper pushforward, for flat pullback of fixed relative
> dimension, and for the Gysin map of the zero scheme of a section of an invertible module. The
> group of all of them is denoted `A^p(X ⟶ Y)`.
>
> Stated against a `Stacks.Chow.GysinSystem`, which supplies the first Chern class rule of Stacks
> 02SO and the vanishing of Stacks 02TO; see the module docstring.

```lean
structure BivariantClass (C : ChowSituation.{u}) (G : GysinSystem C) {X Y : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY]
    (f : X ⟶ Y) [LocallyOfFiniteType f] (hf : f ≫ sY = sX) (p : ℤ)
```

**`Stacks.Chow.BivariantClass.ext`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Basic.lean, line 411](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Basic.lean#L411). The attribute's comment: “extensionality: a bivariant class is determined by its cap operations”.

> **Stacks 0B76.** Two bivariant classes agree as soon as all their cap operations agree.

```lean
theorem BivariantClass.ext {c d : BivariantClass C G sX sY f hf p}
    (h : ∀ {T : Scheme.{u}} (g : T ⟶ Y) [LocallyOfFiniteType g] (k : ℤ)
      (α : chowGroup C (g ≫ sY) k), c.cap g k α = d.cap g k α) : c = d
```

**`Stacks.Chow.BivariantClass.zero_cap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Basic.lean, line 534](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Basic.lean#L534). The attribute's comment: “the zero of the group A^p(X ⟶ Y)”.

> **Stacks 0B76.** The zero bivariant class caps to zero.

```lean
theorem BivariantClass.zero_cap {T : Scheme.{u}} (g : T ⟶ Y) [LocallyOfFiniteType g] (k : ℤ)
    (α : chowGroup C (g ≫ sY) k) :
    (0 : BivariantClass C G sX sY f hf p).cap g k α = 0
```

**`Stacks.Chow.BivariantClass.add_cap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Basic.lean, line 541](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Basic.lean#L541). The attribute's comment: “addition in A^p(X ⟶ Y) is pointwise on cap products”.

> **Stacks 0B76.** A sum of bivariant classes caps to the sum of their cap products.

```lean
theorem BivariantClass.add_cap (c d : BivariantClass C G sX sY f hf p) {T : Scheme.{u}}
    (g : T ⟶ Y) [LocallyOfFiniteType g] (k : ℤ) (α : chowGroup C (g ≫ sY) k) :
    (c + d).cap g k α = c.cap g k α + d.cap g k α
```

**`Stacks.Chow.BivariantClass.neg_cap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Basic.lean, line 548](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Basic.lean#L548). The attribute's comment: “negation in A^p(X ⟶ Y) is pointwise on cap products”.

> **Stacks 0B76.** A negated bivariant class caps to the negated cap product.

```lean
theorem BivariantClass.neg_cap (c : BivariantClass C G sX sY f hf p) {T : Scheme.{u}}
    (g : T ⟶ Y) [LocallyOfFiniteType g] (k : ℤ) (α : chowGroup C (g ≫ sY) k) :
    (-c).cap g k α = -c.cap g k α
```

**`Stacks.Chow.BivariantClass.sub_cap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Basic.lean, line 598](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Basic.lean#L598). The attribute's comment: “subtraction in A^p(X ⟶ Y) is pointwise on cap products”.

> **Stacks 0B76.** A difference of bivariant classes caps to the difference of their cap
> products.

```lean
theorem BivariantClass.sub_cap (c d : BivariantClass C G sX sY f hf p) {T : Scheme.{u}}
    (g : T ⟶ Y) [LocallyOfFiniteType g] (k : ℤ) (α : chowGroup C (g ≫ sY) k) :
    (c - d).cap g k α = c.cap g k α - d.cap g k α
```

**`Stacks.Chow.BivariantClass.nsmul_cap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Basic.lean, line 606](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Basic.lean#L606). The attribute's comment: “natural multiples in A^p(X ⟶ Y) are pointwise on cap products”.

> **Stacks 0B76.** A natural multiple of a bivariant class caps to that multiple of its cap
> product.

```lean
theorem BivariantClass.nsmul_cap (n : ℕ) (c : BivariantClass C G sX sY f hf p) {T : Scheme.{u}}
    (g : T ⟶ Y) [LocallyOfFiniteType g] (k : ℤ) (α : chowGroup C (g ≫ sY) k) :
    (n • c).cap g k α = n • c.cap g k α
```

**`Stacks.Chow.BivariantClass.zsmul_cap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Basic.lean, line 616](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Basic.lean#L616). The attribute's comment: “integer multiples in A^p(X ⟶ Y) are pointwise on cap products”.

> **Stacks 0B76.** An integer multiple of a bivariant class caps to that multiple of its cap
> product.

```lean
theorem BivariantClass.zsmul_cap (n : ℤ) (c : BivariantClass C G sX sY f hf p) {T : Scheme.{u}}
    (g : T ⟶ Y) [LocallyOfFiniteType g] (k : ℤ) (α : chowGroup C (g ≫ sY) k) :
    (n • c).cap g k α = n • c.cap g k α
```

**`Stacks.Chow.CanonicalBivariantClass`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Canonical.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Canonical.lean#L116). The attribute's comment: “the group A^p(X ⟶ Y) of bivariant classes of degree p for f, with nothing assumed: the Gysin system is the canonical one, whose first Chern class rule is the rule of an invertible module and whose vanishing is Stacks 02TO, and the descent conditions Stacks 02S1 and 02S2 of the proper and flat axioms are discharged”.

> **Stacks 0B76.** The group `A^p(X ⟶ Y)` of bivariant classes of degree `p` for a morphism
> `f : X ⟶ Y` of schemes locally of finite type over the base: a rule assigning to every morphism
> `g : T ⟶ Y` locally of finite type and every `k` an additive map
> `A_k(T) ⟶ A_{k-p}(T ×_Y X)`, natural for proper pushforward, for flat pullback of fixed relative
> dimension, and for the Gysin map of the zero scheme of a section of an invertible module.
>
> This is `Stacks.Chow.BivariantClass` read against `Stacks.Chow.canonicalGysinSystem`, with the
> abelian group structure of `Stacks.Chow.BivariantClass`.

```lean
abbrev CanonicalBivariantClass (C : ChowSituation.{u}) {X Y : Scheme.{u}} (sX : X ⟶ C.S)
    [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY] (f : X ⟶ Y)
    [LocallyOfFiniteType f] (hf : f ≫ sY = sX) (p : ℤ)
```

**`Stacks.Chow.BivariantClass.flat_naturality_of_relativeDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Canonical.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Canonical.lean#L134). The attribute's comment: “the flat pullback axiom, with the descent condition Stacks 02S1 discharged; the relative dimension of the base change is assumed, Stacks 02NK being absent”.

> **Stacks 0B76 (2), with Stacks 02S1 discharged.** Cap product with a bivariant class commutes
> with flat pullback of fixed relative dimension, the relative dimension of the base change being a
> hypothesis.

```lean
theorem BivariantClass.flat_naturality_of_relativeDimension (c : BivariantClass C G sX sY f hf p)
    {T T' : Scheme.{u}} (g : T ⟶ Y) [LocallyOfFiniteType g] (h : T' ⟶ T) [LocallyOfFiniteType h]
    [Flat h] (r : ℕ) (hr : AlgebraicGeometry.RelativeDimension h r)
    (h' : pullback f (h ≫ g) ⟶ pullback f g)
    (sq : IsPullback (pullback.snd f (h ≫ g)) h' h (pullback.snd f g))
    (hfst : h' ≫ pullback.fst f g = pullback.fst f (h ≫ g)) (k : ℤ) :
    letI : LocallyOfFiniteType h' :=
      MorphismProperty.of_isPullback sq (P := @LocallyOfFiniteType) inferInstance
    letI : Flat h' := MorphismProperty.of_isPullback sq (P := @Flat) inferInstance
    ∀ (hr' : AlgebraicGeometry.RelativeDimension h' r) (α : chowGroup C (g ≫ sY) k),
      HEq
        (c.cap (h ≫ g) (k + (r : ℤ))
          (flatPullbackChow C ((h ≫ g) ≫ sY) (g ≫ sY) h (by simp [Category.assoc]) r hr k
            (flatPullbackDescends C _ _ _ _ _ _ _) α))
        (flatPullbackChow C (pullback.fst f (h ≫ g) ≫ sX) (pullback.fst f g ≫ sX) h'
          (by rw [← Category.assoc, hfst]) r hr' (k - p)
          (flatPullbackDescends C _ _ _ _ _ _ _) (c.cap g k α))
```

**`Stacks.Chow.BivariantClass.gysin_naturality_gysinChowOfInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Canonical.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Canonical.lean#L160). The attribute's comment: “the Gysin axiom for a class at the canonical Gysin system, stated for the unconditional Gysin map of Stacks 02TO and with the descent condition Stacks 02S2 discharged”.

> **Stacks 0B76 (3), for the canonical Gysin system.** Cap product with a bivariant class read
> against `Stacks.Chow.canonicalGysinSystem` commutes with the unconditional Gysin map
> `Stacks.Chow.gysinChowOfInvertible` of Stacks 02TO, for every pulled-back divisor; the descent
> condition Stacks 02S2 for the identification of the base change of the zero scheme with the zero
> scheme of the pulled-back section is discharged.

```lean
theorem BivariantClass.gysin_naturality_gysinChowOfInvertible
    (c : CanonicalBivariantClass C sX sY f hf p) {T : Scheme.{u}} (g : T ⟶ Y)
    [LocallyOfFiniteType g] (L : T.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible T.sheaf.obj T.ringCatSheaf.property L]
    [AlgebraicGeometry.SheafOfModules.IsInvertible (pullback f g).sheaf.obj
      (pullback f g).ringCatSheaf.property ((Scheme.Modules.pullback (pullback.snd f g)).obj L)]
    (s : Γ(L, ⊤)) (k : ℤ) :
    let D := Stacks.Divisors.zeroScheme T L s
    let L' := (Scheme.Modules.pullback (pullback.snd f g)).obj L
    let s' := AlgebraicGeometry.pullbackGlobalSections (pullback.snd f g) L s
    let E := Stacks.Divisors.zeroScheme (pullback f g) L' s'
    ∀ (e : pullback f (D.subschemeι ≫ g) ≅ E.subscheme)
      (_he : e.hom ≫ E.subschemeι = bivariantBaseChangeMap f g D.subschemeι)
      (hbase : e.hom ≫ (E.subschemeι ≫ pullback.fst f g ≫ sX) =
        pullback.fst f (D.subschemeι ≫ g) ≫ sX)
      (α : chowGroup C (g ≫ sY) (k + 1)),
      properChowPushforward C (pullback.fst f (D.subschemeι ≫ g) ≫ sX)
          (E.subschemeι ≫ pullback.fst f g ≫ sX) e.hom hbase (k - p)
          (properPushforwardDescends C _ _ _ _ _)
          (c.cap (D.subschemeι ≫ g) k (gysinChowOfInvertible C (g ≫ sY) k L s α)) =
        gysinChowOfInvertible C (pullback.fst f g ≫ sX) (k - p) L' s'
          (Eq.mp (congrArg (chowGroup C (pullback.fst f g ≫ sX))
            (by omega : (k + 1) - p = (k - p) + 1)) (c.cap g (k + 1) α))
```

**`Stacks.Chow.BivariantChowClass`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Definition.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Definition.lean#L199). The attribute's comment: “a bivariant class of degree p for f, the elements of A^p(X → Y)”.

> A bivariant class `c` of degree `p` for `f : X ⟶ Y`: a rule assigning to
> every morphism `g : Y' ⟶ Y` locally of finite type and every `k` a map
> `c ∩ - : CH_k(Y') ⟶ CH_{k-p}(X')`, `X' = Y' ×_Y X`, such that
>
> 1. for `h : Y'' ⟶ Y'` proper, `c ∩ h_* α'' = h'_* (c ∩ α'')`, `h' : X'' ⟶ X'` its base change;
> 2. for `h : Y'' ⟶ Y'` flat, locally of finite type, of relative dimension `r`,
>    `c ∩ h^* α' = (h')^* (c ∩ α')`;
> 3. for an invertible module `L` on `Y'` with a global section `s`, zero scheme
>    `i : D = Z(s) ⟶ Y'`, and pullback `(L', s', j : E = Z(s') ⟶ X')` to `X'`,
>    `c ∩ i^* α' = j^* (c ∩ α')`, the scheme `D ×_Y X` being identified with `E` by Remark 0B6Y.
>
> The group of all of them is `A^p(X ⟶ Y)`.

```lean
structure BivariantChowClass (C : ChowSituation.{u}) {X Y : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY]
    (f : X ⟶ Y) (hf : f ≫ sY = sX) (p : ℤ)
```

**`Stacks.Chow.BivariantChowClass.equivBivariantClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Definition.lean, line 504](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Definition.lean#L504). The attribute's comment: “bridge: A^p(X → Y) is BivariantClass at the Gysin system of the first Chern class”.

> A bivariant class of degree `p` for `f` is the same thing as a `Stacks.Chow.BivariantClass`
> at the Gysin system `Stacks.Chow.gysinSystemOfInvertible` of the first Chern class; the cap
> operations correspond identically.

```lean
def equivBivariantClass :
    BivariantChowClass C sX sY f hf p ≃ BivariantClass C (gysinSystemOfInvertible C) sX sY f hf p
```

**`Stacks.Chow.BivariantClass.proper_naturality_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/VanishingUnconditional.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/VanishingUnconditional.lean#L61). The attribute's comment: “the proper pushforward axiom, with the descent condition Stacks 02S2 discharged”.

> Capping with a bivariant class commutes with proper pushforward along a
> proper morphism `h : T' ⟶ T` of test schemes and its base change `h'`, pushforward being taken
> with the descent of Stacks 02S2,
> `Stacks.Chow.properPushforwardFactorsThroughRationalEquivalence_of_isProper`.

```lean
theorem BivariantClass.proper_naturality_of_isProper (c : BivariantClass C G sX sY f hf p)
    {T T' : Scheme.{u}} (g : T ⟶ Y) [LocallyOfFiniteType g] (h : T' ⟶ T) [IsProper h]
    (h' : pullback f (h ≫ g) ⟶ pullback f g)
    (sq : IsPullback (pullback.snd f (h ≫ g)) h' h (pullback.snd f g))
    (hfst : h' ≫ pullback.fst f g = pullback.fst f (h ≫ g)) (k : ℤ)
    (α : chowGroup C ((h ≫ g) ≫ sY) k) :
    letI : IsProper h' := MorphismProperty.of_isPullback sq (P := @IsProper) inferInstance
    c.cap g k (properChowPushforward C ((h ≫ g) ≫ sY) (g ≫ sY) h
        (by simp [Category.assoc]) k
        (properPushforwardFactorsThroughRationalEquivalence_of_isProper C ((h ≫ g) ≫ sY)
          (g ≫ sY) h (by simp [Category.assoc]) k) α) =
      properChowPushforward C (pullback.fst f (h ≫ g) ≫ sX) (pullback.fst f g ≫ sX) h'
        (by rw [← Category.assoc, hfst]) (k - p)
        (properPushforwardFactorsThroughRationalEquivalence_of_isProper C
          (pullback.fst f (h ≫ g) ≫ sX) (pullback.fst f g ≫ sX) h'
          (by rw [← Category.assoc, hfst]) (k - p)) (c.cap (h ≫ g) k α)
```

## Tag 0B78, a lemma

[Tag 0B78](https://stacks.math.columbia.edu/tag/0B78) in the Stacks Project.

**`Stacks.Chow.flatPullbackBivariantCap_flat_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/FlatPullback.lean, line 329](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/FlatPullback.lean#L329). The attribute's comment: “the flat-pullback condition of Stacks 0B76 for the flat-pullback rule, from Stacks 02RD, with the Stacks 02S1 descent hypothesis bundled; the rule is `Stacks.Chow.flatPullbackBivariantCap`, and it is not assembled into a term of `Stacks.Chow.BivariantClass` here because the proper condition is Stacks 02RG and the Gysin condition is Stacks 0B71, neither of which this repository carries”.

> **Stacks 0B78.** The flat-pullback condition of Stacks 0B76 for the rule of Stacks 0B78: the
> rule `α ↦ (f')^* α` commutes with flat pullback of fixed relative dimension along a morphism
> `h : T' ⟶ T` of test schemes.
>
> The base change of `f` over `T'` followed by `h`, and the base change of `h` followed by the base
> change of `f` over `T`, are the same morphism `T' ×_Y X ⟶ T`, because the two cartesian squares
> paste; Stacks 02RD then traverses that morphism both ways. The two sides land in degrees
> `(k + s) - (-r)` and `(k - (-r)) + s`, so the identity is a heterogeneous equality, exactly as
> the corresponding field of `Stacks.Chow.BivariantClass` is.

```lean
theorem flatPullbackBivariantCap_flat_naturality {T T' : Scheme.{u}} (g : T ⟶ Y)
    [LocallyOfFiniteType g] (h : T' ⟶ T) [LocallyOfFiniteType h] [Flat h] (s : ℕ)
    (hs : AlgebraicGeometry.RelativeDimension h s)
    (h' : pullback f (h ≫ g) ⟶ pullback f g) [LocallyOfFiniteType h'] [Flat h']
    (sq : IsPullback (pullback.snd f (h ≫ g)) h' h (pullback.snd f g))
    (hfst : h' ≫ pullback.fst f g = pullback.fst f (h ≫ g)) (k : ℤ)
    (hs' : AlgebraicGeometry.RelativeDimension h' s)
    (hfac : FlatPullbackFactorsThroughRationalEquivalence C ((h ≫ g) ≫ sY) (g ≫ sY) h
      (by simp [Category.assoc]) s hs k)
    (hfac' : FlatPullbackFactorsThroughRationalEquivalence C (pullback.fst f (h ≫ g) ≫ sX)
      (pullback.fst f g ≫ sX) h' (by rw [← Category.assoc, hfst]) s hs' (k - -(r : ℤ)))
    (α : chowGroup C (g ≫ sY) k) :
    flatPullbackBivariantCap C sX sY f hf r hfr hfp (h ≫ g) (k + (s : ℤ))
          (flatPullbackChow C ((h ≫ g) ≫ sY) (g ≫ sY) h (by simp [Category.assoc]) s hs k
            hfac α) ≍
      flatPullbackChow C (pullback.fst f (h ≫ g) ≫ sX) (pullback.fst f g ≫ sX) h'
        (by rw [← Category.assoc, hfst]) s hs' (k - -(r : ℤ)) hfac'
        (flatPullbackBivariantCap C sX sY f hf r hfr hfp g k α)
```

**`Stacks.Chow.flatPullbackBivariantChowClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/FlatPullbackChowClass.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/FlatPullbackChowClass.lean#L72). The attribute's comment: “the flat-pullback rule as an element of A^\{-r}(X → Y), the group of Stacks 0B76 whose three conditions use the genuine proper pushforward, flat pullback and Gysin map; its cap operation is flat pullback along the base change of f (flatPullbackBivariantChowClass\_cap)”.

> **Stacks 0B78.** For `f : X ⟶ Y` flat of relative dimension `r` between schemes locally of
> finite type over `S`, the rule which assigns to `g : Y' ⟶ Y` the flat pullback
> `(f')^* : CH_k(Y') ⟶ CH_{k+r}(X ×_Y Y')` along the base change of `f` is a bivariant class of
> degree `-r`, the class `f^* ∈ A^{-r}(X ⟶ Y)`.

```lean
def flatPullbackBivariantChowClass : BivariantChowClass C sX sY f hf (-(r : ℤ))
```

**`Stacks.Chow.existsUnique_bivariantChowClass_cap_eq_flatPullbackChow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/FlatPullbackChowClassUnique.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/FlatPullbackChowClassUnique.lean#L74). The attribute's comment: “the flat-pullback rule is a bivariant class of degree -r, with nothing assumed: exactly one element of A^\{-r}(X → Y), the group of Stacks 0B76 whose three conditions use the genuine proper pushforward, flat pullback and Gysin map, caps by (f')^*”.

> **Stacks 0B78.** Let `f : X ⟶ Y` be flat of relative dimension `r` between schemes locally of
> finite type over `S`. The rule which assigns to `g : Y' ⟶ Y` the flat pullback
> `(f')^* : CH_k(Y') ⟶ CH_{k+r}(X')` along the base change `f' : X' = X ×_Y Y' ⟶ Y'` of `f` is a
> bivariant class of degree `-r`: there is exactly one `c ∈ A^{-r}(X ⟶ Y)` whose cap operation is
> that rule, read in degree `k - (-r) = k + r`.

```lean
theorem existsUnique_bivariantChowClass_cap_eq_flatPullbackChow :
    ∃! c : BivariantChowClass C sX sY f hf (-(r : ℤ)),
      ∀ {T : Scheme.{u}} (g : T ⟶ Y) [LocallyOfFiniteType g] (k : ℤ)
        (α : chowGroup C (g ≫ sY) k),
        c.cap g k α =
          chowGroupDegreeEquiv C (pullback.fst f g ≫ sX) (by ring : k + (r : ℤ) = k - -(r : ℤ))
            (flatPullbackChow C (pullback.fst f g ≫ sX) (g ≫ sY) (pullback.snd f g)
              (pullbackSnd_comp_structureMorphism_eq C sX sY f hf g) r
              (relativeDimension_pullback_snd f g r hfr) k
              (flatPullbackFactorsThroughRationalEquivalence_general C _ _ _ _ _ _ _) α)
```

**`Stacks.Chow.exists_bivariantChowClass_cap_heq_flatPullbackChow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/FlatPullbackChowClassUnique.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/FlatPullbackChowClassUnique.lean#L97). The attribute's comment: “the flat-pullback rule (f')^* : CH\_k(Y') → CH\_\{k+r}(X') is the cap operation of an element of A^\{-r}(X → Y), with nothing assumed, read in degree k + r as the source writes it”.

> **Stacks 0B78**, with the degree transport removed. For `f : X ⟶ Y` flat of relative
> dimension `r`, there is a bivariant class `c ∈ A^{-r}(X ⟶ Y)` whose cap operation on `CH_k(Y')`
> is the flat pullback `(f')^* : CH_k(Y') ⟶ CH_{k+r}(X')` along the base change of `f`, landing in
> degree `k + r` exactly as in the source. The two degrees `k + r` and `k - (-r)` are equal integers
> that are not the same term, so the identity is a heterogeneous equality.

```lean
theorem exists_bivariantChowClass_cap_heq_flatPullbackChow :
    ∃ c : BivariantChowClass C sX sY f hf (-(r : ℤ)),
      ∀ {T : Scheme.{u}} (g : T ⟶ Y) [LocallyOfFiniteType g] (k : ℤ)
        (α : chowGroup C (g ≫ sY) k),
        c.cap g k α ≍
          flatPullbackChow C (pullback.fst f g ≫ sX) (g ≫ sY) (pullback.snd f g)
            (pullbackSnd_comp_structureMorphism_eq C sX sY f hf g) r
            (relativeDimension_pullback_snd f g r hfr) k
            (flatPullbackFactorsThroughRationalEquivalence_general C _ _ _ _ _ _ _) α
```

**`Stacks.Chow.existsUnique_bivariantClass_isBivariantFlatPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/FlatPullbackChowClassUnique.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/FlatPullbackChowClassUnique.lean#L114). The attribute's comment: “exactly one bivariant class of degree -r, at the Gysin system of the first Chern class, satisfies the characterization Stacks.Chow.IsBivariantFlatPullback, with nothing assumed”.

> **Stacks 0B78** for `Stacks.Chow.BivariantClass` at the Gysin system of the first Chern
> class of an invertible module: exactly one bivariant class of degree `-r` for `f` caps by flat
> pullback along the base change of `f`, in the sense of `Stacks.Chow.IsBivariantFlatPullback`.

```lean
theorem existsUnique_bivariantClass_isBivariantFlatPullback :
    ∃! c : BivariantClass C (gysinSystemOfInvertible C) sX sY f hf (-(r : ℤ)),
      IsBivariantFlatPullback C (gysinSystemOfInvertible C) sX sY f hf r hfr
        (flatPullbackDescends C) c
```

**`Stacks.Chow.flatPullbackBivariantClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/FlatPullbackClass.lean, line 493](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/FlatPullbackClass.lean#L493). The attribute's comment: “with Stacks 02S1 as hS1, Stacks 02RG as hRG and Stacks 0B71 as h71”.

> **Stacks 0B78.** For `f : X ⟶ Y` flat of relative dimension `r` between schemes locally of
> finite type over the base, the rule which assigns to a test scheme `g : T ⟶ Y` the flat pullback
> `A_k(T) ⟶ A_{k+r}(X ×_Y T)` along the base change of `f` is a bivariant class of degree `-r`
> for `f`.
>
> The three inputs of the source that this repository does not have are the named hypotheses `hS1`
> (Stacks 02S1), `hRG` (Stacks 02RG) and `h71` (Stacks 0B71, with the identification of Stacks
> 0B6Y). The fourth, Stacks 02RD, is proved here, as is Stacks 02NK; see the implementation notes
> of `StacksFrontier.AlgebraicGeometry.Chow.Bivariant.FlatPullbackClass`.

```lean
def flatPullbackBivariantClass (hRG : ProperPushforwardFlatPullbackBaseChange C)
    (h71 : G.FlatPullbackNaturality r) :
    BivariantClass C G sX sY f hf (-(r : ℤ))
```

**`Stacks.Chow.flatPullbackBivariantCap_proper_naturality_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/FlatPullbackProperPushforward.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/FlatPullbackProperPushforward.lean#L72). The attribute's comment: “the proper-pushforward condition of Stacks 0B76 for the flat-pullback rule, with NOTHING ASSUMED: Stacks 02RG on Chow groups is the theorem Stacks.Chow.properPushforwardFlatPullbackBaseChange above, and the Stacks 02S1 descent along which the rule is formed is the theorem Stacks.Chow.flatPullbackDescends”.

> The proper-pushforward condition of Stacks 0B76 (1) for the flat-pullback rule of Stacks 0B78:
> flat pullback along the base change of a flat `f : X ⟶ Y` of relative dimension `r` commutes with
> proper pushforward along a proper morphism `h : T' ⟶ T` of test schemes over `Y`.

```lean
theorem flatPullbackBivariantCap_proper_naturality_unconditional (C : ChowSituation.{u})
    {X Y : Scheme.{u}} (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S)
    [LocallyOfFiniteType sY] (f : X ⟶ Y) [LocallyOfFiniteType f] [Flat f] (hf : f ≫ sY = sX)
    (r : ℕ) (hfr : AlgebraicGeometry.RelativeDimension f r) {T T' : Scheme.{u}} (g : T ⟶ Y)
    [LocallyOfFiniteType g] (h : T' ⟶ T) [IsProper h]
    (h' : pullback f (h ≫ g) ⟶ pullback f g) [IsProper h']
    (sq : IsPullback (pullback.snd f (h ≫ g)) h' h (pullback.snd f g))
    (hfst : h' ≫ pullback.fst f g = pullback.fst f (h ≫ g)) (k : ℤ)
    (hfac : ProperPushforwardFactorsThroughRationalEquivalence C ((h ≫ g) ≫ sY) (g ≫ sY) h
      (by simp [Category.assoc]) k)
    (hfac' : ProperPushforwardFactorsThroughRationalEquivalence C
      (pullback.fst f (h ≫ g) ≫ sX) (pullback.fst f g ≫ sX) h'
      (by rw [← Category.assoc, hfst]) (k - -(r : ℤ)))
    (α : chowGroup C ((h ≫ g) ≫ sY) k) :
    flatPullbackBivariantCap C sX sY f hf r hfr (flatPullbackDescends C) g k
        (properChowPushforward C ((h ≫ g) ≫ sY) (g ≫ sY) h (by simp [Category.assoc]) k hfac
          α) =
      properChowPushforward C (pullback.fst f (h ≫ g) ≫ sX) (pullback.fst f g ≫ sX) h'
        (by rw [← Category.assoc, hfst]) (k - -(r : ℤ)) hfac'
        (flatPullbackBivariantCap C sX sY f hf r hfr (flatPullbackDescends C) (h ≫ g) k α)
```

**`Stacks.Chow.flatPullbackBivariantClassOfInvertible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/FlatPullbackProperPushforward.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/FlatPullbackProperPushforward.lean#L104). The attribute's comment: “the flat-pullback rule IS a bivariant class of degree -r, with NOTHING ASSUMED: the Stacks 02S1 descent is the theorem Stacks.Chow.flatPullbackDescends, Stacks 02RG on Chow groups is the theorem Stacks.Chow.properPushforwardFlatPullbackBaseChange above, and Stacks 0B71 with the identification of Stacks 0B6Y is the theorem Stacks.Chow.gysinSystemOfInvertible\_flatPullbackNaturalityAtZeroSchemeComparison”.

> For `f : X ⟶ Y` flat of relative dimension `r` between schemes locally of finite type over the
> base, the rule which assigns to a test scheme `g : T ⟶ Y` the flat pullback
> `A_k(T) ⟶ A_{k+r}(X ×_Y T)` along the base change of `f`, as a bivariant class of degree `-r` for
> `f` over the Gysin system `Stacks.Chow.gysinSystemOfInvertible`.

```lean
def flatPullbackBivariantClassOfInvertible (C : ChowSituation.{u}) {X Y : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY] (f : X ⟶ Y)
    [LocallyOfFiniteType f] [Flat f] (hf : f ≫ sY = sX) (r : ℕ)
    (hfr : AlgebraicGeometry.RelativeDimension f r) :
    BivariantClass C (gysinSystemOfInvertible C) sX sY f hf (-(r : ℤ))
```

**`Stacks.Chow.isBivariantFlatPullback_flatPullbackBivariantClassOfInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/FlatPullbackProperPushforward.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/FlatPullbackProperPushforward.lean#L138). The attribute's comment: “the class of the same tag constructed above satisfies the characterization Stacks.Chow.IsBivariantFlatPullback, with NOTHING ASSUMED, so that the uniqueness statement Stacks.Chow.eq\_of\_isBivariantFlatPullback is about a nonempty collection”.

> The class `Stacks.Chow.flatPullbackBivariantClassOfInvertible` is the flat-pullback class in
> the sense of `Stacks.Chow.IsBivariantFlatPullback`: on every test scheme its cap operation is flat
> pullback along the base change of `f`.

```lean
theorem isBivariantFlatPullback_flatPullbackBivariantClassOfInvertible (C : ChowSituation.{u})
    {X Y : Scheme.{u}} (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S)
    [LocallyOfFiniteType sY] (f : X ⟶ Y) [LocallyOfFiniteType f] [Flat f] (hf : f ≫ sY = sX)
    (r : ℕ) (hfr : AlgebraicGeometry.RelativeDimension f r) :
    IsBivariantFlatPullback C (gysinSystemOfInvertible C) sX sY f hf r hfr
      (flatPullbackDescends C) (flatPullbackBivariantClassOfInvertible C sX sY f hf r hfr)
```

**`Stacks.Chow.completedFlatPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/CompletedFlatPullback.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/CompletedFlatPullback.lean#L164). The attribute's comment: “flat pullback along a flat morphism whose relative dimension is constant on each connected component, in the completed bivariant group A^*(X → Y)^∧”.

> **`f^* ∈ A^*(X ⟶ Y)^∧` for a flat morphism `f`** (Stacks 0B78 on completions). For a flat
> morphism whose restriction to every connected component `X_a` of `X` has pure relative dimension
> `r_a`, the flat-pullback class in the completed bivariant group of Stacks 0FE0: on `X_a` it is the
> class of Stacks 0B78 of the restriction `X_a ⟶ Y_{a'}` of `f`, placed in degree `-r_a`. Every input
> of Stacks 0B78 is discharged.

```lean
def completedFlatPullback [IsLocallyNoetherian X] [IsLocallyNoetherian Y]
    (hrel : ∀ a : _root_.ConnectedComponents X,
      ∃ r : ℕ, AlgebraicGeometry.RelativeDimension (f.resConnectedComponent a) r) :
    completedBivariantGroup C (gysinSystemOfInvertible C) sX sY f hf
```

## Tag 0B79, a lemma

[Tag 0B79](https://stacks.math.columbia.edu/tag/0B79) in the Stacks Project.

**`Stacks.Chow.gysinBivariantClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/GysinClass.lean, line 540](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/GysinClass.lean#L540).

> Let `(𝓛, s, i : D ⟶ X)` be a triple as in Definition 02T8 on a scheme `X` locally of finite
> type over the base. The rule assigning to every `g : X' ⟶ X` locally of finite type the Gysin map
> `(i')^* : CH_k(X') ⟶ CH_{k-1}(D')` of the pulled-back section, where `D' = D ×_X X'`, is a
> bivariant class of degree `1` for `i`: the class below caps by that Gysin map on every test
> scheme.

```lean
def gysinBivariantClass :
    { c : BivariantClass C (gysinSystemOfInvertible C) (gysinTripleInclusion L s ≫ sX) sX
        (gysinTripleInclusion L s) rfl 1 //
      IsGysinBivariantClass C (gysinSystemOfInvertible C) sX L s c }
```

## Tag 0EPK, a lemma

[Tag 0EPK](https://stacks.math.columbia.edu/tag/0EPK) in the Stacks Project.

**`Stacks.Chow.isProper_bivariantPushforwardBaseChange`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ProperPushforward.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ProperPushforward.lean#L210). The attribute's comment: “properness of the base change of the proper morphism”.

> **Stacks 0EPK.** The base change of a proper morphism along a test scheme is proper, so the
> rule of Stacks 0EPK can push forward along it.

```lean
instance isProper_bivariantPushforwardBaseChange {X Y Z T : Scheme.{u}} (f : X ⟶ Y) [IsProper f]
    (g : Y ⟶ Z) (t : T ⟶ Z) : IsProper (bivariantPushforwardBaseChange f g t)
```

**`Stacks.Chow.bivariantProperPushforwardCap_proper_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ProperPushforward.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ProperPushforward.lean#L256). The attribute's comment: “the proper-pushforward axiom of the pushed-forward class”.

> **Stacks 0EPK.** The proper-pushforward axiom of Stacks 0B76 for the rule of Stacks 0EPK: the
> cap operation `α ↦ f'_*(c ∩ α)` commutes with proper pushforward along a morphism of test
> schemes.

```lean
theorem bivariantProperPushforwardCap_proper_naturality {T T' : Scheme.{u}} (t : T ⟶ Z)
    [LocallyOfFiniteType t] (h : T' ⟶ T) [IsProper h]
    (h' : pullback g (h ≫ t) ⟶ pullback g t)
    (sq : IsPullback (pullback.snd g (h ≫ t)) h' h (pullback.snd g t))
    (hfst : h' ≫ pullback.fst g t = pullback.fst g (h ≫ t)) (k : ℤ)
    (α : chowGroup C ((h ≫ t) ≫ sZ) k) :
    letI : IsProper h' := MorphismProperty.of_isPullback sq (P := @IsProper) inferInstance
    bivariantProperPushforwardCap C G sX sY sZ f g hf hg hpp p c t k
        (properChowPushforward C ((h ≫ t) ≫ sZ) (t ≫ sZ) h (by simp [Category.assoc]) k
          (hpp _ _ _ _ _) α) =
      properChowPushforward C (pullback.fst g (h ≫ t) ≫ sY) (pullback.fst g t ≫ sY) h'
        (by rw [← Category.assoc, hfst]) (k - p) (hpp _ _ _ _ _)
        (bivariantProperPushforwardCap C G sX sY sZ f g hf hg hpp p c (h ≫ t) k α)
```

**`Stacks.Chow.eq_of_isBivariantProperPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ProperPushforward.lean, line 319](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ProperPushforward.lean#L319). The attribute's comment: “uniqueness of the pushed-forward class”.

> **Stacks 0EPK.** The rule of Stacks 0EPK determines the pushed-forward class: two bivariant
> classes that both push `c` forward along `f` are equal.

```lean
theorem eq_of_isBivariantProperPushforward
    (h : IsBivariantProperPushforward C G sX sY sZ f g hf hg hpp p c d)
    (h' : IsBivariantProperPushforward C G sX sY sZ f g hf hg hpp p c d') : d = d'
```

**`Stacks.Chow.canonicalBivariantProperPushforwardCap_gysin_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ProperPushforwardCanonical.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ProperPushforwardCanonical.lean#L86). The attribute's comment: “the Gysin axiom of Stacks 0B76 for the rule α ↦ f'\_*(c ∩ α)”.

> **Stacks 0EPK, the Gysin axiom.** For `c ∈ A^p(X ⟶ Z)` and `f` proper, the rule
> `α ↦ f'_*(c ∩ α)` commutes with the Gysin map `i^*` of Stacks 02TO of the zero scheme of a section
> of an invertible module on a test scheme: pushing `f'_*(c ∩ i^* α)` to the zero scheme of the
> pulled-back section on `T ×_Z Y` gives `i'^* f'_*(c ∩ α)`.

```lean
theorem canonicalBivariantProperPushforwardCap_gysin_naturality
    (c : CanonicalBivariantClass C sX sZ (f ≫ g) (comp_comp_structureMorphism_eq hf hg) p)
    {T : Scheme.{u}} (t : T ⟶ Z) [LocallyOfFiniteType t] (L : T.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible T.sheaf.obj T.ringCatSheaf.property L]
    (s : Γ(L, ⊤)) (k : ℤ) :
    let D := Stacks.Divisors.zeroScheme T L s
    let L' := (Scheme.Modules.pullback (pullback.snd g t)).obj L
    let s' := AlgebraicGeometry.pullbackGlobalSections (pullback.snd g t) L s
    let E := Stacks.Divisors.zeroScheme (pullback g t) L' s'
    ∀ (e : pullback g (D.subschemeι ≫ t) ≅ E.subscheme)
      (_he : e.hom ≫ E.subschemeι = bivariantBaseChangeMap g t D.subschemeι)
      (hbase : e.hom ≫ (E.subschemeι ≫ pullback.fst g t ≫ sY) =
        pullback.fst g (D.subschemeι ≫ t) ≫ sY)
      (α : chowGroup C (t ≫ sZ) (k + 1)),
      properChowPushforward C (pullback.fst g (D.subschemeι ≫ t) ≫ sY)
          (E.subschemeι ≫ pullback.fst g t ≫ sY) e.hom hbase (k - p)
          (properPushforwardDescends C _ _ _ _ _)
          (bivariantProperPushforwardCap C (canonicalGysinSystem C) sX sY sZ f g hf hg
            (properPushforwardDescends C) p c (D.subschemeι ≫ t) k
            (gysinChowOfInvertible C (t ≫ sZ) k L s α)) =
        gysinChowOfInvertible C (pullback.fst g t ≫ sY) (k - p) L' s'
          (Eq.mp (congrArg (chowGroup C (pullback.fst g t ≫ sY))
              (by omega : (k + 1) - p = (k - p) + 1))
            (bivariantProperPushforwardCap C (canonicalGysinSystem C) sX sY sZ f g hf hg
              (properPushforwardDescends C) p c t (k + 1) α))
```

**`Stacks.Chow.canonicalBivariantProperPushforward`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ProperPushforwardCanonical.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ProperPushforwardCanonical.lean#L125).

> **Stacks 0EPK.** For `f : X ⟶ Y` proper, `g : Y ⟶ Z` and `c ∈ A^p(X ⟶ Z)`, the rule which to
> a test scheme `t : T ⟶ Z` assigns `α ↦ f'_*(c ∩ α)`, with `f' : T ×_Z X ⟶ T ×_Z Y` the base change
> of `f`, is a bivariant class `f_* ∘ c ∈ A^p(Y ⟶ Z)`. Its cap formula is
> `Stacks.Chow.canonicalBivariantProperPushforward_cap`.

```lean
def canonicalBivariantProperPushforward
    (c : CanonicalBivariantClass C sX sZ (f ≫ g) (comp_comp_structureMorphism_eq hf hg) p) :
    CanonicalBivariantClass C sY sZ g hg p
```

**`Stacks.Chow.existsUnique_canonicalBivariantProperPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ProperPushforwardCanonical.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ProperPushforwardCanonical.lean#L149). The attribute's comment: “existence and uniqueness of f\_* ∘ c with its cap formula”.

> **Stacks 0EPK.** For `f : X ⟶ Y` proper, `g : Y ⟶ Z` and `c ∈ A^p(X ⟶ Z)` there is exactly one
> bivariant class `f_* ∘ c ∈ A^p(Y ⟶ Z)` whose cap operation is `α ↦ f'_*(c ∩ α)` on every test
> scheme `t : T ⟶ Z`, with `f' : T ×_Z X ⟶ T ×_Z Y` the base change of `f`.

```lean
theorem existsUnique_canonicalBivariantProperPushforward
    (c : CanonicalBivariantClass C sX sZ (f ≫ g) (comp_comp_structureMorphism_eq hf hg) p) :
    ∃! d : CanonicalBivariantClass C sY sZ g hg p,
      ∀ {T : Scheme.{u}} (t : T ⟶ Z) [LocallyOfFiniteType t] (k : ℤ)
        (α : chowGroup C (t ≫ sZ) k),
        d.cap t k α =
          properChowPushforward C (pullback.fst (f ≫ g) t ≫ sX) (pullback.fst g t ≫ sY)
            (bivariantPushforwardBaseChange f g t)
            (bivariantPushforwardBaseChange_comp_structure hf g t) (k - p)
            (properPushforwardDescends C _ _ _ _ _) (c.cap t k α)
```

**`Stacks.Chow.bivariantProperPushforwardCap_flat_naturality_of_factors`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ProperPushforwardFlatPullback.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ProperPushforwardFlatPullback.lean#L119). The attribute's comment: “the flat-pullback axiom of the pushed-forward class”.

> **Stacks 0EPK.** The flat-pullback axiom of Stacks 0B76 for the rule of Stacks 0EPK: the cap
> operation `α ↦ f'_*(c ∩ α)` commutes with flat pullback of fixed relative dimension along a
> morphism of test schemes.
>
> The degrees are `(k + r) - p` on the left and `(k - p) + r` on the right, the same integer written
> two ways, which is why the conclusion is an `HEq`.

```lean
theorem bivariantProperPushforwardCap_flat_naturality_of_factors {T T' : Scheme.{u}} (t : T ⟶ Z)
    [LocallyOfFiniteType t] (h : T' ⟶ T) [LocallyOfFiniteType h] [Flat h] (r : ℕ)
    (hr : AlgebraicGeometry.RelativeDimension h r)
    (h' : pullback g (h ≫ t) ⟶ pullback g t)
    (sq : IsPullback (pullback.snd g (h ≫ t)) h' h (pullback.snd g t))
    (hfst : h' ≫ pullback.fst g t = pullback.fst g (h ≫ t)) (k : ℤ)
    (hr' : letI : LocallyOfFiniteType h' :=
        MorphismProperty.of_isPullback sq (P := @LocallyOfFiniteType) inferInstance
      AlgebraicGeometry.RelativeDimension h' r)
    (hfac : FlatPullbackFactorsThroughRationalEquivalence C ((h ≫ t) ≫ sZ) (t ≫ sZ) h
      (by simp [Category.assoc]) r hr k)
    (hfac' : letI : LocallyOfFiniteType h' :=
          MorphismProperty.of_isPullback sq (P := @LocallyOfFiniteType) inferInstance
        letI : Flat h' := MorphismProperty.of_isPullback sq (P := @Flat) inferInstance
      FlatPullbackFactorsThroughRationalEquivalence C (pullback.fst g (h ≫ t) ≫ sY)
        (pullback.fst g t ≫ sY) h' (by rw [← Category.assoc, hfst]) r hr' (k - p))
    (α : chowGroup C (t ≫ sZ) k) :
    letI : LocallyOfFiniteType h' :=
      MorphismProperty.of_isPullback sq (P := @LocallyOfFiniteType) inferInstance
    letI : Flat h' := MorphismProperty.of_isPullback sq (P := @Flat) inferInstance
    bivariantProperPushforwardCap C G sX sY sZ f g hf hg hpp p c (h ≫ t) (k + (r : ℤ))
        (flatPullbackChow C ((h ≫ t) ≫ sZ) (t ≫ sZ) h (by simp [Category.assoc]) r hr k
          hfac α) ≍
      flatPullbackChow C (pullback.fst g (h ≫ t) ≫ sY) (pullback.fst g t ≫ sY) h'
        (by rw [← Category.assoc, hfst]) r hr' (k - p) hfac'
        (bivariantProperPushforwardCap C G sX sY sZ f g hf hg hpp p c t k α)
```

**`Stacks.Chow.bivariantProperPushforwardCap_proper_naturality_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ProperPushforwardUnconditional.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ProperPushforwardUnconditional.lean#L70). The attribute's comment: “the proper-pushforward axiom of the pushed-forward class, with NOTHING ASSUMED: the descent of Stacks 02S2 is the theorem Stacks.Chow.properPushforwardDescends”.

> The proper-pushforward axiom of Stacks 0B76 for the rule of Stacks 0EPK, with proper
> pushforward on Chow groups taken along the descent `Stacks.Chow.properPushforwardDescends`.

```lean
theorem bivariantProperPushforwardCap_proper_naturality_unconditional {T T' : Scheme.{u}}
    (t : T ⟶ Z) [LocallyOfFiniteType t] (h : T' ⟶ T) [IsProper h]
    (h' : pullback g (h ≫ t) ⟶ pullback g t)
    (sq : IsPullback (pullback.snd g (h ≫ t)) h' h (pullback.snd g t))
    (hfst : h' ≫ pullback.fst g t = pullback.fst g (h ≫ t)) (k : ℤ)
    (α : chowGroup C ((h ≫ t) ≫ sZ) k) :
    letI : IsProper h' := MorphismProperty.of_isPullback sq (P := @IsProper) inferInstance
    bivariantProperPushforwardCap C G sX sY sZ f g hf hg (properPushforwardDescends C) p c t k
        (properChowPushforward C ((h ≫ t) ≫ sZ) (t ≫ sZ) h (by simp [Category.assoc]) k
          (properPushforwardDescends C _ _ _ _ _) α) =
      properChowPushforward C (pullback.fst g (h ≫ t) ≫ sY) (pullback.fst g t ≫ sY) h'
        (by rw [← Category.assoc, hfst]) (k - p) (properPushforwardDescends C _ _ _ _ _)
        (bivariantProperPushforwardCap C G sX sY sZ f g hf hg (properPushforwardDescends C) p c
          (h ≫ t) k α)
```

**`Stacks.Chow.bivariantProperPushforwardCap_flat_naturality_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ProperPushforwardUnconditional.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ProperPushforwardUnconditional.lean#L95). The attribute's comment: “the flat-pullback axiom of the pushed-forward class, with NOTHING ASSUMED: Stacks 02RG on Chow groups is the theorem Stacks.Chow.properPushforwardFlatPullbackBaseChange, and the two descents are Stacks.Chow.flatPullbackDescends and Stacks.Chow.properPushforwardDescends”.

> The flat-pullback axiom of Stacks 0B76 for the rule of Stacks 0EPK, with flat pullback and
> proper pushforward on Chow groups taken along the descents `Stacks.Chow.flatPullbackDescends` and
> `Stacks.Chow.properPushforwardDescends`, and the relative dimension of the base change given by
> Stacks 02NK.

```lean
theorem bivariantProperPushforwardCap_flat_naturality_unconditional {T T' : Scheme.{u}}
    (t : T ⟶ Z) [LocallyOfFiniteType t] (h : T' ⟶ T) [LocallyOfFiniteType h] [Flat h] (r : ℕ)
    (hr : AlgebraicGeometry.RelativeDimension h r)
    (h' : pullback g (h ≫ t) ⟶ pullback g t)
    (sq : IsPullback (pullback.snd g (h ≫ t)) h' h (pullback.snd g t))
    (hfst : h' ≫ pullback.fst g t = pullback.fst g (h ≫ t)) (k : ℤ)
    (α : chowGroup C (t ≫ sZ) k) :
    letI : LocallyOfFiniteType h' :=
      MorphismProperty.of_isPullback sq (P := @LocallyOfFiniteType) inferInstance
    letI : Flat h' := MorphismProperty.of_isPullback sq (P := @Flat) inferInstance
    HEq
      (bivariantProperPushforwardCap C G sX sY sZ f g hf hg (properPushforwardDescends C) p c
        (h ≫ t) (k + (r : ℤ))
        (flatPullbackChow C ((h ≫ t) ≫ sZ) (t ≫ sZ) h (by simp [Category.assoc]) r hr k
          (flatPullbackDescends C _ _ _ _ _ _ _) α))
      (flatPullbackChow C (pullback.fst g (h ≫ t) ≫ sY) (pullback.fst g t ≫ sY) h'
        (by rw [← Category.assoc, hfst]) r
        (AlgebraicGeometry.RelativeDimension.of_isPullback sq hr) (k - p)
        (flatPullbackDescends C _ _ _ _ _ _ _)
        (bivariantProperPushforwardCap C G sX sY sZ f g hf hg (properPushforwardDescends C) p c t k
          α))
```

**`Stacks.Chow.bivariantProperPushforwardCap_gysin_naturality_ofInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ProperPushforwardUnconditional.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ProperPushforwardUnconditional.lean#L142). The attribute's comment: “the Gysin axiom of the pushed-forward class at the Gysin system of the first Chern class rule, with NOTHING ASSUMED: Stacks 02TA for that Gysin system is a pair of theorems here, the identification is Stacks 0B6Y, and the descent of Stacks 02S2 is Stacks.Chow.properPushforwardDescends”.

> The Gysin axiom of Stacks 0B76 for the rule of Stacks 0EPK at the Gysin system
> `Stacks.Chow.gysinSystemOfInvertible` of the first Chern class rule, with proper pushforward on
> Chow groups taken along the descent `Stacks.Chow.properPushforwardDescends`.

```lean
theorem bivariantProperPushforwardCap_gysin_naturality_ofInvertible {T : Scheme.{u}} (t : T ⟶ Z)
    [LocallyOfFiniteType t] (L : T.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible T.sheaf.obj T.ringCatSheaf.property L]
    (s : Γ(L, ⊤)) (k : ℤ)
    (e : pullback g ((Stacks.Divisors.zeroScheme T L s).subschemeι ≫ t) ≅
      (Stacks.Divisors.zeroScheme (pullback g t)
        ((Scheme.Modules.pullback (pullback.snd g t)).obj L)
        (AlgebraicGeometry.pullbackGlobalSections (pullback.snd g t) L s)).subscheme)
    (he : e.hom ≫ (Stacks.Divisors.zeroScheme (pullback g t)
        ((Scheme.Modules.pullback (pullback.snd g t)).obj L)
        (AlgebraicGeometry.pullbackGlobalSections (pullback.snd g t) L s)).subschemeι =
      bivariantBaseChangeMap g t (Stacks.Divisors.zeroScheme T L s).subschemeι)
    (hbase : e.hom ≫ ((Stacks.Divisors.zeroScheme (pullback g t)
        ((Scheme.Modules.pullback (pullback.snd g t)).obj L)
        (AlgebraicGeometry.pullbackGlobalSections (pullback.snd g t) L s)).subschemeι ≫
        pullback.fst g t ≫ sY) =
      pullback.fst g ((Stacks.Divisors.zeroScheme T L s).subschemeι ≫ t) ≫ sY)
    (α : chowGroup C (t ≫ sZ) (k + 1)) :
    properChowPushforward C
        (pullback.fst g ((Stacks.Divisors.zeroScheme T L s).subschemeι ≫ t) ≫ sY)
        ((Stacks.Divisors.zeroScheme (pullback g t)
          ((Scheme.Modules.pullback (pullback.snd g t)).obj L)
          (AlgebraicGeometry.pullbackGlobalSections (pullback.snd g t) L s)).subschemeι ≫
          pullback.fst g t ≫ sY) e.hom hbase (k - p)
        (properPushforwardDescends C _ _ _ _ _)
        (bivariantProperPushforwardCap C (gysinSystemOfInvertible C) sX sY sZ f g hf hg
          (properPushforwardDescends C) p c
          ((Stacks.Divisors.zeroScheme T L s).subschemeι ≫ t) k
          ((gysinSystemOfInvertible C).onChow (t ≫ sZ) L s k α)) =
      (gysinSystemOfInvertible C).onChow (pullback.fst g t ≫ sY)
        ((Scheme.Modules.pullback (pullback.snd g t)).obj L)
        (AlgebraicGeometry.pullbackGlobalSections (pullback.snd g t) L s) (k - p)
        (Eq.mp (congrArg (chowGroup C (pullback.fst g t ≫ sY))
          (by omega : k + 1 - p = k - p + 1))
          (bivariantProperPushforwardCap C (gysinSystemOfInvertible C) sX sY sZ f g hf hg
            (properPushforwardDescends C) p c t (k + 1) α))
```

**`Stacks.Chow.bivariantProperPushforwardOfInvertible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ProperPushforwardUnconditional.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ProperPushforwardUnconditional.lean#L191). The attribute's comment: “the pushed-forward class f\_* ∘ c itself, at the Gysin system of the first Chern class rule, with NOTHING ASSUMED: the rule of the lemma IS a bivariant class, so the three axioms of Stacks 0B76 for it are the three fields of this term, and Stacks 02RG, Stacks 02TA for this Gysin system and Stacks 02S2 are all theorems of this repository”.

> The proper pushforward `f_* ∘ c ∈ A^p(Y ⟶ Z)` of a bivariant class `c ∈ A^p(X ⟶ Z)` along a
> proper `f : X ⟶ Y`, at the Gysin system of the first Chern class rule: the bivariant class whose
> cap operation is the rule `α ↦ f'_*(c ∩ α)` of `Stacks.Chow.bivariantProperPushforwardCap`.

```lean
def bivariantProperPushforwardOfInvertible :
    BivariantClass C (gysinSystemOfInvertible C) sY sZ g hg p
```

**`Stacks.Chow.isBivariantProperPushforward_bivariantProperPushforwardOfInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ProperPushforwardUnconditional.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ProperPushforwardUnconditional.lean#L204). The attribute's comment: “the constructed class satisfies the characterization Stacks.Chow.IsBivariantProperPushforward of the same tag, with NOTHING ASSUMED, so the uniqueness statement is about a nonempty collection”.

> The class `Stacks.Chow.bivariantProperPushforwardOfInvertible` caps by the rule
> `α ↦ f'_*(c ∩ α)`, so it is the proper pushforward of `c` in the sense of
> `Stacks.Chow.IsBivariantProperPushforward`.

```lean
theorem isBivariantProperPushforward_bivariantProperPushforwardOfInvertible :
    IsBivariantProperPushforward C (gysinSystemOfInvertible C) sX sY sZ f g hf hg
      (properPushforwardDescends C) p c
      (bivariantProperPushforwardOfInvertible C sX sY sZ f g hf hg p c)
```

**`Stacks.Chow.exists_isBivariantProperPushforward_ofInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ProperPushforwardUnconditional.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ProperPushforwardUnconditional.lean#L218). The attribute's comment: “existence of the pushed-forward class at the Gysin system of the first Chern class rule, with NOTHING ASSUMED”.

> For a proper `f : X ⟶ Y`, a morphism `g : Y ⟶ Z` and a bivariant class `c` of degree `p` for
> `f ≫ g` against the Gysin system of the first Chern class rule, there is a bivariant class of
> degree `p` for `g` whose cap operation is `α ↦ f'_*(c ∩ α)`.

```lean
theorem exists_isBivariantProperPushforward_ofInvertible :
    ∃ d : BivariantClass C (gysinSystemOfInvertible C) sY sZ g hg p,
      IsBivariantProperPushforward C (gysinSystemOfInvertible C) sX sY sZ f g hf hg
        (properPushforwardDescends C) p c d
```

**`Stacks.Chow.bivariantProperPushforwardExistsOfInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ProperPushforwardUnconditional.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ProperPushforwardUnconditional.lean#L232). The attribute's comment: “the bundled existence statement at the Gysin system of the first Chern class rule, with NOTHING ASSUMED: Stacks 02RG on Chow groups and Stacks 02TA for this Gysin system are both theorems of this repository”.

> The bundled existence statement `Stacks.Chow.BivariantProperPushforwardExists` of
> Stacks 0EPK holds at the Gysin system of the first Chern class rule.

```lean
theorem bivariantProperPushforwardExistsOfInvertible (C : ChowSituation.{u}) :
    BivariantProperPushforwardExists C (gysinSystemOfInvertible C)
```

**`Stacks.Chow.eq_of_isBivariantProperPushforward_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ProperPushforwardUnconditional.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ProperPushforwardUnconditional.lean#L243). The attribute's comment: “uniqueness of the pushed-forward class, with NOTHING ASSUMED: the descent of Stacks 02S2 is the theorem Stacks.Chow.properPushforwardDescends”.

> Two bivariant classes that both push `c` forward along `f`, with proper pushforward on Chow
> groups taken along the descent `Stacks.Chow.properPushforwardDescends`, are equal.

```lean
theorem eq_of_isBivariantProperPushforward_unconditional {C : ChowSituation.{u}}
    {G : GysinSystem C} {X Y Z : Scheme.{u}} {sX : X ⟶ C.S} [LocallyOfFiniteType sX]
    {sY : Y ⟶ C.S} [LocallyOfFiniteType sY] {sZ : Z ⟶ C.S} [LocallyOfFiniteType sZ] {f : X ⟶ Y}
    [IsProper f] {g : Y ⟶ Z} [LocallyOfFiniteType g] {hf : f ≫ sY = sX} {hg : g ≫ sZ = sY}
    {p : ℤ} {c : BivariantClass C G sX sZ (f ≫ g) (comp_comp_structureMorphism_eq hf hg) p}
    {d d' : BivariantClass C G sY sZ g hg p}
    (h : IsBivariantProperPushforward C G sX sY sZ f g hf hg (properPushforwardDescends C) p c d)
    (h' : IsBivariantProperPushforward C G sX sY sZ f g hf hg (properPushforwardDescends C) p c
      d') : d = d'
```

## Tag 0F9Z, a remark

[Tag 0F9Z](https://stacks.math.columbia.edu/tag/0F9Z) in the Stacks Project.

**`Stacks.Chow.chowCohomologyRestriction_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyFunctoriality.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowCohomologyFunctoriality.lean#L44). The attribute's comment: “compatibility with compositions, for the restriction map on Chow cohomology of Tag 0B7F”.

> The restriction map of Stacks 0B7F is compatible with composition: restricting a class on `X`
> along `f : Y ⟶ X` and then along `a : W ⟶ Y` gives the restriction along `a ≫ f`,
>
>   `a^*(f^*(c)) = (a ≫ f)^*(c)`.

```lean
theorem chowCohomologyRestriction_comp (c : chowCohomologyComponent C G sX p) :
    chowCohomologyRestriction C G (f ≫ sX) a p hgys
        (chowCohomologyRestriction C G sX f p hgys c) =
      chowCohomologyRestriction C G sX (a ≫ f) p hgys c
```

**`Stacks.Chow.BivariantChowClass.restrict`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowRestriction.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowRestriction.lean#L165). The attribute's comment: “the restriction map A^p(X → Y) → A^p(X' → Y'), c ↦ res(c)”.

> The restriction `res(c) ∈ A^p(X' ⟶ Y')`, `X' = Y' ×_Y X`, of a bivariant class `c ∈ A^p(X ⟶ Y)`
> along `h : Y' ⟶ Y`: a scheme `Y''` locally of finite type over `Y'` is one over `Y`, and
> `res(c) ∩ α'' = c ∩ α''` for `α'' ∈ CH_k(Y'')` (`Stacks.Chow.BivariantChowClass.restrict_cap`).

```lean
def restrict (c : BivariantChowClass C sX sY f hf p) :
    haveI := locallyOfFiniteType_of_structure sY h hh
    BivariantChowClass C (pullback.fst f h ≫ sX) sY' (pullback.snd f h)
      (restrict_structure_eq hf h hh) p
```

**`Stacks.Chow.BivariantChowClass.restrict_cap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowRestriction.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowRestriction.lean#L179). The attribute's comment: “res(c) ∩ α'' = c ∩ α''”.

> `res(c) ∩ α'' = c ∩ α''`: for `g : Y'' ⟶ Y'` and `α'' ∈ CH_k(Y'')`, the cap of the restriction
> is the cap of `c` at `g ≫ h`, read on `(Y' ×_Y X) ×_{Y'} Y''` through the canonical isomorphism
> with `Y'' ×_Y X`.

```lean
theorem restrict_cap (c : BivariantChowClass C sX sY f hf p) {T : Scheme.{u}} (g : T ⟶ Y')
    [LocallyOfFiniteType g] (k : ℤ) (α : chowGroup C (g ≫ sY') k) :
    haveI := locallyOfFiniteType_of_structure sY h hh
    (c.restrict h hh).cap g k α =
      chowPushforwardOfIso C (pullback.fst f (g ≫ h) ≫ sX)
        (pullback.fst (pullback.snd f h) g ≫ (pullback.fst f h ≫ sX))
        (pullbackLeftPullbackSndIso f h g).inv (by simp) (k - p)
        (c.cap (g ≫ h) k (chowGroupCongr C (by rw [Category.assoc, hh]) k α))
```

**`Stacks.Chow.BivariantChowClass.restrict_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowRestriction.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowRestriction.lean#L217). The attribute's comment: “compatibility with compositions: res along Y'' → Y' after res along Y' → Y is res along Y'' → Y”.

> Restriction is compatible with compositions of base changes: restricting `c` along `h : Y' ⟶ Y`
> and then along `h' : Y'' ⟶ Y'` is restricting `c` along `h' ≫ h`, the two classes agreeing after
> the canonical identification `(X ×_Y Y') ×_{Y'} Y'' ≅ X ×_Y Y''` of their sources.

```lean
theorem restrict_restrict {Y'' : Scheme.{u}} {sY'' : Y'' ⟶ C.S} [LocallyOfFiniteType sY'']
    (h' : Y'' ⟶ Y') (hh' : h' ≫ sY' = sY'') (c : BivariantChowClass C sX sY f hf p) :
    haveI := locallyOfFiniteType_of_structure sY h hh
    haveI := locallyOfFiniteType_of_structure sY' h' hh'
    ((c.restrict h hh).restrict h' hh').transport
        (restrict_structure_eq hf (h' ≫ h) (by rw [Category.assoc, hh, hh']))
        (pullbackLeftPullbackSndIso f h h') (pullbackLeftPullbackSndIso_hom_snd f h h') =
      c.restrict (h' ≫ h) (by rw [Category.assoc, hh, hh'])
```

**`Stacks.Chow.BivariantChowClass.restrict_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowRestriction.lean, line 283](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/ChowRestriction.lean#L283). The attribute's comment: “compatibility with compositions: res(a ∘ b) = res(a) ∘ res(b)”.

> Restriction is compatible with the composition of bivariant classes. For `a ∈ A^p(X ⟶ Y)`,
> `b ∈ A^q(Y ⟶ Z)` and `h : Z' ⟶ Z`, write `Y' = Y ×_Z Z'` and `X' = X ×_Y Y' = X ×_Z Z'`; then
> `res(a ∘ b) = res(a) ∘ res(b)` in `A^{p+q}(X' ⟶ Z')`, where `res(a) ∈ A^p(X ×_Y Y' ⟶ Y')` is the
> restriction along `Y' ⟶ Y` and `res(b) ∈ A^q(Y' ⟶ Z')` the restriction along `h`. The two sources
> are identified by the canonical isomorphism `X ×_Y (Y ×_Z Z') ≅ X ×_Z Z'`.

```lean
theorem restrict_comp {Z' : Scheme.{u}} {sZ' : Z' ⟶ C.S} [LocallyOfFiniteType sZ'] (h : Z' ⟶ Z)
    (hh : h ≫ sZ = sZ') (a : BivariantChowClass C sX sY f hf p)
    (b : BivariantChowClass C sY sZ g hg q) :
    haveI := locallyOfFiniteType_of_structure sZ h hh
    ((a.restrict (pullback.fst g h) rfl).comp (b.restrict h hh)).transport
        (restrict_structure_eq (comp_comp_structureMorphism_eq hf hg) h hh)
        (pullbackRightPullbackFstIso g h f) (pullbackRightPullbackFstIso_hom_snd g h f) =
      (a.comp b).restrict h hh
```

**`Stacks.Chow.bivariantRestrictionCap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Restriction.lean, line 676](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Restriction.lean#L676). The attribute's comment: “the cap operation of the restriction”.

> **Stacks 0F9Z.** The cap operation `res(c) ∩ -` of the restriction of a bivariant class `c`
> of degree `p` for `f : X ⟶ Y` along `h : Y' ⟶ Y`: on a test scheme `g : T ⟶ Y'` it is the cap
> operation of `c` at `g ≫ h`, pushed forward along the canonical isomorphism
> `T ×_Y X ≅ (Y' ×_Y X) ×_{Y'} T`.

```lean
def bivariantRestrictionCap (c : BivariantClass C G sX sY f hf p) {T : Scheme.{u}} (g : T ⟶ Y')
    [LocallyOfFiniteType g] (k : ℤ) :
    chowGroup C (g ≫ (h ≫ sY)) k →+
      chowGroup C (pullback.fst (pullback.snd f h) g ≫ (pullback.fst f h ≫ sX)) (k - p)
```

**`Stacks.Chow.bivariantRestriction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Restriction.lean, line 1116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Restriction.lean#L1116).

> **Stacks 0F9Z.** The restriction `res(c)` of a bivariant class `c` of degree `p` for
> `f : X ⟶ Y` along `h : Y' ⟶ Y`: the bivariant class of degree `p` for the base change
> `X ×_Y Y' ⟶ Y'` with `res(c) ∩ α = c ∩ α`. Together with
> `Stacks.Chow.bivariantRestriction_add`, `_neg` and `_zero` this is the restriction map
> `A^p(X ⟶ Y) ⟶ A^p(X' ⟶ Y')` of the tag.
>
> The Gysin axiom of a restricted class is not a consequence of the axioms of `c`, so the
> construction carries the isomorphism case of Stacks 02TA for the Gysin system; see the
> implementation notes of `StacksFrontier.AlgebraicGeometry.Chow.Bivariant.Restriction`.

```lean
def bivariantRestriction (hgys : G.IsNaturalUnderBaseChangeIso)
    (c : BivariantClass C G sX sY f hf p) :
    BivariantClass C G (pullback.fst f h ≫ sX) (h ≫ sY) (pullback.snd f h)
      (pullbackSnd_comp_structureMorphism_eq C sX sY f hf h) p
```

**`Stacks.Chow.bivariantRestrictionAddHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Restriction.lean, line 1243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Restriction.lean#L1243).

> **Stacks 0F9Z.** The restriction map `A^p(X ⟶ Y) ⟶ A^p(X' ⟶ Y')` along `h : Y' ⟶ Y`, as a
> homomorphism of groups.

```lean
def bivariantRestrictionAddHom (hgys : G.IsNaturalUnderBaseChangeIso) :
    BivariantClass C G sX sY f hf p →+
      BivariantClass C G (pullback.fst f h ≫ sX) (h ≫ sY) (pullback.snd f h)
        (pullbackSnd_comp_structureMorphism_eq C sX sY f hf h) p
```

**`Stacks.Chow.bivariantRestrictionCap_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Restriction.lean, line 1343](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Restriction.lean#L1343). The attribute's comment: “compatibility with compositions, on cap operations”.

> **Stacks 0F9Z.** Restriction of a bivariant class is compatible with composition of base
> changes: if `c'` is the restriction of `c` along `h`, then the restriction of `c'` along `h'` caps
> exactly as the restriction of `c` along `h' ≫ h`, after the canonical identification of the two
> iterated fibre products.

```lean
theorem bivariantRestrictionCap_comp (c : BivariantClass C G sX sY f hf p)
    (c' : BivariantClass C G (pullback.fst f h ≫ sX) (h ≫ sY) (pullback.snd f h)
      (pullbackSnd_comp_structureMorphism_eq C sX sY f hf h) p)
    (hc' : IsBivariantRestriction C G sX sY f hf h p c c') {T : Scheme.{u}} (g : T ⟶ Y'')
    [LocallyOfFiniteType g] (k : ℤ) (α : chowGroup C (g ≫ (h' ≫ (h ≫ sY))) k) :
    chowPushforwardOfIso C
        (pullback.fst (pullback.snd (pullback.snd f h) h') g ≫
          (pullback.fst (pullback.snd f h) h' ≫ (pullback.fst f h ≫ sX)))
        (pullback.fst (pullback.snd f (h' ≫ h)) g ≫ (pullback.fst f (h' ≫ h) ≫ sX))
        (iteratedRestrictionIso f h h' g).hom
        (iteratedRestrictionIso_hom_comp C sX f h h' g) (k - p)
        (bivariantRestrictionCap C G (pullback.fst f h ≫ sX) (h ≫ sY) (pullback.snd f h)
          (pullbackSnd_comp_structureMorphism_eq C sX sY f hf h) h' p c' g k α) =
      bivariantRestrictionCap C G sX sY f hf (h' ≫ h) p c g k
        (chowGroupCongr C (congrArg (g ≫ ·) (Category.assoc h' h sY).symm) k α)
```

**`Stacks.Chow.bivariantRestriction_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Restriction.lean, line 1380](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Restriction.lean#L1380).

> **Stacks 0F9Z.** Restriction is compatible with composition of base changes: restricting
> along `h` and then along `h'` agrees with restricting along `h' ≫ h`, after the canonical
> identification of the two iterated fibre products.

```lean
theorem bivariantRestriction_comp (hgys : G.IsNaturalUnderBaseChangeIso)
    (c : BivariantClass C G sX sY f hf p) {T : Scheme.{u}} (g : T ⟶ Y'')
    [LocallyOfFiniteType g] (k : ℤ) (α : chowGroup C (g ≫ (h' ≫ (h ≫ sY))) k) :
    chowPushforwardOfIso C
        (pullback.fst (pullback.snd (pullback.snd f h) h') g ≫
          (pullback.fst (pullback.snd f h) h' ≫ (pullback.fst f h ≫ sX)))
        (pullback.fst (pullback.snd f (h' ≫ h)) g ≫ (pullback.fst f (h' ≫ h) ≫ sX))
        (iteratedRestrictionIso f h h' g).hom
        (iteratedRestrictionIso_hom_comp C sX f h h' g) (k - p)
        ((bivariantRestriction C G (pullback.fst f h ≫ sX) (h ≫ sY) (pullback.snd f h)
          (pullbackSnd_comp_structureMorphism_eq C sX sY f hf h) h' p hgys
          (bivariantRestriction C G sX sY f hf h p hgys c)).cap g k α) =
      (bivariantRestriction C G sX sY f hf (h' ≫ h) p hgys c).cap g k
        (chowGroupCongr C (congrArg (g ≫ ·) (Category.assoc h' h sY).symm) k α)
```

**`Stacks.Chow.isBivariantTransport_bivariantComposite_bivariantRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/RestrictionOfComposite.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/RestrictionOfComposite.lean#L73). The attribute's comment: “the clause `res(a ∘ b) = res(a) ∘ res(b)`: restriction commutes with the composition of bivariant classes of Tag 0B75, on cap operations, read through the comparison isomorphism of the two readings of the source fibre product. The compatibility with the composition of BASE CHANGES is the separate Stacks.Chow.bivariantRestrictionCap\_comp”.

> **Stacks 0F9Z, compatibility with the composition of bivariant classes.** The restriction of
> the composite `a ∘ b` of Stacks 0B75 along `h : W ⟶ Z` caps exactly as the composite of the
> restriction of `a` along `pullback.fst g h` with the restriction of `b` along `h`, read through
> the comparison isomorphism `X ×_Y (Y ×_Z W) ≅ X ×_Z W` of the two sources.

```lean
theorem isBivariantTransport_bivariantComposite_bivariantRestriction
    (hgys : G.IsNaturalUnderBaseChangeIso)
    (hgysc : G.IsNaturalUnderPullbackCompPushforward) :
    IsBivariantTransport C G (pullback.fst f (pullback.fst g h) ≫ sX)
      (pullback.fst (f ≫ g) h ≫ sX) (h ≫ sZ)
      (pullback.snd f (pullback.fst g h) ≫ pullback.snd g h)
      (comp_comp_structureMorphism_eq
        (pullbackSnd_comp_structureMorphism_eq C sX sY f hf (pullback.fst g h))
        (pullbackSnd_comp_structureMorphism_eq C sY sZ g hg h))
      (pullback.snd (f ≫ g) h)
      (pullbackSnd_comp_structureMorphism_eq C sX sZ (f ≫ g)
        (comp_comp_structureMorphism_eq hf hg) h)
      (pullbackRightPullbackFstIso g h f)
      (pullbackRightPullbackFstIso_hom_comp_snd f g h) (p + q)
      (bivariantComposite C G (pullback.fst f (pullback.fst g h) ≫ sX)
        (pullback.fst g h ≫ sY) (h ≫ sZ) (pullback.snd f (pullback.fst g h))
        (pullback.snd g h)
        (pullbackSnd_comp_structureMorphism_eq C sX sY f hf (pullback.fst g h))
        (pullbackSnd_comp_structureMorphism_eq C sY sZ g hg h) p q
        (bivariantRestriction C G sX sY f hf (pullback.fst g h) p hgys a)
        (bivariantRestriction C G sY sZ g hg h q hgys b) hgys hgysc)
      (bivariantRestriction C G sX sZ (f ≫ g) (comp_comp_structureMorphism_eq hf hg) h (p + q)
        hgys
        (bivariantComposite C G sX sY sZ f g hf hg p q a b hgys hgysc))
```

**`Stacks.Chow.bivariantTransport_bivariantComposite_bivariantRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/RestrictionOfComposite.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/RestrictionOfComposite.lean#L123). The attribute's comment: “the clause `res(a ∘ b) = res(a) ∘ res(b)` as an equality of bivariant classes, the composition being that of Tag 0B75 and the transport the comparison isomorphism of the two readings of the source fibre product”.

> **Stacks 0F9Z, compatibility with the composition of bivariant classes**, as an identity of
> bivariant classes: the transport along `X ×_Y (Y ×_Z W) ≅ X ×_Z W` of the composite of the
> restrictions is the restriction of the composite.

```lean
theorem bivariantTransport_bivariantComposite_bivariantRestriction
    (hgys : G.IsNaturalUnderBaseChangeIso)
    (hgysc : G.IsNaturalUnderPullbackCompPushforward) :
    bivariantTransport C G (pullback.fst f (pullback.fst g h) ≫ sX)
        (pullback.fst (f ≫ g) h ≫ sX) (h ≫ sZ)
        (pullback.snd f (pullback.fst g h) ≫ pullback.snd g h)
        (comp_comp_structureMorphism_eq
          (pullbackSnd_comp_structureMorphism_eq C sX sY f hf (pullback.fst g h))
          (pullbackSnd_comp_structureMorphism_eq C sY sZ g hg h))
        (pullback.snd (f ≫ g) h)
        (pullbackSnd_comp_structureMorphism_eq C sX sZ (f ≫ g)
          (comp_comp_structureMorphism_eq hf hg) h)
        (pullbackRightPullbackFstIso g h f)
        (pullbackRightPullbackFstIso_hom_comp_snd f g h) (p + q) hgys
        (bivariantComposite C G (pullback.fst f (pullback.fst g h) ≫ sX)
          (pullback.fst g h ≫ sY) (h ≫ sZ) (pullback.snd f (pullback.fst g h))
          (pullback.snd g h)
          (pullbackSnd_comp_structureMorphism_eq C sX sY f hf (pullback.fst g h))
          (pullbackSnd_comp_structureMorphism_eq C sY sZ g hg h) p q
          (bivariantRestriction C G sX sY f hf (pullback.fst g h) p hgys a)
          (bivariantRestriction C G sY sZ g hg h q hgys b) hgys hgysc) =
      bivariantRestriction C G sX sZ (f ≫ g) (comp_comp_structureMorphism_eq hf hg) h (p + q)
        hgys (bivariantComposite C G sX sY sZ f g hf hg p q a b hgys hgysc)
```

**`Stacks.Chow.completedBivariantRestrictionViaSequence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/CompletedRestrictionFlatCommute.lean, line 579](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/CompletedRestrictionFlatCommute.lean#L579). The attribute's comment: “the restriction on the completed bivariant groups A^*(X → Y)^∧ → A^*(X' → Y')^∧”.

> **Stacks 0F9Z on completions.** The restriction
> `res : A^*(X ⟶ Y)^∧ ⟶ A^*(X ×_Y Y' ⟶ Y')^∧` of completed bivariant classes (Stacks 0FE0) along
> `h : Y' ⟶ Y`, at the Gysin system of the first Chern class rule: reading an element of the
> completed group as the tuple `(c_p)_p` of Stacks 0FE0, it is the tuple `(res(c_p))_p` of the
> restrictions of Stacks 0F9Z, which again vanishes in almost all degrees on each connected
> component.

```lean
def completedBivariantRestrictionViaSequence :
    completedBivariantGroup C (gysinSystemOfInvertible C) sX sY f hf →+
      completedBivariantGroup C (gysinSystemOfInvertible C) (pullback.fst f h ≫ sX) (h ≫ sY)
        (pullback.snd f h) (pullbackSnd_comp_structureMorphism_eq C sX sY f hf h)
```

**`Stacks.Chow.bivariantRestrictionOfInvertible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Gysin42/BaseChangeIsoGysinSystem.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Gysin42/BaseChangeIsoGysinSystem.lean#L236).

> The restriction `res(c)` of a bivariant class `c ∈ A^p(X ⟶ Y)` along a morphism
> `b : Y' ⟶ Y`, for the Gysin system of the first Chern class rule of an invertible module: the
> bivariant class of degree `p` for the base change `X ×_Y Y' ⟶ Y'` with `res(c) ∩ α = c ∩ α`.

```lean
def bivariantRestrictionOfInvertible
    (c : BivariantClass C (gysinSystemOfInvertible C) sX sY f hf p) :
    BivariantClass C (gysinSystemOfInvertible C) (pullback.fst f b ≫ sX) (b ≫ sY)
      (pullback.snd f b) (pullbackSnd_comp_structureMorphism_eq C sX sY f hf b) p
```

**`Stacks.Chow.bivariantRestrictionOfInvertible_cap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Gysin42/BaseChangeIsoGysinSystem.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Gysin42/BaseChangeIsoGysinSystem.lean#L246).

> The restriction caps by the cap operation of `c`: `res(c) ∩ α = c ∩ α`, after the canonical
> identification of the two fibre products.

```lean
theorem bivariantRestrictionOfInvertible_cap
    (c : BivariantClass C (gysinSystemOfInvertible C) sX sY f hf p) {T : Scheme.{u}}
    (g : T ⟶ Y') [LocallyOfFiniteType g] (k : ℤ) (α : chowGroup C (g ≫ (b ≫ sY)) k) :
    (bivariantRestrictionOfInvertible C sX sY f hf b p c).cap g k α =
      bivariantRestrictionCap C (gysinSystemOfInvertible C) sX sY f hf b p c g k α
```

**`Stacks.Chow.bivariantRestrictionAddHomOfInvertible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Gysin42/BaseChangeIsoGysinSystem.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Gysin42/BaseChangeIsoGysinSystem.lean#L256).

> The restriction map `A^p(X ⟶ Y) ⟶ A^p(X' ⟶ Y')` along `b : Y' ⟶ Y`, as a homomorphism of
> groups, for the Gysin system of the first Chern class rule of an invertible module.

```lean
def bivariantRestrictionAddHomOfInvertible :
    BivariantClass C (gysinSystemOfInvertible C) sX sY f hf p →+
      BivariantClass C (gysinSystemOfInvertible C) (pullback.fst f b ≫ sX) (b ≫ sY)
        (pullback.snd f b) (pullbackSnd_comp_structureMorphism_eq C sX sY f hf b) p
```

**`Stacks.Chow.bivariantRestrictionOfInvertible_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Gysin42/BaseChangeIsoGysinSystem.lean, line 269](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Gysin42/BaseChangeIsoGysinSystem.lean#L269).

> Restriction is compatible with composition of base changes: restricting along `b` and then
> along `b'` agrees with restricting along `b' ≫ b`, after the canonical identification of the two
> iterated fibre products.

```lean
theorem bivariantRestrictionOfInvertible_comp
    (c : BivariantClass C (gysinSystemOfInvertible C) sX sY f hf p) {T : Scheme.{u}}
    (g : T ⟶ Y'') [LocallyOfFiniteType g] (k : ℤ) (α : chowGroup C (g ≫ (b' ≫ (b ≫ sY))) k) :
    chowPushforwardOfIso C
        (pullback.fst (pullback.snd (pullback.snd f b) b') g ≫
          (pullback.fst (pullback.snd f b) b' ≫ (pullback.fst f b ≫ sX)))
        (pullback.fst (pullback.snd f (b' ≫ b)) g ≫ (pullback.fst f (b' ≫ b) ≫ sX))
        (iteratedRestrictionIso f b b' g).hom
        (iteratedRestrictionIso_hom_comp C sX f b b' g) (k - p)
        ((bivariantRestrictionOfInvertible C (pullback.fst f b ≫ sX) (b ≫ sY)
          (pullback.snd f b) (pullbackSnd_comp_structureMorphism_eq C sX sY f hf b) b' p
          (bivariantRestrictionOfInvertible C sX sY f hf b p c)).cap g k α) =
      (bivariantRestrictionOfInvertible C sX sY f hf (b' ≫ b) p c).cap g k
        (chowGroupCongr C (congrArg (g ≫ ·) (Category.assoc b' b sY).symm) k α)
```

## Tag 0FA2, a remark

[Tag 0FA2](https://stacks.math.columbia.edu/tag/0FA2) in the Stacks Project.

**`Stacks.Chow.BivariantCommute`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Commuting.lean, line 282](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Commuting.lean#L282). The attribute's comment: “the definition of commuting bivariant classes”.

> Two bivariant classes `c₁ ∈ A^{p₁}(Z₁ ⟶ X)` and `c₂ ∈ A^{p₂}(Z₂ ⟶ X)` *commute* when
>
>   `c₁ ∩ c₂ ∩ α = c₂ ∩ c₁ ∩ α`
>
> for every morphism `t : T ⟶ X` locally of finite type and every `α ∈ CH_k(T)`; this is the
> identity for every `α ∈ CH_k(X)` and after every base change `X' ⟶ X` locally of finite type.
>
> The two sides live on the two iterated fibre products `Z₁ ×_X (Z₂ ×_X T)` and `Z₂ ×_X (Z₁ ×_X T)`
> and in the two degrees `(k - p₂) - p₁` and `(k - p₁) - p₂`; they are compared by pushing the
> first forward along `Stacks.Chow.commuteComparisonHom` and transporting the second along the
> equality of degrees.

```lean
def BivariantCommute : Prop
```

**`Stacks.Chow.bivariantCommute_iff_commuteCompositeCap_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Commuting.lean, line 416](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Commuting.lean#L416). The attribute's comment: “commuting is the equality of the two composites”.

> Two bivariant classes commute if and only if the cap operations of the two
> composites `res(c₁) ∘ c₂` and `res(c₂) ∘ c₁` agree, under the canonical identification
> `Z₁ ×_X Z₂ ≅ Z₂ ×_X Z₁` of their sources and the equality `p₁ + p₂ = p₂ + p₁` of their degrees.

```lean
theorem bivariantCommute_iff_commuteCompositeCap_eq :
    BivariantCommute C G sX f₁ f₂ p₁ p₂ c₁ c₂ ↔
      ∀ {T : Scheme.{u}} (t : T ⟶ X) [LocallyOfFiniteType t] (k : ℤ)
        (α : chowGroup C (t ≫ sX) k),
        chowPushforwardOfIso C
            (pullback.fst (pullback.snd f₁ f₂ ≫ f₂) t ≫ (pullback.fst f₁ f₂ ≫ (f₁ ≫ sX)))
            (pullback.fst (pullback.snd f₂ f₁ ≫ f₁) t ≫ (pullback.fst f₂ f₁ ≫ (f₂ ≫ sX)))
            (compositeComparisonHom f₁ f₂ t)
            (compositeComparisonHom_comp_structureMorphism C sX f₁ f₂ t) ((k - p₂) - p₁)
            (commuteCompositeCap C G sX f₁ f₂ p₁ p₂ c₁ c₂ hgys hpp t k α) =
          chowGroupDegreeEquiv C
            (pullback.fst (pullback.snd f₂ f₁ ≫ f₁) t ≫ (pullback.fst f₂ f₁ ≫ (f₂ ≫ sX)))
            (by ring : (k - p₁) - p₂ = (k - p₂) - p₁)
            (commuteCompositeCap C G sX f₂ f₁ p₂ p₁ c₂ c₁ hgys hpp t k α)
```

**`Stacks.Chow.bivariantCommute_iff_cap_eq_of_isBivariantClassComposition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Commuting.lean, line 439](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Commuting.lean#L439). The attribute's comment: “commuting is the equality of the two composite classes”.

> If `d₁` is the composite `res(c₁) ∘ c₂` and `d₂` is the composite `res(c₂) ∘ c₁` in the sense
> of Stacks 0FE0, then `c₁` and `c₂` commute exactly when `d₁` and `d₂` agree under the canonical
> identification `Z₁ ×_X Z₂ ≅ Z₂ ×_X Z₁`.

```lean
theorem bivariantCommute_iff_cap_eq_of_isBivariantClassComposition
    (d₁ : BivariantClass C G (pullback.fst f₁ f₂ ≫ (f₁ ≫ sX)) sX (pullback.snd f₁ f₂ ≫ f₂)
      (comp_comp_structureMorphism_eq
        (pullbackSnd_comp_structureMorphism_eq C (f₁ ≫ sX) sX f₁ rfl f₂) rfl) (p₁ + p₂))
    (d₂ : BivariantClass C G (pullback.fst f₂ f₁ ≫ (f₂ ≫ sX)) sX (pullback.snd f₂ f₁ ≫ f₁)
      (comp_comp_structureMorphism_eq
        (pullbackSnd_comp_structureMorphism_eq C (f₂ ≫ sX) sX f₂ rfl f₁) rfl) (p₂ + p₁))
    (h₁ : IsBivariantClassComposition C G (pullback.fst f₁ f₂ ≫ (f₁ ≫ sX)) (f₂ ≫ sX) sX
      (pullback.snd f₁ f₂) f₂
      (pullbackSnd_comp_structureMorphism_eq C (f₁ ≫ sX) sX f₁ rfl f₂) rfl hpp p₁ p₂
      (bivariantRestriction C G (f₁ ≫ sX) sX f₁ rfl f₂ p₁ hgys c₁) c₂ d₁)
    (h₂ : IsBivariantClassComposition C G (pullback.fst f₂ f₁ ≫ (f₂ ≫ sX)) (f₁ ≫ sX) sX
      (pullback.snd f₂ f₁) f₁
      (pullbackSnd_comp_structureMorphism_eq C (f₂ ≫ sX) sX f₂ rfl f₁) rfl hpp p₂ p₁
      (bivariantRestriction C G (f₂ ≫ sX) sX f₂ rfl f₁ p₂ hgys c₂) c₁ d₂) :
    BivariantCommute C G sX f₁ f₂ p₁ p₂ c₁ c₂ ↔
      ∀ {T : Scheme.{u}} (t : T ⟶ X) [LocallyOfFiniteType t] (k : ℤ)
        (α : chowGroup C (t ≫ sX) k),
        chowPushforwardOfIso C
            (pullback.fst (pullback.snd f₁ f₂ ≫ f₂) t ≫ (pullback.fst f₁ f₂ ≫ (f₁ ≫ sX)))
            (pullback.fst (pullback.snd f₂ f₁ ≫ f₁) t ≫ (pullback.fst f₂ f₁ ≫ (f₂ ≫ sX)))
            (compositeComparisonHom f₁ f₂ t)
            (compositeComparisonHom_comp_structureMorphism C sX f₁ f₂ t) ((k - p₂) - p₁)
            (chowGroupDegreeEquiv C
              (pullback.fst (pullback.snd f₁ f₂ ≫ f₂) t ≫ (pullback.fst f₁ f₂ ≫ (f₁ ≫ sX)))
              (by ring : k - (p₁ + p₂) = (k - p₂) - p₁) (d₁.cap t k α)) =
          chowGroupDegreeEquiv C
            (pullback.fst (pullback.snd f₂ f₁ ≫ f₁) t ≫ (pullback.fst f₂ f₁ ≫ (f₂ ≫ sX)))
            (by ring : k - (p₂ + p₁) = (k - p₂) - p₁) (d₂.cap t k α)
```

**`Stacks.Chow.bivariantCommute_iff_commuteCompositeOfInvertible_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/CommutingOfInvertible.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/CommutingOfInvertible.lean#L135). The attribute's comment: “commuting is the equality res(c₁) ∘ c₂ = res(c₂) ∘ c₁ of bivariant classes, at the canonical Gysin system, with nothing assumed”.

> **Stacks 0FA2.** Two bivariant classes `c₁ ∈ A^{p₁}(Z₁ ⟶ X)` and `c₂ ∈ A^{p₂}(Z₂ ⟶ X)` at
> the Gysin system of the first Chern class rule commute if and only if
>
>   `res(c₁) ∘ c₂ = res(c₂) ∘ c₁`   in   `A^{p₁ + p₂}(Z₁ ×_X Z₂ ⟶ X)`,
>
> where `res(cᵢ)` is the restriction of Stacks 0F9Z and `∘` the composition of Stacks 0B75. The
> right-hand side, a class in `A^{p₂ + p₁}(Z₂ ×_X Z₁ ⟶ X)`, is read in `A^{p₁ + p₂}(Z₁ ×_X Z₂ ⟶ X)`
> through the symmetry of the fibre product and the equality of degrees.

```lean
theorem bivariantCommute_iff_commuteCompositeOfInvertible_eq
    (c₁ : BivariantClass C (gysinSystemOfInvertible C) (f₁ ≫ sX) sX f₁ rfl p₁)
    (c₂ : BivariantClass C (gysinSystemOfInvertible C) (f₂ ≫ sX) sX f₂ rfl p₂) :
    BivariantCommute C (gysinSystemOfInvertible C) sX f₁ f₂ p₁ p₂ c₁ c₂ ↔
      commuteCompositeOfInvertible C sX f₁ f₂ p₁ p₂ c₁ c₂ =
        bivariantClassDegreeCongr C (gysinSystemOfInvertible C)
          (pullback.fst f₁ f₂ ≫ (f₁ ≫ sX)) sX (pullback.snd f₁ f₂ ≫ f₂)
          (comp_comp_structureMorphism_eq
            (pullbackSnd_comp_structureMorphism_eq C (f₁ ≫ sX) sX f₁ rfl f₂) rfl)
          (add_comm p₂ p₁)
          (bivariantTransport C (gysinSystemOfInvertible C) (pullback.fst f₂ f₁ ≫ (f₂ ≫ sX))
            (pullback.fst f₁ f₂ ≫ (f₁ ≫ sX)) sX (pullback.snd f₂ f₁ ≫ f₁)
            (comp_comp_structureMorphism_eq
              (pullbackSnd_comp_structureMorphism_eq C (f₂ ≫ sX) sX f₂ rfl f₁) rfl)
            (pullback.snd f₁ f₂ ≫ f₂)
            (comp_comp_structureMorphism_eq
              (pullbackSnd_comp_structureMorphism_eq C (f₁ ≫ sX) sX f₁ rfl f₂) rfl)
            (pullbackSymmetry f₂ f₁)
            (by rw [pullbackSymmetry_hom_comp_snd_assoc, pullback.condition]) (p₂ + p₁)
            (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso C)
            (commuteCompositeOfInvertible C sX f₂ f₁ p₂ p₁ c₂ c₁))
```

## Tag 0FA3, an example

[Tag 0FA3](https://stacks.math.columbia.edu/tag/0FA3) in the Stacks Project.

**`Stacks.Chow.gysinBivariantClass_bivariantCommute`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/GysinClassCommuting.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/GysinClassCommuting.lean#L70). The attribute's comment: “the Gysin class i^* of Stacks 0B79 commutes with every c ∈ A^p(Z → X), in the sense of Remark 0FA2”.

> **Stacks 0FA3.** Let `(S, δ)` be as in Situation 02QL, let `X` be locally of finite type over
> `S`, let `(𝓛, s, i : D ⟶ X)` be a triple as in Definition 02T8, let `f : Z ⟶ X` be locally of
> finite type and let `c ∈ A^p(Z ⟶ X)` be a bivariant class of Definition 0B76. Then the bivariant
> Gysin class `i^* ∈ A^1(D ⟶ X)` of Stacks 0B79 commutes with `c` in the sense of Remark 0FA2:
> `i^* ∩ (c ∩ α) = c ∩ (i^* ∩ α)` for every `α ∈ CH_k(T)` and every `T ⟶ X` locally of finite
> type, the two sides compared by the canonical isomorphism `D ×_X (Z ×_X T) ≅ Z ×_X (D ×_X T)`.
>
> This is a restatement of condition (3) of Definition 0B76 for `c`.

```lean
theorem gysinBivariantClass_bivariantCommute
    (c : BivariantChowClass C (f ≫ sX) sX f rfl p) :
    BivariantCommute C (gysinSystemOfInvertible C) sX (gysinTripleInclusion L s) f 1 p
      (gysinBivariantClass C sX L s).1 (BivariantChowClass.equivBivariantClass c)
```

**`Stacks.Chow.gysinBivariantClass_comp_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/GysinClassCommuting.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/GysinClassCommuting.lean#L91). The attribute's comment: “res(i^*) ∘ c = res(c) ∘ i^* in A^\{1+p}(D ×\_X Z → X), the form of Remark 0FA2 on composites”.

> **Stacks 0FA3, on composites.** In the situation of
> `Stacks.Chow.gysinBivariantClass_bivariantCommute`, with `i^* ∈ A^1(D ⟶ X)` the bivariant Gysin
> class of Stacks 0B79 and `c ∈ A^p(Z ⟶ X)`,
>
>   `res(i^*) ∘ c = res(c) ∘ i^*`   in   `A^{1+p}(D ×_X Z ⟶ X)`,
>
> which Remark 0FA2 identifies with the commutation of `i^*` and `c`. Here
> `res(i^*) ∈ A^1(D ×_X Z ⟶ Z)` and `res(c) ∈ A^p(Z ×_X D ⟶ D)` are the restrictions of
> Remark 0F9Z; the second composite lives on `Z ×_X D` and in degree `p + 1`, and is read on
> `D ×_X Z` through the canonical isomorphism and in degree `1 + p`.

```lean
theorem gysinBivariantClass_comp_comm {sZ : Z ⟶ C.S} [LocallyOfFiniteType sZ]
    (hZ : f ≫ sX = sZ) (c : BivariantChowClass C sZ sX f hZ p) :
    ((BivariantChowClass.equivBivariantClass.symm (gysinBivariantClass C sX L s).1).restrict f
        hZ).comp c =
      (((c.restrict (gysinTripleInclusion L s) rfl).comp
          (BivariantChowClass.equivBivariantClass.symm
            (gysinBivariantClass C sX L s).1)).degreeCongr (add_comm p 1)).transport
        (comp_comp_structureMorphism_eq (BivariantChowClass.restrict_structure_eq rfl f hZ) hZ)
        (pullbackSymmetry f (gysinTripleInclusion L s))
        (pullbackSymmetry_hom_comp_snd_comp (gysinTripleInclusion L s) f)
```

**`Stacks.Chow.gysinBivariantCommute`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/GysinCommuting.lean, line 599](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/GysinCommuting.lean#L599).

> **Stacks 0FA3.** Let `(𝓛, s, i : D ⟶ X)` be a triple as in Definition 02T8, let
> `f : Z ⟶ X` be locally of finite type and let `c ∈ A^p(Z ⟶ X)` be a bivariant class. Then the
> bivariant Gysin class `c' ∈ A^1(D ⟶ X)` of Stacks 0B79 commutes with `c` in the sense of
> Stacks 0FA2.
>
> This is a restatement of condition (3) of Definition 0B76: the two iterated cap operations are
> the two sides of `Stacks.Chow.BivariantClass.gysin_naturality` for `c` at the divisor pulled
> back to the test scheme.

```lean
theorem gysinBivariantCommute (hG : G.IsNaturalUnderPullbackCompPushforward)
    (c : BivariantClass C G (f ≫ sX) sX f rfl p)
    (c' : BivariantClass C G (gysinTripleInclusion L s ≫ sX) sX (gysinTripleInclusion L s) rfl 1)
    (hc' : IsGysinBivariantClass C G sX L s c') :
    BivariantCommute C G sX (gysinTripleInclusion L s) f 1 p c' c
```

## Tag 0FDU, a remark

[Tag 0FDU](https://stacks.math.columbia.edu/tag/0FDU) in the Stacks Project.

**`Stacks.Chow.GeneralizedBivariantClass`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Generalized.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Generalized.lean#L155).

> A generalized bivariant class of degree `p` for a diagram `X --x--> Z <--y-- Y` of schemes
> locally of finite type over the base: a rule assigning to every morphism `z' : Z' ⟶ Z` locally of
> finite type and every `k` an additive map `A_k(Z' ×_Z Y) ⟶ A_{k-p}(X ×_Z Z')`, natural for proper
> pushforward, for flat pullback of fixed relative dimension, and for the Gysin map of the zero
> scheme of a section of an invertible module on the test scheme, the Gysin maps being those of the
> `Stacks.Chow.GysinSystem` `G`. The group of all of them is denoted `A^p(X ⟶ Z ⟵ Y)`.

```lean
structure GeneralizedBivariantClass (C : ChowSituation.{u}) (G : GysinSystem C)
    {X Y Z : Scheme.{u}} (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S)
    [LocallyOfFiniteType sY] (sZ : Z ⟶ C.S) [LocallyOfFiniteType sZ] (x : X ⟶ Z)
    [LocallyOfFiniteType x] (y : Y ⟶ Z) [LocallyOfFiniteType y] (hx : x ≫ sZ = sX)
    (hy : y ≫ sZ = sY) (p : ℤ)
```

**`Stacks.Chow.properPushforwardGeneralizedBivariantClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/GeneralizedProperPushforward.lean, line 496](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/GeneralizedProperPushforward.lean#L496). The attribute's comment: “the example of the remark: for a proper f : X₂ ⟶ X₁, f\_* ∈ A^0(X₁ ⟶ X₁ ⟵ X₂), at the canonical Gysin system gysinSystemOfInvertible, with NOTHING ASSUMED”.

> For a proper morphism `f : X₂ ⟶ X₁` of schemes locally of finite type over the base, proper
> pushforward is a generalized bivariant class of degree `0` for the diagram
> `X₁ --id--> X₁ <--f-- X₂`:
>
>   `f_* ∈ A^0(X₁ ⟶ X₁ ⟵ X₂)`.
>
> On a test scheme `z' : Z' ⟶ X₁` its cap operation is proper pushforward
> `A_k(Z' ×_{X₁} X₂) ⟶ A_k(X₁ ×_{X₁} Z')` along the base change of `f`
> (`Stacks.Chow.properPushforwardGeneralizedBivariantClass_cap`). It is formed at the Gysin system of
> the first Chern class rule, `Stacks.Chow.gysinSystemOfInvertible`.

```lean
def properPushforwardGeneralizedBivariantClass :
    GeneralizedBivariantClass C (gysinSystemOfInvertible C) s₁ s₂ s₁ (𝟙 X₁) f
      (Category.id_comp s₁) hf 0
```

**`Stacks.Chow.properPushforwardGeneralizedBivariantClass_cap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/GeneralizedProperPushforward.lean, line 513](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/GeneralizedProperPushforward.lean#L513). The attribute's comment: “the class f\_* ∈ A^0(X₁ ⟶ X₁ ⟵ X₂) caps by proper pushforward along the base change of f”.

> The cap operation of `f_* ∈ A^0(X₁ ⟶ X₁ ⟵ X₂)` on a test scheme `z' : Z' ⟶ X₁` is proper
> pushforward along the base change `Z' ×_{X₁} X₂ ⟶ X₁ ×_{X₁} Z'` of `f`, read in degree `k - 0`.

```lean
theorem properPushforwardGeneralizedBivariantClass_cap {Z' : Scheme.{u}} (z' : Z' ⟶ X₁)
    [LocallyOfFiniteType z'] (k : ℤ) (α : chowGroup C (pullback.snd z' f ≫ s₂) k) :
    (properPushforwardGeneralizedBivariantClass C s₁ s₂ f hf).cap z' k α =
      chowGroupDegreeEquiv C (pullback.fst (𝟙 X₁) z' ≫ s₁) (sub_zero k).symm
        (properChowPushforward C (pullback.snd z' f ≫ s₂) (pullback.fst (𝟙 X₁) z' ≫ s₁)
          (generalizedProperPushforwardMap f z')
          (generalizedProperPushforwardMap_comp_structure C s₁ s₂ f hf z') k
          (properPushforwardDescends C _ _ _ _ _) α)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.33, Tag 0B75](https://stacks.math.columbia.edu/tag/0B75)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
