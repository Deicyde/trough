---
declaration: section
origin: cited
lean: Stacks.Chow.regularTameSymbolOfKrullDimOne, Stacks.Chow.tameSymbolOfKrullDimOne, Stacks.Chow.normPushforwardOfIsIntegrallyClosed, Stacks.Chow.tameSymbolOfFiniteIntegralClosure, Stacks.Chow.tameSymbol_apply_eq_of_tameSymbolPreparation, Stacks.Chow.normPushforward_apply_eq_of_tameSymbolPreparation, Stacks.Chow.normPushforwardOfIsIntegrallyClosed_apply_eq_symbolValue, Stacks.Chow.normPushforwardOfFiniteIntegralClosure_apply_eq_symbolValue
statement: formalized
proof: formalized
---

# 42.5 Tame symbols

Section 42.5 of the Stacks Project, [Tag 0EAH](https://stacks.math.columbia.edu/tag/0EAH). 7 tags here are carried by 34 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EAH, the section

[Tag 0EAH](https://stacks.math.columbia.edu/tag/0EAH) in the Stacks Project.

**`Stacks.Chow.regularTameSymbolOfKrullDimOne`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/KrullDimOne.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/KrullDimOne.lean#L213). The attribute's comment: “on nonzerodivisors, for every one-dimensional Noetherian local ring”.

> The tame symbol of a one-dimensional Noetherian local ring `A` on pairs of nonzerodivisors:
> the symbol of Stacks 02PZ on the module `A` itself, which satisfies Stacks 0EAL, 0EAM, 0EAN and
> 0EAP.

```lean
noncomputable def regularTameSymbolOfKrullDimOne : RegularTameSymbol A
```

**`Stacks.Chow.tameSymbolOfKrullDimOne`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/KrullDimOne.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/KrullDimOne.lean#L239). The attribute's comment: “on Q(A)^*, for every one-dimensional Noetherian local ring”.

> The tame symbol `∂_A : Q(A)^* × Q(A)^* → κ(𝔪)^*` of a one-dimensional Noetherian local
> ring `A`, satisfying Stacks 0EAI, 0EAJ and 0EAK: the extension
> (`Stacks.Chow.RegularTameSymbol.extend`) of the symbol of Stacks 02PZ on pairs of
> nonzerodivisors.

```lean
noncomputable def tameSymbolOfKrullDimOne (Q : Type v) [CommRing Q] [Algebra A Q]
    [IsFractionRing A Q] : TameSymbol A Q
```

**`Stacks.Chow.normPushforwardOfIsIntegrallyClosed`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/NormalModification.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/NormalModification.lean#L160). The attribute's comment: “on nonzerodivisors, for a local domain with a normal finite modification”.

> The tame symbol on nonzerodivisors of a one-dimensional Noetherian local domain `A` with a
> normal finite modification: for `A ⊆ B` module-finite with `B` an integrally closed domain and
> `B/A` annihilated by a power of `𝔪`,
>
> `∂_A(a, b) = ∏_𝔮 Norm_{κ(𝔮)/κ(𝔪)}(∂_{B_𝔮}(a, b))`,
>
> the product over the maximal ideals `𝔮` of `B`.

```lean
noncomputable def normPushforwardOfIsIntegrallyClosed (hA : ¬ IsField A)
    (hinj : Function.Injective (algebraMap A B))
    (hquot : ∃ n : ℕ, maximalIdeal A ^ n • (⊤ : Submodule A B) ≤
      LinearMap.range (Algebra.linearMap A B)) :
    RegularTameSymbol A
```

**`Stacks.Chow.tameSymbolOfFiniteIntegralClosure`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/NormalModification.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/NormalModification.lean#L246). The attribute's comment: “on Q(A)^*, for a local domain with a module-finite integral closure”.

> The tame symbol `∂_A : Q(A)^* × Q(A)^* → κ(𝔪)^*` of a one-dimensional Noetherian local domain
> `A` whose integral closure in its fraction field is module finite: the extension
> `Stacks.Chow.RegularTameSymbol.extend` of `Stacks.Chow.normPushforwardOfFiniteIntegralClosure`.

```lean
noncomputable def tameSymbolOfFiniteIntegralClosure (hA : ¬ IsField A)
    (Q : Type*) [CommRing Q] [Algebra A Q] [IsFractionRing A Q] : TameSymbol A Q
```

## Tag 0EAQ, an equation

[Tag 0EAQ](https://stacks.math.columbia.edu/tag/0EAQ) in the Stacks Project.

**`Stacks.Chow.tameSymbol_apply_eq_of_tameSymbolPreparation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/KeyLemma/TameSymbolPreparationValue.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/KeyLemma/TameSymbolPreparationValue.lean#L82). The attribute's comment: “the factor at a single maximal ideal”.

> **The tame symbol on a localization of a tame-symbol preparation.** At a maximal ideal `q` of
> the finite extension produced by Stacks 0EAG, two members of the prepared family are unit multiples
> of powers of the common parameter, with unit parts units of `B_q`; so the symbol of the two is
>
> `∂_{B_q}(a i, a j) = ((-1) ^ (e_i e_j) ū_i ^ (e_j) v̄_j ^ (-e_i)) ^ m`,
> `m = length_{B_q}(B_q / π_q B_q)`,
>
> by Stacks 0EAL, 0EAM and 0EAN. The unit parts of a preparation are units of the very ring carrying
> the symbol, so this is `Stacks.Chow.RegularTameSymbol.apply_eq_of_factorization` applied directly;
> no passage between units of the base and units of a localization is involved.

```lean
theorem tameSymbol_apply_eq_of_tameSymbolPreparation
    {A : Type u} [CommRing A] [IsLocalRing A] {B : Type v} [CommRing B] [Algebra A B]
    {r : ℕ} {a : Fin r → A} (P : TameSymbolPreparation a B)
    (q : Ideal B) [q.IsMaximal]
    [IsNoetherianRing (Localization.AtPrime q)] [Ring.KrullDimLE 1 (Localization.AtPrime q)]
    (symb : RegularTameSymbol (Localization.AtPrime q))
    (i j : Fin r) (x y : nonZeroDivisors (Localization.AtPrime q))
    (hx : (x : Localization.AtPrime q) = algebraMap A (Localization.AtPrime q) (a i))
    (hy : (y : Localization.AtPrime q) = algebraMap A (Localization.AtPrime q) (a j)) :
    symb x y =
      ((-1) ^ (P.exponent q i * P.exponent q j) *
          Units.map (residue (Localization.AtPrime q)).toMonoidHom (P.factorUnit q i) ^
            P.exponent q j *
          (Units.map (residue (Localization.AtPrime q)).toMonoidHom
            (P.factorUnit q j))⁻¹ ^ P.exponent q i) ^
        (Ring.ord (Localization.AtPrime q) (P.parameter q)).toNat
```

**`Stacks.Chow.normPushforward_apply_eq_of_tameSymbolPreparation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/KeyLemma/TameSymbolPreparationValue.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/KeyLemma/TameSymbolPreparationValue.lean#L115). The attribute's comment: “the product over the maximal ideals”.

> **The tame symbol pushed back from a tame-symbol preparation to its base, evaluated on the
> preparation's data.** The norm pushforward of Stacks 0EAT assembles the symbols on the
> localizations of a finite extension into a symbol on the base; on the output of Stacks 0EAG each of
> those symbols is the formula of
> `Stacks.Chow.tameSymbol_apply_eq_of_tameSymbolPreparation`, so the symbol on the base is the
> product of the norms of those formulas.
>
> This is the passage the proof of Stacks 0EAW makes from the prepared finite extension back to the
> ring it began with. The order-of-vanishing form of it, which is what that proof actually uses,
> needs Algebra 02MJ at the residue fields and is not proved here.

```lean
theorem normPushforward_apply_eq_of_tameSymbolPreparation
    {A : Type u} [CommRing A] [IsNoetherianRing A] [IsLocalRing A] [Ring.KrullDimLE 1 A]
    {B : Type v} [CommRing B] [Algebra A B] [Module.Finite A B]
    [Fintype (MaximalSpectrum B)]
    [∀ q : MaximalSpectrum B, IsLocalHom (algebraMap A (Localization.AtPrime q.asIdeal))]
    [∀ q : MaximalSpectrum B, IsNoetherianRing (Localization.AtPrime q.asIdeal)]
    [∀ q : MaximalSpectrum B, Ring.KrullDimLE 1 (Localization.AtPrime q.asIdeal)]
    (hass : ¬ IsAssociatedPrime (maximalIdeal A) B)
    (symb : ∀ q : MaximalSpectrum B, RegularTameSymbol (Localization.AtPrime q.asIdeal))
    (hinj : Function.Injective (algebraMap A B))
    (hquot : ∃ n : ℕ, maximalIdeal A ^ n • (⊤ : Submodule A B) ≤
      LinearMap.range (Algebra.linearMap A B))
    {r : ℕ} {a : Fin r → A} (P : TameSymbolPreparation a B) (i j : Fin r)
    (x y : nonZeroDivisors A) (hx : (x : A) = a i) (hy : (y : A) = a j) :
    normPushforward hass symb hinj hquot x y =
      ∏ q : MaximalSpectrum B,
        Units.map (Algebra.norm (ResidueField A) :
            ResidueField (Localization.AtPrime q.asIdeal) →* ResidueField A)
          (((-1) ^ (P.exponent q.asIdeal i * P.exponent q.asIdeal j) *
              Units.map (residue (Localization.AtPrime q.asIdeal)).toMonoidHom
                (P.factorUnit q.asIdeal i) ^ P.exponent q.asIdeal j *
              (Units.map (residue (Localization.AtPrime q.asIdeal)).toMonoidHom
                (P.factorUnit q.asIdeal j))⁻¹ ^ P.exponent q.asIdeal i) ^
            (Ring.ord (Localization.AtPrime q.asIdeal) (P.parameter q.asIdeal)).toNat)
```

**`Stacks.Chow.normPushforwardOfIsIntegrallyClosed_apply_eq_symbolValue`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/DefiningFormula.lean, line 263](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/DefiningFormula.lean#L263). The attribute's comment: “for the tame symbol of a normal finite modification, on a preparation over that modification”.

> **Stacks 0EAQ for the tame symbol of a normal finite modification.** Let `(A, 𝔪)` be a
> one-dimensional Noetherian local domain that is not a field and let `A ⊆ B` be module finite with
> `B` an integrally closed domain and `B/A` annihilated by a power of `𝔪`. Let `P` be a
> tame-symbol preparation of a family `a` over `B`, as produced by Stacks 0EAG: a local parameter
> `π_𝔮` at each maximal ideal of `B` together with factorizations `a_i = u_{i, 𝔮} π_𝔮^{e_{i, 𝔮}}`
> in `B_𝔮`. Then for two members `a i`, `a j` of the family, both nonzerodivisors of `A`,
>
> `∂_A(a i, a j) = ∏_𝔮 Norm_{κ(𝔮)/κ(𝔪)}((-1)^{e_i e_j} ū_i^{e_j} ū_j^{-e_i})^{m_𝔮}`,
>
> `m_𝔮 = length_{B_𝔮}(B_𝔮 / π_𝔮 B_𝔮)`, which is the displayed equation of the source.
>
> `∂_A` on the left is this development's tame symbol
> `Stacks.Chow.normPushforwardOfIsIntegrallyClosed`, not a symbol carried as a hypothesis: the
> family of symbols on the localizations is the canonical one of a discrete valuation ring, and the
> three remaining hypotheses of `Stacks.Chow.normPushforward_apply_eq_symbolValue` are consequences
> of the finiteness of `A → B`.

```lean
theorem normPushforwardOfIsIntegrallyClosed_apply_eq_symbolValue
    [Fintype (MaximalSpectrum B)]
    [∀ q : MaximalSpectrum B, IsLocalHom (algebraMap A (Localization.AtPrime q.asIdeal))]
    (hA : ¬ IsField A) (hinj : Function.Injective (algebraMap A B))
    (hquot : ∃ n : ℕ, maximalIdeal A ^ n • (⊤ : Submodule A B) ≤
      LinearMap.range (Algebra.linearMap A B))
    {r : ℕ} {a : Fin r → A} (P : TameSymbolPreparation a B) (i j : Fin r)
    (x y : nonZeroDivisors A) (hx : (x : A) = a i) (hy : (y : A) = a j) :
    normPushforwardOfIsIntegrallyClosed A B hA hinj hquot x y = P.symbolValue i j
```

**`Stacks.Chow.normPushforwardOfFiniteIntegralClosure_apply_eq_symbolValue`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/DefiningFormula.lean, line 322](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/DefiningFormula.lean#L322). The attribute's comment: “for the tame symbol on nonzerodivisors of A, on a preparation over the integral closure of A in its fraction field”.

> **Stacks 0EAQ for the tame symbol on nonzerodivisors of `A`.** With `B` the integral closure
> of `A` in its fraction field, the symbol of
> `Stacks.Chow.normPushforwardOfIsIntegrallyClosed` is
> `Stacks.Chow.normPushforwardOfFiniteIntegralClosure`, which depends on nothing but `A` and `K`;
> so the displayed equation of the source holds for it, on a preparation over that integral
> closure — for instance `Stacks.Chow.integralClosurePreparation`.

```lean
theorem normPushforwardOfFiniteIntegralClosure_apply_eq_symbolValue (hA : ¬ IsField A)
    {r : ℕ} {a : Fin r → A} (P : TameSymbolPreparation a (integralClosure A K)) (i j : Fin r)
    (x y : nonZeroDivisors A) (hx : (x : A) = a i) (hy : (y : A) = a j) :
    normPushforwardOfFiniteIntegralClosure A K hA x y = P.symbolValue i j
```

**`Stacks.Chow.tameSymbolOfFiniteIntegralClosure_apply_eq_symbolValue`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/DefiningFormula.lean, line 353](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/DefiningFormula.lean#L353). The attribute's comment: “for the tame symbol on Q(A)^*, on a preparation over the integral closure of A in its fraction field”.

> **Stacks 0EAQ, at the spelling of the source.** For a one-dimensional Noetherian local domain
> `A` that is not a field and whose integral closure in its fraction field is module finite, the
> tame symbol
>
> `∂_A : Q(A)^* × Q(A)^* → κ(𝔪)^*`
>
> of Stacks 0EAH — `Stacks.Chow.tameSymbolOfFiniteIntegralClosure` — is given on a pair of
> nonzerodivisors of `A` by the product of the source:
>
> `∂_A(a₁, a₂) = ∏_j Norm_{κ(𝔪_j)/κ(𝔪)}((-1)^{e_{1,j} e_{2,j}} u_{1,j}^{e_{2,j}} u_{2,j}^{-e_{1,j}}
>   mod 𝔪_j)^{m_j}`,
>
> computed from any tame-symbol preparation of the pair over the integral closure. The extension of
> a symbol on nonzerodivisors to `Q(A)^*` restricts back to it
> (`Stacks.Chow.RegularTameSymbol.extend_regularFractionUnit`), so this is the previous statement
> transported along `Stacks.Chow.regularFractionUnit`.

```lean
theorem tameSymbolOfFiniteIntegralClosure_apply_eq_symbolValue (hA : ¬ IsField A)
    (Q : Type*) [CommRing Q] [Algebra A Q] [IsFractionRing A Q]
    {r : ℕ} {a : Fin r → A} (P : TameSymbolPreparation a (integralClosure A K)) (i j : Fin r)
    (x y : nonZeroDivisors A) (hx : (x : A) = a i) (hy : (y : A) = a j) :
    tameSymbolOfFiniteIntegralClosure A K hA Q (regularFractionUnit x) (regularFractionUnit y) =
      P.symbolValue i j
```

**`Stacks.Chow.tameSymbolOfFiniteIntegralClosure_eq_symbolValue`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/DefiningFormula.lean, line 392](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/DefiningFormula.lean#L392). The attribute's comment: “unconditionally for a one-dimensional Noetherian local domain with a module-finite integral closure: the symbol of Stacks 0EAH on Q(A)^*, the canonical preparation on the integral closure, and no instance assumed that the finiteness of the extension does not supply”.

> **Stacks 0EAQ with nothing assumed beyond the hypotheses on `A`.** For a one-dimensional
> Noetherian local domain `A` that is not a field whose integral closure in its fraction field is
> module finite, and for any finite family `a` of nonzerodivisors of `A`,
>
> `∂_A(a i, a j) = ∏_j Norm_{κ(𝔪_j)/κ(𝔪)}((-1)^{e_{1,j} e_{2,j}} u_{1,j}^{e_{2,j}}
>   u_{2,j}^{-e_{1,j}} mod 𝔪_j)^{m_j}`,
>
> the preparation being the canonical one on the integral closure
> (`Stacks.Chow.integralClosurePreparation`) and the symbol being
> `Stacks.Chow.tameSymbolOfFiniteIntegralClosure`, the map
> `∂_A : Q(A)^* × Q(A)^* → κ(𝔪)^*` of Stacks 0EAH.
>
> Nothing here is a hypothesis that the finiteness of `A → B` does not already give: the maximal
> ideals of the integral closure are finite in number by
> `Stacks.Length.finite_maximalSpectrum`, each localization is local over `A` by
> `Stacks.Length.isLocalHom_algebraMap_localization`, and those are the two instances the product
> of the source needs in order to be written down at all. They are supplied in the statement rather
> than assumed, which is what distinguishes this from
> `Stacks.Chow.tameSymbolOfFiniteIntegralClosure_apply_eq_symbolValue`.

```lean
theorem tameSymbolOfFiniteIntegralClosure_eq_symbolValue (hA : ¬ IsField A)
    (Q : Type*) [CommRing Q] [Algebra A Q] [IsFractionRing A Q]
    {r : ℕ} (a : Fin r → A) (ha : ∀ i, a i ∈ nonZeroDivisors A) (i j : Fin r) :
    letI := Stacks.Length.finite_maximalSpectrum (A := A) (B := integralClosure A K)
    letI := Fintype.ofFinite (MaximalSpectrum (integralClosure A K))
    letI : ∀ q : MaximalSpectrum (integralClosure A K),
        IsLocalHom (algebraMap A (Localization.AtPrime q.asIdeal)) := fun q =>
      Stacks.Length.isLocalHom_algebraMap_localization q
    tameSymbolOfFiniteIntegralClosure A K hA Q
        (regularFractionUnit ⟨a i, ha i⟩) (regularFractionUnit ⟨a j, ha j⟩) =
      (integralClosurePreparation A K hA a ha).symbolValue i j
```

**`Stacks.Chow.tameSymbolFormula_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/Formula.lean, line 346](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/Formula.lean#L346). The attribute's comment: “the tame symbol defined by the formula from one admissible extension, and equal to the displayed product for every admissible extension A ⊆ B and every choice of local factorizations”.

> **Stacks 0EAQ.** Let `(A, 𝔪)` be a Noetherian local ring of dimension one and `a₁, a₂ ∈ A`
> nonzerodivisors. For every finite ring extension `A ⊆ B` with `B / A` annihilated by a power of
> `𝔪`, every choice of nonzerodivisors `π_j ∈ B_j = B_{𝔪_j}` at the maximal ideals `𝔪_j` of `B`,
> and every choice of factorizations `a_i = u_{i, j} π_j ^ {e_{i, j}}` in `B_j` with `u_{i, j}`
> units and `e_{i, j} ≥ 0` — the data of Stacks 0EAG, bundled as `P` — the tame symbol is
>
> `∂_A(a₁, a₂) = ∏_j Norm_{κ(𝔪_j)/κ(𝔪)}((-1)^{e_{1,j} e_{2,j}} u_{1,j}^{e_{2,j}} u_{2,j}^{-e_{1,j}}
>   mod 𝔪_j) ^ {m_j}`,  `m_j = length_{B_j}(B_j / π_j B_j)`,
>
> the product over the maximal ideals of `B`. The definition `Stacks.Chow.tameSymbolFormula` uses
> one such choice; that every other choice gives the same element is Stacks 0EAR,
> `AlgebraicGeometry.TameSymbolPreparation.symbolValue_eq_symbolValue`.

```lean
theorem tameSymbolFormula_eq (hdim : ringKrullDim A = 1) {a₁ a₂ : A}
    (ha₁ : IsRegular a₁) (ha₂ : IsRegular a₂) {B : Type v} [CommRing B] [Algebra A B]
    (P : TameSymbolPreparation ![a₁, a₂] B) :
    tameSymbolFormula hdim a₁ a₂ ha₁ ha₂ =
      ∏ᶠ q : MaximalSpectrum B,
        haveI := P.isLocalHom q
        Units.map (Algebra.norm (ResidueField A) :
            ResidueField (Localization.AtPrime q.asIdeal) →* ResidueField A)
          ((-1) ^ (P.exponent q.asIdeal 0 * P.exponent q.asIdeal 1) *
            Units.map (residue (Localization.AtPrime q.asIdeal)).toMonoidHom
              (P.factorUnit q.asIdeal 0) ^ P.exponent q.asIdeal 1 *
            (Units.map (residue (Localization.AtPrime q.asIdeal)).toMonoidHom
              (P.factorUnit q.asIdeal 1))⁻¹ ^ P.exponent q.asIdeal 0) ^
          (Module.length (Localization.AtPrime q.asIdeal)
            (Localization.AtPrime q.asIdeal ⧸ Ideal.span {P.parameter q.asIdeal})).toNat
```

## Tag 0EAR, a lemma

[Tag 0EAR](https://stacks.math.columbia.edu/tag/0EAR) in the Stacks Project.

**`AlgebraicGeometry.TameSymbolPreparation.symbolValue_eq_of_preparations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/Independence.lean, line 384](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/Independence.lean#L384). The attribute's comment: “both clauses for the whole symbol: the value of the formula of Stacks 0EAQ depends neither on the choice of the local factorizations nor on the choice of B. Two arbitrary extensions B and B' of A, in unrelated universes, each carrying its own preparation of the family, give the same value; the common refinement that compares them is CONSTRUCTED here, by Stacks.Chow.nonempty_commonRefinement, not supposed. The hypotheses are the source's own: A Noetherian local of Krull dimension at most one, and the family not all units, which is the standing context of Stacks 0EAG in which the formula is written. The factorization clause alone, at a single maximal ideal, is Stacks.Chow.factorizationValue_eq_of_factorizations”.

> **Stacks 0EAR.** Let `(A, 𝔪)` be a one-dimensional Noetherian local ring and let `a` be a
> family of elements of `A`, not all units, admitting a simultaneous power factorization after a
> finite modification — that is, a `AlgebraicGeometry.TameSymbolPreparation`, which Stacks 0EAG
> produces for any family of nonzerodivisors not all units. Then the right-hand side of the formula
> Stacks 0EAQ,
>
> `∏_𝔮 Norm_{κ(𝔮)/κ(𝔪)}((-1)^{e_i e_j} ū_i^{e_j} ū_j^{-e_i})^{m_𝔮}`,
>
> depends on neither the finite modification nor the factorizations: two preparations of the same
> family, over any two finite modifications, give the same element of `κ(𝔪)^*`.
>
> This is the source's proof. The two modifications `A ⊆ B` and `A ⊆ B'` are compared through the
> common refinement `C = (B ⊗_A B')/(𝔪`-power torsion`)`, built by
> `Stacks.Chow.nonempty_commonRefinement`; against `C` the comparison is
> `AlgebraicGeometry.TameSymbolPreparation.symbolValue_eq_of_common_refinement`, which regroups the
> product over the maximal ideals of `C` into a product over those of `B` by transitivity of norms
> (Stacks 0BIJ) and recognizes each fibre factor as the local factor of Stacks 0EAQ. The
> nonzerodivisor the refinement is built from is a nonunit member of the family itself, which the
> preparation makes regular
> (`AlgebraicGeometry.TameSymbolPreparation.algebraMap_mem_nonZeroDivisors`), and every hypothesis of
> Stacks 0EAT for `A ⊆ C` — at `A` and at each maximal ideal of `B` and of `B'` — is derived from
> that.
>
> Nothing is assumed. `AlgebraicGeometry.TameSymbolPreparation.symbolValue` cannot be written down
> without a `Fintype` on the maximal spectrum of its extension and the locality of the structure map
> at each maximal ideal, and those two are not hypotheses here either: each preparation proves them
> itself, by `AlgebraicGeometry.TameSymbolPreparation.finite_maximalSpectrum` and
> `AlgebraicGeometry.TameSymbolPreparation.isLocalHom`, and the statement below installs them from
> the preparations rather than binding them. No generality is lost by fixing the `Fintype`: a type
> has at most one of them (`Subsingleton (Fintype _)`), so the equation at the installed instance is
> the equation at every instance.

```lean
theorem symbolValue_eq_of_preparations (hunit : ¬ ∀ i, IsUnit (a i))
    {B : Type v} [CommRing B] [Algebra A B] {B' : Type w} [CommRing B'] [Algebra A B']
    (P : TameSymbolPreparation a B) (P' : TameSymbolPreparation a B') (i j : Fin r) :
    letI : Fintype (MaximalSpectrum B) := @Fintype.ofFinite _ P.finite_maximalSpectrum
    letI : ∀ q : MaximalSpectrum B,
      IsLocalHom (algebraMap A (Localization.AtPrime q.asIdeal)) := P.isLocalHom
    letI : Fintype (MaximalSpectrum B') := @Fintype.ofFinite _ P'.finite_maximalSpectrum
    letI : ∀ q : MaximalSpectrum B',
      IsLocalHom (algebraMap A (Localization.AtPrime q.asIdeal)) := P'.isLocalHom
    P.symbolValue i j = P'.symbolValue i j
```

**`Stacks.Chow.factorizationValue_eq_of_factorizations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/WellDefined.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/WellDefined.lean#L148). The attribute's comment: “independence of the choice of the local factorizations, at a single maximal ideal”.

> **Stacks 0EAR at a single maximal ideal: the formula Stacks 0EAQ does not depend on the chosen
> local factorization.** If the two elements `a₁`, `a₂` of a one-dimensional Noetherian local ring
> `R` admit simultaneous power factorizations against two nonzerodivisors `π` and `θ`,
>
> `a₁ = u₁ π^{e₁} = v₁ θ^{f₁}`,  `a₂ = u₂ π^{e₂} = v₂ θ^{f₂}`,
>
> with `u_i`, `v_i` units, then the two values of the formula agree.
>
> This is the source's argument. Multiplicativity of the order of vanishing gives
> `e_i m = f_i k` for `m = length_R(R/πR)` and `k = length_R(R/θR)`. Raising
> `u₂^{e₁} a₁^{e₂} = u₁^{e₂} a₂^{e₁}` to the `m`-th power and `v₂^{f₁} a₁^{f₂} = v₁^{f₂} a₂^{f₁}`
> to the `k`-th power and cancelling the nonzerodivisor `a₁^{e₂ m}` gives
> `(u₁^{e₂} u₂^{-e₁})^m = (v₁^{f₂} v₂^{-f₁})^k` already in `R`. The signs agree because
> `m e₁ e₂` is odd exactly when each of `m`, `e₁`, `e₂` is, and `e_i m = f_i k` turns that into
> the same statement for `k`, `f₁`, `f₂`.

```lean
theorem factorizationValue_eq_of_factorizations [IsNoetherianRing R] [Ring.KrullDimLE 1 R]
    {π θ : R} (hπ : π ∈ nonZeroDivisors R) (hθ : θ ∈ nonZeroDivisors R)
    {a₁ a₂ : R} {u₁ u₂ v₁ v₂ : Rˣ} {e₁ e₂ f₁ f₂ : ℕ}
    (hu₁ : a₁ = u₁ * π ^ e₁) (hu₂ : a₂ = u₂ * π ^ e₂)
    (hv₁ : a₁ = v₁ * θ ^ f₁) (hv₂ : a₂ = v₂ * θ ^ f₂) :
    factorizationValue π u₁ u₂ e₁ e₂ = factorizationValue θ v₁ v₂ f₁ f₂
```

**`AlgebraicGeometry.TameSymbolPreparation.symbolValue_eq_of_sameExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/WellDefined.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/WellDefined.lean#L265). The attribute's comment: “independence of the choice of the local factorizations; independence of the choice of B is not proved”.

> **Stacks 0EAR for the choice of local factorizations.** Two tame-symbol preparations of the
> same family over the *same* finite extension `A ⊆ B` differ only in the local parameters, unit
> parts and exponents they choose at each maximal ideal of `B`; by
> `Stacks.Chow.factorizationValue_eq_of_factorizations` each factor of the formula Stacks 0EAQ is
> unchanged, hence so is the product.
>
> Independence of the choice of `B` is not proved; see the module docstring.

```lean
theorem symbolValue_eq_of_sameExtension
    [∀ q : MaximalSpectrum B, IsNoetherianRing (Localization.AtPrime q.asIdeal)]
    [∀ q : MaximalSpectrum B, Ring.KrullDimLE 1 (Localization.AtPrime q.asIdeal)]
    (P P' : TameSymbolPreparation a B) (i j : Fin r) :
    P.symbolValue i j = P'.symbolValue i j
```

**`Stacks.Chow.factorizationValue_eq_of_factorizations_general`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/WellDefinedRefinement.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/WellDefinedRefinement.lean#L104). The attribute's comment: “the first clause, at a single maximal ideal and in an ARBITRARY local ring: the value of the formula of Stacks 0EAQ does not depend on the choice of the local factorizations. This is strictly more general than the form the source states -- R is neither Noetherian nor one-dimensional here -- and Stacks.Chow.factorizationValue_eq_of_factorizations, the form at the rings of the source, is this statement specialised to them”.

> **The factorization half of Stacks 0EAR at a single maximal ideal, in an arbitrary local
> ring.** The same identity as `Stacks.Chow.factorizationValue_eq_of_factorizations`, with `R`
> neither Noetherian nor one-dimensional: the argument needs only that `π` and `θ` are
> nonzerodivisors, so this is `Stacks.Chow.factorizationResidue_pow_ord_eq` read as a statement
> about `Stacks.Chow.factorizationValue`. Since it implies the form at the Noetherian
> one-dimensional local rings the source speaks of, namely
> `Stacks.Chow.factorizationValue_eq_of_factorizations` of
> `StacksFrontier.AlgebraicGeometry.Chow.TameSymbol.WellDefined`, it too carries Stacks 0EAR.

```lean
theorem factorizationValue_eq_of_factorizations_general
    {π θ : R} (hπ : π ∈ nonZeroDivisors R) (hθ : θ ∈ nonZeroDivisors R)
    {a₁ a₂ : R} {u₁ u₂ v₁ v₂ : Rˣ} {e₁ e₂ f₁ f₂ : ℕ}
    (hu₁ : a₁ = u₁ * π ^ e₁) (hu₂ : a₂ = u₂ * π ^ e₂)
    (hv₁ : a₁ = v₁ * θ ^ f₁) (hv₂ : a₂ = v₂ * θ ^ f₂) :
    factorizationValue π u₁ u₂ e₁ e₂ = factorizationValue θ v₁ v₂ f₁ f₂
```

## Tag 0EAS, a lemma

[Tag 0EAS](https://stacks.math.columbia.edu/tag/0EAS) in the Stacks Project.

**`Stacks.Chow.RegularTameSymbol.extend`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/Fraction.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/Fraction.lean#L288). The attribute's comment: “the passage from (4), (5), (6), (7) to (1), (2), (3), for a symbol on nonzerodivisors given as data rather than by the product formula of Stacks 0EAQ”.

> **Stacks 0EAH, the tame symbol of a one-dimensional Noetherian local ring.** The symbol on
> pairs of nonzerodivisors of `A` extends to the units of the total ring of fractions `Q(A)` by the
> formula `∂_A(a/b, c/d) = ∂_A(a, c) ∂_A(a, d)⁻¹ ∂_A(b, c)⁻¹ ∂_A(b, d)`, and the extension
> satisfies Stacks 0EAI, 0EAJ and 0EAK.
>
> This is the "exercise" of Stacks 0EAH and the second half of Stacks 0EAS: the properties
> Stacks 0EAL, 0EAM, 0EAN and 0EAP of the symbol on nonzerodivisors give the three properties of
> the symbol on `Q(A)^*`. The symbol on nonzerodivisors is an argument here rather than the explicit
> product of Stacks 0EAQ. The 0EAQ half — the first half of Stacks 0EAS — is supplied in
> `StacksFrontier.AlgebraicGeometry.Chow.TameSymbol.PairSymbol`, for an arbitrary one-dimensional
> Noetherian local ring: `Stacks.Chow.tameSymbolValue` is the symbol of an arbitrary pair of
> nonzerodivisors, `Stacks.Chow.tameSymbolValue_eq_symbolValue` identifies it with the product
> formula of Stacks 0EAQ at every preparation, and `Stacks.Chow.formulaTameSymbol` feeds it through
> this definition to deliver the map on `Q(A)^*`.

```lean
def extend : TameSymbol A Q
```

**`Stacks.Chow.tameSymbolValue_eq_symbolValue`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/PairSymbol.lean, line 322](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/PairSymbol.lean#L322). The attribute's comment: “that the function of a pair whose properties (4), (5), (6), (7) are proved below is the tame symbol of Stacks 0EAQ: it is the product formula of Stacks 0EAQ at every preparation of every family, over an arbitrary one-dimensional Noetherian local ring”.

> **The function `Stacks.Chow.tameSymbolValue` is the formula Stacks 0EAQ, at every
> preparation.** For any preparation of any family over any finite modification of `A`, in any
> universe, the formula's value on two members of the family is the value of the function on those
> two elements.
>
> Nothing is assumed of the preparation. The two cases are the two clauses of the definition: where
> the pair has a value, `AlgebraicGeometry.TameSymbolPreparation.symbolValue_eq_of_apply_eq`
> identifies it with this one; where it has none, Stacks 0EAG forces the pair to be a pair of units,
> and then both sides are `1`.
>
> This is what makes the four identities below statements about *the tame symbol of Stacks 0EAQ*:
> their subject `Stacks.Chow.tameSymbolValue` is here identified with the product formula
> `∏_𝔮 Norm_{κ(𝔮)/κ(𝔪)}((-1)^{e_i e_j} ū_i^{e_j} ū_j^{-e_i})^{m_𝔮}` of Stacks 0EAQ at every
> preparation at which that formula is written down.

```lean
theorem tameSymbolValue_eq_symbolValue (hdim : ringKrullDim A = 1)
    {B : Type v} [CommRing B] [Algebra A B] {r : ℕ} {a : Fin r → A}
    (P : TameSymbolPreparation a B) (i j : Fin r) (x y : nonZeroDivisors A)
    (hx : (x : A) = a i) (hy : (y : A) = a j) :
    letI : Fintype (MaximalSpectrum B) := @Fintype.ofFinite _ P.finite_maximalSpectrum
    letI : ∀ q : MaximalSpectrum B,
      IsLocalHom (algebraMap A (Localization.AtPrime q.asIdeal)) := P.isLocalHom
    tameSymbolValue x y = P.symbolValue i j
```

**`Stacks.Chow.tameSymbolValue_mul_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/PairSymbol.lean, line 406](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/PairSymbol.lean#L406). The attribute's comment: “property (4) in the first argument, for the tame symbol of Stacks 0EAQ as a function of an arbitrary pair of nonzerodivisors”.

> **Stacks 0EAL in the first argument, for the tame symbol of Stacks 0EAQ on arbitrary pairs of
> nonzerodivisors.** `∂_A(a a', b) = ∂_A(a, b) ∂_A(a', b)`.
>
> The four elements `a`, `a'`, `a a'` and `b` are prepared simultaneously
> (`Stacks.Chow.exists_regularTameSymbol_apply_eq`) unless all four are units, and then the identity
> is the first argument of `Stacks.Chow.RegularTameSymbol.map_mul_left` of that one symbol. If all
> four are units each side is `1`.

```lean
theorem tameSymbolValue_mul_left (hdim : ringKrullDim A = 1) (x x' y : nonZeroDivisors A) :
    tameSymbolValue (x * x') y = tameSymbolValue x y * tameSymbolValue x' y
```

**`Stacks.Chow.tameSymbolValue_mul_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/PairSymbol.lean, line 419](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/PairSymbol.lean#L419). The attribute's comment: “property (4) in the second argument, for the tame symbol of Stacks 0EAQ as a function of an arbitrary pair of nonzerodivisors”.

> **Stacks 0EAL in the second argument, for the tame symbol of Stacks 0EAQ on arbitrary pairs of
> nonzerodivisors.** `∂_A(a, b b') = ∂_A(a, b) ∂_A(a, b')`.

```lean
theorem tameSymbolValue_mul_right (hdim : ringKrullDim A = 1) (x y y' : nonZeroDivisors A) :
    tameSymbolValue x (y * y') = tameSymbolValue x y * tameSymbolValue x y'
```

**`Stacks.Chow.tameSymbolValue_self`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/PairSymbol.lean, line 433](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/PairSymbol.lean#L433). The attribute's comment: “property (5), for the tame symbol of Stacks 0EAQ as a function of an arbitrary pair of nonzerodivisors”.

> **Stacks 0EAM for the tame symbol of Stacks 0EAQ on arbitrary pairs of nonzerodivisors.**
> `∂_A(b, b) = (-1)^m` with `m = length_A(A/bA)`. For `b` a unit both sides are `1`, since
> `length_A(A/bA) = 0`.

```lean
theorem tameSymbolValue_self (hdim : ringKrullDim A = 1) (y : nonZeroDivisors A) :
    tameSymbolValue y y = (-1) ^ (Ring.ord A (y : A)).toNat
```

**`Stacks.Chow.tameSymbolValue_unit_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/PairSymbol.lean, line 449](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/PairSymbol.lean#L449). The attribute's comment: “property (6), for the tame symbol of Stacks 0EAQ as a function of an arbitrary pair of nonzerodivisors”.

> **Stacks 0EAN for the tame symbol of Stacks 0EAQ on arbitrary pairs of nonzerodivisors.**
> `∂_A(u, b) = ū^m` with `m = length_A(A/bA)`, for `u` a unit of `A`. For `b` a unit both sides are
> `1`.

```lean
theorem tameSymbolValue_unit_left (hdim : ringKrullDim A = 1) (x y : nonZeroDivisors A) (u : Aˣ)
    (hu : (x : A) = u) :
    tameSymbolValue x y = Units.map (residue A).toMonoidHom u ^ (Ring.ord A (y : A)).toNat
```

**`Stacks.Chow.tameSymbolValue_steinberg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/PairSymbol.lean, line 466](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/PairSymbol.lean#L466). The attribute's comment: “property (7), for the tame symbol of Stacks 0EAQ as a function of an arbitrary pair of nonzerodivisors”.

> **Stacks 0EAP for the tame symbol of Stacks 0EAQ on arbitrary pairs of nonzerodivisors.**
> `∂_A(a, b - a) ∂_A(b, b) = ∂_A(b, b - a) ∂_A(a, b)` for `a`, `b` and `b - a` nonzerodivisors. If
> all three are units each of the four values is `1`.

```lean
theorem tameSymbolValue_steinberg (hdim : ringKrullDim A = 1) (x y z : nonZeroDivisors A)
    (hz : (z : A) = (y : A) - (x : A)) :
    tameSymbolValue x z * tameSymbolValue y y = tameSymbolValue y z * tameSymbolValue x y
```

**`Stacks.Chow.formulaTameSymbol`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/PairSymbol.lean, line 505](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/PairSymbol.lean#L505). The attribute's comment: “that the tame symbol of Stacks 0EAQ, as a function of an arbitrary pair of nonzerodivisors, hence gives a map on Q(A)^* satisfying (1), (2), (3)”.

> **Stacks 0EAS, the map the formula Stacks 0EAQ gives on the total ring of fractions.** The
> tame symbol
>
> `∂_A : Q(A)^* × Q(A)^* → κ(𝔪)^*`
>
> of Stacks 0EAH, satisfying Stacks 0EAI, 0EAJ and 0EAK, for an arbitrary one-dimensional Noetherian
> local ring: the formula Stacks 0EAQ satisfies Stacks 0EAL, 0EAM, 0EAN and 0EAP on arbitrary pairs
> of nonzerodivisors, so `Stacks.Chow.RegularTameSymbol.extend` extends it. On nonzerodivisors it is
> the formula itself, by `Stacks.Chow.formulaTameSymbol_regularFractionUnit`.

```lean
noncomputable def formulaTameSymbol (hdim : ringKrullDim A = 1) (Q : Type v) [CommRing Q]
    [Algebra A Q] [IsFractionRing A Q] : TameSymbol A Q
```

Declarations registered for the tag:

- [`Stacks.Chow.normPushforwardOfIsIntegrallyClosed`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/NormalModification.lean#L160), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/NormalModification.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/NormalModification.lean#L292) (StacksFrontier): “that the product formula of Stacks 0EAQ satisfies (4), (5), (6), (7), for a local domain with a normal finite modification, where one extension serves every pair of nonzerodivisors”.

## Tag 0EAT, a lemma

[Tag 0EAT](https://stacks.math.columbia.edu/tag/0EAT) in the Stacks Project.

**`Stacks.Chow.tameSymbolFormula_eq_finprod_norm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/FormulaTower.lean, line 282](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/FormulaTower.lean#L282). The attribute's comment: “the displayed equation for the tame symbol of Stacks 0EAQ on A and on each local ring B_j”.

> **Stacks 0EAT.** Let `(A, 𝔪)` be a Noetherian local ring of dimension one, let `A ⊆ B` be a
> finite ring extension with `B / A` annihilated by a power of `𝔪` and `𝔪` not an associated prime
> of `B`. For nonzerodivisors `a, b ∈ A`,
>
> `∂_A(a, b) = ∏_j Norm_{κ(𝔪_j)/κ(𝔪)}(∂_{B_j}(a, b))`,
>
> the product over the maximal ideals `𝔪_j` of `B`, `B_j = B_{𝔪_j}`, where `∂` is the tame symbol of
> Stacks 0EAQ (`Stacks.Chow.tameSymbolFormula`) — on `A`, and on each `B_j`, which is again a
> one-dimensional Noetherian local ring in which `a` and `b` are nonzerodivisors.

```lean
theorem tameSymbolFormula_eq_finprod_norm (hdim : ringKrullDim A = 1)
    {B : Type v} [CommRing B] [Algebra A B] [Module.Finite A B]
    (hinj : Function.Injective (algebraMap A B))
    (hquot : ∃ n : ℕ, maximalIdeal A ^ n • (⊤ : Submodule A B) ≤
      LinearMap.range (Algebra.linearMap A B))
    (hass : ¬ IsAssociatedPrime (maximalIdeal A) B) {a b : A} (ha : IsRegular a)
    (hb : IsRegular b) :
    tameSymbolFormula hdim a b ha hb =
      ∏ᶠ q : MaximalSpectrum B,
        haveI := Stacks.Length.isLocalHom_algebraMap_localization (A := A) q
        haveI : IsNoetherianRing B := IsNoetherianRing.of_finite A B
        Units.map (Algebra.norm (ResidueField A) :
            ResidueField (Localization.AtPrime q.asIdeal) →* ResidueField A)
          (tameSymbolFormula (ringKrullDim_localizationAtPrime_eq_one hdim hinj hass q)
            (algebraMap A (Localization.AtPrime q.asIdeal) a)
            (algebraMap A (Localization.AtPrime q.asIdeal) b)
            (isRegular_algebraMap_localizationAtPrime hdim hass q ha)
            (isRegular_algebraMap_localizationAtPrime hdim hass q hb))
```

**`Stacks.Chow.normProd_eq_prod_norm_normProd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/Tower.lean, line 296](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/Tower.lean#L296). The attribute's comment: “the displayed equation, for both symbols read as the recipe of Stacks 0EAQ relative to the common refinement C the statement quantifies over; the non-associated-prime hypothesis of the source is imposed at each stage of the tower, and the correspondence between the maximal ideals of C and those of B is derived here from the semilocalizations rather than assumed. The spelling in which no refinement appears on the right-hand side is Stacks.Chow.normProd_eq_prod_norm_tameSymbol”.

> **Stacks 0EAT.** Let `(A, 𝔪)` be a one-dimensional Noetherian local ring, let `A ⊆ B` be a
> finite ring extension with `𝔪` not an associated prime of `B`, and let `B ⊆ C` be a further finite
> extension with `𝔪` not an associated prime of `C`. Then
>
> `∂_A(a, b) = ∏_𝔮 Norm_{κ(𝔮)/κ(𝔪)}(∂_{B_𝔮}(a, b))`,
>
> the product being over the maximal ideals `𝔮` of `B`, where `∂_A` is the norm pushforward to `A`
> of a family of tame symbols on the local rings of `C` and `∂_{B_𝔮}` is the norm pushforward of
> the same family to `B_𝔮` along the semilocalization `C_𝔮`.
>
> This is the source's proof: the maximal ideals of `C` are the maximal ideals of the
> semilocalizations `C_𝔮`, whose local rings are the local rings of `C`, and transitivity of norms
> for `κ(𝔪_{𝔮, v})/κ(𝔮)/κ(𝔪)` (Stacks 0BIJ) turns the product over the maximal ideals of `C` into
> the iterated product.

```lean
theorem normProd_eq_prod_norm_normProd
    (hB : ¬ IsAssociatedPrime (maximalIdeal A) B)
    (hC : ¬ IsAssociatedPrime (maximalIdeal A) C)
    (hfibre : ∀ q : MaximalSpectrum B,
      ¬ IsAssociatedPrime (maximalIdeal (Localization.AtPrime q.asIdeal))
        (Localization (Algebra.algebraMapSubmonoid C q.asIdeal.primeCompl)))
    (symb : ∀ r : MaximalSpectrum C, RegularTameSymbol (Localization.AtPrime r.asIdeal))
    (a b : nonZeroDivisors A) :
    normProd hC symb a b =
      ∏ q : MaximalSpectrum B,
        Units.map (Algebra.norm (ResidueField A) :
            ResidueField (Localization.AtPrime q.asIdeal) →* ResidueField A)
          (normProd (hfibre q) (fibreSymbol symb q)
            (toExtensionNonZeroDivisor hB q a) (toExtensionNonZeroDivisor hB q b))
```

**`Stacks.Chow.normPushforward_apply_eq_prod_norm_normPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/Tower.lean, line 322](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/Tower.lean#L322). The attribute's comment: “the displayed equation between the two tame symbols of Stacks 0EAH that the two sides define, for the recipe of Stacks 0EAQ relative to the common refinement C the statement quantifies over”.

> **Stacks 0EAT between the two tame symbols the two sides define.** Both the norm pushforward
> to `A` and each norm pushforward to `B_𝔮` are tame symbols in the sense of Stacks 0EAH, by
> `Stacks.Chow.normPushforward`, and the displayed equation of Stacks 0EAT relates them.

```lean
theorem normPushforward_apply_eq_prod_norm_normPushforward [Module.Finite A C]
    (hB : ¬ IsAssociatedPrime (maximalIdeal A) B)
    (hC : ¬ IsAssociatedPrime (maximalIdeal A) C)
    (hfibre : ∀ q : MaximalSpectrum B,
      ¬ IsAssociatedPrime (maximalIdeal (Localization.AtPrime q.asIdeal))
        (Localization (Algebra.algebraMapSubmonoid C q.asIdeal.primeCompl)))
    (symb : ∀ r : MaximalSpectrum C, RegularTameSymbol (Localization.AtPrime r.asIdeal))
    (hinj : Function.Injective (algebraMap A C))
    (hquot : ∃ n : ℕ, maximalIdeal A ^ n • (⊤ : Submodule A C) ≤
      LinearMap.range (Algebra.linearMap A C))
    (hinjFibre : ∀ q : MaximalSpectrum B,
      Function.Injective (algebraMap (Localization.AtPrime q.asIdeal)
        (Localization (Algebra.algebraMapSubmonoid C q.asIdeal.primeCompl))))
    (hquotFibre : ∀ q : MaximalSpectrum B,
      ∃ n : ℕ, maximalIdeal (Localization.AtPrime q.asIdeal) ^ n •
        (⊤ : Submodule (Localization.AtPrime q.asIdeal)
          (Localization (Algebra.algebraMapSubmonoid C q.asIdeal.primeCompl))) ≤
        LinearMap.range (Algebra.linearMap (Localization.AtPrime q.asIdeal)
          (Localization (Algebra.algebraMapSubmonoid C q.asIdeal.primeCompl))))
    (a b : nonZeroDivisors A) :
    normPushforward hC symb hinj hquot a b =
      ∏ q : MaximalSpectrum B,
        Units.map (Algebra.norm (ResidueField A) :
            ResidueField (Localization.AtPrime q.asIdeal) →* ResidueField A)
          (normPushforward (hfibre q) (fibreSymbol symb q) (hinjFibre q) (hquotFibre q)
            (toExtensionNonZeroDivisor hB q a) (toExtensionNonZeroDivisor hB q b))
```

**`Stacks.Chow.prod_norm_factorizationValue_tower_maximalSpectrum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/WellDefinedRefinement.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/WellDefinedRefinement.lean#L166). The attribute's comment: “the displayed equation for the symbol as the formula of Stacks 0EAQ defines it, over the maximal ideals of the refinement C the statement quantifies over, and generalized to arbitrary local factorization data on the local rings of C. The correspondence between the maximal ideals of C and those of B (Stacks 0EAE) is derived here from the semilocalizations rather than assumed, as is the tower of local rings along a fibre”.

> **Stacks 0EAT for the symbol the formula Stacks 0EAQ defines.** Let `(A, 𝔪)` be a
> one-dimensional Noetherian local ring, let `A ⊆ B` be a finite ring extension and let `B ⊆ C` be a
> further finite extension. Then
>
> `∂_A(a, b) = ∏_j Norm_{κ(𝔪_j)/κ(𝔪)}(∂_{B_j}(a, b))`,
>
> the product being over the maximal ideals `𝔪_j` of `B`, for both symbols read as the formula
> Stacks 0EAQ attaches to the local factorization data on the local rings of `C`: the left-hand side
> is the product over the maximal ideals of `C` of the residue-field norms down to `κ(𝔪)` of the
> local factors, and the factor at `𝔪_j` on the right is the product over the maximal ideals of the
> semilocalization `C_{𝔪_j}` of their norms down to `κ(𝔪_j)`. The two agree by transitivity of norms
> for `κ(𝔪_{j,k})/κ(𝔪_j)/κ(𝔪)`, Stacks 0BIJ.
>
> The correspondence between the maximal ideals of `C` and those of `B` — the content the source
> takes from Stacks 0EAE — is *derived* here, from
> `Stacks.Localization.prod_maximalSpectrum_eq_prod_prod`: the maximal ideals of `C` over `𝔪_j` are
> the maximal ideals of the semilocalization `C_{𝔪_j}`, and the local ring of `C` at the one below
> `v` is `Stacks.Chow.fibrePoint`. The tower `A → B_{𝔪_j} → C_{𝔪_{j,k}}` and the locality of its
> structure maps are derived too, by instance resolution out of
> `Localization.AtPrime.IsLiesOverAlgebra` and `Stacks.Chow.isLocalHom_fibreAlgebraMap`.
>
> The statement quantifies over arbitrary local factorization data `(π, u₁, u₂, e₁, e₂)` on the
> local rings of `C` rather than over data factoring two fixed elements of `A`, which is a
> generalization and not a restriction: the elements `a` and `b` of the source enter the formula
> only through that data, and the identity holds for all of it. The same equation between the two
> tame symbols of Stacks 0EAH that the two sides define, rather than between the two products, is
> `Stacks.Chow.normProd_eq_prod_norm_normProd` and
> `Stacks.Chow.normPushforward_apply_eq_prod_norm_normPushforward`.

```lean
theorem prod_norm_factorizationValue_tower_maximalSpectrum
    (π : ∀ r : MaximalSpectrum C, Localization.AtPrime r.asIdeal)
    (u₁ u₂ : ∀ r : MaximalSpectrum C, (Localization.AtPrime r.asIdeal)ˣ)
    (e₁ e₂ : MaximalSpectrum C → ℕ) :
    ∏ r : MaximalSpectrum C,
        Units.map (Algebra.norm (ResidueField A) :
            ResidueField (Localization.AtPrime r.asIdeal) →* ResidueField A)
          (factorizationValue (π r) (u₁ r) (u₂ r) (e₁ r) (e₂ r)) =
      ∏ q : MaximalSpectrum B,
        Units.map (Algebra.norm (ResidueField A) :
            ResidueField (Localization.AtPrime q.asIdeal) →* ResidueField A)
          (∏ s : MaximalSpectrum
              (Localization (Algebra.algebraMapSubmonoid C q.asIdeal.primeCompl)),
            Units.map (Algebra.norm (ResidueField (Localization.AtPrime q.asIdeal)) :
                ResidueField (Localization.AtPrime (fibrePoint q s).asIdeal) →*
                  ResidueField (Localization.AtPrime q.asIdeal))
              (factorizationValue (π (fibrePoint q s)) (u₁ (fibrePoint q s))
                (u₂ (fibrePoint q s)) (e₁ (fibrePoint q s)) (e₂ (fibrePoint q s))))
```

## Tag 0EPG, a lemma

[Tag 0EPG](https://stacks.math.columbia.edu/tag/0EPG) in the Stacks Project.

**`Stacks.Chow.units_map_residueField_tameSymbol_pow_eq_of_factorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/KeyLemma/TameSymbolFlatBaseChange.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/KeyLemma/TameSymbolFlatBaseChange.lean#L164). The attribute's comment: “for a pair of nonzerodivisors admitting a simultaneous power factorization over `A` itself, so that the finite extension of Stacks 0EAG used by the source's proof is not needed; the length multiplier is Stacks 02M1”.

> **Stacks 0EPG for a pair with a simultaneous power factorization over the base.** Let
> `(A, 𝔪, κ) → (A', 𝔪', κ')` be a flat local homomorphism of one-dimensional Noetherian local
> rings and let `m = length_{A'}(A' / 𝔪A')`. If two nonzerodivisors of `A` are simultaneous unit
> multiples of powers of one nonzerodivisor `π` of `A`, `a = u π ^ e` and `b = v π ^ f`, then
>
> `∂_A(a, b) ^ m` maps to `∂_{A'}(a, b)` under `κ → κ'`.
>
> Both symbols are evaluated by
> `Stacks.Chow.RegularTameSymbol.apply_eq_of_factorization`: over `A` on the parameter `π`, and
> over `A'` on the image of `π`, with the images of `u` and `v` as unit parts and the same
> exponents `e` and `f`. The two resulting expressions have the same base, the image in `κ'` of
> `(-1) ^ (ef) ū ^ f v̄ ^ (-e)`, and their exponents differ by exactly the factor `m`, because
> `length_{A'}(A' / π A') = m · length_A(A / πA)` by
> `Stacks.Chow.ord_algebraMap_eq_ord_mul_length_quotient`.
>
> This covers the case the source's proof disposes of first, `a` and `b` both units (take
> `π = 1`), and more generally a unit against a nonzerodivisor (take `π = b`, `v = 1`, `f = 1`).
> It does not cover a pair for which the finite extension of Stacks 0EAG is genuinely needed.

```lean
theorem units_map_residueField_tameSymbol_pow_eq_of_factorization
    {A : Type u} [CommRing A] [IsNoetherianRing A] [IsLocalRing A] [Ring.KrullDimLE 1 A]
    {A' : Type v} [CommRing A'] [IsNoetherianRing A'] [IsLocalRing A'] [Ring.KrullDimLE 1 A']
    [Algebra A A'] [IsLocalHom (algebraMap A A')] [Module.Flat A A']
    (symb : RegularTameSymbol A) (symb' : RegularTameSymbol A') {m : ℕ}
    (hm : Module.length A' (A' ⧸ extendedMaximalIdeal A A') = m)
    (p a b : nonZeroDivisors A) (u v : Aˣ) (e f : ℕ)
    (ha : (a : A) = u * (p : A) ^ e) (hb : (b : A) = v * (p : A) ^ f) :
    Units.map (ResidueField.map (algebraMap A A')).toMonoidHom (symb a b ^ m) =
      symb' (flatNonZeroDivisor A' a) (flatNonZeroDivisor A' b)
```

**`Stacks.Chow.map_symbolValue_pow_eq_prod_prod_support`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/KeyLemma/TameSymbolFlatBaseChangeFibre.lean, line 647](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/KeyLemma/TameSymbolFlatBaseChangeFibre.lean#L647). The attribute's comment: “for a general pair of nonzerodivisors, in the spelling in which both sides are the formula Stacks 0EAQ: on the left for a tame-symbol preparation over a finite extension `B` of `A`, which Stacks 0EAG provides for every pair, and on the right for the base change of that preparation, with the maximal ideals of the base change presented fibre by fibre over those of `B` and, in each fibre, as those carrying the parameter”.

> **Stacks 0EPG for a general pair of nonzerodivisors, over the supports.** Let
> `(A, 𝔪, κ) → (A', 𝔪', κ')` be a flat local homomorphism of one-dimensional Noetherian local rings
> and let `m = length_{A'}(A' / 𝔪A')`. Let `A ⊆ B` be a finite extension carrying a tame-symbol
> preparation of a family `a` of elements of `A` — by Stacks 0EAG one exists for *every* pair of
> nonzerodivisors of `A`. Then the value of the formula Stacks 0EAQ for two members of that family,
> raised to the power `m` and read in `κ'`, is the value of the same formula over `A'` for the
> base-changed data:
>
> `(∏_𝔮 Norm_{κ(𝔮)/κ}(c_𝔮))^m = ∏_𝔮 ∏_𝔭 Norm_{κ(𝔭)/κ'}(c_𝔭)`,
>
> where `𝔮` runs over the maximal ideals of `B` and `𝔭` over the maximal ideals of `A' ⊗_A B_𝔮`
> containing the image of the parameter `π_𝔮`.
>
> This differs from `Stacks.Chow.map_symbolValue_pow_eq_prod_prod` only in asking for the locality
> of `A' → (A' ⊗_A B_𝔮)_𝔭` and the finiteness of `κ(𝔭) / κ'` at those `𝔭` alone, and that is the
> difference between a statement that applies and one that does not. At a maximal ideal of
> `A' ⊗_A B_𝔮` where the image of `π_𝔮` is a unit the local ring need not be local over `A'`, and
> such maximal ideals do occur: for `A = ℤ_(5)`, `A' = ℤ₅`, `B` the semilocalization of `ℤ[i]` at
> `5` and `𝔮` one of the two maximal ideals of `B`, the ring `A' ⊗_A B_𝔮` is `ℚ₅ × ℤ₅`, whose local
> ring at `0 × ℤ₅` is `ℚ₅`, over which `ℤ₅` is not local.
>
> Each factor is `Stacks.Chow.map_norm_factorizationValue_pow_eq_prod_support`, which is the
> determinant identity Stacks 0GU1; the only other ingredient is that `κ → κ'` is multiplicative.

```lean
theorem map_symbolValue_pow_eq_prod_prod_support
    {m : ℕ} (hm : Module.length A' (A' ⧸ extendedMaximalIdeal A A') = m)
    {r : ℕ} {a : Fin r → A} (P : TameSymbolPreparation a B) (i j : Fin r)
    [∀ q : MaximalSpectrum B,
      Fintype (Stacks.Length.tensorSupport A A' (P.parameter q.asIdeal))]
    [∀ (q : MaximalSpectrum B) (p : Stacks.Length.tensorSupport A A' (P.parameter q.asIdeal)),
      IsLocalHom (algebraMap A' (Localization.AtPrime p.1.asIdeal))]
    [∀ (q : MaximalSpectrum B) (p : Stacks.Length.tensorSupport A A' (P.parameter q.asIdeal)),
      Module.Finite (ResidueField A') (ResidueField (Localization.AtPrime p.1.asIdeal))] :
    Units.map (ResidueField.map (algebraMap A A')).toMonoidHom (P.symbolValue i j) ^ m =
      ∏ q : MaximalSpectrum B,
        ∏ p : Stacks.Length.tensorSupport A A' (P.parameter q.asIdeal),
          Units.map (Algebra.norm (ResidueField A') :
              ResidueField (Localization.AtPrime p.1.asIdeal) →* ResidueField A')
            (factorizationValue (baseChangeLocalizationHom A' p.1 (P.parameter q.asIdeal))
              (Units.map (baseChangeLocalizationHom A' p.1).toMonoidHom
                (P.factorUnit q.asIdeal i))
              (Units.map (baseChangeLocalizationHom A' p.1).toMonoidHom
                (P.factorUnit q.asIdeal j))
              (P.exponent q.asIdeal i) (P.exponent q.asIdeal j))
```

**`Stacks.Chow.map_symbolValue_pow_eq_prod_prod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/KeyLemma/TameSymbolFlatBaseChangeGeneral.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/KeyLemma/TameSymbolFlatBaseChangeGeneral.lean#L200). The attribute's comment: “for a general pair of nonzerodivisors, in the spelling in which both sides are the formula Stacks 0EAQ: on the left for a tame-symbol preparation over a finite extension `B` of `A`, which Stacks 0EAG provides for every pair, and on the right for the base change of that preparation, with the maximal ideals of `A' ⊗_A B` presented fibre by fibre over those of `B`”.

> Let `(A, 𝔪, κ) → (A', 𝔪', κ')` be a flat local homomorphism of one-dimensional Noetherian
> local rings and let `m = length_{A'}(A' / 𝔪A')`. Let `A ⊆ B` be a finite extension carrying a
> tame-symbol preparation of a family `a` of elements of `A` (by Stacks 0EAG one exists for every
> pair of nonzerodivisors of `A`). Then the value of the formula Stacks 0EAQ for two members of
> that family, raised to the power `m` and read in `κ'`, is the value of the same formula over `A'`
> for the base-changed data:
>
> `(∏_𝔮 Norm_{κ(𝔮)/κ}(c_𝔮))^m = ∏_𝔮 ∏_𝔭 Norm_{κ(𝔭)/κ'}(c_𝔭)`,
>
> where `𝔮` runs over the maximal ideals of `B`, `𝔭` over the maximal ideals of `A' ⊗_A B_𝔮`, and
> the local data over `𝔭` is the image of the local data over `𝔮` under `B_𝔮 → (A' ⊗_A B_𝔮)_𝔭`.
> The index set of the right-hand side is thus presented fibre by fibre over the maximal ideals of
> `B`; in the source it is presented as the set of maximal ideals of `A' ⊗_A B`, whose fibred
> decomposition is `Stacks.Chow.baseChangeSigmaEquiv`. The hypotheses below hold only at the maximal
> ideals carrying the parameter; `Stacks.Chow.map_symbolValue_pow_eq_prod_prod_support` is the form
> that asks for them there alone.

```lean
theorem map_symbolValue_pow_eq_prod_prod
    {m : ℕ} (hm : Module.length A' (A' ⧸ extendedMaximalIdeal A A') = m)
    {r : ℕ} {a : Fin r → A} (P : TameSymbolPreparation a B) (i j : Fin r) :
    Units.map (ResidueField.map (algebraMap A A')).toMonoidHom (P.symbolValue i j) ^ m =
      ∏ q : MaximalSpectrum B,
        ∏ p : MaximalSpectrum (A' ⊗[A] Localization.AtPrime q.asIdeal),
          Units.map (Algebra.norm (ResidueField A') :
              ResidueField (Localization.AtPrime p.asIdeal) →* ResidueField A')
            (factorizationValue (baseChangeLocalizationHom A' p (P.parameter q.asIdeal))
              (Units.map (baseChangeLocalizationHom A' p).toMonoidHom (P.factorUnit q.asIdeal i))
              (Units.map (baseChangeLocalizationHom A' p).toMonoidHom (P.factorUnit q.asIdeal j))
              (P.exponent q.asIdeal i) (P.exponent q.asIdeal j))
```

**`Stacks.Chow.map_normPushforward_pow_eq_prod_prod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/KeyLemma/TameSymbolFlatBaseChangeGeneral.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/KeyLemma/TameSymbolFlatBaseChangeGeneral.lean#L223). The attribute's comment: “for a general pair of nonzerodivisors, with the symbol on `A` spelled as the norm pushforward of Stacks 0EAT and the symbol on `A'` as the formula Stacks 0EAQ for the base change”.

> For nonzerodivisors `a₁ = a i` and `a₂ = a j` of `A` and a tame-symbol preparation `P` of `a`
> over `B`, the tame symbol `∂_A(a₁, a₂)` of Stacks 0EAT, raised to the power `m` and read in `κ'`,
> is the value of the formula Stacks 0EAQ over `A'` for the base change of `P`: the right-hand side
> of `Stacks.Chow.map_symbolValue_pow_eq_prod_prod`.

```lean
theorem map_normPushforward_pow_eq_prod_prod [Module.Finite A B]
    {m : ℕ} (hm : Module.length A' (A' ⧸ extendedMaximalIdeal A A') = m)
    (hass : ¬ IsAssociatedPrime (maximalIdeal A) B)
    (symb : ∀ q : MaximalSpectrum B, RegularTameSymbol (Localization.AtPrime q.asIdeal))
    (hinj : Function.Injective (algebraMap A B))
    (hquot : ∃ n : ℕ, maximalIdeal A ^ n • (⊤ : Submodule A B) ≤
      LinearMap.range (Algebra.linearMap A B))
    {r : ℕ} {a : Fin r → A} (P : TameSymbolPreparation a B) (i j : Fin r)
    (x y : nonZeroDivisors A) (hx : (x : A) = a i) (hy : (y : A) = a j) :
    Units.map (ResidueField.map (algebraMap A A')).toMonoidHom
        (normPushforward hass symb hinj hquot x y) ^ m =
      ∏ q : MaximalSpectrum B,
        ∏ p : MaximalSpectrum (A' ⊗[A] Localization.AtPrime q.asIdeal),
          Units.map (Algebra.norm (ResidueField A') :
              ResidueField (Localization.AtPrime p.asIdeal) →* ResidueField A')
            (factorizationValue (baseChangeLocalizationHom A' p (P.parameter q.asIdeal))
              (Units.map (baseChangeLocalizationHom A' p).toMonoidHom (P.factorUnit q.asIdeal i))
              (Units.map (baseChangeLocalizationHom A' p).toMonoidHom (P.factorUnit q.asIdeal j))
              (P.exponent q.asIdeal i) (P.exponent q.asIdeal j))
```

**`Stacks.Chow.map_symbolValue_pow_eq_prod_maximalSpectrum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/KeyLemma/TameSymbolFlatBaseChangeSingleProduct.lean, line 387](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/KeyLemma/TameSymbolFlatBaseChangeSingleProduct.lean#L387). The attribute's comment: “for a general pair of nonzerodivisors, in the spelling of the source: the formula Stacks 0EAQ over `A` for a tame-symbol preparation on a finite extension `B` of `A`, which Stacks 0EAG provides for every pair, raised to the power `m` and read in `κ'`, is one product over the maximal ideals `𝔭` of `A' ⊗_A B`, the factor at `𝔭` being the norm to `κ'` of the formula Stacks 0EAQ computed in `(A' ⊗_A B)_𝔭` for the image of the factorization data at `𝔭 ∩ B`”.

> **Stacks 0EPG for a general pair of nonzerodivisors, as a single product over the maximal
> ideals of the base change.** Let `(A, 𝔪, κ) → (A', 𝔪', κ')` be a flat local homomorphism of
> one-dimensional Noetherian local rings and let `m = length_{A'}(A' / 𝔪A')`. Let `A ⊆ B` be a
> finite extension carrying a tame-symbol preparation of a family `a` of elements of `A` — by
> Stacks 0EAG one exists for *every* pair of nonzerodivisors of `A`. Then the value of the formula
> Stacks 0EAQ for two members of that family, raised to the power `m` and read in `κ'`, is
>
> `(∏_𝔮 Norm_{κ(𝔮)/κ}(w_𝔮)^{m_𝔮})^m = ∏_𝔭 Norm_{κ(𝔭)/κ'}(w_{𝔭 ∩ B})^{m_𝔭}`,
>
> the product on the right running over *all* the maximal ideals `𝔭` of `A' ⊗_A B` and the factor at
> `𝔭` being computed in the local ring `(A' ⊗_A B)_𝔭`, from the image of the factorization data at
> `𝔮 = 𝔭 ∩ B` under `B_𝔮 → (A' ⊗_A B)_𝔭`. This is the spelling of the source: there the maximal
> ideals of `B' = A' ⊗_A B` are listed as `𝔪'_{j,l}`, the maximal ideals above `𝔪_j`, the factor at
> `𝔪'_{j,l}` is read in `B'_{j,l}`, and "as factorizations of `a₁` and `a₂` in `B'_{j,l}` we use the
> image of the factorizations `a_i = u_{i,j} π_j^{e_{i,j}}` given to us in `B_j`".
>
> `Stacks.Chow.map_symbolValue_pow_eq_prod_prod_support` is the same identity with the right-hand
> side presented fibre by fibre over the maximal ideals of `B` and the factor in each fibre read in
> `(A' ⊗_A B_𝔮)_p` rather than in `(A' ⊗_A B)_𝔭`; the two index sets are identified by
> `Stacks.Chow.baseChangeSupportSigmaEquiv` and the two factors agree by
> `Stacks.Chow.units_map_norm_factorizationValue_baseChange`.
>
> The identification of the index sets holds fibre by fibre at a maximal ideal `𝔮` of `B` whose
> parameter lies in the maximal ideal of `B_𝔮`. At a maximal ideal whose parameter is a unit no
> identification is needed: the support of the parameter in `A' ⊗_A B_𝔮` is then empty, and over
> `𝔮` the order of vanishing in `(A' ⊗_A B)_𝔭` is zero, so both fibre products are `1`.

```lean
theorem map_symbolValue_pow_eq_prod_maximalSpectrum
    {m : ℕ} (hm : Module.length A' (A' ⧸ extendedMaximalIdeal A A') = m)
    {r : ℕ} {a : Fin r → A} (P : TameSymbolPreparation a B) (i j : Fin r)
    [∀ q : MaximalSpectrum B,
      Fintype (Stacks.Length.tensorSupport A A' (P.parameter q.asIdeal))] :
    Units.map (ResidueField.map (algebraMap A A')).toMonoidHom (P.symbolValue i j) ^ m =
      ∏ 𝔭 : MaximalSpectrum (A' ⊗[A] B),
        Units.map (Algebra.norm (ResidueField A') :
            ResidueField (Localization.AtPrime 𝔭.asIdeal) →* ResidueField A')
          (factorizationValue (baseChangeFibreHom 𝔭 (P.parameter (baseChangeUnder 𝔭).asIdeal))
            (Units.map (baseChangeFibreHom 𝔭).toMonoidHom
              (P.factorUnit (baseChangeUnder 𝔭).asIdeal i))
            (Units.map (baseChangeFibreHom 𝔭).toMonoidHom
              (P.factorUnit (baseChangeUnder 𝔭).asIdeal j))
            (P.exponent (baseChangeUnder 𝔭).asIdeal i)
            (P.exponent (baseChangeUnder 𝔭).asIdeal j))
```

**`Stacks.Chow.map_tameSymbolFormula_pow_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/FlatBaseChange.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TameSymbol/FlatBaseChange.lean#L212).

> **Flat base change for the tame symbol.** Let `(A, 𝔪, κ) → (A', 𝔪', κ')` be a local
> homomorphism of Noetherian local rings, with `A → A'` flat and `dim(A) = dim(A') = 1`, and let
> `m = length_{A'}(A' / 𝔪A')` (finite, by `Stacks.Chow.isFiniteLength_closedFibre`). For
> nonzerodivisors `a₁, a₂ ∈ A`, the element `∂_A(a₁, a₂)^m` maps to `∂_{A'}(a₁, a₂)` via
> `κ → κ'`, where `∂` is the tame symbol `Stacks.Chow.tameSymbolFormula`.

```lean
theorem map_tameSymbolFormula_pow_eq (hdim : ringKrullDim A = 1) (hdim' : ringKrullDim A' = 1)
    {a₁ a₂ : A} (ha₁ : IsRegular a₁) (ha₂ : IsRegular a₂) :
    Units.map (ResidueField.map (algebraMap A A')).toMonoidHom
        (tameSymbolFormula hdim a₁ a₂ ha₁ ha₂ ^
          (Module.length A' (A' ⧸ Ideal.map (algebraMap A A') (maximalIdeal A))).toNat) =
      tameSymbolFormula hdim' (algebraMap A A' a₁) (algebraMap A A' a₂)
        (Stacks.Fitting.isRegular_algebraMap_of_flat ha₁)
        (Stacks.Fitting.isRegular_algebraMap_of_flat ha₂)
```

## Tag 0GU1, an equation

[Tag 0GU1](https://stacks.math.columbia.edu/tag/0GU1) in the Stacks Project.

**`Stacks.Length.map_norm_pow_length_eq_prod_norm_pow_length`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Length/NormFlatBaseChange.lean, line 473](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Length/NormFlatBaseChange.lean#L473).

> Let `A → S` be a flat local homomorphism of local rings with `m = length_S(S / 𝔪_A S)`, let
> `B` be a local `A`-algebra along a local homomorphism with `κ(B) / κ(A)` finite, and let
> `π`, `u ∈ B` with `B / πB` of finite length. Then, writing `T = S ⊗_A B`,
>
> `(Norm_{κ(B)/κ(A)}(ū) ^ length_B(B / πB)) ^ m
>   = ∏_𝔮 Norm_{κ(T_𝔮)/κ(S)}(ū) ^ length_{T_𝔮}(T_𝔮 / πT_𝔮)`,
>
> the product running over the maximal ideals of `T` and the left-hand side being read in `κ(S)`
> through `κ(A) → κ(S)`.

```lean
theorem map_norm_pow_length_eq_prod_norm_pow_length
    {A : Type u} {S : Type v} {B : Type w}
    [CommRing A] [CommRing S] [CommRing B]
    [IsLocalRing A] [IsLocalRing S] [IsLocalRing B]
    [Algebra A S] [Algebra A B] [IsLocalHom (algebraMap A S)]
    [IsLocalHom (algebraMap A B)] [Module.Flat A S]
    [Fintype (MaximalSpectrum (S ⊗[A] B))]
    [Module.Finite (ResidueField A) (ResidueField B)]
    [∀ q : MaximalSpectrum (S ⊗[A] B),
      IsLocalHom (algebraMap S (Localization.AtPrime q.asIdeal))]
    [∀ q : MaximalSpectrum (S ⊗[A] B),
      Module.Finite (ResidueField S) (ResidueField (Localization.AtPrime q.asIdeal))]
    (π u : B) (hM : IsFiniteLength B (B ⧸ Ideal.span {π}))
    {m : ℕ} (hm : Module.length S (S ⧸ extendedMaximalIdeal A S) = m) :
    ResidueField.map (algebraMap A S)
      ((Algebra.norm (ResidueField A) (residue B u) ^
        (Module.length B (B ⧸ Ideal.span {π})).toNat) ^ m) =
      ∏ q : MaximalSpectrum (S ⊗[A] B),
        Algebra.norm (ResidueField S)
          (residue (Localization.AtPrime q.asIdeal)
            ((algebraMap (S ⊗[A] B) (Localization.AtPrime q.asIdeal))
              (Algebra.TensorProduct.includeRight u))) ^
            (Module.length (Localization.AtPrime q.asIdeal)
            (Localization.AtPrime q.asIdeal ⧸
              Ideal.span {(algebraMap (S ⊗[A] B) (Localization.AtPrime q.asIdeal)
                (Algebra.TensorProduct.includeRight π))})).toNat
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.5, Tag 0EAH](https://stacks.math.columbia.edu/tag/0EAH)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
