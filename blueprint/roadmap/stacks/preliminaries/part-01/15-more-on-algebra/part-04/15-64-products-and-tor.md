---
declaration: section
origin: cited
lean: RingTheory.TorProducts.derivedTorProduct, RingTheory.TorProducts.cohomologyTensorProduct, CochainComplex.DerivedTensor.derivedExtensionScalarsTensorIso, RingTheory.TorProducts.torProduct, GradedTor.existsUnique_algebra, GradedTor.canonical_mul_ofNat, GradedTor.torPieceMap_isAlgebraHom
statement: formalized
proof: formalized
---

# 15.64 Products and Tor

Section 15.64 of the Stacks Project, [Tag 068G](https://stacks.math.columbia.edu/tag/068G). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier) and 6 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 068G, the section

[Tag 068G](https://stacks.math.columbia.edu/tag/068G) in the Stacks Project.

**`RingTheory.TorProducts.derivedTorProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Tor/DerivedObjectProduct.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Tor/DerivedObjectProduct.lean#L107). The attribute's comment: “products on the Tor of derived objects, the last display of the paragraph following Equation 15.64.0.2”.

> The products
> `Torᴿₙ(K, A) ⊗[A] Torᴿₘ(L, A) ⟶ Torᴿₙ₊ₘ(K ⊗ᴸ_R L, A)` on the Tor of derived objects
> `K, L ∈ D(R)`: the cocycle pairing over `A` carried along the base-change identification.

```lean
public noncomputable def derivedTorProduct (f : R →+* A)
    (D : CochainComplex.DerivedExtensionScalars.TotalDerivedExtensionScalars f)
    (K L : DObj R) (n m : ℤ) :
    (derivedTor f D n).obj K ⊗ (derivedTor f D m).obj L ⟶
      (derivedTor f D (n + m)).obj (((canonicalDerivedTensorProductFunctor R).obj K).obj L)
```

Declarations registered for the tag:

- [`RingTheory.TorProducts.cohomologyTensorProduct`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Tor/Products.lean#L289), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Homology/Tor/DerivedObjectProduct.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Tor/DerivedObjectProduct.lean#L131) (StacksFrontier): “Equation 15.64.0.1: the pairing `Hⁱ(K) ⊗ Hʲ(L) ⟶ Hⁱ⁺ʲ(K ⊗ᴸ L)` sending the classes of cocycles `k, l` to the class of `k ⊗ l`.”.
- [`CochainComplex.DerivedTensor.derivedExtensionScalarsTensorIso`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Tor/BaseChangeTensorIso.lean#L827), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Homology/Tor/DerivedObjectProduct.lean, line 135](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Tor/DerivedObjectProduct.lean#L135) (StacksFrontier): “Equation 15.64.0.2: the canonical identification `(K ⊗ᴸ_R A) ⊗ᴸ_A (L ⊗ᴸ_R A) = (K ⊗ᴸ_R L) ⊗ᴸ_R A` in `D(A)`.”.
- [`RingTheory.TorProducts.torProduct`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Tor/CrossProduct/Canonical.lean#L621), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Homology/Tor/DerivedObjectProduct.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Tor/DerivedObjectProduct.lean#L139) (StacksFrontier): “Equation 15.64.0.3: the products `Torᴿₙ(M, A) ⊗[A] Torᴿₘ(N, A) ⟶ Torᴿₙ₊ₘ(M ⊗_R N, A)` for `R`-modules `M` and `N`.”.
- [`GradedTor.existsUnique_algebra`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Tor/GradedAlgebra/Existence.lean#L787), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Homology/Tor/DerivedObjectProduct.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Tor/DerivedObjectProduct.lean#L143) (StacksFrontier): “The `A`-algebra structure on `Torᴿ_⋆(B, A)` for an `R`-algebra `B`, whose multiplication is the product of Equation 15.64.0.3 followed by the map induced by the multiplication `B ⊗_R B → B`.”.
- [`GradedTor.canonical_mul_ofNat`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Tor/GradedAlgebra/Functoriality.lean#L40), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Homology/Tor/DerivedObjectProduct.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Tor/DerivedObjectProduct.lean#L147) (StacksFrontier): “The multiplication of the `A`-algebra `Torᴿ_⋆(B, A)` is the product of Equation 15.64.0.3 followed by the map induced by multiplication on `B`.”.
- [`GradedTor.torPieceMap_isAlgebraHom`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Tor/GradedAlgebra/Functoriality.lean#L240), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Homology/Tor/DerivedObjectProduct.lean, line 151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Tor/DerivedObjectProduct.lean#L151) (StacksFrontier): “Lemma 15.64.1: for an `R`-algebra map `B → C` the induced map `Torᴿ_⋆(B, A) ⟶ Torᴿ_⋆(C, A)` is a homomorphism of `A`-algebras. The source omits the proof.”.

## Tag 068H, an equation

[Tag 068H](https://stacks.math.columbia.edu/tag/068H) in the Stacks Project.

**`RingTheory.TorProducts.cohomologyTensorProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Tor/Products.lean, line 289](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Tor/Products.lean#L289).

> **Stacks 068H.** For any two objects `K` and `L` of `D(R)`, tensoring cocycles gives the
> canonical map
> `Hⁱ(K) ⊗[R] Hʲ(L) ⟶ Hⁱ⁺ʲ(K ⊗ᴸ[R] L)`.
>
> The representative witness in the result specifies the source's formula
> `[p] ⊗ [q] ↦ [p ⊗ q]`.

```lean
public noncomputable def cohomologyTensorProduct
    (K L : DObj R) (i j : ℤ) : CohomologyTensorProduct K L i j
```

## Tag 068I, an equation

[Tag 068I](https://stacks.math.columbia.edu/tag/068I) in the Stacks Project.

**`CochainComplex.DerivedTensor.derivedExtensionScalarsTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Tor/BaseChangeTensorIso.lean, line 827](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Tor/BaseChangeTensorIso.lean#L827).

> The canonical base-change isomorphism
> `(K ⊗ᴸ[R] A) ⊗ᴸ[A] (L ⊗ᴸ[R] A) ≅ (K ⊗ᴸ[R] L) ⊗ᴸ[R] A` in `D(A)`, natural in
> `K, L ∈ D(R)` and represented on K-flat complexes by standard tensor base change.

```lean
public noncomputable def derivedExtensionScalarsTensorIso (f : R →+* A)
    (T_R : DerivedTensorProductGeneral.{uR, max uA v} R)
    (T_A : DerivedTensorProductGeneral.{uA, max uR v} A)
    (D : CochainComplex.DerivedExtensionScalars.TotalDerivedExtensionScalars.{uR, v, uA} f) :
    DerivedExtensionScalarsTensorIso f T_R T_A D
```

## Tag 068J, an equation

[Tag 068J](https://stacks.math.columbia.edu/tag/068J) in the Stacks Project.

**`RingTheory.TorProducts.torProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Tor/CrossProduct/Canonical.lean, line 621](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Tor/CrossProduct/Canonical.lean#L621).

> **Stacks 068J.** The canonical Tor product
> `Torⁿᴿ(M, A) ⊗[A] Torᵐᴿ(N, A) → Torⁿ⁺ᵐᴿ(M ⊗[R] N, A)`, simultaneously for all `R`-modules
> `M` and `N`. Packaging it as a natural transformation records its naturality in both
> variables.

```lean
public noncomputable def torProduct (n m : ℕ) :
    (torBaseChange.{uR, uA, v} R A n).prod (torBaseChange.{uR, uA, v} R A m) ⋙
        tensorBifunctor.{uA, max uR v} A ⟶
      tensorBifunctor.{uR, max uA v} R ⋙ torBaseChange.{uR, uA, v} R A (n + m)
```

## Tag 068K, a lemma

[Tag 068K](https://stacks.math.columbia.edu/tag/068K) in the Stacks Project.

**`GradedTor.torPieceMap_isAlgebraHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Tor/GradedAlgebra/Functoriality.lean, line 240](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Tor/GradedAlgebra/Functoriality.lean#L240). References: SGA 6 VII (2.1), “partial”.

> The maps on Tor induced by an `R`-algebra homomorphism assemble into a
> homomorphism of the canonical graded `A`-algebras on Tor: they preserve the unit and the
> homogeneous multiplication.

```lean
public theorem torPieceMap_isAlgebraHom {B C : AlgCat.{v, uR} R} (g : B ⟶ C) :
    torPieceMap.{uR, uA, v} R A g 0 (canonicalAlgebra.{uR, uA, v} R A B).one =
      (canonicalAlgebra.{uR, uA, v} R A C).one ∧
    ∀ (i j : ℤ) (x : torPiece.{uR, uA, v} R A B i)
        (y : torPiece.{uR, uA, v} R A B j),
      torPieceMap.{uR, uA, v} R A g (i + j)
          ((canonicalAlgebra.{uR, uA, v} R A B).mul i j (x ⊗ₜ[A] y)) =
        (canonicalAlgebra.{uR, uA, v} R A C).mul i j
          (torPieceMap.{uR, uA, v} R A g i x ⊗ₜ[A]
            torPieceMap.{uR, uA, v} R A g j y)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.64, Tag 068G](https://stacks.math.columbia.edu/tag/068G)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
