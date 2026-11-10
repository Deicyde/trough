---
declaration: section
origin: cited
lean: CommAlgCat.exists_tensorProduct_nine_diagram, CommAlgCat.exists_canonical_tensorProduct_nine_diagram, CommAlgCat.cotangentComplex_tensorProduct_of_torIndependent, CommAlgCat.isZero_homology_of_tensorProduct_nine_diagram, CommAlgCat.tensorProduct_rightColumn_homology, CommAlgCat.canonicalTensorProductNineDiagram_upperRight_homology
statement: formalized
proof: formalized
---

# 92.15 Tensor products and the cotangent complex

Section 92.15 of the Stacks Project, [Tag 09D8](https://stacks.math.columbia.edu/tag/09D8). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09D9, an equation

[Tag 09D9](https://stacks.math.columbia.edu/tag/09D9) in the Stacks Project.

**`CommAlgCat.exists_tensorProduct_nine_diagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/TensorProduct.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/TensorProduct.lean#L134).

> **Stacks 09D9**, Equation 92.15.0.1. Let `A` and `B` be algebras over a ring `R`. Given the
> fundamental triangle `L_{A/R} ⊗^L_A (A ⊗_R B) ⟶ L_{A ⊗_R B/R} ⟶ L_{A ⊗_R B/A}` of
> `R → A → A ⊗_R B` and the fundamental triangle
> `L_{B/R} ⊗^L_B (A ⊗_R B) ⟶ L_{A ⊗_R B/R} ⟶ L_{A ⊗_R B/B}` of `R → B → A ⊗_R B`, there is an
> object `E` of `D(A ⊗_R B)` fitting into the upper right corner of the diagram
>
> ```
> L_{A/R} ⊗^L_A (A ⊗_R B) ⟶ L_{A ⊗_R B/B}      ⟶ E
>             ‖                     ↑                ↑
> L_{A/R} ⊗^L_A (A ⊗_R B) ⟶ L_{A ⊗_R B/R}      ⟶ L_{A ⊗_R B/A}
>                                   ↑                ↑
>                       L_{B/R} ⊗^L_B (A ⊗_R B) ═ L_{B/R} ⊗^L_B (A ⊗_R B)
> ```
>
> whose top row and right column are distinguished triangles and whose squares commute.

```lean
theorem exists_tensorProduct_nine_diagram
    {u : cotangentComplexDerivedBaseChange R (CommAlgCat.of R A) (A ⊗[R] B) ⟶
      cotangentComplexDerived R (CommAlgCat.of R (A ⊗[R] B))}
    {p : cotangentComplexDerived R (CommAlgCat.of R (A ⊗[R] B)) ⟶
      cotangentComplexDerived A (CommAlgCat.of A (A ⊗[R] B))}
    {d₁ : cotangentComplexDerived A (CommAlgCat.of A (A ⊗[R] B)) ⟶
      (cotangentComplexDerivedBaseChange R (CommAlgCat.of R A) (A ⊗[R] B))⟦(1 : ℤ)⟧}
    (h₁ : Triangle.mk u p d₁ ∈ distTriang _)
    {v : cotangentComplexDerivedBaseChange R (CommAlgCat.of R B) (A ⊗[R] B) ⟶
      cotangentComplexDerived R (CommAlgCat.of R (A ⊗[R] B))}
    {q : cotangentComplexDerived R (CommAlgCat.of R (A ⊗[R] B)) ⟶
      cotangentComplexDerived B (CommAlgCat.of B (A ⊗[R] B))}
    {d₂ : cotangentComplexDerived B (CommAlgCat.of B (A ⊗[R] B)) ⟶
      (cotangentComplexDerivedBaseChange R (CommAlgCat.of R B) (A ⊗[R] B))⟦(1 : ℤ)⟧}
    (h₂ : Triangle.mk v q d₂ ∈ distTriang _) :
    ∃ (E : DerivedCategory (ModuleCat.{max u v} (A ⊗[R] B)))
      (a : cotangentComplexDerived B (CommAlgCat.of B (A ⊗[R] B)) ⟶ E)
      (b : cotangentComplexDerived A (CommAlgCat.of A (A ⊗[R] B)) ⟶ E)
      (e₁ : E ⟶ (cotangentComplexDerivedBaseChange R (CommAlgCat.of R A) (A ⊗[R] B))⟦(1 : ℤ)⟧)
      (e₂ : E ⟶ (cotangentComplexDerivedBaseChange R (CommAlgCat.of R B) (A ⊗[R] B))⟦(1 : ℤ)⟧),
      Triangle.mk (u ≫ q) a e₁ ∈ distTriang _ ∧
      Triangle.mk (v ≫ p) b e₂ ∈ distTriang _ ∧
      q ≫ a = p ≫ b ∧ b ≫ e₁ = d₁ ∧ a ≫ e₂ = d₂
```

**`CommAlgCat.exists_canonical_tensorProduct_nine_diagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/TensorProductNineDiagramCanonical.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/TensorProductNineDiagramCanonical.lean#L206). The attribute's comment: “the diagram 92.15.0.1 on the canonical maps, with nothing assumed: the middle row and column are the fundamental triangles of Proposition 08QX for R → A → A ⊗\_R B and R → B → A ⊗\_R B, with the functoriality maps of Tag 08PN and their own connecting maps; the top-row and right-column first maps are the 08PN maps of the squares (R → B, A → A ⊗\_R B) and (R → A, B → A ⊗\_R B); the left and lower squares commute; and an object E makes the top row and the right column distinguished, with the upper right square commuting”.

> **Stacks 09D9**, Equation 92.15.0.1, on the canonical maps. Let `A` and `B` be algebras over
> a ring `R`. In `D(A ⊗_R B)` consider
>
> ```
> L_{A/R} ⊗^L_A (A ⊗_R B) ⟶ L_{A ⊗_R B/B}      ⟶ E
>             ‖                     ↑                ↑
> L_{A/R} ⊗^L_A (A ⊗_R B) ⟶ L_{A ⊗_R B/R}      ⟶ L_{A ⊗_R B/A}
>                                   ↑                ↑
>                       L_{B/R} ⊗^L_B (A ⊗_R B) ═ L_{B/R} ⊗^L_B (A ⊗_R B)
> ```
>
> The middle row is the fundamental triangle of `R → A → A ⊗_R B` and the middle column is the
> fundamental triangle of `R → B → A ⊗_R B`. Both are distinguished, with the functoriality maps of
> Tag 08PN (`CommAlgCat.fundamentalMor₁`, `CommAlgCat.fundamentalMor₂`) and the connecting maps
> `CommAlgCat.productFundamentalMor₃`. The first map of the top row is the canonical map
> `CommAlgCat.cotangentTensorProductBaseChangeMap`, and the first map of the right column is
> `CommAlgCat.cotangentTensorProductBaseChangeMapRight`. The left and the lower squares commute.
> There is an object `E` in the upper right corner that makes the top row and the right column
> distinguished triangles, makes the upper right square commute, and has connecting maps that
> recover those of the middle row and the middle column.

```lean
theorem exists_canonical_tensorProduct_nine_diagram :
    Triangle.mk (fundamentalMor₁ R A (A ⊗[R] B)) (fundamentalMor₂ R A (A ⊗[R] B))
        (productFundamentalMor₃ R A (A ⊗[R] B)) ∈ distTriang _ ∧
    Triangle.mk (fundamentalMor₁ R B (A ⊗[R] B)) (fundamentalMor₂ R B (A ⊗[R] B))
        (productFundamentalMor₃ R B (A ⊗[R] B)) ∈ distTriang _ ∧
    fundamentalMor₁ R A (A ⊗[R] B) ≫ fundamentalMor₂ R B (A ⊗[R] B) =
      cotangentTensorProductBaseChangeMap R A B ∧
    fundamentalMor₁ R B (A ⊗[R] B) ≫ fundamentalMor₂ R A (A ⊗[R] B) =
      cotangentTensorProductBaseChangeMapRight R A B ∧
    ∃ (E : DerivedCategory (ModuleCat.{u} (A ⊗[R] B)))
      (a : cotangentComplexDerived B (CommAlgCat.of B (A ⊗[R] B)) ⟶ E)
      (b : cotangentComplexDerived A (CommAlgCat.of A (A ⊗[R] B)) ⟶ E)
      (e₁ : E ⟶ (cotangentComplexDerivedBaseChange R (CommAlgCat.of R A) (A ⊗[R] B))⟦(1 : ℤ)⟧)
      (e₂ : E ⟶ (cotangentComplexDerivedBaseChange R (CommAlgCat.of R B) (A ⊗[R] B))⟦(1 : ℤ)⟧),
      Triangle.mk (cotangentTensorProductBaseChangeMap R A B) a e₁ ∈ distTriang _ ∧
      Triangle.mk (cotangentTensorProductBaseChangeMapRight R A B) b e₂ ∈ distTriang _ ∧
      fundamentalMor₂ R B (A ⊗[R] B) ≫ a = fundamentalMor₂ R A (A ⊗[R] B) ≫ b ∧
      b ≫ e₁ = productFundamentalMor₃ R A (A ⊗[R] B) ∧
      a ≫ e₂ = productFundamentalMor₃ R B (A ⊗[R] B)
```

## Tag 09DA, a lemma

[Tag 09DA](https://stacks.math.columbia.edu/tag/09DA) in the Stacks Project.

**`CommAlgCat.cotangentComplex_tensorProduct_of_torIndependent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/TensorProductTorIndependent.lean, line 544](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/TensorProductTorIndependent.lean#L544).

> If `A` and `B` are Tor independent `R`-algebras, then the object `E` of Equation 92.15.0.1 —
> the cone of the map of complexes
> `L_{A/R} ⊗_R B ⊕ L_{B/R} ⊗_R A ⟶ L_{A ⊗_R B/R}` given by the functoriality maps — is zero;
> the canonical map
> `L_{A/R} ⊗^L_A (A ⊗_R B) ⊕ L_{B/R} ⊗^L_B (A ⊗_R B) ⟶ L_{A ⊗_R B/R}` is an isomorphism in
> `D(A ⊗_R B)`; and this is represented by the complex `L_{A/R} ⊗_R B ⊕ L_{B/R} ⊗_R A` of
> `A ⊗_R B`-modules, the map of complexes being a quasi-isomorphism.

```lean
theorem cotangentComplex_tensorProduct_of_torIndependent
    (hTor : RingTheory.TorIndependence.TorIndependent R A B) :
    IsZero (tensorProductCotangentCone R A B) ∧
      IsIso (biprod.desc (cotangentTensorProductLeftMap R A B)
        (cotangentTensorProductRightMap R A B)) ∧
      QuasiIso (cotangentTensorProductComplexMap R A B)
```

## Tag 09DB, a lemma

[Tag 09DB](https://stacks.math.columbia.edu/tag/09DB) in the Stacks Project.

**`CommAlgCat.isZero_homology_of_tensorProduct_nine_diagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/TensorProductCohomology.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/TensorProductCohomology.lean#L182). The attribute's comment: “the vanishing in degrees i ≥ 1 only, which is the exact ceiling of what the nine diagram of Tag 09D9 determines in this library. The source asserts it for i ≥ -1 and identifies H^\{-2}(E) with Tor\_1^R(A, B); neither is a consequence of the 09D9 conclusion as formalized here, because exists\_tensorProduct\_nine\_diagram leaves the morphisms of the two fundamental triangles arbitrary -- its host file sits upstream of the proof of Tag 08QX and so cannot name the display's own map L\_\{A ⊗ B/R} ⟶ L\_\{A ⊗ B/A} -- and two distinguished triangles on the given objects do not pin those maps down to anything that fixes their homology. At i = 0 the long exact sequence leaves coker H^0(v ≫ p), which the abstract data does not force to vanish”.

> The cohomology of the object `E` of the nine diagram of Tag 09D9 vanishes in degrees `≥ 1`.
>
> Only the middle column `L_{B/R} ⊗^L_B (A ⊗_R B) ⟶ L_{A ⊗_R B/R} ⟶ L_{A ⊗_R B/B}` and the right
> column `L_{B/R} ⊗^L_B (A ⊗_R B) ⟶ L_{A ⊗_R B/A} ⟶ E` of the diagram are used, together with the
> vanishing of the cohomology of a cotangent complex in positive degrees.
>
> This is weaker than Tag 09DB, which asserts the vanishing in all degrees `≥ -1`; see the module
> documentation for why the extra two degrees are not available from the nine diagram alone.

```lean
theorem isZero_homology_of_tensorProduct_nine_diagram
    (h₂ : Triangle.mk v q d₂ ∈ distTriang _)
    (hE₂ : Triangle.mk (v ≫ p) b e₂ ∈ distTriang _) (i : ℤ) (hi : 1 ≤ i) :
    IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{max u v} (A ⊗[R] B)) i).obj E)
```

**`CommAlgCat.tensorProduct_rightColumn_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/TensorProductCohomologyCanonical.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/TensorProductCohomologyCanonical.lean#L145). The attribute's comment: “for every object E in a distinguished triangle on the canonical map L\_\{B/R} ⊗^L\_B (A ⊗\_R B) → L\_\{A ⊗\_R B/A} of the right column of Equation 92.15.0.1, which is how the source's proof describes E: H^i(E) = 0 for i ≥ -1 and H^\{-2}(E) ≅ Tor\_1^R(A, B) as A ⊗\_R B-modules, Tor\_1 with its canonical module structure”.

> **Stacks 09DB**, for every cone `E` of the canonical map
> `L_{B/R} ⊗^L_B (A ⊗_R B) ⟶ L_{A ⊗_R B/A}` of the right column of Equation 92.15.0.1:
> `H^i(E) = 0` for `i ≥ -1` and `H^{-2}(E) ≅ Tor_1^R(A, B)` as `A ⊗_R B`-modules.

```lean
theorem tensorProduct_rightColumn_homology
    (hE : Triangle.mk (cotangentTensorProductBaseChangeMapRight R A B) b e ∈ distTriang _) :
    (∀ i : ℤ, -1 ≤ i →
      IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{u} (A ⊗[R] B)) i).obj E)) ∧
      Nonempty ((DerivedCategory.homologyFunctor (ModuleCat.{u} (A ⊗[R] B)) (-2)).obj E ≅
        torOneTensorProductModule R A B)
