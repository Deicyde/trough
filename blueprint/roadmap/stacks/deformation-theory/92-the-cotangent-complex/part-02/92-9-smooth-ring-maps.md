---
declaration: section
origin: cited
lean: CommAlgCat.nonempty_cotangentComplexDerived_iso_kaehlerDifferential_of_isStandardSmooth, CommAlgCat.nonempty_cotangentComplexDerived_iso_kaehlerDifferential_of_isStandardSmooth_unconditional, CommAlgCat.nonempty_cotangentComplexDerived_iso_kaehlerDifferential_of_etale, CommAlgCat.nonempty_cotangentComplexDerived_iso_kaehlerDifferential_of_etale_unconditional, CommAlgCat.isZero_homology_cotangentComplex_of_smooth_unconditional, CommAlgCat.cotangentComplexDerivedIsoKaehlerDifferentialOfSmoothUnconditional, CommAlgCat.isZero_homology_cotangentComplex_of_smooth, CommAlgCat.cotangentComplexDerivedIsoKaehlerDifferentialOfSmooth
statement: formalized
proof: formalized
---

# 92.9 Smooth ring maps

Section 92.9 of the Stacks Project, [Tag 08R4](https://stacks.math.columbia.edu/tag/08R4). 2 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08R4, the section

[Tag 08R4](https://stacks.math.columbia.edu/tag/08R4) in the Stacks Project.

**`CommAlgCat.nonempty_cotangentComplexDerived_iso_kaehlerDifferential_of_isStandardSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SmoothRingMap.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SmoothRingMap.lean#L331). The attribute's comment: “the SECTION tag `\section{Smooth ring maps}`; its lemma is 08R5”.

> **Stacks Project, Tag 08R5** for a standard smooth ring map, and the covering declaration
> for the section tag **08R4**.
>
> Let `A → B` be standard smooth. Then `L_{B/A} = Ω[B⁄A][0]` in `D(B)`.
>
> The chart `A → A[x_1, …, x_n] → B` with étale second map is *built*, not assumed: it is Mathlib's
> `RingHom.IsStandardSmooth.exists_etale_mvPolynomial`, which is the content of the source's appeal
> to Algebra, Lemma 00TA. The conclusion is then
> `CommAlgCat.nonempty_cotangentComplexDerived_iso_kaehlerDifferential_of_etale`.
>
> One hypothesis is carried, `hQX : CommAlgCat.HasFundamentalTriangles`, which is Proposition 08QX
> — the display of Equation 92.7.0.1 is a distinguished triangle for every tower of ring maps.
> Proposition 08QX is not formalized in this library (see the `No @[stacks 08QX]` section of
> `StacksFrontier.Cotangent.Triangle.Distinguished`) and no `@[stacks 08QX]` attribute is claimed for
> it here. It is carried as the whole proposition rather than as named instances because the two
> towers it is needed for — `A → A[x_1, …, x_n] → B` and `B → B ⊗_{A[x_1, …, x_n]} B → B` — are
> built inside the proof and so cannot be referred to in the statement.
>
> This is **not** the full smooth case of Lemma 08R5. Lemma 00TA is available, and gives a standard
> open cover of `Spec(B)` on which a smooth `A → B` is standard smooth, so this result applies to
> each `B_g`; what is missing is `L_{B_g/A} = (L_{B/A})_g`, which needs Lemma 08R2 item (3), and
> descent along the cover in `D(B)`. See the module docstring.

```lean
theorem nonempty_cotangentComplexDerived_iso_kaehlerDifferential_of_isStandardSmooth
    [Algebra.IsStandardSmooth A B] (hQX : HasFundamentalTriangles.{u}) :
    Nonempty
      (cotangentComplexDerived.{u, u} A (CommAlgCat.of A B) ≅
        (DerivedCategory.singleFunctor (ModuleCat.{u} B) 0).obj
          (ModuleCat.of B (KaehlerDifferential A B)))
```

**`CommAlgCat.nonempty_cotangentComplexDerived_iso_kaehlerDifferential_of_isStandardSmooth_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SmoothUnconditional.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SmoothUnconditional.lean#L122). The attribute's comment: “the SECTION tag `\section{Smooth ring maps}`; its lemma is 08R5”.

> **Stacks Project, Tag 08R5** for a standard smooth ring map, and the covering declaration
> for the section tag **08R4**. This is
> `CommAlgCat.nonempty_cotangentComplexDerived_iso_kaehlerDifferential_of_isStandardSmooth` with
> Proposition 08QX supplied by `CommAlgCat.hasFundamentalTriangles`.

```lean
theorem nonempty_cotangentComplexDerived_iso_kaehlerDifferential_of_isStandardSmooth_unconditional
    [Algebra.IsStandardSmooth A B] :
    Nonempty
      (cotangentComplexDerived.{u, u} A (CommAlgCat.of A B) ≅
        (DerivedCategory.singleFunctor (ModuleCat.{u} B) 0).obj
          (ModuleCat.of B (KaehlerDifferential A B)))
```

## Tag 08R5, a lemma

[Tag 08R5](https://stacks.math.columbia.edu/tag/08R5) in the Stacks Project.

**`CommAlgCat.nonempty_cotangentComplexDerived_iso_kaehlerDifferential_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SmoothRingMap.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SmoothRingMap.lean#L228). The attribute's comment: “the lemma for a ring map `A → B` presented by a CHART: a factorization `A → P → B` with `P` a polynomial algebra over `A` and `P → B` étale. This is the lemma from which the standard-smooth case is deduced in `CommAlgCat.nonempty_cotangentComplexDerived_iso_kaehlerDifferential_of_isStandardSmooth`, which carries the 08R4 tag as well; neither is the FULL SMOOTH case, the localization step of the source's proof being unavailable (it needs Lemma 08R2 item (3), which `StacksFrontier.Cotangent.EtaleVanishing` records as not claimed, and a Zariski-descent statement in `D(B)`). TWO carried hypotheses, both instances of Proposition 08QX (NOT formalized here, and no `@[stacks 08QX]` is claimed): `hT`, the fundamental triangle of `A → P → B`, which Lemma 08R3 consumes, and `hT'`, the fundamental triangle of `B → B ⊗_P B → B`, which `CommAlgCat.isZero_cotangentComplexDerived_of_etale` (Lemma 08R2 item (5)) already carries and which is passed through. The conclusion is the source's, `L_{B/A} = Ω_{B/A}[0]`, read as an isomorphism in `D(B)` in the same spelling as Tag 08QH”.

> **Stacks Project, Tag 08R5**, for a ring map presented by a chart.
>
> Let `A → P → B` be ring maps with `P` a polynomial algebra over `A` and `P → B` étale. Then
> `L_{B/A} = Ω[B⁄A][0]` in `D(B)`.
>
> This is the lemma the standard smooth case is deduced from in
> `CommAlgCat.nonempty_cotangentComplexDerived_iso_kaehlerDifferential_of_isStandardSmooth`, where
> the chart is built rather than assumed. It is kept separate because its carried hypotheses are
> two named instances of Proposition 08QX rather than the whole proposition, and because
> `Algebra.IsPolynomialAlgebra` allows an arbitrary type of variables, so the hypothesis here is
> not merely the standard smooth case.
>
> Two hypotheses are carried, and both are instances of Proposition 08QX, which is not formalized
> in this library (see the `No @[stacks 08QX]` section of
> `StacksFrontier.Cotangent.Triangle.Distinguished`); no `@[stacks 08QX]` is claimed anywhere here.
>
> * `hT` is the distinguished triangle of the display of Equation 92.7.0.1 for the tower
>   `A → P → B`. It is what Lemma 08R3 consumes, in the form
>   `CommAlgCat.nonempty_fundamentalVertex₁_iso_fundamentalVertex₂_of_isZero`, to turn
>   `L_{B/P} = 0` into `L_{B/A} = L_{P/A} ⊗^𝐋_P B`. Proposition 08QX would discharge it.
> * `hT'` is the distinguished triangle of the same display for the tower `B → B ⊗_P B → B`. It is
>   the hypothesis that `CommAlgCat.isZero_cotangentComplexDerived_of_etale` — Lemma 08R2 item (5)
>   — already carries, on its way through Lemma 08R1, and it is passed straight through.
>   Proposition 08QX would discharge it too.
>
> The hypothesis `hP` and the instance `Algebra.Etale P B` are both load-bearing: `hP` is the
> input to Lemma 08QH and the source of the projectivity of `Ω[P⁄A]` that makes the termwise
> extension of scalars compute the derived one, and étaleness supplies both the vanishing of
> `L_{B/P}` through Lemma 08R2 item (5) and, through
> `KaehlerDifferential.tensorKaehlerEquivOfFormallyEtale`, the identification of `B ⊗_P Ω[P⁄A]`
> with `Ω[B⁄A]`.

```lean
theorem nonempty_cotangentComplexDerived_iso_kaehlerDifferential_of_etale
    (hP : Algebra.IsPolynomialAlgebra A P) [Algebra.Etale P B]
    {α : fundamentalVertex₁.{u, u} A P B ⟶ fundamentalVertex₂.{u, u} A B}
    {β : fundamentalVertex₂.{u, u} A B ⟶ fundamentalVertex₃.{u, u} P B}
    {γ : fundamentalVertex₃.{u, u} P B ⟶ (fundamentalVertex₁.{u, u} A P B)⟦(1 : ℤ)⟧}
    (hT : Triangle.mk α β γ ∈ distTriang (DerivedCategory (ModuleCat.{u} B)))
    {α' : fundamentalVertex₁.{u, u} B (B ⊗[P] B) B ⟶ fundamentalVertex₂.{u, u} B B}
    {β' : fundamentalVertex₂.{u, u} B B ⟶ fundamentalVertex₃.{u, u} (B ⊗[P] B) B}
    {γ' : fundamentalVertex₃.{u, u} (B ⊗[P] B) B ⟶
      (fundamentalVertex₁.{u, u} B (B ⊗[P] B) B)⟦(1 : ℤ)⟧}
    (hT' : Triangle.mk α' β' γ' ∈ distTriang (DerivedCategory (ModuleCat.{u} B))) :
    Nonempty
      (cotangentComplexDerived.{u, u} A (CommAlgCat.of A B) ≅
        (DerivedCategory.singleFunctor (ModuleCat.{u} B) 0).obj
          (ModuleCat.of B (KaehlerDifferential A B)))
```

**`CommAlgCat.nonempty_cotangentComplexDerived_iso_kaehlerDifferential_of_isStandardSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SmoothRingMap.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SmoothRingMap.lean#L331). The attribute's comment: “the lemma for a STANDARD SMOOTH ring map, `Algebra.IsStandardSmooth A B`. The chart `A → A[x_1, …, x_n] → B` with étale second map is BUILT, not assumed — it is Mathlib's `RingHom.IsStandardSmooth.exists_etale_mvPolynomial`, which is the content of the source's appeal to Algebra, Lemma 00TA — and the conclusion then comes from `CommAlgCat.nonempty_cotangentComplexDerived_iso_kaehlerDifferential_of_etale`, which carries the 08R5 tag too. This is NOT the full smooth case: Lemma 00TA gives a cover of `Spec(B)` on which a smooth map is standard smooth, so this applies to each `B_g`, but `L_{B_g/A} = (L_{B/A})_g` needs Lemma 08R2 item (3) (which `StacksFrontier.Cotangent.EtaleVanishing` records as not claimed) and descent along the cover in `D(B)` is absent. ONE carried hypothesis, `hQX : CommAlgCat.HasFundamentalTriangles`, which is Proposition 08QX itself, carried whole rather than as instances because the towers it is needed for are built inside the proof; 08QX is NOT formalized in this library and no `@[stacks 08QX]` is claimed here. The conclusion is the source's, `L_{B/A} = Ω_{B/A}[0]`, read as an isomorphism in `D(B)` in the same spelling as Tag 08QH. As for 08R4: the section's only mathematical content is Lemma 08R5, so this declaration covers it; the definitional remark opening the section introduces `weakly quasi-regular` ring maps only to say what a generalization of Lemma 08R2 would look at, and the source then says `For the moment we just stick to smooth ring maps`, so it states no result and nothing is defined for it”.

> **Stacks Project, Tag 08R5** for a standard smooth ring map, and the covering declaration
> for the section tag **08R4**.
>
> Let `A → B` be standard smooth. Then `L_{B/A} = Ω[B⁄A][0]` in `D(B)`.
>
> The chart `A → A[x_1, …, x_n] → B` with étale second map is *built*, not assumed: it is Mathlib's
> `RingHom.IsStandardSmooth.exists_etale_mvPolynomial`, which is the content of the source's appeal
> to Algebra, Lemma 00TA. The conclusion is then
> `CommAlgCat.nonempty_cotangentComplexDerived_iso_kaehlerDifferential_of_etale`.
>
> One hypothesis is carried, `hQX : CommAlgCat.HasFundamentalTriangles`, which is Proposition 08QX
> — the display of Equation 92.7.0.1 is a distinguished triangle for every tower of ring maps.
> Proposition 08QX is not formalized in this library (see the `No @[stacks 08QX]` section of
> `StacksFrontier.Cotangent.Triangle.Distinguished`) and no `@[stacks 08QX]` attribute is claimed for
> it here. It is carried as the whole proposition rather than as named instances because the two
> towers it is needed for — `A → A[x_1, …, x_n] → B` and `B → B ⊗_{A[x_1, …, x_n]} B → B` — are
> built inside the proof and so cannot be referred to in the statement.
>
> This is **not** the full smooth case of Lemma 08R5. Lemma 00TA is available, and gives a standard
> open cover of `Spec(B)` on which a smooth `A → B` is standard smooth, so this result applies to
> each `B_g`; what is missing is `L_{B_g/A} = (L_{B/A})_g`, which needs Lemma 08R2 item (3), and
> descent along the cover in `D(B)`. See the module docstring.

```lean
theorem nonempty_cotangentComplexDerived_iso_kaehlerDifferential_of_isStandardSmooth
    [Algebra.IsStandardSmooth A B] (hQX : HasFundamentalTriangles.{u}) :
    Nonempty
      (cotangentComplexDerived.{u, u} A (CommAlgCat.of A B) ≅
        (DerivedCategory.singleFunctor (ModuleCat.{u} B) 0).obj
          (ModuleCat.of B (KaehlerDifferential A B)))
```

**`CommAlgCat.nonempty_cotangentComplexDerived_iso_kaehlerDifferential_of_etale_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SmoothUnconditional.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SmoothUnconditional.lean#L87). The attribute's comment: “the lemma for a ring map `A → B` presented by a CHART: a factorization `A → P → B` with `P` a polynomial algebra over `A` and `P → B` étale. NOTHING is carried: the fundamental triangles of `A → P → B` and of `B → B ⊗_P B → B` are both Proposition 08QX, `CommAlgCat.productFundamentalTriangle_distinguished`. The conclusion is the source's, `L_{B/A} = Ω_{B/A}[0]`, read as an isomorphism in `D(B)` in the same spelling as Tag 08QH; the full smooth case is `CommAlgCat.cotangentComplexDerivedIsoKaehlerDifferentialOfSmoothUnconditional`”.

> **Stacks Project, Tag 08R5**, for a chart. Let `A → P → B` be ring maps with `P` a
> polynomial algebra over `A` and `P → B` étale. Then `L_{B/A} = Ω[B⁄A][0]` in `D(B)`.
>
> This is `CommAlgCat.nonempty_cotangentComplexDerived_iso_kaehlerDifferential_of_etale` at the
> fundamental triangles of the towers `A → P → B` and `B → B ⊗_P B → B` that Proposition 08QX
> provides.

```lean
theorem nonempty_cotangentComplexDerived_iso_kaehlerDifferential_of_etale_unconditional
    (hP : Algebra.IsPolynomialAlgebra A P) [Algebra.Etale P B] :
    Nonempty
      (cotangentComplexDerived.{u, u} A (CommAlgCat.of A B) ≅
        (DerivedCategory.singleFunctor (ModuleCat.{u} B) 0).obj
          (ModuleCat.of B (KaehlerDifferential A B)))
```

**`CommAlgCat.nonempty_cotangentComplexDerived_iso_kaehlerDifferential_of_isStandardSmooth_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SmoothUnconditional.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SmoothUnconditional.lean#L122). The attribute's comment: “the lemma for a STANDARD SMOOTH ring map, `Algebra.IsStandardSmooth A B`. The chart `A → A[x_1, …, x_n] → B` with étale second map is BUILT, not assumed — it is Mathlib's `RingHom.IsStandardSmooth.exists_etale_mvPolynomial`, which is the content of the source's appeal to Algebra, Lemma 00TA. NOTHING is carried: the towers the fundamental triangle is needed for are built inside the proof and Proposition 08QX, `CommAlgCat.productFundamentalTriangle_distinguished`, holds at each of them. The full smooth case is `CommAlgCat.cotangentComplexDerivedIsoKaehlerDifferentialOfSmoothUnconditional`. The conclusion is the source's, `L_{B/A} = Ω_{B/A}[0]`, read as an isomorphism in `D(B)` in the same spelling as Tag 08QH. As for 08R4: the section's only mathematical content is Lemma 08R5, so this declaration covers it; the definitional remark opening the section introduces `weakly quasi-regular` ring maps only to say what a generalization of Lemma 08R2 would look at, and the source then says `For the moment we just stick to smooth ring maps`, so it states no result and nothing is defined for it”.

> **Stacks Project, Tag 08R5** for a standard smooth ring map, and the covering declaration
> for the section tag **08R4**. This is
> `CommAlgCat.nonempty_cotangentComplexDerived_iso_kaehlerDifferential_of_isStandardSmooth` with
> Proposition 08QX supplied by `CommAlgCat.hasFundamentalTriangles`.

```lean
theorem nonempty_cotangentComplexDerived_iso_kaehlerDifferential_of_isStandardSmooth_unconditional
    [Algebra.IsStandardSmooth A B] :
    Nonempty
      (cotangentComplexDerived.{u, u} A (CommAlgCat.of A B) ≅
        (DerivedCategory.singleFunctor (ModuleCat.{u} B) 0).obj
          (ModuleCat.of B (KaehlerDifferential A B)))
```

**`CommAlgCat.isZero_homology_cotangentComplex_of_smooth_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SmoothUnconditional.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SmoothUnconditional.lean#L142). The attribute's comment: “the vanishing: `Hⁱ(L_{B/A}) = 0` for every `i ≠ 0`, which together with Tag 08QF in degree 0 is the lemma. NOTHING is carried: the fundamental triangle is Tag 08QX, `CommAlgCat.productFundamentalTriangle_distinguished`, applied at each of the towers the proof produces”.

> **[Stacks, Tag 08R5], the vanishing.** For a smooth ring map `A → B`, `Hⁱ(L_{B/A}) = 0` for
> `i ≠ 0`. This is `CommAlgCat.isZero_homology_cotangentComplex_of_smooth` with Proposition 08QX
> supplied by `CommAlgCat.hasFundamentalTriangle`.

```lean
theorem isZero_homology_cotangentComplex_of_smooth_unconditional
    (A : Type u) [CommRing A] (B : Type u) [CommRing B] [Algebra A B] [Algebra.Smooth A B]
    (i : ℤ) (hi : i ≠ 0) :
    IsZero ((cotangentComplex A (CommAlgCat.of A B)).homology i)
```

**`CommAlgCat.cotangentComplexDerivedIsoKaehlerDifferentialOfSmoothUnconditional`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SmoothUnconditional.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SmoothUnconditional.lean#L157). The attribute's comment: “the lemma in full and as data: the isomorphism `L_{B/A} ≅ Ω[B⁄A][0]` in `D(B)`, for a SMOOTH ring map and with NOTHING carried — the fundamental triangle is Tag 08QX, `CommAlgCat.productFundamentalTriangle_distinguished`. Nothing beyond smoothness is assumed, and the conclusion is the source's whole equality rather than only its degree 0 part”.

> **[Stacks, Tag 08R5].** For a smooth ring map `A → B`, the identification
> `L_{B/A} ≅ Ω[B⁄A][0]` in `D(B)` of the cotangent complex with the module of Kähler
> differentials placed in cohomological degree `0`. This is
> `CommAlgCat.cotangentComplexDerivedIsoKaehlerDifferentialOfSmooth` with Proposition 08QX
> supplied by `CommAlgCat.hasFundamentalTriangle`.

```lean
noncomputable def cotangentComplexDerivedIsoKaehlerDifferentialOfSmoothUnconditional
    (A : Type u) [CommRing A] (B : Type u) [CommRing B] [Algebra A B] [Algebra.Smooth A B] :
    cotangentComplexDerived.{u, u} A (CommAlgCat.of A B) ≅
      (DerivedCategory.singleFunctor (ModuleCat.{u} B) 0).obj
        (ModuleCat.of B (KaehlerDifferential A B))
```

**`CommAlgCat.isZero_homology_cotangentComplex_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SmoothVanishing.lean, line 258](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SmoothVanishing.lean#L258). The attribute's comment: “the vanishing: `Hⁱ(L_{B/A}) = 0` for every `i ≠ 0`, which together with Tag 08QF in degree 0 is the lemma. One carried hypothesis `h08QX`: Tag 08QX, that the fundamental triangle is distinguished, which is not formalized in this library; it is quantified over towers because the towers are produced by the proof itself and cannot be enumerated”.

> **[Stacks, Tag 08R5], the vanishing.** For a smooth ring map `A → B` the cotangent complex
> `L_{B/A}` has no cohomology outside degree `0`.
>
> A smooth ring map is standard smooth on a cover of `Spec B` by basic opens, [Stacks, Tag 00TA],
> and the cohomology of `L_{B/A}` is a `B`-module whose localizations along that cover vanish.

```lean
theorem isZero_homology_cotangentComplex_of_smooth (h08QX : HasFundamentalTriangle.{u})
    (A : Type u) [CommRing A] (B : Type u) [CommRing B] [Algebra A B] [Algebra.Smooth A B]
    (i : ℤ) (hi : i ≠ 0) :
    IsZero ((cotangentComplex A (CommAlgCat.of A B)).homology i)
```

**`CommAlgCat.cotangentComplexDerivedIsoKaehlerDifferentialOfSmooth`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SmoothVanishing.lean, line 277](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SmoothVanishing.lean#L277). The attribute's comment: “the lemma in full and as data: the isomorphism `L_{B/A} ≅ Ω[B⁄A][0]` in `D(B)`. One carried hypothesis `h08QX`: Tag 08QX, not formalized in this library. Nothing else is assumed, and the conclusion is the source's whole equality rather than only its degree 0 part”.

> **[Stacks, Tag 08R5].** For a smooth ring map `A → B`, the identification
> `L_{B/A} ≅ Ω[B⁄A][0]` in `D(B)` of the cotangent complex with the module of Kähler
> differentials placed in cohomological degree `0`.
>
> The cohomology vanishes outside degree `0` and is `Ω[B⁄A]` in degree `0` by [Stacks, Tag 08QF],
> so the t-structure on `D(B)` exhibits `L_{B/A}` as a single module in degree `0`.

```lean
noncomputable def cotangentComplexDerivedIsoKaehlerDifferentialOfSmooth
    (h08QX : HasFundamentalTriangle.{u}) (A : Type u) [CommRing A] (B : Type u) [CommRing B]
    [Algebra A B] [Algebra.Smooth A B] :
    cotangentComplexDerived.{u, u} A (CommAlgCat.of A B) ≅
      (DerivedCategory.singleFunctor (ModuleCat.{u} B) 0).obj
        (ModuleCat.of B (KaehlerDifferential A B))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 92.9, Tag 08R4](https://stacks.math.columbia.edu/tag/08R4)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
