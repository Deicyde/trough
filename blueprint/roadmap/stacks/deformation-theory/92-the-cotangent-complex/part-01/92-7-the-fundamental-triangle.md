---
declaration: section
origin: cited
lean: CommAlgCat.fundamentalMor₁, CommAlgCat.fundamentalMor₂, CommAlgCat.fundamentalVertex₁, CommAlgCat.fundamentalVertex₂, CommAlgCat.fundamentalVertex₃, CommAlgCat.productFundamentalMor₃, CommAlgCat.productFundamentalTriangle_distinguished, CommAlgCat.polynomialTowerSite
statement: formalized
proof: formalized
---

# 92.7 The fundamental triangle

Section 92.7 of the Stacks Project, [Tag 08QR](https://stacks.math.columbia.edu/tag/08QR). 8 tags here are carried by 106 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08QS, an equation

[Tag 08QS](https://stacks.math.columbia.edu/tag/08QS) in the Stacks Project.

**`CommAlgCat.fundamentalMor₁`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/DisplayMorphisms.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/DisplayMorphisms.lean#L143). The attribute's comment: “the first displayed morphism `L_{B/A} ⊗^𝐋_B C ⟶ L_{C/A}`, canonical and with no hypothesis on the two ring maps: the functoriality map of Tag 08PN for the square (1\_A, B → C) after extension of scalars. It is the first morphism of the distinguished triangle of Proposition 08QX, `CommAlgCat.productFundamentalTriangle_distinguished`, whose third morphism is `CommAlgCat.productFundamentalMor₃`”.

> **Stacks Project, Tag 08QS.**
>
> The first displayed morphism `L_{B/A} ⊗^𝐋_B C ⟶ L_{C/A}` of the triangle, for arbitrary ring
> maps `A → B → C`: the functoriality map of Tag 08PN for the square `(𝟙_A, B → C)` after
> extension of scalars along `B → C`, read through the identification of the derived base change
> `L_{B/A} ⊗^𝐋_B C` with the degreewise one `C ⊗_B L_{B/A}`.

```lean
def fundamentalMor₁ :
    fundamentalVertex₁.{u, u, u + 1, u + 1} A B C ⟶ fundamentalVertex₂.{u, u, u + 1} A C
```

**`CommAlgCat.fundamentalMor₂`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/DisplayMorphisms.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/DisplayMorphisms.lean#L167). The attribute's comment: “the second displayed morphism `L_{C/A} ⟶ L_{C/B}`, canonical and with no hypothesis on the two ring maps: the functoriality map of Tag 08PN for the square (A → B, 1\_C). It is the second morphism of the distinguished triangle of Proposition 08QX, `CommAlgCat.productFundamentalTriangle_distinguished`, whose third morphism is `CommAlgCat.productFundamentalMor₃`”.

> **Stacks Project, Tag 08QS.**
>
> The second displayed morphism `L_{C/A} ⟶ L_{C/B}` of the triangle, for arbitrary ring maps
> `A → B → C`: the functoriality map of Tag 08PN for the square `(A → B, 𝟙_C)`, read in `D(C)`.

```lean
def fundamentalMor₂ :
    fundamentalVertex₂.{u, u, u + 1} A C ⟶ fundamentalVertex₃.{u, u, u + 1} B C
```

**`CommAlgCat.fundamentalVertex₁`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/FundamentalDisplay.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/FundamentalDisplay.lean#L77). The attribute's comment: “the first vertex of the displayed triangle, `L_{B/A} ⊗^𝐋_B C`. The display's three morphisms are `CommAlgCat.fundamentalMor₁`, `CommAlgCat.fundamentalMor₂` and `CommAlgCat.productFundamentalMor₃`, and that the six form a distinguished triangle is Proposition 08QX, `CommAlgCat.productFundamentalTriangle_distinguished`”.

> **Stacks Project, Tag 08QS.**
>
> The first vertex `L_{B/A} ⊗^𝐋_B C` of the displayed triangle, as an object of `D(C)`.

```lean
noncomputable abbrev fundamentalVertex₁ : DerivedCategory (ModuleCat.{max u v} C)
```

**`CommAlgCat.fundamentalVertex₂`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/FundamentalDisplay.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/FundamentalDisplay.lean#L86). The attribute's comment: “the second vertex of the displayed triangle, `L_{C/A}`, the target of the first displayed morphism `CommAlgCat.fundamentalMor₁` and the source of the second, `CommAlgCat.fundamentalMor₂`”.

> **Stacks Project, Tag 08QS.**
>
> The second vertex `L_{C/A}` of the displayed triangle, as an object of `D(C)`.

```lean
noncomputable abbrev fundamentalVertex₂ : DerivedCategory (ModuleCat.{max u v} C)
```

**`CommAlgCat.fundamentalVertex₃`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/FundamentalDisplay.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/FundamentalDisplay.lean#L95). The attribute's comment: “the third vertex of the displayed triangle, `L_{C/B}`, the target of the second displayed morphism `CommAlgCat.fundamentalMor₂` and the source of the third, `CommAlgCat.productFundamentalMor₃`, which lands in `(L_{B/A} ⊗^𝐋_B C)[1]`”.

> **Stacks Project, Tag 08QS.**
>
> The third vertex `L_{C/B}` of the displayed triangle, as an object of `D(C)`.

```lean
noncomputable abbrev fundamentalVertex₃ : DerivedCategory (ModuleCat.{max u v} C)
```

**`CommAlgCat.productFundamentalMor₃`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/ProductDescent.lean, line 317](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/ProductDescent.lean#L317). The attribute's comment: “the third displayed morphism `L_{C/B} → (L_{B/A} ⊗^𝐋_B C)[1]`, for arbitrary ring maps `A → B → C`: the connecting morphism of the fundamental triangle of `A → B → B × C` base changed along `B × C → C`, read between the display's own two vertices. The display is a distinguished triangle on these three morphisms by `CommAlgCat.productFundamentalTriangle_distinguished`”.

> **The third displayed morphism of [Stacks, Tag 08QS], for arbitrary ring maps
> `A → B → C`.** It is the connecting morphism of the fundamental triangle of
> `A → B → B × C`, base changed along the flat ring map `B × C → C` and read between the display's
> own vertices `L_{C/B}` and `(L_{B/A} ⊗^𝐋_B C)⟦1⟧`.

```lean
def productFundamentalMor₃ :
    fundamentalVertex₃.{u, u, u + 1} B C ⟶
      (fundamentalVertex₁.{u, u, u + 1, u + 1} A B C)⟦(1 : ℤ)⟧
```

**`CommAlgCat.productFundamentalTriangle_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/ProductDescent.lean, line 357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/ProductDescent.lean#L357). The attribute's comment: “the distinguishedness asserted by the display: Equation 92.7.0.1 is written as a triangle, and that the display's three objects and three arrows form a DISTINGUISHED triangle in `D(C)` is the remaining clause of the display, for arbitrary ring maps `A → B → C` with no hypothesis on them. The display's three vertices are `CommAlgCat.fundamentalVertex₁`, `CommAlgCat.fundamentalVertex₂` and `CommAlgCat.fundamentalVertex₃` and its three morphisms are `CommAlgCat.fundamentalMor₁`, `CommAlgCat.fundamentalMor₂` and `CommAlgCat.productFundamentalMor₃`, each of which carries the tag for its own constituent. That the triangle is distinguished is Proposition 08QX, which this declaration also carries”.

> **Stacks Project, Tag 08QX, and the distinguishedness asserted by the display of Tag 08QS.**
> Let `A → B → C` be ring maps. Then
>
> `L_{B/A} ⊗^𝐋_B C ⟶ L_{C/A} ⟶ L_{C/B} ⟶ (L_{B/A} ⊗^𝐋_B C)[1]`
>
> is a distinguished triangle in `D(C)`, on the three vertices of the display of
> [Stacks, Tag 08QS], with the display's own first two morphisms
> `CommAlgCat.fundamentalMor₁` and `CommAlgCat.fundamentalMor₂` — the two functoriality maps of
> [Stacks, Tag 08PN] for the two commutative squares of the tower — and with
> `CommAlgCat.productFundamentalMor₃` for its third.
>
> The display of Tag 08QS is written as a triangle, and what makes it one is exactly this
> statement, so the display's distinguishedness clause is registered here as well: the three
> objects and the three arrows of the display are named by
> `CommAlgCat.fundamentalVertex₁`, `CommAlgCat.fundamentalVertex₂`,
> `CommAlgCat.fundamentalVertex₃`, `CommAlgCat.fundamentalMor₁`, `CommAlgCat.fundamentalMor₂` and
> `CommAlgCat.productFundamentalMor₃`, and that they form a triangle at all is Proposition 08QX.
>
> The proof is the one of [Stacks, Remark 08SD]: the triangle for `A → B → B × C`, where the map
> is the split injection `b ↦ (b, f b)`, base changed along the flat projection `B × C → C`.

```lean
theorem productFundamentalTriangle_distinguished :
    Triangle.mk (fundamentalMor₁.{u} A B C) (fundamentalMor₂.{u} A B C)
        (productFundamentalMor₃ A B C) ∈ distTriang (DerivedCategory (ModuleCat.{u} C))
```

## Tag 08QT, an equation

[Tag 08QT](https://stacks.math.columbia.edu/tag/08QT) in the Stacks Project.

**`CommAlgCat.polynomialTowerSite`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean#L247). The attribute's comment: “the site C\_\{C/B/A}”.

> The site `C_{C/B/A}`: the opposite of the category of polynomial towers `(P → B, Q → C)`,
> so that an object corresponds to the commutative diagram of spectra in which
> `Spec C → Spec Q` lies over `Spec B → Spec P` over `Spec A`.

```lean
abbrev polynomialTowerSite
```

**`CommAlgCat.polynomialTowerTopology_eq_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean#L262). The attribute's comment: “the chaotic topology on C\_\{C/B/A}”.

> The topology of `C_{C/B/A}` is the chaotic topology: its only coverings are the maximal
> sieves, so every presheaf on `C_{C/B/A}` is a sheaf.

```lean
theorem polynomialTowerTopology_eq_bot : polynomialTowerTopology A B C = ⊥
```

**`CommAlgCat.polynomialTowerFirst`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean#L275). The attribute's comment: “the functor u₁”.

> `u₁ : C_{C/B/A} ⥤ C_{B/A}`, the functor `(P → B, Q → C) ↦ (P → B)`.

```lean
def polynomialTowerFirst : polynomialTowerSite A B C ⥤ polynomialSite A (towerBaseAlgebra A B)
```

**`CommAlgCat.isPolynomialAlgebra_towerRightAlgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean, line 284](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean#L284). The attribute's comment: “u₂ lands in C\_\{C/A}”.

> The `A`-algebra `Q` of a polynomial tower is a polynomial algebra over `A`: it is a
> polynomial algebra over the polynomial `A`-algebra `P`, and
> `P[κ] = A[ι][κ] = A[κ ⊕ ι]`. This is what makes `u₂` land in `C_{C/A}`.

```lean
theorem isPolynomialAlgebra_towerRightAlgebra (X : PolynomialTower A B C) :
    IsPolynomialAlgebra A (towerRightAlgebra X.obj)
```

**`CommAlgCat.polynomialTowerSecond`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean, line 310](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean#L310). The attribute's comment: “the functor u₂”.

> `u₂ : C_{C/B/A} ⥤ C_{C/A}`, the functor `(P → B, Q → C) ↦ (Q → C)`.

```lean
def polynomialTowerSecond :
    polynomialTowerSite A B C ⥤ polynomialSite A (towerTotalAlgebra A C)
```

**`CommAlgCat.isPolynomialAlgebra_towerBaseChangeAlgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean, line 442](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean#L442). The attribute's comment: “u₃ lands in C\_\{C/B}”.

> `Q ⊗_P B` is a polynomial algebra over `B`: if `Q = P[κ]` then `Q ⊗_P B = B[κ]`. This is
> what makes `u₃` land in `C_{C/B}`.

```lean
theorem isPolynomialAlgebra_towerBaseChangeAlgebra (X : PolynomialTower A B C) :
    IsPolynomialAlgebra B (towerBaseChangeAlgebra X.obj)
```

**`CommAlgCat.polynomialTowerThird`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean, line 496](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean#L496). The attribute's comment: “the functor u₃”.

> `u₃ : C_{C/B/A} ⥤ C_{C/B}`, the functor `(P → B, Q → C) ↦ (Q ⊗_P B → C)`.

```lean
def polynomialTowerThird :
    polynomialTowerSite A B C ⥤ polynomialSite B (towerRelativeAlgebra B C)
```

**`CommAlgCat.polynomialTowerFirstStructureSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean, line 639](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean#L639). The attribute's comment: “the sheaf 𝒪₁ = g₁⁻¹𝒪”.

> `𝒪₁ = g₁⁻¹𝒪`: the inverse image along `g₁` of the tautological sheaf of rings on
> `C_{B/A}`.

```lean
def polynomialTowerFirstStructureSheaf :
    Sheaf (polynomialTowerTopology A B C) CommRingCat.{u + 1}
```

**`CommAlgCat.polynomialTowerSecondStructureSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean, line 647](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean#L647). The attribute's comment: “the sheaf 𝒪₂ = g₂⁻¹𝒪”.

> `𝒪₂ = g₂⁻¹𝒪`: the inverse image along `g₂` of the tautological sheaf of rings on
> `C_{C/A}`.

```lean
def polynomialTowerSecondStructureSheaf :
    Sheaf (polynomialTowerTopology A B C) CommRingCat.{u + 1}
```

**`CommAlgCat.polynomialTowerThirdStructureSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean, line 655](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean#L655). The attribute's comment: “the sheaf 𝒪₃ = g₃⁻¹𝒪”.

> `𝒪₃ = g₃⁻¹𝒪`: the inverse image along `g₃` of the tautological sheaf of rings on
> `C_{C/B}`.

```lean
def polynomialTowerThirdStructureSheaf :
    Sheaf (polynomialTowerTopology A B C) CommRingCat.{u + 1}
```

**`CommAlgCat.polynomialTowerFirstRinged`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean, line 682](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean#L682). The attribute's comment: “the morphism g₁ of ringed topoi”.

> `g₁ : (Sh(C_{C/B/A}), 𝒪₁) ⟶ (Sh(C_{B/A}), 𝒪)`, the first morphism of ringed topoi of the
> fundamental triangle. Its structure map is the unit of `g₁⁻¹ ⊣ g₁_*` on sheaves of commutative
> rings at `𝒪`, which is the structure map that `𝒪₁ = g₁⁻¹𝒪` forces.

```lean
def polynomialTowerFirstRinged :
    AlgebraicGeometry.RingedToposHom (polynomialTowerFirstRingedTopos A B C)
      (polynomialStructureRingedTopos A (towerBaseAlgebra A B))
```

**`CommAlgCat.polynomialTowerSecondRinged`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean, line 692](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean#L692). The attribute's comment: “the morphism g₂ of ringed topoi”.

> `g₂ : (Sh(C_{C/B/A}), 𝒪₂) ⟶ (Sh(C_{C/A}), 𝒪)`, the second morphism of ringed topoi of the
> fundamental triangle.

```lean
def polynomialTowerSecondRinged :
    AlgebraicGeometry.RingedToposHom (polynomialTowerSecondRingedTopos A B C)
      (polynomialStructureRingedTopos A (towerTotalAlgebra A C))
```

**`CommAlgCat.polynomialTowerThirdRinged`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean, line 702](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean#L702). The attribute's comment: “the morphism g₃ of ringed topoi”.

> `g₃ : (Sh(C_{C/B/A}), 𝒪₃) ⟶ (Sh(C_{C/B}), 𝒪)`, the third morphism of ringed topoi of the
> fundamental triangle.

```lean
def polynomialTowerThirdRinged :
    AlgebraicGeometry.RingedToposHom (polynomialTowerThirdRingedTopos A B C)
      (polynomialStructureRingedTopos B (towerRelativeAlgebra B C))
```

**`CommAlgCat.polynomialTowerProjection`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean, line 744](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean#L744). The attribute's comment: “the projection π”.

> `π : Sh(C_{C/B/A}) ⟶ Sh(*)`, the projection of the chaotic site `C_{C/B/A}` to the
> point.

```lean
abbrev polynomialTowerProjection
```

**`CommAlgCat.polynomialTowerFirstProjection_comp_inverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean, line 762](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean#L762). The attribute's comment: “π = π₁ ∘ g₁, on inverse images”.

> `π = π₁ ∘ g₁`, on inverse images: both are restriction along the unique functor to the
> point, because `u₁` followed by `C_{B/A} ⥤ *` is `C_{C/B/A} ⥤ *`.

```lean
theorem polynomialTowerFirstProjection_comp_inverseImage :
    ((polynomialTowerFirstProjection A B).comp
        (polynomialTowerFirstTopos A B C)).inverseImage =
      (polynomialTowerProjection A B C).inverseImage
```

**`CommAlgCat.polynomialTowerSecondProjection_comp_inverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean, line 769](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean#L769). The attribute's comment: “π = π₂ ∘ g₂, on inverse images”.

> `π = π₂ ∘ g₂`, on inverse images.

```lean
theorem polynomialTowerSecondProjection_comp_inverseImage :
    ((polynomialTowerSecondProjection A C).comp
        (polynomialTowerSecondTopos A B C)).inverseImage =
      (polynomialTowerProjection A B C).inverseImage
```

**`CommAlgCat.polynomialTowerThirdProjection_comp_inverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean, line 776](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean#L776). The attribute's comment: “π = π₃ ∘ g₃, on inverse images”.

> `π = π₃ ∘ g₃`, on inverse images.

```lean
theorem polynomialTowerThirdProjection_comp_inverseImage :
    ((polynomialTowerThirdProjection B C).comp
        (polynomialTowerThirdTopos A B C)).inverseImage =
      (polynomialTowerProjection A B C).inverseImage
```

**`CommAlgCat.polynomialTowerFirstProjection_comp_pushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean, line 784](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean#L784). The attribute's comment: “π = π₁ ∘ g₁, on direct images”.

> `π = π₁ ∘ g₁`, on direct images: the canonical isomorphism `(π₁ ∘ g₁)_* ≅ π_*` between the
> two right adjoints of the common inverse image.

```lean
def polynomialTowerFirstProjection_comp_pushforwardIso :
    ((polynomialTowerFirstProjection A B).comp (polynomialTowerFirstTopos A B C)).pushforward ≅
      (polynomialTowerProjection A B C).pushforward
```

**`CommAlgCat.polynomialTowerSecondProjection_comp_pushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean, line 794](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean#L794). The attribute's comment: “π = π₂ ∘ g₂, on direct images”.

> `π = π₂ ∘ g₂`, on direct images.

```lean
def polynomialTowerSecondProjection_comp_pushforwardIso :
    ((polynomialTowerSecondProjection A C).comp (polynomialTowerSecondTopos A B C)).pushforward ≅
      (polynomialTowerProjection A B C).pushforward
```

**`CommAlgCat.polynomialTowerThirdProjection_comp_pushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean, line 804](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSite.lean#L804). The attribute's comment: “π = π₃ ∘ g₃, on direct images”.

> `π = π₃ ∘ g₃`, on direct images.

```lean
def polynomialTowerThirdProjection_comp_pushforwardIso :
    ((polynomialTowerThirdProjection B C).comp (polynomialTowerThirdTopos A B C)).pushforward ≅
      (polynomialTowerProjection A B C).pushforward
```

**`CommAlgCat.boundedPolynomialTowerSite`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean#L169). The attribute's comment: “the site C\_\{C/B/A} with the section's footnote in force, restricting the two layers of variables to cardinality at most κ, resp. μ. The unrestricted version is `CommAlgCat.polynomialTowerSite`; only this one is essentially small”.

> **Stacks 08QT** with the footnote's restriction. The site `C_{C/B/A}` cut down to the towers
> whose two polynomial layers have at most `κ`, resp. `μ`, variables: the opposite of
> `CommAlgCat.BoundedPolynomialTower`. `CommAlgCat.polynomialTowerSite` is the same construction
> with the footnote omitted.

```lean
abbrev boundedPolynomialTowerSite
```

**`CommAlgCat.isPolynomialAlgebraBelow_towerRightAlgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean, line 374](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean#L374). The attribute's comment: “u₂ lands in C\_\{C/A}, for the small model of the footnote-restricted tower site: the bound on the two layers gives the bound μ + κ on the variables of Q over A”.

> The `A`-algebra `Q` of a restricted polynomial tower is a polynomial algebra over `A` on at
> most `μ + κ` variables: it is `A[ι][τ] = A[τ ⊕ ι]` with `#ι ≤ κ` and `#τ ≤ μ`. This is what
> makes `u₂` land in the restricted site `C_{C/A}`.

```lean
theorem isPolynomialAlgebraBelow_towerRightAlgebra (Y : BoundedPolynomialTower A B C κ μ) :
    IsPolynomialAlgebraBelow A (μ + κ) (towerRightAlgebra Y.obj)
```

**`CommAlgCat.isPolynomialAlgebraBelow_towerBaseChangeAlgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean, line 395](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean#L395). The attribute's comment: “u₃ lands in C\_\{C/B}, for the small model of the footnote-restricted tower site: the base change Q ⊗\_P B has the same set of variables as Q over P, so the bound μ is kept”.

> `Q ⊗_P B` is a polynomial algebra over `B` on at most `μ` variables: if `Q = P[τ]` then
> `Q ⊗_P B = B[τ]`, with the same set of variables. This is what makes `u₃` land in the restricted
> site `C_{C/B}`.

```lean
theorem isPolynomialAlgebraBelow_towerBaseChangeAlgebra (Y : BoundedPolynomialTower A B C κ μ) :
    IsPolynomialAlgebraBelow B μ (towerBaseChangeAlgebra Y.obj)
```

**`CommAlgCat.boundedPolynomialTowerFirst`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean, line 440](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean#L440). The attribute's comment: “the functor u₁, for the footnote-restricted tower site”.

> `u₁` on the restricted sites.

```lean
def boundedPolynomialTowerFirst :
    boundedPolynomialTowerSite A B C κ μ ⥤ boundedPolynomialSite A (towerBaseAlgebra A B) κ
```

**`CommAlgCat.boundedPolynomialTowerSecond`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean, line 446](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean#L446). The attribute's comment: “the functor u₂, for the footnote-restricted tower site”.

> `u₂` on the restricted sites.

```lean
def boundedPolynomialTowerSecond :
    boundedPolynomialTowerSite A B C κ μ ⥤
      boundedPolynomialSite A (towerTotalAlgebra A C) (μ + κ)
```

**`CommAlgCat.boundedPolynomialTowerThird`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean, line 453](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean#L453). The attribute's comment: “the functor u₃, for the footnote-restricted tower site”.

> `u₃` on the restricted sites.

```lean
def boundedPolynomialTowerThird :
    boundedPolynomialTowerSite A B C κ μ ⥤ boundedPolynomialSite B (towerRelativeAlgebra B C) μ
```

**`CommAlgCat.boundedPolynomialTowerFirst_comp_ι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean, line 478](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean#L478). The attribute's comment: “the functor u₁ of the footnote-restricted tower site is u₁”.

> Read in the unrestricted sites, `u₁` on the restricted sites is `u₁`.

```lean
theorem boundedPolynomialTowerFirst_comp_ι :
    boundedPolynomialTowerFirst A B C κ μ ⋙ boundedPolynomialSiteι A (towerBaseAlgebra A B) κ =
      boundedPolynomialTowerSiteι A B C κ μ ⋙ polynomialTowerFirst A B C
```

**`CommAlgCat.boundedPolynomialTowerSecond_comp_ι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean, line 484](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean#L484). The attribute's comment: “the functor u₂ of the footnote-restricted tower site is u₂”.

> Read in the unrestricted sites, `u₂` on the restricted sites is `u₂`.

```lean
theorem boundedPolynomialTowerSecond_comp_ι :
    boundedPolynomialTowerSecond A B C κ μ ⋙
        boundedPolynomialSiteι A (towerTotalAlgebra A C) (μ + κ) =
      boundedPolynomialTowerSiteι A B C κ μ ⋙ polynomialTowerSecond A B C
```

**`CommAlgCat.boundedPolynomialTowerThird_comp_ι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean, line 491](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean#L491). The attribute's comment: “the functor u₃ of the footnote-restricted tower site is u₃”.

> Read in the unrestricted sites, `u₃` on the restricted sites is `u₃`.

```lean
theorem boundedPolynomialTowerThird_comp_ι :
    boundedPolynomialTowerThird A B C κ μ ⋙ boundedPolynomialSiteι B (towerRelativeAlgebra B C) μ =
      boundedPolynomialTowerSiteι A B C κ μ ⋙ polynomialTowerThird A B C
```

**`CommAlgCat.smallBoundedPolynomialTowerFirst`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean, line 510](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean#L510). The attribute's comment: “the functor u₁, for the small model of the footnote-restricted tower site”.

> `u₁ : C_{C/B/A} ⥤ C_{B/A}` on the small models of the restricted sites.

```lean
def smallBoundedPolynomialTowerFirst :
    smallBoundedPolynomialTowerSite A B C κ μ ⥤
      smallBoundedPolynomialSite A (towerBaseAlgebra A B) κ
```

**`CommAlgCat.smallBoundedPolynomialTowerSecond`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean, line 518](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean#L518). The attribute's comment: “the functor u₂, for the small model of the footnote-restricted tower site”.

> `u₂ : C_{C/B/A} ⥤ C_{C/A}` on the small models of the restricted sites: `u₂` on the
> restricted sites, followed by the transport of its value into the small model of `C_{C/A}`.

```lean
def smallBoundedPolynomialTowerSecond :
    smallBoundedPolynomialTowerSite A B C κ μ ⥤
      smallBoundedPolynomialSite A (towerTotalAlgebra A C) (μ + κ)
```

**`CommAlgCat.smallBoundedPolynomialTowerThird`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean, line 527](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean#L527). The attribute's comment: “the functor u₃, for the small model of the footnote-restricted tower site”.

> `u₃ : C_{C/B/A} ⥤ C_{C/B}` on the small models of the restricted sites: `u₃` on the
> restricted sites, followed by the transport of its value into the small model of `C_{C/B}`.

```lean
def smallBoundedPolynomialTowerThird :
    smallBoundedPolynomialTowerSite A B C κ μ ⥤
      smallBoundedPolynomialSite B (towerRelativeAlgebra B C) μ
```

**`CommAlgCat.smallBoundedPolynomialTowerFirst_comp_ι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean, line 536](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean#L536). The attribute's comment: “the functor u₁ of the small model of the footnote-restricted tower site is u₁”.

> **The square for `u₁`.** Read in the unrestricted sites through the fully faithful
> comparisons, `u₁` on the small models is `u₁` on `C_{C/B/A}`.

```lean
theorem smallBoundedPolynomialTowerFirst_comp_ι :
    smallBoundedPolynomialTowerFirst A B C κ μ ⋙
        smallBoundedPolynomialSiteToPolynomialSite A (towerBaseAlgebra A B) κ =
      smallBoundedPolynomialTowerSiteToPolynomialTowerSite A B C κ μ ⋙
        polynomialTowerFirst A B C
```

**`CommAlgCat.smallBoundedPolynomialTowerSecondCompι`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean, line 546](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean#L546). The attribute's comment: “the functor u₂ of the small model of the footnote-restricted tower site is u₂”.

> **The square for `u₂`.** Read in the unrestricted sites through the fully faithful
> comparisons, `u₂` on the small models is `u₂` on `C_{C/B/A}`, up to the canonical isomorphism
> coming from the transport into the small model of `C_{C/A}`.

```lean
def smallBoundedPolynomialTowerSecondCompι :
    smallBoundedPolynomialTowerSecond A B C κ μ ⋙
        smallBoundedPolynomialSiteToPolynomialSite A (towerTotalAlgebra A C) (μ + κ) ≅
      smallBoundedPolynomialTowerSiteToPolynomialTowerSite A B C κ μ ⋙
        polynomialTowerSecond A B C
```

**`CommAlgCat.smallBoundedPolynomialTowerThirdCompι`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean, line 561](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean#L561). The attribute's comment: “the functor u₃ of the small model of the footnote-restricted tower site is u₃”.

> **The square for `u₃`.** Read in the unrestricted sites through the fully faithful
> comparisons, `u₃` on the small models is `u₃` on `C_{C/B/A}`, up to the canonical isomorphism
> coming from the transport into the small model of `C_{C/B}`.

```lean
def smallBoundedPolynomialTowerThirdCompι :
    smallBoundedPolynomialTowerThird A B C κ μ ⋙
        smallBoundedPolynomialSiteToPolynomialSite B (towerRelativeAlgebra B C) μ ≅
      smallBoundedPolynomialTowerSiteToPolynomialTowerSite A B C κ μ ⋙
        polynomialTowerThird A B C
```

**`CommAlgCat.smallBoundedPolynomialTowerTopology_eq_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean, line 577](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean#L577). The attribute's comment: “the chaotic topology on C\_\{C/B/A}, for the small model of the footnote-restricted tower site”.

> The topology of the small model of the restricted site `C_{C/B/A}` is the chaotic topology:
> its only coverings are the maximal sieves, so every presheaf on it is a sheaf.

```lean
theorem smallBoundedPolynomialTowerTopology_eq_bot :
    GrothendieckTopology.trivial (smallBoundedPolynomialTowerSite A B C κ μ) = ⊥
```

**`CommAlgCat.smallBoundedPolynomialTowerProjection`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean, line 683](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean#L683). The attribute's comment: “the projection π, for the small model of the footnote-restricted tower site”.

> `π : Sh(C_{C/B/A}) ⟶ Sh(*)`, the projection of the small model of the restricted site to
> the point, with coefficients in the site's own universe.

```lean
abbrev smallBoundedPolynomialTowerProjection :
    MorphismOfTopoi
      (Sheaf (GrothendieckTopology.trivial (smallBoundedPolynomialTowerSite A B C κ μ)) (Type u))
      (Sheaf (GrothendieckTopology.trivial (Discrete PUnit.{u + 1})) (Type u))
```

**`CommAlgCat.smallBoundedPolynomialTowerFirstProjection_comp_inverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean, line 719](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean#L719). The attribute's comment: “π = π₁ ∘ g₁ on inverse images, for the small model of the footnote-restricted tower site”.

> `π = π₁ ∘ g₁` on inverse images: both are restriction along the unique functor to the
> point, because `u₁` followed by `C_{B/A} ⥤ *` is `C_{C/B/A} ⥤ *`.

```lean
theorem smallBoundedPolynomialTowerFirstProjection_comp_inverseImage :
    ((smallBoundedPolynomialTowerFirstProjection A B κ).comp
        (smallBoundedPolynomialTowerFirstTopos A B C κ μ)).inverseImage =
      (smallBoundedPolynomialTowerProjection A B C κ μ).inverseImage
```

**`CommAlgCat.smallBoundedPolynomialTowerSecondProjection_comp_inverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean, line 727](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean#L727). The attribute's comment: “π = π₂ ∘ g₂ on inverse images, for the small model of the footnote-restricted tower site”.

> `π = π₂ ∘ g₂` on inverse images.

```lean
theorem smallBoundedPolynomialTowerSecondProjection_comp_inverseImage :
    ((smallBoundedPolynomialTowerSecondProjection A C κ μ).comp
        (smallBoundedPolynomialTowerSecondTopos A B C κ μ)).inverseImage =
      (smallBoundedPolynomialTowerProjection A B C κ μ).inverseImage
```

**`CommAlgCat.smallBoundedPolynomialTowerThirdProjection_comp_inverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean, line 735](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean#L735). The attribute's comment: “π = π₃ ∘ g₃ on inverse images, for the small model of the footnote-restricted tower site”.

> `π = π₃ ∘ g₃` on inverse images.

```lean
theorem smallBoundedPolynomialTowerThirdProjection_comp_inverseImage :
    ((smallBoundedPolynomialTowerThirdProjection B C μ).comp
        (smallBoundedPolynomialTowerThirdTopos A B C κ μ)).inverseImage =
      (smallBoundedPolynomialTowerProjection A B C κ μ).inverseImage
```

**`CommAlgCat.smallBoundedPolynomialTowerFirstProjection_comp_pushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean, line 744](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean#L744). The attribute's comment: “π = π₁ ∘ g₁ on direct images, for the small model of the footnote-restricted tower site”.

> `π = π₁ ∘ g₁` on direct images: the canonical isomorphism `(π₁ ∘ g₁)_* ≅ π_*` between the
> two right adjoints of the common inverse image.

```lean
def smallBoundedPolynomialTowerFirstProjection_comp_pushforwardIso :
    ((smallBoundedPolynomialTowerFirstProjection A B κ).comp
        (smallBoundedPolynomialTowerFirstTopos A B C κ μ)).pushforward ≅
      (smallBoundedPolynomialTowerProjection A B C κ μ).pushforward
```

**`CommAlgCat.smallBoundedPolynomialTowerSecondProjection_comp_pushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean, line 757](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean#L757). The attribute's comment: “π = π₂ ∘ g₂ on direct images, for the small model of the footnote-restricted tower site”.

> `π = π₂ ∘ g₂` on direct images.

```lean
def smallBoundedPolynomialTowerSecondProjection_comp_pushforwardIso :
    ((smallBoundedPolynomialTowerSecondProjection A C κ μ).comp
        (smallBoundedPolynomialTowerSecondTopos A B C κ μ)).pushforward ≅
      (smallBoundedPolynomialTowerProjection A B C κ μ).pushforward
```

**`CommAlgCat.smallBoundedPolynomialTowerThirdProjection_comp_pushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean, line 770](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialSiteSmall.lean#L770). The attribute's comment: “π = π₃ ∘ g₃ on direct images, for the small model of the footnote-restricted tower site”.

> `π = π₃ ∘ g₃` on direct images.

```lean
def smallBoundedPolynomialTowerThirdProjection_comp_pushforwardIso :
    ((smallBoundedPolynomialTowerThirdProjection B C μ).comp
        (smallBoundedPolynomialTowerThirdTopos A B C κ μ)).pushforward ≅
      (smallBoundedPolynomialTowerProjection A B C κ μ).pushforward
```

## Tag 08QU, a lemma

[Tag 08QU](https://stacks.math.columbia.edu/tag/08QU) in the Stacks Project.

**`CommAlgCat.towerDifferential_shortExact_extendScalars`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldDifferentialSequence.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldDifferentialSequence.lean#L230). The attribute's comment: “the objectwise split differential sequence after base change: the exactness input of the lemma, at an object of the site”.

> For a tower `R → P → Q` with `Q` formally smooth over `P`, the differential sequence
> `0 → Q ⊗_P Ω_{P/R} → Ω_{Q/R} → Ω_{Q/P} → 0` of Algebra, Lemma 10.138.9 is split, so it stays
> short exact after extending scalars along an arbitrary ring map `ε : Q → S`. This is the
> objectwise input to the exactness of the sequence of Tag 08QU.

```lean
theorem towerDifferential_shortExact_extendScalars
    (R P Q S : Type w) [CommRing R] [CommRing P] [CommRing Q] [CommRing S]
    [Algebra R P] [Algebra P Q] [Algebra R Q] [IsScalarTower R P Q]
    [Algebra.FormallySmooth P Q] (ε : Q →+* S) :
    ((ShortComplex.moduleCatMk (KaehlerDifferential.mapBaseChange R P Q)
        (KaehlerDifferential.map R P Q Q) (by
          apply LinearMap.ext
          intro x
          exact (KaehlerDifferential.exact_mapBaseChange_map R P Q).apply_apply_eq_zero x)).map
      (ModuleCat.extendScalars ε)).ShortExact
```

**`CommAlgCat.isSheaf_polynomialTowerTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldDifferentialSequence.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldDifferentialSequence.lean#L259). The attribute's comment: “exactness may be checked objectwise: every presheaf on the threefold site is a sheaf”.

> Every presheaf on `C_{C/B/A}` is a sheaf, because the topology of the site is chaotic.

```lean
theorem isSheaf_polynomialTowerTopology {D : Type*} [Category D]
    (F : (polynomialTowerSite A B C)ᵒᵖ ⥤ D) :
    Presheaf.IsSheaf (polynomialTowerTopology A B C) F
```

**`CommAlgCat.towerFirstOmega`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldDifferentialSequence.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldDifferentialSequence.lean#L318). The attribute's comment: “the sheaf Ω₁ = Ω\_\{𝒪/A} ⊗\_𝒪 B̲ on C\_\{B/A}”.

> `Ω₁ = Ω_{𝒪/A} ⊗_𝒪 B̲`, the sheaf of `B̲`-modules on `C_{B/A}`.

```lean
abbrev towerFirstOmega : SheafOfModules.{u + 1} (polynomialConstantRingSheaf A
    (towerBaseAlgebra A B))
```

**`CommAlgCat.towerSecondOmega`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldDifferentialSequence.lean, line 324](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldDifferentialSequence.lean#L324). The attribute's comment: “the sheaf Ω₂ = Ω\_\{𝒪/A} ⊗\_𝒪 C̲ on C\_\{C/A}”.

> `Ω₂ = Ω_{𝒪/A} ⊗_𝒪 C̲`, the sheaf of `C̲`-modules on `C_{C/A}`.

```lean
abbrev towerSecondOmega : SheafOfModules.{u + 1} (polynomialConstantRingSheaf A
    (towerTotalAlgebra A C))
```

**`CommAlgCat.towerThirdOmega`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldDifferentialSequence.lean, line 330](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldDifferentialSequence.lean#L330). The attribute's comment: “the sheaf Ω₃ = Ω\_\{𝒪/B} ⊗\_𝒪 C̲ on C\_\{C/B}”.

> `Ω₃ = Ω_{𝒪/B} ⊗_𝒪 C̲`, the sheaf of `C̲`-modules on `C_{C/B}`.

```lean
abbrev towerThirdOmega : SheafOfModules.{u + 1} (polynomialConstantRingSheaf B
    (towerRelativeAlgebra B C))
```

**`CommAlgCat.towerSecondTerm`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldDifferentialSequence.lean, line 363](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldDifferentialSequence.lean#L363). The attribute's comment: “the second term g₂⁻¹Ω₂ of the sequence”.

> `g₂⁻¹Ω₂`, a presheaf of `C̲`-modules on `C_{C/B/A}`: the inverse image along `g₂` is
> restriction along `u₂`, and the inverse image of `C̲` is `C̲`.

```lean
def towerSecondTerm : PresheafOfModules.{u + 1} (towerConstantRingSheaf A B C).obj
```

**`CommAlgCat.towerThirdTerm`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldDifferentialSequence.lean, line 369](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldDifferentialSequence.lean#L369). The attribute's comment: “the third term g₃⁻¹Ω₃ of the sequence”.

> `g₃⁻¹Ω₃`, a presheaf of `C̲`-modules on `C_{C/B/A}`.

```lean
def towerThirdTerm : PresheafOfModules.{u + 1} (towerConstantRingSheaf A B C).obj
```

**`CommAlgCat.towerFirstTerm`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldDifferentialSequence.lean, line 382](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldDifferentialSequence.lean#L382). The attribute's comment: “the first term g₁⁻¹Ω₁ ⊗\_\{B̲} C̲ of the sequence”.

> `g₁⁻¹Ω₁ ⊗_{B̲} C̲`, a presheaf of `C̲`-modules on `C_{C/B/A}`.

```lean
def towerFirstTerm : PresheafOfModules.{u + 1} (towerConstantRingSheaf A B C).obj
```

**`CommAlgCat.towerSections_formallySmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldDifferentialSequence.lean, line 447](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldDifferentialSequence.lean#L447). The attribute's comment: “the sections of 𝒪₂ are formally smooth over the sections of 𝒪₁: the formal smoothness input of the objectwise differential sequence”.

> **The sections of `𝒪₂` are formally smooth over the sections of `𝒪₁`.** Over the tower
> `(P → B, Q → C)` the map is the universe lift of `P → Q`, and `Q` is a polynomial algebra over
> `P` by the first condition on a polynomial tower, hence formally smooth over `P`; formal
> smoothness survives the universe lift by `RingHom.FormallySmooth.ulift`. This is the hypothesis
> `Algebra.FormallySmooth` that `CommAlgCat.towerDifferential_shortExact_extendScalars` needs at
> the object `W` of `C_{C/B/A}`.

```lean
theorem towerSections_formallySmooth (W : (polynomialTowerSite A B C)ᵒᵖ) :
    letI := ((towerLeftToRight A B C).app W).hom.toAlgebra
    Algebra.FormallySmooth ((towerLeftRingPresheaf A B C).obj W)
      ((towerRightRingPresheaf A B C).obj W)
```

**`CommAlgCat.towerSections_isPushout`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldDifferentialSequence.lean, line 466](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldDifferentialSequence.lean#L466). The attribute's comment: “the pushout square of the tower on the universe-lifted sections: the input that identifies the third term of the objectwise sequence”.

> **The pushout square of a polynomial tower survives the universe lift.** The sections of
> `𝒪₃` over the tower `(P → B, Q → C)` are `Q ⊗_P B`, so the square `P → B`, `P → Q`, `B → Q ⊗_P B`,
> `Q → Q ⊗_P B` of the tower is a pushout square of rings; `Algebra.IsPushout.ulift_tensorProduct`
> transports that to the universe lifts, which is the form in which the sections of the three
> structure sheaves carry it. This is the hypothesis `Algebra.IsPushout` that
> `KaehlerDifferential.tensorKaehlerEquiv` needs in order to identify `Ω_{𝒪₃/B̲}` with
> `𝒪₃ ⊗_{𝒪₂} Ω_{𝒪₂/𝒪₁}` on sections.

```lean
theorem towerSections_isPushout (W : (polynomialTowerSite A B C)ᵒᵖ) :
    Algebra.IsPushout (ULift.{u + 1} ↑(towerLeftAlgebra W.unop.unop.obj)) (ULift.{u + 1} B)
      (ULift.{u + 1} ↑(towerRightAlgebra W.unop.unop.obj))
      (ULift.{u + 1} ↑(towerBaseChangeAlgebra W.unop.unop.obj))
```

**`CommAlgCat.towerFirstSequenceMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldDifferentialSequence.lean, line 852](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldDifferentialSequence.lean#L852). The attribute's comment: “the first map g₁⁻¹Ω₁ ⊗\_\{B̲} C̲ ⟶ g₂⁻¹Ω₂ of the sequence”.

> **The first map `g₁⁻¹Ω₁ ⊗_{B̲} C̲ ⟶ g₂⁻¹Ω₂` of the sequence of Tag 08QU.** Both source and
> target are base changes of presheaves of relative differentials, so by the change-of-rings
> adjunction of Tag 03CU and the universal property of the presheaf of differentials the map is
> the same datum as `CommAlgCat.towerFirstDerivation`, namely `c ⊗ b ⊗ d p ↦ c·b ⊗ d p`.

```lean
def towerFirstSequenceMap : towerFirstTerm A B C ⟶ towerSecondTerm A B C
```

**`CommAlgCat.towerSecondSequenceMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldDifferentialSequence.lean, line 861](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldDifferentialSequence.lean#L861). The attribute's comment: “the second map g₂⁻¹Ω₂ ⟶ g₃⁻¹Ω₃ of the sequence”.

> **The second map `g₂⁻¹Ω₂ ⟶ g₃⁻¹Ω₃` of the sequence of Tag 08QU**, the datum of
> `CommAlgCat.towerSecondDerivation` under the change-of-rings adjunction of Tag 03CU and the
> universal property of the presheaf of differentials: `c ⊗ d q ↦ c ⊗ d(1 ⊗ q)`.

```lean
def towerSecondSequenceMap : towerSecondTerm A B C ⟶ towerThirdTerm A B C
```

**`CommAlgCat.towerSequenceMap_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldDifferentialSequence.lean, line 871](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldDifferentialSequence.lean#L871). The attribute's comment: “the two maps of the sequence compose to zero”.

> **The composite of the two maps of the sequence of Tag 08QU vanishes.** By the universal
> properties the composite is the map attached to the derivation `p ↦ 1 ⊗ d(1 ⊗ image of p)` of
> `𝒪₁` with values in `g₃⁻¹Ω₃`, and that derivation is zero: by the pushout square on sections
> (`CommAlgCat.towerRightToPushout_app_towerLeftToRight`) the image of `p` in `𝒪₃` comes from
> `B̲`, and `d` kills the image of the base sheaf of rings.

```lean
theorem towerSequenceMap_comp :
    towerFirstSequenceMap A B C ≫ towerSecondSequenceMap A B C = 0
```

**`CommAlgCat.towerShortComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldDifferentialSequence.lean, line 929](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldDifferentialSequence.lean#L929). The attribute's comment: “the sequence 0 ⟶ g₁⁻¹Ω₁ ⊗\_\{B̲} C̲ ⟶ g₂⁻¹Ω₂ ⟶ g₃⁻¹Ω₃ ⟶ 0 of sheaves of C̲-modules on C\_\{C/B/A}; its short exactness is not asserted here”.

> **The sequence of Tag 08QU as a short complex of sheaves of `C̲`-modules on `C_{C/B/A}`**,
> the image of `CommAlgCat.towerShortComplexPresheaf` under the equivalence
> `CommAlgCat.towerPresheafToSheaf`: every presheaf on the chaotic site is a sheaf.

```lean
def towerShortComplex : ShortComplex (SheafOfModules.{u + 1} (towerConstantRingSheaf A B C))
```

**`CommAlgCat.towerShortComplexPresheaf_shortExact_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldDifferentialSequence.lean, line 1026](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldDifferentialSequence.lean#L1026). The attribute's comment: “the sequence of sections over a polynomial tower is short exact: the objectwise form of the short exactness”.

> **The sequence of Tag 08QU is short exact over every object of `C_{C/B/A}`.** Over the
> polynomial tower `(P → B, Q → C)`, with `T = Q ⊗_P B` and every ring replaced by its universe
> lift, the three modules of sections are `C̲(W) ⊗_{B̲(W)} (B̲(W) ⊗_P Ω_{P/A})`, `C̲(W) ⊗_Q Ω_{Q/A}`
> and `C̲(W) ⊗_T Ω_{T/B}`, and the sequence they form is the split sequence of
> `CommAlgCat.towerDifferential_shortExact_extendScalars` for the tower `A → P → Q` base changed
> along the augmentation `Q → C̲(W)`. The middle terms agree on the nose
> (`CommAlgCat.towerSecondTerm_obj`); the first terms are identified by cancelling the base change
> twice through `C̲(W) ⊗_P Ω_{P/A}`, and the third ones by
> `KaehlerDifferential.tensorKaehlerEquiv`, available because
> `CommAlgCat.towerSections_isPushout` makes `T` the pushout of `B ← P → Q`. Both squares are
> checked on the generators `1 ⊗ 1 ⊗ d p` and `1 ⊗ d q`, where the two maps of the sequence are
> computed by the change-of-rings adjunction of Tag 03CU.

```lean
theorem towerShortComplexPresheaf_shortExact_obj (W : (polynomialTowerSite A B C)ᵒᵖ) :
    ((towerShortComplexPresheaf A B C).map
      (PresheafOfModules.evaluation (towerConstantRingSheaf A B C).obj W)).ShortExact
```

**`CommAlgCat.towerShortComplex_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldDifferentialSequence.lean, line 1345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldDifferentialSequence.lean#L1345). The attribute's comment: “the sequence of sheaves of C-modules on C\_\{C/B/A} is short exact”.

> **Tag 08QU: the sequence of sheaves of `C̲`-modules on `C_{C/B/A}`
> `0 → g₁⁻¹Ω₁ ⊗_{B̲} C̲ → g₂⁻¹Ω₂ → g₃⁻¹Ω₃ → 0` is short exact.** By
> `CommAlgCat.towerShortComplex_shortExact_of_objectwise` this is the objectwise statement
> `CommAlgCat.towerShortComplexPresheaf_shortExact_obj`: a short complex of presheaves of
> `C̲`-modules on the chaotic site `C_{C/B/A}` is short exact as soon as its sequence of sections
> over every polynomial tower is, and there the sequence is the split differential sequence of
> Algebra, Lemma 10.138.9 for `A → P → Q` base changed along the augmentation `Q → C̲`.

```lean
theorem towerShortComplex_shortExact : (towerShortComplex A B C).ShortExact
```

## Tag 08QV, a lemma

[Tag 08QV](https://stacks.math.columbia.edu/tag/08QV) in the Stacks Project.

**`CommAlgCat.leftDerivedColimitThirdInverseImageZeroIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialOnTop/SmallModel.lean, line 310](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialOnTop/SmallModel.lean#L310). The attribute's comment: “the degree-zero half of `Lπ_!(g₃^{-1}ℱ) = Lπ_{3,!}ℱ = π_{3,!}ℱ`, read at the small models of the footnote-restricted sites of Tag 08QT, with `π_!` the colimit over the index category of Tag 08PF and `κ`, `μ` the bounds on the two layers of variables; the vanishing in positive degrees is `CommAlgCat.isZero_leftDerivedColimitThirdInverseImage_succ`”.

> **Stacks 08QV, in degree zero.** With notation as in Tag 08QT, suppose `C = B[E]` is a
> polynomial algebra over `B`. Then `π_!(g₃^{-1}ℱ) = π_{3,!}ℱ` for every abelian presheaf `ℱ` on
> the small model of the restricted site `C_{C/B}`: both sides are the sections of `ℱ` at the
> identity augmentation `C → C`.

```lean
def leftDerivedColimitThirdInverseImageZeroIso
    (hε : SSet.trivialKanFibrations (Functor.whiskerRight ε (forget (CommAlgCat.{u} A))))
    (F : (smallBoundedPolynomialSite B (towerRelativeAlgebra B C) μ)ᵒᵖ ⥤ AddCommGrpCat.{u}) :
    ((colim : ((smallBoundedPolynomialTowerSite A B C κ μ)ᵒᵖ ⥤ AddCommGrpCat.{u}) ⥤
          AddCommGrpCat.{u}).leftDerived 0).obj
        ((smallTowerThirdInverseImage A B C κ μ).obj F) ≅
      colimit F
```

**`CommAlgCat.isZero_leftDerivedColimitThirdInverseImage_succ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialOnTop/SmallModel.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialOnTop/SmallModel.lean#L331). The attribute's comment: “the positive-degree half of `Lπ_!(g₃^{-1}ℱ) = Lπ_{3,!}ℱ = π_{3,!}ℱ`, read at the small models of the footnote-restricted sites of Tag 08QT: `Lπ_!(g₃^{-1}ℱ)` is concentrated in degree zero, where it is `π_{3,!}ℱ` by `CommAlgCat.leftDerivedColimitThirdInverseImageZeroIso`”.

> **Stacks 08QV, in positive degrees.** With notation as in Tag 08QT, suppose `C = B[E]` is a
> polynomial algebra over `B`. Then `L_nπ_!(g₃^{-1}ℱ) = 0` for `n > 0`: the simplicial abelian
> group `(g₃^{-1}ℱ)(U_•)` is constant.

```lean
theorem isZero_leftDerivedColimitThirdInverseImage_succ
    (hε : SSet.trivialKanFibrations (Functor.whiskerRight ε (forget (CommAlgCat.{u} A))))
    (F : (smallBoundedPolynomialSite B (towerRelativeAlgebra B C) μ)ᵒᵖ ⥤ AddCommGrpCat.{u})
    (n : ℕ) :
    IsZero (((colim : ((smallBoundedPolynomialTowerSite A B C κ μ)ᵒᵖ ⥤ AddCommGrpCat.{u}) ⥤
        AddCommGrpCat.{u}).leftDerived (n + 1)).obj
      ((smallTowerThirdInverseImage A B C κ μ).obj F))
```

**`CommAlgCat.polynomialTowerDerivedColimitThirdInverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialOnTopLargeSite.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialOnTopLargeSite.lean#L268). The attribute's comment: “the first equality `Lπ_!(g₃^{-1}ℱ) = Lπ_{3,!}ℱ` in `D(Ab)`, at the sites of Tag 08QT and Tag 08PR themselves -- `CommAlgCat.polynomialTowerSite` and `CommAlgCat.polynomialSite B (towerRelativeAlgebra B C)`, not restrictions of them -- with `Lπ_!` and `Lπ_{3,!}` the total left derived functors of the colimits over the index categories of Tag 08PF and the coefficients at the universe `u + 1` of the sites' objects. The second equality `Lπ_{3,!}ℱ = π_{3,!}ℱ` is `CommAlgCat.polynomialSiteDerivedColimitThirdIso`”.

> **Stacks 08QV, the first equality `Lπ_!(g₃^{-1}ℱ) = Lπ_{3,!}ℱ`, at the sites themselves.**
> With notation as in Tag 08QT, suppose `C = B[E]` is a polynomial algebra over `B`. Then
>
> `Lπ_!(g₃^{-1}ℱ) = Lπ_{3,!}ℱ`
>
> in `D(Ab)`, for every abelian sheaf `ℱ` on `C_{C/B}` -- the abelian presheaves being the abelian
> sheaves, the topology being chaotic.
>
> Both sides are the extended Moore complex of `ℱ(u₃(U_•))` for the cosimplicial object `U_•` of the
> towers `(P_n → B, P_n[E] → C)`: on the left by the criterion of Tag 08Q9 applied to `U_•` on
> `C_{C/B/A}`, on the right by that criterion applied to the constant cosimplicial object at the
> identity augmentation `C → C` on `C_{C/B}`, which `u₃(U_•)` is. No hypothesis on a resolution
> survives: the resolution of `B` over `A` is the standard one of Tag 08PM, whose terms are
> polynomial algebras and whose augmentation is a trivial Kan fibration by Tag 08QI.

```lean
def polynomialTowerDerivedColimitThirdInverseImageIso
    (F : (polynomialSite B (towerRelativeAlgebra B C))ᵒᵖ ⥤ AddCommGrpCat.{u + 1}) :
    (totalDerivedColimit' (polynomialTowerSite A B C) AddCommGrpCat.{u + 1}).obj
        (DerivedCategory.Q.obj
          ((HomologicalComplex.single ((polynomialTowerSite A B C)ᵒᵖ ⥤ AddCommGrpCat.{u + 1})
            (ComplexShape.up ℤ) 0).obj ((towerThirdInverseImage A B C).obj F))) ≅
      (totalDerivedColimit' (polynomialSite B (towerRelativeAlgebra B C))
          AddCommGrpCat.{u + 1}).obj
        (DerivedCategory.Q.obj
          ((HomologicalComplex.single
            ((polynomialSite B (towerRelativeAlgebra B C))ᵒᵖ ⥤ AddCommGrpCat.{u + 1})
            (ComplexShape.up ℤ) 0).obj F))
```

**`CommAlgCat.polynomialSiteDerivedColimitThirdIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldPolynomialOnTopLargeSite.lean, line 304](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldPolynomialOnTopLargeSite.lean#L304). The attribute's comment: “the second equality `Lπ_{3,!}ℱ = π_{3,!}ℱ` in `D(Ab)`, at the site `C_{C/B}` of Tag 08PR itself -- `CommAlgCat.polynomialSite B (towerRelativeAlgebra B C)`, not a restriction of it -- with `Lπ_{3,!}` the total left derived functor of the colimit over its index category and `π_{3,!}ℱ` that colimit, as in Tag 08PF. The first equality `Lπ_!(g₃^{-1}ℱ) = Lπ_{3,!}ℱ` is `CommAlgCat.polynomialTowerDerivedColimitThirdInverseImageIso`”.

> **Stacks 08QV, the second equality `Lπ_{3,!}ℱ = π_{3,!}ℱ`, at the site `C_{C/B}` itself.**
> With notation as in Tag 08QT, suppose `C = B[E]` is a polynomial algebra over `B`. Then
>
> `Lπ_{3,!}ℱ = π_{3,!}ℱ`
>
> in `D(Ab)`, for every abelian sheaf `ℱ` on `C_{C/B}`: the left side is the complex concentrated in
> degree zero on `π_{3,!}ℱ`, the colimit of `ℱ` over the index category of Tag 08PF.
>
> This is where `C = B[E]` is used on `C_{C/B}` itself: it makes the identity augmentation `C → C`
> an object of that site, and that object is initial there, so `π_{3,!}` is an evaluation and hence
> exact.

```lean
def polynomialSiteDerivedColimitThirdIso
    (F : (polynomialSite B (towerRelativeAlgebra B C))ᵒᵖ ⥤ AddCommGrpCat.{u + 1}) :
    (totalDerivedColimit' (polynomialSite B (towerRelativeAlgebra B C))
          AddCommGrpCat.{u + 1}).obj
        (DerivedCategory.Q.obj
          ((HomologicalComplex.single
            ((polynomialSite B (towerRelativeAlgebra B C))ᵒᵖ ⥤ AddCommGrpCat.{u + 1})
            (ComplexShape.up ℤ) 0).obj F)) ≅
      DerivedCategory.Q.obj
        ((HomologicalComplex.single AddCommGrpCat.{u + 1} (ComplexShape.up ℤ) 0).obj
          (colimit F))
```

## Tag 08QW, a lemma

[Tag 08QW](https://stacks.math.columbia.edu/tag/08QW) in the Stacks Project.

**`CommAlgCat.derivedLowerShriek_comp_inverseImage_polynomialTower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ThreefoldLowerShriekComparison.lean, line 308](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ThreefoldLowerShriekComparison.lean#L308).

> **Stacks Project, Tag 08QW.** With notation as in Tag 08QT, `Lg_{i,!} ∘ g_i⁻¹ = id` for
> `i = 1, 2, 3`, and hence also `Lπ_! ∘ g_i⁻¹ = Lπ_{i,!}` for `i = 1, 2, 3`.
>
> Here `g₁`, `g₂`, `g₃` are the morphisms of topoi from `C_{C/B/A}` to `C_{B/A}`, `C_{C/A}` and
> `C_{C/B}` induced by `u₁`, `u₂`, `u₃`, and `π`, `π₁`, `π₂`, `π₃` the projections of the four sites
> to the point; all four sites carry the chaotic topology. The statement is about abelian sheaves on
> the unbounded derived categories, for *every* left derived functor of each lower shriek and
> *every* derived functor of each inverse image, so it does not depend on choices. The six parts
> are `CommAlgCat.derivedLowerShriekFirstInverseImageIso`,
> `CommAlgCat.derivedLowerShriekSecondInverseImageIso`,
> `CommAlgCat.derivedLowerShriekThirdInverseImageIso`,
> `CommAlgCat.derivedLowerShriekProjectionFirstIso`,
> `CommAlgCat.derivedLowerShriekProjectionSecondIso` and
> `CommAlgCat.derivedLowerShriekProjectionThirdIso`.

```lean
theorem derivedLowerShriek_comp_inverseImage_polynomialTower :
    (∀ (L : DerivedCategory (Sheaf (polynomialTowerTopology A B C) AddCommGrpCat.{u + 1}) ⥤
          DerivedCategory
            (Sheaf (polynomialTopology A (towerBaseAlgebra A B)) AddCommGrpCat.{u + 1}))
      (α : DerivedCategory.Qh ⋙ L ⟶
        ((polynomialTowerFirst A B C).sheafPullback AddCommGrpCat.{u + 1}
          (polynomialTowerTopology A B C)
          (polynomialTopology A (towerBaseAlgebra A B))).mapHomotopyCategory
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh)
      [L.IsLeftDerivedFunctor α (HomotopyCategory.quasiIso
        (Sheaf (polynomialTowerTopology A B C) AddCommGrpCat.{u + 1}) (ComplexShape.up ℤ))]
      (G : DerivedCategory
          (Sheaf (polynomialTopology A (towerBaseAlgebra A B)) AddCommGrpCat.{u + 1}) ⥤
          DerivedCategory (Sheaf (polynomialTowerTopology A B C) AddCommGrpCat.{u + 1}))
      (_ : DerivedCategory.Qh ⋙ G ≅
        ((polynomialTowerFirst A B C).sheafPushforwardContinuous AddCommGrpCat.{u + 1}
          (polynomialTowerTopology A B C)
          (polynomialTopology A (towerBaseAlgebra A B))).mapHomotopyCategory
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh),
      Nonempty (G ⋙ L ≅ 𝟭 _)) ∧
    (∀ (L : DerivedCategory (Sheaf (polynomialTowerTopology A B C) AddCommGrpCat.{u + 1}) ⥤
          DerivedCategory
            (Sheaf (polynomialTopology A (towerTotalAlgebra A C)) AddCommGrpCat.{u + 1}))
      (α : DerivedCategory.Qh ⋙ L ⟶
        ((polynomialTowerSecond A B C).sheafPullback AddCommGrpCat.{u + 1}
          (polynomialTowerTopology A B C)
          (polynomialTopology A (towerTotalAlgebra A C))).mapHomotopyCategory
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh)
      [L.IsLeftDerivedFunctor α (HomotopyCategory.quasiIso
        (Sheaf (polynomialTowerTopology A B C) AddCommGrpCat.{u + 1}) (ComplexShape.up ℤ))]
      (G : DerivedCategory
          (Sheaf (polynomialTopology A (towerTotalAlgebra A C)) AddCommGrpCat.{u + 1}) ⥤
          DerivedCategory (Sheaf (polynomialTowerTopology A B C) AddCommGrpCat.{u + 1}))
      (_ : DerivedCategory.Qh ⋙ G ≅
        ((polynomialTowerSecond A B C).sheafPushforwardContinuous AddCommGrpCat.{u + 1}
          (polynomialTowerTopology A B C)
          (polynomialTopology A (towerTotalAlgebra A C))).mapHomotopyCategory
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh),
      Nonempty (G ⋙ L ≅ 𝟭 _)) ∧
    (∀ (L : DerivedCategory (Sheaf (polynomialTowerTopology A B C) AddCommGrpCat.{u + 1}) ⥤
          DerivedCategory
            (Sheaf (polynomialTopology B (towerRelativeAlgebra B C)) AddCommGrpCat.{u + 1}))
      (α : DerivedCategory.Qh ⋙ L ⟶
        ((polynomialTowerThird A B C).sheafPullback AddCommGrpCat.{u + 1}
          (polynomialTowerTopology A B C)
          (polynomialTopology B (towerRelativeAlgebra B C))).mapHomotopyCategory
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh)
      [L.IsLeftDerivedFunctor α (HomotopyCategory.quasiIso
        (Sheaf (polynomialTowerTopology A B C) AddCommGrpCat.{u + 1}) (ComplexShape.up ℤ))]
      (G : DerivedCategory
          (Sheaf (polynomialTopology B (towerRelativeAlgebra B C)) AddCommGrpCat.{u + 1}) ⥤
          DerivedCategory (Sheaf (polynomialTowerTopology A B C) AddCommGrpCat.{u + 1}))
      (_ : DerivedCategory.Qh ⋙ G ≅
        ((polynomialTowerThird A B C).sheafPushforwardContinuous AddCommGrpCat.{u + 1}
          (polynomialTowerTopology A B C)
          (polynomialTopology B (towerRelativeAlgebra B C))).mapHomotopyCategory
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh),
      Nonempty (G ⋙ L ≅ 𝟭 _)) ∧
    (∀ (G : DerivedCategory
          (Sheaf (polynomialTopology A (towerBaseAlgebra A B)) AddCommGrpCat.{u + 1}) ⥤
          DerivedCategory (Sheaf (polynomialTowerTopology A B C) AddCommGrpCat.{u + 1}))
      (_ : DerivedCategory.Qh ⋙ G ≅
        ((polynomialTowerFirst A B C).sheafPushforwardContinuous AddCommGrpCat.{u + 1}
          (polynomialTowerTopology A B C)
          (polynomialTopology A (towerBaseAlgebra A B))).mapHomotopyCategory
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh)
      (L : DerivedCategory (Sheaf (polynomialTowerTopology A B C) AddCommGrpCat.{u + 1}) ⥤
          DerivedCategory
            (Sheaf (GrothendieckTopology.trivial (Discrete PUnit.{u + 2})) AddCommGrpCat.{u + 1}))
      (α : DerivedCategory.Qh ⋙ L ⟶
        ((Functor.star (polynomialTowerSite A B C)).sheafPullback AddCommGrpCat.{u + 1}
          (polynomialTowerTopology A B C)
          (GrothendieckTopology.trivial (Discrete PUnit.{u + 2}))).mapHomotopyCategory
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh)
      [L.IsLeftDerivedFunctor α (HomotopyCategory.quasiIso
        (Sheaf (polynomialTowerTopology A B C) AddCommGrpCat.{u + 1}) (ComplexShape.up ℤ))]
      (L' : DerivedCategory
          (Sheaf (polynomialTopology A (towerBaseAlgebra A B)) AddCommGrpCat.{u + 1}) ⥤
          DerivedCategory
            (Sheaf (GrothendieckTopology.trivial (Discrete PUnit.{u + 2})) AddCommGrpCat.{u + 1}))
      (α' : DerivedCategory.Qh ⋙ L' ⟶
        ((Functor.star (polynomialSite A (towerBaseAlgebra A B))).sheafPullback
          AddCommGrpCat.{u + 1} (polynomialTopology A (towerBaseAlgebra A B))
          (GrothendieckTopology.trivial (Discrete PUnit.{u + 2}))).mapHomotopyCategory
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh)
      [L'.IsLeftDerivedFunctor α' (HomotopyCategory.quasiIso
        (Sheaf (polynomialTopology A (towerBaseAlgebra A B)) AddCommGrpCat.{u + 1})
        (ComplexShape.up ℤ))],
      Nonempty (G ⋙ L ≅ L')) ∧
    (∀ (G : DerivedCategory
          (Sheaf (polynomialTopology A (towerTotalAlgebra A C)) AddCommGrpCat.{u + 1}) ⥤
          DerivedCategory (Sheaf (polynomialTowerTopology A B C) AddCommGrpCat.{u + 1}))
      (_ : DerivedCategory.Qh ⋙ G ≅
        ((polynomialTowerSecond A B C).sheafPushforwardContinuous AddCommGrpCat.{u + 1}
          (polynomialTowerTopology A B C)
          (polynomialTopology A (towerTotalAlgebra A C))).mapHomotopyCategory
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh)
      (L : DerivedCategory (Sheaf (polynomialTowerTopology A B C) AddCommGrpCat.{u + 1}) ⥤
          DerivedCategory
            (Sheaf (GrothendieckTopology.trivial (Discrete PUnit.{u + 2})) AddCommGrpCat.{u + 1}))
      (α : DerivedCategory.Qh ⋙ L ⟶
        ((Functor.star (polynomialTowerSite A B C)).sheafPullback AddCommGrpCat.{u + 1}
          (polynomialTowerTopology A B C)
          (GrothendieckTopology.trivial (Discrete PUnit.{u + 2}))).mapHomotopyCategory
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh)
      [L.IsLeftDerivedFunctor α (HomotopyCategory.quasiIso
        (Sheaf (polynomialTowerTopology A B C) AddCommGrpCat.{u + 1}) (ComplexShape.up ℤ))]
      (L' : DerivedCategory
          (Sheaf (polynomialTopology A (towerTotalAlgebra A C)) AddCommGrpCat.{u + 1}) ⥤
          DerivedCategory
            (Sheaf (GrothendieckTopology.trivial (Discrete PUnit.{u + 2})) AddCommGrpCat.{u + 1}))
      (α' : DerivedCategory.Qh ⋙ L' ⟶
        ((Functor.star (polynomialSite A (towerTotalAlgebra A C))).sheafPullback
          AddCommGrpCat.{u + 1} (polynomialTopology A (towerTotalAlgebra A C))
          (GrothendieckTopology.trivial (Discrete PUnit.{u + 2}))).mapHomotopyCategory
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh)
      [L'.IsLeftDerivedFunctor α' (HomotopyCategory.quasiIso
        (Sheaf (polynomialTopology A (towerTotalAlgebra A C)) AddCommGrpCat.{u + 1})
        (ComplexShape.up ℤ))],
      Nonempty (G ⋙ L ≅ L')) ∧
    (∀ (G : DerivedCategory
          (Sheaf (polynomialTopology B (towerRelativeAlgebra B C)) AddCommGrpCat.{u + 1}) ⥤
          DerivedCategory (Sheaf (polynomialTowerTopology A B C) AddCommGrpCat.{u + 1}))
      (_ : DerivedCategory.Qh ⋙ G ≅
        ((polynomialTowerThird A B C).sheafPushforwardContinuous AddCommGrpCat.{u + 1}
          (polynomialTowerTopology A B C)
          (polynomialTopology B (towerRelativeAlgebra B C))).mapHomotopyCategory
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh)
      (L : DerivedCategory (Sheaf (polynomialTowerTopology A B C) AddCommGrpCat.{u + 1}) ⥤
          DerivedCategory
            (Sheaf (GrothendieckTopology.trivial (Discrete PUnit.{u + 2})) AddCommGrpCat.{u + 1}))
      (α : DerivedCategory.Qh ⋙ L ⟶
        ((Functor.star (polynomialTowerSite A B C)).sheafPullback AddCommGrpCat.{u + 1}
          (polynomialTowerTopology A B C)
          (GrothendieckTopology.trivial (Discrete PUnit.{u + 2}))).mapHomotopyCategory
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh)
      [L.IsLeftDerivedFunctor α (HomotopyCategory.quasiIso
        (Sheaf (polynomialTowerTopology A B C) AddCommGrpCat.{u + 1}) (ComplexShape.up ℤ))]
      (L' : DerivedCategory
          (Sheaf (polynomialTopology B (towerRelativeAlgebra B C)) AddCommGrpCat.{u + 1}) ⥤
          DerivedCategory
            (Sheaf (GrothendieckTopology.trivial (Discrete PUnit.{u + 2})) AddCommGrpCat.{u + 1}))
      (α' : DerivedCategory.Qh ⋙ L' ⟶
        ((Functor.star (polynomialSite B (towerRelativeAlgebra B C))).sheafPullback
          AddCommGrpCat.{u + 1} (polynomialTopology B (towerRelativeAlgebra B C))
          (GrothendieckTopology.trivial (Discrete PUnit.{u + 2}))).mapHomotopyCategory
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh)
      [L'.IsLeftDerivedFunctor α' (HomotopyCategory.quasiIso
        (Sheaf (polynomialTopology B (towerRelativeAlgebra B C)) AddCommGrpCat.{u + 1})
        (ComplexShape.up ℤ))],
      Nonempty (G ⋙ L ≅ L'))
```

## Tag 08QX, a proposition

[Tag 08QX](https://stacks.math.columbia.edu/tag/08QX) in the Stacks Project.

**`CommAlgCat.exists_distTriang_fundamentalVertex_of_isResolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/Fundamental.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/Fundamental.lean#L159). The attribute's comment: “the triangle on the three vertices of the display of Tag 08QS, under TWO carried hypotheses the source lacks: `B → C` injective, as in Tag 08SD, whose removal needs the product decomposition of Tag 08SC; and the key fact of Tag 08SD, that the base-changed resolution Q\_bullet ⊗\_\{P\_bullet} B is a resolution of C over B, which rests on Tag 08RX. Neither tag is proved in this library”.

> **The fundamental triangle of the cotangent complex.** Let `A → B → C` be ring maps. Then there
> is a distinguished triangle
>
> `L_{B/A} ⊗^𝐋_B C ⟶ L_{C/A} ⟶ L_{C/B} ⟶ (L_{B/A} ⊗^𝐋_B C)[1]`
>
> in `D(C)`, on the three vertices of the display of Tag 08QS.
>
> Two hypotheses the source does not have are carried: `B → C` is injective, as in Tag 08SD, and the
> base-changed resolution `Q̄_• = Q_• ⊗_{P_•} B` of Tag 08SD is a resolution of `C` over `B` — its
> terms are polynomial algebras over `B` and its augmentation to `C` is a trivial Kan fibration on
> underlying simplicial sets.

```lean
theorem exists_distTriang_fundamentalVertex_of_isResolution
    (A : Type u) [CommRing A] (B : Type u) [CommRing B] [Algebra A B]
    (C : Type u) [CommRing C] [Algebra A C] [Algebra B C] [IsScalarTower A B C]
    (hf : Function.Injective (algebraMap B C))
    (hP : ∀ n, IsPolynomialAlgebra B
      ((baseChangedStandardResolution A (towerHom A B C)).left.obj n))
    (hε : SSet.trivialKanFibrations (Functor.whiskerRight
      (baseChangedStandardResolution A (towerHom A B C)).hom (forget (CommAlgCat.{u} B)))) :
    ∃ (α : fundamentalVertex₁.{u, u, u + 1, u + 1} A B C ⟶ fundamentalVertex₂.{u, u, u + 1} A C)
      (β : fundamentalVertex₂.{u, u, u + 1} A C ⟶ fundamentalVertex₃.{u, u, u + 1} B C)
      (δ : fundamentalVertex₃.{u, u, u + 1} B C ⟶
        (fundamentalVertex₁.{u, u, u + 1, u + 1} A B C)⟦(1 : ℤ)⟧),
      Triangle.mk α β δ ∈ distTriang (DerivedCategory (ModuleCat.{u} C))
```

**`CommAlgCat.productFundamentalTriangle_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/ProductDescent.lean, line 357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/ProductDescent.lean#L357). The attribute's comment: “the proposition: for ring maps `A → B → C` the display of Tag 08QS is a distinguished triangle in `D(C)`, on the display's own three vertices and with the display's own three morphisms. The third of them is `CommAlgCat.productFundamentalMor₃`”.

> **Stacks Project, Tag 08QX, and the distinguishedness asserted by the display of Tag 08QS.**
> Let `A → B → C` be ring maps. Then
>
> `L_{B/A} ⊗^𝐋_B C ⟶ L_{C/A} ⟶ L_{C/B} ⟶ (L_{B/A} ⊗^𝐋_B C)[1]`
>
> is a distinguished triangle in `D(C)`, on the three vertices of the display of
> [Stacks, Tag 08QS], with the display's own first two morphisms
> `CommAlgCat.fundamentalMor₁` and `CommAlgCat.fundamentalMor₂` — the two functoriality maps of
> [Stacks, Tag 08PN] for the two commutative squares of the tower — and with
> `CommAlgCat.productFundamentalMor₃` for its third.
>
> The display of Tag 08QS is written as a triangle, and what makes it one is exactly this
> statement, so the display's distinguishedness clause is registered here as well: the three
> objects and the three arrows of the display are named by
> `CommAlgCat.fundamentalVertex₁`, `CommAlgCat.fundamentalVertex₂`,
> `CommAlgCat.fundamentalVertex₃`, `CommAlgCat.fundamentalMor₁`, `CommAlgCat.fundamentalMor₂` and
> `CommAlgCat.productFundamentalMor₃`, and that they form a triangle at all is Proposition 08QX.
>
> The proof is the one of [Stacks, Remark 08SD]: the triangle for `A → B → B × C`, where the map
> is the split injection `b ↦ (b, f b)`, base changed along the flat projection `B × C → C`.

```lean
theorem productFundamentalTriangle_distinguished :
    Triangle.mk (fundamentalMor₁.{u} A B C) (fundamentalMor₂.{u} A B C)
        (productFundamentalMor₃ A B C) ∈ distTriang (DerivedCategory (ModuleCat.{u} C))
```

## Tag 08SD, a remark

[Tag 08SD](https://stacks.math.columbia.edu/tag/08SD) in the Stacks Project.

**`CommAlgCat.baseChangedStandardResolution`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/BaseChange.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/BaseChange.lean#L56). The attribute's comment: “base\_changed\_standard\_resolution”.

> The standard resolution of `C` over `A`, base changed along the standard
> resolution of `B` to give an augmented simplicial `B`-algebra.

```lean
noncomputable def baseChangedStandardResolution
    (A : Type u) [CommRing A]
    {B C : CommAlgCat.{max u v} A} (f : B ⟶ C) :
    SimplicialObject.Augmented (CommAlgCat.{max u v} B)
```

**`CommAlgCat.standardResolution_isPolynomialAlgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/BaseChange.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/BaseChange.lean#L189). The attribute's comment: “polynomiality”.

> Every term of the standard resolution of `C` is a polynomial algebra over
> the corresponding term of the standard resolution of `B`, when `B → C` is injective.

```lean
theorem standardResolution_isPolynomialAlgebra
    (A : Type u) [CommRing A]
    {B C : CommAlgCat.{max u v} A} (f : B ⟶ C)
    (hf : Function.Injective f.hom) (n : SimplexCategoryᵒᵖ) :
    let P := (standardResolution A B).left.obj n
    let Q := (standardResolution A C).left.obj n
    letI : Algebra P Q :=
      (((standardResolutionFunctor A).map f).left.app n).hom.toAlgebra
    IsPolynomialAlgebra P (CommAlgCat.of P Q)
```

**`CommAlgCat.fundamentalTriangle_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/BaseChangedResolutionTriangle.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/BaseChangedResolutionTriangle.lean#L132). The attribute's comment: “the first paragraph of the remark, for `A → B → C` with `B → C` injective: `Q_n` is polynomial over `P_n`; `Q̄_• = Q_• ⊗_{P_•} B` is a resolution of `C` over `B`; the sequence of differentials is short exact; and its triangle is the fundamental triangle, with the canonical first two morphisms, on the vertices `L_{B/A} ⊗^𝐋_B C`, `L_{C/A}`, `L_{C/B}`”.

> **Stacks Project, Remark 08SD, first paragraph.** Let `A → B → C` be ring maps with `B → C`
> injective, let `P_• → B` be the standard resolution of `B` over `A`, `Q_• → C` that of `C` over
> `A`, and `Q̄_• = Q_• ⊗_{P_•} B`. Then
>
> 1. every `Q_n` is a polynomial algebra over `P_n`;
> 2. `Q̄_• → C` is a resolution of `C` over `B` (the key fact);
> 3. the sequence of complexes of `C`-modules
>    `0 → Ω_{P_•/A} ⊗_{P_•} C → Ω_{Q_•/A} ⊗_{Q_•} C → Ω_{Q̄_•/B} ⊗_{Q̄_•} C → 0` is short exact;
> 4. the distinguished triangle associated to that short exact sequence is isomorphic to the
>    fundamental triangle `L_{B/A} ⊗^𝐋_B C → L_{C/A} → L_{C/B} → (L_{B/A} ⊗^𝐋_B C)[1]` with its
>    canonical first two morphisms, which is therefore distinguished in `D(C)`.

```lean
theorem fundamentalTriangle_of_injective (hf : Function.Injective (algebraMap B C)) :
    (∀ n : SimplexCategoryᵒᵖ,
      letI : Algebra ((standardResolution A (CommAlgCat.of A B)).left.obj n)
          ((standardResolution A (CommAlgCat.of A C)).left.obj n) :=
        (((standardResolutionFunctor A).map (towerHom A B C)).left.app n).hom.toAlgebra
      IsPolynomialAlgebra ((standardResolution A (CommAlgCat.of A B)).left.obj n)
        (CommAlgCat.of ((standardResolution A (CommAlgCat.of A B)).left.obj n)
          ((standardResolution A (CommAlgCat.of A C)).left.obj n))) ∧
    @IsResolution ↥(CommAlgCat.of A B) (CommAlgCat.of A B).commRing
      ↥(algebraOver (towerHom A B C)) (algebraOver (towerHom A B C)).commRing
      (algebraOver (towerHom A B C)).algebra
      (baseChangedStandardResolution A (towerHom A B C)).left
      (baseChangedStandardResolution A (towerHom A B C)).hom ∧
    (cotangentDifferentialComplexes A (towerHom A B C)).ShortExact ∧
    Nonempty (cotangentTriangle A (towerHom A B C)
        (show Function.Injective (towerHom A B C).hom from hf) ≅
      Triangle.mk (fundamentalMor₁.{u} A B C) (fundamentalMor₂.{u} A B C)
        (fundamentalMor₃ A B C hf)) ∧
    Triangle.mk (fundamentalMor₁.{u} A B C) (fundamentalMor₂.{u} A B C)
        (fundamentalMor₃ A B C hf) ∈ distTriang (DerivedCategory (ModuleCat.{u} C))
```

**`CommAlgCat.fundamentalTriangle_of_productDescent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/BaseChangedResolutionTriangle.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/BaseChangedResolutionTriangle.lean#L191). The attribute's comment: “the second paragraph of the remark, for arbitrary `A → B → C`: `B → B × C` is injective, the base change along the flat `B × C → C` of the fundamental triangle of `A → B → B × C` is distinguished in `D(C)` and, by Tag 08SC, isomorphic to the fundamental triangle of `A → B → C` with its canonical first two morphisms”.

> **Stacks Project, Remark 08SD, second paragraph.** Let `A → B → C` be arbitrary ring maps.
> Then `B → B × C`, `b ↦ (b, f b)`, is injective, so the first paragraph gives the fundamental
> triangle of `A → B → B × C`; its base change along the flat ring map `B × C → C` is a
> distinguished triangle in `D(C)`, and by Tag 08SC it is isomorphic to the fundamental triangle
> `L_{B/A} ⊗^𝐋_B C → L_{C/A} → L_{C/B} → (L_{B/A} ⊗^𝐋_B C)[1]` with its canonical first two
> morphisms, which is therefore distinguished.

```lean
theorem fundamentalTriangle_of_productDescent :
    Function.Injective (algebraMap B (B × C)) ∧
    productDescentTriangle A B C ∈ distTriang (DerivedCategory (ModuleCat.{u} C)) ∧
    Nonempty (productDescentTriangle A B C ≅
      Triangle.mk (fundamentalMor₁.{u} A B C) (fundamentalMor₂.{u} A B C)
        (productFundamentalMor₃ A B C)) ∧
    Triangle.mk (fundamentalMor₁.{u} A B C) (fundamentalMor₂.{u} A B C)
        (productFundamentalMor₃ A B C) ∈ distTriang (DerivedCategory (ModuleCat.{u} C))
```

**`CommAlgCat.exists_distinguished_derivedBaseChange_cotangentTriangle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/DerivedFirstVertex.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/DerivedFirstVertex.lean#L167). The attribute's comment: “differential\_sequence triangle, derived first vertex”.

> **Stacks Project, Tag 08SD, with the derived base change as first vertex.**
>
> For an injective map `f : B ⟶ C` of `A`-algebras there is a distinguished triangle in
> `D(ModuleCat C)`
> `L_{B/A} ⊗ᴸ_B C → L_{C/A} → (third vertex of CommAlgCat.cotangentTriangle) → (L_{B/A} ⊗ᴸ_B C)[1]`
> whose first vertex is literally the derived base change of `L_{B/A}` along `f`, whose second
> vertex is `L_{C/A}` and whose third vertex is the third vertex of
> `CommAlgCat.cotangentTriangle`, the complex of the base-changed relative differentials.
>
> This statement leaves the third vertex as the complex of base-changed relative differentials. Its
> identification with `L_{C/B}`, and the passage to arbitrary `A → B → C` through `B × C` and Tag
> 08SC, are the two paragraphs of Remark 08SD stated whole in
> `StacksFrontier/Cotangent/Triangle/BaseChangedResolutionTriangle.lean`:
> `CommAlgCat.fundamentalTriangle_of_injective` and
> `CommAlgCat.fundamentalTriangle_of_productDescent`.

```lean
theorem exists_distinguished_derivedBaseChange_cotangentTriangle (A : Type u) [CommRing A]
    {B C : CommAlgCat.{max u v} A} [HasDerivedCategory.{wB} (ModuleCat.{max u v} B)]
    [HasDerivedCategory.{wC} (ModuleCat.{max u v} C)]
    (f : B ⟶ C) (hf : Function.Injective f.hom) :
    ∃ (α : (CochainComplex.DerivedExtensionScalars.derivedExtensionScalarsGeneral
            f.hom.toRingHom).functor.obj
          (DerivedCategory.Q.obj (cotangentComplex.{u, v} A B)) ⟶
        DerivedCategory.Q.obj (cotangentComplex.{u, v} A C))
      (β : DerivedCategory.Q.obj (cotangentComplex.{u, v} A C) ⟶
        (cotangentTriangle A f hf).obj₃)
      (δ : (cotangentTriangle A f hf).obj₃ ⟶
        ((CochainComplex.DerivedExtensionScalars.derivedExtensionScalarsGeneral
            f.hom.toRingHom).functor.obj
          (DerivedCategory.Q.obj (cotangentComplex.{u, v} A B)))⟦(1 : ℤ)⟧),
      Triangle.mk α β δ ∈ distTriang (DerivedCategory (ModuleCat.{max u v} C))
```

**`CommAlgCat.standardResolutionDifferentialSequence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/DifferentialSequence.lean, line 880](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/DifferentialSequence.lean#L880). The attribute's comment: “differential\_sequence construction”.

> The specific canonical differential short complex for `A → B → C`.

```lean
noncomputable def standardResolutionDifferentialSequence
    (A : Type u) [CommRing A] {B C : CommAlgCat.{max u v} A} (f : B ⟶ C) :
    DifferentialSequenceData A f
```

**`CommAlgCat.standardResolution_differentials_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/DifferentialSequence.lean, line 926](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/DifferentialSequence.lean#L926). The attribute's comment: “differential\_sequence”.

> The canonical differential complex is short exact.

```lean
theorem standardResolution_differentials_shortExact
    (A : Type u) [CommRing A] {B C : CommAlgCat.{max u v} A} (f : B ⟶ C)
    (hf : Function.Injective f.hom) :
    (standardResolutionDifferentialSequence A f).complex.ShortExact
```

**`CommAlgCat.standardResolution_differentials_firstMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/DifferentialSequence.lean, line 1004](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/DifferentialSequence.lean#L1004). The attribute's comment: “differential\_sequence first map”.

> The first map sends a differential to the differential of its image.

```lean
theorem standardResolution_differentials_firstMap
    (A : Type u) [CommRing A] {B C : CommAlgCat.{max u v} A} (f : B ⟶ C)
    (n : SimplexCategoryᵒᵖ) (p : (standardResolution A B).left.obj n) :
    let D := standardResolutionDifferentialSequence A f
    ((D.firstIso.inv.app n) ≫ (D.complex.f.app n) ≫ (D.secondIso.hom.app n))
      ((1 : C) ⊗ₜ[B] cotangentTermDifferential A B n p) =
      cotangentTermDifferential A C n
        (((standardResolutionFunctor A).map f).left.app n p)
```

**`CommAlgCat.standardResolution_differentials_secondMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/DifferentialSequence.lean, line 1016](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/DifferentialSequence.lean#L1016). The attribute's comment: “differential\_sequence second map”.

> The second map is the canonical map to base-changed relative differentials.

```lean
theorem standardResolution_differentials_secondMap
    (A : Type u) [CommRing A] {B C : CommAlgCat.{max u v} A} (f : B ⟶ C)
    (n : SimplexCategoryᵒᵖ) (q : (standardResolution A C).left.obj n) :
    let D := standardResolutionDifferentialSequence A f
    let R := baseChangedStandardResolution A f
    let T := R.left.obj n
    letI : Algebra T C := ((R.hom.app n).hom.toRingHom).toAlgebra
    ((D.secondIso.inv.app n) ≫ (D.complex.g.app n) ≫ (D.thirdIso n).hom)
      (cotangentTermDifferential A C n q) =
      ((1 : C) ⊗ₜ[T] KaehlerDifferential.D B T (D.toBaseChange n q))
```

**`CommAlgCat.standardResolution_differentials_third_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/DifferentialSequence.lean, line 1030](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/DifferentialSequence.lean#L1030). The attribute's comment: “differential\_sequence naturality”.

> The identification of the third term respects every simplicial map.

```lean
theorem standardResolution_differentials_third_naturality
    (A : Type u) [CommRing A] {B C : CommAlgCat.{max u v} A} (f : B ⟶ C)
    {i j : SimplexCategoryᵒᵖ} (h : i ⟶ j)
    (t : (baseChangedStandardResolution A f).left.obj
      i) :
    let D := standardResolutionDifferentialSequence A f
    let R := baseChangedStandardResolution A f
    let Ti := R.left.obj i
    let Tj := R.left.obj j
    letI : Algebra Ti C := ((R.hom.app i).hom.toRingHom).toAlgebra
    letI : Algebra Tj C := ((R.hom.app j).hom.toRingHom).toAlgebra
    ((D.thirdIso i).inv ≫ D.complex.X₃.map h ≫ (D.thirdIso j).hom)
      ((1 : C) ⊗ₜ[Ti] KaehlerDifferential.D B Ti t) =
      ((1 : C) ⊗ₜ[Tj] KaehlerDifferential.D B Tj (R.left.map h t))
```

**`CommAlgCat.standardResolution_differentials_pushout`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/DifferentialSequence.lean, line 1048](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/DifferentialSequence.lean#L1048). The attribute's comment: “differential\_sequence base change”.

> The map to the base-changed resolution is its canonical pushout leg.

```lean
theorem standardResolution_differentials_pushout
    (A : Type u) [CommRing A] {B C : CommAlgCat.{max u v} A} (f : B ⟶ C)
    (n : SimplexCategoryᵒᵖ) :
    let D := standardResolutionDifferentialSequence A f
    let R := baseChangedStandardResolution A f
    CategoryTheory.IsPushout
      (CommRingCat.ofHom
        (((standardResolutionFunctor A).map f).left.app n).hom.toRingHom)
      (CommRingCat.ofHom (standardResolutionAugmentationHom A B n))
      (CommRingCat.ofHom (D.toBaseChange n))
      (CommRingCat.ofHom (algebraMap B (R.left.obj n)))
```

**`CommAlgCat.standardResolution_differentials_toBaseChange_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/DifferentialSequence.lean, line 1063](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/DifferentialSequence.lean#L1063). The attribute's comment: “differential\_sequence base change naturality”.

> The pushout leg is simplicially natural.

```lean
theorem standardResolution_differentials_toBaseChange_naturality
    (A : Type u) [CommRing A] {B C : CommAlgCat.{max u v} A} (f : B ⟶ C)
    {i j : SimplexCategoryᵒᵖ} (h : i ⟶ j)
    (q : (standardResolution A C).left.obj i) :
    let D := standardResolutionDifferentialSequence A f
    let R := baseChangedStandardResolution A f
    R.left.map h (D.toBaseChange i q) =
      D.toBaseChange j ((standardResolution A C).left.map h q)
```

**`CommAlgCat.standardResolution_differentials_toBaseChange_augmentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/DifferentialSequence.lean, line 1075](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/DifferentialSequence.lean#L1075). The attribute's comment: “differential\_sequence augmentation”.

> The pushout leg is compatible with augmentation to `C`.

```lean
theorem standardResolution_differentials_toBaseChange_augmentation
    (A : Type u) [CommRing A] {B C : CommAlgCat.{max u v} A} (f : B ⟶ C)
    (n : SimplexCategoryᵒᵖ) :
    let D := standardResolutionDifferentialSequence A f
    let R := baseChangedStandardResolution A f
    ((R.hom.app n).hom.toRingHom).comp (D.toBaseChange n) =
      standardResolutionAugmentationHom A C n
```

**`CommAlgCat.cotangentDifferentialComplexes_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/Distinguished.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/Distinguished.lean#L142). The attribute's comment: “differential\_sequence complexes”.

> For an injective map `f : B ⟶ C` of `A`-algebras, the differential short complex of cochain
> complexes of `C`-modules is short exact.

```lean
theorem cotangentDifferentialComplexes_shortExact (A : Type u) [CommRing A]
    {B C : CommAlgCat.{max u v} A} (f : B ⟶ C) (hf : Function.Injective f.hom) :
    (cotangentDifferentialComplexes A f).ShortExact
```

**`CommAlgCat.cotangentTriangle`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/Distinguished.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/Distinguished.lean#L151). The attribute's comment: “differential\_sequence triangle”.

> The triangle in `D(ModuleCat C)` attached to the differential short exact sequence of the
> standard resolutions of `A → B → C`, for `f : B ⟶ C` injective.

```lean
noncomputable def cotangentTriangle (A : Type u) [CommRing A]
    {B C : CommAlgCat.{max u v} A} [HasDerivedCategory.{t} (ModuleCat.{max u v} C)]
    (f : B ⟶ C) (hf : Function.Injective f.hom) :
    Triangle (DerivedCategory (ModuleCat.{max u v} C))
```

**`CommAlgCat.cotangentTriangle_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/Distinguished.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/Distinguished.lean#L159). The attribute's comment: “differential\_sequence triangle distinguished”.

> The triangle attached to the differential sequence is distinguished.

```lean
theorem cotangentTriangle_distinguished (A : Type u) [CommRing A]
    {B C : CommAlgCat.{max u v} A} [HasDerivedCategory.{t} (ModuleCat.{max u v} C)]
    (f : B ⟶ C) (hf : Function.Injective f.hom) :
    cotangentTriangle A f hf ∈ distTriang (DerivedCategory (ModuleCat.{max u v} C))
```

## Tag 08SE, a remark

[Tag 08SE](https://stacks.math.columbia.edu/tag/08SE) in the Stacks Project.

**`CommAlgCat.relativeBaseChangeLeg`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/BaseChangeComparison.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/BaseChangeComparison.lean#L209). The attribute's comment: “the first arrow of the comparison, R\_bullet ⟶ R\_bullet ⊗\_\{S\_bullet} B”.

> **The canonical map `R_• ⟶ R̄_•`** of Remark 08SE: degreewise the pushout leg out of the
> standard resolution of `C` over `B`.

```lean
noncomputable def relativeBaseChangeLeg (f : B ⟶ C) :
    (standardResolution ↥B (algebraOver f)).left ⟶ (relativeBaseChange f).left
```

**`CommAlgCat.standardResolutionSquareMap_baseRingSquare_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/BaseChangeComparison.lean, line 315](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/BaseChangeComparison.lean#L315). The attribute's comment: “the commutative diagram of standard resolutions from which the canonical map Q\_bullet ⊗\_\{P\_bullet} B ⟶ R\_bullet ⊗\_\{S\_bullet} B is obtained”.

> **The commutative diagram of Remark 08SE.** The square
>
> ```
> Q_•  ⟶  R_•
>  ↑        ↑
> P_•  ⟶  S_•
> ```
>
> commutes, the vertical maps being the functoriality of the standard resolution in the algebra and
> the horizontal ones the change of base ring from `A` to `B`.

```lean
theorem standardResolutionSquareMap_baseRingSquare_comm (f : B ⟶ C) (n : SimplexCategoryᵒᵖ) :
    (standardResolutionSquareMap.{u, u, u} (baseRingSquareTop f) n).comp
        ((((standardResolutionFunctor.{u, u} A).map f).left.app n).hom.toRingHom) =
      ((((standardResolutionFunctor.{u, u} ↥B).map (overBase f)).left.app n).hom.toRingHom).comp
        (standardResolutionSquareMap.{u, u, u} (baseRingSquareBot B) n)
```

**`CommAlgCat.baseChangedComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/BaseChangeComparison.lean, line 415](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/BaseChangeComparison.lean#L415). The attribute's comment: “the canonical map Q\_bullet ⊗\_\{P\_bullet} B ⟶ R\_bullet ⊗\_\{S\_bullet} B obtained from the commutative diagram”.

> **The canonical map `Q̄_• ⟶ R̄_•`** of Remark 08SE, obtained from the commutative diagram of
> standard resolutions by the pushout property of `Q̄_•`.

```lean
noncomputable def baseChangedComparison (f : B ⟶ C) :
    (baseChangedStandardResolution A f).left ⟶ (relativeBaseChange f).left
```

**`CommAlgCat.baseChangedStandardResolution_isPolynomialAlgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/BaseChangeComparison.lean, line 588](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/BaseChangeComparison.lean#L588). The attribute's comment: “the degreewise polynomiality of a base-changed standard resolution, applied in the remark both to Q\_bullet ⊗\_\{P\_bullet} B and to R\_bullet ⊗\_\{S\_bullet} B; this is where the injectivity of B → C is used”.

> **Every term of the base-changed standard resolution `Q̄_• = Q_• ⊗_{P_•} B` is a polynomial
> algebra over `B`, when `B → C` is injective.**
>
> This is the elementary half of the "key fact" of Tag 08SD. Injectivity enters through the
> polynomiality of Tag 08SD, `CommAlgCat.standardResolution_isPolynomialAlgebra`, which presents
> `Q_n` as a polynomial algebra over `P_n`; the base change of that presentation along the
> augmentation `P_n → B` presents `Q̄_n` as a polynomial algebra over `B` on the same variables.

```lean
theorem baseChangedStandardResolution_isPolynomialAlgebra (f : B ⟶ C)
    (hf : Function.Injective f.hom) (n : SimplexCategoryᵒᵖ) :
    IsPolynomialAlgebra ↥B ((baseChangedStandardResolution A f).left.obj n)
```

**`CommAlgCat.relativeBaseChange_isPolynomialAlgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/BaseChangeComparison.lean, line 603](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/BaseChangeComparison.lean#L603). The attribute's comment: “R\_bullet ⊗\_\{S\_bullet} B is a simplicial polynomial algebra over B, because B → C is injective”.

> **Every term of `R̄_• = R_• ⊗_{S_•} B` is a polynomial algebra over `B`**, when `B → C` is
> injective: the functoriality map `S_• → R_•` presents `R_n` as a polynomial algebra over `S_n`, so
> this is `CommAlgCat.baseChangedStandardResolution_isPolynomialAlgebra` at the base ring `B`.

```lean
theorem relativeBaseChange_isPolynomialAlgebra (f : B ⟶ C) (hf : Function.Injective f.hom)
    (n : SimplexCategoryᵒᵖ) :
    IsPolynomialAlgebra ↥B ((relativeBaseChange f).left.obj n)
```

**`CommAlgCat.relativeBaseChangeCotangentLeg`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/BaseChangeComparison.lean, line 649](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/BaseChangeComparison.lean#L649). The attribute's comment: “the induced map L\_\{C/B} = Omega[R\_bullet/B] ⊗ C ⟶ Omega[R\_bullet ⊗\_\{S\_bullet} B / B] ⊗ C”.

> **The first arrow of the comparison of Remark 08SE**, the map
> `L_{C/B} = Ω[R_•⁄B] ⊗_{R_•} C ⟶ Ω[R̄_•⁄B] ⊗_{R̄_•} C` induced by `R_• ⟶ R̄_•`.

```lean
noncomputable def relativeBaseChangeCotangentLeg (f : B ⟶ C) :
    cotangentComplex ↥B (algebraOver f) ⟶
      augmentedCotangentCochainComplex (relativeBaseChange f).hom
```

**`CommAlgCat.baseChangedCotangentComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/BaseChangeComparison.lean, line 660](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/BaseChangeComparison.lean#L660). The attribute's comment: “the induced map Omega[Q\_bullet ⊗\_\{P\_bullet} B / B] ⊗ C ⟶ Omega[R\_bullet ⊗\_\{S\_bullet} B / B] ⊗ C”.

> **The second arrow of the comparison of Remark 08SE**, the map
> `Ω[Q̄_•⁄B] ⊗_{Q̄_•} C ⟶ Ω[R̄_•⁄B] ⊗_{R̄_•} C` induced by `Q̄_• ⟶ R̄_•`.

```lean
noncomputable def baseChangedCotangentComparison (f : B ⟶ C) :
    augmentedCotangentCochainComplex (baseChangedStandardResolution A f).hom ⟶
      augmentedCotangentCochainComplex (relativeBaseChange f).hom
```

**`CommAlgCat.isIso_q_relativeBaseChangeCotangentLeg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/BaseChangeComparison.lean, line 698](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/BaseChangeComparison.lean#L698). The attribute's comment: “the first of the two maps is a quasi-isomorphism. CARRIED as the hypothesis `hεR`: that the augmentation of R\_bullet ⊗\_\{S\_bullet} B to C is a trivial Kan fibration, the half of the source's appeal to Cohomology on Sites, Lemma 21.39.12 (Tag 08RX) that this library lacks. Degreewise polynomiality is NOT carried: it is proved from B → C injective”.

> **The first arrow of the comparison is a quasi-isomorphism.**
>
> Both `R_•` and `R̄_•` are resolutions of `C` over `B`, so by Tag 08PU each of their complexes is
> `Lπ_!(i^*Ω_{𝒪/B})` in `D(C)`, compatibly with the morphism `R_• ⟶ R̄_•` between them
> (`CommAlgCat.smallResolutionCotangentDerivedLowerShriekIso_naturality`).
>
> That `R̄_•` is a resolution is used twice over: its degreewise polynomiality is
> `CommAlgCat.relativeBaseChange_isPolynomialAlgebra`, which consumes the injectivity of `B → C`,
> while the trivial Kan fibration condition `hεR` is carried.

```lean
theorem isIso_q_relativeBaseChangeCotangentLeg (f : B ⟶ C) (hf : Function.Injective f.hom)
    (hεR : SSet.trivialKanFibrations (Functor.whiskerRight (relativeBaseChange f).hom
      (forget (CommAlgCat.{u} ↥B)))) :
    IsIso (DerivedCategory.Q.map (relativeBaseChangeCotangentLeg f))
```

**`CommAlgCat.isIso_q_baseChangedCotangentComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/BaseChangeComparison.lean, line 727](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/BaseChangeComparison.lean#L727). The attribute's comment: “the second of the two maps is a quasi-isomorphism. CARRIED as the hypotheses `hεQ` and `hεR`: that the augmentations of Q\_bullet ⊗\_\{P\_bullet} B and R\_bullet ⊗\_\{S\_bullet} B to C are trivial Kan fibrations, the half of Tag 08RX this library lacks. Degreewise polynomiality of both is NOT carried: it is proved from B → C injective”.

> **The second arrow of the comparison is a quasi-isomorphism**, by Tag 08PU at the two
> resolutions `Q̄_•` and `R̄_•` of `C` over `B` and its functoriality in the resolution.

```lean
theorem isIso_q_baseChangedCotangentComparison (f : B ⟶ C) (hf : Function.Injective f.hom)
    (hεQ : SSet.trivialKanFibrations (Functor.whiskerRight
      (baseChangedStandardResolution A f).hom (forget (CommAlgCat.{u} ↥B))))
    (hεR : SSet.trivialKanFibrations (Functor.whiskerRight (relativeBaseChange f).hom
      (forget (CommAlgCat.{u} ↥B)))) :
    IsIso (DerivedCategory.Q.map (baseChangedCotangentComparison f))
```

**`CommAlgCat.baseChangedCotangentComplexIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/BaseChangeComparison.lean, line 757](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/BaseChangeComparison.lean#L757). The attribute's comment: “the canonical identification of Omega[Q\_bullet ⊗\_\{P\_bullet} B / B] ⊗ C with L\_\{C/B}: the second arrow of the comparison followed by the inverse of the first. CARRIED as the hypotheses `hεQ` and `hεR`, the trivial-Kan-fibration halves of Tag 08RX, which this library lacks. The remark's hypothesis that B → C be injective is NOT carried but consumed”.

> **Remark 08SE.** The canonical identification of `Ω[Q̄_•⁄B] ⊗_{Q̄_•} C` with
> `L_{C/B} = Ω[R_•⁄B] ⊗_{R_•} C` in `D(C)`: the second arrow of the comparison composed with the
> inverse of the first.
>
> It is characterised by `CommAlgCat.baseChangedCotangentComplexIso_hom_comp` and
> `CommAlgCat.eq_baseChangedCotangentComplexIso`.

```lean
noncomputable def baseChangedCotangentComplexIso (f : B ⟶ C) (hf : Function.Injective f.hom)
    (hεQ : SSet.trivialKanFibrations (Functor.whiskerRight
      (baseChangedStandardResolution A f).hom (forget (CommAlgCat.{u} ↥B))))
    (hεR : SSet.trivialKanFibrations (Functor.whiskerRight (relativeBaseChange f).hom
      (forget (CommAlgCat.{u} ↥B)))) :
    DerivedCategory.Q.obj
        (augmentedCotangentCochainComplex (baseChangedStandardResolution A f).hom) ≅
      DerivedCategory.Q.obj (cotangentComplex ↥B (algebraOver f))
```

**`CommAlgCat.baseChangedCotangentComplexIso_hom_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/BaseChangeComparison.lean, line 779](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/BaseChangeComparison.lean#L779). The attribute's comment: “the characterising property of the identification: composed with the first arrow of the comparison it is the second, which is what 'composing one with the inverse of the other' means. Same two carried hypotheses as the identification itself”.

> **The identification of Remark 08SE commutes with the two arrows of the comparison.**

```lean
theorem baseChangedCotangentComplexIso_hom_comp (f : B ⟶ C) (hf : Function.Injective f.hom)
    (hεQ : SSet.trivialKanFibrations (Functor.whiskerRight
      (baseChangedStandardResolution A f).hom (forget (CommAlgCat.{u} ↥B))))
    (hεR : SSet.trivialKanFibrations (Functor.whiskerRight (relativeBaseChange f).hom
      (forget (CommAlgCat.{u} ↥B)))) :
    (baseChangedCotangentComplexIso f hf hεQ hεR).hom ≫
        DerivedCategory.Q.map (relativeBaseChangeCotangentLeg f) =
      DerivedCategory.Q.map (baseChangedCotangentComparison f)
```

**`CommAlgCat.eq_baseChangedCotangentComplexIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/BaseChangeComparison.lean, line 802](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/BaseChangeComparison.lean#L802). The attribute's comment: “uniqueness of the identification: it is the ONLY isomorphism whose composite with the first arrow of the comparison is the second. Same two carried hypotheses as the identification itself”.

> **The identification of Remark 08SE is the unique isomorphism commuting with the two arrows of
> the comparison.** This is what pins it down: the first arrow is an isomorphism in `D(C)`, so the
> commutation determines the identification outright.

```lean
theorem eq_baseChangedCotangentComplexIso (f : B ⟶ C) (hf : Function.Injective f.hom)
    (hεQ : SSet.trivialKanFibrations (Functor.whiskerRight
      (baseChangedStandardResolution A f).hom (forget (CommAlgCat.{u} ↥B))))
    (hεR : SSet.trivialKanFibrations (Functor.whiskerRight (relativeBaseChange f).hom
      (forget (CommAlgCat.{u} ↥B))))
    (e : DerivedCategory.Q.obj
        (augmentedCotangentCochainComplex (baseChangedStandardResolution A f).hom) ≅
      DerivedCategory.Q.obj (cotangentComplex ↥B (algebraOver f)))
    (he : e.hom ≫ DerivedCategory.Q.map (relativeBaseChangeCotangentLeg f) =
      DerivedCategory.Q.map (baseChangedCotangentComparison f)) :
    e = baseChangedCotangentComplexIso f hf hεQ hεR
```

**`CommAlgCat.isResolution_relativeBaseChange_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/BaseChangeComparisonOfInjective.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/BaseChangeComparisonOfInjective.lean#L71). The attribute's comment: “R\_bullet ⊗\_\{S\_bullet} B is a simplicial polynomial algebra over B and R\_bullet ⊗\_\{S\_bullet} B → C is a resolution, for B → C injective”.

> **`R̄_• = R_• ⊗_{S_•} B` is a resolution of `C` over `B`** when `B → C` is injective: each
> `R̄_n` is a polynomial algebra over `B` and the augmentation `R̄_• → C` is a trivial Kan
> fibration. `R̄_•` is the base-changed standard resolution at the base ring `B` and the map
> `CommAlgCat.overBase f`, so this is
> `CommAlgCat.isResolution_baseChangedStandardResolution_of_injective` there.

```lean
theorem isResolution_relativeBaseChange_of_injective (f : B ⟶ C)
    (hf : Function.Injective f.hom) :
    @IsResolution ↥B B.commRing ↥(relativeBaseChange f).right
      (relativeBaseChange f).right.commRing (relativeBaseChange f).right.algebra
      (relativeBaseChange f).left (relativeBaseChange f).hom
```

**`CommAlgCat.isIso_q_relativeBaseChangeCotangentLeg_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/BaseChangeComparisonOfInjective.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/BaseChangeComparisonOfInjective.lean#L83). The attribute's comment: “the map L\_\{C/B} = Omega[R\_bullet/B] ⊗ C ⟶ Omega[R\_bullet ⊗\_\{S\_bullet} B / B] ⊗ C is a quasi-isomorphism, for B → C injective”.

> **The first map of Remark 08SE is a quasi-isomorphism**:
> `L_{C/B} = Ω[R_•⁄B] ⊗_{R_•} C ⟶ Ω[R̄_•⁄B] ⊗_{R̄_•} C` becomes an isomorphism in `D(C)` for
> `B → C` injective.

```lean
theorem isIso_q_relativeBaseChangeCotangentLeg_of_injective (f : B ⟶ C)
    (hf : Function.Injective f.hom) :
    IsIso (DerivedCategory.Q.map (relativeBaseChangeCotangentLeg f))
```

**`CommAlgCat.isIso_q_baseChangedCotangentComparison_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/BaseChangeComparisonOfInjective.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/BaseChangeComparisonOfInjective.lean#L94). The attribute's comment: “the map Omega[Q\_bullet ⊗\_\{P\_bullet} B / B] ⊗ C ⟶ Omega[R\_bullet ⊗\_\{S\_bullet} B / B] ⊗ C is a quasi-isomorphism, for B → C injective”.

> **The second map of Remark 08SE is a quasi-isomorphism**:
> `Ω[Q̄_•⁄B] ⊗_{Q̄_•} C ⟶ Ω[R̄_•⁄B] ⊗_{R̄_•} C` becomes an isomorphism in `D(C)` for `B → C`
> injective.

```lean
theorem isIso_q_baseChangedCotangentComparison_of_injective (f : B ⟶ C)
    (hf : Function.Injective f.hom) :
    IsIso (DerivedCategory.Q.map (baseChangedCotangentComparison f))
```

**`CommAlgCat.baseChangedCotangentComplexIsoOfInjective_hom_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/BaseChangeComparisonOfInjective.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/BaseChangeComparisonOfInjective.lean#L110). The attribute's comment: “the identification composed with the first map of the comparison is the second, for B → C injective”.

> **The identification of Remark 08SE is the second map composed with the inverse of the
> first**: followed by the first map it is the second.

```lean
theorem baseChangedCotangentComplexIsoOfInjective_hom_comp (f : B ⟶ C)
    (hf : Function.Injective f.hom) :
    (baseChangedCotangentComplexIsoOfInjective f hf).hom ≫
        DerivedCategory.Q.map (relativeBaseChangeCotangentLeg f) =
      DerivedCategory.Q.map (baseChangedCotangentComparison f)
```

**`CommAlgCat.eq_baseChangedCotangentComplexIsoOfInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/BaseChangeComparisonOfInjective.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/BaseChangeComparisonOfInjective.lean#L122). The attribute's comment: “uniqueness of the identification: the only isomorphism whose composite with the first map of the comparison is the second, for B → C injective”.

> **The identification of Remark 08SE is canonical**: it is the only isomorphism
> `Ω[Q̄_•⁄B] ⊗_{Q̄_•} C ≅ L_{C/B}` in `D(C)` whose composite with the first map of the comparison is
> the second.

```lean
theorem eq_baseChangedCotangentComplexIsoOfInjective (f : B ⟶ C)
    (hf : Function.Injective f.hom)
    (e : DerivedCategory.Q.obj
        (augmentedCotangentCochainComplex (baseChangedStandardResolution A f).hom) ≅
      DerivedCategory.Q.obj (cotangentComplex ↥B (algebraOver f)))
    (he : e.hom ≫ DerivedCategory.Q.map (relativeBaseChangeCotangentLeg f) =
      DerivedCategory.Q.map (baseChangedCotangentComparison f)) :
    e = baseChangedCotangentComplexIsoOfInjective f hf
```

Declarations registered for the tag:

- [`CommAlgCat.baseChangedCotangentComplexIsoOfInjective`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/BaseChangeLegTensor.lean#L418), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Cotangent/Triangle/BaseChangeComparisonOfInjective.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Triangle/BaseChangeComparisonOfInjective.lean#L101) (StacksFrontier): “the canonical identification of Omega[Q\_bullet ⊗\_\{P\_bullet} B / B] ⊗ C with L\_\{C/B} = Omega[R\_bullet/B] ⊗ C in D(C), for B → C injective: the second map of the comparison followed by the inverse of the first”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 92.7, Tag 08QR](https://stacks.math.columbia.edu/tag/08QR)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