```

**`CommAlgCat.canonicalTensorProductNineDiagram_upperRight_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/TensorProductCohomologyCanonical.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/TensorProductCohomologyCanonical.lean#L190). The attribute's comment: “the object E of the nine diagram of Tag 09D9, CommAlgCat.canonicalTensorProductNineDiagram: H^i(E) = 0 for i ≥ -1 and H^\{-2}(E) ≅ Tor\_1^R(A, B) as A ⊗\_R B-modules, Tor\_1 with its canonical module structure (CommAlgCat.torOneTensorProductModule); the isomorphism itself is CommAlgCat.homologyNegTwoCanonicalUpperRightIsoTorOne”.

> **Stacks 09DB.** Let `R` be a ring and let `A`, `B` be `R`-algebras. The object `E` of
> Equation 92.15.0.1 satisfies `H^i(E) = 0` for `i ≥ -1` and `H^{-2}(E) = Tor_1^R(A, B)`, the
> latter as an isomorphism of `A ⊗_R B`-modules.

```lean
theorem canonicalTensorProductNineDiagram_upperRight_homology :
    (∀ i : ℤ, -1 ≤ i →
      IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{u} (A ⊗[R] B)) i).obj
        (canonicalTensorProductNineDiagram R A B).upperRight)) ∧
      Nonempty ((DerivedCategory.homologyFunctor (ModuleCat.{u} (A ⊗[R] B)) (-2)).obj
          (canonicalTensorProductNineDiagram R A B).upperRight ≅
        torOneTensorProductModule R A B)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 92.15, Tag 09D8](https://stacks.math.columbia.edu/tag/09D8)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
