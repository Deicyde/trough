---
declaration: section
origin: cited
lean: Stacks.Chow.KeyFormulaSituation.firstChernClassCapOfInvertible_comm_weilDivisorCycleN, Stacks.Chow.firstChernClassCapOfInvertible_divisorOfMeromorphicSection_comm, Stacks.Chow.firstChernClassCapOfInvertible_divisorCycle_comm, Stacks.Chow.firstChernCapFactorsEverywhere, Stacks.Chow.firstChernClassCapChow, Stacks.Chow.firstChernClassCapOnChowOfInvertible_comm_unconditional
statement: formalized
proof: formalized
---

# 42.28 Intersecting with an invertible sheaf and rational equivalence

Section 42.28 of the Stacks Project, [Tag 02TG](https://stacks.math.columbia.edu/tag/02TG). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02TH, a lemma

[Tag 02TH](https://stacks.math.columbia.edu/tag/02TH) in the Stacks Project.

**`Stacks.Chow.KeyFormulaSituation.firstChernClassCapOfInvertible_comm_weilDivisorCycleN`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/KeyFormula/ChernCapComm.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/KeyFormula/ChernCapComm.lean#L69). The attribute's comment: “the identity for two invertible modules with nonzero meromorphic sections on an integral, locally Noetherian scheme of delta-dimension `k + 2`, with no hypothesis: the key formula of Stacks 0AYC is discharged by `Stacks.Chow.KeyFormulaSituation.keyFormula_toKeyFormulaData` and the two divisor cycles of Stacks 02SJ are the canonical ones of the two sections”.

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

**`Stacks.Chow.firstChernClassCapOfInvertible_divisorOfMeromorphicSection_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/KeyFormula/ChernCapCommutativity.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/KeyFormula/ChernCapCommutativity.lean#L92).

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

**`Stacks.Chow.firstChernClassCapOfInvertible_divisorCycle_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/KeyFormula/ChernCapDischarge.lean, line 497](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/KeyFormula/ChernCapDischarge.lean#L497).

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

**`Stacks.Chow.firstChernCapFactorsEverywhere`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/KeyFormula/ChernCapFactors.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/KeyFormula/ChernCapFactors.lean#L156). The attribute's comment: “the factoring itself, with no hypothesis: capping with the first Chern class of an invertible module kills every cycle rationally equivalent to zero, for every scheme locally of finite type over the base and every module”.

> **Stacks 02TI, with no hypothesis.** Intersecting with the first Chern class of an invertible
> module kills every `(k+1)`-cycle rationally equivalent to zero, whatever the scheme locally of
> finite type over the base and whatever the module.
>
> This is the reduction of `Stacks.Chow.firstChernCapFactorsEverywhere_iff_killsPrincipalDivisor`
> supplied with its integral case.

```lean
theorem firstChernCapFactorsEverywhere : FirstChernCapFactorsEverywhere C k
```

**`Stacks.Chow.firstChernClassCapChow`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/KeyFormula/ChernCapFactors.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/KeyFormula/ChernCapFactors.lean#L176). The attribute's comment: “the descended operation c\_1(L) cap - : A\_\{k+1}(X) ⟶ A\_k(X), agreeing with the cap product of 02SO on cycle representatives (firstChernClassCapChow\_mk)”.

> **Stacks 02TI.** Intersection with the first Chern class of an invertible module, as an
> operation `c₁(L) ∩ - : A_{k+1}(X) ⟶ A_k(X)` on Chow groups.

```lean
def firstChernClassCapChow : chowGroup C p (k + 1) →+ chowGroup C p k
```

## Tag 02TJ, a lemma

[Tag 02TJ](https://stacks.math.columbia.edu/tag/02TJ) in the Stacks Project.

**`Stacks.Chow.firstChernClassCapOnChowOfInvertible_comm_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/FirstChernCommOfInvertible.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/FirstChernCommOfInvertible.lean#L79). The attribute's comment: “the commutativity itself, with no hypotheses beyond the source's: it is `Stacks.Chow.firstChernClassCapOnChowOfInvertible_comm` with both of its inputs supplied by the theorems named below, and it is the one registration of this tag. The four descended cap products are `Stacks.Chow.firstChernClassCapOnChowOfInvertible`, and the Stacks 02TI input each of them needs — the reduced form `Stacks.Chow.FirstChernCapKillsPrincipalDivisor`, the vanishing of the cap product on one principal divisor on an integral scheme, to which `Stacks.Chow.firstChernCapFactorsEverywhere_iff_killsPrincipalDivisor` shows Stacks 02TI is equivalent — is supplied in both degrees by `Stacks.Chow.firstChernCapKillsPrincipalDivisor`, which proves it outright. Stacks 02TH for the restrictions of the two modules to the integral closed subschemes of `X` of delta-dimension `k + 2`, as an equality of classes in `A_k(W)`, which is what the source reduces to, is `Stacks.Chow.GenuineChern.firstChernCapCommutesOnIntegralComponents`, which proves it out of the key formula of Stacks 0AYC. The four cycle-level rules of Stacks 02SO and the four separate instances of Stacks 02TI that `Stacks.Chow.firstChernClassCapOnChow_comm` takes as inputs are all theorems here, and the passage from the integral subschemes to every class is proved too”.

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

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.28, Tag 02TG](https://stacks.math.columbia.edu/tag/02TG)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
