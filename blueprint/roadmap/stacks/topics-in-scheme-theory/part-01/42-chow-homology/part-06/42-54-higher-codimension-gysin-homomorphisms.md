---
declaration: section
origin: cited
lean: Stacks.Chow.VirtualNormalBundle.baseChange, Stacks.Chow.completedVirtualNormalGysinClass, Stacks.Chow.completedBivariantRestriction_completedVirtualNormalGysinClass, Stacks.Chow.virtualNormalBundleClass, Stacks.Chow.projectionPullbackClass_comp_virtualNormalBundleClass, Stacks.Chow.eq_virtualNormalBundleClass_iff, Stacks.Chow.VirtualNormalBundle.bivariantRestriction_virtualNormalClass, Stacks.Chow.VirtualNormalBundle.completedClass
statement: formalized
proof: formalized
---

# 42.54 Higher codimension gysin homomorphisms

Section 42.54 of the Stacks Project, [Tag 0FBI](https://stacks.math.columbia.edu/tag/0FBI). 11 tags here are carried by 46 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FBJ, a lemma

[Tag 0FBJ](https://stacks.math.columbia.edu/tag/0FBJ) in the Stacks Project.

**`Stacks.Chow.VirtualNormalBundle.baseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/VirtualNormalBundleBaseChange.lean, line 522](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/VirtualNormalBundleBaseChange.lean#L522).

> **Stacks 0FBJ.** For a cartesian square of schemes whose horizontal arrows `i : Z ⟶ X`
> and `i' : Z' ⟶ X'` are immersions, the pullback `g^* 𝒩` of a virtual normal bundle `𝒩` for
> `Z` in `X` is a virtual normal bundle for `Z'` in `X'`: it is finite locally free, and the
> surjection `(g^* 𝒩)^∨ ⟶ 𝒞_{Z'/X'}` is the composite of the base-change isomorphism
> `(g^* 𝒩)^∨ ≅ g^* (𝒩^∨)`, the pullback of the given surjection, and the surjection
> `g^* 𝒞_{Z/X} ⟶ 𝒞_{Z'/X'}` of [Stacks Project, Tag 0473].

```lean
def VirtualNormalBundle.baseChange {Z X Z' X' : Scheme.{u}} (i : Z ⟶ X) (i' : Z' ⟶ X')
    [IsImmersion i] [IsImmersion i'] (g : Z' ⟶ Z) (f : X' ⟶ X)
    (sq : IsPullback i' g f i) (N : VirtualNormalBundle i) : VirtualNormalBundle i'
```

## Tag 0FBK, a lemma

[Tag 0FBK](https://stacks.math.columbia.edu/tag/0FBK) in the Stacks Project.

**`Stacks.Chow.completedVirtualNormalGysinClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/CompletedVirtualNormalBundleClass.lean, line 254](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/CompletedVirtualNormalBundleClass.lean#L254). The attribute's comment: “the bivariant class c(Z → X, 𝒩) ∈ A^*(Z → X)^∧ of a virtual normal bundle 𝒩 of arbitrary rank for a closed immersion Z → X”.

> **Stacks 0FBK, the class `c(Z ⟶ X, 𝒩) ∈ A^*(Z ⟶ X)^∧`** of a virtual normal bundle `𝒩` of
> arbitrary rank for a closed immersion `i : Z ⟶ X`. On a connected component `Z_a` of `Z`, on which
> `𝒩` has constant rank `r_a`, it is the class `c(Z_a ⟶ U_a, 𝒩|_{Z_a}) ∘ (U_a ⟶ X_b)^*` of degree
> `r_a`, for the open `U_a = X_b ∖ i(Z ∖ Z_a)` of the connected component `X_b` of `X` containing
> `i(Z_a)`, through which `Z_a ⟶ X_b` factors as the closed immersion `Z_a ⟶ U_a` cut out by the
> base change of `i`.

```lean
def completedVirtualNormalGysinClass (𝒩 : VirtualNormalBundle i) :
    completedBivariantGroup C (gysinSystemOfInvertible C) sZ sX i hi
```

**`Stacks.Chow.completedBivariantRestriction_completedVirtualNormalGysinClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/CompletedVirtualNormalBundleClassBaseChange.lean, line 1350](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/CompletedVirtualNormalBundleClassBaseChange.lean#L1350). The attribute's comment: “base change: the restriction of c(Z → X, 𝒩) ∈ A^*(Z → X)^∧ along X' → X is c(Z ×\_X X' → X', g^*𝒩), for 𝒩 of arbitrary rank”.

> **Stacks 0FBK, the base-change clause, for a virtual normal sheaf of arbitrary rank.** For
> `f : X' ⟶ X` locally of finite type, the restriction (Stacks 0F9Z) of
> `c(Z ⟶ X, 𝒩) ∈ A^*(Z ⟶ X)^∧` along `f` is `c(Z ×_X X' ⟶ X', g^*𝒩)`, for the virtual normal sheaf
> `g^*𝒩` of Stacks 0FBJ. Both are read degree by degree (Stacks 0FE0), and in each degree the cap
> operations agree by `Stacks.Chow.completedVirtualNormalGysinClass_cap_baseChange`.

```lean
theorem completedBivariantRestriction_completedVirtualNormalGysinClass (C : ChowSituation.{u})
    {Z X X' : Scheme.{u}} (sZ : Z ⟶ C.S) [LocallyOfFiniteType sZ] (sX : X ⟶ C.S)
    [LocallyOfFiniteType sX] (i : Z ⟶ X) [IsClosedImmersion i] (hi : i ≫ sX = sZ)
    (f : X' ⟶ X) [LocallyOfFiniteType f] (𝒩 : VirtualNormalBundle i) :
    haveI : IsLocallyNoetherian Z := LocallyOfFiniteType.isLocallyNoetherian sZ
    haveI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    haveI : IsLocallyNoetherian X' := LocallyOfFiniteType.isLocallyNoetherian (f ≫ sX)
    haveI : IsLocallyNoetherian (pullback i f) :=
      LocallyOfFiniteType.isLocallyNoetherian (pullback.fst i f ≫ sZ)
    completedBivariantRestrictionViaSequence C sZ sX i hi f
        (completedVirtualNormalGysinClass C sZ sX i hi 𝒩) =
      completedVirtualNormalGysinClass C (pullback.fst i f ≫ sZ) (f ≫ sX) (pullback.snd i f)
        (pullbackSnd_comp_structureMorphism_eq C sZ sX i hi f)
        (baseChangeVirtualNormalBundle i f 𝒩)
```

**`Stacks.Chow.virtualNormalBundleClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/VirtualNormalBundleClassConstruction.lean, line 356](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/VirtualNormalBundleClassConstruction.lean#L356). The attribute's comment: “the bivariant class c(Z → X, 𝒩) ∈ A^r(Z → X) of a virtual normal bundle 𝒩 of constant rank r for a closed immersion Z → X”.

> **Stacks 0FBK, the class `c(Z ⟶ X, 𝒩) ∈ A^r(Z ⟶ X)`** of a virtual normal bundle `𝒩` of
> constant rank `r` for a closed immersion `i : Z ⟶ X`: the unique bivariant class with
> `p^* ∘ c = ι_* ∘ j^* ∘ C`, the division of `Stacks.Chow.virtualNormalConeClass` by the flat
> pullback `p^*` along the bundle projection.

```lean
def virtualNormalBundleClass (𝒩 : VirtualNormalBundle i) (r : ℕ)
    [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} 𝒩.bundle r] :
    BivariantClass C (gysinSystemOfInvertible C) sZ sX i hi (r : ℤ)
```

**`Stacks.Chow.projectionPullbackClass_comp_virtualNormalBundleClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/VirtualNormalBundleClassConstruction.lean, line 381](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/VirtualNormalBundleClassConstruction.lean#L381). The attribute's comment: “the construction: p^* ∘ c(Z → X, 𝒩) = i\_* ∘ j^* ∘ C in A⁰(N → X), for 𝒩 of constant rank r”.

> **Stacks 0FBK, the defining relation `p^* ∘ c(Z ⟶ X, 𝒩) = ι_* ∘ j^* ∘ C`**, as an equality
> of bivariant classes in `A⁰(N ⟶ X)`: the composite (Stacks 0B75) of the class with the flat
> pullback along the bundle projection is the class `ι_* ∘ j^* ∘ C`, read in degree
> `-r + r = 0`.

```lean
theorem projectionPullbackClass_comp_virtualNormalBundleClass (𝒩 : VirtualNormalBundle i) (r : ℕ)
    [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} 𝒩.bundle r] :
    bivariantCompositeOfInvertible C (𝒩.projection ≫ sZ) sZ sX 𝒩.projection i rfl hi (-(r : ℤ))
        r (𝒩.projectionPullbackClass C sZ i r) (virtualNormalBundleClass C sZ sX i hi 𝒩 r) =
      BivariantClass.copy C (gysinSystemOfInvertible C) (𝒩.projection ≫ sZ) sX rfl
        (comp_comp_structureMorphism_eq rfl hi) (comp_comp_structureMorphism_eq rfl hi)
        (by ring : (0 : ℤ) = -(r : ℤ) + r) (virtualNormalConeClass C sZ sX i hi 𝒩)
```

**`Stacks.Chow.eq_virtualNormalBundleClass_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/VirtualNormalBundleClassConstruction.lean, line 395](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/VirtualNormalBundleClassConstruction.lean#L395). The attribute's comment: “uniqueness: c(Z → X, 𝒩) is the only class in A^r(Z → X) with p^* ∘ c = i\_* ∘ j^* ∘ C (Stacks 02TY)”.

> **Stacks 0FBK, uniqueness**: a bivariant class `c ∈ A^r(Z ⟶ X)` is `c(Z ⟶ X, 𝒩)` exactly
> when `p^* ∘ c = ι_* ∘ j^* ∘ C`.

```lean
theorem eq_virtualNormalBundleClass_iff (𝒩 : VirtualNormalBundle i) (r : ℕ)
    [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} 𝒩.bundle r]
    (c : BivariantClass C (gysinSystemOfInvertible C) sZ sX i hi (r : ℤ)) :
    c = virtualNormalBundleClass C sZ sX i hi 𝒩 r ↔
      bivariantCompositeOfInvertible C (𝒩.projection ≫ sZ) sZ sX 𝒩.projection i rfl hi
          (-(r : ℤ)) r (𝒩.projectionPullbackClass C sZ i r) c =
        BivariantClass.copy C (gysinSystemOfInvertible C) (𝒩.projection ≫ sZ) sX rfl
          (comp_comp_structureMorphism_eq rfl hi) (comp_comp_structureMorphism_eq rfl hi)
          (by ring : (0 : ℤ) = -(r : ℤ) + r) (virtualNormalConeClass C sZ sX i hi 𝒩)
```

**`Stacks.Chow.VirtualNormalBundle.bivariantRestriction_virtualNormalClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalClass/BaseChange.lean, line 850](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalClass/BaseChange.lean#L850). The attribute's comment: “compatibility with base change at constant rank r: for X' → X locally of finite type, c(Z ×\_X X' → X', g^*𝒩) = res(c(Z → X, 𝒩)) in A^r(Z ×\_X X' → X') (Stacks 0FBJ, 0F9Z)”.

> **Compatibility with base change**: for a closed immersion `i : Z ⟶ X`, a virtual normal
> bundle `𝒩` for `i` of constant rank `r` and `h : X' ⟶ X` locally of finite type, the class
> `c(Z' ⟶ X', 𝒩')` of the virtual normal bundle `𝒩' = g^*𝒩` for `Z' = Z ×_X X' ⟶ X'` is the
> restriction of `c(Z ⟶ X, 𝒩)`.

```lean
theorem bivariantRestriction_virtualNormalClass :
    bivariantRestrictionOfInvertible C sZ sX i hZ h (r : ℤ) (𝒩.virtualNormalClass C sX sZ hZ r) =
      (𝒩.baseChangeAlong (IsPullback.of_hasPullback i h).flip).virtualNormalClass C (h ≫ sX)
        (pullback.fst i h ≫ sZ) (pullbackSnd_comp_structureMorphism_eq C sZ sX i hZ h) r
```

**`Stacks.Chow.VirtualNormalBundle.completedClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalClass/Components.lean, line 249](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalClass/Components.lean#L249). The attribute's comment: “the class c(Z → X, 𝒩) ∈ A^*(Z → X)^∧ of a virtual normal bundle of arbitrary rank; its degree p part restricts on each connected component Z\_k to c(Z\_k → W\_k, 𝒩|Z\_k) of the construction when 𝒩 has rank p there, and to zero otherwise”.

> **Stacks 0FBK.** The class `c(Z ⟶ X, 𝒩) ∈ A^*(Z ⟶ X)^∧` of a virtual normal bundle whose rank
> need not be constant: the element of the completed bivariant group of Stacks 0FE0 whose degree
> `p` part is the class `c_p ∈ A^p(Z ⟶ X)` restricting to `c(Z_k ⟶ W_k, 𝒩|_{Z_k})` on every connected
> component `Z_k` on which `𝒩` has rank `p`, and to zero on the others. The schemes `Z` and `X`
> are locally Noetherian, being locally of finite type over the base.

```lean
def completedClass : completedBivariantGroup C (gysinSystemOfInvertible C) sZ sX i hZ
```

**`Stacks.Chow.VirtualNormalBundle.virtualNormalClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalClass/Construction.lean, line 183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalClass/Construction.lean#L183). The attribute's comment: “the construction at constant rank r: the class c(Z → X, 𝒩) ∈ A^r(Z → X), the quotient of ι\_* ∘ j^* ∘ C by p^*, which is bijective on Chow groups (Stacks 02TY)”.

> **Stacks 0FBK, the construction: the class `c(Z ⟶ X, 𝒩) ∈ A^r(Z ⟶ X)`** of a virtual normal
> bundle of constant rank `r` for a closed immersion: the bivariant class with
> `p^* ∘ c(Z ⟶ X, 𝒩) = ι_* ∘ j^* ∘ C`, that is, `c(Z ⟶ X, 𝒩) ∩ α` is the unique `β` with
> `p^* β = ι_* j^*(C ∩ α)`.

```lean
def virtualNormalClass :
    BivariantClass C (gysinSystemOfInvertible C) sZ sX i hZ r
```

**`Stacks.Chow.VirtualNormalBundle.isBivariantClassComposition_virtualNormalClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalClass/Construction.lean, line 215](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalClass/Construction.lean#L215). The attribute's comment: “the construction at constant rank r: p^* ∘ c(Z → X, 𝒩) = ι\_* ∘ j^* ∘ C as an identity of bivariant classes in A⁰(N → X)”.

> **Stacks 0FBK, the characterizing relation `p^* ∘ c(Z ⟶ X, 𝒩) = ι_* ∘ j^* ∘ C`**, as an
> identity of bivariant classes in `A⁰(N ⟶ X)` (Stacks 0FE0).

```lean
theorem isBivariantClassComposition_virtualNormalClass :
    haveI := 𝒩.locallyOfFiniteType_projection r
    haveI := 𝒩.flat_projection r
    IsBivariantClassComposition C (gysinSystemOfInvertible C) (𝒩.proj ≫ sZ)
      sZ sX 𝒩.proj i rfl hZ (properPushforwardDescends C) (-(r : ℤ)) r
      (𝒩.pullbackClass C sZ r) (𝒩.virtualNormalClass C sX sZ hZ r)
      (𝒩.pushforwardClass C sX sZ hZ r)
```

**`Stacks.Chow.VirtualNormalBundle.eq_virtualNormalClass_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalClass/Statement.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalClass/Statement.lean#L70). The attribute's comment: “(1), constant rank r: a class c ∈ A^r(Z → X) equals the constructed class c(Z → X, 𝒩) iff p^* ∘ c = ι\_* ∘ j^* ∘ C on Chow groups of T ×\_X N for every T → X locally of finite type, so c(Z → X, 𝒩) is the unique class with this property”.

> **Stacks 0FBK (1), constant rank.** For `𝒩` of constant rank `r`, with `p : N ⟶ Z` the vector
> bundle of `𝒩`, `C ∈ A^0(W_∞ ⟶ X)` the class of Stacks 0F9J, `j : C_ZX ⟶ W_∞` and
> `ι : C_ZX ⟶ N`, a class `c ∈ A^r(Z ⟶ X)` satisfies `p^* ∘ c = ι_* ∘ j^* ∘ C` (read on
> `T ×_X N` for every `T ⟶ X` locally of finite type) if and only if it is the class
> `c(Z ⟶ X, 𝒩)` of the construction; such a class exists because `p^*` is bijective on Chow groups
> (Stacks 02TY).

```lean
theorem eq_virtualNormalClass_iff (r : ℕ)
    [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} 𝒩.bundle r]
    (c : BivariantClass C (gysinSystemOfInvertible C) sZ sX i hZ r) :
    c = 𝒩.virtualNormalClass C sX sZ hZ r ↔
      ∀ {T : Scheme.{u}} (t : T ⟶ X) [LocallyOfFiniteType t] (k : ℤ)
        (α : chowGroup C (t ≫ sX) k),
        haveI := 𝒩.locallyOfFiniteType_projection r
        haveI := 𝒩.flat_projection r
        middleCap C (gysinSystemOfInvertible C) (𝒩.proj ≫ sZ) sZ 𝒩.proj i
            rfl (-(r : ℤ)) (𝒩.pullbackClass C sZ r) t (k - r) (c.cap t k α) =
          chowGroupDegreeEquiv C (pullback.fst (𝒩.proj ≫ i) t ≫ (𝒩.proj ≫ sZ))
            (by ring : k - (-(r : ℤ) + r) = k - r - -(r : ℤ))
            ((𝒩.pushforwardClass C sX sZ hZ r).cap t k α)
```

**`Stacks.Chow.VirtualNormalBundle.restriction_completedClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalClass/Statement.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalClass/Statement.lean#L92). The attribute's comment: “(1): the degree p part of c(Z → X, 𝒩) ∈ A^*(Z → X)^∧ restricts on each connected component Z\_k to the class of the construction for 𝒩|Z\_k if 𝒩 has rank p there, else to zero”.

> **Stacks 0FBK (1).** The degree `p` part of `c(Z ⟶ X, 𝒩) ∈ A^*(Z ⟶ X)^∧`, restricted to the
> piece `Z_k ⟶ W_k` of a connected component `Z_k` of `Z` (Stacks 0FDZ), is the class
> `c(Z_k ⟶ W_k, 𝒩|_{Z_k})` of the construction when `𝒩` has rank `p` on `Z_k`, and zero otherwise.

```lean
theorem restriction_completedClass (p : ℤ) (k : _root_.ConnectedComponents Z) :
    haveI := LocallyOfFiniteType.isLocallyNoetherian sZ
    haveI := LocallyOfFiniteType.isLocallyNoetherian sX
    bivariantPieceRestrictionOfInvertible C sZ sX i hZ p Z.connectedComponentOpens
        (componentAmbient i) id (le_preimage_componentAmbient i) k
        (completedBivariantSequenceOfInvertible C sZ sX i hZ (𝒩.completedClass C sX sZ hZ) p) =
      𝒩.componentFamily C sX sZ hZ p k
```

**`Stacks.Chow.VirtualNormalBundle.eq_completedClass_of_restriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalClass/Statement.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalClass/Statement.lean#L109). The attribute's comment: “(1), uniqueness: c(Z → X, 𝒩) is the only element of A^*(Z → X)^∧ with these restrictions to the connected components”.

> **Stacks 0FBK (1), uniqueness.** `c(Z ⟶ X, 𝒩)` is the only element of `A^*(Z ⟶ X)^∧` whose
> degree `p` parts restrict on the connected components of `Z` to the classes of the construction
> in the degree of the rank of `𝒩`, and to zero in the other degrees.

```lean
theorem eq_completedClass_of_restriction
    (c : completedBivariantGroup C (gysinSystemOfInvertible C) sZ sX i hZ) :
    haveI := LocallyOfFiniteType.isLocallyNoetherian sZ
    haveI := LocallyOfFiniteType.isLocallyNoetherian sX
    (∀ (p : ℤ) (k : _root_.ConnectedComponents Z),
      bivariantPieceRestrictionOfInvertible C sZ sX i hZ p Z.connectedComponentOpens
          (componentAmbient i) id (le_preimage_componentAmbient i) k
          (completedBivariantSequenceOfInvertible C sZ sX i hZ c p) =
        𝒩.componentFamily C sX sZ hZ p k) →
      c = 𝒩.completedClass C sX sZ hZ
```

**`Stacks.Chow.VirtualNormalBundle.baseChange_completedClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalClass/Statement.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalClass/Statement.lean#L137). The attribute's comment: “(2): c(Z' → X', g^*𝒩) = res(c(Z → X, 𝒩)) in A^*(Z' → X')^∧ for every X' → X locally of finite type”.

> **Stacks 0FBK (2), compatibility with base change.** For `h : X' ⟶ X` locally of finite type,
> `Z' = Z ×_X X'` and the virtual normal bundle `𝒩' = g^*𝒩` of Stacks 0FBJ for `Z' ⟶ X'`,
> `c(Z' ⟶ X', 𝒩')` is the restriction `res(c(Z ⟶ X, 𝒩))` of Stacks 0F9Z, on the completed groups
> of Stacks 0FE0.

```lean
theorem baseChange_completedClass {X' : Scheme.{u}} (h : X' ⟶ X) [LocallyOfFiniteType h] :
    haveI := LocallyOfFiniteType.isLocallyNoetherian sZ
    haveI := LocallyOfFiniteType.isLocallyNoetherian sX
    haveI := LocallyOfFiniteType.isLocallyNoetherian (h ≫ sX)
    haveI := LocallyOfFiniteType.isLocallyNoetherian (pullback.fst i h ≫ sZ)
    (𝒩.baseChangePullback h).completedClass C (h ≫ sX) (pullback.fst i h ≫ sZ)
        (pullbackSnd_comp_structureMorphism_eq C sZ sX i hZ h) =
      completedBivariantRestrictionOfInvertible C sZ sX i hZ h (𝒩.completedClass C sX sZ hZ)
```

**`Stacks.Chow.VirtualNormalBundle.completedClass_of_constantRank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalClass/Statement.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalClass/Statement.lean#L156). The attribute's comment: “(3): for 𝒩 of constant rank r, c(Z → X, 𝒩) lies in A^r(Z → X): its degree r part is the class of the construction and its other parts vanish”.

> **Stacks 0FBK (3).** If `𝒩` has constant rank `r`, then `c(Z ⟶ X, 𝒩) ∈ A^r(Z ⟶ X)`: its degree
> `r` part is the class `c(Z ⟶ X, 𝒩)` of the construction (the unique class with
> `p^* ∘ c = ι_* ∘ j^* ∘ C`) and its other parts vanish.

```lean
theorem completedClass_of_constantRank (r : ℕ)
    [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} 𝒩.bundle r] (p : ℤ) :
    haveI := LocallyOfFiniteType.isLocallyNoetherian sZ
    haveI := LocallyOfFiniteType.isLocallyNoetherian sX
    completedBivariantSequenceOfInvertible C sZ sX i hZ (𝒩.completedClass C sX sZ hZ) p =
      if h : (r : ℤ) = p then h ▸ 𝒩.virtualNormalClass C sX sZ hZ r else 0
