---
catalog: module
lean: CompPoly.GuruswamiSudan.shiftedSubstitutionCoeffTerm_sum, CompPoly.GuruswamiSudan.composeY_shiftedSubstitutionCoeffFold, CompPoly.GuruswamiSudan.composeY_substituteYPolynomialPlusXPowerY
statement: formalized
proof: formalized
---

# Shifted Substitution Lemmas

`CompPoly.Bivariate.GuruswamiSudan.Root.ShiftedSubstitution.Lemmas`, in [CompPoly/Bivariate/GuruswamiSudan/Root/ShiftedSubstitution/Lemmas.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/ShiftedSubstitution/Lemmas.lean), by Valerii Huhnin.

> Semantic proof surface for the generic shifted substitution. The executable
> operation is available independently of these heavier algebraic facts.

`CompPoly.GuruswamiSudan.shiftedSubstitutionCoeffTerm_sum` (theorem, [line 26](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/ShiftedSubstitution/Lemmas.lean#L26))

> The univariate coefficient sum produced by one `Y`-coefficient in shifted
> substitution composes to the corresponding binomial expansion.

```lean
theorem shiftedSubstitutionCoeffTerm_sum {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (coeffY f g : CPolynomial F) (t y : Nat) :
    (List.range (y + 1)).foldl
        (fun acc r ↦ acc + shiftedSubstitutionCoeffTerm coeffY f t y r * g ^ r)
        0 =
      coeffY * (f + CPolynomial.X ^ t * g) ^ y
```

`CompPoly.GuruswamiSudan.composeY_shiftedSubstitutionCoeffFold` (theorem, [line 48](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/ShiftedSubstitution/Lemmas.lean#L48))

> Composing the bivariate contribution from one `Y`-coefficient gives the
> corresponding univariate shifted-substitution term.

```lean
theorem composeY_shiftedSubstitutionCoeffFold {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (coeffY f g : CPolynomial F) (t y : Nat) :
    CBivariate.composeY
        ((List.range (y + 1)).foldl
          (fun (out : CBivariate F) r ↦
            let contribution : CBivariate F := CPolynomial.monomial r
              (shiftedSubstitutionCoeffTerm coeffY f t y r)
            out + contribution)
          0)
        g =
      (List.range (y + 1)).foldl
        (fun acc r ↦ acc + shiftedSubstitutionCoeffTerm coeffY f t y r * g ^ r)
        0
```

`CompPoly.GuruswamiSudan.composeY_substituteYPolynomialPlusXPowerY` (theorem, [line 84](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/ShiftedSubstitution/Lemmas.lean#L84))

> Semantic correctness of the shifted substitution `Y = f(X) + X^t Y`.

```lean
theorem composeY_substituteYPolynomialPlusXPowerY {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (Q : CBivariate F) (f g : CPolynomial F) (t : Nat) :
    CBivariate.composeY (substituteYPolynomialPlusXPowerY Q f t) g =
      CBivariate.composeY Q (f + CPolynomial.X ^ t * g)
```

## Depends on

- [Shifted Substitution for Guruswami-Sudan Root Search](../shiftedsubstitution.md)

## Proof depends on

- [Common Guruswami-Sudan Root Helper Lemmas](../common-2/lemmas.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Root/ShiftedSubstitution/Lemmas.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/ShiftedSubstitution/Lemmas.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Root.ShiftedSubstitution.Lemmas.json)
