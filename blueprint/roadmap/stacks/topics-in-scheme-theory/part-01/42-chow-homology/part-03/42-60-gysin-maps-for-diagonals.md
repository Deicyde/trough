---
declaration: section
origin: cited
lean: Stacks.Chow.isRegularImmersion_diagonal_of_smooth, Stacks.Chow.gysinMapExists_diagonal_of_smooth, Stacks.Chow.diagonalGysinClass, Stacks.Chow.isFiniteLocallyFreeOfRank_diagonalVirtualNormalBundle, Stacks.Chow.diagonalGysinClass_compFlatPullbackEqOne_fst, Stacks.Chow.diagonalGysinClass_compFlatPullbackEqOne_snd, Stacks.Chow.bivariantIdentityClass, Stacks.Chow.eq_bivariantIdentityClass_iff
statement: formalized
proof: formalized
---

# 42.60 Gysin maps for diagonals

Section 42.60 of the Stacks Project, [Tag 0FBR](https://stacks.math.columbia.edu/tag/0FBR). 3 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FBR, the section

[Tag 0FBR](https://stacks.math.columbia.edu/tag/0FBR) in the Stacks Project.

**`Stacks.Chow.isRegularImmersion_diagonal_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DiagonalGysin.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/DiagonalGysin.lean#L50). The attribute's comment: “the diagonal of a smooth morphism is a regular immersion”. References: SGA 6 VII (1.10), “special case”; SGA 6 VIII (1.3), “special case”.

> The diagonal `Δ : X ⟶ X ×_Y X` of a smooth morphism is a regular immersion.

```lean
theorem isRegularImmersion_diagonal_of_smooth [Smooth f] :
    Stacks.AlgebraicGeometry.RegularIdealSheaf.IsRegularImmersion (pullback.diagonal f)
```

**`Stacks.Chow.gysinMapExists_diagonal_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DiagonalGysin.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/DiagonalGysin.lean#L57). The attribute's comment: “the Gysin map Δ^! is available for the diagonal”.

> The Gysin map exists for the diagonal of a smooth morphism, in the sense of Stacks 0FF3.

```lean
theorem gysinMapExists_diagonal_of_smooth [Smooth f] :
    GysinMapExists (pullback.diagonal f)
```

**`Stacks.Chow.diagonalGysinClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DiagonalGysinClass.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/DiagonalGysinClass.lean#L158). The attribute's comment: “the Gysin class Δ^! ∈ A^d(X → X ×_Y X) of the diagonal of a smooth morphism of constant relative dimension d”.

> **Stacks 0FBR, the Gysin class `Δ^! ∈ A^d(Y ⟶ Y ×_Z Y)`** of the diagonal of a smooth
> morphism `g : Y ⟶ Z` of constant relative dimension `d`: the class `c(Y ⟶ Y ×_Z Y, 𝒩)` of Stacks
> 0FBQ (3) of the normal bundle `𝒩` of the diagonal (Stacks 0FEZ), at the open subscheme
> `U = (pullback.diagonal g).coborderRange` in which the diagonal is closed. It is
> `c(Y ⟶ U, 𝒩) ∘ ι^*` by `Stacks.Chow.diagonalGysinClass_eq_bivariantCompositeOfInvertible`.

```lean
def diagonalGysinClass :
    BivariantClass C (gysinSystemOfInvertible C)
      (pullback.diagonal g ≫ (pullback.fst g g ≫ sY)) (pullback.fst g g ≫ sY)
      (pullback.diagonal g) rfl d
```

**`Stacks.Chow.isFiniteLocallyFreeOfRank_diagonalVirtualNormalBundle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DiagonalVirtualNormalBundle.lean, line 286](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/DiagonalVirtualNormalBundle.lean#L286). The attribute's comment: “constant relative dimension d: the normal bundle of the diagonal has rank d”.

> **Stacks Project, Section 42.60 (Tag 0FBR), the degree.** For `f` smooth of constant relative
> dimension `d`, the normal bundle of the diagonal is finite locally free of rank `d`; this is why
> the Gysin class `Δ^!` lies in `A^d(Y ⟶ Y ×_Z Y)`.

```lean
theorem isFiniteLocallyFreeOfRank_diagonalVirtualNormalBundle [Smooth f] {d : ℕ}
    (hd : RelativeDimension f d) :
    AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u}
      (diagonalVirtualNormalBundle f).bundle d
```

## Tag 0FBS, a lemma

[Tag 0FBS](https://stacks.math.columbia.edu/tag/0FBS) in the Stacks Project.

**`Stacks.Chow.diagonalGysinClass_compFlatPullbackEqOne_fst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DiagonalGysinClassUnit.lean, line 375](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/DiagonalGysinClassUnit.lean#L375). The attribute's comment: “Δ^! ∘ pr_1^* = 1 in A^0(X), on cap operations, for the first projection”.

> **Stacks 0FBS for the first projection: `Δ^! ∘ pr_1^* = 1` in `A^0(Y)`.** For `g : Y ⟶ Z`
> smooth of relative dimension `d`, capping the flat pullback along `pr_1 : Y ×_Z Y ⟶ Y` with the
> Gysin class `Δ^!` of the diagonal is the identity on the Chow groups of every test scheme over
> `Y`.

```lean
theorem diagonalGysinClass_compFlatPullbackEqOne_fst :
    (diagonalGysinClass C sY g hd).CompFlatPullbackEqOne (pullback.fst g g) rfl
      (pullback.diagonal_fst g) (relativeDimension_pullback_fst_self g hd)
```

**`Stacks.Chow.diagonalGysinClass_compFlatPullbackEqOne_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DiagonalGysinClassUnit.lean, line 388](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/DiagonalGysinClassUnit.lean#L388). The attribute's comment: “Δ^! ∘ pr_2^* = 1 in A^0(X), on cap operations, for the second projection”.

> **Stacks 0FBS for the second projection: `Δ^! ∘ pr_2^* = 1` in `A^0(Y)`.** For `g : Y ⟶ Z`
> smooth of relative dimension `d`, with `Z` over the base compatibly with `Y`, capping the flat
> pullback along `pr_2 : Y ×_Z Y ⟶ Y` with the Gysin class `Δ^!` of the diagonal is the identity on
> the Chow groups of every test scheme over `Y`.

```lean
theorem diagonalGysinClass_compFlatPullbackEqOne_snd (sZ : Z ⟶ C.S) [LocallyOfFiniteType sZ]
    (hg : g ≫ sZ = sY) :
    (diagonalGysinClass C sY g hd).CompFlatPullbackEqOne (pullback.snd g g)
      (smoothShift_pullback_snd_comp_structureMorphism C sY sZ g hg) (pullback.diagonal_snd g)
      (relativeDimension_pullback_snd g g d hd)
```

**`Stacks.Chow.bivariantIdentityClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DiagonalGysinIdentity.lean, line 284](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/DiagonalGysinIdentity.lean#L284). The attribute's comment: “the right-hand side: the unit 1 ∈ A^0(X) of Stacks 0B76, built with the proper and flat axioms discharged and the Gysin axiom of Stacks 0B76 for its cap operation carried as a hypothesis; the Gysin classes Δ^! and pr_i^! of the left-hand side cannot be written down here, their three inputs — Stacks 0FBK, 0B78 and a construction of the composition of Stacks 0B75 — all being absent from this repository”.

> **Stacks 0FBS, the right-hand side.** The *identity bivariant class* `1 ∈ A^0(X)`: the
> bivariant class of degree `0` for `𝟙 X` whose operation on every test scheme `g : T ⟶ X` is the
> identity of `A_k(T)`, carried to the chosen pullback `X ×_X T` along the canonical isomorphism.
>
> The Gysin axiom of Stacks 0B76 is the hypothesis `hgysin`; it is literally the
> `gysin_naturality` field of `Stacks.Chow.BivariantClass` for this cap operation, hence the
> weakest hypothesis that produces the class, and it is a `Prop`, so the class does not depend on
> which proof is supplied. See the implementation notes of
> `StacksFrontier.AlgebraicGeometry.Chow.DiagonalGysinIdentity`.

```lean
def bivariantIdentityClass (G : GysinSystem C)
    (hgysin : IdentityCapRule.TransportGysinNaturality C sX 0 (identityCapRule C sX) G) :
    BivariantClass C G sX sX (𝟙 X) (Category.id_comp sX) 0
```

**`Stacks.Chow.eq_bivariantIdentityClass_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DiagonalGysinIdentity.lean, line 334](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/DiagonalGysinIdentity.lean#L334). The attribute's comment: “the conclusion, reduced to an identification: a degree-0 class for 𝟙 X equals the unit 1 ∈ A^0(X) exactly when it acts as the identity on every test scheme; the composite Δ^! ∘ pr_i^! itself is not constructed, the Gysin classes needing Stacks 0FBK, 0B78 and a construction of the composition of Stacks 0B75”.

> **Stacks 0FBS, the identification with `1`.** A bivariant class of degree `0` for `𝟙 X` is
> the identity class exactly when the operation it induces on every test scheme is the identity.
>
> This is what the conclusion of Stacks 0FBS asserts of `Δ^! ∘ pr_i^!`, and the direction that
> matters for the tag is the one from right to left: a composite acting as the identity on Chow
> groups *is* the class `1`. Uniqueness comes from
> `Stacks.Chow.BivariantClass.eq_of_pushforward_cap_eq`, pushforward along the base-change
> isomorphism being a bijection of Chow groups.

```lean
theorem eq_bivariantIdentityClass_iff (G : GysinSystem C)
    (hgysin : IdentityCapRule.TransportGysinNaturality C sX 0 (identityCapRule C sX) G)
    (c : BivariantClass C G sX sX (𝟙 X) (Category.id_comp sX) 0) :
    c = bivariantIdentityClass C sX G hgysin ↔
      ∀ {T : Scheme.{u}} (g : T ⟶ X) [LocallyOfFiniteType g] (k : ℤ)
        (α : chowGroup C (g ≫ sX) k),
        chowPushforwardOfIso C (pullback.fst (𝟙 X) g ≫ sX) (g ≫ sX)
            (identityBaseChangeIso g).hom (identityBaseChangeIso_hom_comp_base C sX g) (k - 0)
            (c.cap g k α) =
          identityCapRule C sX g k α
```

**`Stacks.Chow.gysinMapExists_fst_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DiagonalGysinIdentity.lean, line 389](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/DiagonalGysinIdentity.lean#L389). The attribute's comment: “a geometric input: the Gysin map of the first projection X ×_Y X ⟶ X is available, the projection being smooth by base change; the class pr_1^! itself is not constructed, needing Stacks 0FBK, 0B78 and a construction of the composition of Stacks 0B75”.

> **Stacks 0FBS, the geometric input for the first projection.** The Gysin map of Stacks 0FF3
> is available for `pr_1 : X ×_Y X ⟶ X`, which is smooth because `f` is and smoothness is stable
> under base change. Together with `CategoryTheory.Limits.pullback.diagonal_fst`, which says
> `Δ ≫ pr_1 = 𝟙 X`, and `Stacks.Chow.gysinMapExists_diagonal_of_smooth`, this is the geometric
> content the source proof of Stacks 0FBS uses.

```lean
theorem gysinMapExists_fst_of_smooth {X Y : Scheme.{u}} (f : X ⟶ Y) [Smooth f] :
    GysinMapExists (pullback.fst f f)
```

**`Stacks.Chow.gysinMapExists_snd_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DiagonalGysinIdentity.lean, line 399](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/DiagonalGysinIdentity.lean#L399). The attribute's comment: “a geometric input: the Gysin map of the second projection X ×_Y X ⟶ X is available, the projection being smooth by base change; the class pr_2^! itself is not constructed, needing Stacks 0FBK, 0B78 and a construction of the composition of Stacks 0B75”.

> **Stacks 0FBS, the geometric input for the second projection.** The Gysin map of Stacks 0FF3
> is available for `pr_2 : X ×_Y X ⟶ X`, which is smooth by base change; and
> `CategoryTheory.Limits.pullback.diagonal_snd` says `Δ ≫ pr_2 = 𝟙 X`.

```lean
theorem gysinMapExists_snd_of_smooth {X Y : Scheme.{u}} (f : X ⟶ Y) [Smooth f] :
    GysinMapExists (pullback.snd f f)
```

**`Stacks.Chow.copy_cap_heq_bivariantCompositeCap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DiagonalGysinIdentity.lean, line 429](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/DiagonalGysinIdentity.lean#L429). The attribute's comment: “the left-hand side, read in A^0(X): the transport along Δ ≫ pr_i = 𝟙 X of a bivariant class witnessing the composition of one for Δ with one for pr_i in total degree 0 caps by the composite operation; the Gysin classes Δ^! and pr_i^! are carried as arbitrary bivariant classes, since Stacks 0FBK, 0B78 and a construction of the composition of Stacks 0B75 are all absent from this repository”.

> **Stacks 0FBS, the left-hand side.** Let `pr : X ×_Y X ⟶ X` be a projection, so that
> `Δ ≫ pr = 𝟙 X`, let `a ∈ A^p(X ⟶ X ×_Y X)` be a bivariant class for the diagonal — the slot
> `Δ^!` occupies — and let `b ∈ A^q(X ×_Y X ⟶ X)` be one for the projection, the slot `pr^!`
> occupies, with `p + q = 0`. If `c` witnesses that it is the composition of `a` and `b`, then the
> class in `A^0(X ⟶ X)` that `c` becomes under `Δ ≫ pr = 𝟙 X` caps by the composite operation
> `a ∩ (b ∩ -)`.
>
> With `Stacks.Chow.eq_bivariantIdentityClass_iff` this says that `Δ^! ∘ pr^! = 1` holds exactly
> when the composite operation acts as the identity on the Chow groups of every test scheme; and
> by `Stacks.Chow.eq_of_isBivariantClassComposition` there is at most one class `c` witnessing the
> composition, so no generality is lost by carrying it as a hypothesis.

```lean
theorem copy_cap_heq_bivariantCompositeCap
    (a : BivariantClass C G sX sP (pullback.diagonal f) hΔ p)
    (b : BivariantClass C G sP sX pr hpr q)
    (c : BivariantClass C G sX sX (pullback.diagonal f ≫ pr)
      (comp_comp_structureMorphism_eq hΔ hpr) (p + q))
    (hc : IsBivariantClassComposition C G sX sP sX (pullback.diagonal f) pr hΔ hpr hpp p q a b c)
    {T : Scheme.{u}} (t : T ⟶ X) [LocallyOfFiniteType t] (k : ℤ)
    (α : chowGroup C (t ≫ sX) k) :
    HEq ((BivariantClass.copy C G sX sX hdiag (comp_comp_structureMorphism_eq hΔ hpr)
          (Category.id_comp sX) hpq c).cap t k α)
      (bivariantCompositeCap C G sX sP sX (pullback.diagonal f) pr hΔ hpr hpp p q a b t k α)
```

## Tag 0FBT, a proposition

[Tag 0FBT](https://stacks.math.columbia.edu/tag/0FBT) in the Stacks Project.

**`Stacks.Chow.smoothRelativeDimensionShiftEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SmoothChowCohomology.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/SmoothChowCohomology.lean#L79). The attribute's comment: “g^! read as the flat pullback g^* of the smooth morphism g; bivariant classes are those of the Gysin system of invertible modules, `Stacks.Chow.gysinSystemOfInvertible`”.

> **Stacks 0FBT.** Let `f : X ⟶ Y` and `g : Y ⟶ Z` be morphisms of schemes locally of finite
> type over `S`, with `g` smooth of relative dimension `d`. Then `c ↦ c ∘ g^*` is an isomorphism
>
>   `A^p(X ⟶ Y) ≃ A^{p-d}(X ⟶ Z)`,
>
> with inverse `c' ↦ res(Δ^!) ∘ res(c')`, where `Δ^!` is the Gysin class of the diagonal of `g`
> (Stacks 0FBR). For a smooth `g` the Gysin map `g^!` of Stacks 0FEZ is the flat pullback `g^*`.

```lean
def smoothRelativeDimensionShiftEquiv :
    BivariantClass C (gysinSystemOfInvertible C) sX sY f hf p ≃+
      BivariantClass C (gysinSystemOfInvertible C) sX sZ (f ≫ g)
        (comp_comp_structureMorphism_eq hf hg) (p - d)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.60, Tag 0FBR](https://stacks.math.columbia.edu/tag/0FBR)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