```

## Tag 0FBL, a lemma

[Tag 0FBL](https://stacks.math.columbia.edu/tag/0FBL) in the Stacks Project.

**`Stacks.Chow.completedVirtualNormalGysinClass_eq_of_isTopChernComposition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/CompletedVirtualNormalSubbundle.lean, line 259](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/CompletedVirtualNormalSubbundle.lean#L259). The attribute's comment: “c(Z → X, N) = c\_top(E) ∘ c(Z → X, N') in A^*(Z → X)^∧ for a short exact sequence 0 → N' → N → E → 0 of finite locally free modules of arbitrary rank whose surjection factors through that of N'”.

> **Stacks 0FBL.** Let `(S, δ)` be the base situation of chapter 42, let `X` be locally of
> finite type over `S`, let `i : Z ⟶ X` be a closed subscheme with virtual normal sheaf `𝒩`, and
> let `0 ⟶ 𝒩' ⟶ 𝒩 ⟶ ℰ ⟶ 0` be a short exact sequence of finite locally free `𝒪_Z`-modules, of
> arbitrary ranks, such that the conormal surjection `σ : 𝒩^∨ ⟶ 𝒞_{Z/X}` factors as
> `σ' ∘ (𝒩^∨ ⟶ (𝒩')^∨)` through that of `𝒩'`. Then
>
>   `c(Z ⟶ X, 𝒩) = c_top(ℰ) ∘ c(Z ⟶ X, 𝒩')`
>
> in the completed bivariant group `A^*(Z ⟶ X)^∧` of Stacks 0FE0, for the classes of Stacks 0FBK,
> the top Chern class of Stacks 0FA4 and the composition on completions; the composite is a class
> for `𝟙 Z ≫ i = i`.
>
> On a connected component `Z_a` of `Z` both sides are concentrated in the degree `r_a` of `𝒩`, and
> there this is Stacks 0FBL at constant rank for `Z_a ⟶ U_a` composed with `(U_a ⟶ X_b)^*`.

```lean
theorem completedVirtualNormalGysinClass_eq_of_isTopChernComposition
    (w : inc ≫ pr = 0) (hseq : (ShortComplex.mk inc pr w).ShortExact)
    (hsigma : dualMap inc ≫ 𝒩'.surjection = 𝒩.surjection) :
    haveI : IsLocallyNoetherian Z := LocallyOfFiniteType.isLocallyNoetherian sZ
    haveI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    completedVirtualNormalGysinClass C sZ sX i hi 𝒩 =
      completedBivariantGroup.copy C (Category.id_comp i) _ hi
        (completedBivariantCompositeOfInvertible C sZ sZ sX (𝟙 Z) i (Category.id_comp sZ) hi
          (topChernClassOfInvertible C sZ Eb)
          (completedVirtualNormalGysinClass C sZ sX i hi 𝒩'))
```

**`Stacks.Chow.virtualNormalGysinCap_eq_topChernCap_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/VirtualNormalSubbundle.lean, line 347](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/VirtualNormalSubbundle.lean#L347). The attribute's comment: “c(Z -> X, N) = c\_top(E) composed with c(Z -> X, N') for a short exact sequence 0 -> N' -> N -> E -> 0 of finite locally free O\_Z-modules of constant ranks m', m, e whose conormal surjection factors. The short exact sequence IS consumed: it gives m = m' + e, which is what puts the two sides in the same Chow group. Both classes are the ones CHARACTERIZED by Tag 0FBK, neither being constructed in this repository, and the composite is spelled by the top Chern cap rule at `Fin.last e` as Tag 0FAA spells it. CARRIED: Tag 0FAA at the base changes of the two bundle projections (`SubbundleGysinTopChernStep`) -- 0FAA is proved only over the base scheme for the canonical bundles, with no identification of a base-changed vector bundle with the bundle of a pulled-back module; the geometric consequence of the tag's own factoring hypothesis, i\_* = j\_* composed with i'\_* (`SubbundleGysinFactorization`), Tags 0637, 0FBH and 0F9J being absent. THE TAG'S SHEAF-LEVEL FACTORING HYPOTHESIS IS PRESENT AS `_hsigma` BUT UNUSED: the proof runs on that carried geometric consequence instead. Also carried: Tag 02TY injectivity only, Tag 02S1 descent, Tag 0B7G as this directory's standing cap-rule parameter”.

> **Stacks 0FBL**, on cap operations. Let `(S, δ)` be the base situation of chapter 42, let `X`
> be locally of finite type over `S`, let `i : Z ⟶ X` be a closed subscheme with virtual normal
> sheaf `𝒩` of constant rank `m`, and let `0 ⟶ 𝒩' ⟶ 𝒩 ⟶ ℰ ⟶ 0` be a short exact sequence of finite
> locally free `𝒪_Z`-modules of constant ranks `m'`, `m` and `e` whose inclusion dualizes to a
> factorization `σ = σ' ∘ (𝒩^∨ ⟶ (𝒩')^∨)` of the conormal surjection of `𝒩` through that of `𝒩'`.
> Then, for the classes `c = c(Z ⟶ X, 𝒩)` and `c' = c(Z ⟶ X, 𝒩')` of Stacks 0FBK,
>
>   `c ∩ α = c_top(ℰ) ∩ (c' ∩ α)`
>
> on every test scheme `g : T ⟶ X`, in every degree and for every `α ∈ A_k(T)`. Since a bivariant
> class is determined by its cap operations (`Stacks.Chow.BivariantClass.ext`), this is the tag's
> equality `c(Z ⟶ X, 𝒩) = c_top(ℰ) ∘ c(Z ⟶ X, 𝒩')` of bivariant classes; see
> `Stacks.Chow.virtualNormalGysinClass_eq_of_isTopChernComposition`.

```lean
theorem virtualNormalGysinCap_eq_topChernCap_comp
    (w : inc ≫ pr = 0) (hseq : (ShortComplex.mk inc pr w).ShortExact)
    (_hsigma : dualMap inc ≫ P'.normalBundle.surjection = P.normalBundle.surjection) (x : Z)
    (hinj : ∀ {T : Scheme.{u}} (g : T ⟶ X) [LocallyOfFiniteType g] (k : ℤ),
      Function.Injective
        (bundleFlatPullback C sZ sN i q hq m P.flat P.relativeDimension hdesc g k))
    (hfactor : SubbundleGysinFactorization C G sZ sX sN sN' i hi q q' hq hq' j hj E E')
    (hstep : SubbundleGysinTopChernStep C sZ sN sN' i q q' hq hq' j hj m m' e Eb cap hdesc P P')
    {c : BivariantClass C G sZ sX i hi (m : ℤ)}
    {c' : BivariantClass C G sZ sX i hi (m' : ℤ)}
    (hc : IsVirtualNormalGysinClass C G sZ sX sN i hi q hq m 0 E
      (bundleFlatPullback C sZ sN i q hq m P.flat P.relativeDimension hdesc) P c)
    (hc' : IsVirtualNormalGysinClass C G sZ sX sN' i hi q' hq' m' 0 E'
      (bundleFlatPullback C sZ sN' i q' hq' m' P'.flat P'.relativeDimension hdesc) P' c')
    {T : Scheme.{u}} (g : T ⟶ X) [LocallyOfFiniteType g] (k : ℤ)
    (α : chowGroup C (g ≫ sX) k) :
    c.cap g k α =
      chowGroupDegreeEquiv C (pullback.fst i g ≫ sZ)
        (subbundleVirtualNormalDegree_eq P P' Eb inc pr w hseq x k)
        (subbundleTopChernCap C sZ i m' e Eb cap g k (c'.cap g k α))
```

**`Stacks.Chow.virtualNormalGysinClass_eq_of_isTopChernComposition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/VirtualNormalSubbundle.lean, line 392](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/VirtualNormalSubbundle.lean#L392). The attribute's comment: “c(Z -> X, N) = c\_top(E) composed with c(Z -> X, N') for a short exact sequence 0 -> N' -> N -> E -> 0 of finite locally free O\_Z-modules of constant ranks m', m, e whose conormal surjection factors. The short exact sequence IS consumed: it gives m = m' + e, which is what puts the two sides in the same Chow group. Read as an equality of classes in A^m(Z -> X) via `BivariantClass.ext`. Both classes are the ones CHARACTERIZED by Tag 0FBK, neither being constructed in this repository, and the composite is spelled by the top Chern cap rule at `Fin.last e` as Tag 0FAA spells it. CARRIED: Tag 0FAA at the base changes of the two bundle projections (`SubbundleGysinTopChernStep`) -- 0FAA is proved only over the base scheme for the canonical bundles, with no identification of a base-changed vector bundle with the bundle of a pulled-back module; the geometric consequence of the tag's own factoring hypothesis, i\_* = j\_* composed with i'\_* (`SubbundleGysinFactorization`), Tags 0637, 0FBH and 0F9J being absent. THE TAG'S SHEAF-LEVEL FACTORING HYPOTHESIS IS PRESENT AS `_hsigma` BUT UNUSED: the proof runs on that carried geometric consequence instead. Also carried: Tag 02TY injectivity only, Tag 02S1 descent, Tag 0B7G as this directory's standing cap-rule parameter”.

> **Stacks 0FBL**, as an equality in `A^m(Z ⟶ X)`. If `d` is a bivariant class of degree `m`
> for `i : Z ⟶ X` whose cap operation is cap with `c(Z ⟶ X, 𝒩')` followed by `c_top(ℰ)`, that is
> if `d` is the composite `c_top(ℰ) ∘ c(Z ⟶ X, 𝒩')`, then `d = c(Z ⟶ X, 𝒩)`.
>
> The composite is described by its cap operation, in the idiom of
> `Stacks.Chow.IsBivariantClassComposition`.

```lean
theorem virtualNormalGysinClass_eq_of_isTopChernComposition
    (w : inc ≫ pr = 0) (hseq : (ShortComplex.mk inc pr w).ShortExact)
    (hsigma : dualMap inc ≫ P'.normalBundle.surjection = P.normalBundle.surjection) (x : Z)
    (hinj : ∀ {T : Scheme.{u}} (g : T ⟶ X) [LocallyOfFiniteType g] (k : ℤ),
      Function.Injective
        (bundleFlatPullback C sZ sN i q hq m P.flat P.relativeDimension hdesc g k))
    (hfactor : SubbundleGysinFactorization C G sZ sX sN sN' i hi q q' hq hq' j hj E E')
    (hstep : SubbundleGysinTopChernStep C sZ sN sN' i q q' hq hq' j hj m m' e Eb cap hdesc P P')
    {c d : BivariantClass C G sZ sX i hi (m : ℤ)}
    {c' : BivariantClass C G sZ sX i hi (m' : ℤ)}
    (hc : IsVirtualNormalGysinClass C G sZ sX sN i hi q hq m 0 E
      (bundleFlatPullback C sZ sN i q hq m P.flat P.relativeDimension hdesc) P c)
    (hc' : IsVirtualNormalGysinClass C G sZ sX sN' i hi q' hq' m' 0 E'
      (bundleFlatPullback C sZ sN' i q' hq' m' P'.flat P'.relativeDimension hdesc) P' c')
    (hd : ∀ {T : Scheme.{u}} (g : T ⟶ X) [LocallyOfFiniteType g] (k : ℤ)
      (α : chowGroup C (g ≫ sX) k),
      d.cap g k α =
        chowGroupDegreeEquiv C (pullback.fst i g ≫ sZ)
          (subbundleVirtualNormalDegree_eq P P' Eb inc pr w hseq x k)
          (subbundleTopChernCap C sZ i m' e Eb cap g k (c'.cap g k α))) :
    d = c
```

**`Stacks.Chow.VirtualNormalBundle.completedClass_eq_topChernClassCompleted_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalClass/SubbundleCompleted.lean, line 544](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalClass/SubbundleCompleted.lean#L544). The attribute's comment: “c(Z → X, 𝒩) = c\_top(ℰ) ∘ c(Z → X, 𝒩') in A^*(Z → X)^∧, for a short exact sequence 0 → 𝒩' → 𝒩 → ℰ → 0 of finite locally free O\_Z-modules along which σ factors through σ' : (𝒩')^∨ → C\_\{Z/X}; ranks arbitrary, c(Z → X, -) the completed classes of Tag 0FBK, c\_top(ℰ) the completed class of Tag 0FA4, ∘ the composition of Tag 0FE0”.

> **Stacks 0FBL.** Let `i : Z ⟶ X` be a closed immersion with virtual normal sheaf `𝒩`, let
> `0 ⟶ 𝒩' ⟶ 𝒩 ⟶ ℰ ⟶ 0` be a short exact sequence of finite locally free `𝒪_Z`-modules, and let
> `σ' : (𝒩')^∨ ⟶ 𝒞_{Z/X}` be such that `σ = σ' ∘ (𝒩^∨ ⟶ (𝒩')^∨)`. Then
>
>   `c(Z ⟶ X, 𝒩) = c_top(ℰ) ∘ c(Z ⟶ X, 𝒩')`   in   `A^*(Z ⟶ X)^∧`,
>
> where `c(Z ⟶ X, -)` is the class of Stacks 0FBK, `c_top(ℰ) ∈ A^*(Z)^∧` the top Chern class of
> Stacks 0FA4, `∘` the composition `A^*(Z)^∧ × A^*(Z ⟶ X)^∧ ⟶ A^*(Z ⟶ X)^∧` of Stacks 0FE0, and the
> composite, a class for `𝟙 Z ≫ i`, is read at `i`.

```lean
theorem completedClass_eq_topChernClassCompleted_comp :
    haveI := LocallyOfFiniteType.isLocallyNoetherian sZ
    haveI := LocallyOfFiniteType.isLocallyNoetherian sX
    𝒩.completedClass C sX sZ hZ =
      completedBivariantGroupCongr C (gysinSystemOfInvertible C) sZ sX (Category.id_comp i)
        (comp_comp_structureMorphism_eq (Category.id_comp sZ) hZ) hZ
        (completedBivariantCompositeOfInvertible C sZ sZ sX (𝟙 Z) i (Category.id_comp sZ) hZ
          (topChernClassCompleted C sZ E).1
          ((𝒩.ofFactor N' inc σ' hσ).completedClass C sX sZ hZ))
```

## Tag 0FV7, a lemma

[Tag 0FV7](https://stacks.math.columbia.edu/tag/0FV7) in the Stacks Project.

**`Stacks.Chow.completedVirtualNormalGysinRestriction_eq_of_isTopChernComposition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/CompletedVirtualNormalRestrictionExcess.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/CompletedVirtualNormalRestrictionExcess.lean#L73). The attribute's comment: “res(c(Z → X, N)) = c\_top(E) ∘ c(Z' → X', N') in A^*(Z' → X')^∧, for a cartesian square of closed immersions (the chosen fibre product Z' = Z ×\_X X', where restriction lives), virtual normal sheaves N, N' of arbitrary rank, and a short exact sequence 0 → N' → g^*N → E → 0 of finite locally free modules whose dual square against the conormal sheaves commutes; c the completed classes of Tag 0FBK, c\_top(E) of Tag 0FA4, the composite read at Z' → X'; proved as in the source, by the base-change clause of Tag 0FBK and then Tag 0FBL”.

> **Stacks 0FV7.** Let `Z' = Z ×_X X'` be the chosen base change of a closed immersion
> `i : Z ⟶ X` along `f : X' ⟶ X`, both locally of finite type over the base, let `𝒩` be a virtual
> normal sheaf for `Z ⊂ X` and `𝒩'` one for `Z' ⟶ X'`, of arbitrary ranks, and let
> `0 ⟶ 𝒩' ⟶ g^*𝒩 ⟶ ℰ ⟶ 0` be a short exact sequence of finite locally free `𝒪_{Z'}`-modules such
> that the square of `hcomm` commutes. Then
>
>   `res(c(Z ⟶ X, 𝒩)) = c_top(ℰ) ∘ c(Z' ⟶ X', 𝒩')`
>
> in `A^*(Z' ⟶ X')^∧`, for the classes of Stacks 0FBK, the top Chern class of Stacks 0FA4 and the
> composition on completions (a class for `𝟙 ≫ (Z' ⟶ X')`).

```lean
theorem completedVirtualNormalGysinRestriction_eq_of_isTopChernComposition
    (w : inc ≫ pr = 0) (hseq : (ShortComplex.mk inc pr w).ShortExact)
    (hcomm : pullbackDualMap (pullback.fst i f) N.bundle ≫
        dualMap inc ≫ 𝒩'.surjection =
      (modulePullback (pullback.fst i f).toLRSHom.toShHom).map N.surjection ≫
        Stacks.Immersion.immersionConormalSheafMap (pullback.snd i f) i (pullback.fst i f) f
          (Stacks.Immersion.toShHom_square (isPullback_pullbackSnd i f).w)) :
    haveI : IsLocallyNoetherian Z := LocallyOfFiniteType.isLocallyNoetherian sZ
    haveI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    haveI : IsLocallyNoetherian X' := LocallyOfFiniteType.isLocallyNoetherian (f ≫ sX)
    haveI : IsLocallyNoetherian (pullback i f) :=
      LocallyOfFiniteType.isLocallyNoetherian (pullback.fst i f ≫ sZ)
    completedBivariantRestrictionViaSequence C sZ sX i hi f
        (completedVirtualNormalGysinClass C sZ sX i hi N) =
      completedBivariantGroup.copy C (Category.id_comp (pullback.snd i f)) _
        (pullbackSnd_comp_structureMorphism_eq C sZ sX i hi f)
        (completedBivariantCompositeOfInvertible C (pullback.fst i f ≫ sZ)
          (pullback.fst i f ≫ sZ) (f ≫ sX) (𝟙 _) (pullback.snd i f) (Category.id_comp _)
          (pullbackSnd_comp_structureMorphism_eq C sZ sX i hi f)
          (topChernClassOfInvertible C (pullback.fst i f ≫ sZ) Eb)
          (completedVirtualNormalGysinClass C (pullback.fst i f ≫ sZ) (f ≫ sX) (pullback.snd i f)
            (pullbackSnd_comp_structureMorphism_eq C sZ sX i hi f) 𝒩'))
```

**`Stacks.Chow.VirtualNormalBundle.completedBivariantRestriction_completedClass_eq_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalClass/ExcessBaseChange.lean, line 174](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalClass/ExcessBaseChange.lean#L174). The attribute's comment: “res(c(Z → X, 𝒩)) = c\_top(ℰ) ∘ c(Z' → X', 𝒩') in A^*(Z' → X')^∧ for the cartesian square Z' = Z ×\_X X' of a closed immersion i along X' → X locally of finite type, virtual normal sheaves 𝒩 for Z ⊂ X and 𝒩' for Z' ⊂ X', and a short exact sequence 0 → 𝒩' → g^*𝒩 → ℰ → 0 of finite locally free O\_\{Z'}-modules whose dual square against the conormal sheaves commutes; ranks arbitrary, c the completed classes of Tag 0FBK, res on completed groups, c\_top(ℰ) of Tag 0FA4, ∘ the composition of Tag 0FE0”.

> **Stacks 0FV7.** Let `i : Z ⟶ X` be a closed immersion of schemes locally of finite type over
> the base, `h : X' ⟶ X` locally of finite type, and `Z' = Z ×_X X'` with its closed immersion
> `i' : Z' ⟶ X'` and projection `g : Z' ⟶ Z`. Let `𝒩` be a virtual normal sheaf for `Z ⊂ X` and
> `𝒩'` one for `Z' ⊂ X'`, and let `0 ⟶ 𝒩' ⟶ g^*𝒩 ⟶ ℰ ⟶ 0` be a short exact sequence of finite
> locally free `𝒪_{Z'}`-modules such that the square
> `g^*𝒩^∨ ⟶ (𝒩')^∨ ⟶ 𝒞_{Z'/X'}` = `g^*𝒩^∨ ⟶ g^*𝒞_{Z/X} ⟶ 𝒞_{Z'/X'}` commutes (`hcomm`). Then
>
>   `res(c(Z ⟶ X, 𝒩)) = c_top(ℰ) ∘ c(Z' ⟶ X', 𝒩')`   in   `A^*(Z' ⟶ X')^∧`,
>
> where `c(-, -)` are the classes of Stacks 0FBK, `res` the restriction of Stacks 0F9Z on the
> completed groups, `c_top(ℰ) ∈ A^*(Z')^∧` the top Chern class of Stacks 0FA4 and `∘` the
> composition of Stacks 0FE0; the composite, a class for `𝟙 Z' ≫ i'`, is read at `i'`. No rank is
> assumed constant.
>
> The proof is the source's: Stacks 0FBK gives `res(c(Z ⟶ X, 𝒩)) = c(Z' ⟶ X', g^*𝒩)`, the
> commuting square says that the conormal surjection of `g^*𝒩` factors through `σ'` along the dual
> of `𝒩' ⟶ g^*𝒩`, and Stacks 0FBL concludes.

```lean
theorem completedBivariantRestriction_completedClass_eq_comp :
    haveI := LocallyOfFiniteType.isLocallyNoetherian sZ
    haveI := LocallyOfFiniteType.isLocallyNoetherian sX
    haveI := LocallyOfFiniteType.isLocallyNoetherian (h ≫ sX)
    haveI := LocallyOfFiniteType.isLocallyNoetherian (pullback.fst i h ≫ sZ)
    completedBivariantRestrictionOfInvertible C sZ sX i hZ h (𝒩.completedClass C sX sZ hZ) =
      completedBivariantGroupCongr C (gysinSystemOfInvertible C) (pullback.fst i h ≫ sZ)
        (h ≫ sX) (Category.id_comp (pullback.snd i h))
        (comp_comp_structureMorphism_eq (Category.id_comp _)
          (pullbackSnd_comp_structureMorphism_eq C sZ sX i hZ h))
        (pullbackSnd_comp_structureMorphism_eq C sZ sX i hZ h)
        (completedBivariantCompositeOfInvertible C (pullback.fst i h ≫ sZ)
          (pullback.fst i h ≫ sZ) (h ≫ sX) (𝟙 _) (pullback.snd i h) (Category.id_comp _)
          (pullbackSnd_comp_structureMorphism_eq C sZ sX i hZ h)
          (topChernClassCompleted C (pullback.fst i h ≫ sZ) E).1
          (𝒩'.completedClass C (h ≫ sX) (pullback.fst i h ≫ sZ)
            (pullbackSnd_comp_structureMorphism_eq C sZ sX i hZ h)))
```

## Tag 0FBM, a lemma

[Tag 0FBM](https://stacks.math.columbia.edu/tag/0FBM) in the Stacks Project.

**`Stacks.Chow.completedVirtualNormalGysinCap_fundamentalChowClass_excess`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/CompletedExcessIntersectionFormula.lean, line 348](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/CompletedExcessIntersectionFormula.lean#L348). The attribute's comment: “c(Z → X, N) ∩ [Y]\_n = c\_top(E) ∩ [Z ×\_X Y]\_\{n-r} in CH\_*(Z ×\_X Y), for N a virtual normal sheaf of arbitrary rank, c(Z → X, N) ∈ A^*(Z → X)^∧, Z ×\_X Y → Y regular with conormal sheaf of constant rank r, E the excess normal sheaf, and dim\_δ(Y) ≤ n; stated degree by degree”.

> Let `i : Z ⟶ X` be a closed immersion of schemes locally of finite type over the base with a
> virtual normal sheaf `𝒩` (Stacks 0FBQ), of arbitrary rank, and let `g : Y ⟶ X` be locally of
> finite type such that the base change `i' : Z' = Z ×_X Y ⟶ Y` is a regular closed immersion whose
> conormal sheaf `𝒞_{Z'/Y}` has constant rank `r`. Let `ℰ` be the excess normal sheaf,
> `0 ⟶ ℰ^∨ ⟶ 𝒩^∨|_{Z'} ⟶ 𝒞_{Z'/Y} ⟶ 0`. If `dim_δ(Y) ≤ n` then
>
>   `c(Z ⟶ X, 𝒩) ∩ [Y]_n = c_top(ℰ) ∩ [Z']_{n - r}`
>
> in `CH_*(Z ×_X Y)`, for the class `c(Z ⟶ X, 𝒩) ∈ A^*(Z ⟶ X)^∧` of Stacks 0FBK
> (`Stacks.Chow.completedVirtualNormalGysinClass`) and the top Chern class of Stacks 0FA4: in
> degree `n - (r + e)` the degree-`(r + e)` part of the left-hand side is the cap product of
> `[Z']_{n - r}` with the degree-`e` part of `c_top(ℰ)` (`Stacks.Chow.topChernCap`), and in degree
> `n - p` for `p < r` the left-hand side vanishes, as the right-hand side does.

```lean
theorem completedVirtualNormalGysinCap_fundamentalChowClass_excess
    (hreg : IsRegularImmersion i') (r : ℕ)
    [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} (conormalModule i') r]
    (n : ℤ) (hY : schemeDeltaDimension C (g ≫ sX) ≤ (n : EInt)) :
    haveI : IsLocallyNoetherian Z := LocallyOfFiniteType.isLocallyNoetherian sZ
    haveI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    haveI : SheafOfModules.IsFiniteLocallyFree.{u, u, u}
        (𝒩.baseChange i i' g' g sq).excessNormalSheaf :=
      (𝒩.baseChange i i' g' g sq).isFiniteLocallyFree_excessNormalSheaf
        (SheafOfModules.IsFiniteLocallyFreeOfRank.isFiniteLocallyFree _ r)
    (∀ e : ℕ, (completedBivariantSequenceOfInvertible C sZ sX i hi
        (completedVirtualNormalGysinClass C sZ sX i hi 𝒩) ((r + e : ℕ) : ℤ)).cap g n
          (fundamentalChowClass C (g ≫ sX) n) =
        chowPushforwardOfIso C sZ' (pullback.fst i g ≫ sZ) sq.flip.isoPullback.hom
          (isoPullback_hom_comp_structureMorphism C sZ sX sq hi sZ' hi') (n - ((r + e : ℕ) : ℤ))
          (chowGroupDegreeEquiv C sZ' (by push_cast; ring)
            (topChernCap C sZ' (𝒩.baseChange i i' g' g sq).excessNormalSheaf (n - (r : ℤ)) e
              (fundamentalChowClass C sZ' (n - (r : ℤ)))))) ∧
      ∀ p : ℤ, p < r → (completedBivariantSequenceOfInvertible C sZ sX i hi
        (completedVirtualNormalGysinClass C sZ sX i hi 𝒩) p).cap g n
          (fundamentalChowClass C (g ≫ sX) n) = 0
```

**`Stacks.Chow.virtualNormalGysinCap_fundamentalChowClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/ExcessIntersection.lean, line 429](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/ExcessIntersection.lean#L429). The attribute's comment: “at vanishing excess, where `c_top(ℰ) = 1`: `c(Z ⟶ X, 𝒩) ∩ [Y]_n = [Z ×_X Y]_{n-m}` for the class of Stacks 0FBK, proved from its characterizing relation; carried: `ι_* j^* C` on `[Y]_n` — 0F9J, 02TB and most of 0FBG and 0FBH are proved, but the map `j : C_ZX ⟶ W_∞` is not, needing clauses (4) and (5) of 0FBG and condition (3) of 063M; see the implementation notes — injectivity of `p^*` (02TY), the δ-dim bound”.

> **Stacks 0FBM at vanishing excess.** In the situation of the virtual normal sheaf, let
> `g : Y ⟶ X` be locally of finite type and assume that `Z ×_X Y ⟶ Y` is cut out by a regular
> sequence of length `m`, so that the excess normal sheaf vanishes and `c_top(ℰ) = 1`. If
> `dim_δ(Z ×_X Y) ≤ n - m` then
>
>   `c(Z ⟶ X, 𝒩) ∩ [Y]_n = [Z ×_X Y]_{n - m}`
>
> in `A_{n-m}(Z ×_X Y)`, for the class `c` of Stacks 0FBK, that is for any bivariant class of
> degree `m` satisfying the characterizing relation of that tag against the genuine flat pullback
> `Stacks.Chow.bundleFlatPullback` of the bundle projection.
>
> The proof is the source's: the relation says `p^*(c ∩ [Y]_n) = (ι_* ∘ j^* ∘ C) ∩ [Y]_n`, the
> right-hand side is the fundamental class of `N ×_X Y` — the hypothesis `hcone` — and the left-hand
> side is `p^*` of the candidate, which is that same fundamental class by
> `Stacks.Chow.bundleFlatPullbackChow_fundamentalChowClass`; now divide by `p^*`.
>
> See the implementation notes for what `hcone`, `hinj` and `hdim` are and why none of them is this
> conclusion.

```lean
theorem virtualNormalGysinCap_fundamentalChowClass
    (hinj : ∀ {T : Scheme.{u}} (g : T ⟶ X) [LocallyOfFiniteType g] (k : ℤ),
      Function.Injective
        (bundleFlatPullback C sZ sN i q hq m P.flat P.relativeDimension hdesc g k))
    {c : BivariantClass C G sZ sX i hi (m : ℤ)}
    (hc : IsVirtualNormalGysinClass C G sZ sX sN i hi q hq m 0 E
      (bundleFlatPullback C sZ sN i q hq m P.flat P.relativeDimension hdesc) P c)
    {Y : Scheme.{u}} (g : Y ⟶ X) [LocallyOfFiniteType g] (n : ℤ)
    (hdim : schemeDeltaDimension C (pullback.fst i g ≫ sZ) ≤ ((n - (m : ℤ) : ℤ) : EInt))
    (hcone : chowGroupDegreeEquiv C (pullback.fst (q ≫ i) g ≫ sN)
        (by omega : n - (0 : ℤ) = (n - (m : ℤ)) + (m : ℤ))
        (E.cap g n (fundamentalChowClass C (g ≫ sX) n)) =
      fundamentalChowClass C (pullback.fst (q ≫ i) g ≫ sN) ((n - (m : ℤ)) + (m : ℤ))) :
    c.cap g n (fundamentalChowClass C (g ≫ sX) n) =
      fundamentalChowClass C (pullback.fst i g ≫ sZ) (n - (m : ℤ))
```

**`Stacks.Chow.virtualNormalGysinCap_fundamentalChowClass_excess`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/ExcessIntersection.lean, line 479](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/ExcessIntersection.lean#L479). The attribute's comment: “with excess: `c(Z ⟶ X, 𝒩) ∩ [Y]_n = c_top(ℰ) ∩ [Z ×_X Y]_{n-r}`, the normal cone given as a rank-`r` sub-bundle `CN` (063M) and `c_top(ℰ)` as the map `cTop` — `Stacks.Chow.topChernClassOfInvertible` of 0FA4 is proved, but at the Gysin system of the first Chern class, while the higher Chern classes for the Gysin system here are carried as elsewhere in this directory; carried also: Stacks 0FAA for `CN ⟶ N ×_X Y`, proved at the constructed bundles of a short exact sequence but not at an arbitrary sub-bundle”.

> **Stacks 0FBM.** In the situation of the virtual normal sheaf, let `g : Y ⟶ X` be locally of
> finite type, assume `Z ×_X Y ⟶ Y` is a regular closed immersion whose conormal sheaf has constant
> rank `r`, and let `ℰ` be the excess normal sheaf, of rank `m - r`. If `dim_δ(Y) = n` then
>
>   `c(Z ⟶ X, 𝒩) ∩ [Y]_n = c_top(ℰ) ∩ [Z ×_X Y]_{n - r}`
>
> in `A_{n-m}(Z ×_X Y)`.
>
> The regular immersion and the excess sheaf enter through the data they produce: the normal cone
> `C_{Z ×_X Y} Y` is a vector bundle `CN` of rank `r` over `Z ×_X Y`, by the identification
> `𝒞_{*} = Sym(𝒞)` of Stacks 063M, embedded in `N ×_X Y` over `Z ×_X Y` by `ιC` and `pC`; and the
> cap product with `c_top(ℰ)` is the additive map `cTop`, of degree `m - r` by its typing. See the
> implementation notes.
>
> Besides the three hypotheses of `Stacks.Chow.virtualNormalGysinCap_fundamentalChowClass` the proof
> carries one statement, `hexcess`, which is **Stacks 0FAA** for the embedding `CN ⟶ N ×_X Y` of
> vector bundles over `Z ×_X Y`: `ι_* (p')^* α = p^*(c_top(ℰ) ∩ α)`. That lemma is proved, as
> `Stacks.Chow.subbundleEmbedding_pushforward_flatPullback_eq_topChernCap`, but at the canonical
> constructed bundles of a short exact sequence rather than at an arbitrary sub-bundle `CN`, so it
> does not discharge the hypothesis as stated here; see the implementation notes. It is a formula in
> `A_*(N ×_X Y)`, one bundle level above this conclusion, and mentions no bivariant class for
> `Z ⟶ X`.

```lean
theorem virtualNormalGysinCap_fundamentalChowClass_excess
    (hinj : ∀ {T : Scheme.{u}} (g : T ⟶ X) [LocallyOfFiniteType g] (k : ℤ),
      Function.Injective
        (bundleFlatPullback C sZ sN i q hq m P.flat P.relativeDimension hdesc g k))
    {c : BivariantClass C G sZ sX i hi (m : ℤ)}
    (hc : IsVirtualNormalGysinClass C G sZ sX sN i hi q hq m 0 E
      (bundleFlatPullback C sZ sN i q hq m P.flat P.relativeDimension hdesc) P c)
    {Y : Scheme.{u}} (g : Y ⟶ X) [LocallyOfFiniteType g] (n : ℤ) (r : ℕ)
    (hdim : schemeDeltaDimension C (pullback.fst i g ≫ sZ) ≤ ((n - (r : ℤ) : ℤ) : EInt))
    {CN : Scheme.{u}} (ιC : CN ⟶ pullback (q ≫ i) g) [IsClosedImmersion ιC]
    (pC : CN ⟶ pullback i g) [LocallyOfFiniteType pC] [AlgebraicGeometry.Flat pC]
    (hpC : AlgebraicGeometry.RelativeDimension pC r)
    (hCN : ιC ≫ bundleTestBaseChange i q g = pC)
    (cTop : chowGroup C (pullback.fst i g ≫ sZ) (n - (r : ℤ)) →+
      chowGroup C (pullback.fst i g ≫ sZ) (n - (m : ℤ)))
    (hcone : chowGroupDegreeEquiv C (pullback.fst (q ≫ i) g ≫ sN)
        (by omega : n - (0 : ℤ) = (n - (r : ℤ)) + (r : ℤ))
        (E.cap g n (fundamentalChowClass C (g ≫ sX) n)) =
      chowPushforwardOfIsClosedImmersion C (pC ≫ (pullback.fst i g ≫ sZ))
        (pullback.fst (q ≫ i) g ≫ sN) ιC
        (by rw [← bundleTestBaseChange_comp_structureMorphism i q sZ sN hq g,
          ← Category.assoc, hCN]) ((n - (r : ℤ)) + (r : ℤ))
        (fundamentalChowClass C (pC ≫ (pullback.fst i g ≫ sZ)) ((n - (r : ℤ)) + (r : ℤ))))
    (hexcess : ∀ α : chowGroup C (pullback.fst i g ≫ sZ) (n - (r : ℤ)),
      chowGroupDegreeEquiv C (pullback.fst (q ≫ i) g ≫ sN)
          (by omega : (n - (m : ℤ)) + (m : ℤ) = (n - (r : ℤ)) + (r : ℤ))
          (bundleFlatPullbackChow C sZ sN i q hq m P.flat P.relativeDimension hdesc g
            (n - (m : ℤ)) (cTop α)) =
        chowPushforwardOfIsClosedImmersion C (pC ≫ (pullback.fst i g ≫ sZ))
          (pullback.fst (q ≫ i) g ≫ sN) ιC
          (by rw [← bundleTestBaseChange_comp_structureMorphism i q sZ sN hq g,
            ← Category.assoc, hCN]) ((n - (r : ℤ)) + (r : ℤ))
          (flatPullbackChow C (pC ≫ (pullback.fst i g ≫ sZ)) (pullback.fst i g ≫ sZ) pC rfl r hpC
            (n - (r : ℤ))
            (hdesc (pC ≫ (pullback.fst i g ≫ sZ)) (pullback.fst i g ≫ sZ) pC rfl r hpC
              (n - (r : ℤ))) α)) :
    c.cap g n (fundamentalChowClass C (g ≫ sX) n) =
      cTop (fundamentalChowClass C (pullback.fst i g ≫ sZ) (n - (r : ℤ)))
```

## Tag 0FEA, a lemma

[Tag 0FEA](https://stacks.math.columbia.edu/tag/0FEA) in the Stacks Project.

**`Stacks.Chow.virtualNormalGysinClass_cap_fundamentalChowClass_of_isCohenMacaulayLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/VirtualNormalCapCohenMacaulay.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/VirtualNormalCapCohenMacaulay.lean#L67).

> **Stacks 0FEA.** Let `(S, δ)` be as in Stacks 02QL, let `X` be locally of finite type over
> `S`, let `𝒩` be a virtual normal sheaf for a closed subscheme `i : Z ⟶ X` (Stacks 0FBQ), and let
> `g : Y ⟶ X` be locally of finite type. Given integers `r` and `n`, assume
>
> 1. `𝒩` is locally free of rank `r`,
> 2. every irreducible component of `Y` has `δ`-dimension `n`,
> 3. `dim_δ(Z ×_X Y) ≤ n - r`, and
> 4. `𝒪_{Y, ξ}` is Cohen–Macaulay for every `ξ ∈ Z ×_X Y` with `δ(ξ) = n - r`.
>
> Then `c(Z ⟶ X, 𝒩) ∩ [Y]_n = [Z ×_X Y]_{n - r}` in `CH_{n - r}(Z ×_X Y)`.
>
> The proof is the source's: at the points of `Z ×_X Y` of `δ`-dimension `n - r` the ideal of
> `Z ×_X Y` is generated by a regular sequence of length `r`, so `Z ×_X Y ⟶ Y` is a regular closed
> immersion of codimension `r` near them, where the excess normal sheaf vanishes and Stacks 0FBM
> (`Stacks.Chow.virtualNormalGysinClass_capRegularFormula`) applies; this is
> `Stacks.Chow.BivariantClass.cap_fundamentalChowClass_eq_of_capRegularFormula`.

```lean
theorem virtualNormalGysinClass_cap_fundamentalChowClass_of_isCohenMacaulayLocalRing
    [LocallyOfFiniteType i] {n : ℤ} {Y : Scheme.{u}} (g : Y ⟶ X) [LocallyOfFiniteType g]
    (hY : ∀ W : irreducibleComponents Y,
      deltaDimension C (g ≫ sX)
        ⟨W, W.2.1, isClosed_of_mem_irreducibleComponents (W : Set Y) W.2⟩ = n)
    (hZY : schemeDeltaDimension C (pullback.snd i g ≫ (g ≫ sX)) ≤ ((n - r : ℤ) : EInt))
    (hCM : ∀ ξ : (pullback i g : Scheme.{u}),
      relativeDimension C.dimensionFunction (g ≫ sX) ((pullback.snd i g).base ξ) = n - r →
      letI : IsLocallyNoetherian Y := LocallyOfFiniteType.isLocallyNoetherian (g ≫ sX)
      IsCohenMacaulayLocalRing (Y.presheaf.stalk ((pullback.snd i g).base ξ))) :
    (virtualNormalBundleClass C sZ sX i hi 𝒩 r).cap g n (fundamentalChowClass C (g ≫ sX) n) =
      fundamentalChowClass C (pullback.fst i g ≫ sZ) (n - r)
```

**`Stacks.Chow.isRegular_of_isCohenMacaulayLocalRing_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/VirtualNormalCapFundamental.lean, line 238](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/VirtualNormalCapFundamental.lean#L238). The attribute's comment: “the regular sequence of the proof: hypotheses (1)-(4) force the ideal of `Z ×_X Y` in `𝒪_{Y, ξ}` to be generated by a regular sequence of length `r` at every point of `Z ×_X Y` of `δ`-dimension `n - r`. The cap product `c(Z ⟶ X, 𝒩) ∩ [Y]_n` is NOT stated, Stacks 0FBK having no carrier here. See the implementation notes”.

> **Stacks 0FEA, the regular sequence of the proof.** Let `(S, δ)` be as in Stacks 02QL, let
> `X` be locally of finite type over `S`, let `i : Z ⟶ X` be a closed subscheme and let
> `g : Y ⟶ X` be locally of finite type. Assume
>
> * every irreducible component of `Y` has `δ`-dimension `n` (hypothesis (2)),
> * `dim_δ(Z ×_X Y) ≤ n - r` (hypothesis (3)),
> * `ξ ∈ Z ×_X Y` has `δ(ξ) = n - r` and `𝒪_{Y, ξ}` is Cohen–Macaulay (hypothesis (4)), and
> * the ideal of `Z ×_X Y` in `𝒪_{Y, ξ}` is generated by a list `xs` of `r` elements, which is
>   what hypothesis (1) provides.
>
> Then `xs` is a regular sequence. Equivalently: `Z ×_X Y` is cut out of `Y` by a regular sequence
> of length `r` at every point of `δ`-dimension `n - r`, which is what the source establishes
> before invoking the excess intersection formula of Stacks 0FBM to conclude
> `c(Z ⟶ X, 𝒩) ∩ [Y]_n = [Z ×_X Y]_{n - r}`. See the implementation notes for why that
> conclusion is not stated.

```lean
theorem isRegular_of_isCohenMacaulayLocalRing_stalk (C : ChowSituation.{u})
    {X Y Z : Scheme.{u}} (sX : X ⟶ C.S) [LocallyOfFiniteType sX]
    (i : Z ⟶ X) [IsClosedImmersion i] (g : Y ⟶ X) [LocallyOfFiniteType g] {n : ℤ} {r : ℕ}
    (hY : ∀ W : irreducibleComponents Y,
      deltaDimension C (g ≫ sX)
        ⟨W, W.2.1, isClosed_of_mem_irreducibleComponents (W : Set Y) W.2⟩ = n)
    (hZY : schemeDeltaDimension C (pullback.snd i g ≫ (g ≫ sX)) ≤ ((n - r : ℤ) : EInt))
    (ξ : (pullback i g : Scheme.{u}))
    (hξ : relativeDimension C.dimensionFunction (g ≫ sX) ((pullback.snd i g).base ξ) = n - r)
    (hCM : letI : IsLocallyNoetherian Y := LocallyOfFiniteType.isLocallyNoetherian (g ≫ sX)
      IsCohenMacaulayLocalRing (Y.presheaf.stalk ((pullback.snd i g).base ξ)))
    (xs : List (Y.presheaf.stalk ((pullback.snd i g).base ξ))) (hlen : xs.length = r)
    (hxs : Ideal.ofList xs = RingHom.ker ((pullback.snd i g).stalkMap ξ).hom) :
    RingTheory.Sequence.IsRegular (Y.presheaf.stalk ((pullback.snd i g).base ξ)) xs
```

## Tag 0FBN, a lemma

[Tag 0FBN](https://stacks.math.columbia.edu/tag/0FBN) in the Stacks Project.

**`Stacks.Chow.gysinBivariantClass_eq_virtualNormalBundleClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/DivisorVirtualNormalBundleClass.lean, line 336](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/DivisorVirtualNormalBundleClass.lean#L336). The attribute's comment: “unconditional: the constructed Gysin class of Tag 0B79 equals the constructed class c(D → X, 𝒩) of Tag 0FBK for 𝒩 = i^*L with the canonical surjection onto the conormal sheaf, as bivariant classes, so on every test scheme and in every degree”.

> **Stacks 0FBN.** Let `(S, δ)` be as in Situation 02QL, let `X` be locally of finite type over
> `S` and let `(ℒ, s, i : D ⟶ X)` be a triple as in Definition 02T8. The Gysin homomorphism `i^*`,
> viewed as an element of `A^1(D ⟶ X)` (Stacks 0B79, `Stacks.Chow.gysinBivariantClass`), is the
> bivariant class `c(D ⟶ X, 𝒩) ∈ A^1(D ⟶ X)` of Stacks 0FBK (`Stacks.Chow.virtualNormalBundleClass`)
> constructed using `𝒩 = i^*ℒ` viewed as a virtual normal sheaf for `D` in `X`
> (`Stacks.Chow.zeroSchemeVirtualNormalBundle`, with the canonical surjection
> `(i^*ℒ)^∨ ⟶ 𝒞_{D/X}`).
>
> This is `Stacks.Chow.gysinBivariantClass_eq_virtualNormalBundleClass_of_iso`, which holds for any
> surjection `(i^*ℒ)^∨ ⟶ 𝒞_{D/X}`, at the canonical one.

```lean
theorem gysinBivariantClass_eq_virtualNormalBundleClass :
    (gysinBivariantClass C sX L s).1 =
      virtualNormalBundleClass C (gysinTripleInclusion L s ≫ sX) sX (gysinTripleInclusion L s)
        rfl (zeroSchemeVirtualNormalBundle L s) 1
```

## Tag 0FBP, a lemma

[Tag 0FBP](https://stacks.math.columbia.edu/tag/0FBP) in the Stacks Project.

**`Stacks.Chow.virtualNormalGysinClass_bivariantCommute_of_subbundle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/VirtualNormalCommuting.lean, line 357](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/VirtualNormalCommuting.lean#L357). The attribute's comment: “with the factorization c(Z ⟶ X, 𝒩) = c\_top(ℰ) ∘ c(Z ⟶ X, 𝒩') PROVED, by consuming Stacks 0FBL for a short exact sequence 0 ⟶ 𝒩' ⟶ 𝒩 ⟶ ℰ ⟶ 0. CARRIED: the centrality of the top Chern cap of ℰ for c (Stacks 02UA, formalized only against the projective bundle rule and not this directory's carried cap rule), and that c commutes with c(Z ⟶ X, 𝒩')”.

> **Stacks 0FBP with the factorization proved.** Let `i : Z ⟶ X` be a closed subscheme with
> virtual normal sheaf `𝒩` of constant rank `m`, let `0 ⟶ 𝒩' ⟶ 𝒩 ⟶ ℰ ⟶ 0` be a short exact
> sequence of finite locally free modules whose conormal surjection factors as Stacks 0FBL asks,
> let `g : Y ⟶ X` be locally of finite type and let `c ∈ A^p(Y ⟶ X)`. If `c` commutes with
> `c(Z ⟶ X, 𝒩')` and the top Chern cap of `ℰ` is central for `c`, then `c` commutes with
> `c(Z ⟶ X, 𝒩)`.
>
> The factorization `c(Z ⟶ X, 𝒩) = c_top(ℰ) ∘ c(Z ⟶ X, 𝒩')` is **not** carried here: it is
> Stacks 0FBL, `Stacks.Chow.virtualNormalGysinCap_eq_topChernCap_comp`, and its hypotheses — the
> short exact sequence, the factoring of the conormal surjection, the injectivity of Stacks 02TY,
> and the two carried inputs of that tag — are threaded through. What is carried is the centrality
> of the top Chern cap, which is Stacks 02UA; the commutation with `c(Z ⟶ X, 𝒩')` is a hypothesis
> here and is discharged for a divisor in
> `Stacks.Chow.virtualNormalGysinClass_bivariantCommute_of_divisor`.

```lean
theorem virtualNormalGysinClass_bivariantCommute_of_subbundle
    (w : inc ≫ pr = 0) (hseq : (ShortComplex.mk inc pr w).ShortExact)
    (hsigma : dualMap inc ≫ P'.normalBundle.surjection = P.normalBundle.surjection) (x : Z)
    (hinj : ∀ {T : Scheme.{u}} (g : T ⟶ X) [LocallyOfFiniteType g] (k : ℤ),
      Function.Injective
        (bundleFlatPullback C (i ≫ sX) sN i q hq m P.flat P.relativeDimension hdesc g k))
    (hfactor : SubbundleGysinFactorization C G (i ≫ sX) sX sN sN' i rfl q q' hq hq' j hj E E')
    (hstep : SubbundleGysinTopChernStep C (i ≫ sX) sN sN' i q q' hq hq' j hj m m' e Eb cap hdesc
      P P')
    {cN : BivariantClass C G (i ≫ sX) sX i rfl (m : ℤ)}
    {cN' : BivariantClass C G (i ≫ sX) sX i rfl (m' : ℤ)}
    (c : BivariantClass C G (f ≫ sX) sX f rfl p)
    (hcN : IsVirtualNormalGysinClass C G (i ≫ sX) sX sN i rfl q hq m 0 E
      (bundleFlatPullback C (i ≫ sX) sN i q hq m P.flat P.relativeDimension hdesc) P cN)
    (hcN' : IsVirtualNormalGysinClass C G (i ≫ sX) sX sN' i rfl q' hq' m' 0 E'
      (bundleFlatPullback C (i ≫ sX) sN' i q' hq' m' P'.flat P'.relativeDimension hdesc) P' cN')
    (hcentral : ExcessChernCapCommutesWithCap C G sX i f (m' : ℤ) (m : ℤ) p c
      (subbundleExcessChernOperator C sX i m m' e Eb cap P P' inc pr w hseq x))
    (hb : BivariantCommute C G sX i f (m' : ℤ) p cN' c) :
    BivariantCommute C G sX i f (m : ℤ) p cN c
```

**`Stacks.Chow.virtualNormalGysinClass_bivariantCommute_of_divisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/VirtualNormalCommuting.lean, line 433](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/VirtualNormalCommuting.lean#L433). The attribute's comment: “the effective Cartier divisor case, the case the source's reduction lands in. PROVED by consuming Stacks 0FBL (the factorization through the rank-one subsheaf), 0FBN (that factor is the Gysin class i^*) and 0FA3 (i^* commutes with c), with their own hypotheses threaded. CARRIED: only the centrality of the top Chern cap of ℰ, Stacks 02UA”.

> **Stacks 0FBP for an effective Cartier divisor**, the case the source's reduction lands in.
> Let `(𝓛, s, i : Z ⟶ X)` be a triple as in Stacks 02T8, so that `Z` is the zero scheme of `s` and
> hence an effective Cartier divisor, let `𝒩` be a virtual normal sheaf for `i` of constant rank
> `m`, let `𝒩' = i^*𝓛` be the rank-one virtual normal sheaf of the divisor sitting inside `𝒩` with
> quotient the excess sheaf `ℰ`, let `g : Y ⟶ X` be locally of finite type and let
> `c ∈ A^p(Y ⟶ X)`. Then `c(Z ⟶ X, 𝒩)` commutes with `c`.
>
> This is the source's argument with everything but one input discharged. The factorization
> `c(Z ⟶ X, 𝒩) = c_top(ℰ) ∘ c(Z ⟶ X, 𝒩')` is Stacks 0FBL; the identification of the second factor
> with the Gysin homomorphism `i^*` of Stacks 0B79 is Stacks 0FBN,
> `Stacks.Chow.gysinBivariantClass_eq_virtualNormalGysinClass`; and the commutation of `i^*` with
> `c` is Stacks 0FA3, `Stacks.Chow.gysinBivariantCommute`, which derives it from the Gysin
> condition in the definition of a bivariant class. The one carried input is the centrality of the
> top Chern cap of `ℰ`, Stacks 02UA.

```lean
theorem virtualNormalGysinClass_bivariantCommute_of_divisor
    (w : inc ≫ pr = 0) (hseq : (ShortComplex.mk inc pr w).ShortExact)
    (hsigma : dualMap inc ≫ P'.normalBundle.surjection = P.normalBundle.surjection)
    (x : (Stacks.Divisors.zeroScheme X L s).subscheme)
    (hinj : ∀ {T : Scheme.{u}} (g : T ⟶ X) [LocallyOfFiniteType g] (k : ℤ),
      Function.Injective
        (bundleFlatPullback C (gysinTripleInclusion L s ≫ sX) sN (gysinTripleInclusion L s) q hq
          m P.flat P.relativeDimension hdesc g k))
    (hinj' : ∀ {T : Scheme.{u}} (g : T ⟶ X) [LocallyOfFiniteType g] (k : ℤ),
      Function.Injective
        (bundleFlatPullback C (gysinTripleInclusion L s ≫ sX) sN' (gysinTripleInclusion L s) q'
          hq' 1 P'.flat P'.relativeDimension hdesc g k))
    (hfactor : SubbundleGysinFactorization C G (gysinTripleInclusion L s ≫ sX) sX sN sN'
      (gysinTripleInclusion L s) rfl q q' hq hq' j hj E E')
    (hstep : SubbundleGysinTopChernStep C (gysinTripleInclusion L s ≫ sX) sN sN'
      (gysinTripleInclusion L s) q q' hq hq' j hj m 1 e Eb cap hdesc P P')
    (cTop : DivisorTopChernCapFamily C sX L s)
    (hbundle : P'.normalBundle.bundle =
      (Scheme.Modules.pullback (gysinTripleInclusion L s)).obj L)
    (hG : G.IsNaturalUnderPullbackCompPushforward)
    {cN : BivariantClass C G (gysinTripleInclusion L s ≫ sX) sX (gysinTripleInclusion L s)
      rfl (m : ℤ)}
    {cN' gys : BivariantClass C G (gysinTripleInclusion L s ≫ sX) sX (gysinTripleInclusion L s)
      rfl ((1 : ℕ) : ℤ)}
    (c : BivariantClass C G (f ≫ sX) sX f rfl p)
    (hcN : IsVirtualNormalGysinClass C G (gysinTripleInclusion L s ≫ sX) sX sN
      (gysinTripleInclusion L s) rfl q hq m 0 E
      (bundleFlatPullback C (gysinTripleInclusion L s ≫ sX) sN (gysinTripleInclusion L s) q hq m
        P.flat P.relativeDimension hdesc) P cN)
    (hcN' : IsVirtualNormalGysinClass C G (gysinTripleInclusion L s ≫ sX) sX sN'
      (gysinTripleInclusion L s) rfl q' hq' 1 0 E'
      (bundleFlatPullback C (gysinTripleInclusion L s ≫ sX) sN' (gysinTripleInclusion L s) q'
        hq' 1 P'.flat P'.relativeDimension hdesc) P' cN')
    (hgys : IsGysinBivariantClass C G sX L s gys)
    (hoff : GysinCapFundamentalOffDivisor C G sX L s)
    (hon : GysinCapFundamentalOnDivisor C G sX L s cTop)
    (hvn : VirtualNormalCapFundamentalOnDivisor C G sX L s cTop cN')
    (hdim : ∀ {W : Scheme.{u}} (g : W ⟶ X) [LocallyOfFiniteType g] (n : ℤ),
      (¬ ∃ h : W ⟶ (Stacks.Divisors.zeroScheme X L s).subscheme,
        h ≫ gysinTripleInclusion L s = g) →
      schemeDeltaDimension C
          (pullback.fst (gysinTripleInclusion L s) g ≫ (gysinTripleInclusion L s ≫ sX)) ≤
        ((n - ((1 : ℕ) : ℤ) : ℤ) : EInt))
    (hcone : ∀ {W : Scheme.{u}} (g : W ⟶ X) [LocallyOfFiniteType g] (n : ℤ),
      (¬ ∃ h : W ⟶ (Stacks.Divisors.zeroScheme X L s).subscheme,
        h ≫ gysinTripleInclusion L s = g) →
      chowGroupDegreeEquiv C (pullback.fst (q' ≫ gysinTripleInclusion L s) g ≫ sN')
          (by omega : n - (0 : ℤ) = (n - ((1 : ℕ) : ℤ)) + ((1 : ℕ) : ℤ))
          (E'.cap g n (fundamentalChowClass C (g ≫ sX) n)) =
        fundamentalChowClass C (pullback.fst (q' ≫ gysinTripleInclusion L s) g ≫ sN')
          ((n - ((1 : ℕ) : ℤ)) + ((1 : ℕ) : ℤ)))
    (hcentral : ExcessChernCapCommutesWithCap C G sX (gysinTripleInclusion L s) f
      ((1 : ℕ) : ℤ) (m : ℤ) p c
      (subbundleExcessChernOperator C sX (gysinTripleInclusion L s) m 1 e Eb cap P P' inc pr w
        hseq x)) :
    BivariantCommute C G sX (gysinTripleInclusion L s) f (m : ℤ) p cN c
```

**`Stacks.Chow.VirtualNormalBundle.completedClass_bivariantCommute`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalClass/Commuting.lean, line 459](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/VirtualNormalClass/Commuting.lean#L459). The attribute's comment: “c(Z → X, 𝒩) ∈ A^*(Z → X)^∧ of Tag 0FBK commutes (Remark 0FA2) with every c ∈ A^p(Y → X), Y → X locally of finite type: each homogeneous part c(Z → X, 𝒩)\_n and c commute on every test scheme T → X; 𝒩 a virtual normal sheaf of arbitrary rank”.

> **Stacks 0FBP.** Let `(S, δ)` be as in Situation 02QL, let `X` be a scheme locally of finite
> type over `S`, let `Z ⊆ X` be a closed subscheme with virtual normal sheaf `𝒩`, let `g : Y ⟶ X`
> be locally of finite type and let `c ∈ A^p(Y ⟶ X)`. Then `c` and the class
> `c(Z ⟶ X, 𝒩) ∈ A^*(Z ⟶ X)^∧` of Stacks 0FBK commute in the sense of Remark 0FA2: for every
> degree `n`, the degree `n` part of `c(Z ⟶ X, 𝒩)` and `c` satisfy
> `c(Z ⟶ X, 𝒩)_n ∩ (c ∩ α) = c ∩ (c(Z ⟶ X, 𝒩)_n ∩ α)` in `CH_{k-n-p}(Z ×_X Y ×_X T)` for every
> `α ∈ CH_k(T)` and every `T ⟶ X` locally of finite type (`Stacks.Chow.BivariantCommute`). As
> commuting is additive in `c`, this is the commutation with every `c ∈ A^*(Y ⟶ X)`.
>
> The rank of `𝒩` is arbitrary. The class is `Stacks.Chow.VirtualNormalBundle.completedClass`, the
> class constructed in Stacks 0FBK from the class `C` of Stacks 0F9J, the normal cone and the vector
> bundle of `𝒩`; `Z` lies over `S` through `X`.

```lean
theorem VirtualNormalBundle.completedClass_bivariantCommute (𝒩 : VirtualNormalBundle i)
    {Y : Scheme.{u}} (g : Y ⟶ X) [LocallyOfFiniteType g] (n p : ℤ)
    (c : BivariantClass C (gysinSystemOfInvertible C) (g ≫ sX) sX g rfl p) :
    haveI := LocallyOfFiniteType.isLocallyNoetherian (i ≫ sX)
    haveI := LocallyOfFiniteType.isLocallyNoetherian sX
    BivariantCommute C (gysinSystemOfInvertible C) sX i g n p
      (completedBivariantSequenceOfInvertible C (i ≫ sX) sX i rfl
        (𝒩.completedClass C sX (i ≫ sX) rfl) n) c
```

## Tag 0FEB, a lemma

[Tag 0FEB](https://stacks.math.columbia.edu/tag/0FEB) in the Stacks Project.

**`Stacks.Chow.gysinBivariantCap_fundamentalChowClass_normalCone`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/NormalConeZeroSectionGysin.lean, line 851](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/NormalConeZeroSectionGysin.lean#L851). The attribute's comment: “PROVED, at the canonical Gysin system `Stacks.Chow.canonicalGysinSystem` (whose contained-component rule is the first Chern class of the restricted invertible module, Stacks 02SO), which is the o^* of the source. No hypothesis beyond the source's: X integral, locally of finite type over the base of delta-dimension n, Z and Y effective Cartier divisors with Z inside Y. The closed immersion C\_ZY -> Y x\_\{o, C\_YX} C\_ZX that the source leaves implicit is constructed, as `Stacks.Chow.normalConeToZeroFibre`, the unique morphism with the two components the source names (`Stacks.Chow.normalConeZeroSectionGysinRelation_hom_ext`). The proof goes through the deformation to the normal cone D(Z in X) and Tags 0B73, 02TB, 02TA, 02T9 and 0C4U rather than through the blowups of Tag 0FBG used by the source.”.

> **Stacks Project, Tag 0FEB.** Let `(S, δ)` be as in Situation 02QL, let `X` be an integral
> scheme locally of finite type over `S` of δ-dimension `n`, and let `Z ⊆ Y ⊆ X` be closed
> subschemes which are both effective Cartier divisors in `X`. Write `o : Y ⟶ C_YX` for the zero
> section of the normal line cone of `Y` in `X`. Then
>
>     `o^*[C_ZX]_n = [C_ZY]_{n-1}` in `CH_{n-1}(Y ×_{o, C_YX} C_ZX)`.
>
> Here `Y` and `Z` are `DY.subscheme` and `DZ.subscheme`, `Z ⊆ Y` is `hZY : DY ≤ DZ`, `o` is
> `Stacks.Conormal.normalConeZeroSection`, the morphism `C_ZX ⟶ C_YX` is
> `Stacks.Conormal.normalConeMapOfFactorization`, `o^*` is the cap operation
> `Stacks.Chow.gysinBivariantCap` of the canonical Gysin system at the presentation of `o(Y)` by
> `Stacks.Chow.zeroSectionDivisorSheaf` and `Stacks.Chow.zeroSectionDivisorSection`, and the closed
> immersion `C_ZY ⟶ Y ×_{o, C_YX} C_ZX` is `Stacks.Chow.normalConeToZeroFibre`.
>
> The proof is by the deformation to the normal cone `M = D(Z ⊆ X)`, of δ-dimension at most
> `n + 1`. It carries the divisor `Z(t⁻¹) ≅ C_ZX` and the divisor `E_Z`, the inverse image of the
> strict transform `E` of `Y` in `D(Y ⊆ X)`. On `C_ZX` the restriction of `𝒪(E_Z)` with its
> canonical section is `g^*𝒪(o(Y))` with its canonical section (Stacks 0C4U, as `κ_Y⁻¹E = o(Y)`), so
> the left-hand side is `1_{E_Z}|^* (t⁻¹)^*[M]_{n+1}` (Stacks 02TB(1) and 02TA). By
> [Stacks, Tag 0B73] this is `(t⁻¹)|^* 1_{E_Z}^*[M] = (t⁻¹)|^*[E_Z]`; `[E_Z]` and `[D(Z ⊆ Y)]` differ
> by a cycle supported in `Z(t⁻¹)`, on which the Gysin map of the trivial module kills it
> (Stacks 02T9); and `(t⁻¹)|^*[D(Z ⊆ Y)] = [D(Z ⊆ Y) ∩ Z(t⁻¹)] = [C_ZY]` by [Stacks, Tag 02TB].

```lean
theorem gysinBivariantCap_fundamentalChowClass_normalCone [IsIntegral X]
    (hn : schemeDeltaDimension C sX = (n : EInt)) :
    gysinBivariantCap C (canonicalGysinSystem C)
        (Stacks.Conormal.normalConeToBase DY.subschemeι ≫ DY.subschemeι ≫ sX)
        (zeroSectionDivisorSheaf DY) (zeroSectionDivisorSection DY)
        (Stacks.Conormal.normalConeMapOfFactorization DZ.subschemeι DY.subschemeι (inclusion hZY)
          (inclusion_subschemeι hZY)) n
        (fundamentalChowClass C
          (Stacks.Conormal.normalConeMapOfFactorization DZ.subschemeι DY.subschemeι
              (inclusion hZY) (inclusion_subschemeι hZY) ≫
            (Stacks.Conormal.normalConeToBase DY.subschemeι ≫ DY.subschemeι ≫ sX)) n) =
      QuotientAddGroup.mk'
        (rationalEquivalences C
          (pullback.fst
              (gysinTripleInclusion (zeroSectionDivisorSheaf DY) (zeroSectionDivisorSection DY))
              (Stacks.Conormal.normalConeMapOfFactorization DZ.subschemeι DY.subschemeι
                (inclusion hZY) (inclusion_subschemeι hZY)) ≫
            (gysinTripleInclusion (zeroSectionDivisorSheaf DY) (zeroSectionDivisorSection DY) ≫
              (Stacks.Conormal.normalConeToBase DY.subschemeι ≫ DY.subschemeι ≫ sX)))
          (n - 1))
        (cycleAssociatedToClosedSubscheme C
          (pullback.fst
              (gysinTripleInclusion (zeroSectionDivisorSheaf DY) (zeroSectionDivisorSection DY))
              (Stacks.Conormal.normalConeMapOfFactorization DZ.subschemeι DY.subschemeι
                (inclusion hZY) (inclusion_subschemeι hZY)) ≫
            (gysinTripleInclusion (zeroSectionDivisorSheaf DY) (zeroSectionDivisorSection DY) ≫
              (Stacks.Conormal.normalConeToBase DY.subschemeι ≫ DY.subschemeι ≫ sX)))
          (normalConeToZeroFibre DY DZ.subschemeι (inclusion hZY) (inclusion_subschemeι hZY))
          (n - 1))
```

**`Stacks.Chow.gysinBivariantClass_cap_normalCone`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/NormalLineConeZeroSectionGysin.lean, line 598](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/NormalLineConeZeroSectionGysin.lean#L598).

> **Stacks 0FEB.** Let `(S, δ)` be as in Situation 02QL, let `X` be a scheme locally of finite
> type over `S` with `dim_δ(X) ≤ n` (the source: `X` integral of `δ`-dimension `n`), and let
> `Z ⊆ Y ⊆ X` be closed subschemes, `iZY : Z ⟶ Y` the inclusion, with `Y` an effective Cartier
> divisor in `X` (the source also asks it of `Z`; that is not used). Let `o : Y ⟶ C_YX` be the zero
> section of the normal line cone, `o(Y) = D0 = normalConeZeroSectionIdeal iY`
> (`Stacks.Chow.ker_normalConeZeroSection`), an effective Cartier divisor of `C_YX`
> (`Stacks.Chow.isEffectiveCartierDivisor_normalConeZeroSectionIdeal`), and let
> `o^* ∈ A^1(Y ⟶ C_YX)` be its Gysin class (Stacks 0B79, `Stacks.Chow.gysinBivariantClass`, for the
> canonical section of `𝒪(D0)`). Let `φ : C_ZX ⟶ C_YX` be the canonical morphism of normal cones
> induced by `ℐ_Y ⊆ ℐ_Z` (`Stacks.Chow.normalConeChangeOfCentreMap`; on charts it is
> `Spec Gr_{ℐ_Z} ⟶ Spec Gr_{ℐ_Y}`). Then
>
>   `o^*[C_ZX]_n = [C_ZY]_{n-1}`  in  `CH_{n-1}(Y ×_{o, C_YX} C_ZX)`,
>
> where the fibre product is the base change of `o(Y) ⊆ C_YX` along `φ` (Stacks 0B6Y) and
> `[C_ZY]_{n-1}` is pushed forward along the closed immersion
> `Stacks.Chow.normalConeToZeroSectionPullback`, whose component to `C_ZX` is the comparison
> `C_ZY ⟶ C_ZX` of normal cones (`Stacks.Chow.normalConeToZeroSectionPullback_snd`).

```lean
theorem gysinBivariantClass_cap_normalCone {n : ℤ} (hZY : iZY ≫ iY = iZ)
    (hX : schemeDeltaDimension C sX ≤ (n : EInt)) :
    haveI := LocallyOfFiniteType.isLocallyNoetherian sX
    (gysinBivariantClass C (normalConeToX iY ≫ sX)
        (Stacks.Divisors.divisorSheaf (normalConeZeroSectionIdeal iY))
        (Stacks.Divisors.divisorSheafGlobalSection (normalConeZeroSectionIdeal iY))).1.cap
        (normalConeChangeOfCentreMap iZ iY (hZY ▸ Scheme.Hom.le_ker_comp iZY iY)) n
        (fundamentalChowClass C (normalConeChangeOfCentreMap iZ iY
          (hZY ▸ Scheme.Hom.le_ker_comp iZY iY) ≫ normalConeToX iY ≫ sX) n) =
      properChowPushforward C (normalConeToX iZY ≫ iY ≫ sX) _
        (normalConeToZeroSectionPullback iY iZ (hZY ▸ Scheme.Hom.le_ker_comp iZY iY) iZY
          (ker_eq_comap_ker_of_comp_eq iY iZ iZY hZY))
        (normalConeToZeroSectionPullback_toBase C sX iY iZ _ iZY _) (n - 1)
        (properPushforwardDescends C _ _ _ _ _)
        (fundamentalChowClass C (normalConeToX iZY ≫ iY ≫ sX) (n - 1))
```

## Tag 0FEC, a lemma

[Tag 0FEC](https://stacks.math.columbia.edu/tag/0FEC) in the Stacks Project.

**`Stacks.Chow.ConormalCompatibleVirtualNormalBundles`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedChernComposition.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedChernComposition.lean#L101). The attribute's comment: “the hypothesis of the lemma: the three virtual normal bundles of Stacks 0FBQ for Z ⊆ Y ⊆ X, the short exact sequence of their duals, and its two commutative squares against the genuine conormal sequence of Stacks 062S; stated for immersions rather than closed subschemes, which is a generalization”.

> For immersions `i : Z ⟶ Y` and `j : Y ⟶ X`, three virtual
> normal bundles — `𝒩` for `Z ⊆ X`, `𝒩'` for `Z ⊆ Y` and `𝒩''` for `Y ⊆ X` — together with a
> short exact sequence
>
>   `(𝒩'')^∨|_Z ⟶ 𝒩^∨ ⟶ (𝒩')^∨`
>
> of duals and the two commutative squares identifying it, through the structural surjections of
> the three virtual normal bundles, with the conormal sequence
>
>   `𝒞_{Y/X}|_Z ⟶ 𝒞_{Z/X} ⟶ 𝒞_{Z/Y}`
>
> of Stacks 062S.

```lean
structure ConormalCompatibleVirtualNormalBundles {Z Y X : Scheme.{u}} (i : Z ⟶ Y) (j : Y ⟶ X)
    [IsImmersion i] [IsImmersion j]
```

**`Stacks.Chow.localizedChernClass_cap_eq_bivariantCompositeCap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedChernComposition.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedChernComposition.lean#L158). The attribute's comment: “the conclusion, reduced to the composition of bivariant classes and read on cap products; the localized Chern class c(Z ⟶ X, 𝒩) of Stacks 0FBK is not constructed in this repository and is carried as a parameter, as everywhere else here, so that the composition formula is a hypothesis”.

> Granted that the class attached to
> `𝒩` composes the class attached to `𝒩'` with the class attached to `𝒩''`, its cap operation on
> a test scheme `t : T ⟶ X` is: cap with `c(Y ⟶ X, 𝒩'')`, then cap with `c(Z ⟶ Y, 𝒩')`, then push
> forward along the associativity isomorphism `(T ×_X Y) ×_Y Z ≅ T ×_X Z` of pullbacks, the
> degrees `k - (p + q)` and `(k - q) - p` being identified.

```lean
theorem localizedChernClass_cap_eq_bivariantCompositeCap
    (hc : IsBivariantClassComposition C G sZ sY sX i j hi hj hpp p q
      (cloc sZ sY i hi D.bundleZY p) (cloc sY sX j hj D.bundleYX q)
      (cloc sZ sX (i ≫ j) (comp_comp_structureMorphism_eq hi hj) D.bundleZX (p + q)))
    {T : Scheme.{u}} (t : T ⟶ X) [LocallyOfFiniteType t] (k : ℤ)
    (α : chowGroup C (t ≫ sX) k) :
    chowGroupDegreeEquiv C (pullback.fst (i ≫ j) t ≫ sZ)
        (by ring : k - (p + q) = (k - q) - p)
        ((cloc sZ sX (i ≫ j) (comp_comp_structureMorphism_eq hi hj) D.bundleZX (p + q)).cap
          t k α) =
      bivariantCompositeCap C G sZ sY sX i j hi hj hpp p q (cloc sZ sY i hi D.bundleZY p)
        (cloc sY sX j hj D.bundleYX q) t k α
```

**`Stacks.Chow.eq_localizedChernClass_of_isBivariantClassComposition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedChernComposition.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedChernComposition.lean#L178). The attribute's comment: “uniqueness: the composition formula determines c(Z ⟶ X, 𝒩), so the content of the lemma reduces to exhibiting the composite; the localized Chern class of Stacks 0FBK is carried as a parameter”.

> Any bivariant class of degree `p + q` for `Z ⟶ X` that composes `c(Z ⟶ Y, 𝒩')` with
> `c(Y ⟶ X, 𝒩'')` is `c(Z ⟶ X, 𝒩)`, provided the latter composes them.

```lean
theorem eq_localizedChernClass_of_isBivariantClassComposition
    (hc : IsBivariantClassComposition C G sZ sY sX i j hi hj hpp p q
      (cloc sZ sY i hi D.bundleZY p) (cloc sY sX j hj D.bundleYX q)
      (cloc sZ sX (i ≫ j) (comp_comp_structureMorphism_eq hi hj) D.bundleZX (p + q)))
    (c : BivariantClass C G sZ sX (i ≫ j) (comp_comp_structureMorphism_eq hi hj) (p + q))
    (hc' : IsBivariantClassComposition C G sZ sY sX i j hi hj hpp p q
      (cloc sZ sY i hi D.bundleZY p) (cloc sY sX j hj D.bundleYX q) c) :
    cloc sZ sX (i ≫ j) (comp_comp_structureMorphism_eq hi hj) D.bundleZX (p + q) = c
```

**`Stacks.Chow.completedVirtualNormalGysinClass_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedChernCompositionClass.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/LocalizedChernCompositionClass.lean#L103).

> **Stacks 0FEC.** Let `(S, δ)` be as in Situation 02QL, let `i : Z ⟶ Y` and `j : Y ⟶ X` be
> closed immersions of schemes locally of finite type over `S`, and let `𝒩`, `𝒩'`, `𝒩''` be
> virtual normal sheaves for `Z ⊆ X`, `Z ⊆ Y` and `Y ⊆ X` with a short exact sequence
> `(𝒩'')^∨|_Z ⟶ 𝒩^∨ ⟶ (𝒩')^∨` whose two squares against the conormal sequence
> `𝒞_{Y/X}|_Z ⟶ 𝒞_{Z/X} ⟶ 𝒞_{Z/Y}` commute (`Stacks.Chow.ConormalCompatibleVirtualNormalBundles`).
> Then
>
>   `c(Z ⟶ X, 𝒩) = c(Z ⟶ Y, 𝒩') ∘ c(Y ⟶ X, 𝒩'')`   in `A^*(Z ⟶ X)^∧`,
>
> for the classes of Stacks 0FBK (`Stacks.Chow.completedVirtualNormalGysinClass`) and the
> composition of Stacks 0FE0.

```lean
theorem completedVirtualNormalGysinClass_comp :
    haveI : IsLocallyNoetherian Z := LocallyOfFiniteType.isLocallyNoetherian sZ
    haveI : IsLocallyNoetherian Y := LocallyOfFiniteType.isLocallyNoetherian sY
    haveI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    completedVirtualNormalGysinClass C sZ sX (i ≫ j) (comp_comp_structureMorphism_eq hi hj)
        D.bundleZX =
      completedBivariantCompositeOfInvertible C sZ sY sX i j hi hj
        (completedVirtualNormalGysinClass C sZ sY i hi D.bundleZY)
        (completedVirtualNormalGysinClass C sY sX j hj D.bundleYX)
```

## Tag 0FBQ, a remark

[Tag 0FBQ](https://stacks.math.columbia.edu/tag/0FBQ) in the Stacks Project.

**`Stacks.Chow.completedCommutesWithEveryClass_completedVirtualNormalGysinClassOfOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/CompletedVirtualNormalCommuting.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/CompletedVirtualNormalCommuting.lean#L72). The attribute's comment: “(3), counterparts: the counterpart of Lemma 0FBP, c(Z → X, 𝒩) ∈ A^*(Z → X)^∧ commutes with every c ∈ A^*(Y → X), for an immersion Z → X and 𝒩 of arbitrary rank”.

> **The counterpart of Stacks 0FBP for immersions** (Stacks 0FBQ). For an immersion
> `i : Z ⟶ X` with a virtual normal bundle `𝒩` of arbitrary rank, the class
> `c(Z ⟶ X, 𝒩) = c(Z ⟶ U, 𝒩) ∘ (U ⟶ X)^* ∈ A^*(Z ⟶ X)^∧` commutes with every bivariant class over
> `X`, degree by degree.

```lean
theorem completedCommutesWithEveryClass_completedVirtualNormalGysinClassOfOpen (i : Z ⟶ X)
    [IsImmersion i] (hi : i ≫ sX = sZ) (U : X.Opens) (i' : Z ⟶ U.toScheme) [IsClosedImmersion i']
    (hU : i' ≫ U.ι = i) (𝒩 : VirtualNormalBundle i) :
    completedCommutesWithEveryClass C sZ sX i hi
      (completedVirtualNormalGysinClassOfOpen C sZ sX i hi U i' hU 𝒩)
```

**`Stacks.Chow.completedBivariantTransport_completedBivariantRestriction_completedVirtualNormalGysinClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/CompletedVirtualNormalImmersionBaseChange.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/CompletedVirtualNormalImmersionBaseChange.lean#L200). The attribute's comment: “(3), counterparts: the counterpart of the base-change clause of Lemma 0FBK, the restriction of c(Z → X, 𝒩) ∈ A^*(Z → X)^∧ along X' → X is c(Z' → X', g^*𝒩), for a cartesian square of immersions and 𝒩 of arbitrary rank”.

> **The counterpart for immersions of the base-change clause of Stacks 0FBK, at arbitrary
> rank.** For a cartesian square `Z' = Z ×_X X'` of immersions with `f : X' ⟶ X` locally of finite
> type, the restriction (Stacks 0F9Z) of `c(Z ⟶ X, 𝒩) ∈ A^*(Z ⟶ X)^∧` along `f`, carried to `Z'`
> along `Z ×_X X' ≅ Z'`, is `c(Z' ⟶ X', g^*𝒩) ∈ A^*(Z' ⟶ X')^∧`, with `g^*𝒩` the virtual normal
> bundle of Stacks 0FBJ; the opens through which the two immersions factor as closed immersions are
> arbitrary. Both sides are read degree by degree (Stacks 0FE0), and in each degree the cap
> operations agree by `Stacks.Chow.completedVirtualNormalGysinClassOfOpen_cap_baseChange`.

```lean
theorem completedBivariantTransport_completedBivariantRestriction_completedVirtualNormalGysinClass
    (V : X'.Opens) (iV : Z' ⟶ V.toScheme) [IsClosedImmersion iV] (hV : iV ≫ V.ι = i₂) :
    haveI : IsLocallyNoetherian Z := LocallyOfFiniteType.isLocallyNoetherian sZ
    haveI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    haveI : IsLocallyNoetherian Z' := LocallyOfFiniteType.isLocallyNoetherian sZ'
    haveI : IsLocallyNoetherian X' := LocallyOfFiniteType.isLocallyNoetherian (f ≫ sX)
    haveI : IsLocallyNoetherian (pullback i f) :=
      LocallyOfFiniteType.isLocallyNoetherian (pullback.fst i f ≫ sZ)
    completedBivariantTransport C (pullback.fst i f ≫ sZ) sZ' (f ≫ sX) (pullback.snd i f)
        (pullbackSnd_comp_structureMorphism_eq C sZ sX i hi f) i₂ hi₂ sq.flip.isoPullback.symm
        sq.flip.isoPullback_inv_snd
        (completedBivariantRestrictionViaSequence C sZ sX i hi f
          (completedVirtualNormalGysinClassOfOpen C sZ sX i hi U i' hU 𝒩)) =
      completedVirtualNormalGysinClassOfOpen C sZ' (f ≫ sX) i₂ hi₂ V iV hV
        (𝒩.baseChange i i₂ g' f sq)
```

**`Stacks.Chow.completedVirtualNormalGysinRestrictionOfOpen_eq_of_isTopChernComposition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/CompletedVirtualNormalImmersionBaseChange.lean, line 333](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/CompletedVirtualNormalImmersionBaseChange.lean#L333). The attribute's comment: “(3), counterparts: the counterpart of Lemma 0FV7, res(c(Z → X, N)) = c\_top(E) ∘ c(Z' → X', N') in A^*(Z' → X')^∧ for the chosen base change Z' = Z ×\_X X' of an immersion, virtual normal bundles N, N' of arbitrary rank and a short exact sequence 0 → N' → g^*N → E → 0 of finite locally free modules whose dual square against the conormal sheaves commutes”.

> **The counterpart of Stacks 0FV7 for immersions, at arbitrary rank.** Let `Z' = Z ×_X X'` be
> the chosen base change of an immersion `i : Z ⟶ X` along `f : X' ⟶ X`, let `𝒩` be a virtual normal
> bundle for `Z ⟶ X` and `𝒩'` one for `Z' ⟶ X'`, of arbitrary ranks, and let
> `0 ⟶ 𝒩' ⟶ g^*𝒩 ⟶ ℰ ⟶ 0` be a short exact sequence of finite locally free `𝒪_{Z'}`-modules such
> that the square of `hcomm` commutes. Then
>
>   `res(c(Z ⟶ X, 𝒩)) = c_top(ℰ) ∘ c(Z' ⟶ X', 𝒩')`
>
> in `A^*(Z' ⟶ X')^∧`, for the classes of Stacks 0FBQ (3) built from arbitrary opens through which
> the two immersions factor as closed immersions. By the counterpart of the base-change clause of
> Stacks 0FBK and the counterpart of Stacks 0FBL.

```lean
theorem completedVirtualNormalGysinRestrictionOfOpen_eq_of_isTopChernComposition (V : X'.Opens)
    (iV : pullback i f ⟶ V.toScheme) [IsClosedImmersion iV] (hV : iV ≫ V.ι = pullback.snd i f)
    (w : inc ≫ pr = 0) (hseq : (ShortComplex.mk inc pr w).ShortExact)
    (hcomm : pullbackDualMap (pullback.fst i f) N.bundle ≫
        dualMap inc ≫ 𝒩'.surjection =
      (modulePullback (pullback.fst i f).toLRSHom.toShHom).map N.surjection ≫
        Stacks.Immersion.immersionConormalSheafMap (pullback.snd i f) i (pullback.fst i f) f
          (Stacks.Immersion.toShHom_square (isPullback_pullbackSnd i f).w)) :
    haveI : IsLocallyNoetherian Z := LocallyOfFiniteType.isLocallyNoetherian sZ
    haveI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    haveI : IsLocallyNoetherian X' := LocallyOfFiniteType.isLocallyNoetherian (f ≫ sX)
    haveI : IsLocallyNoetherian (pullback i f) :=
      LocallyOfFiniteType.isLocallyNoetherian (pullback.fst i f ≫ sZ)
    completedBivariantRestrictionViaSequence C sZ sX i hi f
        (completedVirtualNormalGysinClassOfOpen C sZ sX i hi U i' hU N) =
      completedBivariantGroup.copy C (Category.id_comp (pullback.snd i f)) _
        (pullbackSnd_comp_structureMorphism_eq C sZ sX i hi f)
        (completedBivariantCompositeOfInvertible C (pullback.fst i f ≫ sZ)
          (pullback.fst i f ≫ sZ) (f ≫ sX) (𝟙 _) (pullback.snd i f) (Category.id_comp _)
          (pullbackSnd_comp_structureMorphism_eq C sZ sX i hi f)
          (topChernClassOfInvertible C (pullback.fst i f ≫ sZ) Eb)
          (completedVirtualNormalGysinClassOfOpen C (pullback.fst i f ≫ sZ) (f ≫ sX)
            (pullback.snd i f) (pullbackSnd_comp_structureMorphism_eq C sZ sX i hi f) V iV hV
            𝒩'))
```

**`Stacks.Chow.completedVirtualNormalGysinClassOfOpen_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/CompletedVirtualNormalImmersionComposition.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/CompletedVirtualNormalImmersionComposition.lean#L250). The attribute's comment: “(3), counterparts: the counterpart of Lemma 0FEC, c(Z → X, 𝒩) = c(Z → Y, 𝒩') ∘ c(Y → X, 𝒩'') in A^*(Z → X)^∧ for immersions Z → Y → X and a conormal-compatible triple of virtual normal bundles of arbitrary rank”.

> **The counterpart of Stacks 0FEC for immersions, at arbitrary rank.** Let `Z ⟶ Y ⟶ X` be
> immersions of schemes locally of finite type over the base, and let `D` be a conormal-compatible
> triple of virtual normal bundles `𝒩`, `𝒩'`, `𝒩''` for `Z ⊆ X`, `Z ⊆ Y` and `Y ⊆ X`, of arbitrary
> (locally constant) ranks. Then
>
>   `c(Z ⟶ X, 𝒩) = c(Z ⟶ Y, 𝒩') ∘ c(Y ⟶ X, 𝒩'')`   in `A^*(Z ⟶ X)^∧`,
>
> for the classes of Stacks 0FBQ (3) built from arbitrary opens `W`, `V`, `U` in which the three
> immersions are closed.

```lean
theorem completedVirtualNormalGysinClassOfOpen_comp
    (W : X.Opens) (iW : Z ⟶ W.toScheme) [IsClosedImmersion iW] (hW : iW ≫ W.ι = i ≫ j)
    (V : Y.Opens) (iV : Z ⟶ V.toScheme) [IsClosedImmersion iV] (hV : iV ≫ V.ι = i)
    (U : X.Opens) (jU : Y ⟶ U.toScheme) [IsClosedImmersion jU] (hU : jU ≫ U.ι = j) :
    haveI : IsLocallyNoetherian Z := LocallyOfFiniteType.isLocallyNoetherian sZ
    haveI : IsLocallyNoetherian Y := LocallyOfFiniteType.isLocallyNoetherian sY
    haveI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    completedVirtualNormalGysinClassOfOpen C sZ sX (i ≫ j) (comp_comp_structureMorphism_eq hi hj)
        W iW hW D.bundleZX =
      completedBivariantCompositeOfInvertible C sZ sY sX i j hi hj
        (completedVirtualNormalGysinClassOfOpen C sZ sY i hi V iV hV D.bundleZY)
        (completedVirtualNormalGysinClassOfOpen C sY sX j hj U jU hU D.bundleYX)
```

**`Stacks.Chow.VirtualNormalBundle`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/VirtualNormalBundle.lean, line 39](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/VirtualNormalBundle.lean#L39). The attribute's comment: “(2): a virtual normal bundle for an immersion”.

> A *virtual normal bundle* for an immersion `i : Z ⟶ X`: a finite locally free `𝒪_Z`-module
> together with a surjection from its dual onto the conormal sheaf `𝒞_{Z/X}` of `i`.

```lean
structure VirtualNormalBundle {Z X : Scheme.{u}} (i : Z ⟶ X) [IsImmersion i]
```

**`Stacks.Chow.completedVirtualNormalGysinClassOfOpen`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/VirtualNormalBundleImmersionClass.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/VirtualNormalBundleImmersionClass.lean#L149). The attribute's comment: “(3), the construction: c(Z → X, 𝒩) = c(Z → U, 𝒩) ∘ (U → X)^* in A^*(Z → X)^∧ for a choice of an open U through which Z → X factors as a closed immersion, 𝒩 of arbitrary rank”.

> **Stacks 0FBQ (3), the construction, for a virtual normal bundle of arbitrary rank.** For an
> immersion `i : Z ⟶ X`, an open subscheme `U ⊆ X` with `i = i' ≫ ι_U` and `i' : Z ⟶ U` a closed
> immersion, and a virtual normal bundle `𝒩` for `i`: the class
>
>   `c(Z ⟶ U, 𝒩) ∘ (U ⟶ X)^* ∈ A^*(Z ⟶ X)^∧`,
>
> the composite on completions (Stacks 0FE0) of flat pullback along `U ⟶ X` (Stacks 0B78) with the
> class of Stacks 0FBK of `𝒩` in `A^*(Z ⟶ U)^∧`, read as a virtual normal bundle for `i'`.

```lean
def completedVirtualNormalGysinClassOfOpen (U : X.Opens) (i' : Z ⟶ U.toScheme)
    [IsClosedImmersion i'] (hU : i' ≫ U.ι = i) (𝒩 : VirtualNormalBundle i) :
    completedBivariantGroup C (gysinSystemOfInvertible C) sZ sX i hi
```

**`Stacks.Chow.completedVirtualNormalGysinClassOfOpen_independent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/VirtualNormalBundleImmersionClass.lean, line 483](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/VirtualNormalBundleImmersionClass.lean#L483). The attribute's comment: “(3), the bivariant class c(Z → X, 𝒩) ∈ A^*(Z → X)^∧ does not depend on the choice of U, for 𝒩 of arbitrary rank”.

> **Stacks 0FBQ (3): the bivariant class `c(Z ⟶ X, 𝒩) ∈ A^*(Z ⟶ X)^∧` does not depend on the
> choice of the open subscheme `U`**, for a virtual normal bundle `𝒩` of arbitrary rank: two opens
> `U₁, U₂ ⊆ X` through which the immersion `i` factors as a closed immersion give the same class
> `c(Z ⟶ U₁, 𝒩) ∘ (U₁ ⟶ X)^* = c(Z ⟶ U₂, 𝒩) ∘ (U₂ ⟶ X)^*`.

```lean
theorem completedVirtualNormalGysinClassOfOpen_independent (U₁ U₂ : X.Opens)
    (i₁ : Z ⟶ U₁.toScheme) [IsClosedImmersion i₁] (h₁ : i₁ ≫ U₁.ι = i) (i₂ : Z ⟶ U₂.toScheme)
    [IsClosedImmersion i₂] (h₂ : i₂ ≫ U₂.ι = i) :
    completedVirtualNormalGysinClassOfOpen C sZ sX i hi U₁ i₁ h₁ 𝒩 =
      completedVirtualNormalGysinClassOfOpen C sZ sX i hi U₂ i₂ h₂ 𝒩
```

**`Stacks.Chow.completedVirtualNormalGysinClassOfOpen_cap_fundamentalChowClass_excess`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/VirtualNormalBundleImmersionCounterparts.lean, line 903](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/VirtualNormalBundleImmersionCounterparts.lean#L903). The attribute's comment: “(3), counterparts: the counterpart of Lemma 0FBM when the virtual normal bundle has unbounded rank, c(Z → X, N) ∩ [Y]\_n = c\_top(E) ∩ [Z ×\_X Y]\_\{n-r} degree by degree in CH\_*, for an immersion Z → X, c(Z → X, N) ∈ A^*(Z → X)^∧, Z ×\_X Y → Y regular with conormal sheaf of constant rank r, E the excess normal sheaf and dim\_δ(Y) ≤ n”.

> **The counterpart of Stacks 0FBM for immersions, at unbounded rank.** Let `i : Z ⟶ X` be an
> immersion with a virtual normal bundle `𝒩` of arbitrary rank, and let `g : Y ⟶ X` be locally of
> finite type such that the base change `i₂ : Z' = Z ×_X Y ⟶ Y` is a regular immersion whose
> conormal sheaf has constant rank `r`; let `ℰ` be the excess normal sheaf. If `dim_δ(Y) ≤ n` then
>
>   `c(Z ⟶ X, 𝒩) ∩ [Y]_n = c_top(ℰ) ∩ [Z']_{n - r}`
>
> degree by degree in `CH_*(Z ×_X Y)`, for `c(Z ⟶ X, 𝒩) = c(Z ⟶ U, 𝒩) ∘ (U ⟶ X)^*` in
> `A^*(Z ⟶ X)^∧`: the degree-`(r + e)` part of the left side is the degree-`e` part of `c_top(ℰ)`
> capped with `[Z']_{n - r}` (`Stacks.Chow.topChernCap`), and the parts of degree `p < r` vanish.
> This is how the source reads the equality when the rank is unbounded on the connected components.
>
> On `V = g⁻¹(U)` the immersion `i₂` factors through the regular closed immersion `Z' ⟶ V`, the
> base change of `Z ⟶ U`, with the same conormal and excess normal sheaves, and `[Y]_n` restricts
> to `[V]_n`; so this is Stacks 0FBM at arbitrary rank
> (`Stacks.Chow.completedVirtualNormalGysinCap_fundamentalChowClass_excess`) for `Z ⟶ U`.

```lean
theorem completedVirtualNormalGysinClassOfOpen_cap_fundamentalChowClass_excess {Y Z' : Scheme.{u}}
    (g : Y ⟶ X) [LocallyOfFiniteType g] (i₂ : Z' ⟶ Y) [IsImmersion i₂] (g' : Z' ⟶ Z)
    (sq : IsPullback i₂ g' g i) (sZ' : Z' ⟶ C.S) [LocallyOfFiniteType sZ']
    (hi₂ : i₂ ≫ (g ≫ sX) = sZ') (hreg : IsRegularImmersion i₂) (r : ℕ)
    [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} (conormalModule i₂) r]
    (n : ℤ) (hY : schemeDeltaDimension C (g ≫ sX) ≤ (n : EInt)) :
    haveI : IsLocallyNoetherian Z := LocallyOfFiniteType.isLocallyNoetherian sZ
    haveI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    haveI : SheafOfModules.IsFiniteLocallyFree.{u, u, u}
        (𝒩.baseChange i i₂ g' g sq).excessNormalSheaf :=
      (𝒩.baseChange i i₂ g' g sq).isFiniteLocallyFree_excessNormalSheaf
        (SheafOfModules.IsFiniteLocallyFreeOfRank.isFiniteLocallyFree _ r)
    (∀ e : ℕ, (completedBivariantSequenceOfInvertible C sZ sX i hi
        (completedVirtualNormalGysinClassOfOpen C sZ sX i hi U i' hU 𝒩) ((r + e : ℕ) : ℤ)).cap g n
          (fundamentalChowClass C (g ≫ sX) n) =
        chowPushforwardOfIso C sZ' (pullback.fst i g ≫ sZ) sq.flip.isoPullback.hom
          (isoPullback_hom_comp_structureMorphism C sZ sX sq hi sZ' hi₂) (n - ((r + e : ℕ) : ℤ))
          (chowGroupDegreeEquiv C sZ' (by push_cast; ring)
            (topChernCap C sZ' (𝒩.baseChange i i₂ g' g sq).excessNormalSheaf (n - (r : ℤ)) e
              (fundamentalChowClass C sZ' (n - (r : ℤ)))))) ∧
      ∀ p : ℤ, p < r → (completedBivariantSequenceOfInvertible C sZ sX i hi
        (completedVirtualNormalGysinClassOfOpen C sZ sX i hi U i' hU 𝒩) p).cap g n
          (fundamentalChowClass C (g ≫ sX) n) = 0
```

**`Stacks.Chow.virtualNormalGysinClassOfOpen_cap_fundamentalChowClass_of_isCohenMacaulayLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/VirtualNormalBundleImmersionCounterparts.lean, line 1020](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/VirtualNormalBundleImmersionCounterparts.lean#L1020). The attribute's comment: “(3), counterparts: the counterpart of Lemma 0FEA, c(Z → X, N) ∩ [Y]\_n = [Z ×\_X Y]\_\{n-r} for an immersion Z → X, N locally free of rank r, Y pure of δ-dimension n, dim\_δ(Z ×\_X Y) ≤ n - r and O\_\{Y,ξ} Cohen-Macaulay at the points of Z ×\_X Y of δ = n - r”.

> **The counterpart of Stacks 0FEA for immersions.** Let `i : Z ⟶ X` be an immersion with a
> virtual normal bundle `𝒩`, let `g : Y ⟶ X` be locally of finite type, and given integers `r` and
> `n` assume
>
> 1. `𝒩` is locally free of rank `r`,
> 2. every irreducible component of `Y` has `δ`-dimension `n`,
> 3. `dim_δ(Z ×_X Y) ≤ n - r`, and
> 4. `𝒪_{Y, ξ}` is Cohen–Macaulay for every `ξ ∈ Z ×_X Y` with `δ(ξ) = n - r`.
>
> Then `c(Z ⟶ X, 𝒩) ∩ [Y]_n = [Z ×_X Y]_{n - r}`, for `c(Z ⟶ X, 𝒩) = c(Z ⟶ U, 𝒩) ∘ (U ⟶ X)^*`.
>
> On `V = g⁻¹(U)` the four hypotheses hold for the closed immersion `Z ⟶ U` and `V ⟶ U`: the
> irreducible components of the open `V` are pure of `δ`-dimension `n`, `Z ×_U V = Z ×_X Y`, and the
> local rings of `V` are those of `Y`. So this is Stacks 0FEA
> (`Stacks.Chow.virtualNormalGysinClass_cap_fundamentalChowClass_of_isCohenMacaulayLocalRing`) for
> `Z ⟶ U`, and `[Y]_n` restricts to `[V]_n`.

```lean
theorem virtualNormalGysinClassOfOpen_cap_fundamentalChowClass_of_isCohenMacaulayLocalRing
    {n : ℤ} {Y : Scheme.{u}} (g : Y ⟶ X) [LocallyOfFiniteType g]
    (hY : ∀ W : irreducibleComponents Y,
      deltaDimension C (g ≫ sX)
        ⟨W, W.2.1, isClosed_of_mem_irreducibleComponents (W : Set Y) W.2⟩ = n)
    (hZY : schemeDeltaDimension C (pullback.snd i g ≫ (g ≫ sX)) ≤ ((n - r : ℤ) : EInt))
    (hCM : ∀ ξ : (pullback i g : Scheme.{u}),
      relativeDimension C.dimensionFunction (g ≫ sX) ((pullback.snd i g).base ξ) = n - r →
      letI : IsLocallyNoetherian Y := LocallyOfFiniteType.isLocallyNoetherian (g ≫ sX)
      IsCohenMacaulayLocalRing (Y.presheaf.stalk ((pullback.snd i g).base ξ))) :
    (virtualNormalGysinClassOfOpen C sZ sX i hi U i' hU 𝒩 r).cap g n
        (fundamentalChowClass C (g ≫ sX) n) =
      fundamentalChowClass C (pullback.fst i g ≫ sZ) (n - r)
```

**`Stacks.Chow.completedVirtualNormalGysinClassOfOpen_eq_of_isTopChernComposition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/VirtualNormalBundleImmersionCounterparts.lean, line 1108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/VirtualNormalBundleImmersionCounterparts.lean#L1108). The attribute's comment: “(3), counterparts: the counterpart of Lemma 0FBL in A^*(Z → X)^∧, c(Z → X, N) = c\_top(E) ∘ c(Z → X, N') for an immersion Z → X and a short exact sequence 0 → N' → N → E → 0 of finite locally free modules of arbitrary rank whose surjection factors through that of N'”.

> **The counterpart of Stacks 0FBL for immersions, at arbitrary rank.** Let `i : Z ⟶ X` be an
> immersion with a virtual normal bundle `𝒩`, and let `0 ⟶ 𝒩' ⟶ 𝒩 ⟶ ℰ ⟶ 0` be a short exact
> sequence of finite locally free `𝒪_Z`-modules, of arbitrary ranks, such that the surjection
> `σ : 𝒩^∨ ⟶ 𝒞_{Z/X}` factors as `σ' ∘ (𝒩^∨ ⟶ (𝒩')^∨)` through that of `𝒩'`. Then
>
>   `c(Z ⟶ X, 𝒩) = c_top(ℰ) ∘ c(Z ⟶ X, 𝒩')`
>
> in `A^*(Z ⟶ X)^∧`, both classes built from the same open `U`. By Stacks 0FBL at arbitrary rank
> (`Stacks.Chow.completedVirtualNormalGysinClass_eq_of_isTopChernComposition`) for `Z ⟶ U` and the
> associativity of the composition on completions (Stacks 0FE0).

```lean
theorem completedVirtualNormalGysinClassOfOpen_eq_of_isTopChernComposition
    (w : inc ≫ pr = 0) (hseq : (ShortComplex.mk inc pr w).ShortExact)
    (hsigma : dualMap inc ≫ 𝒩'.surjection = 𝒩.surjection) :
    haveI : IsLocallyNoetherian Z := LocallyOfFiniteType.isLocallyNoetherian sZ
    haveI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    completedVirtualNormalGysinClassOfOpen C sZ sX i hi U i' hU 𝒩 =
      completedBivariantGroup.copy C (Category.id_comp i) _ hi
        (completedBivariantCompositeOfInvertible C sZ sZ sX (𝟙 Z) i (Category.id_comp sZ) hi
          (topChernClassOfInvertible C sZ Eb)
          (completedVirtualNormalGysinClassOfOpen C sZ sX i hi U i' hU 𝒩'))
```

Declarations registered for the tag:

- [`VirtualNormalBundle.baseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=VirtualNormalBundle.baseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/VirtualNormalBundleImmersionCounterparts.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/VirtualNormalBundleImmersionCounterparts.lean#L90) (StacksFrontier): “(3), counterparts: the counterpart of Lemma 0FBJ, g^*𝒩 is a virtual normal bundle for Z' → X' for a cartesian square whose horizontal arrows are immersions”.
- [`Stacks.Thickenings.immersionConormalSheaf`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Thickenings/UniversalConormalSheaf.lean#L128), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/VirtualNormalBundleOpenFactor.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/VirtualNormalBundleOpenFactor.lean#L44) (StacksFrontier): “(1): the conormal sheaf of an immersion, Stacks 01R2”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.54, Tag 0FBI](https://stacks.math.columbia.edu/tag/0FBI)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
