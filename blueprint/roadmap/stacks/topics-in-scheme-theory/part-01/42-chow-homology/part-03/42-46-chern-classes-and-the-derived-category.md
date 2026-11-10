---
declaration: section
origin: cited
lean: Stacks.Chow.totalChernClassComplex, Stacks.Chow.totalChernClassComplex_eq_prod, Stacks.Chow.totalChernClassComplex_eq_of_cohomologyComparison, Stacks.Chow.powerSumClassComplex, Stacks.Chow.powerSumClassComplex_eq_sum, Stacks.Chow.powerSumClassComplex_eq_of_cohomologyComparison, Stacks.Chow.chernCharacterComplexComponent, Stacks.Chow.chernCharacterComplexComponent_eq_of_cohomologyComparison
statement: formalized
proof: formalized
---

# 42.46 Chern classes and the derived category

Section 42.46 of the Stacks Project, [Tag 0ESY](https://stacks.math.columbia.edu/tag/0ESY). 11 tags here are carried by 75 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0ESZ, a lemma

[Tag 0ESZ](https://stacks.math.columbia.edu/tag/0ESZ) in the Stacks Project.

**`Stacks.Chow.totalChernClassComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassComplex.lean, line 554](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassComplex.lean#L554). The attribute's comment: “the total Chern class c(E^bullet) of a complex of finite locally free modules bounded in a range of degrees, with no constant-rank hypothesis; the total Chern class of a module, Tag 0B7H, and the multiplication of A^*(X), Tag 0FE0, are carried as the parameters R and D, whose field ch_shortExact is the Whitney sum formula of Tag 02UI, exactly as in Stacks.Chow.chernClassKGroup; the locally bounded case is not delivered”.

> **Stacks 0ESZ.** The total Chern class `c(ℰ^•) = ∏_n c(ℰ^n)^{(-1)^n}` of a complex of finite
> locally free modules bounded in the degrees `a, …, a + k`, as an element of the group of series
> with constant term `1` inside `∏_{p ≥ 0} A^p(X)`; the negative exponents are the formal inverses
> of Stacks 0FEL. No rank is assumed constant.

```lean
def totalChernClassComplex (D : TotalChernClassSeries C Gy sX R)
    (P : CochainComplex X.Modules ℤ) (a : ℤ) (k : ℕ) : UnitalSeries R
```

**`Stacks.Chow.totalChernClassComplex_eq_prod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassComplex.lean, line 563](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassComplex.lean#L563). The attribute's comment: “the defining formula c(E^bullet) = prod_n c(E^n)^{(-1)^n} of the section, the inverses being the formal inverses of Tag 0FEL”.

> **Stacks 0ESZ.** The total Chern class of a complex is the alternating product
> `∏_n c(ℰ^n)^{(-1)^n}` of the total Chern classes of its terms, which is the formula of the
> source.

```lean
theorem totalChernClassComplex_eq_prod (D : TotalChernClassSeries C Gy sX R)
    (P : CochainComplex X.Modules ℤ) (a : ℤ) (k : ℕ) :
    totalChernClassComplex C Gy sX D P a k =
      ∏ i ∈ Finset.range (k + 1),
        (⟨D.ch (P.X (a + (i : ℤ))), D.ch_apply_zero (P.X (a + (i : ℤ)))⟩ : UnitalSeries R) ^
          ((a + (i : ℤ)).negOnePow : ℤ)
```

**`Stacks.Chow.totalChernClassComplex_eq_of_cohomologyComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassComplex.lean, line 582](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassComplex.lean#L582). The attribute's comment: “the independence of the representative for the total Chern class. CARRIED: the degreewise data the source's proof extracts from an isomorphism in D(O_X) -- finite local freeness of the kernels and images (Tag 0F8J), the identification of the cohomology modules, and Schanuel's lemma (Tag 00O3) -- together with the reductions of Tags 02UC and 0ESR”.

> **Stacks 0ESZ.** The total Chern class of a complex of finite locally free modules depends
> only on the cohomology modules of the complex. Two complexes representing the same object of
> `D(𝒪_X)` have the same cohomology modules, and this is the form in which the independence of the
> representative is delivered here; see the implementation notes of this file.

```lean
theorem totalChernClassComplex_eq_of_cohomologyComparison (D : TotalChernClassSeries C Gy sX R)
    {P Q : CochainComplex X.Modules ℤ} {a : ℤ} {k : ℕ}
    (S : BoundedComplexSplitting X P a k) (T : BoundedComplexSplitting X Q a k)
    (cmp : ComplexCohomologyComparison S T) :
    totalChernClassComplex C Gy sX D P a k = totalChernClassComplex C Gy sX D Q a k
```

**`Stacks.Chow.powerSumClassComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassComplex.lean, line 645](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassComplex.lean#L645). The attribute's comment: “the class P_p(E^bullet) of a complex of finite locally free modules bounded in a range of degrees, with no constant-rank hypothesis; the constant-rank power sums P_p(E) of Tag 0F9B and their additivity, Tag 0F9C, are carried as the parameter W, as in Stacks.Chow.powerSumClassArbitraryRank; the locally bounded case is not delivered”.

> **Stacks 0ESZ.** The class `P_p(ℰ^•) = ∑_n (-1)^n P_p(ℰ^n) ∈ A^p(X)` of a complex of finite
> locally free modules bounded in the degrees `a, …, a + k`. No rank is assumed constant.

```lean
def powerSumClassComplex (W : PowerSumClassRule C Gy sX) (P : CochainComplex X.Modules ℤ)
    (a : ℤ) (k : ℕ) (p : ℕ) : chowCohomologyComponent C Gy sX (p : ℤ)
```

**`Stacks.Chow.powerSumClassComplex_eq_sum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassComplex.lean, line 652](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassComplex.lean#L652). The attribute's comment: “the defining formula P_p(E^bullet) = sum_n (-1)^n P_p(E^n) of the section”.

> **Stacks 0ESZ.** The class `P_p` of a complex is the alternating sum of the classes `P_p` of
> its terms, which is the formula of the source.

```lean
theorem powerSumClassComplex_eq_sum (W : PowerSumClassRule C Gy sX)
    (P : CochainComplex X.Modules ℤ) (a : ℤ) (k : ℕ) (p : ℕ) :
    powerSumClassComplex C Gy sX W P a k p =
      ∑ i ∈ Finset.range (k + 1),
        ((a + (i : ℤ)).negOnePow : ℤ) • W.cls (P.X (a + (i : ℤ))) p
```

**`Stacks.Chow.powerSumClassComplex_eq_of_cohomologyComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassComplex.lean, line 669](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassComplex.lean#L669). The attribute's comment: “the independence of the representative for P_p. CARRIED: the degreewise data the source's proof extracts from an isomorphism in D(O_X) -- finite local freeness of the kernels and images (Tag 0F8J), the identification of the cohomology modules, and Schanuel's lemma (Tag 00O3) -- together with the reductions of Tags 02UC and 0ESR”.

> **Stacks 0ESZ.** The class `P_p` of a complex of finite locally free modules depends only on
> the cohomology modules of the complex. Two complexes representing the same object of `D(𝒪_X)`
> have the same cohomology modules, and this is the form in which the independence of the
> representative is delivered here; see the implementation notes of this file.

```lean
theorem powerSumClassComplex_eq_of_cohomologyComparison (W : PowerSumClassRule C Gy sX)
    {P Q : CochainComplex X.Modules ℤ} {a : ℤ} {k : ℕ}
    (S : BoundedComplexSplitting X P a k) (T : BoundedComplexSplitting X Q a k)
    (cmp : ComplexCohomologyComparison S T) (p : ℕ) :
    powerSumClassComplex C Gy sX W P a k p = powerSumClassComplex C Gy sX W Q a k p
```

**`Stacks.Chow.chernCharacterComplexComponent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassComplex.lean, line 683](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassComplex.lean#L683). The attribute's comment: “the Chern character component ch_p(E^bullet) = P_p(E^bullet)/p! of a complex of finite locally free modules bounded in a range of degrees, with no constant-rank hypothesis; the constant-rank power sums and their additivity, Tag 0F9C, are carried as the parameter W; the locally bounded case is not delivered”.

> **Stacks 0ESZ.** The degree-`p` component `ch_p(ℰ^•) = P_p(ℰ^•)/p! ∈ A^p(X) ⊗ 𝐐` of the Chern
> character of a complex of finite locally free modules bounded in the degrees `a, …, a + k`.

```lean
def chernCharacterComplexComponent (W : PowerSumClassRule C Gy sX)
    (P : CochainComplex X.Modules ℤ) (a : ℤ) (k : ℕ) (p : ℕ) :
    rationalChowCohomologyComponent C Gy sX (p : ℤ)
```

**`Stacks.Chow.chernCharacterComplexComponent_eq_of_cohomologyComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassComplex.lean, line 696](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassComplex.lean#L696). The attribute's comment: “the independence of the representative for the Chern character. CARRIED: the degreewise data the source's proof extracts from an isomorphism in D(O_X) -- finite local freeness of the kernels and images (Tag 0F8J), the identification of the cohomology modules, and Schanuel's lemma (Tag 00O3) -- together with the reductions of Tags 02UC and 0ESR”.

> **Stacks 0ESZ.** The Chern character of a complex of finite locally free modules depends only
> on the cohomology modules of the complex. Two complexes representing the same object of `D(𝒪_X)`
> have the same cohomology modules, and this is the form in which the independence of the
> representative is delivered here; see the implementation notes of this file.

```lean
theorem chernCharacterComplexComponent_eq_of_cohomologyComparison (W : PowerSumClassRule C Gy sX)
    {P Q : CochainComplex X.Modules ℤ} {a : ℤ} {k : ℕ}
    (S : BoundedComplexSplitting X P a k) (T : BoundedComplexSplitting X Q a k)
    (cmp : ComplexCohomologyComparison S T) (p : ℕ) :
    chernCharacterComplexComponent C Gy sX W P a k p =
      chernCharacterComplexComponent C Gy sX W Q a k p
```

**`Stacks.Chow.totalChernClassComplexLocallyBounded`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassComplexLocallyBounded.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassComplexLocallyBounded.lean#L137). The attribute's comment: “the locally bounded case, on a quasi-compact scheme: the total Chern class of a locally bounded complex of finite locally free modules, which the bounded-window construction of this tag in Stacks.Chow.ChernClassComplex does not deliver; the total Chern class of a module (Tag 0B7H) and the multiplication of A^*(X) (Tag 0FE0) are carried as the parameters R and D exactly as there”.

> **Stacks 0ESZ.** The total Chern class `c(ℰ^•) = ∏_n c(ℰ^n)^{(-1)^n}` of a *locally bounded*
> complex of finite locally free modules on a quasi-compact scheme, as an element of the group of
> series with constant term `1` inside `∏_{p ≥ 0} A^p(X)`. Such a complex vanishes outside a single
> global window of degrees, and the class is the bounded-window class of Stacks 0ESZ on one.

```lean
def totalChernClassComplexLocallyBounded (D : TotalChernClassSeries C Gy sX R)
    (P : CochainComplex X.Modules ℤ) (hP : IsLocallyBoundedFiniteLocallyFree P) :
    UnitalSeries R
```

**`Stacks.Chow.powerSumClassComplexLocallyBounded`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassComplexLocallyBounded.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassComplexLocallyBounded.lean#L174). The attribute's comment: “the locally bounded case, on a quasi-compact scheme: the class P_p of a locally bounded complex of finite locally free modules, which the bounded-window construction of this tag in Stacks.Chow.ChernClassComplex does not deliver; the constant-rank power sums P_p(E) of Tag 0F9B and their additivity, Tag 0F9C, are carried as the parameter W exactly as there”.

> **Stacks 0ESZ.** The class `P_p(ℰ^•) = ∑_n (-1)^n P_p(ℰ^n) ∈ A^p(X)` of a *locally bounded*
> complex of finite locally free modules on a quasi-compact scheme. Such a complex vanishes outside
> a single global window of degrees, and the class is the bounded-window class of Stacks 0ESZ on
> one.

```lean
def powerSumClassComplexLocallyBounded (W : PowerSumClassRule C Gy sX)
    (P : CochainComplex X.Modules ℤ) (hP : IsLocallyBoundedFiniteLocallyFree P) (p : ℕ) :
    chowCohomologyComponent C Gy sX (p : ℤ)
```

**`Stacks.Chow.complexChern`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/ComplexChernClass.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/ComplexChernClass.lean#L186). The attribute's comment: “the class c(E^bullet) in prod_{p >= 0} A^p(Y) of a locally bounded complex of finite locally free modules -- the generalization the lemma refers to: no rank is assumed constant, the complex is only locally bounded, and Y is not assumed quasi-compact”.

> **The total Chern class of a locally bounded complex of finite locally free modules.** On the
> rank locus `Y_ρ` the complex is bounded with constant ranks `ρ`, and there the class is
> `c(P|_{Y_ρ}) = ∏_n c(P^n|_{Y_ρ})^{(-1)^n}`; these classes are assembled into a total class on `Y`
> by Stacks 0FDZ in every degree.

```lean
def complexChern : TotalChowClass C sY
```

**`Stacks.Chow.complexPowerSumComponent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/DerivedChernClasses.lean, line 425](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/DerivedChernClasses.lean#L425). The attribute's comment: “the class P_p(E^bullet) in A^p(Y) of a locally bounded complex of finite locally free modules, as the universal power sum of Tag 0F9B applied to c(E^bullet) -- the degree-zero member being the alternating rank class”.

> **The class `P_p(ℰ^•) ∈ A^p(Y)`**, the degree-`p` component of
> `Stacks.Chow.complexPowerSum`.

```lean
def complexPowerSumComponent (p : ℕ) :
    chowCohomologyComponent C (gysinSystemOfInvertible C) sY (p : ℤ)
```

**`Stacks.Chow.complexChernCharacter`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/DerivedChernClasses.lean, line 446](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/DerivedChernClasses.lean#L446). The attribute's comment: “the class ch(E^bullet) in prod_{p >= 0} (A^p(Y) tensor Q) of a locally bounded complex of finite locally free modules, componentwise as ch_p = P_p/p! as the source reads it”.

> **The Chern character `ch(ℰ^•) ∈ ∏_{p ≥ 0} (A^p(Y) ⊗ 𝐐)` of a locally bounded complex of
> finite locally free modules**, the family of its components.

```lean
def complexChernCharacter : fullRationalChowCohomology C (gysinSystemOfInvertible C) sY
```

**`Stacks.Chow.complexPowerSumComponent_eq_of_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/DerivedChernClasses.lean, line 478](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/DerivedChernClasses.lean#L478). The attribute's comment: “the independence of the choice of the complex for P_p(E^bullet) in A^p(Y)”.

> **Stacks 0ESZ for `P_p ∈ A^p(Y)`.**

```lean
theorem complexPowerSumComponent_eq_of_iso
    (e : DerivedCategory.Q.obj P ≅ DerivedCategory.Q.obj P') (p : ℕ) :
    complexPowerSumComponent C sY hP p = complexPowerSumComponent C sY hP' p
```

**`Stacks.Chow.complexChernCharacter_eq_of_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/DerivedChernClasses.lean, line 497](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/DerivedChernClasses.lean#L497). The attribute's comment: “the independence of the choice of the complex for ch(E^bullet)”.

> **Stacks 0ESZ for the Chern character**, as the family
> `ch(ℰ^•) ∈ ∏_{p ≥ 0} (A^p(Y) ⊗ 𝐐)`.

```lean
theorem complexChernCharacter_eq_of_iso
    (e : DerivedCategory.Q.obj P ≅ DerivedCategory.Q.obj P') :
    complexChernCharacter C sY hP = complexChernCharacter C sY hP'
```

**`Stacks.Chow.complexChern_eq_of_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/Independence.lean, line 282](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/Independence.lean#L282). The attribute's comment: “the independence of the choice of the complex for c(E^bullet), at the hypotheses of the source: two locally bounded complexes of finite locally free modules representing one object of D(O_Y), no rank assumed constant and Y not assumed quasi-compact”.

> **Stacks 0ESZ for the total Chern class.** Let `Y` be locally of finite type over the base of
> chapter 42 and let `P`, `P'` be locally bounded complexes of finite locally free `𝒪_Y`-modules
> representing the same object of `D(𝒪_Y)`. Then their total Chern classes
> `c(P), c(P') ∈ ∏_{p ≥ 0} A^p(Y)` are equal.
>
> The proof is the source's. By Stacks 02UC it suffices to compare the operations of the two
> classes on the fundamental class of a proper birational modification of every integral scheme `T`
> locally of finite type over `Y` (`Stacks.Chow.TotalChowClass.eq_of_op_fundamentalChowClass_eq`).
> Over `T` the pulled-back complexes are bounded with constant ranks, after the admissible blowup of
> Stacks 0ESR the cohomology of the pulled-back object is perfect of Tor dimension at most one, and
> there the two classes agree by Stacks 0F8J, Schanuel's lemma and the Whitney sum formula
> (`Stacks.Chow.exists_isBirational_op_complexChern_eq_of_iso`).

```lean
theorem complexChern_eq_of_iso (e : DerivedCategory.Q.obj P ≅ DerivedCategory.Q.obj P') :
    complexChern C sY hP = complexChern C sY hP'
```

**`Stacks.Chow.powerSumComplex_eq_of_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PowerSumIndependence.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PowerSumIndependence.lean#L208). The attribute's comment: “the classes P_p(E^bullet) of a locally bounded complex of finite locally free modules, ranks varying, depend only on its object of D(O_Y)”.

> Let `P`, `P'` be locally bounded complexes of finite locally free `𝒪_Y`-modules representing
> the same object of `D(𝒪_Y)`. Then `P_p(P) = P_p(P') ∈ A^p(Y)` for every `p`.

```lean
theorem powerSumComplex_eq_of_iso (e : DerivedCategory.Q.obj P ≅ DerivedCategory.Q.obj P')
    (p : ℕ) : powerSumComplex C sY hP p = powerSumComplex C sY hP' p
```

**`Stacks.Chow.chernCharacterComplex_eq_of_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PowerSumIndependence.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PowerSumIndependence.lean#L219). The attribute's comment: “the Chern character ch(E^bullet) = sum_p P_p(E^bullet)/p! of a locally bounded complex of finite locally free modules, ranks varying, depends only on its object of D(O_Y)”.

> `ch_p(P) = ch_p(P') ∈ A^p(Y) ⊗ 𝐐` for locally bounded complexes `P`, `P'` of finite locally
> free modules representing the same object of `D(𝒪_Y)`.

```lean
theorem chernCharacterComplex_eq_of_iso (e : DerivedCategory.Q.obj P ≅ DerivedCategory.Q.obj P')
    (p : ℕ) : chernCharacterComplex C sY hP p = chernCharacterComplex C sY hP' p
```

## Tag 0GUD, a lemma

[Tag 0GUD](https://stacks.math.columbia.edu/tag/0GUD) in the Stacks Project.

**`Stacks.Chow.eq_of_restriction_eq_totalChernClassComplexLocallyBounded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/EnvelopeUniqueness.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/EnvelopeUniqueness.lean#L216). The attribute's comment: “the uniqueness half for the total Chern class c(E), read on the coefficients of the series of Tag 0ESZ; the existence of the classes is not constructed here, and the hypothesis is taken at one envelope presentation rather than at all of them, which is stronger”.

> **Stacks 0GUD, uniqueness for the total Chern class.** Let `E` be an object of `D(𝒪_X)` and
> let `H` be an envelope presentation of it, Stacks 0F9E (1), whose source is quasi-compact. Two
> families `c, d` of Chow cohomology classes of `X` whose restrictions along the envelope of `H`
> are the coefficients of the total Chern class `c(P)` of the presenting complex are equal.
>
> The existence of such a family is **not** proved: see the implementation notes of this file. The
> hypothesis is taken at the single presentation `H` rather than at every presentation of `E`, so
> this is stronger than the uniqueness clause of the tag.

```lean
theorem eq_of_restriction_eq_totalChernClassComplexLocallyBounded
    (H : EnvelopePresentation E) [LocallyOfFiniteType H.f] [CompactSpace H.Y]
    {R : ChowCohomologySeriesRing C G (H.f ≫ sX)} (D : TotalChernClassSeries C G (H.f ≫ sX) R)
    {c d : ∀ p : ℕ, chowCohomologyComponent C G sX (p : ℤ)}
    (hc : ∀ p : ℕ, chowCohomologyRestriction C G sX H.f (p : ℤ) hgys (c p) =
      (totalChernClassComplexLocallyBounded C G (H.f ≫ sX) D H.P H.locallyBounded).1 p)
    (hd : ∀ p : ℕ, chowCohomologyRestriction C G sX H.f (p : ℤ) hgys (d p) =
      (totalChernClassComplexLocallyBounded C G (H.f ≫ sX) D H.P H.locallyBounded).1 p) :
    c = d
```

**`Stacks.Chow.eq_of_restriction_eq_powerSumClassComplexLocallyBounded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/EnvelopeUniqueness.lean, line 240](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/EnvelopeUniqueness.lean#L240). The attribute's comment: “the uniqueness half for the power sums P_p(E), the classes of Tag 0ESZ; the existence of the classes is not constructed here, and the hypothesis is taken at one envelope presentation rather than at all of them, which is stronger”.

> **Stacks 0GUD, uniqueness for the power sums.** Let `E` be an object of `D(𝒪_X)` and let `H`
> be an envelope presentation of it, Stacks 0F9E (1), whose source is quasi-compact. Two families
> `c, d` of Chow cohomology classes of `X` whose restrictions along the envelope of `H` are the
> classes `P_p(P)` of the presenting complex are equal.
>
> The existence of such a family is **not** proved: see the implementation notes of this file. The
> hypothesis is taken at the single presentation `H` rather than at every presentation of `E`, so
> this is stronger than the uniqueness clause of the tag.

```lean
theorem eq_of_restriction_eq_powerSumClassComplexLocallyBounded
    (H : EnvelopePresentation E) [LocallyOfFiniteType H.f] [CompactSpace H.Y]
    (W : PowerSumClassRule C G (H.f ≫ sX))
    {c d : ∀ p : ℕ, chowCohomologyComponent C G sX (p : ℤ)}
    (hc : ∀ p : ℕ, chowCohomologyRestriction C G sX H.f (p : ℤ) hgys (c p) =
      powerSumClassComplexLocallyBounded C G (H.f ≫ sX) W H.P H.locallyBounded p)
    (hd : ∀ p : ℕ, chowCohomologyRestriction C G sX H.f (p : ℤ) hgys (d p) =
      powerSumClassComplexLocallyBounded C G (H.f ≫ sX) W H.P H.locallyBounded p) :
    c = d
```

**`Stacks.Chow.eq_of_restriction_eq_chernCharacterComplexLocallyBounded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/EnvelopeUniqueness.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/EnvelopeUniqueness.lean#L266). The attribute's comment: “the uniqueness half for the Chern character ch(E), read componentwise as ch_p = P_p/p! with the classes P_p of Tag 0ESZ; the existence of the classes is not constructed here, and the hypothesis is taken at one envelope presentation rather than at all of them, which is stronger”.

> **Stacks 0GUD, uniqueness for the Chern character.** Let `E` be an object of `D(𝒪_X)` and let
> `H` be an envelope presentation of it, Stacks 0F9E (1), whose source is quasi-compact. Two
> families `c, d` of rational Chow cohomology classes of `X` whose restrictions along the envelope
> of `H` are the components `ch_p(P) = P_p(P)/p!` of the Chern character of the presenting complex
> are equal.
>
> The existence of such a family is **not** proved: see the implementation notes of this file. The
> hypothesis is taken at the single presentation `H` rather than at every presentation of `E`, so
> this is stronger than the uniqueness clause of the tag.

```lean
theorem eq_of_restriction_eq_chernCharacterComplexLocallyBounded
    (H : EnvelopePresentation E) [LocallyOfFiniteType H.f] [CompactSpace H.Y]
    (W : PowerSumClassRule C G (H.f ≫ sX))
    {c d : ∀ p : ℕ, rationalChowCohomologyComponent C G sX (p : ℤ)}
    (hc : ∀ p : ℕ, rationalChowCohomologyRestriction C G sX H.f (p : ℤ) hgys (c p) =
      ((Nat.factorial p : ℚ)⁻¹) ⊗ₜ[ℤ]
        powerSumClassComplexLocallyBounded C G (H.f ≫ sX) W H.P H.locallyBounded p)
    (hd : ∀ p : ℕ, rationalChowCohomologyRestriction C G sX H.f (p : ℤ) hgys (d p) =
      ((Nat.factorial p : ℚ)⁻¹) ⊗ₜ[ℤ]
        powerSumClassComplexLocallyBounded C G (H.f ≫ sX) W H.P H.locallyBounded p) :
    c = d
```

**`Stacks.Chow.existsUnique_perfectPowerSum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectPowerSum.lean, line 274](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectPowerSum.lean#L274). The attribute's comment: “P_p(E): the unique class of A^p(X) restricting along the envelope of every presentation (f, E^bullet) of E to P_p(E^bullet), independent of f and E^bullet”.

> **Uniqueness of the power sums.** Let `E` be a perfect object of `D(𝒪_X)` whose Chern
> classes are defined. For every `p` there is a unique class `P_p(E) ∈ A^p(X)` whose restriction
> along the envelope `f : Y ⟶ X` of every presentation `(f, 𝓔^•)` of `E` is the class `P_p(𝓔^•)`
> of Lemma 0ESZ, which on the locus where the terms have constant ranks is `∑ (-1)^n P_p(𝓔^n)`
> (`Stacks.Chow.res_complexPowerSum_complexRankLocus`). The class is
> `Stacks.Chow.perfectPowerSumComponent`.

```lean
theorem existsUnique_perfectPowerSum (p : ℕ) :
    ∃! x : chowCohomologyComponent C (gysinSystemOfInvertible C) sX (p : ℤ),
      ∀ H : EnvelopePresentation E,
        chowCohomologyRestriction C (gysinSystemOfInvertible C) sX H.f (p : ℤ)
            (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso C) x =
          complexPowerSumComponent C (H.f ≫ sX) H.locallyBounded p
```

**`Stacks.Chow.existsUnique_perfectChernCharacter`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectPowerSum.lean, line 341](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectPowerSum.lean#L341). The attribute's comment: “ch(E): for every p the unique class of A^p(X) ⊗ Q restricting along the envelope of every presentation (f, E^bullet) of E to ch_p(E^bullet) = P_p(E^bullet)/p!, independent of f and E^bullet”.

> **Uniqueness of the Chern character.** Let `E` be a perfect object of `D(𝒪_X)` whose Chern
> classes are defined. For every `p` there is a unique class `ch_p(E) ∈ A^p(X) ⊗ 𝐐` whose rational
> restriction along the envelope `f : Y ⟶ X` of every presentation `(f, 𝓔^•)` of `E` is the
> component `ch_p(𝓔^•) = P_p(𝓔^•)/p!` of the Chern character of `𝓔^•` (Lemma 0ESZ). The class is
> `Stacks.Chow.perfectChernCharacterComponent`, and the family `(ch_p(E))_p` is
> `ch(E) ∈ ∏_{p ≥ 0} A^p(X) ⊗ 𝐐`.

```lean
theorem existsUnique_perfectChernCharacter (p : ℕ) :
    ∃! x : rationalChowCohomologyComponent C (gysinSystemOfInvertible C) sX (p : ℤ),
      ∀ H : EnvelopePresentation E,
        rationalChowCohomologyRestriction C (gysinSystemOfInvertible C) sX H.f (p : ℤ)
            (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso C) x =
          complexChernCharacterComponent C (H.f ≫ sX) H.locallyBounded p
```

Declarations registered for the tag:

- [`Stacks.Chow.existsUnique_forall_res_eq_complexChern`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/EnvelopeChern.lean#L251), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectPowerSum.lean, line 359](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectPowerSum.lean#L359) (StacksFrontier): “c(E): the unique class of the product of the A^p(X), p ≥ 0, restricting along the envelope of every presentation (f, E^bullet) of E to c(E^bullet), independent of f and E^bullet”.

## Tag 0F9E, a definition

[Tag 0F9E](https://stacks.math.columbia.edu/tag/0F9E) in the Stacks Project.

**`Stacks.Chow.HasDefinedChernClasses`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/Defined.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/Defined.lean#L80). The attribute's comment: “clause (1): the condition under which the Chern classes of a perfect object are defined”.

> **Stacks 0F9E (1).** The Chern classes of an object `E` of `D(𝒪_X)` are **defined** when
> some envelope `f : Y ⟶ X` has `Lf^*E` isomorphic to a locally bounded complex of finite locally
> free `𝒪_Y`-modules.

```lean
def HasDefinedChernClasses {X : Scheme.{u}} (E : DerivedCategory X.Modules) : Prop
```

**`Stacks.Chow.perfectPowerSumComponent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/DerivedChernClasses.lean, line 600](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/DerivedChernClasses.lean#L600). The attribute's comment: “clause (2), the class P_p(E) in A^p(X): the universal power sum of Tag 0F9B applied to c(E), with the alternating rank class r(E) as its degree-zero member. It restricts to P_p(E^bullet) along the envelope of every presentation, which is the property Tag 0GUD defines it by (Stacks.Chow.res_perfectPowerSumComponent)”.

> **The class `P_p(E) ∈ A^p(X)`** of Stacks 0F9E (2), the degree-`p` component of
> `Stacks.Chow.perfectPowerSum`.

```lean
def perfectPowerSumComponent (hE : HasDefinedChernClasses E) (p : ℕ) :
    chowCohomologyComponent C (gysinSystemOfInvertible C) sX (p : ℤ)
```

**`Stacks.Chow.perfectChernCharacter`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/DerivedChernClasses.lean, line 619](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/DerivedChernClasses.lean#L619). The attribute's comment: “clause (2), the class ch(E) in prod_{p >= 0} (A^p(X) tensor Q), componentwise as ch_p(E) = P_p(E)/p! as the source reads it”.

> **The Chern character `ch(E) ∈ ∏_{p ≥ 0} (A^p(X) ⊗ 𝐐)` of a perfect object whose Chern
> classes are defined**, Stacks 0F9E (2), the family of its components.

```lean
def perfectChernCharacter (hE : HasDefinedChernClasses E) :
    fullRationalChowCohomology C (gysinSystemOfInvertible C) sX
```

**`Stacks.Chow.perfectChernClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/EnvelopeChern.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/EnvelopeChern.lean#L210). The attribute's comment: “clause (2) for c(E): the class c(E) in prod_{p >= 0} A^p(X), carrying c_p(E) in degree p, for an object of D(O_X) whose Chern classes are defined in the sense of clause (1). Stacks.Chow.res_perfectChernClass pins it down at every envelope presentation, which is how Lemma 0GUD characterizes it. The two further classes clause (2) names are ch(E) (Stacks.Chow.perfectChernCharacter) and P_p(E) (Stacks.Chow.perfectPowerSumComponent)”.

> **The total Chern class `c(E)` of an object whose Chern classes are defined**, Stacks 0F9E
> (2): the class of Stacks 0GUD, the unique total class of `X` whose restriction along the envelope
> of a presentation of `E` is the total Chern class of the presenting complex. Its degree-`p`
> component is `c_p(E)`.

```lean
def perfectChernClass (hE : HasDefinedChernClasses E) : TotalChowClass C sX
```

## Tag 0GUE, a lemma

[Tag 0GUE](https://stacks.math.columbia.edu/tag/0GUE) in the Stacks Project.

**`Stacks.Chow.hasDefinedChernClasses_of_envelope`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/Criteria.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/Criteria.lean#L69). The attribute's comment: “clause (1): the envelope condition of Tag 0F9E (1) itself”.

> **Stacks 0GUE (1).** If some envelope `f : Y ⟶ X` has `Lf^*E` isomorphic to a locally
> bounded complex of finite locally free `𝒪_Y`-modules, then the Chern classes of `E` are
> defined.

```lean
theorem hasDefinedChernClasses_of_envelope {X Y : Scheme.{u}} (f : Y ⟶ X)
    (hf : IsEnvelope f) (E : DerivedCategory X.Modules) (P : CochainComplex Y.Modules ℤ)
    (hP : IsLocallyBoundedFiniteLocallyFree P)
    (hrep : Nonempty ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
      f.toLRSHom.toShHom).obj E ≅ DerivedCategory.Q.obj P)) :
    HasDefinedChernClasses E
```

**`Stacks.Chow.hasDefinedChernClasses_of_bounded_isFiniteLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/Criteria.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/Criteria.lean#L95). The attribute's comment: “clause (2): a bounded complex of finite locally free modules representing `E`”.

> **Stacks 0GUE (2).** If `E` is represented by a bounded complex of finite locally free
> `𝒪_X`-modules, then the Chern classes of `E` are defined: the identity of `X` is an envelope and
> `L(𝟙 X)^* ≅ 𝟭`.

```lean
theorem hasDefinedChernClasses_of_bounded_isFiniteLocallyFree {X : Scheme.{u}}
    (E : DerivedCategory X.Modules) (P : CochainComplex X.Modules ℤ)
    (hP : CochainComplex.bounded X.Modules P)
    (hflf : ∀ n : ℤ, SheafOfModules.IsFiniteLocallyFree
      (R := structureSheafOfRings X.toRingedSpace) (P.X n))
    (hrep : Nonempty (DerivedCategory.Q.obj P ≅ E)) :
    HasDefinedChernClasses E
```

**`Stacks.Chow.hasDefinedChernClasses_of_derivedPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/Criteria.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/Criteria.lean#L116). The attribute's comment: “clause (5): `E` is the derived pullback of an object whose Chern classes are defined”.

> **Stacks 0GUE (5).** If `E` is isomorphic to the derived pullback of an object `E'` whose
> Chern classes are defined, then the Chern classes of `E` are defined: the base change of an
> envelope of `E'` is an envelope, and the degreewise pullback of a locally bounded complex of
> finite locally free modules is one again and computes the derived pullback.
>
> At `i = Iso.refl` this is the well-definedness that clause (2) of Stacks 0FAC presupposes when it
> writes `c_p(Lg^*E)`.

```lean
theorem hasDefinedChernClasses_of_derivedPullback {X X' : Scheme.{u}} (g : X ⟶ X')
    (E : DerivedCategory X.Modules) (E' : DerivedCategory X'.Modules)
    (hE' : HasDefinedChernClasses E')
    (i : E ≅ (Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
      g.toLRSHom.toShHom).obj E') :
    HasDefinedChernClasses E
```

**`Stacks.Chow.hasDefinedChernClasses_of_isCompact_irreducibleComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/CriteriaComponents.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/CriteriaComponents.lean#L231). The attribute's comment: “clause (3): the irreducible components of X are quasi-compact. The conclusion is the full one: the Chern classes of E are defined, i.e. there is an envelope f : Y -> X with Lf^*E isomorphic in D(O_Y) to a locally bounded complex of finite locally free O_Y-modules, which is Tag 0F9E (1). The hypotheses are exactly the source's: the base situation of Tag 02QL, X locally of finite type over its base, E perfect, and the irreducible components of X quasi-compact”.

> **[Stacks, Tag 0GUE] clause (3).** Let `(S, δ)` be the base situation of chapter 42, let `X`
> be locally of finite type over `S` with quasi-compact irreducible components, and let `E` be a
> perfect object of `D(𝒪_X)`. Then the Chern classes of `E` are defined: there is an envelope
> `f : Y ⟶ X` such that `Lf^*E` is isomorphic in `D(𝒪_Y)` to a locally bounded complex of finite
> locally free `𝒪_Y`-modules.
>
> `X` is locally Noetherian, the base being locally Noetherian and `X` locally of finite type over
> it, so `Stacks.Chow.exists_isEnvelope_sigma_of_isCompact_irreducibleComponents` supplies an
> envelope `∐ W ⟶ X` whose summands are Noetherian — hence quasi-compact and quasi-separated —
> with the resolution property and affine diagonal. Then
> `Stacks.Chow.exists_isLocallyBoundedFiniteLocallyFree_iso_derivedPullback_sigma` represents
> `Lf^*E`, which is clause (1) of the source.
>
> Every hypothesis is a hypothesis of the source: the Chow situation, `X` locally of finite type
> over its base, `E` perfect, and quasi-compactness of the irreducible components of `X`. Local
> Noetherianity, the envelope, the summands' resolution property and affine diagonal, and the
> complex are all derived.

```lean
theorem hasDefinedChernClasses_of_isCompact_irreducibleComponents
    (C : ChowSituation.{u}) {X : Scheme.{u}} (sX : X ⟶ C.S) [LocallyOfFiniteType sX]
    (hqc : ∀ Z ∈ irreducibleComponents X, IsCompact Z)
    (E : DerivedCategory X.Modules) (hE : IsPerfect (X := X.toRingedSpace) E) :
    HasDefinedChernClasses E
```

**`Stacks.Chow.hasDefinedChernClasses_of_compactSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/CriteriaQuasiCompact.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/CriteriaQuasiCompact.lean#L126). The attribute's comment: “clause (4): X is quasi-compact. The conclusion is the full one: the Chern classes of E are defined, i.e. there is an envelope f : Y ⟶ X with Lf^*E isomorphic in D(O_Y) to a locally bounded complex of finite locally free O_Y-modules, which is Tag 0F9E (1). The hypotheses are exactly the source's: the base situation of Tag 02QL, X locally of finite type over its base, E perfect, and X quasi-compact”.

> **[Stacks, Tag 0GUE] clause (4).** Let `(S, δ)` be the base situation of chapter 42, let `X`
> be locally of finite type over `S` and quasi-compact, and let `E` be a perfect object of
> `D(𝒪_X)`. Then the Chern classes of `E` are defined: there is an envelope `f : Y ⟶ X` such that
> `Lf^*E` is isomorphic in `D(𝒪_Y)` to a locally bounded complex of finite locally free
> `𝒪_Y`-modules.
>
> `X` is Noetherian, the base being locally Noetherian, hence quasi-separated, so
> [Stacks, Tag 0GTU] gives an envelope `f : Y ⟶ X` with `Y` carrying an ample family of invertible
> modules; `Y` is Noetherian because `f` is proper, has the resolution property by
> `Stacks.Chow.hasResolutionProperty_of_isAmpleFamily_of_isNoetherian`, and therefore has affine
> diagonal by the Noetherian case of [Stacks, Tag 0F8C]. Then
> `Stacks.Chow.hasDefinedChernClasses_of_resolutionProperty_envelope` applies.
>
> Every hypothesis is a hypothesis of the source: the Chow situation, `X` locally of finite type
> over its base, perfectness of `E`, and quasi-compactness of `X`. Quasi-separatedness,
> Noetherianity, the envelope, the ample family, the resolution property and the affine diagonal
> are all derived.

```lean
theorem hasDefinedChernClasses_of_compactSpace
    (C : ChowSituation.{u}) {X : Scheme.{u}} (sX : X ⟶ C.S) [LocallyOfFiniteType sX]
    [CompactSpace X] (E : DerivedCategory X.Modules)
    (hE : IsPerfect (X := X.toRingedSpace) E) :
    HasDefinedChernClasses E
```

## Tag 0GUF, a lemma

[Tag 0GUF](https://stacks.math.columbia.edu/tag/0GUF) in the Stacks Project.

**`Stacks.Chow.powerSumClass_eq_of_envelopePresentation_modification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassComputedOnModification.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassComputedOnModification.lean#L146). The attribute's comment: “the characteristic class clause res(c_p(E)) = c_p(E^bullet), in the power sum reading P_p of Tag 0ESZ, for the lift a : W' -> Y of the modification to the envelope, so that res is along the g' = a . f of the tag. CARRIED: the family P_p(E) itself, which this repository does not construct -- it is taken as a family restricting along the envelope to P_p of the presenting complex, the hypothesis of the Tag 0GUD uniqueness theorems and the only expression here for 'c is the family of Chern classes of E'; the base change compatibility of the power sum data, which Stacks.Chow.PowerSumClassRule does not record; and the identification of a^*E_Y^. with a representative of L(g')^*E. NOT DELIVERED: the total Chern class reading, which needs the multiplicativity of the restriction map, Tag 0FE0 hence Tag 0B6Y, not formalized here; and the refinement that on an integral W' the pulled back complex has terms of constant rank. The geometric half of the tag is Stacks 0GUF on AlgebraicGeometry.IsEnvelope.exists_properBirational_modification”.

> **Stacks 0GUF, the characteristic class clause, for the power sums.** Let `E` be an object of
> `D(𝒪_X)` and let `H` be an envelope presentation of it, Stacks 0F9E (1), with presenting complex
> `ℰ_Y^• = H.P` vanishing outside the degrees `w, …, w + k`. Let `a : W' ⟶ Y` be the lift to the
> envelope of a modification of a morphism `g : W ⟶ X`, as produced by
> `AlgebraicGeometry.IsEnvelope.exists_properBirational_modification`, so that the morphism
> `g' : W' ⟶ X` of the source is `a ≫ H.f`.
>
> If a family `c` of Chow cohomology classes of `X` restricts along the envelope to the power sums
> of the presenting complex — which is this repository's expression for `c` being the family of
> power sum classes `P_p(E)` of `E`, and is the hypothesis of
> `Stacks.Chow.eq_of_restriction_eq_powerSumClassComplexLocallyBounded` — then its restriction
> along `g' = a ≫ H.f` is the power sum class of the pulled back complex `a^*ℰ_Y^•`:
>
>   `res_{g'}(P_p(E)) = P_p(a^*ℰ_Y^•)`.
>
> This is the source's chain
> `res_{g'}(c_p(E)) = res_a(res_f(c_p(E))) = res_a(c_p(ℰ_Y^•)) = c_p(a^*ℰ_Y^•)`. See the
> implementation notes of this file for what stands in for `c_p(E)`, why the power sums and not the
> total Chern class, and what the statement does not deliver.

```lean
theorem powerSumClass_eq_of_envelopePresentation_modification (H : EnvelopePresentation E)
    [LocallyOfFiniteType H.f] {V : Scheme.{u}} (a : V ⟶ H.Y) [LocallyOfFiniteType a]
    (W : PowerSumClassRule C G (H.f ≫ sX)) (Wa : PowerSumClassRule C G (a ≫ (H.f ≫ sX)))
    (hW : PowerSumClassRule.IsBaseChangeCompatible C G (H.f ≫ sX) a hgys W Wa)
    (w : ℤ) (k : ℕ)
    (hflf : ∀ i ∈ Finset.range (k + 1),
      Stacks.FiniteLocallyFree.IsFiniteLocallyFree.{u, u, u} (R := H.Y.ringCatSheaf)
        (H.P.X (w + (i : ℤ))))
    {c : ∀ p : ℕ, chowCohomologyComponent C G sX (p : ℤ)}
    (hc : ∀ p : ℕ, chowCohomologyRestriction C G sX H.f (p : ℤ) hgys (c p) =
      powerSumClassComplex C G (H.f ≫ sX) W H.P w k p)
    (p : ℕ) :
    chowCohomologyRestriction C G sX (a ≫ H.f) (p : ℤ) hgys (c p) =
      powerSumClassComplex C G (a ≫ (H.f ≫ sX)) Wa
        (((Scheme.Modules.pullback a).mapHomologicalComplex (ComplexShape.up ℤ)).obj H.P)
        w k p
```

**`Stacks.Chow.chernCharacter_eq_of_envelopePresentation_modification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassComputedOnModification.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassComputedOnModification.lean#L230). The attribute's comment: “the characteristic class clause res(c_p(E)) = c_p(E^bullet), in the Chern character reading ch_p = P_p/p! of Tag 0ESZ, for the lift a : W' -> Y of the modification to the envelope, so that res is along the g' = a . f of the tag. CARRIED: the family ch_p(E) itself, which this repository does not construct -- it is taken as a family restricting along the envelope to ch_p of the presenting complex, the hypothesis of the Tag 0GUD uniqueness theorem; the base change compatibility of the power sum data; and the identification of a^*E_Y^. with a representative of L(g')^*E. NOT DELIVERED: the total Chern class reading, which needs the multiplicativity of the restriction map, Tag 0FE0 hence Tag 0B6Y”.

> **Stacks 0GUF, the characteristic class clause, for the Chern character.** The Chern
> character reading of `res(c_p(E)) = c_p(ℰ^•)`: for a family `c` of rational Chow cohomology
> classes of `X` restricting along the envelope of a presentation to the components
> `ch_p(ℰ_Y^•) = P_p(ℰ_Y^•)/p!`, the restriction of `c p` along `g' = a ≫ H.f` is `ch_p(a^*ℰ_Y^•)`.
>
> The hypothesis is the one of `Stacks.Chow.eq_of_restriction_eq_chernCharacterComplexLocallyBounded`,
> the Stacks 0GUD uniqueness theorem for the Chern character, read at a bounded window; see the
> implementation notes of this file.

```lean
theorem chernCharacter_eq_of_envelopePresentation_modification (H : EnvelopePresentation E)
    [LocallyOfFiniteType H.f] {V : Scheme.{u}} (a : V ⟶ H.Y) [LocallyOfFiniteType a]
    (W : PowerSumClassRule C G (H.f ≫ sX)) (Wa : PowerSumClassRule C G (a ≫ (H.f ≫ sX)))
    (hW : PowerSumClassRule.IsBaseChangeCompatible C G (H.f ≫ sX) a hgys W Wa)
    (w : ℤ) (k : ℕ)
    (hflf : ∀ i ∈ Finset.range (k + 1),
      Stacks.FiniteLocallyFree.IsFiniteLocallyFree.{u, u, u} (R := H.Y.ringCatSheaf)
        (H.P.X (w + (i : ℤ))))
    {c : ∀ p : ℕ, rationalChowCohomologyComponent C G sX (p : ℤ)}
    (hc : ∀ p : ℕ, rationalChowCohomologyRestriction C G sX H.f (p : ℤ) hgys (c p) =
      chernCharacterComplexComponent C G (H.f ≫ sX) W H.P w k p)
    (p : ℕ) :
    rationalChowCohomologyRestriction C G sX (a ≫ H.f) (p : ℤ) hgys (c p) =
      chernCharacterComplexComponent C G (a ≫ (H.f ≫ sX)) Wa
        (((Scheme.Modules.pullback a).mapHomologicalComplex (ComplexShape.up ℤ)).obj H.P)
        w k p
```

**`Stacks.Chow.exists_properBirational_res_perfectChernClass_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectChernOnModification.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectChernOnModification.lean#L120). The attribute's comment: “the full lemma: an integral W' with b : W' -> W proper birational, a bounded complex E^bullet of finite locally free O_{W'}-modules of constant ranks representing L(g')^*E for g' = b . g, and res_{g'}(c_p(E)) = c_p(E^bullet) in A^p(W') for the Chern classes c_p(E) of Tag 0F9E (2), Stacks.Chow.perfectChernClass. The perfectness of E is not needed”.

> **Stacks 0GUF.** Let `X` be locally of finite type over the base and let `E` be an object of
> `D(𝒪_X)` whose Chern classes are defined. For `g : W ⟶ X` locally of finite type with `W`
> integral there are an integral scheme `W'` and a proper birational morphism `b : W' ⟶ W` such
> that, for `g' = b ≫ g`, the derived pullback `L(g')^*E` is represented by a bounded complex `ℰ^•`
> of finite locally free `𝒪_{W'}`-modules of constant ranks `ρ`, and
>
>   `res_{g'}(c_p(E)) = c_p(ℰ^•)` in `A^p(W')` for every `p`,
>
> where `c_p(E)` is the degree-`p` component of the total Chern class `c(E)` of Stacks 0F9E (2) and
> `c_p(ℰ^•)` that of `∏_n c(ℰ^n)^{(-1)^n}`.
>
> Perfectness of `E` is not used: the Chern classes being defined is the only hypothesis on `E`
> the construction needs.

```lean
theorem exists_properBirational_res_perfectChernClass_eq (hE : HasDefinedChernClasses E)
    {W : Scheme.{u}} [IsIntegral W] (g : W ⟶ X) [LocallyOfFiniteType g] :
    ∃ (W' : Scheme.{u}) (b : W' ⟶ W) (_ : IsIntegral W') (_ : IsProper b),
      IsBirational b ∧
      ∃ (ℰ : CochainComplex W'.Modules ℤ) (ρ : ℤ →₀ ℕ)
        (hρ : ∀ n,
          AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} (ℰ.X n) (ρ n)),
        (∃ lo hi : ℤ, ∀ n, (n < lo ∨ hi < n) → IsZero (ℰ.X n)) ∧
        Nonempty ((Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
          (b ≫ g).toLRSHom.toShHom).obj E ≅ DerivedCategory.Q.obj ℰ) ∧
        ∀ p : ℕ, chowCohomologyRestriction C (gysinSystemOfInvertible C) sX (b ≫ g) (p : ℤ)
            (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso C)
            (perfectChernClass C sX hE p) =
          complexChernBounded C ((b ≫ g) ≫ sX) ℰ ρ hρ p
```

**`AlgebraicGeometry.IsEnvelope.exists_properBirational_modification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChowGroupsEnvelopes/BirationalModification.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChowGroupsEnvelopes/BirationalModification.lean#L189). The attribute's comment: “existence of the proper birational modification factoring through an envelope”.

> **Stacks 0GUF**, the modification and the factorization. Let `f : Y ⟶ X` be an envelope and
> let `g : W ⟶ X` be a morphism with `W` integral. Then there are an integral scheme `W'`, a
> proper birational morphism `b : W' ⟶ W` and a morphism `a : W' ⟶ Y` with `b ≫ g = a ≫ f`.

```lean
theorem IsEnvelope.exists_properBirational_modification {X Y W : Scheme.{u}}
    {f : Y ⟶ X} (hf : IsEnvelope f) (g : W ⟶ X) [IsIntegral W] :
    ∃ (W' : Scheme.{u}) (b : W' ⟶ W) (a : W' ⟶ Y),
      IsIntegral W' ∧ IsProper b ∧ IsBirational b ∧ b ≫ g = a ≫ f
```

## Tag 0FAC, a lemma

[Tag 0FAC](https://stacks.math.columbia.edu/tag/0FAC) in the Stacks Project.

**`Stacks.Chow.nonhomogeneousBivariantGroupCongr_compositeOfInvertible_perfectChernClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/BivariantCommute.lean, line 713](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/BivariantCommute.lean#L713). The attribute's comment: “(2): c ∘ c_p(E) = c_p(Lg^*E) ∘ c in A^*(X' → X), for every c in A^*(X' → X), the Chern classes of Stacks 0F9E (2) and the composition of Stacks 0B75 at the Gysin system of the first Chern class of an invertible module, extended additively to the graded groups”.

> **Stacks 0FAC (2).** Let `X` be locally of finite type over the base, let `E ∈ D(𝒪_X)` be
> perfect with Chern classes defined, let `g : X' ⟶ X` be locally of finite type and let
> `c ∈ A^*(X' ⟶ X)`. Then for every `p`
>
>   `c ∘ c_p(E) = c_p(Lg^*E) ∘ c`   in   `A^*(X' ⟶ X)`,
>
> the composites being those of Stacks 0B75, extended additively to the graded groups; they are
> classes for the morphisms `g ≫ 𝟙 X` and `𝟙 X' ≫ g`, both read as classes for `g`.

```lean
theorem nonhomogeneousBivariantGroupCongr_compositeOfInvertible_perfectChernClass
    (c : nonhomogeneousBivariantGroup C (gysinSystemOfInvertible C) sX' sX g hg) (p : ℕ) :
    nonhomogeneousBivariantGroupCongr C (gysinSystemOfInvertible C) sX' sX (Category.comp_id g)
        (comp_comp_structureMorphism_eq hg (Category.id_comp sX)) hg
        (nonhomogeneousBivariantCompositeOfInvertible C sX' sX sX g (𝟙 X) hg
          (Category.id_comp sX) c (DirectSum.of _ (p : ℤ) (perfectChernClass C sX hE p))) =
      nonhomogeneousBivariantGroupCongr C (gysinSystemOfInvertible C) sX' sX (Category.id_comp g)
        (comp_comp_structureMorphism_eq (Category.id_comp sX') hg) hg
        (nonhomogeneousBivariantCompositeOfInvertible C sX' sX' sX (𝟙 X') g
          (Category.id_comp sX') hg
          (DirectSum.of _ (p : ℤ) (perfectChernClass C sX' (hE.derivedPullback g) p)) c)
```

**`Stacks.Chow.nonhomogeneousBivariantGroupCongr_compositeOfInvertible_perfectChernClass_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/BivariantCommute.lean, line 747](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/BivariantCommute.lean#L747). The attribute's comment: “(1): c_p(E) is in the center of A^*(X), c · c_p(E) = c_p(E) · c for every c in A^*(X), the product being the composition of Stacks 0B75 at the Gysin system of the first Chern class of an invertible module, extended additively to the graded groups, and the Chern classes of Stacks 0F9E (2)”.

> **Stacks 0FAC (1).** Let `E ∈ D(𝒪_X)` be perfect with Chern classes defined. Then `c_p(E)` is
> in the center of `A^*(X)`: for every `c ∈ A^*(X)`,
>
>   `c · c_p(E) = c_p(E) · c`,
>
> the product of `A^*(X)` being the composition of Stacks 0B75, extended additively to the graded
> groups, of classes for `𝟙 X ≫ 𝟙 X`, read as a class for `𝟙 X`; on homogeneous classes it is
> `Stacks.Chow.BivariantClass.mulId`.

```lean
theorem nonhomogeneousBivariantGroupCongr_compositeOfInvertible_perfectChernClass_comm
    (c : nonhomogeneousBivariantGroup C (gysinSystemOfInvertible C) sX sX (𝟙 X)
      (Category.id_comp sX)) (p : ℕ) :
    nonhomogeneousBivariantGroupCongr C (gysinSystemOfInvertible C) sX sX
        (Category.comp_id (𝟙 X))
        (comp_comp_structureMorphism_eq (Category.id_comp sX) (Category.id_comp sX))
        (Category.id_comp sX)
        (nonhomogeneousBivariantCompositeOfInvertible C sX sX sX (𝟙 X) (𝟙 X) (Category.id_comp sX)
          (Category.id_comp sX) c (DirectSum.of _ (p : ℤ) (perfectChernClass C sX hE p))) =
      nonhomogeneousBivariantGroupCongr C (gysinSystemOfInvertible C) sX sX
        (Category.comp_id (𝟙 X))
        (comp_comp_structureMorphism_eq (Category.id_comp sX) (Category.id_comp sX))
        (Category.id_comp sX)
        (nonhomogeneousBivariantCompositeOfInvertible C sX sX sX (𝟙 X) (𝟙 X) (Category.id_comp sX)
          (Category.id_comp sX) (DirectSum.of _ (p : ℤ) (perfectChernClass C sX hE p)) c)
```

**`Stacks.Chow.comp_perfectChernClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectChernCentral.lean, line 412](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectChernCentral.lean#L412). The attribute's comment: “(2): c ∘ c_p(E) = c_p(Lg^*E) ∘ c in A^*(X' → X) for every g : X' → X locally of finite type and every bivariant class c in A^q(X' → X) of Stacks 0B76”.

> Let `E ∈ D(𝒪_X)` be perfect with defined Chern classes, let `g : X' ⟶ X` be locally of finite
> type and let `c ∈ A^q(X' ⟶ X)` be a bivariant class. Then
>
>   `c ∘ c_p(E) = c_p(Lg^*E) ∘ c`   in   `A^{q+p}(X' ⟶ X)`,
>
> with `c_p(E) ∈ A^p(X)` and `c_p(Lg^*E) ∈ A^p(X')`. The left side is a class for `g ≫ 𝟙 X` of
> degree `q + p`; the right side, a class for `𝟙 X' ≫ g` of degree `p + q`, is read as one for
> `g ≫ 𝟙 X` of degree `q + p` along the identity of `X'`.

```lean
theorem comp_perfectChernClass
    (_perfect : RingedSpace.IsPerfect.{u, u + 1} (X := X.toRingedSpace) E)
    (hE : HasDefinedChernClasses E) (p : ℕ) (g : X' ⟶ X) (hg : g ≫ sX = sX') {q : ℤ}
    (c : BivariantChowClass C sX' sX g hg q) :
    c.comp (BivariantChowClass.equivBivariantClass.symm (perfectChernClass C sX hE p)) =
      (((BivariantChowClass.equivBivariantClass.symm
          (perfectChernClass C sX' (hasDefinedChernClasses_derivedPullback g hE)
            p)).comp c).degreeCongr (add_comm (p : ℤ) q)).transport
        (comp_comp_structureMorphism_eq hg (Category.id_comp sX)) (Iso.refl X') (by simp)
```

**`Stacks.Chow.perfectChernClass_mem_center`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectChernCentral.lean, line 429](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectChernCentral.lean#L429). The attribute's comment: “(1): c_p(E) is in the center of the Chow cohomology ring A^*(X) of Stacks 0B7E”.

> Let `E ∈ D(𝒪_X)` be perfect with defined Chern classes. Then `c_p(E) ∈ A^p(X)` lies in the
> center of the Chow cohomology ring `A^*(X)`.

```lean
theorem perfectChernClass_mem_center
    (_perfect : RingedSpace.IsPerfect.{u, u + 1} (X := X.toRingedSpace) E)
    (hE : HasDefinedChernClasses E) (p : ℕ) :
    letI : Ring (chowCohomology C (gysinSystemOfInvertible C) sX) :=
      chowCohomologyRingOfInvertible C sX
    DirectSum.of (fun q : ℤ ↦ chowCohomologyComponent C (gysinSystemOfInvertible C) sX q)
        (p : ℤ) (perfectChernClass C sX hE p) ∈
      Subring.center (chowCohomology C (gysinSystemOfInvertible C) sX)
```

## Tag 0F9F, a lemma

[Tag 0F9F](https://stacks.math.columbia.edu/tag/0F9F) in the Stacks Project.

**`Stacks.Chow.hasDefinedChernClasses_triangle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/Triangle.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/Triangle.lean#L242). The attribute's comment: “the Chern classes of E₁, E₂, E₃ are defined”.

> **Stacks 0F9F, definedness.** Let `E₁ ⟶ E₂ ⟶ E₃ ⟶ E₁[1]` be a distinguished triangle of
> perfect objects of `D(𝒪_X)` satisfying one of the conditions of Stacks 0F9F. Then the Chern
> classes of `E₁`, `E₂` and `E₃` are defined.

```lean
theorem hasDefinedChernClasses_triangle :
    HasDefinedChernClasses T.obj₁ ∧ HasDefinedChernClasses T.obj₂ ∧
      HasDefinedChernClasses T.obj₃
```

**`Stacks.Chow.perfectChernClass_triangle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/Triangle.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/Triangle.lean#L253). The attribute's comment: “c(E₂) = c(E₁) c(E₃)”.

> **Stacks 0F9F, the total Chern class.** Under the hypotheses of Stacks 0F9F,
> `c(E₂) = c(E₁) c(E₃)`.

```lean
theorem perfectChernClass_triangle (d₁ : HasDefinedChernClasses T.obj₁)
    (d₂ : HasDefinedChernClasses T.obj₂) (d₃ : HasDefinedChernClasses T.obj₃) :
    perfectChernClass C sX d₂ = perfectChernClass C sX d₁ * perfectChernClass C sX d₃
```

**`Stacks.Chow.perfectChernCharacter_triangle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/Triangle.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/Triangle.lean#L262). The attribute's comment: “ch(E₂) = ch(E₁) + ch(E₃), in every degree”.

> **Stacks 0F9F, the Chern character.** Under the hypotheses of Stacks 0F9F,
> `ch(E₂) = ch(E₁) + ch(E₃)`, in every degree `p`.

```lean
theorem perfectChernCharacter_triangle (d₁ : HasDefinedChernClasses T.obj₁)
    (d₂ : HasDefinedChernClasses T.obj₂) (d₃ : HasDefinedChernClasses T.obj₃) (p : ℕ) :
    perfectChernCharacterComponent C sX d₂ p =
      perfectChernCharacterComponent C sX d₁ p + perfectChernCharacterComponent C sX d₃ p
```

**`Stacks.Chow.perfectPowerSum_triangle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/Triangle.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/Triangle.lean#L272). The attribute's comment: “P_p(E₂) = P_p(E₁) + P_p(E₃)”.

> **Stacks 0F9F, the power sums.** Under the hypotheses of Stacks 0F9F,
> `P_p(E₂) = P_p(E₁) + P_p(E₃)` for every `p`.

```lean
theorem perfectPowerSum_triangle (d₁ : HasDefinedChernClasses T.obj₁)
    (d₂ : HasDefinedChernClasses T.obj₂) (d₃ : HasDefinedChernClasses T.obj₃) (p : ℕ) :
    perfectPowerSum C sX d₂ p = perfectPowerSum C sX d₁ p + perfectPowerSum C sX d₃ p
```

**`Stacks.Chow.hasDefinedChernClasses_and_additive_of_envelope`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/TriangleAdditivity.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/TriangleAdditivity.lean#L118). The attribute's comment: “condition (1): there is an envelope f : Y -> X such that Lf^*E_1 -> Lf^*E_2 is represented by a map of locally bounded complexes of finite locally free O_Y-modules. The conclusion is the whole one: the Chern classes of E_1, E_2 and E_3 are defined, c(E_2) = c(E_1)c(E_3), ch(E_2) = ch(E_1) + ch(E_3) and P_p(E_2) = P_p(E_1) + P_p(E_3), the last two read componentwise in A^p(X) tensor Q and in A^p(X) as the source reads them. Perfectness of the three objects is a standing hypothesis of the source that no step of this proof uses, so it is omitted, exactly as for the criteria of Tag 0GUE”.

> **Stacks 0F9F under condition (1) of the source.** Let `T` be a distinguished triangle of
> `D(𝒪_X)`. If there is an envelope `f : Y ⟶ X` such that `Lf^*T.mor₁ : Lf^*E₁ ⟶ Lf^*E₂` is
> represented by a map `α : 𝓔₁^• ⟶ 𝓔₂^•` of locally bounded complexes of finite locally free
> `𝒪_Y`-modules, then the Chern classes of `E₁`, `E₂`, `E₃` are defined and
>
>   `c(E₂) = c(E₁) c(E₃)`,  `ch_p(E₂) = ch_p(E₁) + ch_p(E₃)`,  `P_p(E₂) = P_p(E₁) + P_p(E₃)`.
>
> The cone of `α` is a locally bounded complex of finite locally free modules representing
> `Lf^*E₃`, so `f` together with `𝓔₁^•`, `𝓔₂^•` and `C(α)^•` presents all three objects, and each
> identity is the corresponding identity for those complexes.

```lean
theorem hasDefinedChernClasses_and_additive_of_envelope
    (T : Triangle (DerivedCategory X.Modules))
    (hT : T ∈ distTriang (DerivedCategory X.Modules))
    {Y : Scheme.{u}} (f : Y ⟶ X) (hf : IsEnvelope f)
    {P₁ P₂ : CochainComplex Y.Modules ℤ} (α : P₁ ⟶ P₂)
    (h₁ : IsLocallyBoundedFiniteLocallyFree P₁) (h₂ : IsLocallyBoundedFiniteLocallyFree P₂)
    (e₁ : (Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
      f.toLRSHom.toShHom).obj T.obj₁ ≅ DerivedCategory.Q.obj P₁)
    (e₂ : (Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
      f.toLRSHom.toShHom).obj T.obj₂ ≅ DerivedCategory.Q.obj P₂)
    (hα : e₁.hom ≫ DerivedCategory.Q.map α =
      (Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
        f.toLRSHom.toShHom).map T.mor₁ ≫ e₂.hom) :
    TriangleChernAdditive C sX T
```

**`Stacks.Chow.hasDefinedChernClasses_and_additive_of_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/TriangleAdditivity.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/TriangleAdditivity.lean#L185). The attribute's comment: “condition (2): E_1 -> E_2 is represented by a map of locally bounded complexes of finite locally free O_X-modules. The conclusion is the whole one: the Chern classes of E_1, E_2 and E_3 are defined, c(E_2) = c(E_1)c(E_3), ch(E_2) = ch(E_1) + ch(E_3) and P_p(E_2) = P_p(E_1) + P_p(E_3), the last two read componentwise in A^p(X) tensor Q and in A^p(X) as the source reads them. Perfectness of the three objects is a standing hypothesis of the source that no step of this proof uses, so it is omitted, exactly as for the criteria of Tag 0GUE”.

> **Stacks 0F9F under condition (2) of the source.** If the first map `T.mor₁ : E₁ ⟶ E₂` of a
> distinguished triangle of `D(𝒪_X)` is itself represented by a map `α : 𝓔₁^• ⟶ 𝓔₂^•` of locally
> bounded complexes of finite locally free `𝒪_X`-modules, then the Chern classes of `E₁`, `E₂`,
> `E₃` are defined and
>
>   `c(E₂) = c(E₁) c(E₃)`,  `ch_p(E₂) = ch_p(E₁) + ch_p(E₃)`,  `P_p(E₂) = P_p(E₁) + P_p(E₃)`.
>
> This is condition (1) for the envelope `𝟙 X`, which is proper and completely decomposed; the
> square identifying `α` with `T.mor₁` transports along the naturality of `L(𝟙 X)^* ≅ 𝟭`.

```lean
theorem hasDefinedChernClasses_and_additive_of_map
    (T : Triangle (DerivedCategory X.Modules))
    (hT : T ∈ distTriang (DerivedCategory X.Modules))
    {P₁ P₂ : CochainComplex X.Modules ℤ} (α : P₁ ⟶ P₂)
    (h₁ : IsLocallyBoundedFiniteLocallyFree P₁) (h₂ : IsLocallyBoundedFiniteLocallyFree P₂)
    (i₁ : T.obj₁ ≅ DerivedCategory.Q.obj P₁) (i₂ : T.obj₂ ≅ DerivedCategory.Q.obj P₂)
    (hα : i₁.hom ≫ DerivedCategory.Q.map α = T.mor₁ ≫ i₂.hom) :
    TriangleChernAdditive C sX T
```

**`Stacks.Chow.triangleChernAdditive_of_isCompact_irreducibleComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/TriangleAdditivityComponents.lean, line 351](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/TriangleAdditivityComponents.lean#L351). The attribute's comment: “condition (3): the irreducible components of X are quasi-compact. The conclusion is the whole one: the Chern classes of E_1, E_2 and E_3 are defined, c(E_2) = c(E_1)c(E_3), ch(E_2) = ch(E_1) + ch(E_3) and P_p(E_2) = P_p(E_1) + P_p(E_3), the last two read componentwise in A^p(X) tensor Q and in A^p(X) as the source reads them. The hypotheses are exactly the source's: the base situation of Tag 02QL, X locally of finite type over its base, the distinguished triangle, perfectness of E_1 and E_2, and the irreducible components of X quasi-compact. Perfectness of E_3 is a standing hypothesis of the source that no step of this proof uses, so it is omitted, exactly as for conditions (1), (2) and (4)”.

> **[Stacks, Tag 0F9F] under condition (3) of the source.** Let `T` be a distinguished triangle
> of `D(𝒪_X)` whose first two objects are perfect and let the irreducible components of `X`, which
> is locally of finite type over the base of the Chow situation, be quasi-compact. Then the Chern
> classes of `E₁`, `E₂`, `E₃` are defined and
>
>   `c(E₂) = c(E₁) c(E₃)`,  `ch_p(E₂) = ch_p(E₁) + ch_p(E₃)`,  `P_p(E₂) = P_p(E₁) + P_p(E₃)`.
>
> `X` is locally Noetherian, the base being locally Noetherian and `X` locally of finite type over
> it, so `Stacks.Chow.exists_isEnvelope_sigma_of_isCompact_irreducibleComponents` supplies an
> envelope `∐ W ⟶ X` whose summands are Noetherian — hence quasi-compact and quasi-separated —
> with the resolution property and affine diagonal. On such a source
> `Stacks.Chow.exists_boundedFiniteLocallyFree_sigma_of_isPerfect` presents `Lf^*E₁` and `Lf^*E₂`
> by complexes whose summandwise restrictions are bounded complexes of finite locally free
> modules, and `Stacks.Chow.exists_isLocallyBoundedFiniteLocallyFree_square_sigma` represents
> `Lf^*E₁ ⟶ Lf^*E₂` by a map of locally bounded complexes of finite locally free modules together
> with the commuting square. That is condition (1) of the source, in the shape
> `Stacks.Chow.hasDefinedChernClasses_and_additive_of_envelope` asks for.
>
> Every hypothesis is a hypothesis of the source: the Chow situation, `X` locally of finite type
> over its base, the distinguished triangle, perfectness of `E₁` and `E₂`, and quasi-compactness
> of the irreducible components of `X`. Local Noetherianity, the envelope, the summands'
> resolution property and affine diagonal, the two complexes and the map between them are all
> derived. Perfectness of `E₃` is a standing hypothesis of the source that no step of this proof
> uses, so it is omitted.

```lean
theorem triangleChernAdditive_of_isCompact_irreducibleComponents
    (C : ChowSituation.{u}) {X : Scheme.{u}} (sX : X ⟶ C.S) [LocallyOfFiniteType sX]
    (T : Triangle (DerivedCategory X.Modules)) (hT : T ∈ distTriang (DerivedCategory X.Modules))
    (h₁ : IsPerfect (X := X.toRingedSpace) T.obj₁)
    (h₂ : IsPerfect (X := X.toRingedSpace) T.obj₂)
    (hqc : ∀ Z ∈ irreducibleComponents X, IsCompact Z) :
    TriangleChernAdditive C sX T
```

**`Stacks.Chow.triangleChernAdditive_of_compactSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/TriangleAdditivityQuasiCompact.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/TriangleAdditivityQuasiCompact.lean#L147). The attribute's comment: “condition (4): X is quasi-compact. The conclusion is the whole one: the Chern classes of E_1, E_2 and E_3 are defined, c(E_2) = c(E_1)c(E_3), ch(E_2) = ch(E_1) + ch(E_3) and P_p(E_2) = P_p(E_1) + P_p(E_3), the last two read componentwise in A^p(X) tensor Q and in A^p(X) as the source reads them. Perfectness of E_3 is a standing hypothesis of the source that no step of this proof uses, so it is omitted, exactly as for conditions (1) and (2)”.

> **[Stacks, Tag 0F9F] under condition (4) of the source.** Let `T` be a
> distinguished triangle of `D(𝒪_X)` whose first two objects are perfect and let `X`, which is
> locally of finite type over the base of the Chow situation, be quasi-compact. Then the Chern
> classes of `E₁`, `E₂`, `E₃` are defined and
>
>   `c(E₂) = c(E₁) c(E₃)`,  `ch_p(E₂) = ch_p(E₁) + ch_p(E₃)`,  `P_p(E₂) = P_p(E₁) + P_p(E₃)`.
>
> `X` is Noetherian, the base being locally Noetherian, hence quasi-separated, so
> [Stacks, Tag 0GTU] gives an envelope `f : Y ⟶ X` with `Y` carrying an ample family of invertible
> modules; `Y` is Noetherian because `f` is proper, has the resolution property by
> `Stacks.Chow.hasResolutionProperty_of_isAmpleFamily_of_isNoetherian`, and therefore has affine
> diagonal by the Noetherian case of [Stacks, Tag 0F8C]. That is condition (1) of the source, in
> the shape `Stacks.Chow.triangleChernAdditive_of_resolutionProperty_envelope` asks for.
>
> Every hypothesis is a hypothesis of the source: the Chow situation, `X` locally of finite type
> over its base, the distinguished triangle, perfectness of `E₁` and `E₂`, and quasi-compactness
> of `X`. Quasi-separatedness, Noetherianity, the envelope, the ample family, the resolution
> property and the affine diagonal are all derived. Perfectness of `E₃` is a standing hypothesis
> of the source that no step of this proof uses, so it is omitted.

```lean
theorem triangleChernAdditive_of_compactSpace
    (C : ChowSituation.{u}) {X : Scheme.{u}} (sX : X ⟶ C.S) [LocallyOfFiniteType sX]
    [CompactSpace X]
    (T : Triangle (DerivedCategory X.Modules)) (hT : T ∈ distTriang (DerivedCategory X.Modules))
    (h₁ : IsPerfect (X := X.toRingedSpace) T.obj₁)
    (h₂ : IsPerfect (X := X.toRingedSpace) T.obj₂) :
    TriangleChernAdditive C sX T
```

## Tag 0FAD, a remark

[Tag 0FAD](https://stacks.math.columbia.edu/tag/0FAD) in the Stacks Project.

**`Stacks.Chow.perfectPowerSum_eq_aeval`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectNewtonIdentities.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectNewtonIdentities.lean#L191). The attribute's comment: “P_p(E) is the exact same expression in the Chern classes of E as in the case of vector bundles: the power-sum polynomial P_p of 0F9B evaluated at c_1(E), ..., c_p(E), p >= 1”.

> **Newton's identities for a perfect object**, Remark 0FAD. For `p ≥ 1` the class `P_p(E)` is
> the universal power-sum polynomial `P_p` of Stacks 0F9B evaluated at the Chern classes of `E` — the
> same expression in the Chern classes as for a finite locally free module. The polynomial is
> evaluated in the commutative subring of `A^*(X)` generated by the Chern classes of `E`.

```lean
theorem perfectPowerSum_eq_aeval (p : ℕ) (hp : 0 < p) :
    perfectPowerSum C sX hE p =
      (MvPolynomial.aeval (perfectChernSub C sX hE)
        (powerSumPolynomial p : MvPolynomial ℕ+ ℤ) : TotalChowClass C sX)
```

**`Stacks.Chow.perfectPowerSum_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectNewtonIdentities.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectNewtonIdentities.lean#L206). The attribute's comment: “the first displayed formula P_1(E) = c_1(E)”.

> `P_1(E) = c_1(E)`, Remark 0FAD.

```lean
theorem perfectPowerSum_one :
    perfectPowerSum C sX hE 1 = perfectChernComponent C sX hE 1
```

**`Stacks.Chow.perfectPowerSum_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectNewtonIdentities.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectNewtonIdentities.lean#L213). The attribute's comment: “the second displayed formula P_2(E) = c_1(E)^2 - 2c_2(E)”.

> `P_2(E) = c_1(E)^2 - 2 c_2(E)`, Remark 0FAD.

```lean
theorem perfectPowerSum_two :
    perfectPowerSum C sX hE 2 =
      perfectChernComponent C sX hE 1 ^ 2 - 2 * perfectChernComponent C sX hE 2
```

**`Stacks.Chow.perfectPowerSum_three`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectNewtonIdentities.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectNewtonIdentities.lean#L222). The attribute's comment: “the third displayed formula P_3(E) = c_1(E)^3 - 3c_1(E)c_2(E) + 3c_3(E)”.

> `P_3(E) = c_1(E)^3 - 3 c_1(E) c_2(E) + 3 c_3(E)`, Remark 0FAD.

```lean
theorem perfectPowerSum_three :
    perfectPowerSum C sX hE 3 =
      perfectChernComponent C sX hE 1 ^ 3 -
        3 * perfectChernComponent C sX hE 1 * perfectChernComponent C sX hE 2 +
        3 * perfectChernComponent C sX hE 3
```

**`Stacks.Chow.perfectPowerSum_four`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectNewtonIdentities.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectNewtonIdentities.lean#L235). The attribute's comment: “the fourth displayed formula P_4(E) = c_1(E)^4 - 4c_1(E)^2c_2(E) + 4c_1(E)c_3(E) + 2c_2(E)^2 - 4c_4(E)”.

> `P_4(E) = c_1(E)^4 - 4 c_1(E)^2 c_2(E) + 4 c_1(E) c_3(E) + 2 c_2(E)^2 - 4 c_4(E)`,
> Remark 0FAD.

```lean
theorem perfectPowerSum_four :
    perfectPowerSum C sX hE 4 =
      perfectChernComponent C sX hE 1 ^ 4 -
        4 * perfectChernComponent C sX hE 1 ^ 2 * perfectChernComponent C sX hE 2 +
        4 * perfectChernComponent C sX hE 1 * perfectChernComponent C sX hE 3 +
        2 * perfectChernComponent C sX hE 2 ^ 2 - 4 * perfectChernComponent C sX hE 4
```

**`Stacks.Chow.perfectPowerSum_zero_and_perfectChernCharacterComponent_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectNewtonIdentities.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectNewtonIdentities.lean#L248). The attribute's comment: “the bivariant class P_0(E) = r(E) = ch_0(E)”.

> **`P_0(E) = r(E) = ch_0(E)`**, Remark 0FAD: the degree-zero power sum and the degree-zero
> component of the Chern character are the rank of `E`.

```lean
theorem perfectPowerSum_zero_and_perfectChernCharacterComponent_zero :
    perfectPowerSum C sX hE 0 = perfectRankClass C sX hE ∧
      perfectChernCharacterComponent C sX hE 0 = (1 : ℚ) ⊗ₜ[ℤ] perfectRankClass C sX hE 0
```

**`Stacks.Chow.log_perfectChernClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectNewtonIdentities.lean, line 340](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectNewtonIdentities.lean#L340). The attribute's comment: “formally taking the logarithm: log(c(E)) = sum_p (-1)^{p-1} P_p(E)/p, read in A^p(X) tensor Q degree by degree, the degree-p part of log c(E) being sum_{k=1}^p (-1)^{k-1} (c(E) - 1)^k / k”.

> **The logarithmic identity for a perfect object.** In `A^p(X) ⊗ 𝐐`,
>
>   `∑_{k = 1}^{p} (-1)^{k-1} (c(E) - 1)^k / k = (-1)^{p-1} P_p(E) / p`,
>
> the left hand side being the degree-`p` part of `log c(E)` (the terms with `k > p` vanish in
> degree `p`: `Stacks.Chow.pow_perfectChernClass_sub_one_apply_of_lt`). So
> `log c(E) = ∑_p (-1)^{p-1} P_p(E) / p`, Remark 0FAD.

```lean
theorem log_perfectChernClass (p : ℕ) :
    ∑ k ∈ Finset.Icc 1 p, ((-1 : ℚ) ^ (k - 1) / k) ⊗ₜ[ℤ]
        ((perfectChernClass C sX hE - 1) ^ k) p =
      ((-1 : ℚ) ^ (p - 1) / p) ⊗ₜ[ℤ] perfectPowerSumComponent C sX hE p
```

**`Stacks.Chow.exists_perfectChernClass_eq_perfectPowerSum_zero_ne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectNewtonIdentities.lean, line 540](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectNewtonIdentities.lean#L540). The attribute's comment: “the bivariant class P_0(E) = r(E) cannot be recovered from the Chern class c(E): on every nonempty X, c(O_X[0]) = c(0) = 1 while r(O_X[0]) = 1 differs from r(0) = 0”.

> **The rank of a perfect object is not determined by its total Chern class**, Remark 0FAD: on
> every nonempty `X` there are perfect objects `E` and `F` whose Chern classes are defined, with
> `c(E) = c(F)` but `P_0(E) = r(E) ≠ r(F) = P_0(F)`. Namely `E = 𝒪_X[0]` and `F = 0[0]`: both
> have total Chern class `1`, and their ranks are `1` and `0`.

```lean
theorem exists_perfectChernClass_eq_perfectPowerSum_zero_ne [Nonempty X] :
    ∃ (E F : DerivedCategory X.Modules)
      (_ : RingedSpace.IsPerfect.{u, u + 1} (X := X.toRingedSpace) E)
      (_ : RingedSpace.IsPerfect.{u, u + 1} (X := X.toRingedSpace) F)
      (hE : HasDefinedChernClasses E) (hF : HasDefinedChernClasses F),
      perfectChernClass C sX hE = perfectChernClass C sX hF ∧
        perfectPowerSum C sX hE 0 ≠ perfectPowerSum C sX hF 0
```

**`Stacks.Chow.eq_of_chowCohomologyRestriction_eq_of_envelopePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/SplittingPrinciple.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/SplittingPrinciple.lean#L148). The attribute's comment: “the splitting principle: a relation between bivariant classes on X may be checked after restriction along the envelope of a presentation, restriction along an envelope being injective”.

> **Stacks 0FAD.** A relation between Chow cohomology classes on `X` may be proved after
> restricting along the envelope `f : Y ⟶ X` of a presentation of `E`: two classes of degree `p`
> on `X` whose restrictions to `A^p(Y)` agree are equal.

```lean
theorem eq_of_chowCohomologyRestriction_eq_of_envelopePresentation (C : ChowSituation.{u})
    (G : GysinSystem C) {X : Scheme.{u}} (sX : X ⟶ C.S) [LocallyOfFiniteType sX]
    {E : DerivedCategory X.Modules} (H : EnvelopePresentation E) (p : ℤ)
    (hgys : G.IsNaturalUnderBaseChangeIso) {c d : chowCohomologyComponent C G sX p} :
    letI : IsProper H.f := H.envelope.isProper
    letI : LocallyOfFiniteType H.f := IsProper.toLocallyOfFiniteType
    chowCohomologyRestriction C G sX H.f p hgys c =
        chowCohomologyRestriction C G sX H.f p hgys d →
      c = d
```

**`Stacks.Chow.eq_of_forall_chowCohomologyRestriction_eq_of_hasDefinedChernClasses`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/SplittingPrinciple.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/SplittingPrinciple.lean#L167). The attribute's comment: “the splitting principle with the choice of envelope left open: the Chern classes of E being defined, a relation between bivariant classes on X follows from the relation after restriction along the envelope of every presentation”.

> **Stacks 0FAD.** The same reduction with the envelope left to be chosen, as in the source: if
> the Chern classes of `E` are defined, then two Chow cohomology classes of degree `p` on `X` whose
> restrictions agree along the envelope of every presentation of `E` are equal.

```lean
theorem eq_of_forall_chowCohomologyRestriction_eq_of_hasDefinedChernClasses
    (C : ChowSituation.{u}) (G : GysinSystem C) {X : Scheme.{u}} (sX : X ⟶ C.S)
    [LocallyOfFiniteType sX] {E : DerivedCategory X.Modules} (hE : HasDefinedChernClasses E)
    (p : ℤ) (hgys : G.IsNaturalUnderBaseChangeIso) {c d : chowCohomologyComponent C G sX p}
    (h : ∀ H : EnvelopePresentation E,
      letI : IsProper H.f := H.envelope.isProper
      letI : LocallyOfFiniteType H.f := IsProper.toLocallyOfFiniteType
      chowCohomologyRestriction C G sX H.f p hgys c =
        chowCohomologyRestriction C G sX H.f p hgys d) :
    c = d
```

**`Stacks.Chow.exists_splitCharts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/SplittingPrinciplePerfect.lean, line 739](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/SplittingPrinciplePerfect.lean#L739). The attribute's comment: “the splitting principle: for every envelope f : Y -> X and complex E^bullet representing Lf^*E there are split charts (the connected component of each point of Y, where E^bullet is bounded of fixed ranks, followed by the splitting morphism of 02UL filtering each term by invertible modules L_{n,j}), restriction to all of them is injective on A^*(X), and on them c(E) = prod_{n even} (1 + x_{n,j}) prod_{n odd} (1 + x_{n,j})^{-1} and P_p(E) = sum_{n even} x_{n,j}^p - sum_{n odd} x_{n,j}^p with x_{n,j} = c_1(L_{n,j})”.

> Let `(S, δ)`, `X` and `E` be as in Definition 0F9E, the Chern classes of `E` being defined,
> and choose an envelope `f : Y ⟶ X` and a locally bounded complex `ℰ^•` of finite locally free
> `𝒪_Y`-modules representing `Lf^*E`. Then there is a split chart `π_y : P_y ⟶ V_y` at every point
> `y ∈ Y`: over the connected component `V_y` of `y`, where `ℰ^•` is a bounded complex of finite
> locally free modules of fixed ranks, `π_y` is the splitting morphism of Stacks 02UL, along which
> each `ℰ^n` acquires a filtration with invertible successive quotients `ℒ_{n,j}`. For such a
> choice of charts:
>
> 1. a relation between total Chow cohomology classes on `X` — in particular between the classes
>    `c_p(E)` and `P_p(E)` — may be checked after restriction to all the charts: restriction
>    `A^*(X) ⟶ ∏_y A^*(P_y)` is injective;
> 2. with `x_{n,j} = c_1(ℒ_{n,j})`, on each chart
>    `c(E) = ∏_{n even} ∏_j (1 + x_{n,j}) · (∏_{n odd} ∏_j (1 + x_{n,j}))^{-1}`, the factor
>    `1 + x_{n,j} = c(ℒ_{n,j})` being a unit;
> 3. with `x_{n,j} = c_1(ℒ_{n,j})`, on each chart
>    `P_p(E) = ∑_{n even} ∑_j x_{n,j}^p - ∑_{n odd} ∑_j x_{n,j}^p` for every `p ≥ 0`.
>
> Here `c(E)` and `P_p(E)` are the classes of Definition 0F9E (2).

```lean
theorem exists_splitCharts (hE : HasDefinedChernClasses E) (H : EnvelopePresentation E) :
    ∃ χ : ∀ y : H.Y, SplitChart C sX H y,
      Function.Injective (fun (c : TotalChowClass C sX) (y : H.Y) ↦ (χ y).res c) ∧
      (∀ y n j, ((χ y).rootFactor n j : TotalChowClass C (χ y).T.sP) = 1 + (χ y).root n j) ∧
      (∀ y, (χ y).res (perfectChernClass C sX hE) =
        ↑(((((complexRank H.locallyBounded y).support.sort (· ≤ ·)).filter fun n ↦ Even n).map
            fun n ↦ (List.ofFn ((χ y).rootFactor n)).prod).prod *
          (((((complexRank H.locallyBounded y).support.sort (· ≤ ·)).filter
            fun n ↦ ¬ Even n).map fun n ↦ (List.ofFn ((χ y).rootFactor n)).prod).prod)⁻¹)) ∧
      ∀ y (p : ℕ), (χ y).res (perfectPowerSum C sX hE p) =
        (∑ n ∈ (complexRank H.locallyBounded y).support with Even n,
            ∑ j, (χ y).root n j ^ p) -
          ∑ n ∈ (complexRank H.locallyBounded y).support with ¬ Even n,
            ∑ j, (χ y).root n j ^ p
```

## Tag 0FAE, a lemma

[Tag 0FAE](https://stacks.math.columbia.edu/tag/0FAE) in the Stacks Project.

**`Stacks.Chow.hasDefinedChernClasses_derivedDual`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/DualChernClasses.lean, line 358](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/DualChernClasses.lean#L358). The attribute's comment: “the Chern classes of the derived dual are defined, which is what makes the assertion of the lemma well-typed”.

> **The Chern classes of the derived dual of a perfect object are defined** as soon as those of
> the object are, [Stacks, Tag 0F9E] (1) for `E^∨`: dualize an envelope presentation of `E`.
>
> This is what makes the assertion of [Stacks, Tag 0FAE] well-typed, the classes `c_p`, `P_p` and
> `ch_p` of [Stacks, Tag 0F9E] (2) being defined only under that hypothesis.

```lean
theorem hasDefinedChernClasses_derivedDual
    (hE : Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace) E)
    (h : HasDefinedChernClasses E) :
    HasDefinedChernClasses (Stacks.Chow.derivedDual E)
```

**`Stacks.Chow.perfectChernClass_apply_derivedDual`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/DualChernClasses.lean, line 399](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/DualChernClasses.lean#L399). The attribute's comment: “the Chern classes: c_p(E-dual) = (-1)^p c_p(E) in A^p(X)”.

> **`c_p(E^∨) = (-1)^p c_p(E)` in `A^p(X)`**, the first conclusion of [Stacks, Tag 0FAE].

```lean
theorem perfectChernClass_apply_derivedDual
    (hE : Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace) E)
    (h : HasDefinedChernClasses E) (p : ℕ) :
    perfectChernClass C sX (hasDefinedChernClasses_derivedDual hE h) p =
      ((-1 : ℤ) ^ p) • perfectChernClass C sX h p
```

**`Stacks.Chow.perfectPowerSumComponent_derivedDual`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/DualChernClasses.lean, line 428](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/DualChernClasses.lean#L428). The attribute's comment: “the power-sum classes: P_p(E-dual) = (-1)^p P_p(E) in A^p(X)”.

> **`P_p(E^∨) = (-1)^p P_p(E)` in `A^p(X)`**, the second conclusion of [Stacks, Tag 0FAE].

```lean
theorem perfectPowerSumComponent_derivedDual
    (hE : Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace) E)
    (h : HasDefinedChernClasses E) (p : ℕ) :
    perfectPowerSumComponent C sX (hasDefinedChernClasses_derivedDual hE h) p =
      ((-1 : ℤ) ^ p) • perfectPowerSumComponent C sX h p
```

**`Stacks.Chow.perfectChernCharacterComponent_derivedDual`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/DualChernClasses.lean, line 441](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/DualChernClasses.lean#L441). The attribute's comment: “the Chern character: ch_p(E-dual) = (-1)^p ch_p(E) in A^p(X) tensor Q”.

> **`ch_p(E^∨) = (-1)^p ch_p(E)` in `A^p(X) ⊗ 𝐐`**, the third conclusion of
> [Stacks, Tag 0FAE]. The Chern character component is `P_p/p!`, so the sign passes through the
> tensor factor.

```lean
theorem perfectChernCharacterComponent_derivedDual
    (hE : Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace) E)
    (h : HasDefinedChernClasses E) (p : ℕ) :
    perfectChernCharacterComponent C sX (hasDefinedChernClasses_derivedDual hE h) p =
      ((-1 : ℤ) ^ p) • perfectChernCharacterComponent C sX h p
```

## Tag 0FAF, a lemma

[Tag 0FAF](https://stacks.math.columbia.edu/tag/0FAF) in the Stacks Project.

**`Stacks.Chow.perfectChernClass_derivedTwist_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectTwist.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectTwist.lean#L253).

> **The Chern classes of a twist.** Let `X` be locally of finite type over the base of
> chapter 42, let `E` be a perfect object of `D(𝒪_X)` whose Chern classes are defined and which has
> constant rank `r`, and let `ℒ` be an invertible `𝒪_X`-module. Then
>
>   `c_i(E ⊗ ℒ) = ∑_{j=0}^{i} binom(r - i + j, j) c_{i-j}(E) c_1(ℒ)^j`
>
> in `A^i(X)`, where `c_{i-j}(E)` is the component of degree `i - j` of the total Chern class and
> the product is that of Chow cohomology.

```lean
theorem perfectChernClass_derivedTwist_apply (perfect : RingedSpace.IsPerfect.{u, u + 1} E)
    (definedChernClasses : HasDefinedChernClasses E) (r : ℤ)
    (constantRank : ∀ x : X, DerivedFibreBetti.chiDerivedFibre X E
      (DerivedFibreBetti.isPseudoCoherent_of_isPerfect E perfect) x = r) (i : ℕ) :
    perfectChernClass C sX (hasDefinedChernClasses_derivedTwist definedChernClasses L) i =
      ∑ j ∈ range (i + 1), Ring.choose (r - i + j) j •
        (TotalChowClass.homComponent (i - j) (perfectChernClass C sX definedChernClasses) *
          TotalChowClass.firstChernTotal C sX L ^ j) i
```

## Tag 0FAG, a lemma

[Tag 0FAG](https://stacks.math.columbia.edu/tag/0FAG) in the Stacks Project.

**`Stacks.Chow.perfectChernClass_derivedTensor_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/DerivedTensor.lean, line 349](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/DerivedTensor.lean#L349). The attribute's comment: “the formula for c_1(E tensor^L F), for objects E, F of D(O_X) whose Chern classes are defined; perfectness is not needed. The rank r(E) is the class P_0(E) = perfectPowerSum C sX hE 0 in A^0(X), not assumed constant, and r(E) c_1(F) is the product in the ring TotalChowClass C sX of total Chow cohomology classes. E tensor^L F is the derived tensor product derivedTensorProductFunctor of Stacks 06YU”.

> **The first Chern class of a derived tensor product.** For objects `E`, `F` of `D(𝒪_X)` whose
> Chern classes are defined,
>
>   `c₁(E ⊗^L F) = r(E) c₁(F) + r(F) c₁(E)`
>
> in `A^*(X)`, where `r(E) = P_0(E)` is the rank and `c₁` the degree-one part of the total Chern
> class.

```lean
theorem perfectChernClass_derivedTensor_one :
    TotalChowClass.homComponent 1 (perfectChernClass C sX hEF) =
      perfectPowerSum C sX hE 0 * TotalChowClass.homComponent 1 (perfectChernClass C sX hF) +
        perfectPowerSum C sX hF 0 * TotalChowClass.homComponent 1 (perfectChernClass C sX hE)
```

**`Stacks.Chow.perfectPowerSum_derivedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/DerivedTensor.lean, line 395](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/DerivedTensor.lean#L395). The attribute's comment: “the precise form P_p(E tensor^L F) = sum over p_1 + p_2 = p of C(p, p_1) P_{p_1}(E) P_{p_2}(F) in A^p(X), for every p >= 0, for objects E, F of D(O_X) whose Chern classes are defined (perfectness is not needed); P_p is perfectPowerSum of Stacks 0GUD, P_0 being the rank, and the products are those of TotalChowClass C sX. The statement ch(E tensor F) = ch(E) ch(F) in A^*(X) tensor Q is the consequence of this identity obtained by dividing by p!, which is not stated separately”.

> **The power sums of a derived tensor product.** For objects `E`, `F` of `D(𝒪_X)` whose Chern
> classes are defined and every `p ≥ 0`,
>
>   `P_p(E ⊗^L F) = ∑_{p₁ + p₂ = p} C(p, p₁) P_{p₁}(E) P_{p₂}(F)`
>
> in `A^p(X)`, the power sums `P_0` being the ranks; dividing by `p!` this is
> `ch(E ⊗^L F) = ch(E) ch(F)`.

```lean
theorem perfectPowerSum_derivedTensor (p : ℕ) :
    perfectPowerSum C sX hEF p =
      ∑ q ∈ antidiagonal p, (p.choose q.1 : ℤ) •
        (perfectPowerSum C sX hE q.1 * perfectPowerSum C sX hF q.2)
```

**`Stacks.Chow.perfectChernClass_derivedTensor_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/DerivedTensor.lean, line 440](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/DerivedTensor.lean#L440). The attribute's comment: “the formula for c_2(E tensor^L F), for perfect objects E, F of D(O_X) whose Chern classes are defined, the ranks being arbitrary locally constant functions. r(E) is the class P_0(E) = perfectPowerSum C sX hE 0 in A^0(X); the binomial coefficient C(r(E), 2) is read as the class ofLocallyConstant of the locally constant function x |-> Ring.choose (chi_E(x)) 2, chi_E the derived-fibre Euler characteristic, whose own class is r(E) by perfectPowerSum_zero_eq_ofLocallyConstant; on the open and closed subscheme where E has rank r these are the integers r and C(r, 2), as in Remark 0FA7. The products are those of TotalChowClass C sX, written in the order of the source. The source's 'and so on for higher Chern classes' is not a precise assertion and is not formalized”.

> **The second Chern class of a derived tensor product.** For perfect objects `E`, `F` of
> `D(𝒪_X)` whose Chern classes are defined,
>
>   `c₂(E ⊗^L F) = r(E) c₂(F) + r(F) c₂(E) + C(r(E), 2) c₁(F)² + (r(E) r(F) - 1) c₁(F) c₁(E) +
>     C(r(F), 2) c₁(E)²`
>
> in `A^*(X)`, where `r(E) = P_0(E)` is the rank and `C(r(E), 2)` is the class of the locally
> constant function `x ↦ C(χ_E(x), 2)`, `χ_E` being the Euler characteristic of the derived fibre
> of `E`, whose class is `r(E)` (`Stacks.Chow.perfectPowerSum_zero_eq_ofLocallyConstant`).

```lean
theorem perfectChernClass_derivedTensor_two (perfectE : RingedSpace.IsPerfect.{u, u + 1} E)
    (perfectF : RingedSpace.IsPerfect.{u, u + 1} F) :
    TotalChowClass.homComponent 2 (perfectChernClass C sX hEF) =
      perfectPowerSum C sX hE 0 * TotalChowClass.homComponent 2 (perfectChernClass C sX hF) +
        perfectPowerSum C sX hF 0 * TotalChowClass.homComponent 2 (perfectChernClass C sX hE) +
        ofLocallyConstant C sX ((perfectRank E perfectE).map fun k ↦ Ring.choose k 2) *
          TotalChowClass.homComponent 1 (perfectChernClass C sX hF) ^ 2 +
        (perfectPowerSum C sX hE 0 * perfectPowerSum C sX hF 0 - 1) *
          (TotalChowClass.homComponent 1 (perfectChernClass C sX hF) *
            TotalChowClass.homComponent 1 (perfectChernClass C sX hE)) +
        ofLocallyConstant C sX ((perfectRank F perfectF).map fun k ↦ Ring.choose k 2) *
          TotalChowClass.homComponent 1 (perfectChernClass C sX hE) ^ 2
```

**`Stacks.Chow.exists_tensorSplitCharts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectTensorChernClasses.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectTensorChernClasses.lean#L228). The attribute's comment: “and so on for higher Chern classes: the splitting-principle statement the proof reduces the lemma to. On tensor split charts of any two envelope presentations of E and F -- the connected component of a point of the common envelope followed by one splitting morphism of 02UL for the terms of both presenting complexes -- restriction is injective on A^*(X), c(E) and c(F) are the products of (1 + x)^{(-1)^n} and (1 + y)^{(-1)^m} over their Chern roots, and c(E tensor^L F) is the product of (1 + x + y)^{(-1)^n (-1)^m} over all pairs of roots, as lists of signed roots via Stacks.Chow.TotalChowClass.rootProd and Stacks.Chow.rootTensor”.

> The Chern roots of `E ⊗^𝐋 F` are the sums of the Chern roots of `E` and `F`. For
> presentations of `E` and `F` on envelopes there are tensor split charts at every point of their
> common envelope, restriction to all of them is injective on `A^*(X)`, and on each of them, with
> `x_{n,j}` the Chern roots of `E` and `y_{m,k}` those of `F`,
>
>   `c(E) = ∏ (1 + x_{n,j})^{(-1)^n}`,  `c(F) = ∏ (1 + y_{m,k})^{(-1)^m}`,
>   `c(E ⊗^𝐋 F) = ∏ (1 + x_{n,j} + y_{m,k})^{(-1)^n (-1)^m}`,
>
> so every Chern class of `E ⊗^𝐋 F` is the universal expression in the Chern roots of `E` and `F`.

```lean
theorem exists_tensorSplitCharts (hE : HasDefinedChernClasses E) (hF : HasDefinedChernClasses F)
    (H : EnvelopePresentation E) (H' : EnvelopePresentation F) :
    ∃ χ : ∀ y : (H.tensorLeft H').Y, TensorSplitChart C sX H H' y,
      Function.Injective
        (fun (c : TotalChowClass C sX) (y : (H.tensorLeft H').Y) ↦ (χ y).left.res c) ∧
      (∀ y, (χ y).left.res (perfectChernClass C sX hE) =
        ((TotalChowClass.rootProd (χ y).rootsLeft : (TotalChowClass C (χ y).T.sP)ˣ) :
          TotalChowClass C (χ y).T.sP)) ∧
      (∀ y, (χ y).left.res (perfectChernClass C sX hF) =
        ((TotalChowClass.rootProd (χ y).rootsRight : (TotalChowClass C (χ y).T.sP)ˣ) :
          TotalChowClass C (χ y).T.sP)) ∧
      ∀ y, (χ y).left.res (perfectChernClass C sX (hasDefinedChernClasses_derivedTensor hE hF)) =
        ((TotalChowClass.rootProd (rootTensor (χ y).rootsLeft (χ y).rootsRight) :
          (TotalChowClass C (χ y).T.sP)ˣ) : TotalChowClass C (χ y).T.sP)
```

**`Stacks.Chow.homComponent_one_perfectChernClass_derivedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectTensorChernClasses.lean, line 254](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectTensorChernClasses.lean#L254). The attribute's comment: “the first displayed formula c_1(E tensor^L F) = r(E) c_1(F) + r(F) c_1(E), as classes homogeneous of degree one in the bivariant ring A^*(X) = Stacks.Chow.TotalChowClass, with r = Stacks.Chow.perfectRankClass and c_1 the degree-one homogeneous component of Stacks.Chow.perfectChernClass; the Chern classes of E tensor^L F are defined by Stacks.Chow.hasDefinedChernClasses_derivedTensor. Perfectness of E and F is not used”.

> `c₁(E ⊗^𝐋 F) = r(E) c₁(F) + r(F) c₁(E)` in `A^*(X)`.

```lean
theorem homComponent_one_perfectChernClass_derivedTensor (hE : HasDefinedChernClasses E)
    (hF : HasDefinedChernClasses F) :
    TotalChowClass.homComponent 1
        (perfectChernClass C sX (hasDefinedChernClasses_derivedTensor hE hF)) =
      perfectRankClass C sX hE * TotalChowClass.homComponent 1 (perfectChernClass C sX hF) +
        perfectRankClass C sX hF * TotalChowClass.homComponent 1 (perfectChernClass C sX hE)
```

**`Stacks.Chow.homComponent_two_perfectChernClass_derivedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectTensorChernClasses.lean, line 278](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectTensorChernClasses.lean#L278). The attribute's comment: “the second displayed formula c_2(E tensor^L F) = r(E) c_2(F) + r(F) c_2(E) + binom(r(E), 2) c_1(F)^2 + (r(E) r(F) - 1) c_1(F) c_1(E) + binom(r(F), 2) c_1(E)^2, as classes homogeneous of degree two in the bivariant ring A^*(X) = Stacks.Chow.TotalChowClass, the products being compositions of bivariant classes, in the order of the source. r is Stacks.Chow.perfectRankClass and binom(r, 2) is Stacks.Chow.perfectRankChooseClass ... 2, the class which is binom(n, 2) on the open and closed locus where the rank of the perfect object is n; E and F perfect as in the source”.

> `c₂(E ⊗^𝐋 F) = r(E) c₂(F) + r(F) c₂(E) + C(r(E), 2) c₁(F)² + (r(E) r(F) - 1) c₁(F) c₁(E)
> + C(r(F), 2) c₁(E)²` in `A^*(X)`.

```lean
theorem homComponent_two_perfectChernClass_derivedTensor
    (perfectE : RingedSpace.IsPerfect.{u, u + 1} (X := X.toRingedSpace) E)
    (perfectF : RingedSpace.IsPerfect.{u, u + 1} (X := X.toRingedSpace) F)
    (hE : HasDefinedChernClasses E) (hF : HasDefinedChernClasses F) :
    TotalChowClass.homComponent 2
        (perfectChernClass C sX (hasDefinedChernClasses_derivedTensor hE hF)) =
      perfectRankClass C sX hE * TotalChowClass.homComponent 2 (perfectChernClass C sX hF) +
        perfectRankClass C sX hF * TotalChowClass.homComponent 2 (perfectChernClass C sX hE) +
        perfectRankChooseClass C sX perfectE 2 *
          TotalChowClass.homComponent 1 (perfectChernClass C sX hF) ^ 2 +
        (perfectRankClass C sX hE * perfectRankClass C sX hF - 1) *
          (TotalChowClass.homComponent 1 (perfectChernClass C sX hF) *
            TotalChowClass.homComponent 1 (perfectChernClass C sX hE)) +
        perfectRankChooseClass C sX perfectF 2 *
          TotalChowClass.homComponent 1 (perfectChernClass C sX hE) ^ 2
```

**`Stacks.Chow.perfectChernClass_derivedTensor_apply_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectTensorChernClasses.lean, line 317](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectTensorChernClasses.lean#L317). The attribute's comment: “the first displayed formula read in the single group A^1(X): c_1(E tensor^L F) in A^1(X), the degree-one component of Stacks.Chow.perfectChernClass, is the degree-one component of r(E) c_1(F) + r(F) c_1(E)”.

> The class `c₁(E ⊗^𝐋 F) ∈ A¹(X)` is the degree-one component of
> `r(E) c₁(F) + r(F) c₁(E)`.

```lean
theorem perfectChernClass_derivedTensor_apply_one (hE : HasDefinedChernClasses E)
    (hF : HasDefinedChernClasses F) :
    perfectChernClass C sX (hasDefinedChernClasses_derivedTensor hE hF) 1 =
      (perfectRankClass C sX hE * TotalChowClass.homComponent 1 (perfectChernClass C sX hF) +
        perfectRankClass C sX hF * TotalChowClass.homComponent 1 (perfectChernClass C sX hE))
        1
```

**`Stacks.Chow.perfectChernClass_derivedTensor_apply_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectTensorChernClasses.lean, line 333](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectTensorChernClasses.lean#L333). The attribute's comment: “the second displayed formula read in the single group A^2(X): c_2(E tensor^L F) in A^2(X), the degree-two component of Stacks.Chow.perfectChernClass, is the degree-two component of r(E) c_2(F) + r(F) c_2(E) + binom(r(E), 2) c_1(F)^2 + (r(E) r(F) - 1) c_1(F) c_1(E) + binom(r(F), 2) c_1(E)^2; E and F perfect as in the source”.

> The class `c₂(E ⊗^𝐋 F) ∈ A²(X)` is the degree-two component of
> `r(E) c₂(F) + r(F) c₂(E) + C(r(E), 2) c₁(F)² + (r(E) r(F) - 1) c₁(F) c₁(E) + C(r(F), 2) c₁(E)²`.

```lean
theorem perfectChernClass_derivedTensor_apply_two
    (perfectE : RingedSpace.IsPerfect.{u, u + 1} (X := X.toRingedSpace) E)
    (perfectF : RingedSpace.IsPerfect.{u, u + 1} (X := X.toRingedSpace) F)
    (hE : HasDefinedChernClasses E) (hF : HasDefinedChernClasses F) :
    perfectChernClass C sX (hasDefinedChernClasses_derivedTensor hE hF) 2 =
      (perfectRankClass C sX hE * TotalChowClass.homComponent 2 (perfectChernClass C sX hF) +
        perfectRankClass C sX hF * TotalChowClass.homComponent 2 (perfectChernClass C sX hE) +
        perfectRankChooseClass C sX perfectE 2 *
          TotalChowClass.homComponent 1 (perfectChernClass C sX hF) ^ 2 +
        (perfectRankClass C sX hE * perfectRankClass C sX hF - 1) *
          (TotalChowClass.homComponent 1 (perfectChernClass C sX hF) *
            TotalChowClass.homComponent 1 (perfectChernClass C sX hE)) +
        perfectRankChooseClass C sX perfectF 2 *
          TotalChowClass.homComponent 1 (perfectChernClass C sX hE) ^ 2 : TotalChowClass C sX)
        2
```

**`Stacks.Chow.perfectPowerSumComponent_derivedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectTensorChernClasses.lean, line 356](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectTensorChernClasses.lean#L356). The attribute's comment: “the more precise statement read in the single group A^p(X), which is where the source states it: P_p(E tensor^L F) in A^p(X) (Stacks.Chow.perfectPowerSumComponent) is the degree-p component of the sum over p_1 + p_2 = p of binom(p, p_1) P_{p_1}(E) P_{p_2}(F)”.

> `P_p(E ⊗^𝐋 F) ∈ A^p(X)` is the degree-`p` component of
> `∑_{p₁ + p₂ = p} C(p, p₁) P_{p₁}(E) P_{p₂}(F)`.

```lean
theorem perfectPowerSumComponent_derivedTensor (hE : HasDefinedChernClasses E)
    (hF : HasDefinedChernClasses F) (p : ℕ) :
    perfectPowerSumComponent C sX (hasDefinedChernClasses_derivedTensor hE hF) p =
      ∑ q ∈ antidiagonal p, ((p.choose q.1 : TotalChowClass C sX) *
        (perfectPowerSum C sX hE q.1 * perfectPowerSum C sX hF q.2)) p
```

**`Stacks.Chow.perfectTotalChernCharacter_derivedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectTensorChernClasses.lean, line 446](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectTensorChernClasses.lean#L446). The attribute's comment: “similarly, ch(E tensor^L F) = ch(E) ch(F) in A^*(X) tensor Q: Stacks.Chow.rationalTotalChowClass is the bivariant ring A^*(X) tensored over Z with Q, and ch is the power series over it whose coefficient of degree p is P_p/p!, which read in A^p(X) tensor Q is ch_p of Tag 0F9E (Stacks.Chow.map_coeff_perfectTotalChernCharacter); the identity is the more precise one for P_p divided by p!. Perfectness of E and F is not used”.

> The Chern character is multiplicative: `ch(E ⊗^𝐋 F) = ch(E) ch(F)` in `A^*(X) ⊗ 𝐐`.

```lean
theorem perfectTotalChernCharacter_derivedTensor (hE : HasDefinedChernClasses E)
    (hF : HasDefinedChernClasses F) :
    perfectTotalChernCharacter C sX (hasDefinedChernClasses_derivedTensor hE hF) =
      perfectTotalChernCharacter C sX hE * perfectTotalChernCharacter C sX hF
```

**`Stacks.Chow.perfectChernClasses_derivedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectTensorChernClasses.lean, line 481](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PerfectTensorChernClasses.lean#L481). The attribute's comment: “the whole statement, as one conjunction of the parts registered separately in this module: the Chern classes of E tensor^L F are defined; the formulas for c_1 and c_2 in A^*(X); the splitting-principle form of 'and so on for higher Chern classes' (Chern roots x + y with product signs on injective tensor split charts of any presentations); ch(E tensor^L F) = ch(E) ch(F) in A^*(X) tensor Q; and P_p(E tensor^L F) = sum of binom(p, p_1) P_{p_1}(E) P_{p_2}(F) in A^p(X) for every p, under exactly the source's hypotheses”.

> In Situation 02QL let `X` be locally of finite type over `S` and let `E`,
> `F` be perfect objects of `D(𝒪_X)` whose Chern classes are defined. Then the Chern classes of
> `E ⊗^𝐋 F` are defined, and in `A^*(X)`
>
> * `c₁(E ⊗^𝐋 F) = r(E) c₁(F) + r(F) c₁(E)`;
> * `c₂(E ⊗^𝐋 F) = r(E) c₂(F) + r(F) c₂(E) + C(r(E), 2) c₁(F)² + (r(E) r(F) - 1) c₁(F) c₁(E)
>   + C(r(F), 2) c₁(E)²`;
> * "and so on for higher Chern classes": on tensor split charts of any presentations, on which
>   restriction is injective, the Chern roots of `E ⊗^𝐋 F` are the sums `x + y` of those of `E` and
>   `F`, with the product signs;
> * `ch(E ⊗^𝐋 F) = ch(E) ch(F)` in `A^*(X) ⊗ 𝐐`;
> * more precisely `P_p(E ⊗^𝐋 F) = ∑_{p₁ + p₂ = p} C(p, p₁) P_{p₁}(E) P_{p₂}(F)` in `A^p(X)`.

```lean
theorem perfectChernClasses_derivedTensor
    (perfectE : RingedSpace.IsPerfect.{u, u + 1} (X := X.toRingedSpace) E)
    (perfectF : RingedSpace.IsPerfect.{u, u + 1} (X := X.toRingedSpace) F)
    (hE : HasDefinedChernClasses E) (hF : HasDefinedChernClasses F) :
    HasDefinedChernClasses (((derivedTensorProductFunctor X.sheaf).obj E).obj F) ∧
    TotalChowClass.homComponent 1
        (perfectChernClass C sX (hasDefinedChernClasses_derivedTensor hE hF)) =
      perfectRankClass C sX hE * TotalChowClass.homComponent 1 (perfectChernClass C sX hF) +
        perfectRankClass C sX hF * TotalChowClass.homComponent 1 (perfectChernClass C sX hE) ∧
    TotalChowClass.homComponent 2
        (perfectChernClass C sX (hasDefinedChernClasses_derivedTensor hE hF)) =
      perfectRankClass C sX hE * TotalChowClass.homComponent 2 (perfectChernClass C sX hF) +
        perfectRankClass C sX hF * TotalChowClass.homComponent 2 (perfectChernClass C sX hE) +
        perfectRankChooseClass C sX perfectE 2 *
          TotalChowClass.homComponent 1 (perfectChernClass C sX hF) ^ 2 +
        (perfectRankClass C sX hE * perfectRankClass C sX hF - 1) *
          (TotalChowClass.homComponent 1 (perfectChernClass C sX hF) *
            TotalChowClass.homComponent 1 (perfectChernClass C sX hE)) +
        perfectRankChooseClass C sX perfectF 2 *
          TotalChowClass.homComponent 1 (perfectChernClass C sX hE) ^ 2 ∧
    (∀ (H : EnvelopePresentation E) (H' : EnvelopePresentation F),
      ∃ χ : ∀ y : (H.tensorLeft H').Y, TensorSplitChart C sX H H' y,
        Function.Injective (fun (c : TotalChowClass C sX) (y : (H.tensorLeft H').Y) ↦
          (χ y).left.res c) ∧
        (∀ y, (χ y).left.res (perfectChernClass C sX hE) =
          ((TotalChowClass.rootProd (χ y).rootsLeft : (TotalChowClass C (χ y).T.sP)ˣ) :
            TotalChowClass C (χ y).T.sP)) ∧
        (∀ y, (χ y).left.res (perfectChernClass C sX hF) =
          ((TotalChowClass.rootProd (χ y).rootsRight : (TotalChowClass C (χ y).T.sP)ˣ) :
            TotalChowClass C (χ y).T.sP)) ∧
        ∀ y, (χ y).left.res (perfectChernClass C sX (hasDefinedChernClasses_derivedTensor hE hF)) =
          ((TotalChowClass.rootProd (rootTensor (χ y).rootsLeft (χ y).rootsRight) :
            (TotalChowClass C (χ y).T.sP)ˣ) : TotalChowClass C (χ y).T.sP)) ∧
    perfectTotalChernCharacter C sX (hasDefinedChernClasses_derivedTensor hE hF) =
      perfectTotalChernCharacter C sX hE * perfectTotalChernCharacter C sX hF ∧
    ∀ p : ℕ, perfectPowerSumComponent C sX (hasDefinedChernClasses_derivedTensor hE hF) p =
      ∑ q ∈ antidiagonal p, ((p.choose q.1 : TotalChowClass C sX) *
        (perfectPowerSum C sX hE q.1 * perfectPowerSum C sX hF q.2)) p
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.46, Tag 0ESY](https://stacks.math.columbia.edu/tag/0ESY)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
