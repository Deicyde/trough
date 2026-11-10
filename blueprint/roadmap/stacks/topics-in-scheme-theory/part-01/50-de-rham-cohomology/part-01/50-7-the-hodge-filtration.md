---
declaration: section
origin: cited
lean: AlgebraicGeometry.SheafOfModules.hodgeFiltrationCup, AlgebraicGeometry.SheafOfModules.truncatedDeRhamCohomologyAbelianMap_hodgeFiltrationCup, AlgebraicGeometry.SheafOfModules.deRhamCup_mem_hodgeFiltrationAbelian, AlgebraicGeometry.SheafOfModules.exists_hodgeFiltrationSpectralSequence_iso_cartanEilenbergFirst, AlgebraicGeometry.SheafOfModules.deRhamStupidSubcomplex_antitone, AlgebraicGeometry.SheafOfModules.deRhamStupidSubcomplex_zero, AlgebraicGeometry.SheafOfModules.deRhamStupidGradedPieceDerivedIso, AlgebraicGeometry.SheafOfModules.exists_hodgeToDeRhamSpectralSequence
statement: formalized
proof: formalized
---

# 50.7 The Hodge filtration

Section 50.7 of the Stacks Project, [Tag 0FM7](https://stacks.math.columbia.edu/tag/0FM7). 2 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FM7, the section

[Tag 0FM7](https://stacks.math.columbia.edu/tag/0FM7) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.hodgeFiltrationCup`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/HodgeFiltration/CanonicalCupProduct.lean, line 425](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/HodgeFiltration/CanonicalCupProduct.lean#L425). The attribute's comment: “Section 50.7, the top row of the displayed diagram: the cup products H^n(X, σ^{≥i}Ω^•) × H^m(X, σ^{≥j}Ω^•) ⟶ H^{n+m}(X, σ^{≥(i+j)}Ω^•), the cup product of Cohomology Section 0FKU (the global cup product of the ringed space (X, A) built from the canonical one-point comparison) along the multiplication Tot(σ^{≥i}Ω^• ⊗ σ^{≥j}Ω^•) ⟶ σ^{≥(i+j)}Ω^• that the wedge product of 0FM2 restricts to”.

> **The cup product of Section 50.7 on the hypercohomology of the brutal truncations**,
>
> `H^n(X, σ^{≥i}Ω^•_{X/S}) × H^m(X, σ^{≥j}Ω^•_{X/S}) ⟶ H^{n + m}(X, σ^{≥(i + j)}Ω^•_{X/S})`:
>
> the cup product of Cohomology, Section 0FKU along the multiplication
> `Tot(σ^{≥i}Ω^• ⊗_A σ^{≥j}Ω^•) ⟶ σ^{≥(i + j)}Ω^•` that the wedge product of Tag 0FM2 restricts to,
> `AlgebraicGeometry.SheafOfModules.hodgeFiltrationWedge`.

```lean
def hodgeFiltrationCup (p q i j : ℤ) :
    truncatedDeRhamCohomologyAbelian B D p i → truncatedDeRhamCohomologyAbelian B D q j →
      truncatedDeRhamCohomologyAbelian B D (p + q) (i + j)
```

**`AlgebraicGeometry.SheafOfModules.truncatedDeRhamCohomologyAbelianMap_hodgeFiltrationCup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/HodgeFiltration/CanonicalCupProduct.lean, line 446](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/HodgeFiltration/CanonicalCupProduct.lean#L446). The attribute's comment: “Section 50.7, the commutative diagram it displays, with no parameter: the maps H^n(X, σ^{≥p}Ω^•) ⟶ H^n_dR(X/S) induced by the inclusions σ^{≥p}Ω^• ⟶ Ω^• carry the cup product H^n(X, σ^{≥i}Ω^•) × H^m(X, σ^{≥j}Ω^•) ⟶ H^{n+m}(X, σ^{≥(i+j)}Ω^•) to the cup product on H^*_dR(X/S), both cup products being those of Cohomology Section 0FKU”.

> **The commutative diagram of Section 50.7**: the maps
> `H^n(X, σ^{≥p}Ω^•_{X/S}) ⟶ H^n_{dR}(X/S)` induced by the inclusions of the brutal truncations
> carry the cup product on the brutal truncations to the cup product on de Rham cohomology.

```lean
theorem truncatedDeRhamCohomologyAbelianMap_hodgeFiltrationCup (p q i j : ℤ)
    (x : truncatedDeRhamCohomologyAbelian B D p i)
    (y : truncatedDeRhamCohomologyAbelian B D q j) :
    (truncatedDeRhamCohomologyAbelianMap B D (p + q) (i + j)).hom
        (hodgeFiltrationCup B D p q i j x y) =
      deRhamCup B D i j ((truncatedDeRhamCohomologyAbelianMap B D p i).hom x)
        ((truncatedDeRhamCohomologyAbelianMap B D q j).hom y)
```

**`AlgebraicGeometry.SheafOfModules.deRhamCup_mem_hodgeFiltrationAbelian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/HodgeFiltration/CanonicalCupProduct.lean, line 465](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/HodgeFiltration/CanonicalCupProduct.lean#L465). The attribute's comment: “Section 50.7, its last assertion, with no parameter: the Hodge filtration is multiplicative for the cup product of Cohomology Section 0FKU on de Rham cohomology, F^i H^n_dR(X/S) ∪ F^j H^m_dR(X/S) ⊂ F^{i+j} H^{n+m}_dR(X/S)”.

> **The Hodge filtration is multiplicative**, the last assertion of Section 50.7:
>
> `F^iH^n_{dR}(X/S) ∪ F^jH^m_{dR}(X/S) ⊂ F^{i + j}H^{n + m}_{dR}(X/S)`
>
> for the cup product of Cohomology, Section 0FKU on de Rham cohomology. Membership in a step of
> the filtration `AlgebraicGeometry.SheafOfModules.hodgeFiltrationAbelian` of Tag 0FM8, a subobject
> of `H^n_{dR}`, means being the image of an element of that subobject.

```lean
theorem deRhamCup_mem_hodgeFiltrationAbelian (p q i j : ℤ)
    (x : deRhamCohomologyAbelian B D i) (y : deRhamCohomologyAbelian B D j)
    (hx : ∃ u : (hodgeFiltrationAbelian B D p i : AddCommGrpCat.{u}),
      ((hodgeFiltrationAbelian B D p i).arrow).hom u = x)
    (hy : ∃ v : (hodgeFiltrationAbelian B D q j : AddCommGrpCat.{u}),
      ((hodgeFiltrationAbelian B D q j).arrow).hom v = y) :
    ∃ w : (hodgeFiltrationAbelian B D (p + q) (i + j) : AddCommGrpCat.{u}),
      ((hodgeFiltrationAbelian B D (p + q) (i + j)).arrow).hom w = deRhamCup B D i j x y
```

**`AlgebraicGeometry.SheafOfModules.exists_hodgeFiltrationSpectralSequence_iso_cartanEilenbergFirst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/HodgeFiltration/CanonicalCupProduct.lean, line 488](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/HodgeFiltration/CanonicalCupProduct.lean#L488). The attribute's comment: “Section 50.7: the spectral sequence of Cohomology Lemma 0BKK for Ω^•_{X/S} viewed as a filtered complex (by its brutal truncations) is the same as the Hodge-to-de Rham spectral sequence of Section 0FM6, i.e. the first spectral sequence of Derived Categories Lemma 015J built from a Cartan-Eilenberg resolution of Ω^•_{X/S}: one package, bounded, converging to the hypercohomology of Ω^•_{X/S}, and isomorphic to the first spectral sequence of every Cartan-Eilenberg resolution (Cohomology Example 0FLK)”. References: SGA 7 XXII (3.3), “more general”.

> **The spectral sequence of the Hodge filtration is the Hodge-to-de Rham spectral sequence of
> Section 0FM6.** The spectral sequence of Cohomology, Lemma 0BKK for `Ω^•_{X/S}` filtered by its
> brutal truncations is bounded, converges to the hypercohomology of `Ω^•_{X/S}`, and is isomorphic
> to the first spectral sequence of every Cartan-Eilenberg resolution of `Ω^•_{X/S}`
> (Derived Categories, Lemma 015J), which is how Section 0FM6 constructs the Hodge-to-de Rham
> spectral sequence; this is Cohomology, Example 0FLK, clause (3), for the de Rham complex.

```lean
theorem exists_hodgeFiltrationSpectralSequence_iso_cartanEilenbergFirst :
    ∃ S : Stacks.Cohomology.FilteredComplex.StupidTruncationSpectralSequence
        (baseRingedSpace A) (deRhamComplexInt (X := X) B D),
      IsBounded S.spectralSequence ∧
      SpectralSequence.AbutsTo S.spectralSequence (fun n =>
        Stacks.Cohomology.FilteredComplex.hypercohomology (baseRingedSpace A) S.RΓ
          (deRhamComplexInt (X := X) B D) n) ∧
      ∀ I : (deRhamComplexInt (X := X) B D).CartanEilenbergResolution,
        Nonempty (S.spectralSequence ≅
          Stacks.Cohomology.FilteredComplex.cartanEilenbergFirstSpectralSequence
            (baseRingedSpace A) I)
```

**`AlgebraicGeometry.SheafOfModules.deRhamStupidSubcomplex_antitone`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/HodgeFiltration/HodgeToDeRhamSpectralSequence.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/HodgeFiltration/HodgeToDeRhamSpectralSequence.lean#L147). The attribute's comment: “the brutal truncations are subcomplexes of the relative de Rham complex and form a decreasing filtration of it, the chain Ω^• = σ^{≥0}Ω^• ⊃ σ^{≥1}Ω^• ⊃ σ^{≥2}Ω^• ⊃ ⋯; this is the decreasing half, that σ^{≥q}Ω^• ⊆ σ^{≥p}Ω^• for p ≤ q”.

> The brutal truncations form a **decreasing** chain of subcomplexes of the de Rham complex:
> `σ^{≥1}Ω^• ⊃ σ^{≥2}Ω^• ⊃ ⋯`, because for `p ≤ q` the inclusion of `σ^{≥q}Ω^•` factors through
> `σ^{≥p}Ω^•`.

```lean
theorem deRhamStupidSubcomplex_antitone : Antitone (deRhamStupidSubcomplex B D)
```

**`AlgebraicGeometry.SheafOfModules.deRhamStupidSubcomplex_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/HodgeFiltration/HodgeToDeRhamSpectralSequence.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/HodgeFiltration/HodgeToDeRhamSpectralSequence.lean#L172). The attribute's comment: “the chain Ω^• = σ^{≥0}Ω^• ⊃ σ^{≥1}Ω^• ⊃ ⋯ starts at the de Rham complex itself: the equality Ω^•_{X/S} = σ^{≥0}Ω^•_{X/S} at the left end of the display”.

> The chain of brutal truncations starts at the de Rham complex itself:
> `Ω^•_{𝒪_X/A} = σ^{≥0}Ω^•_{𝒪_X/A}`, because the de Rham complex is concentrated in nonnegative
> degrees.

```lean
theorem deRhamStupidSubcomplex_zero : deRhamStupidSubcomplex B D 0 = ⊤
```

**`AlgebraicGeometry.SheafOfModules.deRhamStupidGradedPieceDerivedIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/HodgeFiltration/HodgeToDeRhamSpectralSequence.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/HodgeFiltration/HodgeToDeRhamSpectralSequence.lean#L200). The attribute's comment: “gr^p(Ω^•_{X/S}) = Ω^p_{X/S}[-p], the identification of the graded pieces of the brutal filtration of the relative de Rham complex”.

> **`gr^p(Ω^•_{𝒪_X/A}) = Ω^p_{𝒪_X/A}[-p]`.** In the derived category of sheaves of
> `A`-modules the `p`-th graded piece of the brutal filtration of the de Rham complex is the sheaf
> `Ω^p_{𝒪_X/A}` of relative `p`-forms, shifted down by `p`.

```lean
def deRhamStupidGradedPieceDerivedIso (p : ℕ) :
    DerivedCategory.Q.obj ((FilteredObject.gr (p : ℤ)).obj
        (CochainComplex.stupidTruncationFiltration (deRhamComplexInt (X := X) B D))) ≅
      ((DerivedCategory.singleFunctor _ 0).obj ((deRhamComplex B D).X p))⟦(-(p : ℤ))⟧
```

**`AlgebraicGeometry.SheafOfModules.exists_hodgeToDeRhamSpectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/HodgeFiltration/HodgeToDeRhamSpectralSequence.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/HodgeFiltration/HodgeToDeRhamSpectralSequence.lean#L290). The attribute's comment: “the spectral sequence of Cohomology Lemma 0BKK for Ω^•_{X/S} viewed as a filtered complex of sheaves is the Hodge-to-de Rham spectral sequence built by Cohomology Example 0FLK: one object, carrying the Tag 0FLK first page E_1^{p,q} = H^q(X, Ω^p), bounded, abutting to H^n_dR(X/S), and converging along the Hodge filtration of Tag 0FM8. Its first page is identified term by term with the abelian-sheaf first page `hodgeToDeRhamFirstPage` of Section 0FM6; the differentials d_1 of the two first pages are not compared”. References: SGA 7 XXII (3.3), “more general”.

> **The Hodge-to-de Rham spectral sequence of the brutal filtration of the de Rham complex.**
>
> Read `Ω^•_{𝒪_X/A}` as a filtered complex of sheaves through its brutal truncations
> `σ^{≥p}Ω^•_{𝒪_X/A}`. Its spectral sequence in the sense of [Stacks, Tag 0BKK] exists — through
> the bounded-below form [Stacks, Tag 0BKL], the de Rham complex being concentrated in nonnegative
> degrees — and comes packaged as a
> `Stacks.Cohomology.FilteredComplex.StupidTruncationSpectralSequence`, the brutal-truncation
> spectral sequence of [Stacks, Tag 0FLK], whose `e₁Iso` field is the first-page formula
> `E_1^{p, q} = H^q(X, Ω^p_{𝒪_X/A})` of the Hodge-to-de Rham spectral sequence of Section 50.6. So
> the two spectral sequences of Section 50.7's third assertion are one object, constructed once.
>
> It is **bounded**, it **abuts to relative de Rham cohomology** `H^n_{dR}(X/A)`, and the
> filtration of the abutment along which it converges is the **Hodge filtration**
> `AlgebraicGeometry.SheafOfModules.hodgeFiltration` of [Stacks, Tag 0FM8]: the last conjunct
> identifies `E_∞^{p, q}` with `F^pH^{p + q}_{dR} / F^{p + 1}H^{p + q}_{dR}`.
>
> The fourth conjunct reads the first page in the abelian-sheaf realization: with the `A(X)`-module
> structure forgotten, `E_1^{p, q}` is the term in position `p` of
> `AlgebraicGeometry.SheafOfModules.hodgeToDeRhamFirstPage B D q`, the `q`-th row of the first page
> of Section 50.6.

```lean
theorem exists_hodgeToDeRhamSpectralSequence :
    ∃ S : Stacks.Cohomology.FilteredComplex.StupidTruncationSpectralSequence
        (baseRingedSpace A) (deRhamComplexInt (X := X) B D),
      IsBounded S.spectralSequence ∧
      SpectralSequence.AbutsTo S.spectralSequence (deRhamCohomology (X := X) B D) ∧
      (∀ n : ℤ, ∃ a b : ℤ, a ≤ b ∧ hodgeFiltration B D a n = ⊤ ∧
        hodgeFiltration B D b n = ⊥) ∧
      (∀ p q : ℕ, Nonempty
        ((forget₂ (ModuleCat.{u} ((underlyingRingSheaf A).obj.obj (op ⊤))) AddCommGrpCat.{u}).obj
            (((Stacks.Cohomology.FilteredComplex.globalSectionsSpectralSequence
                (baseRingedSpace A) S.replacement).page 1 (by omega)).X ((p : ℤ), (q : ℤ))) ≅
          (hodgeToDeRhamFirstPage B D q).X p)) ∧
      ∀ p q : ℤ, Nonempty (S.spectralSequence.pageInfinity (p, q) ≅
        cokernel (Subobject.ofLE (hodgeFiltration B D (p + 1) (p + q))
          (hodgeFiltration B D p (p + q))
          (hodgeFiltration_antitone B D (p + q) (by omega))))
```

**`AlgebraicGeometry.SheafOfModules.hodgeFiltrationWedge`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/HodgeFiltration/Multiplicativity.lean, line 284](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/HodgeFiltration/Multiplicativity.lean#L284). The attribute's comment: “the wedge product of equation 0FM2 sends Tot(σ^{≥i}Ω^•_{X/S} ⊗_{p⁻¹𝒪_S} σ^{≥j}Ω^•_{X/S}) into σ^{≥(i+j)}Ω^•_{X/S}: the multiplication of the Hodge filtration on complexes. One assertion of the section; the hypercohomology diagrams it leads to are registered on `truncatedDeRhamCohomologyAbelianMap_hodgeFiltrationCup` and `deRhamCup_mem_hodgeFiltrationAbelian`, and the filtration, its graded pieces and its spectral sequence on the declarations named in this file's module docstring”.

> **The multiplication of the Hodge filtration**
>
> `Tot(σ^{≥i}Ω^•_{𝒪_X/A} ⊗_A σ^{≥j}Ω^•_{𝒪_X/A}) ⟶ σ^{≥(i + j)}Ω^•_{𝒪_X/A}`
>
> induced by the wedge product of Tag 0FM2: the restriction of `∧` to the brutal truncations lands
> in the `(i + j)`-th step of the filtration, because its source vanishes in every lower degree
> (`AlgebraicGeometry.SheafOfModules.isZero_truncatedTensorSquare_X`).

```lean
def hodgeFiltrationWedge (i j : ℕ) :
    truncatedTensorSquare B D i j ⟶ deRhamBrutal B D (i + j)
```

**`AlgebraicGeometry.SheafOfModules.hodgeFiltrationWedge_ιBrutal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/HodgeFiltration/Multiplicativity.lean, line 296](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/HodgeFiltration/Multiplicativity.lean#L296). The attribute's comment: “that the morphism Tot(σ^{≥i}Ω^• ⊗ σ^{≥j}Ω^•) ⟶ σ^{≥(i+j)}Ω^• of the previous declaration really is the wedge product of equation 0FM2, i.e. that it lies over ∧ under the inclusion σ^{≥(i+j)}Ω^• ⟶ Ω^•. Without this the previous declaration would be some morphism into the (i+j)-th step rather than the section's assertion about ∧”.

> **The multiplication of the Hodge filtration is the wedge product**: composing it with the
> inclusion `σ^{≥(i + j)}Ω^• ⟶ Ω^•_{𝒪_X/A}` returns `∧` restricted to the truncations.

```lean
theorem hodgeFiltrationWedge_ιBrutal (i j : ℕ) :
    hodgeFiltrationWedge B D i j ≫ CochainComplex.ιBrutal (deRhamComplex B D) (i + j) =
      truncatedWedge B D i j
```

## Tag 0FM8, a definition

[Tag 0FM8](https://stacks.math.columbia.edu/tag/0FM8) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.hodgeFiltration`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/HodgeFiltration/Basic.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/HodgeFiltration/Basic.lean#L145).

> **The Hodge filtration** on relative de Rham cohomology: the `p`-th step
> `F^p H^n_{dR} = Im (H^n(X, σ^{≥p}Ω^•) ⟶ H^n_{dR})` is the image of the hypercohomology of the
> brutal truncation `σ^{≥p}Ω^•` of the de Rham complex, under the map induced by the inclusion of
> that truncation.

```lean
def hodgeFiltration (p n : ℤ) : Subobject (deRhamCohomology B D n)
```

**`AlgebraicGeometry.SheafOfModules.hodgeFiltrationAbelian`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/HodgeFiltration/Basic.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/HodgeFiltration/Basic.lean#L200). The attribute's comment: “abelian-sheaf realization in every degree”.

> **The Hodge filtration** on relative de Rham cohomology in the abelian-sheaf realization, in
> every degree: the image of the hypercohomology of the brutal truncation `σ^{≥p}Ω^•` under the map
> induced by its inclusion into the de Rham complex.

```lean
def hodgeFiltrationAbelian (p n : ℤ) : Subobject (deRhamCohomologyAbelian B D n)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 50.7, Tag 0FM7](https://stacks.math.columbia.edu/tag/0FM7)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
