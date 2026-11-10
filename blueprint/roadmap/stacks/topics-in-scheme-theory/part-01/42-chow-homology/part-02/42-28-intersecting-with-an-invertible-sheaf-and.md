---
declaration: section
origin: cited
lean: Stacks.Chow.firstChernClassCap_comm_of_keyFormula, Stacks.Chow.KeyFormulaSituation.firstChernClassCapOfInvertible_comm_weilDivisorCycleN, Stacks.Chow.firstChernClassCapOfInvertible_divisorOfMeromorphicSection_comm, Stacks.Chow.firstChernClassCapOfInvertible_divisorCycle_comm, Stacks.Chow.firstChernCapFactorsEverywhere_iff_killsPrincipalDivisor, Stacks.Chow.firstChernClassCap_eq_zero_of_keyFormula, Stacks.Chow.firstChernClassCapOnChow, Stacks.Chow.firstChernCapFactorsEverywhere
statement: formalized
proof: formalized
---

# 42.28 Intersecting with an invertible sheaf and rational equivalence

Section 42.28 of the Stacks Project, [Tag 02TG](https://stacks.math.columbia.edu/tag/02TG). 3 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02TH, a lemma

[Tag 02TH](https://stacks.math.columbia.edu/tag/02TH) in the Stacks Project.

**`Stacks.Chow.firstChernClassCap_comm_of_keyFormula`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/IntersectionCommutativity.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/IntersectionCommutativity.lean#L144). The attribute's comment: “granting the key formula 0AYC and the divisor cycles of 02SJ”.

> **The commutativity of Stacks 02TH, granting the key formula.** On an integral scheme of
> delta-dimension `k + 2`, intersecting the divisor cycle of a nonzero meromorphic section of one
> invertible module with the first Chern class of the other gives the same class in `A_k(X)`, in
> either order.
>
> Granting the key formula of Stacks 0AYC for the data `D`, this is immediate: the two sides are
> represented by the two halves of its left hand side, so their difference is a locally finite sum
> of principal divisors on the prime divisors `Z_i`. The component rules of the two invertible
> modules, the key formula itself and the two divisor cycles with their presentations by the family
> `{Z_i}` are explicit parameters; see the implementation notes of
> `StacksFrontier.AlgebraicGeometry.Chow.IntersectionCommutativity`.
>
> The `@[stacks 02TH]` attribute sits on
> `Stacks.Chow.firstChernClassCapOfInvertible_divisorCycle_comm`, where every one of those
> parameters is discharged; this is the step its proof is made of.

```lean
theorem firstChernClassCap_comm_of_keyFormula (hKey : D.KeyFormula C p)
    (chernL chernN : FirstChernComponentCycleRule C p k)
    (hchernL : ∀ (i : D.Index) (hW : IsIntegral (D.component i).subscheme)
      (hDim : schemeDeltaDimension C ((D.component i).subschemeι ≫ p) = ((k + 1 : ℤ) : EInt)),
      (chernL (D.component i) hW hDim).1 = D.restrictedDivisorL i)
    (hchernN : ∀ (i : D.Index) (hW : IsIntegral (D.component i).subscheme)
      (hDim : schemeDeltaDimension C ((D.component i).subschemeι ≫ p) = ((k + 1 : ℤ) : EInt)),
      (chernN (D.component i) hW hDim).1 = D.restrictedDivisorN i)
    (divL divN : CycleGroup C p (k + 1))
    (hdivL : ∀ x : X, divL.1 x = ∑ᶠ i, D.orderL i *
      (cycleAssociatedToClosedSubscheme C p (D.component i).subschemeι (k + 1)).1 x)
    (hdivN : ∀ x : X, divN.1 x = ∑ᶠ i, D.orderN i *
      (cycleAssociatedToClosedSubscheme C p (D.component i).subschemeι (k + 1)).1 x) :
    firstChernClassCap C p k chernN divL = firstChernClassCap C p k chernL divN
```

**`Stacks.Chow.KeyFormulaSituation.firstChernClassCapOfInvertible_comm_weilDivisorCycleN`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/KeyFormula/ChernCapComm.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/KeyFormula/ChernCapComm.lean#L69). The attribute's comment: “the identity for two invertible modules with nonzero meromorphic sections on an integral, locally Noetherian scheme of delta-dimension `k + 2`, with no hypothesis: the key formula of Stacks 0AYC is discharged by `Stacks.Chow.KeyFormulaSituation.keyFormula_toKeyFormulaData` and the two divisor cycles of Stacks 02SJ are the canonical ones of the two sections”.

> **Stacks 02TH for the two canonical divisor cycles.** On an integral, locally Noetherian
> scheme of delta-dimension `k + 2`,
>
> `c₁(N) ∩ div_L(s) = c₁(L) ∩ div_N(t)`  in  `A_k(X)`,
>
> where `div_L(s)` and `div_N(t)` are the divisor cycles of the two sections of the situation. No
> parameter besides the situation remains: the two presentations by the family that
> `Stacks.Chow.KeyFormulaSituation.firstChernClassCapOfInvertible_comm` asks for are
> `Stacks.Chow.KeyFormulaSituation.weilDivisorAlgebraicCycle_weilDivisorN_apply`, read on `ℱ` for
> `div_N(t)` and on `ℱ.swap` for `div_L(s)`.

```lean
theorem firstChernClassCapOfInvertible_comm_weilDivisorCycleN
    (hn : schemeDeltaDimension C p = ((k + 2 : ℤ) : EInt)) :
    firstChernClassCapOfInvertible C p k N (ℱ.swap.weilDivisorCycleN C p hn) =
      firstChernClassCapOfInvertible C p k L (ℱ.weilDivisorCycleN C p hn)
```

**`Stacks.Chow.firstChernClassCapOfInvertible_divisorOfMeromorphicSection_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/KeyFormula/ChernCapCommutativity.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/KeyFormula/ChernCapCommutativity.lean#L92).

> **Stacks 02TH.** Let `X` be integral and locally of finite type over the base scheme `S` of
> chapter 42, with `dim_δ(X) = n`, let `L` and `N` be invertible `𝒪_X`-modules, and let `s` and `t`
> be nonzero (that is, regular) meromorphic sections of `L` and `N`. Writing `α = div_L(s)` and
> `β = div_N(t)` for their divisor cycles of Stacks 02SJ (1),
>
>   `c₁(N) ∩ α = c₁(L) ∩ β`  in  `CH_{n-2}(X)`.
>
> The cycles of degree `n - 1` are read in degree `(n - 2) + 1`, the source of the cap product
> `CH_{(n-2)+1} → CH_{n-2}`, by `Stacks.Chow.cycleGroupOfEq`. The proof is the key formula of
> Stacks 0AYC, through `Stacks.Chow.firstChernClassCapOfInvertible_divisorCycle_comm`.

```lean
theorem firstChernClassCapOfInvertible_divisorOfMeromorphicSection_comm (n : ℤ)
    (hn : schemeDeltaDimension C p = (n : EInt)) (L N : X.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L]
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property N]
    (s : AlgebraicGeometry.MeromorphicSection X.sheaf L)
    (hs : AlgebraicGeometry.IsRegularMeromorphicSection X.sheaf L s)
    (t : AlgebraicGeometry.MeromorphicSection X.sheaf N)
    (ht : AlgebraicGeometry.IsRegularMeromorphicSection X.sheaf N t) :
    firstChernClassCapOfInvertible C p (n - 2) N
        (cycleGroupOfEq (by ring) (divisorOfMeromorphicSectionCycle C p n hn L s hs)) =
      firstChernClassCapOfInvertible C p (n - 2) L
        (cycleGroupOfEq (by ring) (divisorOfMeromorphicSectionCycle C p n hn N t ht))
```

**`Stacks.Chow.firstChernClassCapOfInvertible_divisorCycle_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/KeyFormula/ChernCapDischarge.lean, line 497](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/KeyFormula/ChernCapDischarge.lean#L497).

> **Stacks 02TH.** Let `X` be integral and locally of finite type over the base scheme `S` of
> chapter 42, of delta-dimension `k + 2`, let `L` and `N` be invertible modules on `X` and let `s`
> and `t` be nonzero meromorphic sections of `L` and `N`. Writing `α = div_L(s)` and
> `β = div_N(t)` for their divisor cycles of Stacks 02SJ (1),
>
>   `c₁(N) ∩ α = c₁(L) ∩ β`  in  `A_k(X)`.
>
> Nothing is assumed beyond the source's hypotheses: the family of prime divisors and the local
> generators of the situation of Stacks 0AYB are produced by
> `Stacks.Chow.keyFormulaSituationOf`, the key formula of Stacks 0AYC for it is
> `Stacks.Chow.KeyFormulaSituation.keyFormula_toKeyFormulaData`, the component rules of Stacks 02SO
> are the canonical ones of `Stacks.Chow.firstChernClassCapOfInvertible`, and the two divisor
> cycles are presented by the family because a prime divisor outside it carries no order of
> vanishing. The source states the conclusion in `CH_{n-2}(X)` for `dim_δ(X) = n`; here
> `n = k + 2`.

```lean
theorem firstChernClassCapOfInvertible_divisorCycle_comm
    (hn : schemeDeltaDimension C p = ((k + 2 : ℤ) : EInt)) (L N : X.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L]
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property N]
    {s : L.presheaf.stalk (genericPoint X)} (hs : s ≠ 0)
    {t : N.presheaf.stalk (genericPoint X)} (ht : t ≠ 0) :
    firstChernClassCapOfInvertible C p k N (divisorCycleOfInvertibleSection C p hn L s) =
      firstChernClassCapOfInvertible C p k L (divisorCycleOfInvertibleSection C p hn N t)
```

## Tag 02TI, a lemma

[Tag 02TI](https://stacks.math.columbia.edu/tag/02TI) in the Stacks Project.

**`Stacks.Chow.firstChernCapFactorsEverywhere_iff_killsPrincipalDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernCapRationalEquivalenceReduction.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernCapRationalEquivalenceReduction.lean#L230). The attribute's comment: “the vanishing reduced to one principal divisor on an integral scheme”.

> **Stacks 02TI, reduced to its integral case.** The cap product with the first Chern class of
> an invertible module factors through rational equivalence, for every scheme locally of finite type
> over the base and every invertible module on it, **exactly when** it kills the principal divisor of
> a nonzero rational function on an integral scheme of delta-dimension `k + 2`.
>
> The reverse implication is the reduction step of the source's proof of Stacks 02TI; the forward
> implication holds because `div_Z(f)` is rationally equivalent to zero on `Z` itself, which is
> Stacks 02RW. So the delivered content of this tag is the reduction, and what remains of the tag is
> its integral case — the source's appeal to Stacks 02TH.

```lean
theorem firstChernCapFactorsEverywhere_iff_killsPrincipalDivisor :
    FirstChernCapFactorsEverywhere C k ↔ FirstChernCapKillsPrincipalDivisor C k
```

**`Stacks.Chow.firstChernClassCap_eq_zero_of_keyFormula`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/IntersectionCommutativity.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/IntersectionCommutativity.lean#L192). The attribute's comment: “the integral case α = div_X(f), granting the key formula 0AYC”.

> **The integral case of Stacks 02TI.** On an integral scheme of delta-dimension `k + 2`,
> intersecting the principal divisor of a rational function with the first Chern class of an
> invertible module gives zero in `A_k(X)`.
>
> This is Stacks 02TH applied with the second invertible module the structure sheaf `𝒪_X` and its
> meromorphic section the rational function `f`: the chosen generators of `𝒪_X` at the generic
> points `ξ_i` are then units, so the restricted divisors `div_{𝒪_{Z_i}}(t_i|_{Z_i})` vanish, which
> is the hypothesis `hzeroN`, while the orders `ord_{B_i}(f)` presenting `div_𝒪(f) = div_X(f)` need
> not. The resulting class `c₁(𝒪_X) ∩ div_L(s)` vanishes by
> `Stacks.Chow.firstChernClassCap_trivialChernComponentCycleRule`, the second half of Stacks 02SP.
>
> The proof of Stacks 02TI reduces its general statement to this case by proper pushforward along
> `⨿ W_j ⟶ X`, which needs Stacks 02SU and through it the proper pushforward of Chow classes of
> Stacks 0GU8 and 02S2. That reduction is the one step not available here, which is why the
> general vanishing is a hypothesis in
> `StacksFrontier.AlgebraicGeometry.Chow.IntersectionCommutativity.ChernCapDescent`.

```lean
theorem firstChernClassCap_eq_zero_of_keyFormula (hKey : D.KeyFormula C p)
    (hzeroN : ∀ i : D.Index, D.restrictedDivisorN i = 0)
    (chernL : FirstChernComponentCycleRule C p k)
    (hchernL : ∀ (i : D.Index) (hW : IsIntegral (D.component i).subscheme)
      (hDim : schemeDeltaDimension C ((D.component i).subschemeι ≫ p) = ((k + 1 : ℤ) : EInt)),
      (chernL (D.component i) hW hDim).1 = D.restrictedDivisorL i)
    (divL divN : CycleGroup C p (k + 1))
    (hdivL : ∀ x : X, divL.1 x = ∑ᶠ i, D.orderL i *
      (cycleAssociatedToClosedSubscheme C p (D.component i).subschemeι (k + 1)).1 x)
    (hdivN : ∀ x : X, divN.1 x = ∑ᶠ i, D.orderN i *
      (cycleAssociatedToClosedSubscheme C p (D.component i).subschemeι (k + 1)).1 x) :
    firstChernClassCap C p k chernL divN = 0
```

**`Stacks.Chow.firstChernClassCapOnChow`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/IntersectionCommutativity/ChernCapDescent.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/IntersectionCommutativity/ChernCapDescent.lean#L112). The attribute's comment: “the descended operation, granting the vanishing and the rule of 02SO”.

> **Stacks 02TI.** Intersection with the first Chern class, descended to Chow groups,
> `c₁(L) ∩ - : A_{k+1}(X) ⟶ A_k(X)`.

```lean
def firstChernClassCapOnChow
    (h : FirstChernClassCapFactorsThroughRationalEquivalence C p k chern) :
    chowGroup C p (k + 1) →+ chowGroup C p k
```

**`Stacks.Chow.firstChernCapFactorsEverywhere`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/KeyFormula/ChernCapFactors.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/KeyFormula/ChernCapFactors.lean#L156). The attribute's comment: “the factoring itself, with no hypothesis: capping with the first Chern class of an invertible module kills every cycle rationally equivalent to zero, for every scheme locally of finite type over the base and every module”.

> **Stacks 02TI, with no hypothesis.** Intersecting with the first Chern class of an invertible
> module kills every `(k+1)`-cycle rationally equivalent to zero, whatever the scheme locally of
> finite type over the base and whatever the module.
>
> This is the reduction of `Stacks.Chow.firstChernCapFactorsEverywhere_iff_killsPrincipalDivisor`
> supplied with its integral case.

```lean
theorem firstChernCapFactorsEverywhere : FirstChernCapFactorsEverywhere C k
```

**`Stacks.Chow.firstChernClassCapChow`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/KeyFormula/ChernCapFactors.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/KeyFormula/ChernCapFactors.lean#L176). The attribute's comment: “the descended operation c_1(L) cap - : A_{k+1}(X) ⟶ A_k(X) the factoring produces, with no hypothesis”.

> **Stacks 02TI.** Intersection with the first Chern class of an invertible module, as an
> operation `c₁(L) ∩ - : A_{k+1}(X) ⟶ A_k(X)` on Chow groups.

```lean
def firstChernClassCapChow : chowGroup C p (k + 1) →+ chowGroup C p k
```

## Tag 02TJ, a lemma

[Tag 02TJ](https://stacks.math.columbia.edu/tag/02TJ) in the Stacks Project.

**`Stacks.Chow.firstChernClassCapOnChowOfInvertible_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernCapCommutativityInvertible.lean, line 408](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernCapCommutativityInvertible.lean#L408). The attribute's comment: “granted `hkills`, Stacks 02TI in the reduced form `Stacks.Chow.FirstChernCapKillsPrincipalDivisor` — the vanishing of the cap product on one principal divisor on an integral scheme, to which `Stacks.Chow.firstChernCapFactorsEverywhere_iff_killsPrincipalDivisor` shows Stacks 02TI is equivalent with no hypothesis — in each of the two degrees the composite uses; and `hcomm`, Stacks 02TH for the restrictions of the two modules to the integral closed subschemes of `X` of delta-dimension `k + 2`, as an equality of classes in `A_k(W)`, which is the case the source reduces to. Those are the only two inputs: the four component rules of Stacks 02SO and the four separate instances of Stacks 02TI carried by `Stacks.Chow.firstChernClassCapOnChow_comm` are all discharged here, and the passage from the integral components to every class is proved rather than assumed”.

> **Stacks 02TJ.** For two invertible modules `ℒ` and `𝒩` on a scheme `X` locally of finite type
> over the base, intersecting successively with the two first Chern classes is independent of the
> order: `c₁(ℒ) ∩ c₁(𝒩) ∩ α = c₁(𝒩) ∩ c₁(ℒ) ∩ α` in `A_k(X)` for `α ∈ A_{k+1+1}(X)`.
>
> The four descended operations are those of `Stacks.Chow.firstChernClassCapOnChowOfInvertible`, so
> Stacks 02TI enters only through its reduced input `hkills`, and Stacks 02TH only through the
> class-level hypothesis `hcomm`; see the implementation notes of
> `StacksFrontier.AlgebraicGeometry.Chow.ChernCapCommutativityInvertible`.

```lean
theorem firstChernClassCapOnChowOfInvertible_comm
    (hkills : ∀ j : ℤ, FirstChernCapKillsPrincipalDivisor C j)
    (hcomm : FirstChernCapCommutesOnIntegralComponents C p k L N)
    (α : chowGroup C p (k + 1 + 1)) :
    firstChernClassCapOnChowOfInvertible C k (hkills k) p L
        (firstChernClassCapOnChowOfInvertible C (k + 1) (hkills (k + 1)) p N α) =
      firstChernClassCapOnChowOfInvertible C k (hkills k) p N
        (firstChernClassCapOnChowOfInvertible C (k + 1) (hkills (k + 1)) p L α)
```

**`Stacks.Chow.firstChernClassCapOnChowOfInvertible_comm_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/FirstChernCommOfInvertible.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/FirstChernCommOfInvertible.lean#L77). The attribute's comment: “the commutativity itself, with no hypotheses beyond the source's. The four descended cap products are `Stacks.Chow.firstChernClassCapOnChowOfInvertible`, and the Stacks 02TI input each of them needs — the reduced form `Stacks.Chow.FirstChernCapKillsPrincipalDivisor`, the vanishing of the cap product on one principal divisor on an integral scheme, to which `Stacks.Chow.firstChernCapFactorsEverywhere_iff_killsPrincipalDivisor` shows Stacks 02TI is equivalent — is supplied in both degrees by `Stacks.Chow.firstChernCapKillsPrincipalDivisor`, which proves it outright. Stacks 02TH for the restrictions of the two modules to the integral closed subschemes of `X` of delta-dimension `k + 2`, as an equality of classes in `A_k(W)`, which is what the source reduces to, is `Stacks.Chow.GenuineChern.firstChernCapCommutesOnIntegralComponents`, which proves it out of the key formula of Stacks 0AYC. The four cycle-level rules of Stacks 02SO and the four separate instances of Stacks 02TI that `Stacks.Chow.firstChernClassCapOnChow_comm` takes as inputs are all theorems here, and the passage from the integral subschemes to every class is proved too”.

> **Stacks 02TJ.** For two invertible modules `ℒ` and `𝒩` on a scheme `X` locally of finite type
> over the base, intersecting successively with the two first Chern classes is independent of the
> order: `c₁(ℒ) ∩ c₁(𝒩) ∩ α = c₁(𝒩) ∩ c₁(ℒ) ∩ α` in `A_k(X)` for `α ∈ A_{k+1+1}(X)`.
>
> The four descended operations are those of `Stacks.Chow.firstChernClassCapOnChowOfInvertible`,
> whose Stacks 02TI input is supplied by `Stacks.Chow.firstChernCapKillsPrincipalDivisor` in each of
> the two degrees, and Stacks 02TH enters through
> `Stacks.Chow.GenuineChern.firstChernCapCommutesOnIntegralComponents`; see the implementation
> notes of `StacksFrontier.AlgebraicGeometry.Chow.ChernCapCommutativityInvertible`.

```lean
theorem firstChernClassCapOnChowOfInvertible_comm_unconditional
    (α : chowGroup C p (k + 1 + 1)) :
    firstChernClassCapOnChowOfInvertible C k (firstChernCapKillsPrincipalDivisor C k) p L
        (firstChernClassCapOnChowOfInvertible C (k + 1)
          (firstChernCapKillsPrincipalDivisor C (k + 1)) p N α) =
      firstChernClassCapOnChowOfInvertible C k (firstChernCapKillsPrincipalDivisor C k) p N
        (firstChernClassCapOnChowOfInvertible C (k + 1)
          (firstChernCapKillsPrincipalDivisor C (k + 1)) p L α)
```

**`Stacks.Chow.firstChernCapStepsCommute`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/TensorPowerSumsDischarge.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/SplittingPrinciple/TensorPowerSumsDischarge.lean#L245). The attribute's comment: “the identity for the degree-raising steps Stacks.Chow.firstChernCapStep that the Chern class power-sum operators of Stacks 0F9B are built from, with no hypothesis: it is Stacks.Chow.GenuineChern.firstChernClassCapChow_comm, which is the tag itself with nothing carried, transported along the equality of degrees n - i = (n - (i+1)) + 1 that separates the two presentations of c_1(L) cap -”.

> **Stacks 02TJ in the form the power-sum operators consume, with no hypothesis.** For two
> invertible modules the degree-raising operations `c₁(A) ∩ -` and `c₁(B) ∩ -` of
> `Stacks.Chow.firstChernCapStep` commute, in every degree.
>
> This is `Stacks.Chow.GenuineChern.firstChernClassCapChow_comm` — Stacks 02TJ with no
> hypothesis beyond the ones the tag states — transported to the presentation
> `A_{n-i}(X) ⟶ A_{n-(i+1)}(X)` of the same operation by
> `Stacks.Chow.firstChernCapStep_apply`. It discharges every `hcommLN`-style hypothesis of
> `StacksFrontier.AlgebraicGeometry.Chow.SplittingPrinciple.TensorChernClasses`.

```lean
theorem firstChernCapStepsCommute (hA : InvertibleChernCapDescends C p A)
    (hB : InvertibleChernCapDescends C p B) :
    FirstChernCapStepsCommute C p n A B hA hB
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.28, Tag 02TG](https://stacks.math.columbia.edu/tag/02TG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
