---
declaration: section
origin: cited
lean: Stacks.Chow.fullChernCharacter, Stacks.Chow.rationalCap_chernCharacterComponent_eq_zero_of_topologicalKrullDim_le, Stacks.Chow.gradedChernCharacter_eq_fullChernCharacter, Stacks.Chow.moduleChernCharacter_apply_eq, Stacks.Chow.exists_gradedRationalChowCohomology_eq_moduleChernCharacter, Stacks.Chow.moduleChernCharacter, Stacks.Chow.modulePowerSumComponentArbitraryRank_eq_add_of_shortExact, Stacks.Chow.moduleChernCharacter_eq_add_of_shortExact
statement: formalized
proof: formalized
---

# 42.45 The Chern character and tensor products

Section 42.45 of the Stacks Project, [Tag 02UM](https://stacks.math.columbia.edu/tag/02UM). 4 tags here are carried by 18 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0ESX, a remark

[Tag 0ESX](https://stacks.math.columbia.edu/tag/0ESX) in the Stacks Project.

**`Stacks.Chow.fullChernCharacter`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/ChernCharacter.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/ChernCharacter.lean#L225). The attribute's comment: “the full Chern character of a finite locally free module of not necessarily constant rank as an element of the product ∏\_\{p ≥ 0} (A^p(X) ⊗ 𝐐), assembled over the rank loci from the constant-rank power sums P\_p(c\_1(E|X\_r), …, c\_p(E|X\_r)) that the remark recalls from Tags 0ESW, 0FA7 and 0F9C; those are carried as a quantified family, the multiplication of A^*(X) — composition of bivariant classes, Tag 0FE0 — not being constructed in this library”.

> The full Chern character `ch(E) = (ch_0(E), ch_1(E), ch_2(E), …)` of a finite locally free
> module whose rank need not be constant, as an element of the product `∏_{p ≥ 0} (A^p(X) ⊗ 𝐐)`.

```lean
def fullChernCharacter : fullRationalChowCohomology C G sX
```

**`Stacks.Chow.rationalCap_chernCharacterComponent_eq_zero_of_topologicalKrullDim_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/ChernCharacter.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/ChernCharacter.lean#L257). The attribute's comment: “the vanishing of the components ch\_p(E) for p above the dimension d of X, by Tag 0FDX, read on the test schemes of dimension at most d as the library's form of that tag allows; the splitting principle of the source is not needed, that form being a delta-dimension count, and neither is quasi-compactness of X”.

> For `d < p` the class `ch_p(E)` caps every rational Chow class of a test scheme of dimension
> at most `d` to zero.

```lean
theorem rationalCap_chernCharacterComponent_eq_zero_of_topologicalKrullDim_le (d p : ℕ)
    (hp : d < p) {T : Scheme.{u}} (g : T ⟶ X) [LocallyOfFiniteType g]
    (hT : topologicalKrullDim T ≤ (d : WithBot ℕ∞)) (k : ℤ)
    (α : chowGroup C (g ≫ sX) k) :
    rationalCap C G sX (p : ℤ) g k α
      (chernCharacterComponent C G sX E hgysO hgysR hgysC P p) = 0
```

**`Stacks.Chow.gradedChernCharacter_eq_fullChernCharacter`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/ChernCharacter.lean, line 334](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/ChernCharacter.lean#L334). The attribute's comment: “the membership ch(E) ∈ A^*(X) ⊗ 𝐐 for X of dimension at most d: the full Chern character is the image of the finite sum ⊕\_\{p ≤ d} ch\_p(E). The vanishing of the components above d is a hypothesis: the library's Tag 0FDX reaches only the test schemes of dimension at most d, and by Tag 02UC the remaining ones are what the equality ch\_p(E) = 0 in A^p(X) ⊗ 𝐐 needs. Quasi-compactness of X is not assumed, being unused by the library's form of Tag 0FDX”.

> If the components of the Chern character vanish in the degrees above `d`, then the full
> Chern character lies in `A^*(X) ⊗ 𝐐`: it is the image of the finite sum `⊕_{p ≤ d} ch_p(E)` under
> the inclusion of the direct sum into the product `∏_{p ≥ 0} (A^p(X) ⊗ 𝐐)`.

```lean
theorem gradedChernCharacter_eq_fullChernCharacter (d : ℕ)
    (hvan : ∀ p : ℕ, d < p →
      chernCharacterComponent C G sX E hgysO hgysR hgysC P p = 0) :
    (fun p : ℕ ↦ gradedChernCharacter C G sX E hgysO hgysR hgysC P d p) =
      fullChernCharacter C G sX E hgysO hgysR hgysC P
```

**`Stacks.Chow.moduleChernCharacter_apply_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/ChernCharacterLocallyFree.lean, line 392](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/ChernCharacterLocallyFree.lean#L392). The attribute's comment: “the components ch\_p(E) = P\_p(E)/p! ∈ A^p(X) ⊗ Q of the Chern character of a finite locally free module of not necessarily constant rank, with P\_p of 0F9B evaluated at the rank and Chern classes of 0ESW (0FA7), so that ch(E) ∈ ∏\_\{p ≥ 0} (A^p(X) ⊗ Q)”.

> **Stacks 0ESX, the Chern character of a module of arbitrary rank.** For a finite locally free
> module `ℰ` whose rank need not be constant, the Chern character
> `ch(ℰ) = (ch_0(ℰ), ch_1(ℰ), …) ∈ ∏_{p ≥ 0} (A^p(X) ⊗ 𝐐)` (`Stacks.Chow.moduleChernCharacter`) has
> components `ch_p(ℰ) = P_p(ℰ)/p!`, where `P_p(ℰ) ∈ A^p(X)` is the power sum of Stacks 0F9B (with
> `P_0 = r`) evaluated at the rank `r(ℰ)` and the Chern classes `c_i(ℰ)` of Stacks 0ESW, as in
> Stacks 0FA7.

```lean
theorem moduleChernCharacter_apply_eq (p : ℕ) :
    moduleChernCharacter C sX E p =
      ((Nat.factorial p : ℚ)⁻¹) ⊗ₜ[ℤ]
        chernPolynomialComponent C sX E p (powerSumChernPolynomial p)
```

**`Stacks.Chow.exists_gradedRationalChowCohomology_eq_moduleChernCharacter`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/ChernCharacterLocallyFree.lean, line 428](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/ChernCharacterLocallyFree.lean#L428). The attribute's comment: “for X quasi-compact with dim(X) < ∞, ch(E) ∈ A^*(X) ⊗ Q: the full Chern character is the image of an element of ⊕\_p (A^p(X) ⊗ Q)”.

> **Stacks 0ESX, the finite-dimensional case.** If `X` is quasi-compact and `dim X < ∞`, then
> `ch(ℰ) ∈ A^*(X) ⊗ 𝐐`: the full Chern character is the image of an element of the direct sum
> `⊕_{p ≥ 0} (A^p(X) ⊗ 𝐐)` under its inclusion into the product.

```lean
theorem exists_gradedRationalChowCohomology_eq_moduleChernCharacter [CompactSpace X]
    (hdim : topologicalKrullDim X < ⊤) :
    ∃ y : gradedRationalChowCohomology C (gysinSystemOfInvertible C) sX,
      ∀ p : ℕ, y p = moduleChernCharacter C sX E p
```

Declarations registered for the tag:

- [`Stacks.Chow.moduleChernCharacter`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/BivariantPowerSumShortExact.lean#L158), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/ChernCharacterLocallyFree.lean, line 409](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/ChernCharacterLocallyFree.lean#L409) (StacksFrontier): “the full Chern character ch(E) ∈ ∏\_\{p ≥ 0} (A^p(X) ⊗ Q) of a finite locally free module of not necessarily constant rank, built from the genuine classes of 0B7H on the rank loci”.

## Tag 0F9C, a lemma

[Tag 0F9C](https://stacks.math.columbia.edu/tag/0F9C) in the Stacks Project.

**`Stacks.Chow.modulePowerSumComponentArbitraryRank_eq_add_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/BivariantPowerSumShortExact.lean, line 278](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/BivariantPowerSumShortExact.lean#L278). The attribute's comment: “the source's more precise equality P\_p(E) = P\_p(E\_1) + P\_p(E\_2), stated where the source states it: IN A^p(X), the degree-p Chow cohomology of Tag 0B7E at the Gysin system of the first Chern class of an invertible module (Stacks.Chow.chowCohomologyComponent). A^*(X) = prod\_\{q >= 0} A^q(X) is the RING Stacks.Chow.TotalChowClass, whose product is the Cauchy product of the compositions A^i(X) x A^j(X) -> A^\{i+j}(X) of Tag 0B75 (Stacks.Chow.TotalChowClass.instRing), so a polynomial in the Chern classes of a module is itself a bivariant class here; the Chern classes are the bivariant classes of Tag 0B7H, Stacks.Chow.GenuineChern.chernClass, assembled into Stacks.Chow.totalChern. P\_p is CONSTRUCTED, by the Newton recurrence of Tag 0F9B (AlgebraicGeometry.newtonPowerSum) applied to the homogeneous components of the total Chern class with the rank as degree-zero term, so P\_0(E) is the rank as in the source's recursion. THE RANKS ARE ARBITRARY, exactly as in the source: only that the three terms are finite locally free is assumed, no rank is named, and the rank of a finite locally free module is locally constant, so X is decomposed into the open and closed loci where each rank is constant (Stacks.Chow.rankLocus) and the class is assembled over them by Tag 0FDZ as Stacks.Chow.modulePowerSumArbitraryRank; Stacks.Chow.res\_modulePowerSumArbitraryRank\_of\_constantRank identifies its restriction along any morphism of constant rank with the constant-rank power sum there, and the identity is read on a decomposition refining the rank decompositions of E\_1 and of E\_2. No filtration and no splitting of the sequence is supposed: the pulled-back sequence stays short exact with no flatness, a short exact sequence with finite locally free quotient being locally split. The splitting principle of the source is used only through the two results of the chapter it proves, both available here with no extra hypotheses: Tag 02UI on total classes (Stacks.Chow.totalChern\_shortExact) and the commutativity of Chern classes of Tag 02UA (Stacks.Chow.commute\_homComponent\_totalChern). PROVED HERE: that those two give the additivity of every power sum, which is Newton's identities read as the single equation c . nu(c) = D(c) for the derivation D multiplying the index-m component by m”.

> Let `(S, δ)` be as in Situation 02QL, let `X` be locally of finite type over `S` and let
> `0 ⟶ ℰ₁ ⟶ ℰ ⟶ ℰ₂ ⟶ 0` be a short exact sequence of finite locally free `𝒪_X`-modules. Then for
> every `p`
>
>   `P_p(ℰ) = P_p(ℰ₁) + P_p(ℰ₂)`  in  `A^p(X)`,
>
> where `P_p` is the universal power-sum polynomial of Stacks 0F9B evaluated at the Chern classes.
> No constancy of the ranks is assumed.

```lean
theorem modulePowerSumComponentArbitraryRank_eq_add_of_shortExact (p : ℕ) :
    modulePowerSumComponentArbitraryRank C sX S.X₂ p =
      modulePowerSumComponentArbitraryRank C sX S.X₁ p +
        modulePowerSumComponentArbitraryRank C sX S.X₃ p
```

**`Stacks.Chow.moduleChernCharacter_eq_add_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/BivariantPowerSumShortExact.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/BivariantPowerSumShortExact.lean#L325). The attribute's comment: “the headline equality ch(E) = ch(E\_1) + ch(E\_2) for a short exact sequence 0 -> E\_1 -> E -> E\_2 -> 0 of finite locally free O\_X-modules over X locally of finite type over the base of Situation 02QL. THE RANKS ARE ARBITRARY, exactly as in the source: only that the three terms are finite locally free is assumed and no rank is named. ch\_p(F) = P\_p(F)/p! is Stacks.Chow.moduleChernCharacterComponent, an element of A^p(X) tensor Q (Stacks.Chow.rationalChowCohomologyComponent) where A^p(X) is the degree-p Chow cohomology of Tag 0B7E -- the RATIONAL BIVARIANT group, not a ring of cap operators; the integral identity it is divided by holds in A^p(X) itself, in the bivariant ring A^*(X) = Stacks.Chow.TotalChowClass. ch(F) itself is Stacks.Chow.moduleChernCharacter, the family (ch\_0(F), ch\_1(F), ...) in the product prod\_\{p >= 0} (A^p(X) tensor Q), which is the home Tag 0ESX gives the Chern character, the degree in which it is concentrated being governed by a rank that is unbounded in general; addition there is degreewise, so an equality of two such families is an equality of Chern characters read in every degree at once, and Stacks.Chow.moduleChernCharacterComponent\_eq\_add\_of\_shortExact is that reading. It is derived from the source's more precise equality, Stacks.Chow.modulePowerSumComponentArbitraryRank\_eq\_add\_of\_shortExact, by dividing by p!: the division of a sum by a scalar is term by term, so unlike Tag 0F9D no binomial coefficient intervenes. The splitting principle is NOT redone here; it enters only through Tag 02UI on total classes (Stacks.Chow.totalChern\_shortExact) and the commutativity of Chern classes of Tag 02UA”.

> Let `(S, δ)` be as in Situation 02QL, let `X` be locally of finite type over `S` and let
> `0 ⟶ ℰ₁ ⟶ ℰ ⟶ ℰ₂ ⟶ 0` be a short exact sequence of finite locally free `𝒪_X`-modules. Then
>
>   `ch(ℰ) = ch(ℰ₁) + ch(ℰ₂)`.
>
> Both sides lie in `∏_{p ≥ 0} (A^p(X) ⊗ 𝐐)`, the rational Chow cohomology of `X` in which
> Stacks 0ESX places the Chern character.

```lean
theorem moduleChernCharacter_eq_add_of_shortExact :
    moduleChernCharacter C sX S.X₂ =
      moduleChernCharacter C sX S.X₁ + moduleChernCharacter C sX S.X₃
```

**`Stacks.Chow.powerSumOfFiniteLocallyFree_eq_add_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PowerSumComplex.lean, line 244](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PowerSumComplex.lean#L244). The attribute's comment: “the precise form: P\_p(E) = P\_p(E\_1) + P\_p(E\_2) in A^p(X), for every p >= 0, for a short exact sequence of finite locally free modules of arbitrary ranks; P\_p is the polynomial of Stacks 0F9B in the Chern classes of Stacks 0B7H, assembled over the rank loci (Stacks 0ESW, 0FA7)”.

> **Stacks 0F9C.** For a short exact sequence `0 ⟶ ℰ₁ ⟶ ℰ ⟶ ℰ₂ ⟶ 0` of finite locally free
> `𝒪_X`-modules, of ranks that need not be constant, `P_p(ℰ) = P_p(ℰ₁) + P_p(ℰ₂)` for every `p`.

```lean
theorem powerSumOfFiniteLocallyFree_eq_add_of_shortExact (S : ShortComplex X.Modules)
    (hS : S.ShortExact) [h₁ : AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} S.X₁]
    [h₃ : AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} S.X₃] (p : ℕ) :
    haveI := GenuineChern.isFiniteLocallyFree_of_shortExact S hS h₁ h₃
    powerSumOfFiniteLocallyFree C sX S.X₂ p =
      powerSumOfFiniteLocallyFree C sX S.X₁ p + powerSumOfFiniteLocallyFree C sX S.X₃ p
```

**`Stacks.Chow.chernCharacterOfFiniteLocallyFree_eq_add_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PowerSumComplex.lean, line 284](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PowerSumComplex.lean#L284). The attribute's comment: “ch(E) = ch(E\_1) + ch(E\_2), read in every degree p as ch\_p = P\_p/p! in A^p(X) ⊗ Q, for a short exact sequence of finite locally free modules of arbitrary ranks”.

> **Stacks 0F9C for the Chern character**: `ch(ℰ) = ch(ℰ₁) + ch(ℰ₂)`, degree by degree, for a
> short exact sequence of finite locally free modules of arbitrary ranks.

```lean
theorem chernCharacterOfFiniteLocallyFree_eq_add_of_shortExact (S : ShortComplex X.Modules)
    (hS : S.ShortExact) [h₁ : AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} S.X₁]
    [h₃ : AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} S.X₃] (p : ℕ) :
    haveI := GenuineChern.isFiniteLocallyFree_of_shortExact S hS h₁ h₃
    chernCharacterOfFiniteLocallyFree C sX S.X₂ p =
      chernCharacterOfFiniteLocallyFree C sX S.X₁ p +
        chernCharacterOfFiniteLocallyFree C sX S.X₃ p
```

**`Stacks.Chow.powerSumCap_append`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/PowerSumCapProducts.lean, line 335](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/PowerSumCapProducts.lean#L335). The attribute's comment: “componentwise on cap products, and conditional. CORRECTION OF FORM: the source states P\_p(E) = P\_p(E\_1) + P\_p(E\_2) in A^p(X) for a short exact sequence 0 -> E\_1 -> E -> E\_2 -> 0 of finite locally free O\_X-modules, and ch(E) = ch(E\_1) + ch(E\_2) after dividing by p!. There is no bivariant ring here, so the identity is read degree by degree against a fixed cycle: for every n, every alpha in CycleGroup C p n and every p >= 0, P\_p(E) cap alpha = P\_p(E\_1) cap alpha + P\_p(E\_2) cap alpha in A\_\{n-p}(X), each product of Chern classes being a COMPOSITE of operations on Chow groups, as Stacks 0FA6 reads c\_1(F)^2. The module documentation gives both reasons. The division by p! is omitted only because it is a scalar. CARRIED: the three filtrations with invertible quotients L\_i, N\_j, M\_k, Stacks 02TI for each quotient (hfacL, hfacN, hfacM), and hsub, hquot identifying the M\_k with the L\_i followed by the N\_j -- the source's reduction of the short exact sequence, which it gets from Stacks 02UL and the injectivity of pi^* and which cannot be performed here. The Stacks 02UJ data needed to read the operator as P\_p of the Chern classes of the module itself is carried not here but by Stacks.Chow.powerSumCap\_one\_eq\_chernClassCapExt and Stacks.Chow.chernClassCapExt\_one\_append. PROVED HERE: the formal computation the source omits, in every degree and for every pair of ranks, as Stacks.Chow.powerSumRec\_append; no commutativity is used, so Stacks 02TJ is not carried”.

> **Stacks 0F9C, componentwise on cap products.** Let `0 → ℰ₁ → ℰ → ℰ₂ → 0` be a short exact
> sequence of finite locally free `𝒪_X`-modules, `ℰ₁` of rank `r` with a filtration whose
> successive quotients are the invertible modules `ℒ_i = L i`, `ℰ₂` of rank `s` with quotients
> `𝒩_j = N j`, and `ℰ` of rank `r + s` with the filtration obtained by juxtaposing them, whose
> quotients `ℳ_k` are the `ℒ_i` followed by the `𝒩_j`. Then for every `n`-cycle `α` and every
> `p ≥ 0`
>
>   `P_p(ℰ) ∩ α = P_p(ℰ₁) ∩ α + P_p(ℰ₂) ∩ α`
>
> in `A_{n-p}(X)`, which is the identity `P_p(ℰ) = P_p(ℰ₁) + P_p(ℰ₂)` of the source read against
> `α`, and `ch(ℰ) = ch(ℰ₁) + ch(ℰ₂)` after dividing by `p!`. In degree one it is
> `c₁(ℰ) ∩ α = c₁(ℰ₁) ∩ α + c₁(ℰ₂) ∩ α`, which is
> `Stacks.Chow.chernClassCapExt_one_append`; in degree zero it is `r + s = r + s`.

```lean
theorem powerSumCap_append (hsub : ∀ i : Fin r, M (Fin.castAdd s i) ≅ L i)
    (hquot : ∀ j : Fin s, M (Fin.natAdd r j) ≅ N j) (k : ℕ) (α : chowGroup C p n) :
    powerSumCap C p n M hfacM k α
      = powerSumCap C p n L hfacL k α + powerSumCap C p n N hfacN k α
```

**`Stacks.Chow.chernClassCapExt_one_append`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/PowerSumCapProducts.lean, line 368](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/PowerSumCapProducts.lean#L368). The attribute's comment: “the degree-one case, entirely in Chern class cap products, and conditional. P\_1 being c\_1 (AlgebraicGeometry.coe\_powerSumPolynomial\_one), the identity P\_p(E) = P\_p(E\_1) + P\_p(E\_2) reads c\_1(E) cap alpha = c\_1(E\_1) cap alpha + c\_1(E\_2) cap alpha in A\_\{n-1}(X), for every n and every alpha in CycleGroup C p n, where E\_1, E, E\_2 are the tops of the three filtrations and the three terms are the cap products of Stacks 02U5 on those modules themselves. Read degree by degree for the reason given on Stacks.Chow.powerSumCap\_append, of which this is the degree-one case and whose reduction it carries: the three filtrations as the towers Stacks 02UJ consumes, with hsub and hquot. ALSO CARRIED, each an input of Stacks 02UJ itself: chernE, chern1, chern2, the Stacks 02U0 component data; hnormE, hnorm1, hnorm2, the Stacks 02U0 normalisation c\_0 = 1 along each tower; hbinomE, hbinom1, hbinom2, the equality of binomial transforms that Stacks 02UD gives once Stacks 02UG is applied; and hfacL, hfacN, hfacM, Stacks 02TI for c\_1 of each quotient. Stacks 02TJ is NOT carried: the degree-one computation needs no commutativity”.

> **Stacks 0F9C in degree one, entirely in Chern class cap products.** In the situation of
> `Stacks.Chow.powerSumCap_append`, with `ℰ₁ = Q₁ r`, `ℰ₂ = Q₂ s` and `ℰ = Q (r + s)` the tops of
> the three filtrations, for every `n`-cycle `α`
>
>   `c₁(ℰ) ∩ α = c₁(ℰ₁) ∩ α + c₁(ℰ₂) ∩ α`
>
> in `A_{n-1}(X)`. This is the degree-one case of Stacks 0F9C, `P_1` being `c_1`, with no
> power-sum operator left in the statement: the three terms are the Chern class cap products of
> Stacks 02U5 on the three modules themselves.
>
> Each of the three sides is rewritten into its power-sum form by
> `Stacks.Chow.powerSumCap_one_eq_chernClassCapExt`, which is Stacks 02UJ in degree one, and the
> identity is then `Stacks.Chow.powerSumCap_append` in degree one.

```lean
theorem chernClassCapExt_one_append (hsub : ∀ i : Fin r, M (Fin.castAdd s i) ≅ L i)
    (hquot : ∀ j : Fin s, M (Fin.natAdd r j) ≅ N j)
    (QE : ℕ → X.Modules) (subE : ∀ k : Fin (r + s), M k ⟶ QE ((k : ℕ) + 1))
    (projE : ∀ k : Fin (r + s), QE ((k : ℕ) + 1) ⟶ QE (k : ℕ))
    (hzeroE : ∀ k : Fin (r + s), subE k ≫ projE k = 0)
    (hexactE : ∀ k : Fin (r + s), (ShortComplex.mk (subE k) (projE k) (hzeroE k)).ShortExact)
    (hrankE : ∀ m : ℕ, m ≤ r + s → PullbackPreservesRank (QE m) m)
    (chernE : ∀ m : ℕ, ChernClassCycleRule C m)
    (Q₁ : ℕ → X.Modules) (sub₁ : ∀ i : Fin r, L i ⟶ Q₁ ((i : ℕ) + 1))
    (proj₁ : ∀ i : Fin r, Q₁ ((i : ℕ) + 1) ⟶ Q₁ (i : ℕ))
    (hzero₁ : ∀ i : Fin r, sub₁ i ≫ proj₁ i = 0)
    (hexact₁ : ∀ i : Fin r, (ShortComplex.mk (sub₁ i) (proj₁ i) (hzero₁ i)).ShortExact)
    (hrank₁ : ∀ m : ℕ, m ≤ r → PullbackPreservesRank (Q₁ m) m)
    (chern₁ : ∀ m : ℕ, ChernClassCycleRule C m)
    (Q₂ : ℕ → X.Modules) (sub₂ : ∀ j : Fin s, N j ⟶ Q₂ ((j : ℕ) + 1))
    (proj₂ : ∀ j : Fin s, Q₂ ((j : ℕ) + 1) ⟶ Q₂ (j : ℕ))
    (hzero₂ : ∀ j : Fin s, sub₂ j ≫ proj₂ j = 0)
    (hexact₂ : ∀ j : Fin s, (ShortComplex.mk (sub₂ j) (proj₂ j) (hzero₂ j)).ShortExact)
    (hrank₂ : ∀ m : ℕ, m ≤ s → PullbackPreservesRank (Q₂ m) m)
    (chern₂ : ∀ m : ℕ, ChernClassCycleRule C m) (α : CycleGroup C p n)
    (hnormE : ∀ (m : ℕ) (hm : m ≤ r + s),
      chernClassCapExt C p n (QE m) m (hrankE m hm) (chernE m) 0 α =
        cycleClassDegreeZero C p n α)
    (hbinomE : ∀ k : Fin (r + s), ∀ i ≤ (k : ℕ) + 1,
      binomialTransform (inverseFirstChernCapStep C p n (M k) (hfacM k)) ((k : ℕ) + 1)
          (chernCapFamily C p n (QE ((k : ℕ) + 1)) ((k : ℕ) + 1) (hrankE ((k : ℕ) + 1) k.isLt)
            (chernE ((k : ℕ) + 1)) α) i =
        binomialTransform (inverseFirstChernCapStep C p n (M k) (hfacM k)) (k : ℕ)
          (chernCapFamily C p n (QE (k : ℕ)) (k : ℕ) (hrankE (k : ℕ) k.isLt.le)
            (chernE (k : ℕ)) α) i)
    (hnorm₁ : ∀ (m : ℕ) (hm : m ≤ r),
      chernClassCapExt C p n (Q₁ m) m (hrank₁ m hm) (chern₁ m) 0 α =
        cycleClassDegreeZero C p n α)
    (hbinom₁ : ∀ i : Fin r, ∀ t ≤ (i : ℕ) + 1,
      binomialTransform (inverseFirstChernCapStep C p n (L i) (hfacL i)) ((i : ℕ) + 1)
          (chernCapFamily C p n (Q₁ ((i : ℕ) + 1)) ((i : ℕ) + 1) (hrank₁ ((i : ℕ) + 1) i.isLt)
            (chern₁ ((i : ℕ) + 1)) α) t =
        binomialTransform (inverseFirstChernCapStep C p n (L i) (hfacL i)) (i : ℕ)
          (chernCapFamily C p n (Q₁ (i : ℕ)) (i : ℕ) (hrank₁ (i : ℕ) i.isLt.le)
            (chern₁ (i : ℕ)) α) t)
    (hnorm₂ : ∀ (m : ℕ) (hm : m ≤ s),
      chernClassCapExt C p n (Q₂ m) m (hrank₂ m hm) (chern₂ m) 0 α =
        cycleClassDegreeZero C p n α)
    (hbinom₂ : ∀ j : Fin s, ∀ t ≤ (j : ℕ) + 1,
      binomialTransform (inverseFirstChernCapStep C p n (N j) (hfacN j)) ((j : ℕ) + 1)
          (chernCapFamily C p n (Q₂ ((j : ℕ) + 1)) ((j : ℕ) + 1) (hrank₂ ((j : ℕ) + 1) j.isLt)
            (chern₂ ((j : ℕ) + 1)) α) t =
        binomialTransform (inverseFirstChernCapStep C p n (N j) (hfacN j)) (j : ℕ)
          (chernCapFamily C p n (Q₂ (j : ℕ)) (j : ℕ) (hrank₂ (j : ℕ) j.isLt.le)
            (chern₂ (j : ℕ)) α) t) :
    chernClassCapExt C p n (QE (r + s)) (r + s) (hrankE (r + s) le_rfl) (chernE (r + s)) 1 α
      = chernClassCapExt C p n (Q₁ r) r (hrank₁ r le_rfl) (chern₁ r) 1 α
        + chernClassCapExt C p n (Q₂ s) s (hrank₂ s le_rfl) (chern₂ s) 1 α
```

## Tag 0F9D, a lemma

[Tag 0F9D](https://stacks.math.columbia.edu/tag/0F9D) in the Stacks Project.

**`Stacks.Chow.totalChernCharacterArbitraryRank_tensorObj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/BivariantChernCharacter.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/BivariantChernCharacter.lean#L186). The attribute's comment: “the headline equality ch(E\_1 tensor E\_2) = ch(E\_1) ch(E\_2), with hypotheses EXACTLY the source's: Situation 02QL as the ChowSituation C, X locally of finite type over its base, and E\_1, E\_2 finite locally free O\_X-modules -- NO rank is assumed, the predicate being AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree and not ...OfRank. The equality IS read in A^*(X) tensor Q: Stacks.Chow.rationalTotalChowClass is the ring Stacks.Chow.TotalChowClass of total Chow cohomology classes -- the product over q >= 0 of the groups A^q(X) of Stacks 0B7E, whose multiplication is the Cauchy product of the compositions of bivariant classes of Stacks 0B75 -- tensored over Z with Q so that p! is invertible, so each product ch\_\{p\_1}(E\_1) ch\_\{p\_2}(E\_2) is a composition of bivariant classes with rational coefficients. ch\_p(F) = P\_p(F)/p! is Stacks.Chow.chernCharacterComponentArbitraryRank and ch(F) itself is Stacks.Chow.totalChernCharacterArbitraryRank, the formal power series whose degree-p coefficient is ch\_p(F): PowerSeries A is the product over p of copies of A under convolution, which is the home Stacks 0ESX gives the Chern character, the rank of F being unbounded, so an equality of these series is an equality of Chern characters in every degree at once and Stacks.Chow.chernCharacterComponentArbitraryRank\_tensorObj is that reading. It is derived from the source's more precise equality, Stacks.Chow.modulePowerSumArbitraryRank\_tensorObj, by dividing by p!: the binomial coefficient disappears because C(p, p\_1)/p! = 1/(p\_1! p\_2!) when p\_1 + p\_2 = p, which is Nat.add\_choose\_mul\_factorial\_mul\_factorial. The rank decomposition and the splitting principle are PERFORMED by the cited theorem, not supposed; see its note”.

> **Stacks 0F9D, the headline identity.** Let `(S, δ)` be the situation of Stacks 02QL, let `X`
> be locally of finite type over `S` and let `ℰ₁` and `ℰ₂` be finite locally free `𝒪_X`-modules, of
> no assumed rank. Then
>
>   `ch(ℰ₁ ⊗_{𝒪_X} ℰ₂) = ch(ℰ₁) ch(ℰ₂)`.
>
> Both sides are power series over the rational bivariant ring `A^*(X) ⊗ 𝐐` whose degree-`p`
> coefficient is `ch_p = P_p/p!`; multiplying two such series convolves their coefficients, so this
> single identity is `Stacks.Chow.chernCharacterComponentArbitraryRank_tensorObj` in every degree at
> once, and that in turn is `Stacks.Chow.modulePowerSumArbitraryRank_tensorObj` divided by `p!`.

```lean
theorem totalChernCharacterArbitraryRank_tensorObj :
    totalChernCharacterArbitraryRank C sX (Scheme.Modules.tensorObj E₁ E₂)
      = totalChernCharacterArbitraryRank C sX E₁ * totalChernCharacterArbitraryRank C sX E₂
```

**`Stacks.Chow.modulePowerSumArbitraryRank_tensorObj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/BivariantTensorPowerSum.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/BivariantTensorPowerSum.lean#L228). The attribute's comment: “the source's more precise identity P\_p(E\_1 tensor E\_2) = sum over p\_1 + p\_2 = p of binom(p, p\_1) P\_\{p\_1}(E\_1) P\_\{p\_2}(E\_2), with hypotheses EXACTLY the source's: Situation 02QL as the ChowSituation C, X locally of finite type over its base, and E\_1, E\_2 finite locally free O\_X-modules -- NO rank is assumed, the predicate being AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree and not ...OfRank. The identity is read IN THE BIVARIANT RING: Stacks.Chow.TotalChowClass is the product over q >= 0 of the Chow cohomology groups A^q(X) of Stacks 0B7E, whose multiplication is the Cauchy product of the composites of bivariant classes of Stacks 0B75 and whose unit is the identity class of Stacks 0FBS, so each product P\_\{p\_1}(E\_1) P\_\{p\_2}(E\_2) is a composition of bivariant classes and not a composite of cap operators; Stacks.Chow.modulePowerSumComponentArbitraryRank\_tensorObj reads the same identity in the single group A^p(X). P\_p(F) is Stacks.Chow.modulePowerSumArbitraryRank, Newton's recursion of Stacks 0F9B (AlgebraicGeometry.newtonPowerSum, which is the universal power-sum polynomial of that tag by AlgebraicGeometry.newtonPowerSum\_eq\_powerSumOfChernClasses) applied to the bivariant Chern classes c\_i(F) of Stacks 0B7H, Stacks.Chow.GenuineChern.chernClass, assembled over the rank loci of F by Stacks 0FDZ. THE RANK DECOMPOSITION IS PERFORMED, not assumed: the rank of a finite locally free module is locally constant (Stacks.Chow.moduleRank), its loci are open and closed and cover X (Stacks.Chow.isClopenDecomposition\_rankLociFamily), the identity for two modules is read on the common refinement of their two decompositions (Stacks.Chow.eq\_of\_res\_eq\_of\_constantModuleRanks), on a member of which E\_1 tensor E\_2 has constant rank r * s by Stacks 02U9, and restriction of total classes is a ring homomorphism. The constant-rank case is Stacks.Chow.modulePowerSum\_tensorObj, obtained from Stacks.Chow.powerSumChernElem\_tensorObj -- where the splitting principle of Stacks 02UL is performed -- read on EVERY test scheme g : T -> X for the pullbacks g^*E\_1, g^*E\_2 at once, which is what Stacks 0B76 needs for a bivariant class. The division by p! is omitted only because it is a scalar; Stacks.Chow.totalChernCharacterArbitraryRank\_tensorObj performs it”.

> **Stacks 0F9D, the source's more precise identity, in the bivariant ring.** Let `(S, δ)` be
> the situation of Stacks 02QL, let `X` be locally of finite type over `S` and let `ℰ₁` and `ℰ₂` be
> finite locally free `𝒪_X`-modules, of no assumed rank. Then for every `p ≥ 0`
>
>   `P_p(ℰ₁ ⊗_{𝒪_X} ℰ₂) = ∑_{p₁ + p₂ = p} C(p, p₁) P_{p₁}(ℰ₁) P_{p₂}(ℰ₂)`
>
> in `∏_{q ≥ 0} A^q(X)`, the bivariant ring of `X`, whose multiplication is the composition of
> bivariant classes of Stacks 0B75. In degree zero the identity reads `rk(ℰ₁ ⊗ ℰ₂) = rk(ℰ₁) rk(ℰ₂)`
> and in degree one `c₁(ℰ₁ ⊗ ℰ₂) = rk(ℰ₂) c₁(ℰ₁) + rk(ℰ₁) c₁(ℰ₂)`, both as locally constant
> functions on `X`.

```lean
theorem modulePowerSumArbitraryRank_tensorObj (p : ℕ) :
    modulePowerSumArbitraryRank C sX (Scheme.Modules.tensorObj E₁ E₂) p
      = ∑ q ∈ Finset.HasAntidiagonal.antidiagonal p,
          (p.choose q.1 : TotalChowClass C sX) *
            (modulePowerSumArbitraryRank C sX E₁ q.1 *
              modulePowerSumArbitraryRank C sX E₂ q.2)
```

**`Stacks.Chow.modulePowerSumComponentArbitraryRank_tensorObj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/BivariantTensorPowerSum.lean, line 278](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/BivariantTensorPowerSum.lean#L278). The attribute's comment: “the same identity P\_p(E\_1 tensor E\_2) = sum over p\_1 + p\_2 = p of binom(p, p\_1) P\_\{p\_1}(E\_1) P\_\{p\_2}(E\_2) read as an equality of two elements of the SINGLE GROUP A^p(X) = Stacks.Chow.chowCohomologyComponent of Stacks 0B7E at the Gysin system Stacks.Chow.gysinSystemOfInvertible of the genuine first Chern class, which is where the source states it. Hypotheses EXACTLY the source's: Situation 02QL as C, X locally of finite type over its base, E\_1 and E\_2 finite locally free with NO rank assumed. Each product on the right is formed in the bivariant ring Stacks.Chow.TotalChowClass, i.e. is a Cauchy product of the compositions of bivariant classes of Stacks 0B75, read in degree p, so the right-hand side is a sum over the antidiagonal of p of elements of A^p(X), which is the shape the source displays; the degree-p component of Stacks.Chow.modulePowerSumArbitraryRank is Stacks.Chow.modulePowerSumComponentArbitraryRank by definition. See Stacks.Chow.modulePowerSumArbitraryRank\_tensorObj for the same identity in every degree at once and for how the rank decomposition and the splitting principle are performed”.

> **Stacks 0F9D, the source's more precise identity, read in `A^p(X)`.** An equality of two
> elements of the Chow cohomology group `A^p(X)` of Stacks 0B7E: the class `P_p(ℰ₁ ⊗ ℰ₂)` is the
> sum over `p₁ + p₂ = p` of the classes `C(p, p₁) P_{p₁}(ℰ₁) P_{p₂}(ℰ₂)` of `A^p(X)`, each formed
> by the composition of bivariant classes of Stacks 0B75 inside the bivariant ring and read in
> degree `p`. This is `Stacks.Chow.modulePowerSumArbitraryRank_tensorObj` in degree `p`, the
> components of a finite sum of total classes being the sum of their components.

```lean
theorem modulePowerSumComponentArbitraryRank_tensorObj (p : ℕ) :
    modulePowerSumComponentArbitraryRank C sX (Scheme.Modules.tensorObj E₁ E₂) p
      = ∑ q ∈ Finset.HasAntidiagonal.antidiagonal p,
          ((p.choose q.1 : TotalChowClass C sX) *
            (modulePowerSumArbitraryRank C sX E₁ q.1 *
              modulePowerSumArbitraryRank C sX E₂ q.2)) p
```

**`Stacks.Chow.powerSumOfFiniteLocallyFree_sheafTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PowerSumTensor.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/PowerSumTensor.lean#L68). The attribute's comment: “the lemma as stated, for finite locally free E\_1, E\_2 of arbitrary ranks and every p >= 0, with no further hypothesis: P\_p(E\_1 tensor E\_2) = sum over p\_1 + p\_2 = p of C(p, p\_1) P\_\{p\_1}(E\_1) P\_\{p\_2}(E\_2), in the ring TotalChowClass C sX of total Chow cohomology classes (whose degree-p component is A^p(X)); P\_p is the power sum of Stacks 0F9B assembled over the rank loci, powerSumOfFiniteLocallyFree. The form ch(E\_1 tensor E\_2) = ch(E\_1) ch(E\_2) is Stacks.Chow.chernCharacterOfModule\_sheafTensor”.

> **Stacks 0F9D.** For finite locally free `𝒪_X`-modules `ℰ` and `ℱ`, of arbitrary ranks,
>
>   `P_p(ℰ ⊗ ℱ) = ∑_{p₁ + p₂ = p} C(p, p₁) · P_{p₁}(ℰ) · P_{p₂}(ℱ)`
>
> in the ring of total Chow cohomology classes of `X`, for every `p ≥ 0`. Along a morphism over
> which both modules have constant rank this is `Stacks.Chow.powerSumTotal_sheafTensor`, and such
> morphisms detect total classes (`Stacks.Chow.TotalChowClass.eq_of_res_eq_of_constantRank₂`).

```lean
theorem powerSumOfFiniteLocallyFree_sheafTensor (p : ℕ) :
    haveI : AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u}
        (R := X.ringCatSheaf) _ :=
        isFiniteLocallyFree_tensor hE hF
    powerSumOfFiniteLocallyFree C sX (((sheafTensor X.sheaf).obj E).obj F) p =
      ∑ q ∈ antidiagonal p, (p.choose q.1 : ℤ) •
        (powerSumOfFiniteLocallyFree C sX E q.1 * powerSumOfFiniteLocallyFree C sX F q.2)
```

**`Stacks.Chow.rationalTotalChernCharacter_sheafTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalIntersection/ChernCharacterMultiplicative.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalIntersection/ChernCharacterMultiplicative.lean#L138). The attribute's comment: “the Chern character form ch(E\_1 tensor E\_2) = ch(E\_1) ch(E\_2), for finite locally free E\_1, E\_2 of arbitrary ranks, with no further hypothesis, in the ring Stacks.Chow.RationalTotalChowClass C sX = prod over p >= 0 of A^p(X) tensor Q with its Cauchy product; ch(E) is the family of the ch\_p(E) = P\_p(E)/p!”.

> **Stacks 0F9D for the Chern character**: `ch(ℰ ⊗ ℱ) = ch(ℰ) · ch(ℱ)` in
> `∏_{p ≥ 0} A^p(X) ⊗ 𝐐`, for finite locally free modules of arbitrary ranks.
>
> In degree `m` both sides are computed on the lifts `∑_{p ≤ m} P_p/p!` of the two Chern characters
> to `𝐐 ⊗ ∏_q A^q(X)` (`Stacks.Chow.RationalTotalChowClass.mul_apply_eq`); `P_p(ℰ) P_q(ℱ)` is
> homogeneous of degree `p + q`, and the identity is
> `Stacks.Chow.powerSumOfFiniteLocallyFree_sheafTensor` divided by `m!`.

```lean
theorem rationalTotalChernCharacter_sheafTensor :
    haveI : AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u}
        (R := X.ringCatSheaf) _ :=
        isFiniteLocallyFree_tensor hE hF
    rationalTotalChernCharacter C sX (((sheafTensor X.sheaf).obj E).obj F) =
      rationalTotalChernCharacter C sX E * rationalTotalChernCharacter C sX F
```

**`Stacks.Chow.powerSumCap_lexFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/PowerSumCapProducts.lean, line 493](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/PowerSumCapProducts.lean#L493). The attribute's comment: “componentwise on cap products, and conditional. CORRECTION OF FORM: the source states P\_p(E\_1 tensor E\_2) = sum over p\_1 + p\_2 = p of C(p, p\_1) P\_\{p\_1}(E\_1) P\_\{p\_2}(E\_2) in A^p(X), and ch(E\_1 tensor E\_2) = ch(E\_1) ch(E\_2) after dividing by p!. There is no bivariant ring here, so the identity is read degree by degree against a fixed cycle, in A\_\{n-p}(X) for every n, every alpha in CycleGroup C p n and every p >= 0; every product of classes -- P\_\{p\_1}(E\_1) P\_\{p\_2}(E\_2) and the products inside each P\_p -- is a COMPOSITE of operations on Chow groups, as Stacks 0FA6 reads c\_1(F)^2. The module documentation gives both reasons. The division by p! is omitted only because it is a scalar. CARRIED: the three filtrations with invertible quotients, Stacks 02TI for each quotient (hfacL, hfacN, hfacM), and hquot, the source's lexicographic identification M\_\{i*s+j} iso L\_i tensor N\_j, which the source gets from Stacks 02UL and the injectivity of pi^* and which cannot be performed here; and Stacks 02TJ as hcommLN, genuinely needed because the binomial theorem applies to x\_i + y\_j only when those commute -- the members of one family need NOT commute among themselves, so hcommLL and hcommNN are not carried. Reading the operator as P\_p of the Chern classes of the module itself uses the Stacks 02UJ data, carried by Stacks.Chow.powerSumCap\_one\_eq\_chernClassCapExt. PROVED HERE: the formal computation the source omits, in every degree and for every pair of ranks, as Stacks.Chow.powerSumRec\_lexFamily”.

> **Stacks 0F9D, componentwise on cap products.** Let `ℰ₁` be finite locally free of rank `r`
> with a filtration whose successive quotients are the invertible modules `ℒ_i = L i`, let `ℰ₂` be
> finite locally free of rank `s` with quotients `𝒩_j = N j`, and let the filtration of
> `ℰ₁ ⊗_{𝒪_X} ℰ₂` be the lexicographic one of the source, of length `r·s`, whose `(i·s+j)`-th
> quotient is `ℒ_i ⊗ 𝒩_j`. Then for every `n`-cycle `α` and every `p ≥ 0`
>
>   `P_p(ℰ₁ ⊗ ℰ₂) ∩ α = ∑_{p₁ + p₂ = p} C(p, p₁) · (P_{p₁}(ℰ₁) ∘ P_{p₂}(ℰ₂)) ∩ α`
>
> in `A_{n-p}(X)`, which is the identity
> `P_p(ℰ₁ ⊗ ℰ₂) = ∑_{p₁+p₂=p} C(p,p₁) P_{p₁}(ℰ₁) P_{p₂}(ℰ₂)` of the source read against `α`, and
> `ch(ℰ₁ ⊗ ℰ₂) = ch(ℰ₁) · ch(ℰ₂)` after dividing by `p!`, the binomial coefficients being what
> `p! = p₁! · p₂! · C(p, p₁)` absorbs. Each product `P_{p₁}(ℰ₁) · P_{p₂}(ℰ₂)` is a composite of
> operations on Chow groups, as `c₁(ℱ)²` is in Stacks 0FA6. In degree one, `P_0` being the rank,
> the identity is `s·(c₁(ℰ₁) ∩ α) + r·(c₁(ℰ₂) ∩ α)`, the first displayed identity of
> Stacks 0FA6.

```lean
theorem powerSumCap_lexFamily
    (hquot : ∀ (i : Fin r) (j : Fin s),
      M (finLexIndex i j) ≅ Scheme.Modules.tensorObj (L i) (N j))
    (hcommLN : ∀ (a : Fin r) (b : Fin s),
      FirstChernCapStepsCommute C p n (L a) (N b) (hfacL a) (hfacN b))
    (k : ℕ) (α : chowGroup C p n) :
    powerSumCap C p n M hfacM k α
      = ∑ q ∈ Finset.antidiagonal k, k.choose q.1 •
          evalChowGraded C p n α k
            (powerSumShift C p n L hfacL q.1 * powerSumShift C p n N hfacN q.2)
```

## Tag 0FAB, a lemma

[Tag 0FAB](https://stacks.math.columbia.edu/tag/0FAB) in the Stacks Project.

**`Stacks.Chow.moduleChernCharacterComponent_dualSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/DualChernCharacter.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/DualChernCharacter.lean#L115). The attribute's comment: “ch\_i(E^dual) = (-1)^i ch\_i(E) in A^i(X) tensor Q for every i >= 0, X locally of finite type over the base of Situation 02QL and E a finite locally free O\_X-module of arbitrary (not necessarily constant) rank, E^dual = SheafHom(E, O\_X). ch\_i(E) = P\_i(E)/i! is Stacks.Chow.moduleChernCharacterComponent, built from the bivariant Chern classes of Tag 0B7H; the proof is Tag 0FA5 (Stacks.Chow.GenuineChern.chernClass\_dualSheaf) on each rank locus. Nothing is carried.”.

> **Stacks 0FAB.** Let `(S, δ)` be as in Situation 02QL, let `X` be locally of finite type over
> `S` and let `ℰ` be a finite locally free `𝒪_X`-module with dual `ℰ^∨`. Then
>
>   `ch_i(ℰ^∨) = (-1)^i ch_i(ℰ)`  in  `A^i(X) ⊗ 𝐐`
>
> for every `i ≥ 0`.

```lean
theorem moduleChernCharacterComponent_dualSheaf (i : ℕ) :
    haveI := Stacks.AlgebraicGeometry.ReflexiveModules.isFiniteLocallyFree_dualSheaf E hE
    moduleChernCharacterComponent C sX (dualSheaf E) i =
      ((-1 : ℤ) ^ i) • moduleChernCharacterComponent C sX E i
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.45, Tag 02UM](https://stacks.math.columbia.edu/tag/02UM)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
