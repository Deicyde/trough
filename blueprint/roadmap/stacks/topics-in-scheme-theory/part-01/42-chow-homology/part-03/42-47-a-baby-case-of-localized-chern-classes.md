---
declaration: section
origin: cited
lean: Stacks.Chow.existsUnique_localizedChernClassOfClosedCover, Stacks.Chow.existsUnique_localizedPowerSumOfClosedCover, Stacks.Chow.closedCoverPowerSum, Stacks.Chow.closedCoverChernClass, Stacks.Chow.isClosedCoverExtension_closedCoverPowerSum, Stacks.Chow.eq_closedCoverPowerSum_of_isClosedCoverExtension, Stacks.Chow.isClosedCoverExtension_closedCoverChernClass, Stacks.Chow.eq_closedCoverChernClass_of_isClosedCoverExtension
statement: formalized
proof: formalized
---

# 42.47 A baby case of localized Chern classes

Section 42.47 of the Stacks Project, [Tag 0F9G](https://stacks.math.columbia.edu/tag/0F9G). 11 tags here are carried by 30 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0F9H, a lemma

[Tag 0F9H](https://stacks.math.columbia.edu/tag/0F9H) in the Stacks Project.

**`Stacks.Chow.existsUnique_localizedChernClassOfClosedCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BabyLocalizedChern/LocalizedChernClass.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BabyLocalizedChern/LocalizedChernClass.lean#L125). The attribute's comment: “the class c'_p(E₂) ∈ A^p(X₂ ⟶ X), existence and uniqueness of the bivariant class characterized by the two identities on every base change X' ⟶ X, for E₂|_{X₁ ∩ X₂} finite locally free of rank < p in degree 0”.

> **Stacks 0F9H, for the Chern classes.** Let `X` be locally of finite type over `S`, let
> `i_j : X_j ⟶ X` be closed immersions with `X = X₁ ∪ X₂` set theoretically, and let `E₂` be a
> perfect object of `D(𝒪_{X₂})` whose Chern classes are defined and such that `E₂|_{X₁ ∩ X₂}` is
> isomorphic to a finite locally free `𝒪_{X₁ ∩ X₂}`-module of rank `< p` sitting in cohomological
> degree `0`. Then there is a unique bivariant class `c'_p(E₂) ∈ A^p(X₂ ⟶ X)` such that, on every
> test scheme `g : X' ⟶ X` locally of finite type, with `i'_j : X'_j = X_j ×_X X' ⟶ X'`,
>
>   `c'_p(E₂) ∩ i'_{2,*} α₂ = c_p(E₂) ∩ α₂`  and  `c'_p(E₂) ∩ i'_{1,*} α₁ = 0`
>
> for all `α_j ∈ CH_k(X'_j)`; it is `Stacks.Chow.localizedChernClassOfClosedCover`.

```lean
theorem existsUnique_localizedChernClassOfClosedCover
    (_perfect : RingedSpace.IsPerfect.{u, u + 1} (X := X₂.toRingedSpace) E₂)
    (hres : ∃ M : (pullback i₁ i₂).Modules, IsFiniteLocallyFreeOfRankLT M p ∧
      Nonempty ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
          (pullback.snd i₁ i₂).toLRSHom.toShHom).obj E₂ ≅
        (DerivedCategory.singleFunctor (pullback i₁ i₂).Modules 0).obj M)) :
    ∃! c : BivariantClass C (gysinSystemOfInvertible C) (i₂ ≫ sX) sX i₂ rfl (p : ℤ),
      (∀ {T : Scheme.{u}} (g : T ⟶ X) [LocallyOfFiniteType g] (k : ℤ)
        (α : chowGroup C (pullback.fst i₂ g ≫ i₂ ≫ sX) k),
        c.cap g k (chowPush C (pullback.fst i₂ g ≫ i₂ ≫ sX) (g ≫ sX) (pullback.snd i₂ g)
            (pullbackSnd_comp_structureMorphism_eq C (i₂ ≫ sX) sX i₂ rfl g) k α) =
          (perfectChernClass C (i₂ ≫ sX) hE₂ p).idRule C (i₂ ≫ sX) (gysinSystemOfInvertible C)
            (pullback.fst i₂ g) k α) ∧
      (∀ {T : Scheme.{u}} (g : T ⟶ X) [LocallyOfFiniteType g] (k : ℤ)
        (α : chowGroup C (pullback.fst i₁ g ≫ i₁ ≫ sX) k),
        c.cap g k (chowPush C (pullback.fst i₁ g ≫ i₁ ≫ sX) (g ≫ sX) (pullback.snd i₁ g)
            (pullbackSnd_comp_structureMorphism_eq C (i₁ ≫ sX) sX i₁ rfl g) k α) = 0)
```

**`Stacks.Chow.existsUnique_localizedPowerSumOfClosedCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BabyLocalizedChern/LocalizedChernClass.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BabyLocalizedChern/LocalizedChernClass.lean#L179). The attribute's comment: “the class P'_p(E₂) ∈ A^p(X₂ ⟶ X), existence and uniqueness of the bivariant class characterized by the two identities on every base change X' ⟶ X, for E₂|_{X₁ ∩ X₂} zero”.

> **Stacks 0F9H, for the classes `P_p`.** Let `X` be locally of finite type over `S`, let
> `i_j : X_j ⟶ X` be closed immersions with `X = X₁ ∪ X₂` set theoretically, and let `E₂` be a
> perfect object of `D(𝒪_{X₂})` whose Chern classes are defined and whose restriction
> `E₂|_{X₁ ∩ X₂}` is zero. Then there is a unique bivariant class `P'_p(E₂) ∈ A^p(X₂ ⟶ X)` such
> that, on every test scheme `g : X' ⟶ X` locally of finite type, with
> `i'_j : X'_j = X_j ×_X X' ⟶ X'`,
>
>   `P'_p(E₂) ∩ i'_{2,*} α₂ = P_p(E₂) ∩ α₂`  and  `P'_p(E₂) ∩ i'_{1,*} α₁ = 0`
>
> for all `α_j ∈ CH_k(X'_j)`; it is `Stacks.Chow.localizedPowerSumOfClosedCover`. Here `P_p(E₂)` is
> the class of Definition 0F9E (2), `Stacks.Chow.perfectPowerSumComponent`: the class of Stacks 0GUD
> which restricts along every envelope presentation `(f, 𝓔^•)` of `E₂` to `∑ (-1)^n P_p(𝓔^n)`
> (`Stacks.Chow.existsUnique_perfectPowerSum`).

```lean
theorem existsUnique_localizedPowerSumOfClosedCover
    (perfect : RingedSpace.IsPerfect.{u, u + 1} (X := X₂.toRingedSpace) E₂)
    (hzero : IsZero ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
      (pullback.snd i₁ i₂).toLRSHom.toShHom).obj E₂)) :
    ∃! c : BivariantClass C (gysinSystemOfInvertible C) (i₂ ≫ sX) sX i₂ rfl (p : ℤ),
      (∀ {T : Scheme.{u}} (g : T ⟶ X) [LocallyOfFiniteType g] (k : ℤ)
        (α : chowGroup C (pullback.fst i₂ g ≫ i₂ ≫ sX) k),
        c.cap g k (chowPush C (pullback.fst i₂ g ≫ i₂ ≫ sX) (g ≫ sX) (pullback.snd i₂ g)
            (pullbackSnd_comp_structureMorphism_eq C (i₂ ≫ sX) sX i₂ rfl g) k α) =
          (perfectPowerSumComponent C (i₂ ≫ sX) hE₂ p).idRule C (i₂ ≫ sX)
            (gysinSystemOfInvertible C) (pullback.fst i₂ g) k α) ∧
      (∀ {T : Scheme.{u}} (g : T ⟶ X) [LocallyOfFiniteType g] (k : ℤ)
        (α : chowGroup C (pullback.fst i₁ g ≫ i₁ ≫ sX) k),
        c.cap g k (chowPush C (pullback.fst i₁ g ≫ i₁ ≫ sX) (g ≫ sX) (pullback.snd i₁ g)
            (pullbackSnd_comp_structureMorphism_eq C (i₁ ≫ sX) sX i₁ rfl g) k α) = 0)
```

**`Stacks.Chow.closedCoverPowerSum`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/BabyCase.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/BabyCase.lean#L148). The attribute's comment: “the class P'_p(E₂) in A^p(X₂ ⟶ X), for E₂ restricting to zero on X₁ ∩ X₂”.

> Let `i₁ : X₁ ⟶ X` and `i₂ : X₂ ⟶ X` be closed immersions whose images cover `X`, and let
> `E₂ ∈ D(𝒪_{X₂})` have defined Chern classes and restrict to zero on `X₁ ×_X X₂`. The class
> `P'_p(E₂) ∈ A^p(X₂ ⟶ X)` is the extension of `P_p(E₂) ∈ A^p(X₂)` along the closed cover
> (`Stacks.Chow.closedCoverExtension`): on a test scheme `T ⟶ X`, writing a class as
> `j_{1,*} α₁ + j_{2,*} α₂` along the base-changed cover, `P'_p(E₂) ∩ α = P_p(E₂) ∩ α₂`.

```lean
def closedCoverPowerSum (hcover : Set.range i₁ ∪ Set.range i₂ = Set.univ)
    (hzero : IsZero ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
      (pullback.snd i₁ i₂).toLRSHom.toShHom).obj E₂)) :
    BivariantClass C (gysinSystemOfInvertible C) sX₂ sX i₂ hi₂ p
```

**`Stacks.Chow.closedCoverChernClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/BabyCase.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/BabyCase.lean#L163). The attribute's comment: “the class c'_p(E₂) in A^p(X₂ ⟶ X), for E₂ restricting on X₁ ∩ X₂ to a finite locally free module of rank < p in degree 0”.

> Let `i₁ : X₁ ⟶ X` and `i₂ : X₂ ⟶ X` be closed immersions whose images cover `X`, and let
> `E₂ ∈ D(𝒪_{X₂})` have defined Chern classes and restrict on `X₁ ×_X X₂` to a finite locally free
> module of rank `< p` in degree `0`. The class `c'_p(E₂) ∈ A^p(X₂ ⟶ X)` is the extension of
> `c_p(E₂) ∈ A^p(X₂)` along the closed cover (`Stacks.Chow.closedCoverExtension`): on a test scheme
> `T ⟶ X`, writing a class as `j_{1,*} α₁ + j_{2,*} α₂` along the base-changed cover,
> `c'_p(E₂) ∩ α = c_p(E₂) ∩ α₂`.

```lean
def closedCoverChernClass (hcover : Set.range i₁ ∪ Set.range i₂ = Set.univ)
    (hrank : ∃ M : (pullback i₁ i₂).Modules, IsFiniteLocallyFreeOfRankLT M p ∧
      Nonempty ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
        (pullback.snd i₁ i₂).toLRSHom.toShHom).obj E₂ ≅
          (DerivedCategory.singleFunctor _ 0).obj M)) :
    BivariantClass C (gysinSystemOfInvertible C) sX₂ sX i₂ hi₂ p
```

**`Stacks.Chow.isClosedCoverExtension_closedCoverPowerSum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/BabyCase.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/BabyCase.lean#L184). The attribute's comment: “the two formulas P'_p(E₂) ∩ i_{2,*} α₂ = P_p(E₂) ∩ α₂ and P'_p(E₂) ∩ i_{1,*} α₁ = 0, after every base change”.

> On every test scheme `g : T ⟶ X` locally of finite type, `P'_p(E₂)` caps the classes pushed
> forward from `T ×_X X₂` as `P_p(E₂)` does, and kills the classes pushed forward from `T ×_X X₁`:
> `P'_p(E₂) ∩ i_{2,*} α₂ = P_p(E₂) ∩ α₂` and `P'_p(E₂) ∩ i_{1,*} α₁ = 0`.

```lean
theorem isClosedCoverExtension_closedCoverPowerSum :
    IsClosedCoverExtension C (gysinSystemOfInvertible C) sX i₁ i₂ sX₂ hi₂
      (perfectPowerSumComponent C sX₂ hE₂ p)
      (closedCoverPowerSum C sX i₁ i₂ sX₂ hi₂ hE₂ p hcover hzero)
```

**`Stacks.Chow.eq_closedCoverPowerSum_of_isClosedCoverExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/BabyCase.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/BabyCase.lean#L195). The attribute's comment: “uniqueness: P'_p(E₂) is the only class satisfying the two formulas after every base change”.

> A class of `A^p(X₂ ⟶ X)` satisfying the two formulas `c ∩ i_{2,*} α₂ = P_p(E₂) ∩ α₂` and
> `c ∩ i_{1,*} α₁ = 0` after every base change is `P'_p(E₂)`.

```lean
theorem eq_closedCoverPowerSum_of_isClosedCoverExtension
    {c : BivariantClass C (gysinSystemOfInvertible C) sX₂ sX i₂ hi₂ p}
    (hc : IsClosedCoverExtension C (gysinSystemOfInvertible C) sX i₁ i₂ sX₂ hi₂
      (perfectPowerSumComponent C sX₂ hE₂ p) c) :
    c = closedCoverPowerSum C sX i₁ i₂ sX₂ hi₂ hE₂ p hcover hzero
```

**`Stacks.Chow.isClosedCoverExtension_closedCoverChernClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/BabyCase.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/BabyCase.lean#L217). The attribute's comment: “the two formulas c'_p(E₂) ∩ i_{2,*} α₂ = c_p(E₂) ∩ α₂ and c'_p(E₂) ∩ i_{1,*} α₁ = 0, after every base change”.

> On every test scheme `g : T ⟶ X` locally of finite type, `c'_p(E₂)` caps the classes pushed
> forward from `T ×_X X₂` as `c_p(E₂)` does, and kills the classes pushed forward from `T ×_X X₁`:
> `c'_p(E₂) ∩ i_{2,*} α₂ = c_p(E₂) ∩ α₂` and `c'_p(E₂) ∩ i_{1,*} α₁ = 0`.

```lean
theorem isClosedCoverExtension_closedCoverChernClass :
    IsClosedCoverExtension C (gysinSystemOfInvertible C) sX i₁ i₂ sX₂ hi₂
      (perfectChernClass C sX₂ hE₂ p)
      (closedCoverChernClass C sX i₁ i₂ sX₂ hi₂ hE₂ p hcover hrank)
```

**`Stacks.Chow.eq_closedCoverChernClass_of_isClosedCoverExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/BabyCase.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/BabyCase.lean#L228). The attribute's comment: “uniqueness: c'_p(E₂) is the only class satisfying the two formulas after every base change”.

> A class of `A^p(X₂ ⟶ X)` satisfying the two formulas `c ∩ i_{2,*} α₂ = c_p(E₂) ∩ α₂` and
> `c ∩ i_{1,*} α₁ = 0` after every base change is `c'_p(E₂)`.

```lean
theorem eq_closedCoverChernClass_of_isClosedCoverExtension
    {c : BivariantClass C (gysinSystemOfInvertible C) sX₂ sX i₂ hi₂ p}
    (hc : IsClosedCoverExtension C (gysinSystemOfInvertible C) sX i₁ i₂ sX₂ hi₂
      (perfectChernClass C sX₂ hE₂ p) c) :
    c = closedCoverChernClass C sX i₁ i₂ sX₂ hi₂ hE₂ p hcover hrank
```

## Tag 0FAH, a lemma

[Tag 0FAH](https://stacks.math.columbia.edu/tag/0FAH) in the Stacks Project.

**`Stacks.Chow.eq_of_isClosedCoverLocalizedClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/ClosedCoverLocalizedClass.lean, line 284](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/ClosedCoverLocalizedClass.lean#L284). The attribute's comment: “the conclusion in full: the class of Stacks 0F9H in A^p(X_2 -> X) does not depend on the choice of X_1, in the form that two bivariant classes with the characterizing property of Stacks 0F9H for the covers X = X_1 cup X_2 and X = X_1' cup X_2 and for the same class on X_2 are equal. CARRIED, because the Chern classes of a perfect object are not constructed in this repository (only the uniqueness half of Stacks 0GUD is formalized): the class on X_2 that the localized class caps as is a parameter kappa in A^p(X_2), covering the P_p(E_2) and c_p(E_2) halves of the source at once, and the two localized classes are parameters satisfying the characterizing property of Stacks 0F9H rather than its output. NOT NEEDED, since that property is all the source's proof uses: that E_2 is perfect, that its Chern classes are defined, and that its restriction to X_1 cap X_2 resp. X_1' cap X_2 is zero resp. finite locally free of rank < p in degree 0.”.

> **Stacks 0FAH.** The localized class of Stacks 0F9H does not depend on the choice of `X₁`: if
> `c` has the characterizing property for the cover `X = X₁ ∪ X₂` and `c'` has it for the cover
> `X = X₁' ∪ X₂`, both with the same class `κ ∈ A^p(X₂)`, then `c = c'`.
>
> By Stacks 02UC it is enough that `c - c'` kill the fundamental class of every integral scheme
> `T` locally of finite type over `X`. Such a `T` is irreducible and covered by the base changes of
> the two closed subschemes of whichever cover, so for each cover one of the two pieces is the whole
> of `T`; being a surjective closed immersion into a reduced scheme that piece is an isomorphism,
> and `[T]` is the pushforward of the fundamental class of the piece. If the `X₂`-piece fills `T`
> then both classes cap `[T]` to `κ ∩ [T]`; otherwise the `X₁`-piece and the `X₁'`-piece both fill
> `T`, and both classes cap `[T]` to zero.

```lean
theorem eq_of_isClosedCoverLocalizedClass
    (hcover : Set.range i₁.base ∪ Set.range i₂.base = Set.univ)
    (hcover' : Set.range i₁'.base ∪ Set.range i₂.base = Set.univ)
    {κ : chowCohomologyComponent C G sX₂ p} {c c' : BivariantClass C G sX₂ sX i₂ hi₂ p}
    (hc : IsClosedCoverLocalizedClass C G sX sX₁ sX₂ i₁ hi₁ i₂ hi₂ p κ c)
    (hc' : IsClosedCoverLocalizedClass C G sX sX₁' sX₂ i₁' hi₁' i₂ hi₂ p κ c') :
    c = c'
```

## Tag 0GUG, a lemma

[Tag 0GUG](https://stacks.math.columbia.edu/tag/0GUG) in the Stacks Project.

**`Stacks.Chow.localizedChernClassOfClosedCover_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BabyLocalizedChern/LocalizedChernBaseChange.lean, line 460](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BabyLocalizedChern/LocalizedChernBaseChange.lean#L460). The attribute's comment: “the classes c'_p: c'_p(E'₂) built from X' = X'₁ ∪ X'₂ and E'₂ is the restriction of c'_p(E₂)”.

> **Stacks 0GUG, for the Chern classes.** In the situation of Stacks 0F9H, with `E₂|_{X₁ ∩ X₂}`
> finite locally free of rank `< p` in degree `0`, let `q : X' ⟶ X` be locally of finite type,
> let `X' = X'₁ ∪ X'₂` with `X'_j = X_j ×_X X'`, and let `E'₂ = (X'₂ ⟶ X₂)^* E₂`. Then `E'₂`
> satisfies the hypotheses of Stacks 0F9H for this cover, and the class `c'_p(E'₂) ∈ A^p(X'₂ ⟶ X')`
> constructed by Stacks 0F9H from `X' = X'₁ ∪ X'₂` and `E'₂` is the restriction (Remark 0F9Z) of
> `c'_p(E₂) ∈ A^p(X₂ ⟶ X)`.
>
> The restriction is a class for `X₂ ×_X X' ⟶ X'` whose source carries the structure morphism
> `X₂ ×_X X' ⟶ X₂ ⟶ S`, while the class of Stacks 0F9H at `X'` carries `X'₂ ⟶ X' ⟶ S`; the two are
> equal, and the restriction is read with the second one by `Stacks.Chow.bivariantTransport` along
> the identity.

```lean
theorem localizedChernClassOfClosedCover_baseChange
    (hres : ∃ M : (pullback i₁ i₂).Modules, IsFiniteLocallyFreeOfRankLT M p ∧
      Nonempty ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
          (pullback.snd i₁ i₂).toLRSHom.toShHom).obj E₂ ≅
        (DerivedCategory.singleFunctor (pullback i₁ i₂).Modules 0).obj M)) :
    localizedChernClassOfClosedCover C (q ≫ sX) (pullback.snd i₁ q) (pullback.snd i₂ q)
        (range_pullbackSnd_union_range_pullbackSnd i₁ i₂ hcover q)
        (hasDefinedChernClasses_baseChange i₂ hE₂ q) p
        (exists_iso_single_baseChange i₁ i₂ p q hres) =
      bivariantTransport C (gysinSystemOfInvertible C) (pullback.fst i₂ q ≫ i₂ ≫ sX)
        (pullback.snd i₂ q ≫ q ≫ sX) (q ≫ sX) (pullback.snd i₂ q)
        (pullbackSnd_comp_structureMorphism_eq C (i₂ ≫ sX) sX i₂ rfl q)
        (pullback.snd i₂ q) rfl (Iso.refl _) (Category.id_comp _) (p : ℤ)
        (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso C)
        (bivariantRestrictionOfInvertible C (i₂ ≫ sX) sX i₂ rfl q (p : ℤ)
          (localizedChernClassOfClosedCover C sX i₁ i₂ hcover hE₂ p hres))
```

**`Stacks.Chow.localizedPowerSumOfClosedCover_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BabyLocalizedChern/LocalizedChernBaseChange.lean, line 490](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BabyLocalizedChern/LocalizedChernBaseChange.lean#L490). The attribute's comment: “the classes P'_p: P'_p(E'₂) built from X' = X'₁ ∪ X'₂ and E'₂ is the restriction of P'_p(E₂)”.

> **Stacks 0GUG, for the classes `P_p`.** In the situation of Stacks 0F9H, with `E₂` perfect
> and `E₂|_{X₁ ∩ X₂}` zero, let `q : X' ⟶ X` be locally of finite type, let `X' = X'₁ ∪ X'₂` with
> `X'_j = X_j ×_X X'`, and let `E'₂ = (X'₂ ⟶ X₂)^* E₂`. Then `E'₂` satisfies the hypotheses of
> Stacks 0F9H for this cover, and the class `P'_p(E'₂) ∈ A^p(X'₂ ⟶ X')` constructed by Stacks 0F9H
> from `X' = X'₁ ∪ X'₂` and `E'₂` is the restriction (Remark 0F9Z) of `P'_p(E₂) ∈ A^p(X₂ ⟶ X)`,
> read with the structure morphism `X'₂ ⟶ X' ⟶ S` as in
> `Stacks.Chow.localizedChernClassOfClosedCover_baseChange`.

```lean
theorem localizedPowerSumOfClosedCover_baseChange
    (perfect : RingedSpace.IsPerfect.{u, u + 1} (X := X₂.toRingedSpace) E₂)
    (hzero : IsZero ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
      (pullback.snd i₁ i₂).toLRSHom.toShHom).obj E₂)) :
    localizedPowerSumOfClosedCover C (q ≫ sX) (pullback.snd i₁ q) (pullback.snd i₂ q)
        (range_pullbackSnd_union_range_pullbackSnd i₁ i₂ hcover q)
        (hasDefinedChernClasses_baseChange i₂ hE₂ q) p (isPerfect_baseChange i₂ q perfect)
        (isZero_baseChange i₁ i₂ q hzero) =
      bivariantTransport C (gysinSystemOfInvertible C) (pullback.fst i₂ q ≫ i₂ ≫ sX)
        (pullback.snd i₂ q ≫ q ≫ sX) (q ≫ sX) (pullback.snd i₂ q)
        (pullbackSnd_comp_structureMorphism_eq C (i₂ ≫ sX) sX i₂ rfl q)
        (pullback.snd i₂ q) rfl (Iso.refl _) (Category.id_comp _) (p : ℤ)
        (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso C)
        (bivariantRestrictionOfInvertible C (i₂ ≫ sX) sX i₂ rfl q (p : ℤ)
          (localizedPowerSumOfClosedCover C sX i₁ i₂ hcover hE₂ p perfect hzero))
```

## Tag 0F9I, a lemma

[Tag 0F9I](https://stacks.math.columbia.edu/tag/0F9I) in the Stacks Project.

**`Stacks.Chow.pushforward_localizedPowerSumOfClosedCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BabyLocalizedChern/PushforwardLocalizedClass.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BabyLocalizedChern/PushforwardLocalizedClass.lean#L156). The attribute's comment: “the classes P'_p: i_{2,*} ∘ P'_p(E₂) = P_p(E) for E|_{X₁} zero”.

> **Stacks 0F9I, for the classes `P_p`.** Let `X` be locally of finite type over `S`, let
> `i_j : X_j ⟶ X` be closed immersions with `X = X₁ ∪ X₂` set theoretically, and let `E` be a
> perfect object of `D(𝒪_X)` whose Chern classes are defined and whose restriction `E|_{X₁}` is
> zero. Then `E₂ = E|_{X₂}` satisfies the hypotheses of Stacks 0F9H with `E₂|_{X₁ ∩ X₂}` zero, and
>
>   `i_{2,*} ∘ P'_p(E₂) = P_p(E)`   in   `A^p(X)`,
>
> where `P'_p(E₂) ∈ A^p(X₂ ⟶ X)` is the class of Stacks 0F9H
> (`Stacks.Chow.localizedPowerSumOfClosedCover`), `i_{2,*} ∘ -` is the pushforward of
> Stacks 0EPK and `P_p(E)` is the class of Definition 0F9E (2).

```lean
theorem pushforward_localizedPowerSumOfClosedCover
    (perfect : RingedSpace.IsPerfect.{u, u + 1} (X := X.toRingedSpace) E)
    (hzero : IsZero ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
      i₁.toLRSHom.toShHom).obj E)) :
    canonicalBivariantProperPushforward C (i₂ ≫ sX) sX sX i₂ (𝟙 X) rfl (Category.id_comp sX)
        (p : ℤ)
        (bivariantClassCongr C (gysinSystemOfInvertible C) (i₂ ≫ sX) sX
          (Category.comp_id i₂).symm rfl
          (comp_comp_structureMorphism_eq rfl (Category.id_comp sX)) (p : ℤ)
          (localizedPowerSumOfClosedCover C sX i₁ i₂ hcover
            (hasDefinedChernClasses_derivedPullback i₂ hE) p
            (isPerfect_restriction i₂ perfect)
            (isZero_restriction_intersection i₁ i₂ hzero))) =
      perfectPowerSumComponent C sX hE p
```

**`Stacks.Chow.pushforward_localizedChernClassOfClosedCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BabyLocalizedChern/PushforwardLocalizedClass.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BabyLocalizedChern/PushforwardLocalizedClass.lean#L192). The attribute's comment: “the classes c'_p: i_{2,*} ∘ c'_p(E₂) = c_p(E) for E|_{X₁} finite locally free of rank < p in degree 0”.

> **Stacks 0F9I, for the Chern classes.** Let `X` be locally of finite type over `S`, let
> `i_j : X_j ⟶ X` be closed immersions with `X = X₁ ∪ X₂` set theoretically, and let `E` be a
> perfect object of `D(𝒪_X)` whose Chern classes are defined and whose restriction `E|_{X₁}` is
> isomorphic to a finite locally free `𝒪_{X₁}`-module of rank `< p` sitting in cohomological
> degree `0`. Then `E₂ = E|_{X₂}` satisfies the hypotheses of Stacks 0F9H with `E₂|_{X₁ ∩ X₂}`
> finite locally free of rank `< p` in degree `0`, and
>
>   `i_{2,*} ∘ c'_p(E₂) = c_p(E)`   in   `A^p(X)`,
>
> where `c'_p(E₂) ∈ A^p(X₂ ⟶ X)` is the class of Stacks 0F9H
> (`Stacks.Chow.localizedChernClassOfClosedCover`), `i_{2,*} ∘ -` is the pushforward of
> Stacks 0EPK and `c_p(E)` is the class of Definition 0F9E (2).

```lean
theorem pushforward_localizedChernClassOfClosedCover
    (_perfect : RingedSpace.IsPerfect.{u, u + 1} (X := X.toRingedSpace) E)
    (hres : ∃ M : X₁.Modules, IsFiniteLocallyFreeOfRankLT M p ∧
      Nonempty ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
          i₁.toLRSHom.toShHom).obj E ≅ (DerivedCategory.singleFunctor X₁.Modules 0).obj M)) :
    canonicalBivariantProperPushforward C (i₂ ≫ sX) sX sX i₂ (𝟙 X) rfl (Category.id_comp sX)
        (p : ℤ)
        (bivariantClassCongr C (gysinSystemOfInvertible C) (i₂ ≫ sX) sX
          (Category.comp_id i₂).symm rfl
          (comp_comp_structureMorphism_eq rfl (Category.id_comp sX)) (p : ℤ)
          (localizedChernClassOfClosedCover C sX i₁ i₂ hcover
            (hasDefinedChernClasses_derivedPullback i₂ hE) p
            (exists_iso_single_restriction_intersection i₁ i₂ p hres))) =
      perfectChernClass C sX hE p
```

**`Stacks.Chow.properPushforwardChowCohomology_closedCoverPowerSum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/BabyCase.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/BabyCase.lean#L268). The attribute's comment: “the case of P'_p: i_{2,*} ∘ P'_p(E₂) = P_p(E) for E₂ = E|_{X₂} and E|_{X₁} zero”.

> Let `i₁ : X₁ ⟶ X` and `i₂ : X₂ ⟶ X` be closed immersions whose images cover `X`, and let
> `E ∈ D(𝒪_X)` have defined Chern classes and restrict to zero on `X₁`. Let `E₂ = E|_{X₂}` be as in
> Stacks 0F9H: it restricts to zero on `X₁ ×_X X₂`, and its Chern classes are defined by
> `Stacks.Chow.HasDefinedChernClasses.derivedPullback`. Then `i_{2,*} ∘ P'_p(E₂) = P_p(E)` in
> `A^p(X)`, with `i_{2,*} ∘ -` the pushforward of Stacks 0EPK.

```lean
theorem properPushforwardChowCohomology_closedCoverPowerSum
    (hcover : Set.range i₁ ∪ Set.range i₂ = Set.univ)
    (hzero : IsZero ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
      i₁.toLRSHom.toShHom).obj E))
    (hzero₂ : IsZero ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
      (pullback.snd i₁ i₂).toLRSHom.toShHom).obj
        ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
          i₂.toLRSHom.toShHom).obj E))) :
    properPushforwardChowCohomology C sX (i₂ ≫ sX) i₂ rfl
        (closedCoverPowerSum C sX i₁ i₂ (i₂ ≫ sX) rfl (hE.derivedPullback i₂) p hcover
          hzero₂) =
      perfectPowerSumComponent C sX hE p
```

**`Stacks.Chow.properPushforwardChowCohomology_closedCoverChernClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/BabyCase.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/BabyCase.lean#L295). The attribute's comment: “the case of c'_p: i_{2,*} ∘ c'_p(E₂) = c_p(E) for E₂ = E|_{X₂} and E|_{X₁} finite locally free of rank < p in degree 0”.

> Let `i₁ : X₁ ⟶ X` and `i₂ : X₂ ⟶ X` be closed immersions whose images cover `X`, and let
> `E ∈ D(𝒪_X)` have defined Chern classes and restrict on `X₁` to a finite locally free module of rank
> `< p` in degree `0`. Let `E₂ = E|_{X₂}` be as in Stacks 0F9H: it restricts on `X₁ ×_X X₂` to a
> finite locally free module of rank `< p` in degree `0`, and its Chern classes are defined by
> `Stacks.Chow.HasDefinedChernClasses.derivedPullback`. Then `i_{2,*} ∘ c'_p(E₂) = c_p(E)` in
> `A^p(X)`, with `i_{2,*} ∘ -` the pushforward of Stacks 0EPK.

```lean
theorem properPushforwardChowCohomology_closedCoverChernClass
    (hcover : Set.range i₁ ∪ Set.range i₂ = Set.univ)
    (hrank : ∃ M : X₁.Modules, IsFiniteLocallyFreeOfRankLT M p ∧
      Nonempty ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
        i₁.toLRSHom.toShHom).obj E ≅ (DerivedCategory.singleFunctor _ 0).obj M))
    (hrank₂ : ∃ M : (pullback i₁ i₂).Modules, IsFiniteLocallyFreeOfRankLT M p ∧
      Nonempty ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
        (pullback.snd i₁ i₂).toLRSHom.toShHom).obj
          ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
            i₂.toLRSHom.toShHom).obj E) ≅
          (DerivedCategory.singleFunctor _ 0).obj M)) :
    properPushforwardChowCohomology C sX (i₂ ≫ sX) i₂ rfl
        (closedCoverChernClass C sX i₁ i₂ (i₂ ≫ sX) rfl (hE.derivedPullback i₂) p hcover
          hrank₂) =
      perfectChernClass C sX hE p
```

## Tag 0FAI, a lemma

[Tag 0FAI](https://stacks.math.columbia.edu/tag/0FAI) in the Stacks Project.

**`Stacks.Chow.canonicalBivariantProperPushforward_localizedPowerSumOfClosedCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BabyLocalizedChern/ShrinkLocalizedClass.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BabyLocalizedChern/ShrinkLocalizedClass.lean#L202). The attribute's comment: “the classes P'_p: (X₂' ⟶ X₂)_* ∘ P'_p(E₂|_{X₂'}) = P'_p(E₂) for E₂|_{X₁' ∩ X₂} zero”.

> **Stacks 0FAI, for the classes `P_p`.** In the situation of Stacks 0F9H — closed immersions
> `i_j : X_j ⟶ X` with `X = X₁ ∪ X₂` set theoretically, and `E₂ ∈ D(𝒪_{X₂})` perfect with
> defined Chern classes and `E₂|_{X₁ ∩ X₂}` zero — let `X₂' ⊂ X₂` and `X₁ ⊂ X₁' ⊂ X` be closed
> subschemes with `X = X₁' ∪ X₂'` set theoretically, and assume `E₂|_{X₁' ∩ X₂}` is zero. Then
>
>   `(X₂' ⟶ X₂)_* ∘ P'_p(E₂|_{X₂'}) = P'_p(E₂)`   in   `A^p(X₂ ⟶ X)`,
>
> where `P'_p(E₂|_{X₂'}) ∈ A^p(X₂' ⟶ X)` is the class of Stacks 0F9H for the cover
> `X = X₁' ∪ X₂'` (`Stacks.Chow.localizedPowerSumOfClosedCover`), `P'_p(E₂)` the one for
> `X = X₁ ∪ X₂`, and `(X₂' ⟶ X₂)_* ∘ -` the proper pushforward of Stacks 0EPK.

```lean
theorem canonicalBivariantProperPushforward_localizedPowerSumOfClosedCover
    (hcover : Set.range i₁.base ∪ Set.range i₂.base = Set.univ)
    (perfect : RingedSpace.IsPerfect.{u, u + 1} (X := X₂.toRingedSpace) E₂)
    (hzero : IsZero ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
      (pullback.snd i₁ i₂).toLRSHom.toShHom).obj E₂))
    (_hX₁ : ∃ ι : X₁ ⟶ X₁', ι ≫ i₁' = i₁)
    (hcover' : Set.range i₁'.base ∪ Set.range (j ≫ i₂).base = Set.univ)
    (hzero' : IsZero ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
      (pullback.snd i₁' i₂).toLRSHom.toShHom).obj E₂)) :
    canonicalBivariantProperPushforward C ((j ≫ i₂) ≫ sX) (i₂ ≫ sX) sX j i₂
        (Category.assoc j i₂ sX).symm rfl (p : ℤ)
        (localizedPowerSumOfClosedCover C sX i₁' (j ≫ i₂) hcover'
          (hasDefinedChernClasses_derivedPullback j hE₂) p (isPerfect_shrink j perfect)
          (isZero_shrink i₁' i₂ j hzero')) =
      localizedPowerSumOfClosedCover C sX i₁ i₂ hcover hE₂ p perfect hzero
```

**`Stacks.Chow.canonicalBivariantProperPushforward_localizedChernClassOfClosedCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BabyLocalizedChern/ShrinkLocalizedClass.lean, line 254](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BabyLocalizedChern/ShrinkLocalizedClass.lean#L254). The attribute's comment: “the classes c'_p: (X₂' ⟶ X₂)_* ∘ c'_p(E₂|_{X₂'}) = c'_p(E₂) for E₂|_{X₁' ∩ X₂} finite locally free of rank < p in degree 0”.

> **Stacks 0FAI, for the Chern classes.** In the situation of Stacks 0F9H — closed immersions
> `i_j : X_j ⟶ X` with `X = X₁ ∪ X₂` set theoretically, and `E₂ ∈ D(𝒪_{X₂})` perfect with
> defined Chern classes and `E₂|_{X₁ ∩ X₂}` isomorphic to a finite locally free module of rank
> `< p` in degree `0` — let `X₂' ⊂ X₂` and `X₁ ⊂ X₁' ⊂ X` be closed subschemes with
> `X = X₁' ∪ X₂'` set theoretically, and assume `E₂|_{X₁' ∩ X₂}` is isomorphic to a finite locally
> free module of rank `< p` placed in degree `0`. Then
>
>   `(X₂' ⟶ X₂)_* ∘ c'_p(E₂|_{X₂'}) = c'_p(E₂)`   in   `A^p(X₂ ⟶ X)`,
>
> where `c'_p(E₂|_{X₂'}) ∈ A^p(X₂' ⟶ X)` is the class of Stacks 0F9H for the cover
> `X = X₁' ∪ X₂'` (`Stacks.Chow.localizedChernClassOfClosedCover`), `c'_p(E₂)` the one for
> `X = X₁ ∪ X₂`, and `(X₂' ⟶ X₂)_* ∘ -` the proper pushforward of Stacks 0EPK.

```lean
theorem canonicalBivariantProperPushforward_localizedChernClassOfClosedCover
    (hcover : Set.range i₁.base ∪ Set.range i₂.base = Set.univ)
    (_perfect : RingedSpace.IsPerfect.{u, u + 1} (X := X₂.toRingedSpace) E₂)
    (hres : ∃ M : (pullback i₁ i₂).Modules, IsFiniteLocallyFreeOfRankLT M p ∧
      Nonempty ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
          (pullback.snd i₁ i₂).toLRSHom.toShHom).obj E₂ ≅
        (DerivedCategory.singleFunctor (pullback i₁ i₂).Modules 0).obj M))
    (_hX₁ : ∃ ι : X₁ ⟶ X₁', ι ≫ i₁' = i₁)
    (hcover' : Set.range i₁'.base ∪ Set.range (j ≫ i₂).base = Set.univ)
    (hres' : ∃ M : (pullback i₁' i₂).Modules, IsFiniteLocallyFreeOfRankLT M p ∧
      Nonempty ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
          (pullback.snd i₁' i₂).toLRSHom.toShHom).obj E₂ ≅
        (DerivedCategory.singleFunctor (pullback i₁' i₂).Modules 0).obj M)) :
    canonicalBivariantProperPushforward C ((j ≫ i₂) ≫ sX) (i₂ ≫ sX) sX j i₂
        (Category.assoc j i₂ sX).symm rfl (p : ℤ)
        (localizedChernClassOfClosedCover C sX i₁' (j ≫ i₂) hcover'
          (hasDefinedChernClasses_derivedPullback j hE₂) p
          (exists_iso_single_shrink i₁' i₂ j p hres')) =
      localizedChernClassOfClosedCover C sX i₁ i₂ hcover hE₂ p hres
```

## Tag 0FAJ, a lemma

[Tag 0FAJ](https://stacks.math.columbia.edu/tag/0FAJ) in the Stacks Project.

**`Stacks.Chow.comp_localizedChernClassOfClosedCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BabyLocalizedChern/LocalizedChernComposite.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BabyLocalizedChern/LocalizedChernComposite.lean#L181). The attribute's comment: “the classes c'_p: c ∘ c'_p(E₂) = c'_p(Lf₂^*E₂) ∘ c for every bivariant class c in A^r(Y → X), f : Y → X locally of finite type, the composites read as in Remark 0FA2”.

> **Stacks 0FAJ, for the classes `c'_p`.** Let `X` be locally of finite type over `S`, let
> `i_j : X_j ⟶ X` be closed immersions with `X = X₁ ∪ X₂` set theoretically, and let
> `E₂ ∈ D(𝒪_{X₂})` be an object whose Chern classes are defined and whose restriction to
> `X₁ ∩ X₂` is isomorphic to a finite locally free module of rank `< p` in degree `0`, so that
> Stacks 0F9H gives `c'_p(E₂) ∈ A^p(X₂ ⟶ X)`. Let `f : Y ⟶ X` be locally of finite type and
> `c ∈ A^r(Y ⟶ X)`. Then
>
>   `c ∘ c'_p(E₂) = c'_p(Lf₂^*E₂) ∘ c`,
>
> where `f₂ : X₂ ×_X Y ⟶ X₂` is the base change of `f` and `c'_p(Lf₂^*E₂) ∈ A^p(X₂ ×_X Y ⟶ Y)` is
> the class of Stacks 0F9H for the cover of `Y` by the base changes `X_j ×_X Y` and the derived
> pullback `Lf₂^*E₂` (which satisfies the hypotheses of Stacks 0F9H by
> `Stacks.Chow.hasDefinedChernClasses_baseChange` and `Stacks.Chow.exists_iso_single_baseChange`).
> The left side is `res(c) ∘ c'_p(E₂)`, a class for `Y ×_X X₂ ⟶ X` of degree `r + p`; the right side,
> a class for `X₂ ×_X Y ⟶ X` of degree `p + r`, is read on `Y ×_X X₂` through the symmetry of the
> fibre product. Perfectness of `E₂`, assumed in Stacks 0F9H, is not used for `c'_p`.

```lean
theorem comp_localizedChernClassOfClosedCover
    (hres : ∃ M : (pullback i₁ i₂).Modules, IsFiniteLocallyFreeOfRankLT M p ∧
      Nonempty ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
          (pullback.snd i₁ i₂).toLRSHom.toShHom).obj E₂ ≅
        (DerivedCategory.singleFunctor (pullback i₁ i₂).Modules 0).obj M))
    (c : BivariantChowClass C (f ≫ sX) sX f rfl r) :
    (c.restrict i₂ rfl).comp (BivariantChowClass.equivBivariantClass.symm
        (localizedChernClassOfClosedCover C sX i₁ i₂ hcover hE₂ p hres)) =
      (((BivariantChowClass.equivBivariantClass.symm
          (localizedChernClassOfClosedCover C (f ≫ sX) (pullback.snd i₁ f) (pullback.snd i₂ f)
            (range_pullbackSnd_union_range_pullbackSnd i₁ i₂ hcover f)
            (hasDefinedChernClasses_baseChange i₂ hE₂ f) p
            (exists_iso_single_baseChange i₁ i₂ p f hres))).comp c).degreeCongr
        (add_comm (p : ℤ) r)).transport
        (comp_comp_structureMorphism_eq (BivariantChowClass.restrict_structure_eq rfl i₂ rfl) rfl)
        (pullbackSymmetry i₂ f) (pullbackSymmetry_hom_comp_snd_comp f i₂)
```

**`Stacks.Chow.comp_localizedPowerSumOfClosedCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BabyLocalizedChern/LocalizedChernComposite.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BabyLocalizedChern/LocalizedChernComposite.lean#L216). The attribute's comment: “the classes P'_p: c ∘ P'_p(E₂) = P'_p(Lf₂^*E₂) ∘ c for every bivariant class c in A^r(Y → X), f : Y → X locally of finite type, the composites read as in Remark 0FA2”.

> **Stacks 0FAJ, for the classes `P'_p`.** Let `X` be locally of finite type over `S`, let
> `i_j : X_j ⟶ X` be closed immersions with `X = X₁ ∪ X₂` set theoretically, and let
> `E₂ ∈ D(𝒪_{X₂})` be a perfect object whose Chern classes are defined and whose restriction to
> `X₁ ∩ X₂` is zero, so that Stacks 0F9H gives `P'_p(E₂) ∈ A^p(X₂ ⟶ X)`. Let `f : Y ⟶ X` be
> locally of finite type and `c ∈ A^r(Y ⟶ X)`. Then
>
>   `c ∘ P'_p(E₂) = P'_p(Lf₂^*E₂) ∘ c`,
>
> where `f₂ : X₂ ×_X Y ⟶ X₂` is the base change of `f` and `P'_p(Lf₂^*E₂) ∈ A^p(X₂ ×_X Y ⟶ Y)` is
> the class of Stacks 0F9H for the cover of `Y` by the base changes `X_j ×_X Y` and the derived
> pullback `Lf₂^*E₂`, the composites being read as in
> `Stacks.Chow.comp_localizedChernClassOfClosedCover`.

```lean
theorem comp_localizedPowerSumOfClosedCover
    (perfect : RingedSpace.IsPerfect.{u, u + 1} (X := X₂.toRingedSpace) E₂)
    (hzero : IsZero ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
      (pullback.snd i₁ i₂).toLRSHom.toShHom).obj E₂))
    (c : BivariantChowClass C (f ≫ sX) sX f rfl r) :
    (c.restrict i₂ rfl).comp (BivariantChowClass.equivBivariantClass.symm
        (localizedPowerSumOfClosedCover C sX i₁ i₂ hcover hE₂ p perfect hzero)) =
      (((BivariantChowClass.equivBivariantClass.symm
          (localizedPowerSumOfClosedCover C (f ≫ sX) (pullback.snd i₁ f) (pullback.snd i₂ f)
            (range_pullbackSnd_union_range_pullbackSnd i₁ i₂ hcover f)
            (hasDefinedChernClasses_baseChange i₂ hE₂ f) p (isPerfect_baseChange i₂ f perfect)
            (isZero_baseChange i₁ i₂ f hzero))).comp c).degreeCongr
        (add_comm (p : ℤ) r)).transport
        (comp_comp_structureMorphism_eq (BivariantChowClass.restrict_structure_eq rfl i₂ rfl) rfl)
        (pullbackSymmetry i₂ f) (pullbackSymmetry_hom_comp_snd_comp f i₂)
```

**`Stacks.Chow.nonhomogeneousBivariantTransport_compositeOfInvertible_closedCoverPowerSum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/BabyCaseCommute.lean, line 674](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/BabyCaseCommute.lean#L674). The attribute's comment: “for P'_p: c ∘ P'_p(E₂) = P'_p(Lf₂^*E₂) ∘ c in A^*(Y₂ → X), for every c in A^*(Y → X)”.

> Let `i₁ : X₁ ⟶ X`, `i₂ : X₂ ⟶ X` be closed immersions covering `X`, let `E₂ ∈ D(𝒪_{X₂})` have
> defined Chern classes and restrict to zero on `X₁ ∩ X₂`, let `f : Y ⟶ X` be locally of finite type
> and let `c ∈ A^*(Y ⟶ X)`. Then
>
>   `c ∘ P'_p(E₂) = P'_p(Lf₂^*E₂) ∘ c`   in   `A^*(Y₂ ⟶ X)`,
>
> where `Y₂ = X₂ ×_X Y`, `f₂ : Y₂ ⟶ X₂` is the base change of `f`, `P'_p(Lf₂^*E₂) ∈ A^p(Y₂ ⟶ Y)` is
> the class of Stacks 0F9H for the base-changed cover of `Y`, and `c ∘ P'_p(E₂)` is the composite of
> the restriction of `c` to `X₂` with `P'_p(E₂)`, carried from `Y ×_X X₂` to `Y₂`.

```lean
theorem nonhomogeneousBivariantTransport_compositeOfInvertible_closedCoverPowerSum
    (hzero : IsZero ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
      (pullback.snd i₁ i₂).toLRSHom.toShHom).obj E₂))
    (c : nonhomogeneousBivariantGroup C (gysinSystemOfInvertible C) (f ≫ sX) sX f rfl) :
    nonhomogeneousBivariantTransport C (gysinSystemOfInvertible C)
        (pullback.fst f i₂ ≫ (f ≫ sX)) (pullback.fst i₂ f ≫ (i₂ ≫ sX)) sX
        (pullback.snd f i₂ ≫ i₂)
        (comp_comp_structureMorphism_eq
          (pullbackSnd_comp_structureMorphism_eq C (f ≫ sX) sX f rfl i₂) rfl)
        (pullback.snd i₂ f ≫ f)
        (comp_comp_structureMorphism_eq
          (pullbackSnd_comp_structureMorphism_eq C (i₂ ≫ sX) sX i₂ rfl f) rfl)
        (pullbackSymmetry f i₂) (by simp [pullback.condition])
        (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso C)
        (nonhomogeneousBivariantCompositeOfInvertible C (pullback.fst f i₂ ≫ (f ≫ sX)) (i₂ ≫ sX)
          sX (pullback.snd f i₂) i₂
          (pullbackSnd_comp_structureMorphism_eq C (f ≫ sX) sX f rfl i₂) rfl
          (nonhomogeneousBivariantRestriction C (gysinSystemOfInvertible C) (f ≫ sX) sX f rfl i₂
            (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso C) c)
          (DirectSum.of _ (p : ℤ)
            (closedCoverPowerSum C sX i₁ i₂ (i₂ ≫ sX) rfl hE₂ p hcover hzero))) =
      nonhomogeneousBivariantCompositeOfInvertible C (pullback.fst i₂ f ≫ (i₂ ≫ sX)) (f ≫ sX) sX
        (pullback.snd i₂ f) f
        (pullbackSnd_comp_structureMorphism_eq C (i₂ ≫ sX) sX i₂ rfl f) rfl
        (DirectSum.of _ (p : ℤ)
          (closedCoverPowerSum C (f ≫ sX) (pullback.snd i₁ f) (pullback.snd i₂ f)
            (pullback.fst i₂ f ≫ (i₂ ≫ sX))
            (pullbackSnd_comp_structureMorphism_eq C (i₂ ≫ sX) sX i₂ rfl f)
            (hE₂.derivedPullback (pullback.fst i₂ f)) p
            (range_pullbackSnd_union_eq_univ i₁ i₂ hcover f)
            (isZero_derivedPullback_of_isZero_of_comp_eq
              (pullbackLift_comp_pullbackSnd_eq_pullbackSnd_comp_pullbackFst i₁ i₂ f) hzero)))
        c
```

**`Stacks.Chow.nonhomogeneousBivariantTransport_compositeOfInvertible_closedCoverChernClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/BabyCaseCommute.lean, line 725](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/BabyCaseCommute.lean#L725). The attribute's comment: “for c'_p: c ∘ c'_p(E₂) = c'_p(Lf₂^*E₂) ∘ c in A^*(Y₂ → X), for every c in A^*(Y → X)”.

> Let `i₁ : X₁ ⟶ X`, `i₂ : X₂ ⟶ X` be closed immersions covering `X`, let `E₂ ∈ D(𝒪_{X₂})` have
> defined Chern classes and restrict on `X₁ ∩ X₂` to a finite locally free module of rank `< p` in
> degree `0`, let `f : Y ⟶ X` be locally of finite type and let `c ∈ A^*(Y ⟶ X)`. Then
>
>   `c ∘ c'_p(E₂) = c'_p(Lf₂^*E₂) ∘ c`   in   `A^*(Y₂ ⟶ X)`,
>
> where `Y₂ = X₂ ×_X Y`, `f₂ : Y₂ ⟶ X₂` is the base change of `f`, `c'_p(Lf₂^*E₂) ∈ A^p(Y₂ ⟶ Y)` is
> the class of Stacks 0F9H for the base-changed cover of `Y`, and `c ∘ c'_p(E₂)` is the composite of
> the restriction of `c` to `X₂` with `c'_p(E₂)`, carried from `Y ×_X X₂` to `Y₂`.

```lean
theorem nonhomogeneousBivariantTransport_compositeOfInvertible_closedCoverChernClass
    (hrank : ∃ M : (pullback i₁ i₂).Modules, IsFiniteLocallyFreeOfRankLT M p ∧
      Nonempty ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
        (pullback.snd i₁ i₂).toLRSHom.toShHom).obj E₂ ≅
          (DerivedCategory.singleFunctor _ 0).obj M))
    (c : nonhomogeneousBivariantGroup C (gysinSystemOfInvertible C) (f ≫ sX) sX f rfl) :
    nonhomogeneousBivariantTransport C (gysinSystemOfInvertible C)
        (pullback.fst f i₂ ≫ (f ≫ sX)) (pullback.fst i₂ f ≫ (i₂ ≫ sX)) sX
        (pullback.snd f i₂ ≫ i₂)
        (comp_comp_structureMorphism_eq
          (pullbackSnd_comp_structureMorphism_eq C (f ≫ sX) sX f rfl i₂) rfl)
        (pullback.snd i₂ f ≫ f)
        (comp_comp_structureMorphism_eq
          (pullbackSnd_comp_structureMorphism_eq C (i₂ ≫ sX) sX i₂ rfl f) rfl)
        (pullbackSymmetry f i₂) (by simp [pullback.condition])
        (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso C)
        (nonhomogeneousBivariantCompositeOfInvertible C (pullback.fst f i₂ ≫ (f ≫ sX)) (i₂ ≫ sX)
          sX (pullback.snd f i₂) i₂
          (pullbackSnd_comp_structureMorphism_eq C (f ≫ sX) sX f rfl i₂) rfl
          (nonhomogeneousBivariantRestriction C (gysinSystemOfInvertible C) (f ≫ sX) sX f rfl i₂
            (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso C) c)
          (DirectSum.of _ (p : ℤ)
            (closedCoverChernClass C sX i₁ i₂ (i₂ ≫ sX) rfl hE₂ p hcover hrank))) =
      nonhomogeneousBivariantCompositeOfInvertible C (pullback.fst i₂ f ≫ (i₂ ≫ sX)) (f ≫ sX) sX
        (pullback.snd i₂ f) f
        (pullbackSnd_comp_structureMorphism_eq C (i₂ ≫ sX) sX i₂ rfl f) rfl
        (DirectSum.of _ (p : ℤ)
          (closedCoverChernClass C (f ≫ sX) (pullback.snd i₁ f) (pullback.snd i₂ f)
            (pullback.fst i₂ f ≫ (i₂ ≫ sX))
            (pullbackSnd_comp_structureMorphism_eq C (i₂ ≫ sX) sX i₂ rfl f)
            (hE₂.derivedPullback (pullback.fst i₂ f)) p
            (range_pullbackSnd_union_eq_univ i₁ i₂ hcover f)
            (exists_isFiniteLocallyFreeOfRankLT_derivedPullback_of_comp_eq
              (pullbackLift_comp_pullbackSnd_eq_pullbackSnd_comp_pullbackFst i₁ i₂ f) hrank)))
        c
```

## Tag 0FAK, a lemma

[Tag 0FAK](https://stacks.math.columbia.edu/tag/0FAK) in the Stacks Project.

**`Stacks.Chow.closedCoverPowerSum_succ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/BabyCaseLemmas.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/BabyCaseLemmas.lean#L124). The attribute's comment: “Newton's recursion P'_{p+1} = ∑_{j&lt;p} (-1)^j c'_{j+1} P'_{p-j} + (-1)^p (p+1) c'_{p+1}, for every p ≥ 0, with the multiplication of 0FA0; it determines every displayed identity and the ones after it (and so on)”.

> In the situation of Stacks 0F9H, assume that `E₂` restricts to zero on `X₁ ∩ X₂`, so that
> `c'_p(E₂)` is defined for every `p ≥ 1`. Then the classes `P'_p(E₂) ∈ A^p(X₂ ⟶ X)` are Newton's
> polynomials in the classes `c'_i(E₂)`, with the multiplication of Stacks 0FA0
> (`(c, c') ↦ res(c) ∘ c'`, `Stacks.Chow.supportedMul`):
>
>   `P'_{p+1}(E₂) = ∑_{j < p} (-1)^j c'_{j+1}(E₂) P'_{p-j}(E₂) + (-1)^p (p + 1) c'_{p+1}(E₂)`
>
> for every `p ≥ 0`. This is the recursion defining the universal power-sum polynomials of Stacks
> 0F9B, so `P'_1 = c'_1`, `P'_2 = c'_1² - 2c'_2`, `P'_3 = c'_1³ - 3c'_1c'_2 + 3c'_3`, and so on.
> The summand `c'_{j+1} P'_{p-j}` lies in `A^{(j+1)+(p-j)}(X₂ ⟶ X)`, read in degree `p + 1`.

```lean
theorem closedCoverPowerSum_succ (q : ℕ) :
    closedCoverPowerSum C sX i₁ i₂ sX₂ hi₂ hE₂ (q + 1) hcover hzero =
      ∑ j ∈ (Finset.range q).attach, ((-1 : ℤ) ^ (j : ℕ)) •
          bivariantClassDegreeCongr C _ sX₂ sX i₂ hi₂ (newton_degree_eq (Finset.mem_range.mp j.2))
            (supportedMul C sX₂ sX i₂ hi₂
              (closedCoverChernClassOfIsZero C sX i₁ i₂ sX₂ hi₂ hE₂ hcover hzero ((j : ℕ) + 1)
                (Nat.succ_pos _))
              (closedCoverPowerSum C sX i₁ i₂ sX₂ hi₂ hE₂ (q - j) hcover hzero)) +
        ((-1 : ℤ) ^ q * ((q : ℤ) + 1)) •
          closedCoverChernClassOfIsZero C sX i₁ i₂ sX₂ hi₂ hE₂ hcover hzero (q + 1)
            (Nat.succ_pos _)
```

**`Stacks.Chow.closedCoverPowerSum_first_four`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/BabyCaseLemmas.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/BabyCaseLemmas.lean#L167). The attribute's comment: “the four displayed identities, with the multiplication of 0FA0”.

> In the situation of Stacks 0F9H, with `E₂` restricting to zero on `X₁ ∩ X₂`,
>
> * `P'_1 = c'_1`,
> * `P'_2 = c'_1² - 2c'_2`,
> * `P'_3 = c'_1³ - 3c'_1c'_2 + 3c'_3`,
> * `P'_4 = c'_1⁴ - 4c'_1²c'_2 + 4c'_1c'_3 + 2c'_2² - 4c'_4`
>
> in `A^p(X₂ ⟶ X)`, with the multiplication `(c, c') ↦ res(c) ∘ c'` of Stacks 0FA0
> (`Stacks.Chow.supportedMul`), products bracketed to the right and read in the degree of the
> left-hand side. The general case ("and so on") is `Stacks.Chow.closedCoverPowerSum_succ`.

```lean
theorem closedCoverPowerSum_first_four :
    let c := fun i (hi : 0 < i) =>
      closedCoverChernClassOfIsZero C sX i₁ i₂ (i₂ ≫ sX) rfl hE₂ hcover hzero i hi
    let m := fun {a b : ℤ} (x : BivariantClass C (gysinSystemOfInvertible C) (i₂ ≫ sX) sX i₂ rfl a)
      (y : BivariantClass C (gysinSystemOfInvertible C) (i₂ ≫ sX) sX i₂ rfl b) =>
        supportedMul C (i₂ ≫ sX) sX i₂ rfl x y
    let P := fun q => closedCoverPowerSum C sX i₁ i₂ (i₂ ≫ sX) rfl hE₂ q hcover hzero
    let d := fun {a b : ℤ} (h : a = b) =>
      bivariantClassDegreeCongr C (gysinSystemOfInvertible C) (i₂ ≫ sX) sX i₂ rfl h
    P 1 = c 1 (by norm_num) ∧
    P 2 = d (by norm_num) (m (c 1 (by norm_num)) (c 1 (by norm_num))) -
      (2 : ℤ) • c 2 (by norm_num) ∧
    P 3 = d (by norm_num) (m (c 1 (by norm_num)) (d (by norm_num : (1 : ℤ) + 1 = 2)
        (m (c 1 (by norm_num)) (c 1 (by norm_num))))) -
      (3 : ℤ) • d (by norm_num) (m (c 1 (by norm_num)) (c 2 (by norm_num))) +
      (3 : ℤ) • c 3 (by norm_num) ∧
    P 4 = d (by norm_num) (m (c 1 (by norm_num)) (d (by norm_num : (1 : ℤ) + 2 = 3)
        (m (c 1 (by norm_num)) (d (by norm_num : (1 : ℤ) + 1 = 2)
          (m (c 1 (by norm_num)) (c 1 (by norm_num))))))) -
      (4 : ℤ) • d (by norm_num) (m (c 1 (by norm_num)) (d (by norm_num : (1 : ℤ) + 2 = 3)
        (m (c 1 (by norm_num)) (c 2 (by norm_num))))) +
      (4 : ℤ) • d (by norm_num) (m (c 1 (by norm_num)) (c 3 (by norm_num))) +
      (2 : ℤ) • d (by norm_num) (m (c 2 (by norm_num)) (c 2 (by norm_num))) -
      (4 : ℤ) • c 4 (by norm_num)
```

## Tag 0FAL, a lemma

[Tag 0FAL](https://stacks.math.columbia.edu/tag/0FAL) in the Stacks Project.

**`Stacks.Chow.closedCoverTotalChernClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/BabyCaseWhitney.lean, line 438](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/BabyCaseWhitney.lean#L438). The attribute's comment: “the class c^(p)(E) in A^(p)(X₂ → X)”.

> **The class `c^{(p)}(E) ∈ A^{(p)}(X₂ ⟶ X)`.** Let `i₁ : X₁ ⟶ X`, `i₂ : X₂ ⟶ X` be closed
> immersions whose images cover `X`, and let `E ∈ D(𝒪_X)` have defined Chern classes, with
> `(E|_{X₂})|_{X₁ ∩ X₂}` isomorphic to a finite locally free module of rank `< p` placed in degree
> `0`. Then
>
>   `c^{(p)}(E) = 1 + c_1(E) + … + c_{p-1}(E) + c'_p(E|_{X₂}) + c'_{p+1}(E|_{X₂}) + …`:
>
> its component in a degree `0 ≤ i < p` is `c_i(E) ∈ A^i(X)`, in a negative degree it is `0`, and
> in a degree `i ≥ p` it is the class `c'_i(E|_{X₂}) ∈ A^i(X₂ ⟶ X)` of Stacks 0F9H
> (`Stacks.Chow.closedCoverChernClass`), which is defined since a rank `< p` is a rank `< i`.

```lean
def closedCoverTotalChernClass {E : DerivedCategory X.Modules} (hE : HasDefinedChernClasses E)
    (p : ℕ)
    (hrank : ∃ M : (pullback i₁ i₂).Modules, IsFiniteLocallyFreeOfRankLT M p ∧
      Nonempty ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
        (pullback.snd i₁ i₂).toLRSHom.toShHom).obj
          ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
            i₂.toLRSHom.toShHom).obj E) ≅ (DerivedCategory.singleFunctor _ 0).obj M)) :
    localizedBivariantGrading C (gysinSystemOfInvertible C) (i₂ ≫ sX) sX i₂ rfl p
```

**`Stacks.Chow.closedCoverTotalChernClass_biprod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/BabyCaseWhitney.lean, line 551](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/BabyCaseWhitney.lean#L551). The attribute's comment: “CORRECTED: hypothesis (2) is imposed on E|_{X₁}, F|_{X₁} (as written, on X₁ ∩ X₂, it is false: X = ℙ¹ ⊔ pt, E = 𝒪(1)² on ℙ¹ and 0 on pt, F = 0, p = q = 1, where the degree-1 components are c₁(E) ≠ 0 and 0)”.

> Let `i₁ : X₁ ⟶ X`, `i₂ : X₂ ⟶ X` be closed immersions with `X = X₁ ∪ X₂` set-theoretically,
> and let `E, F ∈ D(𝒪_X)` have defined Chern classes, with `E|_{X₁}` and `F|_{X₁}` isomorphic to
> finite locally free `𝒪_{X₁}`-modules of rank `< p` and `< q` placed in degree `0`. Then
>
>   `c^{(p+q)}(E ⊕ F) = c^{(p)}(E) c^{(q)}(F)`   in `A^{(p+q)}(X₂ ⟶ X)`,
>
> with the multiplication of Stacks 0FA0 (`Stacks.Chow.localizedGradingMul`). The hypotheses of
> Stacks 0F9H on `E|_{X₂}`, `F|_{X₂}` and `(E ⊕ F)|_{X₂}`, under which the classes `c^{(·)}` are
> defined, follow from these
> (`Stacks.Chow.exists_isFiniteLocallyFreeOfRankLT_derivedPullback_pullbackSnd`,
> `Stacks.Chow.exists_isFiniteLocallyFreeOfRankLT_derivedPullback_biprod`), and so does the
> definedness of the Chern classes of `E ⊕ F` (`Stacks.Chow.hasDefinedChernClasses_biprod`).
>
> **The correction.** The source assumes in (2) that the restrictions `E|_{X₁ ∩ X₂}` and
> `F|_{X₁ ∩ X₂}` are finite locally free of rank `< p`, `< q` (calling them `𝒪_{X₁}`-modules). As
> written, on `X₁ ∩ X₂`, the statement is false: let `X = X₁ ⊔ X₂` be a disjoint union of
> `X₁ = ℙ¹_k` over a field and a point `X₂`, so that (2) is vacuous; take `E = 𝒪(1)^{⊕ 2}` on `X₁`
> and `0` on `X₂`, `F = 0` and `p = q = 1`. In degree `1 < p + q` the component of
> `c^{(2)}(E ⊕ F)` is `c_1(E) ≠ 0`, while that of `c^{(1)}(E) c^{(1)}(F)` is
> `(i_{2,*} c'_1(E|_{X₂})) · 1 + 1 · (i_{2,*} c'_1(0)) = 0`. The hypothesis on `X₁`, to which the
> phrase "`𝒪_{X₁}`-modules" points, is the one Stacks 0F9I needs to compare the pushed classes
> `i_{2,*} c'_i(E|_{X₂})` with `c_i(E)`, and with it the statement holds. Perfectness of `E`, `F`
> is not used, only that their Chern classes are defined.

```lean
theorem closedCoverTotalChernClass_biprod
    (hrankE : ∃ M : X₁.Modules, IsFiniteLocallyFreeOfRankLT M p ∧
      Nonempty ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
        i₁.toLRSHom.toShHom).obj E ≅ (DerivedCategory.singleFunctor _ 0).obj M))
    (hrankF : ∃ M : X₁.Modules, IsFiniteLocallyFreeOfRankLT M q ∧
      Nonempty ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
        i₁.toLRSHom.toShHom).obj F ≅ (DerivedCategory.singleFunctor _ 0).obj M)) :
    closedCoverTotalChernClass C sX i₁ i₂ hcover (hasDefinedChernClasses_biprod hE hF) (p + q)
        (exists_isFiniteLocallyFreeOfRankLT_derivedPullback_pullbackSnd i₁ i₂
          (exists_isFiniteLocallyFreeOfRankLT_derivedPullback_biprod i₁ hrankE hrankF)) =
      localizedGradingMul C (i₂ ≫ sX) sX i₂ rfl
        (closedCoverTotalChernClass C sX i₁ i₂ hcover hE p
          (exists_isFiniteLocallyFreeOfRankLT_derivedPullback_pullbackSnd i₁ i₂ hrankE))
        (closedCoverTotalChernClass C sX i₁ i₂ hcover hF q
          (exists_isFiniteLocallyFreeOfRankLT_derivedPullback_pullbackSnd i₁ i₂ hrankF))
```

## Tag 0FAM, a lemma

[Tag 0FAM](https://stacks.math.columbia.edu/tag/0FAM) in the Stacks Project.

**`Stacks.Chow.closedCoverPowerSum_biprod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/BabyCaseLemmas.lean, line 320](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/BabyCaseLemmas.lean#L320).

> Let `i₁ : X₁ ⟶ X`, `i₂ : X₂ ⟶ X` be closed immersions with `X = X₁ ∪ X₂` set-theoretically, and
> let `E, F ∈ D(𝒪_{X₂})` have defined Chern classes and restrict to zero on `X₁ ∩ X₂`. Then
> `P'_p(E ⊕ F) = P'_p(E) + P'_p(F)` in `A^p(X₂ ⟶ X)` for every `p ≥ 0`, with `P'_p` the classes of
> Stacks 0F9H. (The Chern classes of `E ⊕ F` are defined and it restricts to zero on `X₁ ∩ X₂`, so
> `P'_p(E ⊕ F)` is defined; perfectness of `E`, `F` is not needed.)

```lean
theorem closedCoverPowerSum_biprod {E F : DerivedCategory X₂.Modules}
    (hE : HasDefinedChernClasses E) (hF : HasDefinedChernClasses F)
    (hzE : IsZero ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
      (pullback.snd i₁ i₂).toLRSHom.toShHom).obj E))
    (hzF : IsZero ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
      (pullback.snd i₁ i₂).toLRSHom.toShHom).obj F)) (p : ℕ) :
    closedCoverPowerSum C sX i₁ i₂ sX₂ hi₂ (hasDefinedChernClasses_biprod hE hF) p hcover
        (isZero_derivedPullback_biprod (pullback.snd i₁ i₂) hzE hzF) =
      closedCoverPowerSum C sX i₁ i₂ sX₂ hi₂ hE p hcover hzE +
        closedCoverPowerSum C sX i₁ i₂ sX₂ hi₂ hF p hcover hzF
```

## Tag 0FAN, a lemma

[Tag 0FAN](https://stacks.math.columbia.edu/tag/0FAN) in the Stacks Project.

**`Stacks.Chow.closedCoverChernClass_derivedTwist`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/BabyCaseLemmas.lean, line 415](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/BabyCaseLemmas.lean#L415).

> In the situation of Stacks 0F9H — `E₂ ∈ D(𝒪_{X₂})` perfect with defined Chern classes,
> restricting on `X₁ ∩ X₂` to a finite locally free module of rank `< p` placed in degree `0` —
> assume that `E₂` has constant rank `0`, and let `ℒ` be an invertible `𝒪_X`-module. Then the
> restriction of `E₂` to `X₁ ∩ X₂` is zero (`hzero` in the statement, by the assumption on the rank),
> so `c'_i(E₂)` and `c'_i(E₂ ⊗ ℒ)` are defined for every `i ≥ 1`, and
>
>   `c'_i(E₂ ⊗ ℒ) = ∑_{j=0}^{i-1} binom(-i + j, j) c'_{i-j}(E₂) c_1(ℒ)^j`
>
> in `A^i(X₂ ⟶ X)`. Here `E₂ ⊗ ℒ` is the twist of `E₂` by `ℒ|_{X₂}` (Stacks 0FAF),
> `c_1(ℒ)^j ∈ A^j(X)`, and the product `A^{i-j}(X₂ ⟶ X) × A^j(X) ⟶ A^i(X₂ ⟶ X)` is the first
> multiplication of Stacks 0FA0 (`Stacks.Chow.supportedRightComp`), the summand being read in
> degree `i`.

```lean
theorem closedCoverChernClass_derivedTwist {E₂ : DerivedCategory X₂.Modules}
    (perfect : RingedSpace.IsPerfect.{u, u + 1} E₂) (hE₂ : HasDefinedChernClasses E₂)
    (constantRank : ∀ x : X₂, DerivedFibreBetti.chiDerivedFibre X₂ E₂
      (DerivedFibreBetti.isPseudoCoherent_of_isPerfect E₂ perfect) x = 0) {p : ℕ}
    (hrank : ∃ M : (pullback i₁ i₂).Modules, IsFiniteLocallyFreeOfRankLT M p ∧
      Nonempty ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
        (pullback.snd i₁ i₂).toLRSHom.toShHom).obj E₂ ≅
          (DerivedCategory.singleFunctor _ 0).obj M)) (i : ℕ) (hi : 0 < i) :
    haveI := isInvertible_pullback i₂ L
    let hzero := DerivedFibreBetti.isZero_derivedPullback_of_chiDerivedFibre_eq_zero
      (pullback.snd i₁ i₂) E₂ perfect constantRank hrank
    closedCoverChernClassOfIsZero C sX i₁ i₂ (i₂ ≫ sX) rfl
        (hasDefinedChernClasses_derivedTwist hE₂ ((Scheme.Modules.pullback i₂).obj L)) hcover
        (isZero_derivedPullback_derivedTwist (pullback.snd i₁ i₂) _ hzero) i hi =
      ∑ j ∈ (Finset.range i).attach, Ring.choose (-(i : ℤ) + (j : ℕ)) (j : ℕ) •
        bivariantClassDegreeCongr C _ (i₂ ≫ sX) sX i₂ rfl
          (twist_degree_eq (Finset.mem_range.mp j.2))
          (supportedRightComp C (i₂ ≫ sX) sX i₂ rfl
            (closedCoverChernClassOfIsZero C sX i₁ i₂ (i₂ ≫ sX) rfl hE₂ hcover hzero (i - j)
              (by have := Finset.mem_range.mp j.2; omega))
            ((TotalChowClass.firstChernTotal C sX L ^ (j : ℕ)) (j : ℕ)))
```

## Tag 0FE5, a lemma

[Tag 0FE5](https://stacks.math.columbia.edu/tag/0FE5) in the Stacks Project.

**`Stacks.Chow.closedCoverPowerSum_derivedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/BabyCaseTensor.lean, line 1056](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/BabyCaseTensor.lean#L1056). The attribute's comment: “the formula P'_p((E tensor^L E')|_(X_2 cap X'_2)) = sum over p_1 + p_2 = p of C(p, p_1) chi_(p_1) chi'_(p_2) in A^p(X_2 cap X'_2 -> X), for every p >= 0, with E, E' perfect with defined Chern classes as in the source. The closed cover of X on which the left hand side is the class of 0F9H is X = Y cup (X_2 cap X'_2) with Y the reduced closed subscheme on |X_1| cup |X'_1| (reducedUnionIdeal); the vanishing of (E tensor^L E')|_(Y cap X_2 cap X'_2) that 0F9H needs is proved (isZero_derivedPullback_derivedTensor_reducedUnion, by derived Nakayama on the derived fibres), for E, E' perfect as in the source. The source's Y = (X_1 cap X'_1) cup (X_1 cap X'_2) cup (X_2 cap X'_1) has the same underlying set; by 0FAH the class does not depend on the choice. The product of a class on X_2 and a class on X'_2 is supportedIntersectionMul, res(c_1) o c_2 for the restriction of 0F9Z and the composition of 0B75”.

> **Stacks 0FE5 for `P'_p`.** Let `X = X₁ ∪ X₂ = X₁' ∪ X₂'` be two closed
> covers and let `E`, `E' ∈ D(𝒪_X)` be perfect objects whose Chern classes are defined and which
> restrict to zero on `X₁` and `X₁'`. Write `χ_p = P'_p(E|_{X₂})` and
> `χ'_p = P'_p(E'|_{X₂'})` for the classes of Stacks 0F9H. Let `Y ⊆ X` be the reduced closed
> subscheme with underlying set `X₁ ∪ X₁'` (`Stacks.Chow.reducedUnionIdeal`); then
> `X = Y ∪ (X₂ ∩ X₂')`, and `E ⊗^L E'` restricts to zero on `Y ∩ (X₂ ∩ X₂')`, so the class of
> Stacks 0F9H of `(E ⊗^L E')|_{X₂ ∩ X₂'}` along `X = Y ∪ (X₂ ∩ X₂')` is defined; by Stacks 0FAH
> it does not depend on the choice of `Y`. Then
>
>   `P'_p((E ⊗^L E')|_{X₂ ∩ X₂'}) = ∑_{p₁ + p₂ = p} C(p, p₁) χ_{p₁} χ'_{p₂}`
>
> in `A^p(X₂ ∩ X₂' ⟶ X)`, with the product of `Stacks.Chow.supportedIntersectionMul`, each summand
> read in degree `p`.

```lean
theorem closedCoverPowerSum_derivedTensor (perfectE : RingedSpace.IsPerfect.{u, u + 1} E)
    (perfectE' : RingedSpace.IsPerfect.{u, u + 1} E') (p : ℕ) :
    closedCoverPowerSum C sX (reducedUnionIdeal i₁ j₁).subschemeι (pullback.snd i₂ j₂ ≫ j₂) _ rfl
        ((hasDefinedChernClasses_derivedTensor hE hE').derivedPullback _) p
        (range_union_range_reducedUnionIdeal i₁ i₂ j₁ j₂ hcover hcover')
        (isZero_derivedPullback_derivedTensor_reducedUnion i₁ i₂ j₁ j₂ hzero hzero' perfectE
          perfectE') =
      ∑ q ∈ (antidiagonal p).attach, (p.choose q.1.1 : ℤ) •
        bivariantClassDegreeCongr C _ _ sX _ rfl
          (by have := mem_antidiagonal.1 q.2; omega)
          (supportedIntersectionMul C sX i₂ j₂ (IsPullback.of_hasPullback i₂ j₂) _ rfl
            (closedCoverPowerSumRestrict C sX i₁ i₂ hcover hE hzero q.1.1)
            (closedCoverPowerSumRestrict C sX j₁ j₂ hcover' hE' hzero' q.1.2))
```

**`Stacks.Chow.closedCoverChernClass_derivedTensor_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/BabyCaseTensor.lean, line 1096](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/BabyCaseTensor.lean#L1096). The attribute's comment: “the formula c'_1((E tensor^L E')|_(X_2 cap X'_2)) = r gamma'_1 + r' gamma_1 in A^1(X_2 cap X'_2 -> X), with E, E' perfect with defined Chern classes as in the source. The closed cover of X on which the left hand side is the class of 0F9H is X = Y cup (X_2 cap X'_2) with Y the reduced closed subscheme on |X_1| cup |X'_1| (reducedUnionIdeal); the vanishing of (E tensor^L E')|_(Y cap X_2 cap X'_2) that 0F9H needs is proved (isZero_derivedPullback_derivedTensor_reducedUnion, by derived Nakayama on the derived fibres), for E, E' perfect as in the source. The source's Y = (X_1 cap X'_1) cup (X_1 cap X'_2) cup (X_2 cap X'_1) has the same underlying set; by 0FAH the class does not depend on the choice. Products are supportedIntersectionMul, res(c_1) o c_2, landing in the class group of X_2 x_X X'_2 -> X for both orders of the factors”.

> **Stacks 0FE5 for `c'_1`.** Let `X = X₁ ∪ X₂ = X₁' ∪ X₂'` be two closed
> covers and let `E`, `E' ∈ D(𝒪_X)` be perfect objects whose Chern classes are defined and which
> restrict to zero on `X₁` and `X₁'`. Write `r = P'_0(E|_{X₂})`,
> `r' = P'_0(E'|_{X₂'})`, `γ_1 = c'_1(E|_{X₂})` and `γ'_1 = c'_1(E'|_{X₂'})` for the classes of
> Stacks 0F9H. Let `Y ⊆ X` be the reduced closed subscheme with
> underlying set `X₁ ∪ X₁'` (`Stacks.Chow.reducedUnionIdeal`); then `X = Y ∪ (X₂ ∩ X₂')`, and
> `E ⊗^L E'` restricts to zero on `Y ∩ (X₂ ∩ X₂')`, so the class of Stacks 0F9H of
> `(E ⊗^L E')|_{X₂ ∩ X₂'}` along `X = Y ∪ (X₂ ∩ X₂')` is defined; by Stacks 0FAH it does not
> depend on the choice of `Y`. Then
>
>   `c'_1((E ⊗^L E')|_{X₂ ∩ X₂'}) = r γ'_1 + r' γ_1`
>
> in `A^1(X₂ ∩ X₂' ⟶ X)`, with the product of `Stacks.Chow.supportedIntersectionMul` (for `r' γ_1`
> along the pullback square with the two factors exchanged), each summand read in degree `1`.

```lean
theorem closedCoverChernClass_derivedTensor_one (perfectE : RingedSpace.IsPerfect.{u, u + 1} E)
    (perfectE' : RingedSpace.IsPerfect.{u, u + 1} E') :
    closedCoverChernClassOfIsZero C sX (reducedUnionIdeal i₁ j₁).subschemeι
        (pullback.snd i₂ j₂ ≫ j₂) _ rfl
        ((hasDefinedChernClasses_derivedTensor hE hE').derivedPullback _)
        (range_union_range_reducedUnionIdeal i₁ i₂ j₁ j₂ hcover hcover')
        (isZero_derivedPullback_derivedTensor_reducedUnion i₁ i₂ j₁ j₂ hzero hzero' perfectE
          perfectE') 1 one_pos =
      bivariantClassDegreeCongr C _ _ sX _ rfl (by norm_num)
          (supportedIntersectionMul C sX i₂ j₂ (IsPullback.of_hasPullback i₂ j₂) _ rfl
            (closedCoverPowerSumRestrict C sX i₁ i₂ hcover hE hzero 0)
            (closedCoverChernClassRestrict C sX j₁ j₂ hcover' hE' hzero' 1 one_pos)) +
        bivariantClassDegreeCongr C _ _ sX _ rfl (by norm_num)
          (supportedIntersectionMul C sX j₂ i₂ (IsPullback.of_hasPullback i₂ j₂).flip _
            pullback.condition
            (closedCoverPowerSumRestrict C sX j₁ j₂ hcover' hE' hzero' 0)
            (closedCoverChernClassRestrict C sX i₁ i₂ hcover hE hzero 1 one_pos))
```

**`Stacks.Chow.closedCoverChernClass_derivedTensor_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/BabyCaseTensor.lean, line 1148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/BabyCaseTensor.lean#L1148). The attribute's comment: “the formula for c'_2((E tensor^L E')|_(X_2 cap X'_2)) in A^2(X_2 cap X'_2 -> X), with E, E' perfect with defined Chern classes as in the source. The closed cover of X on which the left hand side is the class of 0F9H is X = Y cup (X_2 cap X'_2) with Y the reduced closed subscheme on |X_1| cup |X'_1| (reducedUnionIdeal); the vanishing of (E tensor^L E')|_(Y cap X_2 cap X'_2) that 0F9H needs is proved (isZero_derivedPullback_derivedTensor_reducedUnion, by derived Nakayama on the derived fibres), for E, E' perfect as in the source. The source's Y = (X_1 cap X'_1) cup (X_1 cap X'_2) cup (X_2 cap X'_1) has the same underlying set; by 0FAH the class does not depend on the choice. C(r, 2) is read as closedCoverRankChoose: the 0F9H extension of the restriction to X_2 of the class ofLocallyConstant of x |-> C(chi_E(x), 2), chi_E the derived-fibre Euler characteristic whose class is r(E) = P_0(E), exactly as 0FAG reads C(r(E), 2); it vanishes on X_1 because chi_E does, and C(r, 1) = r. The term (r r' - 1) gamma'_1 gamma_1 is read as (r r')(gamma'_1 gamma_1) - gamma'_1 gamma_1, since 1 is not a class supported on X_2 cap X'_2; products of classes supported on X_2 and X'_2 are supportedIntersectionMul, products of classes on one support are supportedMul (0FA0). The source's 'and so on for higher Chern classes' is not a precise assertion and is not formalized”.

> **Stacks 0FE5 for `c'_2`.** Let `X = X₁ ∪ X₂ = X₁' ∪ X₂'` be two closed
> covers and let `E`, `E' ∈ D(𝒪_X)` be perfect objects whose Chern classes are defined and which
> restrict to zero on `X₁` and `X₁'`. Write `r = P'_0(E|_{X₂})`,
> `r' = P'_0(E'|_{X₂'})`, `γ_p = c'_p(E|_{X₂})` and `γ'_p = c'_p(E'|_{X₂'})` for the classes of
> Stacks 0F9H, and `C(r, 2)`, `C(r', 2)` for the classes `Stacks.Chow.closedCoverRankChoose`. Let
> `Y ⊆ X` be the reduced closed subscheme with underlying set `X₁ ∪ X₁'`
> (`Stacks.Chow.reducedUnionIdeal`); then `X = Y ∪ (X₂ ∩ X₂')`, and `E ⊗^L E'` restricts to zero
> on `Y ∩ (X₂ ∩ X₂')`, so the class of Stacks 0F9H of `(E ⊗^L E')|_{X₂ ∩ X₂'}` along
> `X = Y ∪ (X₂ ∩ X₂')` is defined; by Stacks 0FAH it does not depend on the choice of `Y`. Then
>
>   `c'_2((E ⊗^L E')|_{X₂ ∩ X₂'}) =
>     r γ'_2 + r' γ_2 + C(r, 2) (γ'_1)² + ((r r') (γ'_1 γ_1) - γ'_1 γ_1) + C(r', 2) γ_1²`
>
> in `A^2(X₂ ∩ X₂' ⟶ X)`. The products of a class on `X₂` and a class on `X₂'` are those of
> `Stacks.Chow.supportedIntersectionMul`, the squares `(γ'_1)²`, `γ_1²` and the product of `r r'`
> with `γ'_1 γ_1` are the third multiplication of Stacks 0FA0 (`Stacks.Chow.supportedMul`), and each
> summand is read in degree `2`.

```lean
theorem closedCoverChernClass_derivedTensor_two (perfectE : RingedSpace.IsPerfect.{u, u + 1} E)
    (perfectE' : RingedSpace.IsPerfect.{u, u + 1} E') :
    closedCoverChernClassOfIsZero C sX (reducedUnionIdeal i₁ j₁).subschemeι
        (pullback.snd i₂ j₂ ≫ j₂) _ rfl
        ((hasDefinedChernClasses_derivedTensor hE hE').derivedPullback _)
        (range_union_range_reducedUnionIdeal i₁ i₂ j₁ j₂ hcover hcover')
        (isZero_derivedPullback_derivedTensor_reducedUnion i₁ i₂ j₁ j₂ hzero hzero' perfectE
          perfectE') 2 two_pos =
      (bivariantClassDegreeCongr C _ _ sX _ rfl (by norm_num)
          (supportedIntersectionMul C sX i₂ j₂ (IsPullback.of_hasPullback i₂ j₂) _ rfl
            (closedCoverPowerSumRestrict C sX i₁ i₂ hcover hE hzero 0)
            (closedCoverChernClassRestrict C sX j₁ j₂ hcover' hE' hzero' 2 two_pos)) +
        bivariantClassDegreeCongr C _ _ sX _ rfl (by norm_num)
          (supportedIntersectionMul C sX j₂ i₂ (IsPullback.of_hasPullback i₂ j₂).flip _
            pullback.condition
            (closedCoverPowerSumRestrict C sX j₁ j₂ hcover' hE' hzero' 0)
            (closedCoverChernClassRestrict C sX i₁ i₂ hcover hE hzero 2 two_pos)) +
        bivariantClassDegreeCongr C _ _ sX _ rfl (by norm_num)
          (supportedIntersectionMul C sX i₂ j₂ (IsPullback.of_hasPullback i₂ j₂) _ rfl
            (closedCoverRankChoose C sX i₁ i₂ perfectE hcover hzero 2 two_pos)
            (supportedMul C (j₂ ≫ sX) sX j₂ rfl
              (closedCoverChernClassRestrict C sX j₁ j₂ hcover' hE' hzero' 1 one_pos)
              (closedCoverChernClassRestrict C sX j₁ j₂ hcover' hE' hzero' 1 one_pos))) +
        (bivariantClassDegreeCongr C _ _ sX _ rfl (by norm_num)
            (supportedMul C ((pullback.snd i₂ j₂ ≫ j₂) ≫ sX) sX (pullback.snd i₂ j₂ ≫ j₂) rfl
              (supportedIntersectionMul C sX i₂ j₂ (IsPullback.of_hasPullback i₂ j₂) _ rfl
                (closedCoverPowerSumRestrict C sX i₁ i₂ hcover hE hzero 0)
                (closedCoverPowerSumRestrict C sX j₁ j₂ hcover' hE' hzero' 0))
              (supportedIntersectionMul C sX j₂ i₂ (IsPullback.of_hasPullback i₂ j₂).flip _
                pullback.condition
                (closedCoverChernClassRestrict C sX j₁ j₂ hcover' hE' hzero' 1 one_pos)
                (closedCoverChernClassRestrict C sX i₁ i₂ hcover hE hzero 1 one_pos))) -
          bivariantClassDegreeCongr C _ _ sX _ rfl (by norm_num)
            (supportedIntersectionMul C sX j₂ i₂ (IsPullback.of_hasPullback i₂ j₂).flip _
              pullback.condition
              (closedCoverChernClassRestrict C sX j₁ j₂ hcover' hE' hzero' 1 one_pos)
              (closedCoverChernClassRestrict C sX i₁ i₂ hcover hE hzero 1 one_pos))) +
        bivariantClassDegreeCongr C _ _ sX _ rfl (by norm_num)
          (supportedIntersectionMul C sX j₂ i₂ (IsPullback.of_hasPullback i₂ j₂).flip _
            pullback.condition
            (closedCoverRankChoose C sX j₁ j₂ perfectE' hcover' hzero' 2 two_pos)
            (supportedMul C (i₂ ≫ sX) sX i₂ rfl
              (closedCoverChernClassRestrict C sX i₁ i₂ hcover hE hzero 1 one_pos)
              (closedCoverChernClassRestrict C sX i₁ i₂ hcover hE hzero 1 one_pos))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.47, Tag 0F9G](https://stacks.math.columbia.edu/tag/0F9G)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
